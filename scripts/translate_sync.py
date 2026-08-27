import time
import os
import re
import sys
import subprocess
from google import genai
from google.genai import types

CITATION_RE = re.compile(r"\[@([A-Za-z][A-Za-z0-9_-]*),\s*([^\]]+)\]")
ARABIC_RE = re.compile(r"[\u0600-\u06FF]")


def restore_locators(source_text, translated_text):
    """Rétablit les locateurs de citation dans leur forme d'origine.

    Le contenu qui suit la virgule dans `[@ref, art. 13]` est de la SYNTAXE de
    citation, pas de la prose : il doit rester tel quel. Le modèle le traduit
    malgré la consigne — « art. 5 à 7 » devient « art. 5 إلى 7 » —, et c'est
    une transformation assez mécanique pour être défaite ici plutôt que
    négociée à chaque passe.

    Prudence : on ne recopie que si les clés apparaissent dans le même ordre et
    en même nombre des deux côtés. Sinon on ne touche à rien, et le contrôle de
    parité signalera l'écart.
    """
    src = CITATION_RE.findall(source_text)
    dst = CITATION_RE.findall(translated_text)
    if len(src) != len(dst) or [k for k, _ in src] != [k for k, _ in dst]:
        return translated_text

    locators = iter(loc for _, loc in src)

    def swap(match):
        source_locator = next(locators)
        if ARABIC_RE.search(match.group(2)):
            return f"[@{match.group(1)}, {source_locator}]"
        return match.group(0)

    return CITATION_RE.sub(swap, translated_text)


def get_git_diff(base_sha, head_sha, file_path):
    try:
        cmd = ["git", "diff", base_sha, head_sha, "--", file_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return ""

def main():
    if len(sys.argv) < 4:
        print("Usage: python translate_sync.py <base_sha> <head_sha> <file1> <file2> ...")
        sys.exit(0)

    base_sha = sys.argv[1]
    head_sha = sys.argv[2]
    files_to_process = sys.argv[3:]
    
    try:
        client = genai.Client()
    except Exception as e:
        print(f"Erreur d'initialisation de l'API Gemini : {e}")
        sys.exit(1)
    
    guidelines_path = "translation_guidelines.md"
    try:
        with open(guidelines_path, "r", encoding="utf-8") as f:
            guidelines = f.read()
    except Exception:
        guidelines = "Tu es un traducteur professionnel juridique."

    # Glossaire terminologique canonique généré depuis precis/glossaire.yml.
    # Inclus tel quel (sans modifier le guide rédigé à la main) pour garantir
    # la bijection des termes FR↔AR.
    try:
        with open("translation_glossary.generated.md", "r", encoding="utf-8") as f:
            guidelines += "\n\n" + f.read()
    except Exception:
        pass

    fr_files = {f for f in files_to_process if "precis/fr/" in f}
    failures = []

    for file_path in files_to_process:
        if not file_path.endswith(".qmd") and not file_path.endswith("_quarto.yml") and file_path != "CHANGELOG.md":
            continue

        if not os.path.exists(file_path):
            continue

        if file_path == "CHANGELOG.md":
            source_lang = "Français/Anglais"
            target_lang = "Arabe"
            target_path = "CHANGELOG_ar.md"
        elif "precis/fr/" in file_path:
            source_lang = "Français"
            target_lang = "Arabe"
            target_path = file_path.replace("precis/fr/", "precis/ar/")
        elif "precis/ar/" in file_path:
            fr_counterpart = file_path.replace("precis/ar/", "precis/fr/")
            if fr_counterpart in fr_files:
                print(f"Skip : {file_path} (le fichier FR correspondant est aussi dans le diff, FR est la source de vérité)")
                continue
            source_lang = "Arabe"
            target_lang = "Français"
            target_path = file_path.replace("precis/ar/", "precis/fr/")
        else:
            continue
            
        print(f"Mise à jour : {file_path} -> {target_path}")
        
        with open(file_path, "r", encoding="utf-8") as f:
            new_source_text = f.read()
            
        old_target_text = ""
        if os.path.exists(target_path):
            with open(target_path, "r", encoding="utf-8") as f:
                old_target_text = f.read()
                
        diff_text = get_git_diff(base_sha, head_sha, file_path)
        
        # Dès qu'une traduction existe, on part d'elle — même sans diff.
        # Retraduire de zéro un fichier déjà traduit EFFACE les corrections faites
        # à la main sur la seule langue cible, qui sont légitimes et courantes
        # (l'arabe se corrige parfois seul, sans passer par le français). Le DIFF,
        # quand il est disponible, ne sert qu'à désigner ce qui a bougé ; son
        # absence — cas de la re-synchro manuelle — ne doit pas faire basculer en
        # traduction complète.
        if old_target_text:
            if diff_text:
                diff_section = f"""
Voici le DIFF (les modifications) qui viennent d'être faites sur le fichier source :
```diff
{diff_text}
```

TA TÂCHE :
Mets à jour l'ANCIENNE TRADUCTION pour qu'elle corresponde au FICHIER SOURCE MIS À JOUR.
RÈGLE D'OR ABSOLUE : Tu DOIS conserver exactement la même formulation que l'ANCIENNE TRADUCTION pour tous les paragraphes qui n'ont pas été modifiés. Ne modifie la traduction que pour les parties qui ont été ajoutées ou modifiées dans le DIFF.
"""
            else:
                diff_section = """
Aucun DIFF n'est disponible : compare toi-même le FICHIER SOURCE MIS À JOUR et l'ANCIENNE TRADUCTION.

TA TÂCHE :
Mets à jour l'ANCIENNE TRADUCTION pour qu'elle corresponde au FICHIER SOURCE MIS À JOUR.
RÈGLE D'OR ABSOLUE : Tu DOIS conserver exactement la même formulation que l'ANCIENNE TRADUCTION partout où le sens du fichier source n'a pas changé. L'ANCIENNE TRADUCTION peut contenir des corrections faites à la main : ne les défais pas, ne reformule pas ce qui est déjà correct. Ne touche qu'à ce qui ne correspond plus à la source.
"""
            prompt = f"""
Voici une tâche de mise à jour de traduction bilingue.

Langue source : {source_lang}
Langue cible : {target_lang}

Voici le FICHIER SOURCE MIS À JOUR ({source_lang}) :
```markdown
{new_source_text}
```

Voici l'ANCIENNE TRADUCTION CIBLE ({target_lang}) (avant tes modifications) :
```markdown
{old_target_text}
```
{diff_section}
Renvoie UNIQUEMENT le nouveau fichier cible mis à jour, sans aucun commentaire avant ou après.
"""
        else:
            prompt = f"""
Voici le fichier source en {source_lang} à traduire en {target_lang}.
S'il te plaît, traduis-le entièrement et renvoie UNIQUEMENT le code source traduit, sans aucun commentaire.
Préserve TOUTES les balises Markdown, les blocs de code et la structure exacte.

Fichier à traduire :
```markdown
{new_source_text}
```
"""



        try:
            # Retry avec backoff exponentiel sur erreurs transitoires.
            # Gemini renvoie régulièrement 503 UNAVAILABLE en pic de demande ;
            # sans retry, une seule occurrence faisait échouer toute la synchro.
            # Le 500 INTERNAL est tout aussi transitoire — le message de l'API
            # invite lui-même à réessayer — et il n'était pas rattrapé : le
            # 27/08/2026 il a fait échouer la traduction d'un chapitre entier.
            max_attempts = 5
            response = None
            for attempt in range(1, max_attempts + 1):
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=guidelines,
                            temperature=0.0,
                        ),
                    )
                    break
                except Exception as api_err:
                    msg = str(api_err)
                    transient = any(s in msg for s in (
                        "503", "UNAVAILABLE", "429", "RESOURCE_EXHAUSTED", "overloaded",
                        "500", "INTERNAL", "502", "504", "DEADLINE_EXCEEDED",
                    ))
                    if not transient or attempt == max_attempts:
                        raise
                    wait = min(60, 5 * (2 ** (attempt - 1)))  # 5,10,20,40,60s
                    print(f"  {file_path}: erreur transitoire ({msg[:60]}…), retry {attempt}/{max_attempts - 1} dans {wait}s")
                    time.sleep(wait)

            if response is None:
                raise RuntimeError("aucune réponse de l'API après retries")
            translated_text = response.text
            if translated_text.startswith("```markdown\n"):
                translated_text = translated_text[12:]
            if translated_text.endswith("\n```\n"):
                translated_text = translated_text[:-5]
            elif translated_text.endswith("\n```"):
                translated_text = translated_text[:-4]
                
            translated_text = restore_locators(new_source_text, translated_text)

            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(translated_text)
            print(f"Succès : {target_path} mis à jour.")
            time.sleep(5) # Éviter le Rate Limit (15 RPM)
            
        except Exception as e:
            print(f"Erreur lors de la traduction de {file_path}: {e}")
            failures.append(f"{file_path} : {e}")

    # Une synchro partielle ne doit JAMAIS passer pour complète. Jusqu'ici le
    # script signalait l'échec d'un fichier puis rendait la main en code 0 : le
    # workflow committait et ouvrait une PR d'apparence normale, à laquelle il
    # manquait un chapitre. C'est ainsi que l'arabe de `fiscalite` a perdu ses
    # citations sans que personne ne le voie. En échouant ici, on n'ouvre pas de
    # PR trompeuse ; il suffit de relancer la synchro.
    if failures:
        print(f"\n{len(failures)} fichier(s) NON traduit(s) :")
        for line in failures:
            print(f"  - {line}")
        print("\nSynchro incomplète : aucune PR ne doit être ouverte sur cet état. "
              "Relancer le workflow (workflow_dispatch) sur les fichiers concernés.")
        sys.exit(1)

if __name__ == "__main__":
    main()

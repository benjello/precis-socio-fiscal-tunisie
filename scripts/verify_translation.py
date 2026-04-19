import os
import sys
import subprocess
from google import genai
from google.genai import types

def get_git_diff(base_sha, head_sha, file_path):
    try:
        cmd = ["git", "diff", base_sha, head_sha, "--", file_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return ""

def main():
    base_sha = os.environ.get("BASE_SHA")
    head_sha = os.environ.get("HEAD_SHA")
    pr_number = os.environ.get("PR_NUMBER")
    
    if not all([base_sha, head_sha, pr_number]):
        print("Variables d'environnement manquantes (BASE_SHA, HEAD_SHA, PR_NUMBER).")
        sys.exit(0)

    try:
        cmd = ["git", "diff", "--name-only", base_sha, head_sha]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        changed_files = result.stdout.strip().split("\n")
    except subprocess.CalledProcessError:
        sys.exit(0)

    try:
        client = genai.Client()
    except Exception as e:
        print(f"Erreur d'initialisation de l'API Gemini : {e}")
        sys.exit(1)

    warnings = []

    for file_path in changed_files:
        if not file_path.endswith(".qmd") and not file_path.endswith("_quarto.yml"):
            continue
            
        # On vérifie symétriquement
        if "precis/ar/" in file_path:
            source_file = file_path.replace("precis/ar/", "precis/fr/")
            target_file = file_path
            source_lang = "Français"
            target_lang = "Arabe"
        elif "precis/fr/" in file_path:
            source_file = file_path.replace("precis/fr/", "precis/ar/")
            target_file = file_path
            source_lang = "Arabe"
            target_lang = "Français"
        else:
            continue

        source_diff = get_git_diff(base_sha, head_sha, source_file)
        target_diff = get_git_diff(base_sha, head_sha, target_file)
        
        if not target_diff or not source_diff:
            # S'il manque l'un des deux diffs, on passe
            continue

        prompt = f"""
Tu es un agent de contrôle qualité rigoureux (Checker AI) spécialisé dans la relecture de traduction bilingue (français/arabe) de documents juridiques, historiques et socio-économiques.

Ton objectif est d'inspecter les modifications pour t'assurer que le traducteur (ou l'IA traductrice) n'a fait **aucune erreur**, n'a **pas halluciné** de contenu, et a préservé toutes les références.

Voici le DIFF des modifications apportées au fichier source ({source_lang}) :
```diff
{source_diff}
```

Voici le DIFF des modifications apportées à la traduction cible ({target_lang}) :
```diff
{target_diff}
```

VÉRIFICATIONS À EFFECTUER IMPÉRATIVEMENT :
1. Les dates, données chiffrées, et citations bibliographiques `[@ref]` doivent être rigoureusement identiques entre la source et la cible.
2. La traduction cible ne doit modifier QUE les paragraphes qui ont été modifiés dans le fichier source. S'il y a des lignes modifiées dans la cible qui ne correspondent à aucune modification conceptuelle dans la source (un "débordement"), c'est une alerte grave.
3. Le sens historique et pédagogique doit être préservé.

Si tout te semble parfait, cohérent et sans anomalie, réponds UNIQUEMENT par le mot exact : "OK".
S'il y a la moindre anomalie (hallucination de chiffres, perte de balise Markdown, débordement, ou texte non traduit de manière évidente), rédige un rapport d'alerte en français expliquant le problème.
TRES IMPORTANT : Tu dois IMPÉRATIVEMENT inclure une suggestion de correction prête à l'emploi. Montre le texte original fautif, et en dessous, le texte corrigé que l'auteur devrait utiliser.
"""
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(temperature=0.0)
            )
            
            text = response.text.strip()
            # On tolère les minuscules ou petits espaces
            if text.upper() != "OK" and text.upper() != "OK.":
                warnings.append(f"**Fichier `{target_file}`** :\n{text}")
        except Exception as e:
            print(f"Erreur lors de la vérification de {target_file}: {e}")

    if warnings:
        comment_body = "⚠️ **Alerte de l'IA de Vérification (Checker AI)**\n\nJ'ai inspecté la traduction générée pour cette Pull Request et j'ai détecté des anomalies potentielles (débordement, modification de chiffres ou de balises) :\n\n" + "\n\n".join(warnings) + "\n\n_Veuillez vérifier manuellement ces lignes avant de valider._"
        print("Anomalies trouvées :")
        print(comment_body)
        
        try:
            subprocess.run(["gh", "pr", "comment", pr_number, "-b", comment_body], check=True)
        except Exception as e:
            print(f"Impossible de poster le commentaire sur la PR : {e}")
        sys.exit(1) # Échouer le job CI
    else:
        print("Toutes les traductions sont vérifiées et validées. Aucun avertissement.")

if __name__ == "__main__":
    main()

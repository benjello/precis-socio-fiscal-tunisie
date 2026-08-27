"""Contrôles déterministes de parité entre un fichier FR et son homologue AR.

Complément du `verify_translation.py` (Checker AI) : celui-ci juge le SENS, avec
la variabilité d'un modèle ; celui-ci vérifie la MÉCANIQUE, sans appel réseau et
sans faux négatif possible. Il attrape la classe d'erreurs la plus dangereuse en
traduction juridique — celle qui produit un texte parfaitement idiomatique mais
qui ne renvoie plus au bon texte de loi.

Motivation, tirée de deux régressions réelles observées en août 2026 :

  - une passe a converti « loi n°83-112 » en `القانون عدد 83 لسنة 1983`, prenant
    l'année pour le numéro d'ordre (112). Idem pour les lois 68-12, 67-29 et
    72-40. Le résultat est plausible, cohérent avec la date affichée, et
    indétectable à la lecture de l'arabe seul ;
  - un locateur de citation a été partiellement traduit (`art. 5 إلى 7`).

Usage :
    python scripts/check_translation_parity.py [chemins...]

Sans argument, contrôle toutes les paires FR/AR du dépôt. Les chemins donnés
peuvent être FR ou AR ; l'homologue est déduit. Sortie 1 si une divergence est
trouvée, 0 sinon. Aucune dépendance hors bibliothèque standard.

En CI, `translation-sync.yml` ne lui passe QUE les fichiers qu'il vient de
traduire : lancé sur tout le dépôt, il remonte aussi la dette préexistante
— notamment le fait que le corpus arabe mélange deux conventions de
numérotation selon les livres (« الأمر عدد 85-1025 » ici, « الأمر عدد 1025
لسنة 1985 » là) —, ce qui bloquerait toute PR pour des raisons étrangères à
son contenu. Le mode sans argument est fait pour l'audit, à lancer en local.
"""

import glob
import os
import re
import sys

# Les _glossaire.qmd sont générés depuis precis/glossaire.yml : les deux langues
# sont produites ensemble, ce ne sont pas des traductions.
EXCLUDED = ("_glossaire.qmd",)

ARABIC = re.compile(r"[؀-ۿ]")


def strip_noise(text):
    """Retire ce qui n'est pas de la prose traduite : commentaires HTML (les TODO
    restent en français côté AR, par convention) et blocs de code."""
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    return text


def counter(items):
    out = {}
    for it in items:
        out[it] = out.get(it, 0) + 1
    return out


def extract(text):
    """Renvoie les jeux de jetons qui DOIVENT être identiques dans les deux langues."""
    body = strip_noise(text)
    return {
        # Clés de bibliographie [@cle] et renvois internes @tbl-, @fig-, @sec-
        "clés de citation et renvois": counter(re.findall(r"@([A-Za-z][A-Za-z0-9_-]*)", body)),
        # Ancres explicites {#id}
        "ancres": counter(re.findall(r"\{#([A-Za-z0-9_-]+)\}", body)),
        # Cibles de liens internes : ](#ancre) et ](fichier.qmd#ancre)
        "cibles de liens": counter(re.findall(r"\]\(([^)\s]+)\)", body)),
        # Numéros de textes juridiques : 83-112, 97-1832, 2007-268...
        "numéros de textes": counter(re.findall(r"(?<![\d-])(\d{2,4}-\d{1,5})(?![\d-])", body)),
        # Étiquettes des cellules de code, hors strip (elles vivent dans les blocs)
        "labels de figures": counter(re.findall(r"^#\|\s*label:\s*(\S+)", text, flags=re.M)),
    }


def check_locators(text, path, problems):
    """Le contenu d'un locateur Pandoc — après la virgule dans [@ref, art. 13] —
    est de la syntaxe de citation, pas de la prose : il ne doit pas être traduit."""
    for locator in re.findall(r"\[@[A-Za-z][A-Za-z0-9_-]*,\s*([^\]]+)\]", text):
        if ARABIC.search(locator):
            problems.append(
                f"{path} : locateur de citation traduit — « {locator.strip()} ». "
                f"Le locateur reste en français (ex. « art. 5 à 7 »)."
            )


def compare(fr_path, ar_path):
    problems = []
    with open(fr_path, encoding="utf-8") as f:
        fr_text = f.read()
    with open(ar_path, encoding="utf-8") as f:
        ar_text = f.read()

    fr, ar = extract(fr_text), extract(ar_text)

    for kind in fr:
        for token in sorted(set(fr[kind]) | set(ar[kind])):
            n_fr, n_ar = fr[kind].get(token, 0), ar[kind].get(token, 0)
            if n_fr == n_ar:
                continue
            if n_ar == 0:
                problems.append(f"{ar_path} : {kind} — « {token} » absent de l'arabe ({n_fr}× en français).")
            elif n_fr == 0:
                problems.append(f"{ar_path} : {kind} — « {token} » présent en arabe ({n_ar}×) mais absent du français.")
            else:
                problems.append(f"{ar_path} : {kind} — « {token} » apparaît {n_fr}× en français et {n_ar}× en arabe.")

    check_locators(ar_text, ar_path, problems)
    return problems


def pairs_for(paths):
    """Normalise une liste de chemins (FR ou AR) en paires (fr, ar) existantes."""
    seen, out = set(), []
    for p in paths:
        if not p.endswith(".qmd") or os.path.basename(p) in EXCLUDED:
            continue
        fr = p.replace("precis/ar/", "precis/fr/")
        ar = p.replace("precis/fr/", "precis/ar/")
        if fr in seen or not (os.path.exists(fr) and os.path.exists(ar)):
            continue
        seen.add(fr)
        out.append((fr, ar))
    return out


def main():
    args = sys.argv[1:]
    paths = args if args else glob.glob("precis/fr/**/*.qmd", recursive=True)
    pairs = pairs_for(paths)

    if not pairs:
        print("Aucune paire FR/AR à contrôler.")
        return 0

    problems = []
    for fr_path, ar_path in sorted(pairs):
        problems.extend(compare(fr_path, ar_path))

    print(f"{len(pairs)} paire(s) FR/AR contrôlée(s).")
    if problems:
        print(f"\n{len(problems)} divergence(s) :\n")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("Parité mécanique vérifiée : citations, ancres, liens, numéros de textes, labels.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

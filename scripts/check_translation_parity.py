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

Sur les numéros de textes, l'arabe dispose de DEUX écritures également correctes :
la forme littérale reprise du français (`الأمر عدد 97-1832`) et la forme
développée (`الأمر عدد 1832 لسنة 1997`, « texte 1832 de l'année 1997 »). Le
corpus emploie les deux selon les livres. Le contrôle accepte donc les deux, et
ne signale que ce qui est réellement fautif : un numéro absent des deux formes,
ou une conversion qui prend l'ANNÉE pour le numéro d'ordre — l'erreur observée,
la seule qui soit indétectable à la lecture de l'arabe seul.

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
        # Les numéros de textes juridiques sont traités à part, par
        # `check_law_numbers` : l'arabe dispose de DEUX écritures légitimes.
        # Étiquettes des cellules de code, hors strip (elles vivent dans les blocs)
        "labels de figures": counter(re.findall(r"^#\|\s*label:\s*(\S+)", text, flags=re.M)),
    }


LAW_RE = re.compile(r"(?<![\d-])(\d{2,4})-(\d{1,5})(?![\d-])")


def law_year(prefix):
    """Année d'un numéro de texte tunisien, ou None si ce n'en est pas un.

    Un numéro s'écrit `AA-NNN` (année sur deux chiffres, à partir de 1956) ou
    `AAAA-NNN`. Tout le reste — plages d'indices « 225-800 », intervalles
    d'années « 2023-2025 », pages « 415-453 » — n'est pas un numéro de texte et
    doit être écarté, sous peine de bruit."""
    n = int(prefix)
    if len(prefix) == 2:
        return 1900 + n if n >= 56 else 2000 + n
    if len(prefix) == 4 and 1956 <= n <= 2035:
        return n
    return None


def check_law_numbers(fr_text, ar_text, ar_path, problems):
    """Compare les numéros de textes en acceptant les deux écritures arabes."""
    fr_body, ar_body = strip_noise(fr_text), strip_noise(ar_text)

    fr_laws = {}
    for prefix, num in LAW_RE.findall(fr_body):
        year = law_year(prefix)
        if year is None or law_year(num) is not None and len(num) == 4:
            continue  # plage d'années (« 2023-2025 ») : pas un numéro de texte
        key = f"{prefix}-{num}"
        fr_laws[key] = fr_laws.get(key, 0) + 1

    for key, n_fr in sorted(fr_laws.items()):
        prefix, num = key.split("-")
        year = law_year(prefix)
        literal = len(re.findall(rf"(?<![\d-]){re.escape(key)}(?![\d-])", ar_body))
        expanded = len(re.findall(rf"(?<!\d){num}\s+لسنة\s+{year}(?!\d)", ar_body))
        n_ar = literal + expanded

        if n_ar >= n_fr:
            continue

        # Cas le plus grave : l'ANNÉE a été prise pour le numéro d'ordre.
        # « loi n°83-112 » rendue « القانون عدد 83 لسنة 1983 ». Plausible,
        # cohérent avec la date affichée, invisible à la lecture de l'arabe.
        if num != prefix and re.search(rf"(?<!\d){prefix}\s+لسنة\s+{year}(?!\d)", ar_body):
            problems.append(
                f"{ar_path} : numéro de texte FAUSSÉ — « {key} » (texte {num} de {year}) "
                f"est rendu « عدد {prefix} لسنة {year} » : l'année a été prise pour le "
                f"numéro d'ordre."
            )
        elif n_ar == 0:
            problems.append(
                f"{ar_path} : numéro de texte — « {key} » absent de l'arabe "
                f"({n_fr}× en français), sous aucune des deux écritures."
            )
        else:
            problems.append(
                f"{ar_path} : numéro de texte — « {key} » apparaît {n_fr}× en français "
                f"et {n_ar}× en arabe."
            )


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

    check_law_numbers(fr_text, ar_text, ar_path, problems)
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

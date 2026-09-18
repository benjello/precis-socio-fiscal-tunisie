"""Augmentations générales des salaires de la fonction publique : relevé des décrets.

POURQUOI CE MODULE. Le chapitre du régime indiciaire portait ces montants dans un tableau
tapé à la main dont une cellule atteignait 330 caractères : chaque cellule y énonçait en
prose un décret, ses dates d'effet et ses montants par catégorie — « 2016-1, augmentation
générale, à chaque date : 60 D (A1, A2), 55 D (A3), 50 D (B, C, D, ouvriers) ». C'était de
la donnée structurée déguisée en phrase, illisible en tableau et intraçable en série.

Le CSV la rend structurée : une ligne par (décret, date d'effet, catégorie). Le chapitre
en tire alors DEUX tableaux là où il n'en avait qu'un — une chronologie mince des cycles,
et la grille des montants par catégorie — ainsi que la série par catégorie.

POURQUOI DU PYTHON PUR. Les tests du dépôt tournent `--isolated --no-project`, sans aucune
dépendance ; pandas n'apparaît que dans `dataframe()`, hors de la logique.

LES TITRES LONGS PASSENT EN INFOBULLE. Les intitulés officiels de ces décrets font de 234
à 383 caractères. Aucun n'a sa place dans une cellule ; tous doivent rester atteignables.
`infobulle()` émet un span Pandoc — `[forme courte]{title="intitulé complet"}` — qui rend
une infobulle native, sans CSS ni JavaScript.
"""
from __future__ import annotations

import csv
from pathlib import Path

# Ordre hiérarchique des catégories statutaires, puis les postes d'ouvriers, puis la
# mention « tous ». C'est l'ordre de lecture des décrets eux-mêmes.
ORDRE = ["A1", "A2", "A3", "B", "C", "D",
         "ouvriers", "ouvriers 3e unité", "autres ouvriers", "tous"]

# Clé de citation -> (forme courte, intitulé officiel complet).
# L'intitulé est repris VERBATIM de `precis/fr/references.json` : il sert d'infobulle, et
# une infobulle qui paraphraserait le titre officiel ne vaudrait rien.
DECRETS = {
    "decret2015-462": (
        "Décret 2015-462",
        "Décret gouvernemental n° 2015-462 du 24 juin 2015, portant majoration des "
        "indemnités spécifiques au profit des agents de l'Etat, des collectivités "
        "locales et des établissements publics à caractère administratif au titre de "
        "l'année 2014"),
    "decret2016-1": (
        "Décret 2016-1",
        "Décret gouvernemental n° 2016-1 du 5 janvier 2016, portant fixation du "
        "programme et des montants de l'augmentation générale des salaires au titre des "
        "années 2015 et 2016 et du programme et des montants de l'augmentation "
        "spécifique au profit des agents de l'Etat, des collectivités locales et des "
        "établissements publics à caractère administratif au titre des années 2016, "
        "2017 et 2018"),
    "decret2019-209": (
        "Décret 2019-209",
        "Décret gouvernemental n° 2019-209 du 5 mars 2019, portant augmentation des "
        "salaires au titre de la première tranche au profit des agents de l'Etat, des "
        "collectivités locales et des établissements publics à caractère administratif "
        "et fixation de ses montants"),
    "decret2019-1133": (
        "Décret 2019-1133",
        "Décret gouvernemental n° 2019-1133 du 12 décembre 2019, portant octroi de la "
        "deuxième et la troisième tranche de l'augmentation des salaires au profit des "
        "agents de l'Etat, des collectivités locales et des établissements publics à "
        "caractère administratif et la fixation de ses montants"),
    "decret2020-767": (
        "Décret 2020-767",
        "Décret gouvernemental n° 2020-767 du 18 septembre 2020, portant augmentation "
        "des salaires au profit des agents de l'Etat, des collectivités locales et des "
        "établissements publics à caractère administratif et la fixation de ses "
        "montants"),
    "decret-2022-797": (
        "Décret 2022-797",
        "Décret n° 2022-797 du 8 novembre 2022, fixant le programme et les montants de "
        "l'augmentation générale des salaires au profit des agents de l'Etat, des "
        "collectivités locales et des établissements publics à caractère administratif "
        "au titre des années 2023-2024-2025"),
    "decret2026-63": (
        "Décret 2026-63",
        "Décret n° 2026-63 du 30 avril 2026, fixant le programme et les montants de "
        "l'augmentation des salaires des agents de l'Etat, des collectivités locales et "
        "des établissements publics à caractère administratif pour les années 2026, "
        "2027 et 2028"),
}

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre"]


def charge(chemin: str | Path) -> list[dict]:
    """Rend les lignes longues du CSV, telles quelles."""
    with Path(chemin).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def court(cle: str) -> str:
    """Forme courte d'un décret — « Décret 2020-767 », quinze caractères."""
    return DECRETS[cle][0] if cle in DECRETS else cle


def infobulle(cle: str) -> str:
    """Span Pandoc : forme courte visible, intitulé officiel au survol.

    Pandoc rend `[x]{title="y"}` en `<span title="y">x</span>` : l'infobulle est celle du
    navigateur, sans feuille de style ni script. Le titre officiel reste ainsi accessible
    sans encombrer la cellule.
    """
    if cle not in DECRETS:
        return cle
    bref, complet = DECRETS[cle]
    return f'[{bref}]{{title="{complet}"}}'


def formate_date(iso: str) -> str:
    """« 2016-07-01 » -> « 1er juillet 2016 ». Vide si la date n'est pas établie."""
    if not iso:
        return "—"
    a, m, j = iso.split("-")
    jour = "1^er^" if j == "01" else str(int(j))
    return f"{jour} {MOIS[int(m) - 1]} {a}"


def categories_presentes(rangs: list[dict]) -> list[str]:
    """Les catégories effectivement RENDUES, dans l'ordre hiérarchique.

    Seules comptent les lignes portant une date d'effet établie : ce sont les seules que
    la grille affiche. Sans cette restriction, la catégorie « tous » — qui n'apparaît que
    sous le décret n° 2015-462, lequel n'énonce aucune date — ouvrirait une colonne
    entière qu'aucune valeur ne viendrait jamais remplir.
    """
    dates = {r["date_effet"] for r in rangs if r["date_effet"]}
    return [c for c in ORDRE
            if any(r["categorie"] == c and r["date_effet"] in dates for r in rangs)]


def dates_presentes(rangs: list[dict]) -> list[str]:
    """Les dates d'effet établies, en ordre chronologique."""
    return sorted({r["date_effet"] for r in rangs if r["date_effet"]})


def _montant(v: str) -> int:
    return int(float(v))


def tableau_cycles(rangs: list[dict]) -> str:
    """Chronologie MINCE : un cycle par ligne, décrets en forme courte, fourchette.

    Ce tableau ne porte plus les montants détaillés — ils ont leur propre tableau. Il
    répond à la question « quand, par quel texte », et rien d'autre.
    """
    cycles: dict[str, dict] = {}
    for r in rangs:
        c = cycles.setdefault(r["cycle"], {"textes": [], "dates": set(), "montants": []})
        if r["texte"] not in c["textes"]:
            c["textes"].append(r["texte"])
        if r["date_effet"]:
            c["dates"].add(r["date_effet"])
        c["montants"].append(_montant(r["montant"]))
    lignes = ["| Cycle | Décret(s) | Dates d'effet | Montants |",
              "|---|---|---|---|"]
    for cycle in sorted(cycles):
        c = cycles[cycle]
        # PAS de `[@clé]` ici : le style bibliographique développe la citation EN CLAIR
        # entre parenthèses, ce qui réinjecte dans la cellule les 234 à 383 caractères
        # du titre officiel qu'on vient précisément d'en retirer. La cellule mesurait
        # ainsi 664 caractères visibles au lieu des quinze attendus. Le titre reste
        # atteignable par l'infobulle, et la prose autour du tableau porte les citations.
        textes = ", ".join(infobulle(t) for t in c["textes"])
        dates = ", ".join(formate_date(d) for d in sorted(c["dates"])) or "—"
        bas, haut = min(c["montants"]), max(c["montants"])
        plage = f"{bas} D" if bas == haut else f"{bas} à {haut} D"
        lignes.append(f"| {cycle} | {textes} | {dates} | {plage} |")
    return "\n".join(lignes)


def tableau_montants(rangs: list[dict]) -> str:
    """La GRILLE : une ligne par date d'effet, une colonne par catégorie.

    C'est la donnée qui était prisonnière de la prose. Une cellule vide signifie que le
    décret ne vise pas cette catégorie à cette date — elle n'est pas comblée.
    """
    cats = categories_presentes(rangs)
    lignes = ["| Date d'effet | Texte | " + " | ".join(cats) + " |",
              "|---" * (len(cats) + 2) + "|"]
    for date in dates_presentes(rangs):
        du_jour = [r for r in rangs if r["date_effet"] == date]
        texte = infobulle(du_jour[0]["texte"])
        cellules = []
        for c in cats:
            v = [r for r in du_jour if r["categorie"] == c]
            cellules.append(str(_montant(v[0]["montant"])) if v else "")
        lignes.append(f"| {formate_date(date)} | {texte} | " + " | ".join(cellules) + " |")
    return "\n".join(lignes)


def serie_cumulee(rangs: list[dict], categorie: str) -> list[tuple[str, int]]:
    """(date d'effet, cumul des augmentations acquises) pour une catégorie.

    Le cumul est la somme des tranches servies jusqu'à la date : c'est ce que l'agent a
    gagné en dinars mensuels depuis 2015, et non le montant d'une tranche isolée. Les
    lignes sans date d'effet établie sont écartées — on ne peut pas les situer.
    """
    acquis, sortie = 0, []
    for date in dates_presentes(rangs):
        for r in rangs:
            if r["date_effet"] == date and r["categorie"] == categorie:
                acquis += _montant(r["montant"])
        sortie.append((date, acquis))
    return sortie


def imprime(chemin_csv: str | Path, quoi: str) -> None:
    """Imprime un tableau, pour un chunk Quarto `#| output: asis`."""
    rangs = charge(chemin_csv)
    rendu = {"cycles": tableau_cycles, "montants": tableau_montants}[quoi]
    print()
    print(rendu(rangs))
    print()


def dataframe(rangs: list[dict]):
    """Le relevé en DataFrame, pour la figure. Exige pandas."""
    import pandas as pd
    return pd.DataFrame([
        {"cycle": r["cycle"], "texte": r["texte"], "nature": r["nature"],
         "date_effet": r["date_effet"], "categorie": r["categorie"],
         "montant": _montant(r["montant"])}
        for r in rangs])

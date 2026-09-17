"""Lecture des relevés de tarifs et restitution des tableaux du précis.

POURQUOI UN MODULE PLUTÔT QUE `openfisca_tables.tableau_vers_markdown` : ce dernier
aligne à droite toute colonne qu'il juge numérique (`---:`). Les tableaux de tarifs du
chapitre portent `|---|---|` partout ; le réemployer changerait l'alignement du texte
publié. Ici l'émission préserve la forme exacte.

POURQUOI DU PYTHON PUR : les tests du dépôt tournent `--isolated --no-project`, sans
aucune dépendance. Un pivot écrit en pandas ne serait pas couvert. Le seul import
optionnel est `pandas`, réservé à `dataframe()`, qui ne sert qu'au rendu interactif.

FORMAT LONG. Le CSV porte une ligne par (tableau, ordre, colonne). Les quatre états que
le chapitre écrivait en prose dans ses cellules sont portés par `statut`, `valeur`
restant vide ; `recompose` les restitue mot pour mot.
"""
from __future__ import annotations

import csv
from pathlib import Path

# Les états encodés en prose dans les cellules publiées. La correspondance est
# bijective : c'est elle qui garantit que le pivot rend le tableau d'origine.
PROSE = {
    "ligne inexistante": "*(ligne inexistante)*",
    "ligne scindée": "*(ligne scindée)*",
    "non établi": "*(non établi)*",
    "sans objet": "—",
}

# Mise en forme de chaque tableau : colonnes du CSV à afficher, puis en-têtes publiés.
# C'est de la présentation, pas de la provenance — la provenance vit dans le manifeste.
TABLEAUX = {
    "advalorem-1988": {
        "champs": ["produit", "Taux 1988"],
        "entetes": ["Produit", "Taux 1988"],
    },
    "specifiques-1988": {
        "champs": ["position", "produit", "Tarif 1988"],
        "entetes": ["Position", "Produit", "Tarif 1988"],
    },
    "transfert-2007": {
        "champs": ["position", "produit", "Taux"],
        "entetes": ["Position tarifaire", "Désignation", "Taux"],
    },
    "petroliers": {
        "champs": ["position", "produit", "1988", "1991", "1999", "Consolidé 2023"],
        "entetes": ["Position", "Produit", "1988", "1991", "1999", "Consolidé 2023"],
    },
    "en-vigueur-2023": {
        "champs": ["position", "produit", "Droit de consommation"],
        "entetes": ["Position", "Désignation des produits", "Droit de consommation"],
    },
}


def charge(chemin: str | Path) -> list[dict]:
    """Rend les lignes longues du CSV, telles quelles."""
    with Path(chemin).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def recompose(valeur: str, unite: str, statut: str) -> str:
    """Rend la cellule publiée : soit « 15,228 D/hl », soit la prose de l'état."""
    if statut in PROSE:
        return PROSE[statut]
    return f"{valeur} {unite}".strip()


def pivot(rangs: list[dict], tableau: str) -> list[list[str]]:
    """Format long -> lignes du tableau large, dans l'ordre d'origine.

    Une ligne manquante n'est pas inventée : si une colonne attendue n'a pas de rang,
    la cellule reste vide plutôt que de recevoir une valeur plausible.
    """
    spec = TABLEAUX[tableau]
    par_ordre: dict[int, dict[str, str]] = {}
    for r in rangs:
        if r["tableau"] != tableau:
            continue
        d = par_ordre.setdefault(int(r["ordre"]), {})
        d["position"] = r["position"]
        d["produit"] = r["produit"]
        d[r["colonne"]] = recompose(r["valeur"], r["unite"], r["statut"])
    return [[par_ordre[o].get(c, "") for c in spec["champs"]]
            for o in sorted(par_ordre)]


def markdown(rangs: list[dict], tableau: str) -> str:
    """Tableau pipe, alignement à gauche partout — la forme des tableaux publiés."""
    spec = TABLEAUX[tableau]
    lignes = ["| " + " | ".join(spec["entetes"]) + " |",
              "|" + "|".join("---" for _ in spec["entetes"]) + "|"]
    for ligne in pivot(rangs, tableau):
        lignes.append("| " + " | ".join(ligne) + " |")
    return "\n".join(lignes)


def imprime(chemin_csv: str | Path, tableau: str) -> None:
    """Imprime le tableau pipe, pour un chunk Quarto `#| output: asis`.

    La LÉGENDE reste écrite dans le .qmd, juste au-dessus du chunk : elle porte l'ancre
    de référence croisée et se lit à l'œil. Seul le corps chiffré vient d'ici, afin que
    les mêmes valeurs ne soient plus tenues à deux endroits.
    """
    print()
    print(markdown(charge(chemin_csv), tableau))
    print()


def dataframe(rangs: list[dict], tableau: str):
    """Le même tableau en DataFrame, pour le rendu interactif. Exige pandas."""
    import pandas as pd
    spec = TABLEAUX[tableau]
    return pd.DataFrame(pivot(rangs, tableau), columns=spec["entetes"])

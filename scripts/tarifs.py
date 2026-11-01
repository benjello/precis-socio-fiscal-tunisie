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
    # CINQ DATES D'EFFET, une colonne par date où l'une des lignes change. Le tableau de la
    # loi de finances pour 2016 reprend les valeurs de l'annexe du 24 novembre 2015 : il
    # n'a pas de colonne, la date du 1er janvier 2016 ne change aucune valeur.
    "alcools-tarifs": {
        "champs": ["position", "produit", "4 août 1997", "21 février 2013",
                   "24 novembre 2015", "1er janvier 2018", "1er janvier 2021"],
        "entetes": ["Position", "Produit", "Depuis le 4 août 1997",
                    "Depuis le 21 février 2013", "Depuis le 24 novembre 2015",
                    "Depuis le 1er janvier 2018", "Depuis le 1er janvier 2021"],
    },
    "capsule-fiscale": {
        "champs": ["position", "produit", "Annexe IV de 1997", "13 août 2007",
                   "25 juin 2022"],
        "entetes": ["Catégorie", "Vins et contenances", "Annexe IV de 1997",
                    "Depuis le 13 août 2007", "Depuis le 25 juin 2022"],
    },
    # SIX COLONNES DE PÉRIODE, ET NON CINQ. Le taux de droit commun ne change que quatre
    # fois, ce qui suffirait à cinq colonnes ; mais le taux des petites et moyennes
    # sociétés naît en 2018, au milieu de la période où le droit commun vaut 25 %.
    # Fondre 2014-2020 en une colonne ferait croire que ce taux a existé dès 2014.
    "taux-chronologie": {
        "champs": ["produit", "1990-2006", "2007-2013", "2014-2017", "2018-2020",
                   "2021-2023", "Depuis 2024"],
        "entetes": ["Taux", "1990-2006", "2007-2013", "2014-2017", "2018-2020",
                    "2021-2023", "Depuis 2024"],
    },
    # LA PREMIÈRE LIGNE N'EST PAS UNE VALEUR MAIS UNE NATURE. De 1990 à 2005 les montants
    # sont des PLAFONDS — le minimum « ne peut excéder » — et depuis 2006 des PLANCHERS.
    # Un tableau qui les alignerait sans le dire ferait lire une baisse là où le
    # mécanisme s'est inversé.
    "minimum-impot": {
        "champs": ["produit", "1990-1997", "1998-2005", "2006-2010", "2011-2013",
                   "Depuis 2014"],
        "entetes": ["Élément", "1990-1997", "1998-2005", "2006-2010", "2011-2013",
                    "Depuis 2014"],
    },
    # DROITS DE DOUANE (relevé `douane/tarifs-releves-droits-douane.csv`). Le champ spécial
    # « @texte » est la citation de la ligne, `[@texte, article]`, bâtie depuis les champs
    # `texte` et `article` du relevé : le tableau montre alors la source de chaque ligne.
    "redevance": {
        "champs": ["position", "produit", "Minimum", "@texte"],
        "entetes": ["Effet", "Assiette et taux", "Minimum de perception", "Texte et article"],
    },
    # Trois tables « ancien taux → nouveau taux », une par date d'effet. Elles ne se
    # chaînent pas : les taux de départ de 1994 ne sont pas tous des taux d'arrivée de 1988.
    "correspondances": {
        "champs": ["position", "produit", "Taux après", "@texte"],
        "entetes": ["Effet", "Taux avant", "Taux après", "Texte et article"],
    },
    "bandes": {
        "champs": ["position", "produit", "Taux avant", "Taux après", "@texte"],
        "entetes": ["Effet", "Produits visés", "Taux avant", "Taux après",
                    "Texte et article"],
    },
    "minimum-perception": {
        "champs": ["position", "Minimum de perception", "Biens d'équipement", "@texte"],
        "entetes": ["Effet", "Minimum de perception<br>(tarif minimum ad valorem)",
                    "Biens d'équipement", "Texte et article"],
    },
    # Calendrier de l'article 11 de l'accord d'association : une ligne par moment, une
    # colonne par annexe. La ligne n'a pas de date : le texte compte en « années après
    # l'entrée en vigueur ». L'annexe 5 exprime ses parts en « taux de base » (même mot
    # que le texte), les annexes 3 et 4 en « droit de base ».
    "calendrier-ue": {
        "champs": ["position", "Annexe 3", "Annexe 4", "Annexe 5"],
        "entetes": ["Moment du calendrier",
                    "Annexe 3<br>(% du droit de base)",
                    "Annexe 4<br>(% du droit de base)",
                    "Annexe 5<br>(% du taux de base)"],
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
        if r.get("texte"):
            d.setdefault("@texte", "[@" + r["texte"]
                         + (", " + r["article"] if r.get("article") else "") + "]")
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

"""Enseignement supérieur : montants fixés par les textes, en dinars courants et en dinars de 2023.

Deux tableaux : la contribution financière des étudiants à la vie universitaire (`contribution`) ;
le capital minimal des établissements d'enseignement supérieur privés (`capital` : loi n° 2000-73,
art. 4, et loi n° 2008-59, art. 4 nouveau).

Pour la contribution, chaque ligne est un montant annuel fixé par un texte (clé de citation, article et page dans la
colonne `texte`) : décret n° 95-1419 du 31 juillet 1995, modifié par le décret n° 97-1359 du
14 juillet 1997 et par le décret gouvernemental n° 2016-1314 du 29 novembre 2016. Les montants
sont ceux de la note `docs/notes/education-superieur-2026-10-17.md`, § 4 (tableaux de 1995 et de
2016 relus à l'image du fascicule).

Le montant en dinars de 2023 est le montant courant multiplié par le rapport de l'indice des prix
à la consommation de 2023 à celui de l'année d'effet ; pour une année universitaire, l'année où
elle commence ; pour un texte sans clause d'effet, l'année où il devient exécutoire. Indice :
`scripts/dinars_constants.py` (`ipc-longue-periode`), année de base 2023, comme au chapitre des
aides (`fig_educ_aides_dinars_constants.py`).

Les catégories ne se suivent pas d'un texte à l'autre : 1995 distingue trois cycles ; 1997, trois
groupes de disciplines et quatre niveaux ; 2016, huit domaines et cinq niveaux. Les domaines qui
portent les mêmes montants (1 à 4 ; 7 et 8) partagent ici une ligne. Aucune série ne les enchaîne.

Usage : uv run python precis/fr/education/figures/fig_educ_superieur_montants.py
Écrit `figdata/fig_educ_superieur_montants.csv` et son sidecar `.yml`, que les tableaux de
`_superieur.qmd` reprennent. Le module n'est pas appelé au rendu.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parents[3] / "scripts"))
import figtools  # noqa: E402
import dinars_constants  # noqa: E402

ANNEE_BASE = 2023
SERIE_LOCALE = "educ-superieur-montants-du-droit"

T1995 = "decret95-1419, art. 2, p. 1664-1665"
T1995_6 = "decret95-1419, art. 6, p. 1664-1665"
T1997 = "decret97-1359, art. 2 nouveau et art. 3, p. 1347"
T1997_6 = "decret97-1359, art. 6 et 6 bis nouveaux, p. 1347"
T2016 = "decret-gouv2016-1314, art. 2 nouveau, p. 3589-3591"
T2016_6 = "decret-gouv2016-1314, art. 6 et 6 bis nouveaux, p. 3589-3591"

D1995 = "au plus tôt le 16 août 1995"
D1997 = "année universitaire 1997-1998"
D2016 = "au plus tôt le 11 décembre 2016"

# (tableau, texte de référence, catégorie, niveau, date d'effet, année de l'indice, montant courant, texte)
LIGNES = [
    # 1995 : par cycle, somme des six rubriques de l'art. 2
    ("contribution", "1995", "toutes disciplines", "premier cycle", D1995, 1995, 12.5, T1995),
    ("contribution", "1995", "toutes disciplines", "deuxième cycle", D1995, 1995, 17.5, T1995),
    ("contribution", "1995", "toutes disciplines", "troisième cycle", D1995, 1995, 59.0, T1995),
    ("contribution", "1995", "inscription exceptionnelle", "—", D1995, 1995, 20.0, T1995_6),
    # 1997 : par groupe de disciplines
    ("contribution", "1997", "groupe I", "premier cycle", D1997, 1997, 30.0, T1997),
    ("contribution", "1997", "groupe I", "deuxième cycle", D1997, 1997, 40.0, T1997),
    ("contribution", "1997", "groupe I", "DEA et doctorat", D1997, 1997, 100.0, T1997),
    ("contribution", "1997", "groupe I", "DESS", D1997, 1997, 100.0, T1997),
    ("contribution", "1997", "groupe II", "premier cycle", D1997, 1997, 40.0, T1997),
    ("contribution", "1997", "groupe II", "deuxième cycle", D1997, 1997, 60.0, T1997),
    ("contribution", "1997", "groupe II", "DEA et doctorat", D1997, 1997, 130.0, T1997),
    ("contribution", "1997", "groupe II", "DESS", D1997, 1997, 150.0, T1997),
    ("contribution", "1997", "groupe III", "premier cycle", D1997, 1997, 60.0, T1997),
    ("contribution", "1997", "groupe III", "deuxième cycle", D1997, 1997, 80.0, T1997),
    ("contribution", "1997", "groupe III", "DEA et doctorat", D1997, 1997, 200.0, T1997),
    ("contribution", "1997", "groupe III", "DESS", D1997, 1997, 200.0, T1997),
    ("contribution", "1997", "inscription exceptionnelle", "—", D1997, 1997, 40.0, T1997_6),
    ("contribution", "1997", "concours de réorientation", "—", D1997, 1997, 30.0, T1997_6),
    # 2016 : par domaine
    ("contribution", "2016", "domaines 1 à 4", "licence", D2016, 2016, 50.0, T2016),
    ("contribution", "2016", "domaines 1 à 4", "mastère", D2016, 2016, 110.0, T2016),
    ("contribution", "2016", "domaines 1 à 4", "doctorat", D2016, 2016, 110.0, T2016),
    ("contribution", "2016", "domaine 5", "licence", D2016, 2016, 60.0, T2016),
    ("contribution", "2016", "domaine 5", "mastère", D2016, 2016, 140.0, T2016),
    ("contribution", "2016", "domaine 5", "doctorat", D2016, 2016, 160.0, T2016),
    ("contribution", "2016", "domaine 6", "premier cycle", D2016, 2016, 70.0, T2016),
    ("contribution", "2016", "domaine 6", "deuxième cycle", D2016, 2016, 90.0, T2016),
    ("contribution", "2016", "domaine 6", "mastère", D2016, 2016, 210.0, T2016),
    ("contribution", "2016", "domaine 6", "doctorat", D2016, 2016, 210.0, T2016),
    ("contribution", "2016", "domaines 7 et 8", "licence", D2016, 2016, 70.0, T2016),
    ("contribution", "2016", "domaines 7 et 8", "premier cycle", D2016, 2016, 70.0, T2016),
    ("contribution", "2016", "domaines 7 et 8", "deuxième cycle", D2016, 2016, 90.0, T2016),
    ("contribution", "2016", "domaines 7 et 8", "mastère", D2016, 2016, 210.0, T2016),
    ("contribution", "2016", "domaines 7 et 8", "doctorat", D2016, 2016, 210.0, T2016),
    ("contribution", "2016", "inscription exceptionnelle", "—", D2016, 2016, 70.0, T2016_6),
    ("contribution", "2016", "concours de réorientation", "—", D2016, 2016, 50.0, T2016_6),
    # Capital minimal d'un établissement d'enseignement supérieur privé (D)
    ("capital", "2000", "capital minimal", "—", "au plus tôt le 2 août 2000", 2000, 150000.0,
     "loi2000-73, art. 4, p. 1787-1789"),
    ("capital", "2008", "capital minimal", "—", "au plus tôt le 13 août 2008", 2008, 2000000.0,
     "loi2008-59, art. 4 nouveau, p. 2414"),
]


def table() -> pd.DataFrame:
    ipc = dinars_constants.ipc()
    lignes = []
    for tableau, bareme, categorie, niveau, date, annee, montant, texte in LIGNES:
        coef = ipc[ANNEE_BASE] / ipc[annee]
        lignes.append({
            "tableau": tableau, "bareme": bareme, "categorie": categorie, "niveau": niveau, "date_effet": date,
            "annee_indice": annee, "montant_courant": montant,
            "unite": "D/an" if tableau == "contribution" else "D",
            "ipc_annee": ipc[annee], "ipc_2023": ipc[ANNEE_BASE],
            "montant_dinars_2023": round(montant * coef, 1), "texte": texte,
        })
    return pd.DataFrame(lignes)


def main() -> None:
    figtools.register_provenance(
        SERIE_LOCALE,
        titre=("Enseignement supérieur : contribution financière des étudiants à la vie "
               "universitaire (décrets de 1995, 1997 et 2016) et capital minimal des "
               "établissements privés (lois de 2000 et 2008)"),
        sources=["decret95-1419", "decret97-1359", "decret-gouv2016-1314", "loi2000-73",
                 "loi2008-59"],
        caveats=("Montants relevés dans les textes cités ligne par ligne (colonne texte : "
                 "clé de citation, article, page). Montant en dinars de 2023 = montant courant × "
                 "IPC 2023 / IPC de l'année d'effet ; pour une année universitaire, l'année où elle "
                 "commence. Les catégories (cycles en 1995, groupes de disciplines en 1997, domaines "
                 "en 2016) ne se correspondent pas d'un texte à l'autre."),
    )
    d = table()
    figtools.write_figdata(d, ICI.parent / "figdata" / "fig_educ_superieur_montants.csv",
                           SERIE_LOCALE, *dinars_constants.SERIES_IPC)
    with pd.option_context("display.max_rows", None, "display.width", 200):
        print(d[["tableau", "bareme", "categorie", "niveau", "montant_courant", "montant_dinars_2023"]])


if __name__ == "__main__":
    main()

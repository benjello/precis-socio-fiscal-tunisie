"""Enseignement scolaire : montants fixés par les textes, en dinars courants et en dinars de 2023.

Chaque ligne est un montant fixé par un texte (clé de citation et article dans la colonne
`texte`), relevé dans la note documentaire `docs/notes/education-scolaire-2026-10-17.md`
(§ 3.1 et § 5). Le montant en dinars de 2023 est le montant courant multiplié par le rapport
de l'indice des prix à la consommation de 2023 à celui de l'année d'effet ; pour une année
scolaire, l'année d'effet est celle où elle commence ; pour un texte daté « au plus tôt »,
l'année de cette date. L'indice est celui du précis (`scripts/dinars_constants.py` :
`ipc-longue-periode`, base 100 en 1970) ; l'année de base est 2023, celle du livre.

Usage : uv run python precis/fr/education/figures/fig_educ_scolaire_montants.py
Écrit `figdata/fig_educ_scolaire_montants.csv` et son sidecar `.yml`, que les tableaux de
`_scolaire.qmd` reprennent. Le module n'est pas appelé au rendu.
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
SERIE_LOCALE = "educ-scolaire-montants-du-droit"

# (tableau, grandeur, date d'effet, année de l'indice, montant courant, unité, texte)
LIGNES = [
    # Cours particuliers dans l'établissement public, par élève et par mois
    ("cours", "primaire", "au plus tôt le 13 janvier 2016", 2016, 20, "D/mois",
     "arrete2015-12-31-cours-particuliers, art. 1, p. 75-76"),
    ("cours", "cycle préparatoire", "au plus tôt le 13 janvier 2016", 2016, 25, "D/mois",
     "arrete2015-12-31-cours-particuliers, art. 1, p. 75-76"),
    ("cours", "secondaire, 1re à 3e année", "au plus tôt le 13 janvier 2016", 2016, 30, "D/mois",
     "arrete2015-12-31-cours-particuliers, art. 1, p. 75-76"),
    ("cours", "secondaire, 4e année", "au plus tôt le 13 janvier 2016", 2016, 35, "D/mois",
     "arrete2015-12-31-cours-particuliers, art. 1, p. 75-76"),
    ("cours", "primaire", "au plus tôt le 22 novembre 2023", 2023, 30, "D/mois",
     "arrete2023-11-13-cours-particuliers, art. 1 nouveau, p. 3087"),
    ("cours", "cycle préparatoire", "au plus tôt le 22 novembre 2023", 2023, 35, "D/mois",
     "arrete2023-11-13-cours-particuliers, art. 1 nouveau, p. 3087"),
    ("cours", "secondaire, 1re à 3e année", "au plus tôt le 22 novembre 2023", 2023, 40, "D/mois",
     "arrete2023-11-13-cours-particuliers, art. 1 nouveau, p. 3087"),
    ("cours", "secondaire, 4e année", "au plus tôt le 22 novembre 2023", 2023, 45, "D/mois",
     "arrete2023-11-13-cours-particuliers, art. 1 nouveau, p. 3087"),
    # Jardins d'enfants publics du ministère de la famille, par enfant
    ("jardins", "frais d'inscription", "au plus tôt le 23 octobre 2022", 2022, 30, "D/an",
     "arrete2022-10-12-jardins-publics, art. 2, p. 2811"),
    ("jardins", "frais mensuels", "au plus tôt le 23 octobre 2022", 2022, 50, "D/mois",
     "arrete2022-10-12-jardins-publics, art. 2, p. 2811"),
    ("jardins", "assurance", "au plus tôt le 23 octobre 2022", 2022, 5, "D/an",
     "arrete2022-10-12-jardins-publics, art. 2, p. 2811"),
]


def table() -> pd.DataFrame:
    ipc = dinars_constants.ipc()
    lignes = []
    for tableau, grandeur, date, annee, montant, unite, texte in LIGNES:
        coef = ipc[ANNEE_BASE] / ipc[annee]
        lignes.append({
            "tableau": tableau, "grandeur": grandeur, "date_effet": date,
            "annee_indice": annee, "montant_courant": montant, "unite": unite,
            "ipc_annee": ipc[annee], "ipc_2023": ipc[ANNEE_BASE],
            "montant_dinars_2023": round(montant * coef, 3), "texte": texte,
        })
    return pd.DataFrame(lignes)


def main() -> None:
    figtools.register_provenance(
        SERIE_LOCALE,
        titre="Enseignement scolaire : montants fixés par les textes",
        sources=[],
        caveats=("Montants relevés dans les textes cités ligne par ligne (colonne texte : clé de "
                 "citation, article, page). Montant en dinars de 2023 = montant courant × IPC 2023 / "
                 "IPC de l'année d'effet ; pour un texte daté « au plus tôt », l'année de cette date."),
    )
    d = table()
    figtools.write_figdata(d, ICI.parent / "figdata" / "fig_educ_scolaire_montants.csv",
                           SERIE_LOCALE, *dinars_constants.SERIES_IPC)
    with pd.option_context("display.max_rows", None, "display.width", 200):
        print(d[["tableau", "grandeur", "date_effet", "montant_courant", "montant_dinars_2023"]])


if __name__ == "__main__":
    main()

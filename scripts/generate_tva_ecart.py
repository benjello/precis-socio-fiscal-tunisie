"""Écart de la recette de TVA à la prévision de la loi de finances initiale, 2001-2025.

Écrit `precis/_seriescache/tva-ecart-prevision-realise.csv`, lue par `figtools.series` :
une ligne par exercice 2001-2026.

  - `prevision_MD`  : somme des deux lignes de TVA (régime d'importation, régime intérieur)
    du tableau A de la loi de finances INITIALE, millions de dinars courants
    (`precis/fr/fiscalite/tva/recettes-tva-par-regime.csv`) ;
  - `realise_MD`    : rubrique « TVA » des recettes fiscales de l'État du ministère des
    Finances, série `recettes-fiscales-composition` (colonne `tva_MDT`) ; vide en 2026 ;
  - `ecart_MD`      : realise_MD − prevision_MD ;
  - `ecart_pct_prevision` : 100 × ecart_MD / prevision_MD ;
  - `lfc_MD`        : prévision de la loi de finances complémentaire, quand le classeur du
    ministère la porte (`tva/classeur-tva-lf-lfc.csv`) : information, jamais dénominateur ;
  - `pib_base1983_MD`, `pib_base1997_MD`, `pib_base2015_MD`, `pib_non_rattache_MD` : le PIB aux
    prix courants de chaque base des comptes nationaux (série `pib-courant-par-base`), UN par
    colonne, jamais raccordés ; `pib_non_rattache_MD` est la valeur du ministère que la source ne
    rattache à aucune base (2002-2004, 2025) ;
  - `ecart_pct_pib_base1983`, `..._base1997`, `..._base2015`, `..._non_rattache` : 100 ×
    ecart_MD / PIB de la colonne correspondante. Une année absente d'une base reste vide.

Le PIB « présumé » de base 1983 (1986-1991) est hors période. Aucun PIB n'est converti d'une base
à l'autre. `uv run python scripts/generate_tva_ecart.py` régénère le fichier ; le test
`tests/test_tva_ecart.py` le recalcule autrement et le compare.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
CACHE = RACINE / "precis" / "_seriescache"
TVA = RACINE / "precis" / "fr" / "fiscalite" / "tva"
SORTIE = CACHE / "tva-ecart-prevision-realise.csv"
ANNEES = range(2001, 2027)
BASES = ("base1983", "base1997", "base2015", "non_rattache")


def pib_par_base() -> dict[str, dict[int, float]]:
    pib = pd.read_csv(CACHE / "pib-courant-par-base.csv")
    sortie: dict[str, dict[int, float]] = {b: {} for b in BASES}
    for r in pib.itertuples(index=False):
        texte = str(r.base)
        if texte.startswith("non rattachée"):
            cle = "non_rattache"
        elif "présumée" in texte:
            continue
        else:
            cle = next((f"base{b}" for b in (1983, 1997, 2015) if str(b) in texte), None)
            if cle is None:
                continue
        assert int(r.annee) not in sortie[cle], (cle, r.annee)
        sortie[cle][int(r.annee)] = float(r.pib_MD)
    return sortie


def construire() -> pd.DataFrame:
    regimes = pd.read_csv(TVA / "recettes-tva-par-regime.csv")
    prevision = regimes.groupby("annee")["valeur_md"].sum()
    realise = pd.read_csv(CACHE / "recettes-fiscales-composition.csv").set_index("annee")["tva_MDT"]
    lfc = pd.read_csv(TVA / "classeur-tva-lf-lfc.csv").set_index("annee")["lfc_MD"]
    pib = pib_par_base()
    lignes = []
    for a in ANNEES:
        p = float(prevision[a])
        r = float(realise[a]) if a in realise.index and pd.notna(realise.get(a)) and a <= 2025 else None
        ligne = {"annee": a, "prevision_MD": p, "realise_MD": r}
        e = None if r is None else r - p
        ligne["ecart_MD"] = None if e is None else round(e, 6)
        ligne["ecart_pct_prevision"] = None if e is None else round(100 * e / p, 6)
        ligne["lfc_MD"] = float(lfc[a]) if a in lfc.index and pd.notna(lfc[a]) else None
        for b in BASES:
            v = pib[b].get(a)
            ligne[f"pib_{b}_MD"] = v
        for b in BASES:
            v = pib[b].get(a)
            ligne[f"ecart_pct_pib_{b}"] = None if (e is None or v is None) else round(100 * e / v, 6)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def main() -> None:
    d = construire()
    d.to_csv(SORTIE, index=False)
    print(f"{SORTIE.relative_to(RACINE)} : {len(d)} lignes")


if __name__ == "__main__":
    main()

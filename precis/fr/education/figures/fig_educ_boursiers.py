"""Figure « Étudiants et boursiers de la bourse nationale » du chapitre des aides (F3).

`donnees()` copie, ligne à ligne, les trois relevés de la série
`education-boursiers-bourse-nationale` du catalogue de `tunisia-data` (lue par
`figtools.series()`) dans le figdata `figdata/fig_educ_boursiers.csv`, avec leur source et leur
page ; aucune valeur saisie à la main. `vues()` lit ce figdata. Relancer après une correction
de la série :

    uv run python precis/fr/education/figures/fig_educ_boursiers.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
sys.path.insert(0, str(ICI.parents[3] / "scripts"))
import figtools  # noqa: E402
import fig_educ_depense as fd  # noqa: E402

RELEVES = (
    ("etudiants-bourse-nationale", "Étudiants"),
    ("boursiers-bourse-nationale", "Boursiers"),
    ("part-bourse-nationale", "Part des boursiers (%)"),
)
SLUG = "fig_educ_boursiers"
PREVISION = 2016  # année universitaire 2016-2017 : chiffres ronds, vraisemblablement une prévision


def donnees() -> None:
    import fig_educ_depense_donnees as dd
    dd.FICHE = "docs/notes/education-aides-universitaires-2026-10-17.md, sources/education-boursiers.md"
    dd.DATE = "2026-10-30"
    rows = []
    for cle, nom in RELEVES:
        for r in dd.lire(cle).itertuples():
            rows.append({"Série": nom, "Période": r.annee, "Valeur": float(r.valeur) if cle.startswith("part") else int(r.valeur),
                         "Unité": r.unite, "Page": int(r.page), "Source": r.source})
    dd.ecrire(SLUG, pd.DataFrame(rows, dtype=object), ["budget-mesrs-2017", "budget-mesrs-2016"], [
        "Ministère de l'Enseignement supérieur et de la Recherche scientifique, budget de l'État pour 2017 "
        "(p. 33), tableau de l'évolution du nombre d'étudiants et de bourses universitaires en Tunisie ; "
        "le budget de 2016 (p. 25) donne la même table jusqu'en 2015-2016",
        "la source ne dit pas si les étudiants sont ceux du seul enseignement public, ni si les mastères "
        "et doctorats sont comptés ; ces étudiants ne sont pas ceux de l'Annuaire statistique de l'INS",
        "2016-2017 : chiffres ronds, absents du budget de 2016, vraisemblablement une prévision",
        "régime de la bourse de 2012, appliqué dès l'année universitaire 2011-2012"],
        "Étudiants et boursiers de la bourse nationale en Tunisie, 2008-2009 à 2016-2017",
        series=["education-boursiers-bourse-nationale"])


def _serie(d: pd.DataFrame, nom: str) -> pd.Series:
    s = d[d["Série"] == nom].copy()
    s.index = s["Période"].str[:4].astype(int)
    return s["Valeur"].astype(float)


def vues():
    figtools.apply_lang_font()
    d = fd.lire(SLUG)
    et, bo, pa = (_serie(d, n) for _, n in RELEVES)
    vues = []

    fig, ax = plt.subplots(figsize=(9.3, 4.8))
    fd._courbe(ax, et / 1000, fd.BLEU, "Étudiants", "milliers d'étudiants", dec=1, provisoires=(PREVISION,))
    fd._courbe(ax, bo / 1000, fd.ORANGE, "Boursiers", "milliers de boursiers", dec=1, provisoires=(PREVISION,))
    fd._rupture(ax, 2011, "régime de 2012, dès 2011-2012", 0)
    fd._rupture(ax, PREVISION, "2016-2017 : chiffres ronds, probable prévision", 1)
    fd._habille(ax, "Milliers", 2008, 2016, ymin=0, pas=1)
    ax.set_xlabel(figtools.fig_text("Année universitaire commençant en"), fontsize=8)
    fd._legende(ax, 2)
    fig.tight_layout()
    vues.append(("Effectifs", fig))

    fig, ax = plt.subplots(figsize=(9.3, 4.8))
    fd._courbe(ax, pa, fd.VERT, "Part des étudiants qui sont boursiers", "%", dec=1, provisoires=(PREVISION,))
    fd._rupture(ax, 2011, "régime de 2012, dès 2011-2012", 0)
    fd._rupture(ax, PREVISION, "2016-2017 : chiffres ronds, probable prévision", 1)
    fd._habille(ax, "Part des étudiants (%)", 2008, 2016, ymin=0, pas=1)
    ax.set_xlabel(figtools.fig_text("Année universitaire commençant en"), fontsize=8)
    fd._legende(ax, 1)
    fig.tight_layout()
    vues.append(("Part des boursiers", fig))
    return vues


if __name__ == "__main__":
    donnees()

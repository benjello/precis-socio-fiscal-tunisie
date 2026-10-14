"""Indice OMS des services essentiels (ODD 3.8.1), Tunisie, 2000-2023.

La figure lit figtools.series(), qui prend la série cataloguée dans
tunisia-data ou son snapshot versionné pour un rendu autonome du site.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402


SERIE = "oms-couverture-services-tunisie-2000-2023"
_L = {
    "annee": {"fr": "Année", "ar": "السنة"},
    "indice": {"fr": "Couverture des services essentiels (indice de 0 à 100)",
               "ar": "تغطية الخدمات الصحية الأساسية (مؤشر من 0 إلى 100)"},
    "indicateur": {"fr": "Indicateur OMS", "ar": "مؤشر منظمة الصحة العالمية"},
}


def _lab(cle: str) -> str:
    return _L[cle][figtools.lang()]


def _donnees():
    d = figtools.series(SERIE).sort_values("annee")
    assert d.annee.tolist() == list(range(2000, 2024))
    return d


def fig_indice():
    figtools.apply_lang_font()
    d = _donnees()
    fig, ax = plt.subplots(figsize=(9.4, 4.4))
    couleur = "#08519c"
    ax.plot(d.annee, d.indice, color=couleur, lw=2, marker="o", ms=4)
    for r in d.itertuples():
        (point,) = ax.plot([int(r.annee)], [int(r.indice)], marker="o",
                           ls="none", ms=14, color=couleur, alpha=0.01, zorder=5)
        figtools.infobulle(point, f"{int(r.annee)} · {_lab('indice')} : {int(r.indice)}")
    ax.set_xlim(1999.5, 2023.5)
    ax.set_ylim(0, 100)
    ax.set_xticks([2000, 2004, 2008, 2012, 2016, 2020, 2023])
    ax.set_xlabel(figtools.fig_text(_lab("annee")))
    ax.set_ylabel(figtools.fig_text(_lab("indice")))
    ax.grid(axis="y", color="#d7dce2", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig


def table():
    return _donnees().rename(columns={
        "annee": _lab("annee"), "indice": _lab("indice"),
        "indicateur": _lab("indicateur"),
    })

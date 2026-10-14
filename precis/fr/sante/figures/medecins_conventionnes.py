"""Médecins de libre pratique conventionnés par la CNAM, 2007-2021.

L'effectif est celui des deux lignes « Médecins Généralistes » et « Médecins
Spécialistes » de la publication CNAM ; l'activité privée complémentaire est
une autre ligne et n'est pas additionnée. Série issue de tunisia-data, lue par
figtools.series() pour que le site puisse aussi se construire sur son snapshot.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402


SERIE = "cnam-medecins-conventionnes-2007-2021"
COULEURS = {"generalistes": "#08519c", "specialistes": "#b45100"}
MARQUEURS = {"generalistes": "o", "specialistes": "s"}
LIBELLES = {
    "generalistes": {"fr": "Généralistes", "ar": "أطباء عامّون"},
    "specialistes": {"fr": "Spécialistes", "ar": "أطباء مختصّون"},
    "annee": {"fr": "Année", "ar": "السنة"},
    "nombre": {"fr": "Médecins conventionnés", "ar": "أطباء متعاقدون"},
    "edition": {"fr": "Édition", "ar": "الطبعة"},
    "page": {"fr": "Page", "ar": "الصفحة"},
}


def _lab(cle: str) -> str:
    return LIBELLES[cle][figtools.lang()]


def _donnees():
    d = figtools.series(SERIE).sort_values("annee")
    assert len(d) == 15 and d.annee.tolist() == list(range(2007, 2022))
    return d


def fig_effectifs():
    figtools.apply_lang_font()
    d = _donnees()
    fig, ax = plt.subplots(figsize=(9.4, 4.7))
    for cle in ("generalistes", "specialistes"):
        couleur, marqueur = COULEURS[cle], MARQUEURS[cle]
        ax.plot(d.annee, d[cle], color=couleur, marker=marqueur, lw=2,
                ms=5, label=figtools.fig_text(_lab(cle)))
        for r in d.itertuples():
            nombre = int(getattr(r, cle))
            (point,) = ax.plot([int(r.annee)], [nombre], marker=marqueur,
                               ls="none", ms=14, color=couleur, alpha=0.01, zorder=5)
            figtools.infobulle(
                point, f"{int(r.annee)} · {_lab(cle)} : {nombre:,}".replace(",", " "))
    ax.set_xlim(2006.5, 2021.5)
    ax.set_ylim(0, 6100)
    ax.set_xticks([2007, 2010, 2013, 2016, 2019, 2021])
    ax.set_xlabel(figtools.fig_text(_lab("annee")))
    ax.set_ylabel(figtools.fig_text(_lab("nombre")))
    ax.grid(axis="y", color="#d7dce2", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, loc="upper left")
    fig.tight_layout()
    return fig


def table():
    d = _donnees()
    return d.rename(columns={
        "annee": _lab("annee"),
        "generalistes": _lab("generalistes"),
        "specialistes": _lab("specialistes"),
        "edition": _lab("edition"),
        "page": _lab("page"),
    })

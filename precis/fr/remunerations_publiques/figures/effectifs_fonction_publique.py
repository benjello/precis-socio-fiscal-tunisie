"""Figures « effectifs et salaires de la fonction publique » (source INS).

Frontière : les séries viennent de `tunisia_data` (entrepôt, enquête INS
« Caractéristiques des agents de la fonction publique et leurs salaires
2010-2021 ») ; ici on prépare le figdata sourcé et on rend les figures.

    from figures import effectifs_fonction_publique as efp
    efp.fig_effectifs()   # figure d'ouverture : effectifs FP 2015-2021
    efp.fig_salaire()     # salaire mensuel moyen 2015-2020

Réserve : rupture de série des collectivités locales 2016→2017 (changement
de périmètre/comptage). La tendance se lit sur la série **hors collectivités
locales** ; le total est tracé en pointillé avec un repère à la rupture.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# accès aux séries via la couche figtools (entrepôt ou snapshot du précis)
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_EFF = "fonction-publique-effectifs"
SERIE_SAL = "fonction-publique-salaires"

_HORS = "Nombre d’agents hors Collectivités Locales"
_LOC = "Nombre d’agents des Collectivités Locales"
_TOT = "Total"


def _pivot(serie: str, indicateurs: list[str]):
    """Série longue → large (annee × indicateur), restreinte aux niveaux tracés."""
    df = figtools.series(serie)
    w = (df[df["indicateur"].isin(indicateurs)]
         .pivot(index="annee", columns="indicateur", values="valeur")
         .reset_index())
    w.columns.name = None
    return w[["annee", *[c for c in indicateurs if c in w.columns]]]


# libellés bilingues (FR source de vérité ; AR pour le livre arabe)
_L = {
    "col_hors":  {"fr": "Hors collectivités locales", "ar": "باستثناء الجماعات المحلية"},
    "col_loc":   {"fr": "Collectivités locales", "ar": "الجماعات المحلية"},
    "col_tot":   {"fr": "Total fonction publique", "ar": "إجمالي الوظيفة العمومية"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "lg_hors":   {"fr": "Hors collectivités locales (série homogène)",
                  "ar": "باستثناء الجماعات المحلية (سلسلة متجانسة)"},
    "lg_tot":    {"fr": "Total fonction publique", "ar": "إجمالي الوظيفة العمومية"},
    "lg_loc":    {"fr": "Collectivités locales", "ar": "الجماعات المحلية"},
    "rupture":   {"fr": "rupture de série :\nchangement de périmètre\ndes collectivités locales",
                  "ar": "انقطاع السلسلة:\nتغيّر نطاق\nالجماعات المحلية"},
    "xlabel":    {"fr": "Année", "ar": "السنة"},
    "ylabel":    {"fr": "Effectifs (milliers d’agents)", "ar": "الأعداد (بآلاف الأعوان)"},
    "title":     {"fr": "Effectifs de la fonction publique en Tunisie, 2015-2021",
                  "ar": "أعداد أعوان الوظيفة العمومية في تونس، 2015-2021"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def effectifs_table():
    """Tableau (onglet Données) : effectifs par périmètre, milliers d'agents."""
    w = _pivot(SERIE_EFF, [_HORS, _LOC, _TOT])
    return w.rename(columns={
        "annee": _lab("col_annee"),
        _HORS: _lab("col_hors"),
        _LOC: _lab("col_loc"),
        _TOT: _lab("col_tot"),
    })


def fig_effectifs():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    w = _pivot(SERIE_EFF, [_HORS, _LOC, _TOT])
    y = w["annee"]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(y, w[_HORS], "o-", color="#1f6feb", lw=2.2, ms=5, label=ft(_lab("lg_hors")))
    ax.plot(y, w[_TOT], "s--", color="#6e7781", lw=1.6, ms=4, label=ft(_lab("lg_tot")))
    ax.plot(y, w[_LOC], "^:", color="#bf8700", lw=1.4, ms=4, label=ft(_lab("lg_loc")))
    # repère de la rupture de périmètre 2016→2017
    ax.axvspan(2016, 2017, color="#bf8700", alpha=0.08)
    ax.annotate("\n".join(ft(line) for line in _lab("rupture").split("\n")),
                xy=(2016.5, w[_LOC].max() * 0.9), fontsize=7.5, color="#7a5b00",
                ha="center", va="top")
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_ylabel(ft(_lab("ylabel")))
    ax.set_title(ft(_lab("title")))
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="center left", fontsize=8.5)
    fig.tight_layout()
    return fig


def salaire_table():
    df = figtools.series(SERIE_SAL)
    keep = ["Salaire mensuel brut avec contributions",
            "Salaire mensuel brut sans contributions",
            "Le salaire mensuel net"]
    w = (df[df["indicateur"].isin(keep)]
         .pivot(index="annee", columns="indicateur", values="valeur")
         .reset_index())
    w.columns.name = None
    return w.rename(columns={
        "annee": "Année",
        "Salaire mensuel brut avec contributions": "Brut (avec contributions)",
        "Salaire mensuel brut sans contributions": "Brut (sans contributions)",
        "Le salaire mensuel net": "Net",
    })


def fig_salaire():
    w = salaire_table()
    y = w["Année"]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(y, w["Brut (avec contributions)"], "o-", color="#1f6feb", lw=2, ms=4,
            label="Brut (avec contributions)")
    ax.plot(y, w["Brut (sans contributions)"], "s--", color="#8957e5", lw=1.6, ms=3,
            label="Brut (sans contributions)")
    ax.plot(y, w["Net"], "^-.", color="#d1242f", lw=1.6, ms=3, label="Net")
    ax.set_xlabel("Année")
    ax.set_ylabel("Salaire mensuel (dinars courants)")
    ax.set_title("Salaire mensuel moyen dans la fonction publique, 2015-2020")
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8.5)
    fig.tight_layout()
    return fig

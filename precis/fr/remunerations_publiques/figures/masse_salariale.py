"""Figures « masse salariale publique » du livre *Rémunérations publiques*.

Frontière : les séries viennent de `tunisia_data` (entrepôt) ; ici on prépare le
figdata téléchargeable (sourcé) et on rend les figures. À appeler depuis un chunk
Quarto de `index.qmd`.

    from figures import masse_salariale as ms
    ms.prepare()        # écrit figdata/*.csv sourcés
    ms.fig_A()          # rend la figure A
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# helper partagé du précis (precis/scripts/figtools.py)
_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402

HERE = Path(__file__).resolve().parent
FIGDATA = HERE.parent / "figdata"
SERIE = "masse-salariale-ratios"
FACTOR = 1.060  # base2015 / base2010 (mesuré sur le CNAT)


def prepare(generated: str | None = None):
    """Écrit les figdata sourcés (téléchargeables sur le site)."""
    df = figtools.series(SERIE)
    a = df[["annee", "ms_sur_pib_pct", "ms_sur_depenses_totales_pct"]].dropna(how="all")
    figtools.write_figdata(a, FIGDATA / "fig_A_masse_salariale.csv", SERIE,
                           note="masse salariale / PIB et / dépenses, 1990-2025",
                           generated=generated)
    b = df[["annee", "ms_sur_pib_pct"]].copy()
    b["ms_sur_pib_base2010_pct"] = (b["ms_sur_pib_pct"] * FACTOR).round(2)
    figtools.write_figdata(b, FIGDATA / "fig_B_reconciliation.csv",
                           SERIE, "masse-salariale-reconciliation",
                           note="réconciliation base 2015 vs base 2010 (FMI/BM)",
                           generated=generated)
    return df


# libellés bilingues (FR source de vérité ; AR pour le livre arabe)
_L = {
    "lg_pib":  {"fr": "… du PIB (éch. gauche)", "ar": "… من الناتج المحلي الإجمالي (يسار)"},
    "lg_dep":  {"fr": "… des dépenses totales (éch. droite)",
                "ar": "… من إجمالي النفقات (يمين)"},
    "y_pib":   {"fr": "Masse salariale / PIB (%)",
                "ar": "كتلة الأجور / الناتج المحلي الإجمالي (%)"},
    "y_dep":   {"fr": "Masse salariale / dépenses (%)", "ar": "كتلة الأجور / النفقات (%)"},
    "xlabel":  {"fr": "Année", "ar": "السنة"},
    "title":   {"fr": "Poids de la masse salariale publique en Tunisie, 1990-2025",
                "ar": "وزن كتلة الأجور العمومية في تونس، 1990-2025"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_pib":   {"fr": "% du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "col_dep":   {"fr": "% des dépenses totales", "ar": "% من إجمالي النفقات"},
    "col_fonc":  {"fr": "% des dépenses de fonctionnement", "ar": "% من نفقات التسيير"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def fig_A():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    df = figtools.series(SERIE)
    y = df["annee"]
    fig, ax1 = plt.subplots(figsize=(9, 5))
    ax2 = ax1.twinx()
    l1, = ax1.plot(y, df["ms_sur_pib_pct"], "o-", color="#1f6feb", lw=2, ms=4,
                   label=ft(_lab("lg_pib")))
    l2, = ax2.plot(y, df["ms_sur_depenses_totales_pct"], "s--", color="#d1242f", lw=1.8, ms=3,
                   label=ft(_lab("lg_dep")))
    ax1.set_ylabel(ft(_lab("y_pib")), color="#1f6feb")
    ax2.set_ylabel(ft(_lab("y_dep")), color="#d1242f")
    ax1.set_xlabel(ft(_lab("xlabel")))
    ax1.set_title(ft(_lab("title")))
    ax1.grid(True, alpha=0.3)
    ax1.legend(handles=[l1, l2], loc="upper left", fontsize=9)
    fig.tight_layout()
    return fig


def ratios_table():
    """Tableau (onglet Données) : masse salariale en % du PIB et des dépenses."""
    df = figtools.series(SERIE)
    cols = ["annee", "ms_sur_pib_pct", "ms_sur_depenses_totales_pct",
            "ms_sur_depenses_fonctionnement_pct"]
    w = df[[c for c in cols if c in df.columns]].copy()
    return w.rename(columns={
        "annee": _lab("col_annee"),
        "ms_sur_pib_pct": _lab("col_pib"),
        "ms_sur_depenses_totales_pct": _lab("col_dep"),
        "ms_sur_depenses_fonctionnement_pct": _lab("col_fonc"),
    })


def fig_B():
    df = figtools.series(SERIE)
    y, pib = df["annee"], df["ms_sur_pib_pct"]
    fmi_bm = {2010: 10.7, 2017: 14.7, 2019: 14.1, 2020: 17.6}
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(y, pib, "o-", color="#1f6feb", lw=2, ms=4, label="Officiel — PIB base 2015")
    ax.plot(y, pib * FACTOR, "^--", color="#8957e5", lw=1.5, ms=3,
            label="Recalculé en PIB base 2010 (×1,06)")
    ax.scatter(list(fmi_bm), list(fmi_bm.values()), color="#d1242f", zorder=5, s=55,
               label="Rapporté FMI / Banque mondiale (base 2010)")
    ax.set_xlabel("Année")
    ax.set_ylabel("Masse salariale / PIB (%)")
    ax.set_title("Masse salariale / PIB : réconciliation officiel vs FMI/BM")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=9)
    fig.text(0.01, -0.02, figtools.source_line(SERIE, "masse-salariale-reconciliation"),
             fontsize=7, color="#555")
    fig.tight_layout()
    return fig

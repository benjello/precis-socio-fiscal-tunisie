"""Figure « structure des fonctionnaires par catégorie statutaire » (source INS).

Fonctionnaires par catégorie A1/A2/A3/B/C/D, en milliers, 2015-2025. Barres empilées :
structure **et** évolution.

    from figures import categories_statutaires as cs
    cs.fig_structure()    # barres empilées par catégorie
    cs.structure_table()  # tableau (onglet Données)

DEUX PUBLICATIONS DE L'INS, RACCORDÉES : l'enquête 2010-2021 (tab8) pour 2015-2017, le
rapport 2018-2025 (tableau 6) ensuite. Les deux sont **identiques au dixième** sur
2018-2020, et ne diffèrent en 2021 que par l'arrondi (198,342 contre 198,3 milliers en
A1) : le raccord est sûr. Règle : le millésime le plus récent fait foi sur les années
communes. La table dit la source ligne à ligne.

RÉSERVE : la catégorie D passe de 28,4 milliers en 2023 à 39,8 en 2024, sans que la
source l'explique ; la même année, l'unité 1 des ouvriers recule de 48,9 à 35,4
milliers. Un reclassement d'ouvriers en catégorie D n'est qu'une hypothèse, que la
source ne formule pas. La table porte l'unité 1 des ouvriers en regard, pour que le
lecteur puisse faire le rapprochement lui-même.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "fonction-publique-categories"                  # enquête 2010-2021 (tab8)
SERIE_2025 = "fonction-publique-categories-2018-2025"   # rapport 2018-2025 (tableau 6)
SERIE_OUVRIERS = "fonction-publique-ouvriers-unite-2018-2025"  # tableau 7

# Première année que fournit le millésime le plus récent : il fait foi à partir d'elle.
_DEBUT_2025 = 2018
_UNITE1 = "Unité 1"

# ordre hiérarchique + couleurs (A = cadres → froids ; B/C/D → chauds/neutres)
_CATS = ["Catégorie A1", "Catégorie A2", "Catégorie A3",
         "Catégorie B", "Catégorie C", "Catégorie D"]
_SHORT = {"Catégorie A1": "A1", "Catégorie A2": "A2", "Catégorie A3": "A3",
          "Catégorie B": "B", "Catégorie C": "C", "Catégorie D": "D"}
_COLORS = {"A1": "#08519c", "A2": "#3182bd", "A3": "#9ecae1",
           "B": "#fd8d3c", "C": "#fdbe85", "D": "#969696"}

_L = {
    "title": {"fr": "Fonctionnaires de l’État par catégorie statutaire, 2015-2025",
              "ar": "موظفو الدولة حسب الصنف القانوني، 2015-2025"},
    "xlabel": {"fr": "Année", "ar": "السنة"},
    "ylabel": {"fr": "Effectifs (milliers d’agents)", "ar": "الأعداد (بآلاف الأعوان)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_source": {"fr": "Source", "ar": "المصدر"},
    "col_ouvriers": {"fr": "Ouvriers, unité 1 (pour comparaison)",
                     "ar": "العملة، الوحدة الأولى (للمقارنة)"},
    "src_2021": {"fr": "INS, enquête 2010-2021", "ar": "المعهد الوطني للإحصاء، مسح 2010-2021"},
    "src_2025": {"fr": "INS, rapport 2018-2025", "ar": "المعهد الوطني للإحصاء، تقرير 2018-2025"},
    "raccord": {"fr": "2015-2017 : enquête 2010-2021\n2018-2025 : rapport 2018-2025",
                "ar": "سنوات 2015-2017: مسح 2010-2021\nسنوات 2018-2025: تقرير 2018-2025"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _pivot(serie: str):
    df = figtools.series(serie)
    w = (df[df["categorie"].isin(_CATS)]
         .pivot(index="annee", columns="categorie", values="valeur")
         .reset_index())
    w.columns.name = None
    return w[["annee", *[c for c in _CATS if c in w.columns]]]


def _wide():
    """2015-2025 : enquête 2010-2021 jusqu'en 2017, rapport 2018-2025 ensuite."""
    import pandas as pd
    ancien = _pivot(SERIE)
    ancien = ancien[ancien["annee"] < _DEBUT_2025]
    w = pd.concat([ancien, _pivot(SERIE_2025)], ignore_index=True).sort_values("annee")
    w["annee"] = w["annee"].astype(int)
    return w.reset_index(drop=True)


def structure_table():
    """Tableau (onglet Données) : effectifs par catégorie statutaire (milliers), source,
    et l'unité 1 des ouvriers en regard (2018-2025)."""
    w = _wide()
    ouv = figtools.series(SERIE_OUVRIERS)
    ouv = {int(r.annee): float(r.valeur) for r in ouv.itertuples()
           if str(r.categorie).strip() == _UNITE1}
    w["ouvriers"] = [ouv.get(a) for a in w["annee"]]
    w["source"] = [_lab("src_2025") if a >= _DEBUT_2025 else _lab("src_2021")
                   for a in w["annee"]]
    return w.rename(columns={"annee": _lab("col_annee"),
                             **{c: _SHORT[c] for c in _CATS},
                             "ouvriers": _lab("col_ouvriers"),
                             "source": _lab("col_source")})


def fig_structure():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    w = _wide()
    y = w["annee"].astype(int).astype(str)
    fig, ax = plt.subplots(figsize=(9.5, 5))
    bottom = [0.0] * len(w)
    for cat in _CATS:
        if cat not in w.columns:
            continue
        s = _SHORT[cat]
        ax.bar(y, w[cat], bottom=bottom, color=_COLORS[s], label=s, width=0.7)
        bottom = [b + v for b, v in zip(bottom, w[cat].fillna(0))]
    # jonction des deux publications (raccord sûr : identiques sur 2018-2020)
    i = list(w["annee"]).index(_DEBUT_2025)
    ax.axvline(i - 0.5, color="#57606a", lw=0.8, ls=":")
    ax.annotate("\n".join(ft(line) for line in _lab("raccord").split("\n")),
                xy=(i - 0.45, 0.965), xycoords=("data", "axes fraction"),
                fontsize=7, color="#57606a", ha="left", va="top")
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_ylabel(ft(_lab("ylabel")))
    ax.set_title(ft(_lab("title")))
    ax.set_ylim(0, max(bottom) * 1.12)
    ax.grid(True, axis="y", alpha=0.3)
    # légende : ordre hiérarchique, en dehors à droite (codes universels A1..D)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, title="", loc="upper left",
              bbox_to_anchor=(1.01, 1.0), fontsize=9)
    fig.tight_layout()
    return fig

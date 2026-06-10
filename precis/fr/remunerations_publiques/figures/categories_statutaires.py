"""Figure « structure des fonctionnaires par catégorie statutaire » (source INS).

Série tab8 de l'enquête INS (fonctionnaires de l'État par catégorie A1/A2/A3/
B/C/D, 2015-2021, en milliers). Barres empilées : structure **et** évolution.

    from figures import categories_statutaires as cs
    cs.fig_structure()    # barres empilées par catégorie
    cs.structure_table()  # tableau (onglet Données)
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "fonction-publique-categories"

# ordre hiérarchique + couleurs (A = cadres → froids ; B/C/D → chauds/neutres)
_CATS = ["Catégorie A1", "Catégorie A2", "Catégorie A3",
         "Catégorie B", "Catégorie C", "Catégorie D"]
_SHORT = {"Catégorie A1": "A1", "Catégorie A2": "A2", "Catégorie A3": "A3",
          "Catégorie B": "B", "Catégorie C": "C", "Catégorie D": "D"}
_COLORS = {"A1": "#08519c", "A2": "#3182bd", "A3": "#9ecae1",
           "B": "#fd8d3c", "C": "#fdbe85", "D": "#969696"}

_L = {
    "title": {"fr": "Fonctionnaires de l’État par catégorie statutaire, 2015-2021",
              "ar": "موظفو الدولة حسب الصنف القانوني، 2015-2021"},
    "xlabel": {"fr": "Année", "ar": "السنة"},
    "ylabel": {"fr": "Effectifs (milliers d’agents)", "ar": "الأعداد (بآلاف الأعوان)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _wide():
    df = figtools.series(SERIE)
    w = (df[df["categorie"].isin(_CATS)]
         .pivot(index="annee", columns="categorie", values="valeur")
         .reset_index())
    w.columns.name = None
    return w[["annee", *[c for c in _CATS if c in w.columns]]]


def structure_table():
    """Tableau (onglet Données) : effectifs par catégorie statutaire (milliers)."""
    w = _wide()
    return w.rename(columns={"annee": _lab("col_annee"),
                             **{c: _SHORT[c] for c in _CATS}})


def fig_structure():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    w = _wide()
    y = w["annee"].astype(int).astype(str)
    fig, ax = plt.subplots(figsize=(9, 5))
    bottom = [0.0] * len(w)
    for cat in _CATS:
        if cat not in w.columns:
            continue
        s = _SHORT[cat]
        ax.bar(y, w[cat], bottom=bottom, color=_COLORS[s], label=s, width=0.7)
        bottom = [b + v for b, v in zip(bottom, w[cat].fillna(0))]
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_ylabel(ft(_lab("ylabel")))
    ax.set_title(ft(_lab("title")))
    ax.grid(True, axis="y", alpha=0.3)
    # légende : ordre hiérarchique, en dehors à droite (codes universels A1..D)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, title="", loc="upper left",
              bbox_to_anchor=(1.01, 1.0), fontsize=9)
    fig.tight_layout()
    return fig

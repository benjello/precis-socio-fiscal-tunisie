"""Figures du livre *L'environnement* — chapitre « La dépollution et les fonds ».

    from figures import environnement as env
    env.vues_fodep()      ; env.table_fodep()       # fonds de dépollution (FODEP)
    env.vues_esthetique() ; env.table_esthetique()  # fonds de la protection et de
                                                     # l'esthétique de l'environnement

D'OÙ VIENNENT LES DONNÉES. Deux séries du cache du précis donnent, pour chaque fonds et
chaque année, la prévision de recettes et de dépenses inscrite au tableau des fonds spéciaux
du Trésor de la loi de finances de l'année — un montant VOTÉ, équilibré entre recette et
dépense, et non un décaissement réalisé :

  - `env-fodep-previsions` : fonds de dépollution (FODEP), lois de finances 2011-2020 ;
  - `env-esthetique-previsions` : fonds de la protection et de l'esthétique de
    l'environnement, lois de finances 2014-2020.

LE DÉNOMINATEUR. La seconde vue rapporte la prévision du fonds à la dépense de l'État, pour
situer le poids du fonds. Le dénominateur est la dépense RÉALISÉE de l'État hors service de
la dette (série `budget-vote-realise`, lignes `realise`, colonne `total_hors_dette_MDT`),
seule base qui couvre toutes les années de 2011 à 2020. Numérateur voté et dénominateur
réalisé ne se confondent pas : la part est indicative du poids du fonds dans la dépense de
l'État, non un ratio d'exécution. Aucun montant n'est déflaté.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_FODEP = "env-fodep-previsions"
SERIE_ESTHETIQUE = "env-esthetique-previsions"
SERIE_DEPENSES = "budget-vote-realise"

BLEU, GRIS = "#0969da", "#57606a"

# Textes des figures, par langue (le chrome d'interface est, lui, dans figtools).
_L = {
    "fr": {
        "vue_md": "Montant (millions de dinars)",
        "vue_part": "Part de la dépense de l'État (%)",
        "y_md": "Prévision (millions de dinars courants)",
        "y_part": "Part de la dépense de l'État (%)",
        "x": "Année (loi de finances)",
        "t_fodep": "Fonds de dépollution : prévision des lois de finances",
        "t_esthetique": ("Fonds de la protection et de l'esthétique de l'environnement : "
                         "prévision des lois de finances"),
        "col_annee": "Année (loi de finances)",
        "col_md": "Prévision\n(millions de dinars)",
        "col_part": "Part de la dépense\nde l'État (%)",
    },
    "ar": {
        "vue_md": "المبلغ (بملايين الدنانير)",
        "vue_part": "نسبة من نفقات الدولة (%)",
        "y_md": "التقدير (بملايين الدنانير الجارية)",
        "y_part": "نسبة من نفقات الدولة (%)",
        "x": "السنة (قانون المالية)",
        "t_fodep": "صندوق إزالة التلوّث: تقديرات قوانين المالية",
        "t_esthetique": "صندوق حماية البيئة وتجميلها: تقديرات قوانين المالية",
        "col_annee": "السنة (قانون المالية)",
        "col_md": "التقدير\n(بملايين الدنانير)",
        "col_part": "نسبة من نفقات\nالدولة (%)",
    },
}

figtools.register_provenance(
    SERIE_FODEP,
    titre=("Fonds de dépollution : prévision de recettes et de dépenses inscrite aux lois "
           "de finances, 2011-2020 (tableau des fonds spéciaux du Trésor)"),
    titre_ar="صندوق إزالة التلوّث: تقديرات المقابيض والمصاريف في قوانين المالية، 2011-2020",
    sources=["lf-1993", "decret-93-2120", "lf-2013"],
    unite="millions de dinars courants",
    unite_ar="بملايين الدنانير الجارية",
    perimetre=("montant du fonds de dépollution au tableau des prévisions de recettes et de "
               "dépenses des fonds spéciaux du Trésor des lois de finances, 2011-2020 ; "
               "montant voté, équilibré entre recette et dépense"),
    perimetre_ar=("مبلغ صندوق إزالة التلوّث في جدول تقديرات مقابيض ومصاريف الحسابات الخاصة "
                  "في الخزينة، 2011-2020"),
    caveats=("Prévisions votées, et non des décaissements réalisés. Les primes effectivement "
             "versées par le fonds ne figurent pas dans les lois de finances."),
    caveats_ar=("تقديرات مصادق عليها، وليست مصاريف منجزة؛ المنح المدفوعة فعليًّا من الصندوق "
                "لا تَرِد في قوانين المالية."),
)

figtools.register_provenance(
    SERIE_ESTHETIQUE,
    titre=("Fonds de la protection et de l'esthétique de l'environnement : prévision de "
           "recettes et de dépenses inscrite aux lois de finances, 2014-2020"),
    titre_ar=("صندوق حماية البيئة وتجميلها: تقديرات المقابيض والمصاريف في قوانين المالية، "
              "2014-2020"),
    sources=["lf-2004", "lf-2005", "lf-2013"],
    unite="millions de dinars courants",
    unite_ar="بملايين الدنانير الجارية",
    perimetre=("montant du fonds de la protection et de l'esthétique de l'environnement au "
               "tableau des fonds spéciaux du Trésor des lois de finances, 2014-2020 ; "
               "montant voté, équilibré entre recette et dépense"),
    perimetre_ar=("مبلغ صندوق حماية البيئة وتجميلها في جدول الحسابات الخاصة في الخزينة، "
                  "2014-2020"),
    caveats=("Prévisions votées, et non des décaissements réalisés ; les dépenses réalisées "
             "du fonds ne figurent pas dans les lois de finances."),
    caveats_ar=("تقديرات مصادق عليها، وليست مصاريف منجزة؛ المصاريف المنجزة للصندوق لا تَرِد "
                "في قوانين المالية."),
)


def _l(cle: str) -> str:
    return _L.get(figtools.lang(), _L["fr"])[cle]


def _previsions(serie: str) -> dict[int, float]:
    d = figtools.series(serie)
    return {int(r.annee): float(r.prevision_MDT) for r in d.itertuples(index=False)}


def _depense_etat() -> dict[int, float]:
    """Dépense réalisée de l'État hors service de la dette, par année (MDT)."""
    d = figtools.series(SERIE_DEPENSES)
    d = d[d["etat"].astype(str) == "realise"]
    return {int(r.annee): float(r.total_hors_dette_MDT) for r in d.itertuples(index=False)}


def _parts(serie: str) -> dict[int, float]:
    prev = _previsions(serie)
    dep = _depense_etat()
    return {a: 100 * v / dep[a] for a, v in prev.items() if a in dep}


def _nombre(v: float, dec: int = 1) -> str:
    return f"{v:.{dec}f}".replace(".", ",")


def _barres(points: dict[int, float], titre: str, ylabel: str, dec: int) -> plt.Figure:
    figtools.apply_lang_font()
    annees = sorted(points)
    fig, ax = plt.subplots(figsize=(8.5, 4.6))
    barres = ax.bar(annees, [points[a] for a in annees], color=BLEU, width=0.68)
    for a, b in zip(annees, barres):
        figtools.infobulle(b, f"{a} · {_nombre(points[a], dec)}")
        ax.annotate(_nombre(points[a], dec), xy=(a, points[a]),
                    xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom", fontsize=7.5, color=GRIS)
    ax.set_title(figtools.fig_text(titre), fontsize=10.5)
    ax.set_xlabel(figtools.fig_text(_l("x")), fontsize=9)
    ax.set_ylabel(figtools.fig_text(ylabel), fontsize=9)
    ax.set_xticks(annees)
    ax.set_xticklabels([str(a) for a in annees], rotation=45, fontsize=8)
    ax.set_ylim(0, max(points.values()) * 1.18)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(axis="y", labelsize=8)
    fig.tight_layout()
    return fig


def _table(serie: str) -> "object":
    import pandas as pd
    prev = _previsions(serie)
    parts = _parts(serie)
    rows = [{_l("col_annee"): a,
             _l("col_md"): round(prev[a], 1),
             _l("col_part"): None if a not in parts else round(parts[a], 3)}
            for a in sorted(prev)]
    return pd.DataFrame(rows)


def vues_fodep():
    return [(_l("vue_md"), _barres(_previsions(SERIE_FODEP), _l("t_fodep"), _l("y_md"), 0)),
            (_l("vue_part"), _barres(_parts(SERIE_FODEP), _l("t_fodep"), _l("y_part"), 3))]


def table_fodep():
    return _table(SERIE_FODEP)


def vues_esthetique():
    return [(_l("vue_md"),
             _barres(_previsions(SERIE_ESTHETIQUE), _l("t_esthetique"), _l("y_md"), 0)),
            (_l("vue_part"),
             _barres(_parts(SERIE_ESTHETIQUE), _l("t_esthetique"), _l("y_part"), 3))]


def table_esthetique():
    return _table(SERIE_ESTHETIQUE)

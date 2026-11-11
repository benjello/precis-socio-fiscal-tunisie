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
SERIE_TRANSFERTS = "env-transferts-etablissements"

BLEU, GRIS = "#0969da", "#57606a"

# Établissements sous tutelle, dans l'ordre de pile (l'Office de l'assainissement en bas),
# avec leur libellé bilingue et une couleur sobre par établissement.
_ETABS = [
    ("onas", "Office national de l'assainissement",
     "الديوان الوطني للتطهير", "#0b4f6c"),
    ("anged", "Agence nationale de gestion des déchets",
     "الوكالة الوطنية للتصرّف في النفايات", "#2d8c6f"),
    ("anpe", "Agence nationale de protection de l'environnement",
     "الوكالة الوطنية لحماية المحيط", "#5a7fb5"),
    ("apal", "Agence de protection et d'aménagement du littoral",
     "وكالة حماية وتهيئة الشريط الساحلي", "#c08a3e"),
    ("citet", "Centre international des technologies de l'environnement de Tunis",
     "المركز الدولي لتكنولوجيات البيئة بتونس", "#9aa0a6"),
]

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
        "vue_transferts": "Transferts (millions de dinars)",
        "t_transferts": ("Transferts de l'État aux établissements sous tutelle du "
                         "ministère chargé de l'environnement"),
        "y_transferts": "Transfert (millions de dinars courants)",
        "x_annee": "Année",
        "col_etab": "Établissement",
        "col_total": "Total du ministère",
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
        "vue_transferts": "التحويلات (بملايين الدنانير)",
        "t_transferts": "تحويلات الدولة إلى المؤسسات الخاضعة لإشراف الوزارة المكلّفة بالبيئة",
        "y_transferts": "التحويل (بملايين الدنانير الجارية)",
        "x_annee": "السنة",
        "col_etab": "المؤسسة",
        "col_total": "جملة الوزارة",
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

figtools.register_provenance(
    SERIE_TRANSFERTS,
    titre=("Transferts du budget de l'État aux établissements sous tutelle du ministère "
           "chargé de l'environnement, par établissement, 2020-2025"),
    titre_ar=("تحويلات ميزانية الدولة إلى المؤسسات الخاضعة لإشراف الوزارة المكلّفة "
              "بالبيئة، حسب المؤسسة، 2020-2025"),
    sources=["minfin-transferts-garanties"],
    unite="millions de dinars",
    unite_ar="بملايين الدنانير",
    perimetre=("transferts du budget de l'État aux cinq établissements sous tutelle du "
               "ministère chargé de l'environnement, au rapport sur les transferts et les "
               "garanties au profit des entreprises et établissements publics annexé aux "
               "lois de finances, 2020-2025"),
    perimetre_ar=("تحويلات ميزانية الدولة إلى المؤسسات الخمس الخاضعة لإشراف الوزارة "
                  "المكلّفة بالبيئة، 2020-2025"),
    caveats=("2020-2024 réalisations, 2025 loi de finances ; le réalisé dépasse souvent le "
             "voté ; le transfert à l'Agence des déchets est intermittent (composante "
             "d'investissement)."),
    caveats_ar=("2020-2024 إنجازات، 2025 قانون المالية ; المنجز يفوق غالبًا المصادق "
                "عليه ; التحويل إلى وكالة النفايات متقطّع (مكوّن استثماري)."),
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


def _transferts() -> "object":
    """Données longues des transferts (annee, etablissement, montant_MDT)."""
    return figtools.series(SERIE_TRANSFERTS)


def _barres_empilees() -> plt.Figure:
    figtools.apply_lang_font()
    d = _transferts()
    annees = sorted({int(a) for a in d["annee"]})
    x = list(range(len(annees)))
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    bas = [0.0] * len(annees)
    for cle, lib_fr, lib_ar, couleur in _ETABS:
        sous = d[d["etablissement"] == cle]
        par_an = {int(r.annee): float(r.montant_MDT) for r in sous.itertuples(index=False)}
        vals = [par_an.get(a, 0.0) for a in annees]
        lib = lib_ar if figtools.lang() == "ar" else lib_fr
        barres = ax.bar(x, vals, bottom=bas, width=0.66, color=couleur,
                        label=figtools.fig_text(lib))
        for xi, a, b, v in zip(x, annees, barres, vals):
            if v > 0:
                figtools.infobulle(b, f"{a} · {lib} · {_nombre(v, 1)}")
        bas = [b + v for b, v in zip(bas, vals)]
    for xi, a, tot in zip(x, annees, bas):
        ax.annotate(_nombre(tot, 1), xy=(xi, tot), xytext=(0, 3),
                    textcoords="offset points", ha="center", va="bottom",
                    fontsize=7.5, color=GRIS)
    ax.set_title(figtools.fig_text(_l("t_transferts")), fontsize=10.5)
    ax.set_xlabel(figtools.fig_text(_l("x_annee")), fontsize=9)
    ax.set_ylabel(figtools.fig_text(_l("y_transferts")), fontsize=9)
    ax.set_xticks(x)
    ax.set_xticklabels([str(a) for a in annees], fontsize=8)
    ax.set_ylim(0, max(bas) * 1.16)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(axis="y", labelsize=8)
    ax.legend(fontsize=7.5, loc="upper left", framealpha=0.9)
    fig.tight_layout()
    return fig


def vues_transferts():
    return [(_l("vue_transferts"), _barres_empilees())]


def table_transferts():
    import pandas as pd
    d = _transferts()
    annees = sorted({int(a) for a in d["annee"]})
    rows = []
    totaux = {a: 0.0 for a in annees}
    for cle, lib_fr, lib_ar, _ in _ETABS:
        sous = d[d["etablissement"] == cle]
        par_an = {int(r.annee): float(r.montant_MDT) for r in sous.itertuples(index=False)}
        lib = lib_ar if figtools.lang() == "ar" else lib_fr
        row = {_l("col_etab"): lib}
        for a in annees:
            v = par_an.get(a, 0.0)
            row[str(a)] = round(v, 1)
            totaux[a] += v
        rows.append(row)
    total_row = {_l("col_etab"): _l("col_total")}
    for a in annees:
        total_row[str(a)] = round(totaux[a], 1)
    rows.append(total_row)
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

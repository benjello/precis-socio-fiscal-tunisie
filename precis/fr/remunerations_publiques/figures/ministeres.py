"""Figure « ventilation des effectifs de la fonction publique par ministère » (INS).

Série tab11 de l'enquête INS : quatorze entités — onze ministères, la Présidence du
gouvernement, les collectivités locales et les autres établissements — de 2015 à 2021,
en milliers d'agents.

    from figures import ministeres as mi
    mi.fig_ministeres()     # les plus gros effectifs, en courbes
    mi.ministeres_table()   # les quatorze entités (onglet Données)

POURQUOI SEPT COURBES ET NON QUATORZE : l'Éducation pèse 196,7 milliers contre 2,3 à la
Présidence du gouvernement. Tracées ensemble, les petites entités s'écrasent sur l'axe et
la figure devient illisible. On trace donc les cinq premiers ministères, le poste « autres
établissements » et les collectivités locales ; les quatorze sont dans l'onglet Données.

RÉSERVES PORTÉES PAR LA FIGURE ELLE-MÊME :
  - les **collectivités locales** connaissent une rupture de périmètre entre 2016 et 2017
    (6,7 → 17,7 milliers) : tracées en pointillé, la rupture signalée par une bande ;
  - la colonne **2021** de la source porte trois décimales là où 2015-2020 n'en portent
    qu'une : les petits mouvements 2020→2021 sont des artefacts d'arrondi, non des
    évolutions réelles.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "ins-ministere-effectifs"

# Les quatorze entités, dans l'ordre de la source. Le libellé français est celui du CSV ;
# l'arabe est repris VERBATIM de la colonne A de l'INS, à une exception : la source écrit
# « الجماعت المحلية » dans tab11 (coquille) et « الجماعات المحلية » dans tab25 — on retient
# la forme correcte plutôt que de propager la coquille dans le texte rendu.
_ENTITES = [
    ("Présidence du gouvernement", "رئاسة الحكومة"),
    ("Ministère de la défense", "وزارة الدفاع"),
    ("Ministère de l'intérieur", "وزارة الداخلية"),
    ("Ministère de la justice", "وزارة العدل"),
    ("Ministère des finances", "وزارة المالية"),
    ("Ministère de l'agriculture", "وزارة الفلاحة"),
    ("Ministère de l'équipement", "وزارة التجهيز"),
    ("Ministère de la jeunesse et des sports", "وزارة شؤون الشباب والرياضة"),
    ("Ministère de la santé", "وزارة الصحة"),
    ("Ministère de l'éducation", "وزارة التربية"),
    ("Ministère de l'enseignement supérieur", "وزارة التعليم العالي"),
    ("Ministère des affaires sociales", "وزارة الشؤون الاجتماعية"),
    ("Collectivités locales", "الجماعات المحلية"),
    ("Autres établissements", "هياكل أخرى"),
]
_AR = dict(_ENTITES)
_ORDRE = [fr for fr, _ in _ENTITES]

# Les entités tracées : les cinq premiers ministères en effectifs, puis le poste résiduel
# et les collectivités locales, qui portent la rupture de périmètre.
_TRACEES = [
    "Ministère de l'éducation",
    "Ministère de l'intérieur",
    "Ministère de la défense",
    "Ministère de la santé",
    "Ministère de l'enseignement supérieur",
    "Autres établissements",
]
_LOCALES = "Collectivités locales"

# Le gris est réservé au poste RÉSIDUEL « autres établissements » — il n'est pas un
# ministère, et la teinte neutre le dit. Chaque ministère porte une couleur franche :
# deux gris voisins rendaient indiscernables la Défense et le résidu, qui se croisent
# précisément en 2017-2018.
_COULEURS = {
    "Ministère de l'éducation": "#08519c",
    "Ministère de l'intérieur": "#1f6feb",
    "Ministère de la défense": "#117a65",
    "Ministère de la santé": "#d1242f",
    "Ministère de l'enseignement supérieur": "#8957e5",
    "Autres établissements": "#57606a",
}

_L = {
    "title": {"fr": "Effectifs de la fonction publique par ministère, 2015-2021",
              "ar": "أعداد أعوان الوظيفة العمومية حسب الوزارة، 2015-2021"},
    "xlabel": {"fr": "Année", "ar": "السنة"},
    "ylabel": {"fr": "Effectifs (milliers d’agents)", "ar": "الأعداد (بآلاف الأعوان)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "lg_locales": {"fr": "Collectivités locales (rupture de périmètre)",
                   "ar": "الجماعات المحلية (انقطاع في النطاق)"},
    "rupture": {"fr": "rupture de série :\nchangement de périmètre\ndes collectivités locales",
                "ar": "انقطاع السلسلة:\nتغيّر نطاق\nالجماعات المحلية"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _nom(fr: str) -> str:
    """Libellé d'entité dans la langue du livre."""
    return _AR[fr] if figtools.lang() == "ar" else fr


def _wide():
    """Série longue → large (annee × ministère), dans l'ordre de la source."""
    df = figtools.series(SERIE)
    w = (df.pivot(index="annee", columns="ministere", values="valeur")
         .reset_index())
    w.columns.name = None
    return w[["annee", *[c for c in _ORDRE if c in w.columns]]]


def ministeres_table():
    """Tableau (onglet Données) : les quatorze entités, milliers d'agents."""
    w = _wide()
    return w.rename(columns={"annee": _lab("col_annee"),
                             **{fr: _nom(fr) for fr in _ORDRE}})


def fig_ministeres():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    w = _wide()
    y = w["annee"]
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for fr in _TRACEES:
        if fr not in w.columns:
            continue
        ax.plot(y, w[fr], "o-", color=_COULEURS[fr], lw=2, ms=4, label=ft(_nom(fr)))
    if _LOCALES in w.columns:
        ax.plot(y, w[_LOCALES], "^--", color="#bf8700", lw=1.6, ms=4,
                label=ft(_lab("lg_locales")))
        # repère de la rupture de périmètre 2016→2017, comme sur la figure d'ouverture
        ax.axvspan(2016, 2017, color="#bf8700", alpha=0.08)
        # L'annotation se place dans la bande VIDE entre l'Intérieur et l'Éducation :
        # l'ordonnée est donnée en fraction d'axe, non en milliers d'agents, pour qu'elle
        # ne retombe pas sur une courbe si les effectifs changent. Ancrée par le calcul,
        # la note tombait auparavant sur le croisement Défense / autres établissements.
        ax.annotate("\n".join(ft(line) for line in _lab("rupture").split("\n")),
                    xy=(2016.5, 0.72), xycoords=("data", "axes fraction"),
                    fontsize=8, color="#7a5b00", ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.35", fc="#fff8e5",
                              ec="#bf8700", lw=0.6, alpha=0.9))
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_ylabel(ft(_lab("ylabel")))
    ax.set_title(ft(_lab("title")))
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=8.5)
    fig.tight_layout()
    return fig

"""Figure « ventilation des effectifs de la fonction publique par ministère » (INS).

Quatorze entités — onze ministères, la Présidence du gouvernement, les collectivités
locales et les autres établissements —, dans DEUX PUBLICATIONS DE L'INS QUI NE SE
RACCORDENT PAS :

  - `ins-ministere-effectifs` — enquête 2010-2021, tab11 : 2015-2021, en milliers ;
  - `ins-ministere-effectifs-2018-2025` — rapport 2018-2025, tableau 8 : 2018-2025, en
    agents (ramenés ici en milliers, sans arrondi).

Sur les années communes (2018-2021), le rapport 2018-2025 RÉVISE la répartition à total
inchangé : environ 9 000 agents passent des « autres établissements » au ministère de
l'intérieur (2018 : 87,3 → 96,3 milliers pour l'Intérieur, 55,6 → 46,9 pour les autres
établissements), avec des déplacements plus petits pour la Présidence du gouvernement, la
Justice, les Finances et la Santé. La source n'explique pas ce reclassement. Les deux
séries sont donc tracées l'une et l'autre, en tirets (2015-2021) et en trait plein
(2018-2025), et leur chevauchement montre la révision au lieu de la masquer — jamais un
raccord silencieux.

    from figures import ministeres as mi
    mi.fig_ministeres()     # les plus gros effectifs, en courbes
    mi.ministeres_table()   # les quatorze entités, les deux publications (onglet Données)

POURQUOI SEPT ENTITÉS ET NON QUATORZE : l'Éducation compte près de 200 milliers
d'agents, la Présidence du gouvernement moins de 2. Tracées ensemble, les petites entités
s'écrasent sur l'axe. On trace donc les cinq premiers ministères, le poste « autres
établissements » et les collectivités locales ; les quatorze sont dans l'onglet Données.

RÉSERVES PORTÉES PAR LA FIGURE ELLE-MÊME :
  - les **collectivités locales** connaissent une rupture de périmètre entre 2016 et 2017
    (6,7 → 17,7 milliers), signalée par une bande, puis une couverture croissante dans
    la base administrative à partir de 2018, que le rapport 2018-2025 signale lui-même ;
  - dans l'enquête 2010-2021, la colonne **2021** porte trois décimales là où 2015-2020
    n'en portent qu'une : les petits mouvements 2020→2021 de la série en tirets sont des
    artefacts d'arrondi.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "ins-ministere-effectifs"                 # enquête 2010-2021, milliers
SERIE_2025 = "ins-ministere-effectifs-2018-2025"  # rapport 2018-2025, agents

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
    "title": {"fr": "Effectifs de la fonction publique par ministère, 2015-2025",
              "ar": "أعداد أعوان الوظيفة العمومية حسب الوزارة، 2015-2025"},
    "xlabel": {"fr": "Année", "ar": "السنة"},
    "ylabel": {"fr": "Effectifs (milliers d’agents)", "ar": "الأعداد (بآلاف الأعوان)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_source": {"fr": "Source", "ar": "المصدر"},
    "src_2021": {"fr": "INS, enquête 2010-2021", "ar": "المعهد الوطني للإحصاء، مسح 2010-2021"},
    "src_2025": {"fr": "INS, rapport 2018-2025", "ar": "المعهد الوطني للإحصاء، تقرير 2018-2025"},
    "lg_locales": {"fr": "Collectivités locales (rupture de périmètre)",
                   "ar": "الجماعات المحلية (انقطاع في النطاق)"},
    "lg_2025": {"fr": "trait plein : rapport 2018-2025",
                "ar": "خطّ متّصل: تقرير 2018-2025"},
    "lg_2021": {"fr": "tirets : enquête 2010-2021 (répartition révisée depuis)",
                "ar": "خطّ متقطّع: مسح 2010-2021 (توزيع رُوجع لاحقاً)"},
    "rupture": {"fr": "rupture de série :\nchangement de périmètre\ndes collectivités locales",
                "ar": "انقطاع السلسلة:\nتغيّر نطاق\nالجماعات المحلية"},
    "revision": {"fr": "même total, autre répartition :\n~9 000 agents passent des autres\n"
                       "établissements à l’Intérieur",
                 "ar": "المجموع نفسه وتوزيع آخر:\nنحو 9 000 عون ينتقلون من الهياكل\n"
                       "الأخرى إلى الداخلية"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _nom(fr: str) -> str:
    """Libellé d'entité dans la langue du livre."""
    return _AR[fr] if figtools.lang() == "ar" else fr


def _wide(serie: str = SERIE, diviseur: float = 1.0):
    """Série longue → large (annee × ministère), dans l'ordre de la source, en milliers."""
    df = figtools.series(serie)
    w = (df.pivot(index="annee", columns="ministere", values="valeur")
         .reset_index())
    w.columns.name = None
    w = w[["annee", *[c for c in _ORDRE if c in w.columns]]]
    for c in _ORDRE:
        if c in w.columns:
            w[c] = w[c] / diviseur
    w["annee"] = w["annee"].astype(int)
    return w


def _wide_2025():
    """Rapport 2018-2025, ramené des agents aux milliers (trois décimales exactes)."""
    return _wide(SERIE_2025, 1000.0)


def ministeres_table():
    """Tableau (onglet Données) : les quatorze entités, milliers d'agents, les DEUX
    publications l'une sous l'autre — 2018-2021 y figurent deux fois, c'est voulu."""
    import pandas as pd
    a, r = _wide(), _wide_2025()
    a.insert(1, "source", _lab("src_2021"))
    r.insert(1, "source", _lab("src_2025"))
    t = pd.concat([a, r], ignore_index=True)
    t[_ORDRE] = t[_ORDRE].round(3)
    return t.rename(columns={"annee": _lab("col_annee"), "source": _lab("col_source"),
                             **{fr: _nom(fr) for fr in _ORDRE}})


def fig_ministeres():
    from matplotlib.lines import Line2D
    figtools.apply_lang_font()
    ft = figtools.fig_text
    a, r = _wide(), _wide_2025()
    fig, ax = plt.subplots(figsize=(10, 5.8))
    for fr in _TRACEES:
        c = _COULEURS[fr]
        if fr in a.columns:
            ax.plot(a["annee"], a[fr], "o--", color=c, lw=1.1, ms=2.5, alpha=0.6)
        if fr in r.columns:
            ax.plot(r["annee"], r[fr], "o-", color=c, lw=2, ms=4, label=ft(_nom(fr)))
    if _LOCALES in a.columns:
        ax.plot(a["annee"], a[_LOCALES], "^--", color="#bf8700", lw=1.1, ms=2.5, alpha=0.6)
        ax.plot(r["annee"], r[_LOCALES], "^-", color="#bf8700", lw=1.6, ms=4,
                label=ft(_lab("lg_locales")))
        # repère de la rupture de périmètre 2016→2017, comme sur la figure d'ouverture
        ax.axvspan(2016, 2017, color="#bf8700", alpha=0.08)
        # Ordonnée en fraction d'axe, dans la bande vide entre l'Intérieur et l'Éducation,
        # pour que la note ne retombe pas sur une courbe si les effectifs changent.
        ax.annotate("\n".join(ft(line) for line in _lab("rupture").split("\n")),
                    xy=(2016.5, 0.72), xycoords=("data", "axes fraction"),
                    fontsize=8, color="#7a5b00", ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.35", fc="#fff8e5",
                              ec="#bf8700", lw=0.6, alpha=0.9))
    # la révision de 2018-2021, là où les deux publications se chevauchent : une flèche
    # vers chacun des deux écarts, pris à mi-hauteur entre l'ancienne et la nouvelle valeur
    texte = "\n".join(ft(line) for line in _lab("revision").split("\n"))
    boite = dict(boxstyle="round,pad=0.35", fc="#f0f6ff", ec="#1f6feb", lw=0.6, alpha=0.9)
    for k, fr in enumerate(("Autres établissements", "Ministère de l'intérieur")):
        x = 2020
        if x not in set(a["annee"]) or x not in set(r["annee"]):
            continue
        y_mid = (float(a.loc[a["annee"] == x, fr].iloc[0])
                 + float(r.loc[r["annee"] == x, fr].iloc[0])) / 2
        ax.annotate(texte if k == 1 else "", xy=(x, y_mid),
                    xytext=(2019.5, 0.60), textcoords=("data", "axes fraction"),
                    fontsize=7.5, color="#1f3b73", ha="center", va="center",
                    bbox=boite if k == 1 else None,
                    arrowprops=dict(arrowstyle="->", color="#1f6feb", lw=0.7,
                                    shrinkA=4, shrinkB=2))
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_ylabel(ft(_lab("ylabel")))
    ax.set_title(ft(_lab("title")))
    ax.set_ylim(bottom=0)
    ax.set_xticks(list(range(int(a["annee"].min()), int(r["annee"].max()) + 1)))
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    handles += [Line2D([], [], color="#57606a", lw=2, ls="-"),
                Line2D([], [], color="#57606a", lw=1.1, ls="--", alpha=0.6)]
    labels += [ft(_lab("lg_2025")), ft(_lab("lg_2021"))]
    ax.legend(handles, labels, loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=8.5)
    fig.tight_layout()
    return fig

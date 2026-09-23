"""Figures « effectifs et salaires de la fonction publique » (source INS).

Frontière : les séries viennent de `tunisia_data` (entrepôt, ou snapshot du précis) ;
ici on prépare le figdata sourcé et on rend les figures.

    from figures import effectifs_fonction_publique as efp
    efp.fig_effectifs()   # figure d'ouverture : effectifs FP 2015-2025
    efp.fig_salaire()     # salaire mensuel moyen 2015-2025 (trois indicateurs)

DEUX PUBLICATIONS DE L'INS, RACCORDÉES SUR LES EFFECTIFS. L'enquête « Caractéristiques
des agents de la fonction publique et leurs salaires 2010-2021 » (tab1, en milliers)
couvre 2015-2021 ; le rapport « Évolution des effectifs et des rémunérations… 2018-2025 »
(tableau 1, en agents) couvre 2018-2025. Sur les quatre années communes, les deux
concordent à l'arrondi du millier près (669 290 agents en 2021 dans l'un et l'autre) :
le raccord est sûr. Règle : le millésime le plus récent fait foi sur les années communes,
l'enquête 2010-2021 ne fournit que 2015-2017. La table dit la source ligne à ligne.

RÉSERVES PORTÉES PAR LA FIGURE :
  - rupture de périmètre des collectivités locales entre 2016 et 2017 (6,7 → 17,7
    milliers), signalée par une bande ;
  - couverture croissante des collectivités locales dans la base administrative INSAF
    depuis 2018, que le rapport 2018-2025 signale lui-même (p. 4) : la hausse de 21 483
    à 27 697 agents (2018-2022) mêle recrutements et extension du champ.

La tendance se lit donc sur la série **hors collectivités locales**.

Salaire moyen : série raccordée `fonction-publique-salaires-2015-2025` (tab18 pour
2015-2017, tableau 10 du rapport 2018-2025 ensuite). Les deux publications diffèrent
d'environ un dinar sur 2018-2020 (et de 3 dinars sur le net 2018, que le nouveau
millésime rectifie) ; chaque indicateur n'est raccordé qu'à lui-même.
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

SERIE_EFF = "fonction-publique-effectifs"                 # enquête 2010-2021, milliers
SERIE_EFF_2025 = "fonction-publique-effectifs-2018-2025"  # rapport 2018-2025, agents
SERIE_SAL = "fonction-publique-salaires-2015-2025"        # série raccordée des niveaux

# Première année que fournit le millésime le plus récent : il fait foi à partir d'elle.
_DEBUT_2025 = 2018

_HORS = "Nombre d’agents hors Collectivités Locales"
_LOC = "Nombre d’agents des Collectivités Locales"
_TOT = "Total"

_BRUT_AVEC = "Salaire mensuel brut avec contributions"
_BRUT_SANS = "Salaire mensuel brut sans contributions"
_NET = "Salaire mensuel net"


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
    "col_source": {"fr": "Source", "ar": "المصدر"},
    "src_2021":  {"fr": "INS, enquête 2010-2021", "ar": "المعهد الوطني للإحصاء، مسح 2010-2021"},
    "src_2025":  {"fr": "INS, rapport 2018-2025", "ar": "المعهد الوطني للإحصاء، تقرير 2018-2025"},
    "lg_hors":   {"fr": "Hors collectivités locales (série homogène)",
                  "ar": "باستثناء الجماعات المحلية (سلسلة متجانسة)"},
    "lg_tot":    {"fr": "Total fonction publique", "ar": "إجمالي الوظيفة العمومية"},
    "lg_loc":    {"fr": "Collectivités locales", "ar": "الجماعات المحلية"},
    "rupture":   {"fr": "rupture de série :\nchangement de périmètre\ndes collectivités locales",
                  "ar": "انقطاع السلسلة:\nتغيّر نطاق\nالجماعات المحلية"},
    "couverture": {"fr": "collectivités locales : couverture\ncroissante de la base administrative",
                   "ar": "الجماعات المحلية: تغطية\nمتزايدة للقاعدة الإدارية"},
    "raccord":   {"fr": "2015-2017 : enquête 2010-2021\n2018-2025 : rapport 2018-2025",
                  "ar": "سنوات 2015-2017: مسح 2010-2021\nسنوات 2018-2025: تقرير 2018-2025"},
    "xlabel":    {"fr": "Année", "ar": "السنة"},
    "ylabel":    {"fr": "Effectifs (milliers d’agents)", "ar": "الأعداد (بآلاف الأعوان)"},
    "title":     {"fr": "Effectifs de la fonction publique en Tunisie, 2015-2025",
                  "ar": "أعداد أعوان الوظيفة العمومية في تونس، 2015-2025"},
    # salaire moyen
    "sal_avec":  {"fr": "Brut (avec contributions)", "ar": "خام (مع المساهمات)"},
    "sal_sans":  {"fr": "Brut (sans contributions)", "ar": "خام (دون المساهمات)"},
    "sal_net":   {"fr": "Net", "ar": "صافٍ"},
    "sal_y":     {"fr": "Salaire mensuel (dinars courants)", "ar": "الأجر الشهري (دينار جارٍ)"},
    "sal_title": {"fr": "Salaire mensuel moyen dans la fonction publique, 2015-2025",
                  "ar": "متوسّط الأجر الشهري في الوظيفة العمومية، 2015-2025"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _source(annee: int) -> str:
    """Publication dont vient une année de la série raccordée."""
    return _lab("src_2025") if annee >= _DEBUT_2025 else _lab("src_2021")


def _effectifs():
    """Effectifs 2015-2025 en milliers : enquête 2010-2021 jusqu'en 2017, puis rapport 2025.

    Le raccord est sûr — les deux publications concordent à l'arrondi sur 2018-2021 —
    et le millésime le plus récent fait foi sur les années communes. Le rapport 2025
    compte en agents : on le ramène en milliers, sans arrondir.
    """
    import pandas as pd
    ancien = _pivot(SERIE_EFF, [_HORS, _LOC, _TOT])
    ancien = ancien[ancien["annee"] < _DEBUT_2025]
    recent = _pivot(SERIE_EFF_2025, [_HORS, _LOC, _TOT])
    for c in (_HORS, _LOC, _TOT):
        recent[c] = recent[c] / 1000
    w = pd.concat([ancien, recent], ignore_index=True).sort_values("annee")
    w["annee"] = w["annee"].astype(int)
    return w.reset_index(drop=True)


def effectifs_table():
    """Tableau (onglet Données) : effectifs par périmètre, milliers d'agents, et source."""
    w = _effectifs()
    for c in (_HORS, _LOC, _TOT):
        w[c] = w[c].round(3)
    w["source"] = [_source(a) for a in w["annee"]]
    return w.rename(columns={
        "annee": _lab("col_annee"),
        _HORS: _lab("col_hors"),
        _LOC: _lab("col_loc"),
        _TOT: _lab("col_tot"),
        "source": _lab("col_source"),
    })


def fig_effectifs():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    w = _effectifs()
    y = w["annee"]
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.plot(y, w[_HORS], "o-", color="#1f6feb", lw=2.2, ms=5, label=ft(_lab("lg_hors")))
    ax.plot(y, w[_TOT], "s--", color="#6e7781", lw=1.6, ms=4, label=ft(_lab("lg_tot")))
    ax.plot(y, w[_LOC], "^:", color="#bf8700", lw=1.4, ms=4, label=ft(_lab("lg_loc")))
    # repère de la rupture de périmètre 2016→2017
    ax.axvspan(2016, 2017, color="#bf8700", alpha=0.08)
    ax.annotate("\n".join(ft(line) for line in _lab("rupture").split("\n")),
                xy=(2016.5, 0.30), xycoords=("data", "axes fraction"), fontsize=7.5,
                color="#7a5b00", ha="center", va="center")
    # couverture croissante des collectivités locales dans la base INSAF (rapport 2025)
    ax.annotate("\n".join(ft(line) for line in _lab("couverture").split("\n")),
                xy=(2021.5, 0.13), xycoords=("data", "axes fraction"), fontsize=7.5,
                color="#7a5b00", ha="center", va="center")
    # jonction des deux publications : raccord sûr, mais dit
    ax.axvline(_DEBUT_2025 - 0.5, color="#8b949e", lw=0.8, ls=":")
    ax.annotate("\n".join(ft(line) for line in _lab("raccord").split("\n")),
                xy=(_DEBUT_2025 - 0.4, 0.62), xycoords=("data", "axes fraction"),
                fontsize=7, color="#57606a", ha="left", va="center")
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_ylabel(ft(_lab("ylabel")))
    ax.set_title(ft(_lab("title")))
    ax.set_ylim(bottom=0)
    ax.set_xticks(list(range(int(y.min()), int(y.max()) + 1)))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="center left", bbox_to_anchor=(0.0, 0.45), fontsize=8.5)
    fig.tight_layout()
    return fig


def _salaires():
    df = figtools.series(SERIE_SAL)
    keep = [_BRUT_AVEC, _BRUT_SANS, _NET]
    w = (df[df["indicateur"].isin(keep)]
         .pivot(index="annee", columns="indicateur", values="valeur")
         .reset_index())
    w.columns.name = None
    w["annee"] = w["annee"].astype(int)
    return w[["annee", *keep]]


def salaire_table():
    """Tableau (onglet Données) : trois indicateurs, dinars courants, et source par année."""
    w = _salaires()
    w["source"] = [_source(a) for a in w["annee"]]
    return w.rename(columns={
        "annee": _lab("col_annee"),
        _BRUT_AVEC: _lab("sal_avec"),
        _BRUT_SANS: _lab("sal_sans"),
        _NET: _lab("sal_net"),
        "source": _lab("col_source"),
    })


def fig_salaire():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    w = _salaires()
    y = w["annee"]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(y, w[_BRUT_AVEC], "o-", color="#1f6feb", lw=2, ms=4, label=ft(_lab("sal_avec")))
    ax.plot(y, w[_BRUT_SANS], "s--", color="#8957e5", lw=1.6, ms=3, label=ft(_lab("sal_sans")))
    ax.plot(y, w[_NET], "^-.", color="#d1242f", lw=1.6, ms=3, label=ft(_lab("sal_net")))
    ax.axvline(_DEBUT_2025 - 0.5, color="#8b949e", lw=0.8, ls=":")
    ax.annotate("\n".join(ft(line) for line in _lab("raccord").split("\n")),
                xy=(_DEBUT_2025 - 0.4, 0.12), xycoords=("data", "axes fraction"),
                fontsize=7, color="#57606a", ha="left", va="center")
    ax.set_xlabel(ft(_lab("xlabel")))
    ax.set_ylabel(ft(_lab("sal_y")))
    ax.set_title(ft(_lab("sal_title")))
    ax.set_ylim(bottom=0)
    ax.set_xticks(list(range(int(y.min()), int(y.max()) + 1)))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8.5)
    fig.tight_layout()
    return fig

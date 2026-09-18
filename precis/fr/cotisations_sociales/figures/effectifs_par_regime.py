"""Figure « poids des régimes dans les effectifs de la CNSS, 2000 et 2020 » (source CNSS).

    from figures import effectifs_par_regime as epr
    epr.fig_parts()     # part de chaque régime dans les assurés actifs
    epr.table()         # effectifs et parts aux deux dates (onglet Données)

CE QUE LA FIGURE MONTRE. Le livre décrit les taux régime par régime, comme s'ils pesaient
d'un poids comparable. Ils ne le font pas, et le partage s'est déformé en vingt ans : le
régime des salariés non agricoles passe de 76,3 % à 53,8 % des assurés actifs, non parce
qu'il recule — ses effectifs sont multipliés par 1,6 — mais parce que les régimes de
non-salariés et celui des faibles revenus croissent beaucoup plus vite. Le régime des
travailleurs à faible revenu n'existait pas en 2000 ; il pèse 313 152 actifs en 2020,
soit plus que l'ensemble des salariés agricoles et agricoles améliorés réunis.

RÉSERVES QUE LA FIGURE DOIT PORTER :
  - les planches d'origine sont des **camemberts en pourcentages** assortis de quelques
    ancres absolues ; les effectifs se reconstituent par produit et souffrent donc des
    arrondis de la source ;
  - **le bouclage de 2000 n'est pas exact** : les régimes somment à 1 012 220 quand la
    caisse publie 1 013 483 assurés actifs, soit 0,125 % d'écart. Les parts de 2000 sont
    donc rapportées à la somme des régimes, pas au total publié ;
  - **2020 boucle exactement** (2 353 743), à condition d'y compter les 845 « non
    assujettis » que la planche isole et qui ne constituent pas un régime ;
  - un secteur de 0,32 % de la planche de 2020 ne porte aucune étiquette.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "cnss-effectifs-par-regime"
ANNEES = (2000, 2020)

# Sigles de la caisse : identiques dans les deux langues, là où les intitulés complets
# n'ont pas de traduction attestée dans ses publications arabes.
SIGLES = {
    "Régime des salariés non agricoles": "RSNA",
    "Régime des salariés agricoles amélioré": "RSAA",
    "Régime des travailleurs non salariés (secteur non agricole)": "TNSN.A",
    "Régime des travailleurs non salariés (secteur agricole)": "TNS.A",
    "Régime des travailleurs à faible revenu": "RTFR",
    "Régime des salariés agricoles": "RSA",
    "Régime des travailleurs tunisiens à l'étranger": "TTE",
    "Régime des artistes, des créateurs et des intellectuels": "RACI",
    # Pas un régime, mais un poste de la planche : il entre dans la base, sous son nom.
    # « n.a. » se lirait « non disponible », ce qu'il n'est pas.
    "Non assujettis": "Non assujettis",
}

_L = {
    "titre": {"fr": "CNSS : part de chaque régime dans les assurés actifs, 2000 et 2020",
              "ar": "الصندوق الوطني للضمان الاجتماعي: حصّة كلّ نظام من المضمونين النشطين، 2000 و2020"},
    "x": {"fr": "Part des assurés actifs (%)", "ar": "الحصّة من المضمونين النشطين (٪)"},
    "lg_2000": {"fr": "2000", "ar": "2000"},
    "lg_2020": {"fr": "2020", "ar": "2020"},
    "col_sigle": {"fr": "Régime (sigle)", "ar": "النظام (الرمز)"},
    "col_a2000": {"fr": "Actifs 2000", "ar": "النشطون 2000"},
    "col_a2020": {"fr": "Actifs 2020", "ar": "النشطون 2020"},
    "col_p2000": {"fr": "Part 2000 (%)", "ar": "الحصّة 2000 (٪)"},
    "col_p2020": {"fr": "Part 2020 (%)", "ar": "الحصّة 2020 (٪)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _actifs():
    """{année: {sigle: actifs}} — tous les postes de la planche, « non assujettis » compris.

    Les écarter fausserait la base : ils font partie des 2 353 743 assurés actifs publiés
    pour 2020, et c'est en les comptant que la somme des postes retombe sur ce total.
    """
    par = {a: {} for a in ANNEES}
    for r in figtools.series(SERIE).itertuples():
        an = int(r.annee)
        if an not in par:
            continue
        sigle = SIGLES.get(r.regime)
        if sigle is None:
            continue
        par[an][sigle] = int(float(r.actifs))
    return par


def _parts():
    """[(sigle, actifs 2000, actifs 2020, part 2000, part 2020)], du plus lourd au plus léger."""
    par = _actifs()
    bases = {a: sum(par[a].values()) for a in ANNEES}
    sigles = sorted(set(par[2000]) | set(par[2020]),
                    key=lambda s: -par[2020].get(s, 0))
    out = []
    for s in sigles:
        a0, a1 = par[2000].get(s, 0), par[2020].get(s, 0)
        out.append((s, a0, a1, 100 * a0 / bases[2000], 100 * a1 / bases[2020]))
    return out


def table():
    import pandas as pd
    return pd.DataFrame([
        {_lab("col_sigle"): s,
         _lab("col_a2000"): a0 or None,
         _lab("col_a2020"): a1 or None,
         _lab("col_p2000"): round(p0, 2) if a0 else None,
         _lab("col_p2020"): round(p1, 2) if a1 else None}
        for s, a0, a1, p0, p1 in _parts()])


def fig_parts():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _parts()
    y = range(len(d))
    h = 0.38

    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    ax.barh([i + h / 2 for i in y], [p0 for *_, p0, _ in d], height=h,
            color="#9ecae1", label=ft(_lab("lg_2000")))
    ax.barh([i - h / 2 for i in y], [p1 for *_, p1 in d], height=h,
            color="#08519c", label=ft(_lab("lg_2020")))

    for i, (_, a0, _, p0, p1) in enumerate(d):
        if a0:
            ax.text(p0 + 0.8, i + h / 2, f"{p0:.1f}".replace(".", ","),
                    va="center", fontsize=7.5, color="#57606a")
        ax.text(p1 + 0.8, i - h / 2, f"{p1:.1f}".replace(".", ","),
                va="center", fontsize=7.5, color="#24292f")

    ax.set_yticks(list(y))
    ax.set_yticklabels([s for s, *_ in d], fontsize=8.5)
    ax.invert_yaxis()
    ax.set_xlabel(ft(_lab("x")))
    ax.set_title(ft(_lab("titre")))
    # Sur LES DEUX années : borner sur la seule part de 2020 couperait la barre de 2000
    # du régime général, qui pèse 76,3 % contre 53,8 % à l'arrivée.
    ax.set_xlim(0, max(max(p0, p1) for *_, p0, p1 in d) * 1.18)
    ax.grid(True, axis="x", alpha=0.3)
    ax.legend(loc="lower right", fontsize=8.5)
    fig.tight_layout()
    return fig

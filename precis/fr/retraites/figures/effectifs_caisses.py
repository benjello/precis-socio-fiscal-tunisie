"""Figures « affiliés et pensionnés des caisses » (sources CNSS et ministère des Finances).

    from figures import effectifs_caisses as ec
    ec.fig_cnss()      # CNSS : actifs et pensionnés, 2000-2020
    ec.cnss_table()    # les deux séries et leur rapport (onglet Données)
    ec.fig_cnrps()     # CNRPS : affiliés et pensionnés, 2016-2021
    ec.cnrps_table()

POURQUOI DEUX FIGURES ET NON UNE. Les deux caisses ne se mesurent ni sur la même période
ni avec la même précision : la CNSS publie ses effectifs à l'unité sur vingt et un ans, la
CNRPS n'en publie aucun — ses chiffres ne sont connus que par le rapport du ministère des
Finances sur les entreprises publiques, en milliers et sur six ans. Les superposer
donnerait à croire à une comparaison que les sources n'autorisent pas.

CE QUE LES FIGURES DOIVENT PORTER :
  - **2020 est la première année où les actifs de la CNSS reculent** (2 402 269 puis
    2 353 743), tandis que les pensionnés continuent de croître. Le rapport entre les deux
    se dégrade donc par les deux bouts la même année ;
  - sur la période, les **pensionnés sont multipliés par 3,1** et les actifs par 2,3 ;
  - les effectifs CNRPS sont **arrondis au millier** par leur source, et l'édition d'un
    rapport corrige parfois la précédente : seules les valeurs constatées sont tracées,
    les prévisions sont écartées ;
  - le champ des deux caisses est disjoint : salariés du privé et non-salariés d'un côté,
    agents de l'État et des collectivités publiques de l'autre.

LE RAPPORT DÉMOGRAPHIQUE EST CALCULÉ, JAMAIS REPRIS. La caisse publie le sien sur une
définition qu'elle énonce — « nombre des actifs pour un seul *bénéficiaire* de pension » —
et ses valeurs ne se retrouvent pas en divisant les effectifs qu'elle publie par ailleurs.
L'écart est systématique et se constate sur deux millésimes : par régime, les ratios
publiés sont au-dessus des ratios calculés (RSNA 2,42 sur la planche de 2019, 2,2 sur
celle de 2020, contre 2,00 calculé). Le rapport tracé ici est donc calculé à partir des
effectifs publiés, et de ceux-là seuls.

CE QUI N'EST PAS AFFIRMÉ. La planche porte à gauche un graphique d'ensemble dont les douze
étiquettes se répartissent sur six abscisses seulement, avec une ordonnée non monotone
(4,04 est tracé au-dessus de 4,16) : ce n'est pas une série de douze années, et rien n'est
avancé ici sur son contenu. Deux divergences par régime restent inexpliquées, signalées
sans hypothèse : le RSAA, stable d'un millésime à l'autre (10,96 puis 10,9 publiés, 9,71
calculé), et le RTFR, que la planche de 2020 étiquette « RTFR (Emp Etat) » et chiffre à
4,6 quand les deux ancres absolues de la caisse — 313 152 actifs et 31 889 pensionnés,
lues sur ses planches 05 et 06 — impliquent 9,82. Le millésime précédent ne porte ce
régime nulle part.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_CNSS = "cnss-effectifs"                 # actifs et pensionnés, à l'unité
SERIE_CAISSES = "caisses-effectifs-minfin"    # CNRPS et CNSS, en milliers
SERIE_REGIME = "cnss-effectifs-par-regime"    # par régime, 2000 et 2020

# Les sigles employés par la caisse sur ses propres planches. Ils servent d'étiquettes
# d'axe parce qu'ils sont identiques dans les deux langues, là où les intitulés complets
# des régimes n'ont pas de traduction attestée dans les publications arabes de la caisse.
SIGLES = {
    "Régime des salariés agricoles": "RSA",
    "Régime des salariés agricoles amélioré": "RSAA",
    "Régime des salariés non agricoles": "RSNA",
    "Régime des travailleurs non salariés (secteur agricole)": "TNS.A",
    "Régime des travailleurs non salariés (secteur non agricole)": "TNSN.A",
    "Régime des travailleurs tunisiens à l'étranger": "TTE",
    "Régime des artistes, des créateurs et des intellectuels": "RACI",
    "Régime des travailleurs à faible revenu": "RTFR",
}

_L = {
    "titre_cnss": {
        "fr": "CNSS : assurés sociaux actifs et pensionnés, 2000-2020",
        "ar": "الصندوق الوطني للضمان الاجتماعي: المضمونون النشطون وأصحاب الجرايات، 2000-2020"},
    "titre_cnrps": {
        "fr": "CNRPS : affiliés et pensionnés, 2016-2021",
        "ar": "الصندوق الوطني للتقاعد والحيطة الاجتماعية: المنخرطون وأصحاب الجرايات، 2016-2021"},
    "x": {"fr": "Année", "ar": "السنة"},
    "y_cnss": {"fr": "Effectif (millions de personnes)", "ar": "العدد (بملايين الأشخاص)"},
    "y_cnrps": {"fr": "Effectif (milliers de personnes)", "ar": "العدد (بآلاف الأشخاص)"},
    "lg_actifs": {"fr": "Assurés sociaux actifs", "ar": "المضمونون الاجتماعيون النشطون"},
    "lg_pens": {"fr": "Titulaires de pensions", "ar": "أصحاب الجرايات"},
    "lg_affilies": {"fr": "Affiliés", "ar": "المنخرطون"},
    "recul": {"fr": "2020 : les actifs reculent\npour la première fois,\nles pensionnés non",
              "ar": "2020: يتراجع النشطون\nلأوّل مرّة، لا أصحاب الجرايات"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_actifs": {"fr": "Actifs", "ar": "النشطون"},
    "col_pens": {"fr": "Pensionnés", "ar": "أصحاب الجرايات"},
    "col_rapport": {"fr": "Actifs par pensionné", "ar": "النشطون لكلّ صاحب جراية"},
    "col_affilies": {"fr": "Affiliés (milliers)", "ar": "المنخرطون (بالآلاف)"},
    "col_pens_k": {"fr": "Pensionnés (milliers)", "ar": "أصحاب الجرايات (بالآلاف)"},
    "titre_ratio": {
        "fr": "CNSS : nombre d'actifs par pensionné, 2000-2020",
        "ar": "الصندوق الوطني للضمان الاجتماعي: عدد النشطين لكلّ صاحب جراية، 2000-2020"},
    "titre_ratio_reg": {
        "fr": "CNSS : nombre d'actifs par pensionné, par régime, 2020",
        "ar": "الصندوق الوطني للضمان الاجتماعي: عدد النشطين لكلّ صاحب جراية حسب النظام، 2020"},
    "y_ratio": {"fr": "Actifs par pensionné", "ar": "النشطون لكلّ صاحب جراية"},
    "lg_ratio": {"fr": "Rapport calculé", "ar": "النسبة المحتسبة"},
    "sommet": {"fr": "2010 : le sommet\n(4,04 actifs par pensionné)",
               "ar": "2010: الذروة\n(4,04 نشط لكلّ صاحب جراية)"},
    "col_sigle": {"fr": "Régime (sigle)", "ar": "النظام (الرمز)"},
    "col_ratio": {"fr": "Actifs par pensionné", "ar": "النشطون لكلّ صاحب جراية"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _cnss():
    """[(année, actifs, pensionnés)] — effectifs à l'unité, 2000-2020."""
    return sorted((int(r.annee), int(r.actifs), int(r.pensionnes))
                  for r in figtools.series(SERIE_CNSS).itertuples())


def _cnrps():
    """[(année, affiliés, pensionnés)] en milliers — valeurs CONSTATÉES seulement.

    Une même année paraît dans plusieurs éditions du rapport ; on retient la plus
    récente, qui corrige les précédentes.
    """
    par = {}
    for r in figtools.series(SERIE_CAISSES).itertuples():
        if r.caisse != "CNRPS" or r.statut != "realise":
            continue
        if r.indicateur not in ("assures", "pensionnes"):
            continue
        cle = (int(r.annee), r.indicateur)
        edition = str(r.millesime_source)
        if cle not in par or edition > par[cle][0]:
            par[cle] = (edition, float(r.valeur_milliers))
    annees = sorted({a for a, _ in par})
    return [(a, par.get((a, "assures"), (None, None))[1],
             par.get((a, "pensionnes"), (None, None))[1]) for a in annees]


def cnss_table():
    import pandas as pd
    return pd.DataFrame([
        {_lab("col_annee"): a,
         _lab("col_actifs"): act,
         _lab("col_pens"): pen,
         _lab("col_rapport"): round(act / pen, 2)}
        for a, act, pen in _cnss()])


def cnrps_table():
    import pandas as pd
    return pd.DataFrame([
        {_lab("col_annee"): a,
         _lab("col_affilies"): aff,
         _lab("col_pens_k"): pen,
         _lab("col_rapport"): round(aff / pen, 2) if aff and pen else None}
        for a, aff, pen in _cnrps()])


def fig_cnss():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _cnss()
    annees = [a for a, _, _ in d]
    actifs = [x / 1e6 for _, x, _ in d]
    pens = [x / 1e6 for _, _, x in d]

    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    ax.plot(annees, actifs, "o-", color="#08519c", lw=2.2, ms=4, label=ft(_lab("lg_actifs")))
    ax.plot(annees, pens, "s--", color="#bf8700", lw=1.8, ms=4, label=ft(_lab("lg_pens")))

    # 2020 : le seul retournement de la série des actifs. Le cartouche va dans la bande
    # médiane, vide entre les deux courbes à droite.
    if 2020 in annees:
        ax.axvspan(2019.5, 2020.5, color="#6e7781", alpha=0.08)
        ax.annotate("\n".join(ft(l) for l in _lab("recul").split("\n")),
                    xy=(2020, actifs[-1]), xytext=(2014.5, max(actifs) * 0.62),
                    fontsize=7.5, color="#57606a", ha="center", va="center",
                    arrowprops=dict(arrowstyle="->", color="#8b949e", lw=0.8,
                                    shrinkA=2, shrinkB=4),
                    bbox=dict(boxstyle="round,pad=0.35", fc="#f6f8fa",
                              ec="#8b949e", lw=0.6, alpha=0.95))

    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_cnss")))
    ax.set_title(ft(_lab("titre_cnss")))
    ax.set_ylim(0, max(actifs) * 1.15)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8.5)
    fig.tight_layout()
    return fig


def fig_cnrps():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = [(a, aff, pen) for a, aff, pen in _cnrps() if aff is not None and pen is not None]
    annees = [a for a, _, _ in d]

    fig, ax = plt.subplots(figsize=(9.5, 5))
    ax.plot(annees, [x for _, x, _ in d], "o-", color="#08519c", lw=2.2, ms=5,
            label=ft(_lab("lg_affilies")))
    ax.plot(annees, [x for _, _, x in d], "s--", color="#bf8700", lw=1.8, ms=5,
            label=ft(_lab("lg_pens")))
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_cnrps")))
    ax.set_title(ft(_lab("titre_cnrps")))
    ax.set_xticks(annees)
    ax.set_ylim(0, max(x for _, x, _ in d) * 1.2)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="center left", fontsize=8.5)
    fig.tight_layout()
    return fig


def _ratios_regime(annee: int = 2020):
    """[(sigle, actifs, pensionnés, ratio)] triés par ratio croissant.

    Un régime sans pensionnés publiés n'a pas de rapport : il est écarté, non compté
    zéro. C'est le cas des « non assujettis » de 2020 (845 actifs, aucun pensionné).
    """
    out = []
    for r in figtools.series(SERIE_REGIME).itertuples():
        if int(r.annee) != annee:
            continue
        sigle = SIGLES.get(r.regime)
        if sigle is None:
            continue
        try:
            actifs, pens = int(float(r.actifs)), int(float(r.pensionnes))
        except (TypeError, ValueError):       # cellule vide ou NaN
            continue
        if pens == 0:
            continue
        out.append((sigle, actifs, pens, actifs / pens))
    return sorted(out, key=lambda t: t[3])


def ratio_regime_table():
    import pandas as pd
    return pd.DataFrame([
        {_lab("col_sigle"): s,
         _lab("col_actifs"): a,
         _lab("col_pens"): p,
         _lab("col_ratio"): round(r, 2)}
        for s, a, p, r in _ratios_regime()])


def fig_ratio():
    """Le rapport calculé, tous régimes : une cloche, non un déclin continu."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _cnss()
    annees = [a for a, _, _ in d]
    ratio = [act / pen for _, act, pen in d]

    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    ax.plot(annees, ratio, "o-", color="#08519c", lw=2.2, ms=4, label=ft(_lab("lg_ratio")))

    # Le sommet de 2010 est le fait de la figure : avant lui le rapport s'améliore.
    i = ratio.index(max(ratio))
    ax.annotate("\n".join(ft(l) for l in _lab("sommet").split("\n")),
                xy=(annees[i], ratio[i]), xytext=(annees[i] - 4.5, max(ratio) * 1.06),
                fontsize=7.5, color="#57606a", ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color="#8b949e", lw=0.8,
                                shrinkA=2, shrinkB=4),
                bbox=dict(boxstyle="round,pad=0.35", fc="#f6f8fa",
                          ec="#8b949e", lw=0.6, alpha=0.95))

    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_ratio")))
    ax.set_title(ft(_lab("titre_ratio")))
    # Une série annuelle ne se gradue pas en demi-années.
    ax.set_xticks([a for a in annees if a % 5 == 0])
    ax.set_xticks(annees, minor=True)
    ax.set_ylim(0, max(ratio) * 1.25)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower left", fontsize=8.5)
    fig.tight_layout()
    return fig


def fig_ratio_regime():
    """Le même rapport, régime par régime, en 2020 : la dispersion est l'enseignement."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _ratios_regime()
    sigles = [s for s, _, _, _ in d]
    vals = [r for _, _, _, r in d]

    fig, ax = plt.subplots(figsize=(9.5, 5))
    # Le régime déficitaire en actifs se distingue : moins d'un actif par pensionné.
    couleurs = ["#bf8700" if v < 1 else "#08519c" for v in vals]
    ax.barh(range(len(d)), vals, color=couleurs, height=0.62)
    for i, v in enumerate(vals):
        ax.text(v + max(vals) * 0.012, i, f"{v:.2f}".replace(".", ","),
                va="center", fontsize=8, color="#24292f")

    ax.set_yticks(range(len(d)))
    ax.set_yticklabels(sigles, fontsize=8.5)   # sigles : identiques dans les deux langues
    ax.set_xlabel(ft(_lab("y_ratio")))
    ax.set_title(ft(_lab("titre_ratio_reg")))
    ax.set_xlim(0, max(vals) * 1.12)
    ax.axvline(1, color="#6e7781", lw=0.9, ls=":")
    ax.grid(True, axis="x", alpha=0.3)
    fig.tight_layout()
    return fig

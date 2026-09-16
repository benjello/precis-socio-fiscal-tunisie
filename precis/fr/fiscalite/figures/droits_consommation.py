"""Figure « ce que rapportent les droits de consommation » du livre *Fiscalité*.

LA RUPTURE DE SÉRIE EST LE SUJET, PAS UN DÉTAIL — et elle tombe la même année que celle
de la TVA, pour la même raison. La rubrique « droits de consommation » du ministère des
Finances est continue depuis 1986, et c'est le ministère qui l'intitule ainsi ; or la loi
n° 88-62 du 2 juin 1988 ne s'applique qu'à compter du 1er juillet 1988 (décret n° 88-1109,
art. 2), et son article 7 abroge les taxes qui la précédaient — la taxe sur les bières,
vins et autres boissons alcoolisées, et la taxe unique de compensation sur les carburants.
Les exercices 1986 et 1987 mesurent donc ces dispositifs abrogés, non le droit refondu.

La figure le montre au lieu de le taire : ces deux années sont tracées en pointillé gris,
séparées du reste par une bande verticale, et la légende nomme ce qu'elles mesurent.

DEUX RAPPORTS, DEUX AXES, comme pour la TVA. L'axe gauche rapporte le droit au produit
intérieur brut, l'axe droit aux dépenses totales de l'État. Le second ne commence qu'en
1990 : le ministère ne publie pas les dépenses totales avant cette date. Les exercices
1988 et 1989 n'ont donc qu'un seul des deux ratios.

LES COULEURS NE SONT PAS LIBRES. L'ocre est celui de la bande « droits de consommation »
de la figure de composition des recettes (`irpp.py`) : une même couleur pour un même impôt,
d'une figure à l'autre. Le rouge de l'axe droit porte déjà le rapport aux dépenses de
l'État dans les figures de l'impôt sur le revenu et de la TVA.

DEUX DÉNOMINATEURS DE PIB, ET C'EST VOULU — même raison que pour la TVA. Le PIB retenu est
celui du ministère des Finances, sur lequel il calcule lui-même ses ratios ; le tableau
conserve à côté celui des comptes nationaux, qui s'en écarte pour 2012-2014.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402

HERE = Path(__file__).resolve().parent
FIGDATA = HERE.parent / "figdata"

SERIE_COMPOSITION = "recettes-fiscales-composition"
SERIE_RATIOS = "irpp-ratios"

# Première année d'application de la loi n° 88-62 : le décret n° 88-1109, art. 2, la rend
# applicable à compter du 1er juillet 1988, conformément à son article 8. L'exercice 1988
# n'est donc soumis au régime refondu qu'au second semestre.
ANNEE_DC = 1988

# Les dépenses totales de l'État ne sont publiées qu'à partir de 1990.
ANNEE_DEPENSES = 1990

_L = {
    "lg_avant": {
        "fr": "Taxes antérieures sur les produits / PIB",
        "ar": "الأداءات السابقة على المنتجات / الناتج المحلي الإجمالي"},
    "lg_pib": {
        "fr": "Droits de consommation / PIB (éch. gauche)",
        "ar": "المعلوم على الاستهلاك / الناتج المحلي الإجمالي (يسار)"},
    "lg_dep": {
        "fr": "Droits de consommation / dépenses de l'État (éch. droite)",
        "ar": "المعلوم على الاستهلاك / نفقات الدولة (يمين)"},
    "y_pib": {"fr": "En % du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "y_dep": {"fr": "En % des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "xlabel": {"fr": "Année", "ar": "السنة"},
    "title": {"fr": "Ce que rapportent les droits de consommation, 1986-2025",
              "ar": "مردود المعلوم على الاستهلاك، 1986-2025"},
    "rupture": {"fr": "refonte du droit de consommation\n(loi n° 88-62, 1er juillet 1988)",
                "ar": "إصلاح المعلوم على الاستهلاك\n(القانون عدد 88-62، 1 جويلية 1988)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_pib": {"fr": "% du PIB (ministère des Finances)",
                "ar": "% من الناتج المحلي الإجمالي (وزارة المالية)"},
    "col_pib_cnat": {"fr": "% du PIB (comptes nationaux)",
                     "ar": "% من الناتج المحلي الإجمالي (الحسابات القومية)"},
    "col_dep": {"fr": "% des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "col_rec": {"fr": "% des recettes fiscales", "ar": "% من المداخيل الجبائية"},
    "col_mdt": {"fr": "Droits de consommation (MDT)", "ar": "المعلوم على الاستهلاك (م.د)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _donnees():
    """Les deux séries jointes sur l'année, avec les ratios au PIB et aux dépenses.

    La composition des recettes porte le montant du droit de consommation ; les ratios de
    l'impôt sur le revenu portent les deux PIB et les dépenses totales. Aucune des deux ne
    porte tout — c'est la même jointure que pour la figure de la TVA.
    """
    comp = figtools.series(SERIE_COMPOSITION)
    rat = figtools.series(SERIE_RATIOS)
    d = comp[["annee", "consommation_MDT", "consommation_pct"]].merge(
        rat[["annee", "pib_minfin_MDT", "pib_cnat_MDT", "depenses_totales_MDT"]],
        on="annee", how="left")
    d["dc_sur_pib_pct"] = 100 * d["consommation_MDT"] / d["pib_minfin_MDT"]
    d["dc_sur_pib_cnat_pct"] = 100 * d["consommation_MDT"] / d["pib_cnat_MDT"]
    d["dc_sur_depenses_pct"] = 100 * d["consommation_MDT"] / d["depenses_totales_MDT"]
    return d


def table():
    d = _donnees()
    cols = ["annee", "dc_sur_pib_pct", "dc_sur_depenses_pct",
            "dc_sur_pib_cnat_pct", "consommation_pct", "consommation_MDT"]
    w = d[cols].copy()
    for c in ("dc_sur_pib_pct", "dc_sur_depenses_pct",
              "dc_sur_pib_cnat_pct", "consommation_pct"):
        w[c] = w[c].round(2)
    return w.rename(columns={
        "annee": _lab("col_annee"),
        "dc_sur_pib_pct": _lab("col_pib"),
        "dc_sur_depenses_pct": _lab("col_dep"),
        "dc_sur_pib_cnat_pct": _lab("col_pib_cnat"),
        "consommation_pct": _lab("col_rec"),
        "consommation_MDT": _lab("col_mdt"),
    })


def prepare(generated: str | None = None):
    d = _donnees()
    figtools.write_figdata(
        table(), FIGDATA / "fig_droits_consommation_rendement.csv",
        SERIE_COMPOSITION, SERIE_RATIOS,
        note=("rendement des droits de consommation en points de PIB et en part des "
              "dépenses de l'État, 1986-2025 ; rupture de série en 1988, les exercices "
              "antérieurs portant les taxes abrogées par l'article 7 de la loi n° 88-62 ; "
              "les dépenses totales ne sont publiées qu'à partir de 1990"),
        generated=generated)
    return d


def fig_rendement():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    avant = d[d["annee"] < ANNEE_DC]
    apres = d[d["annee"] >= ANNEE_DC]
    depenses = d[d["annee"] >= ANNEE_DEPENSES]

    fig, ax1 = plt.subplots(figsize=(9.5, 5.2))
    ax2 = ax1.twinx()

    # La bande grise couvre les années où la rubrique mesure les dispositifs abrogés.
    ax1.axvspan(d["annee"].min() - 0.5, ANNEE_DC - 0.5, color="#8b949e", alpha=0.13, lw=0)
    ax1.axvline(ANNEE_DC - 0.5, color="#57606a", lw=1.2, ls="--")

    l0, = ax1.plot(avant["annee"], avant["dc_sur_pib_pct"], "o:", color="#57606a",
                   lw=1.6, ms=4, label=ft(_lab("lg_avant")))
    l1, = ax1.plot(apres["annee"], apres["dc_sur_pib_pct"], "o-", color="#bf8700",
                   lw=2, ms=4, label=ft(_lab("lg_pib")))
    l2, = ax2.plot(depenses["annee"], depenses["dc_sur_depenses_pct"], "s--",
                   color="#d1242f", lw=1.8, ms=3, label=ft(_lab("lg_dep")))

    # L'annotation se place dans la moitié basse du cadre, comme pour la TVA, mais pour
    # une raison propre à cette série, relevée sur les données : après 1988 la courbe de
    # gauche culmine à 3,73 point de PIB en 1994, redescend jusqu'à 1,97 en 2015, puis se
    # tient autour de 2,4. Le haut du cadre est donc occupé par les années 1991-1996, et
    # le bas reste libre à partir de 1990, où le texte commence.
    bas, haut = ax1.get_ylim()
    y_texte = bas + 0.15 * (haut - bas)
    ax1.annotate(ft(_lab("rupture")), xy=(ANNEE_DC - 0.5, y_texte),
                 xytext=(ANNEE_DC + 2.0, y_texte),
                 fontsize=8, color="#57606a", va="center",
                 arrowprops=dict(arrowstyle="->", color="#57606a", lw=1))

    ax1.set_ylabel(ft(_lab("y_pib")), color="#bf8700")
    ax2.set_ylabel(ft(_lab("y_dep")), color="#d1242f")
    ax1.set_xlabel(ft(_lab("xlabel")))
    ax1.set_title(ft(_lab("title")))
    ax1.grid(True, alpha=0.3)
    ax1.legend(handles=[l0, l1, l2], loc="upper right", fontsize=8.5)
    fig.tight_layout()
    return fig

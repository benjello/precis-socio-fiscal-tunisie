"""Figure « ce que rapporte l'impôt sur les sociétés » du livre *Fiscalité*.

LA RUPTURE DE SÉRIE EST LE SUJET, PAS UN DÉTAIL — comme pour la taxe sur la valeur
ajoutée et pour l'impôt sur le revenu. La rubrique « impôts sur les sociétés » du
ministère des Finances est continue depuis 1986, et c'est le ministère lui-même qui
l'intitule ainsi ; or l'impôt sur les sociétés naît du code promulgué par la loi
n° 89-114 du 30 décembre 1989 et ne s'applique qu'aux bénéfices réalisés à compter du
1er janvier 1990. Les exercices 1986 à 1989 portent donc l'impôt sur les bénéfices des
sociétés de l'article 9 de la loi n° 85-109, que le code de 1989 abroge — un impôt qui
partageait son article fondateur avec celui des bénéfices industriels et commerciaux.

La figure le montre au lieu de le taire : ces quatre années sont tracées en pointillé
gris, séparées du reste par une bande verticale, et la légende nomme ce qu'elles
mesurent réellement.

DEUX RAPPORTS, DEUX AXES. L'axe gauche rapporte l'impôt au produit intérieur brut, l'axe
droit aux dépenses totales de l'État. Le second ne commence qu'en 1990 : le ministère ne
publie pas les dépenses totales avant cette date. Ici, les deux bornes coïncident, la
création de l'impôt et le début de la série des dépenses tombant la même année.

DEUX DÉNOMINATEURS DE PIB, ET C'EST VOULU. Le PIB n'est publié par aucune des deux
sources : il se déduit du fichier d'indicateurs du ministère. Celui des comptes
nationaux de l'INS, base 2015, ne coïncide pas pour 2012-2014. La figure retient le PIB
du ministère — c'est celui sur lequel il calcule lui-même ses ratios —, et le tableau
conserve les deux colonnes côte à côte : le dénominateur d'un ratio se choisit, il ne se
devine pas.

LES DEUX COLONNES SONT SOUVENT IDENTIQUES, ET CE N'EST PAS UN DÉFAUT. Mesuré sur les
quarante exercices, l'écart entre les deux PIB est nul pour trente-trois d'entre eux, y
compris toute la fin de période. Il n'apparaît que sur sept exercices, où il est alors
considérable : −4,79 % en 2012, −5,00 % en 2013, −5,25 % en 2014. Un lecteur qui verrait
deux colonnes portant le même nombre pourrait croire à une erreur de construction ; la
note de lecture de la figure le prévient expressément. Retirer la colonne pour cause de
ressemblance reviendrait à masquer le seul endroit où les deux sources se contredisent.

CE QUE LA SÉRIE NE PERMET PAS DE FAIRE. Le classeur source distingue les impôts sur les
sociétés « pétrolières » et « non pétrolières ». La série transformée n'en garde qu'un
agrégat. Aucun commentaire de cette figure ne peut donc porter sur la part pétrolière du
rendement, et le texte du chapitre le dit plutôt que de laisser croire le contraire.
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

# Premier exercice régi par l'impôt sur les sociétés : le code promulgué par la loi
# n° 89-114 du 30 décembre 1989 s'applique aux bénéfices réalisés à compter du
# 1er janvier 1990. Les exercices antérieurs portent l'impôt sur les bénéfices des
# sociétés de l'article 9 de la loi n° 85-109 du 31 décembre 1985.
ANNEE_IS = 1990

# Les dépenses totales de l'État ne sont publiées qu'à partir de 1990 — la même année,
# ici, que la création de l'impôt.
ANNEE_DEPENSES = 1990

_L = {
    "lg_avant": {
        "fr": "Impôt sur les bénéfices des sociétés / PIB",
        "ar": "الضريبة على أرباح الشركات / الناتج المحلي الإجمالي"},
    "lg_pib": {
        "fr": "Impôt sur les sociétés / PIB (éch. gauche)",
        "ar": "الضريبة على الشركات / الناتج المحلي الإجمالي (يسار)"},
    "lg_dep": {
        "fr": "Impôt sur les sociétés / dépenses de l'État (éch. droite)",
        "ar": "الضريبة على الشركات / نفقات الدولة (يمين)"},
    "y_pib": {"fr": "En % du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "y_dep": {"fr": "En % des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "xlabel": {"fr": "Année", "ar": "السنة"},
    "title": {"fr": "Ce que rapporte l'impôt sur les sociétés, 1986-2025",
              "ar": "مردود الضريبة على الشركات، 1986-2025"},
    "rupture": {"fr": "création de l'impôt sur les sociétés\n(loi n° 89-114, bénéfices de 1990)",
                "ar": "إحداث الضريبة على الشركات\n(القانون عدد 89-114، أرباح سنة 1990)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_pib": {"fr": "% du PIB (ministère des Finances)",
                "ar": "% من الناتج المحلي الإجمالي (وزارة المالية)"},
    "col_pib_cnat": {"fr": "% du PIB (comptes nationaux)",
                     "ar": "% من الناتج المحلي الإجمالي (الحسابات القومية)"},
    "col_dep": {"fr": "% des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "col_rec": {"fr": "% des recettes fiscales", "ar": "% من المداخيل الجبائية"},
    "col_mdt": {"fr": "Impôt sur les sociétés (MDT)", "ar": "الضريبة على الشركات (م.د)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _donnees():
    """Les deux séries jointes sur l'année, avec les ratios au PIB et aux dépenses.

    La composition des recettes porte le montant de l'impôt sur les sociétés ; les
    ratios de l'impôt sur le revenu portent les deux PIB et les dépenses totales.
    Aucune des deux ne porte tout.
    """
    comp = figtools.series(SERIE_COMPOSITION)
    rat = figtools.series(SERIE_RATIOS)
    d = comp[["annee", "is_MDT", "is_pct"]].merge(
        rat[["annee", "pib_minfin_MDT", "pib_cnat_MDT", "depenses_totales_MDT"]],
        on="annee", how="left")
    d["is_sur_pib_pct"] = 100 * d["is_MDT"] / d["pib_minfin_MDT"]
    d["is_sur_pib_cnat_pct"] = 100 * d["is_MDT"] / d["pib_cnat_MDT"]
    d["is_sur_depenses_pct"] = 100 * d["is_MDT"] / d["depenses_totales_MDT"]
    return d


def table():
    d = _donnees()
    cols = ["annee", "is_sur_pib_pct", "is_sur_depenses_pct",
            "is_sur_pib_cnat_pct", "is_pct", "is_MDT"]
    w = d[cols].copy()
    for c in ("is_sur_pib_pct", "is_sur_depenses_pct",
              "is_sur_pib_cnat_pct", "is_pct"):
        w[c] = w[c].round(2)
    return w.rename(columns={
        "annee": _lab("col_annee"),
        "is_sur_pib_pct": _lab("col_pib"),
        "is_sur_depenses_pct": _lab("col_dep"),
        "is_sur_pib_cnat_pct": _lab("col_pib_cnat"),
        "is_pct": _lab("col_rec"),
        "is_MDT": _lab("col_mdt"),
    })


def prepare(generated: str | None = None):
    d = _donnees()
    figtools.write_figdata(
        table(), FIGDATA / "fig_impot_societes_rendement.csv",
        SERIE_COMPOSITION, SERIE_RATIOS,
        note=("rendement de l'impôt sur les sociétés en points de PIB et en part des "
              "dépenses de l'État, 1986-2025 ; rupture de série en 1990, les exercices "
              "antérieurs portant l'impôt sur les bénéfices des sociétés abrogé par le "
              "code de 1989 ; les dépenses totales ne sont publiées qu'à partir de 1990 ; "
              "la ventilation entre sociétés pétrolières et non pétrolières du classeur "
              "source n'est pas conservée par la série"),
        generated=generated)
    return d


def fig_rendement():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    avant = d[d["annee"] < ANNEE_IS]
    apres = d[d["annee"] >= ANNEE_IS]
    depenses = d[d["annee"] >= ANNEE_DEPENSES]

    fig, ax1 = plt.subplots(figsize=(9.5, 5.2))
    ax2 = ax1.twinx()

    # La bande grise couvre les années où la rubrique mesure autre chose que l'impôt
    # sur les sociétés.
    ax1.axvspan(d["annee"].min() - 0.5, ANNEE_IS - 0.5, color="#8b949e", alpha=0.13, lw=0)
    ax1.axvline(ANNEE_IS - 0.5, color="#57606a", lw=1.2, ls="--")

    l0, = ax1.plot(avant["annee"], avant["is_sur_pib_pct"], "o:", color="#57606a",
                   lw=1.6, ms=4, label=ft(_lab("lg_avant")))
    # Le bleu clair est celui de la bande « impôt sur les sociétés » de la figure de
    # composition : une même couleur pour un même impôt, d'une figure à l'autre. Le
    # rouge de l'axe droit reprend la convention des deux autres figures de rendement,
    # où il porte déjà le rapport aux dépenses de l'État.
    l1, = ax1.plot(apres["annee"], apres["is_sur_pib_pct"], "o-", color="#54aeff",
                   lw=2, ms=4, label=ft(_lab("lg_pib")))
    l2, = ax2.plot(depenses["annee"], depenses["is_sur_depenses_pct"], "s--",
                   color="#d1242f", lw=1.8, ms=3, label=ft(_lab("lg_dep")))

    # L'annotation se place dans la moitié haute du cadre : les deux courbes occupent
    # le bas sur la plus grande partie de la période.
    bas, haut = ax1.get_ylim()
    y_texte = bas + 0.85 * (haut - bas)
    ax1.annotate(ft(_lab("rupture")), xy=(ANNEE_IS - 0.5, y_texte),
                 xytext=(ANNEE_IS + 2.0, y_texte),
                 fontsize=8, color="#57606a", va="center",
                 arrowprops=dict(arrowstyle="->", color="#57606a", lw=1))

    ax1.set_ylabel(ft(_lab("y_pib")), color="#54aeff")
    ax2.set_ylabel(ft(_lab("y_dep")), color="#d1242f")
    ax1.set_xlabel(ft(_lab("xlabel")))
    ax1.set_title(ft(_lab("title")))
    ax1.grid(True, alpha=0.3)
    ax1.legend(handles=[l0, l1, l2], loc="upper left", fontsize=8.5)
    fig.tight_layout()
    return fig

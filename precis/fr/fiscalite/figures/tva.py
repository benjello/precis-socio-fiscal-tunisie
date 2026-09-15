"""Figure « ce que rapporte la TVA » du livre *Fiscalité*.

LA RUPTURE DE SÉRIE EST LE SUJET, PAS UN DÉTAIL — comme pour l'impôt sur le revenu, mais
deux ans plus tôt. La rubrique « 2.2 TVA » du ministère des Finances est continue depuis
1986, et c'est le ministère lui-même qui l'intitule ainsi ; or la taxe sur la valeur
ajoutée est créée par la loi n° 88-61 du 2 juin 1988 et n'entre en vigueur qu'au
1er juillet 1988. Les exercices 1986 et 1987 portent donc les taxes sur le chiffre
d'affaires que le code de 1988 remplace, non la TVA.

La figure le montre au lieu de le taire : ces deux années sont tracées en pointillé gris,
séparées du reste par une bande verticale, et la légende nomme ce qu'elles mesurent
réellement.

DEUX RAPPORTS, DEUX AXES. L'axe gauche rapporte la taxe au produit intérieur brut, l'axe
droit aux dépenses totales de l'État. Le second ne commence qu'en 1990 : le ministère ne
publie pas les dépenses totales avant cette date. Les exercices 1988 et 1989 n'ont donc
qu'un seul des deux ratios, et la courbe de droite ne pénètre jamais la zone grisée.

DEUX DÉNOMINATEURS DE PIB, ET C'EST VOULU. Le PIB n'est publié par aucune des deux
sources : il se déduit du fichier d'indicateurs du ministère (déficit en dinars ÷ déficit
en points de PIB). Celui des comptes nationaux de l'INS, base 2015, ne coïncide pas pour
2012-2014. La figure retient le PIB du ministère — c'est celui sur lequel il calcule
lui-même ses ratios —, et le tableau conserve les deux colonnes côte à côte : le
dénominateur d'un ratio se choisit, il ne se devine pas.
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

# Première année d'application de la TVA : le code promulgué par la loi n° 88-61 du
# 2 juin 1988 s'applique à compter du 1er juillet 1988. L'exercice 1988 n'est donc taxé
# qu'au second semestre, et l'assujettissement s'étend ensuite par paliers — commerce de
# gros en 1989, commerce de détail en 1996 seulement.
ANNEE_TVA = 1988

# Les dépenses totales de l'État ne sont publiées qu'à partir de 1990 : la courbe de
# droite commence donc deux ans après la création de la taxe.
ANNEE_DEPENSES = 1990

_L = {
    "lg_avant": {
        "fr": "Taxes antérieures sur le chiffre d'affaires / PIB",
        "ar": "الأداءات السابقة على رقم المعاملات / الناتج المحلي الإجمالي"},
    "lg_pib": {
        "fr": "TVA / PIB (éch. gauche)",
        "ar": "الأداء على القيمة المضافة / الناتج المحلي الإجمالي (يسار)"},
    "lg_dep": {
        "fr": "TVA / dépenses de l'État (éch. droite)",
        "ar": "الأداء على القيمة المضافة / نفقات الدولة (يمين)"},
    "y_pib": {"fr": "En % du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "y_dep": {"fr": "En % des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "xlabel": {"fr": "Année", "ar": "السنة"},
    "title": {"fr": "Ce que rapporte la taxe sur la valeur ajoutée, 1986-2025",
              "ar": "مردود الأداء على القيمة المضافة، 1986-2025"},
    "rupture": {"fr": "création de la TVA\n(loi n° 88-61, 1er juillet 1988)",
                "ar": "إحداث الأداء على القيمة المضافة\n(القانون عدد 88-61، 1 جويلية 1988)"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_pib": {"fr": "% du PIB (ministère des Finances)",
                "ar": "% من الناتج المحلي الإجمالي (وزارة المالية)"},
    "col_pib_cnat": {"fr": "% du PIB (comptes nationaux)",
                     "ar": "% من الناتج المحلي الإجمالي (الحسابات القومية)"},
    "col_dep": {"fr": "% des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "col_rec": {"fr": "% des recettes fiscales", "ar": "% من المداخيل الجبائية"},
    "col_mdt": {"fr": "TVA (MDT)", "ar": "الأداء على القيمة المضافة (م.د)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _donnees():
    """Les deux séries jointes sur l'année, avec les ratios au PIB et aux dépenses.

    La composition des recettes porte le montant de TVA ; les ratios de l'impôt sur le
    revenu portent les deux PIB et les dépenses totales. Aucune des deux ne porte tout.
    """
    comp = figtools.series(SERIE_COMPOSITION)
    rat = figtools.series(SERIE_RATIOS)
    d = comp[["annee", "tva_MDT", "tva_pct"]].merge(
        rat[["annee", "pib_minfin_MDT", "pib_cnat_MDT", "depenses_totales_MDT"]],
        on="annee", how="left")
    d["tva_sur_pib_pct"] = 100 * d["tva_MDT"] / d["pib_minfin_MDT"]
    d["tva_sur_pib_cnat_pct"] = 100 * d["tva_MDT"] / d["pib_cnat_MDT"]
    d["tva_sur_depenses_pct"] = 100 * d["tva_MDT"] / d["depenses_totales_MDT"]
    return d


def table():
    d = _donnees()
    cols = ["annee", "tva_sur_pib_pct", "tva_sur_depenses_pct",
            "tva_sur_pib_cnat_pct", "tva_pct", "tva_MDT"]
    w = d[cols].copy()
    for c in ("tva_sur_pib_pct", "tva_sur_depenses_pct",
              "tva_sur_pib_cnat_pct", "tva_pct"):
        w[c] = w[c].round(2)
    return w.rename(columns={
        "annee": _lab("col_annee"),
        "tva_sur_pib_pct": _lab("col_pib"),
        "tva_sur_depenses_pct": _lab("col_dep"),
        "tva_sur_pib_cnat_pct": _lab("col_pib_cnat"),
        "tva_pct": _lab("col_rec"),
        "tva_MDT": _lab("col_mdt"),
    })


def prepare(generated: str | None = None):
    d = _donnees()
    figtools.write_figdata(
        table(), FIGDATA / "fig_tva_rendement.csv", SERIE_COMPOSITION, SERIE_RATIOS,
        note=("rendement de la TVA en points de PIB et en part des dépenses de l'État, "
              "1986-2025 ; rupture de série en 1988, les exercices antérieurs portant les "
              "taxes sur le chiffre d'affaires remplacées par le code de 1988 ; les "
              "dépenses totales ne sont publiées qu'à partir de 1990"),
        generated=generated)
    return d


def fig_rendement():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    avant = d[d["annee"] < ANNEE_TVA]
    apres = d[d["annee"] >= ANNEE_TVA]
    depenses = d[d["annee"] >= ANNEE_DEPENSES]

    fig, ax1 = plt.subplots(figsize=(9.5, 5.2))
    ax2 = ax1.twinx()

    # La bande grise couvre les années où la rubrique mesure autre chose que la TVA.
    ax1.axvspan(d["annee"].min() - 0.5, ANNEE_TVA - 0.5, color="#8b949e", alpha=0.13, lw=0)
    ax1.axvline(ANNEE_TVA - 0.5, color="#57606a", lw=1.2, ls="--")

    l0, = ax1.plot(avant["annee"], avant["tva_sur_pib_pct"], "o:", color="#57606a",
                   lw=1.6, ms=4, label=ft(_lab("lg_avant")))
    # Le vert est celui de la bande « TVA » de la figure de composition du chapitre : une
    # même couleur pour un même impôt, d'une figure à l'autre. Le rouge de l'axe droit
    # reprend la convention de la figure de l'impôt sur le revenu, où il porte déjà le
    # rapport aux dépenses de l'État.
    l1, = ax1.plot(apres["annee"], apres["tva_sur_pib_pct"], "o-", color="#2da44e",
                   lw=2, ms=4, label=ft(_lab("lg_pib")))
    l2, = ax2.plot(depenses["annee"], depenses["tva_sur_depenses_pct"], "s--",
                   color="#d1242f", lw=1.8, ms=3, label=ft(_lab("lg_dep")))

    # L'annotation se place dans la moitié basse du cadre de gauche : les deux courbes
    # occupent le haut sur toute la fin de période.
    bas, haut = ax1.get_ylim()
    y_texte = bas + 0.15 * (haut - bas)
    ax1.annotate(ft(_lab("rupture")), xy=(ANNEE_TVA - 0.5, y_texte),
                 xytext=(ANNEE_TVA + 2.0, y_texte),
                 fontsize=8, color="#57606a", va="center",
                 arrowprops=dict(arrowstyle="->", color="#57606a", lw=1))

    ax1.set_ylabel(ft(_lab("y_pib")), color="#2da44e")
    ax2.set_ylabel(ft(_lab("y_dep")), color="#d1242f")
    ax1.set_xlabel(ft(_lab("xlabel")))
    ax1.set_title(ft(_lab("title")))
    ax1.grid(True, alpha=0.3)
    ax1.legend(handles=[l0, l1, l2], loc="lower right", fontsize=8.5)
    fig.tight_layout()
    return fig

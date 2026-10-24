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

LE PIB EST CELUI DE CHAQUE BASE DES COMPTES NATIONAUX (1983, 1997, 2015), jamais raccordées : voir
`figures/rendement_bases.py`, qui trace et tabule le rendement base par base.
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
from figures import rendement_bases as rb  # noqa: E402

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


NOM = {"fr": "Droits de consommation", "ar": "المعلوم على الاستهلاك"}
SERIES_RENDEMENT = rb.SERIES


def _nom() -> str:
    return NOM.get(figtools.lang(), NOM["fr"])


def table():
    return rb.tableau("consommation_MDT", "consommation_pct", _nom())


def fig_rendement():
    return rb.figure("consommation_MDT", "consommation_pct", nom=_nom(),
                     annee_debut=ANNEE_DC, titre=_lab("title"), rupture=_lab("rupture"),
                     y_rupture=0.12)

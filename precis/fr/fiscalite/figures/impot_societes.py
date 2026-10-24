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


NOM = {"fr": "Impôt sur les sociétés", "ar": "الضريبة على الشركات"}
SERIES_RENDEMENT = rb.SERIES


def _nom() -> str:
    return NOM.get(figtools.lang(), NOM["fr"])


def table():
    return rb.tableau("is_MDT", "is_pct", _nom())


def fig_rendement():
    return rb.figure("is_MDT", "is_pct", nom=_nom(), annee_debut=ANNEE_IS,
                     titre=_lab("title"), rupture=_lab("rupture"), y_rupture=0.62)

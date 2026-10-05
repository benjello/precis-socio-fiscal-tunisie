"""Nuages de points : barème légal 1999 et sinistralité CNAM 2021–2023.

Un point de l'article 2 du décret n° 99-1010 n'est attribué à une rubrique
CNAM que si son intitulé correspond et si tous les sous-secteurs susceptibles
de la composer portent le même taux. Le taux du barème n'est ni le taux
effectivement acquitté ni une fréquence d'accident ; ce rapprochement ne
montre pas un effet de la cotisation sur le risque.

Les secteurs larges sans taux unique (chimie, transport, bois/liège, services,
etc.) sont écartés. Les trois rubriques absentes du tableau des décès ne sont
pas traitées comme des secteurs à zéro décès.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

# Enregistre la provenance du barème déjà émis hors build, sans ouvrir ses paramètres.
from figures import atmp_echelles as _bareme  # noqa: F401, E402

ACCIDENTS = "cnam-atmp-2023-ventilations-brutes"
FREQUENCE_MORTS = "cnam-atmp-2023-activites-frequence-mortels-bruts"
BAREME = "atmp-echelles-1995-1999"

# rang de l'activité CNAM (PDF 13 et 15/26) : traduction, points du décret 1999.
# Les dix sous-activités agro-alimentaires ont TOUTES le taux de 1,6 %.
# Les autres correspondances reprennent le libellé spécifique du texte.
SECTEURS = {
    1: ("Confection", ("14-2",)),
    2: ("Alimentation et boissons", tuple(f"6-{n}" for n in range(1, 11))),
    6: ("Bâtiment et travaux publics", ("23",)),
    13: ("Hôtellerie", ("33",)),
    14: ("Industrie plastique", ("22-14",)),
    15: ("Fonderie et sidérurgie", ("10",)),
    17: ("Industrie textile", ("14-1",)),
    18: ("Industrie du meuble", ("16",)),
    19: ("Services de bureaux", ("1",)),
    20: ("Industries extractives", ("29",)),
}
ANNEES = (2021, 2022, 2023)
COULEURS = {2021: "#57606a", 2022: "#bf8700", 2023: "#08519c"}

_L = {
    "secteur": {"fr": "Activité CNAM", "ar": "نشاط الكنام"},
    "point": {"fr": "Point du décret n° 99-1010", "ar": "عدد الأمر 1010 لسنة 1999"},
    "legal": {"fr": "Taux du barème 1999 (%)", "ar": "نسبة جدول 1999 (%)"},
    "freq": {"fr": "Accidents avec arrêt / 1 000 assujettis",
             "ar": "حوادث بتوقّف عن العمل / ألف عامل"},
    "cas": {"fr": "Accidents déclarés (cas)", "ar": "حوادث مصرّح بها"},
    "deces": {"fr": "Accidents mortels (cas)", "ar": "حوادث قاتلة"},
    "mortalite": {"fr": "Accidents mortels / 1 000 accidents déclarés",
                  "ar": "حوادث قاتلة / ألف حادث مصرّح به"},
    "repere": {"fr": "Repère sur la figure", "ar": "رمز النقطة في الرسم"},
    "annee": {"fr": "Année", "ar": "السنة"},
    "page": {"fr": "Pages PDF (taux / fréquence / accidents / décès)",
             "ar": "صفحات PDF (الاشتراك / التواتر / الحوادث / الوفيات)"},
    "title_freq": {"fr": "Taux légal AT/MP (barème 1999) et fréquence des accidents, 2021–2023",
                   "ar": "نسبة الاشتراك القانونية حسب جدول 1999 وتواتر الحوادث، 2021–2023"},
    "title_morts": {"fr": "Taux légal AT/MP (barème 1999) et part des accidents mortels, 2021–2023",
                    "ar": "نسبة الاشتراك القانونية حسب جدول 1999 وحصة الحوادث القاتلة، 2021–2023"},
    "corr": {"fr": "r de Pearson", "ar": "معامل ارتباط بيرسون"},
}


def _lab(key):
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _lignes():
    """Rassemble les sources sans reconstituer un taux patronal moyen par secteur."""
    tarifs = figtools.series(BAREME)
    tarifs = tarifs[tarifs.echelle.astype(str) == "1999"].copy()
    tarifs.point = tarifs.point.astype(str)
    cas = figtools.series(ACCIDENTS)
    cas = cas[(cas.indicateur == "accidents") & (cas.ventilation == "activité")]
    autres = figtools.series(FREQUENCE_MORTS)
    resultats = []
    for rang, (fr, points) in SECTEURS.items():
        sous_tarifs = tarifs[tarifs.point.isin(points)]
        if set(sous_tarifs.point) != set(points) or sous_tarifs.taux.nunique() != 1:
            raise ValueError(f"{rang} : sous-secteurs du barème incomplets ou taux différents")
        taux = float(sous_tarifs.taux.iloc[0]) * 100
        for an in ANNEES:
            c = cas[(cas.rang == rang) & (cas.annee == an)]
            f = autres[(autres.rang == rang) & (autres.annee == an) &
                       (autres.indicateur == "fréquence des accidents avec arrêt")]
            m = autres[(autres.rang == rang) & (autres.annee == an) &
                       (autres.indicateur == "accidents mortels")]
            if any(len(g) != 1 for g in (c, f, m)):
                raise ValueError(f"{rang}, {an} : catégorie absente ou doublonnée")
            c, f, m = (g.iloc[0] for g in (c, f, m))
            if c.libelle_ar != f.libelle_ar or c.libelle_ar != m.libelle_ar:
                raise ValueError(f"{rang}, {an} : les rubriques CNAM ne concordent pas")
            resultats.append(dict(rang=rang, fr=fr, ar=c.libelle_ar, annee=an,
                                  points=", ".join(points), taux=taux,
                                  frequence=float(f.valeur), cas=int(c.valeur),
                                  deces=int(m.valeur)))
    return resultats


def table():
    import pandas as pd

    langue = figtools.lang()
    return pd.DataFrame([{
        _lab("repere"): chr(65 + list(SECTEURS).index(ligne["rang"])),
        _lab("secteur"): ligne[langue], _lab("point"): ligne["points"],
        _lab("legal"): ligne["taux"], _lab("annee"): ligne["annee"],
        _lab("freq"): ligne["frequence"], _lab("cas"): ligne["cas"],
        _lab("deces"): ligne["deces"],
        _lab("mortalite"): round(1000 * ligne["deces"] / ligne["cas"], 2),
        _lab("page"): "JORT art. 2 / 15 / 13 / 26",
    } for ligne in _lignes()])


def _nuage(indicateur):
    """Chaque année : dix observations, droite des moindres carrés et r de Pearson.

    La droite décrit l'association brute dans ces dix rubriques choisies ;
    ni pondération par effectifs ni extrapolation à d'autres secteurs.
    """
    figtools.apply_lang_font()
    lignes = _lignes()
    fig, ax = plt.subplots(figsize=(11.5, 7.5))
    for an in ANNEES:
        valeurs = [d for d in lignes if d["annee"] == an]
        x = np.array([d["taux"] for d in valeurs])
        y = np.array([d["frequence"] if indicateur == "freq" else
                      1000 * d["deces"] / d["cas"] for d in valeurs])
        pente, origine = np.polyfit(x, y, 1)
        corr = np.corrcoef(x, y)[0, 1]
        grille = np.linspace(x.min(), x.max(), 100)
        ax.plot(grille, pente * grille + origine, "--", color=COULEURS[an],
                lw=1.2, alpha=.85)
        ax.scatter(x, y, s=58, color=COULEURS[an], edgecolor="white", linewidth=.8,
                   zorder=3, label=f"{an} · {_lab('corr')} = {corr:+.2f}".replace(".", ","))
        if an == 2023:
            for i, (x_i, y_i) in enumerate(zip(x, y)):
                ax.annotate(chr(65 + i), (x_i, y_i), xytext=(4, 5),
                            textcoords="offset points", color=COULEURS[an], fontsize=8)
    ax.set_xlim(0, 4.15)
    ax.set_ylim(bottom=0)
    ax.set_xlabel(figtools.fig_text(_lab("legal")))
    ax.set_ylabel(figtools.fig_text(_lab("freq" if indicateur == "freq" else "mortalite")))
    ax.set_title(figtools.fig_text(_lab("title_freq" if indicateur == "freq" else "title_morts")))
    ax.grid(alpha=.25)
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    cle = [f"{chr(65 + i)} · {SECTEURS[rang][0] if figtools.lang() == 'fr' else next(d['ar'] for d in lignes if d['rang'] == rang)}"
           for i, rang in enumerate(SECTEURS)]
    fig.text(.5, .025, figtools.fig_text("   |   ".join(cle[:5])) + "\n" +
             figtools.fig_text("   |   ".join(cle[5:])), ha="center", va="bottom", fontsize=8)
    fig.tight_layout(rect=(0, .095, 1, 1))
    return fig


def fig_accidents():
    return _nuage("freq")


def fig_mortalite():
    return _nuage("mortalite")

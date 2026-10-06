"""Figure « les plus gros dispositifs dérogatoires » du livre *Fiscalité*.

PAS APPELÉE PAR LE CHAPITRE « Les dépenses fiscales et les régimes d'incitation »
(`_depenses_fiscales.qmd`), et à ne pas appeler en l'état : la série cousue ci-dessous
porte une rupture de périmètre (voir « TROIS RAPPORTS COUSUS »). Le code est inchangé ;
il est à reprendre quand la série aura été reconstruite périmètre par périmètre.

Sélection : parmi les dispositifs chiffrés **les sept années** de 2017 à 2023, les huit dont
le coût moyen est le plus élevé. Les plus gros et les plus longs, donc — ceux qu'on peut
suivre sans trou et qui pèsent réellement.

TROIS RAPPORTS COUSUS. La série vient de trois rapports annexés aux lois de finances, qui se
chevauchent et se révisent entre eux. On retient le millésime le plus récent pour chaque
exercice, et la figure marque les deux coutures.

LA COUTURE 2019/2020 EST UNE RUPTURE DE PÉRIMÈTRE, et non un simple changement de source
(`docs/notes/fiscalite-depenses-fiscales.md`, § 2.2). Les rapports annexés aux projets de
loi de finances pour 2024 et 2025 donnent leurs montants sans les dépenses fiscales liées
à l'exonération des médicaments et des engrais ; le rapport annexé au projet pour 2021
les compte (tableau n° 9, exercice 2019 : 274,5 MD de médicaments et articles
paramédicaux, 249,9 MD d'engrais). Dans la série traitée, les lignes dont le libellé
nomme médicaments, pharmacie ou engrais passent de 321,8 MD en 2019 à 32,1 MD en 2020 puis
0,0 MD en 2023. La ligne « TVA : médicaments et produits paramédicaux » (222001333), l'une
des huit que la sélection peut retenir, porte donc cet artefact : sa chute entre 2019 et
2020 n'est pas une baisse du coût. La couture 2020/2021 (rapport 2024 → rapport 2025) n'a
pas été examinée sous cet angle. Les rapports annexés aux projets pour 2022 et 2023 ne
sont pas dans la série.
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
SERIE = "depenses-fiscales-detail"

# Millésime retenu pour chaque exercice : le plus récent qui le couvre.
MILLESIME = {2017: "LF2021", 2018: "LF2021", 2019: "LF2021", 2020: "LF2024",
             2021: "LF2025", 2022: "LF2025", 2023: "LF2025"}
COUTURES = [2019.5, 2020.5]  # entre deux rapports
NB = 8

# Intitulés courts, tirés des libellés complets du rapport — ceux-ci font jusqu'à 650
# caractères et ne tiennent pas dans une légende. Le libellé intégral reste dans l'onglet
# « Données ».
COURTS = {
    232000801: {"fr": "Droit de consommation : véhicules de tourisme (concessionnaires)",
                "ar": "معلوم الاستهلاك: سيارات سياحية (وكلاء السيارات)"},
    222001331: {"fr": "TVA : produits alimentaires de consommation",
                "ar": "الأداء على القيمة المضافة: المواد الغذائية الاستهلاكية"},
    233001202: {"fr": "Droit de consommation : taxis, louages, transport rural",
                "ar": "معلوم الاستهلاك: سيارات التاكسي واللواج والنقل الريفي"},
    121107702: {"fr": "IS : souscriptions au capital-risque (SICAR, FCPR)",
                "ar": "الضريبة على الشركات: الاكتتاب في رأس المال الاستثماري"},
    222001333: {"fr": "TVA : médicaments et produits paramédicaux",
                "ar": "الأداء على القيمة المضافة: الأدوية والمنتجات شبه الطبية"},
    232000901: {"fr": "Droit de consommation : véhicules 4 chevaux et populaires",
                "ar": "معلوم الاستهلاك: سيارات 4 خيول والسيارة الشعبية"},
    121601202: {"fr": "IS : entreprises totalement exportatrices",
                "ar": "الضريبة على الشركات: المؤسسات المصدّرة كلّياً"},
    212001308: {"fr": "Droits de douane : aliments fourragers",
                "ar": "المعاليم الديوانية: الأعلاف"},
}

_L = {
    "y": {"fr": "Coût pour l'État (millions de dinars)",
          "ar": "الكلفة على الدولة (بملايين الدنانير)"},
    "x": {"fr": "Année", "ar": "السنة"},
    "titre": {"fr": "Les huit dispositifs dérogatoires les plus coûteux, suivis de 2017 à 2023",
              "ar": "الإجراءات الاستثنائية الثمانية الأكثر كلفة، من 2017 إلى 2023"},
    "couture": {"fr": "changement de rapport", "ar": "تغيير التقرير"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_code": {"fr": "Code", "ar": "الرمز"},
    "col_impot": {"fr": "Impôt", "ar": "الضريبة"},
    "col_montant": {"fr": "Coût (MD)", "ar": "الكلفة (م.د)"},
    "col_lib": {"fr": "Dispositif", "ar": "الإجراء"},
    "col_rapport": {"fr": "Rapport", "ar": "التقرير"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _court(code: int) -> str:
    return COURTS.get(code, {}).get(figtools.lang(), str(code))


def _retenu():
    """Les lignes du millésime retenu pour chaque exercice."""
    d = figtools.series(SERIE)
    return d[[MILLESIME.get(a) == r for a, r in zip(d["annee"], d["rapport"])]]


def _selection():
    """Les NB dispositifs chiffrés les sept années, par coût moyen décroissant."""
    v = _retenu()
    v = v[v["montant_MDT"].notna()]
    g = v.groupby("code").agg(annees=("annee", "nunique"), moyenne=("montant_MDT", "mean"))
    return list(g[g["annees"] == 7].nlargest(NB, "moyenne").index)


def table():
    v = _retenu()
    v = v[v["code"].isin(_selection()) & v["montant_MDT"].notna()]
    w = v[["annee", "code", "impot", "montant_MDT", "libelle_fr", "rapport"]].copy()
    w["libelle_fr"] = w["libelle_fr"].fillna("")
    return w.rename(columns={
        "annee": _lab("col_annee"), "code": _lab("col_code"), "impot": _lab("col_impot"),
        "montant_MDT": _lab("col_montant"), "libelle_fr": _lab("col_lib"),
        "rapport": _lab("col_rapport")})


def prepare(generated: str | None = None):
    figtools.write_figdata(
        table(), FIGDATA / "fig_depenses_fiscales.csv", SERIE,
        note="les huit dispositifs dérogatoires les plus coûteux, 2017-2023",
        generated=generated)


def fig_top():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    v = _retenu()
    codes = _selection()
    fig, ax = plt.subplots(figsize=(10, 5.8))
    couleurs = plt.cm.tab10.colors
    for i, code in enumerate(codes):
        s = v[v["code"] == code].sort_values("annee")
        ax.plot(s["annee"], s["montant_MDT"], "o-", lw=1.9, ms=4.5,
                color=couleurs[i % 10], label=ft(_court(code)))
    for x in COUTURES:
        ax.axvline(x, color="#8b949e", lw=1, ls=":")
    bas, haut = ax.get_ylim()
    ax.text(COUTURES[0] + 0.08, bas + 0.94 * (haut - bas), ft(_lab("couture")),
            fontsize=7.5, color="#8b949e", va="top")
    ax.set_ylabel(ft(_lab("y")))
    ax.set_xlabel(ft(_lab("x")))
    ax.set_title(ft(_lab("titre")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=8,
              frameon=False)
    fig.tight_layout()
    return fig

"""Figures du chapitre « Les droits de douane » du livre *Fiscalité*.

QUATRE FIGURES, UN SEUL NUMÉRATEUR. `fig_parts`, `fig_pib`, `fig_rendement` et
`fig_perception` mesurent la rubrique « droits de douane » du ministère des Finances. Cette
rubrique COMPREND les redevances de prestations douanières : elle égale, pour chaque prévision
contrôlée, la somme des articles 21-01, 21-02 et 21-03 du tableau A (17-01 et 17-02 depuis
2020). Chaque légende le dit. Seule `fig_rendement` sépare les droits et la redevance.

BUDGÉTAIRE D'ABORD. `fig_parts`, `fig_pib` et `fig_rendement` sont budgétaires seules. Dans
`fig_perception`, deux familles se superposent sur un même axe en pourcentage, mais
distinguées par la forme du tracé et par deux légendes : le taux de perception implicite
(budgétaire rapporté à une statistique publique, calcul du précis) et les moyennes simples des
taux du tarif que publient le GATT et l'OMC (rapports extérieurs, chacune avec sa définition).
Les indicateurs de la Banque mondiale (WDI) en sont exclus.

D'OÙ VIENNENT LES DONNÉES.
  - rubrique du ministère et dénominateurs : `figtools.series()` — « recettes-fiscales-
    composition » (rubrique, recettes fiscales), « denominateurs-depenses-etat-pib »
    (dépenses de l'État hors service de la dette, PIB avec son segment de base) ;
  - importations 1998-2023 : « ins-commerce-exterieur-par-regime » (*Annuaire statistique* de
    l'INS, tableau 14.2) ;
  - prévisions du tableau A et réalisations de la Cour des comptes : relevé versionné DANS le
    livre (`douane/rendement-droits-douane.csv`, avec son manifeste) ;
  - importations 1988-1997 de la Banque centrale et moyennes simples des rapports extérieurs :
    relevé `douane/importations-perception.csv`.

LA NOMENCLATURE DU TABLEAU A CHANGE EN 2020 ET LA SÉRIE SE RACCORDE (17-01 = 21-01 ;
17-02 = 21-02 + 21-03). Contrairement au droit de timbre, aucune courbe n'est coupée : un trait
vertical marque la nouvelle nomenclature sur une courbe continue.

PIB PAR SEGMENTS, JAMAIS CHAÎNÉS (`fig_pib`). Un segment par base : 1986-1991 (base 1983
présumée), 1992-1996 (base 1983), 1997-2001 (base 1997, rétropolée), 2002-2004 (valeur propre
au ministère, rattachée à aucune base), 2005-2009 (base 1997), 2010-2024 (base 2015),
2025 (valeur propre au ministère, rattachée à aucune base). Aucun trait n'unit deux segments ;
le changement de base est une rupture (annexe sur le PIB).

LE TAUX DE PERCEPTION EST CALCULÉ, NON PUBLIÉ : rubrique du ministère / importations CAF. Les
importations de 1988-1997 sont celles de la Banque centrale, celles de 1998-2023 de l'INS : la
source change en 1998 (9 489 millions de dinars à la Banque centrale, 9 489,5 à l'INS), sans
rupture de niveau. Entre 2003 et 2004 la série de l'INS se coupe, comme celle du régime off
shore dans `commerce_exterieur_regime.py` : les années 2003 et antérieures ne sont imprimées
dans aucune édition postérieure à la révision du régime off shore.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402
import dinars_constants  # noqa: E402

HERE = Path(__file__).resolve().parent
RELEVES = HERE.parent / "douane"
NOM_REND = "rendement-droits-douane"
NOM_PERC = "importations-perception"

SERIE_COMPOSITION = "recettes-fiscales-composition"
SERIE_DEN = "denominateurs-depenses-etat-pib"
SERIE_INS = "ins-commerce-exterieur-par-regime"
SERIE_REND = "droits-douane-rendement"
SERIE_PERC = "droits-douane-perception"

SERIE_PARTS = "droits-douane-parts"
SERIE_PIB = "droits-douane-pib"
SERIES_PARTS = (SERIE_PARTS,)
SERIES_PIB = (SERIE_PIB,)
SERIES_REND = (SERIE_REND, *dinars_constants.SERIES_IPC)
SERIES_PERC = (SERIE_PERC, SERIE_COMPOSITION, SERIE_INS)

BASE = dinars_constants.ANNEE_BASE
ANNEE_NOMENCLATURE = 2020  # tableau A : 17-01 et 17-02 remplacent 21-01 à 21-03
# Années de rupture du PIB : changement de base ou de source, au sens de l'annexe sur le PIB.
RUPTURES_PIB = (1997, 2002, 2005, 2010, 2025)
# Première année de la série de l'INS imprimée dans une édition postérieure à la révision du
# régime off shore.
ANNEE_RUPTURE_INS = 2004

ROUGE = "#d1242f"      # douanes, comme dans la figure de composition des recettes
BLEU = "#0969da"
VIOLET = "#8250df"
ORANGE = "#bc4c00"
GRIS = "#57606a"

_L = {
    # fig_parts
    "lg_recettes": {"fr": "Part des recettes fiscales", "ar": "حصة المداخيل الجبائية"},
    "lg_depenses": {"fr": "Part des dépenses de l'État hors service de la dette",
                    "ar": "حصة نفقات الدولة دون خدمة الدين"},
    "y_pct": {"fr": "En %", "ar": "%"},
    "x": {"fr": "Année", "ar": "السنة"},
    "title_parts": {
        "fr": "La rubrique « droits de douane », redevances comprises, 1986-2025",
        "ar": "خانة «المعاليم الديوانية»، بما فيها الأتاوة، 1986-2025"},
    "rep_1988": {"fr": "1988 : tarif de la loi de\nfinances pour 1988", "ar": "1988"},
    "rep_1997": {"fr": "1997 : accord d'association\navec l'Union européenne", "ar": "1997"},
    "rep_2016": {"fr": "2016 : réduction des taux\n(chapitres 25 à 97)", "ar": "2016"},
    "rep_2018": {"fr": "2018 : relèvements de taux", "ar": "2018"},
    "rep_nomen": {"fr": "2020 : nouvelle nomenclature\ndu tableau A, série continue",
                  "ar": "2020"},
    # fig_pib
    "y_pib": {"fr": "En % du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "title_pib": {"fr": "Part de la rubrique « droits de douane » dans le PIB, 1986-2025",
                  "ar": "حصة خانة «المعاليم الديوانية» من الناتج المحلي الإجمالي، 1986-2025"},
    "lg_base": {"fr": "base du PIB établie (1983, 1997, 2015)",
                "ar": "أساس الناتج المحلي الإجمالي ثابت (1983، 1997، 2015)"},
    "lg_presumee": {"fr": "base 1983 présumée (1986-1991)",
                    "ar": "أساس 1983 مفترض (1986-1991)"},
    "lg_non_rattachee": {
        "fr": "valeur du ministère des Finances rattachée à aucune base (2002-2004, 2025)",
        "ar": "قيمة وزارة المالية غير مرتبطة بأي أساس (2002-2004، 2025)"},
    "retro": {"fr": "rétropolée {a}-{b}", "ar": "مُرجَعة {a}-{b}"},
    "nr": {"fr": "n. r.", "ar": "غ. م."},
    "cadre_pib": {
        "fr": "au-dessus du cadre : base du PIB de chaque segment ; « n. r. » : valeur propre au ministère des Finances, rattachée à aucune base",
        "ar": "فوق الإطار: أساس الناتج المحلي الإجمالي لكل مقطع؛ «غ. م.»: قيمة خاصة بوزارة المالية غير مرتبطة بأي أساس"},
    "rup_pib": {"fr": "PIB : base {b}", "ar": "الناتج المحلي الإجمالي: أساس {b}"},
    # fig_rendement
    "lg_droits": {"fr": "Droits de douane à l'importation", "ar": "المعاليم الديوانية عند التوريد"},
    "lg_redevance": {"fr": "Redevance de prestations douanières", "ar": "الأتاوة على الخدمات الديوانية"},
    "prev": {"fr": "prévision (loi de finances)", "ar": "تقديرات (قانون المالية)"},
    "real": {"fr": "réalisation (Cour des comptes)", "ar": "إنجازات (محكمة المحاسبات)"},
    "rupture_nomen": {"fr": "nouvelle nomenclature du\ntableau A (2020), série continue",
                      "ar": "تبويب جديد للجدول أ (2020)، سلسلة متصلة"},
    "y_cour": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "y_cst": {"fr": f"Millions de dinars de {BASE}", "ar": f"ملايين الدنانير بأسعار {BASE}"},
    "vue_cour": {"fr": "Dinars courants", "ar": "بالدينار الجاري"},
    "vue_cst": {"fr": f"Dinars de {BASE}", "ar": f"بدينار سنة {BASE}"},
    # fig_perception
    "lg_taux_total": {"fr": "Taux de perception implicite : rubrique / ensemble des importations",
                      "ar": "نسبة الاستخلاص الضمنية: الخانة / مجموع الواردات"},
    "lg_taux_general": {
        "fr": "Taux de perception implicite : rubrique / importations du régime général",
        "ar": "نسبة الاستخلاص الضمنية: الخانة / واردات النظام العام"},
    "lg_bct": {"fr": "marqueur creux : importations de la Banque centrale (1988-1997) ; marqueur plein : INS (depuis 1998)",
               "ar": "علامة مفرغة: واردات البنك المركزي (1988-1997)؛ علامة ممتلئة: المعهد الوطني للإحصاء (منذ 1998)"},
    "ttl_budg": {"fr": "Rubrique « droits de douane » du ministère des Finances, redevances comprises, rapportée aux importations",
                 "ar": "خانة «المعاليم الديوانية» لوزارة المالية، بما فيها الأتاوة، مقيسة إلى الواردات"},
    "ttl_ext": {"fr": "Rapports extérieurs", "ar": "تقارير خارجية"},
    "lg_ext": {
        "fr": "moyenne simple des taux du tarif (GATT 1987-1989 ; OMC 1994, 2005-2016, 2025)",
        "ar": "المتوسط البسيط لنسب التعريفة (الغات 1987-1989؛ المنظمة العالمية للتجارة 1994، 2005-2016، 2025)"},
    "y_perc": {"fr": "En %", "ar": "%"},
    "title_perc": {
        "fr": "Taux de perception implicite et moyennes simples des taux du tarif, 1987-2025",
        "ar": "نسبة الاستخلاص الضمنية والمتوسطات البسيطة لنسب التعريفة، 1987-2025"},
    "rupture_ins": {"fr": "années antérieures absentes\ndes éditions révisées",
                    "ar": "السنوات السابقة غير واردة\nفي الطبعات المراجَعة"},
    # tables
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_rubrique": {"fr": "Rubrique « droits de douane », redevances comprises (MD)",
                     "ar": "خانة «المعاليم الديوانية» بما فيها الأتاوة (م.د)"},
    "col_rec": {"fr": "Recettes fiscales (MD)", "ar": "المداخيل الجبائية (م.د)"},
    "col_part_rec": {"fr": "Part des recettes fiscales (%)", "ar": "حصة المداخيل الجبائية (%)"},
    "col_dep": {"fr": "Dépenses de l'État hors dette (MD)", "ar": "نفقات الدولة دون الدين (م.د)"},
    "col_part_dep": {"fr": "Part des dépenses hors dette (%)", "ar": "حصة النفقات دون الدين (%)"},
    "col_pib": {"fr": "PIB (MD)", "ar": "الناتج المحلي الإجمالي (م.د)"},
    "col_part_pib": {"fr": "Part du PIB (%)", "ar": "حصة الناتج المحلي الإجمالي (%)"},
    "col_segment": {"fr": "Segment de PIB", "ar": "مقطع الناتج المحلي الإجمالي"},
    "col_retro": {"fr": "PIB rétropolé", "ar": "الناتج المحلي الإجمالي المُرجَع"},
    "col_nature": {"fr": "Nature", "ar": "الطبيعة"},
    "col_ligne": {"fr": "Ligne", "ar": "السطر"},
    "col_nomen": {"fr": "Nomenclature", "ar": "التبويب"},
    "col_code": {"fr": "Article du tableau A", "ar": "فصل الجدول أ"},
    "col_lib": {"fr": "Libellé de la source", "ar": "تسمية المصدر"},
    "col_md": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "col_cst": {"fr": f"Millions de dinars de {BASE}", "ar": f"ملايين الدنانير بأسعار {BASE}"},
    "col_trace": {"fr": "Tracée", "ar": "مرسومة"},
    "col_src": {"fr": "Source", "ar": "المصدر"},
    "col_page": {"fr": "Page", "ar": "الصفحة"},
    "col_rem": {"fr": "Remarque", "ar": "ملاحظة"},
    "col_imp": {"fr": "Importations (MD)", "ar": "الواردات (م.د)"},
    "col_imp_src": {"fr": "Source des importations", "ar": "مصدر الواردات"},
    "col_imp_gen": {"fr": "Importations du régime général (MD)",
                    "ar": "واردات النظام العام (م.د)"},
    "col_taux": {"fr": "Taux de perception implicite, ensemble (%)",
                 "ar": "نسبة الاستخلاص الضمنية، المجموع (%)"},
    "col_taux_gen": {"fr": "Taux de perception implicite, régime général (%)",
                     "ar": "نسبة الاستخلاص الضمنية، النظام العام (%)"},
    "col_moy": {"fr": "Moyenne simple des taux du tarif (%)",
                "ar": "المتوسط البسيط لنسب التعريفة (%)"},
    "col_moy_src": {"fr": "Source de la moyenne", "ar": "مصدر المتوسط"},
    "col_moy_trace": {"fr": "Moyenne tracée", "ar": "المتوسط مرسوم"},
}
# Libellés de ligne du relevé de rendement.
_LIGNES = {
    "droits_importation": {"fr": "Droits de douane à l'importation (21-01, 17-01)",
                           "ar": "المعاليم الديوانية عند التوريد (21-01، 17-01)"},
    "redevance_importation": {"fr": "Redevance à l'importation (21-02)",
                              "ar": "الأتاوة عند التوريد (21-02)"},
    "redevance_exportation": {"fr": "Redevance à l'exportation (21-03)",
                              "ar": "الأتاوة عند التصدير (21-03)"},
    "redevance": {"fr": "Redevance, importation et exportation (17-02)",
                  "ar": "الأتاوة، توريد وتصدير (17-02)"},
}


def _l(cle: str, **kw) -> str:
    texte = _L[cle].get(figtools.lang(), _L[cle]["fr"])
    return texte.format(**kw) if kw else texte


def _nb(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _sources(nom: str) -> list[str]:
    import yaml
    return list(yaml.safe_load(
        (RELEVES / f"{nom}.csv.yml").read_text(encoding="utf-8"))["sources"])


figtools.register_provenance(
    SERIE_REND,
    titre=("Droits de douane et redevance de prestations douanières : prévisions des lois de "
           "finances (2001-2026) et réalisations de la Cour des comptes (2018-2024)"),
    sources=_sources(NOM_REND),
    unite="millions de dinars courants",
    perimetre=("articles 21-01 à 21-03 (17-01 et 17-02 depuis 2020) du tableau A des lois de "
               "finances initiales ; réalisations relevées dans les rapports de la Cour des "
               "comptes sur la clôture du budget de l'État"),
    caveats=("Prévisions et réalisations ne se confondent pas. La nomenclature du tableau A "
             "change en 2020 et la série se raccorde : 17-01 = 21-01 ; 17-02 = 21-02 + "
             "21-03. Les articles 21-02 de 2009 et de 2013 sont imprimés avec le libellé "
             "« droits de douane à l'exportation » et lus comme la redevance à "
             "l'importation. La rubrique « droits de douane » du ministère comprend la "
             "redevance."),
)

figtools.register_provenance(
    SERIE_PARTS,
    titre=("Rubrique « droits de douane » du ministère des Finances : part des recettes "
           "fiscales et des dépenses de l'État hors service de la dette, 1986-2025"),
    sources=["minfin-recettes-fiscales", "minfin-remunerations"],
    unite="millions de dinars courants ; pourcentage",
    perimetre=("réalisations de la rubrique « droits de douane », qui comprend les "
               "redevances de prestations douanières ; recettes fiscales de l'État ; "
               "dépenses de l'État hors service de la dette"),
    caveats=("La rubrique « droits de douane » comprend la redevance de prestations "
             "douanières. Les dépenses de l'État sont des réalisations. La nomenclature du "
             "tableau A change en 2020 sans interrompre la rubrique du ministère."),
)

figtools.register_provenance(
    SERIE_PIB,
    titre=("Rubrique « droits de douane » du ministère des Finances : part du PIB, par "
           "segment de base, 1986-2025"),
    sources=["minfin-recettes-fiscales", "minfin-indicateurs-fp", "ins-cnat-2015"],
    unite="millions de dinars courants ; pourcentage du PIB",
    perimetre=("réalisations de la rubrique « droits de douane », qui comprend les "
               "redevances de prestations douanières ; PIB de l'année, par segment de base"),
    caveats=("Le PIB n'est pas chaîné : base 1983 présumée de 1986 à 1991, base 1983 de 1992 "
             "à 1996, base 1997 de 1997 à 2001 (rétropolée) et de 2005 à 2009, valeur propre "
             "au ministère des Finances, rattachée à aucune base, de 2002 à 2004 et en 2025, "
             "base 2015 de l'INS de 2010 à 2024 (rétropolée pour 2010-2014). Chaque "
             "changement de base est une rupture."),
)

figtools.register_provenance(
    SERIE_PERC,
    titre=("Importations de la Banque centrale (1988-1997) et moyennes simples des taux du "
           "tarif des rapports du GATT et de l'OMC"),
    sources=_sources(NOM_PERC),
    unite="millions de dinars courants ; pourcentage",
    perimetre=("importations CAF de biens, 1988-1997 ; moyennes simples des taux du tarif "
               "publiées par le GATT (1994) et l'OMC (2005, 2016, 2025)"),
    caveats=("Le taux de perception implicite est un calcul du précis, non une valeur "
             "publiée : rubrique « droits de douane » du ministère (redevances comprises) "
             "divisée par les importations CAF. Les moyennes simples des rapports extérieurs "
             "diffèrent par la définition (neuf ou onze chiffres, droits complémentaires "
             "provisoires compris ou non) ; elles ne sont pas des taux de perception."),
)


# --- lecture ------------------------------------------------------------------------------

def _composition() -> pd.DataFrame:
    return figtools.series(SERIE_COMPOSITION).set_index("annee")


def _denominateurs() -> pd.DataFrame:
    return figtools.series(SERIE_DEN).set_index("annee")


def _parts() -> pd.DataFrame:
    c = _composition()
    d = _denominateurs()
    out = pd.DataFrame({"rubrique": c["douanes_MDT"], "recettes": c["total_MDT"],
                        "part_recettes": c["douanes_pct"]})
    out["depenses"] = d["depenses_etat_hors_dette_MDT"]
    out["part_depenses"] = out["rubrique"] / out["depenses"] * 100
    out["pib"] = d["pib_MDT"]
    out["part_pib"] = out["rubrique"] / out["pib"] * 100
    out["segment"] = d["segment_pib"]
    out["retro"] = d["pib_retropole"]
    out["rupture_pib"] = d["rupture_pib"]
    return out.loc[1986:2025]


def _releve_rendement() -> pd.DataFrame:
    return pd.read_csv(RELEVES / f"{NOM_REND}.csv")


def _releve_perception() -> pd.DataFrame:
    return pd.read_csv(RELEVES / f"{NOM_PERC}.csv")


def _cadre(ax, titre: str, ylabel: str, x0: int, x1: int) -> None:
    ax.set_title(figtools.fig_text(titre), fontsize=10.5)
    ax.set_ylabel(figtools.fig_text(ylabel))
    ax.set_xlabel(figtools.fig_text(_l("x")))
    ax.set_xlim(x0 - 0.7, x1 + 0.7)
    ax.set_xticks(list(range(x0 + (x0 % 2), x1 + 1, 2)))
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)


def _legende(ax, poignees, ncol: int = 1) -> None:
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=ncol,
              fontsize=7.5, frameon=False)


def _repere(ax, annee: int, cle: str, *, couleur: str = GRIS, ls=(0, (2, 2)), lw: float = 1.0,
            y: float = 0.98, bas: bool = False) -> None:
    """Trait vertical à l'entrée en vigueur d'une année (entre `annee - 1` et `annee`), avec
    son libellé à la verticale le long du trait ; `bas` pose le libellé au pied du trait."""
    x = annee - 0.5
    ax.axvline(x, color=couleur, ls=ls, lw=lw, zorder=1)
    ax.text(x + 0.15, 0.02 if bas else y, figtools.fig_text(_l(cle)),
            transform=ax.get_xaxis_transform(), rotation=90, va="bottom" if bas else "top",
            ha="left", fontsize=6.5, color=couleur)


# --- 1. Part des recettes fiscales et des dépenses ------------------------------------------

def table_parts() -> pd.DataFrame:
    p = _parts()
    out = pd.DataFrame({
        _l("col_annee"): p.index,
        _l("col_rubrique"): p["rubrique"].round(1).values,
        _l("col_rec"): p["recettes"].round(1).values,
        _l("col_part_rec"): p["part_recettes"].round(2).values,
        _l("col_dep"): p["depenses"].round(1).values,
        _l("col_part_dep"): p["part_depenses"].round(2).values})
    return out


def fig_parts():
    figtools.apply_lang_font()
    p = _parts()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    poignees = []
    for col, cle, couleur, marque in (("part_recettes", "lg_recettes", ROUGE, "o"),
                                      ("part_depenses", "lg_depenses", BLEU, "s")):
        ax.plot(p.index, p[col], "-", color=couleur, lw=1.7, zorder=2)
        for a, v in p[col].items():
            if pd.isna(v):
                continue
            pt, = ax.plot([a], [v], marque, color=couleur, ms=3.6, zorder=3)
            figtools.infobulle(pt, f"{a} · {_l(cle)} : {_nb(v, 2)} %")
        poignees.append(Line2D([], [], color=couleur, marker=marque, lw=1.7, ms=4,
                               label=figtools.fig_text(_l(cle))))
    ax.set_ylim(0, 27)
    _cadre(ax, _l("title_parts"), _l("y_pct"), 1986, 2025)
    # Repères : textes de loi qui changent le tarif. 2016 : trait plein ; nomenclature
    # budgétaire de 2020 : trait mixte, la série du ministère n'est pas coupée.
    for annee, cle in ((1988, "rep_1988"), (1997, "rep_1997")):
        _repere(ax, annee, cle, bas=True)
    _repere(ax, 2018, "rep_2018")
    _repere(ax, 2016, "rep_2016", couleur="#1f2328", ls="-", lw=1.1, y=0.62)
    _repere(ax, ANNEE_NOMENCLATURE, "rep_nomen", couleur=VIOLET, ls=(0, (4, 2)), y=0.62)
    _legende(ax, poignees)
    fig.tight_layout()
    return fig


# --- 2. Part du PIB, par segment de base ----------------------------------------------------

def _segments_pib(p: pd.DataFrame) -> list[tuple[int, int, str]]:
    """[(première année, dernière année, segment)] — un segment par base, jamais chaînés."""
    segs: list[list] = []
    for a, s in p["segment"].items():
        if segs and segs[-1][2] == s:
            segs[-1][1] = a
        else:
            segs.append([a, a, s])
    return [tuple(s) for s in segs]


def _statut_segment(segment: str) -> str:
    if "non rattach" in segment:
        return "non_rattachee"
    if "présumée" in segment:
        return "presumee"
    return "base"


def table_pib() -> pd.DataFrame:
    p = _parts()
    return pd.DataFrame({
        _l("col_annee"): p.index,
        _l("col_rubrique"): p["rubrique"].round(1).values,
        _l("col_pib"): p["pib"].round(1).values,
        _l("col_part_pib"): p["part_pib"].round(3).values,
        _l("col_segment"): p["segment"].values,
        _l("col_retro"): p["retro"].values})


def fig_pib():
    figtools.apply_lang_font()
    p = _parts()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    style = {"base": dict(ls="-", marker="o", mfc=ROUGE, color=ROUGE),
             "presumee": dict(ls=(0, (5, 2)), marker="o", mfc=ROUGE, color=ROUGE),
             "non_rattachee": dict(ls=(0, (1, 2)), marker="o", mfc="white", color=GRIS)}
    segs = _segments_pib(p)
    for i, (a0, a1, segment) in enumerate(segs):
        d = p.loc[a0:a1]
        st = _statut_segment(segment)
        s = style[st]
        ax.plot(d.index, d["part_pib"], ls=s["ls"], lw=1.7, color=s["color"], zorder=2)
        for a, v in d["part_pib"].items():
            pt, = ax.plot([a], [v], s["marker"], ms=4, color=s["color"], mfc=s["mfc"],
                          zorder=3)
            figtools.infobulle(pt, f"{a} · {_nb(v, 2)} % du PIB ({segment})")
        # Base du segment au-dessus du cadre.
        m = re.search(r"\((.*)\)", str(segment))
        base = m.group(1) if m else str(segment)
        if st == "non_rattachee":
            base = _l("nr")
        retro = sorted(d[d["retro"] == "oui"].index)
        if retro:
            base += "\n" + _l("retro", a=retro[0], b=retro[-1])
        ax.annotate(figtools.fig_text(base), xy=((a0 + a1) / 2, 1), xycoords=("data", "axes fraction"),
                    xytext=(0, 5), textcoords="offset points", ha="center", va="bottom",
                    fontsize=6.3, color=GRIS, annotation_clip=False)
    for a in RUPTURES_PIB:
        figtools.marque_rupture(ax, a)
    ax.set_ylim(0, 5.5)
    _cadre(ax, _l("title_pib"), _l("y_pib"), 1986, 2025)
    ax.set_title(figtools.fig_text(_l("title_pib")), fontsize=10.5, pad=34)
    poignees = [
        Line2D([], [], color=ROUGE, ls="-", marker="o", lw=1.5, ms=4,
               label=figtools.fig_text(_l("lg_base"))),
        Line2D([], [], color=ROUGE, ls=(0, (5, 2)), marker="o", lw=1.5, ms=4,
               label=figtools.fig_text(_l("lg_presumee"))),
        Line2D([], [], color=GRIS, ls=(0, (1, 2)), marker="o", mfc="white", lw=1.5, ms=4,
               label=figtools.fig_text(_l("lg_non_rattachee"))),
        Line2D([], [], color="none", label=figtools.fig_text(_l("cadre_pib")))]
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=1,
              fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig


# --- 3. Droits et redevance : prévisions et réalisations ------------------------------------

def _constants(annees, valeurs) -> list[float]:
    ipc = dinars_constants.ipc()
    return [round(v * ipc[BASE] / ipc[a], 1) if (a in ipc and a <= BASE) else float("nan")
            for a, v in zip(annees, valeurs)]


def _series_rendement() -> dict[str, pd.Series]:
    """{('prevision'|'realisation', 'droits'|'redevance'): Série annuelle en MD courants}.

    La redevance est la somme des articles de redevance : 21-02 + 21-03 jusqu'en 2019, 17-02
    ensuite ; pour les réalisations, importation + exportation, que la Cour garde distinctes.
    """
    r = _releve_rendement()
    r = r[r["trace"] == "oui"]
    out = {}
    for nature, cle in (("prévision", "prev"), ("réalisation", "real")):
        d = r[r["nature"] == nature]
        droits = d[d["ligne"] == "droits_importation"].set_index("annee")["valeur_md"]
        redev = (d[d["ligne"].str.startswith("redevance")].groupby("annee")["valeur_md"].sum())
        out[(cle, "droits")] = droits.sort_index()
        out[(cle, "redevance")] = redev.sort_index()
    return out


def table_rendement() -> pd.DataFrame:
    df = _releve_rendement()
    cst = _constants(df["annee"], df["valeur_md"])
    out = df.copy()
    out["cst"] = cst
    out["ligne"] = [_LIGNES[x].get(figtools.lang(), _LIGNES[x]["fr"]) for x in df["ligne"]]
    out = out[["annee", "nature", "ligne", "nomenclature", "code_article", "libelle_source",
               "valeur_md", "cst", "trace", "source", "localisateur", "remarque"]]
    out.columns = [_l(k) for k in ("col_annee", "col_nature", "col_ligne", "col_nomen",
                                   "col_code", "col_lib", "col_md", "col_cst", "col_trace",
                                   "col_src", "col_page", "col_rem")]
    return out


def _trace_rendement(constants: bool, fin: int):
    figtools.apply_lang_font()
    s = _series_rendement()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    for ligne, cle, couleur in (("droits", "lg_droits", ROUGE), ("redevance", "lg_redevance", VIOLET)):
        prev = s[("prev", ligne)]
        prev = prev[prev.index <= fin]
        reel = s[("real", ligne)]
        reel = reel[reel.index <= fin]
        pv = _constants(prev.index, prev.values) if constants else list(prev.values)
        rv = _constants(reel.index, reel.values) if constants else list(reel.values)
        ax.plot(list(prev.index), pv, "-", color=couleur, lw=1.8, zorder=2)
        for a, v in zip(prev.index, pv):
            pt, = ax.plot([a], [v], "o", color=couleur, ms=3, zorder=3)
            figtools.infobulle(pt, f"{a} · {_l(cle)}, {_l('prev')} : {_nb(v)} MD")
        for a, v in zip(reel.index, rv):
            pt, = ax.scatter([a], [v], s=48, facecolors="white", edgecolors=couleur,
                             linewidths=1.6, zorder=4),
            figtools.infobulle(pt, f"{a} · {_l(cle)}, {_l('real')} : {_nb(v)} MD")
    figtools.marque_rupture(ax, ANNEE_NOMENCLATURE, figtools.fig_text(_l("rupture_nomen")))
    _cadre(ax, "", _l("y_cst") if constants else _l("y_cour"), 2001, fin)
    ax.set_title("")
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    poignees = [Line2D([], [], color=ROUGE, lw=1.8, marker="o", ms=3,
                       label=figtools.fig_text(_l("lg_droits"))),
                Line2D([], [], color=VIOLET, lw=1.8, marker="o", ms=3,
                       label=figtools.fig_text(_l("lg_redevance"))),
                Line2D([], [], color=GRIS, lw=1.8, marker="o", ms=3,
                       label=figtools.fig_text(_l("prev"))),
                Line2D([], [], color=GRIS, ls="", marker="o", mfc="white", ms=7,
                       label=figtools.fig_text(_l("real")))]
    _legende(ax, poignees, ncol=2)
    fig.tight_layout()
    return fig


def fig_rendement():
    """Deux vues : dinars courants (2001-2026) ; dinars de l'année de base (2001-2025)."""
    return [(_l("vue_cour"), _trace_rendement(False, 2026)),
            (_l("vue_cst"), _trace_rendement(True, BASE))]


# --- 4. Taux de perception implicite et moyennes simples ------------------------------------

def _importations() -> pd.DataFrame:
    """Importations CAF par année : Banque centrale 1988-1997 (relevé), INS 1998-2023 (série)."""
    r = _releve_perception()
    bct = r[(r["grandeur"] == "importations")].set_index("annee")["valeur"].astype(float)
    i = figtools.series(SERIE_INS)
    i = i[i["flux"] == "importations"].set_index("annee").sort_index()
    out = pd.DataFrame(index=sorted(set(bct.index) | set(i.index)))
    out["importations"] = pd.concat([bct, i["ensemble_md"]])
    out["general"] = i["regime_general_md"]
    out["source"] = ["Banque centrale" if a in bct.index else "INS" for a in out.index]
    return out


def _perception() -> pd.DataFrame:
    imp = _importations()
    num = _composition()["douanes_MDT"]
    out = imp.copy()
    out["rubrique"] = num.reindex(out.index)
    out["taux"] = out["rubrique"] / out["importations"] * 100
    out["taux_general"] = out["rubrique"] / out["general"] * 100
    return out


def _moyennes() -> pd.DataFrame:
    r = _releve_perception()
    return r[r["grandeur"] == "moyenne_simple"].copy()


def table_perception() -> pd.DataFrame:
    p = _perception()
    m = _moyennes()
    annees = sorted(set(p.index) | set(m["annee"]))
    rows = []
    for a in annees:
        ligne = {_l("col_annee"): a}
        if a in p.index:
            ligne.update({
                _l("col_rubrique"): round(p.loc[a, "rubrique"], 1),
                _l("col_imp"): round(p.loc[a, "importations"], 1),
                _l("col_imp_src"): p.loc[a, "source"],
                _l("col_imp_gen"): None if pd.isna(p.loc[a, "general"]) else round(p.loc[a, "general"], 1),
                _l("col_taux"): round(p.loc[a, "taux"], 2),
                _l("col_taux_gen"): None if pd.isna(p.loc[a, "taux_general"]) else round(p.loc[a, "taux_general"], 2)})
        for _, x in m[m["annee"] == a].iterrows():
            rows.append({**ligne, _l("col_moy"): float(x["valeur"]),
                         _l("col_moy_src"): x["source"], _l("col_moy_trace"): x["trace"]})
        if not len(m[m["annee"] == a]):
            rows.append(ligne)
    cols = [_l(k) for k in ("col_annee", "col_rubrique", "col_imp", "col_imp_src",
                            "col_imp_gen", "col_taux", "col_taux_gen", "col_moy",
                            "col_moy_src", "col_moy_trace")]
    return pd.DataFrame(rows).reindex(columns=cols)


def _courbe_coupee(ax, d: pd.Series, couleur: str, marque: str, libelle: str, creux=()):
    """Trace une série annuelle en deux segments, coupée entre 2003 et 2004."""
    d = d.dropna()
    for seg in (d[d.index < ANNEE_RUPTURE_INS], d[d.index >= ANNEE_RUPTURE_INS]):
        if len(seg):
            ax.plot(seg.index, seg.values, "-", color=couleur, lw=1.7, zorder=2)
    for a, v in d.items():
        pt, = ax.plot([a], [v], marque, color=couleur, ms=4, zorder=3,
                      mfc="white" if a in creux else couleur)
        figtools.infobulle(pt, f"{a} · {libelle} : {_nb(v, 2)} %")


def fig_perception():
    figtools.apply_lang_font()
    p = _perception()
    fig, ax = plt.subplots(figsize=(9.5, 6.4))
    creux = [a for a in p.index if p.loc[a, "source"] == "Banque centrale"]
    _courbe_coupee(ax, p["taux"], ROUGE, "o", _l("lg_taux_total"), creux)
    _courbe_coupee(ax, p["taux_general"], ORANGE, "s", _l("lg_taux_general"))
    m = _moyennes()
    m = m[m["trace"] == "oui"]
    for _, x in m.iterrows():
        pt, = ax.plot([x["annee"]], [x["valeur"]], "D", color=VIOLET, ms=5.5, zorder=4)
        figtools.infobulle(pt, f"{x['annee']} · {x['source']}, {x['localisateur']} : "
                               f"{_nb(float(x['valeur']))} %")
    figtools.marque_rupture(ax, ANNEE_RUPTURE_INS, figtools.fig_text(_l("rupture_ins")))
    ax.set_ylim(0, 48)
    _cadre(ax, _l("title_perc"), _l("y_perc"), 1987, 2025)
    budg = [
        Line2D([], [], color=ROUGE, marker="o", lw=1.7, ms=4,
               label=figtools.fig_text(_l("lg_taux_total"))),
        Line2D([], [], color=ORANGE, marker="s", lw=1.7, ms=4,
               label=figtools.fig_text(_l("lg_taux_general"))),
        Line2D([], [], color=ROUGE, marker="o", mfc="white", ls="", ms=5,
               label=figtools.fig_text(_l("lg_bct")))]
    ext = [Line2D([], [], color=VIOLET, marker="D", ls="", ms=5.5,
                  label=figtools.fig_text(_l("lg_ext")))]
    # Deux légendes : le calcul du précis (budgétaire), puis les rapports extérieurs.
    leg1 = ax.legend(handles=budg, title=figtools.fig_text(_l("ttl_budg")), loc="upper center",
                     bbox_to_anchor=(0.5, -0.13), fontsize=7.5, title_fontsize=7.5,
                     frameon=False)
    ax.add_artist(leg1)
    ax.legend(handles=ext, title=figtools.fig_text(_l("ttl_ext")), loc="upper center",
              bbox_to_anchor=(0.5, -0.38), fontsize=7.5, title_fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig

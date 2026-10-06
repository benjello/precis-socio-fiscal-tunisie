"""Figures du livre *La compensation*.

    from figures import compensation as cm
    cm.figure("longue_periode", caption=…, note_lecture=…)        # dépense globale, 1984-2026
    cm.figure("par_poste", caption=…, note_lecture=…)             # trois postes, 2003-2026
    cm.figure("prevu_realise", caption=…, note_lecture=…)         # prévu contre réalisé
    cm.figure("recettes_caisse", caption=…, note_lecture=…)       # recettes de la Caisse
    cm.figure("sources_exterieures", caption=…, note_lecture=…)   # FMI, Banque mondiale
    cm.tableau_recettes_affectees(caption=…)                      # tableau 2009-2011

D'OÙ VIENNENT LES DONNÉES. Trois séries de `tunisia-data`, lues par `figtools.series()`
(l'entrepôt s'il est installé, sinon le cache `precis/_seriescache/`) :

  - `compensation-parts` : une ligne par (année, famille, poste) retenue — valeur en millions
    de dinars, part des dépenses de l'État hors service de la dette, part du PIB — avec la
    famille, la nature (budgétaire ou extérieure), l'état de la valeur, le segment de PIB et
    la rupture à marquer ;
  - `compensation-prevu-realise` : chaque prévision (plan, loi de finances, loi de finances
    complémentaire, prévision) en regard de la valeur retenue de la même famille ;
  - `compensation-recettes-caisse` : recettes de la Caisse et dépense en regard.

Les parts sont CELLES DE L'ENTREPÔT : aucune n'est calculée ici, et les parts imprimées par
les sources (série de contrôle `compensation-ratios-publies`) ne sont pas tracées.

RÈGLES COMMUNES À TOUTES LES FIGURES.

  - **Les familles ne se raccordent pas.** Chaque famille a sa couleur, son trait et sa
    marque ; aucun trait ne va d'une famille à l'autre.
  - **Une année manquante interrompt le trait.** Seules des années consécutives sont reliées.
  - **La part du PIB se trace par segments** (`segment_pib`) : le trait s'interrompt à chaque
    changement de source ou de base du PIB, un trait vertical le marque, et la base de chaque
    segment est écrite au-dessus du cadre. Rien n'est chaîné.
  - **Les ruptures viennent des données** (colonne `rupture`) : changement de grandeur en
    2003, première ligne de carburants en 2004, séparation de la commercialisation des
    hydrocarbures en 2015. Leur texte complet est dans l'infobulle du repère triangulaire,
    en haut du trait ; les changements de champ des produits de base sont dans l'infobulle
    des points.
  - **Les lois de finances et les prévisions sont des points creux**, reliés en pointillé.
  - **Budgétaire et extérieur ne sont pas au même rang** : les séries budgétaires sont en
    traits, les rapports du FMI et de la Banque mondiale en marques rouges sans trait.
  - **Une couleur par poste** d'une figure à l'autre : produits de base en bleu, carburants en
    orange, transport en vert ; les hachures les distinguent en noir et blanc.

LA LIGNE « SOURCE ». Les séries citent une cinquantaine de documents. Chaque figure ne cite
que ceux des lignes qu'elle trace (colonne `source` des données) et ses dénominateurs ; une
clé encore absente de la bibliographie du livre est omise de la citation — elle reste dans la
colonne « Source » des données — et réapparaît d'elle-même dès qu'elle y est versée.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter, MaxNLocator

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_PARTS = "compensation-parts"
SERIE_PREVU = "compensation-prevu-realise"
SERIE_RECETTES = "compensation-recettes-caisse"

# Clés de citation des dénominateurs, d'après le catalogue de l'entrepôt.
CLE_DEPENSES = "minfin-remunerations"      # classeur « répartition économique des dépenses »
CLE_PIB = {"pib-minfin": "minfin-indicateurs-fp", "wdi-tunisie": "wb-wdi"}

BLEU, ORANGE, VERT, VIOLET, ROUGE, GRIS, BRUN, NOIR = (
    "#0969da", "#d1600f", "#1a7f37", "#8250df", "#cf222e", "#57606a", "#9a6700", "#24292f")

# Une famille = une couleur, un trait, une marque. Les rapports extérieurs n'ont pas de trait.
STYLE_FAMILLE = {
    "budget": dict(color=NOIR, ls="-", marker="o", lw=2.0, ms=4.5),
    "budget_dotation_cgc_bct": dict(color=BLEU, ls="--", marker="s", lw=1.4, ms=4.5),
    "budget_compensation_bct": dict(color=VIOLET, ls=":", marker="D", lw=1.6, ms=4.5),
    "cgc_charges_bct": dict(color=BRUN, ls="-.", marker="^", lw=1.4, ms=5),
    "cgc_depenses_bct": dict(color=GRIS, ls="-", marker="v", lw=1.2, ms=5),
    "cgc_bm_1985": dict(color=ROUGE, ls="", marker="P", lw=0, ms=7),
    "fmi_1996": dict(color=ROUGE, ls="", marker="X", lw=0, ms=7),
    "fmi_2000": dict(color=ROUGE, ls="", marker="*", lw=0, ms=9),
}
POSTES = (("produits_de_base", BLEU, ""), ("carburants", ORANGE, "////"),
          ("transport", VERT, "...."))
STYLE_HORIZON = {
    "plan": dict(marker="D", color=VIOLET, creux=False),
    "loi de finances": dict(marker="^", color=ROUGE, creux=False),
    "loi de finances complémentaire": dict(marker="s", color=NOIR, creux=False),
    "prévision": dict(marker="o", color=BRUN, creux=True),
}
# États qui ne sont pas des dépenses constatées : points creux.
ETATS_PREVUS = ("loi de finances", "prévision")

_L = {
    "x": {"fr": "Année", "ar": "السنة"},
    "md": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "md_log": {"fr": "Millions de dinars courants\n(échelle logarithmique)",
               "ar": "ملايين الدنانير الجارية\n(سلّم لوغاريتمي)"},
    "pct_dep": {"fr": "En % des dépenses de l'État hors service de la dette",
                "ar": "% من نفقات الدولة دون خدمة الدين"},
    "pct_pib": {"fr": "En % du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "pct_pib_log": {"fr": "En % du PIB\n(échelle logarithmique)",
                    "ar": "% من الناتج المحلي الإجمالي\n(سلّم لوغاريتمي)"},
    "pct_ecart": {"fr": "Écart au prévu (%)", "ar": "الفارق عن المتوقَّع (%)"},
    "pct_couv": {"fr": "Recettes / dépense (%)", "ar": "الموارد / النفقات (%)"},
    "vue_dep": {"fr": "En part des dépenses de l'État", "ar": "كنسبة من نفقات الدولة"},
    "vue_pib": {"fr": "En % du PIB", "ar": "% من الناتج"},
    "vue_md": {"fr": "En millions de dinars", "ar": "بملايين الدنانير"},
    "vue_lf": {"fr": "Lois de finances, 2012-2026", "ar": "قوانين المالية، 2012-2026"},
    "vue_plan": {"fr": "XIe Plan, 2007-2011", "ar": "المخطّط الحادي عشر، 2007-2011"},
    "vue_caisse": {"fr": "Charges de la Caisse, 1986-2011",
                   "ar": "أعباء الصندوق، 1986-2011"},
    # familles
    "f_budget": {"fr": "Dépense budgétaire de compensation, trois postes (ministère des Finances)",
                 "ar": "نفقات الدعم بالميزانية، ثلاثة أبواب (وزارة المالية)"},
    "f_budget_dotation_cgc_bct": {
        "fr": "Dotation du budget à la Caisse, produits de base (rapports de la BCT)",
        "ar": "اعتماد الميزانية لفائدة الصندوق، المواد الأساسية (تقارير البنك المركزي)"},
    "f_budget_compensation_bct": {
        "fr": "« Dépenses de compensation » du budget, produits de base (rapports de la BCT)",
        "ar": "«نفقات الدعم» بالميزانية، المواد الأساسية (تقارير البنك المركزي)"},
    "f_cgc_charges_bct": {
        "fr": "Charges de la Caisse, produits de base (rapports de la BCT)",
        "ar": "أعباء الصندوق، المواد الأساسية (تقارير البنك المركزي)"},
    "f_cgc_depenses_bct": {
        "fr": "Dépenses du fonds spécial de la Caisse (rapport de la BCT)",
        "ar": "نفقات الصندوق الخاص (تقرير البنك المركزي)"},
    "f_fonds_special_lf": {"fr": "Prévision du fonds spécial (loi de finances)",
                           "ar": "تقديرات الصندوق الخاص (قانون المالية)"},
    "f_cgc_bm_1985": {"fr": "Dépenses de la Caisse selon la Banque mondiale (rapport de 1985)",
                      "ar": "نفقات الصندوق حسب البنك الدولي (تقرير 1985)"},
    "f_fmi_1996": {"fr": "Subventions alimentaires selon le FMI (rapport de 1996)",
                   "ar": "الدعم الغذائي حسب صندوق النقد الدولي (تقرير 1996)"},
    "f_fmi_2000": {
        "fr": "Subventions aux consommateurs par la Caisse selon le FMI (rapport de 2000)",
        "ar": "دعم المستهلكين عبر الصندوق حسب صندوق النقد الدولي (تقرير 2000)"},
    "f_recettes_propres_cgc_bct": {
        "fr": "Recettes propres de la Caisse (rapports de la BCT)",
        "ar": "الموارد الذاتية للصندوق (تقارير البنك المركزي)"},
    "f_recettes_affectees_cgc_minfin": {
        "fr": "Recettes affectées du compte de la Caisse (ministère des Finances)",
        "ar": "الموارد المخصَّصة لحساب الصندوق (وزارة المالية)"},
    "d_cgc_charges_bct": {"fr": "Dépense en regard : charges de la Caisse",
                          "ar": "النفقات المقابلة: أعباء الصندوق"},
    "d_budget": {"fr": "Dépense en regard : dépense budgétaire, trois postes",
                 "ar": "النفقات المقابلة: نفقات الدعم بالميزانية، ثلاثة أبواب"},
    # postes
    "p_total": {"fr": "Total", "ar": "المجموع"},
    "p_produits_de_base": {"fr": "Produits de base", "ar": "المواد الأساسية"},
    "p_carburants": {"fr": "Carburants, électricité et gaz", "ar": "المحروقات والكهرباء والغاز"},
    "p_transport": {"fr": "Transport", "ar": "النقل"},
    # horizons
    "h_plan": {"fr": "Prévu au XIe Plan", "ar": "المتوقَّع في المخطّط الحادي عشر"},
    "h_loi de finances": {"fr": "Prévu en loi de finances", "ar": "المتوقَّع في قانون المالية"},
    "h_loi de finances complémentaire": {
        "fr": "Prévu en loi de finances complémentaire",
        "ar": "المتوقَّع في قانون المالية التكميلي"},
    "h_prévision": {"fr": "Prévision publiée avant l'exercice",
                    "ar": "تقدير منشور قبل السنة المالية"},
    "realise": {"fr": "Réalisé (résultat ou estimation selon la source)",
                "ar": "المنجَز (نتيجة أو تقدير حسب المصدر)"},
    "realise_nq": {"fr": "Réalisé, colonne que la source ne qualifie pas",
                   "ar": "المنجَز، عمود لا يصفه المصدر"},
    # légendes
    "lg_prevu": {"fr": "point creux, pointillé : loi de finances ou prévision",
                 "ar": "نقطة فارغة وخطّ منقّط: قانون مالية أو تقدير"},
    "lg_lf_barre": {"fr": "barre claire à bord pointillé : loi de finances",
                    "ar": "عمود فاتح بحافّة منقّطة: قانون المالية"},
    "lg_rupture": {"fr": "trait vertical : rupture de série (infobulle sur le triangle)",
                   "ar": "خطّ عمودي: انقطاع في السلسلة (التفاصيل عند المثلّث)"},
    "lg_pib": {"fr": "au-dessus du cadre : base du PIB de chaque segment",
               "ar": "فوق الإطار: سنة أساس الناتج لكلّ مقطع"},
    "lg_pib_nr": {"fr": " ; « n. r. » : base non précisée par la source",
                  "ar": "؛ «غ. م.»: سنة الأساس غير محدَّدة في المصدر"},
    "lg_pib_bm": {"fr": " ; « BM » : PIB de la Banque mondiale",
                  "ar": "؛ «ب. د.»: ناتج البنك الدولي"},
    "lg_exterieur": {"fr": "en rouge, sans trait : rapports extérieurs",
                     "ar": "بالأحمر ودون خطّ: التقارير الخارجية"},
    # ruptures (repères courts ; le texte complet est dans les données)
    "rup_2003": {"fr": "2003 : dépense\nen trois postes", "ar": "2003: نفقات\nبثلاثة أبواب"},
    "rup_2004": {"fr": "2004 : première ligne\nde carburants",
                 "ar": "2004: أوّل سطر\nللمحروقات"},
    "rup_2015": {"fr": "2015 : commercialisation\ndes hydrocarbures séparée",
                 "ar": "2015: فصل عمليات\nتسويق المحروقات"},
    # bases du PIB (au-dessus du cadre)
    "b_base 1983 présumée": {"fr": "base 1983\n(présumée)", "ar": "أساس 1983\n(مفترض)"},
    "b_base 1983": {"fr": "base 1983", "ar": "أساس 1983"},
    "b_base 1997": {"fr": "base 1997", "ar": "أساس 1997"},
    "b_base 2015": {"fr": "base 2015", "ar": "أساس 2015"},
    "b_non rattachée": {"fr": "n. r.", "ar": "غ. م."},
    "b_bm": {"fr": "BM", "ar": "ب. د."},
    "b_pib": {"fr": "PIB :", "ar": "الناتج:"},
    # recettes
    "recettes": {"fr": "Recettes", "ar": "الموارد"},
    "couverture": {"fr": "Recettes rapportées à la dépense en regard",
                   "ar": "الموارد منسوبة إلى النفقات المقابلة"},
    "t_rec_md": {"fr": "Recettes affectées du compte de la CGC (MD)",
                 "ar": "الموارد المخصَّصة لحساب الصندوق (م.د)"},
    "t_dep_md": {"fr": "Dépense de compensation, trois postes (MD)",
                 "ar": "نفقات الدعم، ثلاثة أبواب (م.د)"},
    "t_pct_dep": {"fr": "— en % des dépenses de l'État hors service de la dette",
                  "ar": "— % من نفقات الدولة دون خدمة الدين"},
    "t_pct_pib": {"fr": "— en % du PIB", "ar": "— % من الناتج المحلي الإجمالي"},
    "t_couv": {"fr": "Recettes rapportées à la dépense (%)",
               "ar": "الموارد منسوبة إلى النفقات (%)"},
    # colonnes des tables
    "c_annee": {"fr": "Année", "ar": "السنة"},
    "c_famille": {"fr": "Série", "ar": "السلسلة"},
    "c_code_famille": {"fr": "Code de la série", "ar": "رمز السلسلة"},
    "c_nature": {"fr": "Nature", "ar": "الطبيعة"},
    "c_poste": {"fr": "Poste", "ar": "الباب"},
    "c_valeur_MDT": {"fr": "Montant (MD)", "ar": "المبلغ (م.د)"},
    "c_etat": {"fr": "État selon la source", "ar": "الحالة حسب المصدر"},
    "c_etat_norme": {"fr": "État", "ar": "الحالة"},
    "c_source": {"fr": "Source", "ar": "المصدر"},
    "c_document": {"fr": "Document", "ar": "الوثيقة"},
    "c_page_imprimee": {"fr": "Page imprimée", "ar": "الصفحة المطبوعة"},
    "c_page_pdf": {"fr": "Page du PDF", "ar": "صفحة الملف"},
    "c_note": {"fr": "Note", "ar": "ملاحظة"},
    "c_depenses_etat_hors_dette_MDT": {"fr": "Dépenses de l'État hors service de la dette (MD)",
                                       "ar": "نفقات الدولة دون خدمة الدين (م.د)"},
    "c_part_depenses_etat_pct": {"fr": "% des dépenses de l'État", "ar": "% من نفقات الدولة"},
    "c_depenses_fonctionnement_MDT": {"fr": "Dépenses de fonctionnement (MD)",
                                      "ar": "نفقات التصرّف (م.د)"},
    "c_part_depenses_fonctionnement_pct": {"fr": "% des dépenses de fonctionnement",
                                           "ar": "% من نفقات التصرّف"},
    "c_pib_MDT": {"fr": "PIB (MD)", "ar": "الناتج المحلي الإجمالي (م.د)"},
    "c_source_pib": {"fr": "Source du PIB", "ar": "مصدر الناتج"},
    "c_base_pib": {"fr": "Base du PIB", "ar": "سنة أساس الناتج"},
    "c_segment_pib": {"fr": "Segment de PIB", "ar": "مقطع الناتج"},
    "c_part_pib_pct": {"fr": "% du PIB", "ar": "% من الناتج"},
    "c_rupture": {"fr": "Rupture", "ar": "الانقطاع"},
    "c_nature_pib": {"fr": "PIB employé : base et rétropolation",
                     "ar": "الناتج المعتمد: سنة الأساس وإعادة الاحتساب"},
    # nature du PIB de chaque segment (colonne des données)
    "n_bm": {"fr": "PIB de la Banque mondiale, qui accole les bases sans les raccorder : base "
                   "non précisée par la source",
             "ar": "ناتج البنك الدولي، بسنوات أساس متتابعة غير مربوطة: سنة الأساس غير محدَّدة "
                   "في المصدر"},
    "n_presumee": {"fr": "PIB du ministère des Finances, base 1983 présumée ; la série ne dit "
                         "pas si la valeur est rétropolée",
                   "ar": "ناتج وزارة المالية، أساس 1983 مفترض؛ لا تبيّن السلسلة إن كانت القيمة "
                         "معاد احتسابها"},
    "n_base": {"fr": "PIB du ministère des Finances, {b} ; la série ne dit pas si la valeur est "
                     "rétropolée",
               "ar": "ناتج وزارة المالية، {b}؛ لا تبيّن السلسلة إن كانت القيمة معاد احتسابها"},
    "n_propre": {"fr": "PIB propre au ministère des Finances : base non précisée par la source",
                 "ar": "ناتج خاصّ بوزارة المالية: سنة الأساس غير محدَّدة في المصدر"},
    "n_retropole": {"fr": "PIB propre au ministère des Finances, rétropolé (environ + 5 % sur "
                          "la base 1997) : base non précisée par la source",
                    "ar": "ناتج خاصّ بوزارة المالية، معاد احتسابه (نحو + 5 % على أساس 1997): "
                          "سنة الأساس غير محدَّدة في المصدر"},
    "n_estimation": {"fr": "PIB estimé par le ministère des Finances : base non précisée par "
                           "la source",
                     "ar": "ناتج مقدَّر من وزارة المالية: سنة الأساس غير محدَّدة في المصدر"},
    "c_horizon": {"fr": "Horizon de la prévision", "ar": "أفق التقدير"},
    "c_prevu_MDT": {"fr": "Prévu (MD)", "ar": "المتوقَّع (م.د)"},
    "c_etat_prevu": {"fr": "Libellé du prévu", "ar": "تسمية المتوقَّع"},
    "c_source_prevu": {"fr": "Source du prévu", "ar": "مصدر المتوقَّع"},
    "c_page_imprimee_prevu": {"fr": "Page imprimée (prévu)", "ar": "الصفحة المطبوعة (المتوقَّع)"},
    "c_page_pdf_prevu": {"fr": "Page du PDF (prévu)", "ar": "صفحة الملف (المتوقَّع)"},
    "c_realise_MDT": {"fr": "Réalisé (MD)", "ar": "المنجَز (م.د)"},
    "c_etat_realise": {"fr": "État du réalisé", "ar": "حالة المنجَز"},
    "c_source_realise": {"fr": "Source du réalisé", "ar": "مصدر المنجَز"},
    "c_page_pdf_realise": {"fr": "Page du PDF (réalisé)", "ar": "صفحة الملف (المنجَز)"},
    "c_ecart_MDT": {"fr": "Écart (MD)", "ar": "الفارق (م.د)"},
    "c_ecart_pct": {"fr": "Écart (% du prévu)", "ar": "الفارق (% من المتوقَّع)"},
    "c_recettes_MDT": {"fr": "Recettes (MD)", "ar": "الموارد (م.د)"},
    "c_famille_depense": {"fr": "Dépense en regard", "ar": "النفقات المقابلة"},
    "c_poste_depense": {"fr": "Poste de la dépense en regard", "ar": "باب النفقات المقابلة"},
    "c_depense_en_regard_MDT": {"fr": "Dépense en regard (MD)", "ar": "النفقات المقابلة (م.د)"},
    "c_couverture_pct": {"fr": "Recettes / dépense (%)", "ar": "الموارد / النفقات (%)"},
    "c_produits_de_base_MDT": {"fr": "Produits de base (MD)", "ar": "المواد الأساسية (م.د)"},
    "c_couverture_produits_de_base_pct": {"fr": "Recettes / produits de base (%)",
                                          "ar": "الموارد / المواد الأساسية (%)"},
    "c_part_pib_depense_pct": {"fr": "Dépense en regard, % du PIB",
                               "ar": "النفقات المقابلة، % من الناتج"},
    "c_part_depenses_etat_depense_pct": {"fr": "Dépense en regard, % des dépenses de l'État",
                                         "ar": "النفقات المقابلة، % من نفقات الدولة"},
}


def _lab(key: str, **valeurs) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"]).format(**valeurs)


def _ft(key: str, **valeurs) -> str:
    return "\n".join(figtools.fig_text(l) for l in _lab(key, **valeurs).split("\n"))


def _nombre(v: float, dec: int = 1) -> str:
    if round(v, dec) == 0:
        v = 0.0
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _unite(mesure: str) -> str:
    if mesure == "md":
        return " MD" if figtools.lang() == "fr" else " م.د"
    return " %"


COLONNE = {"md": "valeur_MDT", "dep": "part_depenses_etat_pct", "pib": "part_pib_pct"}
YLABEL = {"md": "md", "dep": "pct_dep", "pib": "pct_pib"}
DECIMALES = {"md": 1, "dep": 2, "pib": 2}


# --- lecture des séries ------------------------------------------------------------------

def _parts():
    return figtools.series(SERIE_PARTS)


def _prevu():
    return figtools.series(SERIE_PREVU)


def _recettes():
    return figtools.series(SERIE_RECETTES)


def _vide(v) -> bool:
    return v is None or v != v


def _suites(annees) -> list[list[int]]:
    """Suites d'années consécutives : un trait ne franchit jamais une année manquante."""
    suites: list[list[int]] = []
    for a in sorted(int(x) for x in annees):
        if suites and a == suites[-1][-1] + 1:
            suites[-1].append(a)
        else:
            suites.append([a])
    return suites


# --- provenance : la ligne « Source » ne cite que ce que la figure trace ------------------

_META_ORIGINE: dict[str, dict] = {}


# Tournures de relevé, bannies du texte rendu : ce qui en porte une est omis de la page (notes
# des tables, réserves du catalogue) et reste dans la série.
_RE_RELEVE = re.compile(r"relu|couche texte|à l'image", re.IGNORECASE)


def _sans_releve(texte: str) -> str:
    """Le texte sans ses phrases de relevé (découpe sur « . » suivi d'une majuscule)."""
    phrases = re.split(r"(?<=\.) (?=[A-ZÀ-Ý])", texte)
    return " ".join(p for p in phrases if not _RE_RELEVE.search(p))


def _cles_pib(d) -> list[str]:
    cles = []
    for s in d["source_pib"].dropna().unique():
        for prefixe, cle in CLE_PIB.items():
            if str(s).startswith(prefixe) and cle not in cles:
                cles.append(cle)
    return cles


def _declarer(series_id: str, cles) -> list[str]:
    """Restreint la provenance d'une série aux clés que la figure emploie ; rend les clés
    omises parce qu'absentes de la bibliographie du livre."""
    if series_id not in _META_ORIGINE:
        _META_ORIGINE[series_id] = dict(figtools.meta(series_id))
    origine = _META_ORIGINE[series_id]
    connues = figtools._ref_index()
    cles = list(dict.fromkeys(str(k) for k in cles if not _vide(k)))
    champs = {k: v for k, v in origine.items() if k != "id"}
    champs["sources"] = [k for k in cles if k in connues]
    # Réserves du catalogue : la phrase qui décrit le relevé (et non la donnée) n'est pas
    # reprise dans la page ni dans l'en-tête du fichier téléchargé.
    for champ in ("caveats", "caveats_ar"):
        if isinstance(origine.get(champ), str):
            champs[champ] = _sans_releve(origine[champ])
    # « (fichier à tracer) » est une consigne d'atelier, pas un titre.
    champs["titre"] = str(origine.get("titre", series_id)).replace(" (fichier à tracer)", "")
    figtools.register_provenance(series_id, **champs)
    return [k for k in cles if k not in connues]


# --- tables de données -------------------------------------------------------------------

def _nature_pib(segment):
    """Ce que la série dit du PIB d'un segment : sa base, et s'il est rétropolé.

    D'après `segment_pib` et la fiche `docs/compensation-ratios.md` de l'entrepôt : les
    valeurs de 2010-2014 y sont données pour rétropolées, celle de 2025 pour une estimation ;
    pour les segments rattachés à une base, la série ne dit pas si la valeur est celle de la
    publication d'origine. Un tronçon « non rattaché » n'a pas de base précisée."""
    if _vide(segment):
        return None
    s = str(segment)
    if s.startswith("wdi"):
        return _lab("n_bm")
    if "présumée" in s:
        return _lab("n_presumee")
    if "non rattach" in s:
        if "2010-2014" in s:
            return _lab("n_retropole")
        if "2025-2025" in s:
            return _lab("n_estimation")
        return _lab("n_propre")
    m = re.search(r"\((base \d{4})\)", s)
    return _lab("n_base", b=_lab("b_" + m.group(1))) if m else None


def _note(v):
    if _vide(v):
        return v
    morceaux = [m for m in str(v).split(" ; ") if not _RE_RELEVE.search(m)]
    return " ; ".join(morceaux) if morceaux else None


def _table(d, colonnes):
    """Table affichée et téléchargée : toutes les colonnes de provenance, intitulés traduits.

    Les colonnes `lecture` (journal de relevé de l'entrepôt) ne sont pas reprises."""
    d = d.copy()
    out = {}
    for col in colonnes:
        if col == "famille":
            out[_lab("c_famille")] = d["famille"].map(lambda f: _lab("f_" + f))
            out[_lab("c_code_famille")] = d["famille"]
        elif col in ("poste", "poste_depense"):
            out[_lab("c_" + col)] = d[col].map(lambda p: _lab("p_" + p))
        elif col == "famille_depense":
            out[_lab("c_" + col)] = d[col].map(lambda f: _lab("f_" + f))
        elif col == "note":
            out[_lab("c_note")] = d[col].map(_note)
        elif col == "segment_pib":
            out[_lab("c_segment_pib")] = d[col]
            out[_lab("c_nature_pib")] = d[col].map(_nature_pib)
        elif col.startswith("page_"):  # numéros de page : entiers, vides admis
            out[_lab("c_" + col)] = d[col].astype("Int64")
        else:
            out[_lab("c_" + col)] = d[col]
    import pandas as pd
    return pd.DataFrame(out).reset_index(drop=True)


COLS_PARTS = ["annee", "famille", "nature", "poste", "valeur_MDT", "etat_norme", "etat",
              "part_depenses_etat_pct", "part_pib_pct", "source", "document", "page_imprimee",
              "page_pdf", "note", "depenses_etat_hors_dette_MDT", "depenses_fonctionnement_MDT",
              "part_depenses_fonctionnement_pct", "pib_MDT", "source_pib", "base_pib",
              "segment_pib", "rupture"]
COLS_PREVU = ["annee", "famille", "nature", "poste", "horizon", "prevu_MDT", "realise_MDT",
              "ecart_MDT", "ecart_pct", "etat_prevu", "source_prevu", "page_imprimee_prevu",
              "page_pdf_prevu", "etat_realise", "source_realise", "page_pdf_realise", "note"]
COLS_RECETTES = ["annee", "famille", "nature", "recettes_MDT", "famille_depense",
                 "poste_depense", "depense_en_regard_MDT", "couverture_pct",
                 "part_depenses_etat_pct", "part_pib_pct", "part_depenses_etat_depense_pct",
                 "part_pib_depense_pct", "etat", "source", "document", "page_imprimee",
                 "page_pdf", "note", "depenses_etat_hors_dette_MDT", "pib_MDT", "source_pib",
                 "base_pib", "segment_pib", "produits_de_base_MDT",
                 "couverture_produits_de_base_pct"]


# --- tracé générique ---------------------------------------------------------------------

def _cadre(ax, ylabel, x0, x1, xlabel=True):
    ax.set_ylabel(_ft(ylabel))
    if xlabel:
        ax.set_xlabel(figtools.fig_text(_lab("x")))
    ax.set_xlim(x0 - 0.8, x1 + 0.8)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=14))
    ax.grid(True, alpha=0.3)
    ax.set_axisbelow(True)


def _axe_log(ax):
    ax.set_yscale("log")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0)))


def _bulle(r, libelle, valeur, mesure) -> str:
    texte = f"{int(r.annee)} · {libelle} : {_nombre(valeur, DECIMALES[mesure])}{_unite(mesure)}"
    etat = getattr(r, "etat_norme", None)
    if not _vide(etat):
        texte += f" — {etat}"
    doc = getattr(r, "document", None)
    if not _vide(doc):
        texte += f" — {doc}"
    rup = getattr(r, "rupture", None)
    if not _vide(rup):
        texte += f" — {rup}"
    return texte


def _trace_famille(ax, d, famille, mesure, poste=None):
    """Une famille : traits entre années consécutives (d'un même segment de PIB si la mesure
    est la part du PIB), marques pleines, prévisions en marques creuses et pointillé."""
    st = STYLE_FAMILLE[famille]
    col = COLONNE[mesure]
    d = d[(d["famille"] == famille) & d[col].notna()]
    if poste:
        d = d[d["poste"] == poste]
    d = d.sort_values("annee")
    if d.empty:
        return False
    prevus = d[d["etat_norme"].isin(ETATS_PREVUS)]
    fermes = d[~d["etat_norme"].isin(ETATS_PREVUS)]
    groupes = ([g for _, g in fermes.groupby("segment_pib", sort=False)]
               if mesure == "pib" else [fermes])
    if st["ls"]:
        for g in groupes:
            v = dict(zip(g["annee"].astype(int), g[col]))
            for suite in _suites(v):
                ax.plot(suite, [v[a] for a in suite], ls=st["ls"], lw=st["lw"],
                        color=st["color"], zorder=2)
        # Prévisions : pointillé depuis la dernière valeur constatée, si les années se suivent
        # — et jamais d'un segment de PIB à l'autre.
        if mesure != "pib" and len(prevus) and len(fermes):
            chaine = list(fermes.tail(1)["annee"].astype(int)) + list(prevus["annee"].astype(int))
            if _suites(chaine) == [chaine]:
                v = dict(zip(d["annee"].astype(int), d[col]))
                ax.plot(chaine, [v[a] for a in chaine], ls=(0, (1, 2)), lw=1.2,
                        color=st["color"], zorder=2)
    libelle = _lab("f_" + famille)
    for r in d.itertuples(index=False):
        y = getattr(r, col)
        creux = r.etat_norme in ETATS_PREVUS
        p, = ax.plot([int(r.annee)], [y], st["marker"], ms=st["ms"], color=st["color"],
                     mfc="white" if creux else st["color"], zorder=3)
        figtools.infobulle(p, _bulle(r, libelle, y, mesure))
    return True


def _legende_familles(familles) -> list:
    return [Line2D([], [], color=STYLE_FAMILLE[f]["color"], marker=STYLE_FAMILLE[f]["marker"],
                   ls=STYLE_FAMILLE[f]["ls"] or "none", lw=STYLE_FAMILLE[f]["lw"],
                   ms=STYLE_FAMILLE[f]["ms"], label=figtools.fig_text(_lab("f_" + f)))
            for f in familles]


def _poignee(cle, **style) -> Line2D:
    return Line2D([], [], label=figtools.fig_text(_lab(cle)), **style)


def _poignee_pib(d) -> Line2D:
    """Entrée de légende des bases du PIB : ne décrit que les abréviations employées."""
    segments = [str(x) for x in d["segment_pib"].dropna().unique()]
    texte = _lab("lg_pib")
    if any("non rattach" in x for x in segments):
        texte += _lab("lg_pib_nr")
    if any(x.startswith("wdi") for x in segments):
        texte += _lab("lg_pib_bm")
    return Line2D([], [], color="none", label=figtools.fig_text(texte))


def _ruptures_des_donnees(d) -> dict[int, dict[str, list[str]]]:
    """{année: {"pib": […], "champ": […], "serie": […]}} d'après la colonne `rupture`.

    « PIB … » : changement de source ou de base du dénominateur ; « champ : … » : entrée ou
    sortie d'un produit ; le reste : changement de la série elle-même, à marquer d'un trait."""
    out: dict[int, dict[str, list[str]]] = {}
    for r in d[d["rupture"].notna()].itertuples(index=False):
        # Un texte peut réunir plusieurs ruptures, séparées par « ; » ; un morceau qui n'ouvre
        # pas une rupture (« PIB… », « champ : … », « carburants : … ») continue la précédente.
        ruptures: list[str] = []
        for m in str(r.rupture).split(" ; "):
            if ruptures and not m.startswith(("PIB", "champ", "carburants", "première")):
                ruptures[-1] += " ; " + m
            else:
                ruptures.append(m.strip())
        for m in ruptures:
            genre = "pib" if m.startswith("PIB") else "champ" if m.startswith("champ") else "serie"
            liste = out.setdefault(int(r.annee), {}).setdefault(genre, [])
            if m not in liste:
                liste.append(m)
    return out


def _repere(ax, annee, texte):
    """Petit triangle en haut du trait de rupture, porteur de l'infobulle."""
    p, = ax.plot([annee - 0.5], [1], marker=7, ms=6, color=GRIS, clip_on=False, zorder=4,
                 transform=ax.get_xaxis_transform())
    figtools.infobulle(p, texte)


def _marque_ruptures(ax, d, x0, x1, pib=False, cote=None):
    """Traits verticaux des ruptures de série lues dans les données ; pour la part du PIB,
    un trait à chaque changement de segment et la base de chaque segment au-dessus du cadre."""
    rup = _ruptures_des_donnees(d)
    cote = cote or {}
    traces: set[int] = set()
    niveau = 0
    for a in sorted(rup):
        if "serie" not in rup[a] or not (x0 < a <= x1):
            continue
        figtools.marque_rupture(ax, a)
        traces.add(a)
        cle = f"rup_{a}"
        if cle in _L:
            gauche = cote.get(a) == "gauche"
            ax.annotate(_ft(cle), xy=(a - 0.5, 1), xycoords=("data", "axes fraction"),
                        xytext=(-4 if gauche else 4, -4 - 22 * (niveau % 2 if not gauche else 0)),
                        textcoords="offset points", ha="right" if gauche else "left", va="top",
                        fontsize=7, color=GRIS, zorder=5,
                        bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1))
            if not gauche:
                niveau += 1
        textes = rup[a]["serie"] + (rup[a].get("pib", []) if pib else [])
        _repere(ax, a, f"{a} · " + " ; ".join(textes))
    if not pib:
        return
    # Segments de PIB : bornes lues dans le libellé du segment, base au-dessus du cadre.
    segments = []
    for s in d["segment_pib"].dropna().unique():
        m = re.search(r"(\d{4})-(\d{4}) \((.*)\)", str(s))
        if not m:
            continue
        if str(s).startswith("wdi"):
            segments.append([None, None, "bm"])
        else:
            segments.append([int(m.group(1)), int(m.group(2)), m.group(3)])
    debuts = [s[0] for s in segments if s[0] is not None]
    for s in segments:
        if s[0] is None:  # Banque mondiale : avant le premier PIB du ministère
            s[0], s[1] = x0, (min(debuts) - 1 if debuts else x1)
    segments = sorted(s for s in segments if s[0] <= x1 and s[1] >= x0)
    for i, (a0, a1, base) in enumerate(segments):
        a0c, a1c = max(a0, x0), min(a1, x1)
        contigu = i and segments[i - 1][1] == a0 - 1
        if contigu and a0 not in traces:
            figtools.marque_rupture(ax, a0)
            if a0 in rup and "pib" in rup[a0]:
                _repere(ax, a0, f"{a0} · " + " ; ".join(rup[a0]["pib"]))
        cle = "b_" + (base if "b_" + base in _L else "non rattachée"
                      if base.startswith("non rattach") else base)
        if cle not in _L:
            continue
        ax.annotate(_ft(cle), xy=((a0c + a1c) / 2, 1), xycoords=("data", "axes fraction"),
                    xytext=(0, 5), textcoords="offset points", ha="center", va="bottom",
                    fontsize=6.5, color=GRIS, annotation_clip=False)
    ax.annotate(_ft("b_pib"), xy=(0, 1), xycoords="axes fraction", xytext=(-6, 5),
                textcoords="offset points", ha="right", va="bottom", fontsize=6.5, color=GRIS,
                annotation_clip=False)


def _legende(ax, poignees, ncol=2, y=-0.13, taille=7.5):
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, y), ncol=ncol,
              fontsize=taille, frameon=False)


# --- 1. La dépense globale sur la longue période -----------------------------------------

FAMILLES_LONGUES = ("budget", "budget_dotation_cgc_bct", "budget_compensation_bct",
                    "cgc_charges_bct")


def _longue_periode():
    d = _parts()
    d = d[d["famille"].isin(FAMILLES_LONGUES)]
    return d[(d["famille"] != "budget") | (d["poste"] == "total")]


def fig_longue_periode(mesure: str = "dep"):
    figtools.apply_lang_font()
    d = _longue_periode()
    col = COLONNE[mesure]
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    traces = [f for f in FAMILLES_LONGUES if _trace_famille(ax, d, f, mesure)]
    annees = d[d[col].notna()]["annee"].astype(int)
    x0, x1 = int(annees.min()), int(annees.max())
    _cadre(ax, "md_log" if mesure == "md" else YLABEL[mesure], x0, x1)
    if mesure == "md":
        _axe_log(ax)
    else:
        ax.set_ylim(bottom=0)
        ax.set_ylim(top=ax.get_ylim()[1] * 1.12)
    _marque_ruptures(ax, d[d[col].notna()], x0, x1, pib=(mesure == "pib"),
                     cote={2003: "gauche"})
    poignees = _legende_familles(traces)
    poignees.append(_poignee("lg_prevu", color=GRIS, marker="o", mfc="white", ls=(0, (1, 2)),
                             lw=1.2))
    poignees.append(_poignee("lg_rupture", color=GRIS, ls=(0, (2, 2)), lw=1, marker=7, ms=5))
    if mesure == "pib":
        poignees.append(_poignee_pib(d))
    _legende(ax, poignees, ncol=1, y=-0.12)
    fig.tight_layout()
    return fig


def _figure_longue_periode():
    d = _longue_periode().sort_values(["famille", "annee"])
    vues = [(_lab("vue_dep"), fig_longue_periode("dep")),
            (_lab("vue_pib"), fig_longue_periode("pib")),
            (_lab("vue_md"), fig_longue_periode("md"))]
    cles = list(d["source"]) + [CLE_DEPENSES] + _cles_pib(d)
    return vues, _table(d, COLS_PARTS), {SERIE_PARTS: cles}, "fig_compensation_longue_periode"


# --- 2. La décomposition par poste -------------------------------------------------------

def _par_poste():
    d = _parts()
    return d[d["famille"] == "budget"]


def fig_par_poste(mesure: str = "md"):
    figtools.apply_lang_font()
    d = _par_poste()
    col = COLONNE[mesure]
    d = d[d[col].notna()]
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    annees = sorted(d["annee"].astype(int).unique())
    dec = DECIMALES[mesure] if mesure != "md" else 0
    for a in annees:
        da = d[d["annee"] == a]
        prevu = bool(da["etat_norme"].isin(ETATS_PREVUS).any())
        bas = 0.0
        for poste, couleur, hachure in POSTES:
            r = da[da["poste"] == poste]
            if r.empty:
                continue
            r = next(r.itertuples(index=False))
            v = float(getattr(r, col))
            barre = ax.bar([a], [v], bottom=bas, width=0.78, color=couleur, hatch=hachure,
                           edgecolor=couleur if prevu else "white", linewidth=0.8,
                           alpha=0.4 if prevu else 1.0, ls="--" if prevu else "-", zorder=2)
            figtools.infobulle(barre[0], _bulle(r, _lab("p_" + poste), v, mesure))
            bas += v
        total = da[da["poste"] == "total"]
        haut = bas if total.empty else float(total.iloc[0][col])
        ax.annotate(_nombre(haut, dec), xy=(a, bas), xytext=(0, 2), textcoords="offset points",
                    ha="center", va="bottom", fontsize=5.8, color=NOIR)
    x0, x1 = annees[0], annees[-1]
    _cadre(ax, YLABEL[mesure], x0, x1)
    ax.set_xticks(annees)
    ax.tick_params(axis="x", labelsize=7)
    if mesure == "md":
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0)))
    ax.set_ylim(top=ax.get_ylim()[1] * 1.14)
    _marque_ruptures(ax, d, x0, x1, pib=(mesure == "pib"))
    poignees = [Patch(facecolor=c, hatch=h, edgecolor="white",
                      label=figtools.fig_text(_lab("p_" + p))) for p, c, h in POSTES]
    poignees.append(Patch(facecolor=GRIS, alpha=0.4, edgecolor=GRIS, ls="--",
                          label=figtools.fig_text(_lab("lg_lf_barre"))))
    poignees.append(_poignee("lg_rupture", color=GRIS, ls=(0, (2, 2)), lw=1, marker=7, ms=5))
    if mesure == "pib":
        poignees.append(_poignee_pib(d))
    _legende(ax, poignees, ncol=1 if mesure == "pib" else 2)
    fig.tight_layout()
    return fig


def _figure_par_poste():
    d = _par_poste().sort_values(["annee", "poste"])
    vues = [(_lab("vue_md"), fig_par_poste("md")), (_lab("vue_dep"), fig_par_poste("dep")),
            (_lab("vue_pib"), fig_par_poste("pib"))]
    cles = list(d["source"]) + [CLE_DEPENSES] + _cles_pib(d)
    return vues, _table(d, COLS_PARTS), {SERIE_PARTS: cles}, "fig_compensation_par_poste"


# --- 3. Prévu et réalisé -----------------------------------------------------------------

def fig_prevu_realise(vue: str = "lf"):
    """Haut : le réalisé en barres, chaque prévision en marque. Bas : l'écart du réalisé au
    prévu, en % du prévu — le total seul, les postes restant dans les données."""
    figtools.apply_lang_font()
    d = _prevu()
    if vue == "lf":
        d = d[(d["famille"] == "budget") & (d["poste"] == "total") & (d["horizon"] != "plan")]
    elif vue == "plan":
        d = d[(d["famille"] == "budget") & (d["poste"] == "total") & (d["horizon"] == "plan")]
    else:
        d = d[d["famille"] == "cgc_charges_bct"]
    d = d.sort_values(["annee", "horizon"])
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.5, 6.4), sharex=True,
                                 gridspec_kw=dict(height_ratios=[2, 1.15], hspace=0.08))
    annees = sorted(d["annee"].astype(int).unique())
    # réalisé : une barre par année
    qualifie = False
    non_qualifie = False
    for a in annees:
        r = next(d[d["annee"] == a].itertuples(index=False))
        if _vide(r.realise_MDT):
            continue
        nq = str(r.etat_realise) == "non qualifié"
        qualifie |= not nq
        non_qualifie |= nq
        barre = ax.bar([a], [r.realise_MDT], width=0.7, zorder=2,
                       color="white" if nq else "#afb8c1", hatch="///" if nq else "",
                       edgecolor="#8c959f", linewidth=0.8)
        figtools.infobulle(barre[0], f"{a} · {_lab('realise_nq' if nq else 'realise')} : "
                                      f"{_nombre(r.realise_MDT)}{_unite('md')} — {r.source_realise}")
    # prévu : une marque par horizon, décalée quand deux horizons portent la même année
    horizons = [h for h in STYLE_HORIZON if (d["horizon"] == h).any()]
    for a in annees:
        da = d[d["annee"] == a]
        n = len(da)
        for i, r in enumerate(da.itertuples(index=False)):
            st = STYLE_HORIZON[r.horizon]
            x = a + (i - (n - 1) / 2) * 0.34
            mfc = "white" if st["creux"] else st["color"]
            p, = ax.plot([x], [r.prevu_MDT], st["marker"], ms=6.5, color=st["color"], mfc=mfc,
                         zorder=4)
            bulle = (f"{a} · {_lab('h_' + r.horizon)} : {_nombre(r.prevu_MDT)}{_unite('md')}"
                     f" — {r.etat_prevu} — {r.source_prevu}")
            figtools.infobulle(p, bulle)
            if _vide(r.ecart_pct):
                continue
            e = float(r.ecart_pct)
            bx.plot([x, x], [0, e], color=st["color"], lw=1.3, zorder=2)
            q, = bx.plot([x], [e], st["marker"], ms=6, color=st["color"], mfc=mfc, zorder=3)
            figtools.infobulle(q, bulle + f" — {_lab('c_ecart_pct')} : {_nombre(e)} %")
            bx.annotate(("+" if e > 0 else "") + _nombre(e, 0).replace("-", "−") + " %", xy=(x, e),
                        xytext=(0, 5 if e >= 0 else -5), textcoords="offset points",
                        ha="center", va="bottom" if e >= 0 else "top", fontsize=6.5,
                        color=st["color"])
    x0, x1 = annees[0], annees[-1]
    _cadre(ax, "md", x0, x1, xlabel=False)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0)))
    _cadre(bx, "pct_ecart", x0, x1)
    bx.axhline(0, color=NOIR, lw=0.8, zorder=1)
    bx.margins(y=0.28)
    pas = 1 if len(annees) <= 16 or x1 - x0 <= 16 else 2
    bx.set_xticks(list(range(x0, x1 + 1, pas)))
    bx.tick_params(axis="x", labelsize=7.5)
    poignees = []
    if qualifie:
        poignees.append(Patch(facecolor="#afb8c1", edgecolor="#8c959f",
                              label=figtools.fig_text(_lab("realise"))))
    if non_qualifie:
        poignees.append(Patch(facecolor="white", hatch="///", edgecolor="#8c959f",
                              label=figtools.fig_text(_lab("realise_nq"))))
    for h in horizons:
        st = STYLE_HORIZON[h]
        poignees.append(_poignee("h_" + h, color=st["color"], marker=st["marker"], ls="none",
                                 ms=6.5, mfc="white" if st["creux"] else st["color"]))
    bx.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.3), ncol=2,
              fontsize=7.5, frameon=False)
    fig.subplots_adjust(left=0.09, right=0.98, top=0.97, bottom=0.2)
    return fig


def _figure_prevu_realise():
    d = _prevu().sort_values(["famille", "annee", "poste", "horizon"])
    vues = [(_lab("vue_lf"), fig_prevu_realise("lf")),
            (_lab("vue_plan"), fig_prevu_realise("plan")),
            (_lab("vue_caisse"), fig_prevu_realise("caisse"))]
    cles = list(d["source_prevu"]) + list(d["source_realise"])
    return vues, _table(d, COLS_PREVU), {SERIE_PREVU: cles}, "fig_compensation_prevu_realise"


# --- 4. Les recettes de la Caisse face à la dépense --------------------------------------

FAMILLES_RECETTES = (("recettes_propres_cgc_bct", "s", VERT, "cgc_charges_bct"),
                     ("recettes_affectees_cgc_minfin", "D", VIOLET, "budget"))


def _recettes_et_depense():
    """Les recettes, et à côté les parts de la dépense en regard, lues dans la série des parts."""
    r = _recettes().copy()
    p = _parts()[["annee", "famille", "poste", "part_depenses_etat_pct", "part_pib_pct"]]
    p = p.rename(columns={"famille": "famille_depense", "poste": "poste_depense",
                          "part_depenses_etat_pct": "part_depenses_etat_depense_pct",
                          "part_pib_pct": "part_pib_depense_pct"})
    return r.merge(p, on=["annee", "famille_depense", "poste_depense"], how="left")


def _trace_suites(ax, d, col, par_segment=False, **style):
    groupes = [g for _, g in d.groupby("segment_pib", sort=False)] if par_segment else [d]
    for g in groupes:
        v = dict(zip(g["annee"].astype(int), g[col]))
        for suite in _suites(v):
            ax.plot(suite, [v[a] for a in suite], **style)


def fig_recettes_caisse(mesure: str = "md"):
    figtools.apply_lang_font()
    d = _recettes_et_depense().sort_values("annee")
    annees = d["annee"].astype(int)
    x0, x1 = int(annees.min()), int(annees.max())
    if mesure == "md":
        fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.5, 6.4), sharex=True,
                                     gridspec_kw=dict(height_ratios=[2, 1.1], hspace=0.08))
    else:
        fig, ax = plt.subplots(figsize=(9.5, 5.4))
        bx = None
    col_r = {"md": "recettes_MDT", "dep": "part_depenses_etat_pct", "pib": "part_pib_pct"}[mesure]
    col_d = {"md": "depense_en_regard_MDT", "dep": None, "pib": "part_pib_depense_pct"}[mesure]
    poignees = []
    for famille, marque, couleur, fam_dep in FAMILLES_RECETTES:
        g = d[(d["famille"] == famille) & d[col_r].notna()]
        if g.empty:
            continue
        _trace_suites(ax, g, col_r, par_segment=(mesure == "pib"), ls="-", lw=1.5,
                      color=couleur, zorder=2)
        for r in g.itertuples(index=False):
            p, = ax.plot([int(r.annee)], [getattr(r, col_r)], marque, ms=5.5, color=couleur,
                         zorder=3)
            texte = (f"{int(r.annee)} · {_lab('f_' + famille)} : "
                     f"{_nombre(getattr(r, col_r), DECIMALES[mesure])}{_unite(mesure)}"
                     f" — {r.document}")
            if not _vide(_note(r.note)):
                texte += f" — {_note(r.note)}"
            figtools.infobulle(p, texte)
        poignees.append(_poignee("f_" + famille, color=couleur, marker=marque, ls="-", lw=1.5,
                                 ms=5.5))
        if col_d:
            st = STYLE_FAMILLE[fam_dep]
            gd = g[g[col_d].notna()]
            _trace_suites(ax, gd, col_d, par_segment=(mesure == "pib"), ls=st["ls"],
                          lw=st["lw"], color=st["color"], zorder=2)
            for r in gd.itertuples(index=False):
                p, = ax.plot([int(r.annee)], [getattr(r, col_d)], st["marker"], ms=st["ms"],
                             color=st["color"], zorder=3)
                figtools.infobulle(p, f"{int(r.annee)} · {_lab('d_' + fam_dep)} : "
                                      f"{_nombre(getattr(r, col_d), DECIMALES[mesure])}"
                                      f"{_unite(mesure)}")
            poignees.append(_poignee("d_" + fam_dep, color=st["color"], marker=st["marker"],
                                     ls=st["ls"], lw=st["lw"], ms=st["ms"]))
        if bx is not None:
            barres = bx.bar(g["annee"].astype(int), g["couverture_pct"], width=0.7,
                            color=couleur, alpha=0.75, zorder=2)
            for barre, r in zip(barres, g.itertuples(index=False)):
                figtools.infobulle(barre, f"{int(r.annee)} · {_lab('couverture')} : "
                                          f"{_nombre(r.couverture_pct)} %")
                bx.annotate(_nombre(r.couverture_pct), xy=(int(r.annee), r.couverture_pct),
                            xytext=(0, 2), textcoords="offset points", ha="center",
                            va="bottom", fontsize=6.5, color=NOIR)
    if mesure == "md":
        _cadre(ax, "md_log", x0, x1, xlabel=False)
        _axe_log(ax)
        _cadre(bx, "pct_couv", x0, x1)
        bx.set_ylim(0, 75)
        bx.set_xticks(list(range(x0, x1 + 1, 2)))
        bx.tick_params(axis="x", labelsize=7.5)
        bx.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.3), ncol=2,
                  fontsize=7.5, frameon=False)
        fig.subplots_adjust(left=0.09, right=0.98, top=0.97, bottom=0.18)
        return fig
    if mesure == "pib":
        _cadre(ax, "pct_pib_log", x0, x1)
        ax.set_yscale("log")
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 2)))
        _marque_ruptures(ax, d.assign(rupture=None), x0, x1, pib=True)
        poignees.append(_poignee_pib(d))
    else:
        _cadre(ax, "pct_dep", x0, x1)
        ax.set_ylim(bottom=0)
        for r in d[d[col_r].notna()].itertuples(index=False):
            ax.annotate(_nombre(getattr(r, col_r), 2), xy=(int(r.annee), getattr(r, col_r)),
                        xytext=(0, 5), textcoords="offset points", ha="center", va="bottom",
                        fontsize=6.5, color=NOIR)
    ax.set_xticks(list(range(x0, x1 + 1, 2)))
    ax.tick_params(axis="x", labelsize=7.5)
    _legende(ax, poignees, ncol=1 if mesure == "pib" else 2)
    fig.tight_layout()
    return fig


def _figure_recettes_caisse():
    d = _recettes_et_depense().sort_values("annee")
    vues = [(_lab("vue_md"), fig_recettes_caisse("md")),
            (_lab("vue_dep"), fig_recettes_caisse("dep")),
            (_lab("vue_pib"), fig_recettes_caisse("pib"))]
    p = _parts()
    regard = p.merge(d[["annee", "famille_depense", "poste_depense"]].rename(
        columns={"famille_depense": "famille", "poste_depense": "poste"}),
        on=["annee", "famille", "poste"])
    cles = {SERIE_RECETTES: list(d["source"]) + [CLE_DEPENSES] + _cles_pib(d),
            SERIE_PARTS: list(regard["source"])}
    return vues, _table(d, COLS_RECETTES), cles, "fig_compensation_recettes_caisse"


def tableau_recettes_affectees(caption: str, tbl_id: str = "tbl-compensation-recettes-affectees",
                               annees=(2009, 2010, 2011)) -> None:
    """Tableau « recettes affectées et dépense », toutes valeurs lues dans les séries.

    Montants et parts des recettes : `compensation-recettes-caisse` ; parts de la dépense :
    `compensation-parts` (dépense budgétaire, total). À appeler dans un chunk `output: asis`
    NON étiqueté : la légende et l'identifiant du tableau sont écrits ici."""
    d = _recettes_et_depense()
    d = d[d["famille"] == "recettes_affectees_cgc_minfin"].set_index("annee")
    lignes = [("t_rec_md", "recettes_MDT", 1), ("t_pct_dep", "part_depenses_etat_pct", 2),
              ("t_pct_pib", "part_pib_pct", 2), ("t_dep_md", "depense_en_regard_MDT", 1),
              ("t_pct_dep", "part_depenses_etat_depense_pct", 2),
              ("t_pct_pib", "part_pib_depense_pct", 2), ("t_couv", "couverture_pct", 1)]
    out = ["| | " + " | ".join(str(a) for a in annees) + " |",
           "|---|" + "---:|" * len(annees)]
    for cle, col, dec in lignes:
        cases = ["" if _vide(d.at[a, col]) else _nombre(float(d.at[a, col]), dec) for a in annees]
        out.append(f"| {_lab(cle)} | " + " | ".join(cases) + " |")
    print("\n".join(out) + f"\n\n: {caption} {{#{tbl_id}}}\n")


# --- 5. Les sources extérieures face aux séries budgétaires ------------------------------

FAMILLES_BUDGETAIRES_ANCIENNES = ("budget_dotation_cgc_bct", "cgc_charges_bct",
                                  "cgc_depenses_bct")
FAMILLES_EXTERIEURES = ("cgc_bm_1985", "fmi_1996", "fmi_2000")
FIN_EXTERIEUR = 1999  # un an après la dernière année du FMI


def _sources_exterieures():
    d = _parts()
    d = d[d["famille"].isin(FAMILLES_BUDGETAIRES_ANCIENNES + FAMILLES_EXTERIEURES)]
    debut = int(d[d["nature"] == "exterieur"]["annee"].min())
    return d[(d["annee"] >= debut) & (d["annee"] <= FIN_EXTERIEUR)]


def fig_sources_exterieures(mesure: str = "pib"):
    figtools.apply_lang_font()
    d = _sources_exterieures()
    col = COLONNE[mesure]
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    familles = FAMILLES_BUDGETAIRES_ANCIENNES + FAMILLES_EXTERIEURES
    traces = [f for f in familles if _trace_famille(ax, d, f, mesure)]
    annees = d[d[col].notna()]["annee"].astype(int)
    x0, x1 = int(annees.min()), int(annees.max())
    _cadre(ax, YLABEL[mesure], x0, x1)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=18))
    ax.set_ylim(bottom=0)
    ax.set_ylim(top=ax.get_ylim()[1] * 1.08)
    _marque_ruptures(ax, d[d[col].notna()], x0, x1, pib=(mesure == "pib"))
    poignees = _legende_familles(traces)
    poignees.append(_poignee("lg_exterieur", color="none"))
    if mesure == "pib":
        poignees.append(_poignee_pib(d))
    _legende(ax, poignees, ncol=1, y=-0.12)
    fig.tight_layout()
    return fig


def _figure_sources_exterieures():
    d = _sources_exterieures().sort_values(["nature", "famille", "annee"])
    vues = [(_lab("vue_pib"), fig_sources_exterieures("pib")),
            (_lab("vue_md"), fig_sources_exterieures("md"))]
    cles = list(d["source"]) + _cles_pib(d)
    return (vues, _table(d, COLS_PARTS), {SERIE_PARTS: cles},
            "fig_compensation_sources_exterieures")


# --- point d'entrée des chapitres --------------------------------------------------------

FIGURES = {
    "longue_periode": _figure_longue_periode,
    "par_poste": _figure_par_poste,
    "prevu_realise": _figure_prevu_realise,
    "recettes_caisse": _figure_recettes_caisse,
    "sources_exterieures": _figure_sources_exterieures,
}


def cles_absentes() -> dict[str, list[str]]:
    """{figure: clés de citation employées mais absentes de la bibliographie du livre}."""
    out = {}
    for nom, fabrique in FIGURES.items():
        _, _, cles, _ = fabrique()
        plt.close("all")
        manque: list[str] = []
        for sid, liste in cles.items():
            manque += [k for k in _declarer(sid, liste) if k not in manque]
        out[nom] = manque
    return out


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure `nom` en onglets (graphique, données, sources).

    À appeler dans un chunk Quarto étiqueté `#| label: fig-…`, `#| output: asis`. La
    provenance des séries est restreinte, le temps de l'appel, aux documents que la figure
    emploie (voir l'en-tête du module)."""
    vues, table, cles, slug = FIGURES[nom]()
    for sid, liste in cles.items():
        _declarer(sid, liste)
    figtools.figure_tabs(vues, table, *cles, slug=slug, caption=caption,
                         note_lecture=note_lecture)
    plt.close("all")

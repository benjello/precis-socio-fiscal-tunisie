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
    2003, première ligne de carburants en 2004, périmètre élargi en 2015. Une seule est
    déclarée ici, d'après la fiche du compte de la Caisse : 1987, où les recettes de la
    Caisse sont intégrées au budget. Leur texte complet est dans l'infobulle du repère triangulaire,
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
import dinars_constants  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import transcriptions as tr  # noqa: E402  (tableaux du volume devenus figures)

SERIE_PARTS = "compensation-parts"
SERIE_PREVU = "compensation-prevu-realise"
SERIE_RECETTES = "compensation-recettes-caisse"
SERIE_COMPTE = "compensation-compte-caisse"
SERIE_AUDIT = "compensation-carburants-audit-2014"
SERIE_BENEF = "compensation-carburants-beneficiaires"
SERIE_PRIX = "prix-carburants"
SERIE_EVENEMENTS = "prix-carburants-evenements"

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
    "fonds_special_lf": dict(color=GRIS, ls="", marker="h", lw=0, ms=7),
    "cgc_bm_1985": dict(color=ROUGE, ls="", marker="P", lw=0, ms=7),
    "fmi_1996": dict(color=ROUGE, ls="", marker="X", lw=0, ms=7),
    "fmi_2000": dict(color=ROUGE, ls="", marker="*", lw=0, ms=9),
    "fmi_2016_energie": dict(color=ROUGE, ls="", marker="d", lw=0, ms=7),
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
    "pct_total": {"fr": "En % du total de la dépense de compensation de l'année",
                  "ar": "% من مجموع نفقات الدعم للسنة"},
    "vue_struct": {"fr": "En part du total de la compensation", "ar": "كنسبة من مجموع الدعم"},
    "c_part_total_compensation_pct": {"fr": "% du total de la compensation",
                                      "ar": "% من مجموع الدعم"},
    "pct_charges": {"fr": "En % du total des charges de l'année",
                    "ar": "% من مجموع أعباء السنة"},
    "pct_ligne": {"fr": "En % de la ligne « carburants » de l'année",
                  "ar": "% من سطر المحروقات للسنة"},
    "ecart_md": {"fr": "Réalisé − prévu (MD)", "ar": "المنجَز − المتوقَّع (م.د)"},
    "millimes": {"fr": "millimes par litre", "ar": "مليم للتر"},
    "millimes_log": {"fr": "Millimes par litre, prix courants\n(échelle logarithmique)",
                     "ar": "مليم للتر، أسعار جارية\n(سلّم لوغاريتمي)"},
    "vue_charges": {"fr": "En part du total des charges", "ar": "كنسبة من مجموع الأعباء"},
    "vue_ligne": {"fr": "En part de la ligne", "ar": "كنسبة من السطر"},
    "vue_h_lf": {"fr": "Lois de finances", "ar": "قوانين المالية"},
    "vue_h_lfc": {"fr": "Lois de finances complémentaires", "ar": "قوانين المالية التكميلية"},
    "vue_h_prev": {"fr": "Prévisions publiées avant l'exercice",
                   "ar": "تقديرات منشورة قبل السنة المالية"},
    "vue_essence": {"fr": "Essence", "ar": "البنزين"},
    "vue_gasoil": {"fr": "Gasoil", "ar": "الغازوال"},
    "solde": {"fr": "Solde de la Caisse", "ar": "رصيد الصندوق"},
    "lg_solde": {"fr": "Solde de la Caisse (excédent positif, déficit négatif), années où "
                       "la source le donne",
                 "ar": "رصيد الصندوق (فائض موجب، عجز سالب)، في السنوات التي يذكره المصدر"},
    "lg_total_charges": {"fr": "tiret : total des charges de l'année",
                         "ar": "شرطة: مجموع أعباء السنة"},
    "lg_rupture_champ": {"fr": "trait vertical : changement du champ des produits "
                               "(infobulle sur le triangle)",
                         "ar": "خطّ عمودي: تغيّر في قائمة المواد (التفاصيل عند المثلّث)"},
    "lg_ligne_carb": {"fr": "Ligne budgétaire « carburants »", "ar": "سطر المحروقات بالميزانية"},
    "lg_besoins": {"fr": "Besoins de financement de l'ensemble STEG-STIR-ETAP, réalisés",
                   "ar": "حاجيات تمويل مجموعة الشركات الثلاث، المنجَزة"},
    "v_rapport_d": {"fr": "Subvention directe, inscrite au budget (rapport de 2014)",
                    "ar": "الدعم المباشر المرسَّم بالميزانية (تقرير 2014)"},
    "v_rapport_i": {"fr": "Subvention indirecte, hors budget (rapport de 2014)",
                    "ar": "الدعم غير المباشر خارج الميزانية (تقرير 2014)"},
    "v_dgre_d": {"fr": "Subvention directe consommée (ventilation de la DGRE)",
                 "ar": "الدعم المباشر المستهلَك (توزيع الإدارة العامة للموارد والتوازنات)"},
    "v_dgre_i": {"fr": "Subvention indirecte (ventilation de la DGRE)",
                 "ar": "الدعم غير المباشر (توزيع الإدارة العامة للموارد والتوازنات)"},
    "fp_arretes_essence": {
        "fr": "Arrêtés de prix publiés au Journal officiel : essence super, prix à sa date "
              "d'effet (en clair, l'essence normale)",
        "ar": "قرارات الأسعار المنشورة بالرائد الرسمي: البنزين الممتاز، السعر في تاريخ سريانه "
              "(باللون الفاتح: البنزين العادي)"},
    "fp_one_gasoil": {
        "fr": "Observatoire national de l'énergie : gasoil ordinaire, prix en vigueur à sa "
              "date, depuis 2017 (en clair, le gasoil sans soufre)",
        "ar": "المرصد الوطني للطاقة: الغازوال العادي، السعر المعمول به في تاريخه، منذ 2017 "
              "(باللون الفاتح: الغازوال الخالي من الكبريت)"},
    "fp_minist_gasoil": {
        "fr": "Ministère chargé de l'énergie : gasoil ordinaire, moyenne annuelle pondérée, "
              "1990-2016 (en clair, le gasoil 50)",
        "ar": "الوزارة المكلّفة بالطاقة: الغازوال العادي، معدّل سنوي مرجَّح، 1990-2016 "
              "(باللون الفاتح: الغازوال 50)"},
    "fp_arretes": {"fr": "Arrêtés de prix publiés au Journal officiel : prix à sa date d'effet",
                   "ar": "قرارات الأسعار المنشورة بالرائد الرسمي: السعر في تاريخ سريانه"},
    "fp_minist": {"fr": "Ministère chargé de l'énergie : moyenne annuelle pondérée, 1990-2016",
                  "ar": "الوزارة المكلّفة بالطاقة: معدّل سنوي مرجَّح، 1990-2016"},
    "fp_ins": {"fr": "INS : moyenne annuelle des prix de détail",
               "ar": "المعهد الوطني للإحصاء: المعدّل السنوي لأسعار التفصيل"},
    "fp_ajust_off": {"fr": "Ajustement daté : date officielle (rapport de 2014, BCT)",
                     "ar": "تعديل مؤرَّخ: تاريخ رسمي (تقرير 2014، البنك المركزي)"},
    "fp_ajust_presse": {"fr": "Ajustement daté : presse",
                        "ar": "تعديل مؤرَّخ: الصحافة"},
    "fp_one": {"fr": "Observatoire national de l'énergie : prix en vigueur à sa date, depuis "
                     "2017",
               "ar": "المرصد الوطني للطاقة: السعر المعمول به في تاريخه، منذ 2017"},
    "fp_bm": {"fr": "Banque mondiale (source extérieure), 2014",
              "ar": "البنك الدولي (مصدر خارجي)، 2014"},
    "lg_evenement": {"fr": "triangle rouge, au pied : étape du mécanisme d'ajustement "
                           "(infobulle)",
                     "ar": "مثلّث أحمر في الأسفل: مرحلة من آلية التعديل (التفاصيل عند المثلّث)"},
    "rp_1968": {"fr": "1968 : prix\nuniforme", "ar": "1968: سعر\nموحَّد"},
    "rp_1992": {"fr": "1992 : essence\nsans plomb", "ar": "1992: بنزين\nخالٍ من الرصاص"},
    "rp_1995": {"fr": "1995 : moyennes\nannuelles", "ar": "1995: معدّلات\nسنوية"},
    "rp_2017": {"fr": "2017 : prix\ndatés", "ar": "2017: أسعار\nمؤرَّخة"},
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
    "f_fmi_2016_energie": {
        "fr": "Subventions à l'énergie, brutes, reconstituées par le FMI (rapport de 2016)",
        "ar": "دعم الطاقة الخام كما أعاد بناءه صندوق النقد الدولي (تقرير 2016)"},
    "fmi_est": {"fr": "est.", "ar": "تقدير"},
    "fmi_proj": {"fr": "proj.", "ar": "إسقاط"},
    "f_fmi_2000": {
        "fr": "Subventions aux consommateurs par la Caisse selon le FMI (rapport de 2000)",
        "ar": "دعم المستهلكين عبر الصندوق حسب صندوق النقد الدولي (تقرير 2000)"},
    "f_recettes_propres_cgc_bct": {
        "fr": "Recettes propres de la Caisse (rapports de la BCT)",
        "ar": "الموارد الذاتية للصندوق (تقارير البنك المركزي)"},
    "f_recettes_affectees_cgc_minfin": {
        "fr": "Recettes affectées du compte de la Caisse (ministère des Finances)",
        "ar": "الموارد المخصَّصة لحساب الصندوق (وزارة المالية)"},
    "f_recettes_totales_cgc_bct": {
        "fr": "Recettes de toute nature de la Caisse (rapports de la BCT)",
        "ar": "موارد الصندوق بجميع أصنافها (تقارير البنك المركزي)"},
    "d_cgc_depenses_bct": {"fr": "Dépense en regard : dépenses du fonds spécial",
                           "ar": "النفقات المقابلة: نفقات الصندوق الخاص"},
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
    "lg_pib_nr": {"fr": " ; « n. r. » : valeur propre au ministère, rattachée à aucune base",
                  "ar": "؛ «غ. م.»: قيمة خاصّة بالوزارة غير مربوطة بسنة أساس"},
    "lg_pib_bm": {"fr": " ; « BM » : PIB de la Banque mondiale",
                  "ar": "؛ «ب. د.»: ناتج البنك الدولي"},
    "lg_bloc_budgetaire": {
        "fr": "Budgétaire (lois de finances, ministère des Finances, rapports de la BCT qui "
              "les relaient)",
        "ar": "الميزانية (قوانين المالية، وزارة المالية، تقارير البنك المركزي الناقلة عنها)"},
    "lg_bloc_exterieur": {"fr": "Rapports extérieurs (Banque mondiale, FMI)",
                          "ar": "التقارير الخارجية (البنك الدولي، صندوق النقد الدولي)"},
    "lg_bloc_reperes": {"fr": "Repères", "ar": "علامات"},
    # ruptures (repères courts ; le texte complet est dans les données)
    "rup_2003": {"fr": "2003 : dépense\nen trois postes", "ar": "2003: نفقات\nبثلاثة أبواب"},
    "rup_2004": {"fr": "2004 : première ligne\nde carburants",
                 "ar": "2004: أوّل سطر\nللمحروقات"},
    "rup_2015": {"fr": "2015 : périmètre\nélargi", "ar": "2015: توسيع\nالنطاق"},
    "rup_1987": {"fr": "1987 : recettes de la Caisse\nintégrées au budget",
                 "ar": "1987: إدماج موارد\nالصندوق في الميزانية"},
    "retropolee": {"fr": "(rétropolée)", "ar": "(معاد احتسابها)"},
    "retropolee_p": {"fr": "(rétropolée {a}-{b})", "ar": "(معاد احتسابها {a}-{b})"},
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
    "c_page_imprimee": {"fr": "Page", "ar": "الصفحة"},
    "c_page_pdf": {"fr": "Page du fichier", "ar": "صفحة الملف"},
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
    "c_pib_retropole": {"fr": "PIB rétropolé", "ar": "ناتج معاد احتسابه"},
    "c_rupture_pib": {"fr": "Rupture du PIB", "ar": "انقطاع الناتج"},
    "c_plan": {"fr": "Plan", "ar": "المخطّط"},
    "c_periode": {"fr": "Période", "ar": "الفترة"},
    "c_prevu_pct_pib": {"fr": "Prévu (% du PIB)", "ar": "المتوقَّع (% من الناتج)"},
    "c_realise_pct_pib_publie": {"fr": "Réalisé, % du PIB publié",
                                 "ar": "المنجَز، % من الناتج المنشورة"},
    "c_realise_pct_pib_calcule": {"fr": "Réalisé, % du PIB calculé",
                                  "ar": "المنجَز، % من الناتج المحسوبة"},
    "c_ecart_points_pib": {"fr": "Écart (points de PIB)", "ar": "الفارق (نقاط من الناتج)"},
    "c_sens": {"fr": "Sens", "ar": "الاتّجاه"},
    "c_rubrique": {"fr": "Rubrique", "ar": "البند"},
    "c_part_total_charges_pct": {"fr": "% du total des charges", "ar": "% من مجموع الأعباء"},
    "c_valeur": {"fr": "Valeur", "ar": "القيمة"},
    "c_unite": {"fr": "Unité", "ar": "الوحدة"},
    "c_ligne_carburants_MDT": {"fr": "Ligne « carburants » (MD)", "ar": "سطر المحروقات (م.د)"},
    "c_part_de_la_ligne_pct": {"fr": "% de la ligne", "ar": "% من السطر"},
    "c_date_effet": {"fr": "Date d'effet", "ar": "تاريخ السريان"},
    "c_produit": {"fr": "Produit", "ar": "المنتوج"},
    "c_prix_millimes": {"fr": "Prix (millimes)", "ar": "السعر (بالمليم)"},
    "c_nature_du_prix": {"fr": "Nature du prix", "ar": "طبيعة السعر"},
    "c_reference": {"fr": "Référence", "ar": "المرجع"},
    "c_date_du_texte": {"fr": "Date du texte", "ar": "تاريخ النصّ"},
    "c_mecanisme": {"fr": "Mécanisme", "ar": "الآلية"},
    "c_horizon": {"fr": "Horizon de la prévision", "ar": "أفق التقدير"},
    "c_prevu_MDT": {"fr": "Prévu (MD)", "ar": "المتوقَّع (م.د)"},
    "c_etat_prevu": {"fr": "Libellé du prévu", "ar": "تسمية المتوقَّع"},
    "c_source_prevu": {"fr": "Source du prévu", "ar": "مصدر المتوقَّع"},
    "c_page_imprimee_prevu": {"fr": "Page (prévu)", "ar": "الصفحة (المتوقَّع)"},
    "c_page_pdf_prevu": {"fr": "Page du fichier (prévu)", "ar": "صفحة الملف (المتوقَّع)"},
    "c_realise_MDT": {"fr": "Réalisé (MD)", "ar": "المنجَز (م.د)"},
    "c_etat_realise": {"fr": "État du réalisé", "ar": "حالة المنجَز"},
    "c_source_realise": {"fr": "Source du réalisé", "ar": "مصدر المنجَز"},
    "c_page_pdf_realise": {"fr": "Page du fichier (réalisé)", "ar": "صفحة الملف (المنجَز)"},
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


COLONNE = {"md": "valeur_MDT", "dep": "part_depenses_etat_pct", "pib": "part_pib_pct",
           "struct": "part_total_compensation_pct"}
YLABEL = {"md": "md", "dep": "pct_dep", "pib": "pct_pib", "struct": "pct_total"}
DECIMALES = {"md": 1, "dep": 2, "pib": 2, "struct": 1}


# --- lecture des séries ------------------------------------------------------------------

def _parts():
    return figtools.series(SERIE_PARTS)


def _prevu():
    return figtools.series(SERIE_PREVU)


def _recettes():
    return figtools.series(SERIE_RECETTES)


def _serie(series_id: str):
    return figtools.series(series_id)


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


# Tournures de relevé, bannies du texte rendu : la partie de note qui en porte une est omise
# de la table affichée (elle reste dans la série).
_RE_RELEVE = re.compile(r"relu|couche texte|à l'image", re.IGNORECASE)

# Périmètre et réserves affichés dans l'onglet « Sources » et dans l'en-tête des fichiers
# téléchargés. Ceux du catalogue de l'entrepôt s'adressent à qui trace la série (noms de
# colonnes, consignes de tracé, journal de relevé) ; ceux-ci disent la même chose au lecteur.
# Les versions arabes du catalogue sont déjà rédigées pour le lecteur et sont gardées.
PROVENANCE_LECTEUR = {
    SERIE_PARTS: dict(
        perimetre=("une valeur par année, par série et par poste, avec sa source et son état, "
                   "et trois parts calculées : dans les dépenses de l'État hors service de la "
                   "dette et dans les dépenses de fonctionnement (séries budgétaires de l'État, "
                   "1986-2025), dans le PIB (PIB du ministère des Finances 1986-2025, Banque "
                   "mondiale avant 1986)"),
        caveats=("Les séries ne se raccordent pas. La part du PIB se lit par segments : le PIB "
                 "change de source ou de base en 1986, 1997, 2002, 2005, 2010 et 2025. "
                 "Les dépenses de l'État sont hors service de la dette. Carburants : périmètre "
                 "élargi en 2015. 2025 et 2026 sont des lois de finances.")),
    SERIE_PREVU: dict(
        perimetre=("chaque prévision (XIe Plan 2007-2011 ; lois de finances et lois de "
                   "finances complémentaires 2012-2026, par poste ; prévisions initiales des "
                   "charges de la Caisse 1986-2011 citées par la Banque centrale), en regard de "
                   "la valeur de la même série et du même poste"),
        caveats=("Le prévu et le réalisé sont toujours de la même série. Le réalisé de "
                 "2012-2013 et de 2019-2024 est une colonne que la source ne qualifie pas ; les "
                 "prévisions de 2019-2023 sont des colonnes d'années à venir, sans étiquette, "
                 "des rapports de la Banque centrale ; 2025 et 2026 n'ont pas de réalisé. Les "
                 "lois de finances initiales de 2012, 2014 et 2015 n'y figurent pas. Un seul "
                 "plan de développement est chiffré, le XIe, par une annexe du ministère des "
                 "Finances.")),
    SERIE_COMPTE: dict(
        caveats=("La grandeur qui pèse sur le budget est la dotation, non les charges. "
                 "Rupture de 1987 : les recettes de la Caisse sont intégrées au budget, la "
                 "dotation passe de 68 à 189 millions de dinars sans hausse des charges. "
                 "Dotation non donnée par le rapport en 1988-1990, 2000-2001, 2003, 2006, "
                 "2008-2009 et 2011 : laissée vide, jamais déduite des charges. Charges par "
                 "produit incomplètes pour 1985, 1992, 1993 et 1995. Le champ des produits "
                 "change. La part du PIB se lit par segments.")),
    SERIE_AUDIT: dict(
        caveats=("Grandeur distincte de la ligne budgétaire « carburants ». Deux ventilations "
                 "du même total, qui ne s'additionnent pas. Deux lignes de 2011 sont "
                 "douteuses dans la source.")),
    SERIE_BENEF: dict(
        perimetre=("répartition de la dépense budgétaire de compensation des carburants entre "
                   "l'ETAP, la STEG et la STIR ; la somme est égale à la ligne « carburants » "
                   "de l'année"),
        caveats=("Répartition non connue ici pour 2013 et après 2016. Zéro : « néant » dit "
                 "par la source. En 2015 l'ETAP sort de la ligne (périmètre élargi : la STEG "
                 "et la STIR achètent au prix mondial).")),
    SERIE_PRIX: dict(
        caveats=("Dix familles de sources, non raccordées : un prix daté, une moyenne "
                 "annuelle et un relevé mensuel ne sont pas la même grandeur. Ajustements de "
                 "1997-2000 déduits par le calcul ; ceux de 2002-2018 en partie connus par la "
                 "presse reprenant les communiqués. Moyenne du ministère pour 2001 suspecte ; "
                 "moyennes de l'INS pour 2011 fausses de 50 millimes. Ruptures : prix uniforme "
                 "le 10 décembre 1968, sans plomb en 1992, essence normale puis super dans "
                 "l'annuaire en 2006. Prix inchangés depuis le 24 novembre 2022.")),
    SERIE_RECETTES: dict(
        caveats=("Deux séries de recettes et deux dépenses en regard, qui ne se raccordent "
                 "pas. Aucune valeur pour 1987-1990, 1997 et 2000-2008. PIB : celui du "
                 "ministère des Finances, par segments ; Banque mondiale en 1984-1985.")),
}


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
    champs.update(PROVENANCE_LECTEUR.get(series_id, {}))
    # « (fichier à tracer) » est une consigne d'atelier, pas un titre.
    champs["titre"] = str(origine.get("titre", series_id)).replace(" (fichier à tracer)", "")
    figtools.register_provenance(series_id, **champs)
    return [k for k in cles if k not in connues]


# --- tables de données -------------------------------------------------------------------

def _note(v):
    if _vide(v):
        return v
    morceaux = [m for m in str(v).split(" ; ") if not _RE_RELEVE.search(m)]
    return _lisible(" ; ".join(morceaux)) if morceaux else None


def _lisible(v):
    """Une cellule de texte telle qu'elle est affichée : sans les noms de code de l'entrepôt
    ni ce qui décrit son contenu plutôt que la donnée. La série garde le texte d'origine."""
    if _vide(v):
        return v
    t = str(v).replace("la famille `budget`", "la dépense budgétaire en trois postes")
    t = t.replace(" (aucune série de base connue avant 1992 dans l'entrepôt)", "")
    t = t.replace(", état non relevé", "")
    return t.replace("`", "")


def _table(d, colonnes):
    """Table affichée et téléchargée : toutes les colonnes de provenance, intitulés traduits.

    Les colonnes `lecture` (journal de relevé de l'entrepôt) ne sont pas reprises."""
    d = d.copy()
    out = {}
    for col in colonnes:
        if col == "famille":
            out[_lab("c_famille")] = d["famille"].map(
                lambda f: _lab("f_" + f) if "f_" + f in _L else f)
            out[_lab("c_code_famille")] = d["famille"]
        elif col in ("poste", "poste_depense"):
            out[_lab("c_" + col)] = d[col].map(lambda p: _lab("p_" + p))
        elif col == "famille_depense":
            out[_lab("c_" + col)] = d[col].map(lambda f: _lab("f_" + f))
        elif col == "note":
            out[_lab("c_note")] = d[col].map(_note)
        elif col.startswith("page_"):  # numéros de page : entiers, vides admis
            out[_lab("c_" + col)] = d[col].astype("Int64")
        elif d[col].dtype == object:
            out[_lab("c_" + col)] = d[col].map(_lisible)
        else:
            out[_lab("c_" + col)] = d[col]
    import pandas as pd
    return pd.DataFrame(out).reset_index(drop=True)


def _table_simple(d, colonnes):
    """Table des séries sans famille ni poste codés : colonnes telles quelles, intitulés
    traduits, notes et textes passés par les mêmes filtres que `_table`."""
    import pandas as pd
    out = {}
    for col in colonnes:
        if col == "note":
            out[_lab("c_note")] = d[col].map(_note)
        elif col.startswith("page_"):
            out[_lab("c_" + col)] = d[col].astype("Int64")
        elif d[col].dtype == object:
            out[_lab("c_" + col)] = d[col].map(_lisible)
        else:
            out[_lab("c_" + col)] = d[col]
    return pd.DataFrame(out).reset_index(drop=True)


COLS_PARTS = ["annee", "famille", "nature", "poste", "valeur_MDT", "etat_norme", "etat",
              "part_depenses_etat_pct", "part_pib_pct", "source", "document", "page_imprimee",
              "page_pdf", "note", "depenses_etat_hors_dette_MDT", "depenses_fonctionnement_MDT",
              "part_depenses_fonctionnement_pct", "pib_MDT", "source_pib", "base_pib",
              "segment_pib", "pib_retropole", "rupture_pib", "rupture"]
COLS_PREVU = ["annee", "famille", "nature", "poste", "horizon", "prevu_MDT", "realise_MDT",
              "ecart_MDT", "ecart_pct", "etat_prevu", "source_prevu", "page_imprimee_prevu",
              "page_pdf_prevu", "etat_realise", "source_realise", "page_pdf_realise", "note",
              "plan", "periode", "prevu_pct_pib", "realise_pct_pib_publie",
              "realise_pct_pib_calcule", "ecart_points_pib"]
COLS_RECETTES = ["annee", "famille", "nature", "recettes_MDT", "famille_depense",
                 "poste_depense", "depense_en_regard_MDT", "couverture_pct",
                 "part_depenses_etat_pct", "part_pib_pct", "part_depenses_etat_depense_pct",
                 "part_pib_depense_pct", "etat", "source", "document", "page_imprimee",
                 "page_pdf", "note", "depenses_etat_hors_dette_MDT", "pib_MDT", "source_pib",
                 "base_pib", "segment_pib", "pib_retropole", "rupture_pib",
                 "produits_de_base_MDT",
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


# Rupture déclarée ici, la colonne `rupture` ne la portant pas : fiche du compte de la Caisse
# (Banque centrale, rapport annuel 1987, p. 71).
FAMILLES_1987 = ("budget_dotation_cgc_bct", "recettes_propres_cgc_bct")
RUPTURE_1987 = ("1987 : la loi de finances intègre au budget les recettes fiscales et "
                "parafiscales de la Caisse ; la dotation passe de 68 à 189 MD — changement de "
                "mode de financement, non de coût")


def _ruptures_des_donnees(d) -> dict[int, dict[str, list[str]]]:
    """{année: {"pib": […], "champ": […], "serie": […]}} d'après la colonne `rupture`.

    « PIB … » : changement de source ou de base du dénominateur ; « champ : … » : entrée ou
    sortie d'un produit ; le reste : changement de la série elle-même, à marquer d'un trait."""
    out: dict[int, dict[str, list[str]]] = {}
    if "famille" in d and d["famille"].isin(FAMILLES_1987).any():
        out[1987] = {"serie": [RUPTURE_1987]}
    for r in d[d["rupture"].notna()].itertuples(index=False):
        # Un texte peut réunir plusieurs ruptures, séparées par « ; » ; un morceau qui n'ouvre
        # pas une rupture (« PIB… », « champ : … », « carburants : … ») continue la précédente.
        ruptures: list[str] = []
        for m in str(r.rupture).split(" ; "):
            if ruptures and not m.startswith(("PIB", "champ", "carburants", "première", "2015")):
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


def _marque_ruptures(ax, d, x0, x1, pib=False, cote=None, bas=False):
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
            # `bas` : libellés au pied du cadre, quand les courbes occupent le haut (niveaux).
            dy = 4 + 22 * (niveau % 2 if not gauche else 0)
            ax.annotate(_ft(cle), xy=(a - 0.5, 0 if bas else 1),
                        xycoords=("data", "axes fraction"),
                        xytext=(-4 if gauche else 4, dy if bas else -dy),
                        textcoords="offset points", ha="right" if gauche else "left",
                        va="bottom" if bas else "top",
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
        texte = _ft(cle)
        if "pib_retropole" in d and base.startswith("base"):
            ds = d[d["segment_pib"].astype(str).str.contains(f"{a0}-{a1}", regex=False)]
            retro = sorted(ds[ds["pib_retropole"] == "oui"]["annee"].astype(int).unique())
            if retro and not (ds["pib_retropole"] == "non").any():
                texte += "\n" + _ft("retropolee")
            elif retro:
                texte += "\n" + _ft("retropolee_p", a=retro[0], b=retro[-1])
        ax.annotate(texte, xy=((a0c + a1c) / 2, 1), xycoords=("data", "axes fraction"),
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
                     cote={2003: "gauche"}, bas=(mesure == "md"))
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
    """La dépense budgétaire par poste, avec la part de chaque poste dans le total de l'année.

    Cette part est la seule grandeur calculée ici : valeur du poste / valeur de la ligne
    « total » de la même année (même famille, et un seul état retenu par année). Les trois
    postes somment au total chaque année ; `ecarts_au_total()` le contrôle."""
    d = _parts()
    d = d[d["famille"] == "budget"].copy()
    total = d[d["poste"] == "total"].set_index("annee")["valeur_MDT"]
    d["part_total_compensation_pct"] = (100 * d["valeur_MDT"] / d["annee"].map(total)).round(1)
    return d


def ecarts_au_total(seuil: float = 0.05) -> dict[int, float]:
    """{année: somme des trois postes − total} pour les années où l'écart dépasse `seuil` MD."""
    d = _par_poste().pivot(index="annee", columns="poste", values="valeur_MDT").fillna(0)
    e = (d["produits_de_base"] + d["carburants"] + d["transport"] - d["total"]).round(2)
    return {int(a): float(v) for a, v in e.items() if abs(v) > seuil}


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
            if mesure == "struct" and v >= 6:  # pourcentage dans la barre, si la place le permet
                ax.annotate(_nombre(v, 0), xy=(a, bas + v / 2), ha="center", va="center",
                            fontsize=6.2, color=NOIR, zorder=4,
                            bbox=dict(facecolor="white", edgecolor="none", alpha=0.75, pad=0.6))
            bas += v
        if mesure == "struct":
            continue
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
    if mesure == "struct":
        ax.set_ylim(0, 118)  # la marge du haut porte les libellés de rupture
        ax.set_yticks(range(0, 101, 20))
    else:
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
            (_lab("vue_pib"), fig_par_poste("pib")), (_lab("vue_struct"), fig_par_poste("struct"))]
    cles = list(d["source"]) + [CLE_DEPENSES] + _cles_pib(d)
    colonnes = list(COLS_PARTS)
    colonnes.insert(colonnes.index("valeur_MDT") + 1, "part_total_compensation_pct")
    return vues, _table(d, colonnes), {SERIE_PARTS: cles}, "fig_compensation_par_poste"


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
    # Les lignes de plan en cumul ou en part du PIB ne sont pas des prévisions annuelles en
    # dinars : elles restent dans les données.
    d = d[d["horizon"].isin(STYLE_HORIZON) & d["prevu_MDT"].notna()]
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
    # « compensation-depense » y désigne un cumul de la série elle-même, non un document.
    cles = [k for k in list(d["source_prevu"]) + list(d["source_realise"])
            if not str(k).startswith("compensation-")]
    return vues, _table(d, COLS_PREVU), {SERIE_PREVU: cles}, "fig_compensation_prevu_realise"


# --- 4. Les recettes de la Caisse face à la dépense --------------------------------------

FAMILLES_RECETTES = (("recettes_totales_cgc_bct", "o", GRIS, "cgc_depenses_bct"),
                     ("recettes_propres_cgc_bct", "s", VERT, "cgc_charges_bct"),
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
        bx.set_ylim(0, 120)
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


# --- 5. Vue d'ensemble : séries budgétaires et rapports extérieurs ------------------------

FAMILLES_BUDGETAIRES = ("budget", "budget_dotation_cgc_bct", "budget_compensation_bct",
                        "cgc_charges_bct", "cgc_depenses_bct", "fonds_special_lf")
FAMILLES_EXTERIEURES = ("cgc_bm_1985", "fmi_1996", "fmi_2000")
DEBUT_ENSEMBLE = 1982  # première année des rapports extérieurs ; 1971 reste dans les données


def _sources_exterieures():
    """Toutes les familles retenues de la série ; pour la dépense budgétaire, le total."""
    d = _parts()
    d = d[d["famille"].isin(FAMILLES_BUDGETAIRES + FAMILLES_EXTERIEURES)]
    return d[(d["famille"] != "budget") | (d["poste"] == "total")]


SERIE_FMI_ENERGIE = "compensation-fmi-2016-energie-brute"
figtools.register_provenance(
    SERIE_FMI_ENERGIE,
    titre="Les subventions à l'énergie reconstituées en brut par le FMI, 2012-2016",
    sources=[tr.FMI_ENERGIE_CLE], unite="millions de dinars courants",
    perimetre=("ligne « Energy subsidies (gross) » du tableau des opérations de l'administration "
               "centrale du rapport de 2016 (tableau 4a), rétropolée par les services du FMI "
               "jusqu'en 2012"),
    caveats=("Série reconstituée par le FMI, non la ligne budgétaire ; 2015 est une estimation, "
             "2016 une projection. Les parts du PIB du rapport ne sont pas reprises : la part "
             "tracée est calculée sur le PIB des autres séries de la même année."))


def _fmi_energie():
    """La série du FMI de 2016, aux colonnes de la série des parts : part du PIB calculée sur le
    PIB de la dépense budgétaire de la même année (même dénominateur que les autres séries)."""
    import pandas as pd
    parts = _parts()
    pib = {int(r.annee): r for r in parts[(parts["famille"] == "budget")
                                          & (parts["poste"] == "total")].itertuples(index=False)}
    lignes = []
    for a, v, etat in tr.FMI_ENERGIE:
        r = pib.get(a)
        lignes.append(dict(
            annee=a, famille="fmi_2016_energie", nature="exterieur", poste="carburants",
            valeur_MDT=float(v), etat="ligne « Energy subsidies (gross) »", etat_norme=etat,
            source=tr.FMI_ENERGIE_CLE,
            document=f"FMI, rapport de 2016 (n° 16/138), {tr.FMI_ENERGIE_LOC}",
            pib_MDT=r.pib_MDT if r is not None else None,
            source_pib=r.source_pib if r is not None else None,
            base_pib=r.base_pib if r is not None else None,
            segment_pib=r.segment_pib if r is not None else None,
            pib_retropole=r.pib_retropole if r is not None else None,
            part_pib_pct=round(100 * v / r.pib_MDT, 2) if r is not None else None))
    return pd.DataFrame(lignes)


def _trace_fmi_energie(ax, mesure) -> bool:
    """Marques sans trait ; l'estimation et la projection en marques creuses, étiquetées."""
    if mesure not in ("md", "pib"):
        return False
    st = STYLE_FAMILLE["fmi_2016_energie"]
    col = COLONNE[mesure]
    for r in _fmi_energie().itertuples(index=False):
        v = getattr(r, col)
        if _vide(v):
            continue
        creux = r.etat_norme in ("estimation", "projection")
        p, = ax.plot([r.annee], [v], st["marker"], ms=st["ms"], color=st["color"],
                     mfc="white" if creux else st["color"], zorder=5)
        figtools.infobulle(p, f"{r.annee} · {_lab('f_fmi_2016_energie')} : "
                              f"{_nombre(v, DECIMALES[mesure])}{_unite(mesure)} — {r.etat_norme}")
        if creux:
            ax.annotate(_lab("fmi_est" if r.etat_norme == "estimation" else "fmi_proj"),
                        xy=(r.annee, v), xytext=(5, -2), textcoords="offset points",
                        fontsize=6.5, color=st["color"])
    return True


def fig_sources_exterieures(mesure: str = "pib"):
    figtools.apply_lang_font()
    d = _sources_exterieures()
    d = d[d["annee"] >= DEBUT_ENSEMBLE]
    col = COLONNE[mesure]
    fig, ax = plt.subplots(figsize=(9.5, 5.8))
    budgetaires = [f for f in FAMILLES_BUDGETAIRES if _trace_famille(ax, d, f, mesure)]
    exterieures = [f for f in FAMILLES_EXTERIEURES if _trace_famille(ax, d, f, mesure)]
    if _trace_fmi_energie(ax, mesure):
        exterieures.append("fmi_2016_energie")
    trace = d[d[col].notna()]
    annees = trace["annee"].astype(int)
    x0, x1 = int(annees.min()), int(annees.max())
    _cadre(ax, "md_log" if mesure == "md" else YLABEL[mesure], x0, x1)
    if mesure == "md":
        _axe_log(ax)
    else:
        ax.set_ylim(bottom=0)
        ax.set_ylim(top=ax.get_ylim()[1] * 1.12)
    _marque_ruptures(ax, trace, x0, x1, pib=(mesure == "pib"), cote={2003: "gauche"},
                     bas=(mesure == "md"))
    # Légende en blocs titrés : budgétaire, rapports extérieurs, repères.
    titres = []

    def titre(cle):
        titres.append(len(poignees))
        poignees.append(_poignee(cle, color="none"))

    poignees: list = []
    titre("lg_bloc_budgetaire")
    poignees += _legende_familles(budgetaires)
    if exterieures:
        titre("lg_bloc_exterieur")
        poignees += _legende_familles(exterieures)
    titre("lg_bloc_reperes")
    poignees.append(_poignee("lg_prevu", color=GRIS, marker="o", mfc="white", ls=(0, (1, 2)),
                             lw=1.2))
    poignees.append(_poignee("lg_rupture", color=GRIS, ls=(0, (2, 2)), lw=1, marker=7, ms=5))
    if mesure == "pib":
        poignees.append(_poignee_pib(trace))
    legende = ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, 0),
                        borderaxespad=4.2, ncol=1, fontsize=7.2, frameon=False)
    for i in titres:
        legende.get_texts()[i].set_fontweight("bold")
    fig.tight_layout()
    return fig


def _figure_sources_exterieures():
    import pandas as pd
    d = pd.concat([_sources_exterieures(), _fmi_energie()], ignore_index=True)
    d = d.sort_values(["nature", "famille", "annee"])
    vues = [(_lab("vue_pib"), fig_sources_exterieures("pib")),
            (_lab("vue_dep"), fig_sources_exterieures("dep")),
            (_lab("vue_md"), fig_sources_exterieures("md"))]
    cles = [k for k in d["source"] if k != tr.FMI_ENERGIE_CLE] + [CLE_DEPENSES] + _cles_pib(d)
    return (vues, _table(d, COLS_PARTS),
            {SERIE_PARTS: cles, SERIE_FMI_ENERGIE: [tr.FMI_ENERGIE_CLE]},
            "fig_compensation_sources_exterieures")


# --- 6. Le compte de la Caisse -----------------------------------------------------------

DEBUT_COMPTE, FIN_COMPTE = 1984, 2011
RUB_CHARGES = "total des charges"
RUB_RECETTES = "recettes propres de la Caisse"
RUB_DOTATION = "dotation du budget de l'État"
COLS_COMPTE = ["annee", "sens", "rubrique", "valeur_MDT", "part_total_charges_pct", "famille",
               "nature", "etat", "part_depenses_etat_pct", "part_pib_pct", "source", "document",
               "page_imprimee", "page_pdf", "note", "depenses_etat_hors_dette_MDT", "pib_MDT",
               "source_pib", "base_pib", "segment_pib", "pib_retropole", "rupture"]


def _compte():
    """Le compte de la Caisse, avec la part de chaque charge dans le total des charges de
    l'année (seule grandeur calculée ici : rubrique / « total des charges », même famille)."""
    d = _serie(SERIE_COMPTE).copy()
    tot = d[(d["rubrique"] == RUB_CHARGES)].set_index("annee")["valeur_MDT"]
    charge = (d["sens"] == "charge") & (d["famille"] == "cgc_charges_bct")
    d["part_total_charges_pct"] = (100 * d["valeur_MDT"] / d["annee"].map(tot)).where(charge).round(1)
    return d


def _compte_et_budget():
    """Lignes du compte (totaux, ressources, solde) et, à leur suite, la dépense budgétaire en
    trois postes lue dans la série des parts, ramenée aux colonnes du compte."""
    import pandas as pd
    c = _compte()
    c = c[(c["sens"] != "charge") | (c["rubrique"] == RUB_CHARGES)]
    c = c[c["annee"] >= DEBUT_COMPTE]
    b = _parts()
    b = b[(b["famille"] == "budget") & (b["poste"] == "total")].copy()
    b["sens"] = "dépense du budget"
    b["rubrique"] = "dépense budgétaire de compensation, trois postes"
    return pd.concat([c, b[[k for k in c.columns if k in b.columns]]], ignore_index=True)


def fig_compte_caisse(mesure: str = "md"):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    if mesure == "md":
        c = _compte()
        c = c[(c["annee"] >= DEBUT_COMPTE) & (c["annee"] <= FIN_COMPTE) & c["valeur_MDT"].notna()]
        solde = c[c["sens"] == "solde"]
        barres = ax.bar(solde["annee"].astype(int), solde["valeur_MDT"], width=0.6,
                        color="#afb8c1", edgecolor="#8c959f", zorder=2)
        for barre, r in zip(barres, solde.itertuples(index=False)):
            figtools.infobulle(barre, f"{int(r.annee)} · {_lab('solde')} ({r.rubrique}) : "
                                      f"{_nombre(r.valeur_MDT)}{_unite('md')} — {r.document}")
        lignes = ((RUB_CHARGES, "cgc_charges_bct", "f_cgc_charges_bct"),
                  (RUB_DOTATION, "budget_dotation_cgc_bct", "f_budget_dotation_cgc_bct"),
                  (RUB_RECETTES, None, "f_recettes_propres_cgc_bct"))
        poignees = []
        for rub, fam, cle in lignes:
            st = STYLE_FAMILLE[fam] if fam else dict(color=VERT, ls="-", marker="s", lw=1.5, ms=5)
            g = c[c["rubrique"] == rub].sort_values("annee")
            v = dict(zip(g["annee"].astype(int), g["valeur_MDT"]))
            for suite in _suites(v):
                ax.plot(suite, [v[a] for a in suite], ls=st["ls"], lw=st["lw"], color=st["color"],
                        zorder=3)
            for r in g.itertuples(index=False):
                p, = ax.plot([int(r.annee)], [r.valeur_MDT], st["marker"], ms=st["ms"],
                             color=st["color"], zorder=4)
                figtools.infobulle(p, f"{int(r.annee)} · {_lab(cle)} : {_nombre(r.valeur_MDT)}"
                                      f"{_unite('md')} — {r.document}")
            poignees.append(_poignee(cle, color=st["color"], ls=st["ls"], lw=st["lw"],
                                     marker=st["marker"], ms=st["ms"]))
        poignees.append(Patch(facecolor="#afb8c1", edgecolor="#8c959f",
                              label=figtools.fig_text(_lab("lg_solde"))))
        poignees.append(_poignee("lg_rupture", color=GRIS, ls=(0, (2, 2)), lw=1, marker=7, ms=5))
        _cadre(ax, "md", DEBUT_COMPTE, FIN_COMPTE)
        ax.axhline(0, color=NOIR, lw=0.8, zorder=1)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0)))
        ax.set_xticks(range(DEBUT_COMPTE, FIN_COMPTE + 1, 2))
        ax.set_ylim(top=ax.get_ylim()[1] * 1.1)
        _marque_ruptures(ax, c, DEBUT_COMPTE, FIN_COMPTE)
        _legende(ax, poignees, ncol=1, y=-0.12)
        fig.tight_layout()
        return fig
    # Parts : la dotation, et à partir de 2003 la dépense budgétaire en trois postes.
    d = _parts()
    d = d[(d["annee"] >= DEBUT_COMPTE)
          & ((d["famille"] == "budget_dotation_cgc_bct")
             | ((d["famille"] == "budget") & (d["poste"] == "total")))]
    col = COLONNE[mesure]
    traces = [f for f in ("budget_dotation_cgc_bct", "budget") if _trace_famille(ax, d, f, mesure)]
    trace = d[d[col].notna()]
    x0, x1 = int(trace["annee"].min()), int(trace["annee"].max())
    _cadre(ax, YLABEL[mesure], x0, x1)
    ax.set_ylim(bottom=0)
    ax.set_ylim(top=ax.get_ylim()[1] * 1.12)
    _marque_ruptures(ax, trace, x0, x1, pib=(mesure == "pib"), cote={2003: "gauche"})
    poignees = _legende_familles(traces)
    poignees.append(_poignee("lg_prevu", color=GRIS, marker="o", mfc="white", ls=(0, (1, 2)),
                             lw=1.2))
    poignees.append(_poignee("lg_rupture", color=GRIS, ls=(0, (2, 2)), lw=1, marker=7, ms=5))
    if mesure == "pib":
        poignees.append(_poignee_pib(trace))
    _legende(ax, poignees, ncol=1, y=-0.12)
    fig.tight_layout()
    return fig


def _figure_compte_caisse():
    d = _compte_et_budget().sort_values(["sens", "rubrique", "annee"])
    vues = [(_lab("vue_md"), fig_compte_caisse("md")), (_lab("vue_dep"), fig_compte_caisse("dep")),
            (_lab("vue_pib"), fig_compte_caisse("pib"))]
    c = d[d["sens"] != "dépense du budget"]
    b = d[d["sens"] == "dépense du budget"]
    cles = {SERIE_COMPTE: list(c["source"]) + [CLE_DEPENSES] + _cles_pib(c),
            SERIE_PARTS: list(b["source"])}
    return vues, _table(d, COLS_COMPTE), cles, "fig_compensation_compte_caisse"


# --- 7. Les charges de la Caisse par produit ---------------------------------------------

PRODUITS = (("céréales et dérivés", BLEU, ""), ("huiles", ORANGE, "////"),
            ("sucre", VIOLET, "...."), ("lait", VERT, "xxxx"), ("engrais", BRUN, "\\\\\\\\"),
            ("papier scolaire", ROUGE, "++"), ("pâtes alimentaires et couscous", "#bf8700", "oo"),
            ("double concentré de tomate", "#bc4c00", "--"), ("autres", GRIS, ""))


def _par_produit():
    d = _compte()
    d = d[(d["sens"] == "charge") & (d["famille"] == "cgc_charges_bct")]
    detail = d[d["rubrique"] != RUB_CHARGES]["annee"].unique()
    return d[d["annee"].isin(detail) & d["valeur_MDT"].notna()]


def fig_par_produit(mesure: str = "md"):
    figtools.apply_lang_font()
    d = _par_produit()
    col = "valeur_MDT" if mesure == "md" else "part_total_charges_pct"
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    annees = sorted(d["annee"].astype(int).unique())
    presents = []
    for a in annees:
        da = d[d["annee"] == a]
        bas = 0.0
        for rub, couleur, hachure in PRODUITS:
            r = da[da["rubrique"] == rub]
            if r.empty:
                continue
            r = next(r.itertuples(index=False))
            v = float(getattr(r, col))
            barre = ax.bar([a], [v], bottom=bas, width=0.78, color=couleur, hatch=hachure,
                           edgecolor="white", linewidth=0.6, zorder=2)
            figtools.infobulle(barre[0], f"{a} · {rub} : {_nombre(r.valeur_MDT)}{_unite('md')}"
                                         f" ({_nombre(r.part_total_charges_pct)} %) — {r.document}")
            bas += v
            if rub not in presents:
                presents.append(rub)
        if mesure == "md":
            t = da[da["rubrique"] == RUB_CHARGES]
            if not t.empty:
                tv = float(t.iloc[0]["valeur_MDT"])
                p, = ax.plot([a], [tv], "_", ms=11, mew=2, color=NOIR, zorder=4)
                figtools.infobulle(p, f"{a} · {RUB_CHARGES} : {_nombre(tv)}{_unite('md')}")
    x0, x1 = annees[0], annees[-1]
    _cadre(ax, "md" if mesure == "md" else "pct_charges", x0, x1)
    ax.set_xticks(range(x0, x1 + 1))
    ax.tick_params(axis="x", labelsize=7, rotation=90)
    if mesure == "md":
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0)))
        ax.set_ylim(top=ax.get_ylim()[1] * 1.08)
    else:
        ax.set_ylim(0, 108)
    # Ruptures de champ : un trait par année, le texte en infobulle sur le triangle.
    rup = _ruptures_des_donnees(_compte()[_compte()["famille"] == "cgc_charges_bct"])
    for a in sorted(rup):
        if "champ" in rup[a] and x0 < a <= x1:
            figtools.marque_rupture(ax, a)
            _repere(ax, a, f"{a} · " + " ; ".join(rup[a]["champ"]))
    poignees = [Patch(facecolor=c, hatch=h, edgecolor="white", label=figtools.fig_text(r))
                for r, c, h in PRODUITS if r in presents]
    if mesure == "md":
        poignees.append(_poignee("lg_total_charges", color=NOIR, marker="_", ms=11, mew=2,
                                 ls="none"))
    poignees.append(_poignee("lg_rupture_champ", color=GRIS, ls=(0, (2, 2)), lw=1, marker=7,
                             ms=5))
    _legende(ax, poignees, ncol=3, y=-0.15)
    fig.tight_layout()
    return fig


def _figure_par_produit():
    d = _par_produit().sort_values(["annee", "rubrique"])
    vues = [(_lab("vue_md"), fig_par_produit("md")),
            (_lab("vue_charges"), fig_par_produit("struct"))]
    return (vues, _table(d, COLS_COMPTE), {SERIE_COMPTE: list(d["source"])},
            "fig_compensation_par_produit")


# --- 8. Prévu et réalisé par poste -------------------------------------------------------

HORIZONS_POSTES = (("loi de finances", "vue_h_lf"),
                   ("loi de finances complémentaire", "vue_h_lfc"),
                   ("prévision", "vue_h_prev"))


def _prevu_postes():
    d = _prevu()
    return d[(d["famille"] == "budget") & d["poste"].isin([p for p, _, _ in POSTES])
             & d["horizon"].isin([h for h, _ in HORIZONS_POSTES]) & d["prevu_MDT"].notna()]


def fig_prevu_realise_postes(horizon: str):
    """Trois panneaux, un par poste, chacun à son échelle. Haut : réalisé en barres, prévu en
    marques. Bas : l'écart du réalisé au prévu EN DINARS ; le pourcentage est en infobulle."""
    figtools.apply_lang_font()
    d = _prevu_postes()
    d = d[d["horizon"] == horizon].sort_values("annee")
    st = STYLE_HORIZON[horizon]
    mfc = "white" if st["creux"] else st["color"]
    annees = sorted(d["annee"].astype(int).unique())
    rang = {a: i for i, a in enumerate(annees)}  # années en rangs : pas de vide entre elles
    fig, axes = plt.subplots(2, 3, figsize=(11, 5.8), sharex=True,
                             gridspec_kw=dict(height_ratios=[1.6, 1], hspace=0.1, wspace=0.3))
    for j, (poste, couleur, hachure) in enumerate(POSTES):
        ax, bx = axes[0][j], axes[1][j]
        g = d[d["poste"] == poste]
        for r in g.itertuples(index=False):
            a = int(r.annee)
            x = rang[a]
            if not _vide(r.realise_MDT):
                nq = str(r.etat_realise) == "non qualifié"
                barre = ax.bar([x], [r.realise_MDT], width=0.7, color=couleur, zorder=2,
                               alpha=0.45 if nq else 0.9, hatch=hachure, edgecolor="white")
                figtools.infobulle(barre[0], f"{a} · {_lab('p_' + poste)}, "
                                             f"{_lab('realise_nq' if nq else 'realise')} : "
                                             f"{_nombre(r.realise_MDT)}{_unite('md')}")
            bulle = (f"{a} · {_lab('p_' + poste)}, {_lab('h_' + horizon)} : "
                     f"{_nombre(r.prevu_MDT)}{_unite('md')} — {r.etat_prevu}")
            p, = ax.plot([x], [r.prevu_MDT], st["marker"], ms=6.5, color=NOIR, mfc=mfc if
                         st["creux"] else NOIR, zorder=4)
            figtools.infobulle(p, bulle)
            if _vide(r.ecart_MDT):
                continue
            e = float(r.ecart_MDT)
            barre = bx.bar([x], [e], width=0.6, color=couleur, zorder=2, hatch=hachure,
                           edgecolor="white")
            figtools.infobulle(barre[0], bulle + f" — {_lab('c_ecart_MDT')} : {_nombre(e)} ; "
                               f"{_lab('c_ecart_pct')} : {_nombre(float(r.ecart_pct))} %")
            if abs(e) >= 0.5:
                bx.annotate(("+" if e > 0 else "") + _nombre(e, 0).replace("-", "−"), xy=(x, e),
                            xytext=(0, 3 if e >= 0 else -3), textcoords="offset points",
                            ha="center", va="bottom" if e >= 0 else "top", fontsize=5.8,
                            color=NOIR)
        ax.set_title(figtools.fig_text(_lab("p_" + poste)), fontsize=9)
        for z in (ax, bx):
            z.grid(True, alpha=0.3)
            z.set_axisbelow(True)
            z.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0)))
            z.tick_params(axis="y", labelsize=7.5)
        ax.set_ylim(bottom=0)
        if g["ecart_MDT"].abs().max() < 10:  # petits écarts : une décimale sur l'axe
            bx.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 1)))
        bx.axhline(0, color=NOIR, lw=0.8, zorder=1)
        bx.margins(y=0.3)
        bx.set_xlim(-0.7, len(annees) - 0.3)
        bx.set_xticks(range(len(annees)))
        bx.set_xticklabels([str(a) for a in annees])
        bx.tick_params(axis="x", labelsize=7, rotation=90)
    axes[0][0].set_ylabel(_ft("md"), fontsize=8.5)
    axes[1][0].set_ylabel(_ft("ecart_md"), fontsize=8.5)
    poignees = [Patch(facecolor=GRIS, alpha=0.9, label=figtools.fig_text(_lab("realise"))),
                Patch(facecolor=GRIS, alpha=0.45, label=figtools.fig_text(_lab("realise_nq"))),
                _poignee("h_" + horizon, color=NOIR, marker=st["marker"], ls="none", ms=6.5,
                         mfc="white" if st["creux"] else NOIR)]
    fig.legend(handles=poignees, loc="lower center", ncol=3, fontsize=7.5, frameon=False)
    fig.subplots_adjust(left=0.07, right=0.99, top=0.94, bottom=0.17)
    return fig


def _figure_prevu_realise_postes():
    d = _prevu_postes().sort_values(["horizon", "poste", "annee"])
    vues = [(_lab(cle), fig_prevu_realise_postes(h)) for h, cle in HORIZONS_POSTES]
    cles = list(d["source_prevu"]) + list(d["source_realise"])
    return (vues, _table(d, COLS_PREVU), {SERIE_PREVU: cles},
            "fig_compensation_prevu_realise_postes")


# --- 9. Carburants : subvention directe et subvention totale -----------------------------

COLS_CARBURANTS = ["annee", "famille", "nature", "rubrique", "valeur", "unite", "etat_norme",
                   "etat", "part_pib_pct", "source", "document", "page_imprimee", "page_pdf",
                   "note", "pib_MDT", "source_pib", "base_pib", "segment_pib", "pib_retropole"]
VENTILATIONS = (
    ("v_rapport", (("subvention directe (inscrite au budget)", ORANGE, ""),
                   ("subvention indirecte (hors budget)", ORANGE, "////"))),
    ("v_dgre", (("subvention directe consommée — ventilation de la DGRE", BRUN, ""),
                ("subvention indirecte — ventilation de la DGRE", BRUN, "////"))),
)
RUB_BESOINS = "besoins de financement du système STEG-STIR-ETAP"


def _audit():
    return _serie(SERIE_AUDIT)


def _ligne_carburants():
    d = _parts()
    return d[(d["famille"] == "budget") & (d["poste"] == "carburants")]


def fig_carburants_directe_totale(mesure: str = "md"):
    figtools.apply_lang_font()
    d = _audit()
    col = "valeur" if mesure == "md" else "part_pib_pct"
    dec = 1 if mesure == "md" else 2
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    annees = [2010, 2011, 2012]
    for a in annees:
        for i, (cle, rubs) in enumerate(VENTILATIONS):
            x = a + (i - 0.5) * 0.36
            bas = 0.0
            for rub, couleur, hachure in rubs:
                r = d[(d["annee"] == a) & (d["rubrique"] == rub)]
                if r.empty:
                    continue
                v = float(r.iloc[0][col])
                barre = ax.bar([x], [v], bottom=bas, width=0.32, color=couleur,
                               alpha=0.9 if not hachure else 0.45, hatch=hachure,
                               edgecolor="white", zorder=2)
                figtools.infobulle(barre[0], f"{a} · {rub} : {_nombre(v, dec)}{_unite(mesure)}")
                bas += v
            ax.annotate(_nombre(bas, dec if mesure != "md" else 0), xy=(x, bas), xytext=(0, 2),
                        textcoords="offset points", ha="center", va="bottom", fontsize=6.5)
    # la ligne budgétaire (série des parts) et les besoins de financement réalisés
    lb = _ligne_carburants()
    lb = lb[lb["annee"].isin(annees)]
    cb = "valeur_MDT" if mesure == "md" else "part_pib_pct"
    for r in lb.itertuples(index=False):
        p, = ax.plot([int(r.annee) - 0.43], [getattr(r, cb)], "o", ms=7, color=NOIR, zorder=4)
        figtools.infobulle(p, f"{int(r.annee)} · {_lab('lg_ligne_carb')} : "
                              f"{_nombre(getattr(r, cb), dec)}{_unite(mesure)}")
    bf = d[(d["rubrique"] == RUB_BESOINS) & (d["etat_norme"] == "réalisé")]
    for r in bf.itertuples(index=False):
        p, = ax.plot([int(r.annee) + 0.43], [getattr(r, col)], "D", ms=6.5, color=VIOLET, zorder=4)
        figtools.infobulle(p, f"{int(r.annee)} · {RUB_BESOINS} : {_nombre(getattr(r, col), dec)}"
                              f"{_unite(mesure)}")
    _cadre(ax, "md" if mesure == "md" else "pct_pib", 2010, 2012)
    ax.set_xlim(2009.4, 2012.6)
    ax.set_xticks(annees)
    ax.set_ylim(top=ax.get_ylim()[1] * 1.06)
    if mesure == "md":
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0)))
    poignees = [Patch(facecolor=ORANGE, alpha=0.9, label=figtools.fig_text(_lab("v_rapport_d"))),
                Patch(facecolor=ORANGE, alpha=0.45, hatch="////", edgecolor="white",
                      label=figtools.fig_text(_lab("v_rapport_i"))),
                Patch(facecolor=BRUN, alpha=0.9, label=figtools.fig_text(_lab("v_dgre_d"))),
                Patch(facecolor=BRUN, alpha=0.45, hatch="////", edgecolor="white",
                      label=figtools.fig_text(_lab("v_dgre_i"))),
                _poignee("lg_ligne_carb", color=NOIR, marker="o", ls="none", ms=7),
                _poignee("lg_besoins", color=VIOLET, marker="D", ls="none", ms=6.5)]
    _legende(ax, poignees, ncol=2, y=-0.12)
    fig.tight_layout()
    return fig


def _figure_carburants_directe_totale():
    d = _audit().sort_values(["rubrique", "annee"])
    vues = [(_lab("vue_md"), fig_carburants_directe_totale("md")),
            (_lab("vue_pib"), fig_carburants_directe_totale("pib"))]
    lb = _ligne_carburants()
    lb = lb[lb["annee"].isin([2010, 2011, 2012])]
    cles = {SERIE_AUDIT: list(d["source"]) + ["ins-cnat-2015"], SERIE_PARTS: list(lb["source"])}
    return vues, _table_simple(d, COLS_CARBURANTS), cles, "fig_compensation_carburants_directe_totale"


# --- 10. Carburants : la ligne budgétaire par entreprise ---------------------------------

ENTREPRISES = (("ETAP", VIOLET, ""), ("STEG", BRUN, "////"), ("STIR", GRIS, "...."))
COLS_BENEF = ["annee", "famille", "nature", "rubrique", "valeur", "unite",
              "ligne_carburants_MDT", "part_de_la_ligne_pct", "etat_norme", "etat", "source",
              "document", "page_imprimee", "page_pdf", "note"]


def fig_carburants_beneficiaires(mesure: str = "md"):
    figtools.apply_lang_font()
    d = _serie(SERIE_BENEF)
    col = "valeur" if mesure == "md" else "part_de_la_ligne_pct"
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    annees = sorted(d["annee"].astype(int).unique())
    for a in annees:
        bas = 0.0
        for ent, couleur, hachure in ENTREPRISES:
            r = d[(d["annee"] == a) & (d["rubrique"] == ent)]
            if r.empty or float(r.iloc[0][col]) == 0:
                continue
            r = r.iloc[0]
            v = float(r[col])
            barre = ax.bar([a], [v], bottom=bas, width=0.7, color=couleur, hatch=hachure,
                           edgecolor="white", zorder=2)
            figtools.infobulle(barre[0], f"{a} · {ent} : {_nombre(r['valeur'])}{_unite('md')} "
                                         f"({_nombre(r['part_de_la_ligne_pct'])} %) — {r['document']}")
            if mesure != "md" and v >= 6:
                ax.annotate(_nombre(v, 0), xy=(a, bas + v / 2), ha="center", va="center",
                            fontsize=7, bbox=dict(facecolor="white", edgecolor="none",
                                                  alpha=0.75, pad=0.6))
            bas += v
        if mesure == "md":
            ax.annotate(_nombre(bas, 0), xy=(a, bas), xytext=(0, 2), textcoords="offset points",
                        ha="center", va="bottom", fontsize=7)
    _cadre(ax, "md" if mesure == "md" else "pct_ligne", annees[0], annees[-1])
    ax.set_xticks(range(annees[0], annees[-1] + 1))
    if mesure == "md":
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0)))
        ax.set_ylim(top=ax.get_ylim()[1] * 1.15)
    else:
        ax.set_ylim(0, 118)
        ax.set_yticks(range(0, 101, 20))
    lb = _ligne_carburants()
    _marque_ruptures(ax, lb[lb["annee"].isin(annees)], annees[0], annees[-1])
    poignees = [Patch(facecolor=c, hatch=h, edgecolor="white", label=figtools.fig_text(e))
                for e, c, h in ENTREPRISES]
    poignees.append(_poignee("lg_rupture", color=GRIS, ls=(0, (2, 2)), lw=1, marker=7, ms=5))
    _legende(ax, poignees, ncol=4, y=-0.13)
    fig.tight_layout()
    return fig


def _figure_carburants_beneficiaires():
    d = _serie(SERIE_BENEF).sort_values(["annee", "rubrique"])
    vues = [(_lab("vue_md"), fig_carburants_beneficiaires("md")),
            (_lab("vue_ligne"), fig_carburants_beneficiaires("struct"))]
    return (vues, _table_simple(d, COLS_BENEF), {SERIE_BENEF: list(d["source"])},
            "fig_compensation_carburants_beneficiaires")


# --- 11. Les prix à la pompe -------------------------------------------------------------

FIN_PRIX = 2026.58  # fin juillet 2026 : dernier constat des prix inchangés (série des événements)
COLS_PRIX = ["date_effet", "annee", "produit", "prix_millimes", "unite", "famille",
             "nature_du_prix", "source", "reference", "date_du_texte", "mecanisme", "rupture",
             "note"]
# (préfixe de la famille dans la série, clé de libellé, style, tracé)
FAMILLES_PRIX = (
    ("arrêté de prix", "fp_arretes", dict(color=NOIR, lw=1.8, marker="o", ms=3), "escalier"),
    ("ministère chargé de l'énergie, données ouvertes", "fp_minist",
     dict(color=BLEU, lw=1.2, ls="--", marker="s", ms=3.5), "annuel"),
    ("INS, moyenne annuelle", "fp_ins", dict(color=VERT, lw=0, ls="", marker="^", ms=4.5),
     "annuel"),
    ("ajustement daté : date officielle", "fp_ajust_off",
     dict(color=BRUN, lw=0, ls="", marker="D", ms=4.5), "points"),
    ("ajustement daté : presse", "fp_ajust_presse",
     dict(color=BRUN, lw=0, ls="", marker="D", ms=4.5, mfc="white"), "points"),
    ("ministère chargé de l'énergie (Observatoire", "fp_one",
     dict(color=VIOLET, lw=1.8, marker="o", ms=3), "escalier"),
    ("Banque mondiale", "fp_bm", dict(color=ROUGE, lw=0, ls="", marker="P", ms=7), "points"),
)
# Produits tracés par carburant : (produit de la série, trait plein ou tireté)
PRODUITS_PRIX = {
    "essence": ("essence super", "essence sans plomb", "essence normale",
                "essence (ligne « Essence normale » de l'annuaire)",
                "essence (ligne « Essence super » de l'annuaire)", "essence"),
    "gasoil": ("gas-oil", "gasoil ordinaire", "gasoil (libellé de l'INS)", "gasoil sans soufre",
               "gasoil 50", "gasoil à 0,2 % de soufre"),
}
SECONDAIRES = ("essence normale", "gasoil sans soufre", "gasoil 50")
# La bouteille de gaz : une autre unité, une vue à part. Les moyennes de l'INS (« par bouteille »)
# et les prix de la bouteille de 13 kg sont des familles distinctes, jamais reliées.
PRODUITS_PRIX["bouteille"] = ("GPL, bouteille de 13 kg", "GPL, bouteille de gaz")
UNITES_PRIX = {"essence": ("millimes par litre",), "gasoil": ("millimes par litre",),
               "bouteille": ("millimes par bouteille de 13 kg", "millimes par bouteille")}
FIN_PRIX_DATE = "2026-07-31"  # même borne que FIN_PRIX, en date
BASE = dinars_constants.ANNEE_BASE

_L.update({
    "vue_essence_courants": {"fr": "Essence, millimes courants", "ar": "البنزين، بالمليم الجاري"},
    "vue_essence_c": {"fr": f"Essence, millimes de {BASE}", "ar": f"البنزين، بمليمات سنة {BASE}"},
    "vue_gasoil_courants": {"fr": "Gasoil, millimes courants", "ar": "الغازوال، بالمليم الجاري"},
    "vue_gasoil_c": {"fr": f"Gasoil, millimes de {BASE}", "ar": f"الغازوال، بمليمات سنة {BASE}"},
    "vue_bouteille": {"fr": "Bouteille de gaz, dinars courants",
                      "ar": "قارورة الغاز، بالدينار الجاري"},
    "vue_bouteille_c": {"fr": f"Bouteille de gaz, dinars de {BASE}",
                        "ar": f"قارورة الغاز، بدينارات سنة {BASE}"},
    "millimes_2025": {"fr": f"Millimes de {BASE} par litre\n(valeurs calculées)",
                      "ar": f"مليمات سنة {BASE} للتر\n(قيم محسوبة)"},
    "dinars_bouteille": {"fr": "Dinars par bouteille de 13 kg,\nprix courants",
                         "ar": "دينار للقارورة (13 كغ)،\nأسعار جارية"},
    "dinars_bouteille_2025": {"fr": f"Dinars de {BASE} par bouteille de 13 kg\n(valeurs calculées)",
                              "ar": f"دينارات سنة {BASE} للقارورة (13 كغ)\n(قيم محسوبة)"},
    "dinars_bouteille_u": {"fr": "dinars par bouteille", "ar": "دينار للقارورة"},
    "millimes_2025_u": {"fr": f"millimes de {BASE} par litre", "ar": f"مليمات سنة {BASE} للتر"},
    "dinars_bouteille_2025_u": {"fr": f"dinars de {BASE} par bouteille",
                                "ar": f"دينارات سنة {BASE} للقارورة"},
    "calcul": {"fr": "calcul", "ar": "حساب"},
    "fp_arretes_c": {"fr": "Arrêtés de prix publiés au Journal officiel : moyenne annuelle des "
                           "prix en vigueur",
                     "ar": "قرارات الأسعار المنشورة بالرائد الرسمي: المعدّل السنوي للأسعار "
                           "المعمول بها"},
    "fp_arretes_c_essence": {
        "fr": "Arrêtés de prix publiés au Journal officiel : essence super, moyenne annuelle "
              "des prix en vigueur (en clair, l'essence normale)",
        "ar": "قرارات الأسعار المنشورة بالرائد الرسمي: البنزين الممتاز، المعدّل السنوي للأسعار "
              "المعمول بها (باللون الفاتح: البنزين العادي)"},
    "fp_one_c": {"fr": "Observatoire national de l'énergie : moyenne annuelle des prix en "
                       "vigueur, depuis 2018",
                 "ar": "المرصد الوطني للطاقة: المعدّل السنوي للأسعار المعمول بها، منذ 2018"},
    "fp_one_c_gasoil": {
        "fr": "Observatoire national de l'énergie : gasoil ordinaire, moyenne annuelle des prix "
              "en vigueur, depuis 2018 (en clair, le gasoil sans soufre)",
        "ar": "المرصد الوطني للطاقة: الغازوال العادي، المعدّل السنوي للأسعار المعمول بها، منذ "
              "2018 (باللون الفاتح: الغازوال الخالي من الكبريت)"},
    "c_moyenne_vigueur": {"fr": "Moyenne annuelle des prix en vigueur (millimes courants, calcul)",
                          "ar": "المعدّل السنوي للأسعار المعمول بها (بالمليم الجاري، حساب)"},
    "c_indice_prix": {"fr": "Indice des prix à la consommation (base 100 en 1970)",
                      "ar": "مؤشّر أسعار الاستهلاك (أساس 100 سنة 1970)"},
    "c_prix_2025": {"fr": f"Prix en millimes de {BASE} (calcul)",
                    "ar": f"السعر بمليمات سنة {BASE} (حساب)"},
    "nature_moyenne": {"fr": "moyenne annuelle des prix en vigueur au premier jour de chaque mois "
                             "(calcul)",
                       "ar": "المعدّل السنوي للأسعار المعمول بها في اليوم الأوّل من كلّ شهر "
                             "(حساب)"},
})

_IPC: dict | None = None


def _ipc() -> dict[int, float]:
    """L'indice des prix des dinars constants du précis (`dinars_constants.ipc`), lu une fois."""
    global _IPC
    if _IPC is None:
        _IPC = dinars_constants.ipc()
    return _IPC


def _coef(annee) -> float | None:
    """Ce qui ramène un montant de l'année `annee` en monnaie de l'année de base : indice de
    l'année de base ÷ indice de l'année. None hors de l'indice (avant 1962, après la base)."""
    i, a = _ipc(), int(annee)
    return i[BASE] / i[a] if a in i and a <= BASE else None


def _cles_ipc() -> dict[str, list[str]]:
    return {sid: list(figtools.meta(sid).get("sources", [])) for sid in dinars_constants.SERIES_IPC}


def _moyennes_escalier(dates, valeurs, fin: str) -> dict[int, float]:
    """{année: moyenne des valeurs en vigueur au premier jour de chacun des douze mois}
    (`figtools.moyenne_annuelle_escalier`), pour les seules années entièrement couvertes : du
    premier jour d'effet à `fin` (date ISO, exclue). Une année où la grandeur manque un mois —
    supprimée, pas encore créée — n'a pas de moyenne."""
    lignes = sorted((str(d)[:10], v) for d, v in zip(dates, valeurs))
    debut = lignes[0][0]
    sortie = {}
    for a in range(int(debut[:4]), int(fin[:4]) + 1):
        if f"{a}-01-01" < debut or f"{a}-12-01" >= fin:
            continue
        m = figtools.moyenne_annuelle_escalier(lignes, a)
        if m is not None:
            sortie[a] = m
    return sortie


def _annee_decimale(date) -> float:
    import datetime as dt
    j = dt.date.fromisoformat(str(date)[:10]) if len(str(date)) >= 10 else \
        dt.date.fromisoformat(str(date)[:7] + "-01")
    return j.year + (j.timetuple().tm_yday - 1) / 365.25


def _prix(carburant: str | None = None):
    d = _serie(SERIE_PRIX)
    garder = [carburant] if carburant else list(PRODUITS_PRIX)
    masque = d["produit"].isin([])
    for c in garder:
        masque |= d["produit"].isin(PRODUITS_PRIX[c]) & d["unite"].isin(UNITES_PRIX[c])
    return d[masque]


def _trace_famille_prix(famille: str):
    """(clé de libellé, style, tracé) de la famille de sources, ou None si elle n'est pas tracée."""
    for prefixe, cle, st, trace in FAMILLES_PRIX:
        if str(famille).startswith(prefixe):
            return cle, st, trace
    return None


# Années sans moyenne en monnaie constante, faute de prix établi pour toute l'année : l'arrêté
# du 31 décembre 1980, abrogé par celui du 23 juin 1981, n'est pas identifié (recherche
# r-arrete-prix-petroliers-1980-12-31) ; les prix du premier semestre de 1981 ne sont pas établis.
ANNEES_SANS_MOYENNE = {"fp_arretes": {1981}}


def _segments_constants(g, cle, trace):
    """Les points d'une famille et d'un produit en monnaie de l'année de base, par segment
    (un segment par nature de prix pour un escalier) : [(x, valeur de base, valeur courante,
    coefficient, quand, nature)]."""
    segments = []
    if trace == "escalier":
        g = g[g["date_effet"].notna()]
        for nature, h in g.groupby("nature_du_prix", sort=False):
            dates = [str(x)[:10] for x in h["date_effet"]]
            fin = FIN_PRIX_DATE if cle == "fp_one" else max(dates)
            seg = []
            for a, m in _moyennes_escalier(dates, list(h["prix_millimes"]), fin).items():
                c = _coef(a)
                if c is not None and a not in ANNEES_SANS_MOYENNE.get(cle, ()):
                    seg.append((a + 0.5, m * c, m, c, a, f"{nature} — {_lab('nature_moyenne')}"))
            segments.append(seg)
        return segments
    seg = []
    for r in g.sort_values("annee").itertuples(index=False):
        c = _coef(r.annee)
        if c is None:
            continue
        if trace == "annuel" or _vide(r.date_effet):
            x, quand = int(r.annee) + 0.5, int(r.annee)
        else:
            x, quand = _annee_decimale(r.date_effet), r.date_effet
        seg.append((x, r.prix_millimes * c, r.prix_millimes, c, quand, r.nature_du_prix))
    segments.append(seg)
    return segments


def fig_prix_pompe(carburant: str = "essence", constants: bool = False):
    """Une vue par carburant : en millimes courants (dinars pour la bouteille), ou en monnaie de
    l'année de base. En monnaie constante, un prix daté devient la moyenne annuelle des prix en
    vigueur ; une moyenne annuelle et un ajustement daté sont ramenés par l'indice de leur année."""
    figtools.apply_lang_font()
    d = _prix(carburant)
    bouteille = carburant == "bouteille"
    echelle = 1 / 1000 if bouteille else 1
    dec = 2 if bouteille else 0
    unite = (("dinars_bouteille_2025_u" if bouteille else "millimes_2025_u") if constants
             else ("dinars_bouteille_u" if bouteille else "millimes"))
    fig, ax = plt.subplots(figsize=(9.5, 5.8))
    poignees = []
    ymax = 0.0
    for prefixe, cle, st, trace in FAMILLES_PRIX:
        f = d[d["famille"].str.startswith(prefixe)]
        if f.empty:
            continue
        for produit in PRODUITS_PRIX[carburant]:
            g = f[f["produit"] == produit]
            if g.empty:
                continue
            style = dict(st)
            if produit in SECONDAIRES:  # produit voisin : même famille, trait fin et clair
                style.update(alpha=0.45, lw=min(st.get("lw", 0), 1.0))
            marque = dict(marker=style.pop("marker"), ms=style.pop("ms"),
                          mfc=style.pop("mfc", None))
            if constants:
                for seg in _segments_constants(g, cle, trace):
                    if not seg:
                        continue
                    if trace in ("annuel", "escalier") and style.get("lw"):
                        v = {int(x): y * echelle for x, y, *_ in seg}
                        for suite in _suites(v):
                            ax.plot([a + 0.5 for a in suite], [v[a] for a in suite], zorder=2,
                                    **style)
                    for x, y, courant, c, quand, nature in seg:
                        ymax = max(ymax, y * echelle)
                        p, = ax.plot([x], [y * echelle], marque["marker"], ms=marque["ms"],
                                     color=style["color"], mfc=marque["mfc"] or style["color"],
                                     alpha=style.get("alpha", 1), zorder=3)
                        figtools.infobulle(
                            p, f"{quand} · {produit} : {_nombre(y * echelle, dec)} {_lab(unite)} "
                               f"— {_lab('calcul')} : {_nombre(courant * echelle, dec)} × "
                               f"{_nombre(c, 3)} — {_lab(cle)} — {nature}")
            else:
                if trace == "annuel":
                    g = g.sort_values("annee")
                    v = dict(zip(g["annee"].astype(int), g["prix_millimes"] * echelle))
                    if style.get("lw"):
                        for suite in _suites(v):
                            ax.plot([a + 0.5 for a in suite], [v[a] for a in suite], zorder=2,
                                    **style)
                    pts = [(int(r.annee) + 0.5, r) for r in g.itertuples(index=False)]
                else:
                    g = g[g["date_effet"].notna()].sort_values("date_effet")
                    pts = [(_annee_decimale(r.date_effet), r) for r in g.itertuples(index=False)]
                    if trace == "escalier":
                        # Un escalier par nature de prix : la zone A de 1964-1966 et le prix
                        # uniforme de 1968 ne sont pas reliés. Le dernier palier court jusqu'au
                        # prix suivant de la famille ; celui de l'Observatoire, jusqu'au dernier
                        # constat des prix inchangés.
                        for _, h in g.groupby("nature_du_prix", sort=False):
                            xs = [_annee_decimale(x) for x in h["date_effet"]]
                            ys = list(h["prix_millimes"] * echelle)
                            fin = FIN_PRIX if cle == "fp_one" else xs[-1]
                            ax.step(xs + [fin], ys + [ys[-1]], where="post", zorder=2,
                                    **{k: v for k, v in style.items() if k != "ls"})
                for x, r in pts:
                    y = r.prix_millimes * echelle
                    ymax = max(ymax, y)
                    p, = ax.plot([x], [y], marque["marker"], ms=marque["ms"],
                                 color=style["color"], mfc=marque["mfc"] or style["color"],
                                 alpha=style.get("alpha", 1), zorder=3)
                    quand = r.date_effet if not _vide(r.date_effet) else int(r.annee)
                    figtools.infobulle(p, f"{quand} · {r.produit} : {_nombre(y, dec)} "
                                          f"{_lab(unite)} — {_lab(cle)} — {r.nature_du_prix}")
        base_lg = f"{cle}_c" if constants and trace == "escalier" else cle
        cle_lg = f"{base_lg}_{carburant}" if f"{base_lg}_{carburant}" in _L else base_lg
        poignees.append(_poignee(cle_lg, color=st["color"], lw=st.get("lw", 0) or 0,
                                 ls=st.get("ls", "-") or "none", marker=st["marker"],
                                 ms=st["ms"] + 1, mfc=st.get("mfc", st["color"])))
    if constants or bouteille:
        ax.set_ylim(0, ymax * 1.3)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0)))
        ax.set_ylabel(_ft(("dinars_bouteille_2025" if constants else "dinars_bouteille")
                          if bouteille else "millimes_2025"))
    else:
        ax.set_yscale("log")
        ax.set_yticks([50, 100, 200, 500, 1000, 2000, 3000])
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0)))
        ax.set_ylabel(_ft("millimes_log"))
        ax.set_ylim(top=ax.get_ylim()[1] * 1.6)
    ax.set_xlabel(figtools.fig_text(_lab("x")))
    ax.set_xlim(1977 if bouteille else 1963, 2027.5)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=14))
    ax.grid(True, alpha=0.3)
    # Ruptures de produit ou de nature du prix (colonne `rupture`) : trait et libellé court.
    vus = set()
    for i, r in enumerate(d[d["rupture"].notna()].sort_values("annee").itertuples(index=False)):
        x = _annee_decimale(r.date_effet) if not _vide(r.date_effet) else float(r.annee)
        if round(x, 1) in vus:
            continue
        vus.add(round(x, 1))
        ax.axvline(x, color=GRIS, ls=(0, (2, 2)), lw=1, zorder=1)
        p, = ax.plot([x], [1], marker=7, ms=6, color=GRIS, clip_on=False, zorder=4,
                     transform=ax.get_xaxis_transform())
        figtools.infobulle(p, f"{int(r.annee)} · {r.rupture}")
        cle = f"rp_{int(r.annee)}"
        if cle in _L:
            ax.annotate(_ft(cle), xy=(x, 1), xycoords=("data", "axes fraction"),
                        xytext=(3, -4 - 20 * (len(vus) % 2)), textcoords="offset points",
                        ha="left", va="top", fontsize=6.5, color=GRIS, zorder=5,
                        bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1))
    poignees.append(_poignee("lg_rupture", color=GRIS, ls=(0, (2, 2)), lw=1, marker=7, ms=5))
    if not bouteille:
        # Mécanisme d'ajustement des prix des carburants : un repère par événement, au pied.
        for r in _serie(SERIE_EVENEMENTS).itertuples(index=False):
            x = _annee_decimale(r.date)
            p, = ax.plot([x], [0], marker=6, ms=6, color=ROUGE, clip_on=False, zorder=4,
                         transform=ax.get_xaxis_transform())
            figtools.infobulle(p, f"{r.date} · {r.evenement}")
        poignees.append(_poignee("lg_evenement", color=ROUGE, marker=6, ms=6, ls="none"))
    _legende(ax, poignees, ncol=1, y=-0.12, taille=7.2)
    fig.tight_layout()
    return fig


def _table_prix():
    """Les prix tracés et non tracés, tels que la série les donne, et en regard leur valeur en
    monnaie de l'année de base ; pour un prix daté, une ligne de plus par année : la moyenne
    annuelle des prix en vigueur, qui est la valeur ramenée."""
    import pandas as pd
    d = _prix().sort_values(["produit", "famille", "annee", "date_effet"]).copy()
    d["moyenne_vigueur"] = float("nan")
    d["indice_prix"] = float("nan")
    d["prix_2025"] = float("nan")
    i = _ipc()
    for idx, r in d.iterrows():
        tf = _trace_famille_prix(r["famille"])
        c = _coef(r["annee"])
        if tf is None or tf[2] == "escalier" or c is None:
            continue
        d.at[idx, "indice_prix"] = round(i[int(r["annee"])], 2)
        d.at[idx, "prix_2025"] = round(r["prix_millimes"] * c, 1)
    ajouts = []
    for (famille, produit), g in d.groupby(["famille", "produit"], sort=False):
        tf = _trace_famille_prix(famille)
        if tf is None or tf[2] != "escalier":
            continue
        for seg in _segments_constants(g, tf[0], "escalier"):
            for _x, y, courant, _c, a, nature in seg:
                h = g[g["nature_du_prix"] == nature.split(" — ")[0]]
                ajouts.append(dict(
                    annee=a, produit=produit, unite=g["unite"].iloc[0], famille=famille,
                    nature_du_prix=nature, source=" ; ".join(dict.fromkeys(h["source"].dropna())),
                    moyenne_vigueur=round(courant, 1), indice_prix=round(i[a], 2),
                    prix_2025=round(y, 1)))
    d = pd.concat([d, pd.DataFrame(ajouts)], ignore_index=True)
    return _table_simple(d, COLS_PRIX + ["moyenne_vigueur", "indice_prix", "prix_2025"])


def _figure_prix_pompe():
    d = _prix()
    vues = [(_lab("vue_essence_courants"), fig_prix_pompe("essence")),
            (_lab("vue_essence_c"), fig_prix_pompe("essence", constants=True)),
            (_lab("vue_gasoil_courants"), fig_prix_pompe("gasoil")),
            (_lab("vue_gasoil_c"), fig_prix_pompe("gasoil", constants=True)),
            (_lab("vue_bouteille"), fig_prix_pompe("bouteille")),
            (_lab("vue_bouteille_c"), fig_prix_pompe("bouteille", constants=True))]
    trace = d[~d["famille"].str.contains("INFÉRÉ|relevé mensuel")]
    ev = _serie(SERIE_EVENEMENTS)
    cles = {SERIE_PRIX: list(trace["source"]), SERIE_EVENEMENTS: list(ev["source"]),
            **_cles_ipc()}
    return vues, _table_prix(), cles, "fig_compensation_prix_pompe"


# --- 12-16. Les tableaux du volume devenus figures ---------------------------------------
# Leurs valeurs sont dans `transcriptions.py`, chacune avec sa source. Ces séries ne sont pas
# dans l'entrepôt : leur provenance est déclarée ici.

SERIE_TAXE = "compensation-taxe-unique-1964-1981"
SERIE_RECETTES_CARB = "compensation-recettes-carburants-2012-2018"
SERIE_IMPORT = "compensation-import-cession-2016-2025"
SERIE_LF_CAISSE = "compensation-lf-caisse-1987-1994"
SERIE_LF_CAISSE_2005 = "compensation-lf-caisse-2005-2010"

figtools.register_provenance(
    SERIE_TAXE,
    titre=("La taxe au profit de la Caisse sur les produits pétroliers (1964), puis la taxe "
           "unique de compensation (1971), à chaque date d'effet, 1964-1981"),
    sources=tr.cles(tr.TAXE_UNIQUE, 4), unite="dinars par hectolitre",
    perimetre=("tarifs par hectolitre de l'essence, du pétrole lampant et du gas-oil (celui des "
               "travaux agricoles et de la pêche à part depuis 1977), à chaque texte qui les fixe "
               "ou les modifie, du 28 septembre 1964 au 22 février 1984"),
    caveats=("Avant 1971, la taxe de 1964 s'ajoute à la redevance de 1957 ; la taxe unique de 1971 "
             "les réunit : les deux grandeurs ne se raccordent pas. De 1966 à 1970, deux tarifs "
             "d'essence, un par qualité. Les taxes sur le fuel-oil léger (6,990 D par tonne au "
             "1er janvier 1977, 26,990 D au 5 janvier 1982), sur le fuel-oil lourd (4 D par tonne, "
             "décret de 1980), en dinars par tonne, et sur le fuel-oil domestique (1982) ne sont pas "
             "tracées. Les tarifs de l'essence et du gas-oil ordinaire postérieurs à 1981 ne sont "
             "pas établis ; le tarif du gas-oil agricole du 22 février 1984 est dans les données, "
             "non tracé."))
figtools.register_provenance(
    SERIE_RECETTES_CARB,
    titre=("Les recettes non fiscales en regard de la subvention des carburants : revenus de "
           "commercialisation des carburants, prévus et encaissés, et redevance sur le gazoduc, "
           "2012-2018"),
    sources=tr.cles(tr.RECETTES_CARBURANTS, 4), unite="millions de dinars courants",
    perimetre=("revenus de commercialisation des carburants (prévisions des lois de finances et "
               "des lois de finances complémentaires, encaissements) et redevance sur le gazoduc "
               "encaissée, d'après les bulletins d'exécution du budget"),
    caveats="La ligne des revenus de commercialisation n'existe pas avant 2015.")
figtools.register_provenance(
    SERIE_IMPORT,
    titre=("Le prix moyen d'importation de l'année et le prix de cession en vigueur en fin "
           "d'année : essence, gasoil ordinaire, bouteille de gaz de 13 kg, 2016-2025"),
    sources=[tr.IMPORT_CESSION_CLE], unite="millimes par litre ; dinars par bouteille",
    perimetre=("numéros de décembre de la Conjoncture énergétique de l'Observatoire national de "
               "l'énergie et des mines ; pour 2024, données à fin novembre"),
    caveats=("L'écart, importation moins cession, est un calcul, que l'Observatoire dit lui-même "
             "« indicatif » : le prix de cession est celui de la fin de l'année, le prix "
             "d'importation la moyenne de l'année ; l'écart ignore la production de la raffinerie "
             "et n'est pas la subvention budgétaire."))
figtools.register_provenance(
    SERIE_LF_CAISSE,
    titre=("La Caisse générale de compensation dans le tableau des fonds spéciaux du Trésor des "
           "lois de finances initiales, 1987-1994 : subvention du budget, recettes propres, total"),
    sources=tr.cles(tr.LF_CAISSE, 5), unite="millions de dinars courants",
    perimetre=("tableau des fonds spéciaux du Trésor de chaque loi de finances initiale (« L » de "
               "1987 à 1990, « K » de 1991 à 1994), ligne de la Caisse générale de compensation ; "
               "prévisions"),
    caveats=("Les recettes propres de 1988 comprennent le solde reporté. En 1989, le premier "
             "chiffre des recettes propres est rogné sur la page : elles se déduisent du total "
             "(190,0) et de la subvention (188,0)."))
figtools.register_provenance(
    SERIE_LF_CAISSE_2005,
    titre=("La Caisse générale de compensation dans le tableau B des fonds spéciaux du Trésor "
           "des lois de finances initiales, 2005-2010 : recettes prévues du compte"),
    sources=tr.cles(tr.LF_CAISSE_2005, 2), unite="dinars courants",
    perimetre=("tableau B de chaque loi de finances initiale, ligne « Caisse générale de "
               "compensation » (ministère du commerce) ; prévisions de recettes"))

_L.update({
    # taxe unique
    "t64_essence": {"fr": "Essence : taxe de 1964", "ar": "البنزين: معلوم 1964"},
    "t64_essence_2": {"fr": "Essence normale : taxe de 1964, tarif propre depuis 1966",
                      "ar": "البنزين العادي: معلوم 1964، تعريفة خاصة منذ 1966"},
    "t64_lampant": {"fr": "Pétrole lampant : taxe de 1964", "ar": "بترول الإنارة: معلوم 1964"},
    "t64_gasoil": {"fr": "Gas-oil : taxe de 1964", "ar": "الغازوال: معلوم 1964"},
    "tu_essence": {"fr": "Essence : taxe unique de compensation",
                   "ar": "البنزين: المعلوم الموحّد للتعويض"},
    "tu_lampant": {"fr": "Pétrole lampant : taxe unique de compensation",
                   "ar": "بترول الإنارة: المعلوم الموحّد للتعويض"},
    "tu_gasoil": {"fr": "Gas-oil : taxe unique de compensation",
                  "ar": "الغازوال: المعلوم الموحّد للتعويض"},
    "tu_gasoil_agri": {"fr": "Gas-oil des travaux agricoles et de la pêche : taxe unique",
                       "ar": "الغازوال المعدّ للأشغال الفلاحية والصيد البحري: المعلوم الموحّد"},
    "dhl": {"fr": "Dinars courants par hectolitre", "ar": "دينار جارٍ للهكتولتر"},
    "dhl_2025": {"fr": f"Dinars de {BASE} par hectolitre\n(valeurs calculées)",
                 "ar": f"دينارات سنة {BASE} للهكتولتر\n(قيم محسوبة)"},
    "dhl_u": {"fr": "D/hl", "ar": "د/هل"},
    "dhl_2025_u": {"fr": f"D de {BASE}/hl", "ar": f"د سنة {BASE}/هل"},
    "rp_tu_1971": {"fr": "1971 : taxe unique\nde compensation", "ar": "1971: المعلوم\nالموحّد للتعويض"},
    "bulle_tu_1971": {"fr": "1971 · la taxe unique de compensation réunit la taxe de 1964 au profit "
                            "de la Caisse et la redevance de 1957",
                      "ar": "1971 · المعلوم الموحّد للتعويض يجمع معلوم 1964 لفائدة الصندوق "
                            "وإتاوة 1957"},
    "vue_dhl": {"fr": "Dinars courants", "ar": "بالدينار الجاري"},
    "vue_dhl_c": {"fr": f"Dinars de {BASE}", "ar": f"بدينارات سنة {BASE}"},
    "c_grandeur": {"fr": "Grandeur", "ar": "المقدار"},
    "c_ligne": {"fr": "Ligne", "ar": "السطر"},
    "c_tarif_dhl": {"fr": "Tarif (dinars courants par hectolitre)",
                    "ar": "التعريفة (دينار جارٍ للهكتولتر)"},
    "c_moyenne_dhl": {"fr": "Moyenne annuelle des tarifs en vigueur (dinars courants par "
                            "hectolitre, calcul)",
                      "ar": "المعدّل السنوي للتعريفات المعمول بها (دينار جارٍ للهكتولتر، حساب)"},
    "c_tarif_dhl_2025": {"fr": f"Tarif moyen en dinars de {BASE} par hectolitre (calcul)",
                         "ar": f"معدّل التعريفة بدينارات سنة {BASE} للهكتولتر (حساب)"},
    "c_texte": {"fr": "Texte", "ar": "النصّ"},
    "c_localisation": {"fr": "Localisation", "ar": "الموضع"},
    "c_etat_texte": {"fr": "Ce que fait le texte", "ar": "أثر النصّ"},
    "ligne_tarif": {"fr": "tarif à sa date d'effet", "ar": "التعريفة في تاريخ سريانها"},
    "ligne_moyenne": {"fr": "moyenne annuelle des tarifs en vigueur au premier jour de chaque mois "
                            "(calcul)",
                      "ar": "المعدّل السنوي للتعريفات المعمول بها في اليوم الأوّل من كلّ شهر (حساب)"},
    # recettes en regard de la subvention des carburants
    "rc_revenus_commercialisation": {"fr": "Revenus de commercialisation des carburants, encaissés",
                                     "ar": "مداخيل ترويج المحروقات، المقبوضة"},
    "rc_redevance_gazoduc": {"fr": "Redevance sur le gazoduc, encaissée",
                             "ar": "إتاوة أنبوب الغاز، المقبوضة"},
    "rc_lf": {"fr": "Revenus de commercialisation, prévus en loi de finances",
              "ar": "مداخيل الترويج، المتوقّعة بقانون المالية"},
    "rc_lfc": {"fr": "Revenus de commercialisation, prévus en loi de finances complémentaire",
               "ar": "مداخيل الترويج، المتوقّعة بقانون المالية التكميلي"},
    "rc_subvention": {"fr": "Subvention des carburants : ligne budgétaire « carburants »",
                      "ar": "دعم المحروقات: سطر المحروقات بالميزانية"},
    "rc_rupture": {"fr": "2015 · séparation des opérations de commercialisation des hydrocarbures : "
                         "le périmètre de la ligne « carburants » s'élargit",
                   "ar": "2015 · فصل عمليات ترويج المحروقات: يتّسع نطاق سطر المحروقات"},
    "rp_2015_carb": {"fr": "2015 : périmètre\nélargi", "ar": "2015: نطاق\nموسَّع"},
    "c_horizon_rc": {"fr": "Horizon", "ar": "الأفق"},
    "c_MDT": {"fr": "Montant (millions de dinars courants)", "ar": "المبلغ (ملايين الدنانير الجارية)"},
    "h_encaissé": {"fr": "encaissé", "ar": "مقبوض"},
    # importation et cession
    "ic_essence_import": {"fr": "Essence : prix moyen d'importation de l'année",
                          "ar": "البنزين: معدّل سعر التوريد للسنة"},
    "ic_essence_cession": {"fr": "Essence : prix de cession en fin d'année",
                           "ar": "البنزين: سعر الإحالة في آخر السنة"},
    "ic_gasoil_import": {"fr": "Gasoil ordinaire : prix moyen d'importation de l'année",
                         "ar": "الغازوال العادي: معدّل سعر التوريد للسنة"},
    "ic_gasoil_cession": {"fr": "Gasoil ordinaire : prix de cession en fin d'année",
                          "ar": "الغازوال العادي: سعر الإحالة في آخر السنة"},
    "ic_bouteille_import": {"fr": "Bouteille de gaz : prix moyen d'importation de l'année",
                            "ar": "قارورة الغاز: معدّل سعر التوريد للسنة"},
    "ic_bouteille_cession": {"fr": "Bouteille de gaz : prix de cession en fin d'année",
                             "ar": "قارورة الغاز: سعر الإحالة في آخر السنة"},
    "ic_ecart_essence": {"fr": "Essence : importation − cession", "ar": "البنزين: التوريد − الإحالة"},
    "ic_ecart_gasoil": {"fr": "Gasoil ordinaire : importation − cession",
                        "ar": "الغازوال العادي: التوريد − الإحالة"},
    "ic_ecart": {"fr": "Importation − cession\n(millimes courants par litre)",
                 "ar": "التوريد − الإحالة\n(مليم جارٍ للتر)"},
    "ic_ecart_2025": {"fr": f"Importation − cession\n(millimes de {BASE} par litre)",
                      "ar": f"التوريد − الإحالة\n(مليمات سنة {BASE} للتر)"},
    "millimes_courants": {"fr": "Millimes courants par litre", "ar": "مليم جارٍ للتر"},
    "dinars_bouteille_courants": {"fr": "Dinars courants par bouteille de 13 kg",
                                  "ar": "دينار جارٍ للقارورة (13 كغ)"},
    "vue_ic": {"fr": "Essence et gasoil, millimes courants", "ar": "البنزين والغازوال، بالمليم الجاري"},
    "vue_ic_c": {"fr": f"Essence et gasoil, millimes de {BASE}",
                 "ar": f"البنزين والغازوال، بمليمات سنة {BASE}"},
    "fin_novembre": {"fr": "à fin\nnovembre", "ar": "إلى آخر\nنوفمبر"},
    "c_periode_ic": {"fr": "Période couverte", "ar": "الفترة المشمولة"},
    "c_import": {"fr": "Prix moyen d'importation (courant)", "ar": "معدّل سعر التوريد (جارٍ)"},
    "c_cession": {"fr": "Prix de cession en fin d'année (courant)",
                  "ar": "سعر الإحالة في آخر السنة (جارٍ)"},
    "c_ecart_ic": {"fr": "Écart, importation − cession (courant)", "ar": "الفارق، التوريد − الإحالة (جارٍ)"},
    "c_import_2025": {"fr": f"Prix moyen d'importation (monnaie de {BASE}, calcul)",
                      "ar": f"معدّل سعر التوريد (بعملة سنة {BASE}، حساب)"},
    "c_cession_2025": {"fr": f"Prix de cession (monnaie de {BASE}, calcul)",
                       "ar": f"سعر الإحالة (بعملة سنة {BASE}، حساب)"},
    "c_ecart_2025": {"fr": f"Écart (monnaie de {BASE}, calcul)",
                     "ar": f"الفارق (بعملة سنة {BASE}، حساب)"},
    "u_millimes_litre": {"fr": "millimes par litre", "ar": "مليم للتر"},
    "u_dinars_bouteille": {"fr": "dinars par bouteille de 13 kg", "ar": "دينار للقارورة (13 كغ)"},
    "p_essence": {"fr": "essence", "ar": "البنزين"},
    "p_gasoil_ordinaire": {"fr": "gasoil ordinaire", "ar": "الغازوال العادي"},
    "p_bouteille": {"fr": "bouteille de gaz de 13 kg", "ar": "قارورة الغاز (13 كغ)"},
    "loc_decembre": {"fr": "numéro de décembre {a}", "ar": "عدد ديسمبر {a}"},
    "loc_novembre": {"fr": "données à fin novembre {a}", "ar": "معطيات إلى آخر نوفمبر {a}"},
    "periode_annee": {"fr": "année", "ar": "السنة"},
    "periode_novembre": {"fr": "à fin novembre", "ar": "إلى آخر نوفمبر"},
    # la Caisse dans les lois de finances
    "lf_subvention": {"fr": "Subvention du budget, prévue en loi de finances",
                      "ar": "منحة الميزانية، المتوقّعة بقانون المالية"},
    "lf_recettes_propres": {"fr": "Recettes propres, prévues en loi de finances",
                            "ar": "الموارد الذاتية، المتوقّعة بقانون المالية"},
    "lf_total": {"fr": "total des recettes prévues, égal aux dépenses",
                 "ar": "مجموع الموارد المتوقّعة، يساوي النفقات"},
    "lf_dotation_bct": {"fr": "Dotation du budget relayée par la Banque centrale (rapport annuel)",
                        "ar": "منحة الميزانية كما ينقلها البنك المركزي (التقرير السنوي)"},
    "lf_md": {"fr": "Millions de dinars courants (prévisions)",
              "ar": "ملايين الدنانير الجارية (تقديرات)"},
    "lf_tableau_l": {"fr": "tableau L", "ar": "الجدول L"},
    "lf_tableau_k": {"fr": "tableau K", "ar": "الجدول K"},
    "c_gestion": {"fr": "Gestion", "ar": "التصرّف"},
    "c_subvention_lf": {"fr": "Subvention du budget (MD, prévision)",
                        "ar": "منحة الميزانية (م.د، تقدير)"},
    "c_recettes_propres_lf": {"fr": "Recettes propres (MD, prévision)",
                              "ar": "الموارد الذاتية (م.د، تقدير)"},
    "c_total_lf": {"fr": "Total des recettes, égal aux dépenses (MD, prévision)",
                   "ar": "مجموع الموارد، يساوي النفقات (م.د، تقدير)"},
    "c_dotation_bct": {"fr": "Dotation relayée par la BCT (MD)", "ar": "المنحة حسب البنك المركزي (م.د)"},
    "c_source_dotation": {"fr": "Source de la dotation", "ar": "مصدر المنحة"},
    "c_page_dotation": {"fr": "Page (dotation)", "ar": "الصفحة (المنحة)"},
    "c_tableau": {"fr": "Tableau de la loi", "ar": "جدول القانون"},
    "c_remarque": {"fr": "Remarque", "ar": "ملاحظة"},
    "lf_dinars": {"fr": "Dinars courants (recettes prévues du compte)",
                  "ar": "دنانير جارية (الموارد المتوقّعة للحساب)"},
    "c_recettes_prevues_d": {"fr": "Recettes prévues du compte (dinars courants)",
                             "ar": "الموارد المتوقّعة للحساب (دنانير جارية)"},
    "lf_b_barre": {"fr": "Recettes prévues du compte de la Caisse, tableau B",
                   "ar": "الموارد المتوقّعة لحساب الصندوق، الجدول B"},
})

COURBES_TAXE = {  # clé: (couleur, trait, fin de la grandeur, décalage de l'étiquette)
    "t64_essence": (ORANGE, (0, (5, 2)), "1971-01-01", (4, 4, "left")),
    "t64_essence_2": (ORANGE, (0, (1, 1.5)), "1971-01-01", (4, -6, "left")),
    "t64_lampant": (BRUN, (0, (5, 2)), "1971-01-01", (4, 4, "left")),
    "t64_gasoil": (BLEU, (0, (5, 2)), "1971-01-01", (4, -6, "left")),
    "tu_essence": (ORANGE, "-", f"{tr.TAXE_UNIQUE_FIN + 1}-01-01", (4, 4, "left")),
    "tu_lampant": (BRUN, "-", f"{tr.TAXE_UNIQUE_FIN + 1}-01-01", (-4, 2, "right")),
    "tu_gasoil": (BLEU, "-", f"{tr.TAXE_UNIQUE_FIN + 1}-01-01", (4, 4, "left")),
    "tu_gasoil_agri": (BLEU, (0, (1, 1.5)), f"{tr.TAXE_UNIQUE_FIN + 1}-01-01", (4, -6, "left")),
}


def _taxe_lignes() -> dict[str, list]:
    """{grandeur: [(date, valeur ou None, état, texte, clé, localisation)]}, dates croissantes."""
    sortie = {}
    for cle in COURBES_TAXE:
        lignes = sorted((r for r in tr.TAXE_UNIQUE if r[0] == cle), key=lambda r: r[1])
        etats = figtools.etats_escalier([(r[1], r[2], r[3], "") for r in lignes])
        sortie[cle] = [(date, v, etat, texte, r[4], r[5])
                       for (date, v, etat, texte, _l), r in zip(etats, lignes)]
    return sortie


def _taxe_moyennes() -> dict[str, dict[int, float]]:
    """{grandeur: {année: moyenne annuelle courante}} : les seules années entières où la grandeur
    existe ; aucune après 1981, dont les tarifs ne sont pas établis."""
    sortie = {}
    for cle, lignes in _taxe_lignes().items():
        sortie[cle] = _moyennes_escalier([l[0] for l in lignes], [l[1] for l in lignes],
                                         COURBES_TAXE[cle][2])
    return sortie


def _rupture_taxe(ax):
    x = 1971.0
    ax.axvline(x, color=GRIS, ls=(0, (2, 2)), lw=1, zorder=1)
    p, = ax.plot([x], [1], marker=7, ms=6, color=GRIS, clip_on=False, zorder=4,
                 transform=ax.get_xaxis_transform())
    figtools.infobulle(p, _lab("bulle_tu_1971"))
    ax.annotate(_ft("rp_tu_1971"), xy=(x, 1), xycoords=("data", "axes fraction"),
                xytext=(3, -4), textcoords="offset points", ha="left", va="top", fontsize=7,
                color=GRIS, bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1))


def fig_taxe_unique(constants: bool = False):
    """En dinars courants, chaque tarif en escalier à ses dates d'effet ; en monnaie de l'année
    de base, la moyenne annuelle des tarifs en vigueur, un point par année entière."""
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    poignees = []
    if constants:
        for cle, moyennes in _taxe_moyennes().items():
            couleur, ls, _fin, (_dx, dy, _ha) = COURBES_TAXE[cle]
            pts = {a: m * _coef(a) for a, m in moyennes.items() if _coef(a) is not None}
            for suite in _suites(pts):
                ax.plot([a + 0.5 for a in suite], [pts[a] for a in suite], color=couleur, ls=ls,
                        lw=1.8, zorder=2)
            for a, y in pts.items():
                p, = ax.plot([a + 0.5], [y], "o", ms=3.5, color=couleur, zorder=3)
                figtools.infobulle(p, f"{a} · {_lab(cle)} : {_nombre(y, 2)} {_lab('dhl_2025_u')} "
                                      f"— {_lab('calcul')} : {_nombre(moyennes[a], 3)} × "
                                      f"{_nombre(_coef(a), 3)}")
            for a in sorted({min(pts), max(pts)}) if pts else []:
                ax.annotate(_nombre(pts[a], 1), xy=(a + 0.5, pts[a]),
                            xytext=(0, 5 if dy > 0 else -6), textcoords="offset points",
                            ha="center", va="bottom" if dy > 0 else "top", fontsize=7.5,
                            color=couleur, fontweight="bold")
            poignees.append(_poignee(cle, color=couleur, ls=ls, lw=1.8, marker="o", ms=3.5))
        ax.set_ylabel(_ft("dhl_2025"))
    else:
        for cle, lignes in _taxe_lignes().items():
            couleur, ls, fin, (dx, dy, ha) = COURBES_TAXE[cle]
            bout = figtools.abscisse_date(fin)
            # Un tarif daté de la fin du tracé ou après (le gas-oil agricole en 1984) reste dans
            # les données, sans être tracé.
            lignes = [lg for lg in lignes if lg[0] < fin]
            for i, (date, v, etat, texte, cit, loc) in enumerate(lignes):
                x = figtools.abscisse_date(date)
                if v is None:
                    dernier = lignes[i - 1][1]
                    p, = ax.plot([x], [dernier], "o", color=couleur, mfc="white", ms=6.5,
                                 mew=1.6, zorder=4)
                    figtools.infobulle(p, f"{date} · {_lab(cle)} : {figtools.t('esc_supprime')} "
                                          f"· {texte}")
                    continue
                x_suivant = figtools.abscisse_date(lignes[i + 1][0]) if i + 1 < len(lignes) \
                    else bout
                ax.plot([x, x_suivant], [v, v], color=couleur, ls=ls, lw=2, zorder=2)
                suivant = lignes[i + 1][1] if i + 1 < len(lignes) else None
                if suivant is not None and suivant != v:
                    ax.plot([x_suivant, x_suivant], [v, suivant], color=couleur, lw=1, zorder=2)
                p, = ax.plot([x], [v], "o", color=couleur, ms=4.5, zorder=4)
                figtools.infobulle(p, f"{date} · {_lab(cle)} : {_nombre(v, 3)} {_lab('dhl_u')} "
                                      f"· {texte}")
                ax.annotate(_nombre(v, 3), xy=(x, v), xytext=(dx, dy), textcoords="offset points",
                            ha=ha, va="bottom" if dy > 0 else "top", fontsize=7.5,
                            fontweight="bold", color=couleur, zorder=5)
            poignees.append(_poignee(cle, color=couleur, ls=ls, lw=2, marker="o", ms=4.5))
        ax.set_ylabel(_ft("dhl"))
    _rupture_taxe(ax)
    ax.set_ylim(0, None)
    ax.set_ylim(top=ax.get_ylim()[1] * 1.12)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 0 if v >= 10 else 1)))
    ax.set_xlim(1964.2, tr.TAXE_UNIQUE_FIN + 1.4)
    ax.set_xticks(list(range(1964, tr.TAXE_UNIQUE_FIN + 2, 2)))
    ax.set_xlabel(figtools.fig_text(_lab("x")))
    ax.grid(True, alpha=0.3)
    poignees.append(_poignee("lg_rupture", color=GRIS, ls=(0, (2, 2)), lw=1, marker=7, ms=5))
    _legende(ax, poignees, ncol=2, y=-0.12, taille=7.2)
    fig.tight_layout()
    return fig


def _table_taxe():
    import pandas as pd
    lignes = []
    for cle, serie in _taxe_lignes().items():
        for date, v, etat, texte, cit, loc in serie:
            lignes.append({_lab("c_grandeur"): _lab(cle), _lab("c_ligne"): _lab("ligne_tarif"),
                           _lab("c_date_effet"): date, _lab("x"): None, _lab("c_tarif_dhl"): v,
                           _lab("c_etat_texte"): figtools.t(f"esc_{etat}"),
                           _lab("c_moyenne_dhl"): None, _lab("c_indice_prix"): None,
                           _lab("c_tarif_dhl_2025"): None, _lab("c_texte"): texte,
                           _lab("c_source"): cit, _lab("c_localisation"): loc})
    i = _ipc()
    for cle, moyennes in _taxe_moyennes().items():
        for a, m in moyennes.items():
            c = _coef(a)
            lignes.append({_lab("c_grandeur"): _lab(cle), _lab("c_ligne"): _lab("ligne_moyenne"),
                           _lab("c_date_effet"): None, _lab("x"): a, _lab("c_tarif_dhl"): None,
                           _lab("c_etat_texte"): None, _lab("c_moyenne_dhl"): round(m, 4),
                           _lab("c_indice_prix"): round(i[a], 2),
                           _lab("c_tarif_dhl_2025"): round(m * c, 3), _lab("c_texte"): None,
                           _lab("c_source"): None, _lab("c_localisation"): None})
    t = pd.DataFrame(lignes)
    t[_lab("x")] = t[_lab("x")].astype("Int64")
    return t


def _figure_taxe_unique():
    vues = [(_lab("vue_dhl"), fig_taxe_unique()),
            (_lab("vue_dhl_c"), fig_taxe_unique(constants=True))]
    return (vues, _table_taxe(), {SERIE_TAXE: tr.cles(tr.TAXE_UNIQUE, 4), **_cles_ipc()},
            "fig_compensation_taxe_unique")


# --- 13. Les recettes en regard de la subvention des carburants, 2012-2018 -----------------

def _subvention_carburants(a0=2012, a1=2018):
    d = _parts()
    return d[(d["famille"] == "budget") & (d["poste"] == "carburants")
             & d["annee"].between(a0, a1)].sort_values("annee")


def fig_carburants_recettes():
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    largeur = 0.34
    for grandeur, couleur, dx, hachure in (("revenus_commercialisation", VIOLET, -0.18, ""),
                                           ("redevance_gazoduc", VERT, 0.18, "....")):
        for a, g, h, v, cit, loc in tr.RECETTES_CARBURANTS:
            if g != grandeur or h != "encaissé":
                continue
            b = ax.bar([a + dx], [v], width=largeur, color=couleur, alpha=0.75, hatch=hachure,
                       edgecolor="white", zorder=2)
            figtools.infobulle(b[0], f"{a} · {_lab('rc_' + grandeur)} : {_nombre(v)} MD — {cit}")
            ax.annotate(_nombre(v), xy=(a + dx, v), xytext=(0, 2), textcoords="offset points",
                        ha="center", va="bottom", fontsize=6.8, color=couleur)
    for horizon, cle, st in (("loi de finances", "rc_lf", STYLE_HORIZON["loi de finances"]),
                             ("loi de finances complémentaire", "rc_lfc",
                              STYLE_HORIZON["loi de finances complémentaire"])):
        for a, g, h, v, cit, loc in tr.RECETTES_CARBURANTS:
            if h != horizon:
                continue
            p, = ax.plot([a - 0.18], [v], st["marker"], ms=7, color=st["color"], mfc="white",
                         mew=1.5, zorder=4)
            figtools.infobulle(p, f"{a} · {_lab(cle)} : {_nombre(v)} MD — {cit}"
                                  + (f", {loc}" if loc else ""))
    s = _subvention_carburants()
    v = dict(zip(s["annee"].astype(int), s["valeur_MDT"]))
    for suite in _suites(v):
        ax.plot(suite, [v[a] for a in suite], color=ORANGE, lw=2, zorder=3)
    for r in s.itertuples(index=False):
        p, = ax.plot([int(r.annee)], [r.valeur_MDT], "o", color=ORANGE, ms=5, zorder=4)
        figtools.infobulle(p, f"{int(r.annee)} · {_lab('rc_subvention')} : "
                              f"{_nombre(r.valeur_MDT)} MD — {r.etat} — {r.source}")
        ax.annotate(_nombre(r.valeur_MDT, 0), xy=(int(r.annee), r.valeur_MDT), xytext=(-5, 4),
                    textcoords="offset points", ha="right", fontsize=7, color=ORANGE)
    ax.axvline(2014.5, color=GRIS, ls=(0, (2, 2)), lw=1, zorder=1)
    _repere(ax, 2015, _lab("rc_rupture"))
    ax.annotate(_ft("rp_2015_carb"), xy=(2014.5, 1), xycoords=("data", "axes fraction"),
                xytext=(3, -4), textcoords="offset points", ha="left", va="top", fontsize=7,
                color=GRIS, bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1))
    _cadre(ax, "md", 2012, 2018)
    ax.set_xticks(list(range(2012, 2019)))
    ax.set_ylim(0, None)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: _nombre(y, 0)))
    poignees = [Patch(facecolor=VIOLET, alpha=0.75, label=figtools.fig_text(
                    _lab("rc_revenus_commercialisation"))),
                Patch(facecolor=VERT, alpha=0.75, hatch="....", edgecolor="white",
                      label=figtools.fig_text(_lab("rc_redevance_gazoduc"))),
                _poignee("rc_lf", color=STYLE_HORIZON["loi de finances"]["color"],
                         marker=STYLE_HORIZON["loi de finances"]["marker"], mfc="white", ls="none",
                         ms=7),
                _poignee("rc_lfc", color=STYLE_HORIZON["loi de finances complémentaire"]["color"],
                         marker=STYLE_HORIZON["loi de finances complémentaire"]["marker"],
                         mfc="white", ls="none", ms=7),
                _poignee("rc_subvention", color=ORANGE, lw=2, marker="o", ms=5),
                _poignee("lg_rupture", color=GRIS, ls=(0, (2, 2)), lw=1, marker=7, ms=5)]
    _legende(ax, poignees, ncol=2, y=-0.12, taille=7.2)
    fig.tight_layout()
    return fig


def _figure_carburants_recettes():
    import pandas as pd
    lignes = [{_lab("x"): a, _lab("c_grandeur"): _lab("rc_" + g if h == "encaissé" else
                                                      ("rc_lf" if h == "loi de finances"
                                                       else "rc_lfc")),
               _lab("c_horizon_rc"): h, _lab("c_MDT"): v, _lab("c_source"): cit,
               _lab("c_localisation"): loc}
              for a, g, h, v, cit, loc in tr.RECETTES_CARBURANTS]
    s = _subvention_carburants()
    lignes += [{_lab("x"): int(r.annee), _lab("c_grandeur"): _lab("rc_subvention"),
                _lab("c_horizon_rc"): _lisible(r.etat), _lab("c_MDT"): r.valeur_MDT,
                _lab("c_source"): r.source, _lab("c_localisation"): None}
               for r in s.itertuples(index=False)]
    table = pd.DataFrame(lignes).sort_values([_lab("x"), _lab("c_grandeur")])
    cles = {SERIE_RECETTES_CARB: tr.cles(tr.RECETTES_CARBURANTS, 4),
            SERIE_PARTS: list(s["source"])}
    return (fig_carburants_recettes(), table.reset_index(drop=True), cles,
            "fig_compensation_carburants_recettes")


# --- 14. Prix d'importation et prix de cession, 2016-2025 ----------------------------------

def _xticks_ic(ax):
    annees = [r[0] for r in tr.IMPORT_CESSION]
    ax.set_xticks(annees)
    ax.set_xticklabels([f"{a}\n{_lab('fin_novembre')}" if p != "année" else str(a)
                        for a, p, *_ in tr.IMPORT_CESSION], fontsize=7.5)


def fig_import_cession(produit: str = "carburants", constants: bool = False):
    figtools.apply_lang_font()
    k = (lambda a: _coef(a)) if constants else (lambda a: 1.0)
    annees = [r[0] for r in tr.IMPORT_CESSION]
    if produit == "bouteille":
        fig, ax = plt.subplots(figsize=(9.5, 5.2))
        poignees = []
        for rang, cle, ls, marker in ((8, "ic_bouteille_import", "-", "o"),
                                      (9, "ic_bouteille_cession", "--", "s")):
            ys = [r[rang] * k(r[0]) for r in tr.IMPORT_CESSION]
            ax.plot(annees, ys, color=BRUN, ls=ls, lw=1.8, zorder=2)
            for r, y in zip(tr.IMPORT_CESSION, ys):
                p, = ax.plot([r[0]], [y], marker, ms=5, color=BRUN,
                             mfc="white" if ls == "--" else BRUN, zorder=3)
                bulle = f"{r[0]} · {_lab(cle)} : {_nombre(y, 2)}"
                if constants:
                    bulle += f" — {_lab('calcul')} : {_nombre(r[rang], 3)} × {_nombre(k(r[0]), 3)}"
                figtools.infobulle(p, bulle)
                ax.annotate(_nombre(y, 1), xy=(r[0], y), xytext=(0, 5), textcoords="offset points",
                            ha="center", fontsize=6.8, color=BRUN)
            poignees.append(_poignee(cle, color=BRUN, ls=ls, lw=1.8, marker=marker, ms=5,
                                     mfc="white" if ls == "--" else BRUN))
        ax.set_ylabel(_ft("dinars_bouteille_2025" if constants else "dinars_bouteille_courants"))
        ax.set_ylim(0, None)
        ax.set_xlim(2015.4, 2025.6)
        _xticks_ic(ax)
        ax.grid(True, alpha=0.3)
        _legende(ax, poignees, ncol=1, y=-0.14, taille=7.5)
        fig.tight_layout()
        return fig
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.5, 7.0), sharex=True,
                                 gridspec_kw=dict(height_ratios=[2, 1.2], hspace=0.08))
    poignees = []
    for couleur, nom, ri, rc, re_, dx in ((ORANGE, "essence", 2, 3, 4, -0.18),
                                          (BLEU, "gasoil", 5, 6, 7, 0.18)):
        for rang, cle, ls, marker in ((ri, f"ic_{nom}_import", "-", "o"),
                                      (rc, f"ic_{nom}_cession", "--", "s")):
            ys = [r[rang] * k(r[0]) for r in tr.IMPORT_CESSION]
            ax.plot(annees, ys, color=couleur, ls=ls, lw=1.8, zorder=2)
            for r, y in zip(tr.IMPORT_CESSION, ys):
                p, = ax.plot([r[0]], [y], marker, ms=5, color=couleur,
                             mfc="white" if ls == "--" else couleur, zorder=3)
                bulle = f"{r[0]} · {_lab(cle)} : {_nombre(y, 0)}"
                if constants:
                    bulle += f" — {_lab('calcul')} : {_nombre(r[rang], 0)} × {_nombre(k(r[0]), 3)}"
                figtools.infobulle(p, bulle)
            poignees.append(_poignee(cle, color=couleur, ls=ls, lw=1.8, marker=marker, ms=5,
                                     mfc="white" if ls == "--" else couleur))
        for r in tr.IMPORT_CESSION:
            e = r[re_] * k(r[0])
            b = bx.bar([r[0] + dx], [e], width=0.34, color=couleur, alpha=0.75, zorder=2)
            figtools.infobulle(b[0], f"{r[0]} · {_lab(f'ic_ecart_{nom}')} : {_nombre(e, 0)}")
            bx.annotate(_nombre(e, 0).replace("-", "−"), xy=(r[0] + dx, e),
                        xytext=(0, 2 if e >= 0 else -2), textcoords="offset points",
                        ha="center", va="bottom" if e >= 0 else "top", fontsize=6.3,
                        color=couleur)
        poignees.append(Patch(facecolor=couleur, alpha=0.75,
                              label=figtools.fig_text(_lab(f"ic_ecart_{nom}"))))
    ax.set_ylabel(_ft("millimes_2025" if constants else "millimes_courants"))
    ax.set_ylim(0, None)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: _nombre(y, 0)))
    ax.grid(True, alpha=0.3)
    bx.axhline(0, color=NOIR, lw=0.8)
    bx.set_ylabel(_ft("ic_ecart_2025" if constants else "ic_ecart"), fontsize=8)
    bx.margins(y=0.25)
    bx.yaxis.set_major_formatter(FuncFormatter(lambda y, _: _nombre(y, 0)))
    bx.grid(True, axis="y", alpha=0.3)
    bx.set_xlim(2015.4, 2025.6)
    _xticks_ic(bx)
    bx.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.32), ncol=2,
              fontsize=7.2, frameon=False)
    fig.subplots_adjust(left=0.1, right=0.98, top=0.97, bottom=0.24)
    return fig


def _figure_import_cession():
    import pandas as pd
    i = _ipc()
    lignes = []
    for a, periode, *v in tr.IMPORT_CESSION:
        c = _coef(a)
        loc = _lab("loc_novembre" if periode != "année" else "loc_decembre", a=a)
        per = _lab("periode_novembre" if periode != "année" else "periode_annee")
        for nom, unite, imp, ces, ec in (("p_essence", "u_millimes_litre", v[0], v[1], v[2]),
                                         ("p_gasoil_ordinaire", "u_millimes_litre", v[3], v[4], v[5]),
                                         ("p_bouteille", "u_dinars_bouteille", v[6], v[7], None)):
            lignes.append({
                _lab("x"): a, _lab("c_periode_ic"): per, _lab("c_produit"): _lab(nom),
                _lab("c_unite"): _lab(unite), _lab("c_import"): imp, _lab("c_cession"): ces,
                _lab("c_ecart_ic"): ec, _lab("c_indice_prix"): round(i[a], 2),
                _lab("c_import_2025"): round(imp * c, 3 if ec is None else 1),
                _lab("c_cession_2025"): round(ces * c, 3 if ec is None else 1),
                _lab("c_ecart_2025"): None if ec is None else round(ec * c, 1),
                _lab("c_source"): tr.IMPORT_CESSION_CLE, _lab("c_localisation"): loc})
    vues = [(_lab("vue_ic"), fig_import_cession()),
            (_lab("vue_ic_c"), fig_import_cession(constants=True)),
            (_lab("vue_bouteille"), fig_import_cession("bouteille")),
            (_lab("vue_bouteille_c"), fig_import_cession("bouteille", constants=True))]
    return (vues, pd.DataFrame(lignes), {SERIE_IMPORT: [tr.IMPORT_CESSION_CLE], **_cles_ipc()},
            "fig_compensation_import_cession")


# --- 15. La Caisse dans le tableau des fonds spéciaux du Trésor, 1987-1994 -----------------

def _dotations_bct(a0=1987, a1=1994):
    d = _compte()
    return d[(d["famille"] == "budget_dotation_cgc_bct") & d["annee"].between(a0, a1)]


def fig_lf_caisse():
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    for g, sub, rp, tot, tab, cit, loc, rem in tr.LF_CAISSE:
        b1 = ax.bar([g], [sub], width=0.6, color="#cfe2fb", edgecolor=BLEU, ls="--", lw=1,
                    zorder=2)
        b2 = ax.bar([g], [rp], bottom=[sub], width=0.6, color="#cdeed6", edgecolor=VERT, ls="--",
                    lw=1, zorder=2)
        figtools.infobulle(b1[0], f"{g} · {_lab('lf_subvention')} : {_nombre(sub)} MD — {cit}, {loc}")
        figtools.infobulle(b2[0], f"{g} · {_lab('lf_recettes_propres')} : {_nombre(rp)} MD — "
                                  f"{cit}, {loc}" + (f" — {rem}" if rem else ""))
        ax.annotate(_nombre(tot), xy=(g, tot), xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom", fontsize=7.5, color=NOIR)
    dot = _dotations_bct()
    for r in dot.itertuples(index=False):
        p, = ax.plot([int(r.annee) + 0.36], [r.valeur_MDT], "D", ms=6.5, color=NOIR, zorder=4)
        figtools.infobulle(p, f"{int(r.annee)} · {_lab('lf_dotation_bct')} : "
                              f"{_nombre(r.valeur_MDT)} MD — {r.source}, p. {_nombre(r.page_imprimee, 0)}")
    _cadre(ax, "lf_md", 1987, 1994)
    ax.set_xticks([r[0] for r in tr.LF_CAISSE])
    ax.set_xticklabels([f"{r[0]}\n{_lab('lf_tableau_' + r[4].lower())}" for r in tr.LF_CAISSE],
                       fontsize=7.5)
    ax.set_ylim(0, max(r[3] for r in tr.LF_CAISSE) * 1.18)
    poignees = [Patch(facecolor="#cfe2fb", edgecolor=BLEU, ls="--",
                      label=figtools.fig_text(_lab("lf_subvention"))),
                Patch(facecolor="#cdeed6", edgecolor=VERT, ls="--",
                      label=figtools.fig_text(_lab("lf_recettes_propres"))),
                _poignee("lf_dotation_bct", color=NOIR, marker="D", ms=6.5, ls="none")]
    _legende(ax, poignees, ncol=1, y=-0.14, taille=7.5)
    fig.tight_layout()
    return fig


def _figure_lf_caisse():
    import pandas as pd
    dot = {int(r.annee): r for r in _dotations_bct().itertuples(index=False)}
    lignes = []
    for g, sub, rp, tot, tab, cit, loc, rem in tr.LF_CAISSE:
        r = dot.get(g)
        lignes.append({_lab("c_gestion"): g, _lab("c_subvention_lf"): sub,
                       _lab("c_recettes_propres_lf"): rp, _lab("c_total_lf"): tot,
                       _lab("c_tableau"): _lab("lf_tableau_" + tab.lower()),
                       _lab("c_source"): cit, _lab("c_localisation"): loc,
                       _lab("c_remarque"): rem or None,
                       _lab("c_dotation_bct"): r.valeur_MDT if r is not None else None,
                       _lab("c_source_dotation"): r.source if r is not None else None,
                       _lab("c_page_dotation"): (int(r.page_imprimee) if r is not None
                                                 and not _vide(r.page_imprimee) else None)})
    table = pd.DataFrame(lignes)
    table[_lab("c_page_dotation")] = table[_lab("c_page_dotation")].astype("Int64")
    cles = {SERIE_LF_CAISSE: tr.cles(tr.LF_CAISSE, 5),
            SERIE_COMPTE: [r.source for r in dot.values()]}
    return fig_lf_caisse(), table, cles, "fig_compensation_lf_caisse"


# --- 16. La Caisse dans le tableau B des fonds spéciaux du Trésor, 2005-2010 ----------------

def fig_lf_caisse_2005():
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 4.4))
    for g, v, cit, loc in tr.LF_CAISSE_2005:
        b = ax.bar([g], [v], width=0.6, color="#e6d8f7", edgecolor=VIOLET, ls="--", lw=1, zorder=2)
        figtools.infobulle(b[0], f"{g} · {_lab('lf_b_barre')} : {_nombre(v, 0)} D — {cit}, {loc}")
        ax.annotate(_nombre(v, 0), xy=(g, v), xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom", fontsize=7.5, color=VIOLET)
    _cadre(ax, "lf_dinars", 2005, 2010)
    ax.set_xticks([r[0] for r in tr.LF_CAISSE_2005])
    ax.set_ylim(0, max(r[1] for r in tr.LF_CAISSE_2005) * 1.18)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: _nombre(y, 0)))
    _legende(ax, [Patch(facecolor="#e6d8f7", edgecolor=VIOLET, ls="--",
                        label=figtools.fig_text(_lab("lf_b_barre")))], ncol=1, y=-0.16, taille=7.5)
    fig.tight_layout()
    return fig


def _figure_lf_caisse_2005():
    import pandas as pd
    table = pd.DataFrame([{_lab("c_gestion"): g, _lab("c_recettes_prevues_d"): v,
                           _lab("c_source"): cit, _lab("c_localisation"): loc}
                          for g, v, cit, loc in tr.LF_CAISSE_2005])
    return (fig_lf_caisse_2005(), table,
            {SERIE_LF_CAISSE_2005: tr.cles(tr.LF_CAISSE_2005, 2)},
            "fig_compensation_lf_caisse_2005")


# --- point d'entrée des chapitres --------------------------------------------------------

FIGURES = {
    "longue_periode": _figure_longue_periode,
    "par_poste": _figure_par_poste,
    "prevu_realise": _figure_prevu_realise,
    "recettes_caisse": _figure_recettes_caisse,
    "sources_exterieures": _figure_sources_exterieures,
    "compte_caisse": _figure_compte_caisse,
    "par_produit": _figure_par_produit,
    "prevu_realise_postes": _figure_prevu_realise_postes,
    "carburants_directe_totale": _figure_carburants_directe_totale,
    "carburants_beneficiaires": _figure_carburants_beneficiaires,
    "prix_pompe": _figure_prix_pompe,
    "taxe_unique": _figure_taxe_unique,
    "carburants_recettes": _figure_carburants_recettes,
    "import_cession": _figure_import_cession,
    "lf_caisse": _figure_lf_caisse,
    "lf_caisse_2005": _figure_lf_caisse_2005,
}
# Figures qui portent une vue en monnaie constante : la ligne « Source » ne dit pas « valeurs
# courantes », la note de lecture donne la règle de déflation.
AVEC_CONSTANTS = {"prix_pompe", "taxe_unique", "import_cession"}


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
                         note_lecture=note_lecture, nominal=nom not in AVEC_CONSTANTS)
    plt.close("all")

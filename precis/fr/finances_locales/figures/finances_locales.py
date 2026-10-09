"""Figures du livre *Les finances locales*. Le chapitre « La longue période » est dissous :
chaque figure est montée dans le chapitre de sa règle (budgets, impôts, transferts).

    from figures import finances_locales as fl
    fl.vues_ressources()  ; fl.table_ressources()   # recettes de fonctionnement des communes
    fl.fig_autonomie()    ; fl.table_autonomie()    # ratios d'autonomie, publiés et calculés
    fl.vues_impots()      ; fl.table_impots()       # TIB, TNB, TCL, taxe hôtelière
    fl.vues_immeubles_rendement() ; fl.table_immeubles_rendement()   # TIB et TNB, 2008-2023
    fl.fig_immeubles_recouvrement() ; fl.table_recouvrement_tib()    # recouvrement publié
    fl.vues_activite_rendement()  ; fl.table_activite_rendement()    # TCL, taxe hôtelière
    fl.vues_fccl()        ; fl.table_fccl()         # fonds commun des collectivités locales
    fl.vues_cpscl()       ; fl.table_cpscl()        # flux et impayés de la CPSCL
    fl.vues_ins()         ; fl.table_ins()          # épargne brute et FBCF, comptes nationaux
    fl.fig_remunerations() ; fl.table_remunerations()  # rémunérations / recettes du titre I
    fl.vues_depenses()    ; fl.table_depenses()     # dépenses des deux titres, service de la dette

D'OÙ VIENNENT LES DONNÉES. Sept séries de `tunisia-data`, toutes lues par `figtools.series()`
(l'entrepôt s'il est installé, sinon le cache `precis/_seriescache/`) :

  - `finances-locales-communes-agregats` : agrégats publiés par la DGCT (2008-2019) et somme
    des budgets des 350 communes (2018-2023), colonne `source` ;
  - `finances-locales-bm-1985-2012` : tableau 1 du document d'évaluation du programme de la
    Banque mondiale de 2014 (2002-2012) ;
  - `finances-locales-bm-1992` et `finances-locales-bm-1997` : rapports de la Banque mondiale de
    1992 (fig. 6, 1985-1991) et de 1997 (annexe 4, tabl. 2, 1990-1996). L'entrée du catalogue
    de l'entrepôt ne désigne que le fichier de 2014 ; ces deux fichiers sont snapshotés par
    `scripts/snapshot_finances_locales_bm.py`, et leur provenance est déclarée ci-dessous ;
  - `finances-locales-fccl-lois-de-finances` : montant du fonds commun inscrit au tableau des
    fonds spéciaux du Trésor des lois de finances pour 1976 à 1995 (sauf 1979) : une prévision
    votée, pour le fonds entier ;
  - `finances-locales-cpscl` : états financiers de la CPSCL, 2005-2024 ;
  - `finances-locales-ins-comptes` : compte des collectivités locales des comptes de la nation,
    trois bases ;
  - `cnat-pib-nominal` : PIB aux prix courants, édition par édition des comptes de la nation.

RÈGLES COMMUNES À TOUTES LES FIGURES.

  - **Les sources ne sont jamais fusionnées.** Chaque source a sa propre courbe, avec sa
    marque : rond plein pour la DGCT, losange pour la somme des communes, triangle et tirets
    pour le document de 2014, carré et pointillés pour le rapport de 1997, triangle renversé
    pour celui de 1992. Sur les années communes (2002-2012, 2018-2019), les courbes se
    superposent ou s'écartent : l'écart est montré, pas arbitré.
  - **Une case vide reste vide.** Les impôts un à un manquent en 2020 et 2021 : la courbe s'y
    interrompt, rien n'est interpolé.
  - **Les exercices non clos sont marqués** par un point creux : 2021 (situation au
    25 décembre 2021) et 2023 (provisoire au 10 janvier 2024).
  - **Les ruptures sont tracées** (`figtools.marque_rupture`) : décrets gouvernementaux du
    26 mai 2016 créant et étendant des communes (le périmètre passe de 264 à 350 communes) ;
    passage du fonds commun des parts d'impôts à la subvention du budget, à la gestion 1987 ;
    suppression du fonds commun au 1er janvier 2018 ; changements de base des comptes
    nationaux, jamais raccordés.
  - **Le PIB** est celui des comptes de la nation de l'INS, pris pour chaque année dans
    l'édition la plus récente qui la porte : base 1983 jusqu'en 2004, base 1997 de 2005 à
    2014, base 2015 ensuite. Le rapport de 1992 publie son propre PIB, qui sert à ses seuls
    chiffres. Le rapport de 1997 n'en publie pas : ses points n'ont pas de vue au PIB.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import MaxNLocator

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_COMMUNES = "finances-locales-communes-agregats"
SERIE_BM2014 = "finances-locales-bm-1985-2012"
SERIE_BM1992 = "finances-locales-bm-1992"
SERIE_BM1997 = "finances-locales-bm-1997"
SERIE_FCCL_LF = "finances-locales-fccl-lois-de-finances"
SERIE_CPSCL = "finances-locales-cpscl"
SERIE_INS = "finances-locales-ins-comptes"
SERIE_PIB = "cnat-pib-nominal"

# Décrets gouvernementaux n° 2016-600, 2016-601 et 2016-602 du 26 mai 2016 (JORT n° 43 du
# 27 mai 2016, déposé le même jour, exécutoires le 1er juin 2016) : création de communes et
# extension des périmètres communaux. La ligne est tracée entre 2015 et 2016.
RUPTURE_COMMUNES = 2016
# Suppression du fonds commun des collectivités locales au 1er janvier 2018 (loi de finances
# pour 2018, art. 11 et 67) : la ligne est tracée entre 2017 et 2018. C'est une RUPTURE DE
# SÉRIE, et pas seulement un changement de nom : les subventions annuelles qui succèdent au
# fonds se partagent selon l'arrêté conjoint du 22 juin 2018 (85 % de gestion, dont 89 % aux
# communes ; 15 % d'investissement et de besoins spécifiques), non plus selon la loi n° 75-36
# (82 % aux collectivités, dont 86 % aux communes ; 18 % de réserve). Les lignes de 2018-2019
# sont donc des grandeurs distinctes (`sub_…`), jamais reliées à celles de 2008-2017.
RUPTURE_FCCL = 2018
# Loi de finances pour 1987, art. 92 : les parts d'impôts affectées au fonds commun reviennent
# au budget de l'État, qui lui verse une subvention. C'est une RUPTURE DE DÉFINITION du montant
# voté : jusqu'en 1986, le tableau des fonds spéciaux du Trésor imprime une évaluation de
# recettes affectées ; à partir de 1987, une subvention du budget, des recettes propres et leur
# total. Les deux segments ne sont jamais reliés ; la ligne est tracée entre 1986 et 1987.
RUPTURE_FCCL_1987 = 1987

# Les deux fichiers de la Banque mondiale que le catalogue de l'entrepôt ne désigne pas.
figtools.register_provenance(
    SERIE_BM1992,
    titre=("Recettes courantes des communes et fonds commun des collectivités locales selon "
           "la Banque mondiale, 1985-1991 (rapport de 1992, fig. 6)"),
    titre_ar=("المداخيل الاعتيادية للبلديات والمال المشترك للجماعات المحلية حسب البنك "
              "الدولي، 1985-1991 (تقرير 1992، الرسم 6)"),
    sources=["wb-msip-1992"],
    unite="millions de dinars courants",
    unite_ar="بملايين الدنانير الجارية",
    perimetre=("communes ; ligne « F.C.C.L. » du rapport, vraisemblablement le fonds entier "
               "et non la quote-part des communes ; PIB publié par le même rapport"),
    perimetre_ar="البلديات؛ سطر المال المشترك في التقرير، والأرجح أنّه المال بأكمله",
    caveats=("Valeurs lues à l'image ; 1990-1991 vraisemblablement estimées par la mission. "
             "Série séparée, jamais fusionnée avec les autres."),
    caveats_ar="قيم مقروءة من الصورة؛ سنتا 1990-1991 تقديرات على الأرجح. سلسلة منفصلة.",
    fiche="sources/finances-locales-banque-mondiale.md",
)
figtools.register_provenance(
    SERIE_BM1997,
    titre=("Recettes courantes des communes par source selon la Banque mondiale, 1990, 1992 "
           "et 1994-1996 (rapport de 1997, annexe 4, tabl. 2)"),
    titre_ar=("المداخيل الاعتيادية للبلديات حسب المصدر وفق البنك الدولي، 1990 و1992 "
              "و1994-1996 (تقرير 1997، الملحق 4، الجدول 2)"),
    sources=["wb-mdp2-1997"],
    unite="millions de dinars courants ; parts en %",
    unite_ar="بملايين الدنانير الجارية؛ النسب %",
    perimetre="communes ; recettes courantes (titre 1), ressources propres et fonds commun",
    perimetre_ar="البلديات؛ المداخيل الاعتيادية والموارد الذاتية والمال المشترك",
    caveats=("Valeurs lues à l'image ; la ligne de la taxe locative manque au tableau imprimé. "
             "Série séparée, jamais fusionnée avec les autres."),
    caveats_ar="قيم مقروءة من الصورة؛ سطر المعلوم على القيمة الكرائية غائب عن الجدول المطبوع.",
    fiche="sources/finances-locales-banque-mondiale.md",
)

# La série des lois de finances. Le catalogue de l'entrepôt la rattache à vingt et une clés,
# une par loi de finances, que la bibliographie du volume ne porte pas : la source se dit en
# une ligne, et chaque valeur garde sa loi, son fascicule et sa page dans les colonnes
# `texte`, `jort_numero` et `page` du fichier de la série. Les libellés arabes sont ceux du
# catalogue.
_M_LF = figtools.meta(SERIE_FCCL_LF)
figtools.register_provenance(
    SERIE_FCCL_LF,
    titre=("Fonds commun des collectivités locales : montants inscrits aux lois de finances, "
           "1976-1995 (tableau des fonds spéciaux du Trésor)"),
    titre_ar=_M_LF.get("titre_ar"),
    sources=[],
    source_ligne=("lois de finances pour 1976 à 1995, tableaux des fonds spéciaux du Trésor "
                  "(*Journal officiel*, édition française)"),
    source_ligne_ar="قوانين المالية لسنوات 1976 إلى 1995، جداول الحسابات الخاصة في الخزينة",
    unite="millions de dinars courants",
    unite_ar=_M_LF.get("unite_ar"),
    perimetre=("ligne « Fonds commun des collectivités locales » du tableau des fonds spéciaux "
               "du Trésor annexé à chaque loi de finances, de 1976 à 1978 et de 1980 à 1995 ; "
               "fonds entier — toutes collectivités, réserve et prélèvements compris ; "
               "1976-1986 : évaluation des recettes affectées au fonds, égale à celle de ses "
               "dépenses ; 1987-1995 : total des recettes du fonds, soit la subvention du "
               "budget et les recettes propres, égal à ses dépenses"),
    perimetre_ar=_M_LF.get("perimetre_ar"),
    caveats=("Montants votés avec la loi de finances initiale, non montants versés : ni les "
             "lois de finances complémentaires ni les lois de règlement ne sont reprises. "
             "Deux définitions, jamais reliées : parts d'impôts jusqu'en 1986, subvention du "
             "budget à partir de 1987. Aucune valeur pour 1979. À partir de la loi de finances "
             "pour 1996, le tableau n'imprime plus le montant du fonds : la série s'arrête en "
             "1995, le fonds dure jusqu'au 1er janvier 2018. Aucune année commune avec les "
             "agrégats de la Direction générale des collectivités locales (2008-2023) : les "
             "deux séries ne sont pas raccordées. Série séparée des rapports de la Banque "
             "mondiale, dont elle s'écarte en 1985, 1986 et 1990."),
    caveats_ar=_M_LF.get("caveats_ar"),
    fiche="sources/finances-locales-fccl-lois-de-finances.md",
)

BLEU, ORANGE, VERT, VIOLET, ROUGE, GRIS, BRUN = (
    "#0969da", "#d1600f", "#1a7f37", "#8250df", "#cf222e", "#57606a", "#9a6700")

# Une source = une marque et un trait.
STYLE_SOURCE = {
    "bm1992": dict(marker="v", ls="-.", ms=4.5, lw=1.3),
    "bm1997": dict(marker="s", ls=":", ms=4.5, lw=1.5),
    "bm2014": dict(marker="^", ls="--", ms=4.5, lw=1.3),
    "dgct": dict(marker="o", ls="-", ms=4.5, lw=1.8),
    "somme": dict(marker="D", ls="-", ms=4, lw=1.2),
    "lf": dict(marker="P", ls=(0, (6, 1.5)), ms=5, lw=1.4),
}
STYLE_BASE = {1983: ":", 1997: "--", 2015: "-"}

_L = {
    "x": {"fr": "Année", "ar": "السنة"},
    "md": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "pct_r1": {"fr": "En % des recettes de fonctionnement", "ar": "% من موارد العنوان الأوّل"},
    "pct_pib": {"fr": "En % du PIB", "ar": "% من الناتج المحلي الإجمالي"},
    "pct": {"fr": "En %", "ar": "%"},
    "vue_md": {"fr": "En millions de dinars", "ar": "بملايين الدنانير"},
    "vue_r1": {"fr": "En part des recettes de fonctionnement",
               "ar": "كنسبة من موارد العنوان الأوّل"},
    "vue_pib": {"fr": "En % du PIB", "ar": "% من الناتج"},
    "vue_recouvrement": {"fr": "Recouvrement de la TIB", "ar": "استخلاص المعلوم على العقارات المبنية"},
    "recouvrement_tib": {"fr": "Taux de recouvrement de la TIB publié par la DGCT",
                         "ar": "نسبة استخلاص المعلوم على العقارات المبنية المنشورة"},
    "t_recouvrement": {"fr": "Taxe sur les immeubles bâtis : taux de recouvrement publié",
                       "ar": "المعلوم على العقارات المبنية: نسبة الاستخلاص المنشورة"},
    "vue_flux": {"fr": "Flux de l'année", "ar": "تدفّقات السنة"},
    "vue_impayes": {"fr": "Impayés", "ar": "المتخلّدات"},
    # sources
    "src_bm1992": {"fr": "Banque mondiale, rapport de 1992", "ar": "البنك الدولي، تقرير 1992"},
    "src_bm1997": {"fr": "Banque mondiale, rapport de 1997", "ar": "البنك الدولي، تقرير 1997"},
    "src_bm2014": {"fr": "Banque mondiale, document de 2014",
                   "ar": "البنك الدولي، وثيقة 2014"},
    "src_dgct": {"fr": "DGCT, agrégats publiés", "ar": "الإدارة العامة، المجاميع المنشورة"},
    "src_somme": {"fr": "Somme des budgets des communes",
                  "ar": "مجموع ميزانيات البلديات"},
    "src_lf": {"fr": "Lois de finances, montant voté (fonds spéciaux du Trésor)",
               "ar": "قوانين المالية، المبلغ المصادق عليه (الحسابات الخاصة في الخزينة)"},
    "src_cpscl": {"fr": "CPSCL, états financiers", "ar": "الصندوق، القوائم المالية"},
    # grandeurs
    "propres": {"fr": "Recettes propres de fonctionnement",
                "ar": "الموارد الذاتية للعنوان الأوّل"},
    "transferts": {"fr": "Transferts de fonctionnement de l'État",
                   "ar": "تحويلات الدولة بعنوان التسيير"},
    "part_transferts": {"fr": "Part des transferts", "ar": "نسبة التحويلات"},
    "a1": {"fr": "Recettes propres / recettes de fonctionnement",
           "ar": "الموارد الذاتية / موارد العنوان الأوّل"},
    "a": {"fr": "Recettes propres / ressources hors emprunt et hors épargne reportée",
          "ar": "الموارد الذاتية / الموارد دون الاقتراض والادّخار المنقول"},
    "ratio_dgct": {"fr": "Ratio d'autonomie financière publié par la DGCT",
                   "ar": "نسبة الاستقلالية المالية المنشورة"},
    "tib": {"fr": "Taxe sur les immeubles bâtis", "ar": "المعلوم على العقارات المبنية"},
    "tnb": {"fr": "Taxe sur les terrains non bâtis", "ar": "المعلوم على الأراضي غير المبنية"},
    "tcl": {"fr": "Taxe sur les établissements (TCL)",
            "ar": "المعلوم على المؤسسات ذات الصبغة الصناعية أو التجارية أو المهنية"},
    "taxe_hoteliere": {"fr": "Taxe hôtelière", "ar": "المعلوم على النزل"},
    "fccl_credit_global": {"fr": "Fonds commun : crédit global",
                           "ar": "المال المشترك: الاعتماد الجملي"},
    "fccl_communes": {"fr": "Fonds commun : quote-part des communes",
                      "ar": "المال المشترك: مناب البلديات"},
    "fccl_regions": {"fr": "Fonds commun : quote-part des conseils régionaux",
                     "ar": "المال المشترك: مناب المجالس الجهوية"},
    "fccl_reserve": {"fr": "Fonds commun : réserve", "ar": "المال المشترك: الاحتياطي"},
    "fccl_bm": {"fr": "Fonds commun (ligne du rapport)", "ar": "المال المشترك (سطر التقرير)"},
    "fccl_vote": {"fr": "Fonds commun voté, fonds entier (1976-1995)",
                  "ar": "المال المشترك المصادق عليه، بأكمله (1976-1995)"},
    "fccl_vote_parts": {"fr": "Fonds commun voté, fonds entier : évaluation des recettes "
                              "affectées (parts d'impôts)",
                        "ar": "المال المشترك المصادق عليه، بأكمله: تقدير الموارد المخصّصة"},
    "fccl_vote_total": {"fr": "Fonds commun voté, fonds entier : total des recettes "
                              "(subvention du budget et recettes propres)",
                        "ar": "المال المشترك المصادق عليه، بأكمله: مجموع الموارد "
                              "(منحة الميزانية والموارد الذاتية)"},
    "sub_credit_global": {"fr": "Subventions annuelles : crédit global",
                          "ar": "الدعم المالي السنوي: الاعتماد الجملي"},
    "sub_communes": {"fr": "Subventions annuelles : part des communes",
                     "ar": "الدعم المالي السنوي: مناب البلديات"},
    "sub_regions": {"fr": "Subventions annuelles : part des conseils régionaux",
                    "ar": "الدعم المالي السنوي: مناب المجالس الجهوية"},
    "sub_reserve": {"fr": "Subventions annuelles : ligne que la source intitule encore "
                          "« réserve »",
                    "ar": "الدعم المالي السنوي: السطر الذي يسمّيه المصدر «المدّخر»"},
    "dotation_annuelle": {"fr": "Subvention annuelle : quote-parts inscrites aux budgets des "
                                "communes",
                          "ar": "الدعم المالي السنوي: المنابات المرسّمة بميزانيات البلديات"},
    "dotations_recues_etat": {"fr": "Dotations reçues de l'État",
                              "ar": "الاعتمادات المتأتية من الدولة"},
    "subventions_accordees_cl": {"fr": "Subventions accordées aux collectivités",
                                 "ar": "المنح المسندة إلى الجماعات"},
    "prets_accordes_cl": {"fr": "Prêts accordés aux collectivités",
                          "ar": "القروض المسندة إلى الجماعات"},
    "remboursements_prets": {"fr": "Remboursements de prêts reçus",
                             "ar": "استخلاص القروض"},
    "annuites_echues_impayees": {"fr": "Annuités échues et impayées",
                                 "ar": "الأقساط الحالّة وغير المسدّدة"},
    "provisions_impayes": {"fr": "Provisions pour impayés", "ar": "المدّخرات بعنوان المتخلّدات"},
    "epargnebrute": {"fr": "Épargne brute", "ar": "الادّخار الخام"},
    "fbcf": {"fr": "Formation brute de capital fixe", "ar": "تكوين رأس المال الثابت الخام"},
    "base": {"fr": "base {b}", "ar": "أساس {b}"},
    # marques
    "provisoire": {"fr": "exercice non clos", "ar": "سنة غير مختومة"},
    "lg_creux": {"fr": "point creux : exercice non clos (2021, 2023)",
                 "ar": "نقطة فارغة: سنة غير مختومة (2021 و2023)"},
    "lg_creux_fccl": {"fr": "point creux : 2018-2019, subventions annuelles ; 2023, provisoire",
                      "ar": "نقطة فارغة: 2018-2019، الدعم المالي السنوي؛ 2023 وقتية"},
    "lg_creux_ins": {"fr": "point creux : valeur semi-définitive ou provisoire",
                     "ar": "نقطة فارغة: قيمة شبه نهائية أو وقتية"},
    "rup_communes": {"fr": "communes créées et étendues\n(décrets du 26 mai 2016)",
                     "ar": "إحداث بلديات وتوسيعها\n(أوامر 26 ماي 2016)"},
    "rup_fccl": {"fr": "rupture de série :\nfonds supprimé,\nautre base (2018)",
                 "ar": "انقطاع السلسلة:\nحذف المال المشترك،\nقاعدة أخرى (2018)"},
    "rup_fccl_1987": {"fr": "rupture de définition :\nparts d'impôts, puis\n"
                            "subvention du budget (1987)",
                      "ar": "تغيّر التعريف:\nموارد جبائية مخصّصة ثمّ\nمنحة من الميزانية (1987)"},
    "rup_pib": {"fr": "PIB : base {b}", "ar": "الناتج: أساس {b}"},
    # textes marqués sur les figures des chapitres d'impôts
    "mq_abandon_2012": {"fr": "abandon d'arriérés\n(loi de 2012)",
                        "ar": "التخلّي عن متخلّدات\n(قانون 2012)"},
    "mq_baremes_2017": {"fr": "barèmes relevés\n(1er janvier 2017)",
                        "ar": "الترفيع في التعريفات\n(1 جانفي 2017)"},
    "mq_abandon_2019": {"fr": "abandon d'arriérés\n(loi de 2019)",
                        "ar": "التخلّي عن متخلّدات\n(قانون 2019)"},
    "mq_plafond_2012": {"fr": "fin du maximum annuel\n(1er janvier 2012)",
                        "ar": "إلغاء الحدّ الأقصى السنوي\n(1 جانفي 2012)"},
    "mq_assiette_2014": {"fr": "assiette étendue\n(1er janvier 2014)",
                         "ar": "توسيع القاعدة\n(1 جانفي 2014)"},
    "mq_fccl_2014": {"fr": "critères révisés\n(1er janvier 2014)",
                     "ar": "مراجعة المقاييس\n(1 جانفي 2014)"},
    "lg_absence_fccl": {"fr": "1996-2007 : la loi de finances n'imprime plus le montant du fonds",
                        "ar": "1996-2007: قانون المالية لا يذكر مبلغ المال المشترك"},
    "lg_marque_texte": {"fr": "trait rouge : texte de loi ou décret, placé à sa date d'effet",
                        "ar": "خطّ أحمر: نصّ قانوني في تاريخ نفاذه"},
    # dépenses, rémunérations et dette (chapitre des budgets)
    "vue_depenses": {"fr": "Dépenses des deux titres", "ar": "نفقات العنوانين"},
    "vue_dette": {"fr": "Service de la dette et emprunt", "ar": "خدمة الدين والاقتراض"},
    "depenses_t1": {"fr": "Dépenses du titre I", "ar": "نفقات العنوان الأوّل"},
    "depenses_t2": {"fr": "Dépenses du titre II", "ar": "نفقات العنوان الثاني"},
    "interets_dette": {"fr": "Intérêts de la dette", "ar": "فوائد الدين"},
    "remboursement_principal": {"fr": "Remboursement du principal de la dette",
                                "ar": "تسديد أصل الدين"},
    "emprunts_interieurs": {"fr": "Emprunts intérieurs mobilisés",
                            "ar": "موارد الاقتراض الداخلي"},
    "rem_ratio_dgct": {"fr": "Ratio « Rémunération » publié par la DGCT",
                       "ar": "نسبة «التأجير» المنشورة"},
    "rem_meme_annee": {"fr": "Rémunérations / recettes du titre I de la même année",
                       "ar": "التأجير / موارد العنوان الأوّل لنفس السنة"},
    "rem_annee_prec": {"fr": "Rémunérations / recettes du titre I de l'année précédente",
                       "ar": "التأجير / موارد العنوان الأوّل للسنة السابقة"},
    "lg_plafond_moitie": {"fr": "plafond de la moitié, règle de prévision des budgets "
                                "communaux depuis 2019",
                          "ar": "سقف النصف، قاعدة تقديرية لميزانيات البلديات منذ 2019"},
    "lg_creux_budg": {"fr": "point creux : exercice non clos au numérateur ou au "
                            "dénominateur (2021, 2023)",
                      "ar": "نقطة فارغة: سنة غير مختومة في البسط أو المقام (2021 و2023)"},
    "mq_budg_2008": {"fr": "dépense limitée aux\nrecettes réalisées\n(budgets de 2008)",
                     "ar": "حصر النفقات في\nالمقابيض المحقّقة\n(ميزانيات 2008)"},
    "mq_budg_2019": {"fr": "code de 2018\n(budgets de 2019)",
                     "ar": "مجلة 2018\n(ميزانيات 2019)"},
    "t_remunerations": {"fr": "Rémunérations des communes rapportées aux recettes du titre I",
                        "ar": "تأجير أعوان البلديات نسبةً إلى موارد العنوان الأوّل"},
    "t_depenses": {"fr": "Dépenses des communes, par titre",
                   "ar": "نفقات البلديات حسب العنوان"},
    "t_dette": {"fr": "Service de la dette et emprunt des communes",
                "ar": "خدمة الدين والاقتراض للبلديات"},
    # titres
    "t_ressources": {"fr": "Recettes de fonctionnement des communes : recettes propres et "
                           "transferts de l'État",
                     "ar": "موارد العنوان الأوّل للبلديات: الموارد الذاتية وتحويلات الدولة"},
    "t_autonomie": {"fr": "Autonomie financière des communes : ratios publiés et calculés",
                    "ar": "الاستقلالية المالية للبلديات: نسب منشورة ومحسوبة"},
    "t_impots": {"fr": "Rendement des impôts locaux des communes",
                 "ar": "مردود الجباية المحلية للبلديات"},
    "t_immeubles_rendement": {"fr": "Produit des deux taxes sur les immeubles, communes",
                              "ar": "مردود المعلومين على العقارات، البلديات"},
    "t_activite_rendement": {"fr": "Produit de la taxe sur les établissements et de la taxe "
                                   "hôtelière, communes",
                             "ar": "مردود المعلوم على المؤسسات والمعلوم على النزل، البلديات"},
    "t_fccl": {"fr": "Le fonds commun des collectivités locales, puis les subventions annuelles",
               "ar": "المال المشترك للجماعات المحلية ثمّ الدعم المالي السنوي"},
    "t_cpscl": {"fr": "La Caisse des prêts et de soutien des collectivités locales",
                "ar": "صندوق القروض ومساعدة الجماعات المحلية"},
    "t_ins": {"fr": "Épargne brute et investissement des collectivités locales "
                    "(comptes de la nation)",
              "ar": "الادّخار الخام واستثمار الجماعات المحلية (الحسابات القومية)"},
    # colonnes des tables
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_grandeur": {"fr": "Grandeur", "ar": "المقدار"},
    "col_source": {"fr": "Source", "ar": "المصدر"},
    "col_md": {"fr": "Montant (MD)", "ar": "المبلغ (م.د)"},
    "col_pct": {"fr": "Valeur (%)", "ar": "القيمة (%)"},
    "col_pct_r1": {"fr": "% des recettes de fonctionnement", "ar": "% من موارد العنوان الأوّل"},
    "col_pct_pib": {"fr": "% du PIB", "ar": "% من الناتج"},
    "col_statut": {"fr": "Statut", "ar": "الوضعية"},
    "col_base": {"fr": "Base du PIB ou du compte", "ar": "سنة الأساس"},
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


# --- lecture des séries ------------------------------------------------------------------

def _communes() -> dict[str, dict[tuple[str, int], tuple[float, str]]]:
    """{source: {(variable, année): (valeur, statut)}} ; source ∈ dgct, somme."""
    d = figtools.series(SERIE_COMMUNES)
    noms = {"dgct_agregats": "dgct", "somme_communes": "somme"}
    out: dict = {"dgct": {}, "somme": {}}
    for r in d.itertuples(index=False):
        out[noms[r.source]][(r.variable, int(r.annee))] = (float(r.valeur), str(r.statut))
    return out


def _bm2014() -> dict[tuple[str, int], float]:
    d = figtools.series(SERIE_BM2014)
    return {(r.variable, int(r.annee)): float(r.valeur_md) for r in d.itertuples(index=False)}


def _bm1992() -> dict[tuple[str, int], float]:
    d = figtools.series(SERIE_BM1992)
    return {(r.variable, int(r.annee)): float(r.valeur) for r in d.itertuples(index=False)}


def _bm1997() -> dict[tuple[str, int], float]:
    d = figtools.series(SERIE_BM1997)
    return {(r.variable, int(r.annee)): float(r.valeur_md) for r in d.itertuples(index=False)}


def _fccl_lf() -> dict[int, tuple[float, str]]:
    """{année: (montant voté du fonds entier en MD, grandeur)} — lois de finances, 1976-1995.

    1976-1986 : la colonne « Recettes » (égale à « Dépenses »), évaluation des recettes
    affectées. 1987-1995 : le « Total des recettes » (égal à « Dépenses »), que la fiche de
    la série désigne comme le total du fonds — subvention du budget et recettes propres —,
    et non la seule subvention. Les années sans valeur (1979, 1996 et suivantes) sont omises.
    """
    d = figtools.series(SERIE_FCCL_LF)
    d = d[(d["ligne"] == "fccl") & d["valeur_md"].notna()]
    retenue = {"avant_1987_parts_d_impots": ("recettes", "fccl_vote_parts"),
               "depuis_1987_subvention_du_budget": ("total_recettes", "fccl_vote_total")}
    out = {}
    for r in d.itertuples(index=False):
        grandeur, cle = retenue.get(r.regime, (None, None))
        if r.grandeur == grandeur:
            out[int(r.annee)] = (float(r.valeur_md), cle)
    return out


def _base(texte) -> int:
    return int(str(texte).split()[-1])


def _pib() -> dict[int, tuple[float, int]]:
    """{année: (PIB en MD, base)} : l'édition la plus récente qui porte l'année."""
    d = figtools.series(SERIE_PIB).copy()
    d["fin"] = d["edition"].str[-4:].astype(int)
    d = d.sort_values("fin").groupby("annee").last()
    return {int(a): (float(r.valeur), _base(r.base)) for a, r in d.iterrows()}


def _pib_par_base() -> dict[tuple[int, int], float]:
    """{(année, base): PIB} : l'édition la plus récente de chaque base qui porte l'année."""
    d = figtools.series(SERIE_PIB).copy()
    d["fin"] = d["edition"].str[-4:].astype(int)
    d["b"] = d["base"].map(_base)
    d = d.sort_values("fin").groupby(["annee", "b"]).last()
    return {(int(a), int(b)): float(r.valeur) for (a, b), r in d.iterrows()}


def _ruptures_pib(annees) -> list[tuple[int, int]]:
    """Années où la base du PIB change, dans l'intervalle tracé : [(année, nouvelle base)]."""
    p = _pib()
    ans = sorted(a for a in annees if a in p)
    return [(a, p[a][1]) for a0, a in zip(ans, ans[1:]) if p[a][1] != p[a0][1]]


# --- tracé générique ---------------------------------------------------------------------

def _courbe(ax, points, couleur, source, libelle, mesure, dec=1, creux=()):
    """Trace une courbe année → valeur ; `None` interrompt le trait. Un point par appel,
    pour qu'il porte son infobulle."""
    st = STYLE_SOURCE[source]
    ans = sorted(points)
    ys = [points[a] for a in ans]
    xs, yy = [], []
    for a, y in zip(ans, ys):  # trait interrompu par les cases vides
        xs.append(a)
        yy.append(float("nan") if y is None else y)
    ax.plot(xs, yy, ls=st["ls"], lw=st["lw"], color=couleur, zorder=2)
    for a, y in zip(ans, ys):
        if y is None:
            continue
        p, = ax.plot([a], [y], st["marker"], ms=st["ms"], color=couleur,
                     mfc="white" if a in creux else couleur, zorder=3)
        texte = f"{a} · {libelle} — {_lab('src_' + source)} : {_nombre(y, dec)}{_unite(mesure)}"
        if a in creux:
            texte += f" ({_lab('provisoire')})"
        figtools.infobulle(p, texte)


def _legende_sources(sources) -> list:
    return [Line2D([], [], color=GRIS, marker=STYLE_SOURCE[s]["marker"],
                   ls=STYLE_SOURCE[s]["ls"], ms=4, lw=1.2,
                   label=figtools.fig_text(_lab("src_" + s))) for s in sources]


def _legende_grandeurs(paires) -> list:
    return [Line2D([], [], color=c, lw=2.5, label=figtools.fig_text(_lab(k)))
            for k, c in paires]


def _cadre(ax, titre, ylabel, x0, x1):
    ax.set_title(figtools.fig_text(titre), fontsize=10.5)
    ax.set_ylabel(figtools.fig_text(ylabel))
    ax.set_xlabel(figtools.fig_text(_lab("x")))
    ax.set_xlim(x0 - 0.8, x1 + 0.8)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.grid(True, alpha=0.3)


def _ruptures(ax, mesure, annees, communes=True, fccl=False):
    x0, x1 = min(annees), max(annees)
    if communes and x0 < RUPTURE_COMMUNES <= x1:
        figtools.marque_rupture(ax, RUPTURE_COMMUNES, _ft("rup_communes"))
    if fccl and x0 < RUPTURE_FCCL_1987 <= x1:
        figtools.marque_rupture(ax, RUPTURE_FCCL_1987, _ft("rup_fccl_1987"))
    if fccl and x0 < RUPTURE_FCCL <= x1:
        figtools.marque_rupture(ax, RUPTURE_FCCL, _ft("rup_fccl"))
    if mesure == "pib":
        # Le libellé des changements de base va en bas du cadre : en haut, il chevaucherait
        # celui des communes (base 2015 en 2015, décrets de 2016).
        for a, b in _ruptures_pib(annees):
            figtools.marque_rupture(ax, a)
            ax.annotate(_ft("rup_pib", b=b), xy=(a - 0.5, 0), xycoords=("data", "axes fraction"),
                        xytext=(-4, 4), textcoords="offset points", ha="right", va="bottom",
                        fontsize=7, color=GRIS)


def _creux(c: dict, source: str) -> set[int]:
    return {a for (_, a), (_, st) in c[source].items() if st != "definitif"}


# --- 1. Recettes de fonctionnement : propres et transferts -------------------------------

def _ressources() -> list[dict]:
    """Lignes (source, année, recettes T1, transferts, recettes propres, statut)."""
    c = _communes()
    lignes = []
    for a in range(2008, 2020):
        g = lambda v: c["dgct"][(v, a)][0]  # noqa: E731
        t = g("fccl_communes") + g("dotation_exceptionnelle_communes")
        lignes.append(dict(source="dgct", annee=a, r1=g("recettes_t1"), t=t,
                           p=g("recettes_t1") - t, statut="definitif"))
    for a in range(2018, 2024):
        r1, st = c["somme"][("recettes_t1", a)]
        t = c["somme"][("transferts_etat_fonctionnement", a)][0]
        lignes.append(dict(source="somme", annee=a, r1=r1, t=t, p=r1 - t, statut=st))
    b = _bm2014()
    for a in range(2002, 2013):
        t = b[("fccl", a)] + b[("transferts_exceptionnels", a)]
        lignes.append(dict(source="bm2014", annee=a, r1=b[("recettes_t1", a)], t=t,
                           p=b[("ressources_propres", a)], statut="publie"))
    b = _bm1997()
    for a in (1990, 1992, 1994, 1995, 1996):
        lignes.append(dict(source="bm1997", annee=a, r1=b[("total_recettes", a)],
                           t=b[("fccl", a)], p=b[("total_ressources_propres", a)],
                           statut="publie"))
    return lignes


def table_ressources():
    import pandas as pd
    pib = _pib()
    rows = []
    for l in _ressources():
        for k in ("p", "t"):
            v = l[k]
            rows.append({
                _lab("col_annee"): l["annee"],
                _lab("col_grandeur"): _lab("propres" if k == "p" else "transferts"),
                _lab("col_source"): _lab("src_" + l["source"]),
                _lab("col_md"): round(v, 1),
                _lab("col_pct_r1"): round(100 * v / l["r1"], 1),
                _lab("col_pct_pib"): (round(100 * v / pib[l["annee"]][0], 2)
                                      if l["annee"] in pib else None),
                _lab("col_statut"): l["statut"],
            })
    return pd.DataFrame(rows)


def fig_ressources(mesure: str = "md"):
    figtools.apply_lang_font()
    pib = _pib()
    lignes = _ressources()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    sources = ["bm1997", "bm2014", "dgct", "somme"]
    creux = {s: {l["annee"] for l in lignes if l["source"] == s
                 and l["statut"] not in ("definitif", "publie")} for s in sources}
    for s in sources:
        ls = [l for l in lignes if l["source"] == s]
        if mesure == "md":
            paires = (("p", BLEU, "propres"), ("t", ORANGE, "transferts"))
            for k, coul, lib in paires:
                _courbe(ax, {l["annee"]: l[k] for l in ls}, coul, s, _lab(lib), mesure,
                        creux=creux[s])
        elif mesure == "r1":
            _courbe(ax, {l["annee"]: 100 * l["t"] / l["r1"] for l in ls}, ORANGE, s,
                    _lab("part_transferts"), mesure, creux=creux[s])
        else:
            pts = {l["annee"]: l for l in ls if l["annee"] in pib}
            if not pts:
                continue
            for k, coul, lib in (("p", BLEU, "propres"), ("t", ORANGE, "transferts")):
                _courbe(ax, {a: 100 * l[k] / pib[a][0] for a, l in pts.items()}, coul, s,
                        _lab(lib), mesure, dec=2, creux=creux[s])
    annees = sorted({l["annee"] for l in lignes if mesure != "pib" or l["annee"] in pib})
    ylabel = {"md": "md", "r1": "pct_r1", "pib": "pct_pib"}[mesure]
    _cadre(ax, _lab("t_ressources"), _lab(ylabel), annees[0], annees[-1])
    if mesure == "r1":
        ax.set_ylim(0, 60)
    _ruptures(ax, mesure, annees)
    src = [s for s in sources if mesure != "pib" or s != "bm1997"]
    poignees = (_legende_grandeurs([("propres", BLEU), ("transferts", ORANGE)])
                if mesure != "r1" else _legende_grandeurs([("part_transferts", ORANGE)]))
    poignees += _legende_sources(src)
    poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", ls="",
                           label=figtools.fig_text(_lab("lg_creux"))))
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2,
              fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig


def vues_ressources():
    return [(_lab("vue_md"), fig_ressources("md")), (_lab("vue_r1"), fig_ressources("r1")),
            (_lab("vue_pib"), fig_ressources("pib"))]


# --- 2. Autonomie financière -------------------------------------------------------------

def _autonomie() -> list[dict]:
    c = _communes()
    lignes = []
    for a in range(2008, 2020):
        lignes.append(dict(grandeur="ratio_dgct", source="dgct", annee=a,
                           v=100 * c["dgct"][("ratio_autonomie_financiere", a)][0],
                           statut="definitif"))
    for l in _ressources():
        lignes.append(dict(grandeur="a1", source=l["source"], annee=l["annee"],
                           v=100 * l["p"] / l["r1"], statut=l["statut"]))
    for a in range(2018, 2024):
        s = c["somme"]
        r1, st = s[("recettes_t1", a)]
        p = r1 - s[("transferts_etat_fonctionnement", a)][0]
        q = r1 + s[("subventions_equipement", a)][0] + s[("credits_transferes", a)][0]
        lignes.append(dict(grandeur="a", source="somme", annee=a, v=100 * p / q, statut=st))
    return lignes


def table_autonomie():
    import pandas as pd
    return pd.DataFrame([{
        _lab("col_annee"): l["annee"], _lab("col_grandeur"): _lab(l["grandeur"]),
        _lab("col_source"): _lab("src_" + l["source"]), _lab("col_pct"): round(l["v"], 1),
        _lab("col_statut"): l["statut"]} for l in _autonomie()])


def fig_autonomie():
    figtools.apply_lang_font()
    lignes = _autonomie()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    couleurs = {"ratio_dgct": GRIS, "a1": BLEU, "a": VERT}
    for g in ("ratio_dgct", "a1", "a"):
        for s in ("bm1997", "bm2014", "dgct", "somme"):
            ls = [l for l in lignes if l["grandeur"] == g and l["source"] == s]
            if ls:
                creux = {l["annee"] for l in ls if l["statut"] not in ("definitif", "publie")}
                _courbe(ax, {l["annee"]: l["v"] for l in ls}, couleurs[g], s, _lab(g), "pct",
                        creux=creux)
    annees = sorted({l["annee"] for l in lignes})
    _cadre(ax, _lab("t_autonomie"), _lab("pct"), annees[0], annees[-1])
    ax.set_ylim(0, 100)
    _ruptures(ax, "pct", annees)
    poignees = _legende_grandeurs([("ratio_dgct", GRIS), ("a1", BLEU), ("a", VERT)])
    poignees += _legende_sources(["bm1997", "bm2014", "dgct", "somme"])
    poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", ls="",
                           label=figtools.fig_text(_lab("lg_creux"))))
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2,
              fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig


# --- 3. Impôts locaux --------------------------------------------------------------------

IMPOTS = (("tcl", VIOLET), ("tib", BLEU), ("tnb", VERT), ("taxe_hoteliere", BRUN))
# Les deux vues par chapitre : le budgétaire seul (agrégats de la DGCT, somme des budgets par
# commune), sans les points du rapport de la Banque mondiale de 1997, qui restent dans la figure
# à quatre impôts de la longue période.
IMPOTS_IMMEUBLES = (("tib", BLEU), ("tnb", VERT))
IMPOTS_ACTIVITE = (("tcl", VIOLET), ("taxe_hoteliere", BRUN))
SOURCES_IMPOTS = ("bm1997", "dgct", "somme")
SOURCES_BUDGETAIRES = ("dgct", "somme")

# Textes marqués sur les figures des chapitres d'impôts : (année, libellé, hauteur du libellé
# en fraction du cadre). La marque situe un texte dans la série ; elle ne dit pas une cause.
# Le trait s'arrête à la hauteur de son libellé, sous ceux des ruptures de série, posés en haut
# du cadre ; un libellé proche du bord droit, ou qui recouvrirait le libellé précédent, passe
# à gauche du trait.
#   - immeubles : abandons d'arriérés de la loi de finances complémentaire pour 2012 (art. 17)
#     et de la loi de finances pour 2019 (art. 72) ; barèmes relevés au 1er janvier 2017
#     (décrets gouvernementaux n° 2017-396 et 2017-397) ;
#   - activité : fin du maximum annuel au 1er janvier 2012 (loi de finances complémentaire pour
#     2012, art. 50) ; assiette étendue au 1er janvier 2014 (loi de finances pour 2014,
#     art. 49 et 50).
MARQUES_IMMEUBLES = ((2012, "mq_abandon_2012", 0.86), (2017, "mq_baremes_2017", 0.86),
                     (2019, "mq_abandon_2019", 0.9))
# La figure du recouvrement s'arrête en 2019 : le libellé de 2019 passe à gauche de son trait,
# donc plus bas que celui de 2017.
MARQUES_RECOUVREMENT = ((2012, "mq_abandon_2012", 0.86), (2017, "mq_baremes_2017", 0.86),
                        (2019, "mq_abandon_2019", 0.68))
MARQUES_ACTIVITE = ((2012, "mq_plafond_2012", 0.97), (2014, "mq_assiette_2014", 0.88))


def _impots() -> list[dict]:
    c = _communes()
    lignes = []
    for a in range(2008, 2024):
        src = "dgct" if a <= 2019 else "somme"
        r1, st = c[src][("recettes_t1", a)]
        for k, _ in IMPOTS:
            v = c[src].get((k, a))
            lignes.append(dict(impot=k, source=src, annee=a, v=None if v is None else v[0],
                               r1=r1, statut=st))
    b = _bm1997()
    for a in (1990, 1992, 1994, 1995, 1996):
        for k in ("tcl", "taxe_hoteliere"):
            lignes.append(dict(impot=k, source="bm1997", annee=a, v=b[(k, a)],
                               r1=b[("total_recettes", a)], statut="publie"))
    return lignes


def _impots_retenus(impots=IMPOTS, sources=SOURCES_IMPOTS) -> list[dict]:
    """Les lignes de `_impots()` pour un sous-ensemble d'impôts et de sources."""
    cles = {k for k, _ in impots}
    return [l for l in _impots() if l["impot"] in cles and l["source"] in sources]


def _lignes_recouvrement() -> list[dict]:
    c = _communes()
    return [{
        _lab("col_annee"): a, _lab("col_grandeur"): _lab("recouvrement_tib"),
        _lab("col_source"): _lab("src_dgct"),
        _lab("col_pct"): round(100 * c["dgct"][("taux_recouvrement_tib", a)][0])}
        for a in range(2008, 2020)]


def table_impots(impots=IMPOTS, sources=SOURCES_IMPOTS, recouvrement=True, base_pib=False):
    """Données de la figure des impôts. `recouvrement` place en tête le taux de recouvrement
    publié de la TIB (figure d'origine, à quatre vues) ; `base_pib` ajoute la base des comptes
    nationaux du PIB employé, année par année."""
    import pandas as pd
    pib = _pib()
    lignes = []
    for l in _impots_retenus(impots, sources):
        ligne = {
            _lab("col_annee"): l["annee"], _lab("col_grandeur"): _lab(l["impot"]),
            _lab("col_source"): _lab("src_" + l["source"]),
            _lab("col_md"): None if l["v"] is None else round(l["v"], 1),
            _lab("col_pct_r1"): None if l["v"] is None else round(100 * l["v"] / l["r1"], 1),
            _lab("col_pct_pib"): (None if l["v"] is None or l["annee"] not in pib
                                  else round(100 * l["v"] / pib[l["annee"]][0], 3))}
        if base_pib:
            ligne[_lab("col_base")] = (pib[l["annee"]][1]
                                       if l["v"] is not None and l["annee"] in pib else None)
        ligne[_lab("col_statut")] = l["statut"]
        lignes.append(ligne)
    return pd.DataFrame((_lignes_recouvrement() if recouvrement else []) + lignes)


def _marques_textes(ax, marques, x0, x1):
    """Marque des textes du chapitre sur une figure : trait plein fin (les ruptures de série
    gardent le pointillé de `figtools.marque_rupture`), libellé à la hauteur donnée."""
    for annee, cle, hauteur in marques:
        if not x0 < annee <= x1:
            continue
        trait = figtools.marque_rupture(ax, annee)
        trait.set_linestyle("-")
        trait.set_linewidth(0.8)
        trait.set_color(ROUGE)
        trait.set_alpha(0.55)
        trait.set_ydata([0, hauteur + 0.01])
        figtools.infobulle(trait, _lab(cle).replace("\n", " "))
        gauche = annee - 0.5 > x1 - 2  # près du bord droit : libellé à gauche du trait
        ax.annotate(_ft(cle), xy=(annee - 0.5, hauteur), xycoords=("data", "axes fraction"),
                    xytext=(-4 if gauche else 4, 0), textcoords="offset points",
                    ha="right" if gauche else "left", va="top", fontsize=7, color=ROUGE)


def _legende_marques() -> Line2D:
    return Line2D([], [], color=ROUGE, lw=0.8, alpha=0.55,
                  label=figtools.fig_text(_lab("lg_marque_texte")))


def fig_impots(mesure: str = "md", impots=IMPOTS, sources=SOURCES_IMPOTS,
               titre: str = "t_impots", marques=()):
    figtools.apply_lang_font()
    pib = _pib()
    lignes = _impots_retenus(impots, sources)
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    tracees = []
    for k, coul in impots:
        for s in sources:
            ls = [l for l in lignes if l["impot"] == k and l["source"] == s]
            if not ls:
                continue
            if s == "dgct":  # le trait DGCT se prolonge jusqu'à la somme des communes
                ls = ls + [dict(annee=a, v=None, r1=1, statut="") for a in (2020, 2021)]
            pts = {}
            for l in ls:
                if l["v"] is None:
                    pts[l["annee"]] = None
                elif mesure == "md":
                    pts[l["annee"]] = l["v"]
                elif mesure == "r1":
                    pts[l["annee"]] = 100 * l["v"] / l["r1"]
                elif l["annee"] in pib:
                    pts[l["annee"]] = 100 * l["v"] / pib[l["annee"]][0]
            if pts:
                creux = {l["annee"] for l in ls if l["statut"] not in ("definitif", "publie", "")}
                _courbe(ax, pts, coul, s, _lab(k), mesure, dec=3 if mesure == "pib" else 1,
                        creux=creux)
                if s not in tracees and any(v is not None for v in pts.values()):
                    tracees.append(s)
    annees = sorted({l["annee"] for l in lignes if mesure != "pib" or l["annee"] in pib})
    ylabel = {"md": "md", "r1": "pct_r1", "pib": "pct_pib"}[mesure]
    _cadre(ax, _lab(titre), _lab(ylabel), annees[0], annees[-1])
    if marques:  # de la place en haut du cadre pour les libellés des textes
        ax.set_ylim(0, ax.get_ylim()[1] * 1.3)
    _ruptures(ax, mesure, annees)
    _marques_textes(ax, marques, annees[0], annees[-1])
    poignees = _legende_grandeurs(impots)
    poignees += _legende_sources([s for s in sources if s in tracees])
    poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", ls="",
                           label=figtools.fig_text(_lab("lg_creux"))))
    if marques:
        poignees.append(_legende_marques())
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2,
              fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig


def fig_recouvrement_tib(marques=()):
    """Le « taux de recouvrement » de la TIB tel que la DGCT le publie, sans définition."""
    figtools.apply_lang_font()
    c = _communes()
    pts = {a: 100 * c["dgct"][("taux_recouvrement_tib", a)][0] for a in range(2008, 2020)}
    fig, ax = plt.subplots(figsize=(9.5, 4.6))
    _courbe(ax, pts, BLEU, "dgct", _lab("recouvrement_tib"), "pct", dec=0)
    _cadre(ax, _lab("t_recouvrement"), _lab("pct"), 2008, 2019)
    ax.set_ylim(0, 40 if marques else 30)
    _ruptures(ax, "pct", list(pts))
    _marques_textes(ax, marques, 2008, 2019)
    poignees = _legende_grandeurs([("recouvrement_tib", BLEU)]) + _legende_sources(["dgct"])
    if marques:
        poignees.append(_legende_marques())
    ax.legend(handles=poignees, loc="upper center",
              bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig


def table_recouvrement_tib():
    import pandas as pd
    return pd.DataFrame(_lignes_recouvrement())


def vues_impots(impots=IMPOTS, sources=SOURCES_IMPOTS, recouvrement=True,
                titre: str = "t_impots", marques=()):
    """Les vues de la figure des impôts : millions de dinars, part des recettes de
    fonctionnement, % du PIB — et, si `recouvrement`, le taux de recouvrement publié de la
    TIB. Sans argument : la figure d'origine, à quatre impôts et quatre vues."""
    vues = [(_lab("vue_md"), fig_impots("md", impots, sources, titre, marques)),
            (_lab("vue_r1"), fig_impots("r1", impots, sources, titre, marques)),
            (_lab("vue_pib"), fig_impots("pib", impots, sources, titre, marques))]
    if recouvrement:
        vues.append((_lab("vue_recouvrement"), fig_recouvrement_tib()))
    return vues


# Chapitre des impôts sur les immeubles : `fig-fl-immeubles-rendement` et
# `fig-fl-immeubles-recouvrement`.

def vues_immeubles_rendement():
    return vues_impots(IMPOTS_IMMEUBLES, SOURCES_BUDGETAIRES, recouvrement=False,
                       titre="t_immeubles_rendement", marques=MARQUES_IMMEUBLES)


def table_immeubles_rendement():
    return table_impots(IMPOTS_IMMEUBLES, SOURCES_BUDGETAIRES, recouvrement=False,
                        base_pib=True)


def fig_immeubles_recouvrement():
    return fig_recouvrement_tib(marques=MARQUES_RECOUVREMENT)


# Chapitre des impôts sur l'activité : `fig-fl-activite-rendement` (à insérer à la conversion
# du chapitre). Sans la série `finances-locales-bm-1997`.

def vues_activite_rendement():
    return vues_impots(IMPOTS_ACTIVITE, SOURCES_BUDGETAIRES, recouvrement=False,
                       titre="t_activite_rendement", marques=MARQUES_ACTIVITE)


def table_activite_rendement():
    return table_impots(IMPOTS_ACTIVITE, SOURCES_BUDGETAIRES, recouvrement=False,
                        base_pib=True)


# --- 4. Fonds commun ---------------------------------------------------------------------

FCCL_DGCT = (("fccl_credit_global", ROUGE), ("fccl_communes", ORANGE),
             ("fccl_regions", VERT), ("fccl_reserve", GRIS))
# Texte placé à sa date d'effet sur la figure du fonds (trait rouge plein) : la révision des
# critères (loi de finances pour 2014, art. 12). Il situe ce texte ; il ne dit pas une cause.
# La fin des parts d'impôts (loi de finances pour 1987, art. 92) n'est plus une simple marque
# de texte : c'est une rupture de définition de la série votée (`RUPTURE_FCCL_1987`).
MARQUES_FCCL = ((2014, "mq_fccl_2014", 0.84),)
VOTE = VIOLET


def _fccl() -> list[dict]:
    c = _communes()
    lignes = []
    # Montants votés, 1976-1995 : deux grandeurs, une par définition, donc deux courbes que
    # rien ne relie. Aucun PIB n'est attaché : voir `fig_fccl`.
    for a, (v, g) in sorted(_fccl_lf().items()):
        lignes.append(dict(grandeur=g, source="lf", annee=a, v=v, statut="vote"))
    for a in range(2008, 2020):
        for k, _ in FCCL_DGCT:
            # 2018-2019 : même colonne de la source, autre grandeur (voir RUPTURE_FCCL).
            g = k if a < RUPTURE_FCCL else k.replace("fccl_", "sub_")
            lignes.append(dict(grandeur=g, source="dgct", annee=a, v=c["dgct"][(k, a)][0],
                               statut="definitif"))
    for a in (2022, 2023):
        s = c["somme"]
        v = s[("dotation_annuelle_fonctionnement", a)][0] + \
            s[("dotation_annuelle_investissement", a)][0]
        lignes.append(dict(grandeur="dotation_annuelle", source="somme", annee=a, v=v,
                           statut=s[("recettes_t1", a)][1]))
    b = _bm2014()
    for a in range(2002, 2013):
        lignes.append(dict(grandeur="fccl_bm", source="bm2014", annee=a, v=b[("fccl", a)],
                           statut="publie"))
    b = _bm1997()
    for a in (1990, 1992, 1994, 1995, 1996):
        lignes.append(dict(grandeur="fccl_bm", source="bm1997", annee=a, v=b[("fccl", a)],
                           statut="publie"))
    b = _bm1992()
    for a in range(1985, 1992):
        lignes.append(dict(grandeur="fccl_bm", source="bm1992", annee=a, v=b[("fccl", a)],
                           statut="publie", pib=b[("pib", a)]))
    return lignes


def _pib_ligne(l, pib):
    if "pib" in l:
        return l["pib"]
    # Les montants votés de 1976-1995 n'ont pas de vue au PIB : les comptes de la nation lus
    # ici commencent en 2001, et avant 1992 le seul PIB courant disponible est d'une base non
    # dite. On ne rapporte pas une série budgétaire à un dénominateur sans base.
    if l["source"] == "lf":
        return None
    return pib[l["annee"]][0] if l["annee"] in pib else None


def table_fccl():
    import pandas as pd
    pib = _pib()
    rows = []
    for l in _fccl():
        p = _pib_ligne(l, pib)
        rows.append({_lab("col_annee"): l["annee"], _lab("col_grandeur"): _lab(l["grandeur"]),
                     _lab("col_source"): _lab("src_" + l["source"]),
                     _lab("col_md"): round(l["v"], 1),
                     _lab("col_pct_pib"): None if p is None else round(100 * l["v"] / p, 3),
                     _lab("col_statut"): l["statut"]})
    return pd.DataFrame(rows)


def fig_fccl(mesure: str = "md"):
    figtools.apply_lang_font()
    pib = _pib()
    lignes = _fccl()
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    couleurs = dict(FCCL_DGCT, fccl_bm=ORANGE, dotation_annuelle=BLEU,
                    fccl_vote_parts=VOTE, fccl_vote_total=VOTE)
    couleurs.update({k.replace("fccl_", "sub_"): c for k, c in FCCL_DGCT})
    for (g, s) in dict.fromkeys((l["grandeur"], l["source"]) for l in lignes):
        ls = [l for l in lignes if l["grandeur"] == g and l["source"] == s]
        pts = {}
        for l in ls:
            if mesure == "md":
                pts[l["annee"]] = l["v"]
            else:
                p = _pib_ligne(l, pib)
                if p is not None:
                    pts[l["annee"]] = 100 * l["v"] / p
        if pts:
            creux = {l["annee"] for l in ls
                     if l["statut"] not in ("definitif", "publie", "vote")}
            if s == "lf":  # une année sans valeur (1979) interrompt le trait
                pts.update({a: None for a in range(min(pts), max(pts)) if a not in pts})
            # Les deux années DGCT qui suivent la suppression du fonds : autre grandeur,
            # tracée à part (jamais reliée à 2017) et en points creux.
            if s == "dgct":
                creux |= {a for a in pts if a >= RUPTURE_FCCL}
            _courbe(ax, pts, couleurs[g], s, _lab(g), mesure, dec=3 if mesure == "pib" else 1,
                    creux=creux)
    annees = sorted({l["annee"] for l in lignes
                     if mesure == "md" or _pib_ligne(l, pib) is not None})
    _cadre(ax, _lab("t_fccl"), _lab("md" if mesure == "md" else "pct_pib"),
           annees[0], annees[-1])
    _ruptures(ax, mesure, annees, communes=False, fccl=True)
    ax.set_ylim(0, ax.get_ylim()[1] * 1.18)  # de la place en haut pour les libellés
    _marques_textes(ax, MARQUES_FCCL, annees[0], annees[-1])
    vote = mesure == "md"  # la série votée n'a pas de vue au PIB
    if vote:  # le trou de 1996-2007 est dit sur la figure, là où il se voit
        ax.annotate(_ft("lg_absence_fccl").replace(" : ", " :\n"), xy=(2001.5, 0.30),
                    xycoords=("data", "axes fraction"), ha="center", va="center",
                    fontsize=7, color=GRIS, style="italic")
    poignees = _legende_grandeurs(([("fccl_vote", VOTE)] if vote else []) + list(FCCL_DGCT)
                                  + [("fccl_bm", ORANGE), ("dotation_annuelle", BLEU)])
    poignees += _legende_sources(["lf", "bm1992", "bm1997", "bm2014", "dgct", "somme"]
                                 if vote else ["bm1992", "bm2014", "dgct", "somme"])
    poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", ls="",
                           label=figtools.fig_text(_lab("lg_creux_fccl"))))
    poignees.append(_legende_marques())
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2,
              fontsize=7.2, frameon=False)
    fig.tight_layout()
    return fig


def vues_fccl():
    return [(_lab("vue_md"), fig_fccl("md")), (_lab("vue_pib"), fig_fccl("pib"))]


# --- 5. CPSCL ----------------------------------------------------------------------------

CPSCL_FLUX = (("dotations_recues_etat", BLEU), ("subventions_accordees_cl", ORANGE),
              ("prets_accordes_cl", VIOLET), ("remboursements_prets", VERT))
CPSCL_IMPAYES = (("annuites_echues_impayees", ROUGE), ("provisions_impayes", GRIS))


def _cpscl() -> dict[tuple[str, int], float]:
    d = figtools.series(SERIE_CPSCL)
    d = d[d["retenu"].astype(str) == "True"]
    return {(r.poste, int(r.exercice)): float(r.valeur_md) for r in d.itertuples(index=False)}


def table_cpscl():
    import pandas as pd
    c = _cpscl()
    rows = []
    for k, _ in CPSCL_FLUX + CPSCL_IMPAYES:
        for a in range(2005, 2025):
            if (k, a) in c:
                rows.append({_lab("col_annee"): a, _lab("col_grandeur"): _lab(k),
                             _lab("col_md"): round(c[(k, a)], 3)})
    return pd.DataFrame(rows)


def fig_cpscl(vue: str = "flux"):
    """Valeurs absolues : la page porte les décaissements et les provisions en négatif."""
    figtools.apply_lang_font()
    c = _cpscl()
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    paires = CPSCL_FLUX if vue == "flux" else CPSCL_IMPAYES
    for k, coul in paires:
        pts = {a: abs(c[(k, a)]) for a in range(2005, 2025) if (k, a) in c}
        st = STYLE_SOURCE["dgct"]
        ans = sorted(pts)
        ax.plot(ans, [pts[a] for a in ans], ls="-", lw=1.8, color=coul)
        for a in ans:
            p, = ax.plot([a], [pts[a]], "o", ms=st["ms"], color=coul)
            figtools.infobulle(p, f"{a} · {_lab(k)} : {_nombre(pts[a])} MD")
    _cadre(ax, _lab("t_cpscl"), _lab("md"), 2005, 2024)
    ax.set_ylim(bottom=0)
    ax.legend(handles=_legende_grandeurs(paires), loc="upper left", fontsize=8)
    fig.tight_layout()
    return fig


def vues_cpscl():
    return [(_lab("vue_flux"), fig_cpscl("flux")), (_lab("vue_impayes"), fig_cpscl("impayes"))]


# --- 6. Comptes de la nation -------------------------------------------------------------

INS_POSTES = (("epargnebrute", BLEU, ("epargnebrute",)),
              ("fbcf", ORANGE, ("formationbrutedecapitalefixe", "formationbrutedecapitalfixe")))


def _ins() -> list[dict]:
    d = figtools.series(SERIE_INS)
    d = d[d["cote"] == "emplois"]
    lignes = []
    for g, _, postes in INS_POSTES:
        s = d[d["poste"].isin(postes)]
        for r in s.itertuples(index=False):
            lignes.append(dict(grandeur=g, base=int(r.base), annee=int(r.annee),
                               v=float(r.valeur_md), statut=str(r.statut)))
    return lignes


def table_ins():
    import pandas as pd
    pib = _pib_par_base()
    rows = []
    for l in sorted(_ins(), key=lambda l: (l["grandeur"], l["base"], l["annee"])):
        p = pib.get((l["annee"], l["base"]))
        rows.append({_lab("col_annee"): l["annee"], _lab("col_grandeur"): _lab(l["grandeur"]),
                     _lab("col_base"): l["base"], _lab("col_md"): round(l["v"], 1),
                     _lab("col_pct_pib"): None if p is None else round(100 * l["v"] / p, 3),
                     _lab("col_statut"): l["statut"]})
    return pd.DataFrame(rows)


def fig_ins(mesure: str = "md"):
    figtools.apply_lang_font()
    pib = _pib_par_base()
    lignes = _ins()
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    for g, coul, _ in INS_POSTES:
        for b, ls in STYLE_BASE.items():
            pts = {}
            for l in lignes:
                if l["grandeur"] != g or l["base"] != b:
                    continue
                if mesure == "md":
                    pts[l["annee"]] = (l["v"], l["statut"])
                elif (l["annee"], b) in pib:
                    pts[l["annee"]] = (100 * l["v"] / pib[(l["annee"], b)], l["statut"])
            ans = sorted(pts)
            if not ans:
                continue
            ax.plot(ans, [pts[a][0] for a in ans], ls=ls, lw=1.7, color=coul)
            for a in ans:
                v, st = pts[a]
                p, = ax.plot([a], [v], "o", ms=4, color=coul,
                             mfc=coul if st == "definitif" else "white")
                figtools.infobulle(p, f"{a} · {_lab(g)}, {_lab('base', b=b)} : "
                                      f"{_nombre(v, 3 if mesure == 'pib' else 1)}"
                                      f"{_unite(mesure)} ({st})")
    annees = sorted({l["annee"] for l in lignes})
    _cadre(ax, _lab("t_ins"), _lab("md" if mesure == "md" else "pct_pib"),
           annees[0], annees[-1])
    poignees = _legende_grandeurs([(g, c) for g, c, _ in INS_POSTES])
    poignees += [Line2D([], [], color=GRIS, ls=ls, lw=1.5,
                        label=figtools.fig_text(_lab("base", b=b)))
                 for b, ls in STYLE_BASE.items()]
    poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", ls="",
                           label=figtools.fig_text(_lab("lg_creux_ins"))))
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=3,
              fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig


def vues_ins():
    return [(_lab("vue_md"), fig_ins("md")), (_lab("vue_pib"), fig_ins("pib"))]


# --- 7. Dépenses, rémunérations et service de la dette (chapitre des budgets) --------------
#
# Deux textes du chapitre sont placés à leur date d'effet (trait rouge plein) : la refonte de
# 2007, qui s'applique aux budgets de 2008, et le code de 2018, dont les règles budgétaires
# s'appliquent aux communes à partir des budgets de 2019. Ils situent ces textes ; ils ne
# disent pas une cause.
MARQUES_BUDGETS = ((2008, "mq_budg_2008", 0.97), (2019, "mq_budg_2019", 0.80))
# Le plafond des rémunérations (code de 2018, art. 135) porte sur les PRÉVISIONS et se
# rapporte aux recettes du titre I de l'ANNÉE ÉCOULÉE. Les séries sont des réalisations : la
# ligne des 50 % est un repère, tracé de 2019 seulement, non un constat de respect.
PLAFOND_REMUNERATIONS = 50.0
ANNEE_CCL_BUDGETS = 2019


def _remunerations() -> list[dict]:
    """Trois ratios, jamais fusionnés : le ratio publié ; rémunérations / recettes du titre I
    de la même année ; rémunérations / recettes du titre I de l'année précédente."""
    c = _communes()
    lignes = []
    for a in range(2008, 2020):
        d = c["dgct"]
        lignes.append(dict(grandeur="rem_ratio_dgct", source="dgct", annee=a,
                           v=100 * d[("ratio_remunerations", a)][0], statut="definitif"))
        lignes.append(dict(grandeur="rem_meme_annee", source="dgct", annee=a,
                           v=100 * d[("remunerations", a)][0] / d[("recettes_t1", a)][0],
                           statut="definitif"))
        if ("recettes_t1", a - 1) in d:
            lignes.append(dict(grandeur="rem_annee_prec", source="dgct", annee=a,
                               v=100 * d[("remunerations", a)][0] / d[("recettes_t1", a - 1)][0],
                               statut="definitif"))
    s = c["somme"]
    for a in sorted(a for (v, a) in s if v == "remunerations"):
        rem, st = s[("remunerations", a)]
        r1, st1 = s[("recettes_t1", a)]
        lignes.append(dict(grandeur="rem_meme_annee", source="somme", annee=a,
                           v=100 * rem / r1, statut=st if st != "definitif" else st1))
        if ("recettes_t1", a - 1) in s:
            r0, st0 = s[("recettes_t1", a - 1)]
            lignes.append(dict(grandeur="rem_annee_prec", source="somme", annee=a,
                               v=100 * rem / r0, statut=st if st != "definitif" else st0))
    return lignes


def table_remunerations():
    import pandas as pd
    return pd.DataFrame([{
        _lab("col_annee"): l["annee"], _lab("col_grandeur"): _lab(l["grandeur"]),
        _lab("col_source"): _lab("src_" + l["source"]), _lab("col_pct"): round(l["v"], 1),
        _lab("col_statut"): l["statut"]} for l in _remunerations()])


def fig_remunerations():
    figtools.apply_lang_font()
    lignes = _remunerations()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    couleurs = {"rem_ratio_dgct": GRIS, "rem_meme_annee": BLEU, "rem_annee_prec": VERT}
    for g in couleurs:
        for s in ("dgct", "somme"):
            ls = [l for l in lignes if l["grandeur"] == g and l["source"] == s]
            if ls:
                creux = {l["annee"] for l in ls if l["statut"] != "definitif"}
                _courbe(ax, {l["annee"]: l["v"] for l in ls}, couleurs[g], s, _lab(g), "pct",
                        creux=creux)
    annees = sorted({l["annee"] for l in lignes})
    _cadre(ax, _lab("t_remunerations"), _lab("pct_r1"), annees[0], annees[-1])
    ax.set_ylim(30, 65)
    plafond, = ax.plot([ANNEE_CCL_BUDGETS - 0.5, annees[-1] + 0.8],
                       [PLAFOND_REMUNERATIONS] * 2, color=ROUGE, lw=1.2, zorder=1)
    figtools.infobulle(plafond, _lab("lg_plafond_moitie"))
    _ruptures(ax, "pct", annees)
    _marques_textes(ax, ((2019, "mq_budg_2019", 0.97),), annees[0], annees[-1])
    poignees = _legende_grandeurs(list(couleurs.items()))
    poignees.append(Line2D([], [], color=ROUGE, lw=1.2,
                           label=figtools.fig_text(_lab("lg_plafond_moitie"))))
    poignees += _legende_sources(["dgct", "somme"])
    poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", ls="",
                           label=figtools.fig_text(_lab("lg_creux_budg"))))
    poignees.append(_legende_marques())
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2,
              fontsize=7.2, frameon=False)
    fig.tight_layout()
    return fig


DEPENSES_TITRES = (("depenses_t1", BLEU), ("depenses_t2", ORANGE))
DEPENSES_DETTE = (("remboursement_principal", ROUGE), ("interets_dette", VIOLET),
                  ("emprunts_interieurs", VERT))


def _depenses() -> list[dict]:
    """Lignes (vue, grandeur, source, année, MD, statut) ; les sources restent séparées."""
    c = _communes()
    lignes = []
    b = _bm2014()
    for a in range(2002, 2013):
        for k, _ in DEPENSES_TITRES:
            lignes.append(dict(vue="depenses", grandeur=k, source="bm2014", annee=a,
                               v=b[(k, a)], statut="publie"))
        lignes.append(dict(vue="dette", grandeur="remboursement_principal", source="bm2014",
                           annee=a, v=b[("remboursement_capital", a)], statut="publie"))
    for a in range(2008, 2020):
        for k, _ in DEPENSES_TITRES:
            lignes.append(dict(vue="depenses", grandeur=k, source="dgct", annee=a,
                               v=c["dgct"][(k, a)][0], statut="definitif"))
    for a in range(2018, 2024):
        for vue, grandeurs in (("depenses", DEPENSES_TITRES), ("dette", DEPENSES_DETTE)):
            for k, _ in grandeurs:
                v, st = c["somme"][(k, a)]
                lignes.append(dict(vue=vue, grandeur=k, source="somme", annee=a, v=v,
                                   statut=st))
    return lignes


def table_depenses():
    import pandas as pd
    return pd.DataFrame([{
        _lab("col_annee"): l["annee"], _lab("col_grandeur"): _lab(l["grandeur"]),
        _lab("col_source"): _lab("src_" + l["source"]), _lab("col_md"): round(l["v"], 1),
        _lab("col_statut"): l["statut"]} for l in _depenses()])


def fig_depenses(vue: str = "depenses"):
    figtools.apply_lang_font()
    lignes = [l for l in _depenses() if l["vue"] == vue]
    grandeurs = DEPENSES_TITRES if vue == "depenses" else DEPENSES_DETTE
    sources = ("bm2014", "dgct", "somme") if vue == "depenses" else ("bm2014", "somme")
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    for k, coul in grandeurs:
        for s in sources:
            ls = [l for l in lignes if l["grandeur"] == k and l["source"] == s]
            if ls:
                creux = {l["annee"] for l in ls if l["statut"] not in ("definitif", "publie")}
                _courbe(ax, {l["annee"]: l["v"] for l in ls}, coul, s, _lab(k), "md",
                        creux=creux)
    annees = sorted({l["annee"] for l in lignes})
    _cadre(ax, _lab("t_depenses" if vue == "depenses" else "t_dette"), _lab("md"),
           annees[0], annees[-1])
    ax.set_ylim(0, ax.get_ylim()[1] * 1.22)  # de la place en haut pour les libellés
    _ruptures(ax, "md", annees)
    _marques_textes(ax, MARQUES_BUDGETS, annees[0], annees[-1])
    poignees = _legende_grandeurs(list(grandeurs)) + _legende_sources(list(sources))
    poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", ls="",
                           label=figtools.fig_text(_lab("lg_creux"))))
    poignees.append(_legende_marques())
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2,
              fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig


def vues_depenses():
    return [(_lab("vue_depenses"), fig_depenses("depenses")),
            (_lab("vue_dette"), fig_depenses("dette"))]

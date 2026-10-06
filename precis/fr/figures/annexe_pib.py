"""Figures de l'annexe du site « Le PIB et ses changements de base » (`precis/fr/annexe-pib.qmd`).

    from figures import annexe_pib
    annexe_pib.vues_bases()    # les trois vues de la figure `fig-pib-bases` (prix courants)
    annexe_pib.table_bases()   # ses données téléchargeables
    annexe_pib.vues_volume()   # les deux vues de la figure `fig-pib-volume`
    annexe_pib.table_volume()  # ses données téléchargeables

MODULE DE FIGURE D'UNE PAGE DE SITE, et non d'un livre : il vit dans `precis/fr/figures/`, à
côté de la page ; la page arabe le trouve par le lien symbolique `precis/ar/figures`. Les
sorties de `figtools.figure_tabs` vont à côté de la page (`precis/<langue>/_fig/` et
`precis/<langue>/figdata/`), et `build.sh` les copie dans le site.

D'OÙ VIENNENT LES DONNÉES. Cinq séries de `tunisia-data`, lues par `figtools.series()`
(l'entrepôt s'il est installé, sinon le cache `precis/_seriescache/`) :

  - `pib-courant-enchaine` : une ligne par année et par `variante` — `ins_base_1983`,
    `ins_base_1997`, `ins_base_2015` (les niveaux que l'INS a publiés ou recalculés),
    `accolee` (ces niveaux mis bout à bout, sans correction) et `enchainee` (indice 100 en
    2015, chaîné par les taux de croissance ; construction à fin d'illustration) ;
  - `pib-croissance-par-base` : le taux de croissance annuel calculé à l'intérieur de chaque
    base, et sur les niveaux de la Banque mondiale avant 1992 ;
  - `pib-courant-recouvrements` : les années connues dans deux bases, et l'écart de niveau ;
  - `pib-croissance-volume` : tous les taux de croissance en volume, une ligne par année,
    source, base et année de prix (éditions et classeur de l'INS, séries transmises aux
    Nations unies, Banque mondiale) ;
  - `pib-volume-enchaine` : un indice de volume, 100 en 2015, chaîné sur le taux retenu pour
    chaque année, avec la règle de chaque jonction (construction à fin d'illustration).

RÈGLES.

  - **`fig-pib-bases` est aux prix courants** : ses taux de croissance sont nominaux.
    **`fig-pib-volume` est en volume** : un taux y dépend de la base ET de l'année de prix,
    qui ne sont pas la même chose ; chaque jonction dit laquelle des deux change.
  - **Deux familles de sources ne se confondent pas** : les comptes tunisiens (l'INS, et les
    Nations unies qui publient ce que l'INS leur transmet), avec la couleur et la marque de
    leur base (triangle renversé brun quand la base n'est pas dite) ; la Banque mondiale,
    source extérieure, en croix grises.
  - **Aucun nombre n'est écrit dans ce module** : les écarts de niveau, les taux apparents et
    les taux à l'intérieur d'une base sont lus dans les séries.
  - **Une base garde, d'une vue à l'autre, sa couleur, sa marque et son trait** : base 1983 en
    orange, carrés, pointillé ; base 1997 en bleu, triangles, tirets ; base 2015 en vert,
    ronds, trait plein — les traits sont ceux des figures des volumes. La Banque mondiale,
    source extérieure et base non dite, est en gris.
  - **Une valeur recalculée par l'INS** (« rétropolée ») porte une marque creuse et un trait fin.
  - **Les séries enchaînées sont des illustrations** : aucune ne sert de dénominateur à un ratio.
  - Le seul calcul fait ici est l'indice de la série accolée (PIB de l'année ÷ PIB de 2015),
    pour la comparer à l'indice de la série enchaînée ; il a sa propre colonne dans les données.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FixedLocator, FuncFormatter, MultipleLocator, NullLocator

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
import figtools  # noqa: E402

SERIE_ENCHAINE = "pib-courant-enchaine"
SERIE_CROISSANCE = "pib-croissance-par-base"
SERIE_RECOUVREMENTS = "pib-courant-recouvrements"
SERIES = (SERIE_ENCHAINE, SERIE_CROISSANCE, SERIE_RECOUVREMENTS)
SERIE_VOLUME = "pib-croissance-volume"
SERIE_VOLUME_ENCHAINE = "pib-volume-enchaine"
SERIES_VOLUME = (SERIE_VOLUME, SERIE_VOLUME_ENCHAINE, SERIE_ENCHAINE)

ORANGE, BLEU, VERT, GRIS, VIOLET, BRUN, ROUGE, SARCELLE = (
    "#d1600f", "#0969da", "#1a7f37", "#57606a", "#8250df", "#9a6700", "#cf222e", "#0e7490")

# Une base = une couleur, une marque, un trait (les traits sont ceux de
# `finances_locales.STYLE_BASE`). Clé : le libellé de la colonne `base` des séries.
BASES = {
    "base 1983": dict(cle="b1983", couleur=ORANGE, marker="s", ls=":"),
    "base 1997": dict(cle="b1997", couleur=BLEU, marker="^", ls="--"),
    "base 2015": dict(cle="b2015", couleur=VERT, marker="o", ls="-"),
}
VARIANTES_INS = {"ins_base_1983": "base 1983", "ins_base_1997": "base 1997",
                 "ins_base_2015": "base 2015"}
RETROPOLEE = "rétropolée par l'INS"   # valeur de la colonne `construction`
EXTERIEUR = "rapport extérieur"       # valeur de la colonne `famille` : la Banque mondiale
ANNEE_INDICE = 2015                   # l'indice de la série enchaînée vaut 100 cette année-là

_L = {
    "x": {"fr": "Année", "ar": "السنة"},
    "y_md": {"fr": "PIB aux prix courants, millions de dinars (échelle logarithmique)",
             "ar": "الناتج المحلي الإجمالي بالأسعار الجارية، بملايين الدنانير (سلّم لوغاريتمي)"},
    "y_taux": {"fr": "Croissance du PIB aux prix courants, % par an",
               "ar": "نموّ الناتج المحلي الإجمالي بالأسعار الجارية، % سنويًا"},
    "y_indice": {"fr": "PIB aux prix courants, indice 2015 = 100\n(échelle logarithmique)",
                 "ar": "الناتج بالأسعار الجارية، مؤشّر 2015 = 100\n(سلّم لوغاريتمي)"},
    "y_taux_court": {"fr": "Croissance aux prix courants,\n% par an",
                     "ar": "النموّ بالأسعار الجارية،\n% سنويًا"},
    # vues
    "vue_niveaux": {"fr": "Les niveaux, base par base", "ar": "المستويات حسب الأساس"},
    "vue_croissance": {"fr": "La croissance, base par base", "ar": "النموّ حسب الأساس"},
    "vue_enchainee": {"fr": "Série accolée et série enchaînée",
                      "ar": "السلسلة الموصولة دون تصحيح والسلسلة المسلسلة"},
    # bases et séries
    "b1983": {"fr": "base 1983", "ar": "أساس 1983"},
    "b1997": {"fr": "base 1997", "ar": "أساس 1997"},
    "b2015": {"fr": "base 2015", "ar": "أساس 2015"},
    "bm": {"fr": "Banque mondiale, base non dite (source extérieure, avant 1992)",
           "ar": "البنك الدولي، أساس غير مذكور (مصدر خارجي، قبل 1992)"},
    "bm_court": {"fr": "Banque mondiale, base non dite", "ar": "البنك الدولي، أساس غير مذكور"},
    "publie": {"fr": "marque pleine, trait épais : publié par l'INS",
               "ar": "علامة ممتلئة وخطّ سميك: منشور من المعهد الوطني للإحصاء"},
    "retropole": {"fr": "marque creuse, trait fin : rétropolé par l'INS",
                  "ar": "علامة فارغة وخطّ رفيع: معاد احتسابه من المعهد الوطني للإحصاء"},
    "retropole_court": {"fr": "rétropolé par l'INS", "ar": "معاد احتسابه من المعهد"},
    "publie_court": {"fr": "publié", "ar": "منشور"},
    "recouvrement": {"fr": "années connues dans deux bases", "ar": "سنوات معروفة على أساسين"},
    "enchainee": {"fr": "série enchaînée par nos soins — illustration",
                  "ar": "سلسلة مسلسلة من إعدادنا — للتوضيح"},
    "accolee": {"fr": "série accolée : niveaux publiés mis bout à bout",
                "ar": "سلسلة موصولة دون تصحيح: المستويات المنشورة متتالية"},
    "enchainee_court": {"fr": "série enchaînée", "ar": "السلسلة المسلسلة"},
    "accolee_court": {"fr": "série accolée", "ar": "السلسلة الموصولة دون تصحيح"},
    "taux_faux": {"fr": "taux faux de la série accolée (année de jonction)",
                  "ar": "نسبة خاطئة في السلسلة الموصولة (سنة الوصل)"},
    "taux_base": {"fr": "croissance dans l'ancienne base (retenue par la série enchaînée)",
                  "ar": "النموّ في الأساس القديم (المعتمد في السلسلة المسلسلة)"},
    # textes des ruptures et des infobulles
    "rup": {"fr": "{a} : niveau {e} %", "ar": "{a}: المستوى {e} %"},
    "ib_rup": {"fr": "Jonction de {a} : le PIB de {a} vaut {n} MD dans la {bn} et {o} MD dans "
                     "la {bo}, soit un écart de niveau de {e} %",
               "ar": "وصل {a}: ناتج {a} يساوي {n} م.د في {bn} و{o} م.د في {bo}، أي فارق في "
                     "المستوى بـ{e} %"},
    "ib_niveau": {"fr": "{a} · {b}, {c} : {v} MD", "ar": "{a} · {b}، {c}: {v} م.د"},
    "ib_ecart_haut": {"fr": " — {e} % par rapport à la {bo} ({o} MD)",
                      "ar": " — {e} % مقارنة بـ{bo} ({o} م.د)"},
    "ib_ecart_bas": {"fr": " — la {bn} donne {n} MD ({e} %)",
                     "ar": " — {bn} يعطي {n} م.د ({e} %)"},
    "ib_taux": {"fr": "{a} · croissance dans la {b} : {v} %",
                "ar": "{a} · النموّ في {b}: {v} %"},
    "ib_taux_bm": {"fr": "{a} · croissance, niveaux de la Banque mondiale (base non dite) : {v} %",
                   "ar": "{a} · النموّ، مستويات البنك الدولي (أساس غير مذكور): {v} %"},
    "ib_faux": {"fr": "{a} · série accolée : {f} % — taux FAUX. Il mêle la croissance "
                      "({v} % dans la {bo}) et le changement de base (niveau {e} %)",
                "ar": "{a} · السلسلة الموصولة دون تصحيح: {f} % — نسبة خاطئة. تجمع بين النموّ "
                      "({v} % في {bo}) وتغيير الأساس (المستوى {e} %)"},
    "ib_vrai": {"fr": "{a} · série enchaînée : {v} %, taux calculé dans la {bo}",
                "ar": "{a} · السلسلة المسلسلة: {v} %، نسبة محسوبة في {bo}"},
    "ib_indice": {"fr": "{a} · {s} : indice {v}", "ar": "{a} · {s}: المؤشّر {v}"},
    "et_faux": {"fr": "{f} % apparent\npour {v} %", "ar": "{f} % ظاهريًا\nمقابل {v} %"},
    # figure en volume
    "y_vol": {"fr": "Croissance du PIB en volume, % par an",
              "ar": "نموّ الناتج المحلي الإجمالي بالحجم، % سنويًا"},
    "y_indices": {"fr": "PIB, indice 2015 = 100 (échelle logarithmique)",
                  "ar": "الناتج المحلي الإجمالي، مؤشّر 2015 = 100 (سلّم لوغاريتمي)"},
    "vue_volume": {"fr": "La croissance en volume, 1961-2025",
                   "ar": "النموّ بالحجم، 1961-2025"},
    "vue_nominal_volume": {"fr": "Prix courants et volume",
                           "ar": "الأسعار الجارية والحجم"},
    "vol_retenu": {"fr": "taux retenu pour l'indice enchaîné",
                   "ar": "النسبة المعتمدة في المؤشّر المسلسل"},
    "vol_tn": {"fr": "comptes tunisiens (INS, Nations unies) :",
               "ar": "الحسابات التونسية (المعهد، الأمم المتحدة):"},
    "vol_non_dite": {"fr": "base non dite", "ar": "أساس غير مذكور"},
    "vol_bm": {"fr": "Banque mondiale (source extérieure)",
               "ar": "البنك الدولي (مصدر خارجي)"},
    "vol_divergence": {"fr": "1962-1965 : les deux familles de sources divergent",
                       "ar": "1962-1965: تباين بين صنفي المصادر"},
    "j_base": {"fr": "base", "ar": "الأساس"},
    "j_prix": {"fr": "année de prix", "ar": "سنة الأسعار"},
    "j_base_prix": {"fr": "base et année de prix", "ar": "الأساس وسنة الأسعار"},
    "j_serie": {"fr": "série", "ar": "السلسلة"},
    "j_source": {"fr": "source", "ar": "المصدر"},
    "j_etiquette": {"fr": "{a} : {t}", "ar": "{a}: {t}"},
    "ib_jonction": {"fr": "Jonction de {a} — change : {t}. {j}",
                    "ar": "وصل {a} — يتغيّر: {t}. {j}"},
    "ib_vol": {"fr": "{a} · {s}, {b}, {p} : {v} %", "ar": "{a} · {s}، {b}، {p}: {v} %"},
    "ib_vol_retenu": {"fr": "{a} · taux retenu : {v} % ({s}, {b}, {p})",
                      "ar": "{a} · النسبة المعتمدة: {v} % ({s}، {b}، {p})"},
    "ib_vol_bm": {"fr": " — Banque mondiale : {v} %, écart de {e} point(s)",
                  "ar": " — البنك الدولي: {v} %، فارق {e} نقطة"},
    "ind_nominal": {"fr": "aux prix courants : série enchaînée par nos soins — illustration",
                    "ar": "بالأسعار الجارية: سلسلة مسلسلة من إعدادنا — للتوضيح"},
    "ind_volume": {"fr": "en volume : indice enchaîné par nos soins — illustration",
                   "ar": "بالحجم: مؤشّر مسلسل من إعدادنا — للتوضيح"},
    "ind_nominal_court": {"fr": "prix courants", "ar": "الأسعار الجارية"},
    "ind_volume_court": {"fr": "volume", "ar": "الحجم"},
    "col_famille": {"fr": "Famille de sources", "ar": "صنف المصدر"},
    "col_prix": {"fr": "Année de prix", "ar": "سنة الأسعار"},
    "col_taux_vol": {"fr": "Croissance en volume (%)", "ar": "النموّ بالحجم (%)"},
    "col_mode": {"fr": "Mode", "ar": "طريقة الحصول على النسبة"},
    "col_taux_imprime": {"fr": "Taux imprimé (%)", "ar": "النسبة المطبوعة (%)"},
    "col_indice_vol": {"fr": "Indice de volume enchaîné, 2015 = 100",
                       "ar": "مؤشّر الحجم المسلسل، 2015 = 100"},
    "col_indice_nominal": {"fr": "Indice aux prix courants enchaîné, 2015 = 100",
                           "ar": "مؤشّر الأسعار الجارية المسلسل، 2015 = 100"},
    "col_taux_nominal": {"fr": "Croissance aux prix courants (%)",
                         "ar": "النموّ بالأسعار الجارية (%)"},
    "col_taux_bm": {"fr": "Croissance en volume selon la Banque mondiale (%)",
                    "ar": "النموّ بالحجم حسب البنك الدولي (%)"},
    "col_ecart_bm": {"fr": "Écart à la Banque mondiale (points)",
                     "ar": "الفارق مع البنك الدولي (نقاط)"},
    "col_note": {"fr": "Note", "ar": "ملاحظة"},
    # colonnes des données
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_serie": {"fr": "Série", "ar": "السلسلة"},
    "col_variante": {"fr": "Variante", "ar": "الصيغة"},
    "col_construction": {"fr": "Construction", "ar": "طريقة الإعداد"},
    "col_base": {"fr": "Base", "ar": "الأساس"},
    "col_pib": {"fr": "PIB aux prix courants (MD)", "ar": "الناتج بالأسعار الجارية (م.د)"},
    "col_indice": {"fr": "Indice de la série enchaînée, 2015 = 100",
                   "ar": "مؤشّر السلسلة المسلسلة، 2015 = 100"},
    "col_indice_accolee": {"fr": "Indice de la série accolée, 2015 = 100 (calculé ici : PIB ÷ "
                                 "PIB de 2015)",
                           "ar": "مؤشّر السلسلة الموصولة، 2015 = 100 (محسوب هنا)"},
    "col_taux": {"fr": "Croissance aux prix courants (%)", "ar": "النموّ بالأسعار الجارية (%)"},
    "col_faux": {"fr": "Taux faux", "ar": "نسبة خاطئة"},
    "col_base_taux": {"fr": "Base du taux", "ar": "أساس النسبة"},
    "col_jonction": {"fr": "Jonction", "ar": "الوصل"},
    "col_e1983": {"fr": "Écart à la base 1983 (%)", "ar": "الفارق مع أساس 1983 (%)"},
    "col_e1997": {"fr": "Écart à la base 1997 (%)", "ar": "الفارق مع أساس 1997 (%)"},
    "col_e2015": {"fr": "Écart à la base 2015 (%)", "ar": "الفارق مع أساس 2015 (%)"},
    "col_pib_n": {"fr": "PIB de l'année, base du taux (MD)", "ar": "ناتج السنة (م.د)"},
    "col_pib_n1": {"fr": "PIB de l'année précédente, même base (MD)",
                   "ar": "ناتج السنة السابقة، الأساس نفسه (م.د)"},
    "col_publication": {"fr": "Publication", "ar": "المنشور"},
    "col_meme_publication": {"fr": "Deux niveaux de la même publication",
                             "ar": "المستويان من المنشور نفسه"},
    "col_retropole": {"fr": "Rétropolé", "ar": "معاد احتسابه"},
    "col_source": {"fr": "Source", "ar": "المصدر"},
    "col_provenance": {"fr": "Provenance", "ar": "مأتى المعطى"},
}


# --- provenance affichée -----------------------------------------------------------------

# Le catalogue de l'entrepôt décrit ses séries pour qui les exploite : noms de colonnes,
# consignes de filtrage, renvois à ses fiches. La ligne « Source » et l'onglet « Sources »
# s'adressent au lecteur : on y remplace le libellé des bases, le périmètre et les réserves
# par un texte en clair, dans les deux langues. Titres, sources et fiches restent ceux du
# catalogue.
_BASES_LECTEUR = "1983 / 1997 / 2015"

PROVENANCE_LECTEUR = {
    SERIE_ENCHAINE: dict(
        base_pib=_BASES_LECTEUR,
        perimetre=("PIB aux prix courants : les niveaux de la base 1983 (1992-2009), de la "
                   "base 1997 (1997-2017) et de la base 2015 (2010-2025), sur les années que "
                   "l'INS a publiées ou recalculées ; la série accolée, qui met ces niveaux "
                   "bout à bout (1961-2025) ; la série enchaînée, indice 100 en 2015"),
        caveats=("Trois constructions à ne pas confondre. Publié : le niveau figure dans une "
                 "publication de l'INS, ou dans les chiffres que l'INS a transmis aux Nations "
                 "unies. Rétropolé par l'INS : recalculé par l'INS dans une base plus récente, "
                 "pour 1997-2004 en base 1997 et pour 2010-2014 en base 2015. Enchaîné par nos "
                 "soins : construction du précis à fin d'illustration, non une donnée de "
                 "l'INS ; elle préserve les taux de croissance, pas les niveaux ni les "
                 "structures, ne remplace pas une rétropolation et ne sert de dénominateur à "
                 "aucun ratio. La série accolée porte deux taux faux, aux années où elle "
                 "change de base : 1997 et 2010. Avant 1992, les niveaux sont ceux de la "
                 "Banque mondiale, dont la base n'est pas dite."),
        perimetre_ar=("الناتج المحلي الإجمالي بالأسعار الجارية: مستويات أساس 1983 "
                      "(1992-2009) وأساس 1997 (1997-2017) وأساس 2015 (2010-2025)، في السنوات "
                      "التي نشرها المعهد الوطني للإحصاء أو أعاد احتسابها؛ السلسلة الموصولة "
                      "دون تصحيح (1961-2025)؛ السلسلة المسلسلة، مؤشّر 100 في 2015"),
        caveats_ar=("ثلاث طرق إعداد لا ينبغي الخلط بينها. منشور: المستوى وارد في منشور "
                    "للمعهد الوطني للإحصاء أو في الأرقام التي أحالها المعهد إلى الأمم المتحدة. "
                    "معاد احتسابه من المعهد: أعاد المعهد حسابه على أساس أحدث، لسنوات 1997-2004 "
                    "على أساس 1997 ولسنوات 2010-2014 على أساس 2015. مسلسل من إعدادنا: إعداد "
                    "للتوضيح وليس معطى من المعهد؛ يحفظ نسب النموّ لا المستويات ولا البنية، "
                    "ولا يعوّض إعادة الاحتساب، ولا يُستعمل مقامًا لأيّ نسبة. تتضمّن السلسلة "
                    "الموصولة دون تصحيح نسبتين خاطئتين في سنتي تغيير الأساس: 1997 و2010. قبل "
                    "1992، المستويات من البنك الدولي، وأساسها غير مذكور.")),
    SERIE_CROISSANCE: dict(
        base_pib=_BASES_LECTEUR,
        perimetre=("taux de croissance annuel du PIB aux prix courants, calculé à l'intérieur "
                   "de chaque base : base 1983 (1993-2009), base 1997 (1998-2017), base 2015 "
                   "(2011-2025) ; de 1962 à 1992, taux calculé sur les niveaux de la Banque "
                   "mondiale"),
        caveats=("Série construite à fin d'illustration à partir de niveaux publiés ou "
                 "rétropolés par l'INS : chaque taux rapporte deux niveaux de la même base. "
                 "Une année connue dans deux bases a deux taux, qui diffèrent de 0,2 à "
                 "0,4 point en moyenne, alors que les niveaux diffèrent de 5 à 10 %. De 1962 à "
                 "1992, aucune base n'est dite."),
        perimetre_ar=("نسبة النموّ السنوية للناتج بالأسعار الجارية، محسوبة داخل كلّ أساس: "
                      "أساس 1983 (1993-2009)، أساس 1997 (1998-2017)، أساس 2015 (2011-2025)؛ من "
                      "1962 إلى 1992، نسبة محسوبة على مستويات البنك الدولي"),
        caveats_ar=("سلسلة مُعدّة للتوضيح انطلاقًا من مستويات نشرها المعهد الوطني للإحصاء أو "
                    "أعاد احتسابها: كلّ نسبة تقارن مستويين من الأساس نفسه. للسنة المعروفة على "
                    "أساسين نسبتان، تختلفان بـ0,2 إلى 0,4 نقطة في المتوسّط، بينما تختلف "
                    "المستويات بـ5 إلى 10 %. من 1962 إلى 1992 لا يُذكر أيّ أساس.")),
    SERIE_RECOUVREMENTS: dict(
        base_pib=_BASES_LECTEUR,
        perimetre=("années où le PIB aux prix courants est connu dans deux bases : base 1983 "
                   "et base 1997 de 1997 à 2009, base 1997 et base 2015 de 2010 à 2017"),
        caveats=("Écarts observés, de + 9,25 à + 10,91 % entre la base 1983 et la base 1997, "
                 "de + 4,89 à + 6,12 % entre la base 1997 et la base 2015 : ils ne sont pas "
                 "constants et ne donnent pas de coefficient de passage pour d'autres années. "
                 "Aucune année n'est connue à la fois en base 1983 et en base 2015."),
        perimetre_ar=("السنوات التي يُعرف فيها الناتج بالأسعار الجارية على أساسين: أساس 1983 "
                      "وأساس 1997 من 1997 إلى 2009، أساس 1997 وأساس 2015 من 2010 إلى 2017"),
        caveats_ar=("فوارق ملاحظة، من + 9,25 إلى + 10,91 % بين أساس 1983 وأساس 1997، ومن "
                    "+ 4,89 إلى + 6,12 % بين أساس 1997 وأساس 2015: غير ثابتة، ولا يُستخرج منها "
                    "معامل انتقال لسنوات أخرى. لا توجد سنة معروفة على أساس 1983 وأساس 2015 "
                    "معًا.")),
    SERIE_VOLUME: dict(
        base_pib=_BASES_LECTEUR,
        perimetre=("taux de croissance annuel du PIB en volume, source par source : éditions "
                   "des Comptes de la nation et classeur de l'INS du 15 août 2021, séries que "
                   "l'INS a transmises aux Nations unies (1961-2023), Banque mondiale "
                   "(1962-2025)"),
        caveats=("Une année a plusieurs taux, selon la source, la base et l'année de prix. "
                 "L'année de prix n'est pas une base : c'est l'année dont les prix valorisent "
                 "le volume — 1966, 1972, 1980 ou 1990 dans les séries anciennes, l'année "
                 "précédente dans les bases 1997 et 2015. Les sources tunisiennes s'accordent "
                 "à quelques dixièmes de point ; la Banque mondiale s'en écarte de 6 à "
                 "22 points de 1962 à 1965. L'année 1970 n'a de taux que de la Banque "
                 "mondiale. Les séries antérieures à 1993 ne disent pas leur base."),
        perimetre_ar=("نسبة النموّ السنوية للناتج بالحجم، مصدرًا بمصدر: نشرات الحسابات "
                      "القومية ومصنّف المعهد الوطني للإحصاء المؤرّخ في 15 أوت 2021، السلاسل "
                      "التي أحالها المعهد إلى الأمم المتحدة (1961-2023)، البنك الدولي "
                      "(1962-2025)"),
        caveats_ar=("للسنة الواحدة عدّة نسب، حسب المصدر والأساس وسنة الأسعار. سنة الأسعار "
                    "ليست أساسًا: هي السنة التي تُقوَّم بأسعارها الكمّيات — 1966 أو 1972 أو "
                    "1980 أو 1990 في السلاسل القديمة، والسنة السابقة في أساسي 1997 و2015. "
                    "تتقارب المصادر التونسية في حدود أعشار النقطة، ويبتعد عنها البنك الدولي "
                    "بـ6 إلى 22 نقطة من 1962 إلى 1965. سنة 1970 ليس لها نسبة إلّا من البنك "
                    "الدولي. السلاسل السابقة لسنة 1993 لا تذكر أساسها.")),
    SERIE_VOLUME_ENCHAINE: dict(
        base_pib=_BASES_LECTEUR,
        perimetre=("indice de volume du PIB, 100 en 2015, de 1960 à 2025 : un taux par année, "
                   "celui de l'INS dans la base la plus récente, à défaut celui que l'INS a "
                   "transmis aux Nations unies, et celui de la Banque mondiale pour la seule "
                   "année 1970"),
        caveats=("Enchaîné par nos soins : construction du précis à fin d'illustration, non "
                 "une donnée de l'INS. L'indice chaîne des taux de sept combinaisons de base "
                 "et d'année de prix ; il préserve les taux de croissance, pas les niveaux ni "
                 "les structures, ne remplace pas une rétropolation, n'a pas de niveau en "
                 "dinars et ne sert de dénominateur à aucun ratio."),
        perimetre_ar=("مؤشّر حجم الناتج، 100 في 2015، من 1960 إلى 2025: نسبة واحدة لكلّ سنة، "
                      "نسبة المعهد الوطني للإحصاء في أحدث أساس، وإلّا النسبة التي أحالها "
                      "المعهد إلى الأمم المتحدة، ونسبة البنك الدولي لسنة 1970 وحدها"),
        caveats_ar=("مسلسل من إعدادنا: إعداد للتوضيح وليس معطى من المعهد الوطني للإحصاء. "
                    "يسلسل المؤشّر نسبًا من سبع تركيبات بين الأساس وسنة الأسعار؛ يحفظ نسب "
                    "النموّ لا المستويات ولا البنية، ولا يعوّض إعادة الاحتساب، وليس له مستوى "
                    "بالدينار، ولا يُستعمل مقامًا لأيّ نسبة.")),
}


# La colonne de provenance des séries désigne les fichiers et les séries de l'entrepôt. Dans
# le tableau affiché et le fichier téléchargeable, on dit la publication ; la page, la feuille,
# la cellule et l'adresse en ligne sont conservées.
_CLASSEUR = "classeur de l'INS du 15 août 2021"
_EDITIONS = "INS, Les Comptes de la nation"
_PROVENANCE_LISIBLE = [
    (r"data/processed/\S+/pib_nominal_editions\.csv", _EDITIONS),
    (r"data/raw/\S+/INS_2021-08-15_\S+\.xlsx", _CLASSEUR),
    (r"série wdi-tunisie", "Banque mondiale, World Development Indicators"),
    (r"série cnat-pib-(?:nominal|volume)", _EDITIONS),
    (r"série undata-pib(?:-volume)?", "INS, via les Nations unies (UNdata)"),
    (r"série pib-croissance-par-base, chaînée",
     "taux de croissance calculés à l'intérieur de chaque base, chaînés"),
    (r"série pib-courant-par-base \(classeur de l'INS\)", _CLASSEUR),
    (r"série pib-courant-par-base : ", ""),
]
_VARIANTES_LISIBLES = {
    "accolee": "série accolée", "enchainee": "série enchaînée",
    "ins_base_1983": "base 1983 de l'INS", "ins_base_1997": "base 1997 de l'INS",
    "ins_base_2015": "base 2015 de l'INS", "croissance_par_base": "croissance par base",
}
_SERIES_LISIBLES = {
    SERIE_ENCHAINE: "PIB aux prix courants sur longue période",
    SERIE_CROISSANCE: "croissance aux prix courants, base par base",
    SERIE_VOLUME: "croissance en volume, toutes sources",
    SERIE_VOLUME_ENCHAINE: "indice de volume enchaîné",
}


def _lisible(d):
    """Rend lisibles, dans un tableau de données, la provenance, la variante et la série."""
    import re
    def provenance(v):
        if not isinstance(v, str):
            return v
        for motif, texte in _PROVENANCE_LISIBLE:
            v = re.sub(motif, texte, v)
        if re.search(r"data/|\.csv|\.xlsx|série [a-z]+-[a-z-]+", v):
            raise ValueError(f"provenance non traduite pour le lecteur : {v!r}")
        return v
    d = d.copy()
    d["provenance"] = d["provenance"].map(provenance)
    if "variante" in d:
        d["variante"] = d["variante"].map(_VARIANTES_LISIBLES)
    d["serie"] = d["serie"].map(_SERIES_LISIBLES)
    return d


def _declarer() -> None:
    """Remplace, pour l'affichage, les bases, le périmètre et les réserves du catalogue."""
    for sid, champs in PROVENANCE_LECTEUR.items():
        if sid in figtools._DECLAREES:
            continue
        origine = {k: v for k, v in figtools.meta(sid).items() if k != "id"}
        figtools.register_provenance(sid, **{**origine, **champs})


_declarer()


def _lab(key: str, **valeurs) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"]).format(**valeurs)


def _ft(key: str, **valeurs) -> str:
    return "\n".join(figtools.fig_text(l) for l in _lab(key, **valeurs).split("\n"))


def _nombre(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _signe(v: float, dec: int = 2) -> str:
    """« + 9,79 » ou « − 1,20 » : un pourcentage avec son signe."""
    return ("+ " if v >= 0 else "− ") + _nombre(abs(v), dec)


def _base(libelle: str) -> str:
    """Libellé d'une base dans la langue du livre."""
    return _lab(BASES[libelle]["cle"]) if libelle in BASES else _lab("bm_court")


# --- lecture des séries ------------------------------------------------------------------

def _enchaine():
    return figtools.series(SERIE_ENCHAINE)


def _variante(nom: str):
    d = _enchaine()
    return d[d["variante"] == nom].sort_values("annee")


def _croissance():
    return figtools.series(SERIE_CROISSANCE).sort_values(["base", "annee"])


def _recouvrements() -> dict[tuple[int, str], dict]:
    """{(année, base nouvelle): ligne} des années connues dans deux bases."""
    d = figtools.series(SERIE_RECOUVREMENTS)
    return {(int(r.annee), r.base_nouvelle): r._asdict() for r in d.itertuples(index=False)}


def _jonctions() -> list[dict]:
    """Les années où la série accolée change de base : une ligne par jonction.

    `faux` : le taux apparent de la série accolée ; `vrai` : le taux retenu par la série
    enchaînée, calculé dans l'ancienne base ; `ecart` : l'écart de niveau entre les deux bases
    cette année-là. Tout est lu dans les séries.
    """
    acc = _variante("accolee")
    ench = _variante("enchainee").set_index("annee")
    rec = _recouvrements()
    out = []
    for r in acc[acc["croissance_fausse"] == "oui"].itertuples(index=False):
        a = int(r.annee)
        e = rec[(a, r.base)]
        out.append(dict(annee=a, base_nouvelle=r.base, base_ancienne=e["base_ancienne"],
                        faux=float(r.croissance_pct), vrai=float(ench.loc[a, "croissance_pct"]),
                        ecart=float(e["ecart_pct"]), nouveau=float(e["pib_base_nouvelle_MD"]),
                        ancien=float(e["pib_base_ancienne_MD"])))
    return out


# --- habillage commun --------------------------------------------------------------------

def _cadre(ax, ylabel, x0, x1, xlabel=True):
    ax.set_ylabel(figtools.fig_text(ylabel) if "\n" not in ylabel else
                  "\n".join(figtools.fig_text(l) for l in ylabel.split("\n")), fontsize=8.5)
    if xlabel:
        ax.set_xlabel(figtools.fig_text(_lab("x")))
    ax.set_xlim(x0 - 0.8, x1 + 0.8)
    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.tick_params(labelsize=8)
    ax.grid(True, alpha=0.3)


def _echelle_log(ax, graduations):
    ax.set_yscale("log")
    ax.yaxis.set_major_locator(FixedLocator(graduations))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nombre(v, 1 if v < 1 else 0)))


def _marque_jonctions(ax, texte=True):
    """Trait vertical à chaque jonction, avec l'écart de niveau en étiquette et en infobulle."""
    for j in _jonctions():
        trait = figtools.marque_rupture(
            ax, j["annee"],
            _ft("rup", a=j["annee"], e=_signe(j["ecart"], 1)) if texte else None)
        if trait is not None:
            figtools.infobulle(trait, _texte_jonction(j))


def _texte_jonction(j: dict) -> str:
    return _lab("ib_rup", a=j["annee"], n=_nombre(j["nouveau"]), bn=_base(j["base_nouvelle"]),
                o=_nombre(j["ancien"]), bo=_base(j["base_ancienne"]), e=_signe(j["ecart"]))


def _poignee_base(libelle: str, **kw) -> Line2D:
    st = BASES[libelle]
    return Line2D([], [], color=st["couleur"], marker=st["marker"], ls=st["ls"], ms=4.5, lw=1.7,
                  label=figtools.fig_text(_base(libelle)), **kw)


def _legende(ax, poignees, ncol, y=-0.13):
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, y), ncol=ncol,
              fontsize=7.5, frameon=False)


# --- vue 1 : les niveaux, base par base --------------------------------------------------

def fig_niveaux():
    """PIB aux prix courants des trois bases de l'INS, chacune sur ses années, 1992-2025."""
    figtools.apply_lang_font()
    rec = _recouvrements()
    anciens = {(a, r["base_ancienne"]): r for (a, _), r in rec.items()}
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    annees = []
    for variante, libelle in VARIANTES_INS.items():
        d = _variante(variante)
        st = BASES[libelle]
        retro = d[d["construction"] == RETROPOLEE]
        publie = d[d["construction"] != RETROPOLEE]
        # Le tronçon rétropolé est mené jusqu'à la première année publiée : pas de trou.
        if len(retro):
            pont = d[d["annee"] <= publie["annee"].min()]
            ax.plot(pont["annee"], pont["pib_MD"], ls=st["ls"], lw=0.9, color=st["couleur"],
                    zorder=2)
        ax.plot(publie["annee"], publie["pib_MD"], ls=st["ls"], lw=2.1, color=st["couleur"],
                zorder=2)
        for r in d.itertuples(index=False):
            a, creux = int(r.annee), r.construction == RETROPOLEE
            p, = ax.plot([a], [r.pib_MD], st["marker"], ms=4.6, color=st["couleur"],
                         mfc="white" if creux else st["couleur"], zorder=3)
            texte = _lab("ib_niveau", a=a, b=_base(libelle), v=_nombre(r.pib_MD),
                         c=_lab("retropole_court" if creux else "publie_court"))
            if (a, libelle) in rec:      # année aussi connue dans la base précédente
                e = rec[(a, libelle)]
                texte += _lab("ib_ecart_haut", e=_signe(e["ecart_pct"]),
                              bo=_base(e["base_ancienne"]), o=_nombre(e["pib_base_ancienne_MD"]))
            if (a, libelle) in anciens:  # année aussi connue dans la base suivante
                e = anciens[(a, libelle)]
                texte += _lab("ib_ecart_bas", e=_signe(e["ecart_pct"]),
                              bn=_base(e["base_nouvelle"]), n=_nombre(e["pib_base_nouvelle_MD"]))
            figtools.infobulle(p, texte)
            annees.append(a)
    _cadre(ax, _lab("y_md"), min(annees), max(annees))
    _echelle_log(ax, [15000, 20000, 30000, 40000, 60000, 80000, 100000, 130000, 170000])
    _marque_jonctions(ax)
    poignees = [_poignee_base(b) for b in BASES]
    poignees += [
        Line2D([], [], color=GRIS, marker="o", ls="-", lw=2.1, ms=4.6,
               label=figtools.fig_text(_lab("publie"))),
        Line2D([], [], color=GRIS, marker="o", mfc="white", ls="-", lw=0.9, ms=4.6,
               label=figtools.fig_text(_lab("retropole"))),
    ]
    _legende(ax, poignees, ncol=3)
    fig.tight_layout()
    return fig


# --- vue 2 : la croissance, base par base ------------------------------------------------

def _plages_recouvrement(d) -> list[tuple[int, int]]:
    """Plages d'années qui portent un taux dans deux bases."""
    n = d.groupby("annee")["base"].nunique()
    plages: list[list[int]] = []
    for a in sorted(int(a) for a in n[n > 1].index):
        if plages and a == plages[-1][1] + 1:
            plages[-1][1] = a
        else:
            plages.append([a, a])
    return [(debut, fin) for debut, fin in plages]


def fig_croissance():
    """Taux de croissance annuel du PIB courant, calculé à l'intérieur de chaque base."""
    figtools.apply_lang_font()
    d = _croissance()
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    for debut, fin in _plages_recouvrement(d):
        ax.axvspan(debut - 0.5, fin + 0.5, color="#eaeef2", zorder=0, lw=0)
    for libelle in sorted(d["base"].unique(), key=lambda b: (b in BASES, b)):
        g = d[d["base"] == libelle]
        if libelle in BASES:
            st = BASES[libelle]
            style = dict(color=st["couleur"], marker=st["marker"], ls=st["ls"], lw=1.5, ms=4.4)
            cle = "ib_taux"
        else:   # Banque mondiale : source extérieure, base non dite
            style = dict(color=GRIS, marker="x", ls="-", lw=0.9, ms=4)
            cle = "ib_taux_bm"
        ax.plot(g["annee"], g["croissance_pct"], ls=style["ls"], lw=style["lw"],
                color=style["color"], zorder=2)
        for r in g.itertuples(index=False):
            creux = r.retropole == "oui"
            p, = ax.plot([r.annee], [r.croissance_pct], style["marker"], ms=style["ms"],
                         color=style["color"], mfc="white" if creux else style["color"],
                         zorder=3)
            texte = _lab(cle, a=int(r.annee), b=_base(libelle), v=_signe(r.croissance_pct))
            if creux:
                texte += f" ({_lab('retropole_court')})"
            figtools.infobulle(p, texte)
    ax.axhline(0, color=GRIS, lw=0.8, zorder=1)
    _cadre(ax, _lab("y_taux"), int(d["annee"].min()), int(d["annee"].max()))
    _marque_jonctions(ax)
    poignees = [Line2D([], [], color=GRIS, marker="x", ls="-", lw=0.9, ms=4,
                       label=figtools.fig_text(_lab("bm")))]
    poignees += [_poignee_base(b) for b in BASES]
    poignees += [
        Line2D([], [], color=GRIS, marker="o", mfc="white", ls="", ms=4.4,
               label=figtools.fig_text(_lab("retropole_court"))),
        Patch(color="#eaeef2", label=figtools.fig_text(_lab("recouvrement"))),
    ]
    _legende(ax, poignees, ncol=3)
    fig.tight_layout()
    return fig


# --- vue 3 : série accolée et série enchaînée --------------------------------------------

def _indice_accolee():
    """Indice 2015 = 100 de la série accolée : PIB de l'année ÷ PIB de 2015 (seul calcul fait ici)."""
    acc = _variante("accolee").set_index("annee")
    return 100 * acc["pib_MD"] / float(acc.loc[ANNEE_INDICE, "pib_MD"])


def fig_enchainee():
    """Indice (haut) et taux de croissance (bas) de la série accolée et de la série enchaînée."""
    figtools.apply_lang_font()
    ench = _variante("enchainee").set_index("annee")
    acc = _variante("accolee").set_index("annee")
    indice_acc = _indice_accolee()
    jonctions = _jonctions()
    fig, (haut, bas) = plt.subplots(2, 1, figsize=(9.5, 8.2), sharex=True,
                                    gridspec_kw=dict(height_ratios=[3, 2.4], hspace=0.08))
    # Haut : les deux indices.
    haut.plot(indice_acc.index, indice_acc.values, ls="--", lw=1.6, color=BRUN, zorder=2)
    haut.plot(ench.index, ench["indice_2015_100"], ls="-", lw=1.9, color=VIOLET, zorder=3)
    for j in jonctions:   # l'année de jonction et celle qui la précède, sur les deux séries
        for a in (j["annee"] - 1, j["annee"]):
            for valeur, coul, marque, cle in (
                    (float(indice_acc.loc[a]), BRUN, "D", "accolee_court"),
                    (float(ench.loc[a, "indice_2015_100"]), VIOLET, "o", "enchainee_court")):
                p, = haut.plot([a], [valeur], marque, ms=4.2, color=coul, mfc="white", zorder=4)
                figtools.infobulle(p, _lab("ib_indice", a=a, s=_lab(cle), v=_nombre(valeur, 2)))
    _cadre(haut, _lab("y_indice"), int(ench.index.min()), int(ench.index.max()), xlabel=False)
    _echelle_log(haut, [0.5, 1, 2, 5, 10, 20, 50, 100, 200])
    _marque_jonctions(haut)
    # Bas : les taux. Les deux séries ont le même taux partout, sauf aux jonctions.
    bas.plot(acc.index, acc["croissance_pct"], ls="--", lw=1.2, color=BRUN, zorder=2)
    bas.plot(ench.index, ench["croissance_pct"], ls="-", lw=1.5, color=VIOLET, zorder=3)
    bas.axhline(0, color=GRIS, lw=0.8, zorder=1)
    for j in jonctions:
        a = j["annee"]
        faux, = bas.plot([a], [j["faux"]], "X", ms=10, color=ROUGE, mec="white", mew=0.8,
                         zorder=5)
        figtools.infobulle(faux, _lab("ib_faux", a=a, f=_signe(j["faux"]), v=_signe(j["vrai"]),
                                      bo=_base(j["base_ancienne"]), e=_signe(j["ecart"])))
        vrai, = bas.plot([a], [j["vrai"]], "o", ms=6.5, color=VIOLET, mfc="white", mew=1.4,
                         zorder=5)
        figtools.infobulle(vrai, _lab("ib_vrai", a=a, v=_signe(j["vrai"]),
                                      bo=_base(j["base_ancienne"])))
        bas.annotate(_ft("et_faux", f=_signe(j["faux"]), v=_signe(j["vrai"])),
                     xy=(a, j["faux"]), xytext=(9, 2), textcoords="offset points",
                     ha="left", va="center", fontsize=7.5, color=ROUGE)
    _cadre(bas, _lab("y_taux_court"), int(ench.index.min()), int(ench.index.max()))
    _marque_jonctions(bas, texte=False)
    poignees = [
        Line2D([], [], color=VIOLET, ls="-", lw=1.9, label=figtools.fig_text(_lab("enchainee"))),
        Line2D([], [], color=BRUN, ls="--", lw=1.6, label=figtools.fig_text(_lab("accolee"))),
        Line2D([], [], color=ROUGE, marker="X", ms=8, ls="", mec="white",
               label=figtools.fig_text(_lab("taux_faux"))),
        Line2D([], [], color=VIOLET, marker="o", mfc="white", ms=6, ls="", mew=1.4,
               label=figtools.fig_text(_lab("taux_base"))),
    ]
    _legende(bas, poignees, ncol=2, y=-0.2)
    fig.subplots_adjust(left=0.1, right=0.98, top=0.98, bottom=0.14)
    return fig


def vues_bases():
    return [(_lab("vue_niveaux"), fig_niveaux()), (_lab("vue_croissance"), fig_croissance()),
            (_lab("vue_enchainee"), fig_enchainee())]


# --- données téléchargeables -------------------------------------------------------------

def table_bases():
    """Toutes les lignes tracées, avec leurs colonnes de provenance.

    Les lignes de `pib-courant-enchaine` (cinq variantes) puis celles de
    `pib-croissance-par-base` (variante « croissance par base »), sans rien retrancher. Une
    seule colonne est calculée ici : l'indice de la série accolée.
    """
    import pandas as pd
    e = _enchaine().copy()
    e.insert(1, "serie", SERIE_ENCHAINE)
    indice = _indice_accolee()
    e["indice_accolee"] = [round(float(indice.loc[a]), 3) if v == "accolee" else None
                           for a, v in zip(e["annee"], e["variante"])]
    c = _croissance().copy()
    c.insert(1, "serie", SERIE_CROISSANCE)
    c["variante"] = "croissance_par_base"
    d = _lisible(pd.concat([e, c], ignore_index=True))
    colonnes = {
        "annee": "col_annee", "serie": "col_serie", "variante": "col_variante",
        "construction": "col_construction", "base": "col_base", "pib_MD": "col_pib",
        "indice_2015_100": "col_indice", "indice_accolee": "col_indice_accolee",
        "croissance_pct": "col_taux", "croissance_fausse": "col_faux",
        "base_du_taux": "col_base_taux", "jonction": "col_jonction",
        "ecart_base_1983_pct": "col_e1983", "ecart_base_1997_pct": "col_e1997",
        "ecart_base_2015_pct": "col_e2015", "pib_n_MD": "col_pib_n",
        "pib_n_1_MD": "col_pib_n1", "publication": "col_publication",
        "meme_publication": "col_meme_publication", "retropole": "col_retropole",
        "source": "col_source", "provenance": "col_provenance",
    }
    oubliees = set(d.columns) - set(colonnes)
    if oubliees:   # une colonne nouvelle en amont ne doit pas disparaître en silence
        raise KeyError(f"colonnes sans libellé : {sorted(oubliees)}")
    return d[list(colonnes)].rename(columns={k: _lab(v) for k, v in colonnes.items()})


# =========================================================================================
# Figure `fig-pib-volume` : la croissance en volume
# =========================================================================================

def _volume():
    return figtools.series(SERIE_VOLUME).sort_values(["annee", "source", "base"])


def _volume_enchaine():
    return figtools.series(SERIE_VOLUME_ENCHAINE).sort_values("annee")


def _base_volume(libelle) -> str | None:
    """« base 1983 » … ou `None` quand la source ne dit pas sa base (séries 10 et 20, Banque mondiale)."""
    return libelle if libelle in BASES else None


def _jonctions_volume() -> list[dict]:
    """Les années où l'indice de volume change de source, de base ou d'année de prix.

    `type` dit CE QUI change, en comparant l'année à celle qui la précède : `j_base`,
    `j_prix`, `j_base_prix` ; `j_serie` quand l'une des deux bases n'est pas dite — on ne peut
    alors pas affirmer un changement de base ; `j_source` quand la base et l'année de prix
    restent les mêmes, ou que l'une des deux années est prise à la Banque mondiale. `texte`
    est la colonne `jonction` de la série, reprise telle quelle.
    """
    d = _volume_enchaine()
    par_annee = {int(r.annee): r for r in d.itertuples(index=False)}
    out = []
    for r in d[d["jonction"].notna()].itertuples(index=False):
        a = int(r.annee)
        avant = par_annee[a - 1]
        if EXTERIEUR in (r.famille, avant.famille):
            # La Banque mondiale ne fournit que 1970 : de part et d'autre, on compare les
            # comptes tunisiens entre eux (1969 et 1971).
            if r.famille == EXTERIEUR:
                out.append(dict(annee=a, type="j_source", texte=r.jonction))
                continue
            avant = par_annee[a - 2]
        prix = r.annee_de_prix != avant.annee_de_prix
        b0, b1 = _base_volume(avant.base), _base_volume(r.base)
        if b0 is None or b1 is None:
            base, serie = False, r.base != avant.base and not prix
        else:
            base, serie = b0 != b1, False
        cle = ("j_base_prix" if base and prix else "j_base" if base else "j_prix" if prix
               else "j_serie" if serie else "j_source")
        out.append(dict(annee=a, type=cle, texte=r.jonction))
    return out


def _style_volume(base) -> tuple[str, str]:
    """(couleur, marque) d'un taux des comptes tunisiens : celles de sa base."""
    if base in BASES:
        return BASES[base]["couleur"], BASES[base]["marker"]
    return BRUN, "v"


def _texte_jonction_volume(j: dict) -> str:
    return _lab("ib_jonction", a=j["annee"], t=_lab(j["type"]), j=j["texte"])


def fig_volume():
    """Taux de croissance en volume : le taux retenu (trait) et tous les taux des sources."""
    figtools.apply_lang_font()
    d = _volume()
    ench = _volume_enchaine()
    ench = ench[ench["croissance_volume_pct"].notna()]
    fig, ax = plt.subplots(figsize=(9.5, 5.9))
    # 1962-1965 : les années où l'écart à la Banque mondiale dépasse tous les autres.
    gros = ench[ench["ecart_banque_mondiale_points"].abs() > 5]["annee"]
    if len(gros):
        ax.axvspan(gros.min() - 0.5, gros.max() + 0.5, color="#eaeef2", zorder=0, lw=0)
    ax.axhline(0, color=GRIS, lw=0.8, zorder=1)
    # La Banque mondiale : source extérieure.
    bm = d[d["famille"] == EXTERIEUR]
    ax.plot(bm["annee"], bm["croissance_volume_pct"], ls="-", lw=0.7, color=GRIS, zorder=2)
    retenu_bm = {j["annee"]: j for j in _jonctions_volume()
                 if (ench["annee"] == j["annee"]).any()
                 and ench.loc[ench["annee"] == j["annee"], "famille"].iloc[0] == EXTERIEUR}
    for r in bm.itertuples(index=False):
        p, = ax.plot([r.annee], [r.croissance_volume_pct], "x", ms=4.2, color=GRIS, zorder=3)
        texte = _lab("ib_vol", a=int(r.annee), s=r.source, b=r.base, p=r.annee_de_prix,
                     v=_signe(r.croissance_volume_pct))
        if int(r.annee) in retenu_bm:   # 1970 : le taux retenu est celui de la Banque mondiale
            texte += " — " + _texte_jonction_volume(retenu_bm[int(r.annee)])
        figtools.infobulle(p, texte)
    # Le taux retenu, année par année.
    ax.plot(ench["annee"], ench["croissance_volume_pct"], ls="-", lw=1.6, color=SARCELLE,
            zorder=3)
    # Les comptes tunisiens : une marque par taux, couleur et forme de sa base ; creuse si
    # la valeur est rétropolée par l'INS, comme dans `fig-pib-bases`.
    tn = d[d["famille"] != EXTERIEUR]
    retenus = {int(r.annee): r for r in ench.itertuples(index=False)}
    jonctions = {j["annee"]: j for j in _jonctions_volume()}
    for r in tn.itertuples(index=False):
        a = int(r.annee)
        coul, marque = _style_volume(r.base)
        p, = ax.plot([a], [r.croissance_volume_pct], marque, ms=4.4, color=coul,
                     mfc="white" if r.retropole == "oui" else coul, mew=1.0, zorder=4)
        texte = _lab("ib_vol", a=a, s=r.source, b=r.base, p=r.annee_de_prix,
                     v=_signe(r.croissance_volume_pct))
        e = retenus.get(a)
        if (e is not None and (e.source, e.base, e.annee_de_prix) ==
                (r.source, r.base, r.annee_de_prix)):
            texte = _lab("ib_vol_retenu", a=a, s=r.source, b=r.base, p=r.annee_de_prix,
                         v=_signe(r.croissance_volume_pct))
            if e.croissance_banque_mondiale_pct == e.croissance_banque_mondiale_pct:  # non NaN
                texte += _lab("ib_vol_bm", v=_signe(e.croissance_banque_mondiale_pct),
                              e=_nombre(abs(e.ecart_banque_mondiale_points), 2))
            if a in jonctions:
                texte += " — " + _texte_jonction_volume(jonctions[a])
        figtools.infobulle(p, texte)
    _cadre(ax, _lab("y_vol"), int(ench["annee"].min()), int(ench["annee"].max()))
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(ymin, ymax + 0.16 * (ymax - ymin))   # la place des étiquettes de jonction
    # Les jonctions : trait vertical, étiquette qui dit ce qui change, infobulle.
    for i, j in enumerate(_jonctions_volume()):
        trait = figtools.marque_rupture(ax, j["annee"])
        quoi = _lab(j["type"])
        figtools.infobulle(trait, _texte_jonction_volume(j))
        gauche = j["type"] == "j_source" and i == 0   # 1970, serrée contre 1971
        ax.annotate(figtools.fig_text(_lab("j_etiquette", a=j["annee"], t=quoi)),
                    xy=(j["annee"] - 0.5, 1), xycoords=("data", "axes fraction"),
                    xytext=(-3 if gauche else 3, -4 - 10 * (i % 3)),
                    textcoords="offset points", ha="right" if gauche else "left", va="top",
                    fontsize=6.8, color=GRIS)
    poignees = [
        Line2D([], [], color=SARCELLE, ls="-", lw=1.6,
               label=figtools.fig_text(_lab("vol_retenu"))),
        Line2D([], [], color=GRIS, marker="x", ls="-", lw=0.7, ms=4.2,
               label=figtools.fig_text(_lab("vol_bm"))),
        Patch(color="#eaeef2", label=figtools.fig_text(_lab("vol_divergence"))),
        Line2D([], [], color="none", label=figtools.fig_text(_lab("vol_tn"))),
        Line2D([], [], color=BRUN, marker="v", ls="", ms=4.4,
               label=figtools.fig_text(_lab("vol_non_dite"))),
    ]
    poignees += [Line2D([], [], color=st["couleur"], marker=st["marker"], ls="", ms=4.4,
                        label=figtools.fig_text(_base(b))) for b, st in BASES.items()]
    poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", ls="", ms=4.4,
                           label=figtools.fig_text(_lab("retropole_court"))))
    _legende(ax, poignees, ncol=3)
    fig.tight_layout()
    return fig


def fig_nominal_volume():
    """Les deux indices enchaînés, 2015 = 100 : aux prix courants et en volume."""
    figtools.apply_lang_font()
    nominal = _variante("enchainee")
    volume = _volume_enchaine()
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    ax.plot(nominal["annee"], nominal["indice_2015_100"], ls="-", lw=1.9, color=VIOLET, zorder=3)
    ax.plot(volume["annee"], volume["indice_volume_2015_100"], ls="-.", lw=1.9, color=SARCELLE,
            zorder=3)
    for d, col, coul, marque, cle in (
            (nominal, "indice_2015_100", VIOLET, "o", "ind_nominal_court"),
            (volume, "indice_volume_2015_100", SARCELLE, "D", "ind_volume_court")):
        for r in d[d["annee"] % 5 == 0].itertuples(index=False):
            v = float(getattr(r, col))
            p, = ax.plot([r.annee], [v], marque, ms=4, color=coul, mfc="white", zorder=4)
            figtools.infobulle(p, _lab("ib_indice", a=int(r.annee), s=_lab(cle),
                                       v=_nombre(v, 2)))
    _cadre(ax, _lab("y_indices"), int(volume["annee"].min()), int(volume["annee"].max()))
    _echelle_log(ax, [0.5, 1, 2, 5, 10, 20, 50, 100, 200])
    poignees = [
        Line2D([], [], color=VIOLET, ls="-", lw=1.9, marker="o", mfc="white", ms=4,
               label=figtools.fig_text(_lab("ind_nominal"))),
        Line2D([], [], color=SARCELLE, ls="-.", lw=1.9, marker="D", mfc="white", ms=4,
               label=figtools.fig_text(_lab("ind_volume"))),
    ]
    _legende(ax, poignees, ncol=1)
    fig.tight_layout()
    return fig


def vues_volume():
    return [(_lab("vue_volume"), fig_volume()),
            (_lab("vue_nominal_volume"), fig_nominal_volume())]


def table_volume():
    """Tous les taux en volume, l'indice de volume enchaîné et l'indice aux prix courants tracé.

    Les lignes de `pib-croissance-volume`, puis celles de `pib-volume-enchaine`, sans rien
    retrancher ; puis la variante enchaînée de `pib-courant-enchaine`, que la seconde vue trace.
    """
    import pandas as pd
    v = _volume().copy()
    v.insert(1, "serie", SERIE_VOLUME)
    e = _volume_enchaine().copy()
    e.insert(1, "serie", SERIE_VOLUME_ENCHAINE)
    n = _variante("enchainee")[["annee", "construction", "indice_2015_100", "croissance_pct",
                                "base_du_taux"]].copy()
    n = n.rename(columns={"indice_2015_100": "indice_nominal", "croissance_pct": "taux_nominal",
                          "base_du_taux": "base"})
    n.insert(1, "serie", SERIE_ENCHAINE)
    d = _lisible(pd.concat([v, e, n], ignore_index=True))
    colonnes = {
        "annee": "col_annee", "serie": "col_serie", "source": "col_source",
        "famille": "col_famille", "base": "col_base", "annee_de_prix": "col_prix",
        "croissance_volume_pct": "col_taux_vol", "mode": "col_mode",
        "taux_imprime_pct": "col_taux_imprime", "retropole": "col_retropole",
        "publication": "col_publication", "indice_volume_2015_100": "col_indice_vol",
        "jonction": "col_jonction", "construction": "col_construction",
        "croissance_banque_mondiale_pct": "col_taux_bm",
        "ecart_banque_mondiale_points": "col_ecart_bm", "indice_nominal": "col_indice_nominal",
        "taux_nominal": "col_taux_nominal", "provenance": "col_provenance", "note": "col_note",
    }
    oubliees = set(d.columns) - set(colonnes)
    if oubliees:
        raise KeyError(f"colonnes sans libellé : {sorted(oubliees)}")
    return d[list(colonnes)].rename(columns={k: _lab(v) for k, v in colonnes.items()})

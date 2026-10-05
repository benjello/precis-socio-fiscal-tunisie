"""Régénère les snapshots Markdown des tableaux de paramètres du livre « Retraites ».

Même contrat que les trois générateurs qui précèdent : le build du site n'exécute PAS ce
script, il lit les fichiers qu'il produit, versionnés dans `precis/{fr,ar}/retraites/tables/`.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_retraites_tables.py

Les paramètres de retraite vivent dans l'arbre unique d'openfisca-tunisia depuis sa version
0.93, qui y a fusionné openfisca-tunisia-pension. En deçà, `parameters/retraite/` n'existe
pas et le garde-fou de version refuse la génération.

Les deux langues sont produites ici, et non par la pipeline de traduction : ces tableaux
sont des données, pas de la prose. Seuls les en-têtes et les libellés changent d'une langue
à l'autre ; les valeurs, les dates et les clés de citation sortent du même paramètre.

CE QUE CES TABLEAUX DISENT, ET CE QU'ILS NE DISENT PAS
------------------------------------------------------
Ils donnent des **niveaux datés** — un âge, un taux, un montant, une fraction du salaire
minimum — et le texte qui fixe chacun. Ils ne donnent pas les conditions qui entourent ces
niveaux : la durée de 35 ans de services qui s'ajoute à l'âge des fonctions astreignantes,
le caractère facultatif du maintien en activité, la nature de la prestation servie aux
carrières courtes. Ces règles sont dans la prose du chapitre, à l'endroit où le tableau
paraît, et le tableau ne s'y substitue pas.

PLUSIEURS TABLEAUX DU LIVRE RESTENT ÉCRITS À LA MAIN — la liste complète est dans
`docs/notes/recension-parametres-en-dur.md` —, parmi lesquels les cinq ci-dessous, et ce
n'est pas un retard : les paramètres ne portent pas la distinction que leurs colonnes affirment. Celui des âges militaires est
engendré depuis le 20 septembre 2026 ; ceux du salaire de référence et des survivants du
régime non agricole, et celui de l'évolution du régime agricole, depuis le 3 octobre 2026,
comme TABLEAUX MIXTES (`ot.tableau_gabarit`) : le texte de chaque case reste celui du
chapitre, et chaque valeur y est lue dans le paramètre, à la date qui la fonde. C'est ce qui
manquait pour engendrer un tableau dont la démonstration tient à ses règles — le CHOIX entre
deux périodes de 1974, la NON-MODIFICATION de l'article 19 en 1990, le sort de la réversion
au remariage. Voir `tableaux_lot_a`.

- `tbl-cnrps-bonifications` : les paramètres `bonifications/cadre_actif/service_*` portent
  bien le barème 5 / 4 / 3 / 2, mais non la distinction des trois catégories de l'article 32
  — bonification fixe pour les ouvriers, période restant à courir **plafonnée par ce barème**
  pour les cadres actifs, période restant à courir **sans plafond** pour les fonctions
  astreignantes. Engendrer la seule colonne des ouvriers perdrait les deux autres. Le seul
  élément versable de cet article est le repère d'âge — soixante ans, porté à soixante-deux
  par la loi n° 2019-37 —, dont la date d'effet n'est pas établie : l'article premier de
  cette loi fixe un calendrier propre aux âges civils qui ne vaut pas pour son article 2.
- `tbl-cnrps-orphelins` : les conditions d'âge et d'études de la pension d'orphelin ne sont
  pas des valeurs. Le seul paramètre du sujet, `survivants/taux_orphelin`, porte le taux de
  10 % — que ce tableau ne donne pas — et ces conditions dans sa `documentation`.
- `tbl-rsna-anticipes` : l'arbre porte désormais les DURÉES et les TAUX des départs
  anticipés — stages de 360 et 180 mois, décote par trimestre, jouissance à 55 ans de
  l'article 15 ter (PR openfisca-tunisia-pension#52). Ce que ses colonnes affirment reste
  hors de portée : les CONDITIONS de chaque cas — approbation du licenciement par la
  commission de contrôle, inscription au bureau de l'emploi, constat de l'usure, nombre
  d'enfants vivants — sont des faits de situation, non des valeurs datées.
- `tbl-rsna-revalo-montant` et `tbl-rsna-revalo-taux` : la série du SMIG est datée et sourcée
  chez `openfisca-tunisia`, et le cœur chiffré de ces deux tableaux en sortirait. Mais leur
  objet n'est pas le SMIG : c'est la **revalorisation des pensions**, et le paramètre ne
  porte ni la distinction entre la majoration en somme (1980-2000) et la majoration en taux
  (depuis 2001), ni les dates d'effet propres aux pensions — le 1er janvier 2001 pour la
  hausse du SMIG du 1er mai 2000 —, ni les hausses assimilées de 1981 et 1982, ni les
  indemnités spéciales de 1989 et 1991, qui ne sont pas des hausses du SMIG, ni les lignes
  dont la source n'a pas été vérifiée au Journal officiel.

DEUX TABLEAUX À LA MAIN ONT, DEPUIS LE 24 SEPTEMBRE 2026, DES COMPAGNONS ENGENDRÉS : ils
mêlent des règles et des valeurs, et restent à la main pour les règles ; leurs seules lignes
chiffrées sont engendrées à côté.

- `tbl-cnrps-1959-1985` : `cnrps_1959_1985.md` — plafond, maximum d'annuités, plancher
  (rédigé en règle : « traitement de l'indice 100 », « 60 % des émoluments de l'indice
  100 »), réversion et pension d'orphelin, du 1er avril 1959 au 12 septembre 1985.
- `tbl-rtns-coeur` : `rtns_vieillesse.md`, `rtns_agricole.md` et `rtns_classes.md` — les
  états de 1982 et de 1989, qui prennent fin le 19 juillet 1995 par une valeur nulle,
  enchaînés à ceux du décret n° 95-1166 (`enchaine`). Une case vide dit l'absence de
  règle — classe pas encore créée, allocation de vieillesse agricole abrogée —, jamais un
  zéro.
"""

from __future__ import annotations

import datetime
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

ot.utiliser_paquet("openfisca_tunisia")

PAQUET = "openfisca_tunisia"
CNRPS = "parameters/retraite/cnrps"
RSNA = "parameters/retraite/rsna"
RACINE = Path(__file__).parent.parent / "precis"
LANGUES = ("fr", "ar")

# En-têtes de colonnes et libellés. Les équivalents arabes des notions sont ceux du
# glossaire bilingue (`precis/glossaire.yml`), source unique des deux langues.
MOTS = {
    "fr": {
        "effet": "Effet",
        "texte": "Texte",
        # Les en-têtes portent l'ancre du glossaire, comme le faisaient les cellules du
        # tableau écrit à la main : l'ancre `#g-<id>` est commune aux deux langues.
        "cadre_commun": "Cadre commun (art. 24)",
        "penibles": "[Travaux pénibles et insalubres](#g-travaux-penibles-insalubres) (art. 27)",
        "astreignantes": "[Fonctions astreignantes](#g-fonctions-astreignantes) (art. 28)",
        "cadres_actifs": "[Cadres actifs](#g-cadres-actifs) (art. 29)",
        "superieur": "Enseignants du supérieur (art. 29 bis)",
        "mil_troupe": "Hommes de troupe, quartiers-maîtres et matelots",
        "mil_sous_officiers": "Sous-officiers et officiers mariniers",
        "mil_subalternes": "Officiers subalternes",
        "mil_superieurs": "Officiers supérieurs",
        "mil_generaux": "Officiers généraux",
        "tranche_services": "Tranche de services",
        "bareme_annuites": "Barème des annuités",
        "par_an": "Par année",
        "par_trimestre": "Par trimestre",
        "cumul": "Taux cumulé en fin de tranche",
        "plafond": "Plafond du taux de la pension",
        "minimum": "[Pension minimale garantie](#g-pension-minimale-garantie)",
        "allocation_vieillesse": "[Allocation de vieillesse](#g-allocation-de-vieillesse)",
        "allocation_duree": "Allocation de vieillesse : services requis",
        "enfant1": "1^er^ enfant",
        "enfant2": "2^e^ enfant",
        "enfant3": "3^e^ enfant",
        "enfant4": "4^e^ enfant (droits acquis avant 1989)",
        "plancher_sup": "Pension de vieillesse ou d'invalidité",
        "plancher_inf": ("Retraite anticipée (art. 15 bis a et b) et "
                         "[pension proportionnelle](#g-pension-proportionnelle)"),
        "intervalle": "{bas} à {haut}",
        "au_dela": "au-delà de {bas}",
        "smig": "du SMIG",
        "vide": "—",
        # Pensions civiles, de la loi n° 59-18 à la loi n° 85-12.
        "max_annuites": "Maximum d'[annuités liquidables](#g-annuite-liquidable)",
        "plancher": "Plancher de la pension",
        "reversion": "[Réversion](#g-pension-de-reversion) au conjoint",
        "orphelin": "[Pension d'orphelin](#g-pension-temporaire-orphelin), par orphelin",
        "indice_100": {"traitement": "traitement de l'indice 100",
                       "emoluments": "émoluments de l'indice 100"},
        "des": "{taux} des {base}",
        "plancher_1959": ("{pleine} ({n} annuités) ; {taux} du traitement par annuité, "
                          "dans la même limite (moins de {n} annuités)"),
        # Travailleurs non salariés.
        "rtns_age": "Âge",
        "rtns_anticipe": "Départ avec [décote](#g-decote)",
        "rtns_anticipe_cellule": "dès {age}, {taux} par trimestre",
        "rtns_stage": "[Stage](#g-stage-cotisation)",
        "rtns_taux": "Taux au terme du stage",
        "rtns_majoration": "Majoration par trimestre au-delà du stage",
        "rtns_minimum": "Pension minimale",
        "smig_ou_smag": "du SMIG ou du SMAG",
        "rtns_allocation": "[Allocation de vieillesse](#g-allocation-de-vieillesse), ouverte dès",
        "rtns_jours_smag": "[SMAG](#g-smag) du revenu de référence, rapporté à une durée annuelle de",
        "classe": "Classe {k}",
        "assiette": "[Classes de revenus](#g-classe-de-revenus)",
        "assiette_dinars": "[revenu forfaitaire](#g-revenu-forfaitaire) annuel, en dinars",
        "assiette_smig": "multiple du SMIG",
        "assiette_smig_smag": "multiple du SMIG ou du SMAG",
    },
    "ar": {
        "effet": "بداية السريان",
        "texte": "النصّ",
        "cadre_commun": "الإطار العام (الفصل 24)",
        "penibles": "[الأشغال الشاقّة وغير الصحّية](#g-travaux-penibles-insalubres) (الفصل 27)",
        "astreignantes": "[الوظائف المرهقة](#g-fonctions-astreignantes) (الفصل 28)",
        "cadres_actifs": "[الأسلاك النشيطة](#g-cadres-actifs) (الفصل 29)",
        "superieur": "أساتذة التعليم العالي (الفصل 29 مكرّر)",
        "mil_troupe": "رجال الجيش، رؤساء عرفاء وبحارة",
        "mil_sous_officiers": "ضباط الصف وضباط البحرية",
        "mil_subalternes": "الضباط الأعوان",
        "mil_superieurs": "الضباط السامون",
        "mil_generaux": "الضباط العامون",
        "tranche_services": "شريحة الخدمات",
        "bareme_annuites": "جدول نسب السنوات القابلة للتصفية",
        "par_an": "عن كلّ سنة",
        "par_trimestre": "عن كلّ ثلاثية",
        "cumul": "النسبة المتراكمة في نهاية الشريحة",
        "plafond": "سقف نسبة تصفية الجراية",
        "minimum": "[الجراية الدنيا المضمونة](#g-pension-minimale-garantie)",
        "allocation_vieillesse": "[منحة الشيخوخة](#g-allocation-de-vieillesse)",
        "allocation_duree": "منحة الشيخوخة: الخدمات المستوجبة",
        "enfant1": "الطفل الأوّل",
        "enfant2": "الطفل الثاني",
        "enfant3": "الطفل الثالث",
        "enfant4": "الطفل الرابع (حقوق مكتسبة قبل 1989)",
        "plancher_sup": "جراية الشيخوخة أو العجز",
        "plancher_inf": ("التقاعد المبكّر (الفصل 15 مكرّر أ وب) و"
                         "[الجراية النسبية](#g-pension-proportionnelle)"),
        "intervalle": "من {bas} إلى {haut}",
        "au_dela": "ما يفوق {bas}",
        "smig": "من الأجر الأدنى المضمون",
        "vide": "—",
        "max_annuites": "الحدّ الأقصى من [السنوات القابلة للتصفية](#g-annuite-liquidable)",
        "plancher": "الحدّ الأدنى للجراية",
        "reversion": "[جراية القرين الباقي على قيد الحياة](#g-pension-de-reversion)",
        "orphelin": "[الجراية الوقتية لليتيم](#g-pension-temporaire-orphelin)، عن كلّ يتيم",
        "indice_100": {"traitement": "المرتب التابع للرقم القياسي 100",
                       "emoluments": "المرتبات التابعة للرقم القياسي 100"},
        "des": "{taux} من {base}",
        "plancher_1959": ("{pleine} ({n} سنة قابلة للتصفية)؛ {taux} من المرتب عن كلّ سنة "
                          "قابلة للتصفية، في حدود المقدار نفسه (أقلّ من {n} سنة)"),
        "rtns_age": "السنّ",
        "rtns_anticipe": "التقاعد المبكّر مع [التخفيض في الجراية](#g-decote)",
        "rtns_anticipe_cellule": "ابتداءً من {age}، {taux} عن كلّ ثلاثية",
        "rtns_stage": "[مدة الانخراط الدنيا](#g-stage-cotisation)",
        "rtns_taux": "النسبة عند استيفاء مدة الانخراط الدنيا",
        "rtns_majoration": "الترفيع عن كلّ ثلاثية تفوق مدة الانخراط الدنيا",
        "rtns_minimum": "الجراية الدنيا",
        "smig_ou_smag": "من الأجر الأدنى المضمون أو من الأجر الأدنى الفلاحي المضمون",
        "rtns_allocation": "[منحة الشيخوخة](#g-allocation-de-vieillesse)، ابتداءً من",
        "rtns_jours_smag": "[الأجر الأدنى الفلاحي المضمون](#g-smag) المعتمد للدخل المرجعي، محسوبًا على أساس مدة سنوية قدرها",
        "classe": "الشريحة {k}",
        "assiette": "[شرائح الدخل](#g-classe-de-revenus)",
        "assiette_dinars": "[الدخل التقديري](#g-revenu-forfaitaire) السنوي، بالدينار",
        "assiette_smig": "مضاعف الأجر الأدنى المضمون",
        "assiette_smig_smag": "مضاعف الأجر الأدنى المضمون أو الأجر الأدنى الفلاحي المضمون",
    },
}

# Les noms comptés, l'accord arabe et les formateurs de cellules sont communs aux
# générateurs : `ot.compte`, `ot.annees`, `ot.formateurs`.


# Clés de citation du précis, par date d'effet : elles raccrochent chaque rupture à la
# bibliographie du livre, identique dans les deux langues. Toute date d'effet d'un paramètre
# lu doit y figurer — à défaut, la colonne « Texte » reprendrait le titre du paramètre, long
# de cent cinquante caractères. `verifie_texte` le contrôle avant d'écrire le snapshot.
CLES_AGES = {
    "1959-04-01": "loi59-18, art. 9, § I, et 52",
    "1985-09-12": "loi85-12, art. 24 et 27 à 29",
    "2009-04-19": "loi2009-20, art. 2",
    "2019-07-01": "loi2019-37, art. 5",
    "2020-01-01": "loi2019-37, art. 1 et 5",
}
CLES_MILITAIRES = {
    "1985-09-12": "loi85-12, art. 61",
    "1989-01-01": "loi88-71, art. 1",
    # Les deux paliers du calendrier transitoire de 2019, comme pour les âges civils : un an
    # de plus au 1er juillet 2019 (art. 5), puis les âges de l'article 61 nouveau (art. 1).
    "2019-07-01": "loi2019-37, art. 5",
    "2020-01-01": "loi2019-37, art. 1 et 5",
}
CLES_PLAFOND_PLANCHER = {
    "1959-04-01": "loi59-18, art. 22, § II, et 52",
    "1970-07-01": "decretloi70-1, art. 1 et 2",
    "1981-05-01": "loi81-70, art. 4-5",
    "1985-09-12": "loi85-12, art. 38, 39 et 42",
}
CLES_INDEMNITES = {
    "1986-05-01": "decret86-611, art. 1 et 3",
    "1989-01-01": "decret88-1136, art. 1-2 ; @loi88-39",
    "1996-11-01": "decret96-1906, art. 1 à 5",
}
CLES_RSNA_PLANCHERS = {
    "1974-01-01": "decret74-499, art. 45",
    "1982-07-22": "decret82-1030, art. 3 et 5",
}
# Pensions civiles, de la loi n° 59-18 à la loi n° 85-12 : les lignes chiffrées du tableau
# `tbl-cnrps-1959-1985`, que ce tableau-ci accompagne sans le remplacer.
CLES_CNRPS_1959_1985 = {
    "1959-04-01": "loi59-18, art. 20, § III, 22, § II, 31 et 52 ; @loi59-100, art. 1",
    "1970-07-01": "decretloi70-1, art. 1 et 2",
    "1981-05-01": "loi81-70, art. 4-5",
    "1985-09-12": "loi85-12, art. 35, 38, 39, 43 et 45",
}
# La rémunération de l'indice 100 à laquelle le plancher se rapporte change de nom avec le
# décret-loi n° 70-1 : le traitement soumis à retenue, puis les émoluments globaux
# indiciaires. La valeur ne le dit pas — 1 et 0,6 d'une même unité — : la base se lit donc
# à la date, et une date d'effet inconnue ici arrête la génération plutôt que de recevoir
# la base de la ligne précédente.
BASE_INDICE_100 = {"1959-04-01": "traitement", "1970-07-01": "emoluments"}
# Travailleurs non salariés : les lignes chiffrées du tableau `tbl-rtns-coeur`.
CLES_RTNS_VIEILLESSE = {
    "1982-07-01": "decret82-1359, art. 18, 20, 22 et 26",
    "1995-07-19": "decret95-1166, art. 23, 24, 26, 29 et 39",
}
CLES_RTNS_AGRICOLE = {
    "1982-07-01": "decret82-1360, art. 8, 17 et 18",
    "1995-07-19": "decret95-1166, art. 7, 24, 25 et 39",
    # Le SMAG rapporté à 180, 260 puis 300 jours, à titre transitoire : dérogation au
    # décret n° 95-1166, exécutoire le 19 octobre 1996.
    "1996-10-19": "decret-96-1797, art. 1",
    "1997-01-01": "decret-96-1797, art. 1",
    "1998-01-01": "decret-96-1797, art. 1",
}
CLES_RTNS_CLASSES = {
    "1982-07-01": "decret82-1359, art. 7 et 26",
    "1989-10-22": "decret89-1611, art. 1",
    "1995-07-19": "decret95-1166, art. 7",
}
RTNS = "parameters/retraite/rtns"
RTNS_NA = f"{RTNS}/avant_1995/non_agricole"
RTNS_AG = f"{RTNS}/avant_1995/agricole"


# Libellés des liens « Base législative » des tableaux à séries enchaînées. Une même colonne
# lit deux paramètres — l'état de 1982 et celui du régime fusionné de 1995 — : chacun a
# son libellé, sans quoi l'onglet afficherait deux fois « Stage ».
LIENS = {
    "fr": {
        "avant": "{grandeur}, secteur non agricole, du 1er juillet 1982 au 18 juillet 1995",
        "avant_ag": "{grandeur}, secteur agricole, du 1er juillet 1982 au 18 juillet 1995",
        "depuis": "{grandeur}, deux secteurs, depuis le 19 juillet 1995",
        "age": "Âge d'ouverture du droit à pension de vieillesse",
        "anticipe": "Âge du départ avec décote",
        "decote": "Décote par trimestre d'anticipation",
        "stage": "Stage",
        "taux": "Taux de la pension au terme du stage",
        "majoration": "Majoration par trimestre au-delà du stage",
        "plafond": "Plafond du taux de la pension",
        "minimum": "Pension minimale",
        "allocation": "Durée de cotisation ouvrant l'allocation de vieillesse",
        "jours_smag": "Durée annuelle à laquelle le SMAG du revenu de référence est rapporté",
        "classes_dinars": "Classes de revenus en dinars, du 1er juillet 1982 au 21 octobre 1989",
        "classes_smig": "Classes de revenus en multiples du SMIG, du 22 octobre 1989 au "
                        "18 juillet 1995",
        "classes_1995": "Classes de revenus en multiples du SMIG ou du SMAG, depuis le "
                        "19 juillet 1995",
        "cnrps_max": "CNRPS — maximum d'annuités liquidables",
        "cnrps_part": "CNRPS — pension minimale, en part de la rémunération de l'indice 100",
        "cnrps_pleine": "CNRPS — annuités de la pension dont le plancher est la rémunération "
                        "de l'indice 100",
        "cnrps_prop": "CNRPS — plancher des pensions proportionnelles, par annuité",
        "cnrps_minimum": "CNRPS — pension minimale garantie, en fraction du SMIG",
        "cnrps_reversion": "CNRPS — taux de la pension de réversion du conjoint",
        "cnrps_orphelin": "CNRPS — taux de la pension d'orphelin",
    },
    "ar": {
        "avant": "{grandeur}، القطاع غير الفلاحي، من 1 جويلية 1982 إلى 18 جويلية 1995",
        "avant_ag": "{grandeur}، القطاع الفلاحي، من 1 جويلية 1982 إلى 18 جويلية 1995",
        "depuis": "{grandeur}، القطاعان، ابتداءً من 19 جويلية 1995",
        "age": "سنّ استحقاق جراية الشيخوخة",
        "anticipe": "سنّ التقاعد المبكّر مع التخفيض في الجراية",
        "decote": "التخفيض في الجراية عن كلّ ثلاثية",
        "stage": "مدة الانخراط الدنيا",
        "taux": "نسبة الجراية عند استيفاء مدة الانخراط الدنيا",
        "majoration": "الترفيع عن كلّ ثلاثية تفوق مدة الانخراط الدنيا",
        "plafond": "سقف نسبة الجراية",
        "minimum": "الجراية الدنيا",
        "allocation": "مدة الاشتراك التي تفتح الحقّ في منحة الشيخوخة",
        "jours_smag": "المدة السنوية التي يُحتسب على أساسها الأجر الأدنى الفلاحي المضمون المعتمد للدخل المرجعي",
        "classes_dinars": "شرائح الدخل بالدينار، من 1 جويلية 1982 إلى 21 أكتوبر 1989",
        "classes_smig": "شرائح الدخل بمضاعفات الأجر الأدنى المضمون، من 22 أكتوبر 1989 "
                        "إلى 18 جويلية 1995",
        "classes_1995": "شرائح الدخل بمضاعفات الأجر الأدنى المضمون أو الأجر الأدنى الفلاحي "
                        "المضمون، ابتداءً من 19 جويلية 1995",
        "cnrps_max": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — الحدّ الأقصى من السنوات "
                     "القابلة للتصفية",
        "cnrps_part": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — الجراية الدنيا، كسرًا من "
                      "المرتب التابع للرقم القياسي 100",
        "cnrps_pleine": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — عدد السنوات التي "
                        "يكون حدّها الأدنى المرتب التابع للرقم القياسي 100",
        "cnrps_prop": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — الحدّ الأدنى للجرايات "
                      "النسبية، عن كلّ سنة قابلة للتصفية",
        "cnrps_minimum": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — الجراية الدنيا "
                         "المضمونة، كسرًا من الأجر الأدنى المضمون",
        "cnrps_reversion": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — نسبة جراية القرين "
                           "الباقي على قيد الحياة",
        "cnrps_orphelin": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — نسبة الجراية الوقتية "
                          "لليتيم",
    },
}


def tableaux(langue):
    m = MOTS[langue]
    f = ot.formateurs(langue)
    age, taux, dinars, part_smig = f.age, f.taux, f.millimes, f.part_smig
    annees, compte, en_vigueur, enchaine, cellule = (
        ot.annees, ot.compte, ot.en_vigueur, ot.enchaine, ot.cellule)
    datee = dict(langue=langue, colonne_periode=m["effet"], colonne_texte=m["texte"])

    def ages():
        """L'âge de mise à la retraite par catégorie, depuis le 1er avril 1959.

        Le tableau suit les paramètres tels qu'ils sont datés : le cadre commun depuis la loi
        n° 59-18 (art. 9, § I, applicable au 1er avril 1959, art. 52), les autres catégories
        depuis la loi n° 85-12. Une catégorie sans valeur à une date reste vide : pour les
        cadres actifs avant 1985, l'âge dépendait des décrets de classement de l'article 10
        de la loi de 1959, qui ne sont pas versés.
        """
        specs = [
            (f"{CNRPS}/age_legal/civil/cadre_commun.yaml", m["cadre_commun"], age),
            (f"{CNRPS}/age_legal/civil/ouvriers_travaux_penibles.yaml", m["penibles"], age),
            (f"{CNRPS}/age_legal/civil/fonctions_astreignantes/age.yaml", m["astreignantes"], age),
            (f"{CNRPS}/age_legal/civil/cadres_actifs.yaml", m["cadres_actifs"], age),
            (f"{CNRPS}/age_legal/civil/enseignants_du_superieur.yaml", m["superieur"], age),
        ]
        return ot.tableau_evolution_datee(specs, cles=CLES_AGES, **datee)

    def annuites():
        """Le barème des annuités de l'article 38, lu comme un barème à tranches.

        Le paramètre compte en TRIMESTRES : la tranche se rend en années, le taux annuel
        est le quadruple du taux trimestriel, et le taux cumulé en fin de tranche est la
        somme des taux de toutes les tranches parcourues. La dernière tranche, de taux nul,
        n'est pas un oubli : c'est ainsi que le barème rencontre le plafond de 90 % au
        terme de quarante années, sans qu'aucun autre paramètre ait à l'imposer.
        """
        import pandas as pd

        tranches = ot.bareme_a_la_date(
            f"{CNRPS}/bareme_annuite.yaml", datetime.date(1985, 9, 12)
        )
        ot.releve_note(f"{CNRPS}/bareme_annuite.yaml", m["bareme_annuites"])
        if not tranches:
            return None
        lignes, cumul = [], 0.0
        for indice, (seuil, trimestriel) in enumerate(tranches):
            suivant = tranches[indice + 1][0] if indice + 1 < len(tranches) else None
            # Le nom compté porte l'accord sur la borne haute : « 0 à 10 ans », et en arabe
            # « من 0 إلى 10 سنوات » — pluriel à dix, singulier à vingt.
            if suivant is None:
                libelle = m["au_dela"].format(bas=annees(int(seuil // 4), langue))
            else:
                libelle = m["intervalle"].format(
                    bas=int(seuil // 4), haut=annees(int(suivant // 4), langue)
                )
                cumul += (suivant - seuil) * trimestriel
            lignes.append({
                m["tranche_services"]: libelle,
                m["par_an"]: taux(trimestriel * 4),
                m["par_trimestre"]: taux(trimestriel),
                m["cumul"]: taux(cumul),
            })
        return pd.DataFrame(lignes)

    lien = LIENS[langue]
    enchainee = dict(langue=langue, colonne_periode=m["effet"], colonne_texte=m["texte"])

    coefficient, en_dinars = f.coefficient, f.dinars

    def rtns_vieillesse():
        """La pension de vieillesse des non-salariés : secteur non agricole, puis régime fusionné.

        Chaque colonne lit deux paramètres : l'état du décret n° 82-1359, qui prend fin le
        19 juillet 1995, et celui du décret n° 95-1166, qui commence ce jour-là. Le secteur
        agricole n'a pas de colonne avant 1995 : son taux, son stage et son plafond viennent
        de la loi n° 81-6 par renvoi, et ne sont pas des grandeurs du décret n° 82-1360.
        """
        fichiers = {  # grandeur : (état de 1982, état de 1995)
            "age": ("age_legal", "age_legal"),
            "anticipe": ("age_depart_anticipe", "age_depart_anticipe"),
            "decote": ("decote_par_trimestre", "decote_par_trimestre"),
            "stage": ("stage_mois", "stage_trimestres"),
            "taux": ("taux_base", "taux_base"),
            "majoration": ("majoration_par_trimestre", "majoration_par_trimestre"),
            "plafond": ("plafond_taux", "plafond_taux"),
            "minimum": ("plancher_taux", "plancher_taux"),
        }
        chemins = {g: (f"{RTNS_NA}/{a}.yaml", f"{RTNS}/{d}.yaml")
                   for g, (a, d) in fichiers.items()}
        lectures = []
        for g, (avant, depuis) in chemins.items():
            lectures += [(avant, lien["avant"].format(grandeur=lien[g])),
                         (depuis, lien["depuis"].format(grandeur=lien[g]))]

        def paire(g, formateur_avant, formateur_depuis=None):
            avant, depuis = chemins[g]
            return cellule((avant, formateur_avant), (depuis, formateur_depuis or formateur_avant))

        def anticipe(series, date):
            a = paire("anticipe", age)(series, date)
            d = paire("decote", taux)(series, date)
            if m["vide"] in (a, d):
                return m["vide"]
            return m["rtns_anticipe_cellule"].format(age=a, taux=d)

        colonnes = [
            (m["rtns_age"], paire("age", age)),
            (m["rtns_anticipe"], anticipe),
            (m["rtns_stage"], paire("stage", lambda v: compte(int(v), "mois", langue),
                                    lambda v: compte(int(v), "trimestres", langue))),
            (m["rtns_taux"], paire("taux", taux)),
            (m["rtns_majoration"], paire("majoration", taux)),
            (m["plafond"], paire("plafond", taux)),
            # Moitié du SMIG en 1982, trente pour cent du salaire minimum du secteur depuis
            # 1995 : le texte de 1995 ne l'écrit pas en fraction.
            (m["rtns_minimum"], paire("minimum", part_smig,
                                      lambda v: f"{ot.formate_taux(v)} {m['smig_ou_smag']}")),
        ]
        return ot.tableau_enchaine(lectures, colonnes, CLES_RTNS_VIEILLESSE, **enchainee)

    def rtns_agricole():
        """Le secteur agricole : l'âge, puis l'allocation de vieillesse, abrogée en 1995.

        L'allocation n'a pas de successeur dans le régime fusionné, qui sert aux carrières
        inférieures au stage un versement unique (décret n° 95-1166, art. 28) : sa case de
        1995 reste vide, et la ligne « Source : » du chapitre le dit.
        """
        age_ag, age_95 = f"{RTNS_AG}/age_legal.yaml", f"{RTNS}/age_legal.yaml"
        allocation = f"{RTNS_AG}/allocation_vieillesse_trimestres.yaml"
        jours_ag = f"{RTNS_AG}/jours_annuels_smag.yaml"
        jours_95 = f"{RTNS}/revenu_reference/jours_annuels_smag.yaml"
        lectures = [
            (age_ag, lien["avant_ag"].format(grandeur=lien["age"])),
            (age_95, lien["depuis"].format(grandeur=lien["age"])),
            (allocation, lien["avant_ag"].format(grandeur=lien["allocation"])),
            (jours_ag, lien["avant_ag"].format(grandeur=lien["jours_smag"])),
            (jours_95, lien["depuis"].format(grandeur=lien["jours_smag"])),
        ]
        jours = lambda v: compte(int(v), "jours", langue)  # noqa: E731
        colonnes = [
            (m["rtns_age"], cellule((age_ag, age), (age_95, age))),
            (m["rtns_allocation"],
             cellule((allocation, lambda v: compte(int(v), "trimestres", langue)))),
            (m["rtns_jours_smag"], cellule((jours_ag, jours), (jours_95, jours))),
        ]
        return ot.tableau_enchaine(lectures, colonnes, CLES_RTNS_AGRICOLE, **enchainee)

    def rtns_classes():
        """Les classes de revenus : six en dinars (1982), neuf en SMIG (1989), dix (1995).

        Une colonne par rang de classe, qui lit jusqu'à trois barèmes successifs ; la
        colonne « Assiette » dit lequel est en vigueur. Une classe qui n'existe pas encore
        reste vide. Un lien par barème, et non par classe : chaque nœud se lit en un
        tableau.
        """
        noeuds = (
            (f"{RTNS_NA}/classes_dinars", 6, en_dinars, "assiette_dinars", "classes_dinars"),
            (f"{RTNS_NA}/classes_smig", 9, coefficient, "assiette_smig", "classes_smig"),
            (f"{RTNS}/revenu_reference/classes", 10, coefficient, "assiette_smig_smag",
             "classes_1995"),
        )
        lectures = []
        for noeud, nombre, _f, _a, cle in noeuds:
            ot.releve_note(noeud, lien[cle])
            lectures += [(f"{noeud}/classe_{k}.yaml", None) for k in range(1, nombre + 1)]

        def assiette(series, date):
            valeur, cle = enchaine(
                [(series[f"{n}/classe_1.yaml"], a) for n, _k, _f, a, _c in noeuds], date)
            return m["vide"] if valeur is None else m[cle]

        colonnes = [(m["assiette"], assiette)]
        for k in range(1, 11):
            segments = [(f"{n}/classe_{k}.yaml", f) for n, nombre, f, _a, _c in noeuds
                        if k <= nombre]
            colonnes.append((m["classe"].format(k=k), cellule(*segments)))
        return ot.tableau_enchaine(lectures, colonnes, CLES_RTNS_CLASSES, **enchainee)

    def cnrps_1959_1985():
        """Les lignes chiffrées du régime des pensions civiles, de 1959 à 1985.

        Le plancher se dit en règle, non en montant : la rémunération de l'indice 100 dépend
        de la grille des traitements, qui n'est pas ici. Il se compose de trois paramètres
        jusqu'au 30 avril 1981 — la part de cette rémunération, le nombre d'annuités de la
        pension pleine, le taux par annuité des pensions proportionnelles —, puis de la
        fraction du SMIG.
        """
        plafond = f"{CNRPS}/plaf_taux_pension.yaml"
        maximum = f"{CNRPS}/maximum_annuites_liquidables.yaml"
        part = f"{CNRPS}/pension_minimale/indice_100/part_indice_100.yaml"
        pleine = f"{CNRPS}/pension_minimale/indice_100/annuites_pension_pleine.yaml"
        proportionnelle = (f"{CNRPS}/pension_minimale/indice_100/"
                           "taux_par_annuite_proportionnelle.yaml")
        minimum = f"{CNRPS}/pension_minimale/minimum_garanti.yaml"
        conjoint = f"{CNRPS}/survivants/taux_conjoint.yaml"
        orphelin = f"{CNRPS}/survivants/taux_orphelin.yaml"
        lectures = [
            (plafond, LIBELLES_SERIES[langue]["cnrps_plafond"]),
            (maximum, lien["cnrps_max"]),
            (part, lien["cnrps_part"]),
            (pleine, lien["cnrps_pleine"]),
            (proportionnelle, lien["cnrps_prop"]),
            (minimum, lien["cnrps_minimum"]),
            (conjoint, lien["cnrps_reversion"]),
            (orphelin, lien["cnrps_orphelin"]),
        ]

        def plancher(series, date):
            point = en_vigueur(series[part], date)
            if point is None or point[1] is None:
                return cellule((minimum, part_smig))(series, date)
            if point[0] not in BASE_INDICE_100:
                raise ValueError(f"{part} : date d'effet {point[0]} sans base connue "
                                 f"(BASE_INDICE_100)")
            base = m["indice_100"][BASE_INDICE_100[point[0]]]
            texte = base if point[1] == 1 else m["des"].format(taux=taux(point[1]), base=base)
            n, _ = enchaine([(series[pleine], None)], date)
            t, _ = enchaine([(series[proportionnelle], None)], date)
            if n is None or t is None:
                return texte
            return m["plancher_1959"].format(pleine=texte, n=int(n), taux=taux(t))

        colonnes = [
            (m["plafond"], cellule((plafond, taux))),
            (m["max_annuites"], cellule((maximum, lambda v: str(int(v))))),
            (m["plancher"], plancher),
            (m["reversion"], cellule((conjoint, taux))),
            (m["orphelin"], cellule((orphelin, taux))),
        ]
        return ot.tableau_enchaine(lectures, colonnes, CLES_CNRPS_1959_1985, **enchainee)

    return {
        "cnrps_1959_1985.md": cnrps_1959_1985,
        "rtns_vieillesse.md": rtns_vieillesse,
        "rtns_agricole.md": rtns_agricole,
        "rtns_classes.md": rtns_classes,
        "cnrps_ages.md": ages,
        # Cinq valeurs attachées à cinq positions statutaires, et deux dates. Le tableau
        # est orienté comme celui des âges civils — une ligne par date d'effet — plutôt que
        # comme la version tenue à la main, qui mettait les grades en lignes : deux
        # tableaux voisins qui disent la même sorte de chose doivent se lire pareil.
        "cnrps_militaires_ages.md": lambda: ot.tableau_evolution_datee(
            [
                (f"{CNRPS}/age_legal/militaire/hommes_de_troupe.yaml", m["mil_troupe"], age),
                (f"{CNRPS}/age_legal/militaire/sous_officiers.yaml", m["mil_sous_officiers"], age),
                (f"{CNRPS}/age_legal/militaire/officiers_subalternes.yaml", m["mil_subalternes"], age),
                (f"{CNRPS}/age_legal/militaire/officiers_superieurs.yaml", m["mil_superieurs"], age),
                (f"{CNRPS}/age_legal/militaire/officiers_generaux.yaml", m["mil_generaux"], age),
            ],
            cles=CLES_MILITAIRES, **datee,
        ),
        "cnrps_annuites.md": annuites,
        "cnrps_plafond_plancher.md": lambda: ot.tableau_evolution_datee(
            [
                (f"{CNRPS}/plaf_taux_pension.yaml", m["plafond"], taux),
                (f"{CNRPS}/pension_minimale/minimum_garanti.yaml", m["minimum"], part_smig),
                (f"{CNRPS}/pension_minimale/allocation_vieillesse.yaml",
                 m["allocation_vieillesse"], part_smig),
                (f"{CNRPS}/pension_minimale/duree_service_allocation_vieillesse.yaml",
                 m["allocation_duree"], age),
            ],
            cles=CLES_PLAFOND_PLANCHER, **datee,
        ),
        "cnrps_indemnites_familiales.md": lambda: ot.tableau_evolution_datee(
            [
                (f"{CNRPS}/accessoires/indemnites_familiales/rang_1.yaml",
                 m["enfant1"], dinars),
                (f"{CNRPS}/accessoires/indemnites_familiales/rang_2.yaml",
                 m["enfant2"], dinars),
                (f"{CNRPS}/accessoires/indemnites_familiales/rang_3.yaml",
                 m["enfant3"], dinars),
                (f"{CNRPS}/accessoires/indemnites_familiales/rang_4.yaml",
                 m["enfant4"], dinars),
            ],
            cles=CLES_INDEMNITES, **datee,
        ),
        **tableaux_lot_a(langue),
        "rsna_planchers.md": lambda: ot.tableau_evolution_datee(
            [
                (f"{RSNA}/pension_minimale/sup.yaml", m["plancher_sup"], part_smig),
                (f"{RSNA}/pension_minimale/inf.yaml", m["plancher_inf"], part_smig),
            ],
            cles=CLES_RSNA_PLANCHERS, **datee,
        ),
    }


# ------------------------------------------------ tableaux engendrés le 3 octobre 2026
#
# Recension des paramètres écrits en dur (`docs/notes/recension-parametres-en-dur.md`),
# lots 1a à 1c : les entrées dont le paramètre est présent, daté et sourcé, et égal à ce que
# le précis en disait. Trois familles :
#
# - les FICHES de régime (`ot.tableau_a_la_date`) : une grandeur par ligne, à l'état en
#   vigueur, pour les régimes qui n'ont connu aucune réforme de leur cœur — Tunisiens à
#   l'étranger, travailleurs à faibles revenus, artistes, régime agricole amélioré, régime
#   complémentaire ;
# - les SÉRIES datées (`ot.tableau_evolution_datee`, `ot.tableau_enchaine`) : invalidité du
#   régime non agricole, départs anticipés et droits dérivés de la CNRPS ;
# - les TABLEAUX MIXTES (`ot.tableau_gabarit`) : les tableaux de règles qui portaient des
#   valeurs écrites à la main — salaire de référence et survivants du régime non agricole,
#   évolution du régime agricole. Le texte de chaque case est celui du tableau qu'ils
#   remplacent, dans les deux langues ; chaque valeur y est lue dans le paramètre, à la date
#   qui la fonde.
#
# CE QUI N'Y EST PAS, parce que le paramètre diverge du précis (diagnostic B) : la majoration
# et le plafond du régime des artistes, que l'arbre date du 5 janvier 2003 (loi n° 2002-104,
# art. 13) quand le précis les tient du décret n° 2003-894, exécutoire le 5 mai 2003 ;
# l'âge minimal de 50 ans des mères de trois enfants à la CNRPS, sans référence.

# Date de l'état en vigueur lu par les fiches : postérieure à toute date d'effet versée.
ETAT = "2100-01-01"

MOTS_LOT_A = {
    "fr": {
        "grandeur": "Grandeur", "valeur": "Valeur", "effet": "Effet", "texte": "Texte",
        "depuis": "Depuis", "regle": "Règle", "element": "Élément",
        "modifications": "Modifications",
        # Fiches de régime.
        "age": "Âge d'ouverture de la pension de vieillesse",
        "anticipe": "Âge du départ avec [décote](#g-decote)",
        "decote": "Décote par trimestre d'anticipation",
        "stage": "[Stage](#g-stage-cotisation)",
        "taux": "Taux de la pension au terme du stage",
        "taux_secteur": "Taux de la pension au terme du stage, en part du salaire minimum du "
                        "secteur",
        "majoration": "Majoration par trimestre au-delà du stage",
        "plafond": "Plafond du taux de la pension",
        "minimum": "Pension minimale",
        "minimum_mensuel": "Pension minimale, par mois",
        "inv_stage": "Invalidité : stage",
        "inv_taux": "Invalidité : taux de base",
        "inv_seuil": "Invalidité : durée de cotisation au-delà de laquelle la pension est "
                     "majorée",
        "tierce": "Majoration pour tierce personne",
        "classes": "[Classes de revenus](#g-classe-de-revenus), en multiples du SMIG",
        "conjoint": "[Réversion](#g-pension-de-reversion) au conjoint",
        "orphelins": "Pensions d'orphelins, ensemble",
        "ages_orphelin": "Âge limite de l'orphelin : droit commun ; études secondaires ou "
                         "professionnelles ; études supérieures",
        "remariage": "Âge avant lequel le remariage suspend la réversion",
        # Régime agricole amélioré.
        "rsaa_seuil": "Trimestre validé : salaire déclaré, en multiple du SMAG journalier",
        "rsaa_limite": "[Limite de calcul](#g-limite-calcul-prestations), en multiple du "
                       "SMAG annuel",
        "rsaa_minimum": "Pension minimale, en fraction du SMAG annuel",
        "rsaa_jours": "SMAG annuel : durée de référence",
        # Régime complémentaire.
        "cpl_gamma": "Taux de la cotisation contractuelle ($\\gamma$)",
        "cpl_minimum": "Cotisation minimale : salaire de calcul, en fraction du SMIG",
        "cpl_orphelin": "[Pension d'orphelin](#g-pension-temporaire-orphelin)",
        "cpl_orphelin_pm": "Pension d'orphelin de père et de mère",
        # Invalidité du régime non agricole.
        "taux_base": "Taux de base",
        "inv_majoration": "Majoration",
        "inv_majoration_cellule": "{taux} par période de {periode}",
        "inv_au_dela": "au-delà de",
        # CNRPS.
        "da_age": "Départ anticipé sur demande : âge minimal",
        "da_duree": "Départ anticipé sur demande : services requis",
        "meres": "Mères de trois enfants : âge maximal des enfants",
        "sv_orphelin": "[Pension d'orphelin](#g-pension-temporaire-orphelin), par orphelin",
        "sv_plafond": "Plafond du cumul des pensions de survivants, en part de la pension "
                      "de l'agent",
        "sv_cinq": "Part du conjoint à partir de cinq orphelins",
        "pension_agent": "{taux} de la pension de l'agent",
        "regime": "Régime", "reference": "Salaire minimum de référence",
        "reg_rtns": "Travailleurs non salariés",
        "reg_raci": "Artistes, créateurs et intellectuels",
        "reg_rtte": "Tunisiens à l'étranger",
        "ref_smig": "SMIG × {h} heures", "ref_smag": " ou SMAG × {j} jours",
        "lien_classes": "{regime} — classes de revenus, en multiples du salaire minimum",
        "lien_heures": "{regime} — durée annuelle à laquelle le SMIG est rapporté",
        "lien_jours": "{regime} — durée annuelle à laquelle le SMAG est rapporté",
    },
    "ar": {
        "grandeur": "المقدار", "valeur": "القيمة", "effet": "بداية السريان", "texte": "النصّ",
        "depuis": "منذ", "regle": "القاعدة", "element": "العنصر",
        "modifications": "التعديلات",
        "age": "سنّ استحقاق جراية الشيخوخة",
        "anticipe": "سنّ التقاعد المبكّر مع [التخفيض في الجراية](#g-decote)",
        "decote": "التخفيض في الجراية عن كلّ ثلاثية",
        "stage": "[مدة الانخراط الدنيا](#g-stage-cotisation)",
        "taux": "نسبة الجراية عند استيفاء مدة الانخراط الدنيا",
        "taux_secteur": "نسبة الجراية عند استيفاء مدة الانخراط الدنيا، من الأجر الأدنى "
                        "المضمون للقطاع",
        "majoration": "الترفيع عن كلّ ثلاثية تفوق مدة الانخراط الدنيا",
        "plafond": "سقف نسبة الجراية",
        "minimum": "الجراية الدنيا",
        "minimum_mensuel": "الجراية الدنيا، شهريًا",
        "inv_stage": "العجز: مدة الانخراط الدنيا",
        "inv_taux": "العجز: النسبة الأساسية",
        "inv_seuil": "العجز: مدة الاشتراك التي تُرفَّع الجراية بعدها",
        "tierce": "الزيادة بعنوان المساعدة من الغير",
        "classes": "[شرائح الدخل](#g-classe-de-revenus)، بمضاعفات الأجر الأدنى المضمون",
        "conjoint": "[جراية القرين الباقي على قيد الحياة](#g-pension-de-reversion)",
        "orphelins": "جرايات الأيتام، مجتمعة",
        "ages_orphelin": "السنّ القصوى لليتيم: القاعدة العامة؛ الدراسات الثانوية أو "
                         "المهنية؛ الدراسات العليا",
        "remariage": "السنّ التي يوقف قبلها الزواج من جديد جراية القرين",
        "rsaa_seuil": "الثلاثية المعتمدة: الأجر المصرّح به، بمضاعفات الأجر الأدنى الفلاحي "
                      "المضمون اليومي",
        "rsaa_limite": "[الحدّ الأقصى لاحتساب المنافع](#g-limite-calcul-prestations)، "
                       "بمضاعفات الأجر الأدنى الفلاحي المضمون السنوي",
        "rsaa_minimum": "الجراية الدنيا، كسرًا من الأجر الأدنى الفلاحي المضمون السنوي",
        "rsaa_jours": "الأجر الأدنى الفلاحي المضمون السنوي: المدة المعتمدة",
        "cpl_gamma": "نسبة الاشتراك التعاقدي ($\\gamma$)",
        "cpl_minimum": "الاشتراك الأدنى: أجر الاحتساب، كسرًا من الأجر الأدنى المضمون",
        "cpl_orphelin": "[جراية اليتيم](#g-pension-temporaire-orphelin)",
        "cpl_orphelin_pm": "جراية يتيم الأب والأم",
        "taux_base": "النسبة الأساسية",
        "inv_majoration": "الترفيع",
        "inv_majoration_cellule": "{taux} عن كلّ فترة من {periode}",
        "inv_au_dela": "ابتداءً مما يفوق",
        "da_age": "التقاعد المبكّر بطلب: السنّ الدنيا",
        "da_duree": "التقاعد المبكّر بطلب: الخدمات المستوجبة",
        "meres": "الأمهات لثلاثة أطفال: السنّ القصوى للأطفال",
        "sv_orphelin": "[الجراية الوقتية لليتيم](#g-pension-temporaire-orphelin)، عن كلّ يتيم",
        "sv_plafond": "سقف مجموع جرايات الباقين على قيد الحياة، من جراية العون",
        "sv_cinq": "نصيب القرين ابتداءً من خمسة أيتام",
        "pension_agent": "{taux} من جراية العون",
        "regime": "النظام", "reference": "الأجر الأدنى المرجعي",
        "reg_rtns": "العملة غير الأجراء",
        "reg_raci": "الفنانون والمبدعون والمثقفون",
        "reg_rtte": "التونسيون بالخارج",
        "ref_smig": "الأجر الأدنى المضمون × {h} ساعة",
        "ref_smag": " أو الأجر الأدنى الفلاحي المضمون × {j} يوم",
        "lien_classes": "{regime} — شرائح الدخل، بمضاعفات الأجر الأدنى",
        "lien_heures": "{regime} — المدة السنوية التي يُحتسب على أساسها الأجر الأدنى المضمون",
        "lien_jours": "{regime} — المدة السنوية التي يُحتسب على أساسها الأجر الأدنى الفلاحي "
                      "المضمون",
    },
}

# Libellés des liens « Base législative » des tableaux mixtes, par paramètre lu.
LIENS_LOT_A = {
    "periode_courte": ("Salaire de référence — période courte, en années",
                       "الأجر المرجعي — الفترة القصيرة، بالسنوات"),
    "periode_longue": ("Salaire de référence — période longue, en années",
                       "الأجر المرجعي — الفترة الطويلة، بالسنوات"),
    "diviseur_court": ("Salaire de référence — diviseur de la période courte, en mois",
                       "الأجر المرجعي — قاسم الفترة القصيرة، بالأشهر"),
    "diviseur_long": ("Salaire de référence — diviseur de la période longue, en mois",
                      "الأجر المرجعي — قاسم الفترة الطويلة، بالأشهر"),
    "periode_1990": ("Salaire de référence — période de référence de 1990, en années",
                     "الأجر المرجعي — الفترة المرجعية لسنة 1990، بالسنوات"),
    "duree_mois": ("Salaire de référence — période de référence, en mois",
                   "الأجر المرجعي — الفترة المرجعية، بالأشهر"),
    "limite_multiple": ("Limite de calcul des prestations, en multiple du SMIG",
                        "الحدّ الأقصى لاحتساب المنافع، مضاعفًا للأجر الأدنى المضمون"),
    "limite_heures": ("Limite de calcul — durée annuelle à laquelle le SMIG est rapporté",
                      "حدّ الاحتساب — المدة السنوية التي يُحتسب على أساسها الأجر الأدنى "
                      "المضمون"),
    "taux_conjoint": ("Taux de la pension de réversion", "نسبة جراية القرين الباقي على قيد الحياة"),
    "taux_conjoint_majore": ("Taux majoré de la pension de réversion",
                             "النسبة المرفّعة لجراية القرين الباقي على قيد الحياة"),
    "taux_orphelin": ("Taux de la pension d'orphelin", "نسبة جراية اليتيم"),
    "taux_orphelin_pm": ("Taux de la pension d'orphelin de père et de mère",
                         "نسبة جراية يتيم الأب والأم"),
    "age_orphelin": ("Âge limite de l'orphelin", "السنّ القصوى لليتيم"),
    "age_orphelin_etudes": ("Âge limite de l'orphelin en études", "السنّ القصوى لليتيم الدارس"),
    "age_orphelin_sup": ("Âge limite de l'orphelin en études supérieures",
                         "السنّ القصوى لليتيم في التعليم العالي"),
    "remariage": ("Âge avant lequel le remariage suspend la réversion",
                  "السنّ التي يوقف قبلها الزواج من جديد جراية القرين"),
}


def _lien(cle: str) -> dict[str, str]:
    fr, ar = LIENS_LOT_A[cle]
    return {"fr": fr, "ar": ar}


def _entier(v, _langue):
    return str(int(v))


def _milliers(v, _langue):
    return ot.formate_dinars(v)


def _annees_de_mois(v, _langue):
    return str(int(v // 12))


def _fraction(v):
    """Une fraction simple : « 1/2 », « 2/3 » ; un entier tel quel."""
    fraction = Fraction(v).limit_denominator(12)
    if fraction.denominator == 1:
        return str(fraction.numerator)
    return f"{fraction.numerator}/{fraction.denominator}"


def tableaux_lot_a(langue):
    m = MOTS_LOT_A[langue]
    f = ot.formateurs(langue)
    mois, trimestres = f.duree("mois"), f.duree("trimestres")
    fiche = dict(entetes=(m["grandeur"], m["valeur"], m["texte"]), langue=langue)
    datee = dict(langue=langue, colonne_periode=m["effet"], colonne_texte=m["texte"])
    date = lambda d: ot.formate_date(d, langue)  # noqa: E731
    g, L = ot.gabarit, ot.Lecture
    RTTE, RTFR, RACI = ("parameters/retraite/rtte", "parameters/retraite/rtfr",
                        "parameters/retraite/raci")
    RSAA, CPL = "parameters/retraite/rsaa", "parameters/retraite/complementaire"
    SR = f"{RSNA}/salaire_reference"

    def ages_orphelin(base):
        return (f"{base}/age_limite_orphelin.yaml", f"{base}/age_limite_orphelin_etudes.yaml",
                f"{base}/age_limite_orphelin_etudes_superieures.yaml")

    def rtte():
        """Les Tunisiens à l'étranger : l'état du décret n° 89-107, jamais réformé."""
        art = lambda a: f"decret89-107, art. {a}"  # noqa: E731
        classes = tuple(f"{RTTE}/revenu_reference/classes/classe_{k}.yaml" for k in range(1, 5))
        specs = [
            (f"{RTTE}/age_legal.yaml", m["age"], f.age),
            (f"{RTTE}/age_depart_anticipe.yaml", m["anticipe"], f.age),
            (f"{RTTE}/decote_par_trimestre.yaml", m["decote"], f.taux),
            (f"{RTTE}/stage_mois.yaml", m["stage"], mois),
            (f"{RTTE}/taux_base.yaml", m["taux"], f.taux),
            (f"{RTTE}/majoration_par_trimestre.yaml", m["majoration"], f.taux),
            (f"{RTTE}/plafond_taux.yaml", m["plafond"], f.taux),
            (f"{RTTE}/plancher_taux.yaml", m["minimum"], f.part_smig),
            (f"{RTTE}/invalidite/stage_mois.yaml", m["inv_stage"], mois),
            (f"{RTTE}/invalidite/taux_base.yaml", m["inv_taux"], f.taux),
            (f"{RTTE}/invalidite/seuil_majoration_mois.yaml", m["inv_seuil"], mois),
            (classes, m["classes"], f.coefficient),
        ]
        cles = {
            f"{RTTE}/age_legal.yaml": art(18), f"{RTTE}/age_depart_anticipe.yaml": art(18),
            f"{RTTE}/decote_par_trimestre.yaml": art(18), f"{RTTE}/stage_mois.yaml": art(20),
            f"{RTTE}/taux_base.yaml": art(20), f"{RTTE}/majoration_par_trimestre.yaml": art(20),
            f"{RTTE}/plafond_taux.yaml": art(20), f"{RTTE}/plancher_taux.yaml": art(22),
            f"{RTTE}/invalidite/stage_mois.yaml": art(21),
            f"{RTTE}/invalidite/taux_base.yaml": art(21),
            f"{RTTE}/invalidite/seuil_majoration_mois.yaml": art(21),
            classes[0]: art(6),
        }
        return ot.tableau_a_la_date(specs, ETAT, cles=cles, **fiche)

    def rtfr():
        """Les travailleurs à faibles revenus : l'état de la loi n° 2002-32."""
        art = lambda a: f"loi2002-32, art. {a}"  # noqa: E731
        sv = f"{RTFR}/survivants"
        specs = [
            (f"{RTFR}/age_legal.yaml", m["age"], f.age),
            (f"{RTFR}/stage_mois.yaml", m["stage"], mois),
            (f"{RTFR}/taux_base.yaml", m["taux_secteur"], f.taux),
            (f"{RTFR}/majoration_par_trimestre.yaml", m["majoration"], f.taux),
            (f"{RTFR}/plafond_taux.yaml", m["plafond"], f.taux),
            (f"{RTFR}/invalidite/stage_mois.yaml", m["inv_stage"], mois),
            (f"{RTFR}/invalidite/taux_base.yaml", m["inv_taux"], f.taux),
            (f"{RTFR}/invalidite/majoration_tierce_personne.yaml", m["tierce"], f.taux),
            (f"{sv}/taux_conjoint.yaml", m["conjoint"], f.taux),
            (f"{sv}/taux_orphelins.yaml", m["orphelins"], f.taux),
            (ages_orphelin(sv), m["ages_orphelin"], f.age),
            (f"{sv}/age_remariage_suspensif.yaml", m["remariage"], f.age),
        ]
        cles = {
            f"{RTFR}/age_legal.yaml": art(13), f"{RTFR}/stage_mois.yaml": art(13),
            f"{RTFR}/taux_base.yaml": art(14), f"{RTFR}/majoration_par_trimestre.yaml": art(14),
            f"{RTFR}/plafond_taux.yaml": art(14),
            f"{RTFR}/invalidite/stage_mois.yaml": "loi2002-32, art. 16-18",
            f"{RTFR}/invalidite/taux_base.yaml": "loi2002-32, art. 16-18",
            f"{RTFR}/invalidite/majoration_tierce_personne.yaml": "loi2002-32, art. 16-18",
            f"{sv}/taux_conjoint.yaml": "loi2002-32, art. 23 à 28",
            f"{sv}/taux_orphelins.yaml": "loi2002-32, art. 23 à 28",
            ages_orphelin(sv)[0]: "loi2002-32, art. 23 à 28",
            f"{sv}/age_remariage_suspensif.yaml": "loi2002-32, art. 23 à 28",
        }
        return ot.tableau_a_la_date(specs, ETAT, cles=cles, **fiche)

    def raci():
        """Les artistes, créateurs et intellectuels : la loi de 2002, puis le décret de 2003.

        Deux dates d'effet — l'âge, le stage et le minimum au 5 janvier 2003, le taux et les
        classes au 5 mai 2003 —, d'où la colonne « Effet ». La majoration par trimestre et le
        plafond n'y sont pas : leur date n'est pas établie (voir l'en-tête de ce bloc).
        """
        loi = lambda a: f"loi2002-104, art. {a}"  # noqa: E731
        sv = f"{RACI}/survivants"
        classes = tuple(f"{RACI}/revenu_reference/classes/classe_{k}.yaml" for k in range(1, 11))
        specs = [
            (f"{RACI}/age_legal.yaml", m["age"], f.age),
            (f"{RACI}/stage_trimestres.yaml", m["stage"], trimestres),
            (f"{RACI}/taux_base.yaml", m["taux"], f.taux),
            (f"{RACI}/plancher_mensuel.yaml", m["minimum_mensuel"], f.dinars),
            (f"{RACI}/invalidite/stage_trimestres.yaml", m["inv_stage"], trimestres),
            (f"{RACI}/invalidite/seuil_majoration_trimestres.yaml", m["inv_seuil"], trimestres),
            (f"{RACI}/invalidite/majoration_tierce_personne.yaml", m["tierce"], f.taux),
            (classes, m["classes"], f.coefficient),
            (f"{sv}/taux_conjoint.yaml", m["conjoint"], f.taux),
            (f"{sv}/taux_orphelins.yaml", m["orphelins"], f.taux),
            (ages_orphelin(sv), m["ages_orphelin"], f.age),
            (f"{sv}/age_remariage_suspensif.yaml", m["remariage"], f.age),
        ]
        cles = {
            f"{RACI}/age_legal.yaml": loi(12), f"{RACI}/stage_trimestres.yaml": loi(12),
            f"{RACI}/taux_base.yaml": "decret2003-894, art. 17",
            f"{RACI}/plancher_mensuel.yaml": "loi2002-104, art. 13 et 15 ; @decret2003-894, art. 17",
            f"{RACI}/invalidite/stage_trimestres.yaml": "loi2002-104, art. 14-15",
            f"{RACI}/invalidite/seuil_majoration_trimestres.yaml": loi(15),
            f"{RACI}/invalidite/majoration_tierce_personne.yaml": loi(16),
            classes[0]: "decret2003-894, art. 5",
            f"{sv}/taux_conjoint.yaml": "loi2002-104, art. 20 à 23",
            f"{sv}/taux_orphelins.yaml": "loi2002-104, art. 20 à 23",
            ages_orphelin(sv)[0]: "loi2002-104, art. 20 à 23",
            f"{sv}/age_remariage_suspensif.yaml": "loi2002-104, art. 20 à 23",
        }
        return ot.tableau_a_la_date(specs, ETAT, cles=cles, colonne_effet=m["effet"], **fiche)

    def rsaa():
        """Le régime agricole amélioré : ce que le titre III de la loi n° 81-6 fixe en propre."""
        specs = [
            (f"{RSAA}/seuil_trimestre_smag.yaml", m["rsaa_seuil"], f.coefficient),
            (f"{RSAA}/salaire_reference/limite_multiple_smag.yaml", m["rsaa_limite"],
             f.coefficient),
            (f"{RSAA}/plancher_taux.yaml", m["rsaa_minimum"], _fraction),
            (f"{RSAA}/salaire_reference/jours_annuels_smag.yaml", m["rsaa_jours"],
             f.duree("jours")),
        ]
        cles = dict.fromkeys((c for c, _l, _f in specs), "loi89-73")
        return ot.tableau_a_la_date(specs, ETAT, cles=cles, **fiche)

    def complementaire():
        """Le régime complémentaire : le règlement de 1978 et l'arrêté de 1997."""
        reglement = "arrete-1978-11-18-retraite-complementaire, règlement, art. {}"
        sv = f"{CPL}/survivants"
        specs = [
            (f"{CPL}/taux_cotisation_contractuel.yaml", m["cpl_gamma"], f.taux),
            (f"{CPL}/salaire_minimal_cotisable_part_smig.yaml", m["cpl_minimum"], _fraction),
            (f"{sv}/taux_reversion.yaml", m["conjoint"], f.taux),
            (f"{sv}/taux_orphelin.yaml", m["cpl_orphelin"], f.taux),
            (f"{sv}/taux_orphelin_pere_et_mere.yaml", m["cpl_orphelin_pm"], f.taux),
            (f"{sv}/age_limite_suspension_remariage.yaml", m["remariage"], f.age),
        ]
        cles = {
            f"{CPL}/taux_cotisation_contractuel.yaml": reglement.format(10),
            f"{CPL}/salaire_minimal_cotisable_part_smig.yaml": reglement.format(14),
            f"{sv}/taux_reversion.yaml": reglement.format(23),
            f"{sv}/taux_orphelin.yaml": reglement.format("26-27"),
            f"{sv}/taux_orphelin_pere_et_mere.yaml": reglement.format("26-27"),
            f"{sv}/age_limite_suspension_remariage.yaml":
                "arrete-1997-01-27-retraite-complementaire",
        }
        return ot.tableau_a_la_date(specs, ETAT, cles=cles, colonne_effet=m["effet"], **fiche)

    def rsna_invalidite():
        """La pension d'invalidité du régime non agricole : trois états, 1974, 1981, 1982.

        La majoration se lit en deux paramètres — un taux et la période qu'il rémunère — que
        la case réunit : « 2 % par période de 12 mois », puis « 0,5 % par période de 3 mois ».
        """
        inv = f"{RSNA}/invalidite"
        chemins = {c: f"{inv}/{c}.yaml" for c in (
            "stage_mois", "taux_base", "majoration", "periode_majoration_mois",
            "seuil_majoration_mois", "plafond_taux", "majoration_tierce_personne")}
        libelles = {
            "fr": {"stage_mois": "Invalidité — stage", "taux_base": "Invalidité — taux de base",
                   "majoration": "Invalidité — majoration",
                   "periode_majoration_mois": "Invalidité — période de la majoration, en mois",
                   "seuil_majoration_mois": "Invalidité — durée au-delà de laquelle la "
                                            "pension est majorée",
                   "plafond_taux": "Invalidité — plafond du taux",
                   "majoration_tierce_personne": "Invalidité — majoration pour tierce personne"},
            "ar": {"stage_mois": "العجز — مدة الانخراط الدنيا",
                   "taux_base": "العجز — النسبة الأساسية", "majoration": "العجز — الترفيع",
                   "periode_majoration_mois": "العجز — فترة الترفيع، بالأشهر",
                   "seuil_majoration_mois": "العجز — المدة التي تُرفَّع الجراية بعدها",
                   "plafond_taux": "العجز — سقف النسبة",
                   "majoration_tierce_personne": "العجز — الزيادة بعنوان المساعدة من الغير"},
        }[langue]
        lectures = [(chemins[c], libelles[c]) for c in chemins]
        c = ot.cellule

        def majoration(series, d):
            taux_ = c((chemins["majoration"], f.taux))(series, d)
            periode = c((chemins["periode_majoration_mois"], mois))(series, d)
            return m["inv_majoration_cellule"].format(taux=taux_, periode=periode)

        colonnes = [
            (m["stage"], c((chemins["stage_mois"], mois))),
            (m["taux_base"], c((chemins["taux_base"], f.taux))),
            (m["inv_majoration"], majoration),
            (m["inv_au_dela"], c((chemins["seuil_majoration_mois"], mois))),
            (m["plafond"], c((chemins["plafond_taux"], f.taux))),
            (m["tierce"], c((chemins["majoration_tierce_personne"], f.taux))),
        ]
        cles = {"1974-01-01": "decret74-499, art. 21 à 23",
                "1981-02-19": "decret81-188, art. 1",
                "1982-07-22": "decret82-1030, art. 4"}
        return ot.tableau_enchaine(lectures, colonnes, cles, **datee)

    def cnrps_departs():
        """Les conditions du départ anticipé de la CNRPS : 1985, 1989, 2007."""
        da = f"{CNRPS}/depart_anticipe"
        return ot.tableau_evolution_datee(
            [
                (f"{da}/sur_demande/cadre_commun/age_minimum.yaml", m["da_age"], f.age),
                (f"{da}/sur_demande/cadre_commun/duree_minimum.yaml", m["da_duree"], f.age),
                (f"{da}/meres_3_enfants/age_maximum_enfant.yaml", m["meres"], f.age),
            ],
            cles={"1985-09-12": "loi85-12, art. 5 et 30", "1989-01-01": "loi88-71, art. 1 et 2",
                  "2007-07-02": "loi2007-43"},
            **datee)

    def cnrps_survivants():
        """Les droits dérivés de la CNRPS : taux, plafond du cumul, partage à cinq orphelins."""
        sv = f"{CNRPS}/survivants"
        part_agent = lambda v: ot.VIDE if v is None else m["pension_agent"].format(  # noqa: E731
            taux=f.taux(v))
        return ot.tableau_evolution_datee(
            [
                (f"{sv}/taux_conjoint.yaml", m["conjoint"], f.taux),
                (f"{sv}/taux_orphelin.yaml", m["sv_orphelin"], f.taux),
                (f"{sv}/plafond_cumul.yaml", m["sv_plafond"], part_agent),
                (f"{sv}/taux_partage_5_orphelins.yaml", m["sv_cinq"], part_agent),
            ],
            cles={"1959-04-01": "loi59-18, art. 31 et 52 ; @loi59-100, art. 1",
                  "1981-05-01": "loi81-70, art. 4",
                  "1985-09-12": "loi85-12, art. 43 et 45"},
            **datee)

    def rsna_reference():
        """Salaire de référence et limite de calcul du régime non agricole, 1974-1996.

        Tableau mixte : la fenêtre de 1974 est un CHOIX entre deux périodes, celle de 1990
        une NON-MODIFICATION de l'article 19 ; ni l'un ni l'autre ne se dit par une valeur
        seule. Le texte de chaque case est celui du chapitre ; les durées, les diviseurs et
        la limite y sont lus dans le paramètre, à la date de la ligne.
        """
        def lu(nom, chemin, d, formateur):
            return L(f"{SR}/{chemin}.yaml", d, formateur, _lien(nom))

        def limite(d, regime_48h=False):
            fr = ("**{m} fois le SMIG « régime 48 heures »** rapporté à {h} heures par an"
                  if regime_48h else "**{m} fois le SMIG** rapporté à {h} heures par an")
            ar = ("**{m} أضعاف الأجر الأدنى المضمون لمختلف المهن (SMIG) «نظام 48 ساعة»** "
                  "بالنسبة لـ {h} ساعة سنوياً" if regime_48h else
                  "**{m} أضعاف الأجر الأدنى المضمون لمختلف المهن (SMIG)** بالنسبة لـ {h} "
                  "ساعة سنوياً")
            return g({"fr": fr, "ar": ar},
                     m=lu("limite_multiple", "limite_multiple_smig", d, _entier),
                     h=lu("limite_heures", "limite_heures_annuelles", d, _milliers))

        def fenetre_recente(d, actualisation=False):
            fr = "**{n} dernières années**"
            ar = "**السنوات {n} الأخيرة**"
            if actualisation:
                fr += " ; salaires actualisés selon un barème fixé annuellement par arrêté"
                ar += "؛ أجور محيّنة وفقاً لجدول يحدد سنوياً بقرار"
            return g({"fr": fr, "ar": ar}, n=lu("duree_mois", "duree_mois", d, _annees_de_mois))

        def moyenne(d):
            return g({"fr": "{d}", "ar": "{d}"}, d=lu("duree_mois", "duree_mois", d,
                                                     "duree:mois"))

        d74, d90, d94, d95, d96 = ("1974-01-01", "1990-09-23", "1994-07-01", "1995-07-01",
                                   "1996-07-01")
        lignes = [
            [date(d74),
             g({"fr": "salaires des **{c} ou {l} dernières années** précédant l'âge d'ouverture "
                      "du droit, « selon que l'une ou l'autre de ces périodes de référence est "
                      "plus avantageuse » pour l'assuré",
                "ar": "أجور **السنوات {c} أو {l} الأخيرة** التي تسبق سنّ فتح الحق، «حسب ما "
                      "تكون إحدى هاتين الفترتين المرجعيتين أكثر فائدة» للمضمون"},
               c=lu("periode_courte", "periode_courte_annees", d74, _entier),
               l=lu("periode_longue", "periode_longue_annees", d74, _entier)),
             g({"fr": "total divisé par {c} ou {l} mois", "ar": "المجموع مقسوم على {c} أو {l} شهراً"},
               c=lu("diviseur_court", "diviseur_court_mois", d74, _entier),
               l=lu("diviseur_long", "diviseur_long_mois", d74, _entier)),
             limite(d74), "[@decret74-499, art. 18-19]"],
            [date(d90),
             g({"fr": "salaires des **{p} dernières années** précédant l'âge d'ouverture du "
                      "droit ; moyenne sur la période d'activité déclarée si elle est "
                      "inférieure à {p} ans ; salaires « actualisés selon un barème fixé par "
                      "arrêté du ministre des affaires sociales »",
                "ar": "أجور **السنوات {p} الأخيرة** التي تسبق سنّ فتح الحق؛ متوسط على فترة "
                      "النشاط المصرح بها إذا كانت أقل من {p} سنوات؛ أجور «محيّنة وفقاً لجدول "
                      "يحدده قرار من وزير الشؤون الاجتماعية»"},
               p=lu("periode_1990", "periode_annees", d90, _entier)),
             g({"fr": "article 19 non modifié : {c} ou {l} mois",
                "ar": "الفصل 19 لم يعدّل: {c} أو {l} شهراً"},
               c=lu("diviseur_court", "diviseur_court_mois", d90, _entier),
               l=lu("diviseur_long", "diviseur_long_mois", d90, _entier)),
             limite(d90), "[@decret90-1455, art. 1]"],
            [date(d94), fenetre_recente(d94, actualisation=True), moyenne(d94),
             limite(d94, regime_48h=True), "[@decret94-1429, art. 1]"],
            [date(d95), fenetre_recente(d95), moyenne(d95), limite(d95, regime_48h=True),
             "[@decret94-1429, art. 1]"],
            [date(d96), fenetre_recente(d96), moyenne(d96), limite(d96, regime_48h=True),
             "[@decret94-1429, art. 1]"],
        ]
        entetes = {
            "fr": [m["depuis"], "Fenêtre de référence", "Moyenne (article 19)",
                   "Limite de prise en compte des salaires", m["texte"]],
            "ar": [m["depuis"], "نافذة المرجع", "المتوسط (الفصل 19)",
                   "حدّ الأخذ في الاعتبار للأجور", m["texte"]],
        }[langue]
        return ot.tableau_gabarit(entetes, lignes, langue)

    def rsna_survivants():
        """Droits des survivants du régime non agricole : règles et taux, 1974-2007."""
        sv = f"{RSNA}/survivants"

        def lu(nom, chemin, d, formateur="taux"):
            return L(f"{sv}/{chemin}.yaml", d, formateur, _lien(nom))

        d74, d81, d97 = "1974-01-01", "1981-02-19", "1997-05-01"
        lignes = [
            [{"fr": "Bénéficiaire et taux de la réversion",
              "ar": "المستفيد ونسبة جراية القرين الباقي على قيد الحياة"},
             g({"fr": "la veuve, et le veuf invalide : {c}", "ar": "الأرملة، والأرمل العاجز: {c}"},
               c=lu("taux_conjoint", "taux_conjoint", d74)),
             g({"fr": "1981 : jusqu'à {cm} sous condition ; droit rattaché, pour le décès avant "
                      "l'âge normal de la retraite, aux conditions de la pension d'invalidité de "
                      "l'article 21 (décret n° 81-188) ; 1997 : droit ouvert au « conjoint "
                      "survivant » (décret n° 97-291, art. 29)",
                "ar": "1981: حتى {cm} بشرط؛ الحق مرتبط، للوفاة قبل السن العادية للتقاعد، بشروط "
                      "جراية العجز المنصوص عليها في الفصل 21 (الأمر عدد 81-188)؛ 1997: الحق "
                      "مفتوح لـ «القرين الباقي على قيد الحياة» (الأمر عدد 97-291، الفصل 29)"},
               cm=lu("taux_conjoint_majore", "taux_conjoint_majore", d81))],
            [{"fr": "Remariage", "ar": "الزواج من جديد"},
             {"fr": "suppression au premier jour du trimestre civil suivant",
              "ar": "الإلغاء في اليوم الأول من الثلاثي المدني التالي"},
             {"fr": "1990 : rétablissement, revalorisé, au décès du nouveau conjoint ; cumul de "
                    "pensions de conjoint survivant au titre de mariages successifs interdit "
                    "(décret n° 90-1455)",
              "ar": "1990: إعادة التأسيس، مع إعادة تقييم، عند وفاة القرين الجديد؛ منع الجمع بين "
                    "جرايات القرين الباقي على قيد الحياة بموجب زيجات متتالية (الأمر عدد "
                    "90-1455)"}],
            [{"fr": "Taux d'orphelin", "ar": "نسبة اليتيم"},
             g({"fr": "{o}, porté à {pm} pour l'orphelin de père et de mère",
                "ar": "{o}، ترفع إلى {pm} ليتيم الأب والأم"},
               o=lu("taux_orphelin", "taux_orphelin", d74),
               pm=lu("taux_orphelin_pm", "taux_orphelin_pere_et_mere", d74)),
             g({"fr": "1981 : {o} dans tous les cas (décret n° 81-188, art. 34) ; droit étendu "
                      "aux orphelins d'un titulaire de pension d'invalidité ou d'un assuré "
                      "décédé avant l'âge normal qui remplissait les conditions de l'article 21 "
                      "(décret n° 81-188, art. 33)",
                "ar": "1981: {o} في جميع الحالات (الأمر عدد 81-188، الفصل 34)؛ الحق يمتد ليشمل "
                      "أيتام صاحب جراية عجز أو لمضمون توفي قبل السن العادية وكان يستوفي شروط "
                      "الفصل 21 (الأمر عدد 81-188، الفصل 33)"},
               o=lu("taux_orphelin", "taux_orphelin", d81))],
            [{"fr": "Âge limite de l'orphelin", "ar": "السن القصوى لليتيم"},
             g({"fr": "{a} ; {e} en cas d'études ; sans limite en cas d'affection incurable",
                "ar": "{a}؛ {e} في حالة الدراسة؛ بدون حد في حالة مرض عضال"},
               a=lu("age_orphelin", "age_limite_orphelin", d74, "age"),
               e=lu("age_orphelin_etudes", "age_limite_orphelin_etudes", d74, "age")),
             g({"fr": "{d} : {e} en études secondaires, techniques ou professionnelles, {s} en "
                      "études supérieures sans bourse, sans limite pour la fille sans ressources "
                      "ou qui n'est pas à la charge de son mari et en cas d'infirmité (décret "
                      "n° 97-1927) ; 2007 : paiement à la fille définitivement suspendu dès "
                      "qu'une condition fait défaut (décret n° 2007-2148)",
                "ar": "{d}: {e} في الدراسات الثانوية أو الفنية أو المهنية، {s} في الدراسات العليا "
                      "بدون منحة، بدون حد للفتاة التي لا تملك موارد أو التي ليست على نفقة زوجها "
                      "وفي حالة العجز (الأمر عدد 97-1927)؛ 2007: تعليق دفع الجراية للفتاة "
                      "نهائياً بمجرد فقدان شرط (الأمر عدد 2007-2148)"},
               d=L(f"{sv}/age_limite_orphelin_etudes_superieures.yaml", d97,
                   lambda _v, lg: ot.formate_date(d97, lg), _lien("age_orphelin_sup")),
               e=lu("age_orphelin_etudes", "age_limite_orphelin_etudes", d97, "age"),
               s=lu("age_orphelin_sup", "age_limite_orphelin_etudes_superieures", d97, "age"))],
            [{"fr": "Plafond de cumul", "ar": "سقف الجمع"},
             {"fr": "pensions de veuves et d'orphelins limitées à la pension de référence du "
                    "mari, par réduction temporaire des pensions d'orphelins",
              "ar": "جرايات الأرامل والأيتام محدودة بجراية الزوج المرجعية، مع تخفيض مؤقت "
                    "لجرايات الأيتام"},
             {"fr": "1997 : pensions de conjoint survivant et d'orphelins limitées à la pension "
                    "dont bénéficiait ou aurait pu bénéficier le défunt (décret n° 97-291, "
                    "art. 38)",
              "ar": "1997: جرايات القرين الباقي على قيد الحياة والأيتام محدودة بالجراية التي كان "
                    "ينتفع بها أو كان يمكن أن ينتفع بها المتوفى (الأمر عدد 97-291، الفصل 38)"}],
            [{"fr": "Cumul d'une pension d'invalidité et d'une pension de survivant",
              "ar": "الجمع بين جراية عجز وجراية قرين باق على قيد الحياة"},
             {"fr": "interdit, seule la plus élevée étant servie",
              "ar": "ممنوع، تدفع الأعلى فقط"},
             {"fr": "1997 : interdiction supprimée par l'abrogation de l'article 52 (décret "
                    "n° 97-291, art. 2)",
              "ar": "1997: إلغاء المنع بإلغاء الفصل 52 (الأمر عدد 97-291، الفصل 2)"}],
        ]
        entetes = {
            "fr": [m["regle"], f"Décret n° 74-499 ({date(d74)})", m["modifications"]],
            "ar": [m["regle"], f"الأمر عدد 74-499 ({date(d74)})", m["modifications"]],
        }[langue]
        return ot.tableau_gabarit(entetes, lignes, langue)

    def rsa_evolution():
        """Évolution des autres éléments du régime des salariés agricoles, 1981-2026."""
        sv = "parameters/retraite/rsa/survivants"

        def lu(nom, chemin, d, formateur="age"):
            return L(f"{sv}/{chemin}.yaml", d, formateur, _lien(nom))

        d81, d96, d97 = "1981-01-01", "1996-08-04", "1997-05-01"
        lignes = [
            [{"fr": "Délai de présentation de la demande", "ar": "أجل تقديم الطلب"},
             {"fr": "un an", "ar": "سنة واحدة"},
             {"fr": "10 décembre 1995 : cinq ans (loi n° 95-102, art. 74 al. 1)",
              "ar": "10 ديسمبر 1995: خمس سنوات (القانون عدد 95-102، الفصل 74 فقرة 1)"}],
            [{"fr": "Bénéficiaire de la réversion",
              "ar": "المستفيد من جراية القرين الباقي على قيد الحياة"},
             {"fr": "la veuve, et le veuf invalide ; mariage contracté antérieurement à "
                    "l'ouverture du droit à pension",
              "ar": "الأرملة، والأرمل العاجز؛ زواج تم قبل فتح الحق في الجراية"},
             {"fr": "4 août 1996 : le conjoint survivant ; liens de mariage existant au moment "
                    "du décès (loi n° 96-66, art. 60 et 61)",
              "ar": "4 أوت 1996: القرين الباقي على قيد الحياة؛ روابط الزواج القائمة وقت الوفاة "
                    "(القانون عدد 96-66، الفصلان 60 و61)"}],
            [{"fr": "Remariage", "ar": "الزواج من جديد"},
             {"fr": "suppression de la pension", "ar": "إلغاء الجراية"},
             g({"fr": "{d} : suspension seulement en cas de remariage avant {r} ans ; "
                      "rétablissement, revalorisé, au décès du nouveau conjoint ou à la "
                      "dissolution du mariage ; cumul de pensions de conjoint survivant "
                      "interdit, la plus élevée étant servie (loi n° 96-66, art. 63)",
                "ar": "{d}: تعليق فقط في حال الزواج من جديد قبل سن {r}؛ استعادة، مع تعديل، عند "
                      "وفاة القرين الجديد أو حل الزواج؛ منع الجمع بين جرايات القرين الباقي على "
                      "قيد الحياة، وتُصرف الجراية الأعلى (القانون عدد 96-66، الفصل 63)"},
               d=L(f"{sv}/age_remariage_suspensif.yaml", d96,
                   lambda _v, lg: ot.formate_date(d96, lg), _lien("remariage")),
               r=lu("remariage", "age_remariage_suspensif", d96, _entier))],
            [{"fr": "Plafond de cumul", "ar": "سقف الجمع"},
             {"fr": "pension de référence du mari", "ar": "جراية الزوج المرجعية"},
             {"fr": "4 août 1996 : pension dont bénéficiait ou aurait pu bénéficier le défunt "
                    "(loi n° 96-66, art. 69)",
              "ar": "4 أوت 1996: الجراية التي كان يستفيد منها أو كان يمكن أن يستفيد منها "
                    "المتوفى (القانون عدد 96-66، الفصل 69)"}],
            [{"fr": "Âge limite de l'orphelin", "ar": "السن الأقصى لليتيم"},
             g({"fr": "orphelin mineur : {a} ; {e} en cas d'études ; sans limite en cas "
                      "d'infirmité",
                "ar": "يتيم قاصر: {a}؛ {e} في حال الدراسة؛ دون حدّ في حال العجز"},
               a=lu("age_orphelin", "age_limite_orphelin", d81),
               e=lu("age_orphelin_etudes", "age_limite_orphelin_etudes", d81)),
             g({"fr": "{d} : {a} ; {e} en études secondaires, techniques ou professionnelles ; "
                      "{s} en études supérieures sans bourse ; la fille, tant qu'elle ne "
                      "dispose pas de ressources ou que l'obligation alimentaire n'incombe pas "
                      "à son époux ; sans limite en cas d'infirmité (loi n° 97-61, art. 64) ; "
                      "2 juillet 2007 : fille sans limite d'âge, conditions appréciées au décès, "
                      "paiement définitivement suspendu si l'une d'elles fait défaut ; le mot "
                      "« mineur » est supprimé (loi n° 2007-43)",
                "ar": "{d}: {a}؛ {e} في الدراسات الثانوية أو الفنية أو المهنية؛ {s} في الدراسات "
                      "العليا دون منحة؛ البنت، ما دامت لا تملك موارد أو أن واجب النفقة لا يقع "
                      "على عاتق زوجها؛ دون حدّ في حال العجز (القانون عدد 97-61، الفصل 64)؛ "
                      "2 جويلية 2007: البنت دون حدّ للسن، تُقيّم الشروط عند الوفاة، ويُعلّق "
                      "الدفع نهائياً إذا فقد أحدها؛ تُحذف كلمة «قاصر» (القانون عدد 2007-43)"},
               d=L(f"{sv}/age_limite_orphelin_etudes_superieures.yaml", d97,
                   lambda _v, lg: ot.formate_date(d97, lg), _lien("age_orphelin_sup")),
               a=lu("age_orphelin", "age_limite_orphelin", d97),
               e=lu("age_orphelin_etudes", "age_limite_orphelin_etudes", d97),
               s=lu("age_orphelin_sup", "age_limite_orphelin_etudes_superieures", d97))],
            [{"fr": "Revalorisation", "ar": "تعديل الجرايات"},
             {"fr": "à chaque paiement, proportionnellement à la variation du SMAG",
              "ar": "عند كل دفع، تناسبياً مع تغيّر الأجر الأدنى الفلاحي المضمون"},
             {"fr": "aucune ; en 2026, le décret qui fixe le SMAG énonce que son augmentation "
                    "s'applique aux pensions de retraite (décret n° 2026-66, art. 5)",
              "ar": "لا شيء؛ في عام 2026، ينص الأمر الذي يحدد الأجر الأدنى الفلاحي المضمون على "
                    "أن زيادته تُطبق على جرايات التقاعد (الأمر عدد 2026-66، الفصل 5)"}],
        ]
        entetes = {
            "fr": [m["element"], f"Loi n° 81-6 ({date(d81)})", m["modifications"]],
            "ar": [m["element"], f"القانون عدد 81-6 ({date(d81)})", m["modifications"]],
        }[langue]
        return ot.tableau_gabarit(entetes, lignes, langue)

    def classes_revenu():
        """Les classes de revenus des trois régimes à assiette forfaitaire, à l'état en vigueur.

        Une ligne par régime, une colonne par rang de classe ; une classe que le régime n'a
        pas reste vide. Écrit au livre « Cotisations sociales », dont c'est l'assiette.
        """
        import pandas as pd

        mm = MOTS[langue]
        regimes = (
            (m["reg_rtns"], f"{RTNS}/revenu_reference", 10, "decret95-1166, art. 7", True),
            (m["reg_raci"], f"{RACI}/revenu_reference", 10, "decret2003-894, art. 5", False),
            (m["reg_rtte"], f"{RTTE}/revenu_reference", 4, "decret89-107, art. 6", False),
        )
        lignes = []
        for nom, noeud, nombre, cle, agricole in regimes:
            ot.releve_note(f"{noeud}/classes", m["lien_classes"].format(regime=nom))
            ligne = {m["regime"]: nom}
            effets = []
            heures = ot.en_vigueur(ot.serie_datee(f"{noeud}/heures_annuelles_smig.yaml"), ETAT)
            ot.releve_note(f"{noeud}/heures_annuelles_smig.yaml",
                           m["lien_heures"].format(regime=nom))
            reference = m["ref_smig"].format(h=ot.formate_dinars(heures[1]))
            if agricole:
                jours = ot.en_vigueur(ot.serie_datee(f"{noeud}/jours_annuels_smag.yaml"), ETAT)
                ot.releve_note(f"{noeud}/jours_annuels_smag.yaml",
                               m["lien_jours"].format(regime=nom))
                reference += m["ref_smag"].format(j=ot.formate_dinars(jours[1]))
            ligne[m["reference"]] = reference
            for k in range(1, 11):
                if k > nombre:
                    ligne[mm["classe"].format(k=k)] = ot.VIDE
                    continue
                point = ot.en_vigueur(ot.serie_datee(f"{noeud}/classes/classe_{k}.yaml"), ETAT)
                if point is None or point[1] is None:
                    print(f"✗ {noeud}/classes/classe_{k} : aucune valeur en vigueur")
                    return None
                effets.append(point[0])
                ligne[mm["classe"].format(k=k)] = f.coefficient(point[1])
            ligne = {m["regime"]: nom, m["effet"]: date(max(effets)),
                     **{c: v for c, v in ligne.items() if c != m["regime"]}}
            ligne[m["texte"]] = f"[@{cle}]"
            lignes.append(ligne)
        return pd.DataFrame(lignes)

    return {
        "classes_revenu.md": classes_revenu,
        "rsna_reference.md": rsna_reference,
        "rsna_invalidite.md": rsna_invalidite,
        "rsna_survivants.md": rsna_survivants,
        "rsa_evolution.md": rsa_evolution,
        "rsaa.md": rsaa,
        "complementaire.md": complementaire,
        "rtte.md": rtte,
        "rtfr.md": rtfr,
        "raci.md": raci,
        "cnrps_departs_anticipes.md": cnrps_departs,
        "cnrps_survivants.md": cnrps_survivants,
    }



def verifie_texte(df, colonne: str) -> str | None:
    """Refuse un tableau dont une ligne n'a pas de clé de citation.

    Sans ce garde-fou, une date d'effet ajoutée au paramètre et oubliée dans les `CLES_`
    ferait passer le titre entier de la référence dans la colonne — cent cinquante
    caractères de fascicule au milieu du tableau, et une citation qui ne se résout pas.
    """
    if colonne not in df.columns:
        return None
    for valeur in df[colonne]:
        texte = str(valeur)
        if not texte.startswith("[@"):
            return texte
    return None


# Livres où chaque tableau est écrit, quand ce n'est pas celui des retraites seul : la
# fabrique reste unique, le tableau est émis dans chaque livre (`ot.ecrire_dans_livres`).
LIVRE = "retraites"
LIVRES = {
    # Les indemnités familiales du secteur public : accessoire de la pension ici, prestation
    # familiale de l'agent en activité au livre « Prestations sociales ».
    "cnrps_indemnites_familiales.md": (LIVRE, "prestations_sociales"),
    # Les classes de revenus des trois régimes à assiette forfaitaire : l'assiette des
    # cotisations au livre « Cotisations sociales ».
    "classes_revenu.md": ("cotisations_sociales",),
}


def main() -> int:
    minimum = ot.PAQUETS[PAQUET]["version_minimale"]
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien "
            f"(version {ot.version_openfisca()}, minimum {minimum}). "
            f"Les snapshots existants sont conservés."
        )
        return 1
    for langue in LANGUES:
        sortie = RACINE / langue / "retraites" / "tables"
        sortie.mkdir(parents=True, exist_ok=True)
        fabriques = tableaux(langue)
        for nom, fabrique in fabriques.items():
            df, liens = ot.avec_liens(fabrique)
            if df is None or df.empty:
                print(f"✗ {langue}/{nom} : paramètre introuvable ou vide.")
                return 1
            manquante = verifie_texte(df, MOTS[langue]["texte"])
            if manquante is not None:
                print(f"✗ {langue}/{nom} : date d'effet sans clé de citation — {manquante}")
                return 1
            erreur = ot.ecrire_dans_livres(RACINE, langue, LIVRES.get(nom, (LIVRE,)), nom,
                                           df, liens)
            if erreur:
                print(erreur)
                return 1
        print(f"✓ {langue} : {len(fabriques)} tableaux")
    # Chaque série est émise quoi qu'il arrive aux autres, et le code de retour les
    # combine : une série vide ne doit pas en masquer une autre.
    codes = [
        serie_avec_liens("rsna-actualisation-salaires", serie_actualisation),
        serie_avec_liens("retraites-taux-liquidation", serie_taux_liquidation),
        serie_avec_liens("retraites-smig-planchers", serie_smig_planchers),
    ]
    return max(codes)


# Libellés des liens « Base législative » des figures, par clé notée à la lecture. La série
# brute n'a pas de langue ; ses liens en ont une, comme ceux des tableaux. Les équivalents
# arabes des notions sont ceux du glossaire bilingue.
LIBELLES_SERIES = {
    "fr": {
        "actualisation": "Barème d'actualisation des salaires retenus pour le salaire moyen "
                         "de référence, régime des salariés non agricoles",
        "cnrps_bareme": "CNRPS — barème des annuités",
        "cnrps_plafond": "CNRPS — plafond du taux de la pension",
        "cnrps_duree_minimale": "CNRPS — durée de services minimale",
        "rsna_bareme": "Régime des salariés non agricoles — barème des annuités",
        "rsna_plafond": "Régime des salariés non agricoles — plafond du taux de la pension",
        "rsna_stage": "Régime des salariés non agricoles — stage de cotisation",
        "rsna_stage_derog": "Régime des salariés non agricoles — stage dérogatoire",
        "smig_horaire": "SMIG horaire, régime de 48 heures",
        "cnrps_minimum": "CNRPS — pension minimale garantie, en fraction du SMIG",
        "cnrps_allocation": "CNRPS — allocation de vieillesse, en fraction du SMIG",
        "rsna_minimum": "Régime des salariés non agricoles — pension minimale de vieillesse "
                        "ou d'invalidité, en fraction du SMIG",
        "rsna_minimum_reduit": "Régime des salariés non agricoles — pension minimale de la "
                               "retraite anticipée et de la pension proportionnelle, en "
                               "fraction du SMIG",
        "rsna_limite": "Régime des salariés non agricoles — limite de calcul des "
                       "prestations, en multiple du SMIG",
    },
    "ar": {
        "actualisation": "جدول تحيين الأجور المعتمدة في احتساب الأجر المرجعي، "
                         "نظام الأجراء غير الفلاحيين",
        "cnrps_bareme": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — "
                        "جدول نسب السنوات القابلة للتصفية",
        "cnrps_plafond": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — سقف نسبة تصفية الجراية",
        "cnrps_duree_minimale": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — "
                                "المدة الدنيا للخدمات",
        "rsna_bareme": "نظام الأجراء غير الفلاحيين — جدول نسب السنوات القابلة للتصفية",
        "rsna_plafond": "نظام الأجراء غير الفلاحيين — سقف نسبة تصفية الجراية",
        "rsna_stage": "نظام الأجراء غير الفلاحيين — مدة الانخراط الدنيا",
        "rsna_stage_derog": "نظام الأجراء غير الفلاحيين — مدة الانخراط الدنيا الاستثنائية",
        "smig_horaire": "الأجر الأدنى المضمون لمختلف المهن بحساب الساعة، نظام 48 ساعة",
        "cnrps_minimum": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — "
                         "الجراية الدنيا المضمونة، كسرًا من الأجر الأدنى المضمون",
        "cnrps_allocation": "الصندوق الوطني للتقاعد والحيطة الاجتماعية — "
                            "منحة الشيخوخة، كسرًا من الأجر الأدنى المضمون",
        "rsna_minimum": "نظام الأجراء غير الفلاحيين — الجراية الدنيا للشيخوخة أو العجز، "
                        "كسرًا من الأجر الأدنى المضمون",
        "rsna_minimum_reduit": "نظام الأجراء غير الفلاحيين — الجراية الدنيا للتقاعد المبكّر "
                               "والجراية النسبية، كسرًا من الأجر الأدنى المضمون",
        "rsna_limite": "نظام الأجراء غير الفلاحيين — الحدّ الأقصى لاحتساب المنافع، "
                       "مضاعفًا للأجر الأدنى المضمون",
    },
}


def serie_avec_liens(nom: str, fabrique) -> int:
    """Émet une série sous relevé, puis ses liens `_seriescache/<nom>.liens.<langue>.yml`.

    Même esprit que `tables/<nom>.liens.yml` : chaque grandeur lue par la série est notée
    à la lecture (`ot.releve_note(chemin, clé)`), et la figure en tire son onglet « Base
    législative » sans jamais importer openfisca. Un relevé vide est une erreur : la
    série aurait été lue sans rien noter, et la figure perdrait ses liens en silence.
    """
    code, releve = ot.avec_liens(fabrique)
    if code:
        return code
    if not releve:
        print(f"✗ {nom} : aucune grandeur relevée, liens non écrits.")
        return 1
    for langue in LANGUES:
        liens = [(chemin, LIBELLES_SERIES[langue][cle]) for chemin, cle in releve]
        ot.ecrire_fichier_liens(CACHE / f"{nom}.liens.{langue}.yml", liens, langue)
    return 0


def serie_actualisation() -> int:
    """Émet la série brute du barème d'actualisation des salaires, pour la figure.

    Un paramètre par année de salaire, dont chaque valeur est celle d'un arrêté. La figure
    en tire des taux, qui ne se lisent pas dans un tableau markdown : la série est donc
    émise ici, hors du build — le site se construit sans openfisca (#165) —, une seule fois
    puisque des valeurs brutes n'ont pas de langue. Chaque ligne porte l'arrêté qui fixe
    le coefficient et son lien au Journal officiel.
    """
    # Un lien vers le barème entier, et non un par année : le nœud se lit en un tableau,
    # une colonne par année de salaires, avec l'arrêté de chaque barème.
    ot.releve_note(f"{RSNA}/salaire_reference/actualisation", "actualisation")
    lignes = []
    for annee in range(1961, datetime.date.today().year):
        chemin = f"{RSNA}/salaire_reference/actualisation/annee_{annee}.yaml"
        for date, valeur, titre, lien in ot.serie_datee(chemin):
            if valeur is not None:
                lignes.append((date, annee, valeur, titre, lien))
    if not lignes:
        print("✗ rsna-actualisation-salaires : série vide, snapshot conservé.")
        return 1
    lignes.sort()
    cache = RACINE / "_seriescache"
    cache.mkdir(parents=True, exist_ok=True)
    import pandas as pd

    pd.DataFrame(lignes, columns=["bareme", "annee_salaires", "coefficient", "arrete", "lien"]
                 ).to_csv(cache / "rsna-actualisation-salaires.csv", index=False)
    print(f"✓ série rsna-actualisation-salaires : {len(lignes)} coefficients, "
          f"{len({l[0] for l in lignes})} barèmes")
    return 0



# --------------------------------------------------- séries des figures « paramètres »

MARCHE = "parameters/marche_travail"
CACHE = RACINE / "_seriescache"

# Les salaires minimums des pensions sont exprimés en fraction du SMIG « rapporté à une
# durée d'occupation annuelle de 2 400 heures » — 200 heures par mois. Le SMIG mensuel du
# régime de 48 heures (`smig_48h_mensuel`) compte, lui, 208 heures : il n'est pas la base
# de ces montants, qui se calculent sur le SMIG HORAIRE.
HEURES_PAR_MOIS = 2400 / 12


# Une ligne par barème : (régime, chemin du barème, du plafond, de la durée minimale, de
# la durée des carrières courtes ou None). La durée minimale est celle qui ouvre la
# pension au taux du barème ; la figure en tire le tracé plein.
BAREMES = (
    ("cnrps", f"{CNRPS}/bareme_annuite.yaml", f"{CNRPS}/plaf_taux_pension.yaml",
     f"{CNRPS}/duree_de_service_minimale.yaml", None),
    ("rsna", f"{RSNA}/bareme_annuite.yaml", f"{RSNA}/plaf_taux_pension.yaml",
     f"{RSNA}/stage_requis.yaml", f"{RSNA}/stage_derog.yaml"),
)
# Clés des libellés de ces chemins (`LIBELLES_SERIES`), dans le même ordre.
CLES_BAREMES = {
    "cnrps": ("cnrps_bareme", "cnrps_plafond", "cnrps_duree_minimale", None),
    "rsna": ("rsna_bareme", "rsna_plafond", "rsna_stage", "rsna_stage_derog"),
}
DUREE_MAX_ANNEES = 45


def _lien_pist(lien: str) -> str:
    """Le lien au Journal officiel, s'il est sur pist.tn ; sinon rien."""
    return lien if lien.startswith("https://www.pist.tn/") else ""


def _valeur(chemin: str, date: datetime.date) -> float | None:
    donnees = ot.charge_parametre(chemin)
    if not donnees or "values" not in donnees:
        return None
    return ot.valeur_a_la_date(donnees["values"], date)


def _taux_cumule(tranches, trimestres: float) -> float:
    """Taux acquis au terme de `trimestres`, somme des tranches parcourues."""
    total = 0.0
    for indice, (seuil, taux) in enumerate(tranches):
        haut = tranches[indice + 1][0] if indice + 1 < len(tranches) else None
        borne = trimestres if haut is None else min(trimestres, haut)
        if borne > seuil:
            total += (borne - seuil) * taux
    return total


def serie_taux_liquidation() -> int:
    """Émet τ(n), le taux de liquidation selon la durée, pour chaque barème daté.

    Une ligne par (régime, barème, durée en années entières de 0 à 45). Le barème est lu
    à sa date d'effet, en trimestres ; le taux est plafonné par le plafond EN VIGUEUR À
    CETTE DATE s'il en existe un, et reste celui du barème sinon. Depuis la version 0.107
    d'openfisca-tunisia, le barème de 1959 est daté du 1er avril 1959, date à laquelle le
    plafond de 60 % existe : sa courbe plafonne donc à 60 % dès trente annuités.

    L'année seule du barème est émise, et non sa date.
    """
    import pandas as pd

    lignes = []
    for regime, bareme, plafond, minimum, courte in BAREMES:
        for chemin, cle in zip((bareme, plafond, minimum, courte), CLES_BAREMES[regime]):
            if chemin:
                ot.releve_note(chemin, cle)
        donnees = ot.charge_parametre(bareme) or {}
        references = (donnees.get("metadata") or {}).get("reference") or {}
        dates = sorted({ot._date_de_cle(cle) for cle in references})
        for date in dates:
            tranches = ot.bareme_a_la_date(bareme, date)
            if not tranches:
                continue
            titre, lien = ot._reference_a_la_date(donnees, date.isoformat())
            p = _valeur(plafond, date)
            n0 = _valeur(minimum, date)
            n1 = _valeur(courte, date) if courte else None
            for annees in range(DUREE_MAX_ANNEES + 1):
                brut = _taux_cumule(tranches, 4 * annees)
                lignes.append({
                    "regime": regime,
                    "annee_bareme": date.year,
                    "duree_annees": annees,
                    "taux_bareme": round(brut, 6),
                    "plafond": None if p is None else round(p, 6),
                    "taux": round(brut if p is None else min(brut, p), 6),
                    "duree_minimale": n0,
                    "duree_carriere_courte": n1,
                    "texte": titre,
                    "lien": _lien_pist(lien),
                })
    if not lignes:
        print("✗ retraites-taux-liquidation : série vide, snapshot conservé.")
        return 1
    CACHE.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(lignes)
    df.to_csv(CACHE / "retraites-taux-liquidation.csv", index=False)
    print(f"✓ série retraites-taux-liquidation : "
          f"{df.groupby(['regime', 'annee_bareme']).ngroups} barèmes")
    return 0


# Les fractions du SMIG, colonne par colonne : (colonne de la fraction, colonne du montant,
# chemin). Les montants sont mensuels : fraction × SMIG horaire × 200 heures.
FRACTIONS = (
    ("pi_cnrps", "minimum_cnrps", f"{CNRPS}/pension_minimale/minimum_garanti.yaml"),
    ("pi_cnrps_allocation", "allocation_cnrps",
     f"{CNRPS}/pension_minimale/allocation_vieillesse.yaml"),
    ("pi_rsna", "minimum_rsna", f"{RSNA}/pension_minimale/sup.yaml"),
    ("pi_rsna_reduit", "minimum_rsna_reduit", f"{RSNA}/pension_minimale/inf.yaml"),
)
# Clés des libellés des fractions (`LIBELLES_SERIES`), dans le même ordre.
CLES_FRACTIONS = ("cnrps_minimum", "cnrps_allocation", "rsna_minimum", "rsna_minimum_reduit")
SMIG_HORAIRE = f"{MARCHE}/smig_48h_horaire.yaml"
# Le multiple ℓ de la limite de calcul du RSNA : six SMIG rapportés à 2 400 heures depuis le
# 1er janvier 1974, trois rédactions de l'article 18 du décret n° 74-499 (1974, 1990, 1994),
# versé et daté par openfisca-tunisia#442 (version 0.99).
LIMITE_MULTIPLE = f"{RSNA}/salaire_reference/limite_multiple_smig.yaml"


def serie_smig_planchers() -> int:
    """Émet, date par date, le SMIG horaire et les montants mensuels qui en dépendent.

    Une ligne par date à laquelle l'un d'eux change, depuis le 1er janvier 1974 : hausse
    du SMIG, ou création d'une fraction. Chaque montant est la fraction EN VIGUEUR à la
    date appliquée au SMIG horaire du régime de 48 heures, rapporté à 200 heures par mois ;
    il est vide avant le texte qui crée la fraction. Toutes les dates d'effet sont émises,
    paliers déjà publiés des années à venir compris : une série coupée au jour du calcul
    changerait d'une semaine à l'autre sans que rien n'ait bougé.

    La ligne porte le décret qui fixe le SMIG en vigueur, et son lien au Journal officiel
    lorsqu'il est sur pist.tn.
    """
    import pandas as pd

    ot.releve_note(SMIG_HORAIRE, "smig_horaire")
    for (_, _, chemin), cle in zip(FRACTIONS, CLES_FRACTIONS):
        ot.releve_note(chemin, cle)
    ot.releve_note(LIMITE_MULTIPLE, "rsna_limite")
    smig = ot.serie_datee(SMIG_HORAIRE)
    if not smig:
        print("✗ retraites-smig-planchers : SMIG introuvable, snapshot conservé.")
        return 1
    dates = {datetime.date.fromisoformat(d) for d, *_ in smig}
    for _, _, chemin in FRACTIONS:
        dates |= {datetime.date.fromisoformat(d) for d, *_ in ot.serie_datee(chemin)}
    limite = ot.serie_datee(LIMITE_MULTIPLE)
    if not limite:
        print("✗ retraites-smig-planchers : limite de calcul du RSNA introuvable, "
              "snapshot conservé.")
        return 1
    limite_depuis = min(datetime.date.fromisoformat(d) for d, *_ in limite)
    dates |= {datetime.date.fromisoformat(d) for d, *_ in limite}
    dates = sorted(d for d in dates if d >= limite_depuis)

    lignes = []
    for date in dates:
        horaire = _valeur(SMIG_HORAIRE, date)
        if horaire is None:
            continue
        mensuel = horaire * HEURES_PAR_MOIS
        _d, _v, titre, lien = max(
            (s for s in smig if datetime.date.fromisoformat(s[0]) <= date),
            key=lambda s: s[0])
        ligne = {"date": date.isoformat(), "smig_horaire": round(horaire, 5),
                 "smig_200h": round(mensuel, 3)}
        for col_pi, col_montant, chemin in FRACTIONS:
            pi = _valeur(chemin, date)
            ligne[col_pi] = None if pi is None else round(pi, 6)
            ligne[col_montant] = None if pi is None else round(pi * mensuel, 3)
        ell = _valeur(LIMITE_MULTIPLE, date)
        ligne["ell_rsna"] = None if ell is None else float(ell)
        ligne["limite_calcul_rsna"] = None if ell is None else round(ell * mensuel, 3)
        ligne["texte_smig"] = titre
        ligne["lien_smig"] = _lien_pist(lien)
        lignes.append(ligne)
    CACHE.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(lignes)
    df.to_csv(CACHE / "retraites-smig-planchers.csv", index=False)
    print(f"✓ série retraites-smig-planchers : {len(df)} dates, "
          f"{df['date'].iloc[0]} → {df['date'].iloc[-1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

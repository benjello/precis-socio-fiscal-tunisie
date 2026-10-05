"""Régénère les snapshots Markdown des tableaux du livre « Cotisations sociales ».

Même contrat que les deux générateurs qui précèdent : le build ne lance pas ce script, il
lit les fichiers versionnés dans `precis/{fr,ar}/cotisations_sociales/tables/`.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_cotisations_tables.py

Les cotisations sont encodées en barèmes (`brackets`) et non en valeurs scalaires, même
quand elles n'ont qu'un taux unique : d'où `ot.taux_datee` et `ot.tableau_taux_datee`, qui
lisent le taux de la première tranche. Le seul régime réellement plafonné — celui des
travailleurs à faibles revenus — passe par `ot.tableau_bareme`.

CE QUE CES TABLEAUX DISENT ET NE DISENT PAS. Les taux du secteur privé sont exacts mais
portent tous le 1er janvier 1960, qui n'est la date d'aucun d'entre eux : la colonne
« Texte » y est donc vide, et le chapitre doit le dire plutôt que de laisser croire à une
stabilité de soixante-cinq ans. Le secteur public, lui, est daté et sourcé.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

COT = "parameters/prelevements_sociaux/cotisations_sociales"
PRIVE = f"{COT}/secteur_prive"
PUBLIC = f"{COT}/secteur_public"
RACINE = Path(__file__).parent.parent / "precis"
LANGUES = ("fr", "ar")

MOTS = {
    "fr": {
        "effet": "Effet", "texte": "Texte", "branche": "Branche",
        "salarie": "Part salariale", "employeur": "Part patronale",
        "assure": "Cotisation de l'assuré",
        "total": "Total", "regime": "Régime", "taux": "Taux",
        "total_obligatoire": "**Total obligatoire**",
        "tranche": "Tranche d'assiette (en SMIG)",
        "retraite": "Retraite", "maladie": "Maladie", "maternite": "Maternité",
        "deces": "Décès", "famille": "Prestations familiales",
        "at": "Accidents du travail", "perte_emploi": "Perte d'emploi",
        "fse": "Fonds spécial de l'État",
        "pst": "Protection sociale des travailleurs",
        "soin": "Soins",
        "complementaire": "Retraite complémentaire (facultative)",
        "cnrps_retraite": "Cotisation retraite du salarié affilié à la CNRPS",
        "point": "Point", "secteur": "Secteur d'activité",
        "avant": "Avant transfert du point", "apres": "Après transfert du point",
        "cnrps_employeur": "Contribution de l'employeur public",
        "variation": "Variation (en points)",
        "prevoyance": "Cotisation de prévoyance sociale du pensionné",
        "reduction": "Réduction de la part patronale du taux global (en points)",
        "aucune": "aucune",
        "css_salarie": "Contribution sociale de solidarité, taux applicable aux salariés",
        "maladie_employeur": "Part de l'employeur public", "maladie_agent": "Part de l'agent",
        "perte_employeur": "Part de l'employeur", "perte_salarie": "Part du salarié",
        "tfp_manuf": "Taxe de formation professionnelle, industries manufacturières",
        "tfp_autres": "Taxe de formation professionnelle, autres secteurs",
        "foprolos": "Contribution au FOPROLOS",
    },
    "ar": {
        "effet": "بداية السريان", "texte": "النصّ", "branche": "الفرع",
        "salarie": "مساهمة الأجراء", "employeur": "مساهمة الأعراف",
        "assure": "اشتراك المضمون",
        "total": "المجموع", "regime": "النظام", "taux": "النسبة",
        "total_obligatoire": "**المجموع الوجوبي**",
        "tranche": "شريحة الوعاء (بالأجر الأدنى)",
        "retraite": "التقاعد", "maladie": "المرض", "maternite": "الولادة",
        "deces": "الوفاة", "famille": "المنح العائلية",
        "at": "حوادث الشغل", "perte_emploi": "فقدان الشغل",
        "fse": "الصندوق الخاص للدولة",
        "pst": "الحماية الاجتماعية للعملة",
        "soin": "العلاج",
        "complementaire": "التقاعد التكميلي (اختياري)",
        "cnrps_retraite": "مساهمة التقاعد للأجير المنخرط بالصندوق الوطني للتقاعد",
        "point": "العدد", "secteur": "قطاع النشاط",
        "avant": "قبل تحويل النقطة", "apres": "بعد تحويل النقطة",
        "cnrps_employeur": "مساهمة صاحب العمل العمومي",
        "variation": "التغيّر (بالنقاط)",
        "prevoyance": "مساهمة الحيطة الاجتماعية لصاحب الجراية",
        "reduction": "التخفيض في حصة صاحب العمل من النسبة الإجمالية (بالنقاط)",
        "aucune": "لا شيء",
        "css_salarie": "المساهمة الاجتماعية التضامنية، النسبة المطبّقة على الأجراء",
        "maladie_employeur": "مساهمة المؤجر العمومي", "maladie_agent": "مساهمة العون",
        "perte_employeur": "مساهمة المؤجر", "perte_salarie": "مساهمة الأجير",
        "tfp_manuf": "الأداء على التكوين المهني، الصناعات المعملية",
        "tfp_autres": "الأداء على التكوين المهني، القطاعات الأخرى",
        "foprolos": "المساهمة الراجعة لصندوق النهوض بالمسكن لفائدة الأجراء",
    },
}

# Ordre de lecture commun à tous les régimes, des branches les plus lourdes aux plus
# légères. Les régimes n'ont pas les mêmes branches — le RSNA en a dix, le RTFR deux — et
# c'est l'arborescence du régime qui décide des lignes présentes ; cette table ne fixe que
# l'ordre et le libellé.
ORDRE_BRANCHES = [
    ("retraite", "retraite.yaml"),
    ("maladie", "assurances_sociales/maladie.yaml"),
    ("maternite", "assurances_sociales/maternite.yaml"),
    ("deces", "assurances_sociales/deces.yaml"),
    ("soin", "soin.yaml"),
    ("famille", "famille.yaml"),
    ("at", "accident_du_travail.yaml"),
    ("perte_emploi", "perte_d_emploi.yaml"),
    ("pst", "protection_sociale_travailleurs.yaml"),
    ("fse", "fonds_special_etat.yaml"),
    ("complementaire", "retraite_complementaire.yaml"),
]

REGIMES = [
    ("rsna", "Salariés non agricoles", "الأجراء غير الفلاحيين", ""),
    ("rsa", "Salariés agricoles", "الأجراء الفلاحيون", ""),
    ("rsaa", "Salariés agricoles, régime amélioré", "الأجراء الفلاحيون، النظام المحسّن", ""),
    ("rtns", "Travailleurs non salariés", "العملة غير الأجراء", ""),
    ("raci", "Artistes, créateurs et intellectuels", "الفنانون والمبدعون والمثقفون", ""),
    ("rtfr", "Travailleurs à faibles revenus", "العملة ذوو الدخل الضعيف", "forfait"),
    ("rtte", "Tunisiens à l'étranger", "التونسيون بالخارج", ""),
]

# Le régime des étudiants ne relève pas d'un taux : c'est un montant forfaitaire, et il
# n'a donc pas sa place dans un tableau de pourcentages. Le chapitre le dit en prose.
#
# Le 0,66 du RTFR n'est PAS un plafond. L'article 7 de la loi n° 2002-32 et l'article 13
# du décret n° 2002-916 assoient les cotisations de ce régime sur les deux tiers du SMIG
# ou du SMAG selon la catégorie : c'est une assiette forfaitaire, et non un seuil au-delà
# duquel on cesserait de prélever. Le modèle l'encode en seuil de barème faute de mieux.
NOTE_FORFAIT = {
    "fr": " (assiette forfaitaire des deux tiers du SMIG ou du SMAG)",
    "ar": " (وعاء جزافي يساوي ثلثي الأجر الأدنى الصناعي أو الفلاحي)",
}


ATMP = "parameters/prelevements_sociaux/atmp"
ATMP_AVANT = "parameters/prelevements_sociaux/atmp_avant_transfert"
ATMP_1995 = "parameters/prelevements_sociaux/atmp_1995"

# ÉCHELLE AT/MP DU DÉCRET N° 99-1010 (article 2 nouveau du décret n° 95-538), en vigueur le
# 1er avril 1999. Les libellés sont ceux du texte, point par point : français de l'édition
# française (JORT n° 40 du 18 mai 1999, pp. 733-734), arabe TRANSCRIT de l'édition arabe
# (pp. 897-898), qui fait foi — non traduit. Les deux éditions ne disent pas toujours la même
# chose : le point 14-3 est « industrie du cuir » en français, « صناعة الأحذية » (industrie de
# la chaussure) en arabe. Les `short_label` du modèle ne servent pas ici : ils sont en
# français seulement, et ceux des points 9-2 et 9-3 reprennent par erreur celui du 9-1.
# Le numéro de point de chaque feuille se lit dans sa référence (« …, point 3-1 »).
SECTEURS_ATMP_1999 = {
    "1": ("Services de bureaux", "الخدمات المكتبيّة"),
    "2": ("Autres services", "الخدمات الأخرى"),
    "3": ("Commerce", "التجارة"),
    "3-1": ("Commerce de gros", "تجارة الجملة"),
    "3-2": ("Commerce de détail", "تجارة التفصيل"),
    "4": ("Secteur des industries artisanales", "قطاع الصناعات التقليدية"),
    "5": ("Agriculture et pêche", "الفلاحة والصيد البحري"),
    "6": ("Industries agro-alimentaires", "الصناعات الفلاحية والغذائية"),
    "6-1": ("Industries du lait et dérivés", "صناعات الحليب ومشتقاته"),
    "6-2": ("Industries des huiles et des corps gras", "صناعة الزيوت والمواد الدسمة"),
    "6-3": ("Travail des graines", "صناعة الحبوب والدقيق"),
    "6-4": ("Industries de conserverie et semi-conserverie", "صناعة المصبرات ونصف المصبرات"),
    "6-5": ("Industries de séchage et déshydratation", "صناعة تجفيف الأغذية"),
    "6-6": ("Industries du sucre, chocolaterie et dérivés", "صناعة السكر والشوكلاطة ومشتقاتها"),
    "6-7": ("Industries de boissons, boissons alcoolisées et vinaigre",
            "صناعة المشروبات والمشروبات الكحولية والخلّ"),
    "6-8": ("Industries d'aliments composés", "صناعة العلف المركب"),
    "6-9": ("Les abattoirs", "المسالخ"),
    "6-10": ("Autres industries agro-alimentaires", "صناعات غذائية وفلاحية أخرى"),
    "7": ("Industries du tabac", "صناعة التبغ"),
    "8": ("Industries du papier et des arts graphiques", "صناعات الورق وفنون الرسم"),
    "8-1": ("Fabrication du papier et carton", "صناعة الورق والورق المقوّى"),
    "8-2": ("Transformation du papier et carton", "تحويل الورق والورق المقوّى"),
    "8-3": ("Imprimerie et édition", "الطباعة والنشر"),
    "9": ("Industries mécaniques", "الصناعات الميكانيكية"),
    "9-1": ("Fabrication de machines et équipements mécaniques",
            "صناعة الآلات والمعدات الميكانيكية"),
    "9-2": ("Fabrication d'équipements et d'appareils domestiques",
            "صناعة المعدات والتجهيزات المنزلية"),
    "9-3": ("Fabrication automobile et de matériel de transport", "صناعة السيارات ووسائل النقل"),
    "10": ("Industrie de fonderie et sidérurgie", "الصناعات المعدنية والمسابك"),
    "11": ("Fabrication de machines et appareils électriques", "صناعة الآلات والمعدات الكهربائية"),
    "12": ("Fabrication de machines de bureau et de matériels informatiques",
           "صناعة الآلات المكتبية والحاسوب"),
    "13": ("Fabrication d'accumulateurs et de piles électriques", "صناعة البطاريات"),
    "14": ("Industries de textile, confection du cuir et des chaussures",
           "صناعات النسيج والملابس والجلد والأحذية"),
    "14-1": ("Filature et tissage", "صناعة الغزل والنسيج"),
    "14-2": ("Fabrication de vêtements et de fourrures, délavage et blanchisserie",
             "صناعة الملابس والفرو وغسلها وتبييضها"),
    "14-3": ("Industrie du cuir", "صناعة الأحذية"),
    "14-4": ("Les tanneries", "المدابغ"),
    "14-5": ("Fabrication de divers articles en cuir", "صناعة مواد مختلفة من الجلد"),
    "15": ("Industrie du bois", "صناعة الخشب"),
    "16": ("Industrie du meuble et de menuiserie", "صناعة الأثاث والنجارة"),
    "17": ("Industrie du liège", "صناعة الفلين"),
    "18": ("Industrie des matériaux de construction", "صناعة مواد البناء"),
    "19": ("Industrie de verrerie", "صناعة البلور"),
    "20": ("Industrie de la céramique (à l'exception des industries artisanales)",
           "صناعة الخزف (باستثناء الصناعات التقليدية)"),
    "21": ("Autres industries manufacturières", "صناعة معمليّة أخرى"),
    "22": ("Industries chimiques", "الصناعات الكيمياويّة"),
    "22-1": ("Industries chimiques minérales", "الصناعات الكيمياوية المعدنيّة"),
    "22-2": ("Fabrication des produits minéraux divers", "إنتاج المواد المعدنيّة المختلفة"),
    "22-3": ("Fabrication d'engrais et industries de l'azote", "إنتاج الأسمدة وصناعات الأزوت"),
    "22-4": ("Industrie de la synthèse organique", "صناعة التركيبات العضويّة"),
    "22-5": ("Fabrication de produits pharmaceutiques", "صناعة الأدوية والمستحضرات الصيدلية"),
    "22-6": ("Fabrication de peintures, vernis, pigments broyés",
             "صناعة الدهن والفرنيز والصباغ المسحوقة"),
    "22-7": ("Fabrication des produits insecticides et anticryptogamiques",
             "صناعة المواد المبيدة والفطريّة"),
    "22-8": ("Fabrication d'explosifs industriels, d'accessoires, de mises à feu et d'artifices",
             "صناعة المفرقعات الصناعية وتوابعها وأدوات الإشعال والشماريخ"),
    "22-9": ("Forage de pétrole", "التنقيب عن النفط"),
    "22-10": ("Fabrication de gaz industriels", "إنتاج الغاز الصناعي"),
    "22-11": ("Raffinage de pétrole", "مصفاة البترول"),
    "22-12": ("Fabrication des dérivés du pétrole", "صناعة مشتقات المواد البترولية"),
    "22-13": ("Fabrication de caoutchouc et d'ouvrages en caoutchouc",
              "صناعة المطاط والمنتوجات المطاطية"),
    "22-14": ("Fabrication d'ouvrages en matière plastique et de la mousse",
              "صناعة المواد البلاستيكية ورغوة البلاستيك"),
    "22-15": ("Fabrication de savons, de parfums et de produits d'entretien",
              "صناعة الصابون والعطور ومواد التنظيف"),
    "22-16": ("Autres industries chimiques", "صناعات كيمياويّة أخرى"),
    "23": ("Bâtiment et travaux publics", "البناء والأشغال العامة"),
    "24": ("Activités annexes au secteur du bâtiment et travaux publics",
           "نشاطات مرتبطة بقطاع البناء والأشغال العامة"),
    "24-1": ("Installation de menuiserie de bois, de menuiserie métallique et serrurerie",
             "أشغال تركيب المصنوعات الخشبيّة والمعدنيّة والأقفال"),
    "24-2": ("Travaux de plomberie et d'installation d'équipements thermiques et de climatisation",
             "أعمال السباكة وتركيب أجهزة التدفئة والتبريد"),
    "24-3": ("Travaux de peinture et de vitrerie", "أشغال الدهن وتركيب البلور"),
    "24-4": ("Réalisation de charpentes et de couvertures", "إنجاز البناءات المعدنيّة وأعمال التغطية"),
    "24-5": ("Travaux d'installation électrique", "تجهيز البناءات بالكهرباء"),
    "24-6": ("Autres travaux d'installation et de finition", "أشغال أخرى"),
    "25": ("Construction et réparation navale", "البناءات البحريّة"),
    "26": ("Activités liées aux constructions et réparations navales",
           "نشاطات مرتبطة بالبناءات البحريّة"),
    "27": ("Transport et manutention", "النقل والشحن والترصيف"),
    "27-1": ("Transports terrestres", "النقل البريّ"),
    "27-2": ("Transports maritimes", "النقل البحريّ"),
    "27-3": ("Transports aériens", "النقل الجويّ"),
    "27-4": ("Manutention et entreposage", "الشحن والترصيف"),
    "28": ("Auto-école", "تعليم السياقة"),
    "29": ("Industries extractives", "الصناعات الإستخراجيّة"),
    "30": ("Location de la main-d'œuvre pour les services administratifs",
           "كراء اليد العاملة للمصالح الإدارية"),
    "31": ("Gardiennage", "الحراسة"),
    "32": ("Location de la main-d'œuvre autre que pour les services administratifs et le gardiennage",
           "كراء اليد العاملة لغير المصالح الإدارية والحراسة"),
    "33": ("Hôtellerie", "النزل"),
    "34": ("Agences de voyage", "وكالات الأسفار"),
    "34-1": ("Agence de voyage, catégorie A", "وكالات الأسفار رخصة صنف أ"),
    "34-2": ("Agence de voyage, catégorie B", "وكالات الأسفار رخصة صنف ب"),
    "35": ("Concessionnaires automobiles", "متعهدي بيع السيارات"),
    "35-1": ("Avec atelier de réparation", "مع وجود ورشة إصلاح"),
    "35-2": ("Sans atelier de réparation", "بدون وجود ورشة إصلاح"),
    "36": ("Location de voitures et d'équipements", "كراء السيارات والمعدّات"),
    "36-1": ("Sans chauffeur et sans atelier de réparation", "بدون سائق ولا ورشة إصلاح"),
    "36-2": ("Avec atelier de réparation", "مع وجود ورشة إصلاح"),
    "36-3": ("Avec chauffeur", "مع وجود سائق"),
    "37": ("Les activités sportives", "الأنشطة الرياضيّة"),
}


def _points(noeud: str) -> dict[str, str]:
    """Chemin relatif -> numéro de point, lu dans la référence de chaque feuille.

    Un sous-nœud prend le numéro commun à ses feuilles (« 3 » pour « 3-1 » et « 3-2 »).
    """
    points = {}
    for relatif, _p, est_noeud in ot.arborescence(noeud):
        if est_noeud:
            continue
        donnees = ot.charge_parametre(f"{noeud}/{relatif}.yaml") or {}
        refs = (donnees.get("metadata") or {}).get("reference") or {}
        titres = [r.get("title", "") for liste in refs.values() for r in (liste or [])]
        trouve = next((m.group(1) for t in titres
                       if (m := re.search(r"point (\d+(?:-\d+)?)$", t))), None)
        if trouve is None:
            raise ValueError(f"point introuvable dans la référence de {noeud}/{relatif}")
        points[relatif] = trouve
    for relatif, _p, est_noeud in ot.arborescence(noeud):
        if est_noeud:
            enfants = [v for k, v in points.items() if k.startswith(relatif + "/")]
            points[relatif] = enfants[0].split("-")[0]
    return points


# ÉCHELLE AT/MP DU DÉCRET N° 95-538 (articles 1er et 2), du 1er janvier 1995 au 31 mars 1999.
# Libellés de l'article 2 : français de l'édition française (JORT n° 30 du 14 avril 1995,
# p. 691), arabe TRANSCRIT de l'édition arabe (p. 691). Les dix alinéas du point 15-1 ne sont
# pas numérotés dans le texte : la clé est donc le chemin de la feuille, pas un numéro.
# chemin relatif -> (numéro, français, arabe)
SECTEURS_ATMP_1995 = {
    "services_de_bureaux": ("1", "Services de bureaux", "الخدمات المكتبية"),
    "autres_services": ("2", "Autres services", "الخدمات الأخرى"),
    "commerce": ("3", "Commerce", "التجارة"),
    "artisans": ("4", "Artisans", "الصناعات التقليدية"),
    "agriculture_et_peche": ("5", "Agriculture et pêche", "الفلاحة والصيد البحري"),
    "industries_agro_alimentaires": ("6", "Industries agro-alimentaires", "الصناعات الفلاحية والغذائية"),
    "industries_agro_alimentaires/lait_et_derives": ("6-1", "Industrie du lait et dérivés", "صناعة الحليب ومشتقاته"),
    "industries_agro_alimentaires/corps_gras": ("6-2", "Industrie des corps gras", "صناعة المواد الدسمة"),
    "industries_agro_alimentaires/travail_des_graines": ("6-3", "Travail des graines", "صناعة الحبوب والدقيق"),
    "industries_agro_alimentaires/conserverie_semi_conserverie": (
        "6-4", "Industrie de conserverie et semi-conserverie", "صناعة المصبرات ونصف المصبرات"),
    "industries_agro_alimentaires/sechage_deshydratation": (
        "6-5", "Industrie de séchage et de déshydratation", "صناعة تجفيف الأغذية"),
    "industries_agro_alimentaires/sucre_chocolat_derives": (
        "6-6", "Industrie du sucre, chocolaterie et dérivés", "صناعة السكر والشوكلاطة ومشتقاتها"),
    "industries_agro_alimentaires/boissons_alcools_vinaigre": (
        "6-7", "Industrie de boissons, boissons alcoolisées et vinaigre",
        "صناعات المشروبات والمشروبات الكحولية والخل"),
    "industries_agro_alimentaires/alimentaires_diverses": (
        "6-8", "Industries alimentaires diverses", "صناعات غذائية مختلفة"),
    "industries_agro_alimentaires/aliments_composes": ("6-9", "Industries d'aliments composés", "صناعة العلف المركب"),
    "industries_agro_alimentaires/autres_agro_alimentaires": (
        "6-10", "Autres industries agro-alimentaires", "صناعات فلاحية وغذائية أخرى"),
    "industrie_du_froid": ("7", "Industrie du froid", "صناعة التبريد"),
    "papier_et_arts_graphiques": ("8", "Industrie du papier et des arts graphiques", "صناعة الورق وفنون الرسم"),
    "papier_et_arts_graphiques/fabrication_papier_carton": (
        "8-1", "Fabrication du papier et carton", "صناعة الورق والورق المقوى"),
    "papier_et_arts_graphiques/imprimerie_transformation_papier_carton": (
        "8-2", "Imprimerie et transformation du papier et carton", "الطباعة وتحويل الورق والورق المقوى"),
    "mecaniques_fonderies_electriques": (
        "9", "Industries mécaniques, de fonderies et électriques", "الصناعات الميكانيكية والمعدنية والكهربائية"),
    "mecaniques_fonderies_electriques/mecaniques": ("9-1", "Industries mécaniques", "الصناعات الميكانيكية"),
    "mecaniques_fonderies_electriques/fonderie_siderurgie": (
        "9-2", "Industries de fonderie et sidérurgie", "الصناعات المعدنية والمسابك"),
    "mecaniques_fonderies_electriques/electriques": ("9-3", "Industries électriques", "الصناعات الكهربائية"),
    "textile_cuir_chaussures": (
        "10", "Industries de textile, du cuir et des chaussures", "صناعات النسيج والجلد والأحذية"),
    "meuble": ("11", "Industrie du meuble", "صناعة الأثاث"),
    "materiaux_construction_ceramique_verrerie": (
        "12", "Industrie des matériaux de construction, de la céramique et de verrerie",
        "صناعة مواد البناء والخزف والبلور"),
    "bois_liege": ("13", "Industrie du bois et du liège", "صناعة الخشب والفلين"),
    "autres_industries_manufacturieres": ("14", "Autres industries manufacturières", "صناعات معملية أخرى"),
    "industries_chimiques": ("15", "Industries chimiques", "الصناعات الكيميائية"),
    "industries_chimiques/grandes_industries_chimiques": (
        "15-1", "Grandes industries chimiques", "الصناعات الكيميائية الكبيرة"),
    "industries_chimiques/grandes_industries_chimiques/chimiques_minerales": (
        "", "Grandes industries chimiques minérales", "الصناعات الكبرى في الكيميا المعدنية"),
    "industries_chimiques/grandes_industries_chimiques/produits_mineraux_divers": (
        "", "Fabrication de produits minéraux divers", "إنتاج المواد المعدنية المختلفة"),
    "industries_chimiques/grandes_industries_chimiques/engrais_azote": (
        "", "Fabrication d'engrais et industries de l'azote", "إنتاج الأسمدة وصناعات الأزوت"),
    "industries_chimiques/grandes_industries_chimiques/synthese_organique": (
        "", "Industries de la synthèse organique", "صناعة التركيبات العضوية"),
    "industries_chimiques/grandes_industries_chimiques/explosifs_mises_a_feu_artifices": (
        "", "Fabrication d'explosifs industriels, d'accessoires, de mises à feu et d'artifices",
        "صناعة المفرقعات الصناعية وتوابعها وأدوات الإشعال والشماريخ"),
    "industries_chimiques/grandes_industries_chimiques/produits_pharmaceutiques": (
        "", "Fabrication de produits pharmaceutiques", "صناعة مواد الصيدلة"),
    "industries_chimiques/grandes_industries_chimiques/peintures_vernis_pigments": (
        "", "Fabrication de peintures, vernis, pigments broyés", "صناعة الدهن والفرنيز والصباغ المسحوقة"),
    "industries_chimiques/grandes_industries_chimiques/insecticides_anticryptogamiques": (
        "", "Fabrication de produits insecticides et anticryptogamiques", "صناعة المواد المبيدة والفطرية"),
    "industries_chimiques/grandes_industries_chimiques/raffineries_petrole": (
        "", "Raffineries de pétrole", "مصفاة البترول"),
    "industries_chimiques/grandes_industries_chimiques/derives_petrole_charbon_caoutchouc_plastique": (
        "", "Fabrication des dérivés du pétrole et du charbon, et d'ouvrages en caoutchouc et en matière plastique",
        "إنتاج مشتقات النفط والفحم الحجري والمنتوجات المطاطية والمواد البلاستيكية"),
    "industries_chimiques/autres_industries_chimiques": ("15-2", "Autres industries chimiques", "صناعات كيميائية أخرى"),
    "batiment_et_travaux_publics": ("16", "Bâtiment et travaux publics", "البناء والأشغال العامة"),
    "transport_et_manutention": ("17", "Transport et manutention", "النقل والشحن والترصيف"),
    "industries_extractives": ("18", "Industries extractives", "الصناعات الإستخراجية"),
}


def atmp_1999(langue):
    """Échelle AT/MP de 1999, une ligne par secteur, dans l'ordre du décret.

    Deux colonnes, sur la même arborescence : l'article premier nouveau (avant transfert du
    point du régime général) et l'article 2 nouveau (après).
    """
    m = MOTS[langue]
    points = _points(ATMP)
    rang = 0 if langue == "fr" else 1
    libelles = {relatif: SECTEURS_ATMP_1999[point][rang] for relatif, point in points.items()}
    return ot.tableau_arborescence(
        ATMP, [(ATMP_AVANT, "1999-04-01", m["avant"], _taux(langue)),
               (ATMP, "1999-04-01", m["apres"], _taux(langue))],
        libelles=libelles, entete_libelle=m["secteur"],
        numeros=points, entete_numero=m["point"])


def atmp_1995(langue):
    """Échelle AT/MP de 1995 : dix-huit classes, articles 1er et 2 du décret n° 95-538."""
    m = MOTS[langue]
    avant, apres = f"{ATMP_1995}/avant_transfert", f"{ATMP_1995}/apres_transfert"
    lignes = {relatif for relatif, _p, _n in ot.arborescence(apres)}
    if lignes != set(SECTEURS_ATMP_1995):
        raise ValueError(f"libellés AT/MP 1995 désaccordés : {sorted(lignes ^ set(SECTEURS_ATMP_1995))}")
    rang = 1 if langue == "fr" else 2
    return ot.tableau_arborescence(
        apres, [(avant, "1995-01-01", m["avant"], _taux(langue)),
                (apres, "1995-01-01", m["apres"], _taux(langue))],
        libelles={k: v[rang] for k, v in SECTEURS_ATMP_1995.items()},
        entete_libelle=m["secteur"],
        numeros={k: v[0] for k, v in SECTEURS_ATMP_1995.items()}, entete_numero=m["point"])


def _taux(langue):
    def rendu(v):
        return "—" if v is None else ot.formate_taux(v)
    return rendu


def _dernier(chemin: str) -> float | None:
    serie = ot.taux_datee(chemin)
    return serie[-1][1] if serie else None


def _somme_cote(regime: str, cote: str) -> float | None:
    """Somme des taux en vigueur d'un côté d'un régime, hors retraite complémentaire.

    On PARCOURT l'arborescence du régime au lieu d'énumérer des branches connues : les
    régimes n'ont pas les mêmes, et une liste écrite à la main deviendrait fausse au
    premier paramètre ajouté. La retraite complémentaire est écartée parce qu'elle est
    facultative et ne fait donc pas partie du prélèvement obligatoire.
    """
    racine = ot._racine_paquet()
    if racine is None:
        return None
    dossier = Path(str(racine)) / "parameters" / Path(PRIVE).relative_to("parameters") / regime
    base = dossier / f"cotisations_{cote}"
    if not base.is_dir():
        return None
    somme, trouve = 0.0, False
    for fichier in sorted(base.rglob("*.yaml")):
        if fichier.name == "index.yaml" or "retraite_complementaire" in fichier.name:
            continue
        relatif = fichier.relative_to(Path(str(racine))).as_posix()
        valeur = _dernier(relatif)
        if valeur is not None:
            somme += valeur
            trouve = True
    return somme if trouve else None


def branches(regime: str):
    """Fabrique le tableau des branches d'un régime, part salariale et part patronale.

    Une ligne par branche effectivement présente dans l'arborescence du régime : une
    branche que le régime ne connaît pas n'apparaît pas, et une branche qu'un seul des
    deux côtés supporte affiche un tiret de l'autre.
    """
    def tableau(langue):
        import pandas as pd

        m = MOTS[langue]
        lignes = []
        cumul = {"salarie": 0.0, "employeur": 0.0}
        # Un régime sans employeur — non-salariés, artistes, Tunisiens à l'étranger —
        # doit garder le tiret jusque dans sa ligne de total : y écrire « 0 % » ferait
        # croire à une part patronale nulle là où il n'y a pas d'employeur.
        vu = {"salarie": False, "employeur": False}
        # Sans employeur, la cotisation est celle de l'assuré lui-même : les textes disent
        # « les cotisations des assurés » / « اشتراكات المضمونين » (décret n° 89-107, art. 9 ;
        # décret n° 95-1166, art. 10), jamais « part salariale ».
        sans_employeur = all(
            _dernier(f"{PRIVE}/{regime}/cotisations_employeur/{r}") is None
            for _c, r in ORDRE_BRANCHES)
        col_sal = m["assure"] if sans_employeur else m["salarie"]
        for cle, relatif in ORDRE_BRANCHES:
            sal = _dernier(f"{PRIVE}/{regime}/cotisations_salarie/{relatif}")
            emp = _dernier(f"{PRIVE}/{regime}/cotisations_employeur/{relatif}")
            if sal is None and emp is None:
                continue
            for cote, taux in (("salarie", sal), ("employeur", emp)):
                if taux is not None:
                    ot.releve_note(f"{PRIVE}/{regime}/cotisations_{cote}/{relatif}",
                                   f"{m[cle]} — {col_sal if cote == 'salarie' else m[cote]}")
            # La retraite complémentaire est affichée mais reste hors du total : elle est
            # facultative, et c'est le total obligatoire qui doit coïncider au centième
            # près avec celui du tableau de synthèse — d'où un cumul sur les valeurs
            # brutes, jamais sur les pourcentages arrondis de la colonne.
            if cle != "complementaire":
                cumul["salarie"] += sal or 0
                cumul["employeur"] += emp or 0
                vu["salarie"] |= sal is not None
                vu["employeur"] |= emp is not None
            lignes.append({
                m["branche"]: m[cle],
                col_sal: _taux(langue)(sal),
                m["employeur"]: _taux(langue)(emp),
                m["total"]: _taux(langue)((sal or 0) + (emp or 0)),
            })
        if not lignes:
            return pd.DataFrame()
        lignes.append({
            m["branche"]: m["total_obligatoire"],
            col_sal: _taux(langue)(cumul["salarie"] if vu["salarie"] else None),
            m["employeur"]: _taux(langue)(cumul["employeur"] if vu["employeur"] else None),
            m["total"]: _taux(langue)(cumul["salarie"] + cumul["employeur"]),
        })
        return pd.DataFrame(lignes)

    return tableau


def coin_par_regime(langue):
    """Le coin social de chaque régime : ce que le régime prélève au total."""
    import pandas as pd

    m = MOTS[langue]
    lignes = []
    for code, nom_fr, nom_ar, marque in REGIMES:
        totaux = {c: _somme_cote(code, c) for c in ("salarie", "employeur")}
        if totaux["salarie"] is None and totaux["employeur"] is None:
            continue
        nom = nom_fr if langue == "fr" else nom_ar
        # Un total parcourt toute l'arborescence d'un côté du régime : le lien mène au
        # nœud, dont la page publique aligne chaque branche avec ses dates et ses textes.
        for cote, total in totaux.items():
            if total is not None:
                libelle = m["assure"] if cote == "salarie" and totaux["employeur"] is None \
                    else m[cote]
                ot.releve_note(f"{PRIVE}/{code}/cotisations_{cote}", f"{nom} — {libelle}")
        if marque == "forfait":
            nom += NOTE_FORFAIT[langue]
        lignes.append({
            m["regime"]: nom,
            m["salarie"]: _taux(langue)(totaux["salarie"]),
            m["employeur"]: _taux(langue)(totaux["employeur"]),
            m["total"]: _taux(langue)((totaux["salarie"] or 0) + (totaux["employeur"] or 0)),
        })
    return pd.DataFrame(lignes)


def cnrps_retraite(langue):
    """La seule série longue du corpus : douze millésimes de 1959 à 2020."""
    m = MOTS[langue]
    return ot.tableau_taux_datee(
        [(f"{PUBLIC}/salarie_cnrps/cotisations_salarie/retraite.yaml",
          m["cnrps_retraite"], _taux(langue))],
        colonne_periode=m["effet"], colonne_texte=m["texte"], langue=langue)


# Clés de citation, par date d'effet : la colonne « Texte » des tableaux qui en ont.
CLES_CNRPS_EMPLOYEUR = {
    "1959-02-01": "loi59-18, art. 8",
    "1975-01-01": "loi74-101-lf1975, art. 39",
    "1995-07-01": "loi94-71",
    **dict.fromkeys((f"{a}-07-01" for a in range(2002, 2007)), "loi2001-123-lf2002, art. 85"),
    **dict.fromkeys((f"{a}-01-01" for a in range(2007, 2010)), "loi2007-43, art. 1"),
    "2011-07-01": "decretloi2011-48",
    "2019-06-01": "loi2019-37, art. 4",
}
CLES_PREVOYANCE = dict.fromkeys(
    (f"{a}-07-01" for a in range(2007, 2011)), "decret2007-1406, art. 13")
CLES_REDUCTION = {
    "1996-10-01": "loi97-4, art. 41 nouveau ; @decret97-1645",
    "2007-07-01": "decret2007-1406, art. 16",
}
CLES_CSS = {
    "2018-01-01": "lf-2018, art. 53",
    "2023-01-01": "lf-2023, art. 22",
}


def cnrps_employeur(langue):
    """La contribution de l'employeur public, pendant de la retenue de l'agent.

    Des niveaux datés, et non des mouvements : la colonne « Variation » donne le mouvement
    qu'opère chaque texte, en points, sans qu'on ait à l'écrire à la main.
    """
    m = MOTS[langue]
    return ot.tableau_taux_datee(
        [(f"{PUBLIC}/salarie_cnrps/cotisations_employeur/retraite.yaml",
          m["cnrps_employeur"], _taux(langue))],
        cles=CLES_CNRPS_EMPLOYEUR, colonne_periode=m["effet"], colonne_texte=m["texte"],
        langue=langue, colonne_variation=m["variation"])


def prevoyance_pensionnes(langue):
    """La cotisation de prévoyance sociale assise sur la pension, en quatre paliers."""
    m = MOTS[langue]
    return ot.tableau_taux_datee(
        [(f"{PUBLIC}/pensionne_cnrps/prevoyance_sociale.yaml", m["prevoyance"], _taux(langue))],
        cles=CLES_PREVOYANCE, colonne_periode=m["effet"], colonne_texte=m["texte"],
        langue=langue)


def reduction_conventionnelle(langue):
    """La réduction de deux points de la part patronale, de 1996 à 2007.

    Le paramètre est une valeur (`values`), non un barème : il se lit en série datée. Sa
    fin, au 1er juillet 2007, est une valeur nulle — la réduction n'existe plus, ce que la
    case dit en toutes lettres.
    """
    m = MOTS[langue]

    def points(v):
        if v is None:
            return "—"
        return m["aucune"] if v == 0 else ot.formate_points(-v)

    return ot.tableau_evolution_datee(
        [(f"{PRIVE}/rsna/reduction_conventionnelle.yaml", m["reduction"], points)],
        cles=CLES_REDUCTION, langue=langue,
        colonne_periode=m["effet"], colonne_texte=m["texte"])


def css_salarie(langue):
    """Le taux salarial de la contribution sociale de solidarité, depuis 2018.

    Un texte qui reconduit le taux n'est pas une étape de son évolution : la loi de
    finances pour 2025, qui maintient 0,5 %, n'a pas de ligne (`sans_maintien`).
    """
    m = MOTS[langue]
    return ot.tableau_taux_datee(
        [("parameters/prelevements_sociaux/contribution_sociale_solidarite/salarie.yaml",
          m["css_salarie"], _taux(langue))],
        cles=CLES_CSS, colonne_periode=m["effet"], colonne_texte=m["texte"],
        langue=langue, sans_maintien=True)


def cnrps_maladie(langue):
    """La montée en charge de la cotisation d'assurance maladie des agents de la CNRPS.

    Elle commence au 1er juillet 2007 : la part patronale antérieure (1 %) n'est rattachée à
    aucun texte, et ne se publie pas (`depuis`). La première ligne porte la part de l'agent
    alors en vigueur, fixée depuis 1973.
    """
    m = MOTS[langue]
    base = f"{PUBLIC}/salarie_cnrps"
    return ot.tableau_taux_datee(
        [(f"{base}/cotisations_employeur/maladie.yaml", m["maladie_employeur"], _taux(langue)),
         (f"{base}/cotisations_salarie/maladie.yaml", m["maladie_agent"], _taux(langue))],
        cles=dict.fromkeys(("2007-07-01", "2008-07-01", "2009-07-01"), "decret2007-1406, art. 4"),
        colonne_periode=m["effet"], colonne_texte=m["texte"], langue=langue,
        depuis="2007-07-01", colonne_total=m["total"])


def perte_emploi(langue):
    """La cotisation au fonds d'assurance contre la perte d'emploi, depuis 2025."""
    m = MOTS[langue]
    base = f"{PRIVE}/rsna"
    return ot.tableau_taux_datee(
        [(f"{base}/cotisations_employeur/perte_d_emploi.yaml", m["perte_employeur"], _taux(langue)),
         (f"{base}/cotisations_salarie/perte_d_emploi.yaml", m["perte_salarie"], _taux(langue))],
        cles={"2025-01-01": "lf-2025, art. 17"},
        colonne_periode=m["effet"], colonne_texte=m["texte"], langue=langue,
        colonne_total=m["total"])


AUTRES = "parameters/prelevements_sociaux/autres"
CLES_TFP_FOPROLOS = {
    "1967-01-01": "decret66-527, art. 1-2",
    "1977-08-01": "loi77-54, art. 2 et 10",
    "1989-01-01": "loi-88-145-lf-1989, art. 29-30 et 35",
}


def tfp_foprolos(langue):
    """Les deux prélèvements patronaux sur les salaires hors cotisations, depuis 1967.

    Le taux de la taxe de formation professionnelle antérieur à 1967 (décret du 16 janvier
    1957) n'est pas connu : la série commence au taux de 2 % du décret n° 66-527. Avant le
    1er août 1977, la colonne du FOPROLOS est vide.
    """
    m = MOTS[langue]
    return ot.tableau_evolution_datee(
        [(f"{AUTRES}/tfp/taux_industries_manufacturieres.yaml", m["tfp_manuf"], _taux(langue)),
         (f"{AUTRES}/tfp/taux_autres_secteurs.yaml", m["tfp_autres"], _taux(langue)),
         (f"{AUTRES}/foprolos/taux.yaml", m["foprolos"], _taux(langue))],
        cles=CLES_TFP_FOPROLOS, langue=langue,
        colonne_periode=m["effet"], colonne_texte=m["texte"])


TABLEAUX = {
    "tfp_foprolos.md": tfp_foprolos,
    "coin_par_regime.md": coin_par_regime,
    "cnrps_maladie.md": cnrps_maladie,
    "perte_emploi.md": perte_emploi,
    "cnrps_retraite.md": cnrps_retraite,
    "cnrps_employeur.md": cnrps_employeur,
    "prevoyance_pensionnes.md": prevoyance_pensionnes,
    "reduction_conventionnelle.md": reduction_conventionnelle,
    "css_salarie.md": css_salarie,
    "atmp_1995.md": atmp_1995,
    "atmp_1999.md": atmp_1999,
}

# Le régime des étudiants n'a pas de tableau : sa cotisation est un forfait, pas un taux.
for _code, *_ in REGIMES:
    TABLEAUX[f"branches_{_code}.md"] = branches(_code)

# Livres où chaque tableau est écrit, quand ce n'est pas celui des cotisations seul. La
# fabrique reste unique : le tableau est émis dans chaque livre (`ot.ecrire_tableau`).
LIVRE = "cotisations_sociales"
LIVRES = {
    "cnrps_retraite.md": (LIVRE, "remunerations_publiques"),
    "css_salarie.md": ("remunerations_publiques",),
    # L'assurance maladie et la perte d'emploi sont des prestations au livre « Prestations
    # sociales » : il cite les taux qui les financent.
    "cnrps_maladie.md": (LIVRE, "prestations_sociales"),
    "prevoyance_pensionnes.md": (LIVRE, "prestations_sociales"),
    "perte_emploi.md": (LIVRE, "prestations_sociales"),
}


# ------------------------------------------------ série de la figure des deux échelles AT/MP

# CORRESPONDANCE DES CLASSES DE 1995 AUX SECTEURS DE 1999 — un choix éditorial, non un texte :
# aucun texte ne la donne. N'y figurent que les cas évidents — libellé identique, ou classe
# éclatée en sous-secteurs ou en secteurs voisins qui en reprennent les termes. Une classe
# sans équivalent évident a une liste vide ; les secteurs de 1999 que rien ne rejoint sont
# regroupés sur une dernière ligne. Clés : feuilles ou nœuds de premier niveau
# d'`atmp_1995/apres_transfert` ; valeurs : de premier niveau d'`atmp`.
CORRESPONDANCE_ATMP = {
    "services_de_bureaux": ["services_de_bureaux"],
    "autres_services": ["autres_services"],
    "commerce": ["commerce"],
    "artisans": [],
    "agriculture_et_peche": ["agriculture_et_peche"],
    "industries_agro_alimentaires": ["industries_agro_alimentaires"],
    "industrie_du_froid": [],
    "papier_et_arts_graphiques": ["industrie_du_papier_et_des_arts_graphiques"],
    "mecaniques_fonderies_electriques": [],
    "textile_cuir_chaussures": ["textile_cuir_chaussures"],
    "meuble": [],
    "materiaux_construction_ceramique_verrerie": [
        "industries_des_materiaux_de_construction", "industrie_de_verrerie", "industrie_de_la_ceramique"],
    "bois_liege": ["industries_du_bois", "industrie_du_liege"],
    "autres_industries_manufacturieres": ["autres_industries_manufacturieres"],
    "industries_chimiques": ["industries_chimiques"],
    "batiment_et_travaux_publics": ["batiment_et_travaux_publics"],
    "transport_et_manutention": ["transport_et_manutention"],
    "industries_extractives": ["industries_extractives"],
}
SANS_1995 = ("Secteurs de 1999 sans classe en 1995", "قطاعات 1999 دون صنف مقابل في 1995")
SERIE_ATMP = "atmp-echelles-1995-1999"
LIBELLES_SERIE_ATMP = {
    "fr": {"1995": "Échelle des taux AT/MP de 1995, après transfert du point",
           "1999": "Échelle des taux AT/MP de 1999, après transfert du point"},
    "ar": {"1995": "جدول نسب الاشتراكات بعنوان حوادث الشغل والأمراض المهنية لسنة 1995، بعد تحويل النقطة",
           "1999": "جدول نسب الاشتراكات بعنوان حوادث الشغل والأمراض المهنية لسنة 1999، بعد تحويل النقطة"},
}


def _feuilles(noeud: str, tete: str) -> list[str]:
    """Feuilles (chemins relatifs à `noeud`) sous l'enfant de premier niveau `tete`."""
    sous = [f"{tete}/{r}" for r, _p, est_noeud in ot.arborescence(f"{noeud}/{tete}") if not est_noeud]
    return sous or [tete]


def _taux_a(chemin: str, date: str) -> float | None:
    retenu = None
    for d, v, _t, _h in ot.taux_datee(chemin):
        if d <= date:
            retenu = v
    return retenu


def serie_atmp() -> int:
    """Série longue des deux échelles AT/MP après transfert, alignées par classe de 1995.

    Une ligne par taux : (ligne, clé de la classe de 1995, libellés, échelle, point, taux).
    La figure en tire, pour chaque classe de 1995, son taux ou sa fourchette en 1995 et
    celle des secteurs de 1999 qui lui correspondent (`CORRESPONDANCE_ATMP`).
    """
    apres_1995 = f"{ATMP_1995}/apres_transfert"
    tetes_1995 = [r for r, p, _n in ot.arborescence(apres_1995) if p == 0]
    tetes_1999 = [r for r, p, _n in ot.arborescence(ATMP) if p == 0]
    if set(tetes_1995) != set(CORRESPONDANCE_ATMP):
        print(f"✗ {SERIE_ATMP} : classes de 1995 désaccordées : "
              f"{sorted(set(tetes_1995) ^ set(CORRESPONDANCE_ATMP))}")
        return 1
    inconnues = {s for v in CORRESPONDANCE_ATMP.values() for s in v} - set(tetes_1999)
    if inconnues:
        print(f"✗ {SERIE_ATMP} : secteurs de 1999 inconnus : {sorted(inconnues)}")
        return 1
    points_1999 = _points(ATMP)
    ot.releve_note(apres_1995, "1995")
    ot.releve_note(ATMP, "1999")
    lignes = []
    for rang, tete in enumerate(tetes_1995):
        numero, fr, ar = SECTEURS_ATMP_1995[tete]
        for feuille in _feuilles(apres_1995, tete):
            lignes.append((rang, tete, numero, fr, ar, "1995", *SECTEURS_ATMP_1995[feuille],
                           _taux_a(f"{apres_1995}/{feuille}.yaml", "1995-01-01")))
        for secteur in CORRESPONDANCE_ATMP[tete]:
            for feuille in _feuilles(ATMP, secteur):
                lignes.append((rang, tete, numero, fr, ar, "1999", points_1999[feuille],
                               *SECTEURS_ATMP_1999[points_1999[feuille]],
                               _taux_a(f"{ATMP}/{feuille}.yaml", "1999-04-01")))
    rejoints = {s for v in CORRESPONDANCE_ATMP.values() for s in v}
    rang = len(tetes_1995)
    for secteur in (s for s in tetes_1999 if s not in rejoints):
        for feuille in _feuilles(ATMP, secteur):
            lignes.append((rang, "_sans_1995", "", *SANS_1995, "1999", points_1999[feuille],
                           *SECTEURS_ATMP_1999[points_1999[feuille]],
                           _taux_a(f"{ATMP}/{feuille}.yaml", "1999-04-01")))
    if any(l[-1] is None for l in lignes):
        print(f"✗ {SERIE_ATMP} : taux manquant, snapshot conservé.")
        return 1
    import pandas as pd

    cache = RACINE / "_seriescache"
    pd.DataFrame(lignes, columns=["ligne", "classe_1995", "numero_1995", "libelle_fr", "libelle_ar",
                                  "echelle", "point", "point_fr", "point_ar", "taux"]).to_csv(cache / f"{SERIE_ATMP}.csv", index=False)
    print(f"✓ série {SERIE_ATMP} : {len(lignes)} taux")
    return 0


def serie_atmp_avec_liens() -> int:
    """`serie_atmp` sous relevé, puis ses liens « Base législative » dans les deux langues."""
    code, releve = ot.avec_liens(serie_atmp)
    if code:
        return code
    cache = RACINE / "_seriescache"
    for langue in LANGUES:
        ot.ecrire_fichier_liens(cache / f"{SERIE_ATMP}.liens.{langue}.yml",
                                [(c, LIBELLES_SERIE_ATMP[langue][cle]) for c, cle in releve], langue)
    return 0


def main() -> int:
    if not ot.openfisca_utilisable():
        print(f"openfisca-tunisia indisponible ou trop ancien "
              f"(version {ot.version_openfisca()}, minimum {ot.VERSION_MINIMALE}).")
        return 1
    for langue in LANGUES:
        for nom, fabrique in TABLEAUX.items():
            df, liens = ot.avec_liens(lambda: fabrique(langue))
            if df is None or df.empty:
                print(f"✗ {langue}/{nom} : paramètre introuvable ou vide.")
                return 1
            erreur = ot.ecrire_dans_livres(RACINE, langue, LIVRES.get(nom, (LIVRE,)), nom,
                                           df, liens)
            if erreur:
                print(erreur)
                return 1
        print(f"✓ {langue} : {len(TABLEAUX)} tableaux")
    return serie_atmp_avec_liens()


if __name__ == "__main__":
    raise SystemExit(main())

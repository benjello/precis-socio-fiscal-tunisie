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


# ------------------------------------------------ salaires forfaitaires et modulation AT/MP

FORFAITS = "parameters/prelevements_sociaux/atmp_forfaits"
MODULATION = "parameters/prelevements_sociaux/atmp_modulation"
SMIG_48 = {"fr": "SMIG, régime 48 heures", "ar": "الأجر الأدنى المضمون لمختلف المهن، نظام 48 ساعة"}
SMAG = {"fr": "SMAG", "ar": "الأجر الأدنى الفلاحي المضمون"}


def _nombre(v, _langue=None):
    """2400 -> « 2 400 » : les quantités entières, avec l'espace des milliers."""
    return "—" if v is None else f"{int(v):,}".replace(",", " ")


# TABLEAU DES JOURNÉES DE TRAVAIL de la cotisation forfaitaire agricole (décret n° 95-538,
# article 4 ; décret n° 99-1010). Ordre : celui du tableau du texte. Les libellés français
# sont ceux de l'édition française ; les libellés arabes sont des TRADUCTIONS éditoriales
# (le tableau arabe du JORT n'est pas transcrit ici, hors divergences relevées à l'image,
# qui ont leur colonne). feuille -> (fr, ar, unité, variante arabe fr, variante arabe ar).
UNITES_JOURNEES = {
    "hectare": ("jours par hectare", "يوم لكل هكتار"),
    "tete": ("jours par tête", "يوم لكل رأس"),
    "volailles": ("jours pour 1 000 volailles", "يوم لكل 1000 دجاجة"),
    "lapins": ("jours pour 1 000 lapins", "يوم لكل 1000 أرنب"),
    "barque": ("jours par barque", "يوم لكل قارب"),
    "unite": ("jours par unité", "يوم لكل وحدة"),
}
JOURNEES = [
    ("cereales_sec", "Céréales en sec", "الحبوب (بعلي)", "hectare", "", ""),
    ("cereales_irrigue", "Céréales en irrigué", "الحبوب (مروي)", "hectare", "", ""),
    ("legumineuses_grandes_cultures_sec", "Légumineuses et autres grandes cultures en sec",
     "القطاني والزراعات الكبرى الأخرى (بعلي)", "hectare", "", ""),
    ("cultures_industrielles", "Cultures industrielles (betterave à sucre et coton)",
     "الزراعات الصناعية (اللفت السكري والقطن)", "hectare", "", ""),
    ("maraicheres_solanacees", "Cultures maraîchères de plein champ : solanacées (tomates)",
     "زراعات الخضر في الحقل: الباذنجانيات (الطماطم)", "hectare",
     "les tomates seules", "الطماطم فقط"),
    ("maraicheres_pommes_de_terre", "Cultures maraîchères de plein champ : pommes de terre et autres",
     "زراعات الخضر في الحقل: البطاطا وغيرها", "hectare", "", ""),
    ("horticulture_plein_champ", "Horticulture de plein champ", "البستنة في الحقل", "hectare",
     "floriculture de plein champ", "زراعة الأزهار في الحقل"),
    ("oliviers_amandiers", "Oliviers et amandiers", "الزياتين واللوز", "hectare", "", ""),
    ("vigne_cuve", "Vigne de cuve (en sec)", "كروم النبيذ (بعلي)", "hectare", "", ""),
    ("vigne_table", "Vigne de table", "كروم عنب المائدة", "hectare", "", ""),
    ("agrumes", "Agrumes", "القوارص", "hectare", "", ""),
    ("arboriculture_sec", "Arboriculture en sec", "الأشجار المثمرة (بعلي)", "hectare",
     "arbres fruitiers", "الأشجار المثمرة"),
    ("arboriculture_irrigue", "Arboriculture en irrigué", "الأشجار المثمرة (مروي)", "hectare", "", ""),
    ("palmier_dattier", "Palmier dattier", "النخيل", "hectare", "", ""),
    ("cultures_sous_serres", "Cultures sous serres", "الزراعات داخل البيوت المحمية", "hectare", "", ""),
    ("bananes_sous_serres", "Culture des bananes sous serres", "زراعة الموز داخل البيوت المحمية",
     "hectare", "", ""),
    ("elevage_bovins", "Élevage : bovins (1995) ; bovins, équins et camélidés (1999)",
     "تربية الماشية: الأبقار (1995)؛ الأبقار والخيول والإبل (1999)", "tete", "", ""),
    ("elevage_ovins", "Élevage : ovins", "تربية الماشية: الأغنام", "tete",
     "ovins et caprins", "الأغنام والماعز"),
    ("aviculture", "Aviculture", "تربية الدواجن", "volailles", "", ""),
    ("cuniculture", "Cuniculture", "تربية الأرانب", "lapins", "", ""),
    ("peche_cotiere", "Pêche côtière", "الصيد الساحلي", "barque", "", ""),
    ("peche_chalut", "Pêche au chalut", "الصيد بشباك الجر", "unite",
     "pêche au feu", "الصيد بالضوء"),
]
MOTS_ATMP = {
    "fr": {"type": "Type de culture ou d'activité", "unite": "Unité",
           "variante": "Édition arabe, quand elle diffère"},
    "ar": {"type": "نوع الزراعة أو النشاط", "unite": "الوحدة",
           "variante": "الطبعة العربية عند الاختلاف"},
}


def _valeur_a(chemin: str, date: str) -> float | None:
    """Valeur d'un paramètre scalaire (`values`) en vigueur à `date`, ou None."""
    point = ot.en_vigueur(ot.serie_datee(chemin), date)
    return None if point is None else point[1]


def atmp_journees(langue):
    """Journées de travail de la cotisation forfaitaire agricole, 1995 et 1999."""
    import pandas as pd

    noeud = f"{FORFAITS}/agriculture_peche/journees"
    feuilles = {r for r, _p, est_noeud in ot.arborescence(noeud) if not est_noeud}
    if feuilles != {f for f, *_ in JOURNEES}:
        raise ValueError(f"journées AT/MP désaccordées : {sorted(feuilles ^ {f for f, *_ in JOURNEES})}")
    m = MOTS_ATMP[langue]
    rang = 1 if langue == "fr" else 2
    lignes = []
    for feuille, fr, ar, unite, var_fr, var_ar in JOURNEES:
        chemin = f"{noeud}/{feuille}.yaml"
        ot.releve_note(chemin, fr if langue == "fr" else ar)
        lignes.append({
            m["type"]: fr if langue == "fr" else ar,
            m["unite"]: UNITES_JOURNEES[unite][0 if langue == "fr" else 1],
            ot.formate_date("1995-01-01", langue): _nombre(_valeur_a(chemin, "1995-01-01")),
            ot.formate_date("1999-04-01", langue): _nombre(_valeur_a(chemin, "1999-04-01")),
            m["variante"]: (var_fr if langue == "fr" else var_ar) or "",
        })
    return pd.DataFrame(lignes)


def atmp_modulation(langue):
    """Majoration et réduction de la cotisation AT/MP : quotités du décret n° 95-538."""
    g, L = ot.gabarit, ot.Lecture
    d95 = "1995-01-01"
    sup = L(f"{MODULATION}/cotisation_supplementaire.yaml", d95, "taux",
            {"fr": "Cotisation supplémentaire", "ar": "الاشتراك الإضافي"})
    maxi = L(f"{MODULATION}/cotisation_supplementaire_maximum.yaml", d95, "taux",
             {"fr": "Cotisation supplémentaire maximale", "ar": "الحد الأقصى للاشتراك الإضافي"})
    red = L(f"{MODULATION}/reduction_maximum.yaml", d95, "taux",
            {"fr": "Réduction maximale", "ar": "الحد الأقصى للتخفيض"})
    entetes = {
        "fr": ["Mesure", "Quotité, en proportion des cotisations principales", "Condition",
               "Prise d'effet et durée", "Article"],
        "ar": ["الإجراء", "المقدار، نسبةً إلى الاشتراكات الأصلية", "الشرط",
               "بداية السريان والمدة", "الفصل"],
    }[langue]
    lignes = [
        [{"fr": "Cotisation supplémentaire", "ar": "الاشتراك الإضافي"},
         g("{s}", s=sup),
         {"fr": "manquement non corrigé dans le délai notifié par la caisse",
          "ar": "إخلال لم يقع تداركه في الأجل الذي حدّده الصندوق"},
         {"fr": "à compter du trimestre qui suit l'expiration de la mise en demeure, "
                "jusqu'à sa suppression",
          "ar": "ابتداءً من الثلاثية الموالية لانقضاء أجل التنبيه، إلى حين إلغائه"},
         {"fr": "16, 17, 19 et 20", "ar": "16 ا17 ا19 ا20"}],
        [{"fr": "Cotisation supplémentaire doublée", "ar": "الاشتراك الإضافي مضاعَفًا"},
         g({"fr": "{s}, doublés", "ar": "{s}، تُضاعَف"}, s=sup),
         {"fr": "mesures non exécutées dans les six mois qui suivent l'expiration du délai, "
                "ou récidive dans les trois ans pour un risque de même nature",
          "ar": "عدم تنفيذ التدابير في الأشهر الستة الموالية لانقضاء الأجل، أو العود خلال ثلاث "
                "سنوات لخطر من نفس الطبيعة"},
         "—", "17"],
        [g({"fr": "Cotisation supplémentaire portée à {m}", "ar": "الاشتراك الإضافي مرفوعًا إلى {m}"},
           m=maxi),
         g("{m}", m=maxi),
         {"fr": "refus ou négligence persistant six mois après l'application de la majoration "
                "de l'article 17",
          "ar": "استمرار الرفض أو الإهمال ستة أشهر بعد تطبيق الترفيع المنصوص عليه بالفصل 17"},
         "—", "18"],
        [{"fr": "Réduction", "ar": "التخفيض"},
         g({"fr": "{r} au plus", "ar": "{r} كحدّ أقصى"}, r=red),
         {"fr": "quatre conditions cumulatives, dont une baisse sensible des accidents du "
                "travail ou des maladies professionnelles",
          "ar": "أربعة شروط مجتمعة، منها انخفاض ملموس في حوادث الشغل أو الأمراض المهنية"},
         {"fr": "dès le trimestre qui suit la décision, pour un an renouvelable ; suspension "
                "ou suppression à tout moment",
          "ar": "ابتداءً من الثلاثية الموالية للقرار، لمدة سنة قابلة للتجديد؛ ويمكن تعليقه أو "
                "إلغاؤه في أي وقت"},
         {"fr": "22 à 26", "ar": "22 إلى 26"}],
    ]
    return ot.tableau_gabarit(entetes, lignes, langue)


def atmp_forfaits(langue):
    """Salaires forfaitaires AT/MP par catégorie : règles saisies, valeurs engendrées."""
    g, L = ot.gabarit, ot.Lecture
    d95, d99, d00 = "1995-01-01", "1999-04-01", "2000-07-01"
    agri = f"{FORFAITS}/agriculture_peche"

    def lu(chemin, date, formateur, fr, ar):
        return L(chemin, date, formateur, {"fr": fr, "ar": ar})

    t95 = lu(f"{agri}/taux.yaml", d95, "taux",
             "Taux de la cotisation forfaitaire agricole", "نسبة الاشتراك الجزافي الفلاحي")
    t99 = lu(f"{agri}/taux.yaml", d99, "taux",
             "Taux de la cotisation forfaitaire agricole", "نسبة الاشتراك الجزافي الفلاحي")
    coef_agri = lu(f"{agri}/coefficient_cotisation.yaml", d95, "coefficient",
                   "Coefficient de la cotisation forfaitaire agricole", "معامل الاشتراك الجزافي الفلاحي")
    plafond = lu(f"{agri}/plafond_salaire_smag.yaml", d95, "coefficient",
                 "Plafond de salaire du forfait agricole (en SMAG)",
                 "سقف الأجر للجزاف الفلاحي (بالأجر الأدنى الفلاحي)")
    base_agri = lu(f"{agri}/base_prestations_jours.yaml", d95, "entier",
                   "Base des réparations du forfait agricole (jours)", "قاعدة جبر الأضرار الفلاحية (أيام)")
    c_ord = lu(f"{agri}/coefficient_prestations_ordinaire.yaml", d95, "coefficient",
               "Coefficient des prestations — travailleurs ordinaires", "معامل الخدمات — العملة العاديون")
    c_spe = lu(f"{agri}/coefficient_prestations_specialise.yaml", d95, "coefficient",
               "Coefficient des prestations — travailleurs spécialisés", "معامل الخدمات — العملة المختصون")
    c_qua = lu(f"{agri}/coefficient_prestations_qualifie.yaml", d95, "coefficient",
               "Coefficient des prestations — travailleurs qualifiés", "معامل الخدمات — العملة المؤهلون")
    ch_coef = lu(f"{FORFAITS}/chauffeurs_taxi_louage/coefficient.yaml", d95, "coefficient",
                 "Coefficient — chauffeurs de louage et de taxis", "المعامل — سائقو اللواج والتاكسي")
    ch_h = lu(f"{FORFAITS}/chauffeurs_taxi_louage/nombre_heures.yaml", d95, _nombre,
              "Heures par an — chauffeurs de louage et de taxis", "ساعات السنة — سائقو اللواج والتاكسي")
    ch_h00 = lu(f"{FORFAITS}/chauffeurs_taxi_louage/nombre_heures.yaml", d00, _nombre,
                "Heures par an — chauffeurs de louage et de taxis", "ساعات السنة — سائقو اللواج والتاكسي")
    ma_coef = lu(f"{FORFAITS}/masseurs_bains_maures/coefficient.yaml", d95, "coefficient",
                 "Coefficient — masseurs des bains maures", "المعامل — المدلّكون بالحمّامات")
    ma_h = lu(f"{FORFAITS}/masseurs_bains_maures/nombre_heures.yaml", d95, _nombre,
              "Heures par an — masseurs des bains maures", "ساعات السنة — المدلّكون بالحمّامات")
    em_j = lu(f"{FORFAITS}/employes_maison/base_jours.yaml", d95, "entier",
              "Base annuelle (jours) — employés de maison", "القاعدة السنوية (أيام) — عملة المنازل")
    em_aides = lu(f"{FORFAITS}/employes_maison/taux_aides_menage.yaml", d95, "taux",
                  "Taux — aides de ménage", "النسبة — المعينون المنزليون")
    em_autres = lu(f"{FORFAITS}/employes_maison/taux_autres.yaml", d95, "taux",
                   "Taux — autres employés de maison", "النسبة — بقية عملة المنازل")
    em_cond = lu(f"{FORFAITS}/employes_maison/taux_conducteurs.yaml", d95, "taux",
                 "Taux — conducteurs de voitures", "النسبة — سائقو السيارات")
    em_ccond = lu(f"{FORFAITS}/employes_maison/coefficient_conducteurs.yaml", d95, "coefficient",
                  "Coefficient — conducteurs de voitures", "المعامل — سائقو السيارات")
    tp_h = lu(f"{FORFAITS}/temporaires_particuliers/nombre_heures_mensuel.yaml", d95, _nombre,
              "Heures par mois — travailleurs temporaires des particuliers",
              "ساعات الشهر — العملة الوقتيون لدى الخواص")
    tp_ord = lu(f"{FORFAITS}/temporaires_particuliers/coefficient_ordinaire.yaml", d95, "coefficient",
                "Coefficient — travailleurs ordinaires", "المعامل — العملة العاديون")
    tp_qua = lu(f"{FORFAITS}/temporaires_particuliers/coefficient_qualifie.yaml", d95, "coefficient",
                "Coefficient — travailleurs qualifiés", "المعامل — العملة المؤهلون")

    smig48, smag = SMIG_48[langue], SMAG[langue]
    meme_base = {"fr": "même base", "ar": "نفس القاعدة"}
    non_fixe = {"fr": "non fixé par l'article", "ar": "لم يحدّده الفصل"}
    entetes = {
        "fr": ["Catégorie", "Base de la cotisation", "Coefficient", "Taux",
               "Base des réparations", "État d'origine (1^er^ janvier 1995)", "Modifications datées"],
        "ar": ["الصنف", "قاعدة الاشتراك", "المعامل", "النسبة",
               "قاعدة جبر الأضرار", "الوضع الأصلي (1 جانفي 1995)", "التعديلات المؤرّخة"],
    }[langue]
    lignes = [
        # Article 4 : le forfait agricole.
        [g({"fr": "Secteur agricole hors loi n° 89-73 et pêcheurs payés à la part sur bateaux "
                  "de moins de trente tonneaux de jauge, pour les travailleurs payés au plus "
                  "{p} fois le " + smag + " [@decret95-538, art. 4]",
            "ar": "القطاع الفلاحي غير الخاضع للقانون عدد 73 لسنة 1989 والبحّارة المؤجّرون بالحصّة "
                  "على مراكب تقلّ حمولتها عن ثلاثين طنًّا، بالنسبة إلى العملة الذين لا تتجاوز "
                  "أجورهم {p} مرات " + smag + " [@decret95-538, art. 4]"}, p=plafond),
         {"fr": smag + " journalier × nombre de journées de travail fixé par type de culture "
                "ou d'activité (@tbl-atmp-journees)",
          "ar": smag + " اليومي × عدد أيام العمل المحدّد حسب نوع الزراعة أو النشاط "
                "(@tbl-atmp-journees)"},
         g("{c}", c=coef_agri),
         g({"fr": "propre à l'article : {t95}, puis {t99}", "ar": "خاصّة بالفصل: {t95} ثم {t99}"},
           t95=t95, t99=t99),
         g({"fr": "salaire forfaitaire annuel distinct : " + smag + " × {j} jours × {o} "
                  "(travailleurs agricoles ordinaires, pêcheurs), {s} (travailleurs et pêcheurs "
                  "spécialisés, ramendeurs, mécaniciens, seconds des patrons de pêche) ou {q} "
                  "(travailleurs agricoles qualifiés, patrons de pêche)",
            "ar": "أجر جزافي سنوي مستقل: " + smag + " × {j} يومًا × {o} (العملة الفلاحيون "
                  "العاديون والبحّارة)، أو {s} (العملة والبحّارة المختصّون ومصلحو الشباك "
                  "والميكانيكيون ونوّاب الرياس)، أو {q} (العملة الفلاحيون المؤهّلون والرياس)"},
           j=base_agri, o=c_ord, s=c_spe, q=c_qua),
         g({"fr": "taux de {t95} ; tableau des journées de 1995", "ar": "نسبة {t95}؛ جدول أيام 1995"},
           t95=t95),
         g({"fr": "**1^er^ avril 1999** : taux de {t95} → {t99} ; tableau des journées "
                  "complété de deux lignes et élargi sur une troisième. Champ, seuil, "
                  "coefficient, option et base des réparations inchangés "
                  "[@decret99-1010, art. 1^er^ et 2]",
            "ar": "**1 أفريل 1999**: النسبة من {t95} إلى {t99}؛ أُكمل جدول الأيام بسطرين "
                  "ووُسّع سطر ثالث. بقي المجال والسقف والمعامل والخيار وقاعدة جبر الأضرار "
                  "دون تغيير [@decret99-1010, art. 1^er^ et 2]"}, t95=t95, t99=t99)],
        # Article 4 : l'option pour les salaires effectifs.
        [{"fr": "Mêmes employeurs, sur option irrévocable [@decret95-538, art. 4]",
          "ar": "نفس المؤجّرين، بخيار لا رجعة فيه [@decret95-538, art. 4]"},
         {"fr": "salaires effectifs", "ar": "الأجور الفعلية"},
         "—",
         {"fr": "échelle des articles 1^er^ et 2", "ar": "سلّم الفصلين الأول والثاني"},
         {"fr": "droit commun [@loi94-28, art. 17]", "ar": "القواعد العامة [@loi94-28, art. 17]"},
         {"fr": "échelle de 1995 (@tbl-atmp-1995)", "ar": "سلّم 1995 (@tbl-atmp-1995)"},
         {"fr": "**1^er^ avril 1999** : échelle refondue (@tbl-atmp-1999)",
          "ar": "**1 أفريل 1999**: سلّم معاد الصياغة (@tbl-atmp-1999)"}],
        # Article 5 : chauffeurs de louage et de taxis.
        [{"fr": "Chauffeurs de louage et de taxis [@decret95-538, art. 5]",
          "ar": "سائقو سيارات الأجرة (التاكسي واللواج) [@decret95-538, art. 5]"},
         g({"fr": smig48 + ", × {h} heures par an", "ar": smig48 + "، × {h} ساعة في السنة"},
           h=ch_h),
         g({"fr": "{c}, puis aucun", "ar": "{c} ثم لا معامل"}, c=ch_coef),
         non_fixe, meme_base,
         g({"fr": "coefficient {c}", "ar": "المعامل {c}"}, c=ch_coef),
         g({"fr": "**1^er^ juillet 2000** : " + smig48 + ", × {h} heures par an, sans "
                  "coefficient ; transport rural ajouté. L'article 5 n'est pas nommé : portée "
                  "déduite de l'abrogation des « dispositions antérieures contraires » "
                  "[@decret2000-1439, art. 1^er^ à 4]",
            "ar": "**1 جويلية 2000**: " + smig48 + "، × {h} ساعة في السنة، دون معامل؛ "
                  "وأُضيف النقل الريفي. لم يُسمَّ الفصل 5: المدى مستخلص من إلغاء "
                  "«الأحكام السابقة المخالفة» [@decret2000-1439, art. 1^er^ à 4]"}, h=ch_h00)],
        # Article 5 : masseurs des bains maures.
        [{"fr": "« Masseurs » des bains maures [@decret95-538, art. 5]",
          "ar": "«المدلّكون» بالحمّامات [@decret95-538, art. 5]"},
         g({"fr": smig48 + ", × {h} heures par an", "ar": smig48 + "، × {h} ساعة في السنة"},
           h=ma_h),
         g("{c}", c=ma_coef), non_fixe, meme_base,
         g({"fr": "coefficient {c}", "ar": "المعامل {c}"}, c=ma_coef), "—"],
        # Article 6 : employés de maison, trois taux.
        [{"fr": "Aides de ménage [@decret95-538, art. 6]",
          "ar": "المعينون المنزليون [@decret95-538, art. 6]"},
         g({"fr": smag + " × {j} jours par an", "ar": smag + " × {j} يومًا في السنة"}, j=em_j),
         "—",
         g({"fr": "propre à l'article : {t}", "ar": "خاصّة بالفصل: {t}"}, t=em_aides),
         meme_base,
         g({"fr": "taux de {t}", "ar": "نسبة {t}"}, t=em_aides), "—"],
        [{"fr": "Autres employés de maison, sauf les chauffeurs [@decret95-538, art. 6]",
          "ar": "بقية عملة المنازل، باستثناء السائقين [@decret95-538, art. 6]"},
         g({"fr": smag + " × {j} jours par an", "ar": smag + " × {j} يومًا في السنة"}, j=em_j),
         "—",
         g({"fr": "propre à l'article : {t}", "ar": "خاصّة بالفصل: {t}"}, t=em_autres),
         meme_base,
         g({"fr": "taux de {t}", "ar": "نسبة {t}"}, t=em_autres), "—"],
        [{"fr": "Conducteurs de voitures, employés de maison [@decret95-538, art. 6]",
          "ar": "سائقو السيارات من عملة المنازل [@decret95-538, art. 6]"},
         g({"fr": smag + " × {j} jours par an", "ar": smag + " × {j} يومًا في السنة"}, j=em_j),
         g("{c}", c=em_ccond),
         g({"fr": "propre à l'article : {t}", "ar": "خاصّة بالفصل: {t}"}, t=em_cond),
         meme_base,
         g({"fr": "taux de {t} ; coefficient {c}", "ar": "نسبة {t}؛ المعامل {c}"},
           t=em_cond, c=em_ccond), "—"],
        # Article 7 : travailleurs temporaires des particuliers.
        [{"fr": "Travailleurs employés temporairement auprès des individus "
                "[@decret95-538, art. 7]",
          "ar": "العملة المشغّلون وقتيًّا لدى الخواص [@decret95-538, art. 7]"},
         g({"fr": "SMIG, régime horaire non précisé, × {h} heures par mois ; tout mois "
                  "commencé compte pour un mois",
            "ar": "الأجر الأدنى المضمون لمختلف المهن، دون تحديد نظام الساعات، × {h} ساعة "
                  "في الشهر؛ وكل شهر بُدئ يُحسب شهرًا كاملاً"}, h=tp_h),
         g({"fr": "{o} (travailleurs ordinaires) ou {q} (travailleurs qualifiés)",
            "ar": "{o} (العملة العاديون) أو {q} (العملة المؤهّلون)"}, o=tp_ord, q=tp_qua),
         {"fr": "celui de la branche d'activité, que l'article ne désigne pas",
          "ar": "نسبة فرع النشاط، ولا يعيّنه الفصل"},
         meme_base,
         g({"fr": "coefficients {o} et {q}", "ar": "المعاملان {o} و{q}"}, o=tp_ord, q=tp_qua),
         "—"],
    ]
    return ot.tableau_gabarit(entetes, lignes, langue)


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
CLES_PREVOYANCE = {
    "1973-04-01": "decret73-91, art. 15",
    **dict.fromkeys((f"{a}-07-01" for a in range(2007, 2011)), "decret2007-1406, art. 13"),
}
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
    """La cotisation de prévoyance sociale assise sur la pension : 2 % en 1973 (décret
    n° 73-91, article 15), puis les quatre paliers du décret n° 2007-1406."""
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
    """La cotisation de prévoyance sociale, puis d'assurance maladie, des agents de la CNRPS.

    La série commence au 1er avril 1973 : 1 % de cotisation de l'assuré et 1 % de
    contribution de l'État (décret n° 73-91, articles 14 et 16), avant la montée en charge
    du régime de base d'assurance maladie (décret n° 2007-1406, article 4).
    """
    m = MOTS[langue]
    base = f"{PUBLIC}/salarie_cnrps"
    return ot.tableau_taux_datee(
        [(f"{base}/cotisations_employeur/maladie.yaml", m["maladie_employeur"], _taux(langue)),
         (f"{base}/cotisations_salarie/maladie.yaml", m["maladie_agent"], _taux(langue))],
        cles={"1973-04-01": "decret73-91, art. 14 et 16",
              **dict.fromkeys(("2007-07-01", "2008-07-01", "2009-07-01"),
                              "decret2007-1406, art. 4")},
        colonne_periode=m["effet"], colonne_texte=m["texte"], langue=langue,
        colonne_total=m["total"])


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
    "1989-01-01": "loi88-145-lf1989, art. 29-30 et 35",
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
    "atmp_forfaits.md": atmp_forfaits,
    "atmp_journees.md": atmp_journees,
    "atmp_modulation.md": atmp_modulation,
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

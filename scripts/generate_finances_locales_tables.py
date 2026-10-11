"""Régénère les snapshots des tableaux du livre « Les finances locales ».

Même contrat que les autres générateurs : le build du site n'exécute PAS ce script, il lit
les fichiers qu'il produit, versionnés dans `precis/{fr,ar}/finances_locales/tables/`.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_finances_locales_tables.py

CE QUI EST ENGENDRÉ, POUR LE CHAPITRE « LES IMPÔTS SUR LES IMMEUBLES » — les barèmes des deux
taxes sur les immeubles (`fiscalite_locale/`, versé en 0.125) :
  - `tib_taux_dates_reperes.md` : les quatre taux de la taxe sur les immeubles bâtis selon
    le nombre de services, par le composant commun `ot.ecrire_dates_reperes` ;
  - `tib_prix_reference.md` : le minimum et le maximum du prix de référence du mètre carré
    couvert, une ligne par catégorie de superficie, une colonne par grandeur et par date ;
  - `tnb_tarif.md` : le tarif au mètre carré de la taxe sur les terrains non bâtis, une
    ligne par zone de densité, une colonne par date ;
  - deux séries longues au cache `precis/_seriescache/`, par le composant commun
    `ot.ecrire_serie_parametres` : `fl-tib-prix-reference` (huit grandeurs, le minimum et le
    maximum de chaque catégorie) et `fl-tnb-tarif` (trois zones), une ligne par grandeur et
    par date d'effet, avec le texte et son lien au Journal officiel. Les figures en escalier
    du chapitre les lisent par `figtools.series()` ; chacune a sa série, donc ses propres
    liens « Base législative ».

CE QUI EST ENGENDRÉ, POUR LE CHAPITRE « LES IMPÔTS SUR L'ACTIVITÉ » — la taxe sur les
établissements (`fiscalite_locale/taxe_etablissements/`, versé en 0.133) :
  - `tcl_minimum.md` : la taxe par mètre carré de référence, seize lignes — quatre
    catégories d'immeuble, quatre taux de la taxe sur les immeubles bâtis — et une colonne
    par date d'effet. Quatre colonnes de taux à trois dates en feraient douze : le tableau
    se lit donc en long, la catégorie, l'immeuble et le taux chacun dans sa colonne ;
  - `tcl_maximum.md` : le maximum de la taxe à ses quatre dates d'effet, la dernière étant
    sa suppression, dite en clair dans la case (`ParametreSupprimable`) ;
  - `tcl_taux.md` : les six taux par assiette aux trois dates où l'un d'eux change. Les
    assiettes n'ont pas toutes les mêmes dates d'effet — une assiette est créée, une autre
    close — : le tableau exige seulement que chaque date d'effet soit une de ses colonnes
    (`dates_communes=False`), et rend « — » pour une assiette qui n'existe pas à la date ;
  - deux séries longues au cache : `fl-tcl-minimum` (seize grandeurs) et `fl-tcl-maximum`
    (une grandeur, close par une valeur vide au 1er janvier 2012).

LA FORME DES DEUX BARÈMES. `ot.tableau_dates_reperes` met un paramètre par ligne ; ici une
ligne réunit plusieurs paramètres — le minimum et le maximum d'une même catégorie —, et le
barème se lit à ses dates d'effet, côte à côte. `tableau_cote_a_cote` le compose avec les
briques communes (`ParametreDate`, `etat_a_la_date`, relevé des liens). L'unité est dans
l'en-tête, la case ne porte que le nombre — y compris le mètre carré des catégories : sous
ses onglets, le tableau à sept colonnes n'a que 662 px à 1 300 px de fenêtre, et la première
cellule d'un tableau engendré ne se replie pas. Pour la même raison, un libellé long ne va
jamais dans la première colonne : les tableaux de la taxe sur les établissements ont une
première colonne courte (le numéro de la catégorie, la nature de la base) et le libellé long
dans la deuxième, qui se replie.

LES EN-TÊTES RENVOIENT AU REGISTRE DU CHAPITRE. Chaque colonne porte l'année de sa date
d'effet, en lien vers la ligne du registre replié qui donne le décret, son article et sa
page (`ANCRES_PRIX`, `ANCRES_TARIF`, `ANCRES_MINIMUM`, `ANCRES_MAXIMUM`, `ANCRES_TAUX_TCL`). Ces ancres sont déclarées ici, date par date : une
date d'effet que le modèle porte et qui n'a pas sa ligne de registre arrête le générateur,
plutôt que de publier une colonne sans référence.

CE QUI NE L'EST PAS. Les registres des décrets (dates d'effet, abrogations, pages) restent
écrits dans le chapitre : ils portent les références. Le taux d'assiette (2 %) et le taux
sur la valeur vénale (0,3 %) sont donnés en prose, avec leur article. Le seuil au-delà duquel
le produit de la taxe sur les établissements va à un fonds (une valeur, depuis 2013) est
donné en prose lui aussi. La taxe hôtelière (`fiscalite_locale/taxe_hoteliere/`, deux
valeurs de 1997) garde son tableau fait main : ses deux lignes ont chacune leur ligne de
registre et leur base — le chiffre d'affaires, le produit de la taxe —, ce qu'une colonne
de date à une seule ancre et une seule unité ne rend pas. Les droits et redevances ne sont
pas dans l'arbre.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

FL = "parameters/fiscalite_locale"
TIB = f"{FL}/taxe_immeubles_batis"
TNB = f"{FL}/taxe_terrains_non_batis"
TCL = f"{FL}/taxe_etablissements"
RACINE = Path(__file__).parent.parent / "precis"
LIVRE = "finances_locales"
LANGUES = ("fr", "ar")
CACHE = RACINE / "_seriescache"
SERIE_PRIX = "fl-tib-prix-reference"
SERIE_TARIF = "fl-tnb-tarif"
SERIE_MINIMUM = "fl-tcl-minimum"
SERIE_MAXIMUM = "fl-tcl-maximum"

# Date d'effet -> ancre de la ligne du registre replié, dans `_impots_immeubles.qmd`.
ANCRES_PRIX = {"1997-03-13": "r-fl-imm-prix-1997", "2008-01-01": "r-fl-imm-prix-2008",
               "2017-01-01": "r-fl-imm-prix-2017"}
ANCRES_TARIF = {"1997-03-13": "r-fl-imm-tarif-1997", "2008-01-01": "r-fl-imm-tarif-2008",
                "2017-01-01": "r-fl-imm-tarif-2017"}

# Date d'effet -> ancre de la ligne du registre replié, dans `_impots_activite.qmd`. Au
# 1er janvier 2013, deux lignes du registre se suivent — l'assiette sur l'impôt (art. 23),
# le taux réduit (art. 24) ; l'en-tête renvoie à celle du taux, qui cite la rubrique
# commune aux deux articles.
ANCRES_MINIMUM = {"1997-03-13": "r-fl-act-minimum-1997", "2008-01-01": "r-fl-act-minimum-2008",
                  "2017-01-01": "r-fl-act-minimum-2017"}
ANCRES_MAXIMUM = {"1997-03-13": "r-fl-act-plafond-1997", "2003-06-26": "r-fl-act-plafond-2003",
                  "2007-01-01": "r-fl-act-plafond-2007", "2012-01-01": "r-fl-act-plafond-2012"}
ANCRES_TAUX_TCL = {"1997-01-01": "r-fl-act-1997-assiette", "2013-01-01": "r-fl-act-taux-2013",
                   "2014-01-01": "r-fl-act-assiette-2014"}

# Le code entre en vigueur le 1er janvier 1997 ; les quatre taux n'ont pas changé depuis.
EFFET_TAUX = "1997-01-01"
PALIERS = ("un_ou_deux_services", "trois_ou_quatre_services", "plus_de_quatre_services",
           "plus_de_quatre_services_et_autres_services")
CATEGORIES = (1, 2, 3, 4)
ZONES = ("haute", "moyenne", "basse")
TAUX_TIB = (8, 10, 12, 14)
# Assiette de la taxe sur les établissements -> nature de sa base, première colonne du tableau.
ASSIETTES = (("chiffre_affaires_brut_local", "base_ca"), ("chiffre_affaires_brut", "base_ca"),
             ("exportation_et_non_residents", "base_ca"), ("produits_prix_homologues", "base_ca"),
             ("impot_regime_1997", "base_impot"), ("impot_regime_2013", "base_impot"))

# Libellés arabes : noms des taxes et du prix de référence d'après le glossaire ; zones et
# paliers de services d'après l'édition arabe du Journal officiel, que citent les notes des
# paramètres. Pour la taxe sur les établissements : les quatre immeubles et les en-têtes du
# minimum d'après l'édition arabe du décret gouvernemental n° 2017-395 (JORT n° 26 du 31 mars
# 2017, p. 1004-1005) ; l'exportation et les non-résidents d'après celle de la loi de
# finances pour 2014, art. 49 (JORT n° 105 du 31 décembre 2013). Les autres libellés arabes
# de cette taxe — chiffre d'affaires brut, produits à prix homologués, redevables taxés sur
# leur impôt, maximum et sa suppression — ne sont pas relevés sur l'édition arabe des
# textes : ils sont composés avec le vocabulaire du glossaire, et restent à confronter.
MOTS = {
    "fr": {
        "services": "Services dont bénéficie l'immeuble",
        "taux": "Taux $\\tau$<br>(% de l'assiette)",
        "un_ou_deux_services": "un ou deux",
        "trois_ou_quatre_services": "trois ou quatre",
        "plus_de_quatre_services": "plus de quatre",
        "plus_de_quatre_services_et_autres_services":
            "plus de quatre, et services supplémentaires",
        "taux_lien": "Taux de la taxe sur les immeubles bâtis — {palier}",
        "lien_un_ou_deux_services": "un ou deux services",
        "lien_trois_ou_quatre_services": "trois ou quatre services",
        "lien_plus_de_quatre_services": "plus de quatre services",
        "lien_plus_de_quatre_services_et_autres_services":
            "plus de quatre services et d'autres services",
        "categorie": "Catégorie<br>(superficie couverte, m²)",
        "jusqu_a": "{n} : jusqu'à {b}", "de_a": "{n} : de {a} à {b}",
        "plus_de": "{n} : plus de {a}",
        "minimum": "Minimum", "maximum": "Maximum", "unite": "(D/m²)",
        "prix_lien": "{borne} du prix de référence du mètre carré couvert — catégorie {n}",
        "seuil_lien": "Superficie couverte maximale de la catégorie {n}",
        "zone": "Zone du plan d'aménagement urbain",
        "haute": "haute densité", "moyenne": "moyenne densité", "basse": "basse densité",
        "tarif": "Tarif",
        "tarif_lien": "Tarif au mètre carré de la taxe sur les terrains non bâtis — zone à {zone}",
        "categorie_tcl": "Catégorie", "immeuble": "Immeuble",
        "taux_tib": "Taux de la taxe sur les immeubles bâtis<br>(%)",
        "immeuble_1": "à usage administratif, ou d'activité commerciale ou non commerciale",
        "immeuble_2": "à structure légère, à usage industriel",
        "immeuble_3": "en béton solide, à usage industriel",
        "immeuble_4": "à usage industriel, de plus de 5 000 m² de superficie couverte",
        "minimum_lien": ("Taxe par mètre carré de référence du minimum de la taxe sur les "
                         "établissements — catégorie {n}, taux de {t} %"),
        "taxe": "Taxe sur les établissements", "maximum_ligne": "maximum de la taxe",
        "unite_an": "(D par an)", "supprime": "aucun : maximum supprimé",
        "maximum_lien": "Maximum de la taxe sur les établissements",
        "base": "Base", "assiette": "Assiette", "unite_taux": "(% de l'assiette)",
        "taux_tcl": "Taux",
        "base_ca": "chiffre d'affaires", "base_impot": "impôt",
        "chiffre_affaires_brut_local": "chiffre d'affaires brut local",
        "chiffre_affaires_brut": "chiffre d'affaires brut",
        "exportation_et_non_residents": (
            "chiffre d'affaires provenant de l'exportation ; chiffre d'affaires réalisé avec "
            "les non-résidents par les établissements de santé qui leur prêtent la totalité "
            "de leurs services, par les prestataires de services financiers non résidents et "
            "par les sociétés d'investissement à capital variable à règles d'investissement "
            "allégées"),
        "produits_prix_homologues": (
            "chiffre d'affaires des établissements qui commercialisent des produits à prix "
            "homologués à marge brute d'au plus 6 %"),
        "impot_regime_1997": (
            "impôt sur le revenu ou sur les sociétés des forfaitaires, des établissements à "
            "marge brute réglementée d'au plus 4 % et des établissements déficitaires"),
        "impot_regime_2013": (
            "impôt sur le revenu ou sur les sociétés des forfaitaires de l'article 44 bis et "
            "des établissements en perte ; sur option, des établissements qui commercialisent "
            "des produits à prix homologués à marge brute d'au plus 6 %"),
        "taux_tcl_lien": "Taux de la taxe sur les établissements — {assiette}",
        "lien_chiffre_affaires_brut_local": "chiffre d'affaires brut local",
        "lien_chiffre_affaires_brut": "chiffre d'affaires brut",
        "lien_exportation_et_non_residents": "exportation et services aux non-résidents",
        "lien_produits_prix_homologues": "produits à prix homologués à marge d'au plus 6 %",
        "lien_impot_regime_1997": "impôt, redevables désignés en 1997",
        "lien_impot_regime_2013": "impôt, redevables désignés en 2013",
    },
    "ar": {
        "services": "الخدمات التي ينتفع بها العقار",
        "taux": "النسبة $\\tau$<br>(% من الوعاء)",
        "un_ou_deux_services": "خدمة أو خدمتان",
        "trois_ou_quatre_services": "ثلاث أو أربع خدمات",
        "plus_de_quatre_services": "أكثر من أربع خدمات",
        "plus_de_quatre_services_et_autres_services": "أكثر من أربع خدمات وخدمات أخرى",
        "taux_lien": "نسبة المعلوم على العقارات المبنية — {palier}",
        "lien_un_ou_deux_services": "خدمة أو خدمتان",
        "lien_trois_ou_quatre_services": "ثلاث أو أربع خدمات",
        "lien_plus_de_quatre_services": "أكثر من أربع خدمات",
        "lien_plus_de_quatre_services_et_autres_services": "أكثر من أربع خدمات وخدمات أخرى",
        "categorie": "الصنف<br>(المساحة المغطاة، م²)",
        "jusqu_a": "{n}: إلى {b}", "de_a": "{n}: من {a} إلى {b}",
        "plus_de": "{n}: أكثر من {a}",
        "minimum": "الحد الأدنى", "maximum": "الحد الأقصى", "unite": "(د/م²)",
        "prix_lien": "{borne} للثمن المرجعي للمتر المربع المبني — الصنف {n}",
        "seuil_lien": "المساحة المغطاة القصوى للصنف {n}",
        "zone": "المنطقة حسب مثال التهيئة العمرانية",
        "haute": "كثافة عمرانية مرتفعة", "moyenne": "كثافة عمرانية متوسطة",
        "basse": "كثافة عمرانية منخفضة",
        "tarif": "المبلغ",
        "tarif_lien": "مبلغ المعلوم على الأراضي غير المبنية للمتر المربع — منطقة ذات {zone}",
        "categorie_tcl": "صنف العقار", "immeuble": "خصوصية العقار",
        "taux_tib": "نسبة المعلوم على العقارات المبنية<br>(%)",
        "immeuble_1": "عقار معد لاستعمال إداري أو لتعاطي نشاط تجاري أو غير تجاري",
        "immeuble_2": "عقار ذو متانة خفيفة معد لتعاطي نشاط صناعي",
        "immeuble_3": "عقار متين معد لتعاطي نشاط صناعي",
        "immeuble_4": "عقار تفوق مساحته المغطاة 5000 متر مربع معد لتعاطي نشاط صناعي",
        "minimum_lien": ("المعلوم بالمتر المربع المرجعي، الحد الأدنى للمعلوم على المؤسسات — "
                         "الصنف {n}، نسبة {t} %"),
        "taxe": "المعلوم على المؤسسات", "maximum_ligne": "الحد الأقصى للمعلوم",
        "unite_an": "(د في السنة)", "supprime": "لا شيء: حُذف الحد الأقصى",
        "maximum_lien": "الحد الأقصى للمعلوم على المؤسسات",
        "base": "القاعدة", "assiette": "الوعاء", "unite_taux": "(% من الوعاء)",
        "taux_tcl": "النسبة",
        "base_ca": "رقم المعاملات", "base_impot": "الضريبة",
        "chiffre_affaires_brut_local": "رقم المعاملات الخام المحلي",
        "chiffre_affaires_brut": "رقم المعاملات الخام",
        "exportation_et_non_residents": (
            "رقم المعاملات المتأتي من التصدير؛ رقم المعاملات المحقق من قبل المؤسسات الصحية "
            "التي تسدي كامل خدماتها لفائدة غير المقيمين المتأتي من نشاطها مع غير المقيمين، "
            "ومن قبل مسدي الخدمات المالية غير المقيمين المتأتي من عملياتهم مع غير المقيمين، "
            "ومن قبل شركات الاستثمار ذات رأس المال المتغير الخاضعة لقواعد استثمار مخففة "
            "المتأتي من استعمال موجوداتها مع غير المقيمين"),
        "produits_prix_homologues": (
            "رقم معاملات المؤسسات التي تسوّق منتجات خاضعة لنظام المصادقة الإدارية للأسعار "
            "لا يتجاوز هامش ربحها الخام 6 %"),
        "impot_regime_1997": (
            "الضريبة على الدخل أو الضريبة على الشركات للخاضعين للنظام التقديري، وللمؤسسات "
            "التي لا يتجاوز هامش ربحها الخام 4 % بمقتضى نص ترتيبي، وللمؤسسات التي تسجّل خسارة"),
        "impot_regime_2013": (
            "الضريبة على الدخل أو الضريبة على الشركات للخاضعين للنظام التقديري المنصوص عليه "
            "بالفصل 44 مكرر وللمؤسسات التي تسجّل خسارة؛ وباختيار منها، للمؤسسات التي تسوّق "
            "منتجات خاضعة لنظام المصادقة الإدارية للأسعار لا يتجاوز هامش ربحها الخام 6 %"),
        "taux_tcl_lien": "نسبة المعلوم على المؤسسات — {assiette}",
        "lien_chiffre_affaires_brut_local": "رقم المعاملات الخام المحلي",
        "lien_chiffre_affaires_brut": "رقم المعاملات الخام",
        "lien_exportation_et_non_residents": "التصدير والخدمات المسداة لغير المقيمين",
        "lien_produits_prix_homologues": "منتجات خاضعة للمصادقة الإدارية للأسعار، هامش لا يتجاوز 6 %",
        "lien_impot_regime_1997": "الضريبة، المطالبون بالأداء المعيّنون سنة 1997",
        "lien_impot_regime_2013": "الضريبة، المطالبون بالأداء المعيّنون سنة 2013",
    },
}


def pourcentage_nu(valeur: float, _langue: str) -> str:
    """Un taux sans son signe : « 8 », l'unité étant dans l'en-tête de la colonne."""
    return f"{valeur * 100:.4f}".rstrip("0").rstrip(".").replace(".", ",")


def entier_nu(valeur: float, _langue: str) -> str:
    """Un montant en dinars entiers, sans unité ; un montant à millimes arrête le générateur."""
    if not float(valeur).is_integer():
        raise ValueError(f"montant non entier : {valeur}")
    return f"{int(valeur):,}".replace(",", " ")


def millimes_nus(valeur: float, _langue: str) -> str:
    """Un montant au millime, sans unité : « 0,300 », comme l'écrit le Journal officiel."""
    return f"{valeur:,.3f}".replace(",", " ").replace(".", ",")


def tous(champ: str, **valeurs) -> dict[str, str]:
    """Le libellé `champ`, complété par `valeurs`, dans chaque langue."""
    return {l: MOTS[l][champ].format(**{c: (MOTS[l][v] if v in MOTS[l] else v)
                                        for c, v in valeurs.items()}) for l in LANGUES}


def parametres_taux() -> list:
    return [ot.ParametreDate(p, f"{TIB}/taux/{p}.yaml", tous(p), format=pourcentage_nu,
                             lien=tous("taux_lien", palier=f"lien_{p}")) for p in PALIERS]


def parametre_prix(categorie: int, borne: str):
    return ot.ParametreDate(
        f"categorie_{categorie}_{borne}",
        f"{TIB}/prix_reference/categorie_{categorie}/{borne}.yaml", tous(borne),
        format=entier_nu, lien=tous("prix_lien", borne=borne, n=str(categorie)))


def parametre_seuil(categorie: int):
    libelle = tous("seuil_lien", n=str(categorie))
    return ot.ParametreDate(f"seuil_{categorie}",
                            f"{TIB}/seuils_superficie/categorie_{categorie}.yaml",
                            libelle, format=entier_nu)


def parametre_tarif(zone: str):
    return ot.ParametreDate(zone, f"{TNB}/tarif_m2/{zone}_densite.yaml", tous(zone),
                            format=millimes_nus, lien=tous("tarif_lien", zone=zone))


class ParametreSupprimable(ot.ParametreDate):
    """Un paramètre que la loi supprime : la case le dit en clair, au lieu du « — » commun.

    Ne vaut que dans un tableau dont la première colonne est la date de création du
    paramètre : une valeur absente y est alors toujours une suppression.
    """

    def rendre(self, valeur, langue):
        return MOTS[langue]["supprime"] if valeur is None else super().rendre(valeur, langue)


def parametre_minimum(categorie: int, taux: int):
    return ot.ParametreDate(
        f"categorie_{categorie}_taux_{taux}",
        f"{TCL}/minimum/categorie_{categorie}/taux_{taux}.yaml",
        tous("minimum_lien", n=str(categorie), t=str(taux)), format=millimes_nus)


def parametre_maximum():
    return ParametreSupprimable("maximum", f"{TCL}/maximum.yaml", tous("maximum_ligne"),
                                format=entier_nu, lien=tous("maximum_lien"))


def parametre_taux_tcl(assiette: str):
    return ot.ParametreDate(assiette, f"{TCL}/taux/{assiette}.yaml", tous(assiette),
                            format=pourcentage_nu,
                            lien=tous("taux_tcl_lien", assiette=f"lien_{assiette}"))


def libelles_categories(dates: list[str], langue: str) -> list[str]:
    """Les quatre lignes du barème, bornées par les seuils de superficie du code.

    Le libellé n'a pas de date : il n'est écrit que si chaque seuil a la même valeur à
    toutes les dates du tableau. Un seuil qui changerait appellerait une autre forme.
    """
    m = MOTS[langue]
    seuils = []
    for categorie in CATEGORIES[:-1]:
        p = parametre_seuil(categorie)
        serie = p.serie()
        etats = {ot.etat_a_la_date(serie, d) for d in dates}
        if len(etats) != 1 or None in etats:
            raise ValueError(f"seuil de la catégorie {categorie} : états {sorted(map(str, etats))} "
                             f"aux dates {dates}")
        ot.releve_note(p.chemin, p.lien[langue])
        seuils.append(p.rendre(etats.pop(), langue))
    libelles = [m["jusqu_a"].format(n=1, b=seuils[0])]
    libelles += [m["de_a"].format(n=i + 2, a=seuils[i], b=seuils[i + 1])
                 for i in range(len(seuils) - 1)]
    libelles.append(m["plus_de"].format(n=len(seuils) + 1, a=seuils[-1]))
    return libelles


def tableau_cote_a_cote(lignes: list[tuple[str | tuple, list]], grandeurs: list[str],
                        ancres: dict[str, str], entete: str | tuple, unite: str, langue: str,
                        dates_communes: bool = True):
    """Un barème à ses dates d'effet, côte à côte : une colonne par grandeur et par date.

    `lignes` : [(libellé de ligne, [un `ParametreDate` par grandeur])]. `grandeurs` : les
    en-têtes des grandeurs, dans l'ordre des paramètres d'une ligne. `ancres` : date d'effet
    -> ancre du registre du chapitre ; ses dates sont les colonnes. Chaque date d'effet
    d'un paramètre doit y figurer, et chaque date déclarée être une date d'effet : le
    tableau ne passe sous silence aucun texte que le modèle porte, et n'en annonce aucun
    qu'il ne porte pas.

    Le libellé de ligne et `entete` peuvent être des n-uplets de même longueur : la ligne
    s'identifie alors par plusieurs colonnes, une chose par colonne. `dates_communes=False`
    quand les paramètres n'ont pas tous les mêmes dates d'effet — l'un est créé, l'autre
    clos : chaque date d'effet doit encore être une colonne, et chaque colonne la date
    d'effet d'un paramètre au moins ; une case rend « — » si le paramètre n'existe pas à
    la date.
    """
    import pandas as pd

    dates = sorted(ancres)
    entetes = (entete,) if isinstance(entete, str) else tuple(entete)
    series, toutes = {}, set()
    for _libelle, parametres in lignes:
        for p in parametres:
            series[p.chemin] = p.serie()
            if not series[p.chemin]:
                print(f"✗ paramètre introuvable ou vide : {p.chemin}")
                return None
            effets = {d for d, *_ in series[p.chemin]}
            toutes |= effets
            if effets != set(dates) if dates_communes else not effets <= set(dates):
                raise ValueError(f"{p.chemin} : dates d'effet {sorted(effets)}, "
                                 f"registre du chapitre {dates}")
    if toutes != set(dates):
        raise ValueError(f"dates d'effet {sorted(toutes)}, registre du chapitre {dates}")
    sortie = []
    for libelle, parametres in lignes:
        ligne = dict(zip(entetes, (libelle,) if isinstance(libelle, str) else libelle))
        for date in dates:
            for grandeur, p in zip(grandeurs, parametres):
                ot.releve_note(p.chemin, p.lien[langue])
                colonne = "<br>".join(
                    partie for partie in (grandeur, f"[{date[:4]}](#{ancres[date]})", unite)
                    if partie)
                ligne[colonne] = p.rendre(ot.etat_a_la_date(series[p.chemin], date), langue)
        sortie.append(ligne)
    return pd.DataFrame(sortie)


def tableau_prix(langue: str):
    m = MOTS[langue]
    libelles = libelles_categories(sorted(ANCRES_PRIX), langue)
    lignes = [(libelle, [parametre_prix(c, "minimum"), parametre_prix(c, "maximum")])
              for libelle, c in zip(libelles, CATEGORIES)]
    return tableau_cote_a_cote(lignes, [m["minimum"], m["maximum"]], ANCRES_PRIX,
                               m["categorie"], m["unite"], langue)


def tableau_tarif(langue: str):
    m = MOTS[langue]
    lignes = [(m[z], [parametre_tarif(z)]) for z in ZONES]
    return tableau_cote_a_cote(lignes, [m["tarif"]], ANCRES_TARIF, m["zone"], m["unite"],
                               langue)


def tableau_minimum(langue: str):
    m = MOTS[langue]
    lignes = [((str(c), m[f"immeuble_{c}"], str(t)), [parametre_minimum(c, t)])
              for c in CATEGORIES for t in TAUX_TIB]
    return tableau_cote_a_cote(lignes, [m["minimum"]], ANCRES_MINIMUM,
                               (m["categorie_tcl"], m["immeuble"], m["taux_tib"]),
                               m["unite"], langue)


def tableau_maximum(langue: str):
    m = MOTS[langue]
    p = parametre_maximum()
    return tableau_cote_a_cote([(p.libelle[langue], [p])], [m["maximum"]], ANCRES_MAXIMUM,
                               m["taxe"], m["unite_an"], langue)


def tableau_taux_tcl(langue: str):
    m = MOTS[langue]
    lignes = [((m[base], m[assiette]), [parametre_taux_tcl(assiette)])
              for assiette, base in ASSIETTES]
    return tableau_cote_a_cote(lignes, [m["taux_tcl"]], ANCRES_TAUX_TCL,
                               (m["base"], m["assiette"]), m["unite_taux"], langue,
                               dates_communes=False)


def entete_snapshot(dates: list[str], chemins: list[str]) -> str:
    return (f"<!-- Généré par scripts/{Path(__file__).name} — ne pas éditer à la main.\n"
            f"     État en vigueur aux dates d'effet : {', '.join(dates)}.\n"
            f"     Paramètres : {', '.join(chemins)} -->\n\n")


def ecrire_cote_a_cote(nom: str, fabrique, ancres: dict[str, str]) -> int:
    for langue in LANGUES:
        try:
            df, liens = ot.avec_liens(lambda: fabrique(langue))
        except ValueError as erreur:
            print(f"✗ {langue}/{nom} : {erreur}")
            return 1
        if df is None or df.empty:
            print(f"✗ {langue}/{nom} : paramètre introuvable ou vide.")
            return 1
        erreur = ot.ecrire_dans_livres(
            RACINE, langue, (LIVRE,), nom, df, liens,
            entete=entete_snapshot(sorted(ancres), [c for c, _l in liens]))
        if erreur:
            print(erreur)
            return 1
    print(f"✓ {nom} : {len(df)} lignes, {len(df.columns) - 1} colonnes")
    return 0


def ecrire_taux() -> int:
    """Les quatre taux à la date d'entrée en vigueur du code, qui est aussi leur seule date."""
    parametres = parametres_taux()
    for p in parametres:
        effets = [d for d, *_ in p.serie()]
        if effets != [EFFET_TAUX]:
            print(f"✗ tib_taux : {p.chemin} a pour dates d'effet {effets}, et non la seule "
                  f"{EFFET_TAUX} : le tableau à une colonne ne suffit plus.")
            return 1
    code = ot.ecrire_dates_reperes(
        RACINE, LIVRE, "tib_taux", parametres, [EFFET_TAUX],
        entete={l: MOTS[l]["services"] for l in LANGUES},
        entetes_dates={l: {EFFET_TAUX: MOTS[l]["taux"]} for l in LANGUES},
        generateur=Path(__file__).name)
    if not code:
        print(f"✓ tib_taux_dates_reperes.md : {len(parametres)} taux")
    return code


def ecrire_series() -> int:
    """Les barèmes en séries longues, que tracent les figures en escalier des chapitres."""
    prix = [parametre_prix(c, borne) for c in CATEGORIES for borne in ("minimum", "maximum")]
    tarif = [parametre_tarif(z) for z in ZONES]
    minimum = [parametre_minimum(c, t) for c in CATEGORIES for t in TAUX_TIB]
    return (ot.ecrire_serie_parametres(SERIE_PRIX, prix, CACHE)
            or ot.ecrire_serie_parametres(SERIE_TARIF, tarif, CACHE)
            or ot.ecrire_serie_parametres(SERIE_MINIMUM, minimum, CACHE)
            or ot.ecrire_serie_parametres(SERIE_MAXIMUM, [parametre_maximum()], CACHE))


def main() -> int:
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version {ot.version_openfisca()}, "
            f"minimum {ot.VERSION_MINIMALE}). Les snapshots existants sont conservés."
        )
        return 1
    return (ecrire_taux()
            or ecrire_cote_a_cote("tib_prix_reference.md", tableau_prix, ANCRES_PRIX)
            or ecrire_cote_a_cote("tnb_tarif.md", tableau_tarif, ANCRES_TARIF)
            or ecrire_cote_a_cote("tcl_minimum.md", tableau_minimum, ANCRES_MINIMUM)
            or ecrire_cote_a_cote("tcl_maximum.md", tableau_maximum, ANCRES_MAXIMUM)
            or ecrire_cote_a_cote("tcl_taux.md", tableau_taux_tcl, ANCRES_TAUX_TCL)
            or ecrire_series())


if __name__ == "__main__":
    raise SystemExit(main())

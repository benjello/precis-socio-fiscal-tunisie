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

CE QUI EST ENGENDRÉ, POUR LES DISPOSITIONS SECONDAIRES ET LE CHAPITRE « TAXES, REDEVANCES ET
AUTONOMIE FISCALE » — pénalité de retard, taxe sur les spectacles, contribution des
riverains, droit de licence, contribution aux parkings (versés en 0.134) :
  - `penalite_retard.md` : le taux mensuel de la pénalité de retard des taxes sur les
    immeubles et le plafond de son total, aux cinq dates où l'un des deux change. Les deux
    grandeurs n'ont pas la même unité : chacune la porte dans son libellé de ligne, et
    l'absence de plafond avant 2022 est dite en clair (`ParametreSupprimable`) ;
  - `taxes_baremes.md` : les taux et les tarifs des chapitres V à VII du code — spectacles,
    riverains, licence. Ces grandeurs n'ont pas de dates communes (trois dates de 1997, une
    de 2002) : le tableau se lit en long, une grandeur par ligne, chaque ligne à ses dates
    (`tableau_grandeurs_datees`). Une grandeur close — la réduction de la contribution des
    riverains, remplacée au 1er août 2002 — donne sa période et dit en clair ce qui la
    remplace ;
  - `parkings_1997.md` : le barème de 1997 de la contribution aux parkings collectifs, une
    ligne par tranche de population, et son remplacement de 2003 dit en clair ;
  - `parkings_2003.md` : le barème de 2003, à deux entrées — une ligne par tranche de
    population, une colonne par part des places manquantes, neuf montants ;
  - deux séries longues au cache : `fl-tib-penalite-retard` (le taux mensuel) et
    `fl-parkings` (douze grandeurs : les trois du barème de 1997, closes au 1er janvier
    2003, et les neuf du barème de 2003).

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
page (`ANCRES_PRIX`, `ANCRES_TARIF`, `ANCRES_MINIMUM`, `ANCRES_MAXIMUM`, `ANCRES_TAUX_TCL`,
`ANCRES_PENALITE`, `ANCRES_PARKINGS_1997`, `ANCRES_PARKINGS_2003` ; `ANCRES_TAXES`, par grandeur
et par date, pour le tableau en long). Ces ancres sont déclarées ici, date par date : une
date d'effet que le modèle porte et qui n'a pas sa ligne de registre arrête le générateur,
plutôt que de publier une colonne sans référence.

CE QUI NE L'EST PAS. Les registres des décrets (dates d'effet, abrogations, pages) restent
écrits dans le chapitre : ils portent les références. Le taux d'assiette (2 %) et le taux
sur la valeur vénale (0,3 %) sont donnés en prose, avec leur article. Le seuil au-delà duquel
le produit de la taxe sur les établissements va à un fonds (une valeur, depuis 2013) est
donné en prose lui aussi. La taxe hôtelière (`fiscalite_locale/taxe_hoteliere/`, deux
valeurs de 1997) garde son tableau fait main : ses deux lignes ont chacune leur ligne de
registre et leur base — le chiffre d'affaires, le produit de la taxe —, ce qu'une colonne
de date à une seule ancre et une seule unité ne rend pas. Trois tableaux du volume gardent
une forme faite main parce que l'arbre n'en porte qu'une ligne : le prélèvement au profit
du Fonds national d'amélioration de l'habitat avant et depuis 2005 (seul le taux de 2005 est
versé), les deux dégrèvements de la taxe sur les immeubles bâtis (seul le dégrèvement
partiel, clos en 2003, a un taux) et les forfaits qui comprennent la taxe sur les
établissements (seule la part de l'auto-entrepreneur est chiffrée). Les tarifs des taxes et
redevances diverses fixés par décret (chapitre VIII du code, hors parkings) ne sont pas
dans l'arbre.
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
PENALITE = f"{TIB}/penalite_retard"
SPECTACLES = f"{FL}/taxe_spectacles"
RIVERAINS = f"{FL}/contribution_riverains"
LICENCE = f"{FL}/droit_licence"
PARKINGS = f"{FL}/contribution_parkings"
RACINE = Path(__file__).parent.parent / "precis"
LIVRE = "finances_locales"
LANGUES = ("fr", "ar")
CACHE = RACINE / "_seriescache"
SERIE_PRIX = "fl-tib-prix-reference"
SERIE_TARIF = "fl-tnb-tarif"
SERIE_MINIMUM = "fl-tcl-minimum"
SERIE_MAXIMUM = "fl-tcl-maximum"
SERIE_PENALITE = "fl-tib-penalite-retard"
SERIE_PARKINGS = "fl-parkings"

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

# La pénalité de retard : quatre dates pour le taux, une — 2022 — pour le plafond.
ANCRES_PENALITE = {"1997-01-01": "r-fl-imm-penalite-1997", "2002-01-01": "r-fl-imm-penalite-2002",
                   "2007-01-01": "r-fl-imm-penalite-2007", "2022-01-01": "r-fl-imm-penalite-2022",
                   "2023-01-01": "r-fl-imm-penalite-2023"}

# Date d'effet -> ancre de la ligne de registre, dans `_taxes_redevances.qmd`. Le barème de
# 1997 des parkings est clos au 1er janvier 2003 : cette date est une colonne, qui renvoie
# à la loi qui le remplace.
ANCRES_PARKINGS_1997 = {"1997-01-01": "r-fl-tax-1997-parkings-bareme",
                        "2003-01-01": "r-fl-tax-2003-parkings"}
ANCRES_PARKINGS_2003 = {"2003-01-01": "r-fl-tax-2003-parkings"}

# Tranches de population et parts des places manquantes des deux barèmes des parkings :
# (clé du libellé, nom de la feuille ou du nœud).
POPULATIONS_1997 = (("pop_20_50", "population_20000_a_50000"),
                    ("pop_50_100", "population_50000_a_100000"),
                    ("pop_100", "population_plus_de_100000"))
POPULATIONS_2003 = (("pop_0_50", "population_jusqu_a_50000"),
                    ("pop_50_100", "population_50000_a_100000"),
                    ("pop_100", "population_plus_de_100000"))
MANQUES = (("manque_25", "manque_jusqu_a_25"), ("manque_75", "manque_25_a_75"),
           ("manque_100", "manque_plus_de_75"))

# Le tableau en long des chapitres V à VII du code : (chapitre, clé du prélèvement, clé de la
# grandeur, [feuilles], formateur, clé de ce qui remplace la grandeur à sa clôture).
GRANDEURS_TAXES = (
    ("V", "spectacles", "g_part_recettes", (f"{SPECTACLES}/part_recettes_previsionnelles",),
     "pourcentage", None),
    ("V", "spectacles", "g_taux_spectacles", (f"{SPECTACLES}/taux",), "pourcentage", None),
    ("V", "spectacles", "g_prix_exonere", (f"{SPECTACLES}/prix_entree_exonere_maximum",),
     "entier", None),
    ("VI", "riverains", "g_reduction", (f"{RIVERAINS}/reduction_maximale",), "pourcentage",
     "remplacee_degrevement"),
    ("VI", "riverains", "g_avance", (f"{RIVERAINS}/avance/minimum", f"{RIVERAINS}/avance/maximum"),
     "pourcentage", None),
    ("VII", "licence", "g_tarif_1", (f"{LICENCE}/tarif_annuel/categorie_1",), "entier", None),
    ("VII", "licence", "g_tarif_2", (f"{LICENCE}/tarif_annuel/categorie_2",), "entier", None),
    ("VII", "licence", "g_tarif_3", (f"{LICENCE}/tarif_annuel/categorie_3",), "entier", None),
    ("VII", "licence", "g_retenue", (f"{LICENCE}/retenue_budget_etat",), "pourcentage", None),
)

# (clé de la grandeur, date d'effet) -> ancre de la ligne de registre, dans
# `_taxes_redevances.qmd`. Une date de clôture renvoie au texte qui clôt.
ANCRES_TAXES = {
    ("g_part_recettes", "1997-01-01"): "r-fl-tax-1997-spectacles-assiette",
    ("g_taux_spectacles", "1997-01-01"): "r-fl-tax-1997-spectacles-taux",
    ("g_prix_exonere", "1997-04-07"): "r-fl-tax-1997-spectacles-prix",
    ("g_reduction", "1997-01-01"): "r-fl-tax-1997-riverains-calcul",
    ("g_reduction", "2002-08-01"): "r-fl-tax-2002-riverains",
    ("g_avance", "1997-01-01"): "r-fl-tax-1997-riverains-avance",
    ("g_tarif_1", "1997-03-13"): "r-fl-tax-1997-licence-tarif",
    ("g_tarif_2", "1997-03-13"): "r-fl-tax-1997-licence-tarif",
    ("g_tarif_3", "1997-03-13"): "r-fl-tax-1997-licence-tarif",
    ("g_retenue", "1997-01-01"): "r-fl-tax-1997-licence-declaration",
}

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
# Pour la pénalité de retard, les chapitres V à VII et les parkings : les noms des trois
# prélèvements des chapitres V à VII sont ceux du glossaire (entrée du code de la fiscalité
# locale) ; tous les autres libellés arabes — pénalité, plafond, grandeurs des trois
# prélèvements, tranches de population, parts des places manquantes, mentions de
# remplacement — sont composés ici, l'édition arabe de ces articles n'étant pas relue : ils
# restent à confronter au Journal officiel.
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
        "penalite": "Pénalité de retard",
        "penalite_taux": "taux (% par mois de retard)",
        "penalite_plafond": "plafond du total (% du principal)",
        "aucun_plafond": "aucun plafond",
        "penalite_taux_lien": "Taux mensuel de la pénalité de retard de la taxe sur les immeubles bâtis",
        "penalite_plafond_lien": ("Plafond du total des pénalités de retard de la taxe sur les "
                                  "immeubles bâtis, en part du principal"),
        "chapitre": "Chapitre du code", "prelevement": "Prélèvement", "grandeur": "Grandeur",
        "valeur": "Valeur", "en_vigueur": "En vigueur",
        "spectacles": "taxe sur les spectacles",
        "riverains": "contribution des propriétaires riverains",
        "licence": "droit de licence sur les débits de boissons",
        "g_part_recettes": "part des recettes prévisionnelles retenue dans l'assiette (%)",
        "g_taux_spectacles": "taux (% de l'assiette)",
        "g_prix_exonere": "prix d'entrée maximal des spectacles exonérés (D)",
        "g_reduction": "réduction maximale pour les cas sociaux (% de la contribution)",
        "g_avance": "avance, minimum et maximum (% de la contribution)",
        "g_tarif_1": "tarif annuel, établissement de la catégorie 1 (D)",
        "g_tarif_2": "tarif annuel, établissement de la catégorie 2 (D)",
        "g_tarif_3": "tarif annuel, établissement de la catégorie 3 (D)",
        "g_retenue": "retenue au profit du budget de l'État (% du droit)",
        "intervalle": "{a} à {b}",
        "depuis": "depuis le [{debut}](#{ancre})",
        "du_au": "du [{debut}](#{ancre}) au [{fin}](#{ancre_fin})",
        "du_au_remplace": "du [{debut}](#{ancre}) au [{fin}](#{ancre_fin}) ; {suite}",
        "remplacee_degrevement": "remplacée par un dégrèvement total",
        "lien_part_recettes_previsionnelles":
            "Taxe sur les spectacles — part des recettes prévisionnelles retenue",
        "lien_taux": "Taxe sur les spectacles — taux",
        "lien_prix_entree_exonere_maximum": "Taxe sur les spectacles — prix d'entrée exonéré",
        "lien_reduction_maximale": "Contribution des riverains — réduction maximale",
        "lien_minimum": "Contribution des riverains — avance, taux minimal",
        "lien_maximum": "Contribution des riverains — avance, taux maximal",
        "lien_categorie_1": "Droit de licence — tarif annuel, catégorie 1",
        "lien_categorie_2": "Droit de licence — tarif annuel, catégorie 2",
        "lien_categorie_3": "Droit de licence — tarif annuel, catégorie 3",
        "lien_retenue_budget_etat": "Droit de licence — retenue au profit du budget de l'État",
        "population": "Population de la commune",
        "pop_20_50": "plus de 20 000 et au plus 50 000 habitants",
        "pop_0_50": "au plus 50 000 habitants",
        "pop_50_100": "plus de 50 000 et au plus 100 000 habitants",
        "pop_100": "plus de 100 000 habitants",
        "contribution": "Contribution", "unite_place": "(D par place)",
        "bareme_remplace": "barème remplacé",
        "manque_25": "Manque : au plus 25 % des places requises",
        "manque_75": "Manque : plus de 25 % et au plus 75 %",
        "manque_100": "Manque : plus de 75 % et moins de 100 %",
        "parkings_1997_lien": "Contribution aux parkings collectifs, barème de 1997 — {population}",
        "parkings_2003_lien": ("Contribution aux parkings collectifs, barème de 2003 — "
                               "{manque}, {population}"),
        "lien_manque_25": "manque d'au plus 25 %", "lien_manque_75": "manque de 25 à 75 %",
        "lien_manque_100": "manque de plus de 75 %",
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
        "penalite": "خطية التأخير",
        "penalite_taux": "النسبة (% عن كل شهر تأخير)",
        "penalite_plafond": "الحد الأقصى للمجموع (% من أصل الدين)",
        "aucun_plafond": "لا حد أقصى",
        "penalite_taux_lien": "النسبة الشهرية لخطية التأخير للمعلوم على العقارات المبنية",
        "penalite_plafond_lien": ("الحد الأقصى لمجموع خطايا التأخير للمعلوم على العقارات "
                                  "المبنية، نسبةً من أصل الدين"),
        "chapitre": "الباب", "prelevement": "المعلوم", "grandeur": "المقدار",
        "valeur": "القيمة", "en_vigueur": "السريان",
        "spectacles": "المعلوم على العروض",
        "riverains": "مساهمة المالكين الأجوار",
        "licence": "معلوم الإجازة الموظف على محلات بيع المشروبات",
        "g_part_recettes": "الحصة المعتمدة من المداخيل التقديرية في الوعاء (%)",
        "g_taux_spectacles": "النسبة (% من الوعاء)",
        "g_prix_exonere": "السعر الأقصى للدخول إلى العروض المعفاة (د)",
        "g_reduction": "التخفيض الأقصى للحالات الاجتماعية (% من المساهمة)",
        "g_avance": "التسبقة، الحد الأدنى والحد الأقصى (% من المساهمة)",
        "g_tarif_1": "التعريفة السنوية، مؤسسة من الصنف 1 (د)",
        "g_tarif_2": "التعريفة السنوية، مؤسسة من الصنف 2 (د)",
        "g_tarif_3": "التعريفة السنوية، مؤسسة من الصنف 3 (د)",
        "g_retenue": "الخصم لفائدة ميزانية الدولة (% من المعلوم)",
        "intervalle": "من {a} إلى {b}",
        "depuis": "منذ [{debut}](#{ancre})",
        "du_au": "من [{debut}](#{ancre}) إلى [{fin}](#{ancre_fin})",
        "du_au_remplace": "من [{debut}](#{ancre}) إلى [{fin}](#{ancre_fin})؛ {suite}",
        "remplacee_degrevement": "عُوّض بطرح كلّي",
        "lien_part_recettes_previsionnelles":
            "المعلوم على العروض — الحصة المعتمدة من المداخيل التقديرية",
        "lien_taux": "المعلوم على العروض — النسبة",
        "lien_prix_entree_exonere_maximum": "المعلوم على العروض — سعر الدخول المعفى",
        "lien_reduction_maximale": "مساهمة المالكين الأجوار — التخفيض الأقصى",
        "lien_minimum": "مساهمة المالكين الأجوار — التسبقة، النسبة الدنيا",
        "lien_maximum": "مساهمة المالكين الأجوار — التسبقة، النسبة القصوى",
        "lien_categorie_1": "معلوم الإجازة — التعريفة السنوية، الصنف 1",
        "lien_categorie_2": "معلوم الإجازة — التعريفة السنوية، الصنف 2",
        "lien_categorie_3": "معلوم الإجازة — التعريفة السنوية، الصنف 3",
        "lien_retenue_budget_etat": "معلوم الإجازة — الخصم لفائدة ميزانية الدولة",
        "population": "عدد سكان البلدية",
        "pop_20_50": "أكثر من 20 000 ساكن دون أن يتجاوز 50 000",
        "pop_0_50": "لا يتجاوز 50 000 ساكن",
        "pop_50_100": "أكثر من 50 000 ساكن دون أن يتجاوز 100 000",
        "pop_100": "أكثر من 100 000 ساكن",
        "contribution": "المساهمة", "unite_place": "(د عن كل مكان)",
        "bareme_remplace": "عُوّض الجدول",
        "manque_25": "النقص: لا يتجاوز 25 % من الأماكن المطلوبة",
        "manque_75": "النقص: أكثر من 25 % دون أن يتجاوز 75 %",
        "manque_100": "النقص: أكثر من 75 % وأقل من 100 %",
        "parkings_1997_lien": "المساهمة في إنجاز مآوي جماعية، جدول 1997 — {population}",
        "parkings_2003_lien": "المساهمة في إنجاز مآوي جماعية، جدول 2003 — {manque}، {population}",
        "lien_manque_25": "نقص لا يتجاوز 25 %", "lien_manque_75": "نقص من 25 إلى 75 %",
        "lien_manque_100": "نقص يفوق 75 %",
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
    """Un paramètre dont l'absence se dit en clair, au lieu du « — » commun.

    `absent` : clé de `MOTS` de ce que dit la case — « aucun : maximum supprimé » par
    défaut. L'appelant répond du sens : dans un tableau dont la première colonne est la date
    de création du paramètre, une valeur absente est toujours une suppression ou un
    remplacement ; pour un plafond que la loi institue en cours de période, c'est l'absence
    de plafond avant sa création, et le paramètre ne doit alors jamais être clos.
    """

    def __init__(self, *args, absent: str = "supprime", **kwargs):
        super().__init__(*args, **kwargs)
        self.absent = absent

    def rendre(self, valeur, langue):
        return MOTS[langue][self.absent] if valeur is None else super().rendre(valeur, langue)


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


def parametre_penalite_taux():
    return ot.ParametreDate("taux_mensuel", f"{PENALITE}/taux_mensuel.yaml",
                            tous("penalite_taux"), format=pourcentage_nu,
                            lien=tous("penalite_taux_lien"))


def parametre_penalite_plafond():
    return ParametreSupprimable("plafond_part_principal",
                                f"{PENALITE}/plafond_part_principal.yaml",
                                tous("penalite_plafond"), format=pourcentage_nu,
                                lien=tous("penalite_plafond_lien"), absent="aucun_plafond")


def parametre_taxe(chemin: str, formateur: str):
    """Une feuille des chapitres V à VII ; le libellé de son lien porte le nom de la feuille."""
    feuille = chemin.rsplit("/", 1)[-1]
    return ot.ParametreDate(feuille, f"{chemin}.yaml", tous(f"lien_{feuille}"),
                            format=pourcentage_nu if formateur == "pourcentage" else entier_nu)


def parametre_parking_1997(population: str, feuille: str):
    return ParametreSupprimable(
        f"bareme_1997_{feuille}", f"{PARKINGS}/bareme_1997/{feuille}.yaml", tous(population),
        format=entier_nu, lien=tous("parkings_1997_lien", population=population),
        absent="bareme_remplace")


def parametre_parking_2003(manque: str, noeud: str, population: str, feuille: str):
    return ot.ParametreDate(
        f"bareme_2003_{noeud}_{feuille}", f"{PARKINGS}/bareme_2003/{noeud}/{feuille}.yaml",
        tous(population), format=entier_nu,
        lien=tous("parkings_2003_lien", manque=f"lien_{manque}", population=population))


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


def tableau_penalite(langue: str):
    m = MOTS[langue]
    lignes = [(p.libelle[langue], [p])
              for p in (parametre_penalite_taux(), parametre_penalite_plafond())]
    return tableau_cote_a_cote(lignes, [""], ANCRES_PENALITE, m["penalite"], "", langue,
                               dates_communes=False)


def tableau_parkings_1997(langue: str):
    m = MOTS[langue]
    lignes = [(m[population], [parametre_parking_1997(population, feuille)])
              for population, feuille in POPULATIONS_1997]
    return tableau_cote_a_cote(lignes, [m["contribution"]], ANCRES_PARKINGS_1997,
                               m["population"], m["unite_place"], langue)


def tableau_parkings_2003(langue: str):
    m = MOTS[langue]
    lignes = [(m[population], [parametre_parking_2003(manque, noeud, population, feuille)
                               for manque, noeud in MANQUES])
              for population, feuille in POPULATIONS_2003]
    return tableau_cote_a_cote(lignes, [m[manque] for manque, _noeud in MANQUES],
                               ANCRES_PARKINGS_2003, m["population"], m["unite_place"], langue)


def veille(date: str) -> str:
    """La veille d'une date d'effet (ISO) : le dernier jour où vaut l'état précédent."""
    import datetime

    return (datetime.date.fromisoformat(date) - datetime.timedelta(days=1)).isoformat()


def tableau_grandeurs_datees(grandeurs: tuple, ancres: dict[tuple[str, str], str], langue: str):
    """Des grandeurs sans dates communes, en long : une ligne par grandeur et par état.

    `grandeurs` : (chapitre, clé du prélèvement, clé de la grandeur, feuilles, formateur, clé
    de ce qui remplace la grandeur à sa clôture). Une grandeur à plusieurs feuilles — un
    minimum et un maximum — les rend dans une même case (« 10 à 30 ») ; ses feuilles doivent
    avoir les mêmes dates d'effet. `ancres` : (clé de la grandeur, date d'effet) -> ancre du
    registre du chapitre ; une date d'effet sans ancre arrête le générateur, et une ancre
    déclarée pour une date que le modèle ne porte pas aussi.

    La dernière colonne dit la période de chaque état : « depuis le … » pour l'état en
    vigueur ; « du … au … » pour un état que suit un autre, la date de fin étant la veille
    de la date d'effet suivante, en lien vers le texte qui y met fin. Une clôture — valeur
    vide — exige qu'on dise en clair ce qui remplace la grandeur.
    """
    import pandas as pd

    m = MOTS[langue]
    sortie, vues = [], set()
    for chapitre, prelevement, cle, feuilles, formateur, suite in grandeurs:
        parametres = [parametre_taxe(f, formateur) for f in feuilles]
        series = [p.serie() for p in parametres]
        if not all(series):
            print(f"✗ paramètre introuvable ou vide : {[p.chemin for p in parametres]}")
            return None
        dates = [d for d, *_ in series[0]]
        if any([d for d, *_ in s] != dates for s in series):
            raise ValueError(f"{cle} : les feuilles n'ont pas les mêmes dates d'effet")
        for p in parametres:
            ot.releve_note(p.chemin, p.lien[langue])
        for i, date in enumerate(dates):
            if (cle, date) not in ancres:
                raise ValueError(f"{cle} : date d'effet {date} sans ligne de registre")
            vues.add((cle, date))
            valeurs = [s[i][1] for s in series]
            if all(v is None for v in valeurs):
                if not i or not suite:
                    raise ValueError(f"{cle} : clôture au {date} sans mention de ce qui remplace")
                continue
            if any(v is None for v in valeurs):
                raise ValueError(f"{cle} : feuilles closes à des dates différentes ({date})")
            rendues = [p.rendre(v, langue) for p, v in zip(parametres, valeurs)]
            valeur = rendues[0] if len(rendues) == 1 else m["intervalle"].format(
                a=rendues[0], b=rendues[1])
            champs = dict(debut=ot.formate_date(date, langue), ancre=ancres[(cle, date)])
            if i + 1 == len(dates):
                periode = m["depuis"].format(**champs)
            else:
                suivante = dates[i + 1]
                if (cle, suivante) not in ancres:
                    raise ValueError(f"{cle} : date d'effet {suivante} sans ligne de registre")
                champs.update(fin=ot.formate_date(veille(suivante), langue),
                              ancre_fin=ancres[(cle, suivante)])
                close = all(s[i + 1][1] is None for s in series)
                periode = (m["du_au_remplace"].format(suite=m[suite], **champs) if close and suite
                           else m["du_au"].format(**champs))
            sortie.append({m["chapitre"]: chapitre, m["prelevement"]: m[prelevement],
                           m["grandeur"]: m[cle], m["valeur"]: valeur,
                           m["en_vigueur"]: periode})
    if vues != set(ancres):
        raise ValueError(f"ancres sans date d'effet : {sorted(set(ancres) - vues)}")
    return pd.DataFrame(sortie)


def tableau_taxes(langue: str):
    return tableau_grandeurs_datees(GRANDEURS_TAXES, ANCRES_TAXES, langue)


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
    parkings = ([parametre_parking_1997(population, feuille)
                 for population, feuille in POPULATIONS_1997]
                + [parametre_parking_2003(manque, noeud, population, feuille)
                   for manque, noeud in MANQUES for population, feuille in POPULATIONS_2003])
    return (ot.ecrire_serie_parametres(SERIE_PRIX, prix, CACHE)
            or ot.ecrire_serie_parametres(SERIE_TARIF, tarif, CACHE)
            or ot.ecrire_serie_parametres(SERIE_MINIMUM, minimum, CACHE)
            or ot.ecrire_serie_parametres(SERIE_MAXIMUM, [parametre_maximum()], CACHE)
            or ot.ecrire_serie_parametres(SERIE_PENALITE, [parametre_penalite_taux()], CACHE)
            or ot.ecrire_serie_parametres(SERIE_PARKINGS, parkings, CACHE))


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
            or ecrire_cote_a_cote("penalite_retard.md", tableau_penalite, ANCRES_PENALITE)
            or ecrire_cote_a_cote("taxes_baremes.md", tableau_taxes,
                                  {d: a for (_c, d), a in ANCRES_TAXES.items()})
            or ecrire_cote_a_cote("parkings_1997.md", tableau_parkings_1997,
                                  ANCRES_PARKINGS_1997)
            or ecrire_cote_a_cote("parkings_2003.md", tableau_parkings_2003,
                                  ANCRES_PARKINGS_2003)
            or ecrire_series())


if __name__ == "__main__":
    raise SystemExit(main())

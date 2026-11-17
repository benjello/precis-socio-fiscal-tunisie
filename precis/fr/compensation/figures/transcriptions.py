"""Transcriptions, valeur par valeur, des tableaux du volume *La compensation* devenus figures.

Ces cinq tableaux n'ont pas de série dans `tunisia-data`. Leurs valeurs sont recopiées ici telles
que les chapitres les imprimaient, avec, pour chacune, la clé de citation de sa source et sa
localisation (article, tableau, page). Les figures de `compensation.py` les lisent ; leur onglet
« Données » les rend au lecteur, et les clés sont déclarées dans l'onglet « Sources ».

    TAXE_UNIQUE          tbl-compensation-taxe-unique           (_carburants.qmd), 1964-1984
    RECETTES_CARBURANTS  tbl-compensation-carburants-recettes   (_carburants.qmd), 2012-2018
    IMPORT_CESSION       tbl-compensation-import-cession        (_carburants.qmd), 2016-2025
    LF_CAISSE            tbl-compensation-lf-caisse             (_institution.qmd), 1987-1994
    LF_CAISSE_2005       tbl-compensation-lf-caisse-2005        (_institution.qmd), 2005-2010

Rien n'est calculé ici, sauf ce que le tableau calculait lui-même (les écarts d'IMPORT_CESSION,
importation moins cession, dont `verifier()` contrôle l'égalité). Aucune valeur n'est ajoutée :
une case vide du tableau reste absente (ou `None`).
"""
from __future__ import annotations

# --- La taxe au profit de la Caisse, puis la taxe unique de compensation (D/hl) -------------
# (grandeur, date d'effet, dinars par hectolitre ou None = supprimée, texte, clé, localisation)
# Grandeurs : la taxe de 1964 (« t64_ ») jusqu'en 1970, la taxe unique de compensation (« tu_ »)
# depuis le 1er janvier 1971, qui réunit la taxe de 1964 et la redevance de 1957 : deux
# grandeurs distinctes, jamais reliées. En 1966, deux tarifs d'essence, un par qualité
# (« t64_essence » : essence supérieure ; « t64_essence_2 » : essence normale). Depuis le
# 1er janvier 1977, le gas-oil des travaux agricoles et de la pêche a son propre tarif
# (« tu_gasoil_agri »), « tu_gasoil » étant celui des autres utilisations.
TAXE_UNIQUE = [
    ("t64_essence", "1964-09-28", 1.050, "arrêté du 28 septembre 1964",
     "arrete-1964-09-28-prix-petroliers", "art. 1"),
    ("t64_lampant", "1964-09-28", 0.470, "arrêté du 28 septembre 1964",
     "arrete-1964-09-28-prix-petroliers", "art. 1"),
    ("t64_gasoil", "1964-09-28", 0.460, "arrêté du 28 septembre 1964",
     "arrete-1964-09-28-prix-petroliers", "art. 1"),
    ("t64_essence", "1966-01-01", 2.050, "arrêté du 31 décembre 1965",
     "arrete-1965-12-31-prix-petroliers", ""),
    ("t64_essence", "1966-09-25", 1.750, "arrêté du 23 septembre 1966",
     "arrete-1966-09-23-prix-petroliers", ""),
    ("t64_essence_2", "1966-09-25", 1.650, "arrêté du 23 septembre 1966",
     "arrete-1966-09-23-prix-petroliers", ""),
    ("t64_lampant", "1966-09-25", None, "arrêté du 23 septembre 1966",
     "arrete-1966-09-23-prix-petroliers", ""),
    ("t64_gasoil", "1966-09-25", None, "arrêté du 23 septembre 1966",
     "arrete-1966-09-23-prix-petroliers", ""),
    ("t64_essence", "1968-12-10", 2.500, "arrêté du 9 décembre 1968",
     "arrete-1968-12-09-prix-carburants", "art. 1 et 12, p. 1291-1292"),
    ("t64_essence_2", "1968-12-10", 2.300, "arrêté du 9 décembre 1968",
     "arrete-1968-12-09-prix-carburants", "art. 1 et 12, p. 1291-1292"),
    ("tu_essence", "1971-01-01", 1.378, "décret n° 70-622", "decret70-622", "art. 5"),
    ("tu_lampant", "1971-01-01", 0.036, "décret n° 70-622", "decret70-622", "art. 5"),
    ("tu_gasoil", "1971-01-01", 0.235, "décret n° 70-622", "decret70-622", "art. 5"),
    ("tu_essence", "1974-05-24", 6.150, "décret n° 74-576", "decret74-576", ""),
    ("tu_lampant", "1977-01-01", None, "décrets n° 76-1123 et 77-192",
     "decret76-1123 ; decret77-192", "art. 1 et 3, p. 3241 ; art. 1 (nouveau) et 2, p. 464"),
    ("tu_gasoil", "1977-01-01", 0.890, "décret n° 77-192", "decret77-192",
     "art. 1 (nouveau) et 2, p. 464"),
    ("tu_gasoil_agri", "1977-01-01", 0.235, "décret n° 77-192", "decret77-192",
     "art. 1 (nouveau) et 2, p. 464"),
    ("tu_essence", "1978-03-25", 7.120, "décret n° 78-316", "decret78-316", "p. 817"),
    ("tu_essence", "1981-01-01", 9.750, "décret n° 80-1641", "decret80-1641", ""),
    ("tu_gasoil", "1981-01-01", 2.180, "décret n° 80-1641", "decret80-1641", ""),
    ("tu_gasoil_agri", "1981-01-01", 1.525, "décret n° 80-1641", "decret80-1641", ""),
    ("tu_gasoil_agri", "1984-02-22", 0.025, "décret n° 84-210", "decret84-210",
     "art. 1 et 2, p. 535"),
]
# Dernière année tracée : les tarifs de l'essence et du gas-oil ordinaire postérieurs à 1981 ne
# sont pas établis. Le tarif de 1984 du gas-oil agricole est transcrit, mais pas tracé.
TAXE_UNIQUE_FIN = 1981

# --- Les recettes non fiscales en regard de la subvention des carburants (MD courants) ------
# (année, grandeur, horizon, millions de dinars, clé(s), localisation)
_BULLETINS = "minfin-resultats-provisoires-2017-01 ; minfin-resultats-provisoires-2018-07"
RECETTES_CARBURANTS = [
    (2012, "redevance_gazoduc", "encaissé", 210.5, _BULLETINS, ""),
    (2013, "redevance_gazoduc", "encaissé", 109.7, _BULLETINS, ""),
    (2014, "redevance_gazoduc", "encaissé", 121.5, _BULLETINS, ""),
    (2015, "revenus_commercialisation", "loi de finances complémentaire", 487.0, "lfc-2015",
     "tableau A"),
    (2015, "revenus_commercialisation", "encaissé", 150.0, _BULLETINS, ""),
    (2015, "redevance_gazoduc", "encaissé", 38.4, _BULLETINS, ""),
    (2016, "revenus_commercialisation", "encaissé", 0.0, _BULLETINS, ""),
    (2016, "redevance_gazoduc", "encaissé", 293.0, _BULLETINS, ""),
    (2017, "revenus_commercialisation", "loi de finances", 500.0, _BULLETINS, ""),
    (2017, "revenus_commercialisation", "loi de finances complémentaire", 615.0, _BULLETINS, ""),
    (2017, "revenus_commercialisation", "encaissé", 609.5, _BULLETINS, ""),
    (2017, "redevance_gazoduc", "encaissé", 555.1, _BULLETINS, ""),
    (2018, "revenus_commercialisation", "loi de finances", 401.5, _BULLETINS, ""),
    (2018, "revenus_commercialisation", "loi de finances complémentaire", 600.0,
     "minfin-note-execution-2018-12", ""),
    (2018, "revenus_commercialisation", "encaissé", 635.0, "minfin-note-execution-2018-12", ""),
    (2018, "redevance_gazoduc", "encaissé", 605.4, "minfin-note-execution-2018-12", ""),
]

# --- Prix moyen d'importation et prix de cession, 2016-2025 ----------------------------------
# (année, période couverte, essence : import, cession, écart ; gasoil ordinaire : import, cession,
#  écart ; bouteille de gaz de 13 kg : import, cession). Millimes par litre ; bouteille en dinars.
# Source de chaque ligne : Observatoire national de l'énergie et des mines, Conjoncture
# énergétique, numéro de décembre de l'année (pour 2024, données à fin novembre).
IMPORT_CESSION_CLE = "one-conjoncture-energetique"
IMPORT_CESSION = [
    (2016, "année", 768, 817, -49, 716, 769, -53, 11.559, 2.913),
    (2017, "année", 1048, 934, 114, 1023, 884, 139, 15.899, 3.060),
    (2018, "année", 1381, 1077, 304, 1414, 1051, 363, 18.027, 3.001),
    (2019, "année", 1416, 1138, 278, 1484, 1124, 360, 17.871, 2.882),
    (2020, "année", 916, 1004, -88, 963, 1027, -64, 15.46, 2.782),
    (2021, "année", 1510, 1149, 361, 1366, 1141, 225, 24.58, 2.782),
    (2022, "année", 2570, 1498, 1072, 2912, 1464, 1448, 33.40, 3.43),
    (2023, "année", 2131, 1498, 633, 2082, 1464, 618, 26.20, 3.43),
    (2024, "à fin novembre", 2039, 1498, 541, 1990, 1464, 526, 23.98, 3.43),
    (2025, "année", 1711, 1498, 213, 1765, 1464, 301, 24.52, 3.43),
]

# --- La Caisse dans les lois de finances initiales, 1987-1994 (MD courants, prévisions) ------
# (gestion, subvention du budget, recettes propres, total des recettes = dépenses, tableau,
#  clé, localisation, remarque)
LF_CAISSE = [
    (1987, 188.0, 1.0, 189.0, "L", "loi86-106-lf1987", "tableau L, p. 1677", ""),
    (1988, 188.0, 7.0, 195.0, "L", "loi-87-83-lf-1988", "tableau L, p. 1694",
     "recettes propres comprenant le solde reporté"),
    (1989, 188.0, 2.0, 190.0, "L", "loi88-145-lf1989", "tableau L, p. 1870",
     "premier chiffre des recettes propres rogné sur la page : déduites du total (190,0) et de la "
     "subvention (188,0)"),
    (1990, 300.0, 2.0, 302.0, "L", "loi-89-115-lf-1990", "tableau L, p. 2239", ""),
    (1991, 272.0, 13.0, 285.0, "K", "loi90-111-lf1991", "tableau K, p. 2163", ""),
    (1992, 255.0, 15.0, 270.0, "K", "loi91-98-lf1992", "tableau K, p. 2197", ""),
    (1993, 245.0, 37.0, 282.0, "K", "lf-1993", "tableau K, p. 1770", ""),
    (1994, 230.0, 28.0, 258.0, "K", "lf-1994", "tableau K, p. 2294", ""),
]

# --- La Caisse dans le tableau B des fonds spéciaux du Trésor, 2005-2010 (dinars courants) ---
# (gestion, recettes prévues du compte en dinars, clé, localisation)
LF_CAISSE_2005 = [
    (2005, 1_000_000, "lf-2005", "tableau B, p. 3450"),
    (2006, 2_000_000, "lf-2006", "tableau B, p. 3609"),
    (2007, 2_000_000, "lf-2007", "tableau B, p. 4400"),
    (2008, 100_000, "loi-2007-70-lf-2008", "tableau B, p. 4373"),
    (2009, 100_000, "lf-2009", "tableau B, p. 4285"),
    (2010, 100_000, "lf-2010", "tableau B, p. 3928"),
]


def cles(lignes, rang: int) -> list[str]:
    """Les clés de citation d'une transcription (colonne `rang`), dans l'ordre, sans doublon."""
    sortie: list[str] = []
    for ligne in lignes:
        for k in str(ligne[rang]).split(" ; "):
            if k and k not in sortie:
                sortie.append(k)
    return sortie


def verifier() -> None:
    """Contrôles internes : écarts égaux à importation moins cession ; totaux égaux à la somme
    de la subvention et des recettes propres."""
    for a, _p, ei, ec, ee, gi, gc, ge, _bi, _bc in IMPORT_CESSION:
        assert ei - ec == ee, (a, "essence")
        assert gi - gc == ge, (a, "gasoil")
    for g, sub, rp, tot, *_ in LF_CAISSE:
        assert abs(sub + rp - tot) < 1e-9, g


verifier()


# =============================================================================================
# Deuxième lot (validé le 17 novembre 2026) : tableaux des chapitres « La Caisse », « Les
# carburants », « Les rapports extérieurs » et « Les études d'impact ».
# =============================================================================================

# --- Le prélèvement à l'importation sur la poudre de lait, 1990-2015 -------------------------
# (grandeur, date de la marche, millimes par kg — soit dinars par tonne — ou None, décret, clé,
#  localisation). Aucun décret n'énonce sa date d'effet. Avant 1993, la marche est à la date
# d'effet calculée, un jour franc après la publication au Journal officiel (1990 : JORT n° 47 du
# 17 juillet, effet le 19 ; 1991 : n° 67 du 4 octobre, effet le 6). Ensuite, la date de dépôt au
# gouvernorat n'étant pas relevée, la marche est à la date de publication (1993 : n° 83 du
# 2 novembre ; 2002 : n° 84 du 15 octobre ; 2009 : n° 64 du 11 août ; 2015 : n° 8 du 27 janvier). None : le décret de 2002 fixe pour la poudre à 0 % « autre » un
# prélèvement variable, 4 450 dinars par tonne moins la somme du prix à l'importation (coût,
# assurance, fret) et des droits de douane. Grandeurs : « lait26 », poudre à 26 % de matière
# grasse ; « lait0 », poudre à 0 % — à partir de 2002, celle destinée aux nourrissons, aux
# malades ou à l'alimentation animale ; « lait0_autre », poudre à 0 % pour les autres usages.
LAIT = [
    ("lait26", "1990-07-19", 102, "décret n° 90-1194", "decret90-1194", "art. 1 et 2, p. 921"),
    ("lait0", "1990-07-19", 245, "décret n° 90-1194", "decret90-1194", "art. 1 et 2, p. 921"),
    ("lait26", "1991-10-06", 368, "décret n° 91-1391", "decret91-1391", "art. 2, p. 1670"),
    ("lait0", "1991-10-06", 735, "décret n° 91-1391", "decret91-1391", "art. 2, p. 1670"),
    ("lait0", "1993-11-02", 800, "décret n° 93-2116", "decret93-2116", "art. 1, p. 1857"),
    ("lait26", "1993-11-02", 680, "décret n° 93-2116", "decret93-2116", "art. 1, p. 1857"),
    ("lait26", "2002-10-15", 680, "décret n° 2002-2227", "decret2002-2227", "art. 1, p. 2413"),
    ("lait0", "2002-10-15", 800, "décret n° 2002-2227", "decret2002-2227", "art. 1, p. 2413"),
    ("lait0_autre", "2002-10-15", None, "décret n° 2002-2227", "decret2002-2227",
     "art. 1, p. 2413"),
    ("lait0_autre", "2009-08-11", 680, "décret n° 2009-2293", "decret2009-2293",
     "art. 1, p. 2284-2285"),
    ("lait26", "2015-01-27", 1500, "décret n° 2015-50", "decret2015-50", "art. 1, p. 247-248"),
    ("lait0_autre", "2015-01-27", 1500, "décret n° 2015-50", "decret2015-50",
     "art. 1, p. 247-248"),
]
LAIT_FIN = 2015  # aucun décret postérieur n'est lu : les traits s'arrêtent à la fin de 2015

# --- Le compte de la compensation avant 1975 (MD courants) -----------------------------------
# (année, grandeur regroupée, libellé de la source, millions de dinars, clé)
AVANT_1975 = [
    (1965, "subventions", "subventions d'exploitation versées par le compte des opérations de "
     "compensation, hydrocarbures compris", 1.2, "bct-ra-1965"),
    (1965, "versement_budget", "versement du même compte au budget de l'État", 0.8, "bct-ra-1965"),
    (1967, "droits_consommation", "droits de consommation sur les essences et les huiles versés "
     "au compte", 1.0, "bct-ra-1967"),
    (1967, "redevances_transports", "redevances sur les transports versées au compte", 0.45,
     "bct-ra-1967"),
    (1970, "depenses", "dépenses de la Caisse générale", 2.053, "bct-ra-1971"),
    (1971, "depenses", "dépenses de la Caisse générale", 3.7, "bct-ra-1971"),
    (1974, "recettes", "recettes de la Caisse", 18.4, "bct-ra-1975"),
    (1974, "contribution_budget", "contribution du budget de l'État à la Caisse, la première",
     5.3, "bct-ra-1974"),
    (1974, "depenses", "dépenses de la Caisse", 27.3, "bct-ra-1975"),
    (1975, "recettes", "recettes de la Caisse", 52.5, "bct-ra-1975"),
    (1975, "depenses", "dépenses de la Caisse", 49.2, "bct-ra-1975"),
]

# --- Les crédits d'interventions publiques du ministère chargé du commerce (MD courants) -----
# (libellé de la loi, année, crédit, dont interventions dans le domaine social, dotation
#  relayée par la BCT, clé, localisation)
LF_COMMERCE = [
    ("2000", 2000, 248.9, None, None, "lf-2000", "tableau B, p. 2756"),
    ("2001", 2001, 235.2, None, None, "lf-2001", "tableau B, p. 3187"),
    ("2002", 2002, 251.2, None, 235.0, "loi2001-123-lf2002", "tableau B, p. 4266"),
    ("2008 (loi de finances complémentaire)", 2008, 1064.4, None, None, "lfc-2008",
     "tableau C, p. 4172"),
    ("2009 (loi de finances complémentaire)", 2009, 833.5, None, None, "lfc-2009",
     "tableau C, p. 1830"),
    ("2011", 2011, 722.4, 700.0, None, "lf-2011", "tableau C, p. 3483 et p. 3718"),
]

# --- Du projet initial au projet révisé : la subvention des carburants en 2015 (MD) ----------
# (facteur, nature, millions de dinars) ; nature : « départ », « facteur », « arrivée », « écart »
LFC_2015_CLE, LFC_2015_LOC = "minfin-projet-lfc-2015", "§ 17 et 19"
LFC_2015 = [
    ("Loi de finances pour 2015", "départ", 1826),
    ("Prix du baril, de 95 à 62 dollars", "facteur", -2244),
    ("Cours du dollar, de 1,8 à 1,95 dinar", "facteur", 413),
    ("Programme d'ajustement des prix intérieurs non réalisé", "facteur", 356),
    ("Quantités importées", "facteur", 41),
    ("Séparation des opérations de commercialisation des hydrocarbures", "facteur", 894),
    ("Loi de finances complémentaire pour 2015", "arrivée", 1286),
    ("Écart", "écart", -540),
]

# --- La structure du prix des carburants (millimes par litre) -------------------------------
# Source : Observatoire national de l'énergie et des mines, Conjoncture énergétique.
STRUCTURE_CLE = "one-conjoncture-energetique"
# (date ISO, produit, prix de cession, droits et taxes, frais et marges, prix public)
STRUCTURE_SYNTHESE = [
    ("2020-04-07", "essence sans plomb", 1101, 738, 196, 2035),
    ("2020-04-07", "gasoil ordinaire", 1095, 295, 160, 1550),
    ("2020-04-07", "gasoil sans soufre", 1135, 504, 161, 1800),
    ("2021-04-20", "essence sans plomb", 1149, 747, 198, 2095),
    ("2021-04-20", "gasoil ordinaire", 1141, 301, 163, 1605),
    ("2021-04-20", "gasoil sans soufre", 1137, 504, 164, 1805),
    ("2022-04-14", "essence sans plomb", 1343, 785, 202, 2330),
    ("2022-04-14", "gasoil ordinaire", 1300, 323, 167, 1790),
    ("2022-04-14", "gasoil sans soufre", 1314, 528, 168, 2010),
    ("2022-11-24", "essence sans plomb", 1498, 815, 211, 2525),
    ("2022-11-24", "gasoil ordinaire", 1464, 345, 176, 1985),
    ("2022-11-24", "gasoil sans soufre", 1478, 550, 177, 2205),
]
# (libellé de la structure, produit, cession, droits, marges, public) ; None = tiret ou « … »
# de la source ; la ligne « inchangée » du 9 octobre 2020 est gardée, sans valeur.
_S = [
    ("31 mars 2019, décomposée en février 2020",
     (None, 744, 183, 2065), (None, 298, 148, 1570), (None, 508, 149, 1825)),
    ("7 avril 2020", (1101, 738, 196, 2035), (1095, 295, 160, 1550), (1135, 504, 161, 1800)),
    ("8 mai 2020", (None, 733, 192, 2005), (None, 293, 157, 1530), (None, 501, 158, 1775)),
    ("9 juin 2020", (None, 729, 192, 1975), (None, 291, 157, 1510), (None, 498, 158, 1750)),
    ("8 juillet 2020, selon le numéro de juillet",
     (None, 724, 192, 1945), (None, 288, 157, 1490), (None, 495, 158, 1725)),
    ("8 juillet 2020, selon le numéro d'août",
     (1004, 719, 192, 1915), (1027, 286, 157, 1470), (1049, 493, 158, 1700)),
    ("9 octobre 2020", "inchangée", "inchangé", (None, 490, 158, 1675)),
    ("10 novembre 2020", (1004, 719, 192, 1915), (1027, 286, 157, 1470),
     (1005, 487, 158, 1650)),
    ("6 février 2021", (1033, None, None, 1955), (1050, None, None, 1500),
     (1032, None, None, 1685)),
    ("11 mars 2021", (1067, 731, 197, 1995), (1076, 293, 162, 1530), (1063, 495, 162, 1720)),
    ("20 avril 2021", (1149, 747, 198, 2095), (1141, 301, 163, 1605), (1137, 504, 164, 1805)),
    ("1er février 2022", (1198, 757, 200, 2155), (1183, 307, 165, 1655),
     (1184, 511, 165, 1860)),
    ("1er mars 2022", (1251, 767, 201, 2220), (1226, 313, 166, 1705), (1231, 517, 167, 1915)),
    ("14 avril 2022", (1343, 785, 202, 2330), (1300, 323, 167, 1790), (1314, 528, 168, 2010)),
    ("18 septembre 2022", (1398, 796, 206, 2400), (1358, 330, 171, 1860),
     (1372, 536, 172, 2080)),
    ("24 novembre 2022", (1498, 815, 211, 2525), (1464, 345, 176, 1985),
     (1478, 550, 177, 2205)),
]
PRODUITS_STRUCTURE = ("essence sans plomb", "gasoil ordinaire", "gasoil sans soufre")
STRUCTURE_2020_2022 = []
for _lib, *_vals in _S:
    for _p, _v in zip(PRODUITS_STRUCTURE, _vals):
        if isinstance(_v, str):
            STRUCTURE_2020_2022.append((_lib, _p, None, None, None, None, _v))
        else:
            STRUCTURE_2020_2022.append((_lib, _p, *_v, ""))
# La bouteille de gaz de 13 kg (dinars) : (période, cession, droits, marges, public)
STRUCTURE_BOUTEILLE = [
    ("du 7 avril 2020 au 14 avril 2022", 2.782, 0.970, 3.948, 7.7),
    ("après le 14 avril 2022", 3.43, 1.11, 4.27, 8.80),
]

# --- La subvention unitaire prévisionnelle des budgets citoyens (millimes) ------------------
# (budget, produit, coût, prix payé, subvention unitaire, clé, localisation)
SUBVENTION_UNITAIRE = [
    (2021, "bouteille de gaz", 18500, 7700, 10800, "minfin-budget-citoyen-2021", "p. 3"),
    (2022, "essence, le litre", 3325, 2220, 1105, "minfin-budget-citoyen-2022", "p. 4"),
    (2022, "gasoil, le litre", 2754, 1705, 1049, "minfin-budget-citoyen-2022", "p. 4"),
    (2022, "gasoil sans soufre, le litre", 3071, 1915, 1156, "minfin-budget-citoyen-2022", "p. 4"),
    (2022, "bouteille de gaz", 41000, 7700, 33000, "minfin-budget-citoyen-2022", "p. 4"),
    (2023, "essence, le litre", 3396, 2525, 871, "minfin-budget-citoyen-2023", "p. 4"),
    (2023, "gasoil, le litre", 2820, 1985, 835, "minfin-budget-citoyen-2023", "p. 4"),
    (2023, "gasoil sans soufre, le litre", 3140, 2205, 935, "minfin-budget-citoyen-2023", "p. 4"),
    (2023, "bouteille de gaz", 42000, 8800, 33000, "minfin-budget-citoyen-2023", "p. 4"),
    (2024, "essence, le litre", 3055, 2525, 530, "minfin-budget-citoyen-2024", "p. 9"),
    (2024, "gasoil, le litre", 2511, 1985, 526, "minfin-budget-citoyen-2024", "p. 9"),
    (2024, "gasoil sans soufre, le litre", 2813, 2205, 608, "minfin-budget-citoyen-2024", "p. 9"),
    (2024, "bouteille de gaz", 36000, 8800, 27000, "minfin-budget-citoyen-2024", "p. 9"),
]

# --- Les subventions à l'énergie reconstituées en brut par le FMI, 2012-2016 (MD) ------------
FMI_ENERGIE_CLE, FMI_ENERGIE_LOC = "fmi-2016-cr16138", "tableau 4a"
FMI_ENERGIE = [(2012, 2689, "réalisé"), (2013, 4434, "réalisé"), (2014, 3112, "réalisé"),
               (2015, 918, "estimation"), (2016, 166, "projection")]

# --- Les études d'impact (dinars courants de l'année de leurs prix) ---------------------------
QUINTILES = ("1er", "2e", "3e", "4e", "5e")
# INS, CRES et BAD, 2010 : (grandeur, valeurs par quintile, None si non repris)
INCIDENCE_CLE, INCIDENCE_LOC = "ins-cres-bad-2013-subventions", "tableau 1"
INCIDENCE = [
    ("Subvention alimentaire annuelle par tête (D)", (68.2, 84.2, 87.5, 89.9, 89.1)),
    ("dont gros pain (D)", (20.6, None, None, None, 28.5)),
    ("dont semoule (D)", (17.0, None, None, None, 12.1)),
    ("Indice de ciblage absolu", (0.82, None, None, None, 1.07)),
]
# Banque mondiale 2013, part de chaque quintile dans les bénéfices directs (%)
BM2013_CLE = "bm-2013-82712"
BM2013_QUINTILES_LOC = "figures 11 et 12, p. 11-12"
BM2013_QUINTILES = [
    ("Électricité et gaz", (13, 17, 19, 22, 29)),
    ("Essence", (1, 3, 8, 20, 67)),
    ("Gaz de pétrole liquéfié", (15, 19, 21, 23, 22)),
    ("Gasoil", (2, 7, 13, 19, 59)),
    ("Pétrole lampant", (9, 11, 10, 29, 41)),
    ("Ensemble des subventions à l'énergie", (13, 16, 19, 23, 29)),
    ("Pour comparaison, selon la même note : subventions alimentaires", (16, 18, 20, 21, 25)),
]
# Banque mondiale 2013, bénéfice direct par tête et par an, prix d'avril 2013 (dinars)
BM2013_PAR_TETE_LOC = "figure 13, p. 13"
BM2013_PRODUITS = ("Gaz de pétrole liquéfié", "Électricité", "Essence", "Gasoil")
BM2013_PAR_TETE = [  # (quintile, GPL, électricité, essence, gasoil, ensemble)
    ("1er", 44, 17, 1, 0, 62), ("2e", 55, 22, 2, 1, 80), ("3e", 60, 26, 5, 1, 91),
    ("4e", 66, 30, 12, 2, 110), ("5e", 60, 39, 35, 4, 139), ("Moyenne", 56, 27, 9, 1, 94),
]
# Document de travail de 2015, subvention par unité, prix de mai 2014 (dinars)
WPS_CLE = "bm-2015-wps7312"
WPS_UNITAIRE_LOC = "tableau 3, p. 11"
WPS_UNITAIRE = [  # (produit ou tranche, prix non subventionné, prix de vente, subvention, taux %)
    ("Essence, le litre", 1.856, 1.670, 0.186, 10),
    ("Gasoil, le litre", 1.584, 1.250, 0.334, 21),
    ("Gaz de pétrole liquéfié, le kilogramme", 1.790, 0.570, 1.220, 68),
    ("Électricité, ménages jusqu'à 200 kWh par mois : jusqu'à 50 kWh", 0.268, 0.075, 0.193, 72),
    ("idem : jusqu'à 100 kWh", 0.268, 0.108, 0.160, 60),
    ("idem : jusqu'à 200 kWh", 0.268, 0.140, 0.128, 47),
    ("Électricité, ménages au-delà de 200 kWh : 1 à 200 kWh", 0.268, 0.151, 0.117, 43),
    ("idem : 201 à 300 kWh", 0.268, 0.184, 0.084, 31),
    ("idem : 301 à 500 kWh", 0.268, 0.280, -0.012, -4),
    ("idem : plus de 500 kWh", 0.268, 0.350, -0.082, -31),
]
# Document de travail de 2015, subvention reçue par tête et par an, prix de mai 2014 (dinars)
WPS_QUINTILES_LOC = "tableaux 7 et 8, p. 15"
WPS_PRODUITS = ("Essence", "Gasoil", "Gaz de pétrole liquéfié", "Électricité")
WPS_QUINTILES = [  # (quintile, essence, gasoil, GPL, électricité, total, part du total %)
    ("1er", 0.09, 0.15, 44.53, 36.99, 81.76, 14.9),
    ("2e", 0.43, 0.65, 55.33, 41.42, 97.82, 17.9),
    ("3e", 1.57, 1.24, 59.88, 46.06, 108.74, 19.9),
    ("4e", 4.65, 1.86, 68.30, 47.85, 122.67, 22.4),
    ("5e", 18.18, 5.70, 63.91, 48.89, 136.69, 25.0),
    ("Ensemble", 4.98, 1.92, 58.39, 44.24, 109.53, 100.0),
]


def _verifier_lot2() -> None:
    depart = LFC_2015[0][2]
    facteurs = sum(v for _l, n, v in LFC_2015 if n == "facteur")
    assert depart + facteurs == LFC_2015[6][2]
    assert LFC_2015[6][2] - depart == LFC_2015[7][2]
    # Pour la bouteille, les budgets de 2022 à 2024 arrondissent au dinar : pas d'égalité.
    for r in SUBVENTION_UNITAIRE:
        assert r[2] - r[3] == r[4] or r[1] == "bouteille de gaz", r
    for r in WPS_UNITAIRE:
        assert abs(r[1] - r[2] - r[3]) < 1e-9, r


_verifier_lot2()

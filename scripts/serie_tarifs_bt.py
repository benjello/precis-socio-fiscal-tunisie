"""Série « tarif de l'électricité des ménages en basse tension, 1970-2022 » du volume « La compensation ».

    uv run python scripts/serie_tarifs_bt.py ecrire     # écrit precis/_seriescache/<série>.csv
    uv run python scripts/serie_tarifs_bt.py verifier   # compare le CSV aux tableaux du chapitre

La série est une transcription, valeur par valeur, des tableaux du chapitre « L'électricité et le
gaz » : `tbl-compensation-eg-grilles-jo` (1970-1992), `-grilles-relais` (1994-2003),
`-grilles-exterieures` (1993 et 2001), `-grilles-steg` (2004-2022) et, pour le seul tarif du
1er juillet 2005, `-ajustements-1992-2006`. La figure `tarifs_bt` de `figures/electricite.py` la
lit par `figtools.series()`. `verifier` compare le CSV aux tableaux, ligne par ligne : pour chaque
date d'effet, les prix d'un tableau (seuils de consommation retirés) et ceux du CSV forment le même
ensemble de valeurs.

Une ligne par tranche et par date d'effet. Colonnes propres :

  - `tranche`    : la tranche, dans la structure de la grille (voir `NOMS`) ;
  - `structure`  : la structure du tarif ; une courbe ne traverse jamais un changement de
                   structure — 1975, 1978, 1981, 1984, 2006, 2014, 2018, 2022 ;
  - `famille_source` : `officielle` (Journal officiel, STEG), `relais officiel` (agence publique
                   tunisienne qui reproduit la grille) ou `extérieure` (ESMAP, Banque africaine de
                   développement). Les familles ne sont pas confondues : la figure leur donne une
                   marque chacune.

Prix taxes comprises jusqu'en 1987, hors taxe sur la valeur ajoutée à partir du 1er janvier 1991
(colonne `unite`, rupture marquée). Les GRILLES NON ÉTABLIES (`etat = grille_non_etablie`) sont des
dates où le chapitre établit un relèvement sans en donner la grille : le niveau précédent s'y
arrête, aucune valeur n'est reconstituée (`NON_ETABLIES`, avec la pièce qui les date). Le prix
unique de l'éclairage du 30 novembre 1978 n'est pas établi : c'est une ligne sans valeur. Le tarif
de la force motrice de 1978 (46 et 42), qui n'est pas celui des ménages, n'est pas repris.
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from serie_tarifs_mt import _date, _nombre, lire_tableau  # noqa: E402

RACINE = Path(__file__).resolve().parents[1]
SERIE = "steg-tarifs-basse-tension"
CSV = RACINE / "precis" / "_seriescache" / f"{SERIE}.csv"

CHAMPS = ["tranche", "structure", "date_effet", "jour_etabli", "valeur", "unite", "etat",
          "famille_source", "portee", "source", "page", "tableau", "rupture", "remarque"]
TTC = "millimes courants par kWh, taxes comprises"
HT = "millimes courants par kWh, hors taxes"

NOMS = {
    "degressif_1": "tarif dégressif, première tranche",
    "degressif_2": "tarif dégressif, deuxième tranche",
    "degressif_3": "tarif dégressif, troisième tranche",
    "degressif_4": "tarif dégressif, dernière tranche",
    "degressif_kva_1": "tarif dégressif, jusqu'à 10 kWh par mois et par kVA",
    "degressif_kva_2": "tarif dégressif, au-delà de 10 kWh par mois et par kVA",
    "eclairage_unique": "éclairage, prix unique",
    "prix_unique": "tarif général unique",
    "economique": "tranche économique, jusqu'à 50 kWh par mois",
    "normale": "tranche normale",
    "petits_51_a": "petits abonnés, au-delà de 50 kWh : premier prix",
    "petits_51_b": "petits abonnés, au-delà de 50 kWh : second prix",
    "autres_1_300": "autres abonnés, de 1 à 300 kWh",
    "autres_301": "autres abonnés, 301 kWh et plus",
    "t_51_100": "de 51 à 100 kWh",
    "t_101_200_unique": "de 101 à 200 kWh, prix unique sur toute la consommation",
    "fort_1_200": "forte consommation, de 1 à 200 kWh",
    "fort_201_300": "forte consommation, de 201 à 300 kWh",
    "fort_301_500": "forte consommation, de 301 à 500 kWh",
    "fort_501": "forte consommation, plus de 500 kWh",
}

STRUCTURES = {
    "1970": "dégressif selon les heures d'utilisation mensuelle",
    "1975": "dégressif par kVA souscrit",
    "1978": "prix unique de l'éclairage",
    "1981": "tarif général unique",
    "1984": "tranche économique et tranche normale",
    "2006": "tranche économique, petits abonnés et autres abonnés (seconde tranche à partir de 301 kWh)",
    "2014": "six tranches, prix unique en deçà de 200 kWh par mois",
    "2018": "seuil du prix unique ramené à 100 kWh par mois",
    "2022": "toute la consommation au prix de la tranche atteinte",
}
RUPTURES = {
    "1975-04-20": "Le tarif dégressif est désormais fixé par kVA souscrit : les tranches de 1970 et de 1975 ne s'alignent pas",
    "1978-11-30": "Prix unique de l'éclairage, dont le niveau n'est pas établi",
    "1981-08-31": "Éclairage et force motrice réunis en un tarif général unique",
    "1984-05-31": "Réforme de 1984 : le prix unique devient une tranche économique et une tranche normale",
    "1991-01-01": ("Prix taxes comprises jusqu'en 1987, hors taxe sur la valeur ajoutée à partir du "
                   "1er janvier 1991 : les niveaux ne se comparent pas de part et d'autre"),
    "2006-01-01": "Étape de la réforme de 1984 : la tranche normale se scinde, seconde tranche à partir de 301 kWh",
    "2014-05-01": "Réforme de 2014 : six tranches, prix unique sur toute la consommation en deçà de 200 kWh par mois",
    "2018-09-01": "Étape de la réforme de 2014 : seuil du prix unique ramené de 200 à 100 kWh par mois",
    "2022-05-01": "Étape de la réforme de 2014 : toute la consommation au prix de la tranche atteinte",
}

OFF, REL, EXT = "officielle", "relais officiel", "extérieure"
JO, RELAIS, EXTER, STEG, AJUST = ("tbl-compensation-eg-grilles-jo", "tbl-compensation-eg-grilles-relais",
                                  "tbl-compensation-eg-grilles-exterieures",
                                  "tbl-compensation-eg-grilles-steg",
                                  "tbl-compensation-eg-ajustements-1992-2006")

# (date, jour établi, structure, famille, source, page, tableau, portée, {tranche: valeur}, remarque)
GRILLES = [
    ("1970-01-01", "oui", "1970", OFF, "arrete-1970-08-07-tarifs-electricite-gaz", "", JO, "mise en place",
     dict(degressif_1=45, degressif_2=38, degressif_3=30, degressif_4=25), ""),
    ("1975-04-20", "oui", "1975", OFF, "arrete-1975-04-15-tarifs-electricite-gaz", "", JO, "ajustement",
     dict(degressif_kva_1=45, degressif_kva_2=35), ""),
    ("1978-11-30", "oui", "1978", OFF, "arrete-1978-11-27-tarifs-electricite-gaz", "", JO,
     "ajustement de structure", dict(eclairage_unique=None),
     "Le prix unique de l'éclairage n'est pas établi ; le tarif de la force motrice (46 et 42) n'est "
     "pas celui des ménages."),
    ("1981-08-31", "oui", "1981", OFF, "arrete-1981-09-01-tarifs-electricite-gaz", "", JO,
     "ajustement de structure", dict(prix_unique=58), ""),
    ("1982-09-29", "oui", "1981", OFF, "arrete-1982-09-30-tarifs-electricite-gaz", "", JO, "ajustement",
     dict(prix_unique=61), ""),
    ("1984-05-31", "oui", "1984", OFF, "arrete-1984-06-04-tarifs-electricite-gaz", "", JO, "rupture",
     dict(economique=61, normale=70), ""),
    ("1987-06-16", "oui", "1984", OFF, "arrete-1987-06-08-tarifs-electricite-gaz", "", JO, "ajustement",
     dict(economique=59, normale=72), ""),
    ("1991-01-01", "oui", "1984", OFF, "arrete-1990-12-19-tarifs-electricite-gaz", "", JO, "étape",
     dict(economique=57, normale=70), ""),
    ("1992-08-01", "oui", "1984", OFF, "decision-1992-08-11-tarifs-electricite-gaz", "", JO,
     "rupture (application)", dict(economique=59, normale=76), ""),
    ("1993-10-01", "non", "1984", EXT, "esmap-2005-307-electrification-rurale", "tableau 6.3, p. 37", EXTER,
     "ajustement", dict(economique=59, normale=79),
     "Tableau annuel de l'ESMAP rattaché à la grille d'octobre 1993 ; le mois vient de la Banque "
     "mondiale et de la Banque centrale."),
    ("1994-06-01", "non", "1984", REL, "fipa-2001-02-electricite-eng ; fipa-1999-production", "", RELAIS,
     "ajustement", dict(economique=61, normale=83),
     "Le mois vient de deux rapports extérieurs ; la grille ne change pas de 1994 à août 2000."),
    ("2000-08-15", "oui", "1984", REL, "api-2003-04-couts-energie ; fipa-2001-05-electricite", "", RELAIS,
     "ajustement", dict(economique=62, normale=87),
     "La date d'effet vient de la Banque africaine de développement."),
    ("2001-08-01", "oui", "1984", EXT, "esmap-2005-307-electrification-rurale", "tableau 6.2, p. 36", EXTER,
     "ajustement", dict(economique=63, normale=90),
     "Tableau de l'ESMAP rattaché à la date que donne la Banque africaine de développement."),
    ("2003-04-01", "oui", "1984", REL, "fipa-2003-08-electricite-avril-2003", "", RELAIS, "ajustement",
     dict(economique=65, normale=94),
     "Une page de la STEG, non datée et archivée en janvier 2004, donne 90 pour la tranche normale."),
    ("2004-05-01", "oui", "1984", OFF, "steg-grille-2004-05-01", "", STEG, "ajustement",
     dict(economique=65, normale=99), ""),
    ("2005-02-01", "oui", "1984", OFF, "steg-grille-2005-02-01", "", STEG, "ajustement",
     dict(economique=66, normale=103), ""),
    ("2005-07-01", "oui", "1984", EXT, "bad-2006-rap-electricite-vi", "", AJUST, "ajustement",
     dict(economique=70, normale=108), "Tarif connu par un rapport extérieur seul."),
    ("2006-01-01", "oui", "2006", OFF, "steg-grille-2006-01-01", "", STEG, "étape",
     dict(economique=68, petits_51_a=75, petits_51_b=114, autres_1_300=114, autres_301=127), ""),
    ("2008-09-01", "oui", "2006", OFF, "steg-grille-2008-09-01", "", STEG, "ajustement",
     dict(economique=74, petits_51_a=90, petits_51_b=131, autres_1_300=131, autres_301=174), ""),
    ("2010-06-01", "oui", "2006", OFF, "steg-grille-2010-06-01", "", STEG, "ajustement",
     dict(economique=75, petits_51_a=92, petits_51_b=133, autres_1_300=133, autres_301=186),
     "Le rapport annuel de la STEG écrit qu'il n'y a pas eu d'ajustement tarifaire en 2010."),
    ("2012-09-01", "oui", "2006", OFF, "steg-grille-2012-09-01", "", STEG, "ajustement",
     dict(economique=75, petits_51_a=92, petits_51_b=135, autres_1_300=135, autres_301=200), ""),
    ("2014-05-01", "oui", "2014", OFF, "steg-grille-2014-05-01", "", STEG, "rupture",
     dict(economique=75, t_51_100=108, t_101_200_unique=140, fort_1_200=151, fort_201_300=184,
          fort_301_500=280, fort_501=350), ""),
    ("2017-01-01", "oui", "2014", OFF, "steg-grille-2017-01-01", "", STEG, "ajustement",
     dict(economique=75, t_51_100=108, t_101_200_unique=162, fort_1_200=167, fort_201_300=198,
          fort_301_500=285, fort_501=350), ""),
    ("2018-09-01", "oui", "2018", OFF, "steg-grille-2018-09-01", "", STEG, "étape",
     dict(economique=75, t_51_100=108, fort_1_200=176, fort_201_300=218, fort_301_500=295,
          fort_501=355), ""),
    ("2019-06-01", "oui", "2018", OFF, "steg-grille-2019-06-01", "", STEG, "ajustement",
     dict(economique=62, t_51_100=96, fort_1_200=176, fort_201_300=218, fort_301_500=341,
          fort_501=414), ""),
    ("2022-05-01", "oui", "2022", OFF, "steg-grille-2022-05-01", "", STEG, "étape",
     dict(economique=62, t_51_100=96, fort_1_200=176, fort_201_300=218, fort_301_500=341,
          fort_501=414),
     "À partir de cette grille, toute la consommation est facturée au prix de la tranche atteinte : "
     "« forte consommation, de 1 à 200 kWh » est la tranche de 101 à 200 kWh."),
]

# Dates où le chapitre établit un relèvement sans donner la grille des ménages : (date, pièce, remarque).
NON_ETABLIES = [
    ("2007-07-01", "steg-ra-2007", "+6 % sur l'électricité et le gaz (tbl-compensation-eg-ajustements)."),
    ("2007-12-01", "steg-ra-2007", "+6,9 % sur l'électricité (tbl-compensation-eg-ajustements)."),
    ("2008-04-01", "steg-ra-2008", "+7,76 % sur l'électricité (tbl-compensation-eg-ajustements)."),
    ("2014-01-01", "minfin-compensation-carburants-2014",
     "Le rapport de contrôle de 2014 date une hausse du 1er janvier 2014 (p. 75) ; la grille de la "
     "basse tension à cette date n'est pas établie."),
]


def lignes() -> list[dict]:
    sortie = []
    for date, etabli, structure, famille, source, page, tableau, portee, valeurs, remarque in GRILLES:
        unite = TTC if date < "1991-01-01" else HT
        premiere = True
        for tranche, v in valeurs.items():
            sortie.append(dict(
                tranche=tranche, structure=STRUCTURES[structure], date_effet=date, jour_etabli=etabli,
                valeur="" if v is None else v, unite=unite, etat="lu" if v is not None else "non_etabli",
                famille_source=famille, portee=portee, source=source, page=page, tableau=tableau,
                rupture=RUPTURES.get(date, "") if premiere else "", remarque=remarque))
            premiere = False
    for date, source, remarque in NON_ETABLIES:
        sortie.append(dict(
            tranche="grille_non_etablie", structure="", date_effet=date, jour_etabli="oui", valeur="",
            unite="", etat="grille_non_etablie", famille_source=OFF, portee="ajustement", source=source,
            page="", tableau="", rupture="", remarque=remarque))
    return sorted(sortie, key=lambda r: (r["date_effet"], r["tranche"] == "grille_non_etablie"))


def ecrire() -> None:
    CSV.parent.mkdir(parents=True, exist_ok=True)
    with CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CHAMPS, lineterminator="\n")
        w.writeheader()
        w.writerows(lignes())
    print(f"écrit {CSV.relative_to(RACINE)} : {len(lignes())} lignes")


# --- la comparaison au texte des tableaux --------------------------------------------------------

SEUILS = re.compile(r"\d+\s*-\s*\d+|\d+ et plus|au-delà de \d+|plus de \d+|jusqu'à \d+|en deçà de \d+")


def _prix(cellule: str) -> list:
    """Les prix d'une cellule, seuils de consommation retirés."""
    texte = SEUILS.sub(" ", cellule.replace("**", ""))
    return [_nombre(n) for n in re.findall(r"\d+(?:,\d+)?", texte)]


def attendu() -> dict[str, Counter]:
    """{date: multiensemble des prix} lu dans les tableaux."""
    a: dict[str, Counter] = {}
    for r in lire_tableau(JO):
        cell = r[3]
        a[_date(r[0])] = Counter() if cell.startswith("force motrice") else Counter(_prix(cell))
    for tableau in (RELAIS, EXTER):
        for r in lire_tableau(tableau):
            a[_date(r[0])] = Counter([_nombre(r[2]), _nombre(r[3])])
    for r in lire_tableau(STEG):
        a[_date(r[0])] = Counter([_nombre(r[2])] + _prix(r[3]))
    for r in lire_tableau(AJUST):
        if r[0].replace("^er^", "").strip() == "1 juillet 2005":
            a["2005-07-01"] = Counter(_prix(r[2]))
    return a


def verifier() -> list[str]:
    attendus = attendu()
    with CSV.open(encoding="utf-8") as f:
        lus = list(csv.DictReader(f))
    non_etablies = {d for d, *_ in NON_ETABLIES}
    dans_csv: dict[str, Counter] = {}
    for r in lus:
        if r["etat"] == "grille_non_etablie":
            if r["date_effet"] not in non_etablies or r["valeur"] != "" or not r["source"]:
                return [f"grille non établie hors liste ou mal formée : {r['date_effet']}"]
            continue
        c = dans_csv.setdefault(r["date_effet"], Counter())
        if r["valeur"] != "":
            c[_nombre(r["valeur"])] += 1
    ecarts = []
    for date in sorted(set(attendus) | set(dans_csv)):
        if attendus.get(date) != dans_csv.get(date):
            ecarts.append(f"{date} : tableaux {dict(attendus.get(date, {}))}, "
                          f"CSV {dict(dans_csv.get(date, {}))}")
    return ecarts


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "verifier"
    if action == "ecrire":
        ecrire()
    else:
        ecarts = verifier()
        for e in ecarts:
            print(e)
        print(f"{len(attendu())} dates comparées, {len(ecarts)} écart(s)")
        sys.exit(1 if ecarts else 0)

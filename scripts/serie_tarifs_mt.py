"""Série « tarifs de l'électricité en moyenne tension, 1975-2022 » du volume « La compensation ».

    uv run python scripts/serie_tarifs_mt.py ecrire     # écrit precis/_seriescache/<série>.csv
    uv run python scripts/serie_tarifs_mt.py verifier   # compare le CSV aux trois tableaux du chapitre

La série est une transcription, valeur par valeur, des quatre tableaux du chapitre
« L'électricité et le gaz » (`tbl-compensation-eg-mt-jo`, `-mt-1994`, `-mt-2004` et `-mt-2014`),
eux-mêmes sourcés grille par grille. La figure `tarifs_mt` de `figures/electricite.py` la lit par
`figtools.series()` ; elle ne lit jamais le tableau Markdown. `verifier` compare le CSV au texte
des tableaux, dans les deux sens : chaque valeur d'un tableau est dans le CSV, chaque valeur du CSV
est dans un tableau (une case vide d'un tableau est une ligne sans valeur du CSV).

Une ligne par tarif, poste et date d'effet. Les familles ne se raccordent pas :

  - `trois_postes`    : jour, pointe, nuit (grilles du Journal officiel, 1975-1992, et grille de
                        juin 1994, en vigueur jusqu'en août 2000) ;
  - `quatre_postes`   : jour, pointe, soir, nuit (du 15 août 2000 au 1er mai 2014 exclu) ;
  - `quatre_postes_2014` : jour, pointe du matin en été, pointe du soir, nuit (depuis le 1er mai 2014) ;
  - `uniforme`        : le prix unique du tarif uniforme, défini de la même façon sur toute la période.

Le passage de trois à quatre postes a lieu entre la grille de juin 1994 et celle du 15 août 2000 ;
le jour n'est pas établi. Le passage aux quatre postes redéfinis a lieu le 1er mai 2014.

Deux sortes de lignes ne viennent pas des tableaux de valeurs :

  - la rupture fiscale du 1er janvier 1991 (colonne `rupture`) : prix taxes comprises jusqu'en 1987,
    hors taxe sur la valeur ajoutée à partir de 1991 ; l'unité de chaque ligne le dit ;
  - les GRILLES NON ÉTABLIES (`etat = grille_non_etablie`, `poste = grille_non_etablie`, sans
    valeur) : une date où le chapitre établit un relèvement des tarifs sans en donner la grille de
    la moyenne tension. Le niveau précédent s'arrête à cette date ; aucune valeur n'est reconstituée
    jusqu'à la grille suivante. Leur liste est `NON_ETABLIES`, chacune avec la pièce du chapitre
    qui la date ; `verifier` les met à part.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
SERIE = "steg-tarifs-moyenne-tension"
CSV = RACINE / "precis" / "_seriescache" / f"{SERIE}.csv"
QMD = RACINE / "precis" / "fr" / "compensation" / "_electricite_gaz.qmd"
TABLEAUX = ("tbl-compensation-eg-mt-1994", "tbl-compensation-eg-mt-2004",
            "tbl-compensation-eg-mt-2014")

CHAMPS = ["tarif", "famille", "poste", "date_effet", "jour_etabli", "valeur", "unite", "etat",
          "portee", "source", "page", "rupture", "rupture_annee", "remarque"]
KWH = "millimes courants par kWh, hors taxes"
KWH_TTC = "millimes courants par kWh, taxes comprises"
KW = "millimes par kW et par mois"
KVA = "millimes par kVA et par mois"

RUPTURE_1994_2000 = ("De trois à quatre postes horaires : la grille de juin 1994 compte trois postes, "
                     "celle du 15 août 2000 quatre ; le jour du changement n'est pas établi")
RUPTURE_1991 = ("Prix taxes comprises jusqu'en 1987, hors taxe sur la valeur ajoutée à partir du 1er "
                "janvier 1991 : les niveaux ne se comparent pas de part et d'autre")
RUPTURE_2014 = ("Quatre postes redéfinis le 1er mai 2014 (réforme de 2014) : les postes d'avant et "
                "d'après ne s'alignent pas")

# --- la transcription ---------------------------------------------------------------------------
# (date d'effet, jour établi, portée, source, page, famille, valeurs par tarif)
# Tarif à postes horaires : (jour, pointe, soir, nuit, prime) ; None = case vide du tableau.
# Tarif uniforme : (prix, prime) ; secours : (jour, pointe, soir, nuit, prime).

PRIME_JO = "millimes par kW et par mois (unité à vérifier sur les textes de 1975 à 1982)"
PREMIERE_TRANSCRIPTION = ("Valeur d'une première transcription de l'arrêté ; seule la grille de 1992 "
                          "est établie deux fois sur le texte.")

GRILLES_JO = [
    dict(date="1975-04-20", etabli="oui", portee="mise en place", source="arrete-1975-04-15-tarifs-electricite-gaz",
         postes=(11.3, 18.4, None, 4.1, 1500), uniforme_tranches=(20.4, 15.3), ttc=True, prime_unite=PRIME_JO),
    dict(date="1978-11-30", etabli="oui", portee="ajustement", source="arrete-1978-11-27-tarifs-electricite-gaz",
         postes=(18, 30, None, 9, 1500), uniforme_tranches=(30, 26), ttc=True, prime_unite=PRIME_JO),
    dict(date="1981-08-31", etabli="oui", portee="ajustement", source="arrete-1981-09-01-tarifs-electricite-gaz",
         postes=(31, 47, None, 22, 1500), uniforme=(41, None), ttc=True, prime_unite=PRIME_JO),
    dict(date="1982-09-29", etabli="oui", portee="ajustement", source="arrete-1982-09-30-tarifs-electricite-gaz",
         postes=(35, 56, None, 26, 2000), uniforme=(46, None), ttc=True, prime_unite=PRIME_JO),
    dict(date="1984-05-31", etabli="oui", portee="ajustement", source="arrete-1984-06-04-tarifs-electricite-gaz",
         postes=(39, 68, None, 29, 2000), uniforme=(51, None), ttc=True),
    dict(date="1987-06-16", etabli="oui", portee="ajustement", source="arrete-1987-06-08-tarifs-electricite-gaz",
         postes=(42, 77, None, 30, 2000), uniforme=(54, None), ttc=True),
    dict(date="1991-01-01", etabli="oui", portee="ajustement", source="arrete-1990-12-19-tarifs-electricite-gaz",
         postes=(40, 80, None, 29, 2000), uniforme=(52, None), rupture=RUPTURE_1991),
    dict(date="1992-08-01", etabli="oui", portee="ajustement", source="decision-1992-08-11-tarifs-electricite-gaz",
         postes=(40, 84, None, 29, 2500), uniforme=(56, None), transcription_unique=False),
]
for _g in GRILLES_JO:
    _g.update(famille="trois_postes", page="", secours=None)
    _g.setdefault("remarque", PREMIERE_TRANSCRIPTION if _g.pop("transcription_unique", True) else "")

# Dates où le chapitre établit un relèvement des tarifs de la moyenne tension, ou de tous les
# tarifs, sans que la grille de la moyenne tension soit établie : (date, jour établi, pièce).
NON_ETABLIES = [
    ("1981-01-31", "oui", "arrete-1981-01-23-tarifs-electricite",
     "Haute et moyenne tension relevées le 31 janvier 1981 (tbl-compensation-eg-textes-1961-1982) ; "
     "la grille n'est pas reprise au tableau de la moyenne tension."),
    ("1993-10-01", "non", "bm-1998-icr-17374",
     "Ajustement d'octobre 1993, +3 % en moyenne de tous les tarifs selon la Banque mondiale "
     "(tbl-compensation-eg-ajustements-1992-2006) ; grille de la moyenne tension non établie."),
    ("2005-02-01", "oui", "bad-2006-rap-electricite-vi",
     "La Banque africaine de développement liste les barèmes successifs et compte sept ajustements "
     "de 2000 au 1er janvier 2006 ; la grille de la basse tension change le 1er février 2005 "
     "(tbl-compensation-eg-grilles-steg) ; grille de la moyenne tension à cette date non établie."),
    ("2005-07-01", "oui", "bad-2006-rap-electricite-vi",
     "Tarif du 1er juillet 2005, donné pour la basse tension par la Banque africaine de "
     "développement (tbl-compensation-eg-ajustements-1992-2006) ; grille de la moyenne tension non établie."),
    ("2007-07-01", "oui", "steg-ra-2007",
     "+6 % sur l'électricité et le gaz (tbl-compensation-eg-ajustements) ; grille non établie."),
    ("2007-12-01", "oui", "steg-ra-2007",
     "+6,9 % sur l'électricité (tbl-compensation-eg-ajustements) ; grille non établie."),
    ("2008-04-01", "oui", "steg-ra-2008",
     "+7,76 % sur l'électricité (tbl-compensation-eg-ajustements) ; grille non établie."),
    ("2014-01-01", "oui", "minfin-compensation-carburants-2014",
     "Le rapport de contrôle de 2014 date une hausse du 1er janvier 2014 (p. 75, "
     "tbl-compensation-eg-ajustements) ; grille non établie."),
]

GRILLES = GRILLES_JO + [
    dict(date="1994-06-01", etabli="non", portee="ajustement", famille="trois_postes",
         source="fipa-2001-02-electricite-eng ; fipa-1999-production",
         source_autres="fipa-2001-02-electricite-eng", page="",
         postes=(47, 92, None, 30, 3000), uniforme=(60, 300), secours=(58, 98, None, 31, 1500),
         remarque="Le mois vient de la Banque mondiale ; la page de la FIPA porte « au 28 février 1999 »."),
    dict(date="2000-08-15", etabli="oui", portee="ajustement", famille="quatre_postes",
         source="fipa-2001-05-electricite ; api-2003-04-couts-energie", page="",
         postes=(49, 93, 71, 31, 3000), uniforme=(64, 300), secours=(62, 101, 78, 34, 1500),
         rupture=RUPTURE_1994_2000, remarque=""),
    dict(date="2001-08-01", etabli="oui", portee="ajustement", famille="quatre_postes",
         source="esmap-2005-307-electrification-rurale", page="tableau 6.2, p. 36",
         postes=(50, 94, None, None, 3000), uniforme=(65, 300), secours=(63, 102, None, None, 1500),
         remarque="Le tableau de l'ESMAP ne donne ni le soir ni la nuit."),
    dict(date="2003-04-01", etabli="oui", portee="ajustement", famille="quatre_postes",
         source="fipa-2003-08-electricite-avril-2003", page="",
         postes=(54, 97, 76, 37, 3000), uniforme=(69, 300), secours=(65, 105, 83, 40, 1500),
         remarque=""),
    dict(date="2004-05-01", etabli="oui", portee="ajustement de structure", famille="quatre_postes",
         source="steg-grille-2004-05-01", page="", postes=(58, 102, 80, 40, 3000),
         uniforme=(73, None), secours=None, remarque=""),
    dict(date="2006-01-01", etabli="oui", portee="ajustement", famille="quatre_postes",
         source="steg-grille-2006-01-01", page="", postes=(66, 112, 95, 48, 3500),
         uniforme=(84, None), secours=None, remarque=""),
    dict(date="2008-09-01", etabli="oui", portee="ajustement", famille="quatre_postes",
         source="steg-grille-2008-09-01", page="", postes=(96, 153, 122, 76, 3500),
         uniforme=(115, None), secours=None, remarque=""),
    dict(date="2010-06-01", etabli="oui", portee="ajustement", famille="quatre_postes",
         source="steg-grille-2010-06-01", page="", postes=(110, 168, 133, 85, 3500),
         uniforme=(125, None), secours=None, remarque=""),
    dict(date="2012-09-01", etabli="oui", portee="ajustement", famille="quatre_postes",
         source="steg-grille-2012-09-01", page="", postes=(123, 185, 147, 94, 4000),
         uniforme=(137, None), secours=None, remarque=""),
    dict(date="2013-03-01", etabli="oui", portee="ajustement", famille="quatre_postes",
         source="steg-grille-2013-03-01", page="", postes=(132, 197, 154, 100, 5000),
         uniforme=(143, None), secours=None, remarque=""),
    dict(date="2014-05-01", etabli="oui", portee="étape (de la réforme de 2014)",
         famille="quatre_postes_2014", source="steg-grille-2014-05-01", page="",
         postes=(152, 238, 218, 115, 8000), uniforme=(167, None), secours=None,
         rupture=RUPTURE_2014, remarque=""),
    dict(date="2017-01-01", etabli="oui", portee="ajustement", famille="quatre_postes_2014",
         source="steg-grille-2017-01-01", page="", postes=(161, 250, 227, 124, 8000),
         uniforme=(176, None), secours=None, remarque=""),
    dict(date="2018-05-01", etabli="oui", portee="ajustement", famille="quatre_postes_2014",
         source="steg-grille-2018-05-01", page="", postes=(173, 294, 252, 133, 8000),
         uniforme=(189, None), secours=None, remarque=""),
    dict(date="2018-09-01", etabli="oui", portee="ajustement", famille="quatre_postes_2014",
         source="steg-grille-2018-09-01", page="", postes=(215, 323, 291, 167, 11000),
         uniforme=(212, None), secours=None, remarque=""),
    dict(date="2019-06-01", etabli="oui", portee="ajustement", famille="quatre_postes_2014",
         source="steg-grille-2019-06-01", page="", postes=(240, 366, 329, 188, 11000),
         uniforme=(251, None), secours=None, remarque=""),
    dict(date="2022-10-01", etabli="oui", portee="ajustement", famille="quatre_postes_2014",
         source="steg-grille-2022-10-01-mt", page="", postes=(290, 417, 377, 222, 11000),
         uniforme=(291, None), secours=None, remarque=""),
]

NOMS_POSTES = {
    "trois_postes": ("jour", "pointe", None, "nuit"),
    "quatre_postes": ("jour", "pointe", "soir", "nuit"),
    "quatre_postes_2014": ("jour", "pointe_matin_ete", "pointe_soir", "nuit"),
}


def _non_etablies() -> list[dict]:
    return [dict(date=d, etabli=e, source=src, remarque=r, non_etabli=True)
            for d, e, src, r in NON_ETABLIES]


def lignes() -> list[dict]:
    """Les lignes du CSV, dans l'ordre : date, tarif, poste."""
    sortie = []

    def ligne(g, tarif, famille, poste, valeur, unite, source, *, premiere=False):
        sortie.append(dict(
            tarif=tarif, famille=famille, poste=poste, date_effet=g["date"],
            jour_etabli=g["etabli"], valeur="" if valeur is None else valeur, unite=unite,
            etat="lu" if valeur is not None else "non_etabli", portee=g["portee"], source=source,
            page=g["page"], rupture=g.get("rupture", "") if premiere else "",
            rupture_annee=g["date"][:4] if premiere and g.get("rupture") else "",
            remarque=g["remarque"] if (valeur is None or premiere or g.get("ttc")) else ""))

    for g in sorted(GRILLES + _non_etablies(), key=lambda g: g["date"]):
        if g.get("non_etabli"):
            sortie.append(dict(
                tarif="postes_horaires", famille="", poste="grille_non_etablie",
                date_effet=g["date"], jour_etabli=g["etabli"], valeur="", unite="",
                etat="grille_non_etablie", portee="ajustement", source=g["source"], page="",
                rupture="", rupture_annee="", remarque=g["remarque"]))
            continue
        fam = g["famille"]
        noms = NOMS_POSTES[fam]
        autres = g.get("source_autres", g["source"])
        kwh = KWH_TTC if g.get("ttc") else KWH
        premiere = True
        for nom, v in zip(noms, g["postes"][:4]):
            if nom is None:
                continue
            ligne(g, "postes_horaires", fam, nom, v, kwh, g["source"], premiere=premiere)
            premiere = False
        ligne(g, "postes_horaires", fam, "prime_puissance", g["postes"][4],
              g.get("prime_unite", KW), g["source"])
        if "uniforme_tranches" in g:
            for nom, v in zip(("premiere_tranche", "seconde_tranche"), g["uniforme_tranches"]):
                ligne(g, "uniforme", "uniforme_deux_tranches", nom, v, kwh, autres)
        else:
            prix, prime = g["uniforme"]
            ligne(g, "uniforme", "uniforme", "prix_unique", prix, kwh, autres)
            if prime is not None:
                ligne(g, "uniforme", "uniforme", "prime_puissance", prime, KVA, autres)
        if g["secours"]:
            for nom, v in zip(noms, g["secours"][:4]):
                if nom is None:
                    continue
                ligne(g, "secours", fam, nom, v, KWH, autres)
            ligne(g, "secours", fam, "prime_puissance", g["secours"][4], KW, autres)
    return sortie


def ecrire() -> None:
    CSV.parent.mkdir(parents=True, exist_ok=True)
    with CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CHAMPS, lineterminator="\n")
        w.writeheader()
        w.writerows(lignes())
    print(f"écrit {CSV.relative_to(RACINE)} : {len(lignes())} lignes")


# --- la comparaison au texte des tableaux --------------------------------------------------------

MOIS = {"janvier": 1, "février": 2, "mars": 3, "avril": 4, "mai": 5, "juin": 6, "juillet": 7,
        "août": 8, "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12}


def _date(cellule: str) -> str:
    texte = cellule.replace("^er^", "").strip()
    m = re.match(r"(?:(\d+)\s+)?([a-zéûô]+)\s+(\d{4})", texte)
    jour = int(m.group(1)) if m.group(1) else 1
    return f"{int(m.group(3)):04d}-{MOIS[m.group(2)]:02d}-{jour:02d}"


def _nombre(cellule: str):
    c = re.sub(r"\s", "", cellule).replace(",", ".")
    if not c:
        return None
    v = float(c)
    return int(v) if v == int(v) else v


def lire_tableau(identifiant: str) -> list[list[str]]:
    """Les lignes de données (cellules brutes) du tableau Markdown dont la légende porte l'ancre."""
    texte = QMD.read_text(encoding="utf-8").splitlines()
    fin = next(i for i, l in enumerate(texte) if f"{{#{identifiant}}}" in l)
    fin_tableau = fin
    while texte[fin_tableau - 1].strip() == "":
        fin_tableau -= 1
    debut = fin_tableau
    while debut > 0 and texte[debut - 1].strip() != "":
        debut -= 1
    bloc = [l for l in texte[debut:fin_tableau] if l.startswith("|")]
    rangs = [[c.strip() for c in l.strip().strip("|").split("|")] for l in bloc]
    return rangs[2:]  # entête et filet


def attendu() -> dict[tuple, int | None]:
    """{(date, tarif, poste): valeur} lu dans les trois tableaux."""
    a: dict[tuple, int | None] = {}
    for r in lire_tableau("tbl-compensation-eg-mt-jo"):
        date = _date(r[0])
        jour, pointe, nuit, prime = (_nombre(c) for c in r[2:6])
        for nom, v in (("jour", jour), ("pointe", pointe), ("nuit", nuit),
                       ("prime_puissance", prime)):
            a[(date, "postes_horaires", nom)] = v
        uni = r[6].split(" puis ")
        if len(uni) == 2:
            a[(date, "uniforme", "premiere_tranche")] = _nombre(uni[0])
            a[(date, "uniforme", "seconde_tranche")] = _nombre(uni[1])
        else:
            a[(date, "uniforme", "prix_unique")] = _nombre(uni[0])
    for r in lire_tableau("tbl-compensation-eg-mt-1994"):
        date, tarif = _date(r[0]), {"postes horaires": "postes_horaires", "uniforme": "uniforme",
                                    "secours": "secours"}[r[2]]
        premier, pointe, soir, nuit, prime = (_nombre(c) for c in r[3:8])
        if tarif == "uniforme":
            a[(date, tarif, "prix_unique")] = premier
            a[(date, tarif, "prime_puissance")] = prime
            continue
        famille = "trois_postes" if date < "2000-08-15" else "quatre_postes"
        noms = NOMS_POSTES[famille]
        for nom, v in zip(noms, (premier, pointe, soir, nuit)):
            if nom is not None:
                a[(date, tarif, nom)] = v
        a[(date, tarif, "prime_puissance")] = prime
    for tableau, noms in (("tbl-compensation-eg-mt-2004", NOMS_POSTES["quatre_postes"]),
                          ("tbl-compensation-eg-mt-2014", NOMS_POSTES["quatre_postes_2014"])):
        for r in lire_tableau(tableau):
            date = _date(r[0])
            valeurs = [_nombre(c) for c in r[2:8]]  # jour, 2e, 3e, nuit, prime, uniforme
            for nom, v in zip(noms, valeurs[:4]):
                a[(date, "postes_horaires", nom)] = v
            a[(date, "postes_horaires", "prime_puissance")] = valeurs[4]
            a[(date, "uniforme", "prix_unique")] = valeurs[5]
    return a


def verifier() -> list[str]:
    """Écarts entre le CSV et les tableaux ; liste vide si tout concorde."""
    attendus = attendu()
    with CSV.open(encoding="utf-8") as f:
        lus = list(csv.DictReader(f))
    dans_csv: dict[tuple, int | None] = {}
    non_etablies = {d for d, *_ in NON_ETABLIES}
    for r in lus:
        if r["etat"] == "grille_non_etablie":
            if r["date_effet"] not in non_etablies or r["valeur"] != "" or not r["source"]:
                return [f"grille non établie hors liste ou mal formée : {r['date_effet']}"]
            continue
        cle = (r["date_effet"], r["tarif"], r["poste"])
        if cle in dans_csv:
            return [f"clé en double dans le CSV : {cle}"]
        dans_csv[cle] = _nombre(r["valeur"]) if r["valeur"] != "" else None
    ecarts = []
    for cle, v in attendus.items():
        if cle[1] == "secours" and cle not in dans_csv and v is None:
            continue
        if cle not in dans_csv:
            ecarts.append(f"dans le tableau, absent du CSV : {cle} = {v}")
        elif dans_csv[cle] != v:
            ecarts.append(f"valeur différente {cle} : tableau {v}, CSV {dans_csv[cle]}")
    for cle, v in dans_csv.items():
        if cle not in attendus:
            ecarts.append(f"dans le CSV, absent du tableau : {cle} = {v}")
    return ecarts


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "verifier"
    if action == "ecrire":
        ecrire()
    else:
        ecarts = verifier()
        for e in ecarts:
            print(e)
        print(f"{len(attendu())} valeurs comparées, {len(ecarts)} écart(s)")
        sys.exit(1 if ecarts else 0)

"""Série « tarifs de l'électricité en moyenne tension, 1994-2022 » du volume « La compensation ».

    uv run python scripts/serie_tarifs_mt.py ecrire     # écrit precis/_seriescache/<série>.csv
    uv run python scripts/serie_tarifs_mt.py verifier   # compare le CSV aux trois tableaux du chapitre

La série est une transcription, valeur par valeur, des trois tableaux du chapitre
« L'électricité et le gaz » (`tbl-compensation-eg-mt-1994`, `-mt-2004` et `-mt-2014`), eux-mêmes
sourcés grille par grille. La figure `tarifs_mt` de `figures/electricite.py` la lit par
`figtools.series()` ; elle ne lit jamais le tableau Markdown. `verifier` compare le CSV au texte
des tableaux, dans les deux sens : chaque valeur d'un tableau est dans le CSV, chaque valeur du CSV
est dans un tableau (une case vide d'un tableau est une ligne sans valeur du CSV).

Une ligne par tarif, poste et date d'effet. Les familles ne se raccordent pas :

  - `trois_postes`    : jour, pointe, nuit (grille de juin 1994, en vigueur jusqu'en août 2000) ;
  - `quatre_postes`   : jour, pointe, soir, nuit (du 15 août 2000 au 1er mai 2014 exclu) ;
  - `quatre_postes_2014` : jour, pointe du matin en été, pointe du soir, nuit (depuis le 1er mai 2014) ;
  - `uniforme`        : le prix unique du tarif uniforme, défini de la même façon sur toute la période.

Le passage de trois à quatre postes a lieu entre la grille de juin 1994 et celle du 15 août 2000 ;
le jour n'est pas établi. Le passage aux quatre postes redéfinis a lieu le 1er mai 2014.
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
KW = "millimes par kW et par mois"
KVA = "millimes par kVA et par mois"

RUPTURE_1994_2000 = ("De trois à quatre postes horaires : la grille de juin 1994 compte trois postes, "
                     "celle du 15 août 2000 quatre ; le jour du changement n'est pas établi")
RUPTURE_2014 = ("Quatre postes redéfinis le 1er mai 2014 (réforme de 2014) : les postes d'avant et "
                "d'après ne s'alignent pas")

# --- la transcription ---------------------------------------------------------------------------
# (date d'effet, jour établi, portée, source, page, famille, valeurs par tarif)
# Tarif à postes horaires : (jour, pointe, soir, nuit, prime) ; None = case vide du tableau.
# Tarif uniforme : (prix, prime) ; secours : (jour, pointe, soir, nuit, prime).

GRILLES = [
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
            remarque=g["remarque"] if (valeur is None or premiere) else ""))

    for g in GRILLES:
        fam = g["famille"]
        noms = NOMS_POSTES[fam]
        autres = g.get("source_autres", g["source"])
        premiere = True
        for nom, v in zip(noms, g["postes"][:4]):
            if nom is None:
                continue
            ligne(g, "postes_horaires", fam, nom, v, KWH, g["source"], premiere=premiere)
            premiere = False
        ligne(g, "postes_horaires", fam, "prime_puissance", g["postes"][4], KW, g["source"])
        prix, prime = g["uniforme"]
        ligne(g, "uniforme", "uniforme", "prix_unique", prix, KWH, autres)
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
    c = re.sub(r"\s", "", cellule)
    return int(c) if c else None


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
    for r in lus:
        cle = (r["date_effet"], r["tarif"], r["poste"])
        if cle in dans_csv:
            return [f"clé en double dans le CSV : {cle}"]
        dans_csv[cle] = int(r["valeur"]) if r["valeur"] != "" else None
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

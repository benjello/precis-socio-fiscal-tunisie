"""Série « tarif de l'électricité en haute tension, 1978-2022 » du volume « La compensation ».

    uv run python scripts/serie_tarifs_ht.py ecrire     # écrit precis/_seriescache/<série>.csv
    uv run python scripts/serie_tarifs_ht.py verifier   # compare le CSV aux trois tableaux du chapitre

Transcription, valeur par valeur, des trois tableaux du chapitre « L'électricité et le gaz » sur
la haute tension (`tbl-compensation-eg-ht-jo`, `-ht-1994`, `-ht-2004`). La figure `tarifs_ht` de
`figures/electricite.py` la lit par `figtools.series()`. `verifier` compare le CSV aux tableaux
dans les deux sens. Même forme que `serie_tarifs_mt.py`.

Familles de postes, qui ne se raccordent pas :

  - `trois_postes`        : jour, pointe, nuit (Journal officiel, 1978-1992 ; grille de juin 1994) ;
  - `trois_postes_saison` : tarif général à trois postes, du 1er septembre au 31 mai (2000-2003) ;
  - `quatre_postes_ete`   : tarif général à quatre postes, du 1er juin au 31 août (2000-2003) ;
  - `quatre_postes`       : jour, pointe, soir, nuit (2004 au 1er mai 2014 exclu) ;
  - `quatre_postes_2014`  : jour, pointe du matin en été, pointe du soir, nuit (depuis le 1er mai 2014).

De 2000 à 2003, les deux tarifs généraux sont saisonniers et valent la même année : ce ne sont
pas deux familles successives. Prix taxes comprises jusqu'en 1987, hors taxe sur la valeur ajoutée
à partir de 1991. La prime de puissance garde l'unité de chaque texte (dinars par kW et par an
jusqu'en 1987, puis par mois ; millimes par kW et par mois depuis 1994) : rien n'est converti.
Les grilles non établies (`NON_ETABLIES`) arrêtent le niveau précédent, comme pour la moyenne
tension.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from serie_tarifs_mt import (KW, KWH, KWH_TTC, PREMIERE_TRANSCRIPTION, RUPTURE_1991,  # noqa: E402
                             RUPTURE_2014, _date, _nombre, lire_tableau)

RACINE = Path(__file__).resolve().parents[1]
SERIE = "steg-tarifs-haute-tension"
CSV = RACINE / "precis" / "_seriescache" / f"{SERIE}.csv"

CHAMPS = ["tarif", "famille", "poste", "date_effet", "jour_etabli", "valeur", "unite", "etat",
          "portee", "source", "page", "rupture", "rupture_annee", "remarque"]
NOMS_POSTES = {
    "trois_postes": ("jour", "pointe", None, "nuit"),
    "trois_postes_saison": ("jour", "pointe", None, "nuit"),
    "quatre_postes_ete": ("jour", "pointe", "soir", "nuit"),
    "quatre_postes": ("jour", "pointe", "soir", "nuit"),
    "quatre_postes_2014": ("jour", "pointe_matin_ete", "pointe_soir", "nuit"),
}
RUPTURE_2000 = ("Le tarif général devient saisonnier : quatre postes du 1er juin au 31 août, trois "
                "postes du 1er septembre au 31 mai, d'après les pages de la FIPA ; le jour du "
                "changement n'est pas établi")

# Prime du Journal officiel : (valeur, unité), telle que le texte la donne.
D_AN, D_MOIS = "dinars par kW et par an", "dinars par kW et par mois"

# (date, jour établi, portée, source, page, famille, tarif, (jour, pointe, soir, nuit), prime,
#  unité de la prime, rupture, remarque)
G = []


def _g(date, etabli, portee, source, famille, postes, prime, unite_prime=KW, tarif="general",
       page="", rupture="", remarque=""):
    G.append(dict(date=date, etabli=etabli, portee=portee, source=source, page=page,
                  famille=famille, tarif=tarif, postes=postes, prime=prime,
                  unite_prime=unite_prime, rupture=rupture, remarque=remarque))


_g("1978-11-30", "oui", "mise en place", "arrete-1978-11-27-tarifs-electricite-gaz", "trois_postes",
   (15, 22, None, 8), 5, D_AN, remarque=PREMIERE_TRANSCRIPTION)
_g("1981-08-31", "oui", "ajustement", "arrete-1981-09-01-tarifs-electricite-gaz", "trois_postes",
   (26, 37, None, 20), 6, D_AN, remarque=PREMIERE_TRANSCRIPTION)
_g("1982-09-29", "oui", "ajustement", "arrete-1982-09-30-tarifs-electricite-gaz", "trois_postes",
   (31, 46, None, 24), 12, D_AN, remarque=PREMIERE_TRANSCRIPTION)
_g("1984-05-31", "oui", "ajustement", "arrete-1984-06-04-tarifs-electricite-gaz", "trois_postes",
   (33, 58, None, 25), 15, D_AN, remarque=PREMIERE_TRANSCRIPTION)
_g("1987-06-16", "oui", "ajustement", "arrete-1987-06-08-tarifs-electricite-gaz", "trois_postes",
   (34, 68, None, 26), 15, D_AN, remarque=PREMIERE_TRANSCRIPTION)
_g("1991-01-01", "oui", "ajustement", "arrete-1990-12-19-tarifs-electricite-gaz", "trois_postes",
   (33, 68, None, 25), 1.25, D_MOIS, rupture=RUPTURE_1991, remarque=PREMIERE_TRANSCRIPTION)
_g("1992-08-01", "oui", "ajustement", "decision-1992-08-11-tarifs-electricite-gaz", "trois_postes",
   (34, 74, None, 26), 2, D_MOIS)
_g("1994-06-01", "non", "ajustement", "fipa-2001-02-electricite-eng ; fipa-1999-production",
   "trois_postes", (40, 80, None, 27), 2500,
   remarque="Le mois vient de la Banque mondiale ; la grille ne change pas de 1994 à août 2000.")
_g("1994-06-01", "non", "ajustement", "fipa-2001-02-electricite-eng", "trois_postes",
   (47, 88, None, 28), 1000, tarif="secours")
_g("2000-08-15", "oui", "ajustement", "fipa-2001-05-electricite ; api-2003-04-couts-energie",
   "quatre_postes_ete", (41, 81, 62, 28), 2500, rupture=RUPTURE_2000)
_g("2000-08-15", "oui", "ajustement", "fipa-2002-06-electricite-aout-2000", "trois_postes_saison",
   (43, 79, None, 29), 2500)
_g("2000-08-15", "oui", "ajustement", "fipa-2001-05-electricite ; api-2003-04-couts-energie",
   "quatre_postes", (52, 94, 67, 30), 1000, tarif="secours")
_g("2001-08-01", "oui", "ajustement", "esmap-2005-307-electrification-rurale", "quatre_postes_ete",
   (42, 82, 63, 29), 2500, page="tableau 6.2, p. 36", remarque="L'ESMAP ne donne pas la saison.")
_g("2001-08-01", "oui", "ajustement", "esmap-2005-307-electrification-rurale", "trois_postes_saison",
   (44, 80, None, 30), 2500, page="tableau 6.2, p. 36")
_g("2001-08-01", "oui", "ajustement", "esmap-2005-307-electrification-rurale", "quatre_postes",
   (53, 95, 68, 31), 1000, tarif="secours", page="tableau 6.2, p. 36")
_g("2003-04-01", "oui", "ajustement", "fipa-2003-08-electricite-avril-2003", "trois_postes_saison",
   (48, 82, None, 35), 2500)
_g("2003-04-01", "oui", "ajustement", "fipa-2003-08-electricite-avril-2003", "quatre_postes_ete",
   (44, 84, 65, 35), 2500)
_g("2003-04-01", "oui", "ajustement", "fipa-2003-08-electricite-avril-2003", "quatre_postes",
   (55, 97, 70, 37), 1000, tarif="secours")
for _d, _p, _src, _v, _prime in (
        ("2004-05-01", "ajustement", "steg-grille-2004-05-01", (48, 89, 69, 38), 2500),
        ("2006-01-01", "ajustement", "steg-grille-2006-01-01", (59, 103, 79, 45), 3000),
        ("2008-09-01", "ajustement", "steg-grille-2008-09-01", (94, 147, 119, 75), 3000),
        ("2010-06-01", "ajustement", "steg-grille-2010-06-01", (106, 164, 129, 81), 3000),
        ("2013-03-01", "ajustement", "steg-grille-2013-03-01", (126, 192, 142, 96), 4500)):
    _g(_d, "oui", _p, _src, "quatre_postes", _v, _prime)
for _d, _p, _src, _v, _prime in (
        ("2014-05-01", "étape (de la réforme de 2014)", "steg-grille-2014-05-01", (148, 233, 212, 111), 7500),
        ("2017-01-01", "ajustement", "steg-grille-2017-01-01", (156, 249, 221, 120), 7500),
        ("2018-05-01", "ajustement", "steg-grille-2018-05-01", (168, 279, 243, 129), 7500),
        ("2018-09-01", "ajustement", "steg-grille-2018-09-01", (207, 309, 279, 160), 10000),
        ("2022-05-01", "ajustement", "steg-grille-2022-05-01", (238, 364, 332, 179), 10000)):
    _g(_d, "oui", _p, _src, "quatre_postes_2014", _v, _prime,
       rupture=RUPTURE_2014 if _d == "2014-05-01" else "")

NON_ETABLIES = [
    ("1981-01-31", "oui", "arrete-1981-01-23-tarifs-electricite",
     "Haute et moyenne tension relevées le 31 janvier 1981 (tbl-compensation-eg-textes-1961-1982) ; "
     "la grille n'est pas reprise au tableau de la haute tension."),
    ("1993-10-01", "non", "bm-1998-icr-17374",
     "Ajustement d'octobre 1993, +3 % en moyenne de tous les tarifs selon la Banque mondiale ; grille "
     "de la haute tension non établie."),
    ("2005-02-01", "oui", "bad-2006-rap-electricite-vi",
     "La Banque africaine de développement liste les barèmes successifs et compte sept ajustements "
     "de 2000 au 1er janvier 2006 ; la grille de la basse tension change le 1er février 2005 "
     "(tbl-compensation-eg-grilles-steg) ; grille de la haute tension à cette date non établie."),
    ("2005-07-01", "oui", "bad-2006-rap-electricite-vi",
     "Tarif du 1er juillet 2005, donné pour la basse tension par la Banque africaine de "
     "développement (tbl-compensation-eg-ajustements-1992-2006) ; grille de la haute tension non établie."),
    ("2007-07-01", "oui", "steg-ra-2007", "+6 % sur l'électricité et le gaz ; grille non établie."),
    ("2007-12-01", "oui", "steg-ra-2007", "+6,9 % sur l'électricité ; grille non établie."),
    ("2008-04-01", "oui", "steg-ra-2008", "+7,76 % sur l'électricité ; grille non établie."),
    ("2012-09-01", "oui", "steg-grille-2012-09-01",
     "Grille de la moyenne tension du 1er septembre 2012 ; celle de la haute tension n'est pas établie."),
    ("2014-01-01", "oui", "minfin-compensation-carburants-2014",
     "Le rapport de contrôle de 2014 date une hausse du 1er janvier 2014 (p. 75) ; grille non établie."),
]


def lignes() -> list[dict]:
    sortie = []
    for g in G:
        noms = NOMS_POSTES[g["famille"]]
        kwh = KWH_TTC if g["date"] < "1991-01-01" else KWH
        premiere = g["tarif"] == "general"
        for nom, v in zip(noms, g["postes"]):
            if nom is None:
                continue
            sortie.append(dict(
                tarif=g["tarif"], famille=g["famille"], poste=nom, date_effet=g["date"],
                jour_etabli=g["etabli"], valeur="" if v is None else v, unite=kwh,
                etat="lu" if v is not None else "non_etabli", portee=g["portee"], source=g["source"],
                page=g["page"], rupture=g["rupture"] if premiere else "",
                rupture_annee=g["date"][:4] if premiere and g["rupture"] else "",
                remarque=g["remarque"]))
            premiere = False
        sortie.append(dict(
            tarif=g["tarif"], famille=g["famille"], poste="prime_puissance", date_effet=g["date"],
            jour_etabli=g["etabli"], valeur=g["prime"], unite=g["unite_prime"], etat="lu",
            portee=g["portee"], source=g["source"], page=g["page"], rupture="", rupture_annee="",
            remarque=""))
    for date, etabli, source, remarque in NON_ETABLIES:
        sortie.append(dict(
            tarif="general", famille="", poste="grille_non_etablie", date_effet=date,
            jour_etabli=etabli, valeur="", unite="", etat="grille_non_etablie", portee="ajustement",
            source=source, page="", rupture="", rupture_annee="", remarque=remarque))
    return sorted(sortie, key=lambda r: r["date_effet"])


def ecrire() -> None:
    CSV.parent.mkdir(parents=True, exist_ok=True)
    with CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CHAMPS, lineterminator="\n")
        w.writeheader()
        w.writerows(lignes())
    print(f"écrit {CSV.relative_to(RACINE)} : {len(lignes())} lignes")


def _prime_jo(cellule: str):
    """« 5 D par kW et par an » -> (5, unité)."""
    m = re.match(r"([\d,]+) D par kW et par (an|mois)", cellule)
    return _nombre(m.group(1)), D_AN if m.group(2) == "an" else D_MOIS


TARIFS_1994 = {"général, trois postes": "trois", "général, quatre postes": "quatre_postes_ete",
               "secours": "secours"}


def attendu() -> dict[tuple, object]:
    """{(date, tarif, famille, poste): valeur} lu dans les trois tableaux."""
    a: dict[tuple, object] = {}
    for r in lire_tableau("tbl-compensation-eg-ht-jo"):
        date = _date(r[0])
        for nom, c in zip(("jour", "pointe", "nuit"), r[2:5]):
            a[(date, "general", "trois_postes", nom)] = _nombre(c)
        a[(date, "general", "trois_postes", "prime_puissance")] = _prime_jo(r[5])
    for r in lire_tableau("tbl-compensation-eg-ht-1994"):
        date = _date(r[0])
        jour, pointe, soir, nuit, prime = (_nombre(c) for c in r[3:8])
        genre = TARIFS_1994[r[2]]
        if genre == "secours":
            tarif, famille = "secours", "trois_postes" if date < "2000-08-15" else "quatre_postes"
        elif genre == "trois":
            tarif, famille = "general", "trois_postes" if date < "2000-08-15" else "trois_postes_saison"
        else:
            tarif, famille = "general", genre
        for nom, v in zip(NOMS_POSTES[famille], (jour, pointe, soir, nuit)):
            if nom is not None:
                a[(date, tarif, famille, nom)] = v
        a[(date, tarif, famille, "prime_puissance")] = (prime, KW)
    for r in lire_tableau("tbl-compensation-eg-ht-2004"):
        date = _date(r[0])
        famille = "quatre_postes" if date < "2014-05-01" else "quatre_postes_2014"
        valeurs = [_nombre(c) for c in r[2:7]]
        for nom, v in zip(NOMS_POSTES[famille], valeurs[:4]):
            a[(date, "general", famille, nom)] = v
        a[(date, "general", famille, "prime_puissance")] = (valeurs[4], KW)
    return a


def verifier() -> list[str]:
    attendus = attendu()
    with CSV.open(encoding="utf-8") as f:
        lus = list(csv.DictReader(f))
    non_etablies = {d for d, *_ in NON_ETABLIES}
    dans_csv: dict[tuple, object] = {}
    for r in lus:
        if r["etat"] == "grille_non_etablie":
            if r["date_effet"] not in non_etablies or r["valeur"] != "" or not r["source"]:
                return [f"grille non établie hors liste ou mal formée : {r['date_effet']}"]
            continue
        cle = (r["date_effet"], r["tarif"], r["famille"], r["poste"])
        if cle in dans_csv:
            return [f"clé en double dans le CSV : {cle}"]
        v = _nombre(r["valeur"]) if r["valeur"] != "" else None
        dans_csv[cle] = (v, r["unite"]) if r["poste"] == "prime_puissance" else v
    ecarts = []
    for cle, v in attendus.items():
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

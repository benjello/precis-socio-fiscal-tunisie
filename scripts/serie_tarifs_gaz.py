"""Séries du gaz naturel du volume « La compensation » : tarifs de la STEG, et prix et coût de l'Observatoire.

    uv run python scripts/serie_tarifs_gaz.py ecrire     # écrit les deux CSV de precis/_seriescache/
    uv run python scripts/serie_tarifs_gaz.py verifier   # les compare aux tableaux du chapitre

Deux séries, transcrites valeur par valeur des tableaux du chapitre « L'électricité et le gaz » :

  - `steg-tarifs-gaz` : le tarif du gaz naturel en basse pression (`tbl-compensation-eg-gaz`,
    1987-2022) et en moyenne et haute pression (`tbl-compensation-eg-gaz-mp-hp`, 1987-2022), en
    millimes courants par thermie. Une ligne par réseau, tranche et date d'effet. Tant que le prix
    de la haute pression est une formule indexée sur le fuel lourd (« 0,1 F − 0,67 »), la ligne n'a
    pas de valeur : `etat = formule`, la formule dans `formule`. Prix taxe à la production comprise
    en 1987, hors taxes ensuite (colonne `unite`).
  - `one-gaz-prix-cout` : le prix de vente global hors taxes et le coût de revient du gaz, en
    dinars courants par tonne équivalent pétrole, 2017-2025, selon l'Observatoire national de
    l'énergie et des mines (`tbl-compensation-eg-cout-one`, deux dernières colonnes).

Les figures `tarifs_gaz` et `cout_prix_gaz` de `figures/electricite.py` les lisent par
`figtools.series()`. `verifier` compare chaque CSV à ses tableaux dans les deux sens.

GRILLES NON ÉTABLIES (`etat = grille_non_etablie`) : comme pour l'électricité, une date où le
chapitre établit un relèvement sans donner la grille arrête le niveau précédent. Pour la hausse de
1993, dont la Banque mondiale ne donne pas le mois, la date retenue est le 1er janvier 1993 : c'est
une convention, qui arrête le prix de 1992 au plus tôt où il a pu changer. Le prix de juin 1994 de
la basse et de la moyenne pression (17,1 et 14) est rattaché à cette date par un calcul du
chapitre, non par une lecture (`jour_etabli = non`, `remarque`).
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from serie_tarifs_mt import _date, _nombre, lire_tableau  # noqa: E402

RACINE = Path(__file__).resolve().parents[1]
CACHE = RACINE / "precis" / "_seriescache"
SERIE = "steg-tarifs-gaz"
SERIE_ONE = "one-gaz-prix-cout"
CSV = CACHE / f"{SERIE}.csv"
CSV_ONE = CACHE / f"{SERIE_ONE}.csv"

CHAMPS = ["reseau", "tranche", "structure", "date_effet", "jour_etabli", "valeur", "formule", "unite",
          "etat", "portee", "source", "page", "rupture", "remarque"]
HT = "millimes courants par thermie, hors taxes"
TTC = "millimes courants par thermie, taxe à la production comprise"
CALCUL_1994 = ("Prix relayé sans date d'effet par les pages des agences publiques, de 1999 à 2003 ; "
               "rattaché à juin 1994 par un calcul du chapitre (hausses de 1993 et de juin 1994 "
               "données par la Banque mondiale), non par une lecture.")
RUPTURE_1991 = ("Prix taxe à la production comprise en 1987, hors taxes à partir de 1991 : les "
                "niveaux ne se comparent pas de part et d'autre")

# --- basse pression ------------------------------------------------------------------------------
# (date, jour établi, portée, structure, sources, valeurs, rupture, remarque)
BP = [
    ("1987-06-16", "oui", "ajustement", "prix unique", "arrete-1987-06-08-tarifs-electricite-gaz",
     [14], "", ""),
    ("1991-01-01", "oui", "ajustement", "prix unique", "arrete-1990-12-19-tarifs-electricite-gaz",
     [13.7], RUPTURE_1991, ""),
    ("1992-08-01", "oui", "ajustement", "prix unique", "decision-1992-08-11-tarifs-electricite-gaz",
     [15.1], "", ""),
    ("1994-06-01", "non", "ajustement", "prix unique",
     "fipa-1999-production ; fipa-2001-02-electricite-eng ; fipa-2003-08-gaz", [17.1], "", CALCUL_1994),
    ("2008-09-01", "oui", "étape (de la réforme de 1984)", "trois tranches", "steg-grille-2008-09-01",
     [22.09, 25.10, 26.30], "Trois tranches à partir du 1er septembre 2008", ""),
    ("2010-06-01", "oui", "ajustement", "trois tranches", "steg-grille-2010-06-01",
     [22.40, 25.60, 27.00], "", ""),
    ("2014-05-01", "oui", "étape (de la réforme de 2014)", "quatre tranches", "steg-grille-2014-05-01",
     [23.5, 29.5, 36.0, 42.2], "Réforme de 2014 : quatre tranches", ""),
    ("2017-01-01", "oui", "ajustement", "quatre tranches", "steg-grille-2017-01-01",
     [24.3, 30.5, 39.4, 46.2], "", ""),
    ("2018-09-01", "oui", "étape (de la réforme de 2014)", "quatre tranches, ménages",
     "steg-grille-2018-09-01", [24.3, 32.5, 42.4, 53.0],
     "Étape de la réforme de 2014 : les grilles distinguent les ménages des autres abonnés", ""),
    ("2019-06-01", "oui", "ajustement", "quatre tranches, ménages", "steg-grille-2019-06-01",
     [24.3, 35.8, 47.0, 58.6], "", ""),
    ("2022-05-01", "oui", "ajustement", "quatre tranches, ménages", "steg-grille-2022-05-01",
     [24.3, 38.7, 58.5, 86.7], "", ""),
]
NON_ETABLIES_BP = [
    ("1993-01-01", "non", "bm-1998-icr-17374",
     "Hausse de 8,6 % du gaz des ménages en 1993 selon la Banque mondiale, mois non donné : le "
     "1er janvier 1993 est une convention."),
    ("2004-05-01", "oui", "steg-grille-2004-05-01", "Grille exprimée par mètre cube, non reprise."),
    ("2006-01-01", "oui", "steg-grille-2006-01-01", "Grille exprimée par mètre cube, non reprise."),
    ("2007-07-01", "oui", "steg-ra-2007", "+6 % sur l'électricité et le gaz ; grille non établie."),
    ("2007-12-01", "oui", "steg-ra-2007", "+8,3 % sur le gaz ; grille non établie."),
    ("2008-04-01", "oui", "steg-ra-2008", "+13 % sur le gaz ; grille non établie."),
    ("2012-09-01", "oui", "steg-ra-2012", "+8 % sur le gaz ; grille de la basse pression non établie."),
    ("2013-03-01", "oui", "steg-grille-2013-03-01", "Grille de mars 2013, non reprise."),
]

# --- moyenne et haute pression -------------------------------------------------------------------
# (date, jour établi, portée, source, moyenne pression, HP premier niveau, HP second niveau,
#  HP au-delà, rupture, remarque) ; une chaîne est une formule, None une case vide.
MP_HP = [
    ("1987-06-16", "oui", "point de départ", "arrete-1987-06-08-tarifs-electricite-gaz",
     [11.3], "0,1 F − 0,67", None, None, "", ""),
    ("1991-01-01", "oui", "ajustement", "arrete-1990-12-19-tarifs-electricite-gaz",
     [11.1], "0,1 F − 0,67", None, None, RUPTURE_1991, ""),
    ("1992-08-01", "oui", "ajustement", "decision-1992-08-11-tarifs-electricite-gaz",
     [12.3], "0,1 F − 0,67", None, None, "", ""),
    ("1994-06-01", "non", "ajustement", "fipa-1999-production ; fipa-2001-02-electricite-eng",
     [14], None, None, None, "", CALCUL_1994),
    ("2000-04-01", "non", "formule de la haute pression seule", "aner-2000-impact-prix-energie",
     None, "0,1 F + 0,37", None, None, "",
     "Formule en vigueur en avril 2000 selon l'étude de l'ANER (p. 21) ; date d'effet non établie."),
    ("2000-08-15", "oui", "ajustement de la haute pression", "api-2003-04-couts-energie",
     [14], "0,1 F − 0,4", None, None, "", ""),
    ("2004-05-01", "oui", "ajustement", "steg-grille-2004-05-01",
     None, "0,1 F − 1,2475", None, None, "", ""),
    ("2004-08-01", "oui", "ajustement", "steg-grille-2004-05-01",
     [15.76, 15.19], None, None, None, "",
     "Grille du 1er mai 2004, applicable à la moyenne pression le 1er août 2004."),
    ("2006-01-01", "oui", "ajustement", "steg-grille-2006-01-01",
     [16.57, 16.00], "0,1 F − 7,8932", None, None, "", ""),
    ("2008-09-01", "oui", "ajustement de structure", "steg-grille-2008-09-01",
     [23.60, 23.00], 24.00, 24.00, "0,1 F − 4,3571", "", ""),
    ("2010-06-01", "oui", "ajustement", "steg-grille-2010-06-01",
     [25.30, 24.90], 25.30, 26.80, "0,1 F − 1,590", "", ""),
    ("2012-09-01", "oui", "ajustement", "steg-grille-2012-09-01",
     [None, None], 27.10, 29.50, "0,1 F − 1,590", "", "Grille de la moyenne pression non établie."),
    ("2013-03-01", "oui", "ajustement", "steg-grille-2013-03-01",
     [None, None], 29.20, 32.30, "0,1 F − 1,590", "", "Grille de la moyenne pression non établie."),
    ("2014-05-01", "oui", "rupture (réforme de 2014)", "steg-grille-2014-05-01",
     [37.6, 37.1], 35.8, 39.1, 52.5,
     "Réforme de 2014 : la formule indexée sur le fuel lourd laisse la place à un prix fixe", ""),
    ("2017-01-01", "oui", "ajustement", "steg-grille-2017-01-01", [40.3, 39.8], 38.4, 42.6, 56.0, "", ""),
    ("2018-05-01", "oui", "ajustement", "steg-grille-2018-05-01", [44.5, 43.9], 42.5, 47.2, 59.4, "", ""),
    ("2018-09-01", "oui", "ajustement", "steg-grille-2018-09-01", [54.5, 53.8], 52.2, 58.0, 70.0, "", ""),
    ("2022-05-01", "oui", "ajustement", "steg-grille-2022-05-01", [71.1, 70.5], 60.4, 67.1, 81.3, "", ""),
]
NON_ETABLIES_MP = [
    ("1993-01-01", "non", "bm-1998-icr-17374",
     "Hausses du gaz en 1993 selon la Banque mondiale, mois non donné : le 1er janvier 1993 est une "
     "convention."),
    ("2007-07-01", "oui", "steg-ra-2007", "+6 % sur l'électricité et le gaz ; grille non établie."),
    ("2007-12-01", "oui", "steg-ra-2007", "+8,3 % sur le gaz ; grille non établie."),
    ("2008-04-01", "oui", "steg-ra-2008", "+13 % sur le gaz ; grille non établie."),
]


def _ligne(reseau, tranche, structure, date, etabli, valeur, unite, portee, source, rupture="",
           remarque=""):
    formule = valeur if isinstance(valeur, str) else ""
    v = "" if valeur is None or formule else valeur
    etat = "formule" if formule else ("lu" if v != "" else "non_etabli")
    return dict(reseau=reseau, tranche=tranche, structure=structure, date_effet=date,
                jour_etabli=etabli, valeur=v, formule=formule, unite=unite, etat=etat,
                portee=portee, source=source, page="", rupture=rupture, remarque=remarque)


def _non_etablie(reseau, date, etabli, source, remarque):
    return dict(reseau=reseau, tranche="grille_non_etablie", structure="", date_effet=date,
                jour_etabli=etabli, valeur="", formule="", unite="", etat="grille_non_etablie",
                portee="ajustement", source=source, page="", rupture="", remarque=remarque)


def lignes() -> list[dict]:
    sortie = []
    for date, etabli, portee, structure, source, valeurs, rupture, remarque in BP:
        unite = TTC if date < "1991-01-01" else HT
        noms = ["prix_unique"] if len(valeurs) == 1 else [f"tranche_{i}" for i in range(1, 5)]
        for i, (nom, v) in enumerate(zip(noms, valeurs)):
            sortie.append(_ligne("basse_pression", nom, structure, date, etabli, v, unite, portee,
                                 source, rupture if i == 0 else "", remarque))
    for d, e, src, r in NON_ETABLIES_BP:
        sortie.append(_non_etablie("basse_pression", d, e, src, r))
    for date, etabli, portee, source, mp, hp1, hp2, hp3, rupture, remarque in MP_HP:
        unite = TTC if date < "1991-01-01" else HT
        premiere = True
        if mp is not None:
            noms = ["prix_unique"] if len(mp) == 1 else ["premier_niveau", "second_niveau"]
            structure = "prix unique" if len(mp) == 1 else "deux niveaux de débit"
            for nom, v in zip(noms, mp):
                sortie.append(_ligne("moyenne_pression", nom, structure, date, etabli, v, unite,
                                     portee, source, rupture if premiere else "", remarque))
                premiere = False
        for nom, v in (("premier_niveau", hp1), ("second_niveau", hp2), ("au_dela", hp3)):
            if v is None and not (date >= "2008-09-01" and nom != "au_dela"):
                continue
            sortie.append(_ligne("haute_pression", nom, "trois niveaux" if date >= "2008-09-01"
                                 else "formule", date, etabli, v, unite, portee, source,
                                 rupture if premiere else "", remarque))
            premiere = False
    for d, e, src, r in NON_ETABLIES_MP:
        sortie.append(_non_etablie("moyenne_pression", d, e, src, r))
    ordre = {"basse_pression": 0, "moyenne_pression": 1, "haute_pression": 2}
    return sorted(sortie, key=lambda r: (ordre[r["reseau"]], r["date_effet"]))


# --- Observatoire --------------------------------------------------------------------------------

CHAMPS_ONE = ["annee", "grandeur", "valeur", "unite", "etat", "source", "remarque"]
ONE = {  # année: (prix de vente, coût de revient)
    2017: (460.4, 638.1), 2018: (508.0, 864.3), 2019: (600.2, None), 2020: (616.0, None),
    2021: (609.1, None), 2022: (642.9, 1545.9), 2023: (660.1, 1777.9), 2024: (647.4, 1622.8),
    2025: (645.2, 1497.7),
}


def lignes_one() -> list[dict]:
    sortie = []
    for annee, (prix, cout) in ONE.items():
        for grandeur, v in (("prix_de_vente", prix), ("cout_de_revient", cout)):
            sortie.append(dict(
                annee=annee, grandeur=grandeur, valeur="" if v is None else v,
                unite="dinars courants par tonne équivalent pétrole", etat=(
                    "provisoire avant audit" if v is not None else "non_publie"),
                source="one-chiffres-cles-energie",
                remarque="" if v is not None else "Valeur que la publication ne donne pas ou qui n'est pas établie."))
    return sortie


def _ecrire(chemin: Path, champs, rangs) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with chemin.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=champs, lineterminator="\n")
        w.writeheader()
        w.writerows(rangs)
    print(f"écrit {chemin.relative_to(RACINE)} : {len(rangs)} lignes")


def ecrire() -> None:
    _ecrire(CSV, CHAMPS, lignes())
    _ecrire(CSV_ONE, CHAMPS_ONE, lignes_one())


# --- la comparaison au texte des tableaux --------------------------------------------------------

def _valeurs(cellule: str) -> list:
    """« trois tranches : 22,09 ; 25,10 » -> [22.09, 25.1] ; « 0,1 F − 0,67 » -> ['0,1 F − 0,67']."""
    c = cellule.strip()
    if not c:
        return []
    if "F" in c:
        return [c]
    return [_nombre(n) for n in re.findall(r"\d+(?:,\d+)?", c)]


def attendu() -> dict[tuple, object]:
    a: dict[tuple, object] = {}
    for r in lire_tableau("tbl-compensation-eg-gaz"):
        date = _date(r[0])
        vals = _valeurs(r[2])
        noms = ["prix_unique"] if len(vals) == 1 else [f"tranche_{i}" for i in range(1, 5)]
        for nom, v in zip(noms, vals):
            a[("basse_pression", nom, date)] = v
    for r in lire_tableau("tbl-compensation-eg-gaz-mp-hp"):
        cellule = r[0].replace("[]{#r-eg-gaz-hp-1992}", "")
        if cellule.startswith("en vigueur en avril 2000"):
            d_mp = d_hp = "2000-04-01"
        elif "pour la moyenne pression" in cellule:
            d_hp, d_mp = "2004-05-01", "2004-08-01"
        else:
            d_mp = d_hp = _date(cellule)
        mp = _valeurs(r[2])
        if mp:
            noms = ["prix_unique"] if len(mp) == 1 else ["premier_niveau", "second_niveau"]
            for nom, v in zip(noms, mp):
                a[("moyenne_pression", nom, d_mp)] = v
        elif d_mp >= "2008-09-01":
            a[("moyenne_pression", "premier_niveau", d_mp)] = None
            a[("moyenne_pression", "second_niveau", d_mp)] = None
        for nom, c in zip(("premier_niveau", "second_niveau", "au_dela"), r[3:6]):
            v = _valeurs(c)
            if v:
                a[("haute_pression", nom, d_hp)] = v[0]
            elif d_hp >= "2008-09-01" and nom != "au_dela":
                a[("haute_pression", nom, d_hp)] = None
    return a


def _comparer(attendus: dict, dans_csv: dict) -> list[str]:
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


def verifier() -> list[str]:
    with CSV.open(encoding="utf-8") as f:
        lus = list(csv.DictReader(f))
    non_etablies = {(r, d) for r, liste in (("basse_pression", NON_ETABLIES_BP),
                                            ("moyenne_pression", NON_ETABLIES_MP))
                    for d, *_ in liste}
    dans_csv: dict[tuple, object] = {}
    for r in lus:
        if r["etat"] == "grille_non_etablie":
            if (r["reseau"], r["date_effet"]) not in non_etablies or r["valeur"] != "" \
                    or not r["source"]:
                return [f"grille non établie hors liste ou mal formée : {r['date_effet']}"]
            continue
        cle = (r["reseau"], r["tranche"], r["date_effet"])
        if cle in dans_csv:
            return [f"clé en double dans le CSV : {cle}"]
        dans_csv[cle] = r["formule"] or (_nombre(r["valeur"]) if r["valeur"] != "" else None)
    ecarts = _comparer(attendu(), dans_csv)
    # L'Observatoire
    one = {}
    for r in lire_tableau("tbl-compensation-eg-cout-one"):
        annee = int(r[0])
        one[(annee, "prix_de_vente")] = _nombre(r[3])
        one[(annee, "cout_de_revient")] = _nombre(r[4])
    with CSV_ONE.open(encoding="utf-8") as f:
        lus_one = {(int(r["annee"]), r["grandeur"]): (_nombre(r["valeur"]) if r["valeur"] else None)
                   for r in csv.DictReader(f)}
    return ecarts + _comparer(one, lus_one)


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "verifier"
    if action == "ecrire":
        ecrire()
    else:
        ecarts = verifier()
        for e in ecarts:
            print(e)
        print(f"{len(attendu())} valeurs de tarif comparées, {len(ecarts)} écart(s)")
        sys.exit(1 if ecarts else 0)

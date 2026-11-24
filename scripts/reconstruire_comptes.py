#!/usr/bin/env python3
"""Reconstruire le compte des administrations publiques (S13) à partir des postes de l'ouvrage.

Pilote de l'articulation entre chapitres et comptes nationaux : chaque poste du registre
`precis/fr/postes-comptables.csv` rattache un dispositif (une section de l'ouvrage) à une case
des comptes de secteur de l'INS (opération × côté × secteur). Le script :

1. détermine l'année de référence : la dernière année imprimée « définitive » dans l'édition la
   plus récente des comptes des secteurs (statut lu dans l'en-tête de l'INS : sans astérisque,
   définitif ; un astérisque, semi-définitif ; deux, provisoire — colonne `statut_annee` de la
   série `cnat-secteurs`) ;
2. chiffre chaque poste qui a une série : montant de l'année de référence et années couvertes,
   lus dans le cache ; source = première clé de citation de la série ; un poste sans série garde
   un montant vide (jamais estimé) ;
3. pour chaque opération des comptes non financiers de S13 et de ses sous-secteurs, compare la
   cible de l'INS à la somme des postes rattachés : écart (résidu publié) et taux de couverture ;
4. contrôle : un poste par section (une section n'a qu'un domicile), ancres existantes, somme des
   sous-secteurs face au consolidé, solde B.1g recalculé ;
5. écrit precis/fr/compte-apu-reconstruit.csv (une ligne par opération et secteur),
   precis/fr/compte-apu-flux.csv (qui verse à qui) et met à jour les colonnes `annees`,
   `montant_reference` et `source` du registre.

    uv run python scripts/reconstruire_comptes.py            # écrit
    uv run python scripts/reconstruire_comptes.py --verifier # échoue si un contrôle échoue
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
FR = RACINE / "precis" / "fr"
CACHE = RACINE / "precis" / "_seriescache"
REGISTRE = FR / "postes-comptables.csv"
SORTIE = FR / "compte-apu-reconstruit.csv"
FLUX = FR / "compte-apu-flux.csv"
ENCADRES = FR / "encadres-comptes"
SECTEURS = {"apu": "S13", "apu_centrale": "S1311", "apu_locale": "S1313", "apu_secu": "S1314"}
COMPTES_NON_FINANCIERS = ("production", "exploitation", "affectation", "distribution", "utilisation", "capital")
ARRONDI = 0.05
# Opérations agrégées : leur reconstruction somme aussi les postes de leurs composantes.
AGREGATS = {
    "impots_production_importations": ["tva", "impots_importations", "impots_exportations", "autres_impots_produits",
                                       "autres_impots_production"],
    "subventions": ["subventions_produits", "autres_subventions_production"],
    "revenus_propriete": ["interets", "revenus_distribues", "loyers"],
}
# Écarts connus entre comptes et budget, nommés et non corrigés (voir l'annexe des comptes).
RESIDUS_NOMMES = {  # noms descriptifs ; les explications sont testées par scripts/expliquer_residus.py
    "impots_importations": "droits et taxes sur les importations des comptes face aux droits de douane du budget",
    "impots_courants": "impôts courants des comptes face à l'IRPP et à l'IS du budget",
    "fbcf": "FBCF des comptes face aux dépenses d'équipement du budget",
}


def fr(v) -> str:
    """Nombre à la française : espace fine insécable pour les milliers, virgule décimale."""
    return f"{float(v):,.1f}".replace(",", "\u202f").replace(".", ",")


def lire_csv(chemin: Path) -> list[dict]:
    with chemin.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def annee_reference(secteurs: list[dict]) -> tuple[int, str]:
    eds = sorted({l["edition"] for l in secteurs})
    ed = eds[-1]
    defs = sorted({int(l["annee"]) for l in secteurs if l["edition"] == ed and l["statut_annee"] == "definitif"})
    return defs[-1], ed


def montant(serie: str, colonne: str, annee: int) -> tuple[float | None, str]:
    chemin = CACHE / f"{serie}.csv"
    if not chemin.exists():
        return None, ""
    lignes = lire_csv(chemin)
    annees = sorted({int(str(l["annee"])[:4]) for l in lignes if str(l.get("annee", ""))[:4].isdigit()})
    couv = f"{annees[0]}-{annees[-1]}" if annees else ""
    if serie == "compensation-parts":  # total budgétaire de la compensation, une ligne par année
        vals = [float(l["valeur_MDT"]) for l in lignes if str(l["annee"]) == str(annee)
                and l["poste"] == colonne and l["famille"] == "budget"]
        return (-vals[-1] if vals else None), couv  # subvention : ressource négative dans les comptes
    vals = [float(l[colonne]) for l in lignes if str(l["annee"]) == str(annee) and l.get(colonne, "") != ""]
    return (vals[-1] if vals else None), couv


def source_serie(serie: str, snapshot: dict) -> str:
    e = snapshot.get(serie)
    return (e.get("sources") or [""])[0] if e else ""


def ancre_existe(volume: str, chapitre: str, ancre: str) -> bool:
    page = FR / (f"{volume}.qmd" if not chapitre else f"{volume}/{chapitre}.qmd")
    return page.exists() and re.search(r"\{#" + re.escape(ancre) + r"[ }]", page.read_text(encoding="utf-8")) is not None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", action="store_true")
    a = ap.parse_args(argv)
    secteurs = lire_csv(CACHE / "cnat-secteurs.csv")
    an, ed = annee_reference(secteurs)
    snapshot = {e["id"]: e for e in yaml.safe_load((CACHE / "catalog.snapshot.yml").read_text(encoding="utf-8"))}
    postes = lire_csv(REGISTRE)
    erreurs = []
    vus_sections = {}
    for p in postes:
        cle = (p["volume"], p["chapitre"], p["ancre"])
        if cle in vus_sections:
            erreurs.append(f"section {cle} domicile de deux postes ({vus_sections[cle]}, {p['poste']})")
        vus_sections[cle] = p["poste"]
        if not ancre_existe(*cle):
            erreurs.append(f"poste {p['poste']} : ancre {p['ancre']} absente de {p['volume']}/{p['chapitre']}")
        if p["serie"]:
            m, couv = montant(p["serie"], p["colonne"], an)
            p["montant_reference"] = "" if m is None else f"{m:.1f}"
            p["annees"] = couv
            p["source"] = source_serie(p["serie"], snapshot)
        else:
            p["montant_reference"], p["annees"], p["source"] = "", "", ""
    # Cibles de l'INS, édition la plus récente, année de référence
    cible = {}
    for l in secteurs:
        if l["edition"] == ed and int(l["annee"]) == an and l["secteur"] in SECTEURS and l["sous_ligne"] in ("0", "False", ""):
            if any(k in l["compte"].lower() for k in COMPTES_NON_FINANCIERS):
                cible[(l["secteur"], l["cote"], l["operation"])] = (l["code_scn2008"], l["compte"], float(l["valeur"]))
    # sous-lignes utiles (TVA, impôts sur les importations…) : rangées à part
    for l in secteurs:
        if l["edition"] == ed and int(l["annee"]) == an and l["secteur"] in SECTEURS and l["sous_ligne"] not in ("0", "False", ""):
            if any(k in l["compte"].lower() for k in COMPTES_NON_FINANCIERS):
                cible.setdefault((l["secteur"], l["cote"], l["operation"]), (l["code_scn2008"], l["compte"], float(l["valeur"])))
    somme = defaultdict(float)
    rattaches = defaultdict(list)
    for p in postes:
        # le secteur des administrations concerné, qu'il verse ou reçoive (les subventions, versées,
        # sont inscrites par l'INS en ressources négatives)
        for sec in p["secteur_verse"].split(";") + p["secteur_recoit"].split(";"):
            if sec in SECTEURS:
                rattaches[(sec, p["cote"], p["operation"])].append(p["poste"])
                if p["montant_reference"]:
                    somme[(sec, p["cote"], p["operation"])] += float(p["montant_reference"])
                break  # un poste n'est compté que dans un secteur : le premier de la liste
    lignes = []
    for (sec, cote, op), (code, compte, v) in sorted(cible.items(), key=lambda k: (k[0][0], k[1][1], k[0][1], k[0][2])):
        ops = [op] + AGREGATS.get(op, [])
        secs = list(SECTEURS) if sec == "apu" else [sec]
        noms = sorted({n for ss in secs for o in ops for n in rattaches.get((ss, cote, o), [])})
        vals = [somme[(ss, cote, o)] for ss in secs for o in ops if (ss, cote, o) in somme]
        s_postes = sum(vals) if vals else None
        residu = None if s_postes is None else round(v - s_postes, 1)
        lignes.append({"annee": an, "edition": ed, "secteur": SECTEURS[sec], "compte": compte, "cote": cote,
                       "code_scn": code, "operation": op, "cible_ins_md": v,
                       "postes": ";".join(noms), "somme_postes_md": "" if s_postes is None else round(s_postes, 1),
                       "residu_md": "" if residu is None else residu,
                       "couverture_pct": "" if s_postes is None or not v else round(100 * s_postes / v, 1),
                       "residu_nomme": RESIDUS_NOMMES.get(op, "") if residu is not None else ""})
    # Contrôles : sous-secteurs face au consolidé ; solde B.1g
    controles = []
    for (sec, cote, op), (code, compte, v) in cible.items():
        if sec != "apu":
            continue
        parts = [cible[(s, cote, op)][2] for s in ("apu_centrale", "apu_locale", "apu_secu") if (s, cote, op) in cible]
        if len(parts) == 3:
            controles.append({"controle": "sous-secteurs - consolidé", "objet": f"{op} ({cote})",
                              "ecart_md": round(sum(parts) - v, 1),
                              "note": "écart attendu pour les transferts entre administrations (consolidation)"})
    for sec in SECTEURS:
        try:
            p1 = cible[(sec, "ressources", "production")][2]
            p2 = cible[(sec, "emplois", "consommation_intermediaire")][2]
            b1 = cible[(sec, "emplois", "valeur_ajoutee_brute")][2]
            e = round(p1 - p2 - b1, 1)
            controles.append({"controle": "solde B.1g recalculé", "objet": SECTEURS[sec], "ecart_md": e,
                              "note": "ok" if abs(e) <= ARRONDI * 3 else "écart"})
            if abs(e) > ARRONDI * 3:
                erreurs.append(f"B.1g de {SECTEURS[sec]} : écart {e}")
        except KeyError:
            pass
    flux = [{"poste": p["poste"], "operation": p["operation"], "code_scn": p["code_scn"], "verse": p["secteur_verse"],
             "recoit": p["secteur_recoit"], "montant_md": p["montant_reference"], "volume": p["volume"],
             "section": (f"{p['volume']}/{p['chapitre']}" if p["chapitre"] else p["volume"]) + f"#{p['ancre']}"}
            for p in postes]
    if a.verifier:
        for e in erreurs:
            print("ERREUR :", e)
        return 1 if erreurs else 0
    for chemin, rows in ((SORTIE, lignes), (FLUX, flux)):
        with chemin.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
    with (FR / "compte-apu-controles.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["controle", "objet", "ecart_md", "note"], lineterminator="\n")
        w.writeheader()
        w.writerows(controles)
    with REGISTRE.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(postes[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(postes)
    # Encadrés « Dans les comptes », préparés pour les sections dont le poste est chiffré (pilote :
    # ils ne sont pas encore inclus dans les chapitres, la généralisation attend la relecture).
    ENCADRES.mkdir(parents=True, exist_ok=True)
    cible_s13 = {(l["cote"], l["operation"]): l for l in lignes if l["secteur"] == "S13"}
    for p in postes:
        if not p["montant_reference"]:
            continue
        l = cible_s13.get((p["cote"], p["operation"]))
        lien = "../compte-apu.html#sec-capu-operations"
        phrase = (f"Dans les comptes de la nation, ce dispositif relève de l'opération {p['code_scn']} "
                  f"({p['operation'].replace('_', ' ')}, {p['cote']}) du compte des administrations publiques. "
                  f"En {an}, l'ouvrage en chiffre {fr(p['montant_reference'])} millions de dinars")
        if l:
            phrase += (f" ; l'INS inscrit {fr(l['cible_ins_md'])} millions de dinars pour l'ensemble "
                       f"de l'opération")
        (ENCADRES / f"{p['poste']}.md").write_text(
            f"::: {{.callout-tip title=\"Dans les comptes\"}}\n{phrase} ([le compte reconstruit]({lien})).\n:::\n",
            encoding="utf-8")
    chiffres = sum(1 for p in postes if p["montant_reference"])
    s13 = [l for l in lignes if l["secteur"] == "S13"]
    couverts = sum(1 for l in s13 if l["somme_postes_md"] != "")
    print(f"année de référence {an} (édition {ed}) ; {len(postes)} postes dont {chiffres} chiffrés ; "
          f"S13 : {couverts} opérations couvertes sur {len(s13)} ; {len(erreurs)} erreur(s)")
    for e in erreurs:
        print("ERREUR :", e)
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())

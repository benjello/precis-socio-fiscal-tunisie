"""Sommaire par les comptes : pour chaque opération des comptes des secteurs, les secteurs qui l'inscrivent
en emplois et en ressources, son montant en 2020 (année de référence) et en 2023, les postes et sections de
l'ouvrage qui s'y rattachent, la part reconstruite et le résidu.

Montant de l'opération : somme des secteurs résidents (sociétés non financières, sociétés financières,
administrations publiques, ménages) du côté des emplois, ou des ressources quand aucun résident ne l'inscrit
en emplois (reste du monde, de son point de vue, pour les seules opérations qu'aucun résident n'inscrit) ; édition la plus récente où l'année est définitive. Montant reconstruit : somme des postes chiffrés
de l'opération (registre `postes-comptables.csv`), chacun compté une fois. Part reconstruite : montant
reconstruit rapporté au montant de l'opération ; résidu : différence. Rien n'est estimé ni déplacé.

    uv run python scripts/sommaire_comptes.py [--verifier]

Sortie : precis/fr/sommaire-comptes.csv.
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reconstruire_comptes as rc  # noqa: E402

SORTIE = rc.FR / "sommaire-comptes.csv"
ANNEES = (2020, 2023)
RESIDENTS = ("snf", "sf", "apu", "menages")
NOMS = {"snf": "SNF", "sf": "SF", "apu": "APU", "menages": "ménages", "rdm": "reste du monde"}
ORDRE_COMPTES = ["production", "exploitation", "affectation", "distribution", "redistribution", "utilisation", "capital"]


def rang_compte(c: str) -> int:
    c = c.lower()
    return next((i for i, k in enumerate(ORDRE_COMPTES) if k in c), len(ORDRE_COMPTES))


def construire() -> list[dict]:
    secteurs = rc.lire_csv(rc.CACHE / "cnat-secteurs.csv")
    snapshot = {e["id"]: e for e in yaml.safe_load((rc.CACHE / "catalog.snapshot.yml").read_text(encoding="utf-8"))}
    ops = {}
    montants = defaultdict(dict)
    for an in ANNEES:
        ed = rc.edition_pour(secteurs, an)
        lig = [l for l in secteurs if l["edition"] == ed and int(l["annee"]) == an and str(l.get("base", "2015")) == "2015"
               and l["secteur"] in RESIDENTS + ("rdm",) and str(l["sous_ligne"]) in ("0", "1")
               and l["code_scn2008"] and not l["code_scn2008"].startswith(("B.", "F."))]
        postes, *_ = rc.calculer(an, ed, secteurs, snapshot)
        par_op = defaultdict(list)
        for l in lig:
            par_op[(l["code_scn2008"], l["operation"])].append(l)
        for k, ls in par_op.items():
            o = ops.setdefault(k, {"compte": ls[0]["compte"], "libelle": ls[0]["libelle_ins"].strip(), "emplois": set(), "ressources": set()})
            for l in ls:
                if float(l["valeur"]):
                    o[l["cote"]].add(l["secteur"])
            res = [l for l in ls if l["secteur"] in RESIDENTS] or ls  # échanges extérieurs : le reste du monde seul
            cote = "emplois" if any(l["cote"] == "emplois" for l in res) else "ressources"
            v = sum(float(l["valeur"]) for l in res if l["cote"] == cote)
            ps = [p for p in postes if p["operation"] == k[1]]
            chiffres = [float(p["montant_reference"]) for p in ps if p.get("montant_reference")]
            montants[k][an] = (v, cote, sum(chiffres) if chiffres else None, ps)
    out = []
    for k, o in sorted(ops.items(), key=lambda kv: (rang_compte(kv[1]["compte"]), kv[0][0], kv[0][1])):
        ligne = {"compte": o["compte"], "code_scn": k[0], "operation": k[1], "libelle_ins": o["libelle"],
                 "emplois": ";".join(NOMS[s] for s in RESIDENTS + ("rdm",) if s in o["emplois"]),
                 "ressources": ";".join(NOMS[s] for s in RESIDENTS + ("rdm",) if s in o["ressources"])}
        sections = []
        for an in ANNEES:
            v, cote, rec, ps = montants[k].get(an, (None, "", None, []))
            ligne[f"montant_{an}_md"] = "" if v is None else round(v, 1)
            ligne[f"cote_{an}"] = cote
            ligne[f"reconstruit_{an}_md"] = "" if rec is None else round(rec, 1)
            ligne[f"part_{an}_pct"] = "" if rec is None or not v else round(100 * abs(rec) / abs(v), 1)
            ligne[f"residu_{an}_md"] = "" if rec is None or v is None else round(v - rec, 1)
            for p in ps:
                s = f"{p['poste']}|{p['volume']}|{p['chapitre']}|{p['ancre']}"
                if s not in sections:
                    sections.append(s)
        ligne["sections"] = ";".join(sections)
        out.append(ligne)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", action="store_true")
    a = ap.parse_args(argv)
    lignes = construire()
    if a.verifier:
        if [dict(x) for x in rc.lire_csv(SORTIE)] != [{k: str(v) for k, v in l.items()} for l in lignes]:
            print(f"{SORTIE.name} n'est pas à jour : relancer scripts/sommaire_comptes.py")
            return 1
        return 0
    with SORTIE.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(lignes[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(lignes)
    print(f"{len(lignes)} opérations → {SORTIE} ; {sum(bool(l['sections']) for l in lignes)} avec au moins une section")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Comptes des secteurs reconstruits : pour chaque secteur principal, ses opérations de l'année de
référence et les postes de l'ouvrage qui s'y rattachent (lecture seule du cache, rien d'estimé).

Pour S14 (ménages), S11 (sociétés non financières), S12 (sociétés financières) et S2 (reste du
monde), un poste est rattaché à une opération quand le secteur figure du côté de l'opération : parmi
ceux qui versent pour un emploi, parmi ceux qui reçoivent pour une ressource. Le montant du poste
n'est pas rapproché du montant du secteur (un poste chiffre souvent l'opération pour plusieurs
secteurs) : la page dit quelles cases ont un domicile dans l'ouvrage, et leur part des montants.

Sortie : precis/fr/compte-secteurs-reconstruit.csv.
    uv run python scripts/reconstruire_secteurs.py [--verifier]
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
FR = RACINE / "precis" / "fr"
CACHE = RACINE / "precis" / "_seriescache"
SORTIE = FR / "compte-secteurs-reconstruit.csv"
FINANCIER = FR / "compte-secteurs-financier.csv"
TOF_SECTEURS = [("S11", "snf"), ("S12", "sf"), ("S13", "apu"), ("S14", "menages"), ("S2", "rdm")]
INSTRUMENTS = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F", "B9F"]  # « F » : total des opérations financières (code du cache)
SECTEURS = [("menages", "S14", "ménages"), ("snf", "S11", "sociétés non financières"),
            ("sf", "S12", "sociétés financières"), ("rdm", "S2", "reste du monde"), ("apu", "S13", "administrations publiques")]


def lire(p: Path) -> list[dict]:
    with p.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def feuilles(ls: list[dict]) -> list[dict]:
    """Opérations sans les soldes (B.), le compte financier (F.) et les agrégats dont une composante est imprimée."""
    ls = [l for l in ls if l["code_scn2008"] and not l["code_scn2008"].startswith(("B.", "F.")) and l["sous_ligne"] in ("0", "1")]
    out = []
    for cote in ("emplois", "ressources"):
        g = [l for l in ls if l["cote"] == cote]
        codes = {l["code_scn2008"] for l in g}
        ops = {l["operation"] for l in g}
        for l in g:
            c = l["code_scn2008"]
            if any(x != c and x.startswith(c) for x in codes):
                continue
            if l["operation"] == "production" and "production_non_marchande" in ops:
                continue
            out.append(l)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", action="store_true")
    a = ap.parse_args()
    cache = [l for l in lire(CACHE / "cnat-secteurs.csv") if str(l["base"]) == "2015"]
    definitif = [l for l in cache if l["statut_annee"] == "definitif"]
    ed = max(l["edition"] for l in definitif)
    an = max(int(l["annee"]) for l in definitif if l["edition"] == ed)
    postes = lire(FR / "postes-comptables.csv")
    lignes = []
    for sec, code, nom in SECTEURS:
        fs = feuilles([l for l in cache if l["edition"] == ed and int(l["annee"]) == an and l["secteur"] == sec])
        tot = {c: sum(abs(float(l["valeur"])) for l in fs if l["cote"] == c) for c in ("emplois", "ressources")}
        for l in fs:
            cote = "secteur_verse" if l["cote"] == "emplois" else "secteur_recoit"
            ps = [p["poste"] for p in postes if p["operation"] == l["operation"]
                  and any(s == sec or (sec == "apu" and s.startswith("apu")) for s in p[cote].split(";"))]
            lignes.append({"annee": an, "edition": ed, "secteur": code, "nom": nom, "cote": l["cote"],
                           "code_scn": l["code_scn2008"], "operation": l["operation"], "libelle_ins": l["libelle_ins"],
                           "valeur_md": round(float(l["valeur"]), 1),
                           "part_pct": round(100 * abs(float(l["valeur"])) / tot[l["cote"]], 1) if tot[l["cote"]] else "",
                           "postes": ";".join(ps)})
    # Compte financier : flux nets de créances et de dettes par instrument et secteur (TOF), et raccord
    # du solde B9F avec la capacité de financement des comptes des secteurs.
    tof = [l for l in lire(CACHE / "cnat-tof.csv") if l["edition"] == ed and int(l["annee"]) == an and l["tableau"] == "flux"]
    cap = {l["secteur"]: float(l["valeur"]) for l in cache if l["edition"] == ed and int(l["annee"]) == an
           and l["operation"] == "capacite_financement" and l["cote"] == "emplois"}
    fin = []
    for ins in INSTRUMENTS:
        for code, sec in TOF_SECTEURS:
            v = {c: next((float(l["valeur_md"]) for l in tof if l["code"] == ins and l["secteur"] == code and l["cote"] == c), None)
                 for c in ("creances", "dettes")}
            pages = sorted({l["page_fichier"] for l in tof if l["code"] == ins and l["secteur"] == code})
            if v["creances"] is None and v["dettes"] is None:
                continue
            fin.append({"annee": an, "edition": ed, "instrument": ins, "secteur": code,
                        "creances_md": "" if v["creances"] is None else v["creances"],
                        "dettes_md": "" if v["dettes"] is None else v["dettes"],
                        "capacite_financement_md": cap.get(sec, "") if ins == "B9F" else "", "pages": ";".join(pages)})
    if a.verifier:
        if [dict(x) for x in lire(FINANCIER)] != [{k: str(v) for k, v in l.items()} for l in fin]:
            print(f"{FINANCIER.name} n'est pas à jour : relancer scripts/reconstruire_secteurs.py")
            return 1
        if [dict(x) for x in lire(SORTIE)] != [{k: str(v) for k, v in l.items()} for l in lignes]:
            print(f"{SORTIE.name} n'est pas à jour : relancer scripts/reconstruire_secteurs.py")
            return 1
        return 0
    with FINANCIER.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(fin[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(fin)
    with SORTIE.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(lignes[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(lignes)
    for _, code, _ in SECTEURS:
        ls = [l for l in lignes if l["secteur"] == code]
        dom = sum(l["part_pct"] for l in ls if l["postes"]) / 2
        print(f"{code} : {len(ls)} opérations, {sum(bool(l['postes']) for l in ls)} avec un domicile, {dom:.1f} % des montants")
    return 0


if __name__ == "__main__":
    sys.exit(main())

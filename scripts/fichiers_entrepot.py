#!/usr/bin/env python3
"""Copies, dans le cache du précis, de fichiers de l'entrepôt tunisia-data qui ne sont pas des séries du catalogue.

`figtools.refresh_cache` ne copie que les séries du catalogue. Les fichiers ci-dessous (table de raccord des
codes, contrôles d'une série) sont copiés tels quels, octet pour octet, dans `precis/_seriescache/`, et leur
provenance est inscrite dans `precis/_seriescache/fichiers-entrepot.yml` : chemin dans l'entrepôt, commit de
l'entrepôt au moment de la copie, empreinte SHA-256 de la copie.

    TUNISIA_DATA=~/projets/tunisia-data-wt-merge uv run python scripts/fichiers_entrepot.py   # recopie
    uv run python scripts/fichiers_entrepot.py --verifier

`--verifier` échoue si une copie ne correspond plus à l'empreinte inscrite, ou, quand l'entrepôt est présent
(variable `TUNISIA_DATA`, par défaut `~/projets/tunisia-data`) et porte le fichier, si la copie s'écarte du
fichier de l'entrepôt. Un entrepôt absent, ou qui ne porte pas encore le fichier (copie de travail en retard
sur main), est signalé sans faire échouer.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "precis" / "_seriescache"
FICHE = CACHE / "fichiers-entrepot.yml"
ENTREPOT = Path(os.environ.get("TUNISIA_DATA", Path.home() / "projets" / "tunisia-data")).expanduser()
# nom dans le cache -> chemin dans l'entrepôt
FICHIERS = {
    "raccord-scn-1968-1993-2008.csv": "sources/ins-comptes-nationaux/raccord-scn-1968-1993-2008.csv",
    "cnat-secteurs-base1997-controles.csv": "data/processed/ins-comptes-nationaux/cnat_secteurs_base1997_controles.csv",
}


def empreinte(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def commit_entrepot() -> str:
    r = subprocess.run(["git", "-C", str(ENTREPOT), "rev-parse", "HEAD"], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def lire_fiche() -> dict:
    return {e["fichier"]: e for e in (yaml.safe_load(FICHE.read_text("utf-8")) or [])} if FICHE.exists() else {}


def copier() -> int:
    fiche = lire_fiche()
    commit = commit_entrepot()
    for nom, chemin in FICHIERS.items():
        src = ENTREPOT / chemin
        if not src.exists():
            print(f"ERREUR : {src} absent de l'entrepôt")
            return 1
        shutil.copyfile(src, CACHE / nom)
        fiche[nom] = {"fichier": nom, "entrepot": "tunisia-data", "chemin": chemin, "commit": commit,
                      "sha256": empreinte(CACHE / nom),
                      "commande": "TUNISIA_DATA=<entrepôt à jour de main> uv run python scripts/fichiers_entrepot.py"}
    FICHE.write_text(yaml.safe_dump(list(fiche.values()), allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(f"{len(FICHIERS)} fichier(s) copiés depuis {ENTREPOT} (commit {commit[:7]})")
    return 0


def verifier() -> int:
    fiche = lire_fiche()
    erreurs = []
    present = ENTREPOT.is_dir()
    for nom, chemin in FICHIERS.items():
        copie = CACHE / nom
        e = fiche.get(nom)
        if not copie.exists() or not e:
            erreurs.append(f"{nom} : copie ou fiche absente")
            continue
        if empreinte(copie) != e["sha256"]:
            erreurs.append(f"{nom} : la copie ne correspond plus à l'empreinte de la fiche")
        src = ENTREPOT / chemin
        if present and src.exists():
            if src.read_bytes() != copie.read_bytes():
                erreurs.append(f"{nom} : s'écarte de {src} (commit {commit_entrepot()[:7]}, copie faite au commit "
                               f"{e['commit'][:7]}) : relancer scripts/fichiers_entrepot.py")
        elif present:
            print(f"avertissement : {src} absent (entrepôt en retard sur le commit {e['commit'][:7]} ?), non comparé")
    if not present:
        print(f"avertissement : entrepôt {ENTREPOT} absent, copies non comparées à l'entrepôt")
    for x in erreurs:
        print("ERREUR :", x)
    return 1 if erreurs else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", action="store_true")
    return verifier() if ap.parse_args(argv).verifier else copier()


if __name__ == "__main__":
    sys.exit(main())

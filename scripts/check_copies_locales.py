#!/usr/bin/env python3
"""Les copies locales annoncées dans les notices existent dans les manifestes de tunisia-data.

Lit uniquement `precis/fr/**/references.json` (la note arabe est une traduction) et les manifestes
versionnés `../tunisia-data/data/manifeste/*.csv` (colonnes `sha`, `chemin`). Stdlib seule, sans la
base SQLite ni le réseau. Signale :

1. un SHA-256 annoncé dans une note qui ne figure dans aucun manifeste (hors notes qui citent
   `PDFs-legislation-tunisie/`, dépôt que tunisia-data ne manifeste pas) ;
2. un fichier `data/raw/…` annoncé dans une note, sans SHA dans cette note (empreinte à ajouter) ;
3. un fichier `data/raw/…` annoncé qui n'est dans aucun manifeste.

Les gabarits (`<édition>`, `*`, `…`) et les dossiers ne sont pas des fichiers : ignorés.

Sauté (code 0, message) si les manifestes sont absents : `TUNISIA_DATA_DIR` ou `../tunisia-data`.
Sans `--strict`, les écarts sont comptés et listés mais le code de sortie reste 0 : une dette
existait avant ce contrôle. `--strict` sort 1 au premier écart de la catégorie 1 ou 3.

    uv run python scripts/check_copies_locales.py [--strict] [--limite N]
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
RE_SHA = re.compile(r"\b[0-9a-f]{64}\b")
RE_CHEMIN = re.compile(r"(?:tunisia-data/)?data/raw/[^\s,;)»\"(]+")
RE_GABARIT = re.compile(r"[<*…{]|AAAA")


def dossier_donnees() -> Path:
    return Path(os.environ.get("TUNISIA_DATA_DIR") or RACINE.parent / "tunisia-data").expanduser()


def lire_manifestes(dossier: Path) -> tuple[set[str], set[str]]:
    """(empreintes, chemins relatifs à data/raw) de tous les manifestes."""
    shas: set[str] = set()
    chemins: set[str] = set()
    for fichier in sorted(dossier.glob("*.csv")):
        with fichier.open(encoding="utf-8", newline="") as flux:
            for ligne in csv.DictReader(flux):
                shas.add(ligne["sha"])
                chemins.add(ligne["chemin"])
    return shas, chemins


def notes(racine: Path = RACINE):
    """(livre, clé, note) pour chaque item des références françaises."""
    base = racine / "precis" / "fr"
    for fichier in sorted(base.rglob("references.json")):
        livre = fichier.parent.relative_to(base).parts[:1] or ("precis",)
        donnees = json.loads(fichier.read_text(encoding="utf-8"))
        for e in donnees["items"] if isinstance(donnees, dict) else donnees:
            yield livre[0], e["id"], e.get("note") or ""


def fichiers_annonces(note: str) -> list[str]:
    """Chemins de fichiers sous data/raw cités dans la note (ni gabarits ni dossiers)."""
    trouves = []
    for m in RE_CHEMIN.finditer(note):
        brut = m.group(0).rstrip(".:")
        if RE_GABARIT.search(brut) or brut.endswith("/"):
            continue
        trouves.append(brut.split("data/raw/", 1)[1])
    return trouves


def ecarts(racine: Path, shas: set[str], chemins: set[str]) -> dict[str, list[tuple[str, str, str]]]:
    sortie: dict[str, list[tuple[str, str, str]]] = {"sha_absent": [], "chemin_sans_sha": [], "chemin_hors_manifeste": []}
    for livre, cle, note in notes(racine):
        annonces = set(RE_SHA.findall(note))
        if "PDFs-legislation-tunisie/" not in note:
            sortie["sha_absent"] += [(livre, cle, s[:12]) for s in sorted(annonces - shas)]
        for chemin in dict.fromkeys(fichiers_annonces(note)):
            if chemin not in chemins:
                sortie["chemin_hors_manifeste"].append((livre, cle, chemin))
            elif not annonces:
                sortie["chemin_sans_sha"].append((livre, cle, chemin))
    return sortie


def main(argv=None) -> int:
    parseur = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parseur.add_argument("--strict", action="store_true", help="sortir 1 sur un SHA absent ou un fichier hors manifeste")
    parseur.add_argument("--limite", type=int, default=10, help="écarts listés par catégorie (défaut 10)")
    options = parseur.parse_args(argv)
    donnees = dossier_donnees() / "data" / "manifeste"
    if not donnees.is_dir():
        print(f"copies locales : manifestes absents ({donnees}), contrôle sauté")
        return 0
    shas, chemins = lire_manifestes(donnees)
    resultat = ecarts(RACINE, shas, chemins)
    titres = {
        "sha_absent": "SHA annoncé, absent des manifestes",
        "chemin_hors_manifeste": "fichier annoncé, absent des manifestes",
        "chemin_sans_sha": "fichier annoncé sans SHA dans la note",
    }
    for nom, titre in titres.items():
        lignes = resultat[nom]
        print(f"{titre} : {len(lignes)}")
        for livre, cle, detail in lignes[: options.limite]:
            print(f"  {livre}/{cle}  {detail}")
        if len(lignes) > options.limite:
            print(f"  … {len(lignes) - options.limite} de plus")
    bloquant = len(resultat["sha_absent"]) + len(resultat["chemin_hors_manifeste"])
    return 1 if options.strict and bloquant else 0


if __name__ == "__main__":
    sys.exit(main())

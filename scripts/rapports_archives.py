"""Récupère dans l'Internet Archive les rapports d'un groupe, un document à la fois, et en tient le catalogue.

    uv run python scripts/rapports_archives.py bna            # un groupe de scripts/rapports_archives.yml
    uv run python scripts/rapports_archives.py bna --liste    # montre ce qui serait pris, sans télécharger

L'index de l'Internet Archive (CDX) donne les PDF de chaque site ; les motifs du fichier YAML en retiennent
quelques-uns. Les pièces vont sous `tunisia-data/data/raw/entreprises-publiques/bvmt-rapports-archives/<groupe>/`
(hors git), la capture la plus récente de chaque adresse, en copie brute (`id_`). Les refus de l'archive (429) sont
attendus : le script réessaie avec une pause, ne reprend jamais un fichier déjà là et ne lance qu'une requête à la fois.
Le catalogue (adresse d'origine, adresse de la capture, taille, somme de contrôle) s'écrit dans
`sources/bvmt-rapports-archives-urls.csv` du dossier `TUNISIA_DATA_CATALOGUE` (par défaut le worktree `tunisia-data-wt-arch`, branche `donnees/rapports-archives`).
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

DONNEES = (
    Path(os.environ.get("TUNISIA_DATA", "~/projets/tunisia-data")).expanduser()
    / "data/raw/entreprises-publiques/bvmt-rapports-archives"
)
CATALOGUE = (
    Path(
        os.environ.get("TUNISIA_DATA_CATALOGUE", "~/projets/tunisia-data-wt-arch")
    ).expanduser()
    / "sources/bvmt-rapports-archives-urls.csv"
)
SPEC = Path(__file__).with_name("rapports_archives.yml")
PAUSE, ESSAIS, ATTENTE = 8, 8, 45
COLONNES = [
    "fichier",
    "url_origine",
    "url_archive",
    "octets",
    "sha256",
    "consultation",
    "famille",
    "etat",
]


def cdx(motif_site: str) -> list[tuple[str, str]]:
    adresse = (
        "http://web.archive.org/cdx/search/cdx?url="
        + urllib.parse.quote(motif_site)
        + "&output=json&fl=original,timestamp&filter=mimetype:application/pdf&collapse=urlkey&limit=5000"
    )
    for _ in range(4):
        try:
            with urllib.request.urlopen(adresse, timeout=120) as reponse:
                return [tuple(ligne) for ligne in json.load(reponse)[1:]]
        except (OSError, ValueError):
            time.sleep(ATTENTE)
    return []


def choisir(groupe: str, spec: dict) -> list[tuple[str, str]]:
    trouves: dict[str, str] = {}
    for site in spec["sites"]:
        for original, horodatage in cdx(site):
            if any(re.search(m, original) for m in spec["motifs"]):
                cle = re.sub(r"^https?://(www\.)?", "", original.split(":80")[0])
                if cle not in trouves or horodatage > trouves[cle][1]:
                    trouves[cle] = (original, horodatage)
        time.sleep(PAUSE)
    return sorted(trouves.values())


def telecharger(groupe: str, original: str, horodatage: str) -> Path | None:
    nom = urllib.parse.unquote(original.split("/")[-1]).replace(" ", "_")
    cible = DONNEES / groupe / f"{horodatage[:8]}_{nom}"
    if cible.exists() and cible.stat().st_size:
        return cible
    cible.parent.mkdir(parents=True, exist_ok=True)
    adresse = f"http://web.archive.org/web/{horodatage}id_/{original}"
    for essai in range(ESSAIS):
        try:
            with urllib.request.urlopen(
                urllib.request.Request(adresse, headers={"User-Agent": "Mozilla/5.0"}),
                timeout=180,
            ) as r:
                contenu = r.read()
            if contenu[:4] != b"%PDF":
                print(f"  pas un PDF : {nom}", file=sys.stderr)
                return None
            cible.write_bytes(contenu)
            time.sleep(PAUSE)
            return cible
        except OSError as erreur:
            print(f"  {nom} : {str(erreur)[:40]} (essai {essai + 1})", file=sys.stderr)
            time.sleep(ATTENTE)
    return None


def inscrire(groupe: str, cible: Path, original: str, horodatage: str) -> None:
    lignes = {}
    if CATALOGUE.exists():
        with CATALOGUE.open(encoding="utf-8", newline="") as source:
            lignes = {r["fichier"]: r for r in csv.DictReader(source)}
    contenu = cible.read_bytes()
    chemin = f"entreprises-publiques/bvmt-rapports-archives/{groupe}/{cible.name}"
    lignes[chemin] = {
        "fichier": chemin,
        "url_origine": original,
        "url_archive": f"https://web.archive.org/web/{horodatage}/{original}",
        "octets": len(contenu),
        "sha256": hashlib.sha256(contenu).hexdigest(),
        "consultation": time.strftime("%Y-%m-%d"),
        "famille": "archive",
        "etat": f"capture du {horodatage[:8]}",
    }
    CATALOGUE.parent.mkdir(parents=True, exist_ok=True)
    with CATALOGUE.open("w", encoding="utf-8", newline="") as sortie:
        ecrivain = csv.DictWriter(sortie, fieldnames=COLONNES)
        ecrivain.writeheader()
        ecrivain.writerows(sorted(lignes.values(), key=lambda r: r["fichier"]))


def main() -> int:
    analyseur = argparse.ArgumentParser(description=(__doc__ or "").split("\n")[0])
    analyseur.add_argument("groupe")
    analyseur.add_argument("--liste", action="store_true")
    options = analyseur.parse_args()
    specs = yaml.safe_load(SPEC.read_text(encoding="utf-8"))
    if options.groupe not in specs:
        print(
            f"groupe inconnu : {options.groupe} ({', '.join(specs)})", file=sys.stderr
        )
        return 2
    choisis = choisir(options.groupe, specs[options.groupe])
    print(f"{len(choisis)} documents pour {options.groupe}")
    for original, horodatage in choisis:
        if options.liste:
            print(f"  {horodatage[:8]} {original[-80:]}")
            continue
        cible = telecharger(options.groupe, original, horodatage)
        if cible:
            inscrire(options.groupe, cible, original, horodatage)
            print(f"  {cible.name} ({cible.stat().st_size // 1000} ko)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

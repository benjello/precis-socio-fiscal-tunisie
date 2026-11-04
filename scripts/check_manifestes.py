#!/usr/bin/env python3
"""Chaque relevé versionné a un manifeste lisible, et le manifeste dit vrai.

Un relevé est un fichier `.csv` du précis accompagné d'un manifeste `.csv.yml` (`format`,
`cle_de_ligne`, `colonnes`, `sources`). Aucun contrôle ne lisait ces manifestes : deux d'entre eux
ne se lisaient plus en YAML, un portait du texte libre à la place des clés de citation, deux
déclaraient une clé de ligne qui ne distinguait pas les lignes, et un relevé n'avait pas de
manifeste. Ce contrôle refuse :

1. un manifeste qui ne se lit pas en YAML, ou qui n'est pas un dictionnaire ;
2. `format` absent ou autre que `long` / `large` ; `cle_de_ligne` absente ou vide ;
3. une colonne de `cle_de_ligne` ou de `colonnes` qui n'existe pas dans le CSV ;
4. une clé de ligne qui ne distingue pas toutes les lignes du CSV ;
5. une entrée de `sources` qui n'est pas une clé d'un `references.json` ;
6. un `.csv` sans manifeste dans un dossier où d'autres en ont un.

Sont ignorés les dossiers engendrés (`figdata/`, `_seriescache/`) et les CSV qui ne sont pas des
relevés (aucun manifeste dans leur dossier).

    uv run python scripts/check_manifestes.py            # sort 1 et liste les écarts
    uv run python scripts/check_manifestes.py --langue ar
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DOSSIERS_ENGENDRES = {"figdata", "_seriescache"}
FORMATS = {"long", "large"}


def cles_connues(racine: Path = RACINE) -> set[str]:
    cles: set[str] = set()
    for fichier in racine.glob("precis/**/references.json"):
        for entree in json.loads(fichier.read_text(encoding="utf-8")).get("items", []):
            cles.add(entree["id"])
    return cles


def _engendre(chemin: Path) -> bool:
    return bool(DOSSIERS_ENGENDRES & set(chemin.parts))


def manifestes(racine: Path = RACINE, langue: str = "fr") -> list[Path]:
    return sorted(
        p for p in racine.glob(f"precis/{langue}/**/*.csv.yml") if not _engendre(p)
    )


def releves_sans_manifeste(racine: Path = RACINE, langue: str = "fr") -> list[Path]:
    """Les `.csv` d'un dossier qui contient au moins un manifeste, mais qui n'en ont pas."""
    dossiers = {m.parent for m in manifestes(racine, langue)}
    return sorted(
        c for d in dossiers for c in d.glob("*.csv") if not c.with_name(c.name + ".yml").exists()
    )


def lire_manifeste(chemin: Path) -> dict | str:
    """Le manifeste lu, ou le message d'erreur si la lecture échoue."""
    import yaml

    try:
        contenu = yaml.safe_load(chemin.read_text(encoding="utf-8"))
    except yaml.YAMLError as erreur:
        marque = getattr(erreur, "problem_mark", None)
        ou = f" (ligne {marque.line + 1})" if marque else ""
        return f"YAML illisible{ou} : {getattr(erreur, 'problem', erreur)}"
    if not isinstance(contenu, dict):
        return "le manifeste n'est pas un dictionnaire"
    return contenu


def ecarts_manifeste(chemin: Path, manifeste: dict, cles: set[str]) -> list[str]:
    """Les écarts d'un manifeste lu, confronté à son CSV et aux clés de références."""
    problemes: list[str] = []
    if manifeste.get("format") not in FORMATS:
        problemes.append(f"format absent ou inconnu : {manifeste.get('format')!r}")
    cle = manifeste.get("cle_de_ligne")
    if not isinstance(cle, list) or not cle or not all(isinstance(c, str) for c in cle):
        problemes.append("cle_de_ligne absente ou vide")
        cle = []
    # Deux formes de manifeste : un relevé simple (`colonnes` et `sources` à la racine) ; un relevé
    # de tarifs en plusieurs tableaux (`tableaux: {nom: {sources: […], …}}`), dont les `colonnes`
    # sont des en-têtes de tableau, non des colonnes du CSV.
    tableaux = manifeste.get("tableaux")
    tableaux = tableaux if isinstance(tableaux, dict) else {}
    colonnes = manifeste.get("colonnes")
    if not isinstance(colonnes, dict):
        if not tableaux:
            problemes.append("colonnes absentes")
        colonnes = {}
    listes_de_sources = [("sources", manifeste.get("sources"))] + [
        (f"tableaux.{nom}.sources", (t or {}).get("sources")) for nom, t in tableaux.items()
    ]
    if all(s is None for _, s in listes_de_sources):
        problemes.append("sources absentes (liste vide si le relevé n'en a pas)")
    for ou, sources in listes_de_sources:
        if sources is None:
            continue
        if not isinstance(sources, list):
            problemes.append(f"{ou} : liste attendue")
            continue
        for source in sources:
            if not isinstance(source, str) or source not in cles:
                problemes.append(f"{ou} : source inconnue des references.json : {str(source)[:60]!r}")

    csv_path = chemin.with_name(chemin.name[: -len(".yml")])
    if not csv_path.exists():
        problemes.append(f"CSV absent : {csv_path.name}")
        return problemes
    with csv_path.open(encoding="utf-8", newline="") as flux:
        lecteur = csv.DictReader(flux)
        entetes = lecteur.fieldnames or []
        lignes = list(lecteur)
    for colonne in cle:
        if colonne not in entetes:
            problemes.append(f"colonne de cle_de_ligne absente du CSV : {colonne}")
    for colonne in colonnes:
        if colonne not in entetes:
            problemes.append(f"colonne déclarée absente du CSV : {colonne}")
    if cle and all(c in entetes for c in cle):
        compte = Counter(tuple(ligne[c] for c in cle) for ligne in lignes)
        doublons = [(k, n) for k, n in compte.items() if n > 1]
        if doublons:
            k, n = doublons[0]
            problemes.append(
                f"cle_de_ligne {cle} ne distingue pas {sum(n - 1 for _, n in doublons)} ligne(s), "
                f"par exemple {k} ({n} fois)"
            )
    return problemes


def verifier(racine: Path = RACINE, langue: str = "fr") -> list[str]:
    cles = cles_connues(racine)
    problemes: list[str] = []
    for chemin in manifestes(racine, langue):
        relatif = chemin.relative_to(racine).as_posix()
        lu = lire_manifeste(chemin)
        if isinstance(lu, str):
            problemes.append(f"{relatif} : {lu}")
            continue
        problemes += [f"{relatif} : {p}" for p in ecarts_manifeste(chemin, lu, cles)]
    for chemin in releves_sans_manifeste(racine, langue):
        problemes.append(f"{chemin.relative_to(racine).as_posix()} : relevé sans manifeste")
    return problemes


def main(argv: list[str] | None = None) -> int:
    parseur = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parseur.add_argument("--langue", default="fr", choices=("fr", "ar"))
    options = parseur.parse_args(argv)
    problemes = verifier(RACINE, options.langue)
    for probleme in problemes:
        print(f"✗ {probleme}")
    if problemes:
        print(f"{len(problemes)} écart(s) dans les manifestes de relevés.")
        return 1
    print(f"{len(manifestes(RACINE, options.langue))} manifeste(s) de relevés : lisibles et cohérents.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

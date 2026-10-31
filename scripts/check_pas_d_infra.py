"""Ce dépôt est public (GitHub Pages) : l'infrastructure de sauvegarde n'y figure pas.

Les notes et les procédures de la sauvegarde du corpus vivent dans le dépôt privé `tunisia-data`.
Ce contrôle échoue si un fichier SUIVI de ce dépôt en porte la trace.

    uv run python scripts/check_pas_d_infra.py [chemins...]

Sans argument, contrôle tous les fichiers suivis par git. Sortie 1 si une mention subsiste.

La liste des mots à chercher n'est PAS dans ce dépôt : elle les rendrait publics. Elle se lit dans
`PAS_D_INFRA_MOTS` (le texte de la liste) ou, à défaut, dans le fichier désigné par
`PAS_D_INFRA_FICHIER`, ou dans `~/.config/benjello-backup/mots-interdits.txt`. Sans liste, le
contrôle est sauté et le dit. Format, une règle par ligne :

    interdit: <expression régulière>   # mot sans autre emploi ici : interdit partout
    site: <expression régulière>       # nom qui peut être celui d'une personne : interdit
                                       # seulement dans une ligne qui parle de sauvegarde

Ce fichier et son test ne citent aucun mot de la liste.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).parent.parent
FICHIER_PAR_DEFAUT = Path.home() / ".config/benjello-backup/mots-interdits.txt"

CONTEXTE = re.compile(r"sauvegarde|serveur|\bS3\b|r[ée]plica|garage|\bvpn\b|n[œo]ud", re.I)

EXEMPTS = {"scripts/check_pas_d_infra.py", "tests/test_check_pas_d_infra.py"}
TAILLE_MAX = 2_000_000


def lire_regles(texte: str) -> tuple[re.Pattern | None, re.Pattern | None]:
    """(motifs interdits partout, motifs interdits en contexte de sauvegarde)."""
    interdits, sites = [], []
    for ligne in texte.splitlines():
        ligne = ligne.split("#", 1)[0].strip()
        genre, _, motif = ligne.partition(":")
        motif = motif.strip()
        if not motif:
            continue
        {"interdit": interdits, "site": sites}.get(genre.strip(), []).append(motif)

    def compiler(motifs: list[str]) -> re.Pattern | None:
        return re.compile("|".join(motifs), re.I) if motifs else None

    return compiler(interdits), compiler(sites)


def charger_regles() -> tuple[re.Pattern | None, re.Pattern | None] | None:
    texte = os.environ.get("PAS_D_INFRA_MOTS")
    if not texte:
        chemin = Path(os.environ.get("PAS_D_INFRA_FICHIER") or FICHIER_PAR_DEFAUT)
        if not chemin.is_file():
            return None
        texte = chemin.read_text(encoding="utf-8")
    return lire_regles(texte)


def controle(texte: str, regles: tuple[re.Pattern | None, re.Pattern | None]) -> list[tuple[int, str]]:
    """Les lignes fautives du texte : (numéro, extrait trouvé)."""
    interdits, sites = regles
    fautes = []
    for numero, ligne in enumerate(texte.splitlines(), 1):
        trouve = interdits.search(ligne) if interdits else None
        if trouve:
            fautes.append((numero, trouve.group(0)))
            continue
        trouve = sites.search(ligne) if sites else None
        if trouve and CONTEXTE.search(ligne):
            fautes.append((numero, trouve.group(0)))
    return fautes


def fichiers_suivis() -> list[Path]:
    sortie = subprocess.run(
        ["git", "ls-files", "-z"], cwd=RACINE, capture_output=True, check=True
    ).stdout
    return [RACINE / nom for nom in sortie.decode("utf-8").split("\0") if nom]


def main(argv: list[str]) -> int:
    regles = charger_regles()
    if regles is None:
        print("SAUTÉ : liste des mots absente (PAS_D_INFRA_MOTS ou ~/.config/benjello-backup/mots-interdits.txt).")
        return 0
    fichiers = [Path(a) for a in argv] if argv else fichiers_suivis()
    total = 0
    for chemin in fichiers:
        try:
            rel = chemin.resolve().relative_to(RACINE).as_posix()
        except ValueError:
            rel = chemin.as_posix()
        if rel in EXEMPTS or not chemin.is_file() or chemin.stat().st_size > TAILLE_MAX:
            continue
        try:
            texte = chemin.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for numero, extrait in controle(texte, regles):
            print(f"{rel}:{numero}: infrastructure de sauvegarde ({extrait!r})")
            total += 1
    if total:
        print(
            f"\n{total} mention(s). Ce dépôt est public : ces notes vont dans le dépôt privé "
            "`tunisia-data`.",
            file=sys.stderr,
        )
        return 1
    print(f"{len(fichiers)} fichier(s) contrôlé(s) : aucune mention de l'infrastructure de sauvegarde.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

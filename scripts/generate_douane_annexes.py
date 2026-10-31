"""Engendre les tableaux des annexes 1 des décrets n° 2012-3410 et n° 2014-2.

Les relevés `precis/fr/fiscalite/douane/annexe1-decret-*.csv` (transcrits du Journal officiel)
donnent, par numéro du système harmonisé, le taux du droit de douane réduit des produits
agricoles et agro-alimentaires. Le script les met en tableaux Markdown sous
`precis/fr/fiscalite/tables/`, que le chapitre « Les droits de douane » inclut.

    uv run python scripts/generate_douane_annexes.py

Le build du site n'exécute pas ce script : il lit les fichiers qu'il produit.
"""
from __future__ import annotations

import csv
from pathlib import Path

RACINE = Path(__file__).parent.parent
RELEVES = RACINE / "precis/fr/fiscalite/douane"
TABLES = RACINE / "precis/fr/fiscalite/tables"
ANNEXES = {
    "annexe1-decret-2012-3410.csv": "droits_douane_annexe1_2013.md",
    "annexe1-decret-2014-2.csv": "droits_douane_annexe1_2014.md",
}


def cellule(texte: str) -> str:
    """Échappe ce qui casserait une cellule de tableau Markdown."""
    return texte.replace("|", "\\|").replace("*", "\\*")


def tableau(csv_path: Path) -> str:
    lignes = list(csv.DictReader(csv_path.open(encoding="utf-8")))
    sortie = [
        f"<!-- Généré par scripts/generate_douane_annexes.py — ne pas éditer à la main.\n"
        f"     Lignes lues dans precis/fr/fiscalite/douane/{csv_path.name}. -->",
        "",
        "| Position | Numéro | Désignation | Taux (%) | Page |",
        "|---|---|---|---:|---:|",
    ]
    for r in lignes:
        numero = f"{r['ex']} {r['numero']}".strip()
        sortie.append(
            f"| {r['position']} | {numero} | {cellule(r['designation'])} | {r['taux']} | {r['page']} |"
        )
    return "\n".join(sortie) + "\n"


def main() -> None:
    for releve, instantane in ANNEXES.items():
        (TABLES / instantane).write_text(tableau(RELEVES / releve), encoding="utf-8")
        print(f"{instantane} écrit")


if __name__ == "__main__":
    main()

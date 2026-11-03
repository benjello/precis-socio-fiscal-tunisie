"""Ajoute aux `references.json` du volume la notice de chaque état financier récupéré sur la page d'une société de la Bourse de Tunis.

    uv run python scripts/notices_etats_bourse.py stb 2012:individuel 2020:consolide …

Une notice par document, « exercice:nature » (ou « exercice:nature:fichier » quand la Bourse a rangé le document sous l'autre nature : STB 2020) : adresse directe de la page de la Bourse (lue dans le catalogue de `tunisia-data`,
`sources/bvmt-etats-financiers-urls.csv`), copie locale, taille et somme de contrôle (calculées sur le fichier).
Clé : `bvmt-ef-<société>-<exercice>-<nature>`. Les notices existantes ne sont pas réécrites.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import sys
from pathlib import Path

DONNEES = (
    Path(os.environ.get("TUNISIA_DATA", "~/projets/tunisia-data")).expanduser()
    / "data/raw/entreprises-publiques"
)
CATALOGUE = Path(
    "~/projets/tunisia-data-wt-arch/sources/bvmt-etats-financiers-urls.csv"
).expanduser()
LIVRE = (
    Path(__file__).resolve().parent.parent
    / "precis/fr/entreprises_publiques/references.json"
)
# dossier de la société sous bvmt-etats-financiers : (clé courte des notices, éditeur)
EDITEURS = {
    "stb": ("stb", "Société tunisienne de banque"),
    "bh-bank": ("bh", "Banque de l'habitat"),
    "bna": ("bna", "Banque nationale agricole"),
    "star": ("star", "Société tunisienne d'assurances et de réassurances"),
    "bte-adp": ("bte", "Banque de Tunisie et des Emirats"),
    "tunis-re": ("tunisre", "Société tunisienne de réassurance"),
}


def main(arguments: list[str]) -> int:
    societe, documents = arguments[0], arguments[1:]
    court, editeur = EDITEURS[societe]
    with CATALOGUE.open(encoding="utf-8", newline="") as source:
        urls = {r["fichier"]: r for r in csv.DictReader(source)}
    donnees = json.loads(LIVRE.read_text(encoding="utf-8"))
    existants = {e["id"] for e in donnees["items"]}
    ajoutes = 0
    for document in documents:
        exercice, nature, *autre = document.split(":")
        fichier_nature = autre[0] if autre else nature
        cle = f"bvmt-ef-{court}-{exercice}-{nature}"
        if cle in existants:
            continue
        fichier = f"bvmt-etats-financiers/{societe}/{exercice}_{fichier_nature}.pdf"
        contenu = (DONNEES / fichier).read_bytes()
        origine = urls["entreprises-publiques/" + fichier]["url_origine"]
        genre = "États financiers " + (
            "consolidés" if nature == "consolide" else "individuels"
        )
        donnees["items"].append(
            {
                "id": cle,
                "type": "report",
                "title": f"{genre} {exercice}",
                "author": [{"literal": editeur}],
                "publisher": editeur,
                "publisher-place": "Tunis",
                "issued": {"date-parts": [[int(exercice)]]},
                "accessed": {"date-parts": [[2026, 11, 3]]},
                "title-short": f"{editeur}, {genre.lower()} {exercice}",
                "URL": origine,
                "archive": "Bourse de Tunis",
                "archive_location": origine,
                "note": (
                    f"citation-key: {cle}\n{genre} de l'exercice {exercice}, "
                    "page de la société sur le site de la Bourse de Tunis. "
                    f"Copie locale : tunisia-data/data/raw/entreprises-publiques/{fichier} "
                    f"({len(contenu)} octets, SHA-256 {hashlib.sha256(contenu).hexdigest()}), ignorée par git. "
                    "Cité pour : opinion des commissaires aux comptes et périmètre de consolidation. "
                    "Preuve : couche texte du PDF, lue par scripts/opinions_cac.py et scripts/perimetres_groupes_bancaires.py."
                ),
            }
        )
        ajoutes += 1
    LIVRE.write_text(
        json.dumps(donnees, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"{ajoutes} notices ajoutées.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

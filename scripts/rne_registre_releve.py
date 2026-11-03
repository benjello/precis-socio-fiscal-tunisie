"""Relève, pour les entreprises publiques du précis, ce que le Registre national des entreprises affiche sans compte.

Le portail `https://www.registre-entreprises.tn/rne-public/` donne gratuitement, pour chaque
société ou établissement, son identifiant, sa forme juridique, l'état du registre et la liste des
documents déposés (nature, date, exercice pour un état financier), sans le contenu des documents.
L'inventaire est fait ailleurs, en parcours de visiteur : `tunisia-data/sources/rne-fiches.csv` et
`rne-documents.csv` (branche `donnees/rne-inventaire`, script `rne_inventaire.py`). Ce script n'en
reprend que ce que le volume montre, et n'écrit rien d'autre :

    uv run python scripts/rne_registre_releve.py

Sortie : `precis/fr/entreprises_publiques/listes/entreprises-publiques-registre.csv`, une ligne par
entreprise.

  entreprise, sigle, id_unique   nom du précis, sigle, identifiant du Registre
  forme_juridique, etat_registre tels que le portail les imprime
  exercices_etats_financiers     exercices dont un état financier est déposé (liste séparée par des espaces)
  pv_dirigeants, pv_capital      nombre de procès-verbaux de modification dont l'opération est une mise à
                                 jour des dirigeants, un changement de capital (contenu payant, non lu)
  documents                      nombre de documents listés
"""

from __future__ import annotations

import csv
import os
from pathlib import Path

SOURCES = (
    Path(os.environ.get("TUNISIA_DATA", "~/projets/tunisia-data")).expanduser()
    / "sources"
)
SORTIE = (
    Path(__file__).resolve().parent.parent
    / "precis/fr/entreprises_publiques/listes/entreprises-publiques-registre.csv"
)


def lire(nom: str) -> list[dict[str, str]]:
    with (SOURCES / nom).open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def main() -> int:
    fiches = lire("rne-fiches.csv")
    documents = lire("rne-documents.csv")
    lignes = []
    for fiche in fiches:
        propres = [d for d in documents if d["id_unique"] == fiche["id_unique"]]
        dirigeants = sum(
            "Mise à jour des dirigeants" in d["operation"] for d in propres
        )
        capital = sum("Changement de capital" in d["operation"] for d in propres)
        lignes.append(
            [
                fiche["entreprise"],
                fiche["sigle"],
                fiche["id_unique"],
                fiche["forme_juridique"],
                fiche["etat_registre"],
                fiche["exercices_etats_financiers"],
                dirigeants,
                capital,
                fiche["nb_documents"],
                fiche["consulte"],
            ]
        )
    lignes.sort(key=lambda ligne: ligne[0].lower())
    with SORTIE.open("w", encoding="utf-8", newline="") as sortie:
        ecrivain = csv.writer(sortie)
        ecrivain.writerow(
            [
                "entreprise",
                "sigle",
                "id_unique",
                "forme_juridique",
                "etat_registre",
                "exercices_etats_financiers",
                "pv_dirigeants",
                "pv_capital",
                "documents",
                "consulte",
            ]
        )
        ecrivain.writerows(lignes)
    deposent = sum(1 for ligne in lignes if ligne[5])
    print(
        f"{len(lignes)} entreprises, dont {deposent} avec au moins un état financier déposé."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

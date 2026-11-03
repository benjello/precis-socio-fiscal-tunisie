"""Ajoute aux `references.json` du volume la notice de chaque rapport récupéré dans l'Internet Archive.

Une notice par document de `SPECS` : titre, éditeur, exercice, adresse de la capture (lue dans le
catalogue de `tunisia-data`, `sources/bvmt-rapports-archives-urls.csv`), copie locale, taille et somme de
contrôle (calculées sur le fichier). Les notices existantes ne sont pas réécrites.

    uv run python scripts/notices_rapports_archives.py [--catalogue chemin.csv]

Pour une nouvelle entreprise : ajouter ses documents à `SPECS`, relancer, puis lancer le relevé qui les lit.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path

DONNEES = (
    Path(os.environ.get("TUNISIA_DATA", "~/projets/tunisia-data")).expanduser()
    / "data/raw/entreprises-publiques"
)
CATALOGUE = Path(
    "~/projets/tunisia-data-wt-arch/sources/bvmt-rapports-archives-urls.csv"
).expanduser()
LIVRE = (
    Path(__file__).resolve().parent.parent
    / "precis/fr/entreprises_publiques/references.json"
)
# clé, éditeur, exercice, fichier sous bvmt-rapports-archives, objet cité, type de document
SPECS = [
    (
        "ra-stb-2016",
        "Société tunisienne de banque",
        2016,
        "stb/20211103_Rapport_fr_STB_2016.pdf",
        "opinion des commissaires aux comptes de l'exercice 2016",
    ),
    (
        "ra-stb-2019",
        "Société tunisienne de banque",
        2019,
        "stb/20211103_Rapport_2019_FRANCAIS.pdf",
        "opinion des commissaires aux comptes de l'exercice 2019",
    ),
    (
        "ra-bna-2007",
        "Banque nationale agricole",
        2007,
        "bna/20190711_rapport_annuel_2007_fr.pdf",
        "périmètre de consolidation au 31 décembre 2007",
        "Rapport annuel",
    ),
    (
        "ra-bna-2020",
        "Banque nationale agricole",
        2020,
        "bna/20260317_États_financiers_consolidés_au_31_décembre_2020.pdf",
        "périmètre de consolidation au 31 décembre 2020",
        "États financiers consolidés",
    ),
    (
        "ra-stb-2011",
        "Société tunisienne de banque",
        2011,
        "stb/20211103_Rapport_STB_Fr__2011.pdf",
        "périmètre de consolidation aux 31 décembre 2010 et 2011",
    ),
    (
        "ra-stb-2013",
        "Société tunisienne de banque",
        2013,
        "stb/20211103_Rapport_STB_Fr_2013.pdf",
        "périmètre de consolidation aux 31 décembre 2012 et 2013",
    ),
    (
        "ra-stb-2014",
        "Société tunisienne de banque",
        2014,
        "stb/20211103_Rapport_STB_Fr_2014.pdf",
        "périmètre de consolidation aux 31 décembre 2013 et 2014",
    ),
    (
        "ra-stb-2015",
        "Société tunisienne de banque",
        2015,
        "stb/20211103_Rapport_STB_Fr__2015.pdf",
        "périmètre de consolidation aux 31 décembre 2014 et 2015",
    ),
    (
        "ra-stb-2017",
        "Société tunisienne de banque",
        2017,
        "stb/20230228_Rapport_STB_Fr_2017.pdf",
        "périmètre de consolidation aux 31 décembre 2016 et 2017",
    ),
    (
        "ra-stb-2018",
        "Société tunisienne de banque",
        2018,
        "stb/20211103_STB_RAPPORT_2018_FRANÇAIS.pdf",
        "périmètre de consolidation aux 31 décembre 2017 et 2018",
    ),
]


def main() -> int:
    analyseur = argparse.ArgumentParser(description=(__doc__ or "").split("\n")[0])
    analyseur.add_argument("--catalogue", type=Path, default=CATALOGUE)
    options = analyseur.parse_args()
    with options.catalogue.open(encoding="utf-8", newline="") as source:
        urls = {r["fichier"]: r for r in csv.DictReader(source)}
    donnees = json.loads(LIVRE.read_text(encoding="utf-8"))
    existants = {e["id"] for e in donnees["items"]}
    ajoutes = 0
    for cle, editeur, exercice, fichier, objet, *reste in SPECS:
        genre = reste[0] if reste else "Rapport annuel"
        if cle in existants:
            continue
        chemin = DONNEES / "bvmt-rapports-archives" / fichier
        ligne = urls.get("entreprises-publiques/bvmt-rapports-archives/" + fichier, {})
        contenu = chemin.read_bytes()
        capture = ligne.get("url_archive", "")
        date = capture.split("/web/")[1][:8] if "/web/" in capture else ""
        donnees["items"].append(
            {
                "id": cle,
                "type": "report",
                "title": f"{genre} {exercice}",
                "author": [{"literal": editeur}],
                "publisher": editeur,
                "publisher-place": "Tunis",
                "issued": {"date-parts": [[exercice]]},
                "accessed": {"date-parts": [[2026, 11, 3]]},
                "title-short": f"{editeur}, {genre.lower()} {exercice}",
                "URL": capture or ligne.get("url_origine", ""),
                "archive": "Internet Archive (Wayback Machine)",
                "archive_location": ligne.get("url_origine", ""),
                "note": (
                    f"citation-key: {cle}\n{genre} de l'exercice {exercice}, "
                    f"consulté dans la capture de l'Internet Archive du {date[6:8]}/{date[4:6]}/{date[:4]} du site de l'éditeur. "
                    f"Copie locale : tunisia-data/data/raw/entreprises-publiques/bvmt-rapports-archives/{fichier} "
                    f"({len(contenu)} octets, SHA-256 {hashlib.sha256(contenu).hexdigest()}), ignorée par git. "
                    f"Cité pour : {objet}. Preuve : couche texte du PDF, tableau lu ligne à ligne par scripts/perimetres_groupes_bancaires.py."
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
    raise SystemExit(main())

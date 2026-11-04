"""Ajoute aux `references.json` du volume la notice de chaque document du catalogue des rapports du secteur financier.

    uv run python scripts/notices_rapports_finance.py

Lit `precis/fr/entreprises_publiques/listes/inventaire-rapports-finance.csv` (BFPME, BTS, CPSCL : rapports annuels, états
financiers, extraits du rapport des commissaires aux comptes). Clés : `ra-<sigle>-<exercice>` (rapport annuel ou
d'activité), `es-<sigle>-<exercice>` (états financiers publiés par l'entreprise), `bvmt-ef-<sigle>-<exercice>-individuel`
(états financiers de la page de la société à la Bourse de Tunis). Les notices existantes ne sont pas réécrites.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent / "precis/fr/entreprises_publiques"
CATALOGUE = RACINE / "listes/inventaire-rapports-finance.csv"
LIVRE = RACINE / "references.json"
DOSSIER = "tunisia-data/data/raw/entreprises-publiques/rapports-entreprises/"
EDITEURS = {
    "BFPME": "Banque de financement des petites et moyennes entreprises",
    "BTS": "Banque tunisienne de solidarité",
    "CPSCL": "Caisse des prêts et de soutien des collectivités locales",
}
GENRES = {
    "rapport_annuel": (
        "ra",
        "Rapport annuel",
        "rapport annuel de l'exercice {ex}, publié sur le site de l'éditeur",
    ),
    "rapport_activite": (
        "ra",
        "Rapport d'activité",
        "rapport d'activité de l'exercice {ex}, publié sur le site de l'éditeur",
    ),
    "etats_financiers": (
        "es",
        "États financiers",
        "états financiers de l'exercice {ex}, publiés sur le site de l'éditeur",
    ),
    "etats_financiers_cmf": (
        "cmf-ef",
        "États financiers",
        "états financiers de l'exercice {ex}, extrait du Bulletin officiel du Conseil du marché financier publié sur le site du CMF",
    ),
    "etats_financiers_bourse": (
        "bvmt-ef",
        "États financiers individuels",
        "états financiers individuels de l'exercice {ex}, page de la société sur le site de la Bourse de Tunis",
    ),
}
# précisions propres à un document : (sigle, exercice, nature) -> phrase ajoutée à la note
PRECISIONS = {
    ("BFPME", "2013", "etats_financiers_cmf"): (
        "Document scanné, sans couche texte : lu par reconnaissance de caractères (tesseract, français), "
        "page 24 relue sur l'image."
    ),
    ("BFPME", "2006", "etats_financiers_cmf"): (
        "Rapport en arabe (Bulletin officiel n° 2880 du 28 juin 2007) : lu sur la couche texte du PDF, "
        "page 10 relue sur l'image."
    ),
    ("BTS", "2016", "rapport_annuel"): (
        "La couche texte de ce PDF confond certains chiffres (« 1016 » pour 2016, « 18 435 » pour 28 435) : "
        "les nombres cités (pages 46 et 47) ont été relus sur l'image de la page."
    ),
    (
        "BTS",
        "2017",
        "rapport_annuel",
    ): "Les nombres cités page 53 ont été relus sur l'image de la page.",
    (
        "BTS",
        "2018",
        "etats_financiers_bourse",
    ): "Les nombres cités pages 26 et 27 ont été relus sur l'image de la page.",
    (
        "BFPME",
        "2016",
        "etats_financiers_bourse",
    ): "Les nombres cités page 20 ont été relus sur l'image de la page.",
    ("BFPME", "2022", "etats_financiers_bourse"): (
        "La Bourse intitule ce document « états financiers annuels au 19/07/2024 » et le dit arrêté au 31 décembre 2023 ; "
        "le fichier contient les états arrêtés au 31 décembre 2022, rapport des commissaires du 12 juillet 2024."
    ),
}
# pages de sites qui annoncent les documents : (clé, éditeur, titre, adresse, fichier local, ce que la page montre)
PAGES = [
    (
        "cpscl-publications",
        "Caisse des prêts et de soutien des collectivités locales",
        "Publications et rapports",
        "http://www.cpscl.com.tn/template.php?code_menu=147",
        "_pages/cpscl-publications.html",
        "les pages 1 à 10 de la liste (concaténées dans la copie locale) : « états financiers arrêtés au 31/12/N et extrait du rapport du commissaire aux comptes » pour chaque exercice de 2006 à 2024, trois rapports d'activité de la caisse (2015, 2016, 2018) et, de 2018 à 2024, les rapports d'activité de la cellule de gouvernance",
    ),
    (
        "bts-informations-financieres",
        "Banque tunisienne de solidarité",
        "Informations financières",
        "https://www.bts.com.tn/infos-financiers",
        "_pages/bts-informations-financieres.html",
        "dix rapports d'activité (2016 à 2025) et cinq états financiers (2021 à 2025) en PDF ; aucun document antérieur à 2016",
    ),
    (
        "bfpme-publications",
        "Banque de financement des petites et moyennes entreprises",
        "Publications",
        "https://www.bfpme.com.tn/fr/publications",
        "_pages/bfpme-publications.html",
        "trois rapports annuels d'activités (2020, 2022, 2023), chacun avec un lien vide (href=\"\") : aucun fichier n'est joint",
    ),
]
CITE_POUR = {
    "oui": "opinion des commissaires aux comptes",
    "non": "états financiers publiés par l'entreprise (le rapport des commissaires n'y figure pas)",
    "arabe": "existence du document (en arabe, rapport des commissaires non lu)",
    "non lu": "existence du document (rapport des commissaires non lu)",
}


def _cite_pour(cac: str, nature: str, sigle: str) -> str:
    if cac.startswith("oui") and nature == "etats_financiers" and sigle == "CPSCL":
        return "opinion du réviseur des comptes (extrait du rapport général, page 2)"
    for debut, texte in CITE_POUR.items():
        if cac.startswith(debut):
            return texte
    return "existence du document"


def notices(lignes: list[dict[str, str]], existants: set[str]) -> list[dict]:
    """Une notice par ligne du catalogue, sauf si la clé existe déjà."""
    neuves = []
    for ligne in lignes:
        if not ligne["fichier"]:  # document signalé, non récupéré : pas de notice
            continue
        sigle, ex, nature = ligne["sigle"], ligne["exercice"], ligne["nature"]
        prefixe, genre, description = GENRES[nature]
        cle = f"{prefixe}-{sigle.lower()}-{ex}" + (
            "-individuel" if prefixe == "bvmt-ef" else ""
        )
        if cle in existants:
            continue
        editeur = EDITEURS[sigle]
        capture = ligne["url_archive"]
        origine = ligne["url_origine"]
        annee, mois, jour = (int(x) for x in ligne["consultation"].split("-"))
        notice = {
            "id": cle,
            "type": "report",
            "title": f"{genre} {ex}",
            "author": [{"literal": editeur}],
            "publisher": editeur,
            "publisher-place": "Tunis",
            "issued": {"date-parts": [[int(ex)]]},
            "accessed": {"date-parts": [[annee, mois, jour]]},
            "title-short": f"{sigle}, {genre.lower()} {ex}",
            "URL": origine if nature == "etats_financiers_cmf" else capture or origine,
        }
        if nature == "etats_financiers_cmf":
            notice["archive"] = "Conseil du marché financier"
            notice["archive_location"] = origine
        elif capture:
            notice["archive"] = "Internet Archive (Wayback Machine)"
            notice["archive_location"] = origine
        elif nature == "etats_financiers_bourse":
            notice["archive"] = "Bourse de Tunis"
            notice["archive_location"] = origine
        note = (
            f"citation-key: {cle}\n{description.format(ex=ex)[0].upper() + description.format(ex=ex)[1:]}. "
            f"Copie locale : {DOSSIER}{ligne['fichier']} ({ligne['octets']} octets, SHA-256 {ligne['sha256']}), "
            f"ignorée par git. Cité pour : {_cite_pour(ligne['rapport_cac'], nature, sigle)}. "
            "Preuve : couche texte du PDF (pdftotext)."
        )
        if capture and nature == "etats_financiers_cmf":
            note += f" Le même fichier (même somme de contrôle) est sur le site de la banque : capture {capture}."
        precision = PRECISIONS.get((sigle, ex, nature))
        if precision:
            note += " " + precision
        notice["note"] = note
        neuves.append(notice)
    return neuves


def notices_pages(existants: set[str]) -> list[dict]:
    """Une notice par page de site listée dans PAGES."""
    racine = Path(os.environ.get("TUNISIA_DATA", "~/projets/tunisia-data")).expanduser()
    neuves = []
    for cle, editeur, titre, url, fichier, contenu in PAGES:
        if cle in existants:
            continue
        octets = (
            racine / "data/raw/entreprises-publiques/rapports-entreprises" / fichier
        ).read_bytes()
        neuves.append(
            {
                "id": cle,
                "type": "webpage",
                "title": f"{titre} : {editeur}",
                "author": [{"literal": editeur}],
                "publisher": editeur,
                "publisher-place": "Tunis",
                "accessed": {"date-parts": [[2026, 11, 4]]},
                "title-short": f"{editeur}, {titre.lower()}",
                "URL": url,
                "note": (
                    f"citation-key: {cle}\nPage publique du site, lue le 4 novembre 2026 : {contenu}. "
                    f"Copie locale : tunisia-data/data/raw/entreprises-publiques/rapports-entreprises/{fichier} "
                    f"({len(octets)} octets, SHA-256 {hashlib.sha256(octets).hexdigest()}), ignorée par git."
                ),
            }
        )
    return neuves


def main() -> int:
    with CATALOGUE.open(encoding="utf-8", newline="") as source:
        lignes = [r for r in csv.DictReader(source) if r["nature"] in GENRES]
    donnees = json.loads(LIVRE.read_text(encoding="utf-8"))
    existants = {e["id"] for e in donnees["items"]}
    neuves = notices(lignes, existants) + notices_pages(existants)
    donnees["items"].extend(neuves)
    LIVRE.write_text(
        json.dumps(donnees, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"{len(neuves)} notices ajoutées.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Table de correspondance instrument / institution / législation.

La page `precis/fr/correspondance-instruments.qmd` donne, pour chaque instrument documenté
dans les livres, l'organisme qui le gère, le ou les textes qui l'ont fondé et le chapitre où il
se lit. Elle ne recopie rien : les références de loi sont des citations de `references.json`, les chapitres sont des liens.

POURQUOI UN CSV : une ligne par instrument, éditable à la main, vérifiable par un test (clé
bibliographique existante, fichier et ancre existants). Une institution laissée vide signifie
qu'aucun chapitre ne la nomme pour cet instrument.

POURQUOI DU PYTHON PUR : les tests du dépôt tournent `--isolated --no-project`.

FORMAT DU CSV (`precis/fr/correspondance-instruments.csv`)
  groupe       identifiant du groupe (voir GROUPES)
  instrument   nom de l'instrument
  institution  organisme qui le gère, tel que le nomme le chapitre ; vide si non établi
  textes       clés de `references.json`, séparées par « ; », chacune suivie au besoin de
               « |locator » (« lf-2026|art. 88 ») ; un élément commençant par « = » est du texte
  chapitres    « Livre — Chapitre|fichier.html#ancre », séparés par « ; »
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

RACINE_FR = Path(__file__).resolve().parent.parent / "precis" / "fr"
CSV = RACINE_FR / "correspondance-instruments.csv"

GROUPES = {
    "impots": "Impôts, taxes et douane",
    "secu": "Sécurité sociale et assistance",
    "travail": "Travail et rémunérations",
    "autres": "Prix, entreprises publiques, collectivités et enseignement",
}


def lire(chemin: Path = CSV) -> list[dict]:
    with open(chemin, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def references(racine: Path = RACINE_FR) -> dict[str, dict]:
    """Toutes les entrées bibliographiques du fonds commun et des livres, par clé."""
    ids: dict[str, dict] = {}
    for fichier in [racine / "references.json", *sorted(racine.glob("*/references.json"))]:
        for x in json.loads(fichier.read_text(encoding="utf-8"))["items"]:
            ids.setdefault(x["id"], x)
    return ids


def elements(textes: str) -> list[tuple[str, str | None, bool]]:
    """Découpe la colonne `textes` en (clé ou texte, locator, est_texte)."""
    sortie = []
    for brut in (t.strip() for t in textes.split(";") if t.strip()):
        if brut.startswith("="):
            sortie.append((brut[1:].strip(), None, True))
            continue
        cle, _, locator = brut.partition("|")
        sortie.append((cle.strip(), locator.strip() or None, False))
    return sortie


def chapitres(valeur: str) -> list[tuple[str, str]]:
    sortie = []
    for brut in (c.strip() for c in valeur.split(";") if c.strip()):
        libelle, _, cible = brut.partition("|")
        sortie.append((libelle.strip(), cible.strip()))
    return sortie


def cellule_textes(textes: str) -> str:
    """Une citation par texte : la feuille de style imprime l'intitulé et la date."""
    parties = []
    for cle, locator, est_texte in elements(textes):
        if est_texte:
            parties.append(cle)
        else:
            parties.append(f"[@{cle}, {locator}]" if locator else f"[@{cle}]")
    return "<br>".join(parties)


def cellule_chapitres(valeur: str) -> str:
    return "<br>".join(f"[{libelle}]({cible})" for libelle, cible in chapitres(valeur))


def tableau(groupe: str, lignes: list[dict]) -> str:
    sortie = ["| Instrument | Institution | Texte(s) fondateur(s) | Chapitre |", "|---|---|---|---|"]
    for ligne in lignes:
        if ligne["groupe"] != groupe:
            continue
        sortie.append(
            "| {} | {} | {} | {} |".format(
                ligne["instrument"],
                ligne["institution"],
                cellule_textes(ligne["textes"]),
                cellule_chapitres(ligne["chapitres"]),
            )
        )
    return "\n".join(sortie)


def imprime(groupe: str, chemin: Path = CSV) -> None:
    """Émet le tableau d'un groupe, pour un bloc `output: asis`."""
    print(tableau(groupe, lire(chemin)))

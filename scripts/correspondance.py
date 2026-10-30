"""Ébauche de la table de correspondance instrument / institution / législation.

Page non publiée, produite pour relecture : `precis/fr/correspondance-instruments.qmd` donne,
pour chaque instrument décrit dans les livres, sa catégorie juridique, l'organisme qui le gère,
le texte fondateur, les principaux modificatifs, le texte d'application principal, le statut du
texte fondateur lorsqu'il est abrogé, et le chapitre où il se lit. Rien n'est recopié des
chapitres : les références de loi sont des citations de `references.json`, les chapitres sont
des liens.

CHOIX DE FORME (proposés à la relectrice, version par défaut) : une ligne par instrument (A1) ;
classement par famille de droit (B1) ; fondateur et trois ou quatre principaux modificatifs (C2) ;
statut du texte seulement quand le fondateur est abrogé (D2) ; catégorie juridique (E1) et texte
d'application principal (E5) ; instruments déjà décrits dans les livres en ligne (F1).

POURQUOI UN CSV : une ligne par instrument, éditable à la main, vérifiable par un test (clé
bibliographique existante, fichier et ancre existants). Une institution laissée vide signifie
qu'aucun chapitre ne la nomme pour cet instrument.

POURQUOI DU PYTHON PUR : les tests du dépôt tournent `--isolated --no-project`.

FORMAT DU CSV (`precis/fr/correspondance-instruments.csv`)
  famille       identifiant de la famille de droit (voir FAMILLES)
  instrument    nom de l'instrument
  categorie     catégorie juridique
  institution   organisme qui le gère, tel que le nomme le chapitre ; vide si non établi
  fondateur     clés de `references.json`, séparées par « ; », chacune suivie au besoin de
                « |locator » (« lf-2026|art. 88 ») ; un élément commençant par « = » est du texte
  modificatifs  idem ; vide si aucun n'est établi
  application   idem ; vide si aucun n'est établi
  statut        texte libre (Markdown, citations permises) ; seulement si le fondateur est abrogé
  chapitres     « Livre — Chapitre|fichier.html#ancre », séparés par « ; »
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

RACINE_FR = Path(__file__).resolve().parent.parent / "precis" / "fr"
CSV = RACINE_FR / "correspondance-instruments.csv"

FAMILLES = {
    "fiscal": "Droit fiscal et douanier",
    "secu": "Droit de la sécurité sociale",
    "assistance": "Droit de l'assistance",
    "travail": "Droit du travail et de la fonction publique",
    "publiques": "Finances publiques, entreprises publiques et collectivités",
    "enseignement": "Enseignement et formation",
    "prix": "Prix administrés",
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
    """Découpe une colonne de textes en (clé ou texte, locator, est_texte)."""
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
    return "<br>".join(parties) if parties else "à établir"


def cellule_chapitres(valeur: str) -> str:
    return "<br>".join(f"[{libelle}]({cible})" for libelle, cible in chapitres(valeur))


def cellule_vide(valeur: str) -> str:
    return valeur if valeur.strip() else "à établir"


def tableau(famille: str, lignes: list[dict]) -> str:
    sortie = [
        "| Instrument | Catégorie | Institution gestionnaire | Texte de référence | Principaux modificatifs"
        " | Texte d'application | Statut du fondateur | Chapitre du précis |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for ligne in lignes:
        if ligne["famille"] != famille:
            continue
        sortie.append(
            "| {} | {} | {} | {} | {} | {} | {} | {} |".format(
                ligne["instrument"],
                ligne["categorie"],
                cellule_vide(ligne["institution"]),
                cellule_textes(ligne["fondateur"]),
                cellule_textes(ligne["modificatifs"]) if ligne["modificatifs"].strip() else "—",
                cellule_textes(ligne["application"]) if ligne["application"].strip() else "—",
                ligne["statut"].strip() or "—",
                cellule_chapitres(ligne["chapitres"]),
            )
        )
    return "\n".join(sortie)


def imprime(famille: str, chemin: Path = CSV) -> None:
    """Émet le tableau d'une famille, pour un bloc `output: asis`."""
    print(tableau(famille, lire(chemin)))

#!/usr/bin/env python3
"""Le backlog reste lisible : pas de conflit oublié, pas de date future, pas de clé inexistante.

`docs/notes/backlog-precis.md` est tenu à la main par plusieurs agents à la fois. Trois
dérives mécaniques s'y glissent sans que personne les voie, et ce contrôle les refuse :

1. un marqueur de conflit (`<<<<<<<`, `=======`, `>>>>>>>` en début de ligne) laissé par une
   résolution de fusion bâclée ;
2. une date « jour mois année » postérieure à aujourd'hui et proche (90 jours par défaut) :
   une date de lecture ou de rédaction ne peut pas être dans l'avenir. Une date légale future
   voulue (une entrée en vigueur annoncée) se garde en ajoutant `<!-- futur-ok -->` à la fin de
   la ligne ; les dates lointaines (au-delà de la fenêtre) ne sont pas regardées ;
3. une clé de citation (`[@clé]` ou `clé` entre accents graves, d'un type de texte : loi,
   décret, décret-loi, loi de finances, arrêté, avis, note commune) qui n'existe dans aucun
   `references.json` : la clé est fautive, ou une renommée n'a pas suivi. Les lignes qui
   écrivent une correspondance « ancienne clé → nouvelle clé » ne sont pas regardées.

    uv run python scripts/check_backlog.py                      # sort 1 et liste les écarts
    uv run python scripts/check_backlog.py --fenetre 30         # fenêtre de dates plus courte
    uv run python scripts/check_backlog.py --ignorer-dates      # saute le contrôle des dates
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
BACKLOG = RACINE / "docs" / "notes" / "backlog-precis.md"

MOIS = [
    "janvier", "février", "mars", "avril", "mai", "juin",
    "juillet", "août", "septembre", "octobre", "novembre", "décembre",
]
DATE = re.compile(
    r"\b(\d{1,2}|1(?:er|\^er\^))\s+(" + "|".join(MOIS) + r")\s+(\d{4})\b"
)
CONFLIT = re.compile(r"^(<<<<<<<|=======$|>>>>>>>)")
EXEMPT_DATE = "<!-- futur-ok -->"
CLE_ACCENTS = re.compile(
    r"`((?:loi|decret|dl|lf|lfc|arrete|avis|dgi|circulaire)[a-z]*[-0-9][A-Za-z0-9_-]*)`"
)
CLE_CROCHETS = re.compile(r"\[@([A-Za-z0-9][A-Za-z0-9_:.-]*[A-Za-z0-9])(?![A-Za-zÀ-ÿ])")


def aujourdhui() -> datetime.date:
    return datetime.date.today()


def cles_connues(racine: Path = RACINE) -> set[str]:
    cles: set[str] = set()
    for fichier in racine.glob("precis/**/references.json"):
        for entree in json.loads(fichier.read_text(encoding="utf-8")).get("items", []):
            cles.add(entree["id"])
    return cles


def date_de(m: re.Match) -> datetime.date | None:
    jour = 1 if m.group(1).startswith("1") and not m.group(1).isdigit() else int(m.group(1))
    try:
        return datetime.date(int(m.group(3)), MOIS.index(m.group(2)) + 1, jour)
    except ValueError:
        return None


def ecarts(
    lignes: list[str],
    connues: set[str] | None,
    aujourd_hui: datetime.date,
    fenetre: int = 90,
    dates: bool = True,
) -> list[str]:
    """Liste des écarts, un message par ligne fautive (numéro de ligne en tête)."""
    sortie: list[str] = []
    limite = aujourd_hui + datetime.timedelta(days=fenetre)
    for numero, ligne in enumerate(lignes, 1):
        if CONFLIT.match(ligne):
            sortie.append(f"ligne {numero} : marqueur de conflit « {ligne[:7]} »")
        if dates and EXEMPT_DATE not in ligne:
            for m in DATE.finditer(ligne):
                d = date_de(m)
                if d is not None and aujourd_hui < d <= limite:
                    sortie.append(
                        f"ligne {numero} : date future « {m.group(0)} » "
                        f"(aujourd'hui {aujourd_hui.isoformat()})"
                    )
        if connues is not None and "→" not in ligne:
            for cle in CLE_ACCENTS.findall(ligne) + CLE_CROCHETS.findall(ligne):
                if cle not in connues and not cle.endswith((".pdf", ".qmd", ".md", ".py")):
                    sortie.append(f"ligne {numero} : clé « {cle} » absente des references.json")
    return sortie


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--fenetre", type=int, default=90, help="jours de dates futures refusées")
    parser.add_argument("--ignorer-dates", action="store_true", help="saute le contrôle des dates")
    parser.add_argument("--ignorer-cles", action="store_true", help="saute le contrôle des clés")
    args = parser.parse_args(argv)

    lignes = BACKLOG.read_text(encoding="utf-8").splitlines()
    connues = None if args.ignorer_cles else cles_connues()
    trouves = ecarts(lignes, connues, aujourdhui(), args.fenetre, not args.ignorer_dates)
    for message in trouves:
        print(f"backlog-precis.md, {message}")
    if trouves:
        print(f"{len(trouves)} écart(s) dans le backlog.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

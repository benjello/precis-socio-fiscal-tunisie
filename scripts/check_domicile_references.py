#!/usr/bin/env python3
"""Domicile unique des références juridiques : contrôle des sections qui l'adoptent.

Dans une section dont le titre porte la classe `.domicile-unique`, la prose ne cite plus un
texte de loi entre crochets : elle le nomme, et le nom porte un lien `[…](#r-…)` vers sa ligne
dans un bloc `.chronologie-repliable`, qui porte la référence complète (texte, article, page).
En HTML, le lien ouvre au survol une infobulle tirée de cette ligne, et le clic y mène, avec un
retour d'un geste (`precis/legendes.html`). La référence ne va pas non plus en note
`^[[@clé…].]` : l'exposant numéroté est réservé au PDF, où il sera tiré du lien lui-même. Ce
contrôle vérifie que la précision n'a pas été perdue en route :

1. dans une telle section, aucun appel `[@clé…]` à une référence de type `legislation` hors d'un
   bloc `.chronologie-repliable` — ni dans le fil de la phrase, ni en note ;
2. tout lien `(#r-…)` d'un fichier mène à une ancre `{#r-…}` du même fichier ;
3. toute ancre `{#r-…}` est dans un bloc `.chronologie-repliable`, sur une ligne qui cite au
   moins une référence.

Les citations d'études (`report`, `article-journal`…) restent permises dans la prose.

Usage : uv run python scripts/check_domicile_references.py [fichiers.qmd…]
Sans argument : tous les `.qmd` de `precis/fr/`. Sort en 1 s'il trouve une erreur.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TITRE = re.compile(r"^(#{1,6})\s.*$")
CLASSE = ".domicile-unique"
CITATION = re.compile(r"@([A-Za-z0-9][A-Za-z0-9_:.-]*[A-Za-z0-9])")
LIEN = re.compile(r"\]\(#(r-[A-Za-z0-9-]+)\)")
ANCRE = re.compile(r"\{#(r-[A-Za-z0-9-]+)[^}]*\}")
RENVOIS = ("tbl-", "fig-", "sec-", "eq-")
# Note en ligne `^[ … ]`, crochets internes d'un niveau compris (`^[[@clé, art. 3].]`) : elle ne
# sert qu'à dire, dans le message, où la citation fautive se trouve.
NOTE = re.compile(r"\^\[(?:[^\[\]]|\[[^\[\]]*\])*\]")


def types_des_references(fichier: Path) -> dict[str, str]:
    """Clé → type CSL, pour le livre du fichier et le fonds commun de sa langue."""
    types: dict[str, str] = {}
    for depot in (fichier.parent / "references.json", fichier.parent.parent / "references.json"):
        if depot.is_file():
            for entree in json.loads(depot.read_text(encoding="utf-8")).get("items", []):
                types[entree["id"]] = entree.get("type", "")
    return types


def controler(fichier: Path, types: dict[str, str] | None = None) -> list[str]:
    types = types_des_references(fichier) if types is None else types
    erreurs: list[str] = []
    liens: list[tuple[int, str]] = []
    ancres: dict[str, tuple[int, bool, bool]] = {}
    niveau_section = 0  # niveau du titre `.domicile-unique` courant, 0 hors d'une telle section
    dans_registre = False
    ouverture = ""
    dans_code = False
    for numero, ligne in enumerate(fichier.read_text(encoding="utf-8").split("\n"), 1):
        if ligne.startswith("```"):
            dans_code = not dans_code
            continue
        if dans_code:
            continue
        titre = TITRE.match(ligne)
        if titre:
            niveau = len(titre.group(1))
            if CLASSE in ligne:
                niveau_section = niveau
            elif niveau_section and niveau <= niveau_section:
                niveau_section = 0
        fermeture = re.fullmatch(r"(:{3,})\s*", ligne)
        if "chronologie-repliable" in ligne and ligne.lstrip().startswith(":::"):
            dans_registre, ouverture = True, re.match(r"\s*(:+)", ligne).group(1)
        elif dans_registre and fermeture and fermeture.group(1) == ouverture:
            dans_registre = False
        cles = [c for c in CITATION.findall(ligne) if not c.startswith(RENVOIS)]
        for ancre in ANCRE.findall(ligne):
            ancres[ancre] = (numero, dans_registre, bool(cles))
        liens += [(numero, cible) for cible in LIEN.findall(ligne)]
        if niveau_section and not dans_registre and not ligne.lstrip().startswith("<!--"):
            for cle in cles:
                if types.get(cle) == "legislation":
                    lieu = "en note" if NOTE.search(ligne) and cle not in CITATION.findall(
                        NOTE.sub("", ligne)) else "dans la prose"
                    erreurs.append(
                        f"{fichier}:{numero} : « @{cle} » cité {lieu} d'une section à domicile "
                        f"unique — nommer le texte et lier ce nom à sa ligne de registre "
                        f"`[…](#r-…)`, sans crochet de citation ni note")
    for numero, cible in liens:
        if cible not in ancres:
            erreurs.append(f"{fichier}:{numero} : lien vers « #{cible} », ancre introuvable")
    for ancre, (numero, au_registre, citee) in ancres.items():
        if not au_registre:
            erreurs.append(f"{fichier}:{numero} : ancre « #{ancre} » hors d'un bloc "
                           f".chronologie-repliable")
        elif not citee:
            erreurs.append(f"{fichier}:{numero} : la ligne de registre « #{ancre} » ne cite "
                           f"aucune référence")
    return erreurs


def main(arguments: list[str]) -> int:
    fichiers = [Path(a) for a in arguments] or sorted((RACINE / "precis" / "fr").rglob("*.qmd"))
    erreurs = [e for f in fichiers for e in controler(f)]
    for erreur in erreurs:
        print(erreur)
    sections = sum(f.read_text(encoding="utf-8").count(CLASSE) for f in fichiers)
    if not erreurs:
        print(f"{sections} section(s) à domicile unique : registres cohérents.")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

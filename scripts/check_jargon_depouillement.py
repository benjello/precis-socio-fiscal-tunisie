"""Le précis dit ce qui est connu, pas comment on l'a cherché : ce contrôle le vérifie.

Voir `AGENTS.md`, « Écrire dans le précis », et `docs/conventions-redaction.md`. Le texte
RENDU ne parle pas du travail de dépouillement : ni « objet seul », ni « non lu », ni
« métadonnées seules », ni les marques `[T]`/`[M]`/`[D]`, ni « consulté sur pièce »,
« lu à l'image », « relu sur le fac-similé », « OCR », « couche texte ». Il dit en clair
ce qui est connu — « seul l'intitulé de ce texte est connu ici », « aucun texte identifié
ne fixe… », « n'est pas établi ici ». Le constat de travail, lui, va dans un
`<!-- TODO (documentaliste) : … -->`.

Même principe que `check_pas_de_modele.py`, dont on reprend `lignes_rendues` : seul
compte ce que le lecteur voit, hors blocs de code et commentaires HTML. Et même
prudence : les mots isolés sont ambigus — « le ministère consulté », « à l'image de la
loi de 1960 », « le plafond n'a pas été relevé », « un organisme à but non lucratif »,
« le fascicule n° 39 », « le contrôle sur pièces » sont du français ou du droit. On s'en
tient donc à des COLLOCATIONS sans ambiguïté, quitte à laisser passer une tournure
inédite, qu'on ajoutera ici.

Deux tournures sont délibérément laissées au texte : « aucun texte n'a été retrouvé au
*Journal officiel* jusqu'au… » et « n'a pas été trouvé », qui énoncent une borne de
connaissance datée — une réserve, pas un récit de dépouillement.

    uv run python scripts/check_jargon_depouillement.py [chemins...]

Sans argument, contrôle les `.qmd` français (l'arabe est engendré depuis eux). Sortie 1
si une tournure subsiste.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from check_pas_de_modele import lignes_rendues  # noqa: E402

RACINE = Path(__file__).parent.parent

A = r"['’]"  # apostrophe droite ou typographique

COLLOCATIONS = [
    # Marques et étiquettes de fiche documentaire.
    r"\bobjets?\s+seuls?\b",
    r"\bmétadonnées\s+seule(?:s|ment)?\b",
    r"\bpar\s+(?:ses\s+|leurs\s+|les\s+)?(?:seules\s+)?métadonnées\b",
    r"\[[TMD]\]",
    # Lire / relire.
    r"\bnon\s+lue?s?\b",
    rf"\bn{A}(?:a|ont|ayant)\s+(?:pas\s+)?(?:été|pu\s+être)\s+(?:re)?lue?s?\b",
    r"\b(?:a|ont)\s+été\s+(?:re)?lue?s?\s+(?:au|à\s+l|dans|sur)\b",
    r"\b(?:aucun|des|les)\s+textes?\s+lus?\b",
    r"\b(?:re)?lue?s?\s+à\s+l['’]image\b",
    r"\b(?:re)?lue?s?\s+(?:au|sur\s+le)\s+(?:fascicule|fac-similé)",
    r"\blue?s?\s+partiellement\b",
    # Consulter.
    r"\bconsulté(?:e|s|es)?\s+sur\s+pièces?\b",
    rf"\bn{A}(?:a|ont|ayant)\s+(?:pas\s+)?(?:été|pu\s+être)\s+consulté",
    r"\b(?:textes?|documents?|décrets?|sources?|publications?|corpus|fac-similé|numéros?)"
    r"(?:\s+\w+)?\s+consulté(?:e|s|es)?\b",
    # Dépouiller, transcrire, océriser.
    r"\bdépouill\w*",
    r"\bnon\s+transcrit",
    rf"\bn{A}(?:a|ont)\s+pas\s+été\s+transcrit",
    r"\breconnaissance\s+optique\b",
    r"\bcouche\s+texte\b",
    r"\bOCR\b",
    r"\bocéris\w*",
]
JARGON = re.compile("|".join(f"(?:{c})" for c in COLLOCATIONS), re.I)


def controle(chemin: Path) -> list[tuple[int, str]]:
    fautes = []
    for numero, ligne in lignes_rendues(chemin):
        trouve = JARGON.search(ligne)
        if trouve:
            fautes.append((numero, trouve.group(0)))
    return fautes


def main(argv: list[str]) -> int:
    if argv:
        fichiers = [Path(a) for a in argv]
    else:
        fichiers = sorted(
            f for f in (RACINE / "precis" / "fr").rglob("*.qmd")
            if not f.name.startswith("_glossaire")
            and "/public/" not in f.as_posix()
            and "/_book/" not in f.as_posix()
        )

    total = 0
    for chemin in fichiers:
        for numero, extrait in controle(chemin):
            try:
                rel = chemin.relative_to(RACINE)
            except ValueError:
                rel = chemin
            print(f"{rel}:{numero} : jargon de dépouillement dans le texte rendu — « {extrait} »")
            total += 1

    if total:
        print()
        print(f"{total} tournure(s) de dépouillement dans le texte rendu.")
        print("Dire ce qui est connu (« seul l'intitulé est connu ici », « n'est pas établi ici »),")
        print("et reporter le constat de travail dans un <!-- TODO (documentaliste) : … -->.")
        return 1

    print(f"{len(fichiers)} fichier(s) contrôlé(s) : aucun jargon de dépouillement dans le texte rendu.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

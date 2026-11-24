#!/usr/bin/env python3
"""Remplacement en masse, relu avant d'être appliqué.

Un remplacement dans des dizaines de fichiers (un terme, un titre, un nom de volume) se faisait par
des scripts jetables, et les éditions exactes échouaient sur les espaces insécables de la
typographie française. Ce script :

- lit un motif (expression régulière Python) où toute espace vaut aussi une espace insécable
  (U+00A0) ou fine insécable (U+202F) ;
- par défaut, n'écrit rien : il liste chaque occurrence avec son contexte (fichier:ligne), pour
  relecture ;
- avec --appliquer, écrit les remplacements et rend le nombre par fichier ;
- n'entre jamais dans `precis/ar/`, `docs/notes/`, `_site/`, `public/`, `.quarto/` ni dans les
  fichiers engendrés (`_glossaire.qmd`, `_glossaire.infobulles.html`, `tables/`,
  `translation_glossary.generated.md`) ; --exclure ajoute des motifs de chemin à écarter.

Usage :
    uv run python scripts/remplacer.py 'du précis\\b' "de l'ouvrage" 'precis/fr/**/*.qmd'
    uv run python scripts/remplacer.py 'du précis\\b' "de l'ouvrage" 'precis/fr/**/*.qmd' --appliquer
"""
from __future__ import annotations

import argparse
import fnmatch
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TOUJOURS_EXCLUS = ["precis/ar/*", "docs/notes/*", "*/_site/*", "*/public/*", "*/.quarto/*",
                   "*_glossaire.qmd", "*_glossaire.infobulles.html", "*/tables/*",
                   "translation_glossary.generated.md"]
ESPACES = "[ \u00a0\u202f]"


def motif_tolerant(motif: str) -> re.Pattern:
    return re.compile(motif.replace(" ", ESPACES).replace(r"\ ", ESPACES))


def fichiers(globs: list[str], exclus: list[str]) -> list[Path]:
    vus: set[Path] = set()
    for g in globs:
        for p in RACINE.glob(g):
            rel = p.relative_to(RACINE).as_posix()
            if p.is_file() and not any(fnmatch.fnmatch(rel, e) for e in exclus):
                vus.add(p)
    return sorted(vus)


def remplacer(motif: re.Pattern, remplacement: str, chemins: list[Path], appliquer: bool):
    total, rapport = 0, []
    for p in chemins:
        texte = p.read_text(encoding="utf-8")
        occ = list(motif.finditer(texte))
        if not occ:
            continue
        total += len(occ)
        for m in occ:
            ligne = texte.count("\n", 0, m.start()) + 1
            debut = max(0, m.start() - 40)
            ctx = texte[debut:m.end() + 40].replace("\n", " ")
            rapport.append(f"{p.relative_to(RACINE)}:{ligne} : …{ctx}…")
        if appliquer:
            p.write_text(motif.sub(remplacement, texte), encoding="utf-8")
    return total, rapport


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("motif")
    ap.add_argument("remplacement")
    ap.add_argument("globs", nargs="+")
    ap.add_argument("--exclure", action="append", default=[])
    ap.add_argument("--appliquer", action="store_true")
    a = ap.parse_args(argv)
    chemins = fichiers(a.globs, TOUJOURS_EXCLUS + a.exclure)
    total, rapport = remplacer(motif_tolerant(a.motif), a.remplacement, chemins, a.appliquer)
    for r in rapport:
        print(r)
    print(f"{total} occurrence(s) dans {len({r.split(':')[0] for r in rapport})} fichier(s)"
          + (" : remplacées." if a.appliquer else " : rien n'est écrit (ajouter --appliquer)."))
    return 0


if __name__ == "__main__":
    sys.exit(main())

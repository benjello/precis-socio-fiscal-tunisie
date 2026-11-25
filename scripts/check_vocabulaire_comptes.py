"""Homogénéité du vocabulaire de comptabilité nationale dans les sources françaises de l'ouvrage.

Table de référence : docs/conventions/vocabulaire-comptes-nationaux.csv (terme retenu, d'après le SCN 2008
en français, paragraphe et page ; variantes à éviter ; terme imprimé par l'INS quand il diffère).

Deux relevés, en avertissement (le script sort toujours avec le code 0) :
1. les variantes à éviter (expression régulière de la colonne `variantes_a_eviter`) ;
2. les opérations nommées différemment d'une page à l'autre : libellé entre guillemets accolé au code
   (« D.61 « Cotisations sociales » », « « Cotisations sociales » (D.61) ») ; les libellés sont comparés sans
   casse, accents ni ponctuation. Un libellé sans guillemets devant un code n'est pas relevé : la phrase qui
   l'entoure (« les comptes le rangent en loyers (D.45) ») le rend trop incertain.

Les glossaires engendrés, les pages-relais et les fichiers sous precis/ar/ ne sont pas lus. Un libellé de
l'INS cité comme tel est légitime : le relevé dit où regarder, il ne corrige rien.

    uv run python scripts/check_vocabulaire_comptes.py [--detail]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TABLE = RACINE / "docs" / "conventions" / "vocabulaire-comptes-nationaux.csv"
FR = RACINE / "precis" / "fr"
CODE = r"(?:[PDB]\.\d+[a-z]?(?:/[PDB]\.\d+[a-z]?)?)"
GUILLEMETS = [re.compile(r"\b(" + CODE + r")\s*«\s*([^»]{3,90}?)\s*»"),
              re.compile(r"«\s*([^»]{3,90}?)\s*»\s*\((" + CODE + r")\)")]
AVANT_CODE = re.compile(r"\b((?:[a-zàâçéèêëîïôûùüÿœ’'-]+ ){1,6}[a-zàâçéèêëîïôûùüÿœ’'-]+) \((" + CODE + r")\)")


VIDES = {"de", "des", "du", "la", "le", "les", "l", "en", "aux", "au", "et", "ou", "un", "une", "a"}


def nettoyer(lib: str) -> str:
    """Retire les mots vides de tête (« de », « la », « aux »…) d'un libellé relevé avant un code."""
    mots = lib.replace("’", "'").split()
    while mots and (mots[0].lower().split("'")[0] in VIDES):
        mots = mots[1:] if "'" not in mots[0] else ([mots[0].split("'", 1)[1]] + mots[1:] if mots[0].split("'", 1)[1] else mots[1:])
    return " ".join(mots)


def norm(t: str) -> str:
    t = "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", t)


def fichiers():
    for p in sorted(FR.rglob("*.qmd")):
        if p.name.startswith("_glossaire") or "/public/" in str(p):
            continue
        yield p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--detail", action="store_true")
    a = ap.parse_args()
    table = list(csv.DictReader(TABLE.open(encoding="utf-8")))
    variantes = [(r["code"] or r["terme_retenu"], re.compile(r["variantes_a_eviter"], re.I), r["terme_retenu"])
                 for r in table if r["variantes_a_eviter"]]
    trouvees = []
    libelles = defaultdict(lambda: defaultdict(set))
    for p in fichiers():
        texte = p.read_text(encoding="utf-8")
        rel = p.relative_to(RACINE)
        for no, ligne in enumerate(texte.splitlines(), 1):
            for code, motif, retenu in variantes:
                if motif.search(ligne):
                    trouvees.append((str(rel), no, code, retenu, ligne.strip()[:100]))
            for rx in GUILLEMETS:
                for m in rx.finditer(ligne):
                    c, lib = (m.group(1), m.group(2)) if rx is GUILLEMETS[0] else (m.group(2), m.group(1))
                    libelles[c][norm(lib)].add((lib, f"{rel}:{no}"))
    multiples = {c: v for c, v in libelles.items() if len(v) > 1}
    if a.detail:
        for f, no, code, retenu, l in trouvees:
            print(f"VARIANTE {f}:{no} [{code} → {retenu}] {l}")
        for c, v in sorted(multiples.items()):
            print(f"LIBELLÉS {c} : " + " | ".join(f"{sorted(x)[0][0]} ({len(x)})" for x in v.values()))
    print(f"{len(table)} termes dans la table ; {len(trouvees)} variante(s) à éviter relevée(s) ; "
          f"{len(multiples)} opération(s) nommée(s) de plusieurs façons")
    return 0


if __name__ == "__main__":
    sys.exit(main())

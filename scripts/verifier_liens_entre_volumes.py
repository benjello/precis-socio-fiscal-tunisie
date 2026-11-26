#!/usr/bin/env python3
"""Vérifie les liens relatifs entre pages de l'ouvrage : fichier cible et ancre.

Les renvois `@sec-…` ne valent qu'à l'intérieur d'un livre ; d'un livre à l'autre, ou depuis
une page générale, l'ouvrage écrit des liens Markdown relatifs vers la page rendue :
`[texte](../<livre>/_<chapitre>.html#<ancre>)` dans un livre, `[texte](<livre>/_<chapitre>.html#…)`
ou `[texte](annexe-pib.html#…)` dans une page générale. Rien ne contrôlait jusqu'ici qu'ils
mènent quelque part : un chapitre renommé ou une ancre changée cassait le lien en silence.

Pour chaque lien, le script retrouve le `.qmd` source de la page visée (`x.html` → `x.qmd`,
dossier `<livre>/` → `<livre>/index.qmd`) et, s'il y a une ancre, la cherche parmi les
identifiants définis dans ce fichier :
  - `{#id}` (titres, blocs, ancres `[]{#id}`), `#| label: id` (figures et tableaux engendrés) ;
  - les identifiants qu'engendre Pandoc pour un titre sans `{#id}` (règle `auto_identifiers`).

Les liens vers une ancre d'un glossaire engendré (`_glossaire.html#g-…`) sont vérifiés comme les
autres, sur le `_glossaire.qmd` engendré. Les liens d'un glossaire français vers le glossaire arabe d'un
volume dont la traduction n'est pas livrée (pas d'`index.qmd` arabe) sont attendus : comptés à part,
ils ne font pas échouer le contrôle.

Usage : uv run python scripts/verifier_liens_entre_volumes.py [--langue fr] [--detail]
Sortie : 0 si tout lien résout, 1 sinon (liste des liens cassés, fichier et ligne).
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PRECIS = RACINE / "precis"

LIEN = re.compile(r"\]\(([^)\s]+?\.html|(?:\.{1,2}/)*[a-z_]+/)(#[^)\s]+)?\)")
ID_ACCOLADE = re.compile(r"\{#([A-Za-z0-9_:.\-]+)")
LABEL = re.compile(r"^\s*#\|\s*label:\s*([A-Za-z0-9_:.\-]+)", re.M)
# étiquette passée en chaîne aux fonctions de tableau ou de figure (`ot.markdown_avec_legende(…, "tbl-x")`)
CHAINE = re.compile(r"[\"']((?:tbl|fig|sec)-[A-Za-z0-9_:.\-]+)[\"']")
TITRE = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.M)


def identifiant_pandoc(titre: str) -> str:
    """Règle `auto_identifiers` de Pandoc (variante Quarto, accents conservés)."""
    t = re.sub(r"\{[^}]*\}\s*$", "", titre)          # attributs finaux
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)     # liens -> texte
    t = re.sub(r"[`*_~]", "", t)                       # emphase, code
    t = t.lower()
    t = "".join(c for c in t if c.isalnum() or c in " _-.")
    t = re.sub(r"\s+", "-", t.strip())
    t = re.sub(r"^[^a-zà-ɏ]+", "", t)          # commence par une lettre
    return t or "section"


IMPORT_FIGURES = re.compile(r"from figures(?:\.ep)? import (\w+) as (\w+)")


def identifiants_par_defaut(qmd: Path, texte: str) -> set[str]:
    """Étiquettes posées par défaut par les fonctions de figures appelées dans la page
    (`def tableau_x(caption, tbl_id: str = "tbl-…")`) : elles n'apparaissent pas dans le `.qmd`."""
    ids = set()
    for module, alias in IMPORT_FIGURES.findall(texte):
        candidats = [qmd.parent / "figures" / f"{module}.py",
                     qmd.parent.parent / "entreprises_publiques" / "figures" / f"{module}.py"]
        src = next((c.read_text(encoding="utf-8") for c in candidats if c.exists()), "")
        for fonction in set(re.findall(rf"\b{re.escape(alias)}\.(\w+)\(", texte)):
            m = re.search(rf"def {re.escape(fonction)}\((.*?)\)\s*(?:->[^:]*)?:", src, re.S)
            if m:
                ids |= set(re.findall(r"(?:tbl|fig)_id\s*(?::\s*str(?:\s*\|\s*None)?)?\s*=\s*[\"']([^\"']+)[\"']", m.group(1)))
    return ids


def identifiants(qmd: Path) -> set[str]:
    texte = qmd.read_text(encoding="utf-8")
    ids = set(ID_ACCOLADE.findall(texte)) | set(LABEL.findall(texte)) | set(CHAINE.findall(texte))
    ids |= identifiants_par_defaut(qmd, texte)
    for _, titre in TITRE.findall(texte):
        if "{#" not in titre:
            ids.add(identifiant_pandoc(titre))
            ids.add(unicodedata.normalize("NFC", identifiant_pandoc(titre)))
    return ids


def cible(source: Path, href: str) -> Path:
    base = (source.parent / href).resolve()
    if href.endswith("/"):
        return base / "index.qmd"
    return base.with_suffix(".qmd")


def controler(langue_dir: Path, racine: Path = RACINE) -> tuple[int, list[str], int]:
    """(nombre de liens, liens cassés, liens attendus vers un arabe non livré)."""
    cache: dict[Path, set[str]] = {}
    casses, total, attendus = [], 0, 0
    for qmd in sorted(langue_dir.rglob("*.qmd")):
        if any(p in {"_site", "public", "_book", ".quarto"} for p in qmd.parts):
            continue
        for n, ligne in enumerate(qmd.read_text(encoding="utf-8").splitlines(), 1):
            for m in LIEN.finditer(ligne):
                href, ancre = m.group(1), (m.group(2) or "")[1:]
                if href.startswith(("http", "/")):
                    continue
                total += 1
                cib = cible(qmd, href)
                rel = qmd.relative_to(racine)
                if not cib.exists():
                    if "/ar/" in href and not (cib.parent / "index.qmd").exists():
                        attendus += 1   # glossaire arabe d'un volume dont la traduction n'est pas livrée
                        continue
                    casses.append(f"{rel}:{n} : {href} — page absente ({cib.relative_to(racine) if cib.is_relative_to(racine) else cib})")
                    continue
                if ancre:
                    ids = cache.setdefault(cib, identifiants(cib))
                    if ancre not in ids:
                        casses.append(f"{rel}:{n} : {href}#{ancre} — ancre absente de {cib.relative_to(racine)}")
    return total, casses, attendus


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--langue", default="fr")
    ap.add_argument("--detail", action="store_true")
    args = ap.parse_args()
    total, casses, attendus = controler(PRECIS / args.langue)
    print(f"{total} lien(s) relatif(s) entre pages ({args.langue}) : {len(casses)} cassé(s) ; "
          f"{attendus} vers la version arabe d'un volume non encore traduit (attendus, non comptés).")
    for c in casses if (args.detail or len(casses) <= 200) else casses[:200]:
        print("  " + c)
    return 1 if casses else 0


if __name__ == "__main__":
    sys.exit(main())

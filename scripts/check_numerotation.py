"""La numérotation des volumes reste celle que Quarto calcule, sans exception écrite à la main.

Quarto numérote d'office les chapitres et leurs sections. Deux choses la dérèglent :

- un `{.unnumbered}` posé sur le titre d'un chapitre : le chapitre sort de la numérotation,
  et un renvoi `@sec-…` vers l'une de ses sections s'affiche « Section 1 », un numéro qui
  ne désigne rien (constaté le 4 octobre 2026) ;
- une partie déclarée par un FICHIER (`part: _branches.qmd`) : Quarto en fait une page sans
  numéro, et les sections qu'elle porte n'en ont pas non plus. Une partie se déclare par
  son seul titre (`part: "Les branches, une à une"`) ; son texte va dans un chapitre.

Les annexes (`appendices:`) ne sont pas concernées : le glossaire et la bibliographie y
restent hors numérotation.

    uv run python scripts/check_numerotation.py      # code 1 et la liste des écarts
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
RE_TITRE = re.compile(r"^# .*\{[^}]*\.unnumbered[^}]*\}", re.M)


def _chapitres(entrees: list | None, livre: Path, ecarts: list[str]) -> list[Path]:
    fichiers = []
    for e in entrees or []:
        if isinstance(e, str):
            fichiers.append(livre / e)
        elif isinstance(e, dict) and "part" in e:
            if str(e["part"]).endswith(".qmd"):
                ecarts.append(f"{livre.name} : partie déclarée par un fichier ({e['part']}) — "
                              "déclarer la partie par son titre et mettre son texte dans un chapitre")
            fichiers += _chapitres(e.get("chapters"), livre, ecarts)
    return fichiers


def ecarts_du_livre(livre: Path) -> list[str]:
    config = yaml.safe_load((livre / "_quarto.yml").read_text(encoding="utf-8"))
    ecarts: list[str] = []
    for f in _chapitres(config.get("book", {}).get("chapters"), livre, ecarts):
        if f.exists() and RE_TITRE.search(f.read_text(encoding="utf-8")):
            ecarts.append(f"{livre.name}/{f.name} : chapitre marqué {{.unnumbered}} — "
                          "retirer la marque, la numérotation est celle de Quarto")
    return ecarts


def main() -> int:
    ecarts = []
    for config in sorted((RACINE / "precis" / "fr").glob("*/_quarto.yml")):
        ecarts += ecarts_du_livre(config.parent)
    for e in ecarts:
        print(e)
    return 1 if ecarts else 0


if __name__ == "__main__":
    sys.exit(main())

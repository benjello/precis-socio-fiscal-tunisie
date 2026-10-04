"""La numérotation des volumes reste celle que Quarto calcule, et elle se lit sans trou.

Quarto numérote d'office les chapitres et leurs sections. Ce contrôle refuse ce qui dérègle
cette numérotation ou la rend illisible :

1. un `{.unnumbered}` posé sur le titre d'un chapitre : le chapitre sort de la
   numérotation, et un renvoi `@sec-…` vers l'une de ses sections s'affiche « Section 1 »,
   un numéro qui ne désigne rien (constaté le 4 octobre 2026) ;
2. une partie (`part:`) : en HTML, Quarto ne numérote jamais les parties, qui s'intercalent
   sans numéro entre des chapitres numérotés. Les volumes n'en ont donc pas : les chapitres
   se suivent à plat, et l'introduction du volume annonce leurs regroupements (décision
   du 4 octobre 2026) ;
3. un saut de niveau (`###` directement sous `#`) : la numérotation continue dans la
   sous-section sans que la section qui devrait la contenir soit comptée ;
4. un titre plus profond que `number-depth` : il reste sans numéro au milieu de sections
   numérotées ;
5. une section qui n'a qu'une seule sous-section, quel que soit son niveau : une division
   en un seul morceau n'en est pas une. La sous-section remonte d'un niveau, ou la section
   reçoit une seconde sous-section.

Les fichiers inclus (`{{< include … >}}`) sont lus à leur place. Les annexes
(`appendices:`) n'entrent que dans les règles 3 à 5 : le glossaire et la bibliographie y
restent hors numérotation.

    uv run python scripts/check_numerotation.py      # code 1 et la liste des écarts
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
RE_TITRE = re.compile(r"^(#{1,6}) +(.*)$")
RE_INCLUDE = re.compile(r"^\{\{<\s*include\s+(\S+)\s*>\}\}\s*$")


def _fichiers(entrees: list | None, livre: Path, ecarts: list[str]) -> list[Path]:
    fichiers = []
    for e in entrees or []:
        if isinstance(e, str):
            fichiers.append(livre / e)
        elif isinstance(e, dict) and "part" in e:
            ecarts.append(f"{livre.name} : partie « {e['part']} » — Quarto ne la numérote pas ; "
                          "mettre ses chapitres à plat et annoncer le regroupement dans l'introduction")
            fichiers += _fichiers(e.get("chapters"), livre, ecarts)
    return fichiers


def titres(fichier: Path, _vus: frozenset = frozenset()) -> list[tuple[int, str, str]]:
    """[(niveau, titre, « fichier:ligne »)] hors blocs de code, inclusions développées."""
    sortie: list[tuple[int, str, str]] = []
    if fichier in _vus or not fichier.exists():
        return sortie
    code = False
    for n, ligne in enumerate(fichier.read_text(encoding="utf-8").split("\n"), 1):
        if ligne.startswith("```"):
            code = not code
            continue
        if code:
            continue
        m = RE_INCLUDE.match(ligne.strip())
        if m:
            sortie += titres(fichier.parent / m.group(1), _vus | {fichier})
            continue
        m = RE_TITRE.match(ligne)
        if m:
            sortie.append((len(m.group(1)), m.group(2).strip(), f"{fichier.name}:{n}"))
    return sortie


def ecarts_de_structure(t: list[tuple[int, str, str]], profondeur: int, livre: str) -> list[str]:
    """Règles 3 à 5 sur la suite des titres d'un fichier."""
    ecarts = []
    for k, (niveau, titre, lieu) in enumerate(t):
        if k and niveau > t[k - 1][0] + 1:
            ecarts.append(f"{livre}/{lieu} : saut de niveau (h{t[k - 1][0]} → h{niveau}) « {titre[:60]} »")
        if niveau > profondeur and "unnumbered" not in titre:
            ecarts.append(f"{livre}/{lieu} : h{niveau} au-delà de number-depth ({profondeur}), "
                          f"donc sans numéro « {titre[:60]} »")
        enfants = []
        for niveau2, titre2, _lieu2 in t[k + 1:]:
            if niveau2 <= niveau:
                break
            if niveau2 == niveau + 1:
                enfants.append(titre2)
        if len(enfants) == 1:
            ecarts.append(f"{livre}/{lieu} : section à une seule sous-section « {titre[:50]} » "
                          f"→ « {enfants[0][:40]} »")
    return ecarts


def _profondeur(config: dict) -> int:
    html = (config.get("format") or {}).get("html") or {}
    return int(html.get("number-depth", 3))


def ecarts_du_livre(livre: Path) -> list[str]:
    import yaml  # import tardif, comme build_glossary.load_entries() : la CI lance unittest sans PyYAML

    config = yaml.safe_load((livre / "_quarto.yml").read_text(encoding="utf-8"))
    book = config.get("book", {})
    ecarts: list[str] = []
    chapitres = _fichiers(book.get("chapters"), livre, ecarts)
    annexes = _fichiers(book.get("appendices"), livre, ecarts)
    for f in chapitres:
        t = titres(f)
        if t and t[0][0] == 1 and "unnumbered" in t[0][1]:
            ecarts.append(f"{livre.name}/{f.name} : chapitre marqué {{.unnumbered}} — "
                          "retirer la marque, la numérotation est celle de Quarto")
    for f in chapitres + annexes:
        if f.name == "_glossaire.qmd":  # engendré, hors numérotation
            continue
        ecarts += ecarts_de_structure(titres(f), _profondeur(config), livre.name)
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

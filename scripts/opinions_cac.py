"""Relève l'opinion des commissaires aux comptes et ses motifs de réserve dans les rapports annuels d'une entreprise.

    uv run python scripts/opinions_cac.py STB

Le texte du PDF est lu dans l'ordre des colonnes (`pdftotext` sans -layout), page par page. Pour chaque rapport, on
cherche l'intitulé « Justification de l'opinion avec réserves » (ou « Fondement de l'opinion avec réserves »), on
garde le texte jusqu'au titre suivant, et on le coupe en motifs numérotés (« 3.1 », « 2.2 »…). Le relevé donne,
pour chaque motif, la phrase d'ouverture telle que le rapport l'imprime et la page du PDF ; la lecture finale se
fait sur la page : le script prépare, il ne remplace pas la relecture.

Sortie : `precis/fr/entreprises_publiques/listes/opinions-cac.csv`
  groupe, exercice, opinion, rang, motif, page_pdf, source
"""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

DONNEES = Path("~/projets/tunisia-data/data/raw/entreprises-publiques").expanduser()
SORTIE = (
    Path(__file__).resolve().parent.parent
    / "precis/fr/entreprises_publiques/listes/opinions-cac.csv"
)
COLONNES = ["groupe", "exercice", "opinion", "rang", "motif", "page_pdf", "source"]
DOCUMENTS = [
    (
        "STB",
        2011,
        "bvmt-rapports-archives/stb/20211103_Rapport_STB_Fr__2011.pdf",
        "ra-stb-2011",
    ),
    (
        "STB",
        2013,
        "bvmt-rapports-archives/stb/20211103_Rapport_STB_Fr_2013.pdf",
        "ra-stb-2013",
    ),
    (
        "STB",
        2014,
        "bvmt-rapports-archives/stb/20211103_Rapport_STB_Fr_2014.pdf",
        "ra-stb-2014",
    ),
    (
        "STB",
        2015,
        "bvmt-rapports-archives/stb/20211103_Rapport_STB_Fr__2015.pdf",
        "ra-stb-2015",
    ),
    (
        "STB",
        2017,
        "bvmt-rapports-archives/stb/20230228_Rapport_STB_Fr_2017.pdf",
        "ra-stb-2017",
    ),
    (
        "STB",
        2018,
        "bvmt-rapports-archives/stb/20211103_STB_RAPPORT_2018_FRANÇAIS.pdf",
        "ra-stb-2018",
    ),
]
TITRE = re.compile(
    r"(?i)(justification|fondement)\s+de\s+l.opinion\s+avec\s+r[ée]serves?"
)
FIN = re.compile(
    r"(?i)questions\s+cl[ée]s|paragraphe\s+d.observation|rapport\s+sur\s+les\s+v[ée]rifications|responsabilit[ée]s\s+(du|de la|des)|v[ée]rifications\s+sp[ée]cifiques|incertitude"
)
MOTIF = re.compile(r"(?m)^\s*(\d[.\-]\d{1,2})\s+(?=\S)")


def pages(chemin: Path) -> list[str]:
    sortie = subprocess.run(
        ["pdftotext", str(chemin), "-"], capture_output=True, text=True, check=True
    ).stdout
    return sortie.split("\f")


def phrase(texte: str, longueur: int = 230) -> str:
    texte = re.sub(r"\s+", " ", texte).strip()
    texte = re.sub(r"(\w)- (\w)", r"\1\2", texte)
    coupe = texte[:longueur]
    fin = max(coupe.rfind(". "), coupe.rfind("; "), coupe.rfind(": "))
    return (coupe[: fin + 1] if fin > 80 else coupe.rsplit(" ", 1)[0] + " …").strip()


def releve(groupe: str, exercice: int, chemin: Path, source: str) -> list[list[str]]:
    lignes = []
    textes = pages(chemin)
    for numero, page in enumerate(textes, start=1):
        trouve = TITRE.search(page)
        if not trouve:
            continue
        # le motif commence au titre et court jusqu'au titre suivant, sur cette page et la suivante au plus
        corps = (
            page[trouve.end() :]
            + "\n"
            + (textes[numero] if numero < len(textes) else "")
        )
        fin = FIN.search(corps)
        corps = corps[: fin.start()] if fin else corps[:6000]
        morceaux = list(MOTIF.finditer(corps))
        for i, m in enumerate(morceaux):
            suite = morceaux[i + 1].start() if i + 1 < len(morceaux) else len(corps)
            lignes.append(
                [
                    groupe,
                    str(exercice),
                    "avec réserves",
                    m.group(1),
                    phrase(corps[m.end() : suite]),
                    str(numero),
                    source,
                ]
            )
        if not morceaux:
            lignes.append(
                [
                    groupe,
                    str(exercice),
                    "avec réserves",
                    "",
                    phrase(corps),
                    str(numero),
                    source,
                ]
            )
        break
    if not lignes:
        lignes.append([groupe, str(exercice), "à relire", "", "", "", source])
    return lignes


def main(arguments: list[str]) -> int:
    groupes = [a.upper() for a in arguments] or ["STB"]
    nouvelles = []
    for groupe, exercice, fichier, source in DOCUMENTS:
        if groupe in groupes:
            nouvelles += releve(groupe, exercice, DONNEES / fichier, source)
    gardees = []
    if SORTIE.exists():
        with SORTIE.open(encoding="utf-8", newline="") as s:
            gardees = [
                [r[c] for c in COLONNES]
                for r in csv.DictReader(s)
                if r["groupe"] not in groupes
            ]
    with SORTIE.open("w", encoding="utf-8", newline="") as s:
        w = csv.writer(s)
        w.writerow(COLONNES)
        w.writerows(gardees + nouvelles)
    for exercice in sorted({r[1] for r in nouvelles}):
        n = sum(1 for r in nouvelles if r[1] == exercice)
        print(
            f"{exercice} : {n} motifs, page(s) {sorted({r[5] for r in nouvelles if r[1] == exercice})}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

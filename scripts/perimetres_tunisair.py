"""Relève le périmètre de consolidation du groupe Tunisair, exercice par exercice.

Les états financiers consolidés de Tunisair, publiés sur la page de la société à la Bourse de Tunis,
portent un tableau « Périmètre de consolidation » : méthode, société, activité, droits de vote. Les PDF
sont rangés dans `tunisia-data/data/raw/entreprises-publiques/bvmt-etats-financiers/tunisair/` (hors git).

    uv run python scripts/perimetres_tunisair.py

Le tableau imprime la plupart des noms de société sous forme de logo : le texte du PDF ne garde que
l'activité et le pourcentage. Le lecteur range donc chaque ligne par son activité (ACTIVITES) ; ce
rangement a été relu sur l'image de la page de plusieurs exercices (2009, 2010, 2014, 2022) et le
nombre de lignes est recoupé avec celui que le rapport annonce (NOMBRE_ANNONCE). Le tableau chevauche
parfois deux pages : la lecture va de son en-tête à la note qui le suit. Le PDF de 2006 imprime les noms
en texte.

Sortie : `precis/fr/entreprises_publiques/listes/groupes-bancaires-perimetre.csv` (nom du relevé des
banques, que lit `figures/cotees.py`). Le script remplace les lignes du groupe TUNISAIR et garde les autres.

  controle_pct  droits de vote, seule colonne que le tableau donne ; interet_pct reste vide
  methode       intégration globale, intégration proportionnelle ou mise en équivalence
  La société mère n'a pas de ligne ; le pays n'est pas donné.

Un écart entre le nombre de lignes lues et le nombre annoncé arrête le script.
"""

from __future__ import annotations

import csv
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

DONNEES = (
    Path(os.environ.get("TUNISIA_DATA", "~/projets/tunisia-data")).expanduser()
    / "data/raw/entreprises-publiques/bvmt-etats-financiers/tunisair"
)
SORTIE = (
    Path(__file__).resolve().parent.parent
    / "precis/fr/entreprises_publiques/listes/groupes-bancaires-perimetre.csv"
)
COLONNES = [
    "groupe",
    "exercice",
    "entite",
    "methode",
    "controle_pct",
    "interet_pct",
    "pays",
    "source",
]
GROUPE = "TUNISAIR"
EXERCICES = [2006] + list(range(2009, 2023))

# Nombre de sociétés (mère non comprise) que le rapport annonce : rapport des commissaires aux comptes sur les
# comptes consolidés (2009 à 2015) ou note sur le processus de consolidation (2022 : « 5 sociétés … intégration
# globale et deux … mise en équivalence »).
NOMBRE_ANNONCE = {
    2009: 9,
    2010: 9,
    2011: 8,
    2012: 8,
    2013: 8,
    2014: 8,
    2015: 8,
    2022: 7,
}
# 2016 à 2021 : aucun total annoncé ; nombre de sociétés que la note « résultat consolidé » énumère (comptées à la
# main : AISA y figure jusqu'en 2017, en tiret en 2018, plus ensuite). 2006 : aucun recoupement possible dans le texte.
NOMBRE_PAR_LA_NOTE_DU_RESULTAT = {2016: 8, 2017: 8, 2018: 7, 2019: 7, 2020: 7, 2021: 7}

# (mots de l'activité sans accent, entité) : le premier motif qui convient l'emporte.
ACTIVITES = [
    ("transport aerien international", "MAURITANIA AIRWAYS"),
    ("assistance au sol", "TUNISAIR HANDLING"),
    ("prestations de services pour les compagnies", "TUNISAIR HANDLING"),
    ("entretien et reparation", "TUNISAIR TECHNICS"),
    ("maintenance aeronautique", "TUNISAIR TECHNICS"),
    ("gestion de biens", "SCI ESSAFA"),
    ("immobilier", "SCI ESSAFA"),
    ("transport aerien", "TUNISAIR EXPRESS"),
    ("services informatiques et telecoms", "AISA"),
    ("prestations informatiques", "AMADEUS"),
    ("solutions informatiques", "AMADEUS"),
    ("catering", "TUNISIE CATERING"),
    ("formation", "ATCT"),
]
# Nom que le tableau imprime quand il diffère du nom par défaut de l'entité (relu sur l'image ou dans le texte).
NOMS_IMPRIMES = {
    (2006, "TUNISAIR EXPRESS"): "TUNINTER",
    (2009, "TUNISAIR EXPRESS"): "SEVENAIR",
}
MISE_EN_EQUIVALENCE = {"TUNISIE CATERING", "ATCT"}

EN_TETE = re.compile(
    r"M[ée]thode\s+de\s+consolidation\s+Soci[ée]t[ée]s\s+Activit[ée]\s+Droits?\s+de\s+vote",
    re.I,
)
FIN = re.compile(
    r"Notes? [Rr]elatives|NOTES AUX [ÉE]TATS|Note pr[ée]liminaire|\nN\nNo\not|Note 1 ?:"
)


def sans_accent(texte: str) -> str:
    brut = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", brut.lower())


def extraire(fichier: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-raw", str(fichier), "-"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def corps_du_tableau(texte: str, exercice: int) -> str:
    """Le texte du tableau : de son en-tête à la note qui le suit (2006 : de « SOCIETES DU PERIMETRE » au pied de page)."""
    if exercice == 2006:
        debut = texte.index("SOCIETES DU PERIMETRE")
        fin = re.compile(r"\nG\nGR\n").search(texte, debut)
        return texte[debut : fin.start() if fin else debut + 1500]
    entetes = list(EN_TETE.finditer(texte))
    if not entetes:
        raise ValueError("en-tête du tableau introuvable")
    reste = texte[entetes[-1].end() :]
    fin = FIN.search(reste)
    return reste[: fin.start() if fin else 1500]


def methode_de(entite: str, exercice: int) -> str:
    if entite in MISE_EN_EQUIVALENCE:
        return "mise en équivalence"
    if entite == "AISA" and exercice <= 2011:
        return "intégration proportionnelle"
    return "intégration globale"


def lire_tableau(corps: str, exercice: int) -> list[dict]:
    """Une ligne par pourcentage de droits de vote ; l'activité qui le précède donne la société."""
    lignes = []
    debut = 0
    for m in re.finditer(r"(\d{1,3}(?:[,.]\d+)?)\s*%", corps):
        descripteur = sans_accent(corps[debut : m.start()])
        debut = m.end()
        entite = next((nom for mot, nom in ACTIVITES if mot in descripteur), None)
        if entite is None:
            raise ValueError(
                f"activité inconnue avant {m.group(0)} : {descripteur[-100:]!r}"
            )
        lignes.append(
            {
                "entite": NOMS_IMPRIMES.get((exercice, entite), entite),
                "methode": methode_de(entite, exercice),
                "controle_pct": m.group(1).replace(",", "."),
            }
        )
    return lignes


def releve() -> list[list]:
    lignes = []
    for exercice in EXERCICES:
        texte = extraire(DONNEES / f"{exercice}_consolide.pdf")
        lues = lire_tableau(corps_du_tableau(texte, exercice), exercice)
        annonce = NOMBRE_ANNONCE.get(
            exercice, NOMBRE_PAR_LA_NOTE_DU_RESULTAT.get(exercice)
        )
        if annonce is not None and len(lues) != annonce:
            raise SystemExit(
                f"{exercice} : {len(lues)} lignes lues, {annonce} annoncées"
            )
        lignes += [
            [
                GROUPE,
                exercice,
                ligne["entite"],
                ligne["methode"],
                ligne["controle_pct"],
                "",
                "",
                f"bvmt-ef-tunisair-{exercice}-consolide",
            ]
            for ligne in lues
        ]
    return lignes


def ecrire(nouvelles: list[list]) -> None:
    with SORTIE.open(encoding="utf-8", newline="") as source:
        existantes = [r for r in csv.reader(source)][1:]
    gardees = [r for r in existantes if r[0] != GROUPE]
    with SORTIE.open("w", encoding="utf-8", newline="") as sortie:
        w = csv.writer(sortie)  # fins de ligne \r\n, comme le relevé des banques
        w.writerow(COLONNES)
        w.writerows(gardees + nouvelles)


def principal() -> int:
    nouvelles = releve()
    ecrire(nouvelles)
    for exercice in EXERCICES:
        lignes = [r for r in nouvelles if r[1] == exercice]
        print(exercice, len(lignes), [(r[2], r[4]) for r in lignes])
    return 0


if __name__ == "__main__":
    sys.exit(principal())

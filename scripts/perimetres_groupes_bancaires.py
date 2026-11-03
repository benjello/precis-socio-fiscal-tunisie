"""Relève le périmètre de consolidation de la STB, de la BH et de la BNA au 31 décembre 2021.

Le rapport annuel de gestion de chaque banque, publié sur la page de la Bourse de Tunis, donne les
entités que le groupe consolide, avec la méthode et les pourcentages de contrôle et d'intérêt. Les
trois PDF sont rangés dans `tunisia-data/data/raw/entreprises-publiques/bvmt-rapports/` (hors git ;
catalogue : `sources/bvmt-rapports-annuels-urls.csv`). Ce script en lit le texte avec `pdftotext`
(poppler) et n'écrit que le relevé du volume :

    uv run python scripts/perimetres_groupes_bancaires.py

Sortie : `precis/fr/entreprises_publiques/listes/groupes-bancaires-perimetre.csv`.

  groupe, entite, methode     banque, entité consolidée, méthode (intégration globale, mise en équivalence)
  controle_pct, interet_pct   pourcentage de contrôle (droits de vote) et d'intérêt (part du capital),
                              tels que le rapport les imprime ; vide quand le rapport ne donne pas la colonne
  pays                        pays de l'entité quand le rapport le donne (BH)

La mère consolidante est reprise (pourcentage de 100 % ou presque) ; elle porte la méthode « mère ».
La STB ne donne pas la méthode : elle est vide. Le rapport de la BH ne donne que le pourcentage d'intérêt.
"""

from __future__ import annotations

import csv
import os
import re
import subprocess
from pathlib import Path

RAPPORTS = (
    Path(os.environ.get("TUNISIA_DATA", "~/projets/tunisia-data")).expanduser()
    / "data/raw/entreprises-publiques/bvmt-rapports"
)
SORTIE = (
    Path(__file__).resolve().parent.parent
    / "precis/fr/entreprises_publiques/listes/groupes-bancaires-perimetre.csv"
)
FICHIERS = {
    "STB": "stb/stb-rapport-annuel-de-gestion-31-12-2021.pdf",
    "BH": "bh-bank/bh-rapport-annuel-de-gestion-31-12-2021.pdf",
    "BNA": "bna/bna-rapport-annuel-de-gestion-31-12-2021.pdf",
}
METHODES = {
    "integration globale": "intégration globale",
    "mise en equivalence": "mise en équivalence",
}


def texte(chemin: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(chemin), "-"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def nombre(valeur: str) -> str:
    return valeur.replace(",", ".").rstrip("%")


def propre(nom: str) -> str:
    return re.sub(r"\s*\(\d\)\s*$", "", " ".join(nom.split())).strip()


def methode(valeur: str) -> str:
    import unicodedata

    cle = (
        unicodedata.normalize("NFKD", valeur).encode("ascii", "ignore").decode().lower()
    )
    return METHODES.get(cle, valeur.lower())


def stb(contenu: str) -> list[list[str]]:
    """Deux tableaux numérotés de 22 lignes : contrôle (le premier), intérêt (le second)."""
    motif = re.compile(
        r"(\d{1,2})\.\s+(.+?)\s{2,}(\d+,\d+)%\s+(\d+,\d+)%\s+(-?\d+,\d+)%"
    )
    debut = contenu.index("SOCIETES CONSOLIDEES")
    vues: dict[str, dict[str, str]] = {}
    ordre: list[str] = []
    rang = {}
    for ligne in contenu[debut:].splitlines():
        trouve = motif.search(ligne)
        if not trouve:
            continue
        numero, nom = trouve.group(1), propre(trouve.group(2))
        rang[numero] = rang.get(numero, 0) + 1
        if rang[numero] > 2:
            break
        champ = "controle" if rang[numero] == 1 else "interet"
        entree = vues.setdefault(numero, {"nom": nom})
        entree[champ] = nombre(trouve.group(3))
        if numero not in ordre:
            ordre.append(numero)
    lignes = []
    for numero in ordre:
        e = vues[numero]
        mere = "mère" if numero == "1" else ""
        lignes.append(
            [
                "STB",
                re.sub(r"\s*\(société Mère\)", "", e["nom"]),
                mere,
                e.get("controle", ""),
                e.get("interet", ""),
                "",
            ]
        )
    return lignes


def bna(contenu: str) -> list[list[str]]:
    debut = contenu.index("4- PÉRIMÈTRE DE CONSOLIDATION")
    fin = contenu.index("(1) La BNA détient 33,926%", debut)
    motif = re.compile(
        r"^\s*(?:[A-Z]{1,3}\s{2,})?(\S.*?)\s{2,}(Intégration globale|Mise en équivalence)\s+(\d+,\d+)%\s+(\d+,\d+)%"
    )
    lignes = []
    for ligne in contenu[debut:fin].splitlines():
        trouve = motif.match(ligne)
        if trouve:
            nom = propre(trouve.group(1))
            mere = (
                "mère"
                if nom == "Banque Nationale Agricole"
                else methode(trouve.group(2))
            )
            lignes.append(
                [
                    "BNA",
                    nom,
                    mere,
                    nombre(trouve.group(3)),
                    nombre(trouve.group(4)),
                    "Tunisie",
                ]
            )
    return lignes


def bh(contenu: str) -> list[list[str]]:
    debut = contenu.index(
        "Les entreprises retenues dans le périmètre de consolidation, le pourcentage d'intérêt"
    )
    fin = contenu.index("Méthodes de consolidation", debut)
    motif = re.compile(
        r"^\s*(\S.*?)\s{2,}(\d+,\d+)\s+(\d+,\d+)\s+(Intégration Globale|Mise en équivalence)\s+(\w+)"
    )
    lignes = []
    for ligne in contenu[debut:fin].splitlines():
        trouve = motif.match(ligne)
        if trouve:
            nom = propre(trouve.group(1))
            mere = "mère" if nom == "BH BANK" else methode(trouve.group(4))
            lignes.append(
                ["BH", nom, mere, "", nombre(trouve.group(2)), trouve.group(5)]
            )
    return lignes


def main() -> int:
    lignes: list[list[str]] = []
    for groupe, lecteur in (("STB", stb), ("BH", bh), ("BNA", bna)):
        lues = lecteur(texte(RAPPORTS / FICHIERS[groupe]))
        print(f"{groupe} : {len(lues)} entités")
        lignes += lues
    with SORTIE.open("w", encoding="utf-8", newline="") as sortie:
        ecrivain = csv.writer(sortie)
        ecrivain.writerow(
            ["groupe", "entite", "methode", "controle_pct", "interet_pct", "pays"]
        )
        ecrivain.writerows(lignes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

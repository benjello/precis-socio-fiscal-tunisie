"""Relève dans les états financiers de la BNA le tableau de ses engagements envers les entreprises publiques.

    uv run python scripts/bna_engagements_entreprises_publiques.py

La note « Engagements envers les entreprises publiques » (note 4.3.x) donne, en fin d'exercice, pour le total des
entreprises publiques et pour chacune des plus importantes (Office des céréales, STIR, Tunisair, OTD, ONH, El Fouladh,
puis OCT et Transtu), les engagements, les garanties de l'État, les autres garanties, les agios et intérêts réservés,
la classe de risque et les provisions. Chaque état donne l'exercice et le précédent. Le texte du PDF est lu avec
`pdftotext -layout` : les colonnes sont séparées par au moins deux espaces. Pour un exercice donné, on garde la lecture
de l'état de cet exercice, à défaut celle de l'état suivant.

Sortie : `precis/fr/entreprises_publiques/listes/bna-engagements-entreprises-publiques.csv`
  exercice, entite, grandeur, valeur_kdt, page_pdf, source
"""

from __future__ import annotations

import csv
import os
import re
import subprocess
import sys
from pathlib import Path

DONNEES = (
    Path(os.environ.get("TUNISIA_DATA", "~/projets/tunisia-data")).expanduser()
    / "data/raw/entreprises-publiques/bvmt-etats-financiers/bna"
)
SORTIE = (
    Path(__file__).resolve().parent.parent
    / "precis/fr/entreprises_publiques/listes/bna-engagements-entreprises-publiques.csv"
)
COLONNES = ["exercice", "entite", "grandeur", "valeur_kdt", "page_pdf", "source"]
GRANDEURS = {
    "Engagements": "engagements",
    "Garanties de l'état": "garanties de l'État",
    "Autres Garanties": "autres garanties",
    "Agios et intérêts réservés": "agios et intérêts réservés",
    "Classe": "classe de risque",
    "Provisions": "provisions",
}
LIGNE = re.compile(
    r"^\s*(Engagements|Garanties de l.[ée]tat|Autres [Gg]aranties|Agios et int[ée]r[êe]ts r[ée]serv[ée]s|Classe|Provisions)"
    r" au (\d\d/\d\d/(\d{4}))\s*(?:\(\*\))?\s{2,}(.*)$"
)


def nombre(texte: str) -> str:
    texte = texte.strip().replace(" ", " ")
    if texte in ("-", ""):
        return ""
    negatif = re.fullmatch(r"\(\s*([\d\s]+)\)", texte)  # « (19 795) » : montant négatif
    if negatif:
        return "-" + re.sub(r"\s+", "", negatif.group(1))
    return re.sub(r"\s+", "", texte)


NOMS = re.compile(
    r"STIR|TUNIS ?AIR|TRANSTU|ETAP|OCT|O\.T\.D|O\.N\.H|El Fouledh|SNCFT|STEG|SONEDE",
    re.I,
)
AMORCE = re.compile(r"^\s*Engagements au \d\d/\d\d/\d{4}\s*(?:\(\*\))?\s{2,}\d")
COUPE = re.compile(
    r"^\s*(Engagements|Garanties de l.[ée]tat|Autres [Gg]aranties(?: \(\*+\))?|Agios et int[ée]r[êe]ts r[ée]serv[ée]s|Classe|Provisions)\s+au\s*$"
)


def lignes_de_valeurs(
    lignes: list[str], debut: int
) -> list[tuple[str, str, list[str]]]:
    """Les lignes « libellé au jj/mm/aaaa  valeurs » du tableau ; le libellé des agios peut être coupé sur trois lignes."""
    sortie, i = [], debut
    while i < min(len(lignes), debut + 16):
        m = LIGNE.match(lignes[i])
        if m:
            sortie.append(
                (m.group(1), m.group(3), re.split(r"\s{2,}", m.group(4).strip()))
            )
        elif re.match(
            r"^\s*Agios et int[ée]r[êe]ts r[ée]serv[ée]s au\s*$", lignes[i]
        ) and i + 2 < len(lignes):
            d = re.search(r"(\d{4})", lignes[i + 2])
            if d:
                sortie.append(
                    (
                        "Agios et intérêts réservés",
                        d.group(1),
                        re.split(r"\s{2,}", lignes[i + 1].strip()),
                    )
                )
                i += 2
        i += 1
    return sortie


def lignes_coupees(lignes: list[str], debut: int) -> list[tuple[str, str, list[str]]]:
    """Mise en page où le libellé est coupé sur plusieurs lignes : des morceaux de libellé, une ligne de valeurs
    (parfois sur la ligne d'un morceau), puis la date du tableau, à la fin de la dernière ligne du bloc."""
    sortie, tampon = [], []
    for ligne in lignes[debut : debut + 70]:
        if not ligne.strip():
            continue
        tampon.append(ligne)
        d = re.search(r"(\d\d/\d\d/(\d{4}))\s*$", ligne)
        if not d:
            continue
        libelle, valeurs = [], None
        for t in tampon:
            morceaux = [m.strip() for m in re.split(r"\s{2,}", t.strip())]
            if len(morceaux) > 2 and all(
                re.fullmatch(r"[\d\s\-]+", m) for m in morceaux[1:]
            ):
                valeurs = (
                    morceaux[1:]
                    if not re.fullmatch(r"[\d\s\-]+", morceaux[0])
                    else morceaux
                )
                if not re.fullmatch(r"[\d\s\-]+", morceaux[0]):
                    libelle.append(morceaux[0])
            else:
                libelle.append(re.sub(r"\s*\d\d/\d\d/\d{4}\s*$", "", t.strip()))
        lib = re.sub(r"\s+", " ", " ".join(x for x in libelle if x)).strip()
        lib = re.sub(r"\s+au$", "", lib)
        lib = re.sub(r"\s*\(\*+\)", "", lib).strip()
        if valeurs and re.match(
            r"(?i)(Engagements|Garanties|Autres|Agios|Classe|Provisions)", lib
        ):
            lib = (
                "Garanties de l'état"
                if lib.lower().replace("’", "'").startswith("garanties de l")
                else lib
            )
            sortie.append((lib, d.group(2), valeurs))
        tampon = []
    return sortie


def releve(exercice: int) -> list[list[str]]:
    chemin = DONNEES / f"{exercice}_individuel.pdf"
    pages = subprocess.run(
        ["pdftotext", "-layout", str(chemin), "-"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.split("\f")
    candidats: list[list[list[str]]] = []
    for numero, page in enumerate(pages, start=1):
        lignes = "\n".join(
            pages[numero - 1 : numero + 2]
        ).splitlines()  # le tableau peut passer aux pages suivantes
        debut = next(
            (
                i
                for i, texte in enumerate(lignes)
                if AMORCE.match(texte)
                or (COUPE.match(texte) and texte.strip().startswith("Engagements"))
            ),
            None,
        )
        if debut is None:
            continue
        entete = " ".join(lignes[max(0, debut - 6) : debut])
        noms = [
            "Total des entreprises publiques",
            "Office des céréales",
            *[re.sub(r"(?i)tunis ?air", "Tunisair", n) for n in NOMS.findall(entete)],
        ]
        sortie = []
        for libelle, annee, valeurs in (
            lignes_coupees(lignes, debut)
            if COUPE.match(lignes[debut])
            else lignes_de_valeurs(lignes, debut)
        ):
            if len(valeurs) != len(noms):
                print(
                    f"{exercice} p. {numero} : {libelle} {annee} : {len(valeurs)} valeurs pour {len(noms)} colonnes",
                    file=sys.stderr,
                )
                continue
            cle = (
                "Autres Garanties" if libelle.lower().startswith("autres") else libelle
            )
            cle = (
                "Garanties de l'état" if cle.lower().startswith("garanties de") else cle
            )
            for nom, v in zip(noms, valeurs, strict=True):
                sortie.append(
                    [
                        annee,
                        nom,
                        GRANDEURS.get(cle, cle),
                        nombre(v),
                        str(numero),
                        f"bvmt-ef-bna-{exercice}-individuel",
                    ]
                )
        if sortie:
            total = f"{int(sortie[0][3]):,}".replace(",", " ") if sortie[0][3] else ""
            page_tableau = next(
                (
                    k + 1
                    for k, t in enumerate(pages)
                    if total and total in t and "Engagements" in t
                ),
                numero,
            )
            for ligne in sortie:
                ligne[4] = str(page_tableau)
            candidats.append(sortie)
    return max(candidats, key=len, default=[])


def main(arguments: list[str]) -> int:
    retenues: dict[str, tuple[int, list[list[str]]]] = {}
    for exercice in (
        sorted(int(a) for a in arguments) if arguments else range(2017, 2025)
    ):
        if not (DONNEES / f"{exercice}_individuel.pdf").exists():
            continue
        lignes = releve(exercice)
        par_annee: dict[str, list[list[str]]] = {}
        for ligne in lignes:
            par_annee.setdefault(ligne[0], []).append(ligne)
        for annee, ls in par_annee.items():
            distance = exercice - int(annee)
            if annee not in retenues or (len(ls), -distance) > (
                len(retenues[annee][1]),
                -retenues[annee][0],
            ):
                retenues[annee] = (distance, ls)
        print(f"{exercice} : {sorted((a, len(v)) for a, v in par_annee.items())}")
    lignes = [ligne for _, (_, ls) in sorted(retenues.items()) for ligne in ls]
    with SORTIE.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(COLONNES)
        w.writerows(lignes)
    print(f"{len(lignes)} lignes, exercices {sorted(retenues)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

"""Récupère les états financiers annuels d'une société cotée sur la page « Publications des sociétés » de la Bourse de Tunis.

    uv run python scripts/bvmt_etats_financiers.py stb            # nom de la page de la société (informations-<nom>)
    uv run python scripts/bvmt_etats_financiers.py stb --liste    # montre ce qui serait pris, sans télécharger

La liste des publications d'une société (`/publications-societes?type_societe=<id>`) donne, par exercice, les états
financiers annuels individuels et consolidés, avec le rapport des commissaires aux comptes. Le script prend les
publications dont le titre dit « états financiers annuels » (pas les semestriels), ouvre la page de chacune, télécharge le
PDF, et le range sous `tunisia-data/data/raw/entreprises-publiques/bvmt-etats-financiers/<société>/` (hors git) sous le
nom `<exercice>_<individuel|consolide>.pdf`. Un fichier déjà là n'est pas redemandé ; une pause sépare deux requêtes.
Le catalogue (adresse, taille, somme de contrôle) s'écrit dans `sources/bvmt-etats-financiers-urls.csv` du dossier
`TUNISIA_DATA_CATALOGUE` (par défaut le worktree `tunisia-data-wt-arch`).
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

RACINE = "https://tunis-stockexchange.com"
DOSSIER = (
    Path(os.environ.get("TUNISIA_DATA", "~/projets/tunisia-data")).expanduser()
    / "data/raw/entreprises-publiques"
)
PIECES = DOSSIER / "bvmt-etats-financiers"
CATALOGUE = (
    Path(
        os.environ.get("TUNISIA_DATA_CATALOGUE", "~/projets/tunisia-data-wt-arch")
    ).expanduser()
    / "sources/bvmt-etats-financiers-urls.csv"
)
PAUSE = 3
# catégories de la liste des publications : « Etats Financiers » et « Annuels » (individuels et consolidés)
CATEGORIES = ("1524", "3312")
COLONNES = [
    "fichier",
    "url_origine",
    "url_archive",
    "octets",
    "sha256",
    "consultation",
    "famille",
    "etat",
]


def demander(url: str, binaire: bool = False):
    requete = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(requete, timeout=120) as reponse:
        contenu = reponse.read()
    return contenu if binaire else contenu.decode("utf-8")


def identifiant(nom: str) -> str:
    page = demander(f"{RACINE}/informations-{nom}")
    trouve = re.search(r"type_societe=(\d+)", page)
    if not trouve:
        raise SystemExit(f"identifiant de société introuvable pour {nom}")
    return trouve.group(1)


def publications(identifiant_societe: str) -> list[tuple[str, str, str, str]]:
    """(exercice, nature, chemin de la page, date de publication jj/mm/aaaa) des états financiers annuels."""
    trouvees: list[tuple[str, str, str, str]] = []
    for categorie, page in ((c, p) for c in CATEGORIES for p in range(0, 12)):
        corps = demander(
            f"{RACINE}/publications-societes?type_societe={identifiant_societe}&categorie={categorie}&page={page}"
        )
        nouvelles = 0
        for chemin, texte in re.findall(
            r'href="(/node/\d+)"[^>]*>(.*?)</a>', corps, flags=re.S
        ):
            titre = re.sub(
                r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", texte))
            ).strip()
            trouve = re.search(
                r"(?i)[ée]tats\s+financiers\s+annuels?\s+(consolid[ée]s?|individuels?)?.*?(?:au|du)\s+31/12/(\d{4})",
                titre,
            )
            if not trouve or "semestr" in titre.lower():
                continue
            nature = (
                "consolide"
                if (trouve.group(1) or "").lower().startswith("consol")
                else "individuel"
            )
            if "consolid" in titre.lower() and nature == "individuel":
                nature = "consolide"
            date = re.match(r"\s*(\d{2}/\d{2}/\d{4})", titre)
            cle = (trouve.group(2), nature, chemin, date.group(1) if date else "")
            if cle not in trouvees:
                trouvees.append(cle)
                nouvelles += 1
        time.sleep(PAUSE)
        if not nouvelles:
            continue
    return trouvees


def inscrire(lignes: dict[str, dict]) -> None:
    existantes: dict[str, dict] = {}
    if CATALOGUE.exists():
        with CATALOGUE.open(encoding="utf-8", newline="") as source:
            existantes = {r["fichier"]: r for r in csv.DictReader(source)}
    existantes.update(lignes)
    CATALOGUE.parent.mkdir(parents=True, exist_ok=True)
    with CATALOGUE.open("w", encoding="utf-8", newline="") as sortie:
        ecrivain = csv.DictWriter(sortie, fieldnames=COLONNES)
        ecrivain.writeheader()
        ecrivain.writerows(sorted(existantes.values(), key=lambda r: r["fichier"]))


def delais(societe: str, trouvees: list[tuple[str, str, str, str]]) -> None:
    """Relevé « délai de publication » : jours entre le 31 décembre de l'exercice et la date que la Bourse porte à la
    publication (la date de mise en ligne sur la Bourse, non celle de l'assemblée ni du rapport)."""
    from datetime import datetime

    sortie = (
        Path(__file__).resolve().parent.parent
        / "precis/fr/entreprises_publiques/listes/delais-publication.csv"
    )
    lignes = []
    if sortie.exists():
        with sortie.open(encoding="utf-8", newline="") as source:
            lignes = [r for r in csv.DictReader(source) if r["societe"] != societe]
    for exercice, nature, chemin, date in trouvees:
        if not date:
            continue
        jours = (
            datetime.strptime(date, "%d/%m/%Y") - datetime(int(exercice), 12, 31)
        ).days
        lignes.append(
            {
                "societe": societe,
                "exercice": exercice,
                "nature": nature,
                "date_publication": date,
                "jours": jours,
                "page": chemin,
            }
        )
    lignes.sort(key=lambda r: (r["societe"], r["exercice"], r["nature"]))
    with sortie.open("w", encoding="utf-8", newline="") as ecrit:
        ecrivain = csv.DictWriter(
            ecrit,
            fieldnames=[
                "societe",
                "exercice",
                "nature",
                "date_publication",
                "jours",
                "page",
            ],
        )
        ecrivain.writeheader()
        ecrivain.writerows(lignes)
    print(f"{len(lignes)} lignes de délais écrites")


def main() -> int:
    analyseur = argparse.ArgumentParser(description=(__doc__ or "").split("\n")[0])
    analyseur.add_argument("societe")
    analyseur.add_argument("--liste", action="store_true")
    analyseur.add_argument(
        "--delais",
        action="store_true",
        help="écrit le relevé des délais de publication, sans télécharger",
    )
    options = analyseur.parse_args()
    identifiant_societe = identifiant(options.societe)
    trouvees = publications(identifiant_societe)
    print(
        f"{len(trouvees)} publications d'états financiers annuels pour {options.societe}"
    )
    if options.delais:
        delais(options.societe, trouvees)
        return 0
    nouvelles: dict[str, dict] = {}
    for exercice, nature, chemin, _date in trouvees:
        if options.liste:
            print(f"  {exercice} {nature} {chemin}")
            continue
        page = demander(RACINE + chemin)
        pdfs = list(
            dict.fromkeys(
                re.findall(
                    r'href="(/sites/default/files/[^"]+\.pdf)"', page, flags=re.I
                )
            )
        )
        for rang, pdf in enumerate(pdfs):
            nom = (
                f"{exercice}_{nature}"
                + (f"_{rang + 1}" if len(pdfs) > 1 else "")
                + ".pdf"
            )
            cible = PIECES / options.societe / nom
            if not cible.exists():
                cible.parent.mkdir(parents=True, exist_ok=True)
                cible.write_bytes(
                    demander(RACINE + urllib.parse.quote(pdf, safe="/%"), binaire=True)
                )
                time.sleep(PAUSE)
            contenu = cible.read_bytes()
            chemin_relatif = (
                f"entreprises-publiques/bvmt-etats-financiers/{options.societe}/{nom}"
            )
            nouvelles[chemin_relatif] = {
                "fichier": chemin_relatif,
                "url_origine": RACINE + pdf,
                "url_archive": "",
                "octets": len(contenu),
                "sha256": hashlib.sha256(contenu).hexdigest(),
                "consultation": time.strftime("%Y-%m-%d"),
                "famille": "boursier",
                "etat": f"états financiers annuels {nature} au 31/12/{exercice} ({chemin})",
            }
            print(f"  {nom} ({len(contenu) // 1000} ko)")
        time.sleep(PAUSE)
    if nouvelles:
        inscrire(nouvelles)
    return 0


if __name__ == "__main__":
    sys.exit(main())

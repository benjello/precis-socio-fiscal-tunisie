"""Relève, pour chaque société cotée à la Bourse de Tunis, ses actionnaires et son capital.

Chaque société cotée a une page publique, sans compte, à l'adresse
`https://tunis-stockexchange.com/informations-<nom>` : dénomination, forme juridique, numéro au
Registre national des entreprises, principaux actionnaires à la dernière assemblée, capital
social et fonds propres des trois derniers exercices, et l'historique du capital depuis la
constitution. Ce script télécharge ces pages une fois, puis les relit sans réseau.

    uv run python scripts/bvmt_societes_cotees.py telecharger   # liste + une page par société
    uv run python scripts/bvmt_societes_cotees.py extraire      # quatre CSV à partir des pages
    uv run python scripts/bvmt_societes_cotees.py livre         # les deux relevés du volume

Les pages sont rangées sous `DOSSIER` (hors git, dans `tunisia-data`) ; une page déjà
téléchargée n'est pas redemandée, et une pause sépare deux requêtes. Pour mettre à jour,
supprimer les pages à renouveler.

Ce que les pages ne donnent pas : le cours, la capitalisation boursière, le rapport annuel.
Les séries de cours relèvent du service de données de la Bourse.

Les quatre CSV (séparateur « , ») :

  bvmt-societes.csv      une ligne par société : dénomination, forme, RNE, secteur, introduction
  bvmt-actionnaires.csv  principaux actionnaires : date de l'assemblée, nombre d'actions, part
  bvmt-fonds-propres.csv capital social et fonds propres par exercice, en dinars
  bvmt-capital.csv       historique du capital : date, opération, augmentation, capital

`livre` en tire les deux relevés versionnés dans le volume « Les entreprises publiques »
(`listes/societes-cotees-participations.csv` et `listes/societes-cotees-capital.csv`) : les
participations de détenteurs publics, tels que les nomme la Bourse (liste fermée ci-dessous,
rien n'est déduit d'un nom), et l'historique du capital des trois banques publiques cotées.
"""

from __future__ import annotations

import argparse
import csv
import html.parser
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

RACINE = "https://tunis-stockexchange.com"
DOSSIER = Path(
    os.environ.get(
        "BVMT_DOSSIER",
        "~/projets/tunisia-data/data/raw/entreprises-publiques/bvmt",
    )
).expanduser()
AGENT = "Mozilla/5.0 (precis-socio-fiscal, relevé des sociétés cotées)"
PAUSE = 3.0
LIVRE = (
    Path(__file__).resolve().parent.parent / "precis/fr/entreprises_publiques/listes"
)

# Détenteurs publics, tels que les pages les impriment (liste fermée : un nom qui n'y est pas
# n'est pas tenu pour public). « Assurance STAR » et « BNA PARTICIPATIONS » sont repris sous leur
# libellé imprimé ; les sicaf et les assurances du groupe BH ne sont pas repris.
DETENTEURS_PUBLICS = {
    "etat tunisien": "État",
    "cnss": "CNSS",
    "etap": "ETAP",
    "entreprise tunisienne d'activites petrolieres -etap": "ETAP",
    "societe tunisienne des industries de raffinage -stir": "STIR",
    "tunisie telecom": "Tunisie Télécom",
    "office national des postes": "Office national des postes",
    "office du commerce de la tunisie": "Office du commerce de la Tunisie",
    "caisse de depots et de consignations -cdc": "Caisse des dépôts et consignations",
    "bna": "BNA",
    "banque nationale agricole": "BNA",
    "bna participations": "BNA Participations",
    "bh bank": "Banque de l'habitat",
    "assurance star": "STAR",
}
BANQUES = {"stb": "STB", "bh-bank": "BH", "bna": "BNA"}
# Noms d'affichage des sociétés : la Bourse imprime des sigles ou des noms courts.
NOMS = {
    "air-liquide-tunisie": "Air Liquide Tunisie",
    "atl": "ATL",
    "bh-assurance": "BH Assurance",
    "bh-bank": "BH",
    "bh-leasing": "BH Leasing",
    "bna": "BNA",
    "bna-assurances": "BNA Assurances",
    "bte-adp": "BTE",
    "ciments-de-bizerte": "Ciments de Bizerte",
    "simpar": "SIMPAR",
    "sotetel": "SOTETEL",
    "sotrapil": "SOTRAPIL",
    "sotumag": "SOTUMAG",
    "star": "STAR",
    "stb": "STB",
    "tunis-re": "Tunis Re",
    "tunisair": "Tunisair",
    "wifak-international-bank": "Wifak International Bank",
}


def demander(url: str) -> str:
    requete = urllib.request.Request(url, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(requete, timeout=40) as reponse:
        return reponse.read().decode("utf-8")


def noms_des_societes() -> list[str]:
    """Les noms de page de toutes les sociétés cotées, lus sur la liste paginée des émetteurs."""
    noms: set[str] = set()
    for page in range(20):
        corps = demander(f"{RACINE}/emetteurs?page={page}")
        trouves = set(re.findall(r'href="/informations-([^"]+)"', corps))
        if not trouves - noms:
            break
        noms |= trouves
        time.sleep(PAUSE)
    return sorted(urllib.parse.unquote(n) for n in noms)


def fichier(nom: str) -> Path:
    return DOSSIER / (re.sub(r"[^a-z0-9-]", "", unicode_simple(nom)) + ".html")


def unicode_simple(texte: str) -> str:
    import unicodedata

    return (
        unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode().lower()
    )


def telecharger() -> int:
    DOSSIER.mkdir(parents=True, exist_ok=True)
    noms = noms_des_societes()
    print(f"{len(noms)} sociétés cotées.")
    for nom in noms:
        cible = fichier(nom)
        if cible.exists() and cible.stat().st_size:
            continue
        url = f"{RACINE}/informations-{urllib.parse.quote(nom)}"
        try:
            cible.write_text(demander(url), encoding="utf-8")
            print(f"  {nom}")
        except (urllib.error.URLError, TimeoutError, OSError) as erreur:
            print(f"  ÉCHEC {nom} : {erreur}", file=sys.stderr)
        time.sleep(PAUSE)
    return 0


class Tableaux(html.parser.HTMLParser):
    """Rend chaque <table> comme une liste de lignes de cellules, et le texte qui la précède."""

    def __init__(self) -> None:
        super().__init__()
        self.tableaux: list[dict] = []
        self.texte = ""
        self._table: dict | None = None
        self._ligne: list[str] | None = None
        self._cellule: list[str] | None = None
        self._ignorer = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._ignorer += 1
        elif tag == "table":
            self._table = {"avant": self.texte[-300:], "lignes": []}
        elif tag == "tr" and self._table is not None:
            self._ligne = []
        elif tag in ("td", "th") and self._ligne is not None:
            self._cellule = []

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._ignorer -= 1
        elif (
            tag in ("td", "th")
            and self._cellule is not None
            and self._ligne is not None
        ):
            self._ligne.append(" ".join("".join(self._cellule).split()))
            self._cellule = None
        elif tag == "tr" and self._ligne is not None and self._table is not None:
            if any(self._ligne):
                self._table["lignes"].append(self._ligne)
            self._ligne = None
        elif tag == "table" and self._table is not None:
            self.tableaux.append(self._table)
            self._table = None

    def handle_data(self, data):
        if self._ignorer:
            return
        if self._cellule is not None:
            self._cellule.append(data)
        self.texte += " " + data


def nombre(texte: str) -> float | None:
    """« 22 565 045 » ou « 35,26 » en nombre ; None si la cellule n'en est pas un."""
    propre = texte.replace("\xa0", "").replace(" ", "").replace(",", ".")
    return float(propre) if re.fullmatch(r"-?\d+(\.\d+)?", propre) else None


def champ(texte: str, libelle: str) -> str:
    """La valeur qui suit un libellé dans le texte de la page (« Forme Juridique  Société… »)."""
    trouve = re.search(rf"{libelle}\s*:?\s*(.+?)\s{{2,}}", texte)
    return trouve.group(1).strip() if trouve else ""


def lire(chemin: Path) -> dict:
    """Une page de société → son identité, ses actionnaires, ses fonds propres, son capital."""
    page = Tableaux()
    page.feed(chemin.read_text(encoding="utf-8"))
    texte = re.sub(r"\s+", " ", page.texte)

    def apres(libelle: str, fin: str) -> str:
        trouve = re.search(rf"{libelle}\s*:?\s*(.+?)\s*(?:{fin})", texte)
        return trouve.group(1).strip() if trouve else ""

    societe = {
        "nom": chemin.stem,
        "denomination": apres("Dénomination sociale", "Date de Constitution"),
        "constitution": apres(
            "Date de Constitution", "Modalité d'introduction|Forme Juridique"
        ),
        "forme": apres("Forme Juridique", "RNE"),
        "rne": apres(r"RNE", "Secteur d'activité"),
        "secteur": apres("Secteur d'activité", "Cours d'introduction|Législation"),
        "introduction": apres("Introduction en Bourse", "Code ISIN"),
        "isin": apres("Code ISIN", "Marché de la Cote"),
        "marche": apres("Marché de la Cote", "Compartiment"),
    }
    actionnaires, fonds_propres, capital, assemblee = [], [], [], ""
    for table in page.tableaux:
        lignes, avant = table["lignes"], table["avant"]
        entete = " ".join(lignes[0]).lower() if lignes else ""
        if "nom ou raison sociale" in entete and "nombre d'actions" in entete:
            trouve = re.search(r"(\d{2}/\d{2}/\d{4})", avant)
            assemblee = trouve.group(1) if trouve else ""
            for ligne in lignes[1:]:
                if len(ligne) >= 3 and ligne[0].strip().lower() != "total":
                    actionnaires.append((ligne[0], nombre(ligne[1]), nombre(ligne[2])))
        elif re.search(r"\b20\d{2}\b", entete) and any(
            r and r[0] == "Capital social" for r in lignes
        ):
            annees = re.findall(r"20\d{2}", entete)
            for ligne in lignes[1:]:
                if ligne[0] in ("Capital social", "Capitaux propres"):
                    for annee, valeur in zip(annees, ligne[1:]):
                        fonds_propres.append((ligne[0], annee, nombre(valeur)))
        elif lignes and re.fullmatch(
            r"\d{4}-\d{2}-\d{2}", lignes[0][0] if lignes[0] else ""
        ):
            for ligne in lignes:
                capital.append(evolution(ligne))
    if not capital:  # l'historique peut n'avoir pas d'en-tête de table propre
        for table in page.tableaux:
            for ligne in table["lignes"]:
                if ligne and re.fullmatch(r"\d{4}-\d{2}-\d{2}", ligne[0]):
                    capital.append(evolution(ligne))
    return {
        "societe": societe,
        "assemblee": assemblee,
        "actionnaires": actionnaires,
        "fonds_propres": fonds_propres,
        "capital": capital,
    }


def evolution(ligne: list[str]) -> dict:
    """Une ligne de l'historique du capital : date, nominal, opération, puis les montants."""
    date = ligne[0]
    reste = ligne[1:]
    operation = next((c for c in reste if c and nombre(c) is None), "")
    position = reste.index(operation) if operation else len(reste)
    nominal = nombre(reste[position - 1]) if position else None
    montants = [nombre(c) for c in reste[position + 1 :] if nombre(c) is not None]
    if (
        len(montants) == 2
    ):  # avant la division en actions : montants en dinars seulement
        augmentation_dt, capital_dt, augmentation_actions, capital_actions = (
            montants[0],
            montants[1],
            None,
            None,
        )
    elif len(montants) >= 4:
        augmentation_dt, augmentation_actions, capital_dt, capital_actions = montants[
            :4
        ]
    else:
        augmentation_dt = augmentation_actions = capital_dt = capital_actions = None
    return {
        "date": date,
        "nominal": nominal,
        "operation": operation,
        "augmentation_dt": augmentation_dt,
        "augmentation_actions": augmentation_actions,
        "capital_dt": capital_dt,
        "capital_actions": capital_actions,
    }


def ecrire(chemin: Path, colonnes: list[str], lignes: list[list]) -> None:
    with chemin.open("w", newline="", encoding="utf-8") as sortie:
        ecrivain = csv.writer(sortie)
        ecrivain.writerow(colonnes)
        ecrivain.writerows(lignes)


def extraire() -> int:
    pages = sorted(p for p in DOSSIER.glob("*.html"))
    if not pages:
        print(
            f"Aucune page sous {DOSSIER} : lancer d'abord « telecharger ».",
            file=sys.stderr,
        )
        return 1
    societes, actionnaires, fonds, capital = [], [], [], []
    for chemin in pages:
        lu = lire(chemin)
        s = lu["societe"]
        nom = s["nom"]
        societes.append(
            [
                nom,
                s["denomination"],
                s["forme"],
                s["rne"],
                s["secteur"],
                s["constitution"],
                s["introduction"],
                s["isin"],
                s["marche"],
                f"{RACINE}/informations-{nom}",
            ]
        )
        actionnaires += [
            [nom, lu["assemblee"], a, n, p] for a, n, p in lu["actionnaires"]
        ]
        fonds += [
            [nom, libelle, annee, valeur]
            for libelle, annee, valeur in lu["fonds_propres"]
        ]
        capital += [
            [
                nom,
                e["date"],
                e["nominal"],
                e["operation"],
                e["augmentation_dt"],
                e["augmentation_actions"],
                e["capital_dt"],
                e["capital_actions"],
            ]
            for e in lu["capital"]
        ]
    ecrire(
        DOSSIER / "bvmt-societes.csv",
        [
            "nom",
            "denomination",
            "forme",
            "rne",
            "secteur",
            "constitution",
            "introduction",
            "isin",
            "marche",
            "url",
        ],
        societes,
    )
    ecrire(
        DOSSIER / "bvmt-actionnaires.csv",
        ["nom", "assemblee", "actionnaire", "actions", "part_pct"],
        actionnaires,
    )
    ecrire(
        DOSSIER / "bvmt-fonds-propres.csv",
        ["nom", "libelle", "exercice", "dinars"],
        fonds,
    )
    ecrire(
        DOSSIER / "bvmt-capital.csv",
        [
            "nom",
            "date",
            "nominal_dt",
            "operation",
            "augmentation_dt",
            "augmentation_actions",
            "capital_dt",
            "capital_actions",
        ],
        capital,
    )
    sans = [p.stem for p in pages if not any(a[0] == p.stem for a in actionnaires)]
    print(
        f"{len(pages)} sociétés, {len(actionnaires)} actionnaires, {len(fonds)} valeurs de fonds propres, {len(capital)} opérations sur le capital."
    )
    if sans:
        print(f"Sans actionnaires lus : {', '.join(sans)}")
    return 0


def cle_detenteur(nom: str) -> str:
    return unicode_simple(nom.replace("\u2019", "'")).strip()


def livre() -> int:
    """Écrit les deux relevés du volume à partir des CSV de `extraire`."""
    lus = lambda nom: list(csv.DictReader((DOSSIER / nom).open(encoding="utf-8")))  # noqa: E731
    participations = []
    for r in lus("bvmt-actionnaires.csv"):
        detenteur = DETENTEURS_PUBLICS.get(cle_detenteur(r["actionnaire"]))
        if detenteur:
            participations.append(
                [
                    detenteur,
                    NOMS[r["nom"]],
                    r["nom"],
                    r["part_pct"],
                    r["actions"].removesuffix(".0"),
                    r["assemblee"],
                    r["actionnaire"],
                ]
            )
    participations.sort(
        key=lambda ligne: (ligne[0] != "État", ligne[0], -float(ligne[3]))
    )
    LIVRE.mkdir(parents=True, exist_ok=True)
    ecrire(
        LIVRE / "societes-cotees-participations.csv",
        [
            "detenteur",
            "societe",
            "page",
            "part_pct",
            "actions",
            "assemblee",
            "nom_imprime",
        ],
        participations,
    )
    capital = []
    for r in lus("bvmt-capital.csv"):
        if r["nom"] in BANQUES and r["capital_dt"]:
            capital.append(
                [
                    BANQUES[r["nom"]],
                    r["nom"],
                    r["date"],
                    r["operation"],
                    r["augmentation_dt"].removesuffix(".0"),
                    r["capital_dt"].removesuffix(".0"),
                ]
            )
    ecrire(
        LIVRE / "societes-cotees-capital.csv",
        ["banque", "page", "date", "operation", "augmentation_dt", "capital_dt"],
        capital,
    )
    print(
        f"{len(participations)} participations, {len(capital)} opérations sur le capital de {len(BANQUES)} banques."
    )
    return 0


def main() -> int:
    analyseur = argparse.ArgumentParser(description=(__doc__ or "").split("\n")[0])
    analyseur.add_argument("commande", choices=("telecharger", "extraire", "livre"))
    options = analyseur.parse_args()
    commandes = {"telecharger": telecharger, "extraire": extraire, "livre": livre}
    return commandes[options.commande]()


if __name__ == "__main__":
    raise SystemExit(main())

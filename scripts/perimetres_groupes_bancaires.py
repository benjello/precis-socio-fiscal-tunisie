"""Relève le périmètre de consolidation de la STB, de la BH et de la BNA, exercice par exercice.

Le rapport annuel ou les états financiers consolidés de chaque banque donnent les entités que le
groupe consolide, avec la méthode et les pourcentages de contrôle et d'intérêt. Les PDF sont
rangés dans `tunisia-data/data/raw/entreprises-publiques/` (hors git) : `bvmt-rapports/` pour ceux
de la page de la Bourse de Tunis (exercice 2021), `bvmt-rapports-archives/` pour ceux que
l'Internet Archive a gardés des sites des banques (catalogue : `sources/bvmt-rapports-*-urls.csv`).
Le script lit le texte avec `pdftotext` (poppler) et n'écrit que le relevé du volume :

    uv run python scripts/perimetres_groupes_bancaires.py STB      # une banque à la fois
    uv run python scripts/perimetres_groupes_bancaires.py          # toutes

Sortie : `precis/fr/entreprises_publiques/listes/groupes-bancaires-perimetre.csv`. Lancé pour une
banque, le script remplace ses lignes et garde celles des autres.

  groupe, exercice, entite    banque, exercice (31 décembre), entité consolidée telle que le rapport l'imprime
  methode                     intégration globale, mise en équivalence, ou « mère » ; vide quand le
                              rapport ne la donne pas (STB 2020 et 2021)
  controle_pct, interet_pct   pourcentage de contrôle (droits de vote) et d'intérêt (part du capital,
                              directe et indirecte) ; vide quand le rapport ne donne pas la colonne
  pays                        pays de l'entité quand le rapport le donne
  source                      clé de la notice de bibliographie du rapport lu

Un rapport donne souvent deux exercices (N et N-1). Pour un exercice, on garde la lecture qui compte le
plus d'entités (certains rapports tronquent leur tableau), à égalité celle du rapport de cet exercice.
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
    / "data/raw/entreprises-publiques"
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

# (groupe, exercice du rapport, fichier sous DONNEES, lecteur, clé de la notice)
DOCUMENTS = [
    (
        "STB",
        2011,
        "bvmt-rapports-archives/stb/20211103_Rapport_STB_Fr__2011.pdf",
        "stb_ancien",
        "ra-stb-2011",
    ),
    (
        "STB",
        2013,
        "bvmt-rapports-archives/stb/20211103_Rapport_STB_Fr_2013.pdf",
        "stb_ancien",
        "ra-stb-2013",
    ),
    (
        "STB",
        2014,
        "bvmt-rapports-archives/stb/20211103_Rapport_STB_Fr_2014.pdf",
        "stb_ancien",
        "ra-stb-2014",
    ),
    (
        "STB",
        2015,
        "bvmt-rapports-archives/stb/20211103_Rapport_STB_Fr__2015.pdf",
        "stb_ancien",
        "ra-stb-2015",
    ),
    (
        "STB",
        2017,
        "bvmt-rapports-archives/stb/20230228_Rapport_STB_Fr_2017.pdf",
        "stb_ancien",
        "ra-stb-2017",
    ),
    (
        "STB",
        2018,
        "bvmt-rapports-archives/stb/20211103_STB_RAPPORT_2018_FRANÇAIS.pdf",
        "stb_ancien",
        "ra-stb-2018",
    ),
    (
        "STB",
        2021,
        "bvmt-rapports/stb/stb-rapport-annuel-de-gestion-31-12-2021.pdf",
        "stb",
        "bvmt-ra-stb-2021",
    ),
    (
        "BNA",
        2007,
        "bvmt-rapports-archives/bna/20190711_rapport_annuel_2007_fr.pdf",
        "bna_ancien",
        "ra-bna-2007",
    ),
    (
        "BNA",
        2020,
        "bvmt-rapports-archives/bna/20260317_États_financiers_consolidés_au_31_décembre_2020.pdf",
        "bna",
        "ra-bna-2020",
    ),
    (
        "STB",
        2019,
        "bvmt-etats-financiers/stb/2019_consolide.pdf",
        "stb_consolide_2019",
        "bvmt-ef-stb-2019-consolide",
    ),
    (
        "BH",
        2021,
        "bvmt-rapports/bh-bank/bh-rapport-annuel-de-gestion-31-12-2021.pdf",
        "bh",
        "bvmt-ra-bh-2021",
    ),
    (
        "BH",
        2017,
        "bvmt-rapports-archives/bh/20221118_Rapport-annuel-Fr_2017.pdf",
        "bh_rapport",
        "ra-bh-2017",
    ),
    (
        "BH",
        2019,
        "bvmt-rapports-archives/bh/20240507_Rapport_BH_2019_FR_VF.pdf",
        "bh_rapport",
        "ra-bh-2019",
    ),
    (
        "BH",
        2021,
        "bvmt-rapports-archives/bh/20240507_BH_Rapport_annuel_2021Part_3.pdf",
        "bh_rapport",
        "ra-bh-2021",
    ),
    (
        "BH",
        2022,
        "bvmt-rapports-archives/bh/20240507_Rapport-Annuel-Fr_2022-PART3.pdf",
        "bh_rapport",
        "ra-bh-2022",
    ),
    (
        "BNA",
        2021,
        "bvmt-rapports/bna/bna-rapport-annuel-de-gestion-31-12-2021.pdf",
        "bna",
        "bvmt-ra-bna-2021",
    ),
]
METHODES = {
    "integration globale": "intégration globale",
    "mise en equivalence": "mise en équivalence",
}
METHODES_STB = {
    "I-G": "intégration globale",
    "IG": "intégration globale",
    "M-E": "mise en équivalence",
    "ME": "mise en équivalence",
}
JETON = re.compile(
    r"(?<![\w.,-])-?\d+[.,]\d+\s*%?|\b(?:I-G|M-E|H-P|IG|ME|HP)\b|(?<!\S)-(?=\s|$)"
)


def texte_brut(chemin: Path) -> str:
    """Texte dans l'ordre des colonnes (sans `-layout`), pour les rapports en deux colonnes."""
    return subprocess.run(
        ["pdftotext", "-raw", str(chemin), "-"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout


LECTEURS_BRUTS = {"bh_rapport"}


def texte(chemin: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(chemin), "-"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def nombre(valeur: str) -> str:
    return valeur.replace(",", ".").rstrip("%")


def normalise_pct(valeur: str) -> str:
    return re.sub(r"\s+", "", valeur).replace(",", ".").rstrip("%")


def propre(nom: str) -> str:
    return re.sub(r"\s*\(\d\)\s*$", "", " ".join(nom.split())).strip()


def methode(valeur: str) -> str:
    cle = (
        unicodedata.normalize("NFKD", valeur).encode("ascii", "ignore").decode().lower()
    )
    return METHODES.get(cle, valeur.lower())


def nettoie_nombres(texte: str) -> str:
    """Recolle les nombres que la mise en page ou l'extraction a coupés (« 70 ,70% », « 0, 30 % »)."""
    texte = re.sub(r"[\x00-\x08\x0b-\x1f]", "", texte)
    texte = re.sub(r"(?<=\d)\s+(?=[.,]\d)", "", texte)
    return re.sub(r"(?<=\d[.,])\s+(?=\d)", "", texte)


# --- STB ---------------------------------------------------------------------------------


def stb(contenu: str, exercice: int = 2021) -> list[list[str]]:
    """Rapport de 2020 et de 2021 : deux tableaux numérotés (contrôle, puis intérêt), chacun avec la
    colonne de l'exercice, celle de l'exercice précédent et la variation ; la méthode n'y figure pas."""
    motif = re.compile(
        r"(\d{1,2})\.\s+(.+?)\s{2,}(\d+,\d+)%\s+(\d+,\d+)%\s+(-?\d+,\d+)%"
    )
    debut = contenu.index("SOCIETES CONSOLIDEES")
    vues: dict[str, dict] = {}
    ordre: list[str] = []
    rang: dict[str, int] = {}
    for ligne in contenu[debut:].splitlines():
        trouve = motif.search(ligne)
        if not trouve:
            continue
        numero, nom = trouve.group(1), propre(trouve.group(2))
        rang[numero] = rang.get(numero, 0) + 1
        if rang[numero] > 2:
            break
        champ = "controle" if rang[numero] == 1 else "interet"
        entree = vues.setdefault(
            numero, {"nom": re.sub(r"\s*\(société Mère\)", "", nom)}
        )
        entree[champ] = (nombre(trouve.group(3)), nombre(trouve.group(4)))
        if numero not in ordre:
            ordre.append(numero)
    lignes = []
    for numero in ordre:
        e = vues[numero]
        for decalage in (0, 1):
            controle = e.get("controle", ("", ""))[decalage]
            interet = e.get("interet", ("", ""))[decalage]
            lignes.append(
                [
                    "STB",
                    str(exercice - decalage),
                    e["nom"],
                    "mère" if numero == "1" else "",
                    controle,
                    interet,
                    "",
                ]
            )
    return lignes


def ligne_stb_ancienne(ligne: str):
    """Une ligne des rapports de la STB de 2011 à 2018 : contrôle (N, N-1, variation), méthode (N, N-1),
    intérêt (N, N-1, variation). Rend (nom, [valeur N, valeur N-1]), chaque valeur étant
    (méthode, contrôle, intérêt) ou None quand l'entité est hors du périmètre cet exercice-là
    (tiret ou « H-P »), ou rend None si la ligne n'a pas huit jetons."""
    ligne = nettoie_nombres(ligne)
    trouve = re.match(
        r"^\s*(?:\d+\s+)?(\d{1,2})\.\s+(?:\d{1,2}\.\s+)?(.+?)\s*(?=(?<![\w.,-])-?\d+[.,]\d+\s*%|\bH-P\b|\bHP\b)",
        ligne,
    )
    if not trouve:
        return None
    nom = propre(re.sub(r"\(société Mère\)", "", trouve.group(2)))
    jetons = [j.group(0).strip() for j in JETON.finditer(ligne[trouve.end() :])]
    if len(jetons) != 8:
        return None
    controle_n, controle_p, _, methode_n, methode_p, interet_n, interet_p, _ = jetons

    def pct(jeton):
        return (
            None
            if jeton in ("-", "H-P", "HP") or not re.match(r"-?\d", jeton)
            else normalise_pct(jeton)
        )

    def valeur(methode_, controle, interet):
        if methode_ not in METHODES_STB or pct(controle) is None:
            return None
        return (METHODES_STB[methode_], pct(controle), pct(interet) or "")

    return nom, [
        valeur(methode_n, controle_n, interet_n),
        valeur(methode_p, controle_p, interet_p),
    ]


def stb_ancien(contenu: str, exercice: int) -> list[list[str]]:
    lignes, vus = [], set()
    debut = contenu.find("% de Contrôle")
    for ligne in contenu[debut:].splitlines() if debut >= 0 else []:
        lue = ligne_stb_ancienne(ligne)
        if not lue:
            continue
        nom, valeurs = lue
        if nom in vus:  # le tableau reparaît plus loin : on garde la première lecture
            continue
        vus.add(nom)
        for decalage, valeur in enumerate(valeurs):
            if valeur:
                mere = nom.startswith("STB BANK")
                lignes.append(
                    [
                        "STB",
                        str(exercice - decalage),
                        nom,
                        "mère" if mere else valeur[0],
                        valeur[1],
                        valeur[2],
                        "Tunisie",
                    ]
                )
    return lignes


# --- BNA et BH -----------------------------------------------------------------------------


def bna(contenu: str, exercice: int = 2021) -> list[list[str]]:
    """Tableau « entités retenues dans le périmètre » : méthode, % de contrôle, % d'intérêt (première occurrence)."""
    motif = re.compile(
        r"^\s*(?:[A-Z]{1,3}\s{2,})?(\S.*?)\s{2,}(Intégration globale|Mise en équivalence)\s+(\d+,\d+)\s*%\s+(\d+,\d+)\s*%"
    )
    lignes, vus = [], set()
    for ligne in contenu.splitlines():
        trouve = motif.match(ligne)
        if trouve:
            nom = propre(trouve.group(1))
            if nom in vus:
                continue
            vus.add(nom)
            mere = (
                "mère"
                if nom == "Banque Nationale Agricole"
                else methode(trouve.group(2))
            )
            lignes.append(
                [
                    "BNA",
                    str(exercice),
                    nom,
                    mere,
                    nombre(trouve.group(3)),
                    nombre(trouve.group(4)),
                    "Tunisie",
                ]
            )
    return lignes


def bna_ancien(contenu: str, exercice: int) -> list[list[str]]:
    """Rapports annuels de 2007 à 2009 : « PERIMETRE DE CONSOLIDATION AU 31/12/… », nom, activité, contrôle, intérêt,
    sous les titres « intégrées globalement » et « mise en équivalence »."""
    debut = contenu.find("PERIMETRE DE CONSOLIDATION AU")
    if debut < 0:
        return []
    motif = re.compile(
        r"^\s*(\S.*?)\s{2,}(?:\S[^%]*?\s{2,})?(\d+,\d+)\s*%\s+(\d+,\d+)\s*%\s*$"
    )
    lignes, mode, vus = [], "intégration globale", set()
    for ligne in contenu[debut : debut + 12000].splitlines():
        minuscule = ligne.lower()
        if "mise en équivalence" in minuscule and "entreprises" in minuscule:
            mode = "mise en équivalence"
        trouve = motif.match(ligne)
        if not trouve:
            continue
        nom = propre(trouve.group(1))
        if nom in vus or nom.upper().startswith(("DENOMINATION", "DÉNOMINATION")):
            continue
        vus.add(nom)
        mere = nom.replace(".", "").upper() == "BNA"
        lignes.append(
            [
                "BNA",
                str(exercice),
                nom,
                "mère" if mere else mode,
                nombre(trouve.group(2)),
                nombre(trouve.group(3)),
                "Tunisie",
            ]
        )
    return lignes


def bh(contenu: str, exercice: int = 2021) -> list[list[str]]:
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
                [
                    "BH",
                    str(exercice),
                    nom,
                    mere,
                    "",
                    nombre(trouve.group(2)),
                    trouve.group(5),
                ]
            )
    return lignes


NOMS_STB_2019 = {
    "STB": "STB BANK",
    "SOFELAN": "SOFI ELAN SICAF",
    "IMM. AVENUE": "L’IMMOBILIERE DE L’AVENUE",
    "STRC": "STE TUN.RECOUVR. DES CREANCES “STRC”",
    "GEVE": "SOCIETE LA GENERALE DES VENTES",
    "EDDKHILA": "SOCIETE ED DKHILA",
    "ACTIVHOTELS": "SOCIETE ACTIVHOTELS",
    "SICAV INVEST": "SICAV L’INVESTISSEUR",
    "SICAV AVENIR": "SICAV L’AVENIR",
    "SICAV OBLIG": "SICAV EPARGNE OBLIGATAIRE",
    "TFB": "TUNISIAN FOREIGN BANK",
    "STBMG": "STE MOYENS GENERAUX",
    "MGERT": "MAGASINS GENERAUX ET ENTREPORTS REELS DE TUNIS",
    "STCV": "S.T.C.V VERITAS",
    "SONIBANK": "SONI BANK",
    "SCIMB": "S.C.I «LA MAISON DU BANQUIER»",
    "ELFEJJA": "S.P.C.M «ELFEJJA»",
    "STBSG": "STB SECURITE ET GARDIENNAGE",
}


def stb_consolide_2019(contenu: str, exercice: int = 2019) -> list[list[str]]:
    """Tableau « 4.1 » des états consolidés de 2019 : une ligne par entité, avec les pourcentages de contrôle
    et d'intérêt de 2019 et de 2018 (révisé) et la méthode de chaque exercice (IG, MEE ou NI : hors périmètre)."""
    motif = re.compile(
        r"^\s*(\S.*?)\s{2,}(\d+,\d+)%\s+(\d+,\d+)%\s+-?\d+,\d+%\s+(IG|MEE|NI)\s+(IG|MEE|NI)\s+(\d+,\d+)%\s+(\d+,\d+)%"
    )
    par_methode = {"IG": "intégration globale", "MEE": "mise en équivalence"}
    lignes = []
    for ligne in contenu.splitlines():
        trouve = motif.match(ligne)
        if not trouve:
            continue
        abrege = " ".join(trouve.group(1).split())
        nom = NOMS_STB_2019.get(abrege, abrege)
        for annee, controle, methode_, interet in (
            (exercice, trouve.group(2), trouve.group(4), trouve.group(6)),
            (exercice - 1, trouve.group(3), trouve.group(5), trouve.group(7)),
        ):
            if methode_ == "NI":
                continue
            mere = "mère" if abrege == "STB" else par_methode[methode_]
            lignes.append(
                [
                    "STB",
                    str(annee),
                    nom,
                    mere,
                    nombre(controle),
                    nombre(interet),
                    "Tunisie",
                ]
            )
    return lignes


def bh_rapport(contenu: str, exercice: int) -> list[list[str]]:
    """Tableau du périmètre d'un rapport annuel de la BH lu en colonne (`pdftotext -raw`) : deux exercices (N et N-1).

    Trois mises en page : deux pourcentages d'intérêt, méthode et pays sur la ligne (2017, 2021, 2022) ; quatre
    pourcentages (contrôle N, contrôle N-1, intérêt N, intérêt N-1) avec la méthode sur les lignes suivantes (2019)."""
    debut = max(
        contenu.find(
            "se présentent comme suit", contenu.find("consolidation, le pourcentage d")
        ),
        contenu.find("Pourcentage d’intérêt"),
        0,
    )
    fin = contenu.find("Méthodes de consolidation", debut)
    lignes_texte = contenu[debut : fin if fin > debut else debut + 4000].splitlines()
    nombre_pct = r"(\d+,\d+|-)"
    deux = re.compile(
        rf"^(\S.*?)\s+{nombre_pct}\s+{nombre_pct}\s+(Intégration Globale|Mise en équivalence)\s+(\w+)\s*$"
    )
    quatre = re.compile(
        rf"^(\S.*?)\s+{nombre_pct}\s+{nombre_pct}\s+{nombre_pct}\s+{nombre_pct}\s*$"
    )
    sortie = []
    for i, ligne in enumerate(lignes_texte):
        ligne = ligne.strip()
        trouve2, trouve4 = deux.match(ligne), quatre.match(ligne)
        if trouve2:
            nom, n, n1, mode, pays = trouve2.groups()
            controle = (None, None)
            interet = (n, n1)
        elif trouve4:
            nom, c, c1, n, n1 = trouve4.groups()
            controle, interet = (c, c1), (n, n1)
            suite = " ".join(x.strip() for x in lignes_texte[i + 1 : i + 4])
            mode = (
                "Mise en équivalence"
                if suite.startswith(("Mise en", "Mise"))
                else "Intégration Globale"
            )
            pays = "France" if "France" in suite else "Tunisie"
        else:
            continue
        nom = propre(nom)
        for annee, ctrl, inter in (
            (exercice, controle[0], interet[0]),
            (exercice - 1, controle[1], interet[1]),
        ):
            if inter in (None, "-"):
                continue
            mere = (
                "mère"
                if nom.upper() in ("BH BANK", "BANQUE DE L’HABITAT")
                else methode(mode)
            )
            sortie.append(
                [
                    "BH",
                    str(annee),
                    nom,
                    mere,
                    nombre(ctrl) if ctrl and ctrl != "-" else "",
                    nombre(inter),
                    pays,
                ]
            )
    return sortie


LECTEURS = {
    "bh_rapport": bh_rapport,
    "stb_consolide_2019": stb_consolide_2019,
    "stb": stb,
    "stb_ancien": stb_ancien,
    "bna": bna,
    "bna_ancien": bna_ancien,
    "bh": bh,
}


def lire_documents(groupes: list[str]) -> list[list[str]]:
    """Lit les documents des groupes demandés ; pour chaque exercice, la lecture du rapport de cet
    exercice l'emporte sur celle du rapport suivant."""
    retenues: dict[tuple[str, str], tuple[int, list[list[str]]]] = {}
    for groupe, exercice, fichier, lecteur, source in DOCUMENTS:
        if groupe not in groupes:
            continue
        chemin = DONNEES / fichier
        if not chemin.exists():
            print(
                f"{groupe} {exercice} : {chemin.name} manque, ignoré", file=sys.stderr
            )
            continue
        lues = LECTEURS[lecteur](
            (texte_brut if lecteur in LECTEURS_BRUTS else texte)(chemin), exercice
        )
        par_exercice: dict[str, list[list[str]]] = {}
        for ligne in lues:
            par_exercice.setdefault(ligne[1], []).append(ligne + [source])
        for annee, lignes in par_exercice.items():
            distance = exercice - int(annee)
            actuel = retenues.get((groupe, annee))
            if actuel is None or (len(lignes), -distance) > (
                len(actuel[1]),
                -actuel[0],
            ):
                retenues[(groupe, annee)] = (distance, lignes)
    return [ligne for (_, lignes) in retenues.values() for ligne in lignes]


def main(arguments: list[str]) -> int:
    groupes = [a.upper() for a in arguments] or ["STB", "BH", "BNA"]
    nouvelles = lire_documents(groupes)
    gardees: list[list[str]] = []
    if SORTIE.exists():
        with SORTIE.open(encoding="utf-8", newline="") as source:
            gardees = [
                [r.get(c, "") for c in COLONNES]
                for r in csv.DictReader(source)
                if r["groupe"] not in groupes
            ]
    tout = gardees + nouvelles
    ordre = {"STB": 0, "BH": 1, "BNA": 2}
    tout.sort(key=lambda r: (ordre.get(r[0], 9), r[1], r[3] != "mère", r[2]))
    with SORTIE.open("w", encoding="utf-8", newline="") as sortie:
        ecrivain = csv.writer(sortie)
        ecrivain.writerow(COLONNES)
        ecrivain.writerows(tout)
    for groupe in groupes:
        par: dict[str, int] = {}
        for r in nouvelles:
            if r[0] == groupe:
                par[r[1]] = par.get(r[1], 0) + 1
        print(
            f"{groupe} : "
            + ", ".join(f"{a} : {n} lignes" for a, n in sorted(par.items()))
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

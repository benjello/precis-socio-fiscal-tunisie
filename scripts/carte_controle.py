#!/usr/bin/env python3
"""Carte de contrôle des entreprises publiques : qui contrôle quoi, au-delà de la liste officielle.

Réunit en une table toutes les relations « contrôleur -> entité contrôlée » déjà documentées,
éparpillées dans plusieurs relevés et plusieurs chapitres, chaque ligne gardant sa clé de source.

Sources réunies :
  1. Périmètres de consolidation des groupes bancaires et de Tunisair
     (listes/groupes-bancaires-perimetre.csv) : dernier exercice de chaque groupe, ligne mère exclue.
  2. Participations de détenteurs publics dans les sociétés cotées
     (listes/societes-cotees-participations.csv).
  3. ETAP : annexe « portefeuille participations » (section @sec-ep-etap-participations,
     _energie.qmd), d'après @etap-ra-2023 et @etap-ra-2022.
  4. STEG : lignes NOMMÉES de la note « titres de participation »
     (@sec-ep-steg-participations) ; le reste du portefeuille est agrégé, non nominatif.
  5. STAR : filiales du groupe consolidé (@sec-ep-ge-star-groupe).

Déduplication : une même contrôlée détenue par un même contrôleur = une ligne ; on garde
l'exercice le plus récent (à égalité, la première source insérée).

COLONNE `secteur` : nature de l'entité contrôlée, LECTURE de son nom et du périmètre de son
contrôleur, assumée comme telle — jamais un poids économique, jamais une activité devinée. La
règle est transparente et conservatrice ; AU MOINDRE DOUTE, « non classé ». Elle se lit sur le
nom normalisé (`normalise`), dans cet ordre :

  1. Un jeton de forme juridique ou d'activité présent DANS le nom tranche seul :
     « sicar »/« fcpr » -> SICAR/capital-investissement ; « sicav »/« sicaf » -> SICAV/OPCVM ;
     « leasing » -> leasing ; « assurance(s) » -> assurance ; « recouvr… » -> recouvrement ;
     « immo »/« foncière » -> immobilier ; « bank »/« banque » -> banque ; « ciment » ->
     industrie ; « énergie » -> énergie-pétrole ; « catering »/« handling »/« technics »/« gardiennage »/« sécurité »/
     « informatique »/« moyens généraux »/« services » -> services.
  2. À défaut, une courte table d'identités ÉTABLIES (SECTEUR_CONNU) nomme les entités dont la
     nature est documentée ailleurs dans le précis : les banques publiques (BH, BNA, BTE, STB,
     BTS), l'assurance (STAR, Tunis Re), le leasing coté (ATL), l'industrie (Air Liquide
     Tunisie), et les participations PROPRES de l'ETAP — sociétés mixtes d'exploration-
     production, de transport et de stockage d'hydrocarbures (@etap-ra-2023) : Joint Oil,
     Joint-Gaz, SERGAZ, NUMHYD, SEREPT, MARETAP, SODEPS, TPS, APO, SEREE, CTKCP, SSC, SCITT,
     TANKMED, SOTUGAT, SOTRAPIL, TRAPSA, SNDP, SOTULUB, BITUMED, Compagnie tunisienne de forage
     -> énergie-pétrole. Ce classement-là est une lecture du PÉRIMÈTRE pétrolier de l'ETAP, non
     du seul nom ; les titres que l'ETAP détient « pour le compte de l'État » (banques, SICAR,
     réassurance) en sont exclus et retombent sur leur propre nature.
  3. Tout le reste — acronymes dont la nature n'est pas établie ici — reste « non classé ».

Aucun nom de fichier n'apparaît dans le texte publié : ce mapping ne vit QUE dans ce docstring.

    uv run python scripts/carte_controle.py            # engendre listes/carte-controle.csv
"""

from __future__ import annotations

import csv
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
LISTES = RACINE / "precis" / "fr" / "entreprises_publiques" / "listes"
SORTIE = LISTES / "carte-controle.csv"

COLONNES = [
    "controleur",
    "controlee",
    "secteur",
    "part_interet_pct",
    "methode",
    "exercice",
    "controleur_dans_liste_officielle",
    "controlee_dans_liste_officielle",
    "source",
]


def normalise(nom: str) -> str:
    """Clé de rapprochement : sans accents, sans ponctuation, en minuscules, espaces repliés."""
    texte = unicodedata.normalize("NFKD", nom)
    texte = "".join(c for c in texte if not unicodedata.combining(c))
    texte = "".join(c if c.isalnum() else " " for c in texte.lower())
    return " ".join(texte.split())


# Contrôleurs sous un nom d'affichage canonique. La clé est le nom tel qu'il arrive de la source ;
# la valeur, le nom retenu dans la carte.
ALIAS_CONTROLEUR = {
    "TUNISAIR": "Tunisair",
    "Banque de l'habitat": "BH",
}

# Un contrôleur est-il une entreprise publique de la liste officielle ? (établie à la main, à
# partir de entreprises-publiques-listes.csv / etablissements-entreprises-publiques.csv.)
CONTROLEUR_OFFICIEL = {
    "STB": "oui",
    "BH": "oui",
    "BNA": "oui",
    "BTE": "non",
    "Tunisair": "oui",
    "ETAP": "oui",
    "STEG": "oui",
    "STAR": "oui",
    "STIR": "oui",
    "Tunisie Télécom": "oui",
    "CNSS": "oui",
    "Office du commerce de la Tunisie": "oui",
    "Office national des postes": "oui",
    "CDC": "non",
    "Caisse des dépôts et consignations": "non",
    "BNA Participations": "non",
    "État": "non",
}

# Entités contrôlées qui SONT des entreprises publiques de la liste officielle (toutes les autres
# sont tenues hors liste). Clé = clé normalisée du nom de la contrôlée.
CONTROLEE_OFFICIELLE_NORM = {
    normalise(n)
    for n in [
        "STB",
        "STB BANK",
        "BNA",
        "BH",
        "Tunisair",
        "STAR",
        "Tunis Re",
        "SOTUMAG",
        "SOTETEL",
        "Ciments de Bizerte",
        "Compagnie tunisienne de forage",  # CTF
        "TRAPSA",  # Compagnie de transport par pipe-line au Sahara
        "SNDP",  # Société nationale de distribution de pétrole
        "BTS",  # Banque tunisienne de solidarité
    ]
}


def controlee_officielle(controlee: str) -> str:
    return "oui" if normalise(controlee) in CONTROLEE_OFFICIELLE_NORM else "non"


# Jeton de forme juridique ou d'activité présent DANS le nom normalisé -> secteur. Ordre
# significatif : le premier jeton rencontré tranche. Voir le docstring du module (règle 1).
SECTEURS_JETON = [
    ("sicar", "SICAR/capital-investissement"),
    ("fcpr", "SICAR/capital-investissement"),
    ("sicav", "SICAV/OPCVM"),
    ("sicaf", "SICAV/OPCVM"),
    ("leasing", "leasing"),
    ("recouvr", "recouvrement"),
    ("assurance", "assurance"),
    ("immo", "immobilier"),
    ("fonciere", "immobilier"),
    ("ciment", "industrie"),
    ("energie", "énergie-pétrole"),
    ("catering", "services"),
    ("handling", "services"),
    ("technics", "services"),
    ("gardiennage", "services"),
    ("securite", "services"),
    ("informatique", "services"),
    ("moyens generaux", "services"),
    ("services", "services"),
    ("bank", "banque"),
    ("banque", "banque"),
]

# Identités ÉTABLIES ailleurs dans le précis (règle 2 du docstring), par nom normalisé. Prime sur
# les jetons. Les participations propres de l'ETAP sont une lecture de son périmètre pétrolier.
SECTEUR_CONNU = {
    normalise(n): s
    for n, s in {
        "BH": "banque", "BNA": "banque", "BTE": "banque", "STB": "banque", "BTS": "banque",
        "STAR": "assurance", "Tunis Re": "assurance", "TUNIS-RE": "assurance",
        "ATL": "leasing",
        "Air Liquide Tunisie": "industrie",
        "Joint Oil": "énergie-pétrole", "Joint-Gaz": "énergie-pétrole",
        "SERGAZ": "énergie-pétrole", "NUMHYD": "énergie-pétrole", "SEREPT": "énergie-pétrole",
        "MARETAP": "énergie-pétrole", "SODEPS": "énergie-pétrole", "TPS": "énergie-pétrole",
        "APO": "énergie-pétrole", "SEREE": "énergie-pétrole", "CTKCP": "énergie-pétrole",
        "SSC": "énergie-pétrole", "SCITT": "énergie-pétrole", "TANKMED": "énergie-pétrole",
        "SOTUGAT": "énergie-pétrole", "SOTRAPIL": "énergie-pétrole", "TRAPSA": "énergie-pétrole",
        "SNDP": "énergie-pétrole", "SOTULUB": "énergie-pétrole", "BITUMED": "énergie-pétrole",
        "Compagnie tunisienne de forage": "énergie-pétrole",
    }.items()
}


def secteur(controlee: str) -> str:
    """Nature de l'entité contrôlée, lue sur son nom et le périmètre ; « non classé » au doute."""
    cle = normalise(controlee)
    if cle in SECTEUR_CONNU:
        return SECTEUR_CONNU[cle]
    for jeton, sect in SECTEURS_JETON:
        if jeton in cle:
            return sect
    return "non classé"


def lignes_perimetres() -> list[dict]:
    """Dernier exercice de chaque groupe consolidant, ligne mère exclue."""
    rows = list(csv.DictReader((LISTES / "groupes-bancaires-perimetre.csv").open(encoding="utf-8")))
    dernier: dict[str, int] = {}
    for r in rows:
        g, e = r["groupe"], int(r["exercice"])
        dernier[g] = max(dernier.get(g, e), e)
    out = []
    for r in rows:
        if int(r["exercice"]) != dernier[r["groupe"]]:
            continue
        if (r["methode"] or "").strip() == "mère":
            continue
        ctrl = ALIAS_CONTROLEUR.get(r["groupe"], r["groupe"])
        part = r["interet_pct"] or r["controle_pct"]  # Tunisair ne donne que les droits de vote
        out.append(
            {
                "controleur": ctrl,
                "controlee": r["entite"],
                "part_interet_pct": part,
                "methode": r["methode"],
                "exercice": r["exercice"],
                "source": r["source"],
            }
        )
    return out


def lignes_cotees() -> list[dict]:
    """Participations de détenteurs publics dans les sociétés cotées."""
    rows = list(
        csv.DictReader((LISTES / "societes-cotees-participations.csv").open(encoding="utf-8"))
    )
    out = []
    for r in rows:
        ctrl = ALIAS_CONTROLEUR.get(r["detenteur"], r["detenteur"])
        exercice = r["assemblee"].split("/")[-1] if r["assemblee"] else ""
        out.append(
            {
                "controleur": ctrl,
                "controlee": r["societe"],
                "part_interet_pct": r["part_pct"],
                "methode": "",  # participation, pas une consolidation
                "exercice": exercice,
                "source": f"bvmt-{r['page']}",
            }
        )
    return out


def _l(controleur, controlee, part, exercice, source, methode=""):
    return {
        "controleur": controleur,
        "controlee": controlee,
        "part_interet_pct": part,
        "methode": methode,
        "exercice": exercice,
        "source": source,
    }


def lignes_etap() -> list[dict]:
    """Portefeuille participations de l'ETAP (@sec-ep-etap-participations).

    Taux repris du texte, sourcés @etap-ra-2023 (p. 120-121) ; les neuf titres « détenus pour le
    compte de l'État » du même rapport (p. 121). Les participations sans taux imprimé (SNDP
    symbolique, BTS, STUSID Bank, TECI, SNIPE, ITF, S.A.G.E.S, BTL) : part laissée vide.
    """
    ra23 = "etap-ra-2023"
    propres = [
        ("Joint Oil", "50"),
        ("NUMHYD", "50"),
        ("SEREPT", "50"),
        ("CTKCP", "50"),
        ("MARETAP", "50"),
        ("SODEPS", "50"),
        ("TPS", "50"),
        ("APO", "50"),
        ("SEREE", "50"),
        ("Compagnie tunisienne de forage", "90"),
        ("SOTUGAT", "99.8"),
        ("TANKMED", "40"),
        ("SERGAZ", "33.23"),
        ("SOTRAPIL", "18.28"),
        ("SODIK-SICAR", "59.98"),
        ("SODIT-SICAR", "48"),
        ("FCPR TAAHIL INVEST", "71.43"),
        ("SCITT", "50"),
        ("SSC", "40"),
        ("SOTULUB", "27.09"),
        ("PAEZ", "12.4"),
        ("BITUMED", "8"),
        ("SNDP", ""),
        ("BTS", ""),
        ("STUSID Bank", ""),
        ("TECI", ""),
        ("SNIPE", ""),
        ("ITF", ""),
        ("S.A.G.E.S", ""),
    ]
    # « Titres détenus pour le compte de l'État » (p. 121). SCITT y revient pour 12,50 % : déjà
    # présente ci-dessus à 50 %, on ne la redouble pas (la clé contrôleur->contrôlée est unique).
    compte_etat = [
        ("BH", "16.57"),
        ("STAR", "19.02"),
        ("Tunis Re", "3.79"),
        ("BNA", "2.27"),
        ("STB", "2.22"),
        ("TRAPSA", "35"),
        ("SGTBC", "2.43"),
        ("BTL", ""),
    ]
    out = [_l("ETAP", nom, part, "2023", ra23) for nom, part in propres]
    out += [_l("ETAP", nom, part, "2023", ra23) for nom, part in compte_etat]
    return out


def lignes_steg() -> list[dict]:
    """Lignes NOMMÉES de la note « titres de participation » de la STEG (@sec-ep-steg-participations).

    La note agrège un portefeuille de 32 à 35 entreprises et ne nomme que les principales ; les
    montants sont en dinars, pas de taux de détention : part laissée vide.
    """
    return [
        _l("STEG", "STB", "", "2023", "steg-ef-2023"),
        _l("STEG", "Technopole de Borj Cedria", "", "2023", "steg-ef-2023"),
        _l("STEG", "Joint-Gaz", "", "2023", "steg-ef-2023"),
        _l("STEG", "Elmed Études", "", "2023", "steg-ef-2023"),
        _l("STEG", "SODIT SICAR", "", "2018", "steg-ef-2018"),
        _l("STEG", "STEG Énergies renouvelables", "", "2014", "steg-ef-2014"),
    ]


def lignes_star() -> list[dict]:
    """Filiales du groupe STAR consolidé (@sec-ep-ge-star-groupe)."""
    return [
        _l("STAR", "La Lyre Immobilière", "99.997", "2021", "bvmt-ef-star-2021-consolide",
           "intégration globale"),
        _l("STAR", "Institut africain des assurances", "", "2022", "bvmt-ef-star-2022-consolide",
           "intégration globale"),
    ]


def carte() -> list[dict]:
    # Ordre d'insertion = ordre de priorité à la déduplication : périmètres (méthode + intérêt
    # consolidé), puis cotées, ETAP, STEG, STAR.
    brut = (
        lignes_perimetres()
        + lignes_cotees()
        + lignes_etap()
        + lignes_steg()
        + lignes_star()
    )
    retenues: dict[tuple[str, str], dict] = {}
    for r in brut:
        cle = (normalise(r["controleur"]), normalise(r["controlee"]))
        ex = int(r["exercice"]) if r["exercice"] else 0
        garde = retenues.get(cle)
        if garde is None or ex > (int(garde["exercice"]) if garde["exercice"] else 0):
            retenues[cle] = r
    lignes = []
    for r in retenues.values():
        r = dict(r)
        r["controleur_dans_liste_officielle"] = CONTROLEUR_OFFICIEL.get(r["controleur"], "non")
        r["controlee_dans_liste_officielle"] = controlee_officielle(r["controlee"])
        r["secteur"] = secteur(r["controlee"])
        lignes.append({c: r.get(c, "") for c in COLONNES})
    lignes.sort(key=lambda r: (r["controleur"], r["controlee"]))
    return lignes


def ecrire(lignes: list[dict]) -> None:
    with SORTIE.open("w", encoding="utf-8", newline="") as flux:
        ecrivain = csv.DictWriter(flux, fieldnames=COLONNES)
        ecrivain.writeheader()
        ecrivain.writerows(lignes)


def main() -> None:
    lignes = carte()
    ecrire(lignes)
    controleurs = {l["controleur"] for l in lignes}
    hors = {l["controlee"] for l in lignes if l["controlee_dans_liste_officielle"] == "non"}
    print(f"{SORTIE.relative_to(RACINE)} : {len(lignes)} relations")
    print(f"  contrôleurs : {len(controleurs)}")
    print(f"  entités contrôlées distinctes : {len({l['controlee'] for l in lignes})}")
    print(f"  entités contrôlées hors liste officielle (distinctes) : {len(hors)}")
    from collections import Counter

    par_secteur = Counter(l["secteur"] for l in lignes)
    non_classe = par_secteur.get("non classé", 0)
    print(f"  relations classées par secteur : {len(lignes) - non_classe} ; non classées : {non_classe}")
    for sect, n in sorted(par_secteur.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"    {sect} : {n}")


if __name__ == "__main__":
    main()

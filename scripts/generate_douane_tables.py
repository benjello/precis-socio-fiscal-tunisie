"""Régénère les instantanés des tableaux de la redevance et du minimum de perception, depuis openfisca.

Le build du site n'exécute PAS ce script : il lit les fichiers qu'il produit, versionnés dans
`precis/fr/fiscalite/tables/`. Le lancer suppose une copie d'openfisca-tunisia :

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_douane_tables.py

DEUX SOURCES, COMME POUR LE DROIT DE CONSOMMATION. Les montants et les taux viennent des
paramètres de `fiscalite_indirecte/droits_douane/` (versés par openfisca-tunisia#516, version
0.156) ; le relevé `precis/fr/fiscalite/douane/tarifs-releves-droits-douane.csv` garde ce que
les paramètres ne portent pas : les dates en lettres, la prose de l'assiette, la citation de
chaque ligne. La génération échoue si une valeur lue diverge de la cellule du relevé : un
tableau faux doit casser la génération, jamais s'imprimer.

CE QUI EST LU, CE QUI NE L'EST PAS.
- `redevance` : la colonne « Minimum » (minimum de perception par article, à l'importation, et
  à l'exportation quand la ligne le dit) ; les taux à l'importation et à l'exportation et les
  100 D du transit terrestre, que la prose de l'assiette énonce et que le script contrôle. Les
  10 % du produit affectés aux agents des douanes (1994-2013) ne sont pas un paramètre : la
  phrase vient du relevé.
- `minimum-perception` : les deux colonnes, taux général et biens d'équipement. La nuance
  « au plus » de 1987 (un plafond, non un plancher) est du relevé.
- Restent au relevé, faute de paramètre (openfisca-tunisia#517) : les tables de
  correspondance, les bandes du tarif, le registre des lois de finances récentes, l'état du droit.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

RACINE = Path(__file__).parent.parent
CSV_RELEVE = RACINE / "precis/fr/fiscalite/douane/tarifs-releves-droits-douane.csv"
BRANCHE = "parameters/fiscalite_indirecte/droits_douane"
RED = f"{BRANCHE}/redevance_prestations_douanieres"
MIN_IMPORT = f"{RED}/importation/minimum_par_article.yaml"
MIN_EXPORT = f"{RED}/exportation/minimum_par_article.yaml"
TAUX_IMPORT = f"{RED}/importation/taux_sur_droits_et_taxes.yaml"
TAUX_EXPORT = f"{RED}/exportation/taux_sur_valeur_en_douane.yaml"
TRANSIT = f"{RED}/transit_terrestre/par_declaration.yaml"
MIN_GENERAL = f"{BRANCHE}/minimum_perception/taux_general.yaml"
MIN_EQUIPEMENT = f"{BRANCHE}/minimum_perception/biens_equipement.yaml"

# Libellé du lien « Base législative » de chaque paramètre lu par le tableau de la redevance.
LIBELLES_REDEVANCE = {
    TAUX_IMPORT: "Redevance de prestations douanières — taux à l'importation",
    MIN_IMPORT: "Redevance de prestations douanières — minimum par article à l'importation",
    TAUX_EXPORT: "Redevance de prestations douanières — taux à l'exportation",
    MIN_EXPORT: "Redevance de prestations douanières — minimum par article à l'exportation",
    TRANSIT: "Redevance de prestations douanières — transit terrestre",
}

# Tableau du relevé -> (instantané, chemin sous `tables/`).
TABLEAUX = {
    "redevance": "droits_douane_redevance.md",
    "minimum-perception": "droits_douane_minimum_perception.md",
}


def _nombre(valeur: float) -> str:
    """1.5 -> « 1,5 » ; 20.0 -> « 20 »."""
    return f"{valeur:g}".replace(".", ",")


def _pourcentage(fraction: float) -> str:
    """0.015 -> « 1,5 » : les paramètres portent la fraction, les textes le pourcentage."""
    return _nombre(round(fraction * 100, 4))


def _a(chemin: str, date: str) -> float:
    """Valeur du paramètre en vigueur à `date` ; échoue s'il n'y en a pas."""
    point = ot.en_vigueur(ot.serie_datee(chemin), date)
    if point is None or point[1] is None:
        raise ValueError(f"{chemin} : aucune valeur en vigueur au {date}")
    return point[1]


def _lignes(nom: str) -> list[dict]:
    with CSV_RELEVE.open(encoding="utf-8", newline="") as f:
        return [r for r in csv.DictReader(f) if r["tableau"] == nom]


def _publiee(r: dict) -> str:
    import tarifs as releves
    return releves.recompose(r["valeur"], r["unite"], r["statut"])


def _controle_minimum(r: dict, publiee: str) -> None:
    """Le minimum du relevé doit être celui des paramètres à la date d'effet de la ligne."""
    date = r["date_effet"]
    importation = _nombre(_a(MIN_IMPORT, date))
    exportation = _nombre(_a(MIN_EXPORT, date))
    if "exportation" in publiee:
        attendu = {f"{importation} D à l'importation ; {exportation} D à l'exportation"}
    else:
        attendu = {f"{importation} D par article", f"{importation} D"}
    if publiee not in attendu:
        raise ValueError(f"redevance / {date} / minimum : les paramètres rendent "
                         f"« {' ou '.join(sorted(attendu))} », le relevé « {publiee} »")


def _controle_assiette(r: dict) -> None:
    """Les taux et le transit que la prose énonce doivent être ceux des paramètres."""
    date, texte = r["date_effet"], r["produit"]
    if "droits et taxes liquidés" in texte:
        attendu = f"{_pourcentage(_a(TAUX_IMPORT, date))} % des droits et taxes liquidés"
        if attendu not in texte:
            raise ValueError(f"redevance / {date} : le taux à l'importation est "
                             f"« {attendu} » dans les paramètres, le relevé dit « {texte} »")
    if "de la valeur" in texte:
        attendu = f"{_pourcentage(_a(TAUX_EXPORT, date))} % de la valeur"
        if attendu not in texte:
            raise ValueError(f"redevance / {date} : le taux à l'exportation est "
                             f"« {attendu} » dans les paramètres, le relevé dit « {texte} »")
    if "transit terrestre" in texte:
        attendu = f"{_nombre(_a(TRANSIT, date))} D par déclaration de transit terrestre"
        if attendu not in texte:
            raise ValueError(f"redevance / {date} : le transit est « {attendu} » dans les "
                             f"paramètres, le relevé dit « {texte} »")


def _controle_minimum_perception(r: dict, publiee: str) -> None:
    chemin = MIN_GENERAL if r["colonne"] == "Minimum de perception" else MIN_EQUIPEMENT
    attendu = _pourcentage(_a(chemin, r["date_effet"]))
    nombre = publiee.split(" %")[0]
    if nombre != attendu:
        raise ValueError(f"minimum-perception / {r['date_effet']} / {r['colonne']} : le "
                         f"paramètre rend « {attendu} % », le relevé « {publiee} »")


def tableau(nom_releve: str):
    """Un tableau du relevé, rendu après contrôle contre les paramètres.

    Rend (DataFrame, nombre de cases lues).
    """
    import pandas as pd
    import tarifs as releves

    spec = releves.TABLEAUX[nom_releve]
    lignes: dict[int, dict[str, str]] = {}
    lus = 0
    for r in _lignes(nom_releve):
        publiee = _publiee(r)
        if r["statut"] == "lu":
            if nom_releve == "redevance":
                _controle_minimum(r, publiee)
                _controle_assiette(r)
                for chemin in LIBELLES_REDEVANCE:
                    if chemin != TRANSIT or "transit" in r["produit"]:
                        ot.releve_note(chemin, LIBELLES_REDEVANCE[chemin])
            else:
                _controle_minimum_perception(r, publiee)
                ot.releve_note(MIN_GENERAL if r["colonne"] == "Minimum de perception"
                               else MIN_EQUIPEMENT, r["colonne"])
            lus += 1
        ligne = lignes.setdefault(int(r["ordre"]), {"position": r["position"],
                                                    "produit": r["produit"]})
        ligne[r["colonne"]] = publiee
        if r.get("texte"):
            ligne.setdefault("@texte", "[@" + r["texte"]
                             + (", " + r["article"] if r.get("article") else "") + "]")
    df = pd.DataFrame([[lignes[o].get(c, "") for c in spec["champs"]] for o in sorted(lignes)],
                      columns=spec["entetes"])
    return df, lus


def main() -> int:
    if not ot.openfisca_utilisable():
        print(f"openfisca-tunisia indisponible ou trop ancien (version "
              f"{ot.version_openfisca()}). Définir OPENFISCA_TUNISIA_PATH.", file=sys.stderr)
        return 1
    for nom_releve, fichier in TABLEAUX.items():
        try:
            (df, lus), liens = ot.avec_liens(lambda: tableau(nom_releve))
        except ValueError as erreur:
            print(f"Les paramètres ne correspondent plus au relevé du précis : {erreur}",
                  file=sys.stderr)
            return 1
        sortie = RACINE / "precis" / "fr" / "fiscalite" / "tables" / fichier
        sortie.parent.mkdir(parents=True, exist_ok=True)
        ot.ecrire_tableau(
            sortie, df, liens, "fr", a_gauche=True,
            entete="<!-- Généré par scripts/generate_douane_tables.py — ne pas éditer à la main.\n"
            f"     Cases lues dans {BRANCHE} ; les autres viennent du relevé\n"
            "     precis/fr/fiscalite/douane/tarifs-releves-droits-douane.csv, qui sert de "
            "garde-fou. -->\n\n",
        )
        print(f"  {sortie.relative_to(RACINE)} : {len(df)} lignes, {lus} cases lues")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

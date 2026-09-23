"""Régénère l'instantané du tarif pétrolier du droit de consommation, depuis openfisca.

Le build du site n'exécute PAS ce script : il lit le fichier qu'il produit, versionné dans
`precis/fr/fiscalite/tables/`. Le lancer suppose une copie d'openfisca-tunisia :

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_droit_consommation_tables.py

DEUX SOURCES, ET C'EST LE POINT. Les valeurs viennent des paramètres openfisca ; le relevé
`precis/fr/fiscalite/tarifs/tarifs-releves-droits-consommation.csv` sert de GARDE-FOU. Le
script échoue si les deux divergent d'un millième. C'est la même protection que
`CONTROLE_1990` dans `generate_bareme_tables.py` : un tableau faux doit casser la
génération, jamais s'imprimer.

POURQUOI LE FRANÇAIS SEUL. Les autres tableaux engendrés ne traduisent que leurs en-têtes,
leurs données étant des nombres et des clés de citation. Celui-ci porte des NOMS DE
PRODUITS — « white spirit non dénaturé », « fuel-oil domestique ». Les engendrer dans le
livre arabe y déposerait du français non traduit, en contournant la chaîne de traduction ;
et la terminologie arabe n'appartient pas à ce script. Le livre arabe garde donc son
tableau traduit, et cet instantané ne le remplace pas.

ENREGISTRÉ EN INTÉGRATION CONTINUE. `verifier-snapshots.yml` régénère les tableaux depuis
openfisca-tunisia sur `ref: master` et échoue si le résultat diffère du versionné ; ce
script figure dans sa liste d'exécution. Les deux gestes — l'inscription et le versionnement
de l'instantané — ont attendu ensemble la fusion d'openfisca/openfisca-tunisia#427, qui a
porté les paramètres `produits_petroliers` dans `master`. Les poser plus tôt aurait soit
fait échouer la CI, soit laissé l'instantané NON GARDÉ, c'est-à-dire libre de survivre à la
correction du paramètre qu'il reflète — le pourrissement silencieux que ce job combat.

CE QUE LE TABLEAU NE PORTE PAS. Trois colonnes datées, quand le chapitre en publie quatre :
l'état consolidé de 2023 n'a pas de date d'effet établie et n'est donc pas versé dans
openfisca. Deux lignes nées après 1999 manquent pour la même raison. Cet instantané est
une VÉRIFICATION que le modèle et le précis s'accordent, non un remplacement du tableau
publié, qui reste plus complet.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

RACINE = Path(__file__).parent.parent
CSV_RELEVE = RACINE / "precis/fr/fiscalite/tarifs/tarifs-releves-droits-consommation.csv"
SORTIE = RACINE / "precis/fr/fiscalite/tables/droit_consommation_petroliers.md"
BRANCHE = "parameters/fiscalite_indirecte/accises/produits_petroliers"

# Produit du relevé -> nom du paramètre openfisca. La même table que celle du versement :
# elle est explicite, jamais translittérée, deux produits ne pouvant pas partager un nom.
NOMS = {
    "huiles brutes de pétrole ou de minéraux bitumineux": "huiles_brutes",
    "essence super": "essence_super",
    "essence super sans plomb": "essence_super_sans_plomb",
    "essence normale": "essence_normale",
    "essence avion (kérosène, y compris carburéacteur)": "essence_avion",
    "white spirit non dénaturé": "white_spirit",
    "pétrole lampant": "petrole_lampant",
    "gaz-oil": "gaz_oil",
    "fuel-oil domestique": "fuel_oil_domestique",
    "fuel-oil léger": "fuel_oil_leger",
    "fuel-oil lourd": "fuel_oil_lourd",
    "huiles de graissage et lubrifiants": "huiles_graissage_lubrifiants",
    "huiles de vaseline et de paraffine": "huiles_vaseline_paraffine",
    "autres": "autres_position_27_10",
    "propane et butane": "propane_butane",
    "propane et butane, bouteilles ≤ 13 kg": "propane_butane_bouteilles_13kg_ou_moins",
    "propane et butane, en vrac ou bouteilles > 13 kg":
        "propane_butane_vrac_ou_bouteilles_plus_13kg",
}
COLONNES = [("1988", "1988-07-01"), ("1991", "1991-02-05"), ("1999", "1999-04-22")]


def formate_tarif(valeur: float) -> str:
    """15.228 -> « 15,228 » ; 4.7456 -> « 4,7456 » ; 0.4 -> « 0,400 ».

    PAS `formate_dinars`, qui tronque à trois décimales : douze tarifs de 1991 et de 1999
    en portent quatre, et seraient silencieusement altérés. On rend les décimales
    significatives, complétées à droite jusqu'à trois au minimum — les deux formes que
    le tableau publié emploie.
    """
    texte = f"{valeur:.4f}".rstrip("0")
    entier, _, decimales = texte.partition(".")
    decimales = decimales.ljust(3, "0")
    return f"{entier},{decimales}"


def releve() -> dict[int, dict[str, dict]]:
    """Le relevé du précis, indexé par ligne puis par colonne. Sert de garde-fou."""
    par_ordre: dict[int, dict[str, dict]] = {}
    with CSV_RELEVE.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r["tableau"] == "petroliers":
                par_ordre.setdefault(int(r["ordre"]), {})[r["colonne"]] = r
    return par_ordre


def tarifs(par_ordre: dict[int, dict[str, dict]]) -> tuple[list | None, list[str], int]:
    """Lignes du tableau, écarts avec le relevé, nombre de valeurs lues.

    Chaque paramètre lu est noté au relevé sous le nom du produit : c'est le libellé de
    son lien vers la base législative. `None` en tête signale un paramètre inutilisable.
    """
    lignes, ecarts, lus = [], [], 0
    for ordre in sorted(par_ordre):
        cols = par_ordre[ordre]
        base = cols["1988"]
        produit, position = base["produit"], base["position"]
        nom = NOMS.get(produit)
        if nom is None:  # ligne née après 1999, non versée dans openfisca
            continue

        chemin = f"{BRANCHE}/{nom}.yaml"
        serie = {d: v for d, v, _t, _h in ot.serie_datee(chemin)}
        if not serie:
            print(f"paramètre introuvable ou vide : {nom}", file=sys.stderr)
            return None, ecarts, lus

        ot.releve_note(chemin, produit)
        ligne = {"Position": position, "Produit": produit}
        for entete, date in COLONNES:
            attendu = cols.get(entete)
            valeur = serie.get(date)
            # Une colonne absente du relevé, ou un paramètre sans valeur à cette date,
            # ne se distingue pas d'une cellule légitimement vide : on la rend telle.
            if attendu is None or date not in serie:
                ligne[entete] = "—"
                continue
            if valeur is None:
                print(f"paramètre {nom} : valeur nulle au {date}", file=sys.stderr)
                return None, ecarts, lus
            ligne[entete] = f"{formate_tarif(valeur)} {attendu['unite']}"
            lus += 1
            # garde-fou : openfisca et le relevé du précis doivent dire la même chose
            cible = float(attendu["valeur"].replace(",", "."))
            if abs(valeur - cible) > 1e-9:
                ecarts.append(f"{nom} @{date} : openfisca={valeur} relevé={cible}")
        lignes.append(ligne)
    return lignes, ecarts, lus


def main() -> int:
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version "
            f"{ot.version_openfisca()}). Définir OPENFISCA_TUNISIA_PATH.",
            file=sys.stderr,
        )
        return 1

    (lignes, ecarts, lus), liens = ot.avec_liens(lambda: tarifs(releve()))
    if lignes is None:
        return 1

    if ecarts:
        print("Les paramètres openfisca ne correspondent plus au relevé du précis :",
              file=sys.stderr)
        for e in ecarts:
            print("  " + e, file=sys.stderr)
        return 1

    import pandas as pd

    df = pd.DataFrame(lignes, columns=["Position", "Produit"] + [c for c, _ in COLONNES])
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    ot.ecrire_tableau(
        SORTIE, df, liens, "fr",
        entete="<!-- Généré par scripts/generate_droit_consommation_tables.py — ne pas "
        "éditer à la main.\n"
        f"     Paramètres : {BRANCHE}\n"
        "     Garde-fou : precis/fr/fiscalite/tarifs/"
        "tarifs-releves-droits-consommation.csv\n"
        "     Français seul : les noms de produits ne sont pas traduits ici. -->\n\n",
    )
    print(f"  {SORTIE.relative_to(RACINE)}")
    print(f"  lignes : {len(lignes)}   valeurs lues depuis openfisca : {lus}")
    print(f"  écarts avec le relevé : {len(ecarts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

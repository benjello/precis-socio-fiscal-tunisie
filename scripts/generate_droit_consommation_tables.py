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

LES NOMS DE PRODUITS RESTENT EN FRANÇAIS DANS LE LIVRE ARABE. Les tableaux portent des noms
de produits — « white spirit non dénaturé », « fuel-oil domestique » — dont la terminologie
arabe est celle de l'édition arabe des textes, que ce script ne tient pas : elle relève du
terminologue (precis/glossaire.yml). En attendant, l'instantané arabe traduit les en-têtes,
les états et les unités, et garde les noms tels que le relevé les donne — ce qu'imprimait
déjà le livre arabe, qui lisait le relevé français.

ENREGISTRÉ EN INTÉGRATION CONTINUE. `verifier-snapshots.yml` régénère les tableaux depuis
openfisca-tunisia sur `ref: master` et échoue si le résultat diffère du versionné ; ce
script figure dans sa liste d'exécution. Les deux gestes — l'inscription et le versionnement
de l'instantané — ont attendu ensemble la fusion d'openfisca/openfisca-tunisia#427, qui a
porté les paramètres `produits_petroliers` dans `master`. Les poser plus tôt aurait soit
fait échouer la CI, soit laissé l'instantané NON GARDÉ, c'est-à-dire libre de survivre à la
correction du paramètre qu'il reflète — le pourrissement silencieux que ce job combat.

LE TABLEAU PUBLIÉ EST ENGENDRÉ, ET NON PLUS SEULEMENT CONTRÔLÉ (recension des paramètres
en dur, FI-30 et FI-33, 3 octobre 2026). Chaque case que le paramètre porte — tarifs de 1988,
1991 et 1999 — y est lue ; les autres viennent du relevé, qui reste la source de ce que le
paramètre ne porte pas : l'état consolidé de 2023, dont la date d'effet n'est pas établie,
les lignes nées après 1999, les états « ligne inexistante », « ligne scindée », « non
établi », et, au tarif spécifique de 1988, les alcools et les explosifs. Une case lue qui ne
rend pas exactement la cellule du relevé fait échouer la génération.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

RACINE = Path(__file__).parent.parent
CSV_RELEVE = RACINE / "precis/fr/fiscalite/tarifs/tarifs-releves-droits-consommation.csv"
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


# Le tarif spécifique de 1988 écrit autrement deux des produits du tarif pétrolier.
ALIAS = {
    "essence avion (kérosène), y compris carburéacteur":
        "essence avion (kérosène, y compris carburéacteur)",
    "gas-oil": "gaz-oil",
}
# Tableaux engendrés : tableau du relevé -> (instantané, colonne -> date du paramètre).
TABLEAUX = {
    "petroliers": ("droit_consommation_petroliers.md", dict(COLONNES)),
    "specifiques-1988": ("droit_consommation_specifiques_1988.md", {"Tarif 1988": "1988-07-01"}),
}
# Arabe : en-têtes, états et unités. Les noms de produits restent ceux du relevé (en-tête).
AR = {
    "Position": "الموقع التعريفي", "Produit": "المنتوج", "Tarif 1988": "تعريفة 1988",
    "Consolidé 2023": "الحالة المجمّعة 2023",
    "*(ligne inexistante)*": "*(سطر غير موجود)*", "*(ligne scindée)*": "*(سطر مقسّم)*",
    "*(non établi)*": "*(غير ثابت)*",
}
UNITES_AR = {"D/hl": "د/هكتولتر", "D/100 kg": "د/100 كغ", "D/tonne": "د/طن",
             "D/m^3^": "د/م^3^"}


def _ar(texte: str) -> str:
    if texte in AR:
        return AR[texte]
    for unite, traduction in UNITES_AR.items():
        if texte.endswith(" " + unite):
            return texte[: -len(unite)] + traduction
    return texte


def tableau(nom_releve: str, langue: str):
    """Un tableau du relevé, chaque case lue dans le paramètre quand il la porte.

    Rend (DataFrame, nombre de cases lues). Lève une erreur si une case lue diverge du relevé.
    """
    import pandas as pd
    import tarifs as releves

    spec = releves.TABLEAUX[nom_releve]
    _fichier, dates = TABLEAUX[nom_releve]
    lignes: dict[int, dict[str, str]] = {}
    lus = 0
    with CSV_RELEVE.open(encoding="utf-8", newline="") as f:
        rangs = [r for r in csv.DictReader(f) if r["tableau"] == nom_releve]
    for r in rangs:
        publiee = releves.recompose(r["valeur"], r["unite"], r["statut"])
        case = publiee
        produit = ALIAS.get(r["produit"], r["produit"])
        nom = NOMS.get(produit)
        date = dates.get(r["colonne"])
        if nom and date and r["statut"] == "lu" and r["valeur"]:
            chemin = f"{BRANCHE}/{nom}.yaml"
            serie = {d: v for d, v, _t, _h in ot.serie_datee(chemin)}
            if date in serie:
                if serie[date] is None:
                    raise ValueError(f"paramètre {nom} : valeur nulle au {date}")
                case = f"{formate_tarif(serie[date])} {r['unite']}"
                if case != publiee:
                    raise ValueError(f"{nom_releve} / {r['produit']} / {r['colonne']} : le "
                                     f"paramètre rend « {case} », le relevé « {publiee} »")
                ot.releve_note(chemin, r["produit"])
                lus += 1
        ligne = lignes.setdefault(int(r["ordre"]), {"position": r["position"],
                                                    "produit": r["produit"]})
        ligne[r["colonne"]] = case if langue == "fr" else _ar(case)
    entetes = spec["entetes"] if langue == "fr" else [_ar(e) for e in spec["entetes"]]
    df = pd.DataFrame([[lignes[o].get(c, "") for c in spec["champs"]] for o in sorted(lignes)],
                      columns=entetes)
    return df, lus


def main() -> int:
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version "
            f"{ot.version_openfisca()}). Définir OPENFISCA_TUNISIA_PATH.",
            file=sys.stderr,
        )
        return 1
    sys.path.insert(0, str(Path(__file__).parent))
    for langue in ("fr", "ar"):
        for nom_releve, (fichier, _dates) in TABLEAUX.items():
            try:
                (df, lus), liens = ot.avec_liens(lambda: tableau(nom_releve, langue))
            except ValueError as erreur:
                print(f"Les paramètres ne correspondent plus au relevé du précis : {erreur}",
                      file=sys.stderr)
                return 1
            sortie = RACINE / "precis" / langue / "fiscalite" / "tables" / fichier
            sortie.parent.mkdir(parents=True, exist_ok=True)
            ot.ecrire_tableau(
                sortie, df, liens, langue, a_gauche=True,
                entete="<!-- Généré par scripts/generate_droit_consommation_tables.py — ne pas "
                "éditer à la main.\n"
                f"     Cases lues dans {BRANCHE} ; les autres viennent du relevé\n"
                "     precis/fr/fiscalite/tarifs/tarifs-releves-droits-consommation.csv, qui "
                "sert de garde-fou. -->\n\n",
            )
            print(f"  {sortie.relative_to(RACINE)} : {len(df)} lignes, {lus} cases lues")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

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

LE TARIF DES BIÈRES, VINS ET ALCOOLS (positions 22-03 à 22-08, `tbl-dc-alcools-tarifs`) EST
ENGENDRÉ DE LA MÊME MANIÈRE depuis `fiscalite_indirecte/accises/bieres_vins_alcools/`. Les
douze lignes et les cinq colonnes sont celles du relevé ; chaque case est lue dans le
paramètre à la date de la colonne (valeur en vigueur à cette date) et doit rendre exactement la
cellule du relevé. Trois choix :

- DEUX LIGNES LISENT DEUX FEUILLES. La bière classée de 0,661 à 1 l est taxée par récipient
  jusqu'au 23 novembre 2015 (`bieres.par_recipient.recipient_0_661_a_1_l`), puis au centilitre
  (`bieres.par_centilitre`) ; le vin en bouteille de 0,751 à 1 l, par bouteille puis au litre
  (`vins.autres_vins_par_bouteille.bouteille_0_751_a_1_l`, `vins.autres_vins_par_litre`). L'unité
  change avec la feuille, et le tableau la porte dans chaque case.
- CINQ COLONNES, ET NON SIX. Les paramètres portent une date au 1er janvier 2016 (loi de
  finances pour 2016, art. 44), que le tableau n'affiche pas : elle ne change aucune valeur,
  puisque la loi reprend le tarif de l'annexe de 2015. Une sixième colonne répéterait la
  cinquième et ferait lire un changement là où il n'y en a pas. Le script VÉRIFIE l'énoncé : si
  une ligne diffère entre le 24 novembre 2015 et le 1er janvier 2016, la génération échoue.
- Les taux en pourcentage sont des fractions dans les paramètres (6,83 pour 683 %).
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
BRANCHE_ALCOOLS = "parameters/fiscalite_indirecte/accises/bieres_vins_alcools"

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
# TODO (terminologue) : « د/سنتلتر », « د/لتر » et « د للوحدة » (D/cl, D/l, D l'unité) ne viennent
# ni du glossaire ni de l'édition arabe du Journal officiel : à relire sur les annexes arabes des
# décrets de 1997, de 2013 et de 2015 (voir `docs/notes/plan-droits-consommation-alcools.md`).
UNITES_AR = {"D/hl": "د/هكتولتر", "D/100 kg": "د/100 كغ", "D/tonne": "د/طن",
             "D/m^3^": "د/م^3^", "D/cl": "د/سنتلتر", "D/l": "د/لتر",
             "D l'unité": "د للوحدة"}


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


# ------------------------------------------------- bières, vins et alcools (22-03 à 22-08)

def _tarif_litre(valeur: float) -> str:
    """1.8 -> « 1,8 » ; 2.4 -> « 2,4 » : le tarif au litre s'écrit à une décimale significative."""
    texte = f"{valeur:.4f}".rstrip("0")
    entier, _, decimales = texte.partition(".")
    return f"{entier},{decimales or '0'}"


def _pourcentage(valeur: float) -> str:
    """6.83 -> « 683 » : les paramètres portent la fraction, les textes le pourcentage."""
    return str(round(valeur * 100))


# Ligne du relevé -> feuilles lues, de la plus ancienne à la plus récente : (chemin sous la
# branche, unité telle que le relevé l'écrit, mise en forme du nombre). L'ordre est celui de
# la colonne « ordre » du relevé ; le produit vient du relevé, jamais du paramètre.
ALCOOLS = {
    0: [("bieres/par_recipient/recipient_0_661_a_1_l", "D l'unité", formate_tarif),
        ("bieres/par_centilitre", "D/cl", formate_tarif)],
    1: [("vins/vrac_livre_aux_embouteilleurs", "D/hl", formate_tarif)],
    2: [("vins/mousseux", "D l'unité", formate_tarif)],
    3: [("vins/liqueur_mistelles_mouts", "D l'unité", formate_tarif)],
    4: [("vins/autres_vins_par_bouteille/bouteille_0_751_a_1_l", "D l'unité", formate_tarif),
        ("vins/autres_vins_par_litre", "D/l", _tarif_litre)],
    5: [("vermouths", "%", _pourcentage)],
    6: [("autres_boissons_fermentees", "%", _pourcentage)],
    7: [("alcool_ethylique_boissons", "D/hl", formate_tarif)],
    8: [("spiritueux/eaux_de_vie", "%", _pourcentage)],
    9: [("spiritueux/spiritueux_non_classes", "%", _pourcentage)],
    10: [("spiritueux/spiritueux_classes", "%", _pourcentage)],
    11: [("spiritueux/pastis_anisette", "%", _pourcentage)],
}
# Seconde feuille d'une ligne : son libellé de lien précise la forme du tarif.
FORME_ALCOOLS = {
    "bieres/par_recipient/recipient_0_661_a_1_l": "tarif par récipient",
    "bieres/par_centilitre": "tarif au centilitre",
    "vins/autres_vins_par_bouteille/bouteille_0_751_a_1_l": "tarif par bouteille",
    "vins/autres_vins_par_litre": "tarif au litre",
}
FICHIER_ALCOOLS = "droit_consommation_alcools.md"
# Date de la loi de finances pour 2016 : elle reprend le tarif de l'annexe du 24 novembre 2015.
DATE_ANNEXE_2015, DATE_LF_2016 = "2015-11-24", "2016-01-01"


def _valeur_alcools(segments, date: str):
    """(valeur, texte de la case) à `date` le long des feuilles d'une ligne."""
    series = []
    for chemin, unite, mise_en_forme in segments:
        serie = [(d, v, t, h) for d, v, t, h in ot.serie_datee(f"{BRANCHE_ALCOOLS}/{chemin}.yaml")]
        if not serie:
            raise ValueError(f"paramètre introuvable ou vide : {chemin}")
        series.append((serie, (unite, mise_en_forme)))
    valeur, (unite, mise_en_forme) = ot.enchaine(series, date) or (None, None)
    if valeur is None:
        raise ValueError(f"aucune valeur en vigueur au {date}")
    return valeur, f"{mise_en_forme(valeur)} {unite}"


def tableau_alcools(langue: str):
    """Le tableau des alcools : cases lues dans les paramètres, relevé en garde-fou."""
    import pandas as pd
    import tarifs as releves

    spec = releves.TABLEAUX["alcools-tarifs"]
    with CSV_RELEVE.open(encoding="utf-8", newline="") as f:
        rangs = [r for r in csv.DictReader(f) if r["tableau"] == "alcools-tarifs"]
    colonnes = {}  # nom de colonne du relevé -> date d'effet, dans l'ordre du relevé
    for r in rangs:
        colonnes.setdefault(r["colonne"], r["date_effet"])
    lignes: dict[int, dict] = {}
    lus = 0
    for r in rangs:
        ordre = int(r["ordre"])
        segments = ALCOOLS[ordre]
        valeur, case = _valeur_alcools(segments, colonnes[r["colonne"]])
        publiee = releves.recompose(r["valeur"], r["unite"], r["statut"])
        if case != publiee:
            raise ValueError(f"alcools-tarifs / {r['produit']} / {r['colonne']} : le "
                             f"paramètre rend « {case} », le relevé « {publiee} »")
        ligne = lignes.setdefault(ordre, {"position": r["position"], "produit": r["produit"]})
        ligne[r["colonne"]] = case if langue == "fr" else _ar(case)
        lus += 1
    for ordre, segments in ALCOOLS.items():
        avant = _valeur_alcools(segments, DATE_ANNEXE_2015)[1]
        apres = _valeur_alcools(segments, DATE_LF_2016)[1]
        if avant != apres:
            raise ValueError(f"alcools-tarifs / ligne {ordre} : le tarif change entre le "
                             f"{DATE_ANNEXE_2015} (« {avant} ») et le {DATE_LF_2016} "
                             f"(« {apres} ») : le tableau doit porter une colonne 2016")
        for chemin, _unite, _forme in segments:
            produit = lignes[ordre]["produit"]
            forme = FORME_ALCOOLS.get(chemin)
            ot.releve_note(f"{BRANCHE_ALCOOLS}/{chemin}.yaml",
                           f"{produit} ({forme})" if forme else produit)
    if langue == "fr":
        entetes = spec["entetes"]
    else:
        entetes = [_ar(e) for e in spec["entetes"][:2]] + [
            f"ابتداءً من {ot.formate_date(d, 'ar')}" for d in list(colonnes.values())]
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
        try:
            (df, lus), liens = ot.avec_liens(lambda: tableau_alcools(langue))
        except ValueError as erreur:
            print(f"Les paramètres ne correspondent plus au relevé du précis : {erreur}",
                  file=sys.stderr)
            return 1
        sortie = RACINE / "precis" / langue / "fiscalite" / "tables" / FICHIER_ALCOOLS
        ot.ecrire_tableau(
            sortie, df, liens, langue, a_gauche=True,
            entete="<!-- Généré par scripts/generate_droit_consommation_tables.py — ne pas "
            "éditer à la main.\n"
            f"     Cases lues dans {BRANCHE_ALCOOLS} ; le relevé\n"
            "     precis/fr/fiscalite/tarifs/tarifs-releves-droits-consommation.csv sert de "
            "garde-fou. -->\n\n",
        )
        print(f"  {sortie.relative_to(RACINE)} : {len(df)} lignes, {lus} cases lues")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

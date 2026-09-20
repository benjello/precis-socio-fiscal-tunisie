"""Vérifie que les tarifs publiés par le précis concordent avec openfisca.

POURQUOI UN CONTRÔLE ET NON UN GÉNÉRATEUR. La règle du précis veut qu'un tableau de
paramètres vienne des dépôts openfisca. Elle ne s'applique pas telle quelle au relevé
de l'impôt sur les sociétés, pour une raison de fond : ce relevé porte des lignes que
le modèle ne peut pas porter.

  - La ligne « Nature du minimum » dit qu'un même montant a été un PLAFOND de 1990 à
    2005, puis un PLANCHER. Ce n'est pas une valeur, c'est ce qui rend les valeurs
    lisibles : sans elle, la suite 1 000 → 2 000 → 250 dinars se lit comme une baisse,
    alors que le mécanisme s'est inversé.
  - Les paramètres du minimum d'impôt COMMENCENT EN 2006 dans le modèle, à la date de ce
    retournement. Les valeurs antérieures sont délibérément absentes : un plafond et un
    plancher ne partagent pas un paramètre. Un générateur produirait donc un tableau
    amputé de ses deux premières colonnes.
  - Le relevé porte enfin des statuts — « ligne inexistante », « sans objet » — et des
    clés de citation, qui sont de la matière éditoriale et non des valeurs.

Un générateur perdrait tout cela. Ce contrôle garde au relevé sa liberté et lui enlève
son risque : aucune valeur publiée ne peut diverger du modèle sans qu'on le sache.

    uv run python scripts/check_tarifs_openfisca.py

Il exige openfisca-tunisia, via OPENFISCA_TUNISIA_PATH ou une installation.
"""

from __future__ import annotations

import csv
import datetime
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
RELEVE = RACINE / "precis/fr/fiscalite/tarifs/tarifs-releves-impot-societes.csv"

# Chaque ligne du relevé qui porte une valeur LUE doit se retrouver dans le modèle.
# La clé est (tableau, produit) ; la valeur, le chemin dans l'arbre des paramètres.
CORRESPONDANCES = {
    ("taux-chronologie", "Droit commun"): "taux.droit_commun",
    ("taux-chronologie", "Taux réduit"): "taux.reduit",
    ("taux-chronologie", "Petites et moyennes sociétés"): "taux.pme",
    ("taux-chronologie", "Secteurs majorés"): "taux.secteurs_35",
    ("taux-chronologie", "Banques et entreprises d'assurance"): "taux.banques_assurances",
    ("minimum-impot", "Taux — sociétés non soumises"): "minimum_impot.taux_normal",
    ("minimum-impot", "Taux — sociétés soumises"): "minimum_impot.taux_reduit",
    ("minimum-impot", "Montant — sociétés non soumises"): "minimum_impot.montant_minimum_normal",
    ("minimum-impot", "Montant — sociétés soumises"): "minimum_impot.montant_minimum_reduit",
}

# UNE LIGNE DU RELEVÉ PEUT CHANGER DE PARAMÈTRE EN COURS DE ROUTE, quand le modèle
# représente autrement ce que le tableau montre d'un trait. C'est le cas des banques et
# des assurances : elles paient 35 % de 2007 à 2023, mais au titre de la LISTE DES
# SECTEURS MAJORÉS, dont elles font partie. Le paramètre `banques_assurances` ne naît
# qu'en 2024, quand l'article 37 de la loi de finances pour 2025 les en détache pour les
# porter à 40 % — une scission, non une création. Le relevé montre la continuité du taux
# qu'elles supportent ; le modèle montre le texte qui le porte. Les deux ont raison, et
# c'est ce décalage que cette table déclare.
BASCULES = {
    ("taux-chronologie", "Banques et entreprises d'assurance"): [
        ("Depuis 2024", "taux.banques_assurances"),
        (None, "taux.secteurs_35"),   # toute colonne antérieure
    ],
}

# Lignes que le modèle NE PORTE PAS, et qui ne doivent pas le faire échouer. Chacune
# porte son motif : une absence non motivée doit rester une erreur.
HORS_MODELE = {
    ("minimum-impot", "Nature du minimum"):
        "une nature, non une valeur : ce qu'un paramètre ne peut pas porter",
    ("minimum-impot", "Taux — sociétés non soumises", "1990-1997"):
        "plafond, antérieur au retournement de 2006 ; le modèle commence au plancher",
    ("minimum-impot", "Taux — sociétés non soumises", "1998-2005"): "idem",
    ("minimum-impot", "Taux — sociétés soumises", "1990-1997"): "idem",
    ("minimum-impot", "Taux — sociétés soumises", "1998-2005"): "idem",
    ("minimum-impot", "Montant — sociétés non soumises", "1990-1997"): "idem",
    ("minimum-impot", "Montant — sociétés non soumises", "1998-2005"): "idem",
    ("minimum-impot", "Montant — sociétés soumises", "1990-1997"): "idem",
    ("minimum-impot", "Montant — sociétés soumises", "1998-2005"): "idem",
}


sys.path.insert(0, str(RACINE / "scripts"))
import openfisca_tables as oft  # noqa: E402

# On lit les paramètres par `openfisca_tables`, qui sait déjà trouver le paquet — installé
# ou désigné par OPENFISCA_TUNISIA_PATH — et qui contrôle sa version. Refaire cette
# résolution ici l'aurait dédoublée, et fait diverger les deux le jour d'un changement.


def nombre(brut: str, unite: str) -> float:
    """Le relevé écrit « 0,5 » et « 1 000 » ; le modèle, 0.005 et 1000."""
    v = float(brut.replace(" ", "").replace(" ", "").replace(" ", "").replace(",", "."))
    return v / 100 if unite == "%" else v


def cle(ligne):
    """Le produit du relevé est un libellé long ; on le rattache par son début.

    Une bascule déclarée l'emporte : elle dit quel paramètre porte la valeur pour la
    colonne considérée, quand ce n'est pas le même sur toute la ligne.
    """
    for (tab, prefixe), regles in BASCULES.items():
        if ligne["tableau"] != tab or not ligne["produit"].startswith(prefixe):
            continue
        for colonne, chemin in regles:
            if colonne is None or colonne == ligne["colonne"]:
                return (tab, prefixe), chemin
    for (tab, prefixe), chemin in CORRESPONDANCES.items():
        if ligne["tableau"] == tab and ligne["produit"].startswith(prefixe):
            return (tab, prefixe), chemin
    return None, None


def prefixe_hors_modele(ligne):
    for c, motif in HORS_MODELE.items():
        if c[0] != ligne["tableau"] or not ligne["produit"].startswith(c[1]):
            continue
        if len(c) == 2 or c[2] == ligne["colonne"]:
            return motif
    return None


def main() -> int:
    if not oft.openfisca_utilisable():
        print("openfisca-tunisia indisponible ou trop ancien. "
              "Définir OPENFISCA_TUNISIA_PATH.", file=sys.stderr)
        return 2
    ecarts, verifies, ignores, orphelines = [], 0, 0, []

    for ligne in csv.DictReader(RELEVE.open(encoding="utf-8")):
        if ligne["statut"] != "lu" or not ligne["valeur"]:
            continue
        motif = prefixe_hors_modele(ligne)
        if motif:
            ignores += 1
            continue
        _, chemin = cle(ligne)
        if chemin is None:
            orphelines.append(f'{ligne["tableau"]} / {ligne["produit"][:50]}')
            continue
        chemin_yaml = "parameters/impot_societes/" + chemin.replace(".", "/") + ".yaml"
        fichier = oft.charge_parametre(chemin_yaml)
        if fichier is None:
            ecarts.append(f"paramètre introuvable : {chemin_yaml}")
            continue
        # `valeur_a_la_date` lit un bloc de valeurs datées, non le fichier entier :
        # celui-ci porte aussi `description` et `metadata`, dont les clés ne sont pas
        # des dates et feraient échouer le tri.
        attendu = nombre(ligne["valeur"], ligne["unite"])
        obtenu = oft.valeur_a_la_date(
            fichier.get("values"), datetime.date.fromisoformat(ligne["date_effet"]))
        if obtenu is None or abs(float(obtenu) - attendu) > 1e-9:
            ecarts.append(
                f'{ligne["tableau"]} / {ligne["produit"][:44]} / {ligne["colonne"]} : '
                f"le relevé publie {ligne['valeur']} {ligne['unite']}, "
                f"openfisca rend {obtenu} au {ligne['date_effet']} ({chemin})")
        else:
            verifies += 1

    for o in sorted(set(orphelines)):
        ecarts.append(f"ligne sans correspondance déclarée : {o}")

    if ecarts:
        print(f"✗ {len(ecarts)} écart(s) entre le relevé publié et openfisca :")
        for e in ecarts:
            print(f"  - {e}")
        return 1

    print(f"✓ {verifies} valeur(s) du relevé concordent avec openfisca ; "
          f"{ignores} hors modèle, pour un motif déclaré.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

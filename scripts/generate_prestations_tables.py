"""Régénère les snapshots Markdown des tableaux de paramètres du livre « Prestations sociales ».

Même contrat que `generate_bareme_tables.py` : le build du site n'exécute PAS ce script, il
lit les fichiers qu'il produit, versionnés dans `precis/fr/prestations_sociales/tables/`.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_prestations_tables.py

Exige openfisca-tunisia >= 0.76 : c'est la version où les prestations familiales ont été
datées sur leurs textes (PR #392) et où les prestations d'assistance ont été corrigées et
sourcées (PR #393), et où la borne basse d'âge du supplément par enfant a été ajoutée.
Avant elles, toute la branche contributive était un cliché unique daté de 1960 dont aucune
valeur ne datait de 1960.

Ne sont PAS générés, faute de contrepartie dans le modèle : les tableaux de structure
juridique (conditions d'âge de l'enfant à charge, congés de maternité, multiplicateurs du
capital décès, tarifs de l'aide médicale, matrice régime × prestation) et les aides
ponctuelles de l'AMEN social, dont les cinq paramètres ne portent aucune référence et sont
datés de 2019 alors que l'arrêté qui les fixe est de 2020.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

AF = "parameters/prestations/contributives/prestations_familiales"
NC = "parameters/prestations/non_contributives"
SORTIE = Path(__file__).parent.parent / "precis" / "fr" / "prestations_sociales" / "tables"


def _dinars(v):
    """Montant en dinars et millimes, sur trois décimales.

    `ot.formate_dinars` élague les zéros de queue — bon pour un plafond fiscal en milliers
    de dinars, faux ici : les prestations s'écrivent en millimes, et « 18,75 D » pour
    18 dinars 750 millimes n'est pas la façon dont le JORT les imprime.
    """
    if v is None:
        return "—"
    if float(v).is_integer():
        return f"{int(v):,}".replace(",", " ") + " D"
    return f"{v:,.3f}".replace(",", " ").replace(".", ",") + " D"


def _taux(v):
    return "—" if v is None else ot.formate_taux(v)


def _entier(v):
    return "—" if v is None else str(int(v))


def _mois(v):
    return "—" if v is None else f"{int(v)} mois"


def _ans(v):
    if v is None:
        return "—"
    return "aucune" if int(v) == 0 else f"{int(v)} ans"


def _smig(v):
    if v is None:
        return "—"
    nombre = str(int(v)) if float(v).is_integer() else f"{v}".replace(".", ",")
    return f"{nombre} fois le salaire minimum garanti"


def _coefficient(v):
    return "—" if v is None else f"× {int(v)}"


# Clés de citation du précis, par date d'effet : elles raccrochent chaque rupture à la
# bibliographie du livre. À défaut, la colonne « Texte » reprend le titre porté par le
# paramètre lui-même.
CLES_AF = {
    "1960-01-01": "loi60-30, art. 52 et 61",
    "1976-01-01": "loi75-82, art. 1-2",
    "1986-05-01": "loi86-75, art. 1-2",
    "1989-01-01": "loi88-38, art. 1 et 5",
}
CLES_CRECHE = {
    f"{AF}/creche/montant.yaml": "decret95-114, art. 1",
    f"{AF}/creche/duree.yaml": "loi94-88, art. 4",
    f"{AF}/creche/age_min.yaml": "loi94-88, art. 4",
    f"{AF}/creche/age_max.yaml": "loi94-88, art. 4",
    f"{AF}/creche/plaf.yaml": "decret95-114, art. 1",
}
CLES_SALAIRE_UNIQUE = dict.fromkeys(
    (f"{AF}/salaire_unique/enf{i}.yaml" for i in (1, 2, 3)), "loi80-36, art. 1"
)
CLES_AMEN = {
    "2020-05-20": "arrete-2020-05-19-transferts, art. 2",
    "2022-01-01": "arrete-2022-04-01-transferts, art. 1",
    "2023-01-01": "arrete-2023-04-03-transferts, art. 1-2",
    "2024-01-01": "arrete-2024-02-28-transferts, art. 1-2",
    "2025-01-01": "arrete-2025-01-29-transferts, art. 1-2",
}


def af_evolution():
    """Taux par rang, assiette trimestrielle et nombre de rangs servis, de 1960 à nos jours."""
    df = ot.tableau_evolution_datee(
        [
            (f"{AF}/af/taux/enf1.yaml", "1^er^", _taux),
            (f"{AF}/af/taux/enf2.yaml", "2^e^", _taux),
            (f"{AF}/af/taux/enf3.yaml", "3^e^", _taux),
            (f"{AF}/af/taux/enf4.yaml", "4^e^", _taux),
            (f"{AF}/af/plancher_trim.yaml", "_plancher_", _dinars),
            (f"{AF}/af/plaf_trim.yaml", "_plafond_", _dinars),
            (f"{AF}/af/nb_enfants_max.yaml", "Rangs servis", _entier),
        ],
        cles=CLES_AF,
    )
    if df is None:
        return None
    # Plancher et plafond décrivent une seule chose — la bande d'assiette — et se lisent
    # ensemble : « 52 D – 500 D » à l'origine, un plafond simple après 1976.
    assiette = []
    for _, ligne in df.iterrows():
        bas, haut = ligne["_plancher_"], ligne["_plafond_"]
        assiette.append(haut if bas == "—" else f"{bas} – {haut}")
    df = df.drop(columns=["_plancher_", "_plafond_"])
    df.insert(len(df.columns) - 2, "Assiette trimestrielle", assiette)
    return df


TABLEAUX = {
    "af_evolution.md": af_evolution,
    "salaire_unique.md": lambda: ot.tableau_a_la_date(
        [
            (f"{AF}/salaire_unique/enf1.yaml", "Un enfant à charge", _dinars),
            (f"{AF}/salaire_unique/enf2.yaml", "Deux enfants à charge", _dinars),
            (f"{AF}/salaire_unique/enf3.yaml", "Trois enfants à charge ou plus", _dinars),
        ],
        "1980-05-01",
        cles=CLES_SALAIRE_UNIQUE,
    ),
    "creche.md": lambda: ot.tableau_a_la_date(
        [
            (f"{AF}/creche/montant.yaml", "Montant, par enfant et par mois", _dinars),
            (f"{AF}/creche/duree.yaml", "Durée de service, par an", _mois),
            (f"{AF}/creche/age_min.yaml", "Âge minimal de l'enfant", _mois),
            (f"{AF}/creche/age_max.yaml", "Âge maximal de l'enfant", _mois),
            (f"{AF}/creche/plaf.yaml", "Plafond de revenu de la mère", _smig),
        ],
        "1994-10-01",
        cles=CLES_CRECHE,
    ),
    "pnafn_allocation.md": lambda: ot.tableau_evolution_datee(
        [(f"{NC}/pnafn/allocation.yaml", "Allocation mensuelle", _dinars)],
        avec_attestation=True,
    ),
    "amen_base.md": lambda: ot.tableau_evolution_datee(
        [(f"{NC}/amen_social/allocation_base.yaml", "Allocation de base mensuelle", _dinars)],
        cles=CLES_AMEN,
    ),
    "amen_supplement_enfant.md": lambda: ot.tableau_evolution_datee(
        [
            (f"{NC}/amen_social/supplements/enfant_a_charge.yaml", "Supplément mensuel", _dinars),
            (f"{NC}/amen_social/supplements/handicap.yaml", "Carte de handicap", _coefficient),
            (f"{NC}/amen_social/supplements/age_min_enfant.yaml", "Âge minimal", _ans),
            (f"{NC}/amen_social/supplements/limite_age_enfant.yaml", "Âge maximal", _ans),
            (f"{NC}/amen_social/supplements/limite_age_etudiant.yaml",
             "Âge maximal en études, apprentissage ou formation", _ans),
        ],
        cles={
            "2020-05-20": "arrete-2020-05-19-transferts, art. 2",
            "2022-02-01": "arrete-2022-04-01-transferts, art. 1",
        },
    ),
    "amen_vs_afnc.md": lambda: ot.tableau_evolution_datee(
        [
            (f"{NC}/amen_social/allocation_base.yaml", "Base mensuelle du transfert AMEN", _dinars),
            (f"{NC}/allocation_familiale.yaml",
             "Allocation familiale non contributive, par enfant", _dinars),
        ],
        cles=CLES_AMEN,
    ),
}


def main() -> int:
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version {ot.version_openfisca()}, "
            f"minimum {ot.VERSION_MINIMALE}). Les snapshots existants sont conservés."
        )
        return 1
    SORTIE.mkdir(parents=True, exist_ok=True)
    for nom, fabrique in TABLEAUX.items():
        df = fabrique()
        if df is None or df.empty:
            print(f"✗ {nom} : paramètre introuvable ou vide.")
            return 1
        (SORTIE / nom).write_text(ot.tableau_vers_markdown(df), encoding="utf-8")
        print(f"✓ {nom} ({len(df)} ligne(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

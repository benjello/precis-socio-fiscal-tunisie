"""Régénère les snapshots Markdown des barèmes de l'IRPP.

Le build du site n'exécute PAS ce script : il lit les fichiers qu'il produit, versionnés
dans `precis/fr/fiscalite/tables/`. Le lancer suppose une copie d'openfisca-tunisia :

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_bareme_tables.py

Le barème de la contribution personnelle d'État (revenus 1986) n'est pas régénérable :
openfisca-tunisia ne modélise pas l'avant-1990. Son tableau est maintenu à la main.
"""

from __future__ import annotations

import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

BAREME = "parameters/impot_revenu/bareme.yaml"
SORTIE = Path(__file__).parent.parent / "precis" / "fr" / "fiscalite" / "tables"

# (nom de fichier, année de revenus, colonne du taux effectif, en-tête, source JORT)
TABLEAUX = [
    (
        "bareme_1990.md",
        1990,
        True,
        "Tranche de revenu annuel net (dinars)",
        "Article 44 § I du code de l'IRPP et de l'IS annexé à la loi n° 89-114 du "
        "30 décembre 1989, JORT n° 1 des 2-5 janvier 1990, p. 9. Inchangé jusqu'aux "
        "revenus de 2016 inclus.",
    ),
    (
        "bareme_2017.md",
        2017,
        False,
        "Tranche de revenu annuel net (dinars)",
        "Article 14 § 1 de la loi n° 2016-78 du 17 décembre 2016, JORT n° 105 du "
        "27 décembre 2016, p. 3831.",
    ),
    (
        "bareme_2025.md",
        2025,
        False,
        "Tranche de revenu annuel net (dinars)",
        "Article 36 § 1 de la loi n° 2024-48 du 9 décembre 2024, JORT n° 149 du "
        "10 décembre 2024, p. 6429.",
    ),
]

# Colonne des taux effectifs telle qu'imprimée au JORT de 1990 : garde-fou contre une
# dérive silencieuse entre les paramètres et le texte publié.
CONTROLE_1990 = ["0 %", "10,50 %", "15,25 %", "20,12 %", "26,05 %", "—"]


def main() -> int:
    if not ot.openfisca_utilisable():
        version = ot.version_openfisca()
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version {version}, "
            f"minimum {ot.VERSION_MINIMALE}). Définir OPENFISCA_TUNISIA_PATH.",
            file=sys.stderr,
        )
        return 1

    SORTIE.mkdir(parents=True, exist_ok=True)
    for fichier, annee, taux_effectif, entete, source in TABLEAUX:
        df = ot.tableau_bareme(
            BAREME,
            datetime.date(annee, 1, 1),
            colonne_tranche=entete,
            avec_taux_effectif=taux_effectif,
        )
        if df is None:
            print(f"échec : {fichier}", file=sys.stderr)
            return 1
        if annee == 1990:
            obtenu = list(df[df.columns[-1]])
            assert obtenu == CONTROLE_1990, (
                "Les taux effectifs calculés ne correspondent plus au barème publié au "
                f"JORT de 1990.\n  attendu : {CONTROLE_1990}\n  obtenu  : {obtenu}"
            )
        chemin = SORTIE / fichier
        chemin.write_text(
            f"<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
            f"     Source : {source} -->\n\n"
            + ot.tableau_vers_markdown(df)
            + "\n",
            encoding="utf-8",
        )
        print(f"écrit : {chemin.relative_to(SORTIE.parent.parent.parent.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

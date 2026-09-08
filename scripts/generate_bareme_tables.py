"""Régénère les snapshots Markdown des tableaux de paramètres du livre « Fiscalité ».

Le build du site n'exécute PAS ce script : il lit les fichiers qu'il produit, versionnés
dans `precis/fr/fiscalite/tables/`. Le lancer suppose une copie d'openfisca-tunisia :

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_bareme_tables.py

Deux familles de tableaux :
  - les BARÈMES à tranches (IRPP et contribution personnelle d'État) ;
  - les SÉRIES de paramètres scalaires (abattements, déductions, plafonds), dont la colonne
    « Texte » est tirée des métadonnées `reference` du paramètre lui-même. Le tableau publié
    et le paramètre sont ainsi indissociables : corriger l'un corrige l'autre.

Exige openfisca-tunisia >= 0.71 : c'est la version où les paramètres d'assiette ont été
corrigés et où les tarifs de la contribution personnelle d'État ont été ajoutés.
"""

from __future__ import annotations

import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

BAREME = "parameters/impot_revenu/bareme.yaml"
BAREME_CPE = "parameters/impot_revenu/contribution_personnelle_etat/bareme.yaml"
RACINE = Path(__file__).parent.parent / "precis"
LANGUES = ("fr", "ar")

# En-têtes de colonnes. Le reste du tableau — montants, taux, bornes de tranches, clés
# de citation — est identique dans les deux langues : ce sont des données, et les faire
# passer par un traducteur les exposerait à être réécrites.
MOTS = {
    "fr": {
        "tranche_net": "Tranche de revenu annuel net (dinars)",
        "tranche_imposable": "Tranche de revenu imposable (dinars)",
        "taux_tranche": "Taux de la tranche",
        "taux_effectif": "Taux d\u2019imposition du revenu global à la limite supérieure",
        "periode": "Années de revenus",
        "texte": "Texte",
        "taux": "Taux",
        "plafond_annuel": "Plafond annuel",
        "abattement": "Abattement",
        "deduction_sup": "Déduction supplémentaire",
        "deduction_forfait": "Déduction forfaitaire",
        "part_recettes": "Part des recettes brutes imposée",
        "minimum_impot": "Minimum d'impôt",
        "deduction": "Déduction",
        "enfant1": "1\u1d49\u02b3 enfant",
        "enfant4": "4\u1d49 enfant",
        "enfant_infirme": "Enfant infirme",
        "parent": "Parent à charge",
    },
    "ar": {
        "tranche_net": "شريحة الدخل السنوي الصافي (بالدينار)",
        "tranche_imposable": "شريحة الدخل الخاضع للضريبة (بالدينار)",
        "taux_tranche": "نسبة الشريحة",
        "taux_effectif": "نسبة الضريبة على الدخل الجملي عند الحدّ الأعلى",
        "periode": "سنوات المداخيل",
        "texte": "النصّ",
        "taux": "النسبة",
        "plafond_annuel": "السقف السنوي",
        "abattement": "الطرح",
        "deduction_sup": "الطرح الإضافي",
        "deduction_forfait": "الطرح الجزافي",
        "part_recettes": "الجزء الخاضع للضريبة من المقابيض الخام",
        "minimum_impot": "الضريبة الدنيا",
        "deduction": "الطرح",
        "enfant1": "الطفل الأوّل",
        "enfant4": "الطفل الرابع",
        "enfant_infirme": "الطفل المعوق",
        "parent": "الوالد المتكفَّل به",
    },
}

UNITES = {
    "fr": {"dinar": " D", "sans_plafond": "aucun plafond", "aucun": "aucun", "vide": "—"},
    "ar": {"dinar": " د", "sans_plafond": "دون سقف", "aucun": "لا شيء", "vide": "—"},
}

# (nom de fichier, année de revenus, colonne du taux effectif, en-tête, source JORT)
# Barèmes de la contribution personnelle d'État, supprimée pour les revenus 1990.
TABLEAUX_CPE = [
    ("bareme_cpe_1962.md", 1962),
    ("bareme_cpe_1965.md", 1965),
    ("bareme_cpe_1980.md", 1980),
    ("bareme_cpe_1983.md", 1983),
    ("bareme_cpe_1986.md", 1986),
]

# Séries de paramètres scalaires : (fichier, chemin, en-tête de la colonne, formateur).
def formateurs(langue):
    u = UNITES[langue]

    def dinars(v):
        return u["vide"] if v is None else ot.formate_dinars(v) + u["dinar"]

    def taux(v):
        return u["vide"] if v is None else ot.formate_taux(v)

    def plafond(v):
        if v is None or v == float("inf"):
            return u["sans_plafond"]
        return ot.formate_dinars(v) + u["dinar"]

    def plafond_ou_aucun(v):
        if v is None or v == float("inf"):
            return u["aucun"]
        return ot.formate_dinars(v) + u["dinar"]

    return dinars, taux, plafond, plafond_ou_aucun


# Tableaux d'évolution : (fichier, specs, clés de citation).
# Les clés raccrochent chaque rupture à la bibliographie du précis ; les valeurs et les
# dates, elles, viennent des paramètres. Les en-têtes sont symboliques : `MOTS` les rend
# dans la langue voulue.
def evolutions(langue):
    m = MOTS[langue]
    dinars, taux, _plafond, plafond_ou_aucun = formateurs(langue)
    ir = "parameters/impot_revenu"
    return [
        ("frais_professionnels.md",
         [(f"{ir}/tspr/abat_sal.yaml", m["taux"], taux),
          (f"{ir}/tspr/max_abat_sal.yaml", m["plafond_annuel"], plafond_ou_aucun)],
         {"1990-01-01": "code-irpp-is-1990, art. 26", "2017-01-01": "lf-2017, art. 14"}),
        ("abattement_pensions.md",
         [(f"{ir}/tspr/abat_pen.yaml", m["abattement"], taux)],
         {"1990-01-01": "code-irpp-is-1990, art. 26", "2027-01-01": "lf-2026, art. 56",
          "2028-01-01": "lf-2026, art. 56", "2029-01-01": "lf-2026, art. 56"}),
        ("abattement_salaire_minimum.md",
         [(f"{ir}/tspr/abattement_pour_salaire_minimum.yaml", m["deduction_sup"], dinars)],
         {"2004-01-01": "lf-2005, art. 49", "2009-01-01": "lf-2010, art. 39",
          "2014-01-01": "lf-2014, art. 73"}),
        ("foncier_bati.md",
         [(f"{ir}/foncier/bati/deduction_frais.yaml", m["deduction_forfait"], taux)],
         {"1990-01-01": "code-irpp-is-1990, art. 28", "2015-01-01": "lf-2016, art. 21",
          "2024-01-01": "lf-2025, art. 39"}),
        ("bnc_forfait.md",
         [(f"{ir}/bnc/forf/part_forf.yaml", m["part_recettes"], taux)],
         {"1990-01-01": "code-irpp-is-1990, art. 22", "2013-01-01": "lf-2014, art. 46"}),
        ("minimum_impot_avantages.md",
         [(f"{ir}/minimum_impot/taux.yaml", m["minimum_impot"], taux)],
         {"1999-01-01": "lf-1998, art. 62",
          "2017-04-01": "loi-avantages-fiscaux-2017, art. 2"}),
        ("famille_chef_de_famille.md",
         [(f"{ir}/deductions/famille/chef_de_famille.yaml", m["deduction"], dinars),
          (f"{ir}/deductions/famille/enf1.yaml", m["enfant1"], dinars),
          (f"{ir}/deductions/famille/enf4.yaml", m["enfant4"], dinars),
          (f"{ir}/deductions/famille/infirme.yaml", m["enfant_infirme"], dinars),
          (f"{ir}/deductions/famille/parent_max.yaml", m["parent"], dinars)],
         {"1990-01-01": "code-irpp-is-1990, art. 40", "2004-01-01": "lf-2005, art. 50",
          "2009-01-01": "lf-2010, art. 40", "2013-01-01": "lf-2014, art. 94",
          "2017-01-01": "lf-2018, art. 55", "2019-01-01": "lf-2018, art. 54"}),
    ]


TABLEAUX = [
    (
        "bareme_1990.md",
        1990,
        True,
        "tranche_net",
        "Article 44 § I du code de l'IRPP et de l'IS annexé à la loi n° 89-114 du "
        "30 décembre 1989, JORT n° 1 des 2-5 janvier 1990, p. 9. Inchangé jusqu'aux "
        "revenus de 2016 inclus.",
    ),
    (
        "bareme_2017.md",
        2017,
        False,
        "tranche_net",
        "Article 14 § 1 de la loi n° 2016-78 du 17 décembre 2016, JORT n° 105 du "
        "27 décembre 2016, p. 3831.",
    ),
    (
        "bareme_2025.md",
        2025,
        False,
        "tranche_net",
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

    for langue in LANGUES:
        m = MOTS[langue]
        sortie = RACINE / langue / "fiscalite" / "tables"
        sortie.mkdir(parents=True, exist_ok=True)

        for fichier, annee in TABLEAUX_CPE:
            df = ot.tableau_bareme(
                BAREME_CPE,
                datetime.date(annee, 1, 1),
                colonne_tranche=m["tranche_imposable"],
                avec_taux_effectif=True,
                langue=langue,
                colonne_taux=m["taux_tranche"],
                colonne_taux_effectif=m["taux_effectif"],
            )
            if df is None:
                print(f"échec : {langue}/{fichier}", file=sys.stderr)
                return 1
            (sortie / fichier).write_text(
                "<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
                f"     Tarif de la contribution personnelle d'État applicable aux revenus de {annee}.\n"
                "     Source : voir les métadonnées du paramètre\n"
                "     impot_revenu/contribution_personnelle_etat/bareme.yaml -->\n\n"
                + ot.tableau_vers_markdown(df) + "\n",
                encoding="utf-8",
            )

        for fichier, specs, cles in evolutions(langue):
            df = ot.tableau_evolution(
                specs, cles=cles, colonne_periode=m["periode"], colonne_texte=m["texte"]
            )
            if df is None:
                print(f"échec : {langue}/{fichier}", file=sys.stderr)
                return 1
            origines = ", ".join(c for c, _e, _f in specs)
            (sortie / fichier).write_text(
                "<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
                f"     Paramètres : {origines} -->\n\n"
                + ot.tableau_vers_markdown(df) + "\n",
                encoding="utf-8",
            )

        for fichier, annee, taux_effectif, entete, source in TABLEAUX:
            df = ot.tableau_bareme(
                BAREME,
                datetime.date(annee, 1, 1),
                colonne_tranche=m[entete],
                avec_taux_effectif=taux_effectif,
                langue=langue,
                colonne_taux=m["taux_tranche"],
                colonne_taux_effectif=m["taux_effectif"],
            )
            if df is None:
                print(f"échec : {langue}/{fichier}", file=sys.stderr)
                return 1
            if annee == 1990:
                obtenu = list(df[df.columns[-1]])
                assert obtenu == CONTROLE_1990, (
                    "Les taux effectifs calculés ne correspondent plus au barème publié au "
                    f"JORT de 1990.\n  attendu : {CONTROLE_1990}\n  obtenu  : {obtenu}"
                )
            (sortie / fichier).write_text(
                "<!-- Généré par scripts/generate_bareme_tables.py — ne pas éditer à la main.\n"
                f"     Source : {source} -->\n\n"
                + ot.tableau_vers_markdown(df) + "\n",
                encoding="utf-8",
            )

        total = len(TABLEAUX_CPE) + len(evolutions(langue)) + len(TABLEAUX)
        print(f"✓ {langue} : {total} tableaux")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

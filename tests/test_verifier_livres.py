"""Tests des fonctions pures de `scripts/verifier_livres.py` (voir `scripts/verifier.sh`)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from verifier_livres import (  # noqa: E402
    LIVRES,
    compter_arobases_cassees,
    compter_citations_non_resolues,
    figdata_a_restaurer,
    figdata_seule_date_a_change,
    livres_touches,
)

DIFF_DATE_SEULE = (
    "--- a/x\n+++ b/x\n@@ -1 +1 @@\n"
    "-# Figure-data du précis socio-fiscal tunisien — généré le 2026-09-09\n"
    "+# Figure-data du précis socio-fiscal tunisien — généré le 2026-09-24\n"
)
DIFF_SIDECAR_DATE_SEULE = "--- a/x\n+++ b/x\n@@ -5 +5 @@\n-generated: 2026-09-09\n+generated: 2026-09-24\n"
DIFF_CONTENU = "--- a/x\n+++ b/x\n@@ -2 +2 @@\n-1990,19.8\n+1990,99.9\n"


class LivresTouchesTest(unittest.TestCase):

    def test_fichier_d_un_seul_livre(self):
        self.assertEqual(
            livres_touches(["precis/fr/retraites/index.qmd"]), ["retraites"])

    def test_deux_livres_distincts(self):
        self.assertEqual(
            livres_touches([
                "precis/fr/retraites/index.qmd",
                "precis/ar/fiscalite/_regime.qmd",
            ]),
            ["fiscalite", "retraites"])

    def test_fichier_hors_precis_ignore(self):
        self.assertEqual(livres_touches(["scripts/recherches.py", "AGENTS.md"]), [])

    def test_figtools_touche_tous_les_livres(self):
        self.assertEqual(livres_touches(["scripts/figtools.py"]), sorted(LIVRES))

    def test_glossaire_source_touche_tous_les_livres(self):
        self.assertEqual(livres_touches(["precis/glossaire.yml"]), sorted(LIVRES))

    def test_seriescache_touche_tous_les_livres(self):
        self.assertEqual(
            livres_touches(["precis/_seriescache/bct-ipc-base2015.csv"]), sorted(LIVRES))

    def test_theme_partage_touche_tous_les_livres(self):
        self.assertEqual(livres_touches(["precis/legendes.scss"]), sorted(LIVRES))

    def test_modules_de_figures_touchent_tous_les_livres(self):
        for module in ("scripts/augmentations.py", "scripts/tarifs.py"):
            with self.subTest(module=module):
                self.assertEqual(livres_touches([module]), sorted(LIVRES))

    def test_fichier_de_langue_touche_tous_les_livres(self):
        """`precis/fr/references.json` est partagé, pas propre à un livre."""
        self.assertEqual(livres_touches(["precis/fr/references.json"]), sorted(LIVRES))

    def test_fichier_de_meme_nom_dans_un_livre_ne_touche_que_lui(self):
        """`precis/fr/retraites/references.json` reste propre au livre."""
        self.assertEqual(
            livres_touches(["precis/fr/retraites/references.json"]), ["retraites"])

    def test_livre_inconnu_ignore(self):
        self.assertEqual(livres_touches(["precis/fr/inconnu/index.qmd"]), [])

    def test_lignes_vides_ignorees(self):
        self.assertEqual(livres_touches(["", "  ", "precis/fr/retraites/index.qmd"]),
                          ["retraites"])


class CompterCitationsNonResoluesTest(unittest.TestCase):

    def test_citation_non_resolue_comptee(self):
        html = ('<span class="citation" data-cites="x">(<a href="#ref-x">'
                '<strong>x?</strong></a>)</span>')
        self.assertEqual(compter_citations_non_resolues(html), 1)

    def test_legende_des_prestations_non_comptee(self):
        """Le motif empirique exact de `precis/fr/prestations_sociales/index.qmd`."""
        html = "<p><strong>?</strong> la question n’est <strong>pas tranchée</strong>.</p>"
        self.assertEqual(compter_citations_non_resolues(html), 0)

    def test_page_saine_ne_compte_rien(self):
        html = "<p>Un texte <strong>important</strong> sans citation cassée.</p>"
        self.assertEqual(compter_citations_non_resolues(html), 0)

    def test_deux_citations_non_resolues(self):
        html = "<strong>abc?</strong> et <strong>def?</strong>"
        self.assertEqual(compter_citations_non_resolues(html), 2)


class CompterArobasesCasseesTest(unittest.TestCase):

    def test_reference_mal_formee_comptee(self):
        self.assertEqual(compter_arobases_cassees("Voir ?@loi-1960 pour le détail."), 1)

    def test_page_saine_ne_compte_rien(self):
        self.assertEqual(compter_arobases_cassees("<p>Rien à signaler ici.</p>"), 0)

    def test_plusieurs_occurrences(self):
        self.assertEqual(compter_arobases_cassees("?@a et ?@b et ?@c"), 3)


class FigdataSeuleDateAChangeTest(unittest.TestCase):

    def test_seule_la_date_du_csv_change(self):
        diff = (
            "--- a/figure.csv\n+++ b/figure.csv\n@@ -1 +1 @@\n"
            "-# Figure-data du précis socio-fiscal tunisien — généré le 2026-09-09\n"
            "+# Figure-data du précis socio-fiscal tunisien — généré le 2026-09-24\n"
        )
        self.assertTrue(figdata_seule_date_a_change(diff))

    def test_seule_la_date_du_sidecar_change(self):
        diff = "--- a/f.csv.yml\n+++ b/f.csv.yml\n@@ -5 +5 @@\n-generated: 2026-09-09\n+generated: 2026-09-24\n"
        self.assertTrue(figdata_seule_date_a_change(diff))

    def test_une_donnee_changee_n_est_pas_seule_la_date(self):
        diff = "--- a/f.csv\n+++ b/f.csv\n@@ -2 +2 @@\n-1990,19.8\n+1990,99.9\n"
        self.assertFalse(figdata_seule_date_a_change(diff))

    def test_date_et_donnee_changees_ensemble(self):
        diff = (
            "--- a/f.csv\n+++ b/f.csv\n@@ -1,2 +1,2 @@\n"
            "-# Figure-data du précis socio-fiscal tunisien — généré le 2026-09-09\n"
            "+# Figure-data du précis socio-fiscal tunisien — généré le 2026-09-24\n"
            "-1990,19.8\n+1990,99.9\n"
        )
        self.assertFalse(figdata_seule_date_a_change(diff))

    def test_diff_vide_est_sans_danger(self):
        self.assertTrue(figdata_seule_date_a_change(""))


class FigdataARestaurerTest(unittest.TestCase):
    """La décision se prend sur la PAIRE csv/.yml, jamais fichier par fichier."""

    def test_paire_date_seule_des_deux_cotes_restauree_ensemble(self):
        diffs = {
            "f.csv": DIFF_DATE_SEULE,
            "f.csv.yml": DIFF_SIDECAR_DATE_SEULE,
        }
        self.assertEqual(sorted(figdata_a_restaurer(diffs)), ["f.csv", "f.csv.yml"])

    def test_contenu_reel_dans_le_csv_bloque_aussi_le_sidecar(self):
        """Le cas qui a pris la première version en défaut.

        Une légende ajoutée redate le CSV (qui la porte, donc pas « date seule »)
        SANS toucher au sidecar autrement que sur sa propre date : restaurer le
        sidecar seul le ferait mentir sur une date qu'il ne partage plus avec le
        CSV qu'il décrit.
        """
        diffs = {
            "f.csv": DIFF_CONTENU,
            "f.csv.yml": DIFF_SIDECAR_DATE_SEULE,
        }
        self.assertEqual(figdata_a_restaurer(diffs), [])

    def test_csv_seul_modifie_sidecar_absent_du_diff(self):
        """Le sidecar n'a pas changé DU TOUT : il n'apparaît pas dans `diffs`."""
        diffs = {"f.csv": DIFF_DATE_SEULE}
        self.assertEqual(figdata_a_restaurer(diffs), ["f.csv"])

    def test_fichier_isole_avec_contenu_reel_non_restaure(self):
        diffs = {"f.csv": DIFF_CONTENU}
        self.assertEqual(figdata_a_restaurer(diffs), [])

    def test_deux_paires_independantes(self):
        diffs = {
            "a.csv": DIFF_DATE_SEULE,
            "a.csv.yml": DIFF_SIDECAR_DATE_SEULE,
            "b.csv": DIFF_CONTENU,
            "b.csv.yml": DIFF_SIDECAR_DATE_SEULE,
        }
        self.assertEqual(sorted(figdata_a_restaurer(diffs)), ["a.csv", "a.csv.yml"])

    def test_dictionnaire_vide(self):
        self.assertEqual(figdata_a_restaurer({}), [])


if __name__ == "__main__":
    unittest.main()

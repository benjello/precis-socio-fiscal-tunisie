"""Tests du garde qui décide ce qui part à la traduction automatique.

Une erreur ici ne produit pas un plantage : elle produit un fichier arabe écrasé par
une traduction qui ne pouvait pas savoir ce qu'elle effaçait. C'est arrivé aux
`_quarto.yml`, dont la partie arabe — `dir: rtl`, le bloc `language:` des libellés
d'interface, les titres de parties — n'a aucun original français. Le livre arabe rendait
alors 404 jusqu'au rattrapage manuel.

Le garde vit aussi dans le filtre du workflow. Ce n'est pas un doublon : le filtre évite
d'ouvrir une PR de traduction vide, cette fonction protège la re-synchro manuelle, où
les fichiers sont fournis à la main et n'ont jamais traversé le filtre.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from translate_sync import fichier_a_traduire  # noqa: E402


class QuartoYmlTest(unittest.TestCase):
    """LE cas de la règle : la configuration des livres ne se traduit pas."""

    def test_quarto_yml_francais_refuse(self):
        self.assertFalse(fichier_a_traduire("precis/fr/fiscalite/_quarto.yml"))

    def test_quarto_yml_arabe_refuse(self):
        self.assertFalse(fichier_a_traduire("precis/ar/fiscalite/_quarto.yml"))

    def test_quarto_yml_a_la_racine_refuse(self):
        self.assertFalse(fichier_a_traduire("_quarto.yml"))

    def test_refus_quel_que_soit_le_livre(self):
        for livre in ("fiscalite", "retraites", "prestations_sociales",
                      "remunerations_publiques", "cotisations_sociales"):
            with self.subTest(livre=livre):
                self.assertFalse(fichier_a_traduire(f"precis/fr/{livre}/_quarto.yml"))


class ChapitresTest(unittest.TestCase):
    """Ce qui doit continuer de passer : la prose, seule source de vérité française."""

    def test_chapitre_qmd(self):
        self.assertTrue(fichier_a_traduire("precis/fr/fiscalite/_tva.qmd"))

    def test_index_qmd(self):
        self.assertTrue(fichier_a_traduire("precis/fr/fiscalite/index.qmd"))

    def test_chapitre_a_tiret_bas(self):
        self.assertTrue(fichier_a_traduire("precis/fr/retraites/_secteur_public.qmd"))

    def test_changelog(self):
        self.assertTrue(fichier_a_traduire("CHANGELOG.md"))


class AutresFichiersTest(unittest.TestCase):
    def test_un_yml_quelconque_ne_passe_pas(self):
        self.assertFalse(fichier_a_traduire("precis/glossaire.yml"))

    def test_un_json_ne_passe_pas(self):
        self.assertFalse(fichier_a_traduire("precis/fr/fiscalite/references.json"))

    def test_un_script_ne_passe_pas(self):
        self.assertFalse(fichier_a_traduire("scripts/figtools.py"))

    def test_un_markdown_qui_n_est_pas_le_changelog_ne_passe_pas(self):
        """Seul CHANGELOG.md est admis parmi les Markdown : les notes de `docs/` sont
        des documents de travail, et le README n'est pas du précis."""
        self.assertFalse(fichier_a_traduire("docs/notes/fiscalite-tva-documentation.md"))
        self.assertFalse(fichier_a_traduire("README.md"))

    def test_chaine_vide(self):
        self.assertFalse(fichier_a_traduire(""))


class PiegesDeNomTest(unittest.TestCase):
    """Le test porte sur la FIN du nom : un nom qui contient le motif sans finir par lui
    ne doit pas être confondu."""

    def test_un_qmd_dont_le_nom_evoque_quarto(self):
        self.assertTrue(fichier_a_traduire("precis/fr/fiscalite/_quarto.yml.qmd"))

    def test_un_fichier_nomme_quarto_yml_bak(self):
        self.assertFalse(fichier_a_traduire("precis/fr/fiscalite/_quarto.yml.bak"))


if __name__ == "__main__":
    unittest.main()

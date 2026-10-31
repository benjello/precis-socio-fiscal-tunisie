"""Tests du contrôle du backlog : conflit oublié, date future, clé inexistante.

Le contrôle des dates doit refuser une date de lecture dans l'avenir proche (c'est la dérive
constatée le 31 octobre 2026 : « 1er novembre 2026 » écrit la veille) sans refuser une date
légale lointaine (« jusqu'au 31 décembre 2028 »). Celui des clés doit laisser passer les
correspondances « ancienne clé → nouvelle clé » et les noms de fichiers.
"""

import datetime
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from check_backlog import ecarts  # noqa: E402

AUJ = datetime.date(2026, 10, 31)
CLES = {"loi2007-42-rfr", "dl2021-21-lf2022"}


class Conflits(unittest.TestCase):
    def test_marqueurs_refuses(self):
        for marqueur in ("<<<<<<< HEAD", "=======", ">>>>>>> abc123 (message)"):
            self.assertEqual(len(ecarts([marqueur], None, AUJ)), 1, marqueur)

    def test_ligne_ordinaire_acceptee(self):
        self.assertEqual(ecarts(["| a | b |", "texte ======= au milieu"], None, AUJ), [])


class Dates(unittest.TestCase):
    def test_date_future_proche_refusee(self):
        for texte in (
            "lu le 1er novembre 2026",
            "lu le 1^er^ novembre 2026",
            "versé le 2 novembre 2026",
        ):
            self.assertEqual(len(ecarts([texte], None, AUJ)), 1, texte)

    def test_aujourdhui_et_passe_acceptes(self):
        self.assertEqual(ecarts(["lu le 31 octobre 2026", "du 3 mai 1998"], None, AUJ), [])

    def test_date_lointaine_ignoree(self):
        self.assertEqual(ecarts(["prolongation jusqu'au 31 décembre 2028"], None, AUJ), [])

    def test_exemption_explicite(self):
        ligne = "entrée en vigueur le 1er janvier 2027 <!-- futur-ok -->"
        self.assertEqual(ecarts([ligne], None, AUJ), [])

    def test_option_ignorer_dates(self):
        self.assertEqual(ecarts(["lu le 1er novembre 2026"], None, AUJ, dates=False), [])

    def test_date_impossible_sans_erreur(self):
        self.assertEqual(ecarts(["le 31 février 2026"], None, AUJ), [])


class Cles(unittest.TestCase):
    def test_cle_inconnue_refusee(self):
        self.assertEqual(len(ecarts(["voir `loi2099-1-inconnue`"], CLES, AUJ)), 1)
        self.assertEqual(len(ecarts(["voir [@decret1999-9-absent, art. 2]"], CLES, AUJ)), 1)

    def test_cle_connue_acceptee(self):
        self.assertEqual(ecarts(["voir `loi2007-42-rfr` et [@dl2021-21-lf2022]"], CLES, AUJ), [])

    def test_correspondance_de_renommage_ignoree(self):
        self.assertEqual(ecarts(["`loi86-83-lfr1986` → `loi-86-83-lfr-1986`"], CLES, AUJ), [])

    def test_fichier_ignore(self):
        self.assertEqual(ecarts(["le fichier `loireg2018.pdf`"], CLES, AUJ), [])

    def test_espace_reserve_de_cle_ignore(self):
        self.assertEqual(ecarts(["une citation `[@clé, art. 1 à 5]`"], CLES, AUJ), [])

    def test_controle_des_cles_sauté_sans_depot(self):
        self.assertEqual(ecarts(["voir `loi2099-1-inconnue`"], None, AUJ), [])


if __name__ == "__main__":
    unittest.main()

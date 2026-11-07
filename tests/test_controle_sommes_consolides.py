"""Tests de `scripts/controle_sommes_consolides.py` : sans PDF, sur des extraits de texte."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import controle_sommes_consolides as c  # noqa: E402

EQUILIBRE = """
TOTAL DES ACTIFS                                                     1 915 180      2 088 736
TOTAL DES CAPITAUX PROPRES CONSOLIDES                                 ‐1 745 820    ‐1 520 391
TOTAL DES CAPITAUX PROPRES ET PASSIFS                                 1 915 180      2 088 736
"""
ORDRE_INVERSE = """
TOTAL ACTIF                                                          9 847 795     8 801 419
TOTAL DES CAPITAUX PROPRES, PART DU GROUPE                             788 989       665 392
TOTAL PASSIF & CAPITAUX PROPRES                                      9 847 795     8 801 419
"""
DESEQUILIBRE = """
TOTAL ACTIF                                                          1 000 000       900 000
TOTAL CAPITAUX PROPRES ET PASSIFS                                      999 900       900 000
"""
COLONNES_COLLEES = """
TOTAL ACTIF                                                          7 734 656 6 702 354
TOTAL PASSIF & CAPITAUX PROPRES                                      7 734 657 6 702 354
"""


class EntierTest(unittest.TestCase):
    def test_signe_moins_unicode_et_parentheses(self):
        self.assertEqual(c.entier("‐1 745 820"), -1745820)  # tiret unicode U+2010
        self.assertEqual(c.entier("(26 002)"), -26002)
        self.assertEqual(c.entier("1 915 180"), 1915180)
        self.assertIsNone(c.entier("6.14"))  # code de note, pas un montant


class ControleTest(unittest.TestCase):
    def test_bilan_equilibre_et_fonds_propres_negatifs(self):
        r = c.controle(EQUILIBRE)
        self.assertIs(r["equilibre"], True)
        self.assertEqual(r["actif"], 1915180)
        self.assertEqual(r["capitaux_propres"], -1745820)  # relevé, et négatif

    def test_libelle_ordre_inverse(self):
        self.assertIs(c.controle(ORDRE_INVERSE)["equilibre"], True)

    def test_vrai_desequilibre_detecte(self):
        self.assertIs(c.controle(DESEQUILIBRE)["equilibre"], False)

    def test_colonnes_collees_non_exploite_pas_faux_desequilibre(self):
        # 7 734 656 et 6 702 354 collés -> nombre à 13 chiffres, invraisemblable -> non exploité (None)
        self.assertIsNone(c.controle(COLONNES_COLLEES)["equilibre"])


if __name__ == "__main__":
    unittest.main()

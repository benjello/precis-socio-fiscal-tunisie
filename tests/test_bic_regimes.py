"""Impôt des BIC selon le régime (`scripts/bic_regimes.py`) : table de cas explicite.

Les montants attendus sont ceux des textes cités, lus tranche par tranche :
  - annexe II du code de 1990 (colonne « autres opérations » : 1 000 D -> 0, 1 000,001 à
    2 000 -> 10, … 28 000,001 à 30 000 -> 700) ;
  - annexe II de la loi de finances pour 1993 (15 D jusqu'à 3 000 D, 45 D de 3 000,001 à 6 000…) ;
  - article 44 *ter* de 2011 (2 % avec plancher de 50 D) et de 2016 (75 D jusqu'à 10 000 D, puis
    ce montant plus 3 % de la fraction au-delà de 10 000 D, d'après la note commune n° 27/2016) ;
  - minimum d'impôt de l'article 44 § II : plafonné à 500 D (1990), plancher de 100 D (2006).
"""
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from bic_regimes import impot_forfait, impot_reel, minimum_impot, plafond  # noqa: E402

A1993 = [(0, 3000, 15, None, None), (3000, 6000, 45, None, None),
         (6000, 9000, 75, None, None), (27000, 30000, 700, None, None)]
TAUX_2011 = [(0, 100000, None, 0.02, 50)]
FIXE_3PC_2016 = [(0, 10000, 75, None, None), (10000, 100000, 75, 0.03, None)]
FIXE_3PC_2016_COMMUNALE = [(0, 10000, 150, None, None), (10000, 100000, 150, 0.03, None)]
IRPP_1990 = [(0, 0.0), (1500, 0.15), (5000, 0.20), (10000, 0.25), (20000, 0.30), (50000, 0.35)]


class ForfaitParTranche(unittest.TestCase):
    def test_bornes_de_tranche(self):
        self.assertEqual(impot_forfait(A1993, 3000), 15)      # la tranche inférieure à la borne
        self.assertEqual(impot_forfait(A1993, 3000.01), 45)   # la suivante dès 3 000,001
        self.assertEqual(impot_forfait(A1993, 6000), 45)
        self.assertEqual(impot_forfait(A1993, 30000), 700)

    def test_hors_champ(self):
        self.assertIsNone(impot_forfait(A1993, 30000.01))     # au-delà du plafond : pas de forfait
        self.assertIsNone(impot_forfait(A1993, 0))            # pas de chiffre d'affaires

    def test_plafond(self):
        self.assertEqual(plafond(A1993), 30000)


class ForfaitTauxEtPlancher(unittest.TestCase):
    def test_plancher_puis_taux(self):
        self.assertEqual(impot_forfait(TAUX_2011, 2000), 50)      # 2 % = 40 < 50
        self.assertEqual(impot_forfait(TAUX_2011, 2500), 50)      # 2 % = 50 : égalité
        self.assertAlmostEqual(impot_forfait(TAUX_2011, 3000), 60)
        self.assertAlmostEqual(impot_forfait(TAUX_2011, 100000), 2000)
        self.assertIsNone(impot_forfait(TAUX_2011, 100000.01))

    def test_montant_fixe_puis_trois_pour_cent_de_la_fraction(self):
        # Note commune n° 27/2016 : 3 % de la fraction du chiffre d'affaires au-dessus de 10 000 D,
        # en plus du montant fixe, non 3 % du chiffre d'affaires entier.
        self.assertEqual(impot_forfait(FIXE_3PC_2016, 10000), 75)
        self.assertAlmostEqual(impot_forfait(FIXE_3PC_2016, 10000.01), 75.0003)  # continu à 10 000
        self.assertAlmostEqual(impot_forfait(FIXE_3PC_2016, 100000), 75 + 2700)
        self.assertIsNone(impot_forfait(FIXE_3PC_2016, 100000.01))

    def test_exemples_de_la_note_commune_27_2016(self):
        # Exemple 1 (p. 11) : zone communale, 85 500 D -> 150 + 3 % × 75 500 = 2 415 D.
        self.assertAlmostEqual(impot_forfait(FIXE_3PC_2016_COMMUNALE, 85500), 2415)
        # Exemple 2 (p. 12) : hors zone communale, 50 000 + 20 000 = 70 000 D -> 75 + 3 % × 60 000.
        self.assertAlmostEqual(impot_forfait(FIXE_3PC_2016, 70000), 1875)


class MinimumEtReel(unittest.TestCase):
    def test_minimum_plafonne_1990(self):
        self.assertAlmostEqual(minimum_impot("plafonne", 0.005, 500, 40000), 200)
        self.assertEqual(minimum_impot("plafonne", 0.005, 500, 200000), 500)

    def test_minimum_plancher_2006(self):
        self.assertEqual(minimum_impot("plancher", 0.001, 100, 50000), 100)
        self.assertAlmostEqual(minimum_impot("plancher", 0.001, 100, 400000), 400)

    def test_forme_inconnue(self):
        with self.assertRaises(ValueError):
            minimum_impot("autre", 0.001, 100, 1000)

    def test_reel_barème_sur_le_benefice(self):
        # CA 40 000 D, bénéfice 25 % = 10 000 D : 0 + 3 500 × 15 % + 5 000 × 20 % = 1 525 D
        self.assertAlmostEqual(impot_reel(IRPP_1990, ("plafonne", 0.005, 500), 40000, 0.25), 1525)

    def test_reel_borne_par_le_minimum(self):
        # CA 40 000 D, bénéfice 2,5 % = 1 000 D < 1 500 D : barème nul, minimum 0,5 % = 200 D
        self.assertAlmostEqual(impot_reel(IRPP_1990, ("plafonne", 0.005, 500), 40000, 0.025), 200)
        # plancher de 100 D exigible sur un petit chiffre d'affaires
        self.assertEqual(impot_reel(IRPP_1990, ("plancher", 0.001, 100), 5000, 0.10), 100)

    def test_pas_de_nan(self):
        self.assertFalse(math.isnan(impot_reel(IRPP_1990, ("plancher", 0.001, 100), 1, 0.25)))


if __name__ == "__main__":
    unittest.main()

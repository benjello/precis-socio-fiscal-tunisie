"""Le coefficient « monnaie du dernier mois publié » : indice du mois / indice annuel de l'année."""
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "scripts"))

import dinars_constants  # noqa: E402


class TestCoefficientDernierMois(unittest.TestCase):
    def setUp(self):
        self._ancien = dinars_constants.dernier_indice_mensuel
        # (mois, indice du mois en base 2015, moyenne mensuelle de 2025 en base 2015)
        dinars_constants.dernier_indice_mensuel = lambda: ("2026-07", 196.2, 186.3)

    def tearDown(self):
        dinars_constants.dernier_indice_mensuel = self._ancien

    def test_2025_est_le_rapport_des_indices_de_base_2015(self):
        indice = {2022: 1697.4, 2025: 2092.7}
        self.assertAlmostEqual(dinars_constants.coefficient_dernier_mois(2025, indice),
                               196.2 / 186.3, places=9)

    def test_une_annee_anterieure_se_deduit_de_l_indice_annuel(self):
        indice = {2022: 1697.4, 2025: 2092.7}
        attendu = 2092.7 * (196.2 / 186.3) / 1697.4
        self.assertAlmostEqual(dinars_constants.coefficient_dernier_mois(2022, indice), attendu,
                               places=9)

    def test_le_coefficient_decroit_avec_l_annee(self):
        indice = {2020: 1482.6, 2021: 1567.2, 2025: 2092.7}
        cs = [dinars_constants.coefficient_dernier_mois(a, indice) for a in (2020, 2021, 2025)]
        self.assertEqual(cs, sorted(cs, reverse=True))


if __name__ == "__main__":
    unittest.main()

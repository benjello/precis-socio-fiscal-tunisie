"""Les séries des tarifs de l'électricité (basse et haute tension) et du gaz concordent, valeur par
valeur, avec les tableaux du chapitre « L'électricité et le gaz »."""
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "scripts"))

import serie_tarifs_bt  # noqa: E402
import serie_tarifs_gaz  # noqa: E402
import serie_tarifs_ht  # noqa: E402


class TestSeriesTarifs(unittest.TestCase):
    def test_basse_tension(self):
        self.assertEqual(serie_tarifs_bt.verifier(), [])
        self.assertGreater(len(serie_tarifs_bt.attendu()), 20)

    def test_haute_tension(self):
        self.assertEqual(serie_tarifs_ht.verifier(), [])
        self.assertGreater(len(serie_tarifs_ht.attendu()), 100)

    def test_gaz(self):
        self.assertEqual(serie_tarifs_gaz.verifier(), [])
        self.assertGreater(len(serie_tarifs_gaz.attendu()), 80)


if __name__ == "__main__":
    unittest.main()

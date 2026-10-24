"""La série des tarifs de la moyenne tension concorde, valeur par valeur, avec les trois tableaux."""
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "scripts"))

import serie_tarifs_mt  # noqa: E402


class TestSerieTarifsMt(unittest.TestCase):
    def test_csv_egal_aux_tableaux(self):
        self.assertEqual(serie_tarifs_mt.verifier(), [])

    def test_les_tableaux_sont_lus(self):
        self.assertGreater(len(serie_tarifs_mt.attendu()), 100)


if __name__ == "__main__":
    unittest.main()

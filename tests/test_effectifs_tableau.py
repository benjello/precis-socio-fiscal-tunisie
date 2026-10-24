"""La série de la figure 5.3 donne exactement les valeurs du tableau 5.22."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verifier_effectifs_tableau as v  # noqa: E402


class EffectifsTableauTest(unittest.TestCase):
    def test_csv_egal_au_tableau(self):
        self.assertEqual(v.controle(), [])


if __name__ == "__main__":
    unittest.main()

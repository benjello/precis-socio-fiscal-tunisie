"""La série des montants du programme rapportés par des études : valeurs contre citations."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verifier_pnafn_montants_etudes as v  # noqa: E402


class MontantsEtudesTest(unittest.TestCase):
    def test_controle_interne(self):
        self.assertEqual(v.controle_interne(), [])

    def test_controle_externe_quand_les_pdf_sont_la(self):
        raw = Path.home() / "projets/tunisia-data/data/raw"
        erreurs, verifiees = v.controle_externe(raw)
        self.assertEqual(erreurs, [])

    def test_une_valeur_par_ligne_et_quatre_familles(self):
        familles = {r["famille"] for r in v.lignes()}
        self.assertEqual(familles, v.FAMILLES)


if __name__ == "__main__":
    unittest.main()

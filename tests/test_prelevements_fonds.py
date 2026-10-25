"""La série des prélèvements sur le fonds de promotion du logement pour les salariés."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verifier_prelevements_fonds as v  # noqa: E402


class PrelevementsFondsTest(unittest.TestCase):
    def test_controle_interne(self):
        self.assertEqual(v.controle_interne(), [])

    def test_controle_externe_quand_le_corpus_est_la(self):
        erreurs, _lus = v.controle_externe(v.CORPUS)
        self.assertEqual(erreurs, [])

    def test_aucune_annee_non_lue_entre_1987_et_2026(self):
        annees = {int(r["annee"]) for r in v.lignes()}
        self.assertEqual(annees, set(range(1987, 2027)))

    def test_un_zero_a_sa_loi(self):
        for r in v.lignes():
            if r["statut"] == "aucun":
                self.assertTrue(r["texte"] and r["source"] and r["edition"])


if __name__ == "__main__":
    unittest.main()

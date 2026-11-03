"""Tests de `scripts/perimetres_groupes_bancaires.py` : sans PDF, sur des extraits de texte."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import perimetres_groupes_bancaires as p  # noqa: E402

BNA = """
   4- PÉRIMÈTRE DE CONSOLIDATION
               Banque Nationale Agricole                                                         Intégration globale       100,000%      99,833%
               TUNIS-RE                                                                          Mise en équivalence        21,51%        19,77%
               SIMPAR (1)                                                                        Intégration globale        40,51%        33,38%
      (1) La BNA détient 33,926% des droits de vote dans la société cotée en bourse SIMPAR.
"""
BH = """
Les entreprises retenues dans le périmètre de consolidation, le pourcentage d'intérêt ainsi que les méthodes
BH BANK                                                                    100,00           100,00                    Intégration Globale                               Tunisie
TFB                                                                         27,86            27,86                    Mise en équivalence                               France
• Méthodes de consolidation
"""
STB = """
SOCIETES CONSOLIDEES
   1. STB BANK (société Mère)                           100,00%   100,00%    0,00%
   2. STB INVEST                                         95,05%    94,60%    0,44%
SOCIETES CONSOLIDEES
   1. STB BANK (société Mère)                              99,98%     99,99%      0,00%
   2. STB INVEST                                           94,72%     94,73%      0,00%
"""


class PerimetresTest(unittest.TestCase):
    def test_bna_methode_controle_et_interet(self):
        lignes = p.bna(BNA)
        self.assertEqual(
            lignes[0][:6],
            ["BNA", "2021", "Banque Nationale Agricole", "mère", "100.000", "99.833"],
        )
        self.assertEqual(lignes[1][3], "mise en équivalence")
        self.assertEqual(lignes[2][2], "SIMPAR")  # le renvoi « (1) » n'est pas gardé

    def test_bh_ne_donne_que_l_interet(self):
        lignes = p.bh(BH)
        self.assertEqual(lignes[0][:6], ["BH", "2021", "BH BANK", "mère", "", "100.00"])
        self.assertEqual(lignes[1][4:7], ["", "27.86", "France"])

    def test_stb_rapproche_controle_et_interet_par_numero(self):
        lignes = [l for l in p.stb(STB) if l[1] == "2021"]
        self.assertEqual(
            lignes[0][:6], ["STB", "2021", "STB BANK", "mère", "100.00", "99.98"]
        )
        self.assertEqual(lignes[1][4:6], ["95.05", "94.72"])


if __name__ == "__main__":
    unittest.main()

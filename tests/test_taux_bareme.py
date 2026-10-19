"""Taux marginal, montant dû et taux moyen d'un barème à tranches (`scripts/taux_bareme.py`).

Table de cas explicite : chaque seuil, le dinar qui le suit, une assiette nulle (taux
moyen NON DÉFINI, jamais 0), un barème dont la première tranche commence au-dessus de 0,
un barème à taux unique. Deux ancres extérieures au calcul :
  - le barème de l'IRPP de 1990, dont le code imprime lui-même le taux d'imposition du
    revenu global à la limite supérieure de chaque tranche (art. 44 § I ; tronqué à deux
    décimales : 10,50 %, 15,25 %, 20,12 %, 26,05 %) ;
  - le tarif successoral de 1984 en ligne directe, calculé à la main.
"""

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from taux_bareme import (  # noqa: E402
    bareme_a_la_date,
    grille,
    montant_du,
    taux_marginal,
    taux_moyen,
    taux_unique,
)

try:
    import pandas as pd
except ImportError:  # le job de tests n'installe aucun paquet
    pd = None

# Code de l'IRPP de 1990, art. 44 § I.
IRPP_1990 = [(0, 0.0), (1500, 0.15), (5000, 0.20), (10000, 0.25), (20000, 0.30), (50000, 0.35)]
# Loi de finances pour 1984, art. 12 : ligne directe et époux.
SUCC_1984_LD = [(0, 0.06), (5000, 0.08), (10000, 0.10), (15000, 0.13), (45000, 0.18),
                (90000, 0.25)]
# Barème fictif dont la première tranche commence au-dessus de 0.
DECALE = [(1000, 0.10), (3000, 0.20)]

# (barème, assiette, taux marginal, montant dû, taux moyen — None : non défini)
CAS = [
    # IRPP 1990 : tranche à 0 %, seuils exacts (tranche inférieure) et dinar suivant.
    (IRPP_1990, 0, 0.0, 0.0, None),
    (IRPP_1990, 1000, 0.0, 0.0, 0.0),          # 0 vrai : assiette positive à 0 %
    (IRPP_1990, 1500, 0.0, 0.0, 0.0),
    (IRPP_1990, 1501, 0.15, 0.15, 0.15 / 1501),
    (IRPP_1990, 5000, 0.15, 525.0, 0.105),
    (IRPP_1990, 10000, 0.20, 1525.0, 0.1525),
    (IRPP_1990, 20000, 0.25, 4025.0, 0.20125),
    (IRPP_1990, 50000, 0.30, 13025.0, 0.2605),
    (IRPP_1990, 100000, 0.35, 30525.0, 0.30525),
    # Successions 1984, ligne directe.
    (SUCC_1984_LD, 0, 0.06, 0.0, None),
    (SUCC_1984_LD, 5000, 0.06, 300.0, 0.06),
    (SUCC_1984_LD, 10000, 0.08, 700.0, 0.07),
    (SUCC_1984_LD, 15000, 0.10, 1200.0, 0.08),
    (SUCC_1984_LD, 45000, 0.13, 5100.0, 5100 / 45000),
    (SUCC_1984_LD, 90000, 0.18, 13200.0, 13200 / 90000),
    (SUCC_1984_LD, 100000, 0.25, 15700.0, 0.157),
    # Première tranche au-dessus de 0 : rien n'est dû en deçà.
    (DECALE, 0, 0.0, 0.0, None),
    (DECALE, 500, 0.0, 0.0, 0.0),
    (DECALE, 1000, 0.0, 0.0, 0.0),
    (DECALE, 2000, 0.10, 100.0, 0.05),
    (DECALE, 3000, 0.10, 200.0, 200 / 3000),
    (DECALE, 4000, 0.20, 400.0, 0.10),
    # Taux unique : moyen = marginal partout, sauf en 0 où le moyen n'est pas défini.
    ([(0, 0.025)], 0, 0.025, 0.0, None),
    ([(0, 0.025)], 80000, 0.025, 2000.0, 0.025),
]


class TableDeCasTest(unittest.TestCase):
    def test_table_de_cas(self):
        for bareme, assiette, marginal, du, moyen in CAS:
            with self.subTest(bareme=bareme, assiette=assiette):
                self.assertAlmostEqual(taux_marginal(bareme, assiette), marginal, places=12)
                self.assertAlmostEqual(montant_du(bareme, assiette), du, places=9)
                if moyen is None:
                    self.assertIsNone(taux_moyen(bareme, assiette))
                else:
                    self.assertAlmostEqual(taux_moyen(bareme, assiette), moyen, places=12)

    def test_irpp_1990_taux_imprimes_au_code(self):
        """Le taux moyen aux limites supérieures, tronqué, est celui que le code imprime."""
        imprimes = {5000: 10.50, 10000: 15.25, 20000: 20.12, 50000: 26.05}
        for limite, attendu in imprimes.items():
            with self.subTest(limite=limite):
                tronque = math.floor(100 * 100 * taux_moyen(IRPP_1990, limite) + 1e-9) / 100
                self.assertEqual(tronque, attendu)

    def test_le_moyen_reste_sous_le_marginal(self):
        for x in grille(SUCC_1984_LD, 120000):
            self.assertLessEqual(taux_moyen(SUCC_1984_LD, x),
                                 taux_marginal(SUCC_1984_LD, x) + 1e-12)


class FormeTest(unittest.TestCase):
    def test_taux_unique(self):
        self.assertTrue(taux_unique([(0, 0.05)]))
        self.assertFalse(taux_unique(SUCC_1984_LD))
        self.assertFalse(taux_unique([(1000, 0.05)]))  # rien n'est dû avant 1 000

    def test_bareme_mal_forme(self):
        for bareme in ([], [(5000, 0.1), (0, 0.05)], [(0, 0.1), (0, 0.2)]):
            with self.subTest(bareme=bareme), self.assertRaises(ValueError):
                montant_du(bareme, 100)

    def test_assiette_negative(self):
        with self.assertRaises(ValueError):
            taux_marginal(IRPP_1990, -1)

    def test_grille_sans_zero_avec_seuils(self):
        g = grille(SUCC_1984_LD, 120000, n=7)
        self.assertNotIn(0, g)
        self.assertLessEqual({5000, 10000, 15000, 45000, 90000}, set(g))
        self.assertEqual(g, sorted(g))
        self.assertEqual(g[-1], 120000)


@unittest.skipIf(pd is None, "pandas absent")
class BaremeALaDateTest(unittest.TestCase):
    def test_ecarte_les_tranches_closes(self):
        nan = float("nan")
        d = pd.DataFrame([
            {"parente": "ld", "tranche": 1, "date_effet": "1984-01-01", "seuil": 0.0, "taux": 0.06},
            {"parente": "ld", "tranche": 2, "date_effet": "1984-01-01", "seuil": 5000.0,
             "taux": 0.08},
            {"parente": "ld", "tranche": 1, "date_effet": "1993-05-17", "seuil": 0.0, "taux": 0.05},
            {"parente": "ld", "tranche": 2, "date_effet": "1993-05-17", "seuil": nan, "taux": nan},
            {"parente": "fs", "tranche": 1, "date_effet": "1984-01-01", "seuil": 0.0, "taux": 0.2},
        ])
        self.assertEqual(bareme_a_la_date(d, "parente", "ld", "1983-12-31"), [])
        self.assertEqual(bareme_a_la_date(d, "parente", "ld", "1984-01-01"),
                         [(0.0, 0.06), (5000.0, 0.08)])
        self.assertEqual(bareme_a_la_date(d, "parente", "ld", "1993-05-17"), [(0.0, 0.05)])
        self.assertEqual(bareme_a_la_date(d, "parente", "fs", "2000-01-01"), [(0.0, 0.2)])


if __name__ == "__main__":
    unittest.main()

"""Pont de la facture des combustibles de la STEG en points de PIB (figure `gaz_pib`).

Les effets (prix, quantité, PIB) d'une décomposition logarithmique somment exactement à la variation
du ratio facture / PIB ; les ponts de la figure se retrouvent sur les séries snapshotées.

Le module de figure demande pandas et matplotlib, que le job `tests.yml` n'installe pas
(`unittest` sans dépendance) : hors de cet environnement le fichier est sauté, comme en CI ;
`scripts/verifier.sh` (pytest, environnement du projet) l'exécute.
"""
import importlib.util
import math
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
try:
    import matplotlib  # noqa: F401
    import pandas as pd
except ImportError:
    raise unittest.SkipTest("pandas et matplotlib requis : exécuté par scripts/verifier.sh")

SPEC = importlib.util.spec_from_file_location(
    "electricite_compensation", RACINE / "precis/fr/compensation/figures/electricite.py")
el = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(el)


def _synthetique():
    """Trois années inventées, sans lien avec les séries : la décomposition ne dépend que des
    trois grandeurs facture, prix et PIB."""
    d = pd.DataFrame({"facture": [100.0, 150.0, 90.0], "prix": [10.0, 30.0, 12.0],
                      "pib": [1000.0, 1100.0, 1500.0]}, index=[2001, 2002, 2003])
    d["quantite"] = d["facture"] / d["prix"] * 1000
    d["ratio"] = 100 * d["facture"] / d["pib"]
    return d


class PontPibElectricite(unittest.TestCase):
    def test_les_effets_annuels_somment_a_la_variation_du_ratio(self):
        d = _synthetique()
        e = el.effets_annuels(d)
        for a in (2002, 2003):
            self.assertLess(abs(e.loc[a].sum() - (d.at[a, "ratio"] - d.at[a - 1, "ratio"])), 1e-9)

    def test_pont_depart_plus_effets_egale_arrivee(self):
        c = el.pont(_synthetique(), 2001, 2003)
        self.assertLess(abs(c["depart"] + c["prix"] + c["quantite"] + c["pib"] - c["arrivee"]), 1e-9)

    def test_effet_nul_quand_la_grandeur_ne_bouge_pas(self):
        d = _synthetique()
        d["prix"] = 10.0
        d["quantite"] = d["facture"] / d["prix"] * 1000
        self.assertLess(abs(el.effets_annuels(d)["prix"]).max(), 1e-12)

    def test_moyenne_logarithmique(self):
        self.assertEqual(el._moyenne_log(3.0, 3.0), 3.0)
        self.assertAlmostEqual(el._moyenne_log(4.0, 1.0), 3 / math.log(4), places=12)

    def test_ponts_sur_les_series_de_la_figure(self):
        d = el.donnees_pont()
        self.assertEqual(list(d.index), list(range(2013, 2024)))
        attendus = {(2013, 2016): (5.60, -2.54, -0.04, -0.81, 2.20),
                    (2016, 2022): (2.20, 4.92, 0.00, -1.34, 5.78),
                    (2022, 2023): (5.78, -0.18, -0.17, -0.39, 5.05),
                    (2013, 2023): (5.60, 2.20, -0.21, -2.54, 5.05)}
        for (a, b), valeurs in attendus.items():
            c = el.pont(d, a, b)
            self.assertLess(abs(c["depart"] + c["prix"] + c["quantite"] + c["pib"] - c["arrivee"]), 1e-9)
            for cle, v in zip(("depart", "prix", "quantite", "pib", "arrivee"), valeurs):
                self.assertAlmostEqual(c[cle], v, delta=0.005, msg=f"{a}-{b} {cle}")

    def test_la_quantite_deduite_est_le_total_des_achats_de_gaz(self):
        d = el.donnees_pont()
        for a, total in {2019: 5804, 2020: 5478, 2021: 5765, 2022: 5480, 2023: 5315}.items():
            self.assertLess(abs(d.at[a, "quantite"] - total), 2)


if __name__ == "__main__":
    unittest.main()

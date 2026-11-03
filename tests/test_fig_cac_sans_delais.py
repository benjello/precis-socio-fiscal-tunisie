"""Tests de `figures/cotees.py::fig_cac` : la courbe des délais n'est tracée que si la société en a.

Une entreprise sans page de la Bourse de Tunis (office, régie) n'a pas de date de publication des
états financiers : la figure garde la carte des thèmes et les barres, sans la courbe vide.
Le test ne lit aucun fichier : il remplace `_lire` par de petits relevés.
"""

import sys
import unittest
from pathlib import Path

try:
    import matplotlib
    import pandas as pd

    matplotlib.use("Agg")
    sys.path.insert(
        0,
        str(
            Path(__file__).resolve().parent.parent
            / "precis/fr/entreprises_publiques/figures"
        ),
    )
    import cotees as ct
except ImportError:  # job de tests sans pandas ni matplotlib
    ct = None


def _opinions():
    return pd.DataFrame(
        {
            "groupe": ["X", "X", "X"],
            "exercice": ["2019", "2020", "2021"],
            "opinion": ["sans réserve", "avec réserves", "sans réserve"],
            "rang": ["1", "1", "1"],
            "themes": ["", "suspens", ""],
        }
    )


def _delais():
    return pd.DataFrame(
        {
            "societe": ["x", "x", "autre"],
            "exercice": ["2019", "2020", "2020"],
            "nature": ["individuel", "individuel", "individuel"],
            "jours": ["120", "150", "99"],
        }
    )


@unittest.skipIf(ct is None, "pandas ou matplotlib absent")
class FigCacSansDelais(unittest.TestCase):
    def setUp(self):
        self._lire = ct._lire
        ct._lire = lambda nom: {
            "opinions-cac": _opinions(),
            "delais-publication": _delais(),
        }[nom]

    def tearDown(self):
        ct._lire = self._lire
        ct.plt.close("all")

    def test_societe_avec_delais_trois_vues(self):
        fig = ct.fig_cac("X", "x")
        self.assertEqual(len(fig.axes), 3)

    def test_societe_sans_delais_deux_vues(self):
        fig = ct.fig_cac("X", "societe_sans_page")
        self.assertEqual(len(fig.axes), 2)
        self.assertEqual(
            [t.get_text() for t in fig.axes[1].get_xticklabels()],
            ["2018", "2019", "2020", "2021"],
        )


if __name__ == "__main__":
    unittest.main()

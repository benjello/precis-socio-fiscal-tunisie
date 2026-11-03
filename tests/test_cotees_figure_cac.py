"""Test de `figure_cac` (figures/cotees.py) : sans ligne dans delais-publication.csv, pas de courbe des délais."""

import sys
import unittest
from pathlib import Path

from unittest import mock

import pandas as pd

sys.path.insert(
    0, str(Path(__file__).resolve().parent.parent / "precis/fr/entreprises_publiques")
)

from figures import cotees as ct  # noqa: E402

OPINIONS = pd.DataFrame(
    [
        ["X", "2019", "sans réserve", "1", "aucune réserve", "3", "src", ""],
        ["X", "2020", "avec réserves", "1", "motif", "4", "src", "garanties"],
    ],
    columns=[
        "groupe",
        "exercice",
        "opinion",
        "rang",
        "motif",
        "page_pdf",
        "source",
        "themes",
    ],
)
DELAIS = pd.DataFrame(
    [["autre", "2019", "individuel", "01/01/2020", "90", "/node/1"]],
    columns=["societe", "exercice", "nature", "date_publication", "jours", "page"],
)


class FigureCacTest(unittest.TestCase):
    def _tracer(self, societe):
        with mock.patch.object(
            ct, "_lire", lambda nom: OPINIONS if nom == "opinions-cac" else DELAIS
        ):
            fig = ct.fig_cac("X", societe)
        n = len(fig.axes)
        ct.plt.close("all")
        return n

    def test_sans_page_a_la_bourse_deux_panneaux(self):
        self.assertEqual(self._tracer("sans-page"), 2)

    def test_avec_page_a_la_bourse_trois_panneaux(self):
        self.assertEqual(self._tracer("autre"), 3)

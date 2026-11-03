"""Test de `figure_cac` : une société sans page de la Bourse n'a pas de courbe des délais de publication."""

import sys
import unittest
from pathlib import Path
from unittest import mock

import pandas as pd

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "precis/fr/entreprises_publiques"))

from figures import cotees  # noqa: E402

OPINIONS = pd.DataFrame(
    [
        ["ZZ", "2013", "avec réserves", "1", "motif", "5", "k-2013", "immobilisations"],
        ["ZZ", "2014", "sans réserve", "1", "", "5", "k-2014", ""],
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
    [["zz", "2013", "individuel", "30/06/2014", "181", "/node/1"]],
    columns=["societe", "exercice", "nature", "date_publication", "jours", "page"],
)


def lire(nom, delais=DELAIS):
    return {"opinions-cac": OPINIONS, "delais-publication": delais}[nom]


class FigureCacTest(unittest.TestCase):
    def test_sans_delais_deux_vues(self):
        with mock.patch.object(cotees, "_lire", lambda nom: lire(nom)):
            fig = cotees.fig_cac("ZZ", "autre")
        self.assertEqual(len(fig.axes), 2)
        cotees.plt.close("all")

    def test_avec_delais_trois_vues(self):
        with mock.patch.object(cotees, "_lire", lambda nom: lire(nom)):
            fig = cotees.fig_cac("ZZ", "zz")
        self.assertEqual(len(fig.axes), 3)
        cotees.plt.close("all")


if __name__ == "__main__":
    unittest.main()

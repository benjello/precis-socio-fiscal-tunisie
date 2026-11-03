"""Test de `figures/cotees.fig_cac` pour une entreprise sans page de la Bourse : pas de courbe des délais."""

import sys
import unittest
from pathlib import Path
from unittest import mock

import pandas as pd

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "precis/fr/entreprises_publiques"))
sys.path.insert(0, str(RACINE / "scripts"))

from figures import cotees as ct  # noqa: E402

OPINIONS = pd.DataFrame(
    [
        [
            "ETAP",
            "2013",
            "avec réserves",
            "1",
            "motif",
            "5",
            "es-etap-2013",
            "etap_cost_oil",
        ],
        ["ETAP", "2014", "sans réserve", "1", "", "7", "es-etap-2014", ""],
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
    [["stb", "2013", "individuel", "120"], ["stb", "2014", "individuel", "90"]],
    columns=["societe", "exercice", "nature", "jours"],
)


def lire(nom):
    return {"opinions-cac": OPINIONS, "delais-publication": DELAIS}[nom]


class FigureCacSansDelais(unittest.TestCase):
    def test_sans_ligne_de_delais_deux_vues(self):
        with mock.patch.object(ct, "_lire", lire):
            fig = ct.fig_cac("ETAP", "")
        self.assertEqual(len(fig.axes), 2)
        ct.plt.close("all")

    def test_avec_delais_trois_vues(self):
        opinions = OPINIONS.assign(groupe="STB")
        with mock.patch.object(
            ct, "_lire", lambda n: opinions if n == "opinions-cac" else DELAIS
        ):
            fig = ct.fig_cac("STB", "stb")
        self.assertEqual(len(fig.axes), 3)
        ct.plt.close("all")


if __name__ == "__main__":
    unittest.main()

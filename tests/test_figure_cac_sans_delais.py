"""Test de `figures/cotees.py` : `fig_cac` trace sans la courbe des délais quand la société n'a pas de page de la Bourse."""

import sys
import unittest
from pathlib import Path
from unittest import mock

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

racine = (
    Path(__file__).resolve().parent.parent / "precis" / "fr" / "entreprises_publiques"
)
sys.path.insert(0, str(racine))
sys.path.insert(0, str(racine.parent.parent.parent / "scripts"))

from figures import cotees  # noqa: E402

OPINIONS = pd.DataFrame(
    {
        "groupe": ["XYZ", "XYZ"],
        "exercice": ["2019", "2020"],
        "opinion": ["sans réserve", "avec réserves"],
        "rang": ["1", "1"],
        "motif": ["", "immobilisations"],
        "page_pdf": ["3", "3"],
        "source": ["", ""],
        "themes": ["", "immobilisations"],
    }
)
DELAIS = pd.DataFrame(
    {
        "societe": ["AUTRE"],
        "nature": ["individuel"],
        "exercice": ["2019"],
        "jours": ["100"],
    }
)


def lire(nom):
    return {"opinions-cac": OPINIONS, "delais-publication": DELAIS}[nom]


class FigureCacSansDelais(unittest.TestCase):
    def test_deux_panneaux_sans_delai(self):
        with mock.patch.object(cotees, "_lire", lire):
            fig = cotees.fig_cac("XYZ", "XYZ")
        self.assertEqual(len(fig.axes), 2)
        plt.close("all")

    def test_trois_panneaux_avec_delai(self):
        delais = DELAIS.assign(societe="XYZ")
        with mock.patch.object(
            cotees,
            "_lire",
            lambda n: {"opinions-cac": OPINIONS, "delais-publication": delais}[n],
        ):
            fig = cotees.fig_cac("XYZ", "XYZ")
        self.assertEqual(len(fig.axes), 3)
        plt.close("all")


def tearDownModule():
    # figtools ferme les figures seulement si pyplot est déjà importé : on laisse les autres tests comme on les a trouvés
    sys.modules.pop("matplotlib.pyplot", None)


if __name__ == "__main__":
    unittest.main()

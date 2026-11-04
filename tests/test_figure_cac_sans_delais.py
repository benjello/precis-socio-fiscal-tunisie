"""fig_cac trace sans la courbe des délais quand la société n'a pas de ligne dans delais-publication.csv."""

import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "scripts"))
sys.path.insert(0, str(RACINE / "precis/fr/entreprises_publiques/figures"))

try:
    import matplotlib  # noqa: E402
    import pandas  # noqa: E402,F401
except (
    ImportError
) as exc:  # l'intégration continue lance les tests sans matplotlib ni pandas
    raise unittest.SkipTest(f"dépendance absente : {exc.name}") from exc

import cotees  # noqa: E402

matplotlib.use("Agg")


class FigureCacSansDelais(unittest.TestCase):
    def test_societe_sans_delai_a_deux_panneaux(self):
        fig = cotees.fig_cac("TUNISAIR", "societe-sans-page-de-la-bourse")
        self.assertEqual(len(fig.axes), 2)

    def test_societe_avec_delais_garde_trois_panneaux(self):
        fig = cotees.fig_cac("TUNISAIR", "tunisair")
        self.assertEqual(len(fig.axes), 3)


if __name__ == "__main__":
    unittest.main()

"""Tests de `figures/cotees.py::fig_cac` : la courbe des délais n'est tracée que si la société en a.

Une entreprise sans page de la Bourse de Tunis (office, régie) n'a pas de date de publication des
états financiers : la figure garde la carte des thèmes et les barres, sans la courbe vide.

Le test tourne dans un sous-processus : importer matplotlib dans le processus des tests changerait
le comportement de `figtools._image_vue`, que `test_figtools` éprouve avec une fausse figure
(`matplotlib` « jamais importé »). Il ne lit aucun fichier : `_lire` est remplacé par de petits relevés.
"""

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
FIGURES = RACINE / "precis/fr/entreprises_publiques/figures"

PROGRAMME = """
import sys
sys.path.insert(0, {figures!r})
import matplotlib
matplotlib.use("Agg")
import pandas as pd
import cotees as ct

opinions = pd.DataFrame({{
    "groupe": ["X", "X", "X"],
    "exercice": ["2019", "2020", "2021"],
    "opinion": ["sans réserve", "avec réserves", "sans réserve"],
    "rang": ["1", "1", "1"],
    "themes": ["", "suspens", ""],
}})
delais = pd.DataFrame({{
    "societe": ["x", "x", "autre"],
    "exercice": ["2019", "2020", "2020"],
    "nature": ["individuel", "individuel", "individuel"],
    "jours": ["120", "150", "99"],
}})
ct._lire = lambda nom: {{"opinions-cac": opinions, "delais-publication": delais}}[nom]
avec = ct.fig_cac("X", "x")
sans = ct.fig_cac("X", "societe_sans_page")
print(len(avec.axes), len(sans.axes), [t.get_text() for t in sans.axes[1].get_xticklabels()])
"""


@unittest.skipIf(
    importlib.util.find_spec("pandas") is None
    or importlib.util.find_spec("matplotlib") is None,
    "pandas ou matplotlib absent",
)
class FigCacSansDelais(unittest.TestCase):
    def test_trois_vues_avec_delais_deux_sans(self):
        r = subprocess.run(
            [sys.executable, "-c", PROGRAMME.format(figures=str(FIGURES))],
            capture_output=True,
            text=True,
            cwd=RACINE,
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout.strip(), "3 2 ['2018', '2019', '2020', '2021']")


if __name__ == "__main__":
    unittest.main()

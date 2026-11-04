"""Test de `figure_cac` : une société sans page de la Bourse n'a pas de courbe des délais de publication.

Le test tourne dans un sous-processus : importer `figures.cotees` charge matplotlib.pyplot, et
`figtools._image_vue` (testé ailleurs avec de fausses figures) ne ferme une figure que si pyplot est chargé.
"""

import subprocess
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

PROGRAMME = """
import sys
from unittest import mock
import pandas as pd
sys.path.insert(0, "precis/fr/entreprises_publiques")
from figures import cotees

OPINIONS = pd.DataFrame(
    [
        ["ZZ", "2013", "avec réserves", "1", "motif", "5", "k-2013", "immobilisations"],
        ["ZZ", "2014", "sans réserve", "1", "", "5", "k-2014", ""],
    ],
    columns=["groupe", "exercice", "opinion", "rang", "motif", "page_pdf", "source", "themes"],
)
DELAIS = pd.DataFrame(
    [["zz", "2013", "individuel", "30/06/2014", "181", "/node/1"]],
    columns=["societe", "exercice", "nature", "date_publication", "jours", "page"],
)
with mock.patch.object(cotees, "_lire", lambda nom: {"opinions-cac": OPINIONS, "delais-publication": DELAIS}[nom]):
    print(len(cotees.fig_cac("ZZ", "autre").axes), len(cotees.fig_cac("ZZ", "zz").axes))
"""


class FigureCacTest(unittest.TestCase):
    def test_deux_vues_sans_delais_trois_avec(self):
        sortie = subprocess.run(
            [sys.executable, "-c", PROGRAMME],
            cwd=RACINE,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        self.assertEqual(sortie.split(), ["2", "3"])


if __name__ == "__main__":
    unittest.main()

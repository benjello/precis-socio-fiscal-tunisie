"""Test de `figures/cotees.fig_cac` pour une entreprise sans page de la Bourse : pas de courbe des délais.

La figure est tracée dans un sous-processus : l'import de matplotlib.pyplot ne doit pas
changer l'état des autres tests (test_figtools).
"""

import subprocess
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

CODE = """
import sys
from unittest import mock
import pandas as pd
sys.path.insert(0, {ep!r})
sys.path.insert(0, {scripts!r})
from figures import cotees as ct

OPINIONS = pd.DataFrame(
    [
        ["ETAP", "2013", "avec réserves", "1", "motif", "5", "es-etap-2013", "etap_cost_oil"],
        ["ETAP", "2014", "sans réserve", "1", "", "7", "es-etap-2014", ""],
    ],
    columns=["groupe", "exercice", "opinion", "rang", "motif", "page_pdf", "source", "themes"],
)
DELAIS = pd.DataFrame(
    [["stb", "2013", "individuel", "120"], ["stb", "2014", "individuel", "90"]],
    columns=["societe", "exercice", "nature", "jours"],
)

def lire(nom):
    return {{"opinions-cac": OPINIONS, "delais-publication": DELAIS}}[nom]

with mock.patch.object(ct, "_lire", lire):
    print(len(ct.fig_cac("ETAP", "etap").axes))
    print(len(ct.fig_cac("ETAP", "stb").axes))
"""


class FigureCacSansDelais(unittest.TestCase):
    def test_deux_vues_sans_delais_trois_avec(self):
        code = CODE.format(
            ep=str(RACINE / "precis/fr/entreprises_publiques"),
            scripts=str(RACINE / "scripts"),
        )
        sortie = subprocess.run(
            [sys.executable, "-c", code], capture_output=True, text=True, check=True
        ).stdout.split()
        self.assertEqual(sortie, ["2", "3"])


if __name__ == "__main__":
    unittest.main()

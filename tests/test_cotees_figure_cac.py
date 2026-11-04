"""La figure des opinions des commissaires : trois vues avec les délais de la Bourse, deux sans."""

import sys
import unittest
from pathlib import Path
from unittest import mock

try:
    import matplotlib  # noqa: F401
    import pandas as pd
except (
    ImportError
) as exc:  # l'intégration continue lance les tests sans matplotlib ni pandas
    raise unittest.SkipTest(f"dépendance absente : {exc.name}") from exc

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "scripts"))
sys.path.insert(0, str(RACINE / "precis/fr/entreprises_publiques"))

from figures import cotees as ct  # noqa: E402


def _tables():
    opinions = pd.DataFrame(
        [
            (
                "AAA",
                "2008",
                "avec réserves",
                "1",
                "motif",
                "3",
                "ra-aaa-2008",
                "suspens",
            ),
            ("AAA", "2009", "sans réserve", "1", "", "4", "ra-aaa-2009", ""),
            (
                "BBB",
                "2008",
                "avec réserves",
                "1",
                "motif",
                "3",
                "ra-bbb-2008",
                "tt_immeubles",
            ),
            ("BBB", "2009", "sans réserve", "1", "", "4", "ra-bbb-2009", ""),
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
    delais = pd.DataFrame(
        [("aaa", "individuel", "2008", "120"), ("aaa", "individuel", "2009", "100")],
        columns=["societe", "nature", "exercice", "jours"],
    )
    return {"opinions-cac": opinions, "delais-publication": delais}


class FigCacTest(unittest.TestCase):
    def _fig(self, groupe, societe):
        with mock.patch.object(ct, "_lire", side_effect=lambda nom: _tables()[nom]):
            return ct.fig_cac(groupe, societe)

    def test_societe_avec_delais_trois_vues(self):
        fig = self._fig("AAA", "aaa")
        self.assertEqual(len(fig.axes), 3)

    def test_societe_sans_delais_deux_vues(self):
        fig = self._fig("BBB", "bbb")
        self.assertEqual(len(fig.axes), 2)
        self.assertEqual(
            [t.get_text() for t in fig.axes[1].get_xticklabels()],
            ["2007", "2008", "2009"],
        )

    def test_themes_propres_a_un_groupe_hors_des_groupes_sans_reserve(self):
        tables = _tables()
        tables["opinions-cac"] = tables["opinions-cac"][
            tables["opinions-cac"]["groupe"] == "AAA"
        ].assign(opinion="sans réserve", themes="")
        with mock.patch.object(ct, "_lire", side_effect=lambda nom: tables[nom]):
            fig = ct.fig_cac("AAA", "aaa")
        etiquettes = [t.get_text() for t in fig.axes[0].get_yticklabels()]
        self.assertFalse(any("Immeubles apportés" in e for e in etiquettes))
        self.assertTrue(any("Comptes de suspens" in e for e in etiquettes))


if __name__ == "__main__":
    unittest.main()

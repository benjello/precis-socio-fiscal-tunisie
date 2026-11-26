"""Rendu ciblé : une série du cache modifiée ne fait rendre que les livres et pages qui la citent."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import verifier_livres as v  # noqa: E402


class TestSeriesCiblees(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        r = self.racine = Path(self._tmp.name)
        (r / "scripts").mkdir()
        (r / "scripts/figtools.py").write_text('X = "serie-partagee"\n', encoding="utf-8")
        (r / "precis/fr/annexe-pib.qmd").parent.mkdir(parents=True, exist_ok=True)
        (r / "precis/fr/annexe-pib.qmd").write_text("import figtools\n", encoding="utf-8")
        (r / "precis/fr/fiscalite/figures").mkdir(parents=True)
        (r / "precis/fr/fiscalite/figures/tva.py").write_text('SERIE = "tva-taux"\n', encoding="utf-8")
        (r / "precis/fr/retraites").mkdir(parents=True)
        (r / "precis/fr/retraites/_x.qmd").write_text("figtools.series('pensions')\n", encoding="utf-8")
        (r / "precis/fr/figures").mkdir(parents=True)
        (r / "precis/fr/figures/annexe_budget.py").write_text('S = "budget-vote-realise"\n', encoding="utf-8")
        (r / "precis/fr/annexe-budget-etat.qmd").write_text("from figures import annexe_budget\n", encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def test_utilisateurs(self):
        self.assertEqual(v.utilisateurs_serie("tva-taux", self.racine), ({"fiscalite"}, set()))
        self.assertEqual(v.utilisateurs_serie("pensions", self.racine), ({"retraites"}, set()))
        self.assertEqual(v.utilisateurs_serie("budget-vote-realise", self.racine), (set(), {"fr/annexe-budget-etat"}))

    def test_repli_sur_tous_les_livres(self):
        self.assertIsNone(v.utilisateurs_serie("inconnue", self.racine))
        self.assertIsNone(v.utilisateurs_serie("serie-partagee", self.racine))

    def test_series_touchees(self):
        self.assertEqual(v.series_touchees(["precis/_seriescache/tva-taux.csv",
                                            "precis/_seriescache/tva-taux.liens.fr.yml"]), ["tva-taux", "tva-taux"])
        self.assertIsNone(v.series_touchees(["precis/_seriescache/catalog.snapshot.yml"]))
        self.assertEqual(v.series_touchees(["precis/_seriescache/catalog.snapshot.yml",
                                            "precis/_seriescache/tva-taux.csv"]), ["tva-taux"])

    def test_livres_touches_reel(self):
        # Sur le dépôt : la population aux recensements ne fait rendre que les finances locales ;
        # le snapshot seul, tous les livres.
        livres = v.livres_touches(["precis/_seriescache/population-milieu-communal-recensements.csv"])
        self.assertIn("finances_locales", livres)
        self.assertLess(len(livres), len(v.LIVRES))  # pas tous les livres : seulement ceux qui la citent
        self.assertEqual(v.livres_touches(["precis/_seriescache/catalog.snapshot.yml"]), sorted(v.LIVRES))


if __name__ == "__main__":
    unittest.main()

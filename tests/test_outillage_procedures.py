"""remplacer.py (espaces insécables, exclusions) et cache_series.ecrire_serie (fiche à sa place)."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"

try:
    import yaml
    AVEC_YAML = True
except ImportError:
    AVEC_YAML = False


def _module(nom):
    spec = importlib.util.spec_from_file_location(nom, SCRIPTS / f"{nom}.py")
    assert spec and spec.loader
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


rem = _module("remplacer")


class TestRemplacer(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.racine = Path(self._tmp.name)
        self._ancienne = rem.RACINE
        rem.RACINE = self.racine

    def tearDown(self):
        rem.RACINE = self._ancienne
        self._tmp.cleanup()

    def test_espaces_insecables(self):
        p = self.racine / "a.qmd"
        p.write_text("Comment lire ce précis ; le précis dit.", encoding="utf-8")
        total, _ = rem.remplacer(rem.motif_tolerant(r"ce précis"), "cet ouvrage", [p], appliquer=False)
        self.assertEqual(total, 1)
        self.assertTrue(p.read_text(encoding="utf-8").startswith("Comment lire ce précis"))
        rem.remplacer(rem.motif_tolerant(r"ce précis"), "cet ouvrage", [p], appliquer=True)
        self.assertIn("cet ouvrage", p.read_text(encoding="utf-8"))

    def test_espace_echappee(self):
        self.assertTrue(rem.motif_tolerant(r"ce\ précis").search("ce précis"))

    def test_exclusions(self):
        for f in ["precis/fr/a.qmd", "precis/ar/b.qmd", "precis/fr/x/_glossaire.qmd", "docs/notes/n.md"]:
            (self.racine / f).parent.mkdir(parents=True, exist_ok=True)
            (self.racine / f).write_text("x", encoding="utf-8")
        vus = [p.relative_to(self.racine).as_posix()
               for p in rem.fichiers(["precis/**/*.qmd", "docs/**/*.md"], rem.TOUJOURS_EXCLUS)]
        self.assertEqual(vus, ["precis/fr/a.qmd"])


@unittest.skipUnless(AVEC_YAML, "PyYAML absent")
class TestEcrireSerie(unittest.TestCase):
    def test_fiche_a_sa_place(self):
        cs = _module("cache_series")
        with tempfile.TemporaryDirectory() as d:
            cache = Path(d)
            (cache / "catalog.snapshot.yml").write_text(yaml.safe_dump(
                [{"id": "a", "titre": "A", "sources": ["k"]}, {"id": "b", "titre": "B", "sources": ["k"]}]),
                encoding="utf-8")
            cs.ecrire_serie("a", [{"annee": 2020, "valeur": 1.0}], {"titre": "A bis", "sources": ["k"]}, cache=cache)
            cs.ecrire_serie("c", [{"annee": 2020, "valeur": 2.0}], {"titre": "C", "sources": ["k"]}, cache=cache)
            snap = yaml.safe_load((cache / "catalog.snapshot.yml").read_text("utf-8"))
            self.assertEqual([e["id"] for e in snap], ["a", "b", "c"])
            self.assertEqual(snap[0]["titre"], "A bis")
            self.assertTrue((cache / "c.csv").read_text("utf-8").startswith("annee,valeur"))
            with self.assertRaises(ValueError):
                cs.ecrire_serie("d", [{"x": 1}], {"titre": "D"}, cache=cache)


if __name__ == "__main__":
    unittest.main()

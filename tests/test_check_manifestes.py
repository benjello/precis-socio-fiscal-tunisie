"""Tests du contrôle des manifestes de relevés (`.csv.yml`)."""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

try:
    import yaml  # noqa: F401
    AVEC_YAML = True
except ImportError:
    AVEC_YAML = False

from check_manifestes import (  # noqa: E402
    ecarts_manifeste,
    lire_manifeste,
    releves_sans_manifeste,
    verifier,
)

MANIFESTE = """format: long
cle_de_ligne: [exercice, entite]
colonnes:
  exercice: exercice
  entite: entité
  valeur: montant
sources: [cle-a]
"""


def releve(dossier: Path, nom: str, manifeste: str = MANIFESTE, lignes: str = "exercice,entite,valeur\n2020,a,1\n2021,a,2\n") -> Path:
    (dossier / f"{nom}.csv").write_text(lignes, encoding="utf-8")
    chemin = dossier / f"{nom}.csv.yml"
    chemin.write_text(manifeste, encoding="utf-8")
    return chemin


class Manifestes(unittest.TestCase):
    def setUp(self):
        if not AVEC_YAML:
            raise unittest.SkipTest("pyyaml absent")
        self.tmp = tempfile.TemporaryDirectory()
        self.racine = Path(self.tmp.name)
        self.listes = self.racine / "precis" / "fr" / "livre" / "listes"
        self.listes.mkdir(parents=True)
        (self.racine / "precis" / "fr" / "references.json").write_text(
            '{"items": [{"id": "cle-a"}]}', encoding="utf-8"
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_manifeste_correct_accepte(self):
        releve(self.listes, "r")
        self.assertEqual(verifier(self.racine), [])

    def test_yaml_illisible_refuse(self):
        chemin = releve(self.listes, "r", manifeste="colonnes:\n  a: b (vide : non demandée)\n")
        self.assertIn("YAML illisible (ligne 2)", lire_manifeste(chemin))

    def test_source_inconnue_refusee(self):
        chemin = releve(self.listes, "r", manifeste=MANIFESTE.replace("[cle-a]", '["Texte libre, site"]'))
        problemes = ecarts_manifeste(chemin, lire_manifeste(chemin), {"cle-a"})
        self.assertEqual(len(problemes), 1)
        self.assertIn("source inconnue", problemes[0])

    def test_tableaux_avec_sources_par_tableau_acceptes(self):
        manifeste = "format: long\ncle_de_ligne: [exercice, entite]\ntableaux:\n  t:\n    sources: [cle-a]\n"
        chemin = releve(self.listes, "r", manifeste=manifeste)
        self.assertEqual(ecarts_manifeste(chemin, lire_manifeste(chemin), {"cle-a"}), [])
        manifeste = "format: long\ncle_de_ligne: [exercice, entite]\ntableaux:\n  t:\n    sources: [cle-z]\n"
        chemin = releve(self.listes, "r", manifeste=manifeste)
        problemes = ecarts_manifeste(chemin, lire_manifeste(chemin), {"cle-a"})
        self.assertEqual(len(problemes), 1)
        self.assertIn("tableaux.t.sources", problemes[0])

    def test_cle_de_ligne_non_distinctive_refusee(self):
        chemin = releve(self.listes, "r", lignes="exercice,entite,valeur\n2020,a,1\n2020,a,2\n")
        problemes = ecarts_manifeste(chemin, lire_manifeste(chemin), {"cle-a"})
        self.assertEqual(len(problemes), 1)
        self.assertIn("ne distingue pas 1 ligne", problemes[0])

    def test_colonne_absente_refusee(self):
        chemin = releve(self.listes, "r", lignes="exercice,valeur\n2020,1\n")
        problemes = ecarts_manifeste(chemin, lire_manifeste(chemin), {"cle-a"})
        self.assertTrue(any("cle_de_ligne absente du CSV : entite" in p for p in problemes))

    def test_releve_sans_manifeste_signale(self):
        releve(self.listes, "r")
        (self.listes / "orphelin.csv").write_text("a\n1\n", encoding="utf-8")
        self.assertEqual([p.name for p in releves_sans_manifeste(self.racine)], ["orphelin.csv"])
        self.assertTrue(any("relevé sans manifeste" in p for p in verifier(self.racine)))

    def test_dossiers_engendres_ignores(self):
        figdata = self.racine / "precis" / "fr" / "livre" / "figdata"
        figdata.mkdir()
        releve(figdata, "fig", manifeste="format: nimporte\n")
        self.assertEqual(verifier(self.racine), [])


if __name__ == "__main__":
    unittest.main()

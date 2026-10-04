"""Contrôle de la numérotation des volumes (scripts/check_numerotation.py).

Écrit pour `unittest` (CI sans dépendance) : sauté quand PyYAML manque, comme les autres
tests qui lisent du YAML.
"""

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

PROFONDEUR_4 = "format:\n  html:\n    number-depth: 4\n"


@unittest.skipUnless(AVEC_YAML, "PyYAML absent")
class NumerotationTest(unittest.TestCase):
    def ecarts(self, quarto, fichiers):
        from check_numerotation import ecarts_du_livre
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp) / "livre"
            d.mkdir()
            (d / "_quarto.yml").write_text(quarto, encoding="utf-8")
            for nom, texte in fichiers.items():
                (d / nom).write_text(texte, encoding="utf-8")
            return ecarts_du_livre(d)

    def test_livre_conforme(self):
        self.assertEqual(self.ecarts(
            "book:\n  chapters: [index.qmd, a.qmd]\n  appendices: [_glossaire.qmd]\n",
            {"index.qmd": "# Présentation\n", "a.qmd": "# A {#sec-a}\n",
             "_glossaire.qmd": "# Glossaire {.unnumbered}\n"}), [])

    def test_chapitre_non_numerote(self):
        self.assertEqual(len(self.ecarts("book:\n  chapters: [index.qmd]\n",
                                         {"index.qmd": "# Présentation {.unnumbered #sec-p}\n"})), 1)

    def test_toute_partie_est_refusee(self):
        e = self.ecarts("book:\n  chapters:\n    - index.qmd\n    - part: \"P\"\n      chapters: [a.qmd]\n",
                        {"index.qmd": "# P\n", "a.qmd": "# A\n"})
        self.assertTrue(any("partie" in x for x in e))

    def test_saut_de_niveau(self):
        e = self.ecarts("book:\n  chapters: [index.qmd]\n" + PROFONDEUR_4,
                        {"index.qmd": "# P\n\n## A\n\n## B\n\n#### trop bas\n"})
        self.assertTrue(any("saut de niveau" in x for x in e))

    def test_au_dela_de_la_profondeur(self):
        e = self.ecarts("book:\n  chapters: [index.qmd]\nformat:\n  html:\n    number-depth: 2\n",
                        {"index.qmd": "# P\n\n## A\n\n### a1\n\n### a2\n\n## B\n"})
        self.assertTrue(any("au-delà de number-depth" in x for x in e))

    def test_section_a_un_seul_enfant_y_compris_par_inclusion(self):
        e = self.ecarts("book:\n  chapters: [index.qmd]\n" + PROFONDEUR_4,
                        {"index.qmd": "# P\n\n## A\n\n{{< include _inc.qmd >}}\n\n## B\n",
                         "_inc.qmd": "### seul\n\ntexte\n"})
        self.assertTrue(any("une seule sous-section" in x for x in e))

    def test_les_blocs_de_code_ne_sont_pas_des_titres(self):
        self.assertEqual(self.ecarts(
            "book:\n  chapters: [index.qmd]\n" + PROFONDEUR_4,
            {"index.qmd": "# P\n\n## A\n\n```python\n# commentaire\n```\n\n## B\n"}), [])


if __name__ == "__main__":
    unittest.main()

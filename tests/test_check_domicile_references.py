"""Domicile unique des références : la prose nomme, le registre cite."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_domicile_references as cdr  # noqa: E402

TYPES = {"lf-1999": "legislation", "etude-2014": "report"}
REGISTRE = """
:::: {.chronologie-repliable titre="Tous les textes"}

| Date | Texte |
|---|---|
| []{#r-x-1999}1^er^ janvier 1999 | loi de finances pour 1999 [@lf-1999, art. 56, p. 2507] |

::::
"""


def erreurs(tmp: Path, texte: str) -> list[str]:
    fichier = tmp / "chapitre.qmd"
    fichier.write_text(texte, encoding="utf-8")
    return cdr.controler(fichier, TYPES)


class DomicileUniqueTest(unittest.TestCase):
    def setUp(self):
        import tempfile
        self._dossier = tempfile.TemporaryDirectory()
        self.tmp = Path(self._dossier.name)

    def tearDown(self):
        self._dossier.cleanup()

    def test_section_conforme(self):
        texte = ("## Crédit {#sec-c .domicile-unique}\n\n[La loi de finances pour 1999](#r-x-1999) "
                 "porte la part à 50 % ; une étude le chiffre [@etude-2014, p. 3].\n" + REGISTRE)
        self.assertEqual(erreurs(self.tmp, texte), [])

    def test_loi_citee_dans_la_prose(self):
        texte = ("## Crédit {#sec-c .domicile-unique}\n\nLa part passe à 50 % "
                 "[@lf-1999, art. 56].\n" + REGISTRE)
        self.assertEqual(len(erreurs(self.tmp, texte)), 1)

    def test_loi_en_note_admise(self):
        texte = ("## Crédit {#sec-c .domicile-unique}\n\nLa loi de finances pour 1999"
                 "^[[@lf-1999, art. 56, p. 2507].] porte la part à 50 %.\n" + REGISTRE)
        self.assertEqual(erreurs(self.tmp, texte), [])

    def test_hors_section_la_citation_reste_permise(self):
        texte = ("## Crédit {#sec-c .domicile-unique}\n\nTexte.\n" + REGISTRE +
                 "\n## Autre section\n\nLa part passe à 50 % [@lf-1999, art. 56].\n")
        self.assertEqual(erreurs(self.tmp, texte), [])

    def test_lien_sans_ancre(self):
        texte = "## Crédit {.domicile-unique}\n\n[En 2010](#r-x-2010), le délai change.\n" + REGISTRE
        self.assertTrue(any("ancre introuvable" in e for e in erreurs(self.tmp, texte)))

    def test_ancre_hors_registre_ou_sans_reference(self):
        hors = "## Crédit {.domicile-unique}\n\n[]{#r-x-1}Texte.\n"
        self.assertTrue(any("hors d'un bloc" in e for e in erreurs(self.tmp, hors)))
        muette = REGISTRE.replace(" [@lf-1999, art. 56, p. 2507]", "")
        self.assertTrue(any("ne cite" in e for e in erreurs(self.tmp, "## C {.domicile-unique}\n" + muette)))


if __name__ == "__main__":
    unittest.main()

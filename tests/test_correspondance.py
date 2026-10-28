"""La table de correspondance instrument / institution / législation.

Python pur, sans dépendance : la suite tourne `--isolated --no-project`. Le test garde la
table honnête : chaque clé de texte existe dans les références, chaque chapitre cité existe
et porte l'ancre visée, chaque groupe est connu.
"""
import re
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "scripts"))

import correspondance  # noqa: E402

FR = correspondance.RACINE_FR


class TestCorrespondance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lignes = correspondance.lire()
        cls.refs = correspondance.references()

    def test_groupes_connus(self):
        for ligne in self.lignes:
            self.assertIn(ligne["groupe"], correspondance.GROUPES, ligne["instrument"])

    def test_chaque_ligne_a_un_texte_et_un_chapitre(self):
        for ligne in self.lignes:
            self.assertTrue(ligne["instrument"].strip())
            self.assertTrue(correspondance.elements(ligne["textes"]), ligne["instrument"])
            self.assertTrue(correspondance.chapitres(ligne["chapitres"]), ligne["instrument"])

    def test_cles_bibliographiques_existantes(self):
        for ligne in self.lignes:
            for cle, _, est_texte in correspondance.elements(ligne["textes"]):
                if not est_texte:
                    self.assertIn(cle, self.refs, f"{ligne['instrument']} : {cle}")

    def test_chapitres_et_ancres_existent(self):
        for ligne in self.lignes:
            for _, cible in correspondance.chapitres(ligne["chapitres"]):
                fichier, _, ancre = cible.partition("#")
                source = FR / fichier.replace(".html", ".qmd")
                self.assertTrue(source.is_file(), f"{ligne['instrument']} : {source}")
                self.assertTrue(ancre, f"{ligne['instrument']} : ancre manquante")
                texte = source.read_text(encoding="utf-8")
                self.assertRegex(
                    texte, r"\{[^}]*#" + re.escape(ancre) + r"[\s}]",
                    f"{ligne['instrument']} : #{ancre} absent de {source.name}",
                )

    def test_pas_de_doublon_d_instrument(self):
        noms = [ligne["instrument"] for ligne in self.lignes]
        self.assertEqual(len(noms), len(set(noms)))

    def test_cellules(self):
        self.assertEqual(correspondance.cellule_textes("lf-2026|art. 88"), "[@lf-2026, art. 88]")
        self.assertEqual(correspondance.cellule_textes("a;b"), "[@a]<br>[@b]")
        self.assertEqual(correspondance.cellule_textes("=Aucun texte"), "Aucun texte")
        self.assertEqual(
            correspondance.cellule_chapitres("A — B|x/_y.html#z"), "[A — B](x/_y.html#z)"
        )


if __name__ == "__main__":
    unittest.main()

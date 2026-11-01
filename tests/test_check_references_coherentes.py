"""Tests du contrôle de cohérence des clés de références entre livres."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from check_references_coherentes import charger, ecarts, charger_tolerances  # noqa: E402


def entree(**kw):
    return {"id": "lfc-2014", "type": "legislation", "title": "Loi n° 2014-54", "issue": "68",
            "page": "2095-2142", **kw}


def jeu(*definitions):
    return {"fr": {"lfc-2014": {f"precis/fr/livre{i}/references.json": e for i, e in enumerate(definitions)}}}


class Divergences(unittest.TestCase):
    def test_definitions_identiques_acceptees(self):
        self.assertEqual(ecarts(jeu(entree(), entree()), []), [])

    def test_page_differente_refusee(self):
        problemes = ecarts(jeu(entree(), entree(page="2183-2232")), [])
        self.assertEqual(len(problemes), 1)
        self.assertIn("page", problemes[0])

    def test_champ_absent_d_un_cote_refuse(self):
        problemes = ecarts(jeu(entree(volume="160"), entree()), [])
        self.assertEqual(len(problemes), 1)
        self.assertIn("volume", problemes[0])

    def test_titre_compare_sans_casse_ni_ponctuation(self):
        a = entree(title="Décret de la Société de promotion, et d'autres")
        b = entree(title="Décret de la société de promotion et d'autres")
        self.assertEqual(ecarts(jeu(a, b), []), [])

    def test_note_et_titre_court_non_compares(self):
        a = entree(note="lu le 1er", **{"title-short": "A"})
        b = entree(note="autre note", **{"title-short": "B"})
        self.assertEqual(ecarts(jeu(a, b), []), [])

    def test_une_seule_definition_ignoree(self):
        self.assertEqual(ecarts(jeu(entree()), []), [])


class Tolerances(unittest.TestCase):
    TOL = {"langue": "fr", "cle": "lfc-2014", "champs": ["page"], "date": "2026-11-01", "raison": "à unifier"}

    def test_tolerance_declaree_acceptee(self):
        self.assertEqual(ecarts(jeu(entree(), entree(page="2183-2232")), [self.TOL]), [])

    def test_tolerance_inutile_refusee(self):
        problemes = ecarts(jeu(entree(), entree()), [self.TOL])
        self.assertEqual(len(problemes), 1)
        self.assertIn("inutile", problemes[0])

    def test_tolerance_sans_raison_refusee(self):
        tol = {k: v for k, v in self.TOL.items() if k != "raison"}
        problemes = ecarts(jeu(entree(), entree(page="2183-2232")), [tol])
        self.assertTrue(any("incomplète" in p for p in problemes))

    def test_tolerance_date_illisible_refusee(self):
        tol = {**self.TOL, "date": "hier"}
        problemes = ecarts(jeu(entree(), entree(page="2183-2232")), [tol])
        self.assertTrue(any("date illisible" in p for p in problemes))


class DepotReel(unittest.TestCase):
    def test_le_depot_est_coherent(self):
        self.assertEqual(ecarts(charger(), charger_tolerances()), [])


if __name__ == "__main__":
    unittest.main()

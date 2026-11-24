"""Pilote S13 : registre des postes et reconstruction du compte des administrations publiques."""
import csv
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

try:
    import yaml  # noqa: F401
    AVEC_YAML = True
except ImportError:
    AVEC_YAML = False


def lire(nom):
    with (RACINE / "precis" / "fr" / nom).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


class TestRegistre(unittest.TestCase):
    def test_une_section_un_poste(self):
        p = lire("postes-comptables.csv")
        sections = [(x["volume"], x["chapitre"], x["ancre"]) for x in p]
        self.assertEqual(len(sections), len(set(sections)))
        self.assertEqual(len({x["poste"] for x in p}), len(p))

    def test_pas_de_montant_sans_serie(self):
        for x in lire("postes-comptables.csv"):
            if not x["serie"]:
                self.assertEqual(x["montant_reference"], "", x["poste"])


@unittest.skipUnless(AVEC_YAML, "PyYAML absent")
class TestReconstruction(unittest.TestCase):
    def test_verifier_sans_erreur(self):
        import reconstruire_comptes as rc
        self.assertEqual(rc.main(["--verifier"]), 0)

    def test_annee_reference_definitive(self):
        import reconstruire_comptes as rc
        an, ed = rc.annee_reference(rc.lire_csv(rc.CACHE / "cnat-secteurs.csv"))
        lignes = [l for l in rc.lire_csv(rc.CACHE / "cnat-secteurs.csv") if l["edition"] == ed and int(l["annee"]) == an]
        self.assertTrue(lignes and all(l["statut_annee"] == "definitif" for l in lignes))

    def test_residu_egal_cible_moins_postes(self):
        for l in lire("compte-apu-reconstruit.csv"):
            if l["somme_postes_md"]:
                self.assertAlmostEqual(float(l["residu_md"]), float(l["cible_ins_md"]) - float(l["somme_postes_md"]), places=1)


if __name__ == "__main__":
    unittest.main()

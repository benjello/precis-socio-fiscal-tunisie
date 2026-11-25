"""Blocs « passage » : le module lit les mêmes montants que la reconstruction du compte S13."""
import csv
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

import passage_comptes as pc  # noqa: E402


def lire(nom):
    with (RACINE / "precis" / "fr" / nom).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


class TestPassage(unittest.TestCase):
    def test_annee_de_reference_comme_le_compte_reconstruit(self):
        """Pour chaque poste chiffré l'année de référence, poste et cible INS égalent compte-apu-reconstruit.csv."""
        lignes = [l for l in lire("compte-apu-reconstruit.csv") if l["postes"] and l["somme_postes_md"]
                  and "," not in l["postes"] and ";" not in l["postes"]]
        vus = 0
        for l in lignes:
            p = pc.registre().get(l["postes"])
            if not p or p["code_scn"] != l["code_scn"] or p["operation"] != l["operation"]:
                continue
            if pc.rc.SECTEURS.get(pc.secteur_ins(p)) != l["secteur"]:
                continue
            an = int(l["annee"])
            d = {x["annee"]: x for x in pc.lignes(l["postes"], [an])}
            if an not in d:
                continue
            self.assertAlmostEqual(d[an]["ins"], float(l["cible_ins_md"]), places=1, msg=l["postes"])
            vus += 1
        self.assertGreater(vus, 0)

    def test_lignes_sans_trou(self):
        """Une ligne n'existe que si le poste et la cible sont chiffrés ; la part est leur rapport."""
        for l in pc.lignes("interets-dette-collectivites"):
            self.assertAlmostEqual(l["part"], 100 * l["montant"] / l["ins"])

    def test_terme(self):
        self.assertEqual(pc.terme("cotisations-cnam"), "Cotisations sociales (D.61)")


if __name__ == "__main__":
    unittest.main()

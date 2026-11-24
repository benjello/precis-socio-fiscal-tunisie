"""Les résidus de 2023 : tests reproductibles et statuts bornés."""
import csv
import subprocess
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent


class TestResidus(unittest.TestCase):
    def test_a_jour(self):
        r = subprocess.run(["uv", "run", "python", "scripts/expliquer_residus.py", "--verifier"], cwd=RACINE, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_statuts_et_chiffres(self):
        ls = list(csv.DictReader((RACINE / "precis/fr/compte-apu-residus.csv").open(encoding="utf-8")))
        self.assertTrue({l["statut"] for l in ls} <= {"établi", "plausible", "écarté"})
        for l in ls:
            if l["statut"] == "établi":
                self.assertNotEqual(l["chiffre_md"], "", l)  # un « établi » porte toujours son chiffre
        d1 = next(l for l in ls if l["operation"] == "remuneration_salaries" and l["hypothese"] == "périmètre")
        self.assertEqual(d1["statut"], "établi")


if __name__ == "__main__":
    unittest.main()

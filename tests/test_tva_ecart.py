"""Contrôle, valeur par valeur, de la série `tva-ecart-prevision-realise`.

La série est écrite par `scripts/generate_tva_ecart.py` ; ce test la recalcule AUTREMENT (module
`csv`, sans pandas, sans le code du générateur) à partir des relevés et des séries sources, et
vérifie : chaque valeur de l'écart, la cohérence des bases du PIB (jamais raccordées), le
rapprochement avec le classeur du ministère (périmètre de la prévision) et les cases vides.
"""
import csv
import math
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
CACHE = RACINE / "precis" / "_seriescache"
TVA = RACINE / "precis" / "fr" / "fiscalite" / "tva"


def lire(chemin):
    with open(chemin, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def nombre(v):
    return None if v in ("", None) else float(v)


class EcartTvaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.serie = {int(r["annee"]): r for r in lire(CACHE / "tva-ecart-prevision-realise.csv")}
        cls.prevision = {}
        for r in lire(TVA / "recettes-tva-par-regime.csv"):
            cls.prevision[int(r["annee"])] = cls.prevision.get(int(r["annee"]), 0.0) + float(r["valeur_md"])
        cls.realise = {int(r["annee"]): nombre(r["tva_MDT"])
                       for r in lire(CACHE / "recettes-fiscales-composition.csv")}
        cls.pib = {}
        for r in lire(CACHE / "pib-courant-par-base.csv"):
            cls.pib.setdefault(int(r["annee"]), []).append((r["base"], float(r["pib_MD"])))
        cls.classeur = {int(r["annee"]): r for r in lire(TVA / "classeur-tva-lf-lfc.csv")}

    def test_annees(self):
        self.assertEqual(sorted(self.serie), list(range(2001, 2027)))

    def test_prevision_et_realise(self):
        for a, r in self.serie.items():
            self.assertAlmostEqual(float(r["prevision_MD"]), self.prevision[a], places=6, msg=a)
            if a <= 2025:
                self.assertAlmostEqual(float(r["realise_MD"]), self.realise[a], places=6, msg=a)
            else:
                self.assertEqual(r["realise_MD"], "", msg=a)

    def test_ecart_en_md_et_en_pct_de_la_prevision(self):
        for a, r in self.serie.items():
            if a > 2025:
                self.assertEqual((r["ecart_MD"], r["ecart_pct_prevision"]), ("", ""), msg=a)
                continue
            e = self.realise[a] - self.prevision[a]
            self.assertAlmostEqual(float(r["ecart_MD"]), e, places=4, msg=a)
            self.assertAlmostEqual(float(r["ecart_pct_prevision"]), 100 * e / self.prevision[a],
                                   places=4, msg=a)

    def test_ecart_en_pct_du_pib_par_base_sans_raccord(self):
        # Une colonne par base ; une année absente d'une base reste vide ; deux bases la même année
        # donnent deux valeurs différentes, jamais l'une pour l'autre.
        noms = {"base1983": "1983", "base1997": "1997", "base2015": "2015"}
        for a, r in self.serie.items():
            e = None if a > 2025 else self.realise[a] - self.prevision[a]
            attendu = {}
            for base, pib in self.pib.get(a, []):
                if base.startswith("non rattachée"):
                    attendu["non_rattache"] = pib
                elif "présumée" in base:
                    continue
                else:
                    for cle, an in noms.items():
                        if an in base:
                            attendu[cle] = pib
            for cle in ("base1983", "base1997", "base2015", "non_rattache"):
                v = r[f"ecart_pct_pib_{cle}"]
                if cle in attendu and e is not None:
                    self.assertAlmostEqual(float(v), 100 * e / attendu[cle], places=4, msg=(a, cle))
                    self.assertAlmostEqual(float(r[f"pib_{cle}_MD"]), attendu[cle], places=6)
                else:
                    self.assertEqual(v, "", msg=(a, cle))

    def test_couverture_des_bases(self):
        # 1983 : 2001-2009 ; 1997 : 2001-2017 ; 2015 : 2010-2025 ; non rattaché : 2002-2004 et 2025.
        def annees(cle):
            return [a for a, r in self.serie.items() if r[f"pib_{cle}_MD"] != ""]
        self.assertEqual(annees("base1983"), list(range(2001, 2010)))
        self.assertEqual(annees("base1997"), list(range(2001, 2018)))
        self.assertEqual(annees("base2015"), list(range(2010, 2026)))
        self.assertEqual(annees("non_rattache"), [2002, 2003, 2004, 2025])

    def test_classeur_du_ministere_perimetre_de_la_prevision(self):
        # Les colonnes LF du classeur égalent la somme des deux lignes du tableau A, 2014-2026 ;
        # ses réalisations égalent la série de composition des recettes fiscales.
        n = 0
        for a, r in self.classeur.items():
            lf = nombre(r["lf_MD"])
            if lf is not None:
                n += 1
                self.assertAlmostEqual(lf, self.prevision[a], places=6, msg=a)
            re = nombre(r["realise_MD"])
            if re is not None:
                self.assertAlmostEqual(re, self.realise[a], places=6, msg=a)
        self.assertEqual(n, 13)

    def test_lfc_signalee_quand_elle_existe(self):
        for a, r in self.serie.items():
            lfc = nombre(self.classeur[a]["lfc_MD"]) if a in self.classeur else None
            self.assertEqual(nombre(r["lfc_MD"]), lfc, msg=a)

    def test_valeurs_extremes_citees_au_texte(self):
        # Les chiffres du chapitre : plus grands écarts de 2020 et de 2021.
        r20, r21 = self.serie[2020], self.serie[2021]
        self.assertTrue(math.isclose(float(r20["ecart_pct_prevision"]), -19.77, abs_tol=0.01))
        self.assertTrue(math.isclose(float(r21["ecart_pct_prevision"]), 16.05, abs_tol=0.01))
        self.assertTrue(math.isclose(float(r20["ecart_pct_pib_base2015"]), -1.48, abs_tol=0.01))
        self.assertTrue(math.isclose(float(r21["ecart_pct_pib_base2015"]), 0.92, abs_tol=0.01))


if __name__ == "__main__":
    unittest.main()

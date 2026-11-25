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

    def test_montant_caisse_et_fenetre(self):
        import reconstruire_comptes as rc
        # forme « CAISSE|indicateur » : toutes les années de la série, édition la plus récente
        self.assertEqual(rc.montant("minfin-ep-caisses", "CNAM|recettes techniques", 2020), (3525.2, "2020-2023"))
        self.assertEqual(rc.montant("minfin-ep-caisses", "CNRPS|recettes techniques", 2022), (6197.6, "2020-2023"))
        # forme « CAISSE|indicateur|AAAA-AAAA » : rien hors de la fenêtre, années couvertes = la fenêtre
        self.assertEqual(rc.montant("minfin-ep-caisses", "CNSS|recettes techniques|2021-2023", 2020), (None, "2021-2023"))
        self.assertEqual(rc.montant("minfin-ep-caisses", "CNSS|recettes techniques|2021-2023", 2021), (3749.2, "2021-2023"))
        self.assertEqual(rc.montant("minfin-ep-caisses", "CNSS|recettes techniques|2021-2023", 2023), (4556.9, "2021-2023"))
        # forme sans caisse : indicateur seul, inchangée
        m, couv = rc.montant("minfin-ep-caisses", "recettes techniques", 2023)
        self.assertIsNotNone(m)
        self.assertEqual(couv, "2020-2023")

    def test_montant_somme_d_entreprises(self):
        import reconstruire_comptes as rc
        s = "entreprises-publiques-effectifs-par-entreprise"
        # « champ|e1;e2 » : somme sur ces entreprises, dernière édition de chaque exercice
        self.assertEqual(rc.montant(s, "charges_personnel_md|steg;etap", 2020), (619.0, "2018-2023"))
        # une entreprise sans valeur une année (Groupe chimique, 2023) : aucun montant, périmètre constant
        self.assertEqual(rc.montant(s, "charges_personnel_md|steg;gct", 2023), (None, "2018-2022"))
        # le poste du registre : 19 sociétés non financières, 2020
        p = next(x for x in lire("postes-comptables.csv") if x["poste"] == "remunerations-entreprises-publiques")
        self.assertEqual(rc.montant(p["serie"], p["colonne"], 2020), (2062.4, "2018-2023"))

    def test_fin_encadre_poste_borne(self):
        import reconstruire_comptes as rc
        borne = {"montant_reference": "", "colonne": "CNSS|recettes techniques|2021-2023", "annees": "2021-2023"}
        self.assertIn("chiffre les années 2021-2023, non l'année de référence 2020", rc.fin_encadre(borne, 2020, [2021, 2022, 2023]))
        sans = {"montant_reference": "", "colonne": "CNAM|recettes techniques", "annees": "2020-2023"}
        self.assertIn("ne chiffre pas encore", rc.fin_encadre(sans, 2020, []))
        # poste non borné sans valeur l'année de référence : ses années, suivies ou discontinues
        self.assertIn("chiffre les années 2022-2024, non l'année de référence 2020", rc.fin_encadre(sans, 2020, [2022, 2023, 2024]))
        self.assertIn("chiffre les années 2019, 2021 et 2023, non", rc.fin_encadre(sans, 2020, [2019, 2021, 2023]))
        self.assertIn("chiffre l'année 2023, non", rc.fin_encadre(sans, 2020, [2023]))
        self.assertEqual(rc.liste_annees([2008, 2009, 2010, 2022, 2023]), "2008-2010 et 2022-2023")
        # années lues dans la série : P.61 n'a de valeur qu'à partir de 2022 ; fenêtre d'un poste borné respectée
        p61 = {"serie": "bct-bdp-postes-s2", "colonne": "P.61 exportations de biens"}
        self.assertEqual(rc.annees_chiffrees(p61), [2022, 2023, 2024])
        self.assertEqual(rc.annees_chiffrees({"serie": "minfin-ep-caisses", "colonne": "CNSS|recettes techniques|2021-2023"}),
                         [2021, 2022, 2023])
        self.assertEqual(rc.annees_chiffrees({"serie": "", "colonne": ""}), [])
        avec = {"montant_reference": "3430.0", "colonne": "cotisations_md", "annees": "2000-2020"}
        self.assertIn("en chiffre 3 430,0", rc.fin_encadre(avec, 2020))

    def test_phrase_montant_selon_secteur(self):
        import reconstruire_comptes as rc
        cible = {("ressources", "autres_transferts_courants"): {"cible_ins_md": 4041.0}}
        qui = [{"operation": "autres_transferts_courants", "secteur": "reste du monde", "cote": "ressources",
                "niveau": "secteur", "valeur_md": 556.3}]
        rdm = {"secteur_verse": "snf;sf;menages", "secteur_recoit": "rdm", "cote": "ressources",
               "operation": "autres_transferts_courants", "montant_reference": "489.3", "colonne": "", "annees": ""}
        # poste sans administration : montant du reste du monde, jamais celui des administrations
        txt = rc.phrase_montant(rdm, cible, qui, 2020)
        self.assertIn("Le reste du monde y inscrit 556,3 millions de dinars (ressources)", txt)
        self.assertNotIn("administrations publiques", txt)
        # montant du secteur absent des comptes : pas de phrase
        self.assertEqual(rc.phrase_montant(rdm, cible, [], 2020), "")
        # plusieurs secteurs du côté du poste : pas de phrase
        plusieurs = dict(rdm, cote="emplois")
        self.assertEqual(rc.phrase_montant(plusieurs, cible, qui, 2020), "")
        # poste d'une administration : montant de S13
        apu = dict(rdm, secteur_recoit="apu_centrale")
        self.assertIn("Les administrations publiques y inscrivent 4 041,0", rc.phrase_montant(apu, cible, qui, 2020))

    def test_residu_egal_cible_moins_postes(self):
        for l in lire("compte-apu-reconstruit.csv"):
            if l["somme_postes_md"]:
                self.assertAlmostEqual(float(l["residu_md"]), float(l["cible_ins_md"]) - float(l["somme_postes_md"]), places=1)


if __name__ == "__main__":
    unittest.main()

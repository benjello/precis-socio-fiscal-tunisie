"""Tests de `scripts/perimetres_tunisair.py` : sans PDF, sur des extraits de texte."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import perimetres_tunisair as p  # noqa: E402

# Texte brut de pdftotext, états financiers consolidés 2022 (page 11) : les noms de Handling, Technics, Amadeus,
# Tunisie Catering et ATCT sont des logos, absents du texte.
TEXTE_2022 = """
Choix des méthodes : AMADEUS SA est considéré filiale en se basant sur le critère de droit de vote (70%).
PÉRIMÈTRE DE CONSOLIDATION
Le périmètre de consolidation au 31 décembre 2022, se présente comme suit :
Méthode de
consolidation
Sociétés Activité Droit
de
vote
Sociétés
intégrées
globalement
Prestations de services pour les
compagnies Aériennes. 100%
Entretien et réparation des
avions et des équipements
avioniques
100%
SCI ESSAFA Immobilier 99,9%
TUNISAIR EXPRESS
Transport aérien 88,73%
Prestations informatiques
70%
Sociétés
mises en
équivalence
Catering 45%
Formation Aéronautique 37%
NOTES AUX ÉTATS FINANCIERS CONSOLIDÉS
Note 1 : TITRES MIS EN EQUIVALENCE (T.M.E)
Tunisie Catering détenue à hauteur de 45%.
"""
# 2009 : tableau sur deux pages, AISA en intégration proportionnelle, logo « SEVENAIR » pour le transport aérien.
TEXTE_2009 = """
Méthode de consolidation Sociétés Activité Droits de vote
Sociétés intégrées
globalement
Prestations de services
pour les compagnies
Aériennes.
100%
Entretien et réparation
des avions et des
équipements
avioniques
100%
SCI ESSAFA Immobilier 99,9%
Transport aérien 88,73%
Prestations
informatiques et
Télécom
70%
Transport aérien
international et
domestique
51%
Société intégrée
proportionnellement
Services informatiques
et Télécoms
50%
ETATS FINANCIERS CONSOLIDES 2009
9
Sociétés mises en
équivalence
Catering 45%
Formation
Aéronautique
34%
Notes Relatives Aux Postes Des Etats Financiers consolidés :
Titres TUNISIE CATERING 9 438 656
"""
TEXTE_2006 = """
SOCIETES DU PERIMETRE
8/14
Sociétés Activité Droits de vote
- TUNINTER Transport aérien 83,37%
- AMADEUS
Prestations
informatiques
70%
- MAURITANIA
AIRWAYS
Transport aérien
international et
domestique
51%
- TUNISIE CATERING Catering 45%
Sociétés mises en
équivalence
- ATCT Formation Aéronautique 34%
G
GR
RO
OU
UP
PE
E T
"""


class TestPerimetresTunisair(unittest.TestCase):
    def lire(self, texte, exercice):
        return p.lire_tableau(p.corps_du_tableau(texte, exercice), exercice)

    def test_2022_sept_societes_noms_par_activite(self):
        lignes = self.lire(TEXTE_2022, 2022)
        self.assertEqual(
            [
                (ligne["entite"], ligne["methode"], ligne["controle_pct"])
                for ligne in lignes
            ],
            [
                ("TUNISAIR HANDLING", "intégration globale", "100"),
                ("TUNISAIR TECHNICS", "intégration globale", "100"),
                ("SCI ESSAFA", "intégration globale", "99.9"),
                ("TUNISAIR EXPRESS", "intégration globale", "88.73"),
                ("AMADEUS", "intégration globale", "70"),
                ("TUNISIE CATERING", "mise en équivalence", "45"),
                ("ATCT", "mise en équivalence", "37"),
            ],
        )
        self.assertEqual(len(lignes), p.NOMBRE_ANNONCE[2022])

    def test_le_texte_hors_tableau_n_est_pas_lu(self):
        # le 70 % et le 45 % des pages voisines ne sont pas des lignes du tableau
        self.assertEqual(len(self.lire(TEXTE_2022, 2022)), 7)

    def test_2009_proportionnelle_et_nom_imprime(self):
        lignes = self.lire(TEXTE_2009, 2009)
        self.assertEqual(len(lignes), 9)
        par_nom = {ligne["entite"]: ligne for ligne in lignes}
        self.assertIn("SEVENAIR", par_nom)
        self.assertNotIn("TUNISAIR EXPRESS", par_nom)
        self.assertEqual(par_nom["AISA"]["methode"], "intégration proportionnelle")
        self.assertEqual(par_nom["AISA"]["controle_pct"], "50")
        self.assertEqual(par_nom["MAURITANIA AIRWAYS"]["controle_pct"], "51")
        self.assertEqual(par_nom["ATCT"]["methode"], "mise en équivalence")

    def test_aisa_en_integration_globale_des_2012(self):
        self.assertEqual(p.methode_de("AISA", 2011), "intégration proportionnelle")
        self.assertEqual(p.methode_de("AISA", 2012), "intégration globale")

    def test_2006_noms_du_texte(self):
        lignes = self.lire(TEXTE_2006, 2006)
        self.assertEqual(
            [(ligne["entite"], ligne["controle_pct"]) for ligne in lignes],
            [
                ("TUNINTER", "83.37"),
                ("AMADEUS", "70"),
                ("MAURITANIA AIRWAYS", "51"),
                ("TUNISIE CATERING", "45"),
                ("ATCT", "34"),
            ],
        )

    def test_activite_inconnue_arrete_la_lecture(self):
        with self.assertRaises(ValueError):
            p.lire_tableau("Activité nouvelle 12%", 2020)

    def test_en_tete_introuvable(self):
        with self.assertRaises(ValueError):
            p.corps_du_tableau("rien", 2015)


if __name__ == "__main__":
    unittest.main()

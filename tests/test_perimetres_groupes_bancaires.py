"""Tests de `scripts/perimetres_groupes_bancaires.py` : sans PDF, sur des extraits de texte."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import perimetres_groupes_bancaires as p  # noqa: E402

BNA = """
   4- PÉRIMÈTRE DE CONSOLIDATION
               Banque Nationale Agricole                                                         Intégration globale       100,000%      99,833%
               TUNIS-RE                                                                          Mise en équivalence        21,51%        19,77%
               SIMPAR (1)                                                                        Intégration globale        40,51%        33,38%
      (1) La BNA détient 33,926% des droits de vote dans la société cotée en bourse SIMPAR.
"""
BH = """
Les entreprises retenues dans le périmètre de consolidation, le pourcentage d'intérêt ainsi que les méthodes
BH BANK                                                                    100,00           100,00                    Intégration Globale                               Tunisie
TFB                                                                         27,86            27,86                    Mise en équivalence                               France
• Méthodes de consolidation
"""
STB_2019 = """
STB INVEST                   94,60%     99,51%          -4,91%         IG          IG               94,73%        99,48%         -4,75%
SOFELAN                      0,00%      60,63%      -60,63%            NI          IG                  0,00%      59,89%        -59,89%
MGERT                        49,95%      0,00%      49,95%             IG          NI               49,94%         0,00%        49,94%
SICAV OBLIG                  1,61%       1,59%          0,01%       MEE           MEE               1,55%       1,47%         0,07%
"""
BH_RAPPORT_2019 = """
Les entreprises retenues dans le périmètre de consolidation, le pourcentage d'intérêt ainsi que les méthodes de leur
consolidation, se présentent comme suit:
Désignation
2019 2018 2019 2018
BH BANK 100,00 100,00 100,00 100,00
Intégration
Globale
Tunisie
TFB 34,22 33,42 34,22 33,41
Mise en équiva-
lence
France
Méthodes de consolidation
"""
BH_RAPPORT_2022 = """
se présentent comme suit :
BH BANK 100,00 100,00 Intégration Globale Tunisie
TFB 18,79 27,86 Mise en équivalence France
SICAV BH-Capitalisation 20,25 21,24 Intégration Globale Tunisie
• Méthodes de consolidation
"""
STB = """
SOCIETES CONSOLIDEES
   1. STB BANK (société Mère)                           100,00%   100,00%    0,00%
   2. STB INVEST                                         95,05%    94,60%    0,44%
SOCIETES CONSOLIDEES
   1. STB BANK (société Mère)                              99,98%     99,99%      0,00%
   2. STB INVEST                                           94,72%     94,73%      0,00%
"""

BTE_2009 = """
Le tableau suivant synthétise le périmètre et les méthodes de consolidation utilisées pour
l'élaboration des états financiers consolidés du Groupe BTE :
Sociétés Secteur
Pourcentage
de contrôle Qualification
Méthode de
consolidation
Pourcentage
d'intérêt
Banque de Tunisie
et des Emirats financier 100% Mère
intégration
globale 100%
L'Intermédiaire International financier 39,47% Associée
mise en
équivalence 39,47%
Société Djerba Aghir touristique 43,67% Associée
mise en
équivalence 43 ,67%
Tuniso Emiratie Sicav (TES) * financier 25.26% Filiale
intégration
globale 20,44%
*Données retraitées pour les besoins de comparabilité
5. PRINCIPES COMPTABLES DE PRESENTATION ET D'EVALUATION
"""
BTE_2020 = """
Le tableau suivant synthétise le périmètre
Sociétés Secteur
Pourcentage
de contrôle
Qualification
Méthode de
consolidation
Pourcentage
d'intérêt
Banque de Tunisie et des Émirats Financier 100% Mère
Intégration
globale
100%
Tuniso Émiratie Sicav (TES) Financier 5.73% Filiale
Intégration
globale
5.73%
 Nature de la relation entre la société mère BTE et la SICAV TES
"""


class PerimetresTest(unittest.TestCase):
    def test_bna_methode_controle_et_interet(self):
        lignes = p.bna(BNA)
        self.assertEqual(
            lignes[0][:6],
            ["BNA", "2021", "Banque Nationale Agricole", "mère", "100.000", "99.833"],
        )
        self.assertEqual(lignes[1][3], "mise en équivalence")
        self.assertEqual(lignes[2][2], "SIMPAR")  # le renvoi « (1) » n'est pas gardé

    def test_bh_ne_donne_que_l_interet(self):
        lignes = p.bh(BH)
        self.assertEqual(lignes[0][:6], ["BH", "2021", "BH BANK", "mère", "", "100.00"])
        self.assertEqual(lignes[1][4:7], ["", "27.86", "France"])

    def test_stb_rapproche_controle_et_interet_par_numero(self):
        lignes = [l for l in p.stb(STB) if l[1] == "2021"]
        self.assertEqual(
            lignes[0][:6], ["STB", "2021", "STB BANK", "mère", "100.00", "99.98"]
        )
        self.assertEqual(lignes[1][4:6], ["95.05", "94.72"])


class TestStbConsolide2019(unittest.TestCase):
    def test_deux_exercices_et_hors_perimetre(self):
        lignes = p.stb_consolide_2019(STB_2019, 2019)
        par = {(l[1], l[2]): l for l in lignes}
        self.assertNotIn(("2019", "SOFI ELAN SICAF"), par)  # NI en 2019
        self.assertEqual(par[("2018", "SOFI ELAN SICAF")][5], "59.89")
        self.assertNotIn(
            ("2018", "MAGASINS GENERAUX ET ENTREPORTS REELS DE TUNIS"), par
        )  # NI en 2018
        self.assertEqual(
            par[("2019", "MAGASINS GENERAUX ET ENTREPORTS REELS DE TUNIS")][4:6],
            ["49.95", "49.94"],
        )
        self.assertEqual(
            par[("2018", "SICAV EPARGNE OBLIGATAIRE")][3], "mise en équivalence"
        )
        self.assertEqual(len(lignes), 6)


class TestBhRapport(unittest.TestCase):
    def test_quatre_pourcentages_puis_methode_sur_les_lignes_suivantes(self):
        par = {(r[1], r[2]): r for r in p.bh_rapport(BH_RAPPORT_2019, 2019)}
        self.assertEqual(
            par[("2019", "TFB")][3:6], ["mise en équivalence", "34.22", "34.22"]
        )
        self.assertEqual(par[("2018", "TFB")][4:6], ["33.42", "33.41"])
        self.assertEqual(par[("2019", "BH BANK")][3], "mère")

    def test_deux_pourcentages_et_methode_sur_la_ligne(self):
        lignes = p.bh_rapport(BH_RAPPORT_2022, 2022)
        par = {(r[1], r[2]): r for r in lignes}
        self.assertEqual(len(lignes), 6)
        self.assertEqual(par[("2021", "TFB")][5], "27.86")
        self.assertEqual(
            par[("2022", "SICAV BH-Capitalisation")][3:6],
            ["intégration globale", "", "20.25"],
        )


BH_RAPPORT_2023 = """
Les entreprises retenues dans le périmètre de consolidation
BH BANK                        100,00      100,00      Intégration Globale      Tunisie
tion BH-Capitalisa-             18,75       20,25      Intégration Globale      Tunisie
TFB                             19,99       18,79      Mise en équivalence      France
Méthodes de consolidation
"""


class TestBhRapport2023(unittest.TestCase):
    def test_coupure_sicav_bh_capitalisation_reparee(self):
        par = {(r[1], r[2]): r for r in p.bh_rapport(BH_RAPPORT_2023, 2023)}
        # « tion BH-Capitalisa- » (nom coupé par la mise en page) est rétabli en SICAV BH-Capitalisation
        self.assertIn(("2023", "SICAV BH-Capitalisation"), par)
        self.assertNotIn(("2023", "tion BH-Capitalisa-"), par)
        self.assertEqual(par[("2023", "SICAV BH-Capitalisation")][5], "18.75")
        self.assertEqual(par[("2023", "TFB")][3:6], ["mise en équivalence", "", "19.99"])


class TestBte(unittest.TestCase):
    def test_methode_pourcentages_et_nom_sans_etoile(self):
        par = {r[2]: r for r in p.bte(BTE_2009, 2009)}
        self.assertEqual(len(par), 4)
        self.assertEqual(
            par["Banque de Tunisie et des Emirats"][:7],
            [
                "BTE",
                "2009",
                "Banque de Tunisie et des Emirats",
                "mère",
                "100",
                "100",
                "",
            ],
        )
        self.assertEqual(
            par["Société Djerba Aghir"][3:6], ["mise en équivalence", "43.67", "43.67"]
        )  # « 43 ,67% » recollé
        self.assertEqual(
            par["Tuniso Emiratie Sicav (TES)"][3:6],
            ["intégration globale", "25.26", "20.44"],
        )  # l'astérisque de renvoi n'est pas gardé

    def test_la_derniere_ligne_n_est_pas_prise_pour_un_titre(self):
        # « 5.73% » en début de ligne n'est pas le titre « 5. Principes comptables »
        noms = [r[2] for r in p.bte(BTE_2020, 2020)]
        self.assertEqual(
            noms, ["Banque de Tunisie et des Émirats", "Tuniso Émiratie Sicav (TES)"]
        )


if __name__ == "__main__":
    unittest.main()

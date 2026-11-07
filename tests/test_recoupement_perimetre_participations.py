"""Tests de `scripts/recoupement_perimetre_participations.py` : sans PDF, sur des extraits de texte."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import recoupement_perimetre_participations as r  # noqa: E402

PARTICIPATIONS = """
La liste des principales entreprises filiales au 31/12/2019 se détaille comme suit :
                                 Filiales                          Quote part        Brute      Prov      Nette
SECTEUR FINANCIER
STRC                                                                 91,93%          36 462         0      36 462
STB-FINANCE                                                          61.34%            4 749         0       4 749
SECTEUR TOURISTIQUE
SKANES PALACE INTERNATIO                                             99.76%            6 180     6 180           0
STE LA GENERALE DE VENTE                                            50,00%            2 000     1 485         515
Les résultats et les capitaux propres des filiales se présentent comme suit :
"""

BILAN = """
Total des passifs                                                                      10 317 012    9 697 420
Intérêts Minoritaires (*)                                                                   7 086        6 550
Total des Capitaux propres                                                  6.14         1 082 745      911 052
Total des capitaux propres et passifs                                                  11 406 843   10 615 022
Total des actifs                                                                        11 406 843   10 615 022
Résultat net de l'exercice                                                                 178 807       60 938
Intérêts minoritaires dans le résultat (*)                                                     133        1 024
Résultat Net consolidé part du groupe                                                      178 674       59 914
"""


# --- BH : note « participations dans les parties liées » (Brut/Prov/Net) et « Liste des filiales » (%) ---
BH_PARTICIPATIONS = """
Les participations dans les parties liées à la banque se détaillent comme suit :
                                               31/12/2021              31/12/2020
Participations                            Brut        Prov      Net      Brut      Prov     Net
BH LEASING                              12 371           -   12 371    12 371      (99)  12 272
STIMEC                                     420       (420)        -       420     (420)       -
Société Moderne de titrisation             326       (326)        -       326     (326)       -
TFB                                     41 000    (30 409)   10 591    41 000  (28 968)  12 032
Total                                  100 994    (31 858)   69 136   100 994  (30 708)  70 286
"""

BH_FILIALES = """
Liste des entreprises filiales
           Dénomination                              Adresse               Capital       %        Résultat
Modern Leasing (*)                Immeuble SALIM, Centre Urbain Nord       35 000    37,44%      2 432
Société SIFIB                     Siège Assurances Salim                    3 000    30,00%        313
Société Moderne de titrisation    Espace Tunis, Mont plaisir                  500    40,00%          -
"""

# --- BNA : note « portefeuille titres d'investissement » (% + brute/prov/nette) ---
BNA_PORTEFEUILLE = """
Le portefeuille titres d'investissement se détaillent au 31/12/2021 comme suit :
                                   % de         Valeur brute                 Valeur brute                 Valeur nette au
Titres                         participation   au 31/12/2020   Cessions      au 31/12/2021   Provisions    31/12/2021
SICAF Participations               99,99%              500            -             500              -           500
SICAR INVEST                       59,80%            6 616            -           6 616              -         6 616
LES ŒILLETS                        29,39%              265            -             265          (265)             -
SODAL                              69,01%            1 447            -           1 447        (1 447)             -
GENERALE DES VENTES                50,00%            2 000            -           2 000          (936)         1 064
Total général                                     185 008          274         185 283       (57 345)       127 938
Les résultats et les capitaux propres des filiales se présentent comme suit :
"""

# Bilan consolidé BH : code de note « 12 » devant les capitaux propres, colonnes N/N-1 collées par une seule espace.
BH_BILAN = """
Total des actifs                       12 941 622 13 129 605
Total des passifs                      11 578 186 11 884 632
Intérêts Minoritaires                     179 261    171 526
Total des Capitaux propres        12    1 184 175  1 073 447
Total des capitaux propres et passifs  12 941 622 13 129 605
"""

# Bilan consolidé BNA : libellés « IM - … » et « …, Part du groupe », minoritaires du résultat imprimés négatifs.
BNA_BILAN = """
 Total des actifs                      19 707 078 14 673 493   5 033 585  34,3%
 Total des passifs                     17 590 365 12 684 441   4 905 924  38,7%
 IM - Intérêts Minoritaires               355 616    338 456      17 160   5,1%
Total des Capitaux propres ( Part du Groupe)   1 761 097  1 650 596  110 501  6,7%
Total des capitaux propres et passifs  19 707 078 14 673 493   5 033 585  34,3%
Produit Net Bancaire                      912 190    691 244     220 946  32,0%
Résultat net de l'exercice                179 899    117 441      62 458  53,2%
Intérêts minoritaires                      (6 533)    (9 802)       3 269  33,4%
Résultat net de l'exercice, Part du groupe 173 366    107 639      65 727  61,1%
"""


class CleTest(unittest.TestCase):
    def test_rapproche_individuel_et_consolide(self):
        # mêmes clés des deux côtés malgré « Société », « STE », l'apostrophe « L' » et les guillemets
        self.assertEqual(r.cle("IMMOBILIERE DE L'AVENUE"), r.cle("L’IMMOBILIERE DE L’AVENUE"))
        self.assertEqual(r.cle("ED-DKHILA"), r.cle("SOCIETE ED DKHILA"))
        self.assertEqual(r.cle("STRC"), r.cle("STE TUN.RECOUVR. DES CREANCES “STRC”"))
        self.assertEqual(r.cle("STE LA GENERALE DE VENTE"), r.cle("SOCIETE LA GENERALE DES VENTES"))

    def test_alias_bh_bna(self):
        # BH : « SIFIB » = « BH Invest » ; « Obligataire » = « Obligatoire » ; « Assurances » = « Assurance »
        self.assertEqual(r.cle("Société SIFIB"), r.cle("Société BH Invest"))
        self.assertEqual(r.cle("SICAV BH-Obligataire"), r.cle("SICAV BH-Obligatoire"))
        self.assertEqual(r.cle("Assurances SALIM (*)"), r.cle("Assurance SALIM"))
        # BNA : « GENERALE DES VENTES » (individuel) = « GENERALE DE VENTE » (périmètre)
        self.assertEqual(r.cle("GENERALE DES VENTES"), r.cle("GENERALE DE VENTE"))


class ParticipationsTest(unittest.TestCase):
    def test_lit_part_et_provision(self):
        parts = {p["entite"]: p for p in r.participations_stb(PARTICIPATIONS)}
        self.assertEqual(len(parts), 4)
        self.assertAlmostEqual(parts["STRC"]["pct"], 91.93)
        self.assertEqual(parts["STRC"]["net"], 36462)
        # valeur nette nulle = provisionnée à 100 %
        self.assertEqual(parts["SKANES PALACE INTERNATIO"]["net"], 0)
        self.assertEqual(parts["SKANES PALACE INTERNATIO"]["secteur"], "Touristique")


class ParticipationsBHTest(unittest.TestCase):
    def test_brut_prov_net_et_pourcentage(self):
        parts = {p["entite"]: p for p in r.participations_bh(BH_PARTICIPATIONS + BH_FILIALES)}
        self.assertEqual(set(parts), {"BH LEASING", "STIMEC", "Société Moderne de titrisation", "TFB"})
        self.assertEqual(parts["BH LEASING"]["net"], 12371)       # 3e colonne (exercice N), pas la N-1
        self.assertEqual(parts["STIMEC"]["net"], 0)               # provisionnée à 100 %
        self.assertEqual(parts["STIMEC"]["brute"], 420)
        # % de détention récupéré dans la « Liste des entreprises filiales »
        self.assertAlmostEqual(parts["Société Moderne de titrisation"]["pct"], 40.0)
        self.assertIsNone(parts["BH LEASING"]["pct"])            # absente de la liste des filiales


class ParticipationsBNATest(unittest.TestCase):
    def test_pct_et_provision(self):
        parts = {p["entite"]: p for p in r.participations_bna(BNA_PORTEFEUILLE)}
        self.assertEqual(len(parts), 5)                           # le sous-total « Total général » est ignoré
        self.assertAlmostEqual(parts["SICAF Participations"]["pct"], 99.99)
        self.assertEqual(parts["SICAF Participations"]["net"], 500)
        # nette nulle + brute positive = provisionnée à 100 % (SODAL en liquidation, détenue 69 %)
        self.assertEqual(parts["SODAL"]["net"], 0)
        self.assertAlmostEqual(parts["SODAL"]["pct"], 69.01)
        self.assertEqual(parts["GENERALE DES VENTES"]["net"], 1064)


class SommeTest(unittest.TestCase):
    def test_les_sommes_bouclent(self):
        verifs = r.controles_somme(BILAN)
        self.assertEqual(len(verifs), 3)
        self.assertTrue(all(calc == imprime for _, calc, imprime in verifs))

    def test_une_somme_fausse_est_detectee(self):
        faux = BILAN.replace("178 674", "999 999")  # part du groupe trafiquée
        verifs = r.controles_somme(faux)
        self.assertFalse(all(calc == imprime for _, calc, imprime in verifs))

    def test_bilan_bh_code_de_note_et_colonnes_collees(self):
        # le « 12 » (code de note) ne doit pas être pris pour les capitaux propres, et « N N-1 » collés par
        # une seule espace ne doivent pas fusionner
        verifs = r.controles_somme(BH_BILAN)
        self.assertEqual(len(verifs), 2)  # pas de cascade de résultat dans ce bilan BH
        self.assertTrue(all(calc == imprime for _, calc, imprime in verifs))
        self.assertEqual(r.ligne_chiffree(BH_BILAN, "Total des Capitaux propres"), 1184175)

    def test_bilan_bna_libelles_et_minoritaires_negatifs(self):
        # libellés « IM - … » / « …, Part du groupe » et minoritaires du résultat imprimés négatifs
        verifs = r.controles_somme(BNA_BILAN)
        self.assertEqual(len(verifs), 3)
        self.assertTrue(all(calc == imprime for _, calc, imprime in verifs))


class RecoupeTest(unittest.TestCase):
    def test_verdicts(self):
        parts = r.participations_stb(PARTICIPATIONS)
        perim = {r.cle("STE TUN.RECOUVR. DES CREANCES “STRC”"): {"methode": "intégration globale"}}
        lignes = {x["entite"]: x for x in r.recouper(parts, perim)}
        self.assertTrue(lignes["STRC"]["consolidee"])
        # détenue à ~100 %, provisionnée, absente -> exclusion motivée, pas un trou
        self.assertFalse(lignes["SKANES PALACE INTERNATIO"]["consolidee"])
        self.assertIn("provisionnée", lignes["SKANES PALACE INTERNATIO"]["verdict"])
        # détenue à 50 % (pas > 50 %), non consolidée -> ni trou ni exclusion
        self.assertIn("≤ 50", lignes["STE LA GENERALE DE VENTE"]["verdict"])

    def test_verdict_sans_pourcentage(self):
        # participation BH sans % publié mais provisionnée à 100 % et hors périmètre -> exclusion motivée
        parts = [{"secteur": "", "entite": "Société Moderne de titrisation", "pct": None, "brute": 326, "net": 0}]
        verdict = r.recouper(parts, {})[0]["verdict"]
        self.assertIn("provisionnée", verdict)
        # sans % ni provision ni périmètre -> à vérifier, mais jamais qualifié de trou « à expliquer »
        parts = [{"secteur": "", "entite": "X", "pct": None, "brute": 100, "net": 100}]
        self.assertIn("à vérifier", r.recouper(parts, {})[0]["verdict"])


if __name__ == "__main__":
    unittest.main()

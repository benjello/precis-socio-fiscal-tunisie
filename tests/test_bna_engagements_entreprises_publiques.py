"""Tests de `scripts/bna_engagements_entreprises_publiques.py` : sans PDF, sur deux mises en page de la note.

Les extraits sont ceux de `pdftotext -layout` des états de 2017 (une ligne par grandeur, montants négatifs entre
parenthèses, ligne « Classe » à six valeurs) et de 2022 (libellés coupés sur plusieurs lignes, tableau qui passe à la
page suivante).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import bna_engagements_entreprises_publiques as b  # noqa: E402

PAGE_2017 = """                 4.3.7- Engagements des entreprises publiques

Le tableau suivant récapitule les engagements de ces relations au 31 décembre 2017 :


                                                                                           Dont engagements des sociétés
                                               Total des
                                              entreprises
                                                               Office des
                                               publiques
Cadre légal                                                    Céréales          STIR          TUNIS AIR         O.T.D                O.N.H            El Fouledh

Engagements au 31/12/2016                         1 127 547          523 958         58 581          55 300              94 525            60 641             51 104

Engagements au 31/12/2017                         1 359 880          544 357        151 605          52 490             107 650            108 536             52 600

Garanties de l'état au 31/12/2017                  902 390           524 000               -         52 320              98 251            76 202             46 238

Agios et intérêts réservés au 31/12/2017           (19 795)                 -              -               -             (9 246)                   -          (6 362)

Classe au 31/12/2017                                                        0             0                0                  0                    0                4

Provisions au 31/12/2017                                (7)                 -              -               -                   -                   -                -

            4.4-Portefeuille-titres commercial
"""

PAGE_2022_A = """4.3.8- Engagements des entreprises publiques
Le tableau suivant récapitule les engagements de ces relations au 31 décembre 2022 :

                    Total des                                      Dont engagements des sociétés
                    entreprises Office des
                    publiques Céréales             ETAP             TRANSTU       O.T.D             O.N.H             El Fouledh
Cadre légal
Engagements au
                    5 176 212      3 940 881       70 540           94 412        162 221           180 469           94 242
31/12/2021
Engagements au
                    5 945 280      4 768 074       65 383           102 365       189 259           201 704           105 613
31/12/2022
Garanties de
                    5 543 139      4 768 074       -                94 776        188 757           201 704           76 761
l'état au
"""

PAGE_2022_B = """31/12/2022
Autres Garanties
                     111 469       -            65 000           -             502             -            -
au 31/12/2022
Agios et intérêts
réservés au          43 624        -            -                -             -               -            28 852
31/12/2022
Classe au
                     -             0            0                0             0               0            4
31/12/2022
Provisions au
                     12 123        -            -                -             -               -            0
31/12/2022
4.4-        Portefeuille-titres commercial
"""


def cellules(lignes: list[list[str]], annee: str, grandeur: str) -> dict[str, str]:
    return {r[1]: r[3] for r in lignes if r[0] == annee and r[2] == grandeur}


class NombreTest(unittest.TestCase):
    def test_signes_et_tirets(self):
        self.assertEqual(b.nombre("1 127 547"), "1127547")
        self.assertEqual(b.nombre("(19 795)"), "-19795")
        self.assertEqual(b.nombre("-"), "")
        self.assertEqual(b.nombre("0"), "0")

    def test_espace_insecable(self):
        self.assertEqual(b.nombre("5 945 280"), "5945280")


class MiseEnPage2017Test(unittest.TestCase):
    def setUp(self):
        self.lignes = b.releve_pages(2017, [PAGE_2017])

    def test_deux_exercices_dans_un_etat(self):
        self.assertEqual({r[0] for r in self.lignes}, {"2016", "2017"})
        self.assertEqual(len(cellules(self.lignes, "2016", "engagements")), 7)

    def test_colonnes_et_noms(self):
        e = cellules(self.lignes, "2017", "engagements")
        self.assertEqual(
            list(e),
            [
                "Total des entreprises publiques",
                "Office des céréales",
                "STIR",
                "Tunisair",
                "O.T.D",
                "O.N.H",
                "El Fouledh",
            ],
        )
        self.assertEqual(e["O.T.D"], "107650")
        self.assertEqual(e["Total des entreprises publiques"], "1359880")

    def test_tiret_vide_et_parentheses_negatives(self):
        self.assertEqual(
            cellules(self.lignes, "2017", "garanties de l'État")["STIR"], ""
        )
        agios = cellules(self.lignes, "2017", "agios et intérêts réservés")
        self.assertEqual(agios["Total des entreprises publiques"], "-19795")
        self.assertEqual(agios["El Fouledh"], "-6362")
        self.assertEqual(
            cellules(self.lignes, "2017", "provisions")[
                "Total des entreprises publiques"
            ],
            "-7",
        )

    def test_classe_a_six_valeurs_laisse_le_total_vide(self):
        classe = cellules(self.lignes, "2017", "classe de risque")
        self.assertEqual(classe["Total des entreprises publiques"], "")
        self.assertEqual(classe["Office des céréales"], "0")
        self.assertEqual(classe["El Fouledh"], "4")

    def test_page_de_la_ligne(self):
        self.assertEqual({r[4] for r in self.lignes}, {"1"})


class MiseEnPage2022Test(unittest.TestCase):
    def setUp(self):
        self.lignes = b.releve_pages(2022, [PAGE_2022_A, PAGE_2022_B])

    def test_libelles_coupes(self):
        self.assertEqual(
            {r[2] for r in self.lignes if r[0] == "2022"},
            {
                "engagements",
                "garanties de l'État",
                "autres garanties",
                "agios et intérêts réservés",
                "classe de risque",
                "provisions",
            },
        )
        self.assertEqual(
            cellules(self.lignes, "2021", "engagements")["O.N.H"], "180469"
        )

    def test_noms_normalises(self):
        e = cellules(self.lignes, "2022", "engagements")
        self.assertEqual(list(e)[2:4], ["ETAP", "Transtu"])

    def test_valeurs_des_lignes_suivantes(self):
        self.assertEqual(
            cellules(self.lignes, "2022", "autres garanties")["ETAP"], "65000"
        )
        self.assertEqual(
            cellules(self.lignes, "2022", "agios et intérêts réservés")["El Fouledh"],
            "28852",
        )
        self.assertEqual(cellules(self.lignes, "2022", "provisions")["El Fouledh"], "0")
        self.assertEqual(
            cellules(self.lignes, "2022", "garanties de l'État")["ETAP"], ""
        )

    def test_page_ou_commence_chaque_ligne(self):
        pages = {(r[0], r[2]): r[4] for r in self.lignes}
        self.assertEqual(pages[("2022", "engagements")], "1")
        self.assertEqual(pages[("2022", "garanties de l'État")], "1")
        self.assertEqual(pages[("2022", "autres garanties")], "2")
        self.assertEqual(pages[("2022", "provisions")], "2")


if __name__ == "__main__":
    unittest.main()

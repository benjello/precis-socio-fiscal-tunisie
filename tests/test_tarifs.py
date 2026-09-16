"""Le pivot des tarifs relevés : format long -> tableau publié.

Python pur, sans dépendance : la suite tourne `--isolated --no-project`. C'est la raison
pour laquelle `scripts/tarifs.py` n'emploie pandas que dans `dataframe()`, hors du pivot.
"""
import csv
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "scripts"))

import tarifs  # noqa: E402

CSV_REEL = RACINE / "precis/fr/fiscalite/tarifs/tarifs-releves-droits-consommation.csv"


def rang(tableau, ordre, colonne, valeur="", unite="", statut="lu",
         position="", produit="p"):
    return dict(tableau=tableau, ordre=str(ordre), colonne=colonne, valeur=valeur,
                unite=unite, statut=statut, position=position, produit=produit)


class RecomposeTest(unittest.TestCase):
    def test_valeur_et_unite_sont_rejointes(self):
        self.assertEqual(tarifs.recompose("15,228", "D/hl", "lu"), "15,228 D/hl")

    def test_unite_pourcent(self):
        self.assertEqual(tarifs.recompose("11", "%", "lu"), "11 %")

    def test_valeur_sans_unite_ne_laisse_pas_d_espace(self):
        self.assertEqual(tarifs.recompose("11", "", "lu"), "11")

    def test_chaque_sentinelle_retrouve_sa_prose(self):
        for statut, prose in tarifs.PROSE.items():
            self.assertEqual(tarifs.recompose("", "", statut), prose)

    def test_la_valeur_est_ignoree_quand_l_etat_est_une_sentinelle(self):
        # Une valeur résiduelle ne doit jamais ressortir sous un statut d'absence.
        self.assertEqual(tarifs.recompose("99", "D/hl", "non établi"), "*(non établi)*")

    def test_la_correspondance_est_bijective(self):
        # Deux états qui partageraient la même prose rendraient le pivot ambigu.
        self.assertEqual(len(set(tarifs.PROSE.values())), len(tarifs.PROSE))


class PivotTest(unittest.TestCase):
    def test_les_lignes_sortent_dans_l_ordre_d_origine(self):
        rangs = [rang("transfert-2007", 1, "Taux", "10", "%", position="33-04"),
                 rang("transfert-2007", 0, "Taux", "10", "%", position="33-03")]
        self.assertEqual([l[0] for l in tarifs.pivot(rangs, "transfert-2007")],
                         ["33-03", "33-04"])

    def test_une_colonne_absente_reste_vide_et_n_est_pas_inventee(self):
        rangs = [rang("petroliers", 0, "1988", "0,400", "D/hl", position="27-09")]
        ligne = tarifs.pivot(rangs, "petroliers")[0]
        self.assertEqual(ligne[2], "0,400 D/hl")
        self.assertEqual(ligne[3:], ["", "", ""])

    def test_les_rangs_d_un_autre_tableau_sont_ignores(self):
        rangs = [rang("transfert-2007", 0, "Taux", "10", "%"),
                 rang("petroliers", 0, "1988", "0,400", "D/hl")]
        self.assertEqual(len(tarifs.pivot(rangs, "transfert-2007")), 1)

    def test_quatre_eres_donnent_une_seule_ligne(self):
        rangs = [rang("petroliers", 0, c, "1", "D/hl", position="27-10")
                 for c in ("1988", "1991", "1999", "Consolidé 2023")]
        self.assertEqual(len(tarifs.pivot(rangs, "petroliers")), 1)


class MarkdownTest(unittest.TestCase):
    def test_alignement_a_gauche_partout(self):
        # tableau_vers_markdown aligne à droite les colonnes numériques ; les tableaux
        # publiés du chapitre ne le font pas. Le séparateur ne doit porter aucun « : ».
        rangs = [rang("transfert-2007", 0, "Taux", "10", "%", position="33-03")]
        separateur = tarifs.markdown(rangs, "transfert-2007").splitlines()[1]
        self.assertNotIn(":", separateur)
        self.assertEqual(separateur, "|---|---|---|")

    def test_entetes_publies(self):
        rangs = [rang("transfert-2007", 0, "Taux", "10", "%")]
        self.assertEqual(tarifs.markdown(rangs, "transfert-2007").splitlines()[0],
                         "| Position tarifaire | Désignation | Taux |")


class CsvReelTest(unittest.TestCase):
    """Garde-fous sur le fichier versionné lui-même."""

    @classmethod
    def setUpClass(cls):
        if not CSV_REEL.is_file():
            raise unittest.SkipTest("relevé de tarifs absent")
        with CSV_REEL.open(encoding="utf-8", newline="") as f:
            cls.rangs = list(csv.DictReader(f))

    def test_tout_statut_est_connu(self):
        connus = set(tarifs.PROSE) | {"lu", "consolidé"}
        self.assertEqual({r["statut"] for r in self.rangs} - connus, set())

    def test_tout_tableau_est_declare(self):
        self.assertEqual({r["tableau"] for r in self.rangs} - set(tarifs.TABLEAUX), set())

    def test_une_sentinelle_n_a_pas_de_valeur(self):
        for r in self.rangs:
            if r["statut"] in tarifs.PROSE:
                self.assertEqual(r["valeur"], "", r["produit"])

    def test_une_valeur_lue_n_est_jamais_vide(self):
        for r in self.rangs:
            if r["statut"] not in tarifs.PROSE:
                self.assertTrue(r["valeur"], r["produit"])

    def test_chaque_tableau_pivote_sans_trou_inattendu(self):
        for nom in tarifs.TABLEAUX:
            for ligne in tarifs.pivot(self.rangs, nom):
                self.assertEqual([c for c in ligne if c is None], [], nom)


if __name__ == "__main__":
    unittest.main()

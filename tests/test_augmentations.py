"""Le relevé des augmentations : dépliage, formes courtes, infobulles, cumul.

Python pur, sans dépendance : la suite tourne `--isolated --no-project`. C'est pourquoi
`scripts/augmentations.py` n'emploie pandas que dans `dataframe()`, hors de la logique.
"""
import csv
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "scripts"))

import augmentations  # noqa: E402

CSV_REEL = (RACINE / "precis/fr/remunerations_publiques/augmentations"
            / "augmentations-fonction-publique.csv")
CSV_IGE = (RACINE / "precis/fr/remunerations_publiques/augmentations"
           / "augmentations-ige.csv")


def rang(texte="decret2016-1", date="2016-01-01", categorie="A1", montant="60",
         cycle="2015-2018", nature="augmentation générale", statut="lu"):
    return dict(cycle=cycle, texte=texte, nature=nature, date_effet=date,
                categorie=categorie, montant=montant, unite="D/mois", statut=statut)


class FormeCourteTest(unittest.TestCase):
    def test_la_forme_courte_tient_en_une_poignee_de_caracteres(self):
        for cle in augmentations.DECRETS:
            self.assertLessEqual(len(augmentations.court(cle)), 20, cle)

    def test_une_cle_inconnue_est_rendue_telle_quelle(self):
        # Mieux vaut afficher la clé brute qu'inventer un libellé.
        self.assertEqual(augmentations.court("decret-inexistant"), "decret-inexistant")


class InfobulleTest(unittest.TestCase):
    def test_le_span_pandoc_porte_le_titre_complet(self):
        rendu = augmentations.infobulle("decret2020-767")
        self.assertTrue(rendu.startswith("[Décret 2020-767]{title=\""))
        self.assertIn("18 septembre 2020", rendu)
        self.assertTrue(rendu.endswith('"}'))

    def test_aucun_titre_ne_contient_de_guillemet_droit(self):
        # Un guillemet droit dans le titre casserait l'attribut title="…".
        for cle, (_bref, complet) in augmentations.DECRETS.items():
            self.assertNotIn('"', complet, cle)

    def test_le_titre_complet_est_bien_plus_long_que_la_forme_courte(self):
        # C'est la raison d'être de l'infobulle : sinon elle n'apporterait rien.
        for cle, (bref, complet) in augmentations.DECRETS.items():
            self.assertGreater(len(complet), 3 * len(bref), cle)


class FormateDateTest(unittest.TestCase):
    def test_le_premier_du_mois_prend_l_exposant(self):
        self.assertEqual(augmentations.formate_date("2016-07-01"), "1^er^ juillet 2016")

    def test_une_date_absente_ne_devient_pas_une_date_supposee(self):
        self.assertEqual(augmentations.formate_date(""), "—")


class TableauCyclesTest(unittest.TestCase):
    def test_une_ligne_par_cycle(self):
        rangs = [rang(cycle="2015-2018"), rang(cycle="2019-2020", texte="decret2020-767")]
        lignes = augmentations.tableau_cycles(rangs).splitlines()
        self.assertEqual(len(lignes), 4)  # en-tête + séparateur + deux cycles

    def test_la_cellule_porte_la_forme_courte_sans_citation_developpee(self):
        # La citation `[@clé]` est proscrite dans la cellule : le style bibliographique
        # la développe en clair entre parenthèses et y réinjecte le titre officiel.
        rendu = augmentations.tableau_cycles([rang(texte="decret2020-767")])
        self.assertIn("[Décret 2020-767]{title=", rendu)
        self.assertNotIn("[@decret2020-767]", rendu)

    def test_un_montant_unique_ne_devient_pas_une_fourchette(self):
        rendu = augmentations.tableau_cycles([rang(montant="50")])
        self.assertIn("| 50 D |", rendu)

    def test_deux_montants_donnent_une_fourchette(self):
        rangs = [rang(montant="50"), rang(montant="90", categorie="A2")]
        self.assertIn("| 50 à 90 D |", augmentations.tableau_cycles(rangs))


class TableauMontantsTest(unittest.TestCase):
    def test_les_categories_sortent_dans_l_ordre_hierarchique(self):
        rangs = [rang(categorie="D", montant="35"), rang(categorie="A1", montant="60")]
        entete = augmentations.tableau_montants(rangs).splitlines()[0]
        # Chercher « D » nu trouverait le D de « Date d'effet » : on vise la CELLULE.
        self.assertLess(entete.index("| A1 |"), entete.index("| D |"))

    def test_une_categorie_non_visee_reste_vide_et_n_est_pas_comblee(self):
        rangs = [rang(categorie="A1", montant="60"),
                 rang(categorie="D", montant="50", date="2017-01-01")]
        lignes = augmentations.tableau_montants(rangs).splitlines()
        self.assertTrue(lignes[2].endswith("| 60 |  |"))

    def test_les_dates_sortent_en_ordre_chronologique(self):
        rangs = [rang(date="2020-08-01"), rang(date="2016-01-01")]
        lignes = augmentations.tableau_montants(rangs).splitlines()[2:]
        self.assertIn("2016", lignes[0])
        self.assertIn("2020", lignes[1])


class SerieCumuleeTest(unittest.TestCase):
    def test_le_cumul_additionne_les_tranches(self):
        rangs = [rang(date="2016-01-01", montant="60"),
                 rang(date="2017-01-01", montant="60")]
        self.assertEqual(augmentations.serie_cumulee(rangs, "A1"),
                         [("2016-01-01", 60), ("2017-01-01", 120)])

    def test_une_date_sans_montant_pour_la_categorie_reporte_le_cumul(self):
        rangs = [rang(date="2016-01-01", montant="60"),
                 rang(date="2017-01-01", montant="50", categorie="D")]
        self.assertEqual(augmentations.serie_cumulee(rangs, "A1"),
                         [("2016-01-01", 60), ("2017-01-01", 60)])

    def test_une_ligne_sans_date_etablie_est_ecartee(self):
        # Le décret n° 2015-462 n'énonce aucune date : on ne la suppose pas.
        rangs = [rang(date="", montant="50", categorie="tous", statut="date non établie"),
                 rang(date="2016-01-01", montant="60")]
        self.assertEqual(augmentations.serie_cumulee(rangs, "A1"), [("2016-01-01", 60)])


class CsvReelTest(unittest.TestCase):
    """Garde-fous sur le fichier versionné lui-même."""

    @classmethod
    def setUpClass(cls):
        if not CSV_REEL.is_file():
            raise unittest.SkipTest("relevé des augmentations absent")
        with CSV_REEL.open(encoding="utf-8", newline="") as f:
            cls.rangs = list(csv.DictReader(f))

    def test_toute_categorie_est_connue(self):
        self.assertEqual({r["categorie"] for r in self.rangs} - set(augmentations.ORDRE),
                         set())

    def test_tout_decret_a_sa_forme_courte_et_son_titre(self):
        self.assertEqual({r["texte"] for r in self.rangs} - set(augmentations.DECRETS),
                         set())

    def test_tout_montant_est_un_entier_positif(self):
        for r in self.rangs:
            self.assertGreater(int(r["montant"]), 0, r["texte"])

    def test_une_date_vide_porte_le_statut_qui_l_explique(self):
        for r in self.rangs:
            if not r["date_effet"]:
                self.assertEqual(r["statut"], "date non établie", r["texte"])

    def test_une_date_etablie_est_au_format_iso(self):
        for r in self.rangs:
            if r["date_effet"]:
                self.assertRegex(r["date_effet"], r"^\d{4}-\d{2}-\d{2}$")

    def test_aucun_doublon_de_cle_de_ligne(self):
        cles = [(r["texte"], r["date_effet"], r["categorie"]) for r in self.rangs]
        self.assertEqual(len(cles), len(set(cles)))

    def test_les_six_categories_statutaires_sont_couvertes_a_chaque_date(self):
        # Une catégorie qui manquerait à une date trouerait la série cumulée.
        dates = augmentations.dates_presentes(self.rangs)
        for cat in ["A1", "A2", "A3", "B", "C", "D"]:
            vues = {r["date_effet"] for r in self.rangs if r["categorie"] == cat}
            self.assertEqual(set(dates) - vues, set(), cat)


class DemiDinarTest(unittest.TestCase):
    """Les décrets de 2002 à 2007 fixent des demi-dinars : ni troncature, ni « 60.0 »."""

    def test_un_demi_dinar_n_est_pas_tronque(self):
        rendu = augmentations.tableau_montants([rang(montant="25.5")])
        self.assertTrue(rendu.splitlines()[2].endswith("| 25,5 |"))

    def test_un_entier_reste_un_entier(self):
        self.assertEqual(augmentations.affiche(augmentations._montant("60")), "60")

    def test_la_fourchette_porte_la_virgule(self):
        rangs = [rang(montant="13.5"), rang(montant="32", categorie="A2")]
        self.assertIn("| 13,5 à 32 D |", augmentations.tableau_cycles(rangs))


class CsvIgeTest(unittest.TestCase):
    """Le relevé de l'indemnité de gestion et d'exécution, 1993-2013."""

    # Montant global de chaque cycle triennal, tel que l'article 1er ou 2 du premier
    # décret du cycle le fixe (A1 conseiller, A2, B, D, ouvriers de 1re unité). La somme
    # des tranches lues doit le retrouver : c'est le contrôle de lecture des tableaux.
    GLOBAUX = {
        "1993-1995": {"A1 conseiller": 95, "A2": 86, "B": 56, "D": 40, "ouvriers 1re unité": 40},
        "1996-1998": {"A1 conseiller": 90, "A2": 80, "B": 55, "D": 40, "ouvriers 1re unité": 40},
        "1999-2001": {"A1 conseiller": 95, "A2": 85, "B": 60, "D": 45, "ouvriers 1re unité": 45},
        "2002-2004": {"A1 conseiller": 92, "A2": 82.5, "B": 58, "D": 43.5,
                      "ouvriers 1re unité": 43.5},
        "2005-2007": {"A1 conseiller": 92, "A2": 82.5, "B": 58, "D": 43.5,
                      "ouvriers 1re unité": 43.5},
        "2008-2010": {"A1 général": 226, "A1 en chef": 197, "A1 conseiller": 168, "A2": 124,
                      "B": 87, "D": 66, "ouvriers 1re unité": 66},
    }

    @classmethod
    def setUpClass(cls):
        if not CSV_IGE.is_file():
            raise unittest.SkipTest("relevé de l'IGE absent")
        cls.rangs = augmentations.charge(CSV_IGE)

    def test_toute_categorie_est_connue(self):
        self.assertEqual({r["categorie"] for r in self.rangs} - set(augmentations.ORDRE),
                         set())

    def test_tout_decret_a_sa_forme_courte_et_son_titre(self):
        self.assertEqual({r["texte"] for r in self.rangs} - set(augmentations.DECRETS),
                         set())

    def test_les_tranches_retrouvent_le_montant_global_du_cycle(self):
        for cycle, globaux in self.GLOBAUX.items():
            for cat, attendu in globaux.items():
                somme = sum(float(r["montant"]) for r in self.rangs
                            if r["cycle"] == cycle and r["categorie"] == cat)
                self.assertEqual(somme, attendu, (cycle, cat))

    def test_toute_ligne_a_une_date_d_effet(self):
        for r in self.rangs:
            self.assertRegex(r["date_effet"], r"^\d{4}-\d{2}-\d{2}$")


if __name__ == "__main__":
    unittest.main()

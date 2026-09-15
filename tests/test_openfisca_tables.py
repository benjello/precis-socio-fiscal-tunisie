"""Tests des fonctions qui décident quelle valeur du droit s'applique à quelle date.

C'est le risque le plus lourd du dépôt : ces fonctions alimentent les tableaux de
paramètres publiés, c'est-à-dire du **droit chiffré**. Une erreur n'y produit pas un
plantage mais un tableau plausible et faux — un montant, un taux ou une date d'effet
que personne ne peut distinguer du vrai sans retourner au Journal officiel.

Ne sont couvertes ici que les fonctions PURES. `bareme_a_la_date` en est exclue : elle
appelle `charge_parametre()`, donc lit dans le paquet openfisca, et n'est pas testable
sans lui.
"""

import datetime
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from openfisca_tables import (  # noqa: E402
    _annee,
    taux_effectifs_limite_superieure,
    valeur_a_la_date,
)


class AnneeTest(unittest.TestCase):
    """Les clés de paramètres sont tantôt des dates, tantôt des chaînes."""

    def test_objet_date(self):
        self.assertEqual(_annee(datetime.date(1987, 6, 3)), 1987)

    def test_chaine_iso(self):
        self.assertEqual(_annee("2014-01-01"), 2014)

    def test_chaine_annee_seule(self):
        self.assertEqual(_annee("1999"), 1999)


class ValeurALaDateTest(unittest.TestCase):
    BLOC = {
        "1987-01-01": {"value": 7.7},
        "2000-01-01": {"value": 36.3},
        "2015-01-01": {"value": 150.0},
    }

    def test_bloc_vide_ou_absent(self):
        self.assertIsNone(valeur_a_la_date(None, datetime.date(2015, 1, 1)))
        self.assertIsNone(valeur_a_la_date({}, datetime.date(2015, 1, 1)))

    def test_valeur_en_vigueur(self):
        self.assertEqual(valeur_a_la_date(self.BLOC, datetime.date(2010, 6, 1)), 36.3)

    def test_dernier_palier_se_prolonge(self):
        self.assertEqual(valeur_a_la_date(self.BLOC, datetime.date(2026, 1, 1)), 150.0)

    def test_avant_le_premier_palier(self):
        """Aucune valeur n'existe encore : None, et non la plus ancienne."""
        self.assertIsNone(valeur_a_la_date(self.BLOC, datetime.date(1980, 1, 1)))

    def test_valeur_brute_sans_dictionnaire(self):
        """Certains paramètres portent le nombre directement."""
        self.assertEqual(valeur_a_la_date({"2010-01-01": 42}, datetime.date(2012, 1, 1)),
                         42.0)


class ParametreAbrogeTest(unittest.TestCase):
    """`value: null` signifie que le paramètre CESSE d'exister à cette date.

    On ne remonte alors pas au palier antérieur : c'est ce qui permet à une tranche de
    barème de disparaître. Une « correction » qui chercherait la dernière valeur non
    nulle ressusciterait des tranches abrogées — et republierait du droit abrogé.
    """

    BLOC = {"1990-01-01": {"value": 0.35}, "2017-01-01": {"value": None}}

    def test_avant_abrogation(self):
        self.assertEqual(valeur_a_la_date(self.BLOC, datetime.date(2016, 1, 1)), 0.35)

    def test_apres_abrogation_ne_remonte_pas(self):
        self.assertIsNone(valeur_a_la_date(self.BLOC, datetime.date(2020, 1, 1)))

    def test_cle_portant_None_directement(self):
        bloc = {"1990-01-01": {"value": 0.35}, "2017-01-01": None}
        self.assertIsNone(valeur_a_la_date(bloc, datetime.date(2020, 1, 1)))


class ComparaisonParDateTest(unittest.TestCase):
    """La comparaison porte sur la DATE COMPLÈTE (#215).

    Elle ne portait que sur l'année : un palier daté du 1er juillet s'appliquait dès
    janvier, alors qu'il n'était pas encore en vigueur. Le cas du PNAFN — 53,333 D au
    1er janvier 2009, 56,666 D au 1er juillet — en est l'illustration réelle.

    Ces tests étaient écrits à l'envers ; ils figeaient l'ancien comportement pour
    qu'on le change en connaissance de cause. C'est fait.
    """

    BLOC = {"2009-01-01": {"value": 53.3}, "2009-07-01": {"value": 56.6}}

    def test_un_palier_de_juillet_ne_vaut_pas_des_janvier(self):
        self.assertEqual(valeur_a_la_date(self.BLOC, datetime.date(2009, 1, 1)), 53.3)

    def test_la_veille_du_palier(self):
        self.assertEqual(valeur_a_la_date(self.BLOC, datetime.date(2009, 6, 30)), 53.3)

    def test_le_jour_meme_du_palier(self):
        """La date d'effet est incluse : le palier vaut dès son premier jour."""
        self.assertEqual(valeur_a_la_date(self.BLOC, datetime.date(2009, 7, 1)), 56.6)

    def test_apres_le_palier(self):
        self.assertEqual(valeur_a_la_date(self.BLOC, datetime.date(2009, 8, 1)), 56.6)

    def test_cle_en_objet_date(self):
        """PyYAML rend les dates en objets `date` : les deux formes doivent coïncider."""
        bloc = {datetime.date(2009, 1, 1): {"value": 53.3},
                datetime.date(2009, 7, 1): {"value": 56.6}}
        self.assertEqual(valeur_a_la_date(bloc, datetime.date(2009, 1, 1)), 53.3)


class TauxEffectifsTest(unittest.TestCase):
    """Troisième colonne des barèmes publiés au JORT jusqu'en 1990, recalculée ici.

    Elle n'existe pas dans openfisca : si ce calcul dérive, le précis publie une colonne
    fausse que rien ne recoupe.
    """

    def test_bareme_a_trois_tranches(self):
        tranches = [(0.0, 0.0), (1000.0, 0.15), (2000.0, 0.20)]
        # 1re : (1000-0)×0 = 0, rapporté à 1000 -> 0
        # 2e  : cumul 0 + (2000-1000)×0,15 = 150, rapporté à 2000 -> 0,075
        # 3e  : tranche ouverte -> pas de limite supérieure
        self.assertEqual(taux_effectifs_limite_superieure(tranches),
                         [0.0, 0.075, None])

    def test_derniere_tranche_toujours_None(self):
        """La dernière tranche est ouverte : elle n'a pas de limite supérieure."""
        resultats = taux_effectifs_limite_superieure([(0.0, 0.10), (500.0, 0.20)])
        self.assertIsNone(resultats[-1])

    def test_liste_vide(self):
        self.assertEqual(taux_effectifs_limite_superieure([]), [])

    def test_limite_nulle_ne_divise_pas_par_zero(self):
        """Garde-fou : deux seuils identiques donneraient une division par zéro."""
        self.assertEqual(taux_effectifs_limite_superieure([(0.0, 0.10), (0.0, 0.20)]),
                         [0.0, None])


if __name__ == "__main__":
    unittest.main()

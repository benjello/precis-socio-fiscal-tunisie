"""Tests de `restore_locators` — la fonction qui remet les locateurs de citation.

Le contenu qui suit la virgule dans `[@ref, art. 13]` est de la SYNTAXE de citation,
pas de la prose : il doit traverser la traduction intact. Le modèle le traduit malgré
la consigne — « art. 5 à 7 » devient « art. 5 إلى 7 » —, et c'est assez mécanique pour
être défait ici plutôt que renégocié à chaque passe.

Comme `restore_urls`, cette fonction réécrit du contenu publié. Elle est plus délicate
encore : sa règle de prudence compare les clés ET leur ordre, et sa restauration est
POSITIONNELLE — le générateur de locateurs est consommé à chaque correspondance, y
compris celles qu'on ne remplace pas. Cet alignement est invisible à la lecture ; ces
tests le verrouillent.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from translate_sync import restore_locators  # noqa: E402

AR = "إلى"  # « à », le mot qui apparaît quand le modèle traduit un intervalle


class RestaurationTest(unittest.TestCase):
    def test_locateur_traduit_est_restaure(self):
        source = "Texte [@loi-83-112, art. 5 à 7] ici.\n"
        traduit = "نصّ [@loi-83-112, art. 5 " + AR + " 7] هنا.\n"
        self.assertEqual(restore_locators(source, traduit),
                         "نصّ [@loi-83-112, art. 5 à 7] هنا.\n")

    def test_seule_la_citation_traduite_est_restauree(self):
        """Les autres gardent leur forme : on ne réécrit que ce qui a été abîmé."""
        source = "A [@a-1, art. 2] et B [@b-2, art. 3 à 4].\n"
        traduit = "أ [@a-1, art. 2] و ب [@b-2, art. 3 " + AR + " 4].\n"
        self.assertEqual(restore_locators(source, traduit),
                         "أ [@a-1, art. 2] و ب [@b-2, art. 3 à 4].\n")

    def test_meme_cle_deux_fois_restauration_positionnelle(self):
        """La correspondance est POSITIONNELLE, pas par clé.

        Deux citations de la même référence portant des locateurs différents doivent
        recevoir chacune le sien, dans l'ordre. Une restauration par clé les
        confondrait — et attacherait le mauvais article à la bonne loi.
        """
        source = "D'abord [@loi-83-112, art. 5] puis [@loi-83-112, art. 9 à 11].\n"
        traduit = ("أولاً [@loi-83-112, art. 5 " + AR + " 5] "
                   "ثم [@loi-83-112, art. 9 " + AR + " 11].\n")
        attendu = "أولاً [@loi-83-112, art. 5] ثم [@loi-83-112, art. 9 à 11].\n"
        self.assertEqual(restore_locators(source, traduit), attendu)


class AbstentionTest(unittest.TestCase):
    """La correspondance un-à-un n'est pas établie : on ne touche à rien.

    Le contrôle de parité signalera l'écart. Mieux vaut une divergence visible qu'un
    locateur recopié au mauvais endroit.
    """

    def test_nombre_de_citations_different(self):
        source = "A [@a-1, art. 2] et B [@b-2, art. 3].\n"
        traduit = "أ [@a-1, art. 2 " + AR + " 3].\n"
        self.assertEqual(restore_locators(source, traduit), traduit)

    def test_ordre_des_cles_different(self):
        source = "A [@a-1, art. 2] et B [@b-2, art. 3].\n"
        traduit = "ب [@b-2, art. 3 " + AR + " 4] و أ [@a-1, art. 2].\n"
        self.assertEqual(restore_locators(source, traduit), traduit)


class PérimètreTest(unittest.TestCase):
    """Ce que la fonction ne prétend PAS faire — figé pour éviter la surprise."""

    def test_locateur_altere_en_francais_reste_tel_quel(self):
        """Elle ne répare que les locateurs TRADUITS, repérés à l'écriture arabe.

        Un locateur altéré sans être traduit — « art. 5 » devenu « art. 6 » — passe au
        travers. C'est le périmètre choisi, pas un oubli : sans marqueur arabe, rien ne
        distingue une altération d'une correction légitime. Le contrôle de parité, lui,
        compare les clés, non les locateurs.
        """
        source = "Texte [@loi-83-112, art. 5] ici.\n"
        traduit = "نصّ [@loi-83-112, art. 6] هنا.\n"
        self.assertEqual(restore_locators(source, traduit), traduit)

    def test_citation_sans_locateur_est_ignoree(self):
        """`[@cle]` sans virgule ne porte pas de locateur : hors sujet."""
        source = "Texte [@loi-83-112] ici.\n"
        traduit = "نصّ [@loi-83-112] هنا.\n"
        self.assertEqual(restore_locators(source, traduit), traduit)

    def test_texte_sans_citation_inchange(self):
        source = "Texte sans citation.\n"
        traduit = "نصّ بلا استشهاد.\n"
        self.assertEqual(restore_locators(source, traduit), traduit)


if __name__ == "__main__":
    unittest.main()

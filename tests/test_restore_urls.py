"""Tests de `restore_urls` — la fonction qui remet les URL abîmées par le modèle.

Pourquoi ces tests existent : le 14 septembre 2026, le CHANGELOG arabe est revenu
corrompu CINQ fois dans la même journée, toujours dans du texte non traduisible —
« github.enjello » (trois fois), « github.Bcom », un domaine remplacé par la date
du jour, le segment « benjello/ » disparu, et une passe où ~150 URL sur 195
étaient réécrites d'un coup. Chacune a coûté une réparation à la main.

`restore_urls` recopie les URL depuis la source après traduction. Elle réécrit donc
du contenu publié : une erreur y attacherait silencieusement une URL au mauvais
texte. Les trois cas d'ABSTENTION comptent autant que les cas de réparation.
"""

import io
import contextlib
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from translate_sync import restore_urls  # noqa: E402

B = "https://github.com/benjello/precis-socio-fiscal-tunisie"
U1 = B + "/commit/aaa"
U2 = B + "/issues/1"
U3 = B + "/compare/v1.0.0...v1.1.0"
SOURCE = "* correctif ([abc](" + U1 + ")), closes [#1](" + U2 + ")\nVoir [v1](" + U3 + ")\n"


def run(source, traduction):
    """Renvoie (texte restauré, trace journalisée)."""
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        resultat = restore_urls(source, traduction)
    return resultat, tampon.getvalue().strip()


class RestaurationTest(unittest.TestCase):
    """Le modèle a abîmé des URL : elles doivent revenir à l'identique."""

    def test_une_url_corrompue(self):
        abime = SOURCE.replace(U1, U1.replace("github.com/benjello", "github.enjello"))
        resultat, trace = run(SOURCE, abime)
        self.assertEqual(resultat, SOURCE)
        self.assertIn("1 sur 3", trace)

    def test_toutes_les_urls_corrompues(self):
        # La forme observée le 14/09/2026 : ~150 URL réécrites en une passe.
        abime = SOURCE.replace("github.com/benjello", "github.enjello")
        resultat, trace = run(SOURCE, abime)
        self.assertEqual(resultat, SOURCE)
        self.assertIn("3 sur 3", trace)


class AbstentionTest(unittest.TestCase):
    """Le nombre d'URL diffère : la correspondance un-à-un n'est pas établie.

    On ne touche à RIEN — une URL restaurée au mauvais endroit serait pire que la
    corruption qu'elle prétend défaire — et on le DIT, faute de quoi on croirait la
    traduction examinée alors qu'elle ne l'a pas été.
    """

    def test_url_disparue(self):
        manque = SOURCE.replace("Voir [v1](" + U3 + ")", "Voir v1")
        resultat, trace = run(SOURCE, manque)
        self.assertEqual(resultat, manque)
        self.assertIn("correspondance non établie", trace)

    def test_url_ajoutee(self):
        ajout = SOURCE.replace("Voir [v1](", "Voir [v0](" + B + "/x) et [v1](")
        resultat, trace = run(SOURCE, ajout)
        self.assertEqual(resultat, ajout)
        self.assertIn("correspondance non établie", trace)


class SilenceTest(unittest.TestCase):
    """Rien à faire : la fonction se tait.

    Une trace à chaque passe rendrait le journal illisible, et un journal qu'on ne
    lit plus ne garde rien.
    """

    def test_traduction_saine(self):
        resultat, trace = run(SOURCE, SOURCE)
        self.assertEqual(resultat, SOURCE)
        self.assertEqual(trace, "")

    def test_prose_arabe_urls_intactes(self):
        arabe = "نصّ [x](" + U1 + ") ونصّ [y](" + U2 + ") و [z](" + U3 + ")\n"
        resultat, trace = run(arabe, arabe)
        self.assertEqual(resultat, arabe)
        self.assertEqual(trace, "")


class LimiteConnueTest(unittest.TestCase):
    """La restauration est POSITIONNELLE : elle ne contrôle que le nombre.

    Si la traduction réordonnait les URL sans en changer le nombre, la fonction leur
    réimposerait l'ordre de la source. C'est accepté — l'ordre des URL suit celui de
    la prose, que le modèle met à jour sans réorganiser — mais ce test fige le
    comportement : c'est le premier endroit à regarder si une URL se retrouve un
    jour attachée au mauvais texte.
    """

    def test_reordonnee_reprend_l_ordre_de_la_source(self):
        reordonne = ("* correctif ([abc](" + U2 + ")), closes [#1](" + U1 + ")\n"
                     "Voir [v1](" + U3 + ")\n")
        resultat, trace = run(SOURCE, reordonne)
        self.assertEqual(resultat, SOURCE)
        self.assertIn("2 sur 3", trace)


if __name__ == "__main__":
    unittest.main()

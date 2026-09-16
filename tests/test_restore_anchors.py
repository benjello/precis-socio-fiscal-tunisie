"""Tests de `restore_anchors` — la fonction qui remet les ancres fléchies par le modèle.

Pourquoi ces tests existent : le 16 septembre 2026, la passe de traduction du chapitre
des droits de consommation a mis une cible de lien au PLURIEL — `#g-entrepositaire`
devenu `#g-entrepositaires`, qui n'est ancré nulle part. Le renvoi arabe ne pointait
plus sur rien. Le contrôle de parité a bloqué la PR #255, et le correctif manuel était
éphémère : la régénération suivante pouvait refléchir la même ancre.

`restore_anchors` réécrit du contenu publié : une erreur y attacherait silencieusement
un nom à la mauvaise ancre. Les cas d'ABSTENTION comptent donc autant que les cas de
réparation — et il y en a deux, l'un sur le nombre, l'autre sur la forme.
"""

import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from translate_sync import restore_anchors  # noqa: E402

SOURCE = (
    "Voir le [droit de consommation](#g-droit-de-consommation) et les\n"
    "[entrepositaires](#g-entrepositaire).\n\n"
    ": Tarif des produits pétroliers {#tbl-dc-petroliers}\n"
)


def run(source, traduction):
    """Renvoie (texte restauré, trace journalisée)."""
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        resultat = restore_anchors(source, traduction)
    return resultat, tampon.getvalue().strip()


class RestaurationTest(unittest.TestCase):
    """Le modèle a fléchi une ancre : elle doit revenir à l'identique."""

    def test_le_defaut_observe_le_16_septembre(self):
        abime = SOURCE.replace("#g-entrepositaire)", "#g-entrepositaires)")
        resultat, trace = run(SOURCE, abime)
        self.assertEqual(resultat, SOURCE)
        self.assertIn("1 sur 3", trace)

    def test_une_definition_d_ancre_flechie(self):
        abime = SOURCE.replace("{#tbl-dc-petroliers}", "{#tbl-dc-petrolier}")
        resultat, trace = run(SOURCE, abime)
        self.assertEqual(resultat, SOURCE)
        self.assertIn("1 sur 3", trace)

    def test_toutes_les_ancres_abimees(self):
        abime = (SOURCE.replace("#g-droit-de-consommation", "#g-droits-de-consommation")
                       .replace("#g-entrepositaire)", "#g-entrepositaires)")
                       .replace("{#tbl-dc-petroliers}", "{#tbl-dc-petrolier}"))
        resultat, trace = run(SOURCE, abime)
        self.assertEqual(resultat, SOURCE)
        self.assertIn("3 sur 3", trace)

    def test_la_prose_traduite_est_preservee(self):
        # La fonction ne touche qu'aux ancres : le texte autour reste celui de la cible.
        traduit = SOURCE.replace("Voir le", "انظر").replace(
            "#g-entrepositaire)", "#g-entrepositaires)")
        resultat, _ = run(SOURCE, traduit)
        self.assertIn("انظر", resultat)
        self.assertIn("#g-entrepositaire)", resultat)
        self.assertNotIn("#g-entrepositaires", resultat)


class AbstentionTest(unittest.TestCase):
    """Deux cas où la correspondance n'est pas établie : on ne touche à RIEN.

    Une ancre restaurée au mauvais endroit serait pire que le fléchissement qu'elle
    prétend défaire. Et l'abstention se DIT, faute de quoi on croirait la passe saine.
    """

    def test_ancre_en_moins_dans_la_traduction(self):
        abime = SOURCE.replace("[entrepositaires](#g-entrepositaire)", "entrepositaires")
        resultat, trace = run(SOURCE, abime)
        self.assertEqual(resultat, abime)
        self.assertIn("correspondance non établie", trace)

    def test_ancre_en_trop_dans_la_traduction(self):
        abime = SOURCE + "Encore [un lien](#g-assujetti).\n"
        resultat, trace = run(SOURCE, abime)
        self.assertEqual(resultat, abime)
        self.assertIn("correspondance non établie", trace)

    def test_une_definition_devenue_lien(self):
        # Même nombre d'ancres, mais la forme a changé : restaurer positionnellement
        # attacherait un nom à la mauvaise structure.
        abime = SOURCE.replace(": Tarif des produits pétroliers {#tbl-dc-petroliers}",
                               "Voir le [tarif](#tbl-dc-petroliers)")
        resultat, trace = run(SOURCE, abime)
        self.assertEqual(resultat, abime)
        self.assertIn("ne correspondent pas", trace)


class SilenceTest(unittest.TestCase):
    """Rien n'a bougé : la fonction ne dit rien et ne touche à rien.

    Une fonction bavarde à vide noie ses propres signaux utiles dans le journal.
    """

    def test_aucune_ancre_abimee(self):
        resultat, trace = run(SOURCE, SOURCE)
        self.assertEqual(resultat, SOURCE)
        self.assertEqual(trace, "")

    def test_texte_sans_aucune_ancre(self):
        resultat, trace = run("Du texte sans ancre.\n", "نص بلا مرساة.\n")
        self.assertEqual(resultat, "نص بلا مرساة.\n")
        self.assertEqual(trace, "")


if __name__ == "__main__":
    unittest.main()

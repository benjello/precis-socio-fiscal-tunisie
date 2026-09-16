"""Tests du saut de ligne final des fichiers écrits par la traduction.

Un caractère, et une classe entière de fausses PR. La passe écrivait la réponse du
modèle telle quelle, sans saut de ligne terminal, alors que les sources françaises en
portent un. Conséquence : toute modification d'un chapitre français régénérait une PR
`auto-translate` dont le diff se réduisait à « +1/-1 » sur la dernière ligne.

Le 16/09/2026, #246 : la dernière ligne de `precis/ar/fiscalite/_tva.qmd` faisait 217
caractères des deux côtés, identique octet pour octet. La PR ne retirait qu'un
caractère — mais elle touchait un vrai fichier, sur une branche attendue, et
ressemblait à une mise à jour légitime. Le piège n'est pas qu'elle casse quelque
chose : c'est qu'elle invite à être fusionnée, et qu'il faut la mesurer pour savoir
qu'elle ne dit rien.

Mesuré le même jour : 9 fichiers arabes sur 24 étaient dans ce cas, contre 1 sur 23
côté français. L'asymétrie est la signature de la passe, non du hasard.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from translate_sync import texte_a_ecrire  # noqa: E402


class SautFinalTest(unittest.TestCase):
    """Le cas de la règle : ce que rend le modèle n'a pas de saut final."""

    def test_saut_ajoute_quand_il_manque(self):
        self.assertEqual(texte_a_ecrire("dernière ligne"), "dernière ligne\n")

    def test_saut_conserve_quand_il_est_deja_la(self):
        self.assertEqual(texte_a_ecrire("dernière ligne\n"), "dernière ligne\n")

    def test_plusieurs_sauts_ramenes_a_un(self):
        """Sinon le correctif remplacerait une divergence par une autre."""
        self.assertEqual(texte_a_ecrire("dernière ligne\n\n\n"), "dernière ligne\n")


class ContenuPreserveTest(unittest.TestCase):
    """La fonction touche à la FIN du texte, à rien d'autre."""

    def test_le_texte_n_est_pas_modifie(self):
        texte = "# Titre\n\nUn paragraphe.\n\n## Sous-titre\n\nUn autre."
        self.assertEqual(texte_a_ecrire(texte), texte + "\n")

    def test_les_sauts_internes_survivent(self):
        texte = "un\n\n\ndeux"
        self.assertEqual(texte_a_ecrire(texte), "un\n\n\ndeux\n")

    def test_l_arabe_passe_intact(self):
        texte = "الأداء على القيمة المضافة"
        self.assertEqual(texte_a_ecrire(texte), texte + "\n")


class CasReelTest(unittest.TestCase):
    """#246, reconstituée : le contenu est identique, seul le saut final diffère."""

    def test_pr_246_ne_serait_plus_ouverte(self):
        ligne = "x" * 217
        avec_saut = ligne + "\n"
        sans_saut = ligne
        # Les deux versions ne différaient que par là. Après le correctif, la passe
        # écrit la même chose que ce qui est déjà sur master : diff vide, pas de PR.
        self.assertEqual(texte_a_ecrire(sans_saut), avec_saut)
        self.assertEqual(texte_a_ecrire(avec_saut), avec_saut)


class IdempotenceTest(unittest.TestCase):
    """Appliquer deux fois ne doit pas dériver : c'est ce qui garantit qu'une passe
    suivante sur un fichier déjà corrigé ne rouvre pas une PR."""

    def test_deux_applications_donnent_le_meme_resultat(self):
        for texte in ("a", "a\n", "a\n\n", "# Titre\nfin"):
            with self.subTest(texte=texte):
                une = texte_a_ecrire(texte)
                self.assertEqual(texte_a_ecrire(une), une)


class CasDegeneresTest(unittest.TestCase):
    def test_chaine_vide_reste_vide(self):
        """Un fichier vide ne doit pas gagner une ligne : il n'y a rien à terminer."""
        self.assertEqual(texte_a_ecrire(""), "")

    def test_valeur_absente_rendue_telle_quelle(self):
        self.assertIsNone(texte_a_ecrire(None))

    def test_texte_fait_de_sauts_seuls(self):
        self.assertEqual(texte_a_ecrire("\n\n\n"), "\n")


if __name__ == "__main__":
    unittest.main()

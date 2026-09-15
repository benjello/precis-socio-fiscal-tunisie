"""Tests du garde « le précis ne parle pas du modèle ».

Invariant éditorial : le texte publié expose le DROIT, jamais l'outil qui le code.
Une mention d'openfisca dans la prose est une fuite visible par le lecteur.

Ce garde est délicat pour une raison inhabituelle : il doit **sous-détecter**. Le mot
« modèle » a des emplois parfaitement légitimes en droit — « le modèle français de
carrière », « le modèle de score de l'AMEN » —, et la première version du contrôle les
signalait tous les trois. D'où le choix, assumé dans le code, de s'en tenir à des
collocations sans ambiguïté : « mieux vaut un contrôle qu'on croit qu'un contrôle qui
crie ». Les tests d'exclusion comptent donc autant que ceux de détection.

Second point non évident : `lignes_rendues` saute les blocs de code ET les commentaires
HTML. Ce n'est pas un détail d'implémentation mais l'application d'une convention du
dépôt — les TODO concernant le modèle se cachent précisément dans ces commentaires. Si
ce comportement se perdait, la convention deviendrait inapplicable.
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from check_pas_de_modele import controle, lignes_rendues  # noqa: E402


class FichierTemporaire(unittest.TestCase):
    """Écrit un .qmd jetable : ces deux fonctions lisent le disque."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        self._tmp.cleanup()

    def ecrire(self, texte):
        chemin = Path(self._tmp.name) / "chapitre.qmd"
        chemin.write_text(texte, encoding="utf-8")
        return chemin


class LignesRenduesTest(FichierTemporaire):
    def test_numerotation_a_partir_de_un(self):
        chemin = self.ecrire("premiere\ndeuxieme\n")
        self.assertEqual(list(lignes_rendues(chemin)),
                         [(1, "premiere"), (2, "deuxieme")])

    def test_bloc_de_code_saute_delimiteurs_compris(self):
        chemin = self.ecrire("avant\n```python\nimport openfisca\n```\napres\n")
        rendues = [ligne for _, ligne in lignes_rendues(chemin)]
        self.assertEqual(rendues, ["avant", "apres"])

    def test_commentaire_html_sur_une_ligne(self):
        chemin = self.ecrire("avant\n<!-- note interne -->\napres\n")
        self.assertEqual([l for _, l in lignes_rendues(chemin)], ["avant", "apres"])

    def test_commentaire_html_sur_plusieurs_lignes(self):
        chemin = self.ecrire("avant\n<!-- debut\nmilieu\nfin -->\napres\n")
        self.assertEqual([l for _, l in lignes_rendues(chemin)], ["avant", "apres"])

    def test_ligne_mixte_entierement_sautee(self):
        """Subtilité invisible à la lecture : la prose VISIBLE d'une telle ligne
        échappe au contrôle, le commentaire s'ouvrant sur la même ligne."""
        chemin = self.ecrire("Texte visible <!-- puis un commentaire\nfin -->\napres\n")
        self.assertEqual([l for _, l in lignes_rendues(chemin)], ["apres"])


class DetectionTest(FichierTemporaire):
    """Ce que le garde DOIT signaler."""

    def test_nom_du_modele_dans_la_prose(self):
        fautes = controle(self.ecrire("Le paramètre est encodé dans openfisca.\n"))
        self.assertEqual(len(fautes), 1)
        numero, quoi, _ = fautes[0]
        self.assertEqual(numero, 1)
        self.assertIn("nom du modèle", quoi)

    def test_collocation_parametres_du_modele(self):
        fautes = controle(self.ecrire("Les paramètres du modèle retiennent 60 %.\n"))
        self.assertEqual(len(fautes), 1)
        self.assertIn("modèle", fautes[0][1])

    def test_collocation_selon_le_modele(self):
        self.assertEqual(len(controle(self.ecrire("Selon le modèle, la règle change.\n"))), 1)

    def test_une_seule_faute_par_ligne(self):
        """`controle` s'arrête au premier motif : une ligne ne compte qu'une fois."""
        chemin = self.ecrire("Dans openfisca, les paramètres du modèle changent.\n")
        self.assertEqual(len(controle(chemin)), 1)

    def test_numero_de_ligne_exact(self):
        chemin = self.ecrire("propre\npropre\nmention d'openfisca ici\n")
        self.assertEqual(controle(chemin)[0][0], 3)


class ExclusionTest(FichierTemporaire):
    """Ce que le garde ne doit PAS signaler — aussi important que la détection."""

    def test_openfisca_dans_un_bloc_de_code(self):
        chemin = self.ecrire("prose\n```python\nimport openfisca_tunisia\n```\n")
        self.assertEqual(controle(chemin), [])

    def test_openfisca_dans_un_commentaire_html(self):
        """La convention du dépôt : les TODO sur le modèle vivent en commentaire."""
        chemin = self.ecrire("prose\n<!-- TODO : vérifier openfisca -->\n")
        self.assertEqual(controle(chemin), [])

    def test_modele_francais(self):
        self.assertEqual(controle(self.ecrire("Dans le modèle français de carrière.\n")), [])

    def test_modele_de_score(self):
        self.assertEqual(controle(self.ecrire("Selon le modèle de score de l'AMEN.\n")), [])

    def test_modele_de_la_declaration(self):
        self.assertEqual(controle(self.ecrire("D'après le modèle de la déclaration.\n")), [])

    def test_texte_sans_mention(self):
        self.assertEqual(controle(self.ecrire("Le décret fixe le taux à 5 %.\n")), [])


if __name__ == "__main__":
    unittest.main()

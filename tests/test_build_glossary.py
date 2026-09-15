"""Tests du générateur de glossaire bilingue.

Ce module produit **huit fichiers publiés** — un `_glossaire.qmd` par livre et par
langue — et porte le verrou qui empêche qu'une notion arrive à moitié traduite dans
le texte rendu. Ses fonctions ne décident pas du droit, mais de ce que lisent les
lecteurs des deux versions.

Deux mécanismes méritaient des tests avant tout autre :

  - `validate`, qui distingue ce qui BLOQUE de ce qui AVERTIT. Confondre les deux
    laisse passer une entrée incomplète, ou fait échouer la CI sur un détail ;
  - `ancres_utilisees`, qui lit DEUX sources. N'avoir lu que les `.qmd` a coûté trois
    notions au livre « Retraites » — « Cadres actifs », « Fonctions astreignantes »,
    « Travaux pénibles et insalubres » — passées de la prose à l'en-tête d'un tableau
    engendré : l'annexe a cessé de les définir pendant que le chapitre continuait d'y
    renvoyer, et trois liens morts sont partis en production.
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import build_glossary  # noqa: E402
from build_glossary import ancres_utilisees, cite, clean, validate  # noqa: E402


class CiteTest(unittest.TestCase):
    """Quatre formes de source canonique, plus un retour muet."""

    def test_source_absente(self):
        self.assertIsNone(cite(None))
        self.assertIsNone(cite(""))

    def test_chaine_simple(self):
        self.assertEqual(cite("loi-83-112"), "[@loi-83-112]")

    def test_dictionnaire_avec_reference_seule(self):
        self.assertEqual(cite({"ref": "loi-83-112"}), "[@loi-83-112]")

    def test_dictionnaire_avec_locateur(self):
        self.assertEqual(cite({"ref": "loi-83-112", "locator": "art. 5"}),
                         "[@loi-83-112, art. 5]")

    def test_dictionnaire_sans_reference_rend_None_silencieusement(self):
        """Cas piège : la citation DISPARAÎT du glossaire publié sans rien signaler.

        Figé ici pour que le jour où l'on veut une alerte, on sache qu'il faut la
        créer — et non croire qu'elle existe déjà.
        """
        self.assertIsNone(cite({"locator": "art. 5"}))


class CleanTest(unittest.TestCase):
    def test_espaces_reduits(self):
        self.assertEqual(clean("  un   texte \n  sur deux lignes "),
                         "un texte sur deux lignes")

    def test_valeur_absente(self):
        self.assertEqual(clean(None), "")


def entree(eid, fr_terme="Terme", ar_terme="مصطلح", **extra):
    e = {"id": eid, "fr": {"terme": fr_terme}, "ar": {"terme": ar_terme}}
    e.update(extra)
    return e


class ValidateTest(unittest.TestCase):
    """Le verrou de synchro FR/AR : ce qui bloque, et ce qui ne fait qu'avertir."""

    def test_entree_conforme(self):
        erreurs, avertissements = validate([entree("pib")])
        self.assertEqual(erreurs, [])
        self.assertEqual(avertissements, [])

    def test_terme_francais_manquant(self):
        erreurs, _ = validate([entree("pib", fr_terme="")])
        self.assertTrue(any("pib" in e and "FR" in e for e in erreurs), erreurs)

    def test_terme_arabe_manquant(self):
        """L'arabe est exigé au même titre que le français : c'est tout l'objet du verrou."""
        erreurs, _ = validate([entree("pib", ar_terme="   ")])
        self.assertTrue(any("pib" in e and "AR" in e for e in erreurs), erreurs)

    def test_identifiant_en_double(self):
        erreurs, _ = validate([entree("pib"), entree("pib")])
        self.assertTrue(any("double" in e for e in erreurs), erreurs)


class StatutValideTest(unittest.TestCase):
    """Les définitions ne sont exigées QUE des entrées `valide`.

    C'est la distinction qui permet d'introduire une notion en chantier sans bloquer
    la CI, tout en garantissant que rien d'incomplet n'est publié comme validé.
    """

    def test_brouillon_sans_definition_ne_bloque_pas(self):
        erreurs, _ = validate([entree("pib", statut="a-valider")])
        self.assertEqual(erreurs, [])

    def test_valide_sans_definition_francaise_bloque(self):
        e = entree("pib", statut="valide", source_definition="ins")
        e["ar"]["definition"] = "تعريف"
        erreurs, _ = validate([e])
        self.assertTrue(any("pib" in x and "FR" in x for x in erreurs), erreurs)

    def test_valide_sans_definition_arabe_bloque(self):
        e = entree("pib", statut="valide", source_definition="ins")
        e["fr"]["definition"] = "Définition"
        erreurs, _ = validate([e])
        self.assertTrue(any("pib" in x and "AR" in x for x in erreurs), erreurs)

    def test_source_manquante_AVERTIT_sans_bloquer(self):
        """Distinction essentielle : un avertissement ne doit pas faire échouer la CI."""
        e = entree("pib", statut="valide")
        e["fr"]["definition"] = "Définition"
        e["ar"]["definition"] = "تعريف"
        erreurs, avertissements = validate([e])
        self.assertEqual(erreurs, [])
        self.assertEqual(avertissements, ["pib"])


class AncresUtiliseesTest(unittest.TestCase):
    """Les ancres `#g-…` sont cherchées dans DEUX sources, et seulement en français."""

    def setUp(self):
        self._racine = build_glossary.ROOT
        self._tmp = tempfile.TemporaryDirectory()
        build_glossary.ROOT = self._tmp.name
        self.livre = Path(self._tmp.name) / "precis" / "fr" / "livre"
        self.livre.mkdir(parents=True)

    def tearDown(self):
        build_glossary.ROOT = self._racine
        self._tmp.cleanup()

    def ecrire(self, chemin_relatif, texte):
        cible = self.livre / chemin_relatif
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_text(texte, encoding="utf-8")

    def test_ancres_de_la_prose(self):
        self.ecrire("index.qmd", "Voir [le PIB](#g-pib) et [les recettes](#g-recettes).\n")
        self.assertEqual(ancres_utilisees("livre"), {"pib", "recettes"})

    def test_ancres_des_tableaux_engendres(self):
        """LA régression de septembre 2026 : trois liens morts partis en production.

        Une notion qui quitte la prose pour l'en-tête d'un tableau engendré reste
        référencée. Ne lire que les `.qmd` la déclarait orpheline et la supprimait
        de l'annexe, pendant que le tableau continuait d'y renvoyer.
        """
        self.ecrire("tables/ages.md", "| [Cadres actifs](#g-cadres-actifs) |\n")
        self.assertEqual(ancres_utilisees("livre"), {"cadres-actifs"})

    def test_les_deux_sources_sont_reunies(self):
        self.ecrire("index.qmd", "[PIB](#g-pib)\n")
        self.ecrire("tables/ages.md", "[Cadres actifs](#g-cadres-actifs)\n")
        self.assertEqual(ancres_utilisees("livre"), {"pib", "cadres-actifs"})

    def test_le_glossaire_lui_meme_est_exclu(self):
        """Sans cette exclusion, l'annexe se justifierait elle-même.

        Chaque notion y porte sa propre ancre : la lire rendrait toute orpheline
        indétectable, et le contrôle deviendrait décoratif.
        """
        self.ecrire("_glossaire.qmd", "## Notion {#g-fantome}\n")
        self.assertEqual(ancres_utilisees("livre"), set())

    def test_livre_inexistant(self):
        self.assertEqual(ancres_utilisees("livre-absent"), set())


if __name__ == "__main__":
    unittest.main()

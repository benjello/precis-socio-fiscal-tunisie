"""Tests du contrôle de parité FR/AR, et surtout de son MODE DIFFÉRENTIEL.

Ce contrôle décide si une traduction est fusionnable. Deux façons de se tromper,
symétriques et toutes deux observées :

  - laisser passer une régression — une clé de citation perdue produit un arabe
    parfaitement idiomatique qui ne renvoie plus au bon texte de loi ;
  - reprocher une dette que personne n'a introduite. Le 14/09/2026, le chapitre
    des prestations sociales portait 13 divergences avant comme après un
    changement : toute synchronisation de ce livre échouait d'avance, et ce rouge
    permanent masquait le seul signal utile — une divergence NEUVE.

D'où `--compare-to` : mesurer les deux arbres, ne reprocher que les nouvelles.
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from check_translation_parity import compare, divergences, pairs_for  # noqa: E402

FR = "precis/fr/livre/index.qmd"
AR = "precis/ar/livre/index.qmd"


def arbre(racine, texte_fr, texte_ar):
    """Écrit une paire FR/AR sous `racine` et renvoie la racine."""
    for chemin, texte in ((FR, texte_fr), (AR, texte_ar)):
        cible = Path(racine) / chemin
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_text(texte, encoding="utf-8")
    return racine


class ParitéTest(unittest.TestCase):
    def test_paire_conforme_aucune_divergence(self):
        with tempfile.TemporaryDirectory() as tmp:
            arbre(tmp,
                  "Texte [@loi-83-112, art. 5] et {#sec-a}.\n",
                  "نصّ [@loi-83-112, art. 5] و {#sec-a}.\n")
            self.assertEqual(divergences([FR], tmp), [])

    def test_cle_de_citation_perdue_est_signalee(self):
        with tempfile.TemporaryDirectory() as tmp:
            arbre(tmp,
                  "Texte [@loi-83-112, art. 5].\n",
                  "نصّ sans la clé.\n")
            problemes = divergences([FR], tmp)
            self.assertTrue(any("loi-83-112" in p for p in problemes), problemes)

    def test_ancre_presente_en_arabe_absente_du_francais(self):
        """La substitution se voit par les DEUX bouts : c'est ce second message
        qui nomme le jeton fautif, et non seulement celui qui manque."""
        with tempfile.TemporaryDirectory() as tmp:
            arbre(tmp, "Texte {#sec-a}.\n", "نصّ {#sec-b}.\n")
            problemes = divergences([FR], tmp)
            self.assertTrue(any("sec-b" in p and "absent du français" in p
                                for p in problemes), problemes)

    def test_locateur_traduit_est_signale(self):
        with tempfile.TemporaryDirectory() as tmp:
            arbre(tmp,
                  "Texte [@loi-83-112, art. 5 à 7].\n",
                  "نصّ [@loi-83-112, art. 5 إلى 7].\n")
            problemes = compare(FR, AR, tmp)
            self.assertTrue(any("locateur" in p for p in problemes), problemes)


class ModeDifférentielTest(unittest.TestCase):
    """Le cœur de la correction : dette héritée ≠ régression."""

    CASSE = ("Texte [@loi-83-112, art. 5] et [@decret-96-1906, art. 2].\n")
    DETTE = "نصّ [@loi-83-112, art. 5] seulement.\n"          # decret manquant : dette
    NEUVE = "نصّ seulement.\n"                                 # les DEUX manquent

    def test_dette_heritee_ne_produit_aucune_nouveaute(self):
        with tempfile.TemporaryDirectory() as base, \
             tempfile.TemporaryDirectory() as tete:
            arbre(base, self.CASSE, self.DETTE)
            arbre(tete, self.CASSE, self.DETTE)
            heritees = set(divergences([FR], base))
            actuelles = divergences([FR], tete)
            self.assertTrue(actuelles, "le cas de test doit porter une dette")
            self.assertEqual([p for p in actuelles if p not in heritees], [])

    def test_divergence_neuve_est_reprochee(self):
        with tempfile.TemporaryDirectory() as base, \
             tempfile.TemporaryDirectory() as tete:
            arbre(base, self.CASSE, self.DETTE)
            arbre(tete, self.CASSE, self.NEUVE)
            heritees = set(divergences([FR], base))
            nouvelles = [p for p in divergences([FR], tete) if p not in heritees]
            self.assertTrue(nouvelles, "la régression doit être reprochée")
            self.assertTrue(any("loi-83-112" in p for p in nouvelles), nouvelles)


class PérimètreTest(unittest.TestCase):
    def test_le_changelog_est_dans_le_perimetre(self):
        """Il en était absent, et quatre corruptions y sont passées en un jour."""
        with tempfile.TemporaryDirectory() as tmp:
            for nom in ("CHANGELOG.md", "CHANGELOG_ar.md"):
                (Path(tmp) / nom).write_text("[x](https://a/b)\n", encoding="utf-8")
            self.assertEqual(pairs_for(["CHANGELOG.md"], tmp),
                             [("CHANGELOG.md", "CHANGELOG_ar.md")])

    def test_le_glossaire_genere_est_hors_perimetre(self):
        """Les deux langues sont produites ensemble : ce ne sont pas des traductions."""
        self.assertEqual(pairs_for(["precis/fr/livre/_glossaire.qmd"]), [])


if __name__ == "__main__":
    unittest.main()

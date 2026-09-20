"""Tests du garde-fou contre la traduction tronquée.

C'est la dernière défense avant qu'un chapitre amputé n'entre dans une PR. Le
symptôme est indétectable en aval : un chapitre tronqué reste un chapitre bien
formé, il se rend sans erreur, et la PR ouverte automatiquement ressemble à
n'importe quelle autre. Deux cas réels :

  - 9 septembre 2026 : un chapitre arabe de 636 lignes revient à 68 (89 % de perte) ;
  - 14 septembre 2026 : le chapitre des prestations sociales revient à 191 lignes
    contre 656 auparavant et 805 à la source. Le garde a refusé d'écrire le fichier,
    et la synchronisation a échoué au lieu d'ouvrir une PR trompeuse.

Le calcul tient en une ligne, mais chacun de ses termes porte une décision — le
`min`, le `max(1, …)`, le sens de la comparaison. Ces tests les figent un par un.
"""

import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

from translate_sync import SEUIL_TRONCATURE, motif_de_troncature  # noqa: E402


class TraductionSaineTest(unittest.TestCase):
    def test_longueurs_comparables(self):
        self.assertIsNone(motif_de_troncature(800, 790, 805))

    def test_traduction_plus_longue_que_la_source(self):
        """L'arabe peut être plus long : rien à signaler."""
        self.assertIsNone(motif_de_troncature(800, 900, 805))


class TroncatureTest(unittest.TestCase):
    def test_cas_reel_du_14_septembre(self):
        motif = motif_de_troncature(656, 191, 805)
        self.assertIsNotNone(motif)
        for nombre in ("191", "656", "805"):
            self.assertIn(nombre, motif)

    def test_cas_reel_du_9_septembre(self):
        self.assertIsNotNone(motif_de_troncature(636, 68, 640))

    def test_le_message_invite_a_relancer(self):
        """Ce texte est ce qu'un opérateur lit quand la synchro échoue."""
        motif = motif_de_troncature(656, 191, 805)
        self.assertIn("traduction tronquée", motif)
        self.assertIn("Relancer", motif)


class SourceRaccourcieTest(unittest.TestCase):
    """Le `min` existe pour ce cas, et rien ne l'attestait.

    Si le FRANÇAIS a perdu la moitié de ses lignes, l'arabe doit pouvoir en perdre
    autant sans déclencher l'alarme. Se régler sur l'ancienne traduction seule
    ferait échouer toute coupe légitime de la source.
    """

    def test_coupe_legitime_de_la_source(self):
        # L'ancienne traduction faisait 600 lignes, la source n'en fait plus que 100.
        # Le repère est 100, pas 600 : une cible de 95 lignes est normale.
        self.assertIsNone(motif_de_troncature(600, 95, 100))

    def test_coupe_de_la_source_ET_amputation(self):
        # Même source réduite, mais la cible fond bien plus vite qu'elle.
        self.assertIsNotNone(motif_de_troncature(600, 12, 100))


class FrontiereTest(unittest.TestCase):
    """Le seuil exact, dans les deux sens — la ligne où le comportement bascule."""

    def test_juste_au_seuil_passe(self):
        seuil = int(100 * SEUIL_TRONCATURE)  # 60
        self.assertIsNone(motif_de_troncature(100, seuil, 100))

    def test_juste_sous_le_seuil_echoue(self):
        seuil = int(100 * SEUIL_TRONCATURE)
        self.assertIsNotNone(motif_de_troncature(100, seuil - 1, 100))


class CasDegeneresTest(unittest.TestCase):
    def test_traduction_vide_toujours_fautive(self):
        """Le `max(1, …)` garantit qu'une sortie vide ne passe jamais."""
        self.assertIsNotNone(motif_de_troncature(10, 0, 10))

    def test_traduction_vide_meme_avec_reperes_nuls(self):
        """Sans le `max(1, …)`, le seuil vaudrait 0 et une sortie vide passerait."""
        self.assertIsNotNone(motif_de_troncature(0, 0, 0))

    def test_source_minuscule_une_ligne_suffit(self):
        self.assertIsNone(motif_de_troncature(500, 1, 1))


if __name__ == "__main__":
    unittest.main()


class TroncatureSansAncienneCible(unittest.TestCase):
    """Le garde-fou doit servir AUSSI quand il n'y a pas d'ancienne traduction.

    C'est le cas de la première traduction d'un fichier et, surtout, de la
    RETRADUCTION COMPLÈTE, où l'ancienne cible est volontairement ignorée. Le
    contrôle y était sauté — donc absent précisément là où la troncature est la
    plus probable. Mesuré le 20 septembre 2026 sur le vrai script : une réponse de
    trois lignes écrasait un chapitre arabe de 175 lignes, et la passe sortait en 0.
    """

    def test_la_source_sert_de_repere_a_defaut_de_cible(self):
        # C'est la substitution que fait l'appelant : `avant` vaut la source.
        self.assertIsNotNone(motif_de_troncature(185, 3, 185))

    def test_une_traduction_complete_de_bonne_taille_passe(self):
        self.assertIsNone(motif_de_troncature(185, 180, 185))

    def test_l_appelant_ne_saute_plus_le_controle(self):
        source = (RACINE / "scripts" / "translate_sync.py").read_text(encoding="utf-8")
        self.assertNotIn("            if old_target_text:\n                motif =", source,
                         "le contrôle ne doit plus dépendre de l'existence d'une cible")
        self.assertIn("or len(new_source_text.splitlines())", source)

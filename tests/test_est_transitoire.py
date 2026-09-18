"""Tests d'`est_transitoire` — la fonction qui décide si un appel mérite un réessai.

Pourquoi ces tests existent : le 18 septembre 2026, la passe de traduction a échoué sur
un `429 RESOURCE_EXHAUSTED` dont le message disait « Your project has exceeded its
monthly spending cap ». Le script classait tout 429 en erreur passagère : il a réessayé
quatre fois par fichier sur six fichiers — vingt-quatre appels voués à l'échec — et le
journal a noyé la cause réelle sous vingt-quatre lignes « erreur transitoire ».

Le point délicat n'est pas de reconnaître le plafond, c'est de ne pas jeter avec lui les
vrais cas passagers : un dépassement de débit porte le MÊME code 429 et doit, lui, être
réessayé. Les deux sens du 429 sont donc testés côte à côte, et c'est l'essentiel de ce
fichier.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import translate_sync  # noqa: E402

# Le message exact renvoyé par l'API le 18 septembre 2026.
PLAFOND = ("429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'Your project "
           "has exceeded its monthly spending cap. Please go to AI Studio at "
           "https://ai.studio/spend to manage your project spend cap.', "
           "'status': 'RESOURCE_EXHAUSTED'}}")


class LimiteDureTest(unittest.TestCase):
    def test_le_plafond_de_depense_n_est_pas_transitoire(self):
        self.assertFalse(translate_sync.est_transitoire(PLAFOND))

    def test_la_limite_dure_l_emporte_sur_le_code_429(self):
        # Le 429 est escorté d'une mention de plafond : c'est elle qui décide.
        self.assertIn("429", PLAFOND)
        self.assertFalse(translate_sync.est_transitoire(PLAFOND))

    def test_les_variantes_de_formulation(self):
        for msg in ("429 spend cap reached",
                    "billing account is disabled",
                    "Project exceeded its monthly limit"):
            self.assertFalse(translate_sync.est_transitoire(msg), msg)

    def test_la_casse_n_a_pas_d_importance(self):
        self.assertFalse(translate_sync.est_transitoire("429 SPENDING CAP exceeded"))


class ErreurPassagereTest(unittest.TestCase):
    def test_le_debit_reste_transitoire_malgre_le_meme_code(self):
        # Même code, sens opposé : celui-ci DOIT être réessayé.
        self.assertTrue(translate_sync.est_transitoire(
            "429 RESOURCE_EXHAUSTED: Quota exceeded for requests per minute"))

    def test_les_pannes_serveur_restent_transitoires(self):
        for msg in ("503 UNAVAILABLE", "500 INTERNAL", "502 Bad Gateway",
                    "504 DEADLINE_EXCEEDED", "The model is overloaded"):
            self.assertTrue(translate_sync.est_transitoire(msg), msg)

    def test_le_mot_quota_seul_ne_fait_pas_abandonner(self):
        # « quota » est volontairement absent des marqueurs durs : un quota par minute
        # se résorbe, et l'inclure ferait renoncer à des appels qu'il fallait réessayer.
        self.assertTrue(translate_sync.est_transitoire("429 quota exceeded"))


class HorsClassificationTest(unittest.TestCase):
    def test_une_erreur_inconnue_n_est_pas_reessayee(self):
        # Ni passagère ni dure : on ne réessaie pas à l'aveugle.
        self.assertFalse(translate_sync.est_transitoire("400 INVALID_ARGUMENT"))

    def test_message_vide(self):
        self.assertFalse(translate_sync.est_transitoire(""))


if __name__ == "__main__":
    unittest.main()

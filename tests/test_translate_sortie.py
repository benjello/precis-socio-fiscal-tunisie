"""Diagnostic de la sortie du modèle de traduction : raison d'arrêt, jetons, formule perdue.

Le 2 octobre 2026, la retraduction complète du chapitre « Cotisations sociales » (115 Ko) a
échoué deux fois à l'identique — « ⟦MATH0⟧ attendu 3 fois, trouvé 2 fois » — sans que le
journal dise si la sortie avait été coupée ou si le modèle avait omis une formule en pleine
phrase. Ces tests portent sur ce qui rend l'échec lisible, sans appel à l'API.
"""

import contextlib
import io
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from translate_sync import (  # noqa: E402
    FormulesAlterees,
    SortieTronquee,
    TableFormules,
    _lignes_du_jeton,
    journal_jetons,
    masquer_formules,
    raison_d_arret,
    reinjecter_formules,
    verifier_fin,
)


def reponse(raison, **usage):
    """Une réponse factice : `finish_reason` à la manière d'une énumération du SDK."""
    return SimpleNamespace(
        candidates=[SimpleNamespace(finish_reason=SimpleNamespace(name=raison))],
        usage_metadata=SimpleNamespace(**usage) if usage else None)


def silencieux(fonction, *args):
    with contextlib.redirect_stdout(io.StringIO()) as sortie:
        resultat = fonction(*args)
    return resultat, sortie.getvalue()


class RaisonDArretTest(unittest.TestCase):
    def test_enumeration(self):
        self.assertEqual(raison_d_arret(reponse("STOP")), "STOP")

    def test_chaine_qualifiee(self):
        r = SimpleNamespace(candidates=[SimpleNamespace(finish_reason="FinishReason.MAX_TOKENS")])
        self.assertEqual(raison_d_arret(r), "MAX_TOKENS")

    def test_reponse_sans_candidat(self):
        self.assertEqual(raison_d_arret(SimpleNamespace(candidates=[])), "")
        self.assertEqual(raison_d_arret(SimpleNamespace()), "")


class VerifierFinTest(unittest.TestCase):
    def test_max_tokens_leve(self):
        r = reponse("MAX_TOKENS", prompt_token_count=40000, candidates_token_count=65000,
                    thoughts_token_count=500, total_token_count=105500)
        with contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(SortieTronquee) as ctx:
                verifier_fin(r, "precis/fr/x/index.qmd")
        self.assertIn("sortie 65000", str(ctx.exception))

    def test_stop_passe_et_journalise_les_jetons(self):
        r = reponse("STOP", prompt_token_count=10, candidates_token_count=20,
                    thoughts_token_count=5, total_token_count=35)
        _, journal = silencieux(verifier_fin, r, "f.qmd")
        self.assertIn("« STOP »", journal)
        self.assertIn("réflexion 5", journal)

    def test_jetons_inconnus(self):
        self.assertEqual(journal_jetons(SimpleNamespace()), "")


class FormulePerdueTest(unittest.TestCase):
    def test_lignes_du_jeton(self):
        texte = "a ⟦MATH0⟧ b\nrien\nc ⟦MATH0⟧"
        self.assertEqual(_lignes_du_jeton(texte, "⟦MATH0⟧"),
                         "l. 1 « a ⟦MATH0⟧ b », l. 3 « c ⟦MATH0⟧ »")
        self.assertEqual(_lignes_du_jeton("x", "⟦MATH0⟧"), "aucune")

    def test_le_message_dit_quelle_occurrence_manque(self):
        source = "On note $\\kappa$ le taux.\n\n| $\\kappa$ | taux |\n"
        table = TableFormules()
        masquee = masquer_formules(source, table)
        traduction = masquee.replace("| ⟦MATH0⟧ |", "| κ |")  # l'occurrence du tableau perdue
        with self.assertRaises(FormulesAlterees) as ctx:
            reinjecter_formules(source, traduction, table)
        message = str(ctx.exception)
        self.assertIn("source : l. 1", message)
        self.assertIn("l. 3", message)
        self.assertIn("traduction : l. 1", message)


if __name__ == "__main__":
    unittest.main()

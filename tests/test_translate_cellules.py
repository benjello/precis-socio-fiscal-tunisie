"""Garde-fou des cellules Python dans la traduction : structure identique, chaînes libres.

Le 3 octobre 2026, la retraduction de `retraites/_secteur_prive.qmd` a mis des guillemets
droits à l'intérieur de chaînes Python délimitées par des guillemets droits : trois cellules
ne compilaient plus. Ces tests portent sur `verifier_cellules`, sans appel à l'API.
"""

import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from translate_sync import CellulesAlterees, verifier_cellules  # noqa: E402

SOURCE = '''Texte.

```{python}
#| label: fig-x
#| fig-cap: "Légende en français."
#| echo: false
import figtools
figtools.figure_tabs(
    fig, df, "serie",
    note_lecture=(
        "Le « taux d'équilibre (pensions ÷ salaires) » passe de 14 % "
        "à 20 %."))
```
'''

BONNE = SOURCE.replace("Texte.", "نص.").replace("Légende en français.", "تعليق.").replace(
    "Le « taux d'équilibre (pensions ÷ salaires) » passe de 14 % ",
    "تنتقل « نسبة التوازن (الجرايات ÷ الأجور) » من 14 % ").replace("à 20 %.", "إلى 20 %.")

# Le cas réel : les « » rendus par des guillemets droits dans une chaîne à guillemets droits.
CASSEE = BONNE.replace("« نسبة التوازن (الجرايات ÷ الأجور) »", '"نسبة التوازن (الجرايات ÷ الأجور)"')


def silencieux(*args):
    with contextlib.redirect_stdout(io.StringIO()) as sortie:
        resultat = verifier_cellules(*args)
    return resultat, sortie.getvalue()


class VerifierCellulesTest(unittest.TestCase):
    def test_traduction_conforme_inchangee(self):
        self.assertEqual(silencieux(SOURCE, BONNE)[0], BONNE)

    def test_guillemets_interieurs_repares(self):
        resultat, journal = silencieux(SOURCE, CASSEE)
        self.assertEqual(resultat, BONNE.replace("« نسبة التوازن (الجرايات ÷ الأجور) »",
                                                 "«نسبة التوازن (الجرايات ÷ الأجور)»"))
        self.assertIn("1 cellule(s) réparée(s)", journal)

    def test_cellule_qui_ne_compile_plus_refusee(self):
        cassee = BONNE.replace('fig, df, "serie",', 'fig, df, "serie" "',)
        with self.assertRaises(CellulesAlterees) as ctx:
            silencieux(SOURCE, cassee)
        self.assertIn("fig-x", str(ctx.exception))

    def test_code_different_signale_sans_bloquer(self):
        alteree = BONNE.replace('"serie"', '"serie", 42')
        resultat, journal = silencieux(SOURCE, alteree)
        self.assertEqual(resultat, alteree)
        self.assertIn("AVERTISSEMENT", journal)
        self.assertIn("fig-x", journal)

    def test_option_differente_signalee(self):
        alteree = BONNE.replace("#| echo: false", "#| echo: true")
        self.assertIn("AVERTISSEMENT", silencieux(SOURCE, alteree)[1])

    def test_legende_traduite_acceptee(self):
        self.assertIn("تعليق.", silencieux(SOURCE, BONNE)[0])

    def test_cellule_perdue_signalee(self):
        sans = BONNE.split("```{python}")[0]
        resultat, journal = silencieux(SOURCE, sans)
        self.assertEqual(resultat, sans)
        self.assertIn("aucune dans la traduction", journal)

    def test_sans_cellule(self):
        self.assertEqual(silencieux("a\n", "ب\n")[0], "ب\n")


if __name__ == "__main__":
    unittest.main()

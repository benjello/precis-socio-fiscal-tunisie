"""Masquage du code des cellules Python avant traduction, et sa réinjection.

Le 3 octobre 2026, une note de lecture faite d'une vingtaine de littéraux concaténés,
ponctuée de « », est revenue de la traduction avec des guillemets droits au milieu de
littéraux à guillemets droits : la cellule ne compilait plus. Le code est désormais
remplacé par des jetons `⟪CODEn⟫` ; le modèle ne voit que le corps des chaînes de prose.
Ces tests simulent la traduction à la main, sans appel à l'API.
"""

import contextlib
import io
import re
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

from translate_sync import (  # noqa: E402
    CellulesAlterees,
    JETON_CODE_RE,
    TableCode,
    TableFormules,
    masquer_cellules,
    masquer_formules,
    reinjecter_cellules,
    reinjecter_formules,
    verifier_cellules,
)

# Le cas réel, abrégé : une note de lecture de littéraux concaténés, avec des « » dont
# une paire s'ouvre dans un littéral et se ferme dans le suivant.
SOURCE = '''Texte d'introduction.

```{python}
#| label: fig-taux-equilibre
#| fig-cap: "Taux d'équilibre du régime, 1975-2020."
#| echo: false
#| output: asis
import sys; sys.path.insert(0, "../../../scripts")
import figtools
figtools.figure_tabs(
    fig, df, "cnss-rsna-taux-equilibre",
    slug="fig_taux_equilibre",
    caption="Taux d'équilibre du régime, 1975-2020",
    note_lecture=(
        "**Le « Taux d'équilibre (pensions ÷ masse salariale déclarée) » passe ensuite "
        "de 14,05 % à 20 %.** La courbe du régime complémentaire (« Taux d'équilibre, "
        "avec le régime complémentaire », trait fin) suit la première. "
        "Les dinars sont "
        "courants.\\n\\n"
        "La lecture « en points » reste indicative."
    ),
    generated="{{< meta date >}}",
)
```

## Suite {#sec-suite}

Fin.
'''

# Traduction simulée du texte masqué : le modèle rend les « » par des guillemets droits,
# y compris pour la paire qui chevauchait deux littéraux dans la source.
TRADUCTIONS = {
    "Texte d'introduction.": "نص تمهيدي.",
    "Taux d'équilibre du régime, 1975-2020.": "نسبة توازن النظام، 1975-2020.",
    "Taux d'équilibre du régime, 1975-2020": "نسبة توازن النظام، 1975-2020",
    "**Le « Taux d'équilibre (pensions ÷ masse salariale déclarée) » passe ensuite ":
        '**تنتقل "نسبة التوازن (الجرايات ÷ كتلة الأجور المصرح بها)" بعد ذلك ',
    "de 14,05 % à 20 %.** La courbe du régime complémentaire (« Taux d'équilibre, ":
        'من 14,05 % إلى 20 %.** ومنحنى النظام التكميلي ("نسبة التوازن، ',
    "avec le régime complémentaire », trait fin) suit la première. ":
        'مع النظام التكميلي"، خط رفيع) يتبع الأول. ',
    "Les dinars sont ": "الدنانير ",
    "courants.\\n\\n": "جارية.\\n\\n",
    "La lecture « en points » reste indicative.": 'تبقى القراءة "بالنقاط" إرشادية.',
    "Suite": "تتمة",
    "Fin.": "نهاية.",
}


def traduire(masque):
    for fr, ar in TRADUCTIONS.items():
        masque = masque.replace(fr, ar)
    return masque


def silencieux(fonction, *args):
    with contextlib.redirect_stdout(io.StringIO()) as sortie:
        resultat = fonction(*args)
    return resultat, sortie.getvalue()


def cellule(texte):
    return re.search(r"```\{python\}\n(.*?)```", texte, re.S).group(1)


class MasquageTest(unittest.TestCase):
    def test_le_code_n_est_plus_visible(self):
        masque = masquer_cellules(SOURCE, TableCode())
        for code in ("import", "figtools", "sys.path", "{{< meta", "```{python}",
                     "#| label", "note_lecture", "cnss-rsna-taux-equilibre"):
            self.assertNotIn(code, masque)
        self.assertIn("Les dinars sont ", masque)
        self.assertIn("Taux d'équilibre du régime, 1975-2020.", masque)  # fig-cap

    def test_aller_retour_a_vide_rend_la_source(self):
        table = TableCode()
        masque = masquer_cellules(SOURCE, table)
        self.assertEqual(silencieux(reinjecter_cellules, SOURCE, masque, table)[0], SOURCE)

    def test_aller_retour_sur_les_fichiers_du_depot(self):
        """Mesure demandée : sans traduction, masquage puis réinjection = identité."""
        fichiers = sorted(RACINE.glob("precis/*/*/*.qmd"))
        self.assertTrue(fichiers)
        for chemin in fichiers:
            texte = chemin.read_text(encoding="utf-8")
            table_code, table_formules = TableCode(), TableFormules()
            with contextlib.redirect_stdout(io.StringIO()):
                sans_code = masquer_cellules(texte, table_code)
                masque = masquer_formules(sans_code, table_formules)
                rendu = reinjecter_formules(sans_code, masque, table_formules)
                rendu = reinjecter_cellules(texte, rendu, table_code)
            self.assertEqual(rendu, texte, chemin)


class ReinjectionTest(unittest.TestCase):
    def setUp(self):
        self.table = TableCode()
        self.masque = masquer_cellules(SOURCE, self.table)

    def test_cas_reel_guillemets_droits_rendus_et_cellule_compile(self):
        rendu, journal = silencieux(reinjecter_cellules, SOURCE, traduire(self.masque),
                                    self.table)
        code = cellule(rendu)
        compile("\n".join(ligne for ligne in code.split("\n") if not ligne.startswith("#|")),
                "<cellule>", "exec")
        # La paire qui chevauche deux littéraux s'ouvre puis se ferme : « … », jamais « … «.
        self.assertIn("(«نسبة", code)
        self.assertIn("التكميلي»، خط رفيع)", code)
        # Autant de littéraux qu'à la source, aux mêmes retours à la ligne.
        note = code[code.index("note_lecture=("):code.index("    ),")]
        self.assertEqual(note.count('\n        "'), 6)
        self.assertIn("«نسبة التوازن (الجرايات ÷ كتلة الأجور المصرح بها)»", code)
        self.assertIn("«بالنقاط»", code)
        self.assertNotIn('""', code.replace('"""', ""))
        # Le code autour est intact.
        self.assertIn('fig, df, "cnss-rsna-taux-equilibre",', code)
        self.assertIn('generated="{{< meta date >}}",', code)
        self.assertIn('#| fig-cap: "نسبة توازن النظام، 1975-2020."', code)
        self.assertIn("correction(s) d'échappement", journal)
        # Et le garde-fou existant n'a plus rien à redire.
        self.assertEqual(silencieux(verifier_cellules, SOURCE, rendu)[0], rendu)

    def test_litteraux_concatenes_montres_d_un_tenant(self):
        # Le 3 octobre 2026, montrés un à un entre deux jetons, les littéraux d'une note
        # ont été recousus par le modèle, qui a perdu trois jetons intermédiaires.
        self.assertIn("passe ensuite de 14,05 %", self.masque)
        self.assertIn("Les dinars sont courants.", self.masque)
        self.assertEqual(len(JETON_CODE_RE.findall(self.masque)), 4)

    def test_phrases_deplacees_d_un_litteral_a_l_autre(self):
        source = ('```{python}\nf(note=(\n    "Une première phrase "\n'
                  '    "coupée en deux."\n))\n```\n')
        table = TableCode()
        masque = masquer_cellules(source, table)
        traduction = masque.replace("Une première phrase coupée en deux.",
                                    "جملة أولى طويلة جدا مقسومة إلى جزأين اثنين.")
        rendu, _ = silencieux(reinjecter_cellules, source, traduction, table)
        self.assertIn('    "جملة أولى طويلة جدا مقسومة "\n    "إلى جزأين اثنين."\n', rendu)

    def test_blanc_de_bord_retabli(self):
        source = 'A.\n\n```{python}\nf(note="Texte un ", x=1)\n```\n'
        table = TableCode()
        masque = masquer_cellules(source, table)
        rendu, _ = silencieux(reinjecter_cellules, source,
                              masque.replace("Texte un ", "نص"), table)
        self.assertIn('f(note="نص ", x=1)', rendu)

    def test_jetons_dans_un_autre_ordre_refuses(self):
        traduction = traduire(self.masque)
        jetons = JETON_CODE_RE.findall(traduction)
        a, b = f"⟪CODE{jetons[0]}⟫", f"⟪CODE{jetons[1]}⟫"
        permutee = traduction.replace(a, "§").replace(b, a).replace("§", b)
        with self.assertRaises(CellulesAlterees) as ctx:
            silencieux(reinjecter_cellules, SOURCE, permutee, self.table)
        self.assertIn("rang 0", str(ctx.exception))

    def test_jeton_perdu_refuse(self):
        traduction = traduire(self.masque)
        perdu = JETON_CODE_RE.search(traduction).group(0)
        with self.assertRaises(CellulesAlterees):
            silencieux(reinjecter_cellules, SOURCE, traduction.replace(perdu, "", 1),
                       self.table)

    def test_jeton_aux_chiffres_indo_arabes_normalise(self):
        traduction = traduire(self.masque).replace("⟪CODE1⟫", "⟪ CODE ١ ⟫")
        rendu, journal = silencieux(reinjecter_cellules, SOURCE, traduction, self.table)
        self.assertIn("normalisé", journal)
        self.assertIn("```{python}\n#| label: fig-taux-equilibre", rendu)

    def test_cloture_collee_au_texte_remise_en_debut_de_ligne(self):
        traduction = traduire(self.masque).replace("نص تمهيدي.\n\n⟪", "نص تمهيدي. ⟪")
        rendu, journal = silencieux(reinjecter_cellules, SOURCE, traduction, self.table)
        self.assertIn("نص تمهيدي. \n```{python}\n", rendu)
        self.assertIn("début de ligne", journal)

    def test_barre_oblique_invalide_doublee_hors_chaine_brute(self):
        source = 'A.\n\n```{python}\nf(note="un texte libre")\ng(r"un texte brut")\n```\n'
        table = TableCode()
        masque = masquer_cellules(source, table)
        traduction = masque.replace("un texte libre", "نص \\d حر\\").replace(
            "un texte brut", "نص \\d خام")
        rendu, _ = silencieux(reinjecter_cellules, source, traduction, table)
        self.assertIn('f(note="نص \\\\d حر")', rendu)  # doublée, barre finale retirée
        self.assertIn('g(r"نص \\d خام")', rendu)        # chaîne brute : intacte
        compile(cellule(rendu), "<cellule>", "exec")

    def test_formule_dans_une_chaine_brute_masquee_puis_restituee(self):
        source = ('A.\n\n```{python}\nf(note=(\n    r"le taux $\\tau_0 = 40\\,\\%$ au terme "\n'
                  '    r"du stage."))\n```\n')
        table_code, table_formules = TableCode(), TableFormules()
        sans_code = masquer_cellules(source, table_code)
        masque = masquer_formules(sans_code, table_formules)
        self.assertNotIn("\\tau", masque)
        traduction = masque.replace("le taux ", "النسبة ").replace(" au terme ", " في نهاية ")
        with contextlib.redirect_stdout(io.StringIO()):
            rendu = reinjecter_formules(sans_code, traduction, table_formules)
            rendu = reinjecter_cellules(source, rendu, table_code)
        self.assertIn('r"النسبة $\\tau_0 = 40\\,\\%$ في نهاية "', rendu)

    def test_identifiants_et_chemins_restent_du_code(self):
        source = ('```{python}\nimport x\nx.imprime("augmentations/a.csv", "cycles")\n'
                  'x.f(generated="{{< meta date >}}")\n"""Docstring avec des mots."""\n```\n')
        masque = masquer_cellules(source, TableCode())
        self.assertRegex(masque, r"^⟪CODE0⟫\n$")


if __name__ == "__main__":
    unittest.main()

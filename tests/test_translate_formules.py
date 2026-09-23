"""Tests du masquage des formules mathématiques avant traduction.

Pourquoi ces tests existent : le chapitre CNRPS du livre des retraites introduit les
premières formules LaTeX du précis — des blocs `$$ … $$` et une centaine de formules
en ligne `$…$`. Tout ce que le modèle voit, il peut l'abîmer : chiffres indo-arabes,
`\\%` devenu `٪`, backslashs perdus, symboles traduits. Les formules sont donc
remplacées par des jetons `⟦MATHn⟧` avant l'envoi, et réinjectées après.

Deux propriétés comptent, et les tests les prennent une à une :
  - l'aller-retour est EXACT, à l'octet près, y compris quand la traduction
    réordonne la phrase — c'est l'avantage du jeton nommé sur la restauration par
    position ;
  - toute altération d'un jeton (perdu, dupliqué, inventé, formule réécrite en
    clair) fait ÉCHOUER le fichier, au lieu de publier une formule fausse.

Les formules sont celles du chapitre `_secteur_public.qmd` (branche
feat/retraites-cnrps-plan), recopiées telles quelles.
"""

import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from translate_sync import (  # noqa: E402
    FormulesAlterees,
    TableFormules,
    _zones_de_code,
    diff_masque,
    formules_de,
    masquer_formules,
    reinjecter_formules,
    trouver_formules,
)

SOURCE = r"""## La loi de 1959 {#sec-cnrps-loi-1959}

$$
P = \max\big(\min(\tau(n),\ \bar\tau)\cdot R,\ P_{\min}\big), \qquad \tau(n) = \alpha\,n, \qquad n \le n_{\max}
$$

où $P$ est la pension de retraite, $R$ l'assiette de liquidation, $n$ la durée liquidable, $\tau(n)$ le taux de liquidation acquis pour cette durée, $\bar\tau$ le plafond de ce taux, $P_{\min}$ la pension minimale garantie [@loi59-18, art. 22].

$$
\alpha_1 = 2\,\%, \qquad \alpha_2 = 3\,\%, \qquad \alpha_3 = 2\,\%, \qquad \bar\tau = 90\,\%
$$

Le rendement est $\beta = 2\,\%$ par année ; les taux sont $\theta_o = 10\,\%$ et $\theta_c(k) = 75\,\%$.

$$
\tau^* = \frac{N_p\,\bar p}{N_c\,\bar w} = \frac{\bar p}{\bar w}\times\frac{N_p}{N_c}
$$

| $\Delta_i(n)$ | part de la durée $n$ comprise dans la tranche $i$ | @sec-cnrps-formule |
"""

DISPLAY_1 = (
    "$$\nP = \\max\\big(\\min(\\tau(n),\\ \\bar\\tau)\\cdot R,\\ P_{\\min}\\big), "
    "\\qquad \\tau(n) = \\alpha\\,n, \\qquad n \\le n_{\\max}\n$$"
)


def masquer(texte):
    table = TableFormules()
    return masquer_formules(texte, table), table


def muet(fonction, *args):
    """Appelle `fonction` en avalant son journal."""
    with contextlib.redirect_stdout(io.StringIO()):
        return fonction(*args)


class Reperage(unittest.TestCase):
    def test_blocs_et_formules_en_ligne(self):
        formules = formules_de(SOURCE)
        self.assertIn(DISPLAY_1, formules)
        for f in ("$P$", "$\\bar\\tau$", "$P_{\\min}$", "$\\tau(n)$",
                  "$\\beta = 2\\,\\%$", "$\\theta_c(k) = 75\\,\\%$",
                  "$\\Delta_i(n)$", "$i$"):
            self.assertIn(f, formules, f)
        # Trois blocs, chacun compté une fois, délimiteurs compris.
        self.assertEqual(sum(1 for f in formules if f.startswith("$$")), 3)
        self.assertEqual(formules["$n$"], 2)

    def test_le_code_n_est_pas_touche(self):
        texte = (
            "Formule $x$.\n\n"
            "```{python}\n"
            "#| label: fig-x\n"
            "print(f\"${montant}$\")  # $a$ et $$b$$\n"
            "```\n\n"
            "~~~\n$c$\n~~~\n\n"
            "Lancer `echo $BASE_SHA $x$` puis $y$.\n"
        )
        self.assertEqual(formules_de(texte), {"$x$": 1, "$y$": 1})
        masque, _ = masquer(texte)
        self.assertIn('print(f"${montant}$")  # $a$ et $$b$$', masque)
        self.assertIn("~~~\n$c$\n~~~", masque)
        self.assertIn("`echo $BASE_SHA $x$`", masque)

    def test_dollars_qui_ne_sont_pas_des_formules(self):
        # `\$` échappé, `$` suivi d'une espace, `$` fermant suivi d'un chiffre.
        texte = "Prix \\$5 et \\$6. Un $ seul. De 5 $ à 10 $. Ou $a$1."
        self.assertEqual(trouver_formules(texte), [])

    def test_texte_sans_formule_inchange(self):
        texte = "Aucun symbole ici [@loi85-12, art. 36] (@sec-cnrps-formule).\n"
        masque, table = masquer(texte)
        self.assertEqual(masque, texte)
        self.assertEqual(len(table), 0)
        self.assertEqual(reinjecter_formules(texte, "ترجمة بلا رموز\n", table),
                         "ترجمة بلا رموز\n")


class AllerRetour(unittest.TestCase):
    def test_aller_retour_exact(self):
        masque, table = masquer(SOURCE)
        self.assertNotIn("$", masque)
        self.assertNotIn("\\", masque)
        # La traduction « identité » restitue la source à l'octet près.
        self.assertEqual(muet(reinjecter_formules, SOURCE, masque, table), SOURCE)

    def test_bloc_masque_en_un_jeton_seul_sur_sa_ligne(self):
        masque, _ = masquer(SOURCE)
        self.assertTrue(masque.split("\n")[2] == "⟦MATH0⟧", masque[:80])

    def test_meme_formule_meme_jeton(self):
        masque, table = masquer(SOURCE)
        numero = table.par_formule["$n$"]
        self.assertEqual(masque.count(f"⟦MATH{numero}⟧"), 2)

    def test_traduction_qui_reordonne_la_phrase(self):
        source = "où $P$ est la pension, $R$ l'assiette et $\\bar\\tau = 90\\,\\%$ le plafond.\n"
        masque, table = masquer(source)
        self.assertEqual(masque, "où ⟦MATH0⟧ est la pension, ⟦MATH1⟧ l'assiette "
                                 "et ⟦MATH2⟧ le plafond.\n")
        # Ordre inverse en arabe : chaque formule suit son jeton, pas sa position.
        traduction = "حيث ⟦MATH2⟧ السقف، و⟦MATH1⟧ الأساس، و⟦MATH0⟧ الجراية.\n"
        self.assertEqual(
            muet(reinjecter_formules, source, traduction, table),
            "حيث $\\bar\\tau = 90\\,\\%$ السقف، و$R$ الأساس، و$P$ الجراية.\n",
        )

    def test_chiffres_indo_arabes_dans_le_jeton_normalises(self):
        source = "soit $\\beta = 2\\,\\%$ par année.\n"
        _masque, table = masquer(source)
        journal = io.StringIO()
        with contextlib.redirect_stdout(journal):
            sortie = reinjecter_formules(source, "أي ⟦MATH٠⟧ سنويا.\n", table)
        self.assertEqual(sortie, "أي $\\beta = 2\\,\\%$ سنويا.\n")
        self.assertIn("normalisé", journal.getvalue())

    def test_diff_masque(self):
        ancienne = "Le plafond est $\\bar\\tau = 80\\,\\%$.\n\n$$\n\\rho = t\\cdot B\n$$\n"
        nouvelle = "Le plafond est $\\bar\\tau = 90\\,\\%$.\n\n$$\n\\rho = t\\cdot B\n$$\n"
        table = TableFormules()
        masquer_formules(nouvelle, table)  # la source d'abord, comme dans main()
        diff = diff_masque(ancienne, nouvelle, "precis/fr/x.qmd", table)
        self.assertNotIn("$", diff)
        self.assertNotIn("\\", diff)
        nouveau, ancien, bloc = (table.par_formule["$\\bar\\tau = 90\\,\\%$"],
                                 table.par_formule["$\\bar\\tau = 80\\,\\%$"],
                                 table.par_formule["$$\n\\rho = t\\cdot B\n$$"])
        self.assertIn(f"-Le plafond est ⟦MATH{ancien}⟧.", diff)
        self.assertIn(f"+Le plafond est ⟦MATH{nouveau}⟧.", diff)
        self.assertIn(f" ⟦MATH{bloc}⟧", diff)  # bloc inchangé : ligne de contexte


class Detection(unittest.TestCase):
    def setUp(self):
        self.masque, self.table = masquer(SOURCE)

    def echoue(self, traduction):
        with self.assertRaises(FormulesAlterees) as ctx:
            muet(reinjecter_formules, SOURCE, traduction, self.table)
        return str(ctx.exception)

    def test_jeton_manquant(self):
        message = self.echoue(self.masque.replace("⟦MATH0⟧", "", 1))
        self.assertIn("⟦MATH0⟧ attendu 1 fois, trouvé 0 fois", message)

    def test_jeton_duplique(self):
        message = self.echoue(self.masque.replace("⟦MATH1⟧", "⟦MATH1⟧ ⟦MATH1⟧", 1))
        self.assertIn("⟦MATH1⟧ attendu 1 fois, trouvé 2 fois", message)

    def test_jeton_inconnu(self):
        self.assertIn("⟦MATH99⟧ inconnu", self.echoue(self.masque + "⟦MATH99⟧\n"))

    def test_jeton_d_une_formule_que_la_source_n_a_plus(self):
        # Formule présente dans l'ANCIENNE traduction seulement : elle a un jeton
        # dans la table, mais la source ne l'attend plus.
        masquer_formules("$\\bar\\tau = 80\\,\\%$", self.table)
        obsolete = self.table.par_formule["$\\bar\\tau = 80\\,\\%$"]
        self.assertIn(f"⟦MATH{obsolete}⟧ attendu 0 fois",
                      self.echoue(self.masque + f"⟦MATH{obsolete}⟧\n"))

    def test_jeton_mutile(self):
        # « MATH3 » sans crochets : le compte manque ET un résidu reste.
        self.echoue(self.masque.replace("⟦MATH3⟧", "MATH3", 1))

    def test_bloc_qui_n_est_plus_seul_sur_sa_ligne(self):
        # Le bloc remonte dans le paragraphe suivant : les comptes sont justes,
        # mais l'équation ne serait plus rendue comme un bloc.
        message = self.echoue(self.masque.replace("⟦MATH0⟧\n\noù", "⟦MATH0⟧ où", 1))
        self.assertIn("n'est plus seul sur sa ligne", message)

    def test_formule_reecrite_en_clair(self):
        # Le modèle recopie le LaTeX (tiré de l'ancienne traduction, par exemple)
        # à la place du jeton, en l'abîmant au passage.
        traduction = self.masque.replace("⟦MATH1⟧", "$ج$", 1)
        self.echoue(traduction)

    def test_jeton_entoure_de_dollars(self):
        # `$⟦MATH1⟧$` se réinjecte en `$$P$$` : une formule que la source n'a pas.
        self.echoue(self.masque.replace("⟦MATH1⟧", "$⟦MATH1⟧$", 1))


class Corpus(unittest.TestCase):
    """Tout le corpus traduit : aller-retour exact, et aucun `$` laissé hors code.

    Sans objet tant que le précis n'a pas de formule ; il attrapera, le jour où il
    en aura, une forme que le repérage manquerait et qui partirait en clair.
    """

    def test_corpus(self):
        racine = Path(__file__).resolve().parent.parent
        chemins = sorted(racine.glob("precis/*/**/*.qmd"))
        chemins += [racine / "CHANGELOG.md", racine / "CHANGELOG_ar.md"]
        for chemin in chemins:
            if not chemin.exists():
                continue
            texte = chemin.read_text(encoding="utf-8")
            masque, table = masquer(texte)
            with self.subTest(chemin=str(chemin.relative_to(racine))):
                self.assertEqual(muet(reinjecter_formules, texte, masque, table), texte)
                hors_code = masque
                for zone in reversed(_zones_de_code(masque)):
                    hors_code = hors_code[:zone[0]] + hors_code[zone[1]:]
                self.assertNotIn("$", hors_code.replace("\\$", ""))


if __name__ == "__main__":
    unittest.main()

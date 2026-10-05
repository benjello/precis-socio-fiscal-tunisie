"""Tests de `restore_relative_links` et de `restore_heading_spacing`.

Deux dégâts réels de la traduction, réparés après coup sans appel à l'API :
  - un segment de chemin déformé dans un lien d'un livre à l'autre
    (`../cotisations_socales/` pour `../cotisations_sociales/`) : lien mort ;
  - des intertitres arabes collés à la ligne précédente : Pandoc n'y voit plus de titre,
    l'ancre disparaît, et le renvoi `@sec-cnrps-invalidite` ne résout plus.
"""

import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from translate_sync import restore_heading_spacing, restore_relative_links  # noqa: E402


def silencieux(fonction, *args):
    with contextlib.redirect_stdout(io.StringIO()) as sortie:
        resultat = fonction(*args)
    return resultat, sortie.getvalue()


SOURCE = (
    "Voir le [taux](../cotisations_sociales/index.html#sec-cot-pensions-public), le "
    "[régime](_regime_conventionnel.qmd), la [section](_regime_indiciaire.qmd#sec-a), "
    "la [définition](#g-pension) et le [site](https://pist.tn/x).\n\n"
    "![](figures/carte.png)\n"
)
TRADUCTION = (
    "انظر [النسبة](../cotisations_socales/index.html#sec-cot-pensions-publique)، "
    "[النظام](_regime_conventionel.qmd)، [القسم](_regime_indiciaire.qmd#sec-a)، "
    "[التعريف](#g-pension) و[الموقع](https://pist.tn/x).\n\n"
    "![](figures/carte.png)\n"
)


class RestoreRelativeLinksTest(unittest.TestCase):
    def test_segments_deformes_retablis_fragment_compris(self):
        rendu, journal = silencieux(restore_relative_links, SOURCE, TRADUCTION)
        self.assertIn("](../cotisations_sociales/index.html#sec-cot-pensions-public)", rendu)
        self.assertIn("](_regime_conventionnel.qmd)", rendu)
        self.assertIn("انظر [النسبة]", rendu)  # la prose n'est pas touchée
        self.assertEqual(journal.count("lien relatif restauré"), 2)
        self.assertIn("cotisations_socales", journal)

    def test_ancres_et_url_ne_sont_pas_des_liens_relatifs(self):
        traduction = TRADUCTION.replace("#g-pension)", "#g-pensions)").replace(
            "https://pist.tn/x", "https://pist.tn/y")
        rendu, _ = silencieux(restore_relative_links, SOURCE, traduction)
        self.assertIn("](#g-pensions)", rendu)       # affaire de restore_anchors
        self.assertIn("](https://pist.tn/y)", rendu)  # affaire de restore_urls

    def test_rien_a_faire_muette(self):
        rendu, journal = silencieux(restore_relative_links, SOURCE, SOURCE)
        self.assertEqual((rendu, journal), (SOURCE, ""))

    def test_abstention_si_les_nombres_different(self):
        # Un lien de glossaire ajouté par le modèle rompt la correspondance un à un.
        traduction = TRADUCTION + "[مصطلح](../glossaire.html#g-x)\n"
        rendu, journal = silencieux(restore_relative_links, SOURCE, traduction)
        self.assertEqual(rendu, traduction)
        self.assertIn("aucune restauration", journal)


SOURCE_TITRES = (
    "# Retraites {#sec-retraites}\n\n"
    "Paragraphe.\n\n"
    "## Invalidité {#sec-cnrps-invalidite}\n\n"
    "Texte.\n\n"
    "### Sans ancre\n\n"
    "```{python}\n# commentaire\nx = 1\n```\n\n"
    "<!--\n## Titre en commentaire\n-->\n"
)


class RestoreHeadingSpacingTest(unittest.TestCase):
    def test_ligne_vide_reinseree_devant_les_titres_colles(self):
        traduction = (
            "# التقاعد {#sec-retraites}\n\n"
            "فقرة.\n"
            "## العجز {#sec-cnrps-invalidite}\n\n"
            "نص.\n"
            "### بدون مرساة\n\n"
            "```{python}\n# commentaire\nx = 1\n```\n\n"
            "<!--\n## Titre en commentaire\n-->\n"
        )
        rendu, journal = silencieux(restore_heading_spacing, SOURCE_TITRES, traduction)
        self.assertIn("فقرة.\n\n## العجز {#sec-cnrps-invalidite}", rendu)
        self.assertIn("نص.\n\n### بدون مرساة", rendu)
        self.assertIn("2 titre(s)", journal)
        # Le code et les commentaires ne sont pas des titres.
        self.assertIn("```{python}\n# commentaire\n", rendu)
        self.assertIn("<!--\n## Titre en commentaire\n-->", rendu)

    def test_jointure_de_deux_morceaux(self):
        # Le premier morceau a perdu sa ligne vide finale : le titre du second s'y colle.
        traduction = "# التقاعد {#sec-retraites}\n\nفقرة.\n" + "## العجز {#sec-cnrps-invalidite}\n\nنص.\n"
        source = "# Retraites {#sec-retraites}\n\nParagraphe.\n\n## Invalidité {#sec-cnrps-invalidite}\n\nTexte.\n"
        rendu, _ = silencieux(restore_heading_spacing, source, traduction)
        self.assertIn("فقرة.\n\n## العجز", rendu)

    def test_titre_sans_ancre_ignore_si_les_nombres_different(self):
        traduction = "فقرة.\n### بدون مرساة\n### عنوان زائد\n"
        source = "Paragraphe.\n\n### Sans ancre\n"
        rendu, _ = silencieux(restore_heading_spacing, source, traduction)
        self.assertEqual(rendu, traduction)

    def test_rien_a_faire_muette(self):
        rendu, journal = silencieux(restore_heading_spacing, SOURCE_TITRES, SOURCE_TITRES)
        self.assertEqual((rendu, journal), (SOURCE_TITRES, ""))


if __name__ == "__main__":
    unittest.main()

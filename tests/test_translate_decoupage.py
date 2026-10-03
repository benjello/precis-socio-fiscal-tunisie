"""Découpage des longs fichiers pour la traduction : coupes sûres, recollage exact, appariement.

Le 3 octobre 2026, `retraites/_secteur_prive.qmd` (231 Ko) a épuisé le plafond de sortie du
modèle même sans réflexion. Au-delà de `SEUIL_DECOUPAGE`, le fichier est traduit par
morceaux coupés aux titres ancrés. Ces tests portent sur le découpage, sans appel à l'API.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from translate_sync import (  # noqa: E402
    DecoupageImpossible,
    apparier,
    decouper,
    points_de_coupe,
)

RACINE = Path(__file__).resolve().parent.parent


def texte(*sections):
    return "".join(sections)


SECTION = "## Titre {n} {{#sec-{n}}}\n\n" + ("Une phrase de prose. " * 20 + "\n\n") * 3


class PointsDeCoupeTest(unittest.TestCase):
    def test_titres_ancres_seulement(self):
        t = "intro\n\n## Sans ancre\n\nx\n\n## Avec {#sec-a}\n\ny\n\n### Sous {#sec-b}\n\nz\n"
        self.assertEqual([a for _p, a in points_de_coupe(t)], ["sec-a", "sec-b"])

    def test_jamais_dans_un_bloc_de_code(self):
        t = "a\n\n```{python}\n## faux titre {#sec-faux}\n```\n\n## Vrai {#sec-vrai}\n"
        self.assertEqual([a for _p, a in points_de_coupe(t)], ["sec-vrai"])

    def test_jamais_dans_un_commentaire(self):
        t = "a\n\n<!--\n## commenté {#sec-faux}\n-->\n\n## Vrai {#sec-vrai}\n"
        self.assertEqual([a for _p, a in points_de_coupe(t)], ["sec-vrai"])

    def test_jamais_dans_un_bloc_div(self):
        t = "a\n\n::: {.callout-note}\n## dans un encadré {#sec-faux}\n:::\n\n## Vrai {#sec-vrai}\n"
        self.assertEqual([a for _p, a in points_de_coupe(t)], ["sec-vrai"])


class DecouperTest(unittest.TestCase):
    def test_recollage_exact_et_taille(self):
        t = texte(*(SECTION.format(n=i) for i in range(12)))
        morceaux = decouper(t, taille=1500)
        self.assertEqual("".join(m for _a, m in morceaux), t)
        self.assertGreater(len(morceaux), 3)
        self.assertIsNone(morceaux[0][0])

    def test_court_reste_entier(self):
        t = SECTION.format(n=1)
        self.assertEqual(decouper(t, taille=10_000), [(None, t)])

    def test_ancres_permises(self):
        t = texte(*(SECTION.format(n=i) for i in range(6)))
        morceaux = decouper(t, taille=500, ancres_permises={"sec-3"})
        self.assertEqual([a for a, _m in morceaux], [None, "sec-3"])


class ApparierTest(unittest.TestCase):
    def test_appariement_par_ancres(self):
        fr = texte(*(SECTION.format(n=i) for i in range(6)))
        ar = fr.replace("Une phrase de prose.", "جملة.")
        morceaux = decouper(fr, taille=1500)
        cibles = apparier(morceaux, ar)
        self.assertEqual(len(cibles), len(morceaux))
        self.assertEqual("".join(cibles), ar)
        for (ancre, _m), cible in zip(morceaux[1:], cibles[1:]):
            self.assertIn("{#" + ancre + "}", cible.splitlines()[0])

    def test_ancre_absente(self):
        fr = texte(*(SECTION.format(n=i) for i in range(6)))
        morceaux = decouper(fr, taille=1500)
        ar = fr.replace("{#" + morceaux[1][0] + "}", "")
        with self.assertRaises(DecoupageImpossible):
            apparier(morceaux, ar)


class ChapitresReelsTest(unittest.TestCase):
    """Les longs chapitres du précis se découpent en morceaux bien formés."""

    def test_secteur_prive(self):
        source = (RACINE / "precis/fr/retraites/_secteur_prive.qmd").read_text(encoding="utf-8")
        morceaux = decouper(source)
        self.assertEqual("".join(m for _a, m in morceaux), source)
        self.assertGreater(len(morceaux), 2)
        for _a, m in morceaux:
            self.assertEqual(m.count("```") % 2, 0)
            self.assertEqual(m.count("<!--"), m.count("-->"))


if __name__ == "__main__":
    unittest.main()

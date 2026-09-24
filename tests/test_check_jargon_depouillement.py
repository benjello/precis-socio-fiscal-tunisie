"""Tests du garde « le précis ne parle pas du dépouillement ».

Invariant éditorial (AGENTS.md) : le texte publié dit ce qui est CONNU du droit — « seul
l'intitulé de ce texte est connu ici », « n'est pas établi ici » —, jamais comment on l'a
cherché : ni « consulté sur pièce », ni « lu à l'image », ni « OCR ». Le constat de
travail vit dans un commentaire `<!-- TODO (documentaliste) : … -->`.

Comme son voisin `check_pas_de_modele`, ce garde doit SOUS-détecter : « le ministère
consulté », « à l'image de la loi », « non lucratif », « le plafond n'a pas été relevé »,
« le fascicule n° 39 » sont du français ou du droit. Les tests d'exclusion comptent donc
autant que ceux de détection.
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from check_jargon_depouillement import controle  # noqa: E402


class FichierTemporaire(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        self._tmp.cleanup()

    def fautes(self, texte):
        chemin = Path(self._tmp.name) / "chapitre.qmd"
        chemin.write_text(texte, encoding="utf-8")
        return controle(chemin)


class DetectionTest(FichierTemporaire):
    """Ce que le garde DOIT signaler."""

    PHRASES = [
        "Ces deux textes n'ont pas été consultés sur pièce.",
        "Le décret n° 2019-209 a été consulté dans l'édition arabe ; aucun des décrets consultés ne le dit.",
        "Le numéro 58 de 2026 n'a pu être consulté.",
        "Il n'existe pas, dans le corpus consulté, de série.",
        "Le décret, objet seul, est cité.",
        "Ces textes sont repérés par métadonnées seulement.",
        "Les métadonnées seules sont connues.",
        "Loi n° 60-30 [T], décret n° 74-499 [M].",
        "Une date d'effet non lue dans le texte.",
        "La loi n° 65-17 n'a pas été lue.",
        "Son contenu n'a pu être lu.",
        "Chacun des trois taux a été lu dans le fascicule.",
        "Les trois articles ont été lus au fascicule.",
        "Le partage n'est fixé par aucun texte lu.",
        "Sources : textes lus à l'image.",
        "Seules pages relues sur le fac-similé.",
        "Texte repéré et lu partiellement seulement.",
        "C'est le résultat le plus solide du dépouillement.",
        "Sept textes restent à dépouiller.",
        "Taux non transcrits.",
        "Les valeurs n'ont pas été transcrites.",
        "Lu par reconnaissance optique d'un scan sans couche texte.",
        "Le fascicule a été passé à l'OCR.",
        "Le fascicule a été océrisé.",
        # Recherches infructueuses : la trace va dans docs/recherches.yml.
        "Ce décret n'a pas été retrouvé.",
        "Aucun texte n'a été retrouvé en ce sens.",
        "Aucune modification n'a été retrouvée.",
        "Les arrêtés n'ont pas été retrouvés.",
        "Aucun texte n'a été repéré.",
        "Le décret n'ayant pas été retrouvé, le taux reste inconnu.",
        "Rien au *Journal officiel* jusqu'au numéro du 18 septembre 2026.",
        "Rien au JORT jusqu'au 18 septembre 2026.",
        "Vérifié jusqu'au n° 93 de 2026.",
        "Aucun modificatif jusqu'au JORT du 18 septembre 2026.",
        "Aucun modificatif jusqu'au *Journal officiel* du 18 septembre 2026.",
    ]

    def test_chaque_tournure_est_signalee(self):
        for phrase in self.PHRASES:
            with self.subTest(phrase=phrase):
                self.assertEqual(len(self.fautes(phrase + "\n")), 1)

    def test_apostrophe_typographique(self):
        self.assertEqual(len(self.fautes("La loi n’a pas été lue.\n")), 1)

    def test_numero_de_ligne_exact(self):
        self.assertEqual(self.fautes("propre\npropre\ntexte non lu\n")[0][0], 3)

    def test_une_seule_faute_par_ligne(self):
        self.assertEqual(len(self.fautes("Non lu, non consulté sur pièce, OCR.\n")), 1)


class ExclusionTest(FichierTemporaire):
    """Ce que le garde ne doit PAS signaler — aussi important que la détection."""

    PHRASES = [
        "Le ministère consulté rend un avis conforme.",
        "Le conseil d'administration est consulté sur le budget.",
        "À l'image de la loi de 1960, le décret fixe un taux.",
        "Une association à but non lucratif.",
        "Le plafond de 2 000 dinars n'a pas été relevé en 2017 : il a été créé.",
        "Les retenues à la source relevées en 2021.",
        "Les huit articles figurent p. 847 du fascicule n° 39 du 10 juin 1988.",
        "Publié dans le même fascicule que le décret n° 88-1443.",
        "Le contrôle sur pièces de l'administration fiscale.",
        "Seul l'intitulé de ce texte est connu ici.",
        "Ce décret n'est pas identifié ici.",
        "Le régime s'applique jusqu'au 31 décembre 2026.",
        "Du 1er janvier jusqu'au 30 juin, le taux est de 5 %.",
        "La pension est servie jusqu'au décès du conjoint.",
        "Le texte a été retrouvé par la veuve dans les archives, dit l'arrêt.",
        "Le décret n'a pas été trouvé en ce sens par la Cour.",
        "Publié au *Journal officiel* n° 129 du 23 octobre 2024.",
        "<!-- RECHERCHE r-dl2024-4-art33 : n'a pas été retrouvé au JORT jusqu'au n° 93 -->",
        "Le contenu de ce tableau n'est pas établi ici.",
        "Le montant dû suit l'activité au lieu d'être lu dans une grille.",
        "*Transcription d'après le texte publié au JORT n° 62.*",
    ]

    def test_emplois_legitimes(self):
        for phrase in self.PHRASES:
            with self.subTest(phrase=phrase):
                self.assertEqual(self.fautes(phrase + "\n"), [])

    def test_constat_dans_un_commentaire_html(self):
        """La destination prévue du constat de travail."""
        texte = "prose\n<!-- TODO (documentaliste) : non lu, consulté sur pièce,\nOCR à refaire. -->\n"
        self.assertEqual(self.fautes(texte), [])

    def test_constat_dans_un_bloc_de_code(self):
        self.assertEqual(self.fautes("prose\n```{python}\n# texte non lu, OCR\n```\n"), [])


if __name__ == "__main__":
    unittest.main()

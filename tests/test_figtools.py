"""Tests de la date de génération des figdata.

Chaque `quarto render` réécrivait les figdata avec la date du jour, même quand ni les
données ni la provenance n'avaient bougé. Le dépôt se salissait donc d'une vingtaine
de fichiers à chaque build — CSV **et** sidecar `.yml` —, qu'il fallait restaurer à la
main avant tout commit sous peine de les emporter. Le 16/09/2026 : quatre
restaurations en une matinée, et un commit passé (`b140ea2`) qui réparait déjà
exactement cela, six figdata dont seule la date changeait.

Le piège du correctif est dans l'autre sens. Conserver la date dès que les DONNÉES
sont identiques ferait mentir l'en-tête : une légende, une source ou une réserve
modifiée doit redater le fichier, car cet en-tête tient lieu de provenance dans un CSV
publié et téléchargeable. D'où la double condition que ces tests figent — corps
identique **et** en-tête hors date identique.

`date_deja_inscrite` est volontairement pure : elle reçoit le texte déjà écrit et ne
lit aucun fichier. Elle se teste donc sans pandas, conformément à la règle du job de
tests — « si l'un d'eux réclame un jour un paquet, c'est le signe qu'il teste autre
chose que ce qu'il annonce ».
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from figtools import date_deja_inscrite  # noqa: E402

ENTETE = [
    "# séries (tunisia_data) : recettes-fiscales-composition",
    "# sources (citation) : @minfin-recettes",
    "# fiches : fiche-recettes.md",
    "# méthode/hypothèses : périmètre budget de l'État",
]
CORPS = "annee,valeur\n1990,19.8\n1991,21.4\n"


def figdata(date, entete=None, corps=None):
    """Reconstitue un figdata tel que `write_figdata` l'écrit."""
    lignes = [f"# Figure-data du précis socio-fiscal tunisien — généré le {date}"]
    lignes += ENTETE if entete is None else entete
    return "\n".join(lignes) + "\n" + (CORPS if corps is None else corps)


class RienNaChangeTest(unittest.TestCase):
    """LE cas de la règle : un rendu identique ne doit pas redater."""

    def test_la_date_existante_est_conservee(self):
        ancien = figdata("2026-09-09")
        self.assertEqual(date_deja_inscrite(ancien, ENTETE, CORPS), "2026-09-09")

    def test_avec_une_note_identique(self):
        entete = ENTETE + ["# note : Rendement comparé au PIB"]
        ancien = figdata("2026-09-09", entete=entete)
        self.assertEqual(date_deja_inscrite(ancien, entete, CORPS), "2026-09-09")


class LesDonneesChangentTest(unittest.TestCase):
    """Une donnée modifiée doit redater : c'est la raison d'être du fichier."""

    def test_valeur_modifiee(self):
        ancien = figdata("2026-09-09", corps="annee,valeur\n1990,19.8\n1991,99.9\n")
        self.assertIsNone(date_deja_inscrite(ancien, ENTETE, CORPS))

    def test_ligne_ajoutee(self):
        ancien = figdata("2026-09-09", corps=CORPS + "1992,22.0\n")
        self.assertIsNone(date_deja_inscrite(ancien, ENTETE, CORPS))

    def test_corps_vide(self):
        ancien = figdata("2026-09-09", corps="")
        self.assertIsNone(date_deja_inscrite(ancien, ENTETE, CORPS))


class LaProvenanceChangeTest(unittest.TestCase):
    """L'autre moitié de la règle, et la plus facile à oublier.

    Si seule la provenance bouge, les données sont identiques — mais l'en-tête décrit
    désormais autre chose. Conserver la date le ferait mentir sur ce qu'il documente,
    ce qui est pire qu'une date qui bouge pour rien.
    """

    def test_source_de_citation_modifiee(self):
        ancien = figdata("2026-09-09", entete=[
            ENTETE[0], "# sources (citation) : @autre-source", ENTETE[2], ENTETE[3],
        ])
        self.assertIsNone(date_deja_inscrite(ancien, ENTETE, CORPS))

    def test_serie_modifiee(self):
        ancien = figdata("2026-09-09", entete=[
            "# séries (tunisia_data) : une-autre-serie", *ENTETE[1:],
        ])
        self.assertIsNone(date_deja_inscrite(ancien, ENTETE, CORPS))

    def test_reserve_methodologique_modifiee(self):
        ancien = figdata("2026-09-09", entete=[
            *ENTETE[:3], "# méthode/hypothèses : périmètre administrations publiques",
        ])
        self.assertIsNone(date_deja_inscrite(ancien, ENTETE, CORPS))

    def test_note_ajoutee(self):
        """La légende passe dans l'en-tête : la modifier doit redater."""
        ancien = figdata("2026-09-09")
        entete = ENTETE + ["# note : une légende neuve"]
        self.assertIsNone(date_deja_inscrite(ancien, entete, CORPS))

    def test_note_retiree(self):
        entete = ENTETE + ["# note : une légende"]
        ancien = figdata("2026-09-09", entete=entete)
        self.assertIsNone(date_deja_inscrite(ancien, ENTETE, CORPS))


class PremierEcritureTest(unittest.TestCase):
    """Sans fichier antérieur, il n'y a pas de date à conserver."""

    def test_fichier_absent(self):
        self.assertIsNone(date_deja_inscrite(None, ENTETE, CORPS))

    def test_fichier_vide(self):
        self.assertIsNone(date_deja_inscrite("", ENTETE, CORPS))

    def test_fichier_sans_entete(self):
        """Un CSV nu, écrit par autre chose que `write_figdata`."""
        self.assertIsNone(date_deja_inscrite(CORPS, ENTETE, CORPS))


class DateLueTest(unittest.TestCase):
    """La date est le dernier mot de la première ligne."""

    def test_date_quelconque(self):
        self.assertEqual(date_deja_inscrite(figdata("2025-01-31"), ENTETE, CORPS),
                         "2025-01-31")

    def test_premiere_ligne_sans_date(self):
        """Le cas qui a pris la fonction en défaut, gardé tel quel.

        Sans validation de la forme, `rsplit` rendait le mot précédant la date —
        « … généré le » donnait « le » —, et cette chaîne repartait comme date dans le
        fichier réécrit : l'en-tête aurait affiché « généré le le ».
        """
        ancien = figdata("").replace(" généré le \n", " généré le\n")
        self.assertIsNone(date_deja_inscrite(ancien, ENTETE, CORPS))

    def test_date_illisible(self):
        """En-tête corrompu : mieux vaut redater que propager une date fausse."""
        for valeur in ("hier", "2026-13-45", "09/09/2026", "2026-09"):
            with self.subTest(valeur=valeur):
                self.assertIsNone(date_deja_inscrite(figdata(valeur), ENTETE, CORPS))


if __name__ == "__main__":
    unittest.main()

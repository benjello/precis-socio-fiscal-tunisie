"""Les notices citées par plusieurs volumes vivent au fonds commun, en un seul exemplaire.

La convention collective des assurances est décrite dans deux volumes : sa chaîne d'avenants
dans « Les rémunérations dans le secteur public », ses grilles dans l'annexe des conventions
collectives du volume « Marché du travail ». Ses clés `cc-assurances-*` ont longtemps été
tenues en double, à la main, dans les `references.json` des deux livres ; le 13 octobre 2026,
elles ont été versées au fonds commun (`precis/<langue>/references.json`) avec les autres
références citées par plusieurs volumes.

Le premier test reste en garde : si une clé revient un jour dans les deux livres, ses deux
copies doivent être identiques. Le deuxième vérifie que les clés des assurances sont bien au
fonds commun et dans aucun des deux livres.

Restent en double hors de cette paire, relevé du 13 octobre 2026 : `lfc-2012` (fiscalité et
finances locales), `decret80-75` et `lf-1996` (fonds commun et un livre).
"""

import json
import unittest
from pathlib import Path

PRECIS = Path(__file__).resolve().parent.parent / "precis"
LANGUES = ("fr", "ar")
LIVRES = ("marche_travail", "remunerations_publiques")


def notices(langue: str, livre: str) -> dict:
    chemin = PRECIS / langue / livre / "references.json"
    with chemin.open(encoding="utf-8") as f:
        return {notice["id"]: notice for notice in json.load(f)["items"]}


class NoticesCommunes(unittest.TestCase):

    def test_une_clé_commune_a_la_même_notice_dans_les_deux_livres(self):
        for langue in LANGUES:
            ici, ailleurs = (notices(langue, livre) for livre in LIVRES)
            for cle in sorted(set(ici) & set(ailleurs)):
                with self.subTest(langue=langue, cle=cle):
                    self.assertEqual(
                        ici[cle], ailleurs[cle],
                        f"{cle} ({langue}) : la notice diffère entre {LIVRES[0]} et "
                        f"{LIVRES[1]} ; recopier à l'identique la copie corrigée")

    def test_les_clés_des_assurances_sont_au_fonds_commun(self):
        for langue in LANGUES:
            with (PRECIS / langue / "references.json").open(encoding="utf-8") as f:
                commun = {notice["id"] for notice in json.load(f)["items"]}
            assurances = {cle for cle in commun if cle.startswith("cc-assurances-")}
            with self.subTest(langue=langue):
                self.assertIn("cc-assurances-avenant11-grille-2015", assurances)
                self.assertGreaterEqual(len(assurances), 18)
                for livre in LIVRES:
                    self.assertFalse(assurances & set(notices(langue, livre)),
                                     f"{livre} ({langue}) garde une copie d'une clé du fonds commun")

    def test_les_deux_langues_tiennent_les_mêmes_clés_communes(self):
        communes = []
        for langue in LANGUES:
            ici, ailleurs = (notices(langue, livre) for livre in LIVRES)
            communes.append(set(ici) & set(ailleurs))
        self.assertEqual(communes[0], communes[1])


if __name__ == "__main__":
    unittest.main()

"""Les notices communes au marché du travail et aux rémunérations publiques sont identiques.

La convention collective des assurances est décrite dans deux volumes : sa chaîne d'avenants
dans « Les rémunérations dans le secteur public », ses grilles dans l'annexe des conventions
collectives du volume « Marché du travail ». Les clés `cc-assurances-*` sont donc tenues en
double, à la main, dans les `references.json` des deux livres — en français et en arabe.

Rien ne signale qu'une des deux copies a été corrigée seule : les deux livres rendent, et la
même clé donne alors deux notices différentes selon le volume. Ce test compare, pour chaque
langue, toute clé présente dans les deux livres.

Il ne porte que sur cette paire de livres. D'autres clés communes à d'autres volumes
divergent déjà (relevé du 9 octobre 2026 : `loi86-106-lf1987`, `loi57-73`,
`loi-2007-70-lf-2008`, `lfc-2012`, `ins-annuaire` ; en arabe, aussi `loi59-45` et
`loi86-86`) : elles ne sont pas contrôlées ici.
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

    def test_les_clés_des_assurances_sont_bien_dans_les_deux_livres(self):
        # Sans clé commune, le test ci-dessus passerait à vide.
        for langue in LANGUES:
            ici, ailleurs = (notices(langue, livre) for livre in LIVRES)
            communes = {cle for cle in set(ici) & set(ailleurs)
                        if cle.startswith("cc-assurances-")}
            with self.subTest(langue=langue):
                self.assertIn("cc-assurances-avenant11-grille-2015", communes)
                self.assertGreaterEqual(len(communes), 18)

    def test_les_deux_langues_tiennent_les_mêmes_clés_communes(self):
        communes = []
        for langue in LANGUES:
            ici, ailleurs = (notices(langue, livre) for livre in LIVRES)
            communes.append(set(ici) & set(ailleurs))
        self.assertEqual(communes[0], communes[1])


if __name__ == "__main__":
    unittest.main()

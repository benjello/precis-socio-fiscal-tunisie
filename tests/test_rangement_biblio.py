"""Tests du contrôle de rangement bibliographique (lecture seule).

`push_biblio.ranger` fait `sorted(actuelles | voulues)` : il **ajoute** des collections
et n'en retire jamais. Une référence qui devient commune à plusieurs livres garde donc
la collection du livre où elle est née, et chaque descente la redescend dans ce livre
au lieu du fonds commun. C'est ce mécanisme qui a fait tomber le fonds commun à 7 clés.

Rien ne détectait cette dérive : le `dry-run` Zotero vérifie que la *conversion*
fonctionne, jamais le *rangement*. Les deux défauts sont distincts, et le second a duré
des mois sans que le premier ne le voie.

## Le contrat, et pourquoi il est orienté ainsi

  - citée par **exactement 1 livre** → elle veut la collection de ce livre ;
  - citée par **2 livres ou plus**   → elle ne veut **aucune** collection de livre,
    afin que la descente la verse dans `precis/fr/references.json` ;
  - citée par **aucun** livre         → on ne prend **aucune** position. Retirer une
    collection sur la foi d'une absence changerait l'état d'une bibliothèque partagée
    à partir d'une preuve qu'on n'a pas su trouver.

## Les citations se lisent à TROIS sources

Mesuré le 16/09/2026 sur le corpus :

  - la prose (`*.qmd`) ;
  - les tableaux engendrés (`tables/*.md`) — **36 clés distinctes** n'y vivent que là,
    dont les arrêtés de transferts sociaux ;
  - **l'annexe de glossaire** (`_glossaire.qmd`), que `build_glossary.render_book`
    remplit de vraies `[@clé]` résolues contre la bibliographie du livre.

Le glossaire ne doit PAS être exclu, quoi qu'en fasse `ancres_utilisees` : son exclusion
y est justifiée pour les *ancres* — l'annexe se définirait elle-même —, raison qui ne
vaut pas pour les *citations*. L'exclure ferait passer cinq clés de « partagée » à
« propre à un livre » : `decret-2017-668-smig` (trois livres), `lf-2018`, `loi82-70`,
`loi83-112`, `loi85-78`. Toutes dans le même sens, et le pire : le contrôle aurait
conservé la collection qui doit partir, perpétuant la dérive qu'il existe pour détecter.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from push_biblio import classe_rangement  # noqa: E402


def cat(resultat, nom):
    return resultat[nom]


class UnSeulLivreTest(unittest.TestCase):
    """Une référence propre à un livre veut la collection de ce livre."""

    def test_bien_rangee(self):
        r = classe_rangement({"fiscalite": {"code-tva"}}, {"code-tva": {"fiscalite"}})
        self.assertEqual(cat(r, "bien_rangee"), ["code-tva"])
        self.assertEqual(cat(r, "a_declasser"), [])
        self.assertEqual(cat(r, "a_ranger"), [])

    def test_collection_manquante_a_ranger(self):
        r = classe_rangement({"fiscalite": {"code-tva"}}, {"code-tva": set()})
        self.assertEqual(cat(r, "a_ranger"), [("code-tva", ["fiscalite"])])

    def test_collection_du_mauvais_livre(self):
        """Elle doit gagner la bonne ET perdre l'autre."""
        r = classe_rangement({"fiscalite": {"code-tva"}}, {"code-tva": {"retraites"}})
        self.assertEqual(cat(r, "a_ranger"), [("code-tva", ["fiscalite"])])
        self.assertEqual(cat(r, "a_declasser"), [("code-tva", ["retraites"])])


class PlusieursLivresTest(unittest.TestCase):
    """LE cas de la règle : citée par plusieurs livres, donc AUCUNE collection."""

    def test_deux_livres_declasse(self):
        r = classe_rangement(
            {"fiscalite": {"lf-2018"}, "remunerations_publiques": {"lf-2018"}},
            {"lf-2018": {"fiscalite"}})
        self.assertEqual(cat(r, "a_declasser"), [("lf-2018", ["fiscalite"])])
        self.assertEqual(cat(r, "a_ranger"), [])

    def test_trois_livres_declasse_toutes_ses_collections(self):
        r = classe_rangement(
            {"cotisations_sociales": {"smig"}, "fiscalite": {"smig"}, "retraites": {"smig"}},
            {"smig": {"fiscalite", "retraites"}})
        self.assertEqual(cat(r, "a_declasser"), [("smig", ["fiscalite", "retraites"])])

    def test_deja_sans_collection_est_bien_rangee(self):
        """Une clé partagée et sans collection est dans l'état voulu."""
        r = classe_rangement(
            {"fiscalite": {"lf-2018"}, "retraites": {"lf-2018"}}, {"lf-2018": set()})
        self.assertEqual(cat(r, "bien_rangee"), ["lf-2018"])
        self.assertEqual(cat(r, "a_declasser"), [])


class AucuneCitationTest(unittest.TestCase):
    """On ne prend AUCUNE position : signalé, jamais agi.

    Retirer une collection parce qu'on n'a trouvé aucune citation reviendrait à
    modifier une bibliothèque partagée sur la foi d'une absence — or une absence peut
    n'être qu'une recherche mal faite.
    """

    def test_signalee_sans_action(self):
        r = classe_rangement({}, {"dormante": {"fiscalite"}})
        self.assertEqual(cat(r, "sans_citation"), ["dormante"])
        self.assertEqual(cat(r, "a_declasser"), [])
        self.assertEqual(cat(r, "a_ranger"), [])

    def test_sans_citation_ni_collection(self):
        r = classe_rangement({}, {"dormante": set()})
        self.assertEqual(cat(r, "sans_citation"), ["dormante"])
        self.assertEqual(cat(r, "a_declasser"), [])


class CleInconnueDeZoteroTest(unittest.TestCase):
    """Une clé citée mais absente de Zotero n'est pas un défaut de rangement.

    Elle relève du versement, donc du bibliographe, et le contrôle ne doit pas la
    confondre avec une collection en trop.
    """

    def test_absente_de_zotero(self):
        r = classe_rangement({"fiscalite": {"neuve"}}, {})
        self.assertEqual(cat(r, "absente_de_zotero"), ["neuve"])
        self.assertEqual(cat(r, "a_ranger"), [])
        self.assertEqual(cat(r, "a_declasser"), [])


class OrdreTest(unittest.TestCase):
    """Sorties triées : un rapport de plusieurs dizaines de clés doit être lisible,
    et deux exécutions doivent se comparer."""

    def test_cles_triees(self):
        r = classe_rangement(
            {"fiscalite": {"b", "a", "c"}},
            {"a": set(), "b": set(), "c": set()})
        self.assertEqual([cle for cle, _ in cat(r, "a_ranger")], ["a", "b", "c"])

    def test_collections_triees(self):
        r = classe_rangement(
            {"fiscalite": {"x"}, "retraites": {"x"}},
            {"x": {"retraites", "fiscalite", "cotisations_sociales"}})
        self.assertEqual(cat(r, "a_declasser"),
                         [("x", ["cotisations_sociales", "fiscalite", "retraites"])])


class CasDegeneresTest(unittest.TestCase):
    def test_tout_vide(self):
        r = classe_rangement({}, {})
        for nom in ("a_declasser", "a_ranger", "bien_rangee", "sans_citation",
                    "absente_de_zotero"):
            self.assertEqual(cat(r, nom), [], nom)

    def test_livre_sans_citation(self):
        r = classe_rangement({"fiscalite": set()}, {})
        self.assertEqual(cat(r, "a_ranger"), [])


if __name__ == "__main__":
    unittest.main()

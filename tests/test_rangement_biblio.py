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

import tempfile  # noqa: E402

from push_biblio import classe_rangement, cles_citees  # noqa: E402


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


class ClesCiteesTest(unittest.TestCase):
    """Un `@nom` n'est pas toujours une citation.

    Quarto emploie la même syntaxe pour citer une référence et pour renvoyer à un
    élément numéroté — `@tbl-dc-petroliers`, `@sec-rsna`, `@fig-effectifs-fp`. Les
    seconds ne sont ni dans `references.json` ni dans Zotero.

    Mesuré le 16/09/2026, à la première exécution réelle du contrôle : 359 `@nom`
    relevés sur le corpus, dont **24 renvois** pour 335 citations. Le rapport annonçait
    38 clés « absentes de Zotero » là où il n'y en avait que 14 — et « absente de
    Zotero » est la catégorie qui appelle un versement. Le bruit pousse donc à créer
    des références qui n'ont pas lieu d'être.
    """

    def livre(self, nom_livre, fichiers):
        racine = tempfile.mkdtemp()
        base = Path(racine) / "precis" / "fr" / nom_livre
        base.mkdir(parents=True)
        for nom, texte in fichiers.items():
            cible = base / nom
            cible.parent.mkdir(parents=True, exist_ok=True)
            cible.write_text(texte, encoding="utf-8")
        return racine

    def test_les_citations_passent(self):
        r = self.livre("livre", {"index.qmd": "Voir [@loi-88-62-droit-consommation, art. 1]."})
        self.assertEqual(cles_citees("livre", r), {"loi-88-62-droit-consommation"})

    def test_les_renvois_sont_ecartes(self):
        r = self.livre("livre", {"index.qmd": "Voir @tbl-dc-petroliers et @sec-rsna et @fig-effectifs-fp."})
        self.assertEqual(cles_citees("livre", r), set())

    def test_melange(self):
        """Le cas réel : une prose qui cite ET qui renvoie."""
        r = self.livre("livre", {
            "index.qmd": "Le tarif [@decret-99-894-tarif-petroliers] figure au @tbl-dc-petroliers.",
        })
        self.assertEqual(cles_citees("livre", r), {"decret-99-894-tarif-petroliers"})

    def test_une_cle_qui_COMMENCE_comme_un_renvoi_mais_n_en_est_pas(self):
        """Le filtre porte sur le préfixe exact : `section-` n'est pas `sec-`."""
        r = self.livre("livre", {"index.qmd": "[@section-speciale-1988] et [@tbl-2016]"})
        self.assertEqual(cles_citees("livre", r), {"section-speciale-1988"})

    def test_les_tableaux_engendres_sont_lus(self):
        r = self.livre("livre", {"tables/ages.md": "| [@arrete-2020-05-19-transferts] |"})
        self.assertEqual(cles_citees("livre", r), {"arrete-2020-05-19-transferts"})

    def test_le_glossaire_est_lu_lui_aussi(self):
        """Contrairement aux ancres, les citations du glossaire comptent : elles
        résolvent contre la bibliographie du livre."""
        r = self.livre("livre", {"_glossaire.qmd": "*Source :* [@loi-88-61-tva]"})
        self.assertEqual(cles_citees("livre", r), {"loi-88-61-tva"})


class IdentiteArithmetiqueTest(unittest.TestCase):
    """Le rapport doit s'additionner — et là où il ne s'additionne pas, dire pourquoi.

    Rien n'épinglait cette identité, et la première exécution réelle l'a payé : le
    16/09/2026, `controle-rangement` a rendu 175 + 40 + 108 + 12 = 335 pour 333 clés
    annoncées. Le classement était juste ; c'était l'affichage qui suggérait une
    partition là où les deux listes de défaut SE CHEVAUCHENT, une clé mal rangée devant
    à la fois perdre une collection et en gagner une.

    Un rapport qui ne s'additionne pas se fait soupçonner tout entier, y compris dans
    ses parties exactes. D'où cette identité, vérifiée sur les clés DISTINCTES.
    """

    def identite(self, citations, collections):
        r = classe_rangement(citations, collections)
        distinctes = ({c for c, _ in r["a_declasser"]} | {c for c, _ in r["a_ranger"]})
        total = len(r["bien_rangee"]) + len(r["sans_citation"]) + len(distinctes)
        self.assertEqual(total, len(collections),
                         f"bien_rangee={r['bien_rangee']} sans_citation={r['sans_citation']} "
                         f"distinctes={sorted(distinctes)}")
        return r, distinctes

    def test_cas_simple(self):
        self.identite({"fiscalite": {"a"}}, {"a": {"fiscalite"}})

    def test_avec_chevauchement(self):
        """Deux clés dans la collection d'un mauvais livre : comptées deux fois en brut."""
        r, distinctes = self.identite(
            {"fiscalite": {"a", "b", "ok"}},
            {"a": {"retraites"}, "b": {"retraites"}, "ok": {"fiscalite"}})
        brut = len(r["a_declasser"]) + len(r["a_ranger"])
        self.assertEqual(brut - len(distinctes), 2)

    def test_melange_complet(self):
        """Les quatre situations à la fois, plus une clé absente de Zotero."""
        r, _ = self.identite(
            {"fiscalite": {"propre", "malrangee", "partagee", "neuve"},
             "retraites": {"partagee"}},
            {"propre": {"fiscalite"},
             "malrangee": {"retraites"},
             "partagee": {"fiscalite"},
             "dormante": {"retraites"}})
        self.assertEqual(r["absente_de_zotero"], ["neuve"])
        self.assertEqual(r["sans_citation"], ["dormante"])

    def test_les_absentes_de_zotero_sont_hors_du_total(self):
        """Elles ne sont pas dans `collections_par_cle` : les compter fausserait tout."""
        r, _ = self.identite({"fiscalite": {"neuve"}}, {})
        self.assertEqual(r["absente_de_zotero"], ["neuve"])


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

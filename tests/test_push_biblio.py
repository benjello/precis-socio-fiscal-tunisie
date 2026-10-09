"""Tests de la conversion CSL-JSON → Zotero, et de son inverse.

`csl_vers_zotero` est appliquée d'un bloc à toutes les références à verser : une seule
entrée qu'elle refuse arrête le versement des autres. Le 15/09/2026, un `number-of-pages`
sur un rapport bloquait ainsi 333 références ; en octobre 2026, c'est le premier chapitre
d'ouvrage collectif (`dafflon-2021-budget-local`, type CSL `chapter`) qui arrêtait tout,
le type n'étant pas dans la table.

Ces tests fixent donc trois choses : le chapitre et ses éditeurs scientifiques font
l'aller-retour sans perte ; `language` ne se perd plus à l'envoi ; et TOUTES les entrées
de TOUTES les bibliographies du dépôt se convertissent — ce dernier contrôle est celui
qui aurait vu les deux pannes le jour où l'entrée fautive a été écrite.

Le schéma Zotero vient de `tests/zotero_schema_extrait.json` : les huit types visés,
leurs champs et leurs rôles, tirés de https://api.zotero.org/schema (version 42). Le
cache `.zotero-schema.json` que lit le script est hors git ; s'en remettre à lui ferait
dépendre les tests du réseau.
"""

import glob
import json
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

from push_biblio import (  # noqa: E402
    ROLES,
    TYPES,
    champs_du_type,
    csl_vers_zotero,
    roles_du_type,
    zotero_vers_csl,
)

SCHEMA = json.loads((Path(__file__).parent / "zotero_schema_extrait.json").read_text("utf-8"))

BIBLIOGRAPHIES = sorted(
    glob.glob(str(RACINE / "precis" / "*" / "references.json"))
    + glob.glob(str(RACINE / "precis" / "*" / "*" / "references.json"))
)


def entrees(chemin):
    return json.loads(Path(chemin).read_text("utf-8"))["items"]


def entree_reelle(chemin_relatif, cle):
    return next(e for e in entrees(RACINE / chemin_relatif) if e["id"] == cle)


def aller_retour(entree):
    return zotero_vers_csl(csl_vers_zotero(entree, SCHEMA), SCHEMA)


CHAPITRE = {
    "id": "auteur-2020-chapitre",
    "type": "chapter",
    "title": "Les finances des communes",
    "title-short": "Finances des communes",
    "author": [{"family": "Ben Salah", "given": "Amel"}],
    "editor": [{"family": "Dupont", "given": "Jeanne"},
               {"literal": "Centre d'études fiscales"}],
    "translator": [{"family": "Martin", "given": "Paul"}],
    "container-author": [{"family": "Durand", "given": "Luc"}],
    "container-title": "Mélanges de droit fiscal",
    "publisher": "Presses universitaires",
    "publisher-place": "Tunis",
    "page": "11-42",
    "volume": "2",
    "ISBN": "978-9938-00-000-0",
    "DOI": "10.0000/exemple",
    "URL": "https://example.org/chapitre.pdf",
    "language": "fr",
    "issued": {"date-parts": [[2020, 5]]},
    "accessed": {"date-parts": [[2026, 10, 9]]},
    "note": "citation-key: auteur-2020-chapitre\nExemplaire consulté à la bibliothèque.",
}


class ChapitreTest(unittest.TestCase):
    """`chapter` → `bookSection`, avec les noms de champs du schéma."""

    def test_element_zotero_du_chapitre_reel(self):
        entree = entree_reelle("precis/fr/finances_locales/references.json",
                               "dafflon-2021-budget-local")
        item = csl_vers_zotero(entree, SCHEMA)
        self.assertEqual(item["itemType"], "bookSection")
        self.assertEqual(item["bookTitle"], entree["container-title"])
        self.assertNotIn("publicationTitle", item)
        self.assertEqual(item["pages"], "391-425")
        self.assertEqual(item["publisher"], entree["publisher"])
        self.assertEqual(item["place"], "Sfax")
        self.assertEqual(item["date"], "2021")
        self.assertEqual(item["url"], entree["URL"])
        self.assertEqual(item["creators"], [
            {"creatorType": "author", "firstName": "Bernard", "lastName": "Dafflon"}])
        self.assertTrue(item["extra"].startswith("citation-key: dafflon-2021-budget-local\n"))

    def test_aller_retour_du_chapitre_reel(self):
        for langue in ("fr", "ar"):
            with self.subTest(langue=langue):
                entree = entree_reelle(f"precis/{langue}/finances_locales/references.json",
                                       "dafflon-2021-budget-local")
                self.assertEqual(aller_retour(entree), entree)

    def test_aller_retour_du_chapitre_a_deux_editeurs(self):
        self.assertEqual(aller_retour(CHAPITRE), CHAPITRE)

    def test_createurs_du_chapitre_a_deux_editeurs(self):
        self.assertEqual(csl_vers_zotero(CHAPITRE, SCHEMA)["creators"], [
            {"creatorType": "author", "firstName": "Amel", "lastName": "Ben Salah"},
            {"creatorType": "editor", "firstName": "Jeanne", "lastName": "Dupont"},
            {"creatorType": "editor", "name": "Centre d'études fiscales"},
            {"creatorType": "translator", "firstName": "Paul", "lastName": "Martin"},
            {"creatorType": "bookAuthor", "firstName": "Luc", "lastName": "Durand"},
        ])

    def test_tout_champ_emis_existe_dans_le_type(self):
        """Zotero refuse l'article entier pour un seul champ inconnu du type."""
        item = csl_vers_zotero(CHAPITRE, SCHEMA)
        permis = champs_du_type("bookSection", SCHEMA) | {"itemType", "creators"}
        self.assertEqual(set(item) - permis, set())


class RolesTest(unittest.TestCase):

    def test_un_role_que_le_type_n_a_pas_est_refuse_nommement(self):
        loi = {"id": "loi-x", "type": "legislation", "title": "Loi",
               "editor": [{"literal": "Imprimerie officielle"}]}
        with self.assertRaisesRegex(ValueError, "loi-x.*editor.*statute"):
            csl_vers_zotero(loi, SCHEMA)

    def test_un_ouvrage_collectif_sans_auteur_ne_revient_pas_avec_un_auteur_vide(self):
        ouvrage = {"id": "collectif-2021", "type": "book", "title": "Transparence et droit",
                   "editor": [{"family": "Dupont", "given": "Jeanne"},
                              {"family": "Martin", "given": "Paul"}],
                   "issued": {"date-parts": [[2021]]},
                   "note": "citation-key: collectif-2021"}
        item = csl_vers_zotero(ouvrage, SCHEMA)
        self.assertEqual([c["creatorType"] for c in item["creators"]], ["editor", "editor"])
        retour = zotero_vers_csl(item, SCHEMA)
        self.assertNotIn("author", retour)
        self.assertEqual(retour["editor"], ouvrage["editor"])

    def test_chaque_role_de_la_table_existe_dans_le_schema(self):
        connus = set()
        for type_zotero in TYPES.values():
            connus |= roles_du_type(type_zotero, SCHEMA)
        self.assertEqual(set(ROLES.values()) - connus, set())

    def test_une_entree_a_seuls_auteurs_donne_l_element_d_avant(self):
        """Non-régression : cet élément est celui que le script émettait avant les rôles."""
        rapport = {"id": "ins-2020", "type": "report", "title": "Rapport annuel",
                   "author": [{"literal": "Institut national de la statistique"},
                              {"family": "Chérif", "given": "Salah Eddine"}],
                   "publisher": "INS", "issued": {"date-parts": [[2020, 3, 1]]},
                   "note": "citation-key: ins-2020"}
        self.assertEqual(csl_vers_zotero(rapport, SCHEMA), {
            "itemType": "report",
            "title": "Rapport annuel",
            "institution": "INS",
            "date": "2020-03-01",
            "creators": [
                {"creatorType": "author", "name": "Institut national de la statistique"},
                {"creatorType": "author", "firstName": "Salah Eddine", "lastName": "Chérif"},
            ],
            "extra": "citation-key: ins-2020",
        })


class LangueTest(unittest.TestCase):
    """`language` va dans le champ natif, que les huit types visés possèdent."""

    def test_les_types_vises_ont_tous_le_champ(self):
        for type_zotero in TYPES.values():
            with self.subTest(type=type_zotero):
                self.assertIn("language", champs_du_type(type_zotero, SCHEMA))

    def test_langue_conservee_sur_les_entrees_reelles(self):
        for chemin, cle in (
            ("precis/fr/cotisations_sociales/references.json", "courdescomptes2021-rapport32"),
            ("precis/fr/fiscalite/references.json", "minfin-cnf-2013-forfait"),
        ):
            with self.subTest(cle=cle):
                entree = entree_reelle(chemin, cle)
                item = csl_vers_zotero(entree, SCHEMA)
                self.assertEqual(item["language"], "ar")
                self.assertNotIn("language:", item["extra"])
                self.assertEqual(zotero_vers_csl(item, SCHEMA)["language"], "ar")


class ToutesLesBibliographiesTest(unittest.TestCase):
    """Aucune entrée du dépôt, française ou arabe, ne doit être refusée.

    Le versement convertit tout d'un bloc : une entrée refusée ici, c'est le mode à
    blanc et le versement arrêtés pour toutes les autres.
    """

    def test_les_bibliographies_sont_trouvees(self):
        self.assertGreaterEqual(len(BIBLIOGRAPHIES), 20)

    def test_toute_entree_se_convertit(self):
        refusees, total = [], 0
        for chemin in BIBLIOGRAPHIES:
            for entree in entrees(chemin):
                total += 1
                try:
                    csl_vers_zotero(entree, SCHEMA)
                except Exception as erreur:  # noqa: BLE001 — on veut la raison, quelle qu'elle soit
                    refusees.append(f"{Path(chemin).relative_to(RACINE)} — {erreur}")
        self.assertGreater(total, 2000)
        self.assertEqual(refusees, [], "\n" + "\n".join(refusees))

    def test_aucun_champ_ne_se_perd_a_l_aller_retour(self):
        """Ce que fait `--verifier`, étendu à l'arabe et à tous les fichiers."""
        pertes = []
        for chemin in BIBLIOGRAPHIES:
            for entree in entrees(chemin):
                retour = aller_retour(entree)
                for champ, valeur in entree.items():
                    if champ == "note":
                        continue
                    if json.dumps(retour.get(champ), sort_keys=True, default=str) != \
                            json.dumps(valeur, sort_keys=True, default=str) \
                            and str(retour.get(champ)) != str(valeur):
                        pertes.append(f"{Path(chemin).relative_to(RACINE)} — "
                                      f"{entree['id']} : « {champ} »")
        self.assertEqual(pertes, [], "\n" + "\n".join(pertes[:40]))


class SchemaTest(unittest.TestCase):

    def test_l_extrait_couvre_les_types_vises(self):
        self.assertEqual({t["itemType"] for t in SCHEMA["itemTypes"]}, set(TYPES.values()))

    @unittest.skipUnless((RACINE / ".zotero-schema.json").exists(),
                         "cache du schéma absent (hors git)")
    def test_l_extrait_suit_le_cache_du_schema(self):
        complet = json.loads((RACINE / ".zotero-schema.json").read_text("utf-8"))
        for type_zotero in TYPES.values():
            with self.subTest(type=type_zotero):
                self.assertEqual(champs_du_type(type_zotero, SCHEMA),
                                 champs_du_type(type_zotero, complet))
                self.assertEqual(roles_du_type(type_zotero, SCHEMA),
                                 roles_du_type(type_zotero, complet))


if __name__ == "__main__":
    unittest.main()

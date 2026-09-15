"""Tests de la répartition des références entre fichiers de livre et fonds commun.

Cette fonction décide où chaque référence bibliographique est écrite, et une erreur
n'y produit pas un plantage mais une citation non résolue dans un livre publié — ou
la même clé écrite deux fois.

Pourquoi la règle a changé : l'ancienne ne versait au fonds commun que ce qui
n'appartenait à AUCUN livre. Une descente Zotero réinjectait donc dans les fichiers de
livre les clés qui relèvent du partagé, et `push_biblio.ranger` ne peut pas les
rattraper, puisqu'il n'ajoute que des collections et n'en retire aucune.

Le corpus ne compte pour l'instant qu'une poignée de références citées par plusieurs
livres. Ces tests valent donc surtout pour la suite : ils fixent la règle avant que le
volume n'arrive.

Le cas qui compte est celui d'une loi de finances citée par la fiscalité, les
cotisations et les retraites : elle n'appartient à aucun de ces livres en propre.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from sync_biblio import (  # noqa: E402
    index_local,
    items_par_cle,
    preserve_traductions,
    preserve_urls_absentes,
    repartit_references,
)


def ref(identifiant):
    return {"id": identifiant, "title": "Titre de " + identifiant}


def ids(items):
    return [item["id"] for item in items]


class UnSeulLivreTest(unittest.TestCase):
    """Une référence propre à un livre reste dans son fichier."""

    def test_reste_dans_son_livre(self):
        livres, partage = repartit_references(
            {"fiscalite": [ref("code-irpp")]}, [ref("code-irpp")])
        self.assertEqual(ids(livres["fiscalite"]), ["code-irpp"])
        self.assertEqual(partage, [])


class PlusieursLivresTest(unittest.TestCase):
    """LE cas de la règle : citée par plusieurs livres, donc du fonds commun."""

    def test_deux_livres_promeut_au_partage(self):
        _, partage = repartit_references(
            {"fiscalite": [ref("lf-2017")], "cotisations_sociales": [ref("lf-2017")]},
            [ref("lf-2017")])
        self.assertEqual(ids(partage), ["lf-2017"])

    def test_et_disparait_des_fichiers_de_livre(self):
        """Sans ce retrait, la clé serait écrite deux fois et citée en double."""
        livres, _ = repartit_references(
            {"fiscalite": [ref("lf-2017")], "cotisations_sociales": [ref("lf-2017")]},
            [ref("lf-2017")])
        self.assertEqual(livres, {})

    def test_trois_livres(self):
        _, partage = repartit_references(
            {"fiscalite": [ref("lf-2017")],
             "cotisations_sociales": [ref("lf-2017")],
             "retraites": [ref("lf-2017")]},
            [ref("lf-2017")])
        self.assertEqual(ids(partage), ["lf-2017"])

    def test_un_livre_garde_ses_references_propres(self):
        """La promotion ne retire que la référence partagée, pas les autres."""
        livres, partage = repartit_references(
            {"fiscalite": [ref("code-irpp"), ref("lf-2017")],
             "retraites": [ref("lf-2017"), ref("loi-85-12")]},
            [ref("code-irpp"), ref("lf-2017"), ref("loi-85-12")])
        self.assertEqual(ids(livres["fiscalite"]), ["code-irpp"])
        self.assertEqual(ids(livres["retraites"]), ["loi-85-12"])
        self.assertEqual(ids(partage), ["lf-2017"])


class AucunLivreTest(unittest.TestCase):
    """Comportement conservé : ce qui n'est rangé dans aucun livre va au commun."""

    def test_reference_sans_livre(self):
        _, partage = repartit_references({}, [ref("decret-1956")])
        self.assertEqual(ids(partage), ["decret-1956"])

    def test_melange_sans_livre_et_partagee(self):
        _, partage = repartit_references(
            {"fiscalite": [ref("lf-2017")], "retraites": [ref("lf-2017")]},
            [ref("decret-1956"), ref("lf-2017")])
        self.assertEqual(ids(partage), ["decret-1956", "lf-2017"])


class OrdreTest(unittest.TestCase):
    """L'ordre d'origine est conservé — un diff de centaines de clés doit rester lisible."""

    def test_le_partage_suit_l_ordre_de_la_bibliotheque(self):
        _, partage = repartit_references(
            {"fiscalite": [ref("b")], "retraites": [ref("b")]},
            [ref("c"), ref("b"), ref("a")])
        self.assertEqual(ids(partage), ["c", "b", "a"])

    def test_le_livre_conserve_son_ordre(self):
        livres, _ = repartit_references(
            {"fiscalite": [ref("z"), ref("partagee"), ref("a")],
             "retraites": [ref("partagee")]},
            [ref("z"), ref("partagee"), ref("a")])
        self.assertEqual(ids(livres["fiscalite"]), ["z", "a"])


class CasDegeneresTest(unittest.TestCase):
    def test_tout_vide(self):
        self.assertEqual(repartit_references({}, []), ({}, []))

    def test_livre_vide_n_apparait_pas(self):
        """Un livre dont tout est promu disparaît : pas de fichier vide à écrire."""
        livres, _ = repartit_references(
            {"fiscalite": [ref("x")], "retraites": [ref("x")], "cotisations_sociales": [ref("y")]},
            [ref("x"), ref("y")])
        self.assertNotIn("fiscalite", livres)
        self.assertNotIn("retraites", livres)
        self.assertEqual(ids(livres["cotisations_sociales"]), ["y"])

    def test_items_sans_cle_ne_se_confondent_pas(self):
        """Deux items sans clé dans deux livres ne doivent pas être « promus » ensemble.

        Ils partageraient l'identifiant `None`, seraient vus comme une même référence
        citée par deux livres, et disparaîtraient de tous les fichiers de livre à la
        fois. `sans_cle_de_citation` ne les écarte qu'APRÈS cette fonction.
        """
        livres, _ = repartit_references(
            {"fiscalite": [{"title": "sans cle"}],
             "retraites": [{"title": "sans cle non plus"}]},
            [])
        self.assertEqual(len(livres["fiscalite"]), 1)
        self.assertEqual(len(livres["retraites"]), 1)

    def test_reference_du_livre_absente_de_la_bibliotheque(self):
        """Le partage se construit sur `all_items` : ce qui n'y est pas n'y entre pas."""
        _, partage = repartit_references(
            {"fiscalite": [ref("fantome")], "retraites": [ref("fantome")]}, [])
        self.assertEqual(partage, [])


class SecoursDePreservationTest(unittest.TestCase):
    """Ce qui est local et que Zotero ignore doit SUIVRE la référence qui change de côté.

    Les deux fonctions de préservation ne lisaient que le fichier de destination. Or une
    clé promue au fonds commun n'y est pas encore : elles n'y trouvaient rien, et une URL
    absente de Zotero ou un champ traduit à la main disparaissaient au premier
    déplacement — sans erreur, sans trace au rendu.
    """

    def ecrire(self, chemin, items):
        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_text(json.dumps({"items": items}, ensure_ascii=False))

    def test_items_par_cle_fichier_absent(self):
        self.assertEqual(items_par_cle("/inexistant/references.json"), {})

    def test_index_local_rassemble_partage_et_livres(self):
        with tempfile.TemporaryDirectory() as d:
            precis = Path(d)
            self.ecrire(precis / "fr" / "references.json", [ref("commune")])
            self.ecrire(precis / "fr" / "fiscalite" / "references.json", [ref("propre")])
            index = index_local(str(precis), "fr")
            self.assertEqual(sorted(index), ["commune", "propre"])

    def test_index_local_langue_absente(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(index_local(d, "ar"), {})

    def test_url_reprise_du_secours(self):
        """La clé n'est pas dans la destination : sans secours, l'URL serait perdue."""
        with tempfile.TemporaryDirectory() as d:
            destination = Path(d) / "references.json"
            self.ecrire(destination, [])
            items = [{"id": "lf-2018", "title": "Loi de finances"}]
            secours = {"lf-2018": {"id": "lf-2018",
                                   "URL": "https://www.pist.tn/jort/2017/2017F/Jo1012017.pdf"}}
            preserve_urls_absentes(items, str(destination), secours)
            self.assertEqual(items[0]["URL"],
                             "https://www.pist.tn/jort/2017/2017F/Jo1012017.pdf")

    def test_la_destination_reste_prioritaire(self):
        with tempfile.TemporaryDirectory() as d:
            destination = Path(d) / "references.json"
            self.ecrire(destination, [{"id": "x", "URL": "https://destination"}])
            items = [{"id": "x"}]
            preserve_urls_absentes(items, str(destination), {"x": {"URL": "https://secours"}})
            self.assertEqual(items[0]["URL"], "https://destination")

    def test_une_url_venue_de_zotero_n_est_pas_ecrasee(self):
        with tempfile.TemporaryDirectory() as d:
            destination = Path(d) / "references.json"
            self.ecrire(destination, [])
            items = [{"id": "x", "URL": "https://zotero"}]
            preserve_urls_absentes(items, str(destination), {"x": {"URL": "https://secours"}})
            self.assertEqual(items[0]["URL"], "https://zotero")

    def test_traduction_arabe_reprise_du_secours(self):
        with tempfile.TemporaryDirectory() as d:
            destination = Path(d) / "references.json"
            self.ecrire(destination, [])
            items = [{"id": "x", "title": "Arrêté du ministre des affaires sociales"}]
            preserve_traductions(items, str(destination),
                                 {"x": {"title": "قرار من وزير الشؤون الاجتماعية"}})
            self.assertEqual(items[0]["title"], "قرار من وزير الشؤون الاجتماعية")

    def test_sans_secours_le_comportement_est_inchange(self):
        with tempfile.TemporaryDirectory() as d:
            destination = Path(d) / "references.json"
            self.ecrire(destination, [{"id": "x", "URL": "https://destination"}])
            items = [{"id": "x"}]
            preserve_urls_absentes(items, str(destination))
            self.assertEqual(items[0]["URL"], "https://destination")


if __name__ == "__main__":
    unittest.main()

"""Tests du générateur de l'annexe « Les conventions collectives, branche par branche ».

Le générateur ne nomme aucune branche : il parcourt un nœud de paramètres. Sont donc figés
ici le parcours — ordre de l'index, descente dans les clés d'un fichier de nœud comme dans
les dossiers —, la déduction de la grille d'une case d'après les chemins, d'où vient
l'adresse de sa page publique, et la règle qui, mal tenue, tracerait un chiffre faux sans
rien faire échouer : une date sans valeur ne rend ni zéro ni la valeur précédente.

Fonctions PURES seulement, sur des dictionnaires déjà chargés : le job de tests n'installe
ni PyYAML ni pandas, et le modèle n'est pas là.
"""

import datetime
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import generate_conventions_collectives_tables as cc  # noqa: E402
import openfisca_tables as ot  # noqa: E402

PIST = "https://www.pist.tn/jort/1993/1993F/Jo07293.pdf"


def parametre(valeurs, unite="currency/mois", court="Échelon 1", sans_lien=()):
    """Un paramètre comme PyYAML le charge : dates en `datetime.date`, références en listes."""
    return {
        "description": "Salaire mensuel de base",
        "values": {datetime.date.fromisoformat(d): {"value": v} for d, v in valeurs.items()},
        "metadata": {
            "short_label": court, "unit": unite,
            "reference": {datetime.date.fromisoformat(d): [{
                "title": f"Avenant du {d}",
                **({} if d in sans_lien else {"href": PIST}),
                "note": f"JORT n° 72 du 24 septembre 1993, édition française, p. 1600. "
                        f"La grille prend effet le {d}. Valeur relevée sur le fascicule.",
            }] for d in valeurs},
        },
    }


# Une branche à deux formes de case : une clé d'un fichier de nœud (`echelle_1` → `echelon_1`)
# et un fichier de paramètre sous un dossier (`grille_b/manoeuvre`).
BRANCHE = {
    "description": "Convention collective nationale des assurances",
    "metadata": {"short_label": "Assurances", "order": ["salaire_base"]},
    "documentation": "Texte libre.",
    "salaire_base": {
        "description": "Salaires de base",
        "metadata": {"short_label": "Salaire de base", "order": ["grille_b", "echelle_1"]},
        "echelle_1": {
            "description": "Échelle 1",
            "metadata": {"short_label": "Échelle 1", "order": ["echelon_1"]},
            "echelon_2": parametre({"1999-06-01": 300.0}, court="Échelon 2"),
            "echelon_1": parametre({"1993-06-01": 181.137, "1994-06-01": 192.877,
                                    "2026-01-01": None}),
        },
        "grille_b": {
            "metadata": {"short_label": "Personnel occasionnel"},
            "manoeuvre": parametre({"1996-05-01": 0.95}, unite="currency/heure",
                                   court="Manœuvre ordinaire", sans_lien=("1996-05-01",)),
        },
    },
}


class ParcoursTest(unittest.TestCase):

    def test_l_ordre_de_l_index_puis_l_alphabet(self):
        noms = [n for n, _ in cc.enfants(BRANCHE["salaire_base"])]
        self.assertEqual(noms, ["grille_b", "echelle_1"])
        noms = [n for n, _ in cc.enfants(BRANCHE["salaire_base"]["echelle_1"])]
        self.assertEqual(noms, ["echelon_1", "echelon_2"])

    def test_les_clés_réservées_ne_sont_pas_des_enfants(self):
        self.assertEqual([n for n, _ in cc.enfants(BRANCHE)], ["salaire_base"])

    def test_toutes_les_cases_sans_liste_écrite(self):
        chemins = [c for c, _ in cc.cases(BRANCHE, ("assurances",), (BRANCHE,))]
        self.assertEqual(chemins, [
            ("assurances", "salaire_base", "grille_b", "manoeuvre"),
            ("assurances", "salaire_base", "echelle_1", "echelon_1"),
            ("assurances", "salaire_base", "echelle_1", "echelon_2"),
        ])

    def test_une_case_ajoutée_entre_sans_toucher_au_script(self):
        import copy
        arbre = copy.deepcopy(BRANCHE)
        arbre["indemnites"] = {"metadata": {"short_label": "Indemnités"},
                               "transport": parametre({"2017-06-01": 85.0}, court="Transport")}
        chemins = [c for c, _ in cc.cases(arbre, ("assurances",), (arbre,))]
        self.assertIn(("assurances", "indemnites", "transport"), chemins)
        self.assertEqual(len(chemins), 4)

    def test_descente_dans_un_fichier_de_nœud(self):
        fichier = BRANCHE["salaire_base"]["echelle_1"]
        self.assertIs(ot.descend(fichier, ["echelon_1"]), fichier["echelon_1"])
        self.assertIsNone(ot.descend(fichier, ["echelon_9"]))
        self.assertIsNone(ot.descend(fichier, ["description", "x"]))


class LibellesTest(unittest.TestCase):

    def fiche(self, *chemin):
        lignee, noeud = [BRANCHE], BRANCHE
        for nom in chemin:
            noeud = noeud[nom]
            lignee.append(noeud)
        return cc.fiche_case(("assurances",) + chemin, tuple(lignee))

    def test_libellé_tiré_des_nœuds(self):
        f = self.fiche("salaire_base", "echelle_1", "echelon_1")
        self.assertEqual(f["libelle"], "Échelle 1, échelon 1")
        self.assertEqual(f["grandeur"], "Salaire de base")
        self.assertEqual(f["unite"], "dinars par mois")
        self.assertEqual(cc.libelle_lien("Assurances", f),
                         "Assurances — échelle 1, échelon 1 : salaire de base (dinars par mois)")

    def test_chemin_de_la_page_publique(self):
        f = self.fiche("salaire_base", "echelle_1", "echelon_1")
        self.assertNotIn("tableau", f)
        self.assertTrue(ot.url_parametre(f["parametre"]).endswith(
            "/marche_travail.conventions_collectives.assurances.salaire_base.echelle_1."
            "echelon_1/table/"))

    def test_comptes_valeurs_et_dates_sans_valeur(self):
        f = self.fiche("salaire_base", "echelle_1", "echelon_1")
        self.assertEqual((f["dates"], f["valeurs"], f["sans_valeur"]), (3, 2, 1))
        self.assertEqual((f["debut"], f["derniere_valeur"]), ("1993-06-01", "1994-06-01"))

    def test_unité(self):
        self.assertEqual(cc.unite({"metadata": {"unit": "currency/heure"}}), "dinars par heure")
        self.assertEqual(cc.unite({"metadata": {"unit": "currency/mois"}}, "ar"),
                         "دينار في الشهر")
        self.assertEqual(cc.unite({"metadata": {}}), "")
        self.assertEqual(cc.unite({"metadata": {"unit": "/1"}}), "")


class SerieTest(unittest.TestCase):

    def test_une_date_sans_valeur_n_est_ni_zéro_ni_la_précédente(self):
        p = BRANCHE["salaire_base"]["echelle_1"]["echelon_1"]
        self.assertEqual([(d, v) for d, v, *_ in cc.serie(p)],
                         [("1993-06-01", 181.137), ("1994-06-01", 192.877),
                          ("2026-01-01", None)])

    def test_le_texte_et_son_lien_suivent_la_date(self):
        avec = cc.serie(BRANCHE["salaire_base"]["echelle_1"]["echelon_1"])[0]
        self.assertEqual(avec[2:4], ("Avenant du 1993-06-01", PIST))
        sans = cc.serie(BRANCHE["salaire_base"]["grille_b"]["manoeuvre"])[0]
        self.assertEqual(sans[2:4], ("Avenant du 1996-05-01", ""))


def branche(nom, grandeur):
    """Une branche à une grandeur, `salaire_base`, de structure donnée."""
    return (nom, {"metadata": {"short_label": nom.capitalize()},
                  "salaire_base": {"metadata": {"short_label": "Salaire de base"}, **grandeur}})


def case(unite="currency/heure", court="Échelon 0"):
    return parametre({"1996-05-01": 1.0}, unite=unite, court=court)


def noeud(court, **enfants):
    return {"metadata": {"short_label": court}, **enfants}


class GrillesTest(unittest.TestCase):
    """La grille d'une case se déduit des chemins : aucune n'est nommée dans le générateur.

    Les trois formes sont celles des branches versées — une grandeur à plusieurs grilles de
    catégories à échelons, une grille de catégories sans échelon, une grandeur qui est
    elle-même la grille de ses échelles.
    """

    BASE = ("https://parameters.tn.tax-benefit.org/parameters/"
            "marche_travail.conventions_collectives.")

    def grilles(self, nom, grandeur, langue="fr"):
        nom, arbre = branche(nom, grandeur)
        return cc.grilles(cc.cases(arbre, (nom,), (arbre,)), langue)

    def test_catégories_à_échelons_sous_une_grille_nommée(self):
        g, = self.grilles("textile", {"agents_payes_a_l_heure": noeud(
            "Agents payés à l'heure",
            categorie_1=noeud("Catégorie I", echelon_0=case()),
            categorie_4_2=noeud("Catégorie IV-2", echelon_0=case()))})
        self.assertEqual(g["cle"], "salaire_base.agents_payes_a_l_heure")
        self.assertEqual(ot.url_parametre(g["parametre"]),
                         self.BASE + "textile.salaire_base.agents_payes_a_l_heure/table/")
        self.assertEqual(g["cases"], ["salaire_base.agents_payes_a_l_heure.categorie_1.echelon_0",
                                      "salaire_base.agents_payes_a_l_heure.categorie_4_2.echelon_0"])
        self.assertEqual(cc.libelle_lien_grille("Textile", g),
                         "Textile — agents payés à l'heure : salaire de base, cases de la grille "
                         "(dinars par heure)")

    def test_catégories_sans_échelon(self):
        g, = self.grilles("batiment", {"personnel_occasionnel": noeud(
            "Personnel occasionnel", manoeuvre_ordinaire=case(court="Manœuvre ordinaire"),
            chef_equipe_3e_degre=case(court="Chef d'équipe du 3e degré"))})
        self.assertEqual(ot.url_parametre(g["parametre"]),
                         self.BASE + "batiment.salaire_base.personnel_occasionnel/table/")

    def test_la_grandeur_est_la_grille_de_ses_échelles(self):
        g, = self.grilles("assurances", {
            "echelle_1": noeud("Échelle 1", echelon_1=case("currency/mois")),
            "echelle_21": noeud("Échelle 21", echelon_12=case("currency/mois"),
                                echelon_14=case("currency/mois"))})
        self.assertEqual(ot.url_parametre(g["parametre"], "ar"),
                         self.BASE.replace("/parameters/", "/ar/parameters/")
                         + "assurances.salaire_base/table/")
        self.assertEqual(g["libelle"], "")
        self.assertEqual(cc.libelle_lien_grille("Assurances", g),
                         "Assurances : salaire de base, cases de la grille (dinars par mois)")

    def test_deux_unités_deux_grilles(self):
        horaire, mensuelle = self.grilles("textile", {
            "agents_payes_a_l_heure": noeud(
                "Agents payés à l'heure",
                categorie_1=noeud("Catégorie I", echelon_0=case()),
                categorie_4_2=noeud("Catégorie IV-2", echelon_0=case())),
            "agents_payes_au_mois": noeud(
                "Agents payés au mois",
                categorie_1=noeud("Catégorie 1", echelon_0=case("currency/mois")),
                categorie_17=noeud("Catégorie 17", echelon_0=case("currency/mois")))})
        self.assertEqual(horaire["cle"], "salaire_base.agents_payes_a_l_heure")
        self.assertEqual(mensuelle["cle"], "salaire_base.agents_payes_au_mois")
        self.assertEqual(mensuelle["unite"], "dinars par mois")

    def test_une_case_seule_a_pour_grille_le_nœud_qui_la_contient(self):
        g, = self.grilles("batiment", {"personnel_occasionnel": noeud(
            "Personnel occasionnel", manoeuvre_ordinaire=case())})
        self.assertEqual(g["cle"], "salaire_base.personnel_occasionnel")

    def test_jamais_au_dessus_de_la_grandeur(self):
        g, = self.grilles("x", {"taux_unique": case()})
        self.assertEqual(g["cle"], "salaire_base")


if __name__ == "__main__":
    unittest.main()

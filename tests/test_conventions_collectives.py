"""Tests du générateur de l'annexe « Les conventions collectives, branche par branche ».

Le générateur ne nomme aucune branche : il parcourt un nœud de paramètres. Sont donc figés
ici le parcours — ordre de l'index, descente dans les clés d'un fichier de nœud comme dans
les dossiers —, la déduction de la grille d'une case d'après les chemins, d'où vient
l'adresse de sa page publique, et la règle qui, mal tenue, tracerait un chiffre faux sans
rien faire échouer : une date sans valeur ne rend ni zéro ni la valeur précédente.

Sont figées aussi les règles qui choisissent ce que l'annexe trace, grille par grille : le
bas et le haut pris à la dernière date publiée de la grille, parmi les lignes qui y sont
encore ; la colonne de stage, qui n'est pas un échelon ; les trois espèces de valeur vide
(case illisible, ligne close, grille non publiée) ; et la grille antérieure ou d'une seule
date, qui n'a pas de courbe — sur une structure qui imite les deux nœuds que la PR n° 490
d'openfisca-tunisia ajoute aux assurances.

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


def valeurs(dates_valeurs):
    """Une série de case comme `cc.serie` la rend, réduite à (date, valeur)."""
    return [(d, v) for d, v in dates_valeurs]


class ValeursVidesTest(unittest.TestCase):
    """Une valeur vide dit trois choses différentes, que la forme de la grille distingue."""

    SERIES = {
        # illisible en tête de série, puis lue
        "a": valeurs([("1996", None), ("1997", 2.0), ("1998", 3.0), ("2026", None)]),
        # illisible au milieu : reprend ensuite
        "b": valeurs([("1996", 5.0), ("1997", None), ("1998", 6.0), ("2026", None)]),
        # ligne close en 1998 : plus aucune date ensuite
        "c": valeurs([("1996", 1.0), ("1997", 1.5), ("1998", None)]),
        # ligne qui commence en cours de série
        "d": valeurs([("1998", 4.0), ("1999", 4.5), ("2026", None)]),
    }

    def test_les_trois_espèces(self):
        e = cc.etat_grille(self.SERIES)
        self.assertEqual(e["dates_publiees"], ["1996", "1997", "1998", "1999"])
        self.assertEqual((e["debut"], e["fin"], e["cloture"]), ("1996", "1999", "2026"))
        self.assertEqual(e["cases_vides"], 2)            # a en 1996, b en 1997
        self.assertEqual(e["dates_cases_vides"], ["1996", "1997"])
        self.assertEqual(e["lignes_closes"], 1)          # c en 1998
        self.assertEqual(e["non_publiees"], 3)           # a, b et d en 2026
        self.assertEqual(e["valeurs"], 8)

    def test_une_case_vide_à_la_dernière_date_publiée_est_illisible(self):
        e = cc.etat_grille({"a": valeurs([("1996", 1.0), ("1997", None)]),
                            "b": valeurs([("1996", 2.0), ("1997", 3.0)])})
        self.assertEqual((e["cases_vides"], e["lignes_closes"], e["cloture"]), (1, 0, None))

    def test_une_valeur_vide_n_est_pas_reportée(self):
        self.assertIsNone(cc.en_vigueur(self.SERIES["b"], "1997"))
        self.assertEqual(cc.en_vigueur(self.SERIES["b"], "1996"), 5.0)
        self.assertEqual(cc.en_vigueur(self.SERIES["b"], "1999"), 6.0)
        self.assertIsNone(cc.en_vigueur(self.SERIES["d"], "1997"))   # avant sa première date
        self.assertIsNone(cc.en_vigueur(self.SERIES["c"], "1999"))   # après sa clôture

    def test_le_début_d_une_case_est_sa_première_valeur(self):
        f = cc.fiche_case(("x", "salaire_base", "a"), (
            {}, {"metadata": {"short_label": "Salaire de base"}},
            parametre({"1996-05-01": None, "1997-05-01": 2.0, "2026-01-01": None})))
        self.assertEqual((f["debut"], f["derniere_valeur"]), ("1997-05-01", "1997-05-01"))
        self.assertEqual((f["dates"], f["valeurs"], f["sans_valeur"]), (3, 1, 2))


class FormesTest(unittest.TestCase):
    """La forme d'une grille — lignes, colonnes, cases — se compte date par date."""

    def test_des_colonnes_ajoutées_en_cours_de_série(self):
        series = {"l1.e1": valeurs([("1994", 1.0), ("1999", None), ("2000", 3.0)]),
                  "l1.e2": valeurs([("1999", 2.0), ("2000", 3.0)]),
                  "l2.e1": valeurs([("1994", 1.0), ("1999", 2.0), ("2000", 3.0)]),
                  "l2.e2": valeurs([("1999", 2.0), ("2000", 3.0)])}
        place = {c: tuple(c.split(".")) for c in series}
        self.assertEqual(cc.formes(series, place), [
            {"depuis": "1994", "jusqu_a": "1994", "lignes": 2, "colonnes": 1, "cases": 2},
            # la case illisible de 1999 est une case de la grille
            {"depuis": "1999", "jusqu_a": "2000", "lignes": 2, "colonnes": 2, "cases": 4}])

    def test_une_ligne_close_et_deux_lignes_nouvelles(self):
        series = {"a": valeurs([("1996", 1.0), ("2008", 2.0), ("2024", 3.0), ("2026", None)]),
                  "b": valeurs([("1996", 9.0), ("2008", None)]),
                  "b1": valeurs([("2008", 2.5), ("2024", 3.5), ("2026", None)]),
                  "b2": valeurs([("2008", 2.7), ("2024", 3.7), ("2026", None)])}
        place = {c: (c, "") for c in series}
        self.assertEqual(cc.formes(series, place), [
            {"depuis": "1996", "jusqu_a": "1996", "lignes": 2, "colonnes": 1, "cases": 2},
            # la date qui clôt « b » ne la compte plus ; la grille non publiée n'a pas de forme
            {"depuis": "2008", "jusqu_a": "2024", "lignes": 3, "colonnes": 1, "cases": 3}])


class BasEtHautTest(unittest.TestCase):
    """Le bas et le haut se prennent à la dernière date publiée, parmi les lignes présentes."""

    def test_une_ligne_close_n_est_pas_le_bas_par_sa_vieille_valeur(self):
        # « c » a la plus basse des dernières valeurs (1,5 en 1997), mais elle est close.
        self.assertEqual(cc.bas_et_haut(ValeursVidesTest.SERIES), ("a", "b"))

    def test_une_ligne_qui_commence_en_cours_de_série_concourt_si_elle_est_présente(self):
        series = {"ancienne": valeurs([("1996", 9.0), ("2008", None)]),
                  "basse": valeurs([("1996", 1.0), ("2008", 2.0)]),
                  "nouvelle": valeurs([("2008", 7.0)])}
        self.assertEqual(cc.bas_et_haut(series), ("basse", "nouvelle"))

    def test_une_case_illisible_à_la_dernière_date_ne_concourt_pas(self):
        series = {"a": valeurs([("1996", 1.0), ("1997", None)]),
                  "b": valeurs([("1996", 2.0), ("1997", 3.0)]),
                  "c": valeurs([("1996", 4.0), ("1997", 5.0)])}
        self.assertEqual(cc.bas_et_haut(series), ("b", "c"))

    def test_le_choix_ne_regarde_pas_la_grille_non_publiée(self):
        series = {"a": valeurs([("2024", 1.0), ("2026", None)]),
                  "b": valeurs([("2024", 2.0), ("2026", None)])}
        self.assertEqual(cc.bas_et_haut(series), ("a", "b"))

    def test_à_égalité_la_première_en_bas_la_dernière_en_haut(self):
        series = {k: valeurs([("2024", 1.0)]) for k in "abc"}
        self.assertEqual(cc.bas_et_haut(series), ("a", "c"))

    def test_les_cases_écartées_ne_concourent_pas(self):
        series = {"stage": valeurs([("2024", 0.5)]), "e1": valeurs([("2024", 1.0)]),
                  "e2": valeurs([("2024", 2.0)])}
        self.assertEqual(cc.bas_et_haut(series, {"stage"}), ("e1", "e2"))
        self.assertIsNone(cc.bas_et_haut(series, {"stage", "e1", "e2"}))

    def test_grille_sans_valeur(self):
        self.assertIsNone(cc.bas_et_haut({"a": valeurs([("2024", None)])}))


class HorsRangTest(unittest.TestCase):

    ECHELONS = ["stage"] + [f"echelon_{i}" for i in range(1, 21)]

    def test_le_stage_n_est_pas_un_échelon(self):
        self.assertTrue(cc.hors_rang("stage", self.ECHELONS))
        self.assertFalse(cc.hors_rang("echelon_1", self.ECHELONS))
        self.assertFalse(cc.hors_rang("echelon_20", self.ECHELONS))

    def test_des_échelons_seuls(self):
        freres = [f"echelon_{i}" for i in range(0, 21)]
        self.assertFalse(any(cc.hors_rang(n, freres) for n in freres))

    def test_des_emplois_nommés_ne_sont_pas_des_colonnes_numérotées(self):
        emplois = ["manoeuvre_ordinaire", "aide_ouvrier", "ouvrier_hautement_qualifie",
                   "ouvrier_hautement_qualifie_1", "ouvrier_hautement_qualifie_2",
                   "chef_equipe_1er_degre", "chef_equipe_3e_degre"]
        self.assertFalse(any(cc.hors_rang(n, emplois) for n in emplois))

    def test_une_case_seule(self):
        self.assertFalse(cc.hors_rang("taux_unique", ["taux_unique"]))


def ligne(court, colonnes, unite="currency/mois"):
    """Une ligne de grille : {nom de colonne: {date: valeur}} -> nœud à cases."""
    return noeud(court, **{nom: parametre(v, unite=unite, court=nom.replace("_", " ").capitalize())
                           for nom, v in colonnes.items()})


def grille_synthetique(dates, n_lignes=3, n_colonnes=2, base=100.0, pas=10.0, clos=None,
                       prefixe="echelle"):
    """`n_lignes` × `n_colonnes` cases croissantes, aux `dates` ; `clos` : date de clôture."""
    lignes = {}
    for i in range(1, n_lignes + 1):
        colonnes = {}
        for j in range(1, n_colonnes + 1):
            v = {d: base + pas * (i * n_colonnes + j) + rang for rang, d in enumerate(dates)}
            if clos:
                v[clos] = None
            colonnes[f"echelon_{j}"] = v
        lignes[f"{prefixe}_{i}"] = ligne(f"Échelle {i}", colonnes)
    return lignes


class GrillesTraceesTest(unittest.TestCase):
    """Chaque grille courante a son bas et son haut ; une grille antérieure, ou d'une ou deux
    dates, n'a pas de courbe."""

    def entree(self, nom, arbre):
        return cc.entree_branche(nom, arbre)

    def test_deux_grilles_d_une_branche_chacune_son_bas_et_son_haut(self):
        # La grille mensuelle a une colonne de stage, plus basse que l'échelon 1 à la
        # dernière date : le bas reste l'échelon 1, celui de la confirmation.
        dates = ["1994-05-01", "2008-05-01", "2026-01-01"]
        horaire = noeud("Agents payés à l'heure", **{
            f"categorie_{i}": ligne(f"Catégorie {i}", {
                f"echelon_{j}": {d: i + j / 10 + r for r, d in enumerate(dates)}
                for j in range(0, 3)}, unite="currency/heure") for i in (1, 2)})
        mensuelle = noeud("Agents payés au mois", **{
            f"categorie_{i}": ligne(f"Catégorie {i}", {
                "stage": {dates[0]: 100.0 * i + 1, dates[1]: 100.0 * i, dates[2]: 100.0 * i},
                "echelon_1": {dates[0]: 100.0 * i + 1, dates[1]: 100.0 * i + 5,
                              dates[2]: 100.0 * i + 9},
                "echelon_2": {dates[0]: None, dates[1]: 100.0 * i + 20,
                              dates[2]: 100.0 * i + 30}}) for i in (1, 2)})
        nom, arbre = branche("textile", {"agents_payes_a_l_heure": horaire,
                                         "agents_payes_au_mois": mensuelle})
        entree, liens = self.entree(nom, arbre)
        h, m = entree["grilles"]
        self.assertEqual((h["unite"], m["unite"]), ("dinars par heure", "dinars par mois"))
        self.assertTrue(h["tracee"] and m["tracee"])
        self.assertEqual((h["lignes"], h["colonnes"], h["cases"]), (2, 3, 6))
        self.assertEqual((m["lignes"], m["colonnes"], m["cases"]), (2, 3, 6))
        self.assertEqual(m["formes"], [{"depuis": "1994-05-01", "jusqu_a": "2026-01-01",
                                        "lignes": 2, "colonnes": 3, "cases": 6}])
        self.assertEqual(h["bas"]["cle"], "salaire_base.agents_payes_a_l_heure.categorie_1.echelon_0")
        self.assertEqual(h["haut"]["cle"], "salaire_base.agents_payes_a_l_heure.categorie_2.echelon_2")
        # le bas et le haut de la grille mensuelle ne viennent pas de la grille horaire
        self.assertEqual(m["bas"]["cle"], "salaire_base.agents_payes_au_mois.categorie_1.echelon_1")
        self.assertEqual(m["haut"]["cle"], "salaire_base.agents_payes_au_mois.categorie_2.echelon_2")
        self.assertEqual(m["hors_rang"], ["Stage"])
        self.assertEqual(h["hors_rang"], [])
        # deux cases illisibles en tête de série, comptées une fois chacune
        self.assertEqual((m["cases_vides"], m["dates_cases_vides"]), (2, ["1994-05-01"]))
        self.assertEqual((entree["cases"], entree["cases_vides"]), (12, 2))
        self.assertEqual(m["serie"], "cc-grille-textile-salaire-base-agents-payes-au-mois")
        self.assertNotIn("dates_publiees", m)
        self.assertEqual([l["grille"] for l in liens], [h["cle"], m["cle"]])

    def test_ligne_close_et_lignes_nouvelles(self):
        # Le bâtiment de 2008 : une ligne close, dont la dernière valeur est la plus haute
        # de toutes les « dernières valeurs », et deux lignes qui commencent à cette date.
        d = {"1996-05-01": 1.0, "2008-05-01": 2.0, "2024-01-01": 3.0, "2026-01-01": None}
        occasionnel = noeud("Personnel occasionnel", **{
            "manoeuvre": parametre(d, unite="currency/heure", court="Manœuvre"),
            "ouvrier": parametre({"1996-05-01": 9.0, "2008-05-01": None},
                                 unite="currency/heure", court="Ouvrier"),
            "ouvrier_1": parametre({"2008-05-01": 2.5, "2024-01-01": 3.5, "2026-01-01": None},
                                   unite="currency/heure", court="Ouvrier I"),
            "ouvrier_2": parametre({"2008-05-01": 2.7, "2024-01-01": 3.7, "2026-01-01": None},
                                   unite="currency/heure", court="Ouvrier II"),
            "chef": parametre({k: (v and v + 2) for k, v in d.items()},
                              unite="currency/heure", court="Chef d'équipe")})
        nom, arbre = branche("batiment", {"personnel_occasionnel": occasionnel})
        (g,), _liens = self.entree(nom, arbre)[0]["grilles"], None
        self.assertEqual(g["bas"]["cle"], "salaire_base.personnel_occasionnel.manoeuvre")
        self.assertEqual(g["haut"]["cle"], "salaire_base.personnel_occasionnel.chef")
        self.assertEqual((g["lignes"], g["colonnes"], g["cases"]), (5, 0, 5))
        self.assertEqual([(f["depuis"], f["jusqu_a"], f["lignes"], f["colonnes"], f["cases"])
                          for f in g["formes"]],
                         [("1996-05-01", "1996-05-01", 3, 1, 3),
                          ("2008-05-01", "2024-01-01", 4, 1, 4)])
        self.assertEqual((g["lignes_closes"], g["cases_vides"]), (1, 0))
        # grille non publiée en 2026, sans grille qui lui succède : elle reste courante
        self.assertEqual((g["fin"], g["cloture"], g["tracee"], g["motif"]),
                         ("2024-01-01", "2026-01-01", True, "courante"))
        self.assertEqual(g["hors_rang"], [])

    def assurances_avec_grilles_anterieures(self):
        """La forme de la PR n° 490 : trois nœuds frères sous la branche, de même unité.

        `salaire_base` (1993-2021, non publiée en 2026) ; `salaire_base_avant_1993`
        (1975-1992, close au 1er juin 1993, une case illisible) ; et la grille n° 1 de 1990,
        d'une seule date, close au 1er juin 1991, dont les montants sont les plus bas de tous.
        """
        courante = grille_synthetique(
            ["1993-06-01", "1999-06-01", "2021-06-01"], base=200.0, clos="2026-01-01")
        avant = grille_synthetique(
            ["1975-01-01", "1983-01-01", "1989-01-01", "1990-06-01", "1991-06-01",
             "1992-06-01"], base=50.0, clos="1993-06-01")
        avant["echelle_1"]["echelon_1"]["values"][datetime.date(1989, 1, 1)] = {"value": None}
        grille_1 = grille_synthetique(["1990-06-01"], base=1.0, clos="1991-06-01")
        arbre = {"metadata": {"short_label": "Assurances",
                              "order": ["salaire_base", "salaire_base_avant_1993",
                                        "salaire_base_avant_1993_grille_1_de_1990"]},
                 "salaire_base": {"metadata": {"short_label": "Salaire de base"}, **courante},
                 "salaire_base_avant_1993": {
                     "metadata": {"short_label": "Salaire de base hors indemnité"}, **avant},
                 "salaire_base_avant_1993_grille_1_de_1990": {
                     "metadata": {"short_label": "Salaire de base, grille n° 1 de 1990"},
                     **grille_1}}
        return cc.entree_branche("assurances", arbre)

    def test_structure_de_la_pr_490(self):
        entree, liens = self.assurances_avec_grilles_anterieures()
        courante, avant, grille_1 = entree["grilles"]
        self.assertEqual([g["cle"] for g in entree["grilles"]],
                         ["salaire_base", "salaire_base_avant_1993",
                          "salaire_base_avant_1993_grille_1_de_1990"])
        self.assertEqual([(g["tracee"], g["motif"]) for g in entree["grilles"]],
                         [(True, "courante"), (False, "anterieure"), (False, "peu_de_dates")])
        # Le bas tracé est celui de la grille courante, non la case — plus basse — de la
        # grille n° 1 de 1990, qui n'a qu'une date.
        self.assertEqual(courante["bas"]["cle"], "salaire_base.echelle_1.echelon_1")
        self.assertEqual(courante["haut"]["cle"], "salaire_base.echelle_3.echelon_2")
        self.assertEqual(courante["bas"]["debut"], "1993-06-01")
        for g in (avant, grille_1):
            self.assertNotIn("bas", g)
            self.assertNotIn("haut", g)
            self.assertNotIn("serie", g)
        self.assertEqual((avant["dates"], avant["debut"], avant["fin"], avant["cloture"]),
                         (6, "1975-01-01", "1992-06-01", "1993-06-01"))
        self.assertEqual((avant["cases_vides"], avant["dates_cases_vides"]), (1, ["1989-01-01"]))
        self.assertEqual((grille_1["dates"], grille_1["debut"], grille_1["cloture"]),
                         (1, "1990-06-01", "1991-06-01"))
        self.assertEqual(entree["cases_vides"], 1)
        # chaque grille garde son lien, tracée ou non
        self.assertEqual(list(dict.fromkeys(l["grille"] for l in liens)),
                         [g["cle"] for g in entree["grilles"]])
        self.assertEqual(
            liens[1]["libelle"],
            "Assurances : salaire de base hors indemnité, cases de la grille (dinars par mois)")

    def test_la_série_d_une_grille_ne_porte_que_son_bas_et_son_haut(self):
        entree, _liens = self.assurances_avec_grilles_anterieures()
        declares = cc.parametres_dates(entree, entree["grilles"][0])
        self.assertEqual([p.cle for p in declares],
                         ["salaire_base.echelle_1.echelon_1", "salaire_base.echelle_3.echelon_2"])

    def test_marque_tracees(self):
        def etat(unite, dates, cloture=None):
            return {"unite": unite, "dates_publiees": dates, "debut": dates[0] if dates else None,
                    "cloture": cloture}
        # close, mais aucune grille de même unité ne lui succède : courante
        self.assertEqual(cc.marque_tracees([
            etat("h", ["1996", "1997", "1998"], "2026"),
            etat("m", ["1996", "1997", "2027"])]),
            [(True, "courante"), (True, "courante")])
        # deux dates ne font pas une évolution
        self.assertEqual(cc.marque_tracees([etat("h", ["1996", "1997"])]),
                         [(False, "peu_de_dates")])
        self.assertEqual(cc.marque_tracees([etat("h", [])]), [(False, "sans_valeur")])
        # une grille de même unité commence à la date de clôture : antérieure
        self.assertEqual(cc.marque_tracees([
            etat("m", ["1975", "1983", "1989"], "1993"), etat("m", ["1993", "1994", "1995"])]),
            [(False, "anterieure"), (True, "courante")])
        # une grille d'une autre unité ne lui succède pas
        self.assertEqual(cc.marque_tracees([
            etat("m", ["1975", "1983", "1989"], "1993"), etat("h", ["1993", "1994", "1995"])]),
            [(True, "courante"), (True, "courante")])


class LiensGrilleTest(unittest.TestCase):
    """La vue en tableau d'un nœud n'existe qu'en deçà de 200 cases : au-delà, une par ligne."""

    def grille(self, n_lignes, n_colonnes):
        nom, arbre = branche("assurances", grille_synthetique(
            ["1993-06-01"], n_lignes=n_lignes, n_colonnes=n_colonnes))
        g, = cc.grilles(cc.cases(arbre, (nom,), (arbre,)))
        return g

    def test_grille_entière_en_deçà_du_plafond(self):
        g = self.grille(19, 10)                                   # 190 cases
        lien, = cc.liens_grille("Assurances", g)
        self.assertEqual(lien["parametre"], g["parametre"])
        self.assertEqual((lien["grille"], lien["ligne"]), ("salaire_base", ""))
        self.assertEqual(lien["libelle"], lien["libelle_grille"])

    def test_un_lien_par_ligne_au_delà(self):
        g = self.grille(20, 10)                                   # 200 cases
        liens = cc.liens_grille("Assurances", g)
        self.assertEqual(len(liens), 20)
        self.assertEqual(liens[0]["ligne"], "Échelle 1")
        self.assertTrue(ot.url_parametre(liens[0]["parametre"]).endswith(
            ".assurances.salaire_base.echelle_1/table/"))
        self.assertEqual(liens[0]["libelle"],
                         "Assurances — échelle 1 : salaire de base, cases de la ligne "
                         "(dinars par mois)")
        self.assertEqual(liens[0]["libelle_grille"],
                         "Assurances : salaire de base, cases de la grille (dinars par mois)")
        self.assertEqual({l["grille"] for l in liens}, {"salaire_base"})

    def test_ligne_sous_une_grille_nommée(self):
        g = {"libelle": "Agents payés au mois", "grandeur": "Salaire de base",
             "unite": "dinars par mois"}
        self.assertEqual(cc.libelle_lien_grille("Textile", g, ligne="Catégorie 1A"),
                         "Textile — agents payés au mois, catégorie 1A : salaire de base, "
                         "cases de la ligne (dinars par mois)")


if __name__ == "__main__":
    unittest.main()

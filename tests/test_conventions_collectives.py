"""Tests du générateur de l'annexe « Les conventions collectives, branche par branche ».

Le générateur ne nomme aucune branche : il parcourt un nœud de paramètres. Sont donc figés
ici le parcours — ordre de l'index, descente dans les clés d'un fichier de nœud comme dans
les dossiers — et les trois règles qui, mal tenues, imprimeraient un chiffre faux sans rien
faire échouer : une date sans valeur ne rend ni zéro ni la valeur précédente ; un montant
garde ses trois décimales ; la note d'un relevé ne passe pas dans le tableau, hors sa
localisation au Journal officiel.

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

    def test_chemin_de_la_page_publique_et_nom_du_tableau(self):
        f = self.fiche("salaire_base", "echelle_1", "echelon_1")
        self.assertEqual(f["tableau"], "cc_assurances_salaire_base_echelle_1_echelon_1.md")
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


class CellulesTest(unittest.TestCase):

    def test_une_date_sans_valeur_n_est_ni_zéro_ni_la_précédente(self):
        p = BRANCHE["salaire_base"]["echelle_1"]["echelon_1"]
        lignes = cc.lignes_case(p)
        self.assertEqual([l[1] for l in lignes], ["181,137", "192,877", "non publiée"])
        self.assertEqual(cc.montant(None, "ar"), "غير منشورة")
        self.assertEqual(cc.montant(0.0), "0,000")

    def test_trois_décimales_toujours(self):
        self.assertEqual(cc.montant(0.95), "0,950")
        self.assertEqual(cc.montant(2.41), "2,410")
        self.assertEqual(cc.montant(1598.617), "1 598,617")
        self.assertEqual(cc.montant(1002.9), "1 002,900")

    def test_la_date_ne_se_coupe_pas(self):
        self.assertEqual(cc.date_insecable("1993-06-01"), "[1^er^ juin 1993]{.insecable}")
        self.assertEqual(cc.date_insecable("2005-06-15"), "[15 juin 2005]{.insecable}")

    def test_seule_la_localisation_passe_de_la_note_au_tableau(self):
        cas = {
            "JORT n° 72 du 24 septembre 1993, édition française, p. 1600. La grille prend "
            "effet le 1er juin 1993 ; valeur relevée.":
                "n° 72 du 24 septembre 1993, édition française, p. 1600",
            "JORT n° 44 du 30 avril 2026, pp. 838-839. Article premier : hausse de 5 %.":
                "n° 44 du 30 avril 2026, pp. 838-839",
            "JORT n° 4 du 13 janvier 2015, édition arabe, p. 151. Suite.":
                "n° 4 du 13 janvier 2015, édition arabe, p. 151",
            "JORT n° 7 du 24 janvier 2006, édition arabe, p. 7.": "n° 7 du 24 janvier 2006, "
                                                                  "édition arabe, p. 7",
            "Valeur relevée sur une copie.": "—",
            "": "—",
        }
        for note, attendu in cas.items():
            self.assertEqual(cc.journal(note), attendu, note)

    def test_le_texte_porte_son_lien_ou_reste_nu(self):
        avec = cc.lignes_case(BRANCHE["salaire_base"]["echelle_1"]["echelon_1"])[0]
        self.assertEqual(avec[2], f"[Avenant du 1993-06-01]({PIST})")
        sans = cc.lignes_case(BRANCHE["salaire_base"]["grille_b"]["manoeuvre"])[0]
        self.assertEqual(sans[2], "Avenant du 1996-05-01")

    def test_tableau_d_une_case(self):
        p = BRANCHE["salaire_base"]["grille_b"]["manoeuvre"]
        texte = cc.tableau_case("Salaire de base", p).splitlines()
        self.assertEqual(texte[0], "| Date d'effet | Salaire de base<br>(dinars par heure) | "
                                   "Texte | *Journal officiel* |")
        self.assertEqual(texte[1], "|---|---:|---|---|")
        self.assertEqual(len(texte), 3)

    def test_dates_repères(self):
        s1 = cc.serie(BRANCHE["salaire_base"]["echelle_1"]["echelon_1"])
        s2 = cc.serie(BRANCHE["salaire_base"]["echelle_1"]["echelon_2"])
        self.assertEqual(cc.reperes([s2, s1]),
                         ["1993-06-01", "2000-01-01", "2010-01-01", "2020-01-01",
                          "2025-01-01", "2026-01-01"])
        tardive = [("2012-05-01", 1.0, "", "", "")]
        self.assertEqual(cc.reperes([tardive]),
                         ["2012-05-01", "2020-01-01", "2025-01-01", "2026-01-01"])


class TableauAuxDatesReperesTest(unittest.TestCase):
    """Une date par ligne, une case par colonne ; trois états distincts dans une case."""

    def test_tiret_valeur_et_mention(self):
        ancienne = [("1993-06-01", 642.206, "t", PIST), ("2026-01-01", None, "t", PIST)]
        recente = [("1999-06-01", 839.9, "t", PIST), ("2026-01-01", None, "t", PIST)]
        parametres = [ot.ParametreDate(c, "x.yaml", {"fr": c}, format=cc.montant,
                                       sans_valeur={"fr": "non publiée"}) for c in "ab"]
        lignes = cc.lignes_reperes(parametres, [ancienne, recente],
                                   ["1993-06-01", "2025-01-01", "2026-01-01"])
        self.assertEqual(lignes, [
            ["[1^er^ juin 1993]{.insecable}", "642,206", "—"],
            ["[1^er^ janvier 2025]{.insecable}", "642,206", "839,900"],
            ["[1^er^ janvier 2026]{.insecable}", "non publiée", "non publiée"],
        ])


class CaseAuxDatesReperesTest(unittest.TestCase):
    """`ParametreDate.case` : la mention d'une date sans valeur, quand elle est déclarée."""

    SERIE = [("1999-06-01", 839.9, "t", PIST), ("2026-01-01", None, "t", PIST)]

    def setUp(self):
        self.declare = ot.ParametreDate("c", "x.yaml", {"fr": "Case"}, unite="millimes",
                                        sans_valeur={"fr": "non publiée"})
        self.defaut = ot.ParametreDate("c", "x.yaml", {"fr": "Case"}, unite="millimes")

    def test_avant_la_création_un_tiret(self):
        self.assertEqual(self.declare.case(self.SERIE, "1993-06-01", "fr"), "—")

    def test_la_valeur_en_vigueur(self):
        self.assertEqual(self.declare.case(self.SERIE, "2025-12-31", "fr"), "839,900 D")

    def test_la_mention_à_compter_de_la_date_sans_valeur(self):
        self.assertEqual(self.declare.case(self.SERIE, "2026-01-01", "fr"), "non publiée")
        self.assertEqual(self.declare.case(self.SERIE, "2027-06-01", "fr"), "non publiée")

    def test_sans_déclaration_le_tiret_de_l_abrogation_est_gardé(self):
        self.assertEqual(self.defaut.case(self.SERIE, "2026-01-01", "fr"), "—")
        self.assertEqual(self.defaut.case(self.SERIE, "2025-12-31", "fr"), "839,900 D")


if __name__ == "__main__":
    unittest.main()

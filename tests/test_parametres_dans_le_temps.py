"""Tests des deux composants « paramètres dans le temps ».

Un tableau aux dates repères et une figure en escalier affirment la même chose : une valeur
court de sa date d'effet à la veille de la suivante. Une erreur d'un jour sur cette borne
ne plante rien — elle imprime, dans une case ou sur une marche, une valeur qui n'était pas
en vigueur. Sont donc figées ici les quatre bornes de la lecture « valeur à une date » :
la veille d'une date d'effet, le jour même, après une abrogation, avant la création.

L'écriture de la série longue est testée sur ses octets : `precis/_seriescache/tva-taux.csv`
est gardé par le contrôle de fraîcheur, et une case vide, un guillemet ou une fin de ligne
qui changent le font échouer sans qu'aucune valeur ait bougé.

Fonctions PURES seulement, sans pandas ni PyYAML : le job de tests n'installe rien.
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import figtools  # noqa: E402
import openfisca_tables as ot  # noqa: E402

# Série d'un taux créé au 1er juillet 1988, relevé au 1er janvier 1998, abrogé au
# 1er janvier 2007 — la forme que rend `serie_datee` : (date, valeur, titre, lien).
PIST = "https://www.pist.tn/jort/1988/1988F/Jo03988.pdf"
SERIE = [
    ("1988-07-01", 0.17, "Loi de 1988, article 7", PIST),
    ("1998-01-01", 0.18, "Loi de finances pour 1998", PIST),
    ("2007-01-01", None, "Loi de 2006, article 13", PIST),
]


class EtatALaDateTest(unittest.TestCase):
    """La valeur à une date est la dernière valeur d'effet antérieure ou égale."""

    def test_paramètre_pas_encore_créé(self):
        self.assertIsNone(ot.etat_a_la_date(SERIE, "1988-06-30"))

    def test_le_jour_de_la_création(self):
        self.assertEqual(ot.etat_a_la_date(SERIE, "1988-07-01"), 0.17)

    def test_la_veille_d_une_date_d_effet(self):
        self.assertEqual(ot.etat_a_la_date(SERIE, "1997-12-31"), 0.17)

    def test_le_jour_même_d_une_date_d_effet(self):
        self.assertEqual(ot.etat_a_la_date(SERIE, "1998-01-01"), 0.18)

    def test_la_veille_de_l_abrogation(self):
        self.assertEqual(ot.etat_a_la_date(SERIE, "2006-12-31"), 0.18)

    def test_paramètre_abrogé_le_jour_même_et_après(self):
        self.assertIsNone(ot.etat_a_la_date(SERIE, "2007-01-01"))
        self.assertIsNone(ot.etat_a_la_date(SERIE, "2026-01-01"))

    def test_série_vide(self):
        self.assertIsNone(ot.etat_a_la_date([], "2026-01-01"))


class RendreTest(unittest.TestCase):
    """Une case rend la valeur dans son unité, ou un tiret — jamais un zéro."""

    def test_taux_et_dinars_dans_les_deux_langues(self):
        taux = ot.ParametreDate("t", "parameters/x.yaml", {"fr": "Taux", "ar": "النسبة"})
        dinars = ot.ParametreDate("d", "parameters/y.yaml", {"fr": "D", "ar": "د"},
                                  unite="dinars")
        self.assertEqual(taux.rendre(0.17, "fr"), "17 %")
        self.assertEqual(dinars.rendre(1500.0, "fr"), "1 500 D")
        self.assertEqual(dinars.rendre(1500.0, "ar"), "1 500 د")

    def test_absence_de_valeur(self):
        p = ot.ParametreDate("t", "parameters/x.yaml", {"fr": "Taux", "ar": "النسبة"})
        self.assertEqual(p.rendre(None, "fr"), "—")

    def test_format_propre_et_lien_par_défaut(self):
        p = ot.ParametreDate("t", "parameters/x.yaml", {"fr": "Seuil", "ar": "عتبة"},
                             format=lambda v, langue: f"{v:g} SMIG")
        self.assertEqual(p.rendre(2.0, "fr"), "2 SMIG")
        self.assertEqual(p.lien, p.libelle)


class SerieLongueTest(unittest.TestCase):
    """Une ligne par paramètre et par date d'effet, dans l'ordre de la déclaration."""

    def test_lignes_avec_textes(self):
        lignes = ot.lignes_serie_longue([("normal", SERIE)], colonne="taux")
        self.assertEqual([l["date_effet"] for l in lignes],
                         ["1988-07-01", "1998-01-01", "2007-01-01"])
        self.assertEqual(list(lignes[0]), ["taux", "date_effet", "valeur", "texte", "lien"])
        self.assertIsNone(lignes[2]["valeur"])  # la suppression reste une ligne

    def test_ordre_de_la_déclaration_puis_des_dates(self):
        lignes = ot.lignes_serie_longue([("b", SERIE[:2]), ("a", SERIE[:1])])
        self.assertEqual([(l["parametre"], l["date_effet"]) for l in lignes],
                         [("b", "1988-07-01"), ("b", "1998-01-01"), ("a", "1988-07-01")])

    def test_une_date_sans_texte_fait_échouer(self):
        with self.assertRaises(ValueError):
            ot.lignes_serie_longue([("normal", [("1988-07-01", 0.17, "", "")])])

    def test_un_lien_hors_du_journal_officiel_fait_échouer(self):
        with self.assertRaises(ValueError):
            ot.lignes_serie_longue(
                [("normal", [("1988-07-01", 0.17, "Loi", "http://www.legislation.tn/x")])])

    def test_sans_textes_les_valeurs_seules(self):
        lignes = ot.lignes_serie_longue([("chef", [("1990-01-01", 150.0, "", "")])],
                                        avec_textes=False)
        self.assertEqual(lignes, [{"parametre": "chef", "date_effet": "1990-01-01",
                                   "valeur": 150.0}])

    def test_écriture_octet_pour_octet(self):
        lignes = ot.lignes_serie_longue([("normal", SERIE)], colonne="taux")
        with tempfile.TemporaryDirectory() as dossier:
            fichier = Path(dossier) / "serie.csv"
            ot.ecrire_csv_serie(fichier, lignes)
            contenu = fichier.read_bytes().decode("utf-8")
        self.assertEqual(contenu, (
            "taux,date_effet,valeur,texte,lien\n"
            f'normal,1988-07-01,0.17,"Loi de 1988, article 7",{PIST}\n'
            f"normal,1998-01-01,0.18,Loi de finances pour 1998,{PIST}\n"
            # Suppression : case vide, et non « None » ni « nan ».
            f'normal,2007-01-01,,"Loi de 2006, article 13",{PIST}\n'))


# Les lignes d'une grandeur telles que la figure les lit dans la série : valeurs en %.
LIGNES = [("1995-01-01", 10.0, "", ""), ("2002-01-01", 10.0, "", ""),
          ("2007-01-01", 12.0, "", ""), ("2018-01-01", None, "", "")]


class EscalierTest(unittest.TestCase):
    """Ce que la figure déduit de la série, sans rien tracer."""

    def test_états_déduits_de_la_valeur_précédente(self):
        self.assertEqual([e for _d, _v, e, _t, _l in figtools.etats_escalier(LIGNES)],
                         ["creation", "reprise", "changement", "suppression"])

    def test_valeur_aux_bornes(self):
        self.assertIsNone(figtools.valeur_escalier(LIGNES, "1994-12-31"))
        self.assertEqual(figtools.valeur_escalier(LIGNES, "2006-12-31"), 10.0)
        self.assertEqual(figtools.valeur_escalier(LIGNES, "2007-01-01"), 12.0)
        self.assertIsNone(figtools.valeur_escalier(LIGNES, "2018-01-01"))

    def test_moyenne_annuelle_pondérée_par_les_mois(self):
        lignes = [("1990-01-01", 100.0, "", ""), ("1992-05-01", 160.0, "", "")]
        # Quatre mois à 100, huit mois à 160.
        self.assertAlmostEqual(figtools.moyenne_annuelle_escalier(lignes, 1992), 140.0)
        self.assertEqual(figtools.moyenne_annuelle_escalier(lignes, 1991), 100.0)

    def test_pas_de_moyenne_sur_une_année_incomplète(self):
        lignes = [("1988-07-01", 17.0, "", "")]
        self.assertIsNone(figtools.moyenne_annuelle_escalier(lignes, 1988))
        self.assertIsNone(figtools.moyenne_annuelle_escalier(LIGNES, 2018))

    def test_abscisse_d_une_date(self):
        self.assertEqual(figtools.abscisse_date("1995-01-01"), 1995.0)
        # 1988 est bissextile : le 1er juillet est son 183e jour.
        self.assertAlmostEqual(figtools.abscisse_date("1988-07-01"), 1988 + 182 / 366)


if __name__ == "__main__":
    unittest.main()

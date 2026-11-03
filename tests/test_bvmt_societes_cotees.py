"""Tests de `scripts/bvmt_societes_cotees.py` : sans réseau, sur de petits morceaux de page."""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import bvmt_societes_cotees as b  # noqa: E402

PAGE = """<html><body>
<p>Dénomination sociale</p><p>BNA</p><p>Date de Constitution</p><p>1 juin 1959</p>
<p>Forme Juridique</p><p>Société Anonyme (SA)</p><p>RNE</p><p>0000123L</p>
<p>Secteur d'activité</p><p>BANQUES</p><p>Cours d'introduction</p>
<p>4. Principaux actionnaires : AGO- 30/04/2026</p>
<table><tr><th>Nom ou raison sociale</th><th>Nombre d'actions</th><th>%</th></tr>
<tr><td>Etat Tunisien</td><td>22565045</td><td>35.26</td></tr>
<tr><td>Actionnaires détenant moins que 5%</td><td>41434955</td><td>64.74</td></tr>
<tr><td>Total</td><td>64000000</td><td>100</td></tr></table>
<table><tr><th>Nom ou raison sociale</th><th>Qualité</th></tr><tr><td>M. X</td><td>Président</td></tr></table>
<table><tr><th>Chiffres clés</th><th>2025</th><th>2024</th></tr>
<tr><td>Capital social</td><td> 320 000 000</td><td> 300 000 000</td></tr></table>
<table><tr><td>1959-05-31</td><td>Capital Initial</td><td> 400000</td><td> 400000</td></tr>
<tr><td>1989-06-24</td><td>10</td><td>Fusion par absorption</td><td> 10000000</td><td> 10000000</td>
<td> 33000000</td><td> 33000000</td></tr></table>
</body></html>"""


class LireTest(unittest.TestCase):
    def lu(self):
        with tempfile.TemporaryDirectory() as dossier:
            chemin = Path(dossier) / "bna.html"
            chemin.write_text(PAGE, encoding="utf-8")
            return b.lire(chemin)

    def test_identite(self):
        societe = self.lu()["societe"]
        self.assertEqual(societe["denomination"], "BNA")
        self.assertEqual(societe["rne"], "0000123L")
        self.assertEqual(societe["secteur"], "BANQUES")

    def test_les_actionnaires_ne_confondent_pas_le_conseil(self):
        lu = self.lu()
        self.assertEqual(lu["assemblee"], "30/04/2026")
        self.assertEqual(lu["actionnaires"][0], ("Etat Tunisien", 22565045.0, 35.26))
        self.assertEqual(
            len(lu["actionnaires"]), 2
        )  # ni « Total », ni le tableau du conseil

    def test_fonds_propres_par_exercice(self):
        valeurs = {(e, v) for _, e, v in self.lu()["fonds_propres"]}
        self.assertEqual(valeurs, {("2025", 320000000.0), ("2024", 300000000.0)})

    def test_historique_du_capital_avant_et_apres_la_division_en_actions(self):
        ancien, recent = self.lu()["capital"]
        self.assertEqual(
            (ancien["capital_dt"], ancien["capital_actions"]), (400000.0, None)
        )
        self.assertEqual(recent["nominal"], 10.0)
        self.assertEqual(
            (recent["capital_dt"], recent["capital_actions"]), (33000000.0, 33000000.0)
        )


class DetenteursTest(unittest.TestCase):
    def test_liste_fermee_sur_noms_normalises(self):
        self.assertEqual(b.DETENTEURS_PUBLICS[b.cle_detenteur("Etat Tunisien")], "État")
        self.assertEqual(
            b.DETENTEURS_PUBLICS[
                b.cle_detenteur("Entreprise Tunisienne d’Activités Pétrolières -ETAP")
            ],
            "ETAP",
        )
        self.assertNotIn(b.cle_detenteur("Groupe HORCHANI"), b.DETENTEURS_PUBLICS)
        self.assertNotIn(b.cle_detenteur("BH SICAF"), b.DETENTEURS_PUBLICS)


class ResultatsTest(unittest.TestCase):
    def lignes(self, assemblee, exercice="2025", dividende="1.15"):
        participations = [
            ["État", "BNA", "bna", "35.26", "1000", assemblee, "Etat Tunisien"]
        ]
        indicateurs = [
            {
                "nom": "bna",
                "libelle": "Résultat net (2)",
                "exercice": exercice,
                "dinars": "287737000.0",
            },
            {
                "nom": "bna",
                "libelle": "Dividende par action",
                "exercice": exercice,
                "dinars": dividende,
            },
            {
                "nom": "bna",
                "libelle": "Capital social",
                "exercice": exercice,
                "dinars": "320000000.0",
            },
        ]
        return b.resultats(lambda nom: indicateurs, participations)

    def test_le_dividende_de_l_etat_est_calcule_pour_l_assemblee_de_l_annee_suivante(
        self,
    ):
        (ligne,) = self.lignes("30/04/2026")
        self.assertEqual(ligne[2:5], ["2025", "287737000", "1.15"])
        self.assertEqual(ligne[-1], "1150")  # 1,15 dinar × 1 000 actions

    def test_pas_de_calcul_si_l_assemblee_n_est_pas_celle_qui_vote_le_dividende(self):
        (ligne,) = self.lignes("30/04/2026", exercice="2024")
        self.assertEqual(ligne[-1], "")

    def test_seuls_le_resultat_net_et_le_dividende_sont_repris(self):
        self.assertEqual(len(self.lignes("30/04/2026")), 1)


if __name__ == "__main__":
    unittest.main()

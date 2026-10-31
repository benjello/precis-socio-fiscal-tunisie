"""Tests du garde « le dépôt public ne parle pas de l'infrastructure de sauvegarde ».

La liste réelle des mots est privée : les tests emploient une liste fictive. Ils vérifient les
deux familles de règles — mots interdits partout, noms interdits seulement en contexte de
sauvegarde, pour épargner les noms de personnes —, le chargement de la liste et le saut sans liste.
"""

import os
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import check_pas_d_infra as garde  # noqa: E402

LISTE = """\
# commentaire
interdit: zzoutil|zzhote\\.exemple
interdit: \\b10\\.99\\.\\d{1,3}\\.\\d{1,3}
site: zzville
"""
REGLES = garde.lire_regles(LISTE)


class Detection(unittest.TestCase):
    def test_mot_interdit(self):
        self.assertEqual(garde.controle("on sauvegarde avec zzoutil ici", REGLES)[0][1].lower(), "zzoutil")

    def test_hote(self):
        self.assertTrue(garde.controle("hôte zzhote.exemple", REGLES))

    def test_adresse(self):
        self.assertTrue(garde.controle("adresse 10.99.0.7", REGLES))

    def test_site_en_contexte_de_sauvegarde(self):
        self.assertTrue(garde.controle("la copie est sur le serveur de Zzville", REGLES))
        self.assertTrue(garde.controle("réplica à Zzville", REGLES))

    def test_numero_de_ligne(self):
        self.assertEqual(garde.controle("ligne un\nzzoutil\n", REGLES)[0][0], 2)


class Exclusion(unittest.TestCase):
    def test_nom_sans_contexte(self):
        self.assertEqual(garde.controle("Les Lettres de Zzville, roman", REGLES), [])

    def test_prose_ordinaire(self):
        self.assertEqual(garde.controle("La loi de finances fixe le taux de la TVA.", REGLES), [])
        self.assertEqual(garde.controle("Adresse IP 192.168.0.1 d'un exemple.", REGLES), [])

    def test_commentaires_et_lignes_vides_de_la_liste(self):
        interdits, sites = garde.lire_regles("# rien\n\nsite: aaa\n")
        self.assertIsNone(interdits)
        self.assertIsNotNone(sites)

    def test_fichiers_exemptes(self):
        self.assertIn("scripts/check_pas_d_infra.py", garde.EXEMPTS)
        self.assertIn("tests/test_check_pas_d_infra.py", garde.EXEMPTS)


class Chargement(unittest.TestCase):
    def test_liste_par_variable(self):
        with mock.patch.dict(os.environ, {"PAS_D_INFRA_MOTS": LISTE}):
            self.assertTrue(garde.controle("zzoutil", garde.charger_regles()))

    def test_sans_liste_le_controle_est_saute(self):
        env = {k: v for k, v in os.environ.items() if not k.startswith("PAS_D_INFRA")}
        env["PAS_D_INFRA_FICHIER"] = "/inexistant/mots.txt"
        with mock.patch.dict(os.environ, env, clear=True):
            self.assertIsNone(garde.charger_regles())
            self.assertEqual(garde.main([]), 0)


if __name__ == "__main__":
    unittest.main()

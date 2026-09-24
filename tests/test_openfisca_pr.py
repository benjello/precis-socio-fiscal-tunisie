"""Tests des fonctions pures d'`openfisca_pr.py` : renumérotation du CHANGELOG.

`maj`, `ci` et `formules` appellent `git` et `gh` : ce qu'on peut tester sans réseau
ni dépôt est isolé dans des fonctions pures (extraction, renumérotation, insertion,
calcul de version), et c'est ce que ce fichier couvre — conformément à la règle du
job de tests (`unittest`, aucune dépendance nouvelle).

`maj` lui-même a été éprouvé à la main contre un dépôt jetable local (bare + clone
dans le répertoire de travail), pas ici : voir le rapport de la tâche qui a introduit
ce script. Il ne s'exécute jamais sur une vraie PR openfisca-tunisia.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from openfisca_pr import (  # noqa: E402
    ErreurOutillage,
    diff_hors_version,
    est_fichier_formule,
    extraire_section,
    fichiers_py_hors_tests,
    inserer_en_tete,
    lire_version_pyproject,
    prochaine_version,
    remplacer_version_pyproject,
    remplacer_version_uv_lock,
    renumeroter_section,
)

CHANGELOG = """# Changelog

## 0.112 - [#459](https://github.com/openfisca/openfisca-tunisia/pull/459)

* Évolution du système socio-fiscal.
* Détails :
  - Un premier point.
  - Un second point.

### 0.111.1 - [#458](https://github.com/openfisca/openfisca-tunisia/pull/458)

* Changement mineur.

## 0.111 - [#457](https://github.com/openfisca/openfisca-tunisia/pull/457)

* Évolution du système socio-fiscal.
"""


class ProchaineVersionTest(unittest.TestCase):

    def test_incrementation_simple(self):
        self.assertEqual(prochaine_version("0.112"), "0.113")

    def test_passage_a_trois_chiffres(self):
        self.assertEqual(prochaine_version("0.99"), "0.100")

    def test_format_semver_refuse(self):
        """Le dépôt numérote 0.NNN, jamais MAJEUR.MINEUR.PATCH."""
        with self.assertRaises(ErreurOutillage):
            prochaine_version("1.2.3")

    def test_espaces_tolérés(self):
        self.assertEqual(prochaine_version(" 0.5 \n"), "0.6")


class ExtraireSectionTest(unittest.TestCase):

    def test_section_de_tete(self):
        """S'arrête au prochain titre, MÊME PLUS PROFOND : les entrées sont sœurs."""
        section = extraire_section(CHANGELOG, 459)
        self.assertTrue(section.startswith("## 0.112 "))
        self.assertIn("Un premier point", section)
        self.assertNotIn("### 0.111.1", section)

    def test_section_de_rang_trois_ne_deborde_pas_sur_la_suivante(self):
        """Une section `###` s'arrête à la prochaine `##`, pas seulement `###`."""
        section = extraire_section(CHANGELOG, 458)
        self.assertTrue(section.startswith("### 0.111.1 "))
        self.assertNotIn("0.111 -", section)

    def test_section_intermediaire(self):
        section = extraire_section(CHANGELOG, 457)
        self.assertTrue(section.startswith("## 0.111 "))

    def test_pr_absente(self):
        with self.assertRaises(ErreurOutillage):
            extraire_section(CHANGELOG, 999)

    def test_lien_ambigu_leve(self):
        """Deux titres qui citeraient la même PR sont un CHANGELOG cassé : on s'arrête."""
        double = CHANGELOG + "\n## 0.110 - [#459](https://github.com/x/y/pull/459)\n"
        with self.assertRaises(ErreurOutillage):
            extraire_section(double, 459)


class RenumeroterSectionTest(unittest.TestCase):

    def test_conserve_le_niveau_de_titre(self):
        section = "### 0.111.1 - [#458](.../pull/458)\n\n* Changement mineur.\n"
        renumerotee = renumeroter_section(section, "0.113")
        self.assertTrue(renumerotee.startswith("### 0.113 "))

    def test_conserve_le_lien_de_pr(self):
        section = "## 0.112 - [#459](https://github.com/o/r/pull/459)\n\n* x\n"
        renumerotee = renumeroter_section(section, "0.200")
        self.assertIn("[#459](https://github.com/o/r/pull/459)", renumerotee)

    def test_titre_sans_numero_leve(self):
        with self.assertRaises(ErreurOutillage):
            renumeroter_section("## pas un numéro - [#1](x/pull/1)\n", "0.9")


class InsererEnTeteTest(unittest.TestCase):

    def test_insertion_juste_apres_len_tete(self):
        master = "# Changelog\n\n## 0.111 - [#457](x/pull/457)\n\n* ancien\n"
        section = "## 0.112 - [#459](x/pull/459)\n\n* nouveau\n"
        resultat = inserer_en_tete(master, section)
        self.assertEqual(resultat, (
            "# Changelog\n\n"
            "## 0.112 - [#459](x/pull/459)\n\n* nouveau\n\n"
            "## 0.111 - [#457](x/pull/457)\n\n* ancien\n"
        ))

    def test_entete_manquante_leve(self):
        with self.assertRaises(ErreurOutillage):
            inserer_en_tete("Changelog\n\n## 0.1\n", "## 0.2\n")


class VersionPyprojectEtUvLockTest(unittest.TestCase):

    def test_lire_version(self):
        self.assertEqual(
            lire_version_pyproject('[project]\nname = "x"\nversion = "0.112"\n'), "0.112")

    def test_lire_version_absente_leve(self):
        with self.assertRaises(ErreurOutillage):
            lire_version_pyproject('[project]\nname = "x"\n')

    def test_remplace_seulement_la_premiere_occurrence(self):
        texte = 'version = "0.112"\nautre = "version = \\"0.112\\""\n'
        # Une seule vraie occurrence de la ligne de version en tête de fichier.
        resultat = remplacer_version_pyproject('version = "0.112"\n', "0.112", "0.113")
        self.assertEqual(resultat, 'version = "0.113"\n')

    def test_occurrence_dupliquee_leve(self):
        with self.assertRaises(ErreurOutillage):
            remplacer_version_pyproject(
                'version = "0.1"\nversion = "0.1"\n', "0.1", "0.2")

    def test_uv_lock_cible_le_bon_paquet(self):
        uv_lock = (
            'name = "autre-paquet"\nversion = "0.112"\n\n'
            'name = "openfisca-tunisia"\nversion = "0.112"\n'
        )
        resultat = remplacer_version_uv_lock(uv_lock, "0.112", "0.113")
        self.assertIn('name = "openfisca-tunisia"\nversion = "0.113"', resultat)
        self.assertIn('name = "autre-paquet"\nversion = "0.112"', resultat)

    def test_uv_lock_sans_entree_leve(self):
        with self.assertRaises(ErreurOutillage):
            remplacer_version_uv_lock('name = "autre"\nversion = "0.1"\n', "0.1", "0.2")


class DiffHorsVersionTest(unittest.TestCase):

    def test_seule_la_version_change_est_ignore(self):
        ancien = 'name = "x"\nversion = "0.1"\ndependencies = ["numpy"]\n'
        nouveau = 'name = "x"\nversion = "0.2"\ndependencies = ["numpy"]\n'
        self.assertFalse(diff_hors_version(ancien, nouveau))

    def test_dependance_ajoutee_est_detectee(self):
        ancien = 'name = "x"\nversion = "0.1"\ndependencies = ["numpy"]\n'
        nouveau = 'name = "x"\nversion = "0.2"\ndependencies = ["numpy", "scipy"]\n'
        self.assertTrue(diff_hors_version(ancien, nouveau))


class FichiersPyHorsTestsTest(unittest.TestCase):
    """`formules` liste TOUS les .py hors tests, pas seulement variables/regimes —
    la restriction à variables/regimes n'est qu'un marquage, appliqué à part
    (`est_fichier_formule`)."""

    def test_liste_tout_py_hors_tests(self):
        fichiers = ["openfisca_tunisia_pension/variables/survivants.py",
                    "openfisca_tunisia/sous_ensembles.py", "CHANGELOG.md"]
        self.assertEqual(
            fichiers_py_hors_tests(fichiers),
            ["openfisca_tunisia_pension/variables/survivants.py",
             "openfisca_tunisia/sous_ensembles.py"])

    def test_test_yaml_pension_est_exclu(self):
        self.assertEqual(fichiers_py_hors_tests(["tests_pension/formulas/rsa/survivants.yaml"]), [])

    def test_fichier_test_python_est_exclu(self):
        self.assertEqual(
            fichiers_py_hors_tests(["openfisca_tunisia/variables/test_survivants.py"]), [])

    def test_dossier_tests_est_exclu(self):
        self.assertEqual(
            fichiers_py_hors_tests(["openfisca_tunisia/tests/variables/survivants.py"]), [])

    def test_parametre_yaml_n_est_pas_du_python(self):
        self.assertEqual(
            fichiers_py_hors_tests(["openfisca_tunisia/parameters/retraite/cnrps/taux.yaml"]), [])

    def test_aucun_fichier_py(self):
        self.assertEqual(fichiers_py_hors_tests(["CHANGELOG.md", "pyproject.toml"]), [])


class EstFichierFormuleTest(unittest.TestCase):

    def test_variable_est_une_formule(self):
        self.assertTrue(est_fichier_formule("openfisca_tunisia_pension/variables/survivants.py"))

    def test_regime_est_une_formule(self):
        self.assertTrue(est_fichier_formule("openfisca_tunisia/regimes/cnrps.py"))

    def test_module_hors_variables_regimes_n_est_pas_une_formule(self):
        self.assertFalse(est_fichier_formule("openfisca_tunisia/sous_ensembles.py"))
        self.assertFalse(est_fichier_formule("openfisca_tunisia/entities.py"))


if __name__ == "__main__":
    unittest.main()

"""Tests du générateur de sous-agents Claude Code (`scripts/sync_agents.py`).

Le texte des rôles éditoriaux (`docs/agents/<role>.md`) est neutre — sans en-tête
ni nom d'outil — précisément pour pouvoir servir à un autre outil que Claude
Code. `sync_agents.py` est le seul endroit qui connaît le format d'en-tête
attendu par `.claude/agents/*.md` (`name`, `description`, `tools`, `model`) et
la table qui traduit un NIVEAU abstrait (`docs/agents/roles.yml`) en nom de
modèle Claude Code. Ces tests isolent cette mécanique dans un dossier jetable
— on ne veut pas que casser un rôle réel empêche de tester le générateur, ni
l'inverse — puis vérifient, en fin de fichier, que le dépôt réel est à jour :
c'est le même contrôle que `--verifier`, mais qui tombe avec `pytest`.
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

# La CI lance les tests sans dépendances (`uv run --isolated --no-project`) :
# sans PyYAML, `sync_agents` ne s'importe pas, et le module entier est sauté.
# L'étape `sync_agents.py --verifier` de verifier-conventions.yml couvre la CI.
try:
    import yaml  # noqa: F401
except ImportError:
    raise unittest.SkipTest("PyYAML absent : lancer par `uv run pytest`")

import sync_agents  # noqa: E402


class DepotJetable(unittest.TestCase):
    """Un docs/agents/ et un .claude/agents/ isolés, avec un roles.yml minimal."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        racine = Path(self._tmp.name)
        self.dossier_docs = racine / "docs" / "agents"
        self.dossier_claude = racine / ".claude" / "agents"
        self.dossier_docs.mkdir(parents=True)
        self.dossier_claude.mkdir(parents=True)

        self._roles_yml_orig = sync_agents.ROLES_YML
        self._dossier_docs_orig = sync_agents.DOSSIER_DOCS
        self._dossier_claude_orig = sync_agents.DOSSIER_CLAUDE
        sync_agents.ROLES_YML = self.dossier_docs / "roles.yml"
        sync_agents.DOSSIER_DOCS = self.dossier_docs
        sync_agents.DOSSIER_CLAUDE = self.dossier_claude

    def tearDown(self):
        sync_agents.ROLES_YML = self._roles_yml_orig
        sync_agents.DOSSIER_DOCS = self._dossier_docs_orig
        sync_agents.DOSSIER_CLAUDE = self._dossier_claude_orig
        self._tmp.cleanup()

    def ecrire_roles_yml(self, texte):
        sync_agents.ROLES_YML.write_text(texte, encoding="utf-8")

    def ecrire_corps(self, nom_role, texte):
        (self.dossier_docs / f"{nom_role}.md").write_text(texte, encoding="utf-8")

    ROLES_YML_UN_ROLE = """
roles:
  documentaliste:
    description: "Rassemble la matière."
    tools: [Read, Grep]
    niveau: raisonnement
modeles:
  claude-code:
    raisonnement: opus
    standard: sonnet
    mecanique: haiku
  openai:
    raisonnement: null
    standard: null
    mecanique: null
"""

    def config_un_role(self):
        self.ecrire_roles_yml(self.ROLES_YML_UN_ROLE)
        self.ecrire_corps("documentaliste", "Corps du rôle.\n")
        return sync_agents.charger_config()


class EngendrerClaudeCodeTest(DepotJetable):
    def test_en_tete_et_avertissement(self):
        config = self.config_un_role()
        contenu = sync_agents.engendrer_claude_code("documentaliste", config)
        self.assertEqual(
            contenu,
            "---\n"
            "name: documentaliste\n"
            "description: Rassemble la matière.\n"
            "tools: Read, Grep\n"
            "model: opus\n"
            "---\n"
            "\n"
            "Fichier engendré par scripts/sync_agents.py depuis "
            "docs/agents/documentaliste.md — ne pas éditer.\n"
            "\n"
            "Corps du rôle.\n",
        )

    def test_modele_choisi_selon_le_niveau(self):
        config = self.config_un_role()
        config["roles"]["documentaliste"]["niveau"] = "standard"
        contenu = sync_agents.engendrer_claude_code("documentaliste", config)
        self.assertIn("model: sonnet\n", contenu)

    def test_niveau_sans_modele_leve(self):
        """`mecanique` existe comme niveau mais n'est affecté à aucun rôle : le
        générateur doit quand même refuser de produire un fichier sans modèle
        si un rôle finissait par le porter, plutôt que d'écrire `model: None`."""
        config = self.config_un_role()
        config["roles"]["documentaliste"]["niveau"] = "openai-style-absent"
        config["modeles"]["claude-code"]["openai-style-absent"] = None
        with self.assertRaises(ValueError):
            sync_agents.engendrer_claude_code("documentaliste", config)

    def test_niveau_inconnu_de_la_table_leve(self):
        config = self.config_un_role()
        config["roles"]["documentaliste"]["niveau"] = "inexistant"
        with self.assertRaises(KeyError):
            sync_agents.engendrer_claude_code("documentaliste", config)

    def test_ordre_des_tools_preserve(self):
        """L'ordre déclaré dans roles.yml doit survivre, rôle par rôle : les
        fichiers réels du dépôt ne l'ordonnent pas tous pareil (`terminologue`
        met `Edit` avant `Write`, les autres l'inverse)."""
        self.ecrire_roles_yml(
            self.ROLES_YML_UN_ROLE.replace(
                "tools: [Read, Grep]", "tools: [Edit, Write, Read]"
            )
        )
        self.ecrire_corps("documentaliste", "Corps.\n")
        config = sync_agents.charger_config()
        contenu = sync_agents.engendrer_claude_code("documentaliste", config)
        self.assertIn("tools: Edit, Write, Read\n", contenu)


class VerifierEtEcrireTest(DepotJetable):
    def test_verifier_signale_fichier_absent(self):
        config = self.config_un_role()
        self.assertEqual(sync_agents.verifier(config), ["documentaliste"])

    def test_ecrire_puis_verifier_est_propre(self):
        config = self.config_un_role()
        modifies = sync_agents.ecrire(config)
        self.assertEqual(modifies, ["documentaliste"])
        self.assertEqual(sync_agents.verifier(config), [])

    def test_ecrire_est_idempotent(self):
        config = self.config_un_role()
        sync_agents.ecrire(config)
        self.assertEqual(sync_agents.ecrire(config), [])

    def test_verifier_signale_fichier_perime(self):
        config = self.config_un_role()
        sync_agents.ecrire(config)
        # Le rôle change de niveau après une première génération : le fichier
        # engendré porte encore l'ancien modèle.
        self.ecrire_roles_yml(
            self.ROLES_YML_UN_ROLE.replace("niveau: raisonnement", "niveau: standard")
        )
        config2 = sync_agents.charger_config()
        self.assertEqual(sync_agents.verifier(config2), ["documentaliste"])

    def test_corps_edite_sans_regeneration_est_detecte(self):
        """Le cas réel visé par la CI : docs/agents/<role>.md change, personne
        ne relance sync_agents.py, .claude/agents/<role>.md reste périmé."""
        config = self.config_un_role()
        sync_agents.ecrire(config)
        self.ecrire_corps("documentaliste", "Corps modifié.\n")
        self.assertEqual(sync_agents.verifier(config), ["documentaliste"])


class DepotReelTest(unittest.TestCase):
    """Le même contrôle que `--verifier`, sur le dépôt réel plutôt qu'un jetable.

    Si ce test rougit, c'est qu'un rôle a été édité dans docs/agents/ sans
    relancer `uv run python scripts/sync_agents.py` avant de commiter.
    """

    def test_agents_engendres_a_jour(self):
        config = sync_agents.charger_config()
        en_retard = sync_agents.verifier(config)
        self.assertEqual(
            en_retard, [],
            "Régénérer avec : uv run python scripts/sync_agents.py",
        )

    def test_six_roles_editoriaux_presents(self):
        config = sync_agents.charger_config()
        self.assertEqual(
            set(config["roles"]),
            {
                "bibliographe",
                "documentaliste",
                "modeliste",
                "redacteur",
                "relecteur-ar",
                "terminologue",
            },
        )

    def test_niveaux_conformes_a_la_consigne(self):
        config = sync_agents.charger_config()
        niveaux = {nom: r["niveau"] for nom, r in config["roles"].items()}
        self.assertEqual(
            niveaux,
            {
                "bibliographe": "standard",
                "documentaliste": "raisonnement",
                "modeliste": "raisonnement",
                "redacteur": "raisonnement",
                "relecteur-ar": "standard",
                "terminologue": "raisonnement",
            },
        )


if __name__ == "__main__":
    unittest.main()

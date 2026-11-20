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
        self.dossier_pi = racine / ".pi" / "agents"
        self.dossier_opencode = racine / ".opencode" / "agent"
        self.dossier_docs.mkdir(parents=True)
        self.dossier_claude.mkdir(parents=True)
        self.dossier_pi.mkdir(parents=True)
        self.dossier_opencode.mkdir(parents=True)

        self._roles_yml_orig = sync_agents.ROLES_YML
        self._dossier_docs_orig = sync_agents.DOSSIER_DOCS
        self._dossier_claude_orig = sync_agents.DOSSIER_CLAUDE
        self._dossier_pi_orig = sync_agents.DOSSIER_PI
        self._dossier_opencode_orig = sync_agents.DOSSIER_OPENCODE
        sync_agents.ROLES_YML = self.dossier_docs / "roles.yml"
        sync_agents.DOSSIER_DOCS = self.dossier_docs
        sync_agents.DOSSIER_CLAUDE = self.dossier_claude
        sync_agents.DOSSIER_PI = self.dossier_pi
        sync_agents.DOSSIER_OPENCODE = self.dossier_opencode

    def tearDown(self):
        sync_agents.ROLES_YML = self._roles_yml_orig
        sync_agents.DOSSIER_DOCS = self._dossier_docs_orig
        sync_agents.DOSSIER_CLAUDE = self._dossier_claude_orig
        sync_agents.DOSSIER_PI = self._dossier_pi_orig
        sync_agents.DOSSIER_OPENCODE = self._dossier_opencode_orig
        self._tmp.cleanup()

    def ecrire_roles_yml(self, texte):
        sync_agents.ROLES_YML.write_text(texte, encoding="utf-8")

    def ecrire_corps(self, nom_role, texte):
        (self.dossier_docs / f"{nom_role}.md").write_text(texte, encoding="utf-8")

    ROLES_YML_UN_ROLE = """
roles:
  documentaliste:
    description: "Rassemble la matière."
    tools: [read, grep]
    niveau: raisonnement
modeles:
  claude-code:
    raisonnement: opus
    standard: sonnet
    mecanique: haiku
  pi:
    raisonnement: null
    standard: null
    mecanique: null
  opencode:
    raisonnement: null
    standard: null
    mecanique: null
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
            # La consigne commune (routage des reports) est insérée par les
            # générateurs entre l'avertissement et le corps (PR #784).
            + sync_agents.CONSIGNE_COMMUNE + "\n"
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
        met `edit` avant `write`, les autres l'inverse)."""
        self.ecrire_roles_yml(
            self.ROLES_YML_UN_ROLE.replace(
                "tools: [read, grep]", "tools: [edit, write, read]"
            )
        )
        self.ecrire_corps("documentaliste", "Corps.\n")
        config = sync_agents.charger_config()
        contenu = sync_agents.engendrer_claude_code("documentaliste", config)
        self.assertIn("tools: Edit, Write, Read\n", contenu)


class TraduireOutilsTest(DepotJetable):
    """Le cœur de la robustesse multi-harnais : un vocabulaire neutre traduit
    dans le nom que chaque harnais attend. web_search/web_fetch et glob sont
    les cas qui, mal traduits, faisaient démarrer des rôles sans web sous pi."""

    def test_claude_capitalise_et_web(self):
        self.assertEqual(
            sync_agents.traduire_outils(
                ["read", "glob", "web_search", "web_fetch"], "claude-code"),
            "Read, Glob, WebSearch, WebFetch",
        )

    def test_pi_minuscule_glob_devient_find_et_web(self):
        self.assertEqual(
            sync_agents.traduire_outils(
                ["read", "glob", "web_search", "web_fetch"], "pi"),
            "read, find, web_search, web_fetch",
        )

    def test_opencode_meme_vocabulaire_que_pi(self):
        outils = ["read", "write", "edit", "grep", "glob", "bash",
                  "web_search", "web_fetch"]
        self.assertEqual(
            sync_agents.traduire_outils(outils, "opencode"),
            sync_agents.traduire_outils(outils, "pi"),
        )

    def test_outil_neutre_inconnu_leve(self):
        with self.assertRaises(KeyError):
            sync_agents.traduire_outils(["read", "telepathy"], "pi")


class EngendrerPiEtOpencodeTest(DepotJetable):
    def test_pi_traduit_les_outils_et_omet_model_si_null(self):
        config = self.config_un_role()
        config["roles"]["documentaliste"]["tools"] = ["read", "web_search"]
        contenu = sync_agents.engendrer_pi("documentaliste", config)
        self.assertIn("tools: read, web_search\n", contenu)
        self.assertNotIn("model:", contenu)  # modeles.pi est null dans la fixture

    def test_opencode_porte_mode_subagent(self):
        config = self.config_un_role()
        contenu = sync_agents.engendrer_opencode("documentaliste", config)
        self.assertTrue(contenu.startswith("---\nmode: subagent\nname: documentaliste\n"))
        self.assertIn("tools: read, grep\n", contenu)
        self.assertNotIn("model:", contenu)

    def test_model_pi_ecrit_si_renseigne(self):
        config = self.config_un_role()
        config["modeles"]["pi"]["raisonnement"] = "claude-sonnet-4-5"
        contenu = sync_agents.engendrer_pi("documentaliste", config)
        self.assertIn("model: claude-sonnet-4-5\n", contenu)


class VerifierEtEcrireTest(DepotJetable):
    # Depuis la génération à trois cibles (.claude/, .pi/, .opencode/), verifier()
    # et ecrire() rendent des noms préfixés par la cible : `<outil>/<role>`.
    TROIS_CIBLES = ["claude-code/documentaliste", "pi/documentaliste",
                    "opencode/documentaliste"]

    def test_verifier_signale_fichier_absent(self):
        config = self.config_un_role()
        self.assertEqual(sync_agents.verifier(config), self.TROIS_CIBLES)

    def test_ecrire_puis_verifier_est_propre(self):
        config = self.config_un_role()
        modifies = sync_agents.ecrire(config)
        self.assertEqual(modifies, self.TROIS_CIBLES)
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
        # Seul le fichier Claude Code porte un modèle (modeles.pi est null dans
        # la fixture : la ligne model: est omise et ne périme pas) : seul lui
        # est signalé périmé.
        self.assertEqual(sync_agents.verifier(config2), ["claude-code/documentaliste"])

    def test_corps_edite_sans_regeneration_est_detecte(self):
        """Le cas réel visé par la CI : docs/agents/<role>.md change, personne
        ne relance sync_agents.py, .claude/agents/<role>.md reste périmé."""
        config = self.config_un_role()
        sync_agents.ecrire(config)
        self.ecrire_corps("documentaliste", "Corps modifié.\n")
        self.assertEqual(sync_agents.verifier(config), self.TROIS_CIBLES)


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

    def test_roles_editoriaux_presents(self):
        config = sync_agents.charger_config()
        self.assertEqual(
            set(config["roles"]),
            {
                "archiviste-backlog",
                "architecte",
                "bibliographe",
                "documentaliste",
                "economiste",
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
                "archiviste-backlog": "standard",
                "architecte": "raisonnement",
                "bibliographe": "standard",
                "documentaliste": "raisonnement",
                "economiste": "raisonnement",
                "modeliste": "raisonnement",
                "redacteur": "raisonnement",
                "relecteur-ar": "standard",
                "terminologue": "raisonnement",
            },
        )


if __name__ == "__main__":
    unittest.main()

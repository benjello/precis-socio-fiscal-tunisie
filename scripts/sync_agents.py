"""Engendre les sous-agents Claude Code à partir des rôles éditoriaux neutres.

Le TEXTE de chaque rôle (documentaliste, rédacteur, terminologue, bibliographe,
relecteur-ar, modeliste) vit désormais dans `docs/agents/<role>.md` — de la
prose simple, sans en-tête ni syntaxe propre à un outil. Ses métadonnées
(`name`, `description`, `tools`, et un NIVEAU abstrait qui dit combien de
jugement la tâche demande) vivent dans `docs/agents/roles.yml`, avec une table
`modeles` qui associe chaque niveau à un modèle, par outil.

Ce script engendre `.claude/agents/<role>.md` : l'en-tête YAML que Claude Code
attend (`name`, `description`, `tools`, `model` — ce dernier tiré de
`modeles.claude-code` selon le niveau du rôle), une ligne d'avertissement, puis
le corps commun tel quel.

    uv run python scripts/sync_agents.py              # écrit .claude/agents/*.md
    uv run python scripts/sync_agents.py --verifier   # ne rien écrire ; sort 1
                                                        # si un fichier engendré
                                                        # n'est pas à jour

La CI (`verifier-conventions.yml`) et `scripts/verifier.sh` lancent `--verifier` :
un rôle édité dans `docs/agents/` sans régénération laisse `.claude/agents/`
en retard, silencieusement, jusqu'à ce contrôle.

Pour un AUTRE outil (Codex, Cursor…) : ce script ne fournit délibérément aucune
génération, faute de format de sous-agent vérifié pour lui ici — la table
`modeles.openai` de `roles.yml` est d'ailleurs vide (« à renseigner par
l'humain »). Le chemin documenté (voir AGENTS.md, § « Économiser ») est de
charger `docs/agents/<role>.md` comme consigne et de choisir le modèle dans
`modeles.<outil>` selon `roles.<role>.niveau`. Si un format d'en-tête pour cet
outil devient vérifié, ajouter ici une fonction `engendrer_<outil>()` sur le
modèle de `engendrer_claude_code()`, plus une entrée `--outil <nom>` : ne pas
deviner ce format à l'avance.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
DOSSIER_DOCS = RACINE / "docs" / "agents"
DOSSIER_CLAUDE = RACINE / ".claude" / "agents"
ROLES_YML = DOSSIER_DOCS / "roles.yml"

AVERTISSEMENT = (
    "Fichier engendré par scripts/sync_agents.py depuis docs/agents/{role}.md "
    "— ne pas éditer."
)


def charger_config() -> dict:
    return yaml.safe_load(ROLES_YML.read_text(encoding="utf-8"))


def corps(nom_role: str) -> str:
    """Le texte commun du rôle, tel qu'écrit dans docs/agents/<role>.md."""
    return (DOSSIER_DOCS / f"{nom_role}.md").read_text(encoding="utf-8")


def engendrer_claude_code(nom_role: str, config: dict) -> str:
    """L'en-tête YAML + l'avertissement + le corps, format .claude/agents/*.md."""
    role = config["roles"][nom_role]
    niveau = role["niveau"]
    try:
        modele = config["modeles"]["claude-code"][niveau]
    except KeyError as exc:
        raise KeyError(
            f"{nom_role} : niveau {niveau!r} absent de modeles.claude-code dans "
            f"{ROLES_YML}"
        ) from exc
    if not modele:
        raise ValueError(
            f"{nom_role} : modeles.claude-code.{niveau} n'est pas renseigné dans "
            f"{ROLES_YML}"
        )

    outils = ", ".join(role["tools"])
    entete = (
        "---\n"
        f"name: {nom_role}\n"
        f"description: {role['description']}\n"
        f"tools: {outils}\n"
        f"model: {modele}\n"
        "---\n"
        "\n"
        f"{AVERTISSEMENT.format(role=nom_role)}\n"
        "\n"
    )
    return entete + corps(nom_role)


def roles_ordonnes(config: dict) -> list[str]:
    return list(config["roles"].keys())


def engendrer_tout(config: dict) -> dict[str, str]:
    """{nom_role: contenu engendré}, pour tous les rôles de roles.yml."""
    return {nom: engendrer_claude_code(nom, config) for nom in roles_ordonnes(config)}


def verifier(config: dict) -> list[str]:
    """Rôles dont .claude/agents/<role>.md n'est pas à jour, ou absent."""
    en_retard = []
    for nom, attendu in engendrer_tout(config).items():
        cible = DOSSIER_CLAUDE / f"{nom}.md"
        if not cible.exists() or cible.read_text(encoding="utf-8") != attendu:
            en_retard.append(nom)
    return en_retard


def ecrire(config: dict) -> list[str]:
    """Écrit les fichiers engendrés ; renvoie les rôles effectivement modifiés."""
    modifies = []
    for nom, attendu in engendrer_tout(config).items():
        cible = DOSSIER_CLAUDE / f"{nom}.md"
        if not cible.exists() or cible.read_text(encoding="utf-8") != attendu:
            cible.write_text(attendu, encoding="utf-8")
            modifies.append(nom)
    return modifies


def main(argv: list[str]) -> int:
    mode_verifier = "--verifier" in argv

    config = charger_config()

    if mode_verifier:
        en_retard = verifier(config)
        if en_retard:
            print(f"{len(en_retard)} sous-agent(s) Claude Code à régénérer :")
            for nom in en_retard:
                print(f"  - .claude/agents/{nom}.md (source : docs/agents/{nom}.md)")
            print("Lancer : uv run python scripts/sync_agents.py")
            return 1
        print(f"{len(config['roles'])} sous-agent(s) Claude Code à jour.")
        return 0

    modifies = ecrire(config)
    if modifies:
        print(f"{len(modifies)} sous-agent(s) régénéré(s) :")
        for nom in modifies:
            print(f"  - .claude/agents/{nom}.md")
    else:
        print(f"{len(config['roles'])} sous-agent(s) Claude Code déjà à jour.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

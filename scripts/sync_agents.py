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
DOSSIER_PI = RACINE / ".pi" / "agents"
ROLES_YML = DOSSIER_DOCS / "roles.yml"

AVERTISSEMENT = (
    "Fichier engendré par scripts/sync_agents.py depuis docs/agents/{role}.md "
    "— ne pas éditer."
)

# Consigne COMMUNE à tous les rôles : insérée par les générateurs après l'avertissement,
# avant le corps. Un seul point d'édition pour « informer tous les agents » du routage des
# reports. Voir docs/backlog-routage.md.
CONSIGNE_COMMUNE = (
    "> **Reports & lacunes.** À chaque point d'arrêt, verse ce qui n'a pu être fait, les données\n"
    "> manquantes et les pistes non suivies à leur destination durable selon\n"
    "> `docs/backlog-routage.md` — jamais seulement dans la conversation ou une liste de session.\n"
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
        f"{CONSIGNE_COMMUNE}"
        "\n"
    )
    return entete + corps(nom_role)


def engendrer_pi(nom_role: str, config: dict) -> str:
    """L'en-tête YAML + l'avertissement + le corps, format .pi/agents/*.md
    (extension @tintinweb/pi-subagents). Mêmes champs que Claude Code (`name`,
    `description`, `tools`, `model`), que pi accepte. Le modèle vient de
    `modeles.pi` selon le niveau ; s'il est null (non renseigné), la ligne
    `model:` est OMISE et l'agent hérite du modèle de la session parente
    (défaut documenté de pi) — on n'invente aucun identifiant."""
    role = config["roles"][nom_role]
    niveau = role["niveau"]
    try:
        modele = config["modeles"]["pi"][niveau]
    except KeyError as exc:
        raise KeyError(
            f"{nom_role} : niveau {niveau!r} absent de modeles.pi dans {ROLES_YML}"
        ) from exc
    outils = ", ".join(role["tools"])
    lignes = ["---", f"name: {nom_role}", f"description: {role['description']}",
              f"tools: {outils}"]
    if modele:
        lignes.append(f"model: {modele}")
    lignes += ["---", "", AVERTISSEMENT.format(role=nom_role), "", CONSIGNE_COMMUNE]
    return "\n".join(lignes) + "\n" + corps(nom_role)


# Cibles engendrées : (nom, dossier, générateur). Ajouter un outil = une entrée
# ici + une fonction engendrer_<outil>() + une table modeles.<outil> dans
# roles.yml — jamais deviner le format d'en-tête d'un outil non vérifié.
# Le dossier est nommé (pas capturé) : les tests monkey-patchent DOSSIER_CLAUDE
# et DOSSIER_PI, et engendrer_tout() doit lire la valeur COURANTE du module —
# une Path figée ici écrirait dans le dépôt réel pendant les tests.
CIBLES = [
    ("claude-code", "DOSSIER_CLAUDE", engendrer_claude_code),
    ("pi", "DOSSIER_PI", engendrer_pi),
]


def roles_ordonnes(config: dict) -> list[str]:
    return list(config["roles"].keys())


def engendrer_tout(config: dict) -> dict[tuple[str, str], tuple[Path, str]]:
    """{(outil, role): (chemin_cible, contenu)} pour toutes les cibles."""
    out = {}
    for nom_outil, nom_dossier, gen in CIBLES:
        dossier = globals()[nom_dossier]
        for nom in roles_ordonnes(config):
            out[(nom_outil, nom)] = (dossier / f"{nom}.md", gen(nom, config))
    return out


def verifier(config: dict) -> list[str]:
    """Fichiers engendrés pas à jour ou absents, format 'outil/role'."""
    en_retard = []
    for (nom_outil, nom), (cible, attendu) in engendrer_tout(config).items():
        if not cible.exists() or cible.read_text(encoding="utf-8") != attendu:
            en_retard.append(f"{nom_outil}/{nom}")
    return en_retard


def ecrire(config: dict) -> list[str]:
    """Écrit les fichiers engendrés ; renvoie les cibles modifiées 'outil/role'."""
    modifies = []
    for (nom_outil, nom), (cible, attendu) in engendrer_tout(config).items():
        if not cible.exists() or cible.read_text(encoding="utf-8") != attendu:
            cible.parent.mkdir(parents=True, exist_ok=True)
            cible.write_text(attendu, encoding="utf-8")
            modifies.append(f"{nom_outil}/{nom}")
    return modifies


def main(argv: list[str]) -> int:
    mode_verifier = "--verifier" in argv

    config = charger_config()

    total = len(config["roles"]) * len(CIBLES)
    if mode_verifier:
        en_retard = verifier(config)
        if en_retard:
            print(f"{len(en_retard)} sous-agent(s) à régénérer :")
            for cle in en_retard:
                outil, nom = cle.split("/", 1)
                dossier = ".claude/agents" if outil == "claude-code" else ".pi/agents"
                print(f"  - {dossier}/{nom}.md (source : docs/agents/{nom}.md)")
            print("Lancer : uv run python scripts/sync_agents.py")
            return 1
        print(f"{total} sous-agent(s) à jour ({len(CIBLES)} outils).")
        return 0

    modifies = ecrire(config)
    if modifies:
        print(f"{len(modifies)} sous-agent(s) régénéré(s) :")
        for cle in modifies:
            outil, nom = cle.split("/", 1)
            dossier = ".claude/agents" if outil == "claude-code" else ".pi/agents"
            print(f"  - {dossier}/{nom}.md")
    else:
        print(f"{total} sous-agent(s) déjà à jour ({len(CIBLES)} outils).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""Engendre les sous-agents de PLUSIEURS harnais à partir des rôles neutres.

Le TEXTE de chaque rôle (documentaliste, rédacteur, terminologue, bibliographe,
relecteur-ar, modeliste…) vit dans `docs/agents/<role>.md` — de la prose simple,
sans en-tête ni syntaxe propre à un outil. Ses métadonnées (`description`, une
liste d'outils en VOCABULAIRE NEUTRE, et un NIVEAU abstrait qui dit combien de
jugement la tâche demande) vivent dans `docs/agents/roles.yml`, avec une table
`modeles` qui associe chaque niveau à un modèle, par harnais.

Ce script engendre un fichier de sous-agent pour chaque harnais VÉRIFIÉ :
    - claude-code → .claude/agents/<role>.md  (tools: liste ; model requis)
    - pi          → .pi/agents/<role>.md      (tools: liste ; model omis si null)
    - opencode    → .opencode/agent/<role>.md  (mode: subagent ; model omis si null)
Chacun porte l'en-tête propre au harnais, une ligne d'avertissement, la consigne
commune, puis le corps commun tel quel.

VOCABULAIRE D'OUTILS NEUTRE — roles.yml écrit des noms indépendants du harnais
(read, write, edit, grep, glob, bash, web_search, web_fetch) ; `OUTILS_PAR_HARNAIS`
les traduit dans le nom que chaque harnais attend. C'est le correctif central :
pi et opencode nomment la recherche web `web_search`/`web_fetch`, là où Claude
Code dit `WebSearch`/`WebFetch` ; écrire les noms Claude en dur faisait démarrer
documentaliste/économiste/bibliographe SANS web sous pi (pi ignore un nom d'outil
qu'il ne connaît pas). De même `glob` → `Glob` (Claude) mais `find` (pi, opencode).

    uv run python scripts/sync_agents.py              # écrit les trois cibles
    uv run python scripts/sync_agents.py --verifier   # ne rien écrire ; sort 1
                                                        # si un fichier engendré
                                                        # n'est pas à jour

La CI (`verifier-conventions.yml`) et `scripts/verifier.sh` lancent `--verifier` :
un rôle édité dans `docs/agents/` sans régénération laisse les cibles en retard,
silencieusement, jusqu'à ce contrôle.

Pour un AUTRE outil (Codex, Cursor…) : ce script ne fournit délibérément aucune
génération, faute de format de sous-agent vérifié pour lui ici — la table
`modeles.openai` de `roles.yml` est d'ailleurs vide (« à renseigner par
l'humain »). Le chemin documenté (voir docs/conventions/economiser.md) est de
charger `docs/agents/<role>.md` comme consigne et de choisir le modèle dans
`modeles.<outil>` selon `roles.<role>.niveau`. Si un format d'en-tête pour cet
outil devient vérifié, ajouter une table `OUTILS_PAR_HARNAIS[<outil>]`, une
fonction `engendrer_<outil>()`, une entrée `CIBLES` et une table
`modeles.<outil>` : ne pas deviner ce format à l'avance.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
DOSSIER_DOCS = RACINE / "docs" / "agents"
DOSSIER_CLAUDE = RACINE / ".claude" / "agents"
DOSSIER_PI = RACINE / ".pi" / "agents"
DOSSIER_OPENCODE = RACINE / ".opencode" / "agent"
ROLES_YML = DOSSIER_DOCS / "roles.yml"

# Libellé du dossier pour les messages à l'humain, par harnais.
DOSSIER_AFFICHE = {
    "claude-code": ".claude/agents",
    "pi": ".pi/agents",
    "opencode": ".opencode/agent",
}

# Traduction du vocabulaire d'outils neutre (roles.yml) vers le nom que chaque
# harnais attend. Un nom neutre absent d'une table est une erreur explicite
# (traduire_outils lève) : on ajoute la traduction, on ne devine pas. Les noms
# pi/opencode sont relevés sur les agents écrits à la main qui fonctionnent
# (~/.pi/agent/agents/, ~/.config/opencode/agent/ : read, grep, find, bash,
# web_search, web_fetch).
OUTILS_PAR_HARNAIS = {
    "claude-code": {
        "read": "Read", "write": "Write", "edit": "Edit", "grep": "Grep",
        "glob": "Glob", "bash": "Bash",
        "web_search": "WebSearch", "web_fetch": "WebFetch",
    },
    "pi": {
        "read": "read", "write": "write", "edit": "edit", "grep": "grep",
        "glob": "find", "bash": "bash",
        "web_search": "web_search", "web_fetch": "web_fetch",
    },
    "opencode": {
        "read": "read", "write": "write", "edit": "edit", "grep": "grep",
        "glob": "find", "bash": "bash",
        "web_search": "web_search", "web_fetch": "web_fetch",
    },
}

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


def traduire_outils(outils_neutres: list[str], harnais: str) -> str:
    """La liste d'outils neutre, traduite et jointe pour l'en-tête du harnais.
    Lève si un nom neutre n'a pas de traduction connue — on ne devine pas."""
    table = OUTILS_PAR_HARNAIS[harnais]
    traduits = []
    for nom in outils_neutres:
        try:
            traduits.append(table[nom])
        except KeyError as exc:
            raise KeyError(
                f"outil neutre {nom!r} absent de OUTILS_PAR_HARNAIS[{harnais!r}] "
                f"(dans {__file__}) — ajouter sa traduction, ne pas deviner"
            ) from exc
    return ", ".join(traduits)


def modele_pour(nom_role: str, config: dict, harnais: str):
    """Le modèle du rôle pour ce harnais, ou None si la table le laisse à null.
    Lève KeyError si le niveau du rôle est absent de la table du harnais."""
    niveau = config["roles"][nom_role]["niveau"]
    try:
        return config["modeles"][harnais][niveau]
    except KeyError as exc:
        raise KeyError(
            f"{nom_role} : niveau {niveau!r} absent de modeles.{harnais} dans "
            f"{ROLES_YML}"
        ) from exc


def engendrer_claude_code(nom_role: str, config: dict) -> str:
    """L'en-tête YAML + l'avertissement + le corps, format .claude/agents/*.md.
    Claude Code EXIGE un modèle : un niveau à null lève plutôt qu'écrire None."""
    role = config["roles"][nom_role]
    modele = modele_pour(nom_role, config, "claude-code")
    if not modele:
        niveau = role["niveau"]
        raise ValueError(
            f"{nom_role} : modeles.claude-code.{niveau} n'est pas renseigné dans "
            f"{ROLES_YML}"
        )

    outils = traduire_outils(role["tools"], "claude-code")
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
    (agents natifs de pi). Champs `name`, `description`, `tools`, `model`. Les
    outils sont traduits en noms pi (web_search/web_fetch, find…). Le modèle
    vient de `modeles.pi` selon le niveau ; s'il est null, la ligne `model:` est
    OMISE et l'agent hérite du modèle de la session parente (défaut documenté de
    pi) — on n'invente aucun identifiant."""
    role = config["roles"][nom_role]
    modele = modele_pour(nom_role, config, "pi")
    outils = traduire_outils(role["tools"], "pi")
    lignes = ["---", f"name: {nom_role}", f"description: {role['description']}",
              f"tools: {outils}"]
    if modele:
        lignes.append(f"model: {modele}")
    lignes += ["---", "", AVERTISSEMENT.format(role=nom_role), "", CONSIGNE_COMMUNE]
    return "\n".join(lignes) + "\n" + corps(nom_role)


def engendrer_opencode(nom_role: str, config: dict) -> str:
    """L'en-tête YAML + l'avertissement + le corps, format .opencode/agent/*.md
    (opencode V1, binaire 1.x). Champs relevés sur les agents opencode écrits à
    la main qui fonctionnent (~/.config/opencode/agent/) : `mode: subagent`,
    `name`, `description`, `tools` (liste), `model`. Les outils sont traduits en
    noms opencode (mêmes noms que pi). Le modèle vient de `modeles.opencode` ;
    null → ligne `model:` OMISE, l'agent hérite du modèle parent — rien d'inventé."""
    role = config["roles"][nom_role]
    modele = modele_pour(nom_role, config, "opencode")
    outils = traduire_outils(role["tools"], "opencode")
    lignes = ["---", "mode: subagent", f"name: {nom_role}",
              f"description: {role['description']}", f"tools: {outils}"]
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
    ("opencode", "DOSSIER_OPENCODE", engendrer_opencode),
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
                dossier = DOSSIER_AFFICHE[outil]
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
            dossier = DOSSIER_AFFICHE[outil]
            print(f"  - {dossier}/{nom}.md")
    else:
        print(f"{total} sous-agent(s) déjà à jour ({len(CIBLES)} outils).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

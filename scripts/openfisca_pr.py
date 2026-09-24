#!/usr/bin/env python3
"""Outillage des PR openfisca-tunisia (fusion de master, CI, repérage des PR à formules).

Trois sous-commandes, réunies parce qu'elles portent toutes sur le cycle d'une PR du
dépôt de modèle. Rien ici ne fusionne une PR ni n'écrit dans le précis : le seul dépôt
touché est `openfisca-tunisia` (ou son miroir `--depot`), et seulement la branche visée.

    uv run python scripts/openfisca_pr.py maj <PR> <branche> [--depot CHEMIN] [--trailer TEXTE]
    uv run python scripts/openfisca_pr.py ci <PR> [--depot CHEMIN] [--sans-relance] [--attente S]
    uv run python scripts/openfisca_pr.py formules <PR> [--depot CHEMIN]

`maj` — fusionne `origin/master` dans `<branche>` (sans réécrire son historique), en
gardant de master `CHANGELOG.md`, `pyproject.toml` et `uv.lock` : la branche ne porte
que sa propre section de CHANGELOG, réinsérée en tête et renumérotée à la version
« master + 1 » (format `0.NNN` du dépôt, pas semver à trois nombres). Travaille dans
une worktree jetable, en `HEAD` détachée sur `origin/<branche>` — jamais de
`checkout -B <branche>` : si `<branche>` est déjà extraite ailleurs (le clone
principal, une autre worktree), cette commande échoue. La poussée se fait par
`HEAD:<branche>`, jamais par une branche locale du même nom.

Garde-fous :
  - un conflit de fusion hors des trois fichiers ci-dessus interrompt la commande
    (`CONFLIT`, code 3) — la fusion n'est pas terminée, rien n'est poussé ;
  - si `pyproject.toml` de la branche diffère de celui de leur ancêtre commun
    AILLEURS que sur la ligne `version`, la commande s'arrête (code 4) : prendre
    `pyproject.toml` de master effacerait silencieusement une dépendance que la PR
    aurait ajoutée. Revoir à la main, puis relancer avec `--forcer-pyproject` ;
  - rien n'est commité si le résultat ne diffère pas de la branche déjà à jour
    (pas de commit vide).

`ci` — attend que la CI du COMMIT DE TÊTE de la PR (pas le résumé agrégé de la PR, qui
peut rester à « en attente » après coup) ait fini de tourner, puis relance le job
`dbnomics` s'il a échoué par collision de poussée (« rejected … fetch first »), le
seul échec qu'une relance suffit à réparer.

`formules` — liste tous les fichiers `.py` hors tests de la PR, et marque ceux sous
`variables/` ou `regimes/` : une PR qui en touche change des résultats de calcul, et
ne se fusionne pas sans validation humaine (`AGENTS.md`, « Découper »). Sort en 1 dès
qu'un tel fichier est présent.

Aucune sous-commande ne fusionne de PR sur GitHub, n'écrit de message [ci skip]/[no ci]
(ni variante) dans un titre ou un commit, ni ne pousse en force.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

DEPOT_DEFAUT = "/home/benjello/projets/openfisca-tunisia"
FICHIERS_PRIS_DE_MASTER = ("CHANGELOG.md", "pyproject.toml", "uv.lock")
NOM_PAQUET = "openfisca-tunisia"
# Pas de trailer par défaut : ce script est versionné et réutilisé d'une session à
# l'autre, par des agents différents — lui coder en dur l'attribution d'une seule
# session mentirait sur l'auteur des sessions suivantes. `--trailer` (ou son appelant)
# fournit l'attribution qui convient à l'appel en cours.
TRAILER_DEFAUT = ""


class ErreurOutillage(RuntimeError):
    """Erreur métier (conflit, section introuvable, etc.) — jamais une trace Python."""


# --------------------------------------------------------------------------------
# Fonctions pures (testées sans réseau ni dépôt) : renumérotation du CHANGELOG.
# --------------------------------------------------------------------------------

def prochaine_version(ancienne: str) -> str:
    """« 0.112 » -> « 0.113 ». Le dépôt numérote `0.NNN`, pas `MAJEUR.MINEUR.PATCH`."""
    m = re.fullmatch(r"0\.(\d+)", ancienne.strip())
    if not m:
        raise ErreurOutillage(f"version inattendue {ancienne!r} (format attendu « 0.NNN »)")
    return f"0.{int(m.group(1)) + 1}"


def extraire_section(changelog: str, pr: int) -> str:
    """Isole, dans un CHANGELOG entier, la section dont le TITRE lie vers `/pull/<pr>)`.

    Les entrées sont des SŒURS, pas des sections imbriquées : `CONTRIBUTING.md` fait
    porter à chacune le niveau de titre (`#`, `##` ou `###`) qui correspond à
    l'ampleur de son incrément de version, pas à une hiérarchie — un `###` (patch)
    peut très bien précéder un `##` (mineur) sans lui être subordonné (ex. les
    versions 0.31.x/0.33.x du dépôt). Une section court donc jusqu'au TOUT PROCHAIN
    titre, quel que soit son niveau. Diviser sur `## ` seul couperait au milieu
    d'une section `###`, ou l'avalerait dans la section `##` précédente.
    """
    lignes = changelog.splitlines(keepends=True)
    titres = [i for i, l in enumerate(lignes) if re.match(r"^#{1,3} ", l)]
    cibles = [i for i in titres if f"/pull/{pr})" in lignes[i]]
    if len(cibles) != 1:
        raise ErreurOutillage(
            f"section de la PR #{pr} : {len(cibles)} titre(s) trouvé(s), 1 attendu")
    debut = cibles[0]
    suivants = [i for i in titres if i > debut]
    fin = suivants[0] if suivants else len(lignes)
    return "".join(lignes[debut:fin])


def renumeroter_section(section: str, nouvelle_version: str) -> str:
    """Remplace le numéro de version du titre, en conservant son niveau (#, ## ou ###).

    Le numéro remplacé peut avoir deux composantes (`0.112`, format actuel) ou trois
    (`0.33.4`, format des versions plus anciennes du CHANGELOG) : on accepte les deux.
    """
    nouvelle, n = re.subn(
        r"^(#{1,3} )[0-9]+(?:\.[0-9]+)+\b", rf"\g<1>{nouvelle_version}", section, count=1)
    if n != 1:
        raise ErreurOutillage(f"titre de section inattendu : {section.splitlines()[0]!r}")
    return nouvelle


def inserer_en_tete(changelog_master: str, section: str) -> str:
    """Insère `section` juste après l'en-tête `# Changelog`, avant tout le reste."""
    entete = "# Changelog\n\n"
    if not changelog_master.startswith(entete):
        raise ErreurOutillage("CHANGELOG.md ne commence pas par « # Changelog\\n\\n »")
    return entete + section.rstrip("\n") + "\n\n" + changelog_master[len(entete):]


def remplacer_version_pyproject(pyproject: str, ancienne: str, nouvelle: str) -> str:
    motif = f'version = "{ancienne}"'
    if pyproject.count(motif) != 1:
        raise ErreurOutillage(
            f"« {motif} » : {pyproject.count(motif)} occurrence(s) dans pyproject.toml, 1 attendue")
    # Seule la PREMIÈRE occurrence : le fichier peut citer une contrainte de version
    # d'une dépendance sous la même forme plus bas.
    return pyproject.replace(motif, f'version = "{nouvelle}"', 1)


def remplacer_version_uv_lock(uv_lock: str, ancienne: str, nouvelle: str) -> str:
    motif = f'name = "{NOM_PAQUET}"\nversion = "{ancienne}"'
    if uv_lock.count(motif) != 1:
        raise ErreurOutillage(
            f"entrée « {NOM_PAQUET} {ancienne} » : {uv_lock.count(motif)} trouvée(s) dans "
            "uv.lock, 1 attendue")
    return uv_lock.replace(motif, f'name = "{NOM_PAQUET}"\nversion = "{nouvelle}"', 1)


def lire_version_pyproject(pyproject: str) -> str:
    m = re.search(r'(?m)^version\s*=\s*"([^"]+)"', pyproject)
    if not m:
        raise ErreurOutillage("pyproject.toml : aucune ligne « version = \"…\" »")
    return m.group(1)


def diff_hors_version(ancien_pyproject: str, nouveau_pyproject: str) -> bool:
    """Vrai si `pyproject.toml` diffère AILLEURS que sur la ligne de version."""
    def sans_version(texte: str) -> list[str]:
        return [l for l in texte.splitlines() if not re.match(r'^version\s*=', l)]
    return sans_version(ancien_pyproject) != sans_version(nouveau_pyproject)


# --------------------------------------------------------------------------------
# Appels externes (git, gh) — isolés pour que les fonctions ci-dessus restent pures.
# --------------------------------------------------------------------------------

def sh(args: list[str], cwd: str | Path | None = None, check: bool = True) -> str:
    resultat = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if check and resultat.returncode != 0:
        raise ErreurOutillage(
            f"« {' '.join(args)} » a échoué (code {resultat.returncode}) :\n{resultat.stderr}")
    return resultat.stdout


def depot_owner_repo(depot: str) -> str:
    """« owner/repo » déduit de `git remote -v`, pour les appels `gh api`."""
    sortie = sh(["git", "remote", "get-url", "origin"], cwd=depot)
    m = re.search(r"[:/]([^/:]+)/([^/]+?)(?:\.git)?\s*$", sortie.strip())
    if not m:
        raise ErreurOutillage(f"URL d'origine illisible : {sortie!r}")
    return f"{m.group(1)}/{m.group(2)}"


# --------------------------------------------------------------------------------
# maj
# --------------------------------------------------------------------------------

def cmd_maj(args: argparse.Namespace) -> int:
    depot, pr, branche = args.depot, args.pr, args.branche
    trailer = args.trailer or TRAILER_DEFAUT

    sh(["git", "fetch", "-q", "origin"], cwd=depot)
    changelog_branche = sh(["git", "show", f"origin/{branche}:CHANGELOG.md"], cwd=depot)
    pyproject_branche = sh(["git", "show", f"origin/{branche}:pyproject.toml"], cwd=depot)
    base = sh(["git", "merge-base", "origin/master", f"origin/{branche}"], cwd=depot).strip()
    pyproject_base = sh(["git", "show", f"{base}:pyproject.toml"], cwd=depot)

    if not args.forcer_pyproject and diff_hors_version(pyproject_base, pyproject_branche):
        raise ErreurOutillage(
            "pyproject.toml de la branche diffère de celui de sa base ailleurs que sur la "
            "version (dépendance ajoutée ?) : prendre celui de master l'effacerait. Revoir "
            "à la main, puis relancer avec --forcer-pyproject si c'est sans conséquence.")

    with tempfile.TemporaryDirectory(prefix="openfisca-pr-maj-") as tmp:
        sh(["git", "worktree", "add", "-q", "--detach", tmp, f"origin/{branche}"], cwd=depot)
        try:
            fusion = subprocess.run(
                ["git", "merge", "--no-commit", "--no-ff", "origin/master"],
                cwd=tmp, capture_output=True, text=True)
            en_conflit = sh(["git", "diff", "--name-only", "--diff-filter=U"], cwd=tmp).split()
            hors_liste = [f for f in en_conflit if f not in FICHIERS_PRIS_DE_MASTER]
            if hors_liste or (fusion.returncode != 0 and not en_conflit):
                sh(["git", "merge", "--abort"], cwd=tmp, check=False)
                if hors_liste:
                    raise ErreurOutillage(f"CONFLIT hors des fichiers pris de master : {hors_liste}")
                raise ErreurOutillage(f"échec de la fusion :\n{fusion.stderr}")

            ancienne_version = lire_version_pyproject(
                sh(["git", "show", "origin/master:pyproject.toml"], cwd=depot))
            nouvelle_version = prochaine_version(ancienne_version)

            sh(["git", "checkout", "-q", "origin/master", "--", *FICHIERS_PRIS_DE_MASTER], cwd=tmp)

            section = renumeroter_section(extraire_section(changelog_branche, pr), nouvelle_version)
            changelog_master = (Path(tmp) / "CHANGELOG.md").read_text(encoding="utf-8")
            (Path(tmp) / "CHANGELOG.md").write_text(
                inserer_en_tete(changelog_master, section), encoding="utf-8")

            pyproject_master = (Path(tmp) / "pyproject.toml").read_text(encoding="utf-8")
            (Path(tmp) / "pyproject.toml").write_text(
                remplacer_version_pyproject(pyproject_master, ancienne_version, nouvelle_version),
                encoding="utf-8")

            uv_lock_master = (Path(tmp) / "uv.lock").read_text(encoding="utf-8")
            (Path(tmp) / "uv.lock").write_text(
                remplacer_version_uv_lock(uv_lock_master, ancienne_version, nouvelle_version),
                encoding="utf-8")

            sh(["git", "add", "-A"], cwd=tmp)
            diff_cache = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=tmp)
            if diff_cache.returncode == 0:
                print(f"maj {branche} : rien à committer (déjà à jour, version {ancienne_version}).")
                return 0

            message = f"Merge master into {branche} : version {nouvelle_version}"
            if trailer:
                message += f"\n\n{trailer}"
            sh(["git", "commit", "-q", "-m", message], cwd=tmp)
            sh(["git", "push", "-q", "origin", f"HEAD:{branche}"], cwd=tmp)
            print(f"maj {branche} : version {ancienne_version} -> {nouvelle_version}, poussé.")
            return 0
        finally:
            sh(["git", "worktree", "remove", "--force", tmp], cwd=depot, check=False)


# --------------------------------------------------------------------------------
# ci
# --------------------------------------------------------------------------------

def _check_runs(depot: str, sha: str) -> list[dict]:
    repo = depot_owner_repo(depot)
    sortie = sh(["gh", "api", f"repos/{repo}/commits/{sha}/check-runs", "--paginate"], cwd=depot)
    runs: list[dict] = []
    for bloc in sortie.strip().split("\n"):
        if bloc.strip():
            runs.extend(json.loads(bloc)["check_runs"])
    return runs


def _run_id_de(check_run: dict) -> str:
    """Le SEUL endroit qui suppose que l'id du check-run == l'id du job Actions.

    C'est le cas pour les jobs GitHub Actions (constaté sur ce dépôt le 24/09/2026) :
    `html_url` a la forme `.../actions/runs/<run-id>/job/<job-id>`, et `<job-id>` vaut
    `check_run["id"]`. `gh run rerun` réclame néanmoins le `<run-id>`, extrait d'ici.
    """
    m = re.search(r"/actions/runs/(\d+)/job/\d+", check_run.get("html_url") or "")
    if not m:
        raise ErreurOutillage(f"run-id introuvable dans html_url : {check_run.get('html_url')!r}")
    return m.group(1)


def _attendre_completion(depot: str, sha: str, attente: int, intervalle: int) -> list[dict] | None:
    """Sonde `check-runs` jusqu'à ce que plus rien ne soit `en_cours`, ou expire.

    `gh api .../check-runs` ne rend, par défaut, que la DERNIÈRE tentative de
    chaque job (`filter=latest`) : une relance (`gh run rerun --job`) y remplace
    donc directement l'échec qu'elle rejoue, sans qu'il faille la distinguer ici.
    """
    attente_totale = 0
    while True:
        runs = _check_runs(depot, sha)
        if not runs:
            print("  aucun check-run pour l'instant…")
        else:
            en_cours = [r for r in runs if r["status"] != "completed"]
            echecs = [r for r in runs if r["status"] == "completed"
                      and r["conclusion"] not in ("success", "skipped", "neutral")]
            print(f"  {len(runs) - len(en_cours)}/{len(runs)} terminé(s), "
                  f"{len(echecs)} en échec.")
            if not en_cours:
                return runs
        if attente_totale >= attente:
            return None
        time.sleep(min(intervalle, attente - attente_totale))
        attente_totale += intervalle


def cmd_ci(args: argparse.Namespace) -> int:
    depot, pr = args.depot, args.pr
    repo = depot_owner_repo(depot)
    sha = json.loads(sh(["gh", "pr", "view", str(pr), "--repo", repo, "--json", "headRefOid"]))[
        "headRefOid"]
    print(f"ci PR #{pr} : commit de tête {sha}")

    relances_restantes = 0 if args.sans_relance else args.max_relances
    while True:
        runs = _attendre_completion(depot, sha, args.attente, args.intervalle)
        if runs is None:
            print(f"ci : encore en cours après {args.attente}s, abandon de l'attente.")
            return 1

        echecs = [r for r in runs if r["conclusion"] not in ("success", "skipped", "neutral")]
        if not echecs:
            print("ci : tout est vert.")
            return 0

        for run in echecs:
            print(f"  ✗ {run['name']} : {run['conclusion']} — {run['html_url']}")

        if relances_restantes <= 0:
            if args.sans_relance:
                print("ci : échec(s) restant(s), --sans-relance : pas de relance.")
            else:
                print("ci : échec(s) restant(s) après le nombre maximal de relances.")
            return 1

        releve = 0
        for run in echecs:
            if "dbnomics" not in run["name"]:
                continue
            run_id = _run_id_de(run)
            journal = sh(["gh", "run", "view", run_id, "--job", str(run["id"]), "--log-failed"],
                         cwd=depot, check=False)
            if "rejected" in journal and "fetch first" in journal:
                print(f"  → collision de poussée détectée sur {run['name']}, relance…")
                sh(["gh", "run", "rerun", run_id, "--job", str(run["id"])], cwd=depot)
                releve += 1
            else:
                print(f"  → {run['name']} en échec pour une autre raison, pas de relance automatique.")

        if releve != len(echecs):
            print("ci : au moins un échec n'est pas une collision dbnomics relançable.")
            return 1

        relances_restantes -= 1
        print(f"  → relancé, on rattend la CI ({relances_restantes} relance(s) restante(s))…")


# --------------------------------------------------------------------------------
# formules
# --------------------------------------------------------------------------------

def _est_un_test(chemin: str) -> bool:
    segments = chemin.split("/")
    return "tests" in segments or "tests_pension" in segments or Path(chemin).name.startswith("test_")


def fichiers_py_hors_tests(fichiers: list[str]) -> list[str]:
    """Tous les fichiers `.py` de la PR, hors tests — quel que soit leur dossier."""
    return [f for f in fichiers if f.endswith(".py") and not _est_un_test(f)]


def est_fichier_formule(chemin: str) -> bool:
    """Sous `variables/` ou `regimes/` : une PR qui en touche change des résultats
    de calcul, et ne se fusionne pas sans validation humaine."""
    segments = chemin.split("/")
    return "variables" in segments or "regimes" in segments


def cmd_formules(args: argparse.Namespace) -> int:
    depot, pr = args.depot, args.pr
    repo = depot_owner_repo(depot)
    sortie = sh(["gh", "api", f"repos/{repo}/pulls/{pr}/files", "--paginate",
                 "-q", ".[].filename"], cwd=depot)
    fichiers = [l for l in sortie.splitlines() if l.strip()]
    py_hors_tests = fichiers_py_hors_tests(fichiers)
    if not py_hors_tests:
        print(f"formules PR #{pr} : aucun fichier .py hors tests. Rien à signaler.")
        return 0

    print(f"formules PR #{pr} : fichier(s) .py hors tests :")
    for f in py_hors_tests:
        marque = " ← variables/regimes" if est_fichier_formule(f) else ""
        print(f"  - {f}{marque}")

    a_formules = [f for f in py_hors_tests if est_fichier_formule(f)]
    if a_formules:
        print("PR À FORMULES (sous variables/ ou regimes/), ne pas fusionner sans validation humaine.")
        return 1
    return 0


# --------------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument("--depot", default=DEPOT_DEFAUT,
                         help=f"chemin du dépôt openfisca-tunisia (défaut : {DEPOT_DEFAUT})")

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = parser.add_subparsers(dest="commande", required=True)

    p_maj = sous.add_parser("maj", parents=[parent], help="fusionne master dans une branche")
    p_maj.add_argument("pr", type=int)
    p_maj.add_argument("branche")
    p_maj.add_argument("--trailer", default=None,
                        help="pied de commit (jamais de drapeau [ci skip]/[no ci])")
    p_maj.add_argument("--forcer-pyproject", action="store_true",
                        help="ignore un pyproject.toml de la branche modifié hors la version")
    p_maj.set_defaults(func=cmd_maj)

    p_ci = sous.add_parser("ci", parents=[parent], help="attend la CI du commit de tête")
    p_ci.add_argument("pr", type=int)
    p_ci.add_argument("--sans-relance", action="store_true",
                       help="n'essaie pas de relancer dbnomics sur collision")
    p_ci.add_argument("--attente", type=int, default=1800, help="secondes avant abandon, PAR sondage")
    p_ci.add_argument("--intervalle", type=int, default=30, help="secondes entre deux sondages")
    p_ci.add_argument("--max-relances", type=int, default=2,
                       help="relances dbnomics au plus, avant d'abandonner (défaut : 2)")
    p_ci.set_defaults(func=cmd_ci)

    p_formules = sous.add_parser("formules", parents=[parent],
                                  help="liste les fichiers de variables/regimes hors tests")
    p_formules.add_argument("pr", type=int)
    p_formules.set_defaults(func=cmd_formules)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except ErreurOutillage as erreur:
        print(f"✗ {erreur}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())

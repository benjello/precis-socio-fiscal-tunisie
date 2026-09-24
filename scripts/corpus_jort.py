"""Mise à jour du corpus local du JORT : la base `jort_cache.db` et les fascicules.

    uv run python scripts/corpus_jort.py crawl --from 2026 --to 2026 [--delai-max 3600] [--a-blanc]
    uv run python scripts/corpus_jort.py telecharger 2025 2026 [--a-blanc]

Le dépôt `~/projets/PDFs-legislation-tunisie` appartient à un autre utilisateur ; seuls
`jort_cache.db` et `PDFs/JORT/` y sont à nous. Ce script n'écrit RIEN d'autre dans ce
dépôt (`docs/notes/outillage-sources.md`, § 1 et 3) :

`crawl` met à jour les métadonnées par le crawler du dépôt (`jort_api.crawl`), mais sur
une COPIE : sauvegarde datée de la base dans `~/sauvegardes/`, crawl de la copie dans un
délai maximal (le crawler boucle sans fin sur une erreur réseau, dont celle du certificat
échu), `pragma integrity_check`, contrôle que le nombre de textes ne baisse pas, puis
recopie du CONTENU par-dessus `jort_cache.db` (le répertoire du dépôt n'est pas
inscriptible : pas de renommage). Relancer ensuite le serveur MCP `jort`, qui garde
l'ancienne base ouverte.

`telecharger` rapatrie de pist.tn les fascicules FR et AR que `jort_cache` connaît et que
`PDFs/JORT/<année>/<fr|ar>/` n'a pas. Rien n'est écrit qui ne commence par `%PDF`, ni
par-dessus un fichier existant (écriture `.part`, puis lien sans écrasement) ; une
requête toutes les 0,5 s.

Le certificat de www.pist.tn est échu depuis le 25 août 2026 : la vérification TLS est
désactivée pour ce seul hôte, avec l'autorisation explicite de l'humain du 24 septembre
2026 (`scripts/pist_tls.py`, seul endroit où elle tombe).
"""

from __future__ import annotations

import argparse
import datetime as dt
import http.client
import os
import shutil
import signal
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pist_tls  # noqa: E402
import recherches as r  # noqa: E402

SAUVEGARDES = Path.home() / "sauvegardes"
COPIE = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "precis-recherches" / "jort_cache.crawl.db"
DELAI = 0.5


def depot() -> Path:
    return r.PDFS_LEGISLATION


def dossier_jort() -> Path:
    return depot() / "PDFs" / "JORT"


# ---------------------------------------------------------------------------
# crawl
# ---------------------------------------------------------------------------


def copie_sqlite(source: Path, cible: Path) -> None:
    """Copie cohérente d'une base SQLite (API de sauvegarde), la source ouverte en lecture."""
    cible.parent.mkdir(parents=True, exist_ok=True)
    src = sqlite3.connect(f"file:{source}?mode=ro", uri=True)
    dst = sqlite3.connect(cible)
    try:
        src.backup(dst)
    finally:
        dst.close()
        src.close()


def controle(chemin: Path) -> tuple[str, int]:
    """(résultat de `pragma integrity_check`, nombre de textes)."""
    cnx = sqlite3.connect(f"file:{chemin}?mode=ro", uri=True)
    try:
        integrite = cnx.execute("pragma integrity_check").fetchone()[0]
        n = cnx.execute("select count(*) from textes").fetchone()[0]
    finally:
        cnx.close()
    return integrite, n


def commande_crawl(copie: Path, debut: int, fin: int) -> list[str]:
    # `--no-sync` : uv ne touche ni au .venv ni au uv.lock du dépôt, qui n'est pas à nous.
    return ["uv", "run", "--no-sync", "--project", str(depot()), "python",
            str(Path(__file__).resolve().parent / "pist_tls.py"), "crawl",
            "--db", str(copie), "--from", str(debut), "--to", str(fin)]


def lance_borne(cmd: list[str], delai_max: float) -> int | None:
    """Lance `cmd` dans son propre groupe de processus ; au-delà de `delai_max`, tue tout
    le groupe (uv lance Python en petit-fils : tuer uv seul laisserait le crawler tourner).
    Rend le code de retour, ou None en cas de dépassement."""
    proc = subprocess.Popen(cmd, start_new_session=True)
    try:
        return proc.wait(timeout=delai_max)
    except subprocess.TimeoutExpired:
        return None
    finally:
        # Dépassement, Ctrl-C (le groupe détaché ne reçoit pas le SIGINT du terminal) ou
        # toute autre sortie : aucun crawler ne survit à la commande.
        if proc.poll() is None:
            tue_groupe(proc)


def tue_groupe(proc: subprocess.Popen) -> None:
    for sig in (signal.SIGTERM, signal.SIGKILL):
        try:
            os.killpg(proc.pid, sig)
        except ProcessLookupError:
            return
        try:
            proc.wait(timeout=10)
            return
        except subprocess.TimeoutExpired:
            continue


def cmd_crawl(debut: int, fin: int, delai_max: float, a_blanc: bool) -> int:
    base = r.chemin_base()
    horodatage = dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
    sauvegarde = SAUVEGARDES / f"jort_cache.db.{horodatage}"
    cmd = commande_crawl(COPIE, debut, fin)
    print(f"base         : {base}")
    print(f"sauvegarde   : {sauvegarde}")
    print(f"copie        : {COPIE}")
    print(f"crawl        : {' '.join(cmd)}")
    print(f"délai maximal: {delai_max:.0f} s")
    if not base.exists():
        print(f"✗ base absente : {base}")
        return 1
    if not os.access(base, os.W_OK):
        print(f"✗ base non inscriptible : {base}")
        return 1
    if a_blanc:
        print("\n(à blanc : rien n'est copié ni lancé)")
        return 0

    if sauvegarde.exists():
        print(f"✗ la sauvegarde existe déjà : {sauvegarde}")
        return 1
    copie_sqlite(base, sauvegarde)
    integrite, avant = controle(sauvegarde)
    print(f"✓ sauvegarde : {avant} textes, intégrité {integrite}")
    if integrite != "ok":
        print("✗ la base d'origine n'est pas intègre : rien n'est lancé")
        return 1
    etat_base = (base.stat().st_size, base.stat().st_mtime_ns)

    for f in (COPIE, COPIE.with_name(COPIE.name + "-journal"), COPIE.with_name(COPIE.name + "-wal")):
        f.unlink(missing_ok=True)
    copie_sqlite(base, COPIE)
    code = lance_borne(cmd, delai_max)
    if code is None:
        print(f"✗ crawl interrompu après {delai_max:.0f} s (erreur réseau en boucle ?) : "
              f"jort_cache.db n'est pas touchée ; copie partielle : {COPIE}")
        return 1
    if code != 0:
        print(f"✗ le crawler a échoué (code {code}) : jort_cache.db n'est pas touchée")
        return 1
    for suffixe in ("-journal", "-wal"):
        if COPIE.with_name(COPIE.name + suffixe).exists():
            print(f"✗ journal SQLite résiduel ({suffixe}) : copie non close, rien n'est recopié")
            return 1
    integrite, apres = controle(COPIE)
    print(f"copie crawlée : {apres} textes (avant : {avant}), intégrité {integrite}")
    if integrite != "ok":
        print("✗ copie non intègre : jort_cache.db n'est pas touchée")
        return 1
    if apres < avant:
        print("✗ le nombre de textes baisse : jort_cache.db n'est pas touchée")
        return 1
    if (base.stat().st_size, base.stat().st_mtime_ns) != etat_base:
        print("✗ jort_cache.db a changé pendant le crawl : rien n'est recopié par-dessus")
        return 1
    try:
        shutil.copyfile(COPIE, base)  # le contenu, en place : le répertoire n'est pas inscriptible
    except BaseException:
        print(f"✗ recopie interrompue : jort_cache.db est peut-être tronquée. Retour arrière : "
              f"cp {sauvegarde} {base}")
        raise
    integrite, final = controle(base)
    print(f"✓ jort_cache.db mise à jour : {final} textes (+{final - avant}), intégrité {integrite}")
    print(f"  dernière publication indexée : {r.derniere_publication(r.ouvre_base(base))}")
    print("→ relancer le serveur MCP `jort` (/mcp dans Claude Code) : il garde l'ancienne base ouverte.")
    print(f"  Retour arrière : cp {sauvegarde} {base}")
    COPIE.unlink(missing_ok=True)
    return 0 if integrite == "ok" else 1


# ---------------------------------------------------------------------------
# telecharger
# ---------------------------------------------------------------------------


def numeros_connus(base: Path, annee: int) -> list[int]:
    cnx = r.ouvre_base(base)
    try:
        return sorted({int(n) for (n,) in cnx.execute(
            "select distinct jort_numero from textes where jort_annee = ? and jort_numero is not null",
            (annee,)) if str(n).isdigit()})
    finally:
        cnx.close()


def numeros_douteux(base: Path, annee: int) -> list[int]:
    """Numéros postérieurs au dernier numéro cohérent avec les dates (n° 107 de 2026 pour
    le n° 7, n° 203 de 2025 pour le n° 102) : pist.tn y répondra sans doute 404."""
    cnx = r.ouvre_base(base)
    try:
        dates = {(a, n): d for a, n, d in cnx.execute(
            "select jort_annee, jort_numero, min(date_publication) from textes "
            "where jort_annee = ? and jort_numero is not null group by jort_annee, jort_numero",
            (annee,))}
    finally:
        cnx.close()
    dernier = r.dernier_numero_coherent(dates, annee)
    return sorted(n for (_, n) in dates if n > dernier)


def a_telecharger(base: Path, annees: list[int]) -> list[tuple[int, str, int, str, Path]]:
    """[(année, langue, n°, url, destination)] : connus de jort_cache, absents du corpus."""
    racine = dossier_jort()
    manquants = []
    for annee in annees:
        nums = numeros_connus(base, annee)
        presents = r.fascicules_locaux(depot(), range(annee, annee + 1), sources=("pdf",))
        for langue in ("fr", "ar"):
            for num in nums:
                if (annee, langue, num) in presents:
                    continue
                url = r.url_fascicule(annee, langue, num)
                dest = racine / str(annee) / langue / url.rsplit("/", 1)[1]
                if not dest.exists():
                    manquants.append((annee, langue, num, url, dest))
    return manquants


def ecrit_sans_ecraser(dest: Path, contenu: bytes) -> bool:
    """Écrit `dest` s'il n'existe pas : `.part` d'abord, puis lien (qui échoue si `dest`
    est apparu entre-temps). Rend False si `dest` existait."""
    if not dest.resolve().is_relative_to(dossier_jort().resolve()):
        raise ValueError(f"hors de PDFs/JORT/ : {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    part = dest.with_name(dest.name + ".part")
    part.unlink(missing_ok=True)  # reste d'un essai interrompu : c'est notre fichier temporaire
    with open(part, "xb") as f:
        f.write(contenu)
    try:
        os.link(part, dest)
    except FileExistsError:
        return False
    finally:
        part.unlink()
    return True


def cmd_telecharger(annees: list[int], a_blanc: bool, telecharge=None) -> int:
    base = r.chemin_base()
    if not base.exists():
        print(f"✗ base absente : {base}")
        return 1
    manquants = a_telecharger(base, annees)
    print(f"{len(manquants)} fascicule(s) connus de jort_cache et absents de {dossier_jort()}")
    if a_blanc:
        for annee in annees:
            for langue in ("fr", "ar"):
                nums = [n for a, l, n, _, _ in manquants if a == annee and l == langue]
                if nums:
                    print(f"  {annee} {langue} : {r.compacte(nums)}")
            douteux = numeros_douteux(base, annee)
            if douteux:
                print(f"  {annee} : numéros de jort_cache incohérents avec leurs dates, sans doute "
                      f"erronés (outillage-sources.md, § 1) : {r.compacte(douteux)}")
        print("(à blanc : rien n'est téléchargé)")
        return 0
    telecharge = telecharge or (lambda url: pist_tls.requete(url, "GET", timeout=90))
    bilan = {"téléchargés": 0, "absents": 0, "erreurs": 0, "déjà là": 0}
    for annee, langue, num, url, dest in manquants:
        try:
            statut, corps = telecharge(url)
        except (OSError, http.client.HTTPException) as e:
            print(f"✗ {annee} {langue} n° {num} : {e}", flush=True)
            bilan["erreurs"] += 1
            time.sleep(DELAI * 4)
            continue
        if statut == 200 and corps[:4] == b"%PDF":
            if ecrit_sans_ecraser(dest, corps):
                print(f"✓ {annee} {langue} n° {num} ({len(corps) // 1024} Ko)", flush=True)
                bilan["téléchargés"] += 1
            else:
                bilan["déjà là"] += 1
        else:
            quoi = f"HTTP {statut}" if statut != 200 else "réponse qui n'est pas un PDF"
            print(f"– {annee} {langue} n° {num} : {quoi} ({url})", flush=True)
            bilan["absents"] += 1
        time.sleep(DELAI)
    print("BILAN : " + ", ".join(f"{k} {v}" for k, v in bilan.items()))
    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="commande", required=True)
    p = sub.add_parser("crawl", help="mettre à jour jort_cache.db (sur une copie, puis recopie)")
    p.add_argument("--from", dest="debut", type=int, required=True)
    p.add_argument("--to", dest="fin", type=int, required=True)
    p.add_argument("--delai-max", type=float, default=3600,
                   help="secondes au-delà desquelles le crawl est interrompu (défaut : 3600)")
    p.add_argument("--a-blanc", action="store_true", help="afficher le plan, ne rien lancer")
    p = sub.add_parser("telecharger", help="fascicules connus de jort_cache, absents du corpus")
    p.add_argument("annees", type=int, nargs="+")
    p.add_argument("--a-blanc", action="store_true", help="lister, ne rien télécharger")
    args = ap.parse_args(argv)
    if args.commande == "crawl":
        if args.fin < args.debut:
            ap.error("--to précède --from")
        return cmd_crawl(args.debut, args.fin, args.delai_max, args.a_blanc)
    return cmd_telecharger(args.annees, args.a_blanc)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

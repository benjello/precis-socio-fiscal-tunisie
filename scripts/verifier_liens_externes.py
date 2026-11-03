"""Vérifie que les adresses des `references.json` répondent, et dit pourquoi quand elles ne répondent pas.

Le rendu du livre ne s'arrête pas sur un lien mort, et `verifier_liens_base_legislative.py` ne
regarde que les liens vers les paramètres. Ce contrôle interroge le champ `URL` de chaque
notice de bibliographie et classe la réponse :

  ok           la page répond (200, 206, ou une redirection qui aboutit)
  absent       404 ou 410 : le document n'est plus à cette adresse
  certificat   la chaîne de certificat ne se vérifie pas ; un lecteur voit un avertissement
  injoignable  le serveur ne répond pas (refus de connexion, délai dépassé)
  limite       tout autre code (403, 429, 5xx…) : le serveur refuse ce passage-ci, sans dire que la page manque

Les copies de web.archive.org sont interrogées une à une, avec une pause : l'Internet Archive
coupe les connexions qui vont trop vite, et une coupure ne dit rien de la copie. Le certificat
n'est jamais contourné : un site qui ne le tient pas est signalé, pas excusé.

    uv run python scripts/verifier_liens_externes.py                  # tout le corpus
    uv run python scripts/verifier_liens_externes.py --hote steg.com.tn
    uv run python scripts/verifier_liens_externes.py --archive        # propose une copie
    uv run python scripts/verifier_liens_externes.py --avertir        # sort 0 même en cas d'échec

Sortie : 1 dès qu'une adresse est absente, à certificat invalide ou injoignable (« limite »
n'est pas un échec). Le rapport complet est écrit dans `liens-externes-rapport.json`.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import pathlib
import socket
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request

RACINE = pathlib.Path(__file__).parent.parent
RAPPORT = RACINE / "liens-externes-rapport.json"
AGENT = "Mozilla/5.0 (precis-socio-fiscal, verification des liens)"
ARCHIVE = "web.archive.org"
ECHECS = ("absent", "certificat", "injoignable")


def classer(url: str, essais: int = 2, delai: float = 30.0) -> tuple[str, str]:
    """Rend (classe, détail) pour une adresse. Réessaie une fois avant de conclure."""
    detail, classe = "", "injoignable"
    for essai in range(essais):
        requete = urllib.request.Request(
            url, headers={"User-Agent": AGENT, "Range": "bytes=0-1023"}
        )
        try:
            with urllib.request.urlopen(requete, timeout=delai) as reponse:
                return "ok", str(reponse.status)
        except urllib.error.HTTPError as erreur:
            if erreur.code in (404, 410):
                return "absent", str(erreur.code)
            if (
                erreur.code == 416
            ):  # la plage demandée dépasse un fichier vide : la page répond
                return "ok", "416"
            detail, classe = str(erreur.code), "limite"
        except urllib.error.URLError as erreur:
            raison = erreur.reason
            if isinstance(raison, ssl.SSLCertVerificationError):
                return "certificat", getattr(raison, "verify_message", None) or str(
                    raison
                )
            if isinstance(raison, ssl.SSLError):
                return "certificat", str(raison)
            detail, classe = str(raison), "injoignable"
        except (TimeoutError, socket.timeout, ConnectionError, OSError) as erreur:
            detail, classe = str(erreur), "injoignable"
        if essai + 1 < essais:
            time.sleep(5)
    return classe, detail


def adresses(hote: str | None = None) -> dict[str, list[str]]:
    """Les URL des notices, avec les clés (`livre:clé`) qui les citent."""
    trouvees: dict[str, list[str]] = {}
    for fichier in sorted((RACINE / "precis").rglob("references.json")):
        livre = fichier.parent.relative_to(RACINE / "precis").as_posix()
        for entree in json.loads(fichier.read_text(encoding="utf-8"))["items"]:
            url = entree.get("URL", "")
            if not url.startswith("http"):
                continue
            if hote and hote not in urllib.parse.urlparse(url).netloc:
                continue
            trouvees.setdefault(url, []).append(f"{livre}:{entree['id']}")
    return trouvees


def copie_archive(url: str) -> str | None:
    """La copie la plus proche de l'Internet Archive pour `url`, ou None."""
    requete = "http://archive.org/wayback/available?url=" + urllib.parse.quote(
        url, safe=""
    )
    try:
        with urllib.request.urlopen(requete, timeout=40) as reponse:
            proche = json.load(reponse).get("archived_snapshots", {}).get("closest")
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        return None
    return proche["url"] if proche and proche.get("available") else None


def verifier(urls: list[str]) -> dict[str, tuple[str, str]]:
    """Les copies d'archive une à une, les autres adresses en parallèle."""
    resultats: dict[str, tuple[str, str]] = {}
    archives = [u for u in urls if ARCHIVE in urllib.parse.urlparse(u).netloc]
    autres = [u for u in urls if u not in set(archives)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for url, verdict in zip(autres, pool.map(classer, autres)):
            resultats[url] = verdict
    for url in archives:
        resultats[url] = classer(url, essais=3)
        time.sleep(2)
    return resultats


def main() -> int:
    analyseur = argparse.ArgumentParser(description=(__doc__ or "").split("\n")[0])
    analyseur.add_argument(
        "--hote", help="ne tester que les adresses de cet hôte (sous-chaîne)"
    )
    analyseur.add_argument(
        "--archive", action="store_true", help="chercher une copie pour chaque échec"
    )
    analyseur.add_argument(
        "--avertir", action="store_true", help="sortir en 0 même en cas d'échec"
    )
    options = analyseur.parse_args()

    urls = adresses(options.hote)
    print(f"{len(urls)} adresses à vérifier.")
    verdicts = verifier(sorted(urls))

    rapport = []
    for url, (classe, detail) in sorted(
        verdicts.items(), key=lambda kv: (kv[1][0], kv[0])
    ):
        ligne = {"url": url, "classe": classe, "detail": detail, "notices": urls[url]}
        if options.archive and classe in ECHECS:
            ligne["copie"] = copie_archive(url)
            time.sleep(2)
        rapport.append(ligne)
        if classe != "ok":
            copie = f"  → {ligne['copie']}" if ligne.get("copie") else ""
            print(f"  {classe:11} {detail[:40]:40} {url[:110]}{copie}")
    RAPPORT.write_text(
        json.dumps(rapport, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    comptes = {
        c: sum(1 for r in rapport if r["classe"] == c)
        for c in ("ok", "limite", *ECHECS)
    }
    print("\n" + ", ".join(f"{n} {c}" for c, n in comptes.items()))
    echecs = sum(comptes[c] for c in ECHECS)
    return 0 if options.avertir or not echecs else 1


if __name__ == "__main__":
    raise SystemExit(main())

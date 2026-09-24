"""Accès à www.pist.tn sans vérification du certificat — pour CE SEUL hôte.

Le certificat de www.pist.tn est échu depuis le 25 août 2026. L'humain a autorisé
explicitement, le 24 septembre 2026, la désactivation de la vérification TLS pour
pist.tn seulement : on y lit des documents publics (fascicules du JORT, notices), sans
rien y envoyer. Ce module est le SEUL endroit où cette vérification tombe, et il la
restreint à l'hôte exact `www.pist.tn` en HTTPS :

  - `requete()` ouvre une connexion dont l'hôte est écrit en dur (`http.client`), sans
    suivre aucune redirection : la vérification désactivée ne peut pas fuir ailleurs ;
  - `patche_requests()` (pour le crawler de `PDFs-legislation-tunisie`, qui emploie
    `requests`) ne désactive la vérification que requête par requête, d'après l'URL
    effectivement envoyée — une redirection vers un autre hôte reste vérifiée.

Quand le certificat sera renouvelé, remettre `VERIFIER = True` suffit.

Lancé comme script, il sert d'enrobage au crawler (voir `scripts/corpus_jort.py`) :

    uv run --no-sync --project ~/projets/PDFs-legislation-tunisie \\
        python scripts/pist_tls.py crawl --db COPIE --from 2026 --to 2026
"""

from __future__ import annotations

import http.client
import ssl
import sys
from urllib.parse import urlsplit

HOTE = "www.pist.tn"
VERIFIER = False  # certificat échu le 25/08/2026 ; autorisation du 24/09/2026, pist.tn seul


def hote_pist(url: str) -> bool:
    """Vrai pour une URL HTTPS dont l'hôte est exactement `www.pist.tn` (port 443)."""
    try:
        u = urlsplit(url)
        port = u.port
    except ValueError:
        return False
    return u.scheme == "https" and (u.hostname or "").lower() == HOTE and port in (None, 443)


def contexte_tls() -> ssl.SSLContext:
    if VERIFIER:
        return ssl.create_default_context()
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def requete(url: str, methode: str = "HEAD", timeout: float = 60) -> tuple[int, bytes]:
    """(statut HTTP, corps) d'une requête sur www.pist.tn ; ne suit aucune redirection.

    Refuse toute URL d'un autre hôte : c'est ce refus qui cantonne la vérification
    désactivée à pist.tn."""
    if not hote_pist(url):
        raise ValueError(f"hôte refusé (seul https://{HOTE} est admis) : {url}")
    u = urlsplit(url)
    cnx = http.client.HTTPSConnection(HOTE, timeout=timeout, context=contexte_tls())
    try:
        cnx.request(methode, u.path + (f"?{u.query}" if u.query else ""),
                    headers={"User-Agent": "precis-socio-fiscal-tunisie (lecture du JORT)"})
        rep = cnx.getresponse()
        return rep.status, rep.read() if methode != "HEAD" else b""
    finally:
        cnx.close()


def patche_requests() -> None:
    """Désactive la vérification dans `requests` pour les seules requêtes vers pist.tn."""
    import requests.adapters
    import urllib3

    if VERIFIER:
        return
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    origine = requests.adapters.HTTPAdapter.send

    def send(self, request, *args, **kwargs):
        if hote_pist(request.url):
            kwargs["verify"] = False
        return origine(self, request, *args, **kwargs)

    requests.adapters.HTTPAdapter.send = send


def main(argv: list[str]) -> int:
    if not argv or argv[0] != "crawl":
        print("usage : pist_tls.py crawl [arguments de jort_api.crawl]")
        return 2
    patche_requests()
    from jort_api import crawl

    return crawl.main(argv[1:])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

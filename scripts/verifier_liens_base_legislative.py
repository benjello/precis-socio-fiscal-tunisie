"""Vérifie que chaque lien de l'onglet « Base législative » des tableaux répond.

Les listes `precis/<langue>/<livre>/tables/<nom>.liens.yml` sont engendrées avec les
tableaux. Un paramètre renommé ou déplacé dans l'arbre de paramètres rendrait son lien mort
sans que rien ne le signale : ce contrôle interroge chaque adresse et sort en 1 dès qu'une
page ne répond pas.

    uv run python scripts/verifier_liens_base_legislative.py
"""

from __future__ import annotations

import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

RACINE = Path(__file__).parent.parent / "precis"


def statut(url: str) -> int:
    requete = urllib.request.Request(url, headers={"User-Agent": "precis-socio-fiscal"})
    try:
        with urllib.request.urlopen(requete, timeout=30) as reponse:
            return reponse.status
    except urllib.error.HTTPError as erreur:
        return erreur.code
    except urllib.error.URLError:
        return 0


def main() -> int:
    fichiers = sorted(RACINE.glob("*/*/tables/*.liens.yml"))
    urls = {}
    for fichier in fichiers:
        for entree in yaml.safe_load(fichier.read_text(encoding="utf-8")) or []:
            urls.setdefault(entree["url"], []).append(fichier.relative_to(RACINE))
    morts = [(url, statut(url), sources) for url, sources in sorted(urls.items())]
    morts = [m for m in morts if m[1] != 200]
    for url, code, sources in morts:
        print(f"✗ {code} {url}  ({', '.join(map(str, sources))})")
    print(f"{len(urls)} lien(s) dans {len(fichiers)} fichier(s) : "
          f"{len(morts)} ne répond(ent) pas.")
    return 1 if morts else 0


if __name__ == "__main__":
    sys.exit(main())

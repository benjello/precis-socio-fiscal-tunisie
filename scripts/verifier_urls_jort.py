"""Recense les fascicules du JORT dont l'édition homologue n'existe pas sur pist.tn.

Le JORT paraît en deux éditions, servies sous deux chemins qui ne diffèrent que par une
lettre. `sync_biblio.py` dérive donc l'une de l'autre pour donner à chaque langue le lien
qu'elle peut lire. Toutes les conversions n'aboutissent pas : certains fascicules français
récents ne sont pas en ligne, et une dérivation aveugle fabriquerait des liens morts.

Ce script teste les deux éditions de chaque URL du corpus et écrit la liste des exceptions
dans `precis/urls-jort.json`, que la descente consulte. Il interroge le réseau : on le lance
à la main, pas à chaque build, et son résultat est versionné pour que la descente reste
déterministe et reproductible hors ligne.

    python scripts/verifier_urls_jort.py

DEUX PIÈGES, tous deux rencontrés :

  - le certificat de pist.tn est expiré, d'où la vérification sans validation TLS ;
  - un code 200 ne prouve pas que le fascicule servi est celui de l'édition demandée. Le
    JORT n° 88 de 2025 répond 200 sous le chemin français et sert l'arabe. On compare donc
    la TAILLE des deux réponses : deux éditions du même fascicule n'ont jamais exactement
    le même poids, et une taille identique trahit le même fichier servi deux fois.
"""

from __future__ import annotations

import json
import pathlib
import ssl
import sys
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from sync_biblio import FICHIER_EXCEPTIONS, JORT_AR, JORT_FR, url_jort  # noqa: E402

RACINE = pathlib.Path(__file__).parent.parent
CONTEXTE = ssl.create_default_context()
CONTEXTE.check_hostname = False
CONTEXTE.verify_mode = ssl.CERT_NONE


def taille(url: str) -> int | None:
    """Taille annoncée par pist.tn, ou None si le fascicule est absent."""
    requete = urllib.request.Request(url, method="HEAD")
    requete.add_header("User-Agent", "Mozilla/5.0 (precis-socio-fiscal)")
    try:
        with urllib.request.urlopen(requete, timeout=30, context=CONTEXTE) as reponse:
            if reponse.status != 200:
                return None
            longueur = reponse.headers.get("Content-Length")
            return int(longueur) if longueur else 0
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError):
        return None


def urls_du_corpus() -> set[str]:
    trouvees = set()
    for fichier in (RACINE / "precis").rglob("references.json"):
        for entree in json.loads(fichier.read_text(encoding="utf-8"))["items"]:
            url = entree.get("URL", "")
            if JORT_FR.search(url) or JORT_AR.search(url):
                trouvees.add(url)
    return trouvees


def main() -> int:
    urls = sorted(urls_du_corpus())
    print(f"{len(urls)} URL du JORT à vérifier.\n")
    exceptions, controles = [], 0
    for url in urls:
        langue_cible = "fr" if JORT_AR.search(url) else "ar"
        homologue = url_jort(url, langue_cible)
        if homologue == url:
            continue
        controles += 1
        ici, la_bas = taille(url), taille(homologue)
        if la_bas is None:
            exceptions.append(url)
            print(f"  ✗ {url.split('/')[-1]:16} → {homologue.split('/')[-1]:16} absent")
        elif ici is not None and ici == la_bas:
            exceptions.append(url)
            print(f"  ✗ {url.split('/')[-1]:16} → même fichier servi ({ici} octets) : "
                  "les deux chemins ne servent pas deux éditions")
        else:
            print(f"  ✓ {url.split('/')[-1]:16} → {homologue.split('/')[-1]:16} "
                  f"{ici} / {la_bas} octets")

    sortie = pathlib.Path(FICHIER_EXCEPTIONS)
    sortie.write_text(
        json.dumps(
            {
                "commentaire": "Fascicules dont l'édition homologue est absente de pist.tn, "
                               "ou dont les deux chemins servent le même fichier. La "
                               "synchronisation descendante les laisse tels quels. "
                               "Régénérer avec scripts/verifier_urls_jort.py.",
                "sans_homologue": sorted(exceptions),
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"\n{controles} conversion(s) testée(s), {len(exceptions)} exception(s) "
          f"écrite(s) dans {sortie.relative_to(RACINE)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

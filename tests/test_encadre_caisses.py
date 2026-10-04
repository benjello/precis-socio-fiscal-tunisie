"""L'encadré « Les caisses de sécurité sociale » : une source, trois partiels identiques à elle.

Le partiel de chaque livre est engendré par `scripts/generate_encadre_caisses.py`. Une
retouche faite à la main dans l'un d'eux le ferait diverger des deux autres sans que rien
ne le signale ; ce test, lancé par `scripts/verifier.sh` et la CI, le signale. Il contrôle
aussi que chaque clé citée résout dans la bibliographie de chaque livre, dans les deux
langues : l'arabe ne se rend pas avant la traduction, le contrôle ne peut donc pas attendre
le rendu.
"""

import json
import re
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))

import generate_encadre_caisses as enc  # noqa: E402


def ids(fichier: Path) -> set[str]:
    if not fichier.is_file():
        return set()
    donnees = json.loads(fichier.read_text(encoding="utf-8"))
    entrees = donnees.get("items", []) if isinstance(donnees, dict) else donnees
    return {e["id"] for e in entrees}


class EncadreCaissesTest(unittest.TestCase):
    def test_partiels_a_jour(self):
        self.assertEqual(enc.derives(), [],
                         "partiel à régénérer : uv run python scripts/generate_encadre_caisses.py")

    def test_cles_resolues_dans_chaque_livre_et_chaque_langue(self):
        for livre in enc.PROPRE:
            cles = set(re.findall(r"@([\w-]+)", enc.texte(livre)))
            for langue in ("fr", "ar"):
                connues = (ids(RACINE / "precis" / langue / livre / "references.json")
                           | ids(RACINE / "precis" / langue / "references.json"))
                with self.subTest(livre=livre, langue=langue):
                    self.assertEqual(sorted(cles - connues), [])


if __name__ == "__main__":
    unittest.main()

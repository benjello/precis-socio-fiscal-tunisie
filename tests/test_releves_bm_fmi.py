"""Les trois relevés Banque mondiale et FMI : clé de ligne unique, notices présentes (livre ou fonds commun)."""

import csv
import json
from pathlib import Path

import unittest

try:
    import yaml
except ImportError:
    raise unittest.SkipTest("pyyaml absent")

RACINE = Path(__file__).resolve().parent.parent
LISTES = RACINE / "precis/fr/entreprises_publiques/listes"
RELEVES = [
    "banque-mondiale-per-2020-entreprises",
    "fmi-2021-arrieres-croises",
    "banque-mondiale-matrice-reformes-2022",
]


def _manifeste(nom):
    return yaml.safe_load((LISTES / f"{nom}.csv.yml").read_text(encoding="utf-8"))


def _lignes(nom):
    with open(LISTES / f"{nom}.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def test_cle_de_ligne_unique():
    for nom in RELEVES:
        cle = _manifeste(nom)["cle_de_ligne"]
        vues = [tuple(r[c] for c in cle) for r in _lignes(nom)]
        assert len(vues) == len(set(vues)), nom


def test_colonnes_du_manifeste_et_du_fichier_concordent():
    for nom in RELEVES:
        colonnes = list(_manifeste(nom)["colonnes"])
        assert list(_lignes(nom)[0]) == colonnes, nom


def test_sources_dans_les_references_du_livre():
    ids = set()
    for fichier in ("precis/fr/entreprises_publiques/references.json", "precis/fr/references.json"):
        refs = json.loads((RACINE / fichier).read_text(encoding="utf-8"))
        ids |= {e["id"] for e in refs["items"]}
    for nom in RELEVES:
        for source in _manifeste(nom)["sources"]:
            assert source in ids, (nom, source)
        for r in _lignes(nom):
            assert r["document"] in ids, (nom, r["document"])

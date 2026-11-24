"""Comptes des secteurs (cache) : contrôles sans échec, deux côtés, matrice dont les pages existent."""
import csv
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "precis" / "_seriescache"


def _lire(chemin):
    with chemin.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_controles_sans_echec():
    c = _lire(CACHE / "cnat-secteurs-controles.csv")
    assert c and not [r for r in c if r["statut"] == "echec"]
    for r in c:
        if r["statut"] == "ok":
            assert abs(float(r["ecart"])) <= 0.05 * int(r["n_valeurs"]) + 1e-9


def test_deux_cotes_et_sous_secteurs():
    s = _lire(CACHE / "cnat-secteurs.csv")
    assert {r["cote"] for r in s} == {"emplois", "ressources"}
    assert {"apu_centrale", "apu_locale", "apu_secu", "sf_credit"} <= {r["secteur"] for r in s}


def _page_existe(page: str) -> bool:
    chemin, _, ancre = page.partition("#")
    fr = RACINE / "precis" / "fr"
    qmd = fr / chemin / "index.qmd" if chemin.endswith("/") else (fr / chemin).with_suffix(".qmd")
    return qmd.exists() and (not ancre or f"{{#{ancre}}}" in qmd.read_text(encoding="utf-8"))


def test_matrice_pages_existent():
    d = _lire(RACINE / "precis" / "fr" / "correspondance-comptes.csv")
    pages = {p for r in d if r["pages"] for p in r["pages"].split(" ; ")}
    assert pages and all(_page_existe(p) for p in pages)
    assert {r["couverture"] for r in d} <= {"domicile", "renvoi", "vide", "solde"}

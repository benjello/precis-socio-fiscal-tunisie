"""remplacer.py (espaces insécables, exclusions) et cache_series.ecrire_serie (fiche à sa place)."""
import importlib.util
from pathlib import Path

import pytest
import yaml

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"


def _module(nom):
    spec = importlib.util.spec_from_file_location(nom, SCRIPTS / f"{nom}.py")
    assert spec and spec.loader
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


rem = _module("remplacer")
cs = _module("cache_series")


def test_motif_tolere_les_espaces_insecables(tmp_path):
    rem.RACINE = tmp_path
    p = tmp_path / "a.qmd"
    p.write_text("Comment lire ce\u00a0précis ; le précis dit.", encoding="utf-8")
    total, rapport = rem.remplacer(rem.motif_tolerant(r"ce précis"), "cet ouvrage", [p], appliquer=False)
    assert total == 1 and p.read_text(encoding="utf-8").startswith("Comment lire ce\u00a0précis")
    total, _ = rem.remplacer(rem.motif_tolerant(r"ce précis"), "cet ouvrage", [p], appliquer=True)
    assert "cet ouvrage" in p.read_text(encoding="utf-8")


def test_exclusions(tmp_path):
    rem.RACINE = tmp_path
    for f in ["precis/fr/a.qmd", "precis/ar/b.qmd", "precis/fr/x/_glossaire.qmd", "docs/notes/n.md"]:
        (tmp_path / f).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / f).write_text("x", encoding="utf-8")
    vus = [p.relative_to(tmp_path).as_posix() for p in rem.fichiers(["precis/**/*.qmd", "docs/**/*.md"], rem.TOUJOURS_EXCLUS)]
    assert vus == ["precis/fr/a.qmd"]


def test_ecrire_serie(tmp_path):
    (tmp_path / "catalog.snapshot.yml").write_text(
        yaml.safe_dump([{"id": "a", "titre": "A", "sources": ["k"]}, {"id": "b", "titre": "B", "sources": ["k"]}]),
        encoding="utf-8")
    cs.ecrire_serie("a", [{"annee": 2020, "valeur": 1.0}], {"titre": "A bis", "sources": ["k"]}, cache=tmp_path)
    cs.ecrire_serie("c", [{"annee": 2020, "valeur": 2.0}], {"titre": "C", "sources": ["k"]}, cache=tmp_path)
    snap = yaml.safe_load((tmp_path / "catalog.snapshot.yml").read_text("utf-8"))
    assert [e["id"] for e in snap] == ["a", "b", "c"] and snap[0]["titre"] == "A bis"
    assert (tmp_path / "c.csv").read_text("utf-8").startswith("annee,valeur")
    with pytest.raises(ValueError):
        cs.ecrire_serie("d", [{"x": 1}], {"titre": "D"}, cache=tmp_path)


def test_espace_echappee():
    assert rem.motif_tolerant(r"ce\ précis").search("ce\u00a0précis")

"""Copies de fichiers de l'entrepôt hors catalogue : empreinte et écart avec l'entrepôt."""
import shutil
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import fichiers_entrepot as fe  # noqa: E402


def test_copies_conformes_a_la_fiche(monkeypatch, tmp_path):
    monkeypatch.setattr(fe, "ENTREPOT", tmp_path / "absent")
    assert fe.verifier() == 0


def test_ecart_avec_l_entrepot_detecte(monkeypatch, tmp_path):
    for nom, chemin in fe.FICHIERS.items():
        (tmp_path / chemin).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(fe.CACHE / nom, tmp_path / chemin)
    monkeypatch.setattr(fe, "ENTREPOT", tmp_path)
    assert fe.verifier() == 0
    premier = tmp_path / next(iter(fe.FICHIERS.values()))
    premier.write_bytes(premier.read_bytes() + b"x\n")
    assert fe.verifier() == 1

"""Contrôle de la numérotation des volumes (scripts/check_numerotation.py)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from check_numerotation import ecarts_du_livre  # noqa: E402


def livre(tmp_path, quarto, fichiers):
    d = tmp_path / "livre"
    d.mkdir()
    (d / "_quarto.yml").write_text(quarto, encoding="utf-8")
    for nom, texte in fichiers.items():
        (d / nom).write_text(texte, encoding="utf-8")
    return d


def test_livre_conforme(tmp_path):
    d = livre(tmp_path, """
book:
  chapters:
    - index.qmd
    - part: "Une partie"
      chapters: [a.qmd]
  appendices: [_glossaire.qmd]
""", {"index.qmd": "# Présentation\n", "a.qmd": "# A {#sec-a}\n",
      "_glossaire.qmd": "# Glossaire {.unnumbered}\n"})
    assert ecarts_du_livre(d) == []


def test_chapitre_non_numerote(tmp_path):
    d = livre(tmp_path, "book:\n  chapters: [index.qmd]\n",
              {"index.qmd": "# Présentation {.unnumbered #sec-p}\n"})
    assert len(ecarts_du_livre(d)) == 1


def test_partie_par_fichier(tmp_path):
    d = livre(tmp_path, """
book:
  chapters:
    - index.qmd
    - part: _partie.qmd
      chapters: [a.qmd]
""", {"index.qmd": "# P\n", "_partie.qmd": "# Partie\n", "a.qmd": "# A\n"})
    assert any("partie déclarée par un fichier" in e for e in ecarts_du_livre(d))

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
    - a.qmd
  appendices: [_glossaire.qmd]
""", {"index.qmd": "# Présentation\n", "a.qmd": "# A {#sec-a}\n",
      "_glossaire.qmd": "# Glossaire {.unnumbered}\n"})
    assert ecarts_du_livre(d) == []


def test_chapitre_non_numerote(tmp_path):
    d = livre(tmp_path, "book:\n  chapters: [index.qmd]\n",
              {"index.qmd": "# Présentation {.unnumbered #sec-p}\n"})
    assert len(ecarts_du_livre(d)) == 1


def test_toute_partie_est_refusee(tmp_path):
    d = livre(tmp_path, """
book:
  chapters:
    - index.qmd
    - part: _partie.qmd
      chapters: [a.qmd]
""", {"index.qmd": "# P\n", "_partie.qmd": "# Partie\n", "a.qmd": "# A\n"})
    assert any("partie" in e for e in ecarts_du_livre(d))


def test_saut_de_niveau(tmp_path):
    d = livre(tmp_path, "book:\n  chapters: [index.qmd]\nformat:\n  html:\n    number-depth: 4\n",
              {"index.qmd": "# P\n\n## A\n\n## B\n\n#### trop bas\n"})
    assert any("saut de niveau" in e for e in ecarts_du_livre(d))


def test_au_dela_de_la_profondeur(tmp_path):
    d = livre(tmp_path, "book:\n  chapters: [index.qmd]\nformat:\n  html:\n    number-depth: 2\n",
              {"index.qmd": "# P\n\n## A\n\n### a1\n\n### a2\n\n## B\n"})
    assert any("au-delà de number-depth" in e for e in ecarts_du_livre(d))


def test_section_a_un_seul_enfant_y_compris_par_inclusion(tmp_path):
    d = livre(tmp_path, "book:\n  chapters: [index.qmd]\nformat:\n  html:\n    number-depth: 4\n",
              {"index.qmd": "# P\n\n## A\n\n{{< include _inc.qmd >}}\n\n## B\n",
               "_inc.qmd": "### seul\n\ntexte\n"})
    assert any("une seule sous-section" in e for e in ecarts_du_livre(d))


def test_les_blocs_de_code_ne_sont_pas_des_titres(tmp_path):
    d = livre(tmp_path, "book:\n  chapters: [index.qmd]\nformat:\n  html:\n    number-depth: 4\n",
              {"index.qmd": "# P\n\n## A\n\n```python\n# commentaire\n```\n\n## B\n"})
    assert ecarts_du_livre(d) == []

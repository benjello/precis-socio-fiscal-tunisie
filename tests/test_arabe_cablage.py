"""Câblage des livres arabes et pages-relais (scripts/arabe_cablage.py)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import arabe_cablage as ac  # noqa: E402
import check_translation_parity as parite  # noqa: E402

FR_YML = """project:
  type: book

lang: fr

book:
  title: "Livre"
  chapters:
    - index.qmd
    - _a.qmd
    - _b.qmd
  appendices:
    - _glossaire.qmd

format:
  html:
    toc: true
"""

AR_YML = """project:
  type: book

lang: ar
dir: rtl

book:
  title: "كتاب"
  chapters:
    - index.qmd
    # - _b.qmd   # commenté
    - _arabe_seul.qmd
  appendices:
    - _glossaire.qmd

language:
  toc-title-document: "المحتويات"

format:
  html:
    toc: true
"""

GLOSSAIRE = """entries:
  - id: tva
    fr: {terme: Titre B, definition: x}
    ar: {terme: عنوان ب, definition: y}
"""


def _arbre(tmp_path):
    p = tmp_path / "precis"
    (p / "fr" / "livre").mkdir(parents=True)
    (p / "ar" / "livre").mkdir(parents=True)
    (p / "glossaire.yml").write_text(GLOSSAIRE, encoding="utf-8")
    (p / "fr" / "livre" / "_quarto.yml").write_text(FR_YML, encoding="utf-8")
    (p / "ar" / "livre" / "_quarto.yml").write_text(AR_YML, encoding="utf-8")
    (p / "fr" / "livre" / "index.qmd").write_text("# Présentation {#sec-pres}\n", encoding="utf-8")
    (p / "fr" / "livre" / "_a.qmd").write_text("# Titre A {#sec-a .domicile-unique}\n", encoding="utf-8")
    (p / "fr" / "livre" / "_b.qmd").write_text("# Titre B {#sec-b}\n", encoding="utf-8")
    (p / "fr" / "livre" / "_glossaire.qmd").write_text("# Glossaire\n", encoding="utf-8")
    (p / "ar" / "livre" / "_glossaire.qmd").write_text("# مسرد\n", encoding="utf-8")
    (p / "ar" / "livre" / "index.qmd").write_text("# تقديم {#sec-pres}\n", encoding="utf-8")
    (p / "ar" / "livre" / "_arabe_seul.qmd").write_text("# فقط\n", encoding="utf-8")
    return p


def test_ajout_des_chapitres_manquants_et_relais(tmp_path):
    p = _arbre(tmp_path)
    voulus, _ = ac.calculer(p)
    yml = voulus[p / "ar" / "livre" / "_quarto.yml"]
    assert ac.lire_listes(yml)["chapters"] == ["index.qmd", "_a.qmd", "_b.qmd", "_arabe_seul.qmd"]
    relais_a = voulus[p / "ar" / "livre" / "_a.qmd"]
    assert ac.MARQUEUR_RELAIS in relais_a
    assert "# Titre A {#sec-a}" in relais_a  # titre français, ancre conservée, sans classes
    assert ac.AVIS in relais_a and "../../fr/livre/_a.html" in relais_a
    assert "# عنوان ب {#sec-b}" in voulus[p / "ar" / "livre" / "_b.qmd"]  # titre du glossaire
    assert p / "ar" / "livre" / "_glossaire.qmd" not in voulus  # jamais de relais de glossaire
    assert p / "ar" / "livre" / "index.qmd" not in voulus  # une vraie traduction reste


def test_les_cles_arabes_sans_original_sont_preservees(tmp_path):
    p = _arbre(tmp_path)
    voulus, _ = ac.calculer(p)
    yml = voulus[p / "ar" / "livre" / "_quarto.yml"]
    for garde in ("dir: rtl", "lang: ar", "toc-title-document: \"المحتويات\"", 'title: "كتاب"',
                  "  appendices:\n    - _glossaire.qmd\n\nlanguage:"):
        assert garde in yml
    # seul le bloc chapters a changé
    assert yml.split("  chapters:")[0] == AR_YML.split("  chapters:")[0]
    assert yml.split("  appendices:")[1] == AR_YML.split("  appendices:")[1]


def test_idempotence_et_verification(tmp_path):
    p = _arbre(tmp_path)
    voulus, _ = ac.calculer(p)
    assert ac.ecarts(voulus)
    for chemin, texte in voulus.items():
        chemin.write_text(texte, encoding="utf-8")
    voulus2, _ = ac.calculer(p)
    assert ac.ecarts(voulus2) == []
    # une dérive : un chapitre français de plus
    (p / "fr" / "livre" / "_quarto.yml").write_text(
        FR_YML.replace("    - _b.qmd\n", "    - _b.qmd\n    - _c.qmd\n"), encoding="utf-8")
    (p / "fr" / "livre" / "_c.qmd").write_text("# C\n", encoding="utf-8")
    voulus3, _ = ac.calculer(p)
    assert p / "ar" / "livre" / "_c.qmd" in ac.ecarts(voulus3)


def test_la_traduction_remplace_le_relais_et_n_est_plus_ecrasee(tmp_path):
    p = _arbre(tmp_path)
    for chemin, texte in ac.calculer(p)[0].items():
        chemin.write_text(texte, encoding="utf-8")
    assert ac.est_relais(p / "ar" / "livre" / "_a.qmd")
    (p / "ar" / "livre" / "_a.qmd").write_text("# ترجمة حقيقية {#sec-a}\n", encoding="utf-8")
    voulus, _ = ac.calculer(p)
    assert p / "ar" / "livre" / "_a.qmd" not in voulus
    assert not ac.est_relais(p / "ar" / "livre" / "_a.qmd")


def test_page_generale_sans_arabe(tmp_path):
    p = _arbre(tmp_path)
    (p / "fr" / "annexe.qmd").write_text('---\ntitle: "Annexe PIB"\n---\n\nTexte\n', encoding="utf-8")
    voulus, _ = ac.calculer(p)
    r = voulus[p / "ar" / "annexe.qmd"]
    assert r.startswith("---\ntitle: \"Annexe PIB\"\nlang: ar\ndir: rtl\n---")
    assert "../fr/annexe.html" in r


def test_le_relais_est_exempte_de_la_parite(tmp_path, monkeypatch):
    p = _arbre(tmp_path)
    for chemin, texte in ac.calculer(p)[0].items():
        chemin.write_text(texte, encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    paires = parite.pairs_for(["precis/fr/livre/_a.qmd", "precis/fr/livre/index.qmd"])
    assert ("precis/fr/livre/index.qmd", "precis/ar/livre/index.qmd") in paires
    assert all("_a.qmd" not in fr for fr, _ in paires)


def test_translate_sync_ne_prend_pas_le_relais_pour_une_traduction():
    import translate_sync
    assert translate_sync.est_relais_texte(ac.MARQUEUR_RELAIS + "\n\n# x\n")
    assert not translate_sync.est_relais_texte("# ترجمة\n")


def test_retard_traite_le_relais_comme_jamais_traduit(monkeypatch, tmp_path):
    import subprocess
    import traduction_en_retard as tr
    (tmp_path / "precis" / "fr").mkdir(parents=True)
    (tmp_path / "precis" / "ar").mkdir(parents=True)
    (tmp_path / "precis" / "fr" / "x.qmd").write_text("# x\n", encoding="utf-8")
    (tmp_path / "precis" / "fr" / "y.qmd").write_text("# y\n", encoding="utf-8")
    (tmp_path / "precis" / "ar" / "x.qmd").write_text(ac.MARQUEUR_RELAIS + "\n", encoding="utf-8")
    (tmp_path / "precis" / "ar" / "y.qmd").write_text("# ي\n", encoding="utf-8")
    git = ["git", "-c", "user.name=t", "-c", "user.email=t@t"]
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    # un seul commit : les dates sont égales, donc y est « à jour » ; x est un relais
    subprocess.run([*git, "commit", "-qm", "t"], cwd=tmp_path, check=True)
    monkeypatch.setattr(tr, "RACINE", tmp_path)
    retard = tr.en_retard()
    assert [(f.name, d_ar) for f, _d, d_ar in retard] == [("x.qmd", None)]

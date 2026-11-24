"""Le contrôle des liens entre volumes trouve les pages et les ancres absentes."""
import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "verifier_liens_entre_volumes.py"
spec = importlib.util.spec_from_file_location("vlv", SCRIPT)
assert spec and spec.loader
vlv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vlv)


def _ecrire(p: Path, texte: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")


def test_liens_bons_et_casses(tmp_path):
    fr = tmp_path / "precis" / "fr"
    _ecrire(fr / "a" / "_x.qmd", "# Titre {#sec-x}\n\n## Une section sans identifiant\n\n"
            '```{python}\not.markdown_avec_legende(t, "Légende", "tbl-y")\n```\n')
    _ecrire(fr / "a" / "index.qmd", "# Présentation\n")
    _ecrire(fr / "b" / "index.qmd",
            "[ok](../a/_x.html#sec-x) [auto](../a/_x.html#une-section-sans-identifiant) "
            "[chaine](../a/_x.html#tbl-y) [dossier](../a/) "
            "[ancre](../a/_x.html#sec-absente) [page](../a/_z.html) "
            "[arabe](../../ar/a/_glossaire.html)\n")
    total, casses, attendus = vlv.controler(fr, tmp_path)
    assert total == 7
    assert attendus == 1
    assert len(casses) == 2
    assert any("sec-absente" in c for c in casses)
    assert any("_z.html" in c for c in casses)


def test_identifiant_pandoc():
    assert vlv.identifiant_pandoc("Les grandes réformes") == "les-grandes-réformes"
    assert vlv.identifiant_pandoc("1. La mise en place") == "la-mise-en-place"

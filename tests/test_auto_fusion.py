"""Éligibilité d'une PR de traduction à l'auto-fusion (fonction pure)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from auto_fusion import eligible  # noqa: E402

BON = dict(auteur="github-actions[bot]", branche="auto-translate/abc-lot-1",
           fichiers=["precis/ar/fiscalite/_tva.qmd", "precis/ar/fiscalite/_quarto.yml",
                     "translation_glossary.generated.md"],
           parite="success", rendu="success", verification="success")


def verdict(**kw):
    args = {**BON, **kw}
    return eligible(args.pop("auteur"), args.pop("branche"), args.pop("fichiers"), **args)


def test_pr_conforme():
    assert verdict() == (True, [])


def test_autres_auteurs_refuses():
    for a in ("benjello", "release-please[bot]", "dependabot[bot]"):
        ok, raisons = verdict(auteur=a)
        assert not ok and "auteur" in raisons[0]


def test_nom_gh_du_robot_accepte():
    assert verdict(auteur="app/github-actions")[0]


def test_branche_hors_traduction_refusee():
    assert not verdict(branche="release-please--branches--master")[0]


def test_un_fichier_hors_ar_suffit_a_refuser():
    for hors in ("precis/fr/fiscalite/_tva.qmd", ".github/workflows/deploy.yml",
                 "scripts/translate_sync.py", "CHANGELOG_ar.md", "precis/arabe/x.qmd"):
        ok, raisons = verdict(fichiers=BON["fichiers"] + [hors])
        assert not ok and hors in " ".join(raisons)


def test_aucun_fichier_refuse():
    assert not verdict(fichiers=[])[0]


def test_chaque_controle_doit_reussir_pas_seulement_ne_pas_echouer():
    for cle in ("parite", "rendu", "verification"):
        for valeur in ("failure", "skipped", "cancelled", ""):
            ok, raisons = verdict(**{cle: valeur})
            assert not ok and len(raisons) == 1


def test_brouillon_refuse():
    assert not verdict(brouillon=True)[0]


def test_toutes_les_raisons_sont_donnees():
    ok, raisons = verdict(auteur="x", parite="failure", rendu="skipped")
    assert not ok and len(raisons) == 3

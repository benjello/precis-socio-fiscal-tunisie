"""Pages générales touchées, nettoyage borné après rendu, liste complète des livres."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from verifier_livres import (  # noqa: E402
    LIVRES, livres_sources_touchees, nettoyage_apres_rendu, pages_generales_touchees)

RACINE = Path(__file__).resolve().parent.parent


def test_tous_les_livres_sont_verifies():
    livres = {p.name for p in (RACINE / "precis" / "fr").iterdir() if (p / "_quarto.yml").exists()}
    assert livres == set(LIVRES)


def test_pages_generales_touchees():
    assert pages_generales_touchees(["precis/fr/principes-structure.qmd"]) == ["fr/principes-structure"]
    assert pages_generales_touchees(["precis/fr/fiscalite/_tva.qmd"]) == []
    # un module de figures fait rendre les pages qui l'importent
    assert "fr/annexe-comptes-nation" in pages_generales_touchees(["precis/fr/figures/annexe_comptes_nation.py"])


def test_nettoyage_borne():
    diff = ["precis/fr/fiscalite/_tva.qmd", "precis/fr/fiscalite/figdata/a.csv"]
    restaurer, supprimer = nettoyage_apres_rendu(
        avant_modifies=["precis/fr/caisses/figdata/deja.csv"],
        apres_modifies=["precis/fr/caisses/figdata/deja.csv", "precis/fr/caisses/figdata/b.csv",
                        "precis/fr/fiscalite/figdata/c.csv"],
        avant_non_suivis=[],
        apres_non_suivis=["precis/ar/caisses/figdata/n.csv", "precis/fr/fiscalite/figdata/n.csv"],
        livres_sources_touchees=livres_sources_touchees(diff))
    # déjà modifié avant : laissé ; livre dont la source a changé (fiscalité) : laissé
    assert restaurer == ["precis/fr/caisses/figdata/b.csv"]
    assert supprimer == ["precis/ar/caisses/figdata/n.csv"]


def test_page_generale_ne_fait_pas_rendre_les_livres():
    from verifier_livres import livres_touches
    assert livres_touches(["precis/fr/comment-lire.qmd"]) == []
    assert livres_touches(["precis/fr/references.json"]) == sorted(LIVRES)

"""Relevés des listes d'entreprises publiques (annexe du volume « Les entreprises publiques »).

Les totaux sont ceux que la note documentaire a comptés sur les pages des décrets et du rapport
du ministère des Finances (docs/notes/entreprises-publiques-liste-2026-10-13.md, § 2 et § 3) :
si l'un ne revient pas, c'est la transcription qui est fausse.
"""
import csv
from pathlib import Path

LISTES = Path(__file__).resolve().parent.parent / "precis/fr/entreprises_publiques/listes"


def _lire(nom):
    with open(LISTES / f"{nom}.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def test_totaux_du_tableau_de_tutelle_et_du_rapport():
    lignes = _lire("entreprises-publiques-listes")
    totaux = {}
    for l in lignes:
        totaux[l["liste"]] = totaux.get(l["liste"], 0) + int(l["nombre"])
        assert (l["presente"] == "oui") == (int(l["nombre"]) > 0)
    assert totaux == {"1998": 123, "2002": 105, "2005": 104, "2010": 105, "2021": 110}


def test_totaux_de_la_liste_des_etablissements():
    lignes = _lire("etablissements-entreprises-publiques")
    totaux = {}
    for l in lignes:
        totaux[l["liste"]] = totaux.get(l["liste"], 0) + (l["present"] == "oui")
    assert totaux == {"1997": 41, "1998": 42, "1999": 44, "2002": 44, "2004": 44, "2006": 43,
                      "2007-07": 45, "2007": 46}


def test_les_deux_listes_se_recoupent():
    """Les établissements marqués au tableau de tutelle redonnent l'état de leur liste."""
    lignes = _lire("entreprises-publiques-listes")
    marques = {}
    for l in lignes:
        marques[l["liste"]] = marques.get(l["liste"], 0) + (l["etablissement_public"] == "oui")
    assert (marques["1998"], marques["2002"], marques["2005"], marques["2010"]) == (42, 44, 44, 46)


def test_une_ligne_par_entreprise_et_par_liste():
    for nom, n_listes in (("entreprises-publiques-listes", 5),
                          ("etablissements-entreprises-publiques", 8)):
        lignes = _lire(nom)
        cles = [(l["rang"], l["liste"]) for l in lignes]
        assert len(cles) == len(set(cles))
        assert len(lignes) % n_listes == 0


def test_sorties_rapprochees_du_recueil():
    """Chaque sortie rapprochée du recueil de la privatisation est bien une sortie du relevé,
    retrouve au moins une ligne du recueil, et sa position dit vrai."""
    presence = {(l["rang"], l["liste"]): l["presente"] for l in _lire("entreprises-publiques-listes")}
    cache = LISTES.parents[2] / "_seriescache/privatisation-recueil-operations.csv"
    with open(cache, encoding="utf-8", newline="") as f:
        recueil = list(csv.DictReader(f))
    positions = {}
    for s in _lire("sorties-recueil-privatisation"):
        assert presence[(s["rang"], s["liste_avant"])] == "oui", s["entreprise"]
        assert presence[(s["rang"], s["liste_apres"])] == "non", s["entreprise"]
        lignes = [r for r in recueil
                  if (r["secteur"], r["sigle"]) == (s["secteur_recueil"], s["sigle_recueil"])]
        assert lignes, s["entreprise"]
        debut = min(int(r["annee_debut"]) for r in lignes)
        if s["position"] == "entre les deux listes":
            assert int(s["liste_avant"]) <= debut <= int(s["liste_apres"]), s["entreprise"]
        else:
            assert s["position"] == "avant la première liste"
            assert max(int(r["annee_fin"]) for r in lignes) < int(s["liste_avant"]), s["entreprise"]
        positions[s["position"]] = positions.get(s["position"], 0) + 1
    assert positions == {"entre les deux listes": 15, "avant la première liste": 2}


def test_plafond_de_la_garantie_est_continu():
    """Un relèvement en cours de gestion porte le montant d'avant, qui est celui que la loi de
    finances de l'année avait fixé ; les gestions se suivent de 1959-60 à 1994, sauf 1960."""
    lignes = _lire("plafond-garanties-lois-de-finances")
    fixe = {}
    for l in lignes:
        if l["nature"] == "fixation" and l["plafond_md"]:
            fixe[l["gestion"]] = float(l["plafond_md"])
    for l in lignes:
        if l["plafond_avant_md"]:
            assert float(l["plafond_avant_md"]) == fixe[l["gestion"]]
            assert float(l["plafond_md"]) > float(l["plafond_avant_md"])
    assert [l["gestion"] for l in lignes if l["nature"] == "fixation"] == [
        "1958-59", "1959-60"] + [str(a) for a in range(1961, 1995)]
    assert fixe["1977"] == 200.0 and fixe["1994"] == 950.0 and fixe["1992"] == 250.0
    # une ligne par montant : pas deux fois le même article pour la même gestion
    cles = [(l["gestion"], l["loi"], l["article"]) for l in lignes]
    assert len(cles) == len(set(cles))


def test_registre_du_plafond_du_chapitre_est_celui_du_releve():
    """Le registre écrit dans le chapitre (pour que les ancres se lisent) est la sortie de
    `tableau_plafond` : si le relevé change, le chapitre doit être recopié."""
    import contextlib
    import io
    import sys

    import pytest

    pytest.importorskip("matplotlib")
    racine = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(racine / "precis/fr/entreprises_publiques"))
    from figures import listes

    sortie = io.StringIO()
    with contextlib.redirect_stdout(sortie):
        listes.tableau_plafond("x")
    attendu = [l for l in sortie.getvalue().splitlines() if "{#r-ep-pl-" in l]
    chapitre = (racine / "precis/fr/entreprises_publiques/_relation_financiere.qmd").read_text(
        encoding="utf-8")
    ecrit = [l for l in chapitre.splitlines() if "{#r-ep-pl-" in l]
    assert attendu and ecrit == attendu


def test_parts_du_plafond_de_la_garantie():
    """Parts du plafond : PIB de l'année de la gestion (aucune part pour 1959-60), dépenses de
    l'État hors service de la dette de 1986 à 1994 seulement, PIB en deux segments de base."""
    import sys

    import pytest

    pytest.importorskip("matplotlib")
    racine = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(racine / "precis/fr/entreprises_publiques"))
    from figures import listes

    t = listes.table_plafond().set_index("Gestion")
    pib = "Plafond fixé, en % du PIB"
    dep = "Plafond fixé, en % des dépenses de l'État"
    assert t.loc["1959-60", pib] != t.loc["1959-60", pib]  # NaN : pas d'année de PIB
    assert t.loc["1961", "PIB de l'année (MD)"] == 363.8
    assert t.loc["1977", pib] == pytest.approx(100 * 200 / 2191.9, abs=0.01)
    assert t.loc["1994", dep] == pytest.approx(100 * 950 / 4276.6, abs=0.01)
    assert t.loc["1985", dep] != t.loc["1985", dep]  # NaN : pas de dépenses avant 1986
    assert t.loc["1986", dep] == pytest.approx(100 * 200 / 2395.0, abs=0.01)
    assert set(t.loc["1961":"1991", "Base du PIB"]) == {"base non dite"}
    assert set(t.loc["1992":"1994", "Base du PIB"]) == {"base 1983"}

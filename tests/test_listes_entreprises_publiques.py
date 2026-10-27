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


def _plafond_serie():
    """Le plafond, lu dans le cache de la série `jort-lf-plafond-garanties` de tunisia-data,
    sous les noms de colonnes de l'ancien relevé."""
    cache = LISTES.parents[2] / "_seriescache/jort-lf-plafond-garanties.csv"
    with open(cache, encoding="utf-8", newline="") as f:
        lignes = list(csv.DictReader(f))
    for l in lignes:
        l["plafond_md"], l["plafond_avant_md"] = l["valeur_md"], l["valeur_avant_md"]
    return lignes


def test_plafond_de_la_garantie_est_continu():
    """Un relèvement en cours de gestion porte le montant d'avant, qui est celui que la loi de
    finances de l'année avait fixé ; les gestions se suivent de 1959-60 à 2026, sauf 1960."""
    lignes = _plafond_serie()
    fixe = {}
    for l in lignes:
        if l["nature"] == "fixation" and l["plafond_md"]:
            fixe[l["gestion"]] = float(l["plafond_md"])
    for l in lignes:
        if l["plafond_avant_md"]:
            assert float(l["plafond_avant_md"]) == fixe[l["gestion"]]
            assert float(l["plafond_md"]) > float(l["plafond_avant_md"])
    assert [l["gestion"] for l in lignes if l["nature"] == "fixation"] == [
        "1958-59", "1959-60"] + [str(a) for a in range(1961, 2027)]
    assert fixe["1977"] == 200.0 and fixe["1994"] == 950.0 and fixe["1992"] == 250.0
    # 1995-2015 : 950 MD jusqu'en 2010 sauf 2003 (1 200), 1 800 en 2011, 4 000 en 2012, 3 000 de 2013 à 2015
    assert all(fixe[str(a)] == 950.0 for a in range(1994, 2011) if a != 2003)
    assert fixe["2003"] == 1200.0 and fixe["2011"] == 1800.0 and fixe["2012"] == 4000.0
    assert {fixe[str(a)] for a in (2013, 2014, 2015)} == {3000.0}
    # relèvements en cours de gestion depuis 1995 : 2002 (loi n° 2002-90), 2011 (décret-loi n° 2011-56),
    # 2019 (loi n° 2019-77), 2020 (loi n° 2020-45), 2023 (loi n° 2023-12)
    releves = {l["gestion"]: (float(l["plafond_avant_md"]), float(l["plafond_md"]))
               for l in lignes if l["plafond_avant_md"] and int(l["gestion"][:4]) >= 1995}
    assert releves == {"2002": (950.0, 1800.0), "2011": (1800.0, 4000.0), "2019": (4500.0, 4790.0),
                       "2020": (5000.0, 7000.0), "2023": (7000.0, 8000.0)}
    # 2016-2026 : 3 000 jusqu'en 2018, puis 4 500, 5 000, 7 000 (2021-2023), 8 000 (2024-2025), 7 000 (2026)
    assert {fixe[str(a)] for a in (2016, 2017, 2018)} == {3000.0}
    assert fixe["2019"] == 4500.0 and fixe["2020"] == 5000.0
    assert {fixe[str(a)] for a in (2021, 2022, 2023)} == {7000.0}
    assert fixe["2024"] == 8000.0 and fixe["2025"] == 8000.0 and fixe["2026"] == 7000.0
    # une ligne par montant : pas deux fois le même article pour la même gestion
    cles = [(l["gestion"], l["loi"], l["article"]) for l in lignes]
    assert len(cles) == len(set(cles))


def test_budget_ordinaire_vote_recettes_et_credits_egaux():
    """Le budget ordinaire voté (titre I) a des recettes égales aux crédits chaque année : l'égalité
    contrôle la lecture. 1959-60 n'a que les recettes (crédits effacés à l'image) ; les gestions se
    suivent de 1961 à 1986."""
    lignes = _lire("budget-ordinaire-lois-de-finances")
    assert [l["gestion"] for l in lignes] == ["1959-60"] + [str(a) for a in range(1961, 1987)]
    for l in lignes:
        if l["credits_md"]:
            assert float(l["credits_md"]) == float(l["recettes_md"]), l["gestion"]
        else:
            assert l["gestion"] == "1959-60"
    montants = [float(l["recettes_md"]) for l in lignes]
    assert montants == sorted(montants)  # le budget voté ne baisse jamais, en dinars courants
    par = {l["gestion"]: float(l["recettes_md"]) for l in lignes}
    assert par["1961"] == 55.8 and par["1969"] == 131.35 and par["1977"] == 441.5
    assert par["1983"] == 1420.0 and par["1986"] == 1970.0
    # chaque loi du relevé du budget est une loi du relevé du plafond, même numéro et même date
    plafond = {(l["gestion"], l["loi"]): l["date"] for l in _plafond_serie()
               if l["nature"] == "fixation"}
    for l in lignes:
        assert plafond[(l["gestion"], l["loi"])] == l["date"], l["gestion"]


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
    l'État hors service de la dette de 1986 à 2015 seulement, budget ordinaire voté de 1959-60 à 1986, PIB en quatre segments de base."""
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
    bud = "Plafond fixé, en % du budget ordinaire voté"
    assert t.loc["1959-60", bud] == pytest.approx(100 * 12 / 48.6, abs=0.01)
    assert t.loc["1977", bud] == pytest.approx(100 * 200 / 441.5, abs=0.01)
    assert t.loc["1974", "Montant en vigueur à la fin, en % du budget ordinaire voté"] == (
        pytest.approx(100 * 50 / 247.2, abs=0.01))
    assert t.loc["1986", bud] == pytest.approx(100 * 200 / 1970.0, abs=0.01)  # recouvrement 1986
    assert t.loc["1987", bud] != t.loc["1987", bud]  # NaN : le budget voté s'arrête en 1986
    assert t.loc["1986", dep] == pytest.approx(100 * 200 / 2395.0, abs=0.01)
    assert set(t.loc["1961":"1991", "Base du PIB"]) == {"base non dite"}
    assert set(t.loc["1992":"1996", "Base du PIB"]) == {"base 1983"}
    assert set(t.loc["1997":"2009", "Base du PIB"]) == {"base 1997"}
    assert set(t.loc["2010":"2015", "Base du PIB"]) == {"base 2015"}
    assert t.loc["2012", dep] == pytest.approx(100 * 4000 / 19141.9, abs=0.01)
    assert t.loc["2011", "Montant en vigueur à la fin, en % du PIB"] == pytest.approx(
        100 * 4000 / 67747.3, abs=0.01)


def test_figure_des_dettes_et_creances_croisees_recoupe_le_tableau():
    """Les trois séries de la figure sont les totaux du tableau ; le solde est créances moins
    dettes ; le PIB est en base 2015, non rétropolé."""
    import contextlib
    import io
    import sys

    import pytest

    pytest.importorskip("matplotlib")
    racine = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(racine / "precis/fr/entreprises_publiques"))
    sys.path.insert(0, str(racine / "scripts"))
    from figures import entreprises_publiques as ep

    t = ep.table_croisees().set_index("Fin d'année")
    assert list(t.index) == [2021, 2022, 2023]
    assert t["Dettes envers l'État (MD)"].tolist() == [8391.8, 10899.3, 11246.3]
    assert t["Créances sur l'État (MD)"].tolist() == [9864.4, 12184.3, 11960.7]
    for a in t.index:
        assert t.loc[a, "Solde, créances moins dettes (MD)"] == pytest.approx(
            t.loc[a, "Créances sur l'État (MD)"] - t.loc[a, "Dettes envers l'État (MD)"], abs=0.1)
    assert set(t["Base du PIB"]) == {"base 2015"}
    sortie = io.StringIO()
    with contextlib.redirect_stdout(sortie):
        ep.tableau_croisees("x")
    for a in t.index:
        for col in ("Dettes envers l'État (MD)", "Créances sur l'État (MD)"):
            assert ep._n(t.loc[a, col]) in sortie.getvalue()


def test_budget_d_equipement_et_total_de_l_etat():
    """Voies et moyens = crédits de paiement ; le total de l'État est le budget ordinaire plus les
    crédits de paiement moins la contribution ; celui de 1983 est établi par la loi ; le budget
    ordinaire repris est celui du relevé du budget ordinaire."""
    ordinaire = {l["gestion"]: l["credits_md"] or l["recettes_md"]
                 for l in _lire("budget-ordinaire-lois-de-finances")}
    lignes = _lire("budget-equipement-lois-de-finances")
    assert len([l for l in lignes if l["voies_moyens_md"]]) == 25
    for l in lignes:
        if not l["voies_moyens_md"]:
            continue
        assert float(l["voies_moyens_md"]) == float(l["credits_paiement_md"]), l["gestion"]
        if l["total_etat_calcule_md"]:
            assert l["budget_ordinaire_md"] and l["gestion"] in ordinaire
            assert float(l["budget_ordinaire_md"]) == float(ordinaire[l["gestion"]]), l["gestion"]
            attendu = (float(l["budget_ordinaire_md"]) + float(l["credits_paiement_md"])
                       - float(l["contribution_budget_ordinaire_md"]))
            assert abs(float(l["total_etat_calcule_md"]) - attendu) < 0.01, l["gestion"]
    par = {l["gestion"]: l for l in lignes}
    assert par["1983"]["total_etat_etabli_md"] == "1753" == par["1983"]["total_etat_calcule_md"]
    assert not par["1962"]["total_etat_calcule_md"] and not par["1962-1964"]["total_etat_calcule_md"]


def test_registre_des_prets_du_tresor_du_chapitre_est_celui_du_releve():
    """Le registre des prêts du Trésor écrit dans le chapitre (ancres r-ep-pt-…) est la sortie de
    `tableau_prets_tresor` : si la série change, le chapitre doit être recopié."""
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
        listes.tableau_prets_tresor("x")
    attendu = [l for l in sortie.getvalue().splitlines() if "{#r-ep-pt-" in l]
    chapitre = (racine / "precis/fr/entreprises_publiques/_relation_financiere.qmd").read_text(
        encoding="utf-8")
    ecrit = [l for l in chapitre.splitlines() if "{#r-ep-pt-" in l]
    assert attendu and ecrit == attendu

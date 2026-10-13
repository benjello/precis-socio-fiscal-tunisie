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

"""Règles de somme sur les participations des sociétés cotées et sur les engagements de la BNA.

Plan : docs/notes/plan-cas-bna-consolidation-flux-2026-11-04.md. Un échec veut dire que la transcription
d'un relevé a changé ou est fausse ; aucune valeur n'est corrigée ici.
  A : le nombre total d'actions déduit de chaque détenteur (actions / part) est le même, à l'arrondi de la part près ;
  B : la somme des parts nommées ne dépasse pas 100 % ;
  D : dividende de l'État imprimé = actions de l'État x dividende par action ;
  G : somme des engagements (ou des garanties) détaillés <= total imprimé ; garantie <= engagement par entité.
"""
import csv
from collections import defaultdict
from pathlib import Path

LISTES = Path(__file__).resolve().parent.parent / "precis/fr/entreprises_publiques/listes"


def _lire(nom):
    with open(LISTES / f"{nom}.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _par_societe():
    par = defaultdict(list)
    for p in _lire("societes-cotees-participations"):
        par[p["societe"]].append(p)
    return par


def test_regle_a_nombre_total_d_actions_coherent():
    for societe, lignes in _par_societe().items():
        if len(lignes) < 2:
            continue
        implicites = [int(p["actions"]) / (float(p["part_pct"]) / 100) for p in lignes]
        tolerance = max(0.005 / float(p["part_pct"]) for p in lignes)
        ecart = (max(implicites) - min(implicites)) / min(implicites)
        assert ecart <= tolerance, f"{societe} : écart {ecart:.4%} > arrondi {tolerance:.4%}"


def test_regle_b_somme_des_parts_nommees():
    for societe, lignes in _par_societe().items():
        total = sum(float(p["part_pct"]) for p in lignes)
        assert 0 < total <= 100, f"{societe} : {total} %"


def test_regle_d_dividende_de_l_etat():
    n = 0
    for r in _lire("societes-cotees-resultats"):
        if r["dividende_etat_dt"] and r["dividende_par_action_dt"]:
            calcule = int(r["actions_etat"]) * float(r["dividende_par_action_dt"])
            assert abs(calcule - float(r["dividende_etat_dt"])) <= 1, f"{r['societe']} {r['exercice']}"
            n += 1
    assert n >= 4, "au moins quatre dividendes imprimés contrôlés"


def test_actions_de_l_etat_egales_dans_les_deux_relevés():
    etat = {p["societe"]: int(p["actions"]) for p in _lire("societes-cotees-participations") if p["detenteur"] == "État"}
    for r in _lire("societes-cotees-resultats"):
        assert etat[r["societe"]] == int(r["actions_etat"]), r["societe"]


def test_regle_g_engagements_et_garanties_de_la_bna():
    par = defaultdict(dict)
    for x in _lire("bna-engagements-entreprises-publiques"):
        if x["valeur_kdt"].lstrip("-").isdigit():
            par[(x["exercice"], x["entite"])][x["grandeur"]] = int(x["valeur_kdt"])
    annees = sorted({e for e, _ in par})
    for annee in annees:
        total = par[(annee, "Total des entreprises publiques")]
        detail = [v for (e, ent), v in par.items() if e == annee and not ent.startswith("Total")]
        for grandeur in ("engagements", "garanties de l'État"):
            somme = sum(v.get(grandeur, 0) for v in detail)
            if grandeur in total:
                assert somme <= total[grandeur], f"{annee} {grandeur} : {somme} > {total[grandeur]}"
        for v in detail:
            if "garanties de l'État" in v and "engagements" in v:
                assert v["garanties de l'État"] <= v["engagements"], f"{annee}"

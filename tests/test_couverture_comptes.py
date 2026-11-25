"""La part du compte couverte ne peut pas monter quand on retire un poste ; la justesse est distincte."""
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import couverture_comptes as cc  # noqa: E402


def ligne(cote, op, v, code="D.61"):
    return {"cote": cote, "operation": op, "valeur": str(v), "code_scn2008": code, "sous_ligne": "0"}


def poste(op, cote, verse, recoit, m):
    return {"operation": op, "cote": cote, "secteur_verse": verse, "secteur_recoit": recoit,
            "montant_reference": "" if m is None else str(m)}


OPS = [ligne("ressources", "cotisations_sociales", 1000), ligne("emplois", "prestations_especes", 800, "D.62"),
       ligne("ressources", "subventions", -200, "D.3"), ligne("emplois", "consommation_intermediaire", 500, "P.2")]
POSTES = [poste("cotisations_sociales", "ressources", "menages", "apu_secu", 900),
          poste("prestations_especes", "emplois", "apu_secu", "menages", 600),
          poste("subventions", "ressources", "apu_secu", "snf", 150)]


def part(postes, ops=OPS, membres=("apu_secu",), cle="part_couverte_pct"):
    return cc.indicateurs(ops, cc.postes_du_secteur(postes, membres))[cle]


def montant(postes, ops=OPS, membres=("apu_secu",)):
    return part(postes, ops, membres, "part_montant_couverte_pct")


def test_definitions_sur_un_exemple():
    r = cc.indicateurs(OPS, cc.postes_du_secteur(POSTES, ("apu_secu",)))
    assert r["operations"] == 4 and r["operations_chiffrees"] == 3
    assert r["part_couverte_pct"] == round(100 * 2000 / 2500, 1)  # 1000 + 800 + 200 sur 2500
    assert r["justesse_pct"] == round(100 * 1650 / 2000, 1)  # 900 + 600 + 150 sur 2000


def test_subventions_inscrites_en_ressources_du_payeur():
    r = cc.indicateurs([OPS[2]], cc.postes_du_secteur([POSTES[2]], ("apu_secu",)))
    assert r["operations_chiffrees"] == 1


def test_le_receveur_n_inscrit_pas_en_emplois():
    # le fournisseur de l'État ne voit pas l'achat dans sa consommation intermédiaire
    p = poste("consommation_intermediaire", "emplois", "apu_centrale", "snf", 300)
    assert part([p], [OPS[3]], ("snf",)) == 0.0


def test_retirer_un_poste_ne_fait_pas_monter_la_part_exemple():
    base = part(POSTES)
    for i in range(len(POSTES)):
        assert part(POSTES[:i] + POSTES[i + 1:]) <= base
        sans_montant = [dict(p, montant_reference="") if j == i else p for j, p in enumerate(POSTES)]
        assert part(sans_montant) <= base


@pytest.mark.parametrize("annee", [2020, 2023])
def test_retirer_un_poste_ne_fait_pas_monter_la_part_donnees(annee):
    import yaml
    import reconstruire_comptes as rc
    secteurs = rc.lire_csv(rc.CACHE / "cnat-secteurs.csv")
    snapshot = {e["id"]: e for e in yaml.safe_load((rc.CACHE / "catalog.snapshot.yml").read_text(encoding="utf-8"))}
    ed = rc.edition_pour(secteurs, annee)
    postes, *_ = rc.calculer(annee, ed, secteurs, snapshot)
    lig = [l for l in secteurs if l["edition"] == ed and int(l["annee"]) == annee]
    for code, (sec, membres) in cc.SECTEURS.items():
        ops = cc.feuilles([l for l in lig if l["secteur"] == sec], garder=set(cc.postes_du_secteur(postes, membres)))
        base = part(postes, ops, membres)
        base_m = montant(postes, ops, membres)
        assert base_m <= base
        for i, p in enumerate(postes):
            if p.get("montant_reference"):
                reste = postes[:i] + postes[i + 1:]
                assert part(reste, ops, membres) <= base, (code, p["poste"])
                assert montant(reste, ops, membres) <= base_m, (code, p["poste"])


def test_agregat_garde_quand_lui_seul_porte_un_poste():
    ls = [ligne("emplois", "remuneration_salaries", 100, "D.1"), ligne("emplois", "salaires_bruts", 80, "D.11"),
          ligne("emplois", "cotisations_employeurs", 20, "D.12")]
    assert [l["operation"] for l in cc.feuilles(ls, {"remuneration_salaries"})] == ["remuneration_salaries"]
    assert [l["operation"] for l in cc.feuilles(ls)] == ["salaires_bruts", "cotisations_employeurs"]
    assert [l["operation"] for l in cc.feuilles(ls, {"remuneration_salaries", "salaires_bruts"})] == ["salaires_bruts", "cotisations_employeurs"]


def test_part_du_montant_plafonnee_et_partielle():
    r = cc.indicateurs(OPS, cc.postes_du_secteur(POSTES, ("apu_secu",)))
    assert r["part_montant_couverte_pct"] == round(100 * (900 + 600 + 150) / 2500, 1)
    trop = [poste("cotisations_sociales", "ressources", "menages", "apu_secu", 5000)]
    assert cc.indicateurs(OPS, cc.postes_du_secteur(trop, ("apu_secu",)))["part_montant_couverte_pct"] == 40.0
    partage = [poste("cotisations_sociales", "ressources", "menages", "apu_secu;apu_centrale", 900)]
    assert cc.indicateurs(OPS, cc.postes_du_secteur(partage, ("apu_secu",)))["part_montant_couverte_pct"] == 0.0


def test_retirer_un_poste_ne_fait_pas_monter_la_part_du_montant_exemple():
    base = montant(POSTES)
    for i in range(len(POSTES)):
        assert montant(POSTES[:i] + POSTES[i + 1:]) <= base


# Production imprimée sous le seul code P.1 : valeurs de l'édition 2020-2024, année 2020 (cnat-secteurs.csv).
def ops_retenues(ls, garder=None):
    return sorted(l["operation"] for l in cc.feuilles(ls, garder))


def test_p1_seul_est_garde():
    ls = [ligne("ressources", "production_bs_marchands", 100437.0, "P.1")]
    assert ops_retenues(ls) == ["production_bs_marchands"]


def test_p1_parent_de_p11_et_p13_ne_s_ajoute_pas():
    ls = [ligne("ressources", "production", 64030.4, "P.1"), ligne("ressources", "production_marchande", 55753.8, "P.11"),
          ligne("ressources", "production_non_marchande", 8276.6, "P.13")]
    assert ops_retenues(ls) == ["production_marchande", "production_non_marchande"]


def test_societes_financieres_composantes_imprimees_sous_p1():
    # le total est la ligne « biens et services marchands » ; assurance et SIFIM sont des composantes
    ls = [ligne("ressources", "production_bs_marchands", 6573.0, "P.1"),
          ligne("ressources", "production_services_assurance", 994.1, "P.1"),
          ligne("ressources", "production_sifim", 3325.0, "P.1"),
          ligne("ressources", "production_marchande", 2083.1, "P.11"),
          ligne("ressources", "production_non_marchande", 170.9, "P.13")]
    fs = cc.feuilles(ls)
    assert sorted(l["operation"] for l in fs) == ["production_marchande", "production_non_marchande",
                                                 "production_services_assurance", "production_sifim"]
    assert round(sum(float(l["valeur"]) for l in fs), 1) == 6573.1


def test_administrations_production_marchande_sous_p1():
    ls = [ligne("ressources", "production", 27526.1, "P.1"), ligne("ressources", "production_bs_marchands", 1533.1, "P.1"),
          ligne("ressources", "production_non_marchande", 25993.0, "P.13")]
    assert ops_retenues(ls) == ["production_bs_marchands", "production_non_marchande"]


def test_total_et_composantes_tous_sous_p1():
    # sociétés d'assurance : ni P.11 ni P.13, le total ne s'ajoute pas à ses composantes
    ls = [ligne("ressources", "production", 1006.8, "P.1"), ligne("ressources", "production_bs_marchands", 12.7, "P.1"),
          ligne("ressources", "production_services_assurance", 994.1, "P.1")]
    assert ops_retenues(ls) == ["production_bs_marchands", "production_services_assurance"]


def test_deux_lignes_de_meme_code_sans_composante_sont_gardees():
    ls = [ligne("emplois", "interets", 5000.0, "D.41"), ligne("emplois", "correction_sifim", 5000.0, "D.41")]
    assert ops_retenues(ls) == ["correction_sifim", "interets"]


def test_total_p1_garde_quand_lui_seul_porte_un_poste():
    ls = [ligne("ressources", "production", 27526.1, "P.1"), ligne("ressources", "production_bs_marchands", 1533.1, "P.1"),
          ligne("ressources", "production_non_marchande", 25993.0, "P.13")]
    assert ops_retenues(ls, {"production"}) == ["production"]
    assert ops_retenues(ls, {"production", "production_non_marchande"}) == ["production_bs_marchands",
                                                                            "production_non_marchande"]


def test_deux_totaux_possibles_est_une_erreur():
    ls = [ligne("ressources", "a", 0.0, "P.1"), ligne("ressources", "b", 0.0, "P.1"), ligne("ressources", "c", 0.0, "P.13")]
    with pytest.raises(ValueError):
        cc.feuilles(ls)


def test_chaque_total_p1_du_cache_est_reconnu():
    # dans le cache, toute famille P.1 d'au moins trois lignes dont deux sous le seul code P.1 a un total et un seul
    import csv
    from collections import defaultdict
    with (RACINE / "precis" / "_seriescache" / "cnat-secteurs.csv").open(encoding="utf-8") as f:
        lig = [l for l in csv.DictReader(f) if l["code_scn2008"].startswith("P.1") and l["sous_ligne"] in ("0", "1")]
    g = defaultdict(list)
    for l in lig:
        g[(l["base"], l["edition"], l["annee"], l["secteur"], l["cote"])].append(l)
    familles = [ls for ls in g.values() if len(ls) >= 3 and sum(l["code_scn2008"] == "P.1" for l in ls) >= 2]
    assert familles and all("P.1" in cc.totaux_meme_code(ls) for ls in familles)

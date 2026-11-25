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
        ops = cc.feuilles([l for l in lig if l["secteur"] == sec], garder=cc.garder_par_cote(cc.postes_du_secteur(postes, membres)))
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


def test_feuilles_decidees_cote_par_cote():
    # Reste du monde : un poste sur D.75 en emplois (versé par S2), un poste sur l'agrégat D.7 en ressources
    # (reçu par S2). En ressources, D.7 reste la feuille ; en emplois, il cède la place à ses composantes.
    ls = [ligne(c, op, v, code) for c in ("emplois", "ressources")
          for op, v, code in (("autres_transferts_courants", 100, "D.7"), ("primes_assurance_dommages", 10, "D.71"),
                              ("transferts_courants_divers", 90, "D.75"))]
    postes = [poste("transferts_courants_divers", "emplois", "rdm", "menages", 60),
              poste("autres_transferts_courants", "ressources", "menages", "rdm", 5)]
    ratt = cc.postes_du_secteur(postes, ("rdm",))
    assert cc.garder_par_cote(ratt) == {"emplois": {"transferts_courants_divers"},
                                        "ressources": {"autres_transferts_courants"}}
    fs = cc.feuilles(ls, cc.garder_par_cote(ratt))
    assert sorted((l["cote"], l["operation"]) for l in fs) == [
        ("emplois", "primes_assurance_dommages"), ("emplois", "transferts_courants_divers"),
        ("ressources", "autres_transferts_courants")]
    # les deux postes comptent : 60 en emplois, 5 en ressources
    assert cc.indicateurs(fs, ratt)["montant_couvert_md"] == 65.0
    # un ensemble unique, valable pour les deux côtés, garde le comportement antérieur
    assert all(l["operation"] != "autres_transferts_courants" for l in cc.feuilles(ls, set(ratt)))


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


def _annees():
    import reconstruire_comptes as rc
    return {(int(l["annee"]), l["secteur"]): l for l in rc.lire_csv(rc.ANNEES)}


def test_annee_2010_couverte_en_base_1997():
    l = _annees()[(2010, "S13")]
    assert l["base"] == "1997" and l["edition"] == "2010-2014"
    assert int(l["operations_chiffrees"]) > 0 and float(l["part_montant_couverte_pct"]) > 0


def test_annee_2015_inchangee_en_base_2015():
    """2015 est publiée dans les deux bases : elle reste mesurée en base 2015, sur l'édition retenue par
    edition_pour, et le calcul direct sur le cache en base 2015 redonne la ligne écrite."""
    import yaml
    import reconstruire_comptes as rc
    secteurs = rc.lire_csv(rc.CACHE / "cnat-secteurs.csv")
    snapshot = {e["id"]: e for e in yaml.safe_load((rc.CACHE / "catalog.snapshot.yml").read_text(encoding="utf-8"))}
    ed = rc.edition_pour(secteurs, 2015)
    postes, *_ = rc.calculer(2015, ed, secteurs, snapshot)
    attendu = rc.couverture_annee(postes, [l for l in secteurs if l["edition"] == ed and int(l["annee"]) == 2015])
    ecrit = _annees()
    for code, ind in attendu.items():
        l = ecrit[(2015, code)]
        assert l["base"] == "2015" and l["edition"] == ed
        assert {k: l[k] for k in ind} == {k: str(v) for k, v in ind.items()}, code


def test_operation_a_valider_non_couverte():
    """Une opération dont le lien au SCN 2008 est « à valider » n'est ni couverte ni comptée, même portée
    par un poste chiffré ; l'opération « identique » voisine l'est."""
    import reconstruire_comptes as rc
    liens = rc.liens_raccord("1997")
    a_valider = next(o for o, lien in liens.items() if lien == "à valider")
    assert liens["cotisations_sociales"] == "identique"
    ops = [ligne("ressources", "cotisations_sociales", 100), ligne("ressources", a_valider, 50, code="D.62")]
    postes = [poste("cotisations_sociales", "ressources", "menages", "apu_secu", 100),
              poste(a_valider, "ressources", "menages", "apu_secu", 50)]
    ratt = cc.postes_du_secteur(postes, ("apu_secu",))
    assert cc.indicateurs(ops, ratt)["operations_chiffrees"] == 2
    ind = cc.indicateurs(cc.raccord_identique(ops, liens), ratt)
    assert ind["operations"] == ind["operations_chiffrees"] == 1 and ind["ins_total_md"] == 100.0


def test_redevance_gazoduc_hors_des_loyers_en_base_1997():
    """INS, éd. 2015-2020, vol. A, p. 17 : avant la base 2015, la redevance du gazoduc était comptée en
    production du secteur transport, non en loyers (D.45)."""
    import reconstruire_comptes as rc
    assert rc.poste_hors_base("redevance-gazoduc", "1997")
    assert not rc.poste_hors_base("redevance-gazoduc", "2015")
    reg = {p["poste"]: p for p in rc.lire_csv(rc.REGISTRE)}
    assert reg["redevance-gazoduc"]["operation"] == "loyers"
    a = _annees()
    for y in range(2005, 2015):  # le reste du monde n'a plus d'opération chiffrée propre en base 1997
        assert a[(y, "S2")]["justesse_pct"] == "", y


def test_controles_en_echec_portee():
    import reconstruire_comptes as rc
    base = {"edition": "2009-2013", "annee": "2009", "statut": "echec", "publie": "1", "recalcule": "2", "ecart": "-1"}
    src = [{**base, "controle": "solde", "secteur": "apu", "objet": "valeur_ajoutee_brute"},
           {**base, "controle": "equilibre", "secteur": "", "objet": "cotisations_sociales"},
           {**base, "controle": "equilibre", "secteur": "", "objet": "operation_hors_total"},
           {**base, "statut": "ok", "controle": "solde", "secteur": "apu_secu", "objet": "valeur_ajoutee_brute"}]
    out = rc.controles_en_echec(src, 2009, "2009-2013", {"cotisations_sociales"})
    assert [(l["objet"], l["touche_total"]) for l in out] == [("valeur_ajoutee_brute", "non"),
                                                               ("cotisations_sociales", "indetermine")]


def test_base_1983_sans_administration_centrale():
    """La série en base 1983 du cache ne porte pas le compte de l'administration centrale : les années qu'elle
    est seule à couvrir ont les collectivités locales et la sécurité sociale, ni l'État ni la somme des trois
    sous-secteurs ; chaque année est lue dans la dernière édition où elle est définitive."""
    import reconstruire_comptes as rc
    b83 = rc.lire_base1997(rc.BASE1983)
    assert "apu_centrale" not in {l["secteur"] for l in b83}
    a = _annees()
    ans83 = sorted({y for (y, _), l in a.items() if l["base"] == "1983"})
    assert ans83 and max(ans83) < min(y for (y, _), l in a.items() if l["base"] == "1997")
    for y in ans83:
        assert (y, "S13") not in a and (y, "S1311") not in a, y
        assert a[(y, "S1313")]["edition"] == a[(y, "S1314")]["edition"] == rc.edition_pour(b83, y)


def test_operations_exclues_base_1983():
    """En base 1983, une feuille dont le lien au SCN 2008 n'est pas « identique » est listée, avec la présence
    d'un poste chiffré ; aucune opération « identique » ne l'est."""
    import reconstruire_comptes as rc
    liens = rc.liens_raccord("1983")
    ex = [l for l in rc.lire_csv(rc.EXCLUES) if l["base"] == "1983"]
    assert ex and all(liens.get(l["operation"]) != "identique" for l in ex)
    assert any(l["operation"] == "prestations_especes" and l["secteur"] == "S1314" and l["poste_chiffre"] == "oui"
               for l in ex)


def test_controles_en_echec_scn68_portee():
    import reconstruire_comptes as rc
    base = {"edition": "2002-2006", "annee": "2002", "imprime": "1", "calcule": "2", "ecart_md": "-1", "cote": "ressources"}
    src = [{**base, "controle": "total", "secteur": "apu", "compte": "COMPTE DE REVENU", "categorie": "ecart"},
           {**base, "controle": "total", "secteur": "apu_locale", "compte": "COMPTE DE CAPITAL", "categorie": "ecart"},
           {**base, "controle": "total", "secteur": "sf", "compte": "COMPTE DE CAPITAL", "categorie": "ecart"},
           {**base, "controle": "total", "secteur": "apu_secu", "compte": "COMPTE DE CAPITAL", "categorie": "ok"}]
    out = rc.controles_en_echec_scn68(src, 2002, "2002-2006")
    assert [(l["secteur"], l["touche_total"], l["base"]) for l in out] == [("apu", "non", "1983"),
                                                                           ("apu_locale", "compte", "1983")]
    assert out[1]["libelle_scn2008"] == "Compte de capital, ressources"


def _ins_d1():
    """D.1 de l'INS : reçu par les ménages, versé par l'État, les sociétés non financières et les ménages."""
    lig = [dict(ligne("ressources", "remuneration_salaries", 1000, "D.1"), secteur="menages"),
           dict(ligne("emplois", "remuneration_salaries", 400, "D.1"), secteur="apu_centrale"),
           dict(ligne("emplois", "salaires_bruts", 500, "D.11"), secteur="snf"),
           dict(ligne("emplois", "remuneration_salaries", 100, "D.1"), secteur="menages"),
           dict(ligne("emplois", "remuneration_salaries", 0, "D.1"), secteur="rdm")]
    return lig[:1], cc.montants_ins(lig)


def test_justesse_exige_toute_la_contrepartie():
    """D.1 en ressources des ménages chiffré par la seule masse salariale de l'État : l'opération reste couverte
    pour la part du montant, mais n'entre pas dans la justesse ; un poste dont les payeurs couvrent tous les
    secteurs qui versent du D.1 selon l'INS (les sociétés par leur D.11, un montant nul ne comptant pas) y entre."""
    ops, ins = _ins_d1()
    etat = [poste("remuneration_salaries", "emplois", "apu_centrale", "menages", 380)]
    r = cc.indicateurs(ops, cc.postes_du_secteur(etat, ("menages",)), "menages", ins)
    assert r["operations_chiffrees"] == 1 and r["montant_couvert_md"] == 380.0
    assert r["operations_justesse"] == 0 and r["justesse_pct"] == ""
    assert cc.indicateurs(ops, cc.postes_du_secteur(etat, ("menages",)))["operations_justesse"] == 1  # sans `ins`
    tous = [poste("remuneration_salaries", "emplois", "apu_centrale;snf;menages", "menages", 950)]
    r = cc.indicateurs(ops, cc.postes_du_secteur(tous, ("menages",)), "menages", ins)
    assert r["operations_justesse"] == 1 and r["justesse_pct"] == 95.0


def test_justesse_poste_sans_contrepartie_nommee():
    """Un poste dont le registre ne nomme pas l'autre bout (FBCF, consommation finale) reste régi par la règle
    des postes propres."""
    lig = [dict(ligne("emplois", "fbcf", 100, "P.51g"), secteur="apu_centrale"),
           dict(ligne("ressources", "fbcf", 100, "P.51g"), secteur="snf")]
    ins = cc.montants_ins(lig)
    p = [poste("fbcf", "emplois", "apu_centrale", "", 90)]
    r = cc.indicateurs(lig[:1], cc.postes_du_secteur(p, ("apu_centrale",)), "apu_centrale", ins)
    assert r["operations_justesse"] == 1

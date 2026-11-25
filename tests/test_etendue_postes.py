"""Étendue des postes et couverture par année sur toute la période des séries."""
import csv
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import etendue_postes as ep  # noqa: E402
import reconstruire_comptes as rc  # noqa: E402


def lire(nom):
    with (RACINE / "precis" / "fr" / nom).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_fichiers_a_jour():
    assert ep.main(["--verifier"]) == 0


def test_etendue_conforme_aux_series():
    registre = {p["poste"]: p for p in rc.lire_csv(rc.REGISTRE)}
    et = lire("postes-etendue.csv")
    assert [l["poste"] for l in et] == list(registre)
    for l in et:
        p = registre[l["poste"]]
        if not p["serie"]:
            assert l["premiere_annee"] == l["derniere_annee"] == "" and l["annees_chiffrees"] == "0"
            continue
        if l["premiere_annee"] == "":
            continue
        a, b = int(l["premiere_annee"]), int(l["derniere_annee"])
        assert ep.chiffre(p, a) and ep.chiffre(p, b), l["poste"]
        assert not ep.chiffre(p, a - 1) and not ep.chiffre(p, b + 1), l["poste"]
        assert int(l["annees_chiffrees"]) == sum(ep.chiffre(p, y) for y in range(a, b + 1))


def test_annees_base2015_du_cache():
    secteurs = [l for l in rc.lire_csv(rc.CACHE / "cnat-secteurs.csv") if l["base"] == "2015"]
    ans = rc.annees_base2015(secteurs)
    assert sorted({int(l["annee"]) for l in lire("compte-couverture-annees.csv") if l["base"] == "2015"}) == ans
    for y in ans:  # l'édition retenue porte un compte complet, non une ligne isolée
        ed = rc.edition_pour(secteurs, y)
        assert sum(1 for l in secteurs if l["edition"] == ed and int(l["annee"]) == y) > 500, y


def test_pas_de_part_du_montant_avant_la_base_1997():
    cv = lire("compte-couverture-annees.csv")
    debut = min(int(l["annee"]) for l in cv)
    pa = lire("compte-couverture-postes-annees.csv")
    assert "part_montant_couverte_pct" not in pa[0]
    assert min(int(l["annee"]) for l in pa) < debut
    assert {l["base"] for l in cv} == {"1997", "2015"}
    # chaque année dans une seule base : la base 1997 s'arrête avant la première année de la base 2015
    assert max(int(l["annee"]) for l in cv if l["base"] == "1997") < min(int(l["annee"]) for l in cv if l["base"] == "2015")


def test_debut_aux_comptes_des_caisses():
    et = lire("postes-etendue.csv")
    pa = lire("compte-couverture-postes-annees.csv")
    secu = [int(l["premiere_annee"]) for l in et if l["premiere_annee"] and "apu_secu" in
            (l["secteur_verse"] + ";" + l["secteur_recoit"]).split(";")]
    assert min(int(l["annee"]) for l in pa) == min(secu)


def test_retirer_une_serie_ne_fait_pas_monter_le_compte():
    postes = rc.lire_csv(rc.REGISTRE)
    debut = min(int(l["annee"]) for l in lire("compte-couverture-postes-annees.csv"))
    ans = range(debut, debut + 15)
    base = {(l["annee"], l["secteur"]): l["postes_chiffres"] for l in ep.par_annee(postes, ans)}
    for i, p in enumerate(postes):
        if not p["serie"]:
            continue
        reste = postes[:i] + [dict(p, serie="")] + postes[i + 1:]
        for l in ep.par_annee(reste, ans):
            assert l["postes_chiffres"] <= base[(l["annee"], l["secteur"])], p["poste"]

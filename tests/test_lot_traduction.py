"""Choix du lot de traduction, et découpage des gros chapitres (sans réseau)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import lot_traduction as lt  # noqa: E402
import translate_sync as ts  # noqa: E402


def f(chemin, n, jamais=False):
    return {"fichier": chemin, "caracteres": n, "jamais": jamais}


RETARD = [
    f("precis/fr/sante/index.qmd", 10_000, True),
    f("precis/fr/retraites/index.qmd", 20_000),
    f("precis/fr/finances_locales/_a.qmd", 30_000, True),
    f("precis/fr/finances_locales/index.qmd", 5_000, True),
    f("precis/fr/prestations_sociales/_soins.qmd", 40_000, True),
    f("precis/fr/prestations_sociales/_matrice.qmd", 15_000),
    f("precis/fr/prestations_sociales/index.qmd", 8_000),
    f("precis/fr/annexe-pib.qmd", 3_000, True),
]


def lot(**kw):
    base = dict(budget=1_000_000, consommation=0)
    base.update(kw)
    return lt.choisir_lot(RETARD, **base)


def test_ordre_des_livres_priorite_puis_traduits_puis_jamais_traduits():
    assert lt.ordre_des_livres(RETARD) == [
        "prestations_sociales", "finances_locales", "retraites", "sante", "(racine)"]


def test_un_seul_livre_et_perimes_d_abord_index_en_tete():
    r = lot()
    assert r["livre"] == "prestations_sociales"
    assert [x["fichier"].split("/")[-1] for x in r["fichiers"]] == [
        "index.qmd", "_matrice.qmd", "_soins.qmd"]


def test_borne_en_fichiers():
    assert len(lot(max_fichiers=2)["fichiers"]) == 2


def test_borne_en_caracteres_saute_ce_qui_depasse():
    r = lot(max_caracteres=25_000)
    assert [x["caracteres"] for x in r["fichiers"]] == [8_000, 15_000]
    assert r["caracteres"] <= 25_000


def test_plafond_de_passage_fraction_du_budget():
    # 35 % de 100 000 = 35 000 : index (8 000) + matrice (15 000) ; _soins (40 000) ne tient pas
    r = lot(budget=100_000)
    assert r["caracteres"] == 23_000


def test_budget_du_mois_consomme_ne_donne_rien():
    r = lot(budget=100_000, consommation=75_000)   # 75 % planifiés déjà dépensés
    assert r["fichiers"] == [] and "budget" in r["raison"]


def test_un_gros_fichier_part_seul_s_il_tient_dans_le_restant():
    gros = [f("precis/fr/fiscalite/_tva.qmd", 100_000)]
    r = lt.choisir_lot(gros, budget=200_000, consommation=0)  # passage : 70 000 < 100 000
    assert [x["fichier"] for x in r["fichiers"]] == ["precis/fr/fiscalite/_tva.qmd"]
    r = lt.choisir_lot(gros, budget=120_000, consommation=0)  # restant 90 000 < 100 000
    assert r["fichiers"] == []


def test_les_fichiers_d_une_pr_ouverte_sont_ecartes():
    r = lot(exclus={"precis/fr/prestations_sociales/index.qmd",
                    "precis/fr/prestations_sociales/_matrice.qmd",
                    "precis/fr/prestations_sociales/_soins.qmd"})
    assert r["livre"] == "finances_locales"


def test_sonde_apres_limite_un_seul_petit_fichier():
    r = lot(limite_atteinte=True)
    assert len(r["fichiers"]) == 1 and r["fichiers"][0]["caracteres"] == 8_000
    assert "sonde" in r["raison"]


def test_livre_force():
    assert lot(livre="sante")["livre"] == "sante"


def test_retard_nul():
    r = lt.choisir_lot([], budget=1000, consommation=0)
    assert r["fichiers"] == []


def test_reprise_apres_un_lot_le_suivant_prend_la_suite():
    premier = lot(max_fichiers=2)
    traduits = {x["fichier"] for x in premier["fichiers"]}
    reste = [r for r in RETARD if r["fichier"] not in traduits]
    suite = lt.choisir_lot(reste, budget=1_000_000, consommation=0)
    assert suite["livre"] == "prestations_sociales"
    assert not traduits & {x["fichier"] for x in suite["fichiers"]}


# ---------- découpage ----------

LONG = "".join(f"## Section {i}\n\n" + ("Une phrase de prose. " * 40 + "\n\n") * 4
               for i in range(20))


def test_decoupage_sans_ancre_pour_une_premiere_traduction():
    avec = ts.decouper(LONG, taille=5_000)
    assert len(avec) == 1, "sans ancre, aucune coupe permise par défaut"
    sans = ts.decouper(LONG, taille=5_000, sans_ancre=True)
    assert len(sans) > 3
    assert "".join(m for _a, m in sans) == LONG
    assert all(m.startswith("## Section") for _a, m in sans[1:])


def test_decoupage_jamais_dans_du_code_meme_sans_ancre():
    t = "a\n\n```\n## faux titre\n```\n\n## vrai\n"
    assert [p for p, _ in ts.points_de_coupe(t, sans_ancre=True)] == [t.index("## vrai")]


def test_seuils_abaisses():
    assert ts.SEUIL_DECOUPAGE <= 90_000 and ts.TAILLE_MORCEAU <= 45_000

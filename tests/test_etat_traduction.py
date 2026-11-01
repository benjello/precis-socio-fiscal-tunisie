"""L'issue d'état des traductions arabes se construit sans réseau."""
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import etat_traduction as et  # noqa: E402

OCT = datetime(2026, 10, 30, 6, 41, tzinfo=timezone.utc)
RETARD = [
    {"fichier": "precis/fr/fiscalite/_tva.qmd", "caracteres": 100_000, "jamais": False},
    {"fichier": "precis/fr/sante/index.qmd", "caracteres": 20_000, "jamais": True},
    {"fichier": "precis/fr/annexe-pib.qmd", "caracteres": 5_000, "jamais": True},
]


def _donnees(bilan=None, historique=None, etat=None, maintenant=OCT):
    d = {"historique": historique or {}, "etat": etat}
    return et.enregistrer_passage(d, bilan, maintenant)


def test_le_corps_porte_le_marqueur_et_se_retrouve():
    corps = et.construire_corps(RETARD, OCT, _donnees())
    assert et.marqueur() in corps
    assert et.trouver_issue([{"number": 9, "body": "autre"},
                             {"number": 4, "body": corps},
                             {"number": 7, "body": corps}])["number"] == 4
    assert et.trouver_issue([{"number": 1, "body": None}]) is None


def test_retard_nul_le_corps_le_dit():
    corps = et.construire_corps([], OCT, _donnees())
    assert "à jour" in corps and "aucun" in corps


def test_liste_par_livre_et_totaux():
    corps = et.construire_corps(RETARD, OCT, _donnees())
    assert "3 fichier(s)" in corps and "2 jamais" in corps
    assert "| fiscalite | 1 | 0 | 100 000 |" in corps
    assert "| (racine) | 1 | 1 | 5 000 |" in corps


def test_suspension_donne_la_date_de_renouvellement_estimee():
    bilan = {"etat": "suspendue", "nature": "plafond_mensuel", "caracteres": 90_000,
             "traduits": ["precis/ar/a.qmd"], "non_traduits": ["precis/fr/b.qmd"]}
    corps = et.construire_corps(RETARD, OCT, _donnees(bilan))
    assert "plafond mensuel atteint" in corps
    assert "2026-11-01" in corps and "estimation" in corps
    assert "plafond de dépense mensuel" in corps  # ce que l'on sait


def test_renouvellement_en_decembre():
    d = datetime(2026, 12, 15, tzinfo=timezone.utc)
    assert et.renouvellement_estime(d) == datetime(2027, 1, 1, tzinfo=timezone.utc)


def test_le_402_se_distingue_du_plafond():
    bilan = {"etat": "suspendue", "nature": "credit_prepaye", "caracteres": 0,
             "traduits": [], "non_traduits": []}
    corps = et.construire_corps(RETARD, OCT, _donnees(bilan))
    assert "402" in corps


def test_la_suspension_se_leve_au_premier_passage_reussi():
    suspendu = _donnees({"etat": "suspendue", "nature": "plafond_mensuel", "caracteres": 10,
                         "traduits": [], "non_traduits": []})
    corps1 = et.construire_corps(RETARD, OCT, suspendu)
    donnees = et.lire_donnees(corps1)
    # passage sans lot : le constat tient
    sans_lot = et.enregistrer_passage(donnees, None, OCT)
    assert "suspendue" in et.construire_corps(RETARD, OCT, sans_lot)
    # passage réussi : levée
    ok = et.enregistrer_passage(donnees, {"etat": "ok", "caracteres": 500, "traduits": ["x"],
                                          "non_traduits": []}, OCT)
    corps = et.construire_corps(RETARD, OCT, ok)
    assert "**État : en cours**" in corps


def test_les_donnees_survivent_dans_le_corps():
    corps = et.construire_corps(RETARD, OCT, _donnees({"etat": "ok", "caracteres": 1234,
                                                       "traduits": [], "non_traduits": []}))
    assert et.lire_donnees(corps)["historique"]["2026-10"]["caracteres"] == 1234
    assert et.lire_donnees("n'importe quoi") == {"historique": {}, "etat": None}


def test_budget_appris_moyenne_des_trois_derniers_mois_plafonnes():
    h = {
        "2026-06": {"caracteres": 900, "limite_atteinte": True},
        "2026-07": {"caracteres": 300, "limite_atteinte": True},
        "2026-08": {"caracteres": 600, "limite_atteinte": True},
        "2026-09": {"caracteres": 900, "limite_atteinte": True},
        "2026-10": {"caracteres": 50, "limite_atteinte": False},
    }
    assert et.budget_estime(h, "2026-10") == (600, True)  # (300+600+900)/3
    assert et.budget_estime({}, "2026-10") == (et.BUDGET_INITIAL, False)
    # un mois sans limite ne mesure rien
    assert et.budget_estime({"2026-09": {"caracteres": 5, "limite_atteinte": False}},
                            "2026-10") == (et.BUDGET_INITIAL, False)


def test_mois_pour_resorber():
    assert et.mois_pour_resorber(0, 1000) == 0
    assert et.mois_pour_resorber(1500, 1000) == 2  # 750 par mois
    assert et.mois_pour_resorber(10, 1000) == 1


def test_la_consommation_du_mois_s_additionne():
    d = _donnees({"etat": "ok", "caracteres": 100, "traduits": [], "non_traduits": []})
    d = et.enregistrer_passage(d, {"etat": "ok", "caracteres": 50, "traduits": [],
                                   "non_traduits": []}, OCT)
    assert et.consommation(d["historique"], "2026-10") == 150


def test_les_pr_ouvertes_sont_listees_avec_leur_sort():
    prs = [{"number": 7, "title": "Auto-translate sync", "sort": "relecture et fusion à faire à la main"},
           {"number": 8, "title": "Auto-translate lot", "sort": "fusion automatique activée"}]
    corps = et.construire_corps(RETARD, OCT, _donnees(), prs_en_attente=prs)
    assert "#7 Auto-translate sync : relecture et fusion à faire à la main" in corps
    assert "#8 Auto-translate lot : fusion automatique activée" in corps
    assert "PR de traduction ouvertes" not in et.construire_corps(RETARD, OCT, _donnees())

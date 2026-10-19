"""Écrit les séries du régime forfaitaire des bénéfices industriels et commerciaux.

Le build du site n'exécute PAS ce script : il lit les trois CSV qu'il écrit dans
`precis/_seriescache/`, par `figtools.series()` (figure `bic_regimes` du livre « Fiscalité »).

    uv run python scripts/generate_forfait_bic_series.py

D'OÙ VIENNENT LES VALEURS. Les paramètres du forfait ne sont pas encore versés en amont
(openfisca-tunisia#476). Les valeurs ci-dessous sont celles de la note documentaire
`docs/notes/fiscalite-regime-forfaitaire.md` (§ 1 à 5), lues sur les fascicules du *Journal
officiel* ; chaque ligne porte le texte et la page qui la fixent. Le jour où les paramètres
existent en amont, ce générateur est remplacé par une lecture de l'arbre, sans changer le
format des séries.

TROIS SÉRIES.
  - `bic-forfait-tarifs` : une ligne par morceau de tarif, état (année de la loi), régime
    (« forfait » ou « option »), activité, zone. Voir `bic_regimes.Morceau`.
  - `bic-minimum-impot` : le minimum d'impôt de l'article 44 § II, une ligne par modificatif.
  - `bic-hypotheses-benefice` : les taux de bénéfice (part du chiffre d'affaires) du régime
    réel que la figure suppose.

Le lien de chaque ligne est l'URL de la référence, lue dans `references.json` : jamais écrite
ici ; une référence sans URL vérifiée laisse la case vide.
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

RACINE = Path(__file__).resolve().parent.parent / "precis"
CACHE = RACINE / "_seriescache"

SERIE_TARIFS = "bic-forfait-tarifs"
SERIE_MINIMUM = "bic-minimum-impot"
SERIE_HYPOTHESES = "bic-hypotheses-benefice"

INF = None  # plafond ouvert : jamais utilisé, chaque régime a un plafond de chiffre d'affaires


def _urls() -> dict[str, str]:
    urls = {}
    for chemin in (RACINE / "fr" / "references.json", RACINE / "fr" / "fiscalite" / "references.json"):
        items = json.loads(chemin.read_text(encoding="utf-8"))
        items = items["items"] if isinstance(items, dict) else items
        for e in items:
            if e.get("URL") and e["id"] not in urls:
                urls[e["id"]] = e["URL"]
    return urls


# --- Annexe II, code de 1990 (p. 18) : montants par tranche de chiffre d'affaires --------

def _par_tranches(pas: list[tuple[float, float]]) -> list[tuple[float, float, float]]:
    """[(haut, montant)…] -> [(bas, haut, montant)…], la première tranche s'ouvrant à 0."""
    out, bas = [], 0.0
    for haut, montant in pas:
        out.append((bas, haut, montant))
        bas = haut
    return out


A1990_CONSO = _par_tranches([(1000, 0), (2000, 20), (3000, 30), (4000, 40), (5000, 50),
                             (6000, 60), (7000, 70), (8000, 80), (9000, 90), (10000, 100),
                             (11000, 140), (12000, 180), (13000, 220), (14000, 260),
                             (15000, 300), (16000, 340), (17000, 380), (18000, 420),
                             (19000, 460), (20000, 500)])
A1990_SERVICES = _par_tranches([(1000, 0), (2000, 30), (3000, 45), (4000, 60), (5000, 100),
                                (6000, 150), (7000, 200), (8000, 250), (9000, 300),
                                (10000, 350), (11000, 400), (12000, 450), (13000, 500),
                                (14000, 550), (15000, 600)])
A1990_AUTRES = _par_tranches([(1000, 0), (2000, 10), (4000, 20), (6000, 30), (8000, 60),
                              (10000, 90), (12000, 150), (14000, 220), (16000, 280),
                              (18000, 340), (20000, 400), (22000, 460), (24000, 520),
                              (26000, 580), (28000, 640), (30000, 700)])
# Annexe II de la loi de finances pour 1993 (art. 101) : grille unique, dix tranches de 3 000 D.
A1993 = _par_tranches([(3000, 15), (6000, 45), (9000, 75), (12000, 120), (15000, 180),
                       (18000, 260), (21000, 360), (24000, 460), (27000, 580), (30000, 700)])
# Loi de finances pour 2006 (art. 44) : première tranche relevée de 15 à 25 D.
A2006 = [(0.0, 3000.0, 25.0)] + A1993[1:]

T_1990 = ("Code de l'IRPP et de l'IS annexé à la loi n° 89-114 du 30 décembre 1989, JORT n° 1 "
          "des 2-5 janvier 1990, art. 44 § IV (p. 9) et annexe II (p. 18)")
T_1993 = ("Loi n° 92-122 du 29 décembre 1992 portant loi de finances pour 1993, JORT n° 88 du "
          "31 décembre 1992, art. 101 et 102 (pp. 1676-1677)")
T_1999 = ("Loi n° 98-111 du 28 décembre 1998 portant loi de finances pour 1999, JORT n° 104 des "
          "29-31 décembre 1998, art. 59 à 61 (pp. 2507-2508) ; grille de l'annexe II de la loi "
          "de finances pour 1993, art. 101")
T_1999_OPTION = ("Loi n° 98-111 du 28 décembre 1998 portant loi de finances pour 1999, JORT "
                 "n° 104 des 29-31 décembre 1998, art. 61 (pp. 2507-2508) : impôt forfaitaire "
                 "annuel de 1 500 D, relevé seulement au-delà de 100 000 D de chiffre d'affaires")
T_2006 = ("Loi n° 2005-106 du 19 décembre 2005 portant loi de finances pour 2006, JORT n° 101 "
          "du 20 décembre 2005, art. 44 (p. 3602) ; autres tranches de l'annexe II inchangées")
T_2011 = ("Loi n° 2010-58 du 17 décembre 2010 portant loi de finances pour 2011, JORT n° 102 du "
          "21 décembre 2010, art. 32 (pp. 3471-3472), art. 44 ter")
T_2014 = ("Loi n° 2013-54 du 30 décembre 2013 portant loi de finances pour 2014, JORT n° 105 du "
          "31 décembre 2013, art. 45 (p. 3678), art. 44 ter")
T_2016 = ("Loi n° 2015-53 du 25 décembre 2015 portant loi de finances pour 2016, JORT n° 104 du "
          "29 décembre 2015, art. 17 (p. 3141), art. 44 ter")
T_2018 = ("Loi n° 2017-66 du 18 décembre 2017 portant loi de finances pour 2018, JORT n° 101 du "
          "19 décembre 2017, art. 16 (p. 4271), art. 44 ter")
T_2023 = ("Décret-loi n° 2022-79 du 22 décembre 2022 portant loi de finances pour 2023, JORT "
          "n° 141 du 23 décembre 2022, art. 55 (p. 4073, édition arabe), art. 44 ter")
T_2026 = ("Loi n° 2025-17 du 12 décembre 2025 portant loi de finances pour 2026, JORT n° 148 du "
          "12 décembre 2025, art. 91 (p. 4255, édition arabe), art. 44 ter ; effet : art. 110")

CLE = {1990: "code-irpp-is-1990", 1993: "lf-1993", 1999: "lf-1999", 2006: "lf-2006",
       2011: "lf-2011", 2014: "lf-2014", 2016: "lf-2016", 2018: "lf-2018", 2023: "lf-2023",
       2026: "lf-2026"}


def _lignes_tarifs() -> list[dict]:
    L: list[dict] = []

    def grille(etat, regime, activite, zone, tranches, texte, cle, plafond_services=None):
        for bas, haut, montant in tranches:
            L.append(dict(etat=etat, regime=regime, activite=activite, zone=zone, bas=bas,
                          haut=haut, montant=montant, taux=None, plancher=None,
                          plafond_services=plafond_services, texte=texte, cle=cle))

    def taux_plancher(etat, activite, zone, taux, plancher, haut, texte, cle,
                      plafond_services=None):
        L.append(dict(etat=etat, regime="forfait", activite=activite, zone=zone, bas=0.0,
                      haut=haut, montant=None, taux=taux, plancher=plancher,
                      plafond_services=plafond_services, texte=texte, cle=cle))

    def fixe_puis_taux(etat, zone, fixe, texte, cle):
        L.append(dict(etat=etat, regime="forfait", activite="toutes", zone=zone, bas=0.0,
                      haut=10_000.0, montant=fixe, taux=None, plancher=None,
                      plafond_services=None, texte=texte, cle=cle))
        L.append(dict(etat=etat, regime="forfait", activite="toutes", zone=zone, bas=10_000.0,
                      haut=100_000.0, montant=None, taux=0.03, plancher=None,
                      plafond_services=None, texte=texte, cle=cle))

    def option_fixe(etat, zone, montant_bas, montant_haut, texte, cle):
        L.append(dict(etat=etat, regime="option", activite="toutes", zone=zone, bas=0.0,
                      haut=50_000.0, montant=montant_bas, taux=None, plancher=None,
                      plafond_services=None, texte=texte, cle=cle))
        L.append(dict(etat=etat, regime="option", activite="toutes", zone=zone, bas=50_000.0,
                      haut=100_000.0, montant=montant_haut, taux=None, plancher=None,
                      plafond_services=None, texte=texte, cle=cle))

    # 1990 : trois colonnes de l'annexe II, plafonds de 20 000, 15 000 et 30 000 D.
    grille(1990, "forfait", "conso", "", A1990_CONSO, T_1990, CLE[1990])
    grille(1990, "forfait", "services", "", A1990_SERVICES, T_1990, CLE[1990])
    grille(1990, "forfait", "achat_transfo", "", A1990_AUTRES, T_1990, CLE[1990])
    # 1993 : grille unique ; plafond de 12 000 D pour les services, 30 000 D pour les autres.
    grille(1993, "forfait", "toutes", "", A1993, T_1993, CLE[1993], plafond_services=12_000.0)
    # 1999 : plafond unique de 30 000 D ; option à 1 500 D.
    grille(1999, "forfait", "toutes", "", A1993, T_1999, CLE[1999])
    L.append(dict(etat=1999, regime="option", activite="toutes", zone="", bas=0.0,
                  haut=100_000.0, montant=1500.0, taux=None, plancher=None,
                  plafond_services=None, texte=T_1999_OPTION, cle=CLE[1999]))
    # 2006 : première tranche à 25 D ; option à 1 500 D inchangée.
    grille(2006, "forfait", "toutes", "", A2006, T_2006, CLE[2006])
    L.append(dict(etat=2006, regime="option", activite="toutes", zone="", bas=0.0,
                  haut=100_000.0, montant=1500.0, taux=None, plancher=None,
                  plafond_services=None, texte=T_1999_OPTION, cle=CLE[1999]))
    # 2011 : 2 % (achat-revente, transformation) ou 2,5 % (autres), plancher selon la zone.
    for etat, (hors, communale), texte in ((2011, (50.0, 100.0), T_2011),
                                          (2014, (75.0, 150.0), T_2014)):
        for zone, plancher in (("hors_communale", hors), ("communale", communale)):
            taux_plancher(etat, "achat_transfo", zone, 0.02, plancher, 100_000.0, texte,
                          CLE[etat])
            taux_plancher(etat, "autres", zone, 0.025, plancher, 100_000.0, texte, CLE[etat],
                          plafond_services=50_000.0)
    # 2016, 2018, 2023 : montant fixe jusqu'à 10 000 D, 3 % au-delà, plafond de 100 000 D.
    for etat, (hors, communale), texte in ((2016, (75.0, 150.0), T_2016),
                                          (2018, (100.0, 200.0), T_2018),
                                          (2023, (200.0, 400.0), T_2023)):
        fixe_puis_taux(etat, "hors_communale", hors, texte, CLE[etat])
        fixe_puis_taux(etat, "communale", communale, texte, CLE[etat])
    # 2026 : tarif de 2023 inchangé ; option à 4 000 / 5 000 D, moitié dans les campagnes.
    fixe_puis_taux(2026, "hors_communale", 200.0, T_2023, CLE[2023])
    fixe_puis_taux(2026, "communale", 400.0, T_2023, CLE[2023])
    option_fixe(2026, "", 4000.0, 5000.0, T_2026, CLE[2026])
    option_fixe(2026, "campagnes", 2000.0, 2500.0, T_2026, CLE[2026])
    return L


MINIMUM = [
    # (année d'effet, forme, taux, montant, texte, clé)
    (1990, "plafonne", 0.005, 500.0,
     "Code de l'IRPP et de l'IS annexé à la loi n° 89-114, JORT n° 1 des 2-5 janvier 1990, "
     "art. 44 § II (p. 9) : 0,5 % du chiffre d'affaires brut, sans excéder 500 D",
     "code-irpp-is-1990"),
    (1998, "plafonne", 0.005, 1000.0,
     "Loi n° 97-88 du 29 décembre 1997 portant loi de finances pour 1998, JORT n° 104 des "
     "30-31 décembre 1997, art. 45 (p. 2435) : plafond relevé à 1 000 D", "lf-1998"),
    (2006, "plancher", 0.001, 100.0,
     "Loi n° 2005-106 du 19 décembre 2005 portant loi de finances pour 2006, JORT n° 101 du "
     "20 décembre 2005, art. 42 : 0,1 % du chiffre d'affaires brut, au moins 100 D", "lf-2006"),
    (2011, "plancher", 0.001, 200.0,
     "Loi n° 2010-58 du 17 décembre 2010 portant loi de finances pour 2011, JORT n° 102 du "
     "21 décembre 2010, art. 38 : plancher relevé à 200 D", "lf-2011"),
    (2014, "plancher", 0.002, 300.0,
     "Loi n° 2013-54 du 30 décembre 2013 portant loi de finances pour 2014, JORT n° 105 du "
     "31 décembre 2013, art. 48 : 0,2 % du chiffre d'affaires local, au moins 300 D", "lf-2014"),
]

HYPOTHESES = [
    # (taux de bénéfice, texte, clé)
    (0.25, "Loi n° 2025-17 du 12 décembre 2025 portant loi de finances pour 2026, art. 91 "
           "(p. 4255, édition arabe) : taux de bénéfice net estimé de l'option, au plus 25 % du "
           "chiffre d'affaires déclaré", "lf-2026"),
    (0.10, "Hypothèse de lecture, sans texte : un bénéfice égal à 10 % du chiffre d'affaires", ""),
]


def main() -> int:
    urls = _urls()
    CACHE.mkdir(parents=True, exist_ok=True)

    def lien(cle: str) -> str:
        return urls.get(cle, "")

    tarifs = pd.DataFrame(_lignes_tarifs())
    tarifs["lien"] = tarifs["cle"].map(lien)
    tarifs = tarifs.drop(columns="cle")
    tarifs.to_csv(CACHE / f"{SERIE_TARIFS}.csv", index=False)

    mini = pd.DataFrame([dict(annee_effet=a, forme=f, taux=t, montant=m, texte=x, lien=lien(c))
                         for a, f, t, m, x, c in MINIMUM])
    mini.to_csv(CACHE / f"{SERIE_MINIMUM}.csv", index=False)

    hyp = pd.DataFrame([dict(taux_benefice=t, texte=x, lien=lien(c)) for t, x, c in HYPOTHESES])
    hyp.to_csv(CACHE / f"{SERIE_HYPOTHESES}.csv", index=False)
    print(f"{len(tarifs)} morceaux de tarif, {len(mini)} minima, {len(hyp)} hypothèses")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

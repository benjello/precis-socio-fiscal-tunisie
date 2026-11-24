"""Comprendre les résidus du compte reconstruit des administrations publiques (pilote S13).

Pour chaque opération chiffrée du pilote, le script teste une à une les explications possibles de
l'écart entre la valeur de l'INS et la somme des postes, sans rien corriger : périmètre (S13
consolidé ou administration centrale S1311, apport des collectivités locales et de la sécurité
sociale), moment d'enregistrement (signe de l'écart sur 2015-2023), classement (rapport stable,
transferts en capital), source du budget (nature de la série pour l'année de référence). Chaque
explication reçoit un statut : « établi » (mesuré par un chiffre sourcé), « plausible » (non
chiffré, ou chiffres seulement compatibles) ou « écarté ». Aucune cause n'est affirmée sans chiffre.

Chaque année est lue dans la dernière édition des comptes de la nation qui la publie.
Sorties : precis/fr/compte-apu-residus.csv (tests) et compte-apu-residus-series.csv (écarts
année par année, 2015-2023).

    uv run python scripts/expliquer_residus.py [--verifier]
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import pandas as pd

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "precis" / "_seriescache"
SORTIE = RACINE / "precis" / "fr" / "compte-apu-residus.csv"
SERIES = RACINE / "precis" / "fr" / "compte-apu-residus-series.csv"
FRAGMENTS = RACINE / "precis" / "fr" / "encadres-comptes"
AN = 2023
ANNEES = list(range(2015, AN + 1))
INS, RF, DEP, DETTE, BCT = "ins-cnat-2015", "minfin-recettes-fiscales", "minfin-repartition-depenses-xls", \
    "minfin-service-dette-xls", "bct-ra-2024"


def fr(v: float, d: int = 1) -> str:
    return f"{v:,.{d}f}".replace(",", " ").replace(".", ",")


def charger():
    s = pd.read_csv(CACHE / "cnat-secteurs.csv")
    s = s[s.base == 2015]

    def v(secteur, cote, op):
        x = s[(s.secteur == secteur) & (s.cote == cote) & (s.operation == op)].sort_values("edition")
        return x.groupby("annee").last().valeur

    r = pd.read_csv(CACHE / "recettes-fiscales-composition.csv").set_index("annee")
    b = pd.read_csv(CACHE / "budget-desagregation-nature.csv").set_index("annee")
    d = pd.read_csv(CACHE / "budget-service-dette.csv").set_index("annee")
    c = pd.read_csv(CACHE / "compensation-parts.csv")
    c23 = c[(c.famille == "budget") & (c.poste == "total") & (c.annee == AN)]
    c = c[(c.famille == "budget") & (c.poste == "total")].set_index("annee").valeur_MDT
    return v, r, b, d, c, c23


def signes(e: pd.Series) -> tuple[int, int]:
    """(années à écart positif, changements de signe) sur 2015-AN. Un décalage dans le temps n'est
    retenu comme plausible que si chaque signe revient au moins deux fois."""
    x = e.loc[[a for a in ANNEES if a in e.index]]
    sg = (x > 0).astype(int)
    return int(sg.sum()), int((sg.diff().abs() == 1).sum())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", action="store_true")
    a = ap.parse_args()
    v, r, b, d, c, c23 = charger()
    ops = {  # opération : (libellé, côté, série budgétaire, clé de source du budget)
        "tva": ("D.211 TVA", "ressources", r.tva_MDT, RF),
        "impots_importations": ("D.212 droits et taxes sur les importations", "ressources", r.douanes_MDT, RF),
        "autres_impots_produits": ("D.214 autres impôts sur les produits", "ressources", r.consommation_MDT, RF),
        "impots_production_importations": ("D.2 impôts sur la production et les importations", "ressources",
                                           r[["tva_MDT", "douanes_MDT", "consommation_MDT", "autres_indirects_MDT"]].sum(axis=1), RF),
        "impots_courants": ("D.5 impôts courants sur le revenu", "ressources", r.irpp_MDT + r.is_MDT, RF),
        "remuneration_salaries": ("D.1 rémunération des salariés", "emplois", b.remunerations_MDT, DEP),
        "interets": ("D.41 intérêts", "emplois", d.interets_MDT, DETTE),
        "subventions_produits": ("D.31 subventions sur les produits", "ressources", c, BCT),
        "fbcf": ("P.51g formation brute de capital fixe", "emplois", b.equipement_MDT, DEP),
    }
    series, tests = [], []

    def test(op, hypothese, explication, statut, chiffre, source):
        tests.append({"operation": op, "libelle": ops[op][0], "hypothese": hypothese, "explication": explication,
                      "statut": statut, "chiffre_md": "" if chiffre is None else round(chiffre, 1), "source": source})

    for op, (_, cote, budget, src) in ops.items():
        ins13 = v("apu", cote, op)
        ins11 = v("apu_centrale", cote, op)
        signe = -1 if op == "subventions_produits" else 1  # les subventions sont imprimées en négatif
        for sec, ins in (("S13", ins13), ("S1311", ins11)):
            for an in ANNEES:
                if an in ins.index and an in budget.index and pd.notna(budget.get(an)):
                    x, y = signe * ins[an], budget[an]
                    series.append({"operation": op, "secteur": sec, "annee": an, "ins_md": round(x, 1),
                                   "postes_md": round(y, 1), "ecart_md": round(x - y, 1), "rapport": round(x / y, 3)})
        e13 = signe * ins13[AN] - budget[AN]
        e11 = signe * ins11[AN] - budget[AN]
        autres = signe * (ins13[AN] - ins11[AN])
        # 1. Périmètre
        if abs(autres) < 0.05:
            test(op, "périmètre", f"S13 et S1311 portent la même valeur ({fr(signe * ins13[AN])} MD) : les collectivités "
                 "et la sécurité sociale n'y prennent aucune part.", "écarté", 0.0, INS)
        else:
            loc = v("apu_locale", cote, op).get(AN)
            secu = v("apu_secu", cote, op).get(AN)
            parts = "; ".join(f"{n} {fr(signe * x)} MD" for n, x in (("collectivités locales", loc), ("sécurité sociale", secu))
                              if x is not None and pd.notna(x))
            test(op, "périmètre", f"Les autres sous-secteurs portent {fr(autres)} MD ({parts}) ; face à l'administration "
                 f"centrale (S1311), l'écart est de {fr(e11)} MD au lieu de {fr(e13)} MD.", "établi", autres, INS)
        # 2. Moment d'enregistrement
        e = pd.Series({s_["annee"]: s_["ecart_md"] for s_ in series if s_["operation"] == op and s_["secteur"] == "S1311"})
        pos, chg = signes(e)
        n = len(e)
        if min(pos, n - pos) >= 2:
            test(op, "moment d'enregistrement", f"Face à S1311, l'écart change {chg} fois de signe sur {n} ans ({pos} positifs), "
                 f"de {fr(e.min())} à {fr(e.max())} MD : profil d'un décalage entre encaissement ou paiement et droits "
                 "constatés, que les séries présentes ne mesurent pas.", "plausible", None, f"{INS} ; {src}")
        else:
            test(op, "moment d'enregistrement", f"Face à S1311, l'écart garde le même signe {max(pos, n - pos)} années sur {n} "
                 f"(de {fr(e.min())} à {fr(e.max())} MD) : un décalage dans le temps s'annulerait d'une année à l'autre ; "
                 "le profil désigne plutôt un périmètre ou un classement.", "écarté", None, f"{INS} ; {src}")
        # 3. Source du budget
        if op == "subventions_produits":
            etat = c23.etat.iloc[0]
            test(op, "source du budget", f"La compensation de {AN} ({fr(budget[AN])} MD) est lue dans le rapport annuel 2024 "
                 f"de la BCT, {etat} : rien n'établit qu'il s'agit de l'exécution définitive.", "plausible", None, BCT)
        else:
            test(op, "source du budget", f"La série budgétaire de {AN} est une série de réalisations du ministère des Finances, "
                 "pas une prévision de loi de finances.", "écarté", None, src)
    # 4. Classement : tests propres à certaines opérations
    e = pd.Series({s_["annee"]: s_["rapport"] for s_ in series if s_["operation"] == "impots_importations" and s_["secteur"] == "S13"})
    test("impots_importations", "classement", f"Le rapport entre D.212 et les droits de douane reste entre {fr(e.min(), 2)} et "
         f"{fr(e.max(), 2)} sur 2015-{AN} : stabilité d'une différence de définition (D.212 couvrirait des taxes à "
         "l'importation que le budget range ailleurs) ; la ventilation des recettes douanières par nature trancherait.",
         "plausible", None, f"{INS} ; {RF}")
    e = pd.Series({s_["annee"]: s_["rapport"] for s_ in series if s_["operation"] == "autres_impots_produits" and s_["secteur"] == "S13"})
    test("autres_impots_produits", "classement", f"Le rapport entre D.214 et les droits de consommation va de {fr(e.min(), 2)} à "
         f"{fr(e.max(), 2)} : D.214 réunit d'autres impôts sur les produits que le budget classe dans d'autres rubriques.",
         "plausible", None, f"{INS} ; {RF}")
    test("impots_production_importations", "classement", "La rubrique budgétaire « autres impôts indirects » réunit, selon "
         "la série, fonds spéciaux du Trésor, fonds de concours et reliquat : des recettes que les comptes ne rangent pas "
         "nécessairement parmi les impôts ; la série ne les sépare pas.", "plausible", None, RF)
    test("interets", "classement", "La ligne « intérêts » des comptes précède la correction SIFIM, imprimée à part "
         f"({fr(v('apu_centrale', 'emplois', 'correction_sifim')[AN])} MD pour S1311) : le SIFIM n'entre pas dans l'écart.",
         "écarté", None, INS)
    fb = v("apu_centrale", "emplois", "fbcf")
    d9 = v("apu_centrale", "emplois", "transferts_capital")
    rap = {an: (fb[an] + d9[an]) / b.equipement_MDT[an] for an in ANNEES}
    avant = [rap[a] for a in ANNEES if a <= 2020]
    apres = [rap[a] for a in ANNEES if a > 2020]
    test("fbcf", "classement", f"Les transferts en capital versés par S1311 (D.9) valent {fr(d9[AN])} MD en {AN} ; FBCF plus D.9 "
         f"couvrent {fr(100 * rap[AN], 1)} % des dépenses d'équipement (reste {fr(b.equipement_MDT[AN] - fb[AN] - d9[AN])} MD). "
         f"Ce rapport va de {fr(min(avant), 2)} à {fr(max(avant), 2)} en 2015-2020, puis de {fr(min(apres), 2)} à "
         f"{fr(max(apres), 2)} depuis 2021 : compatible avec un équipement qui comprend des subventions d'investissement, "
         "rupture non expliquée depuis 2021.", "plausible", d9[AN], f"{INS} ; {DEP}")
    e = pd.Series({s_["annee"]: s_["rapport"] for s_ in series if s_["operation"] == "fbcf" and s_["secteur"] == "S1311"})
    test("fbcf", "définition (rapport stable)", f"Le rapport entre FBCF et équipement passe de {fr(e.iloc[0], 2)} en 2015 à "
         f"{fr(e.iloc[-1], 2)} en {AN} : il n'est pas stable, une différence de définition seule ne suffit pas.",
         "écarté", None, f"{INS} ; {DEP}")
    # Explications que les séries présentes ne permettent pas de chiffrer ; la source qui trancherait est dite.
    for op, hyp, txt, src in (
        ("tva", "restitutions", "Le budget compte-t-il la TVA nette des restitutions et des remboursements de crédits, "
         "comme les comptes ? La série ne le dit pas ; les recettes brutes et les restitutions trancheraient.", RF),
        ("remuneration_salaries", "classement", "Les comptes peuvent ajouter aux salaires des cotisations imputées (D.122) "
         "que le budget ne paie pas ; les comptes des secteurs n'impriment pas cette ligne à part.", INS),
        ("impots_courants", "classement", "Les retenues à la source et les impôts directs autres que l'IRPP et l'IS (impôts "
         "sur le patrimoine) peuvent être rangés différemment ; la série budgétaire ne les isole pas.", RF),
        ("subventions_produits", "classement", "D.31 peut comprendre des subventions sur les produits autres que la "
         "compensation (transferts aux entreprises publiques), et la compensation des transferts que les comptes "
         "rangent ailleurs (D.39, D.9) ; les comptes des caisses et des entreprises publiques trancheraient.", INS),
    ):
        test(op, hyp, txt, "plausible", None, src)
    tests.sort(key=lambda t: list(ops).index(t["operation"]))
    if a.verifier:
        for p, rows in ((SORTIE, tests), (SERIES, series)):
            with p.open(encoding="utf-8") as f:
                if [dict(x) for x in csv.DictReader(f)] != [{k: str(x) for k, x in row.items()} for row in rows]:
                    print(f"{p.name} n'est pas à jour : relancer scripts/expliquer_residus.py")
                    return 1
        return 0
    passages = {}
    for t in tests:  # un fragment par opération, inclus dans le bloc « passage » de la section domicile
        passages.setdefault(t["operation"], [f"Les explications testées de l'écart de {AN} pour {t['libelle']}, "
                                             "établies, plausibles ou écartées :", ""])
        passages[t["operation"]].append(f"- **{t['hypothese']}** ({t['statut']}) : {t['explication']}")
    for op, ls in passages.items():
        ls += ["", "Le tableau complet, avec les sources, est dans [le compte reconstruit](../compte-apu.html#sec-capu-residus)."]
        (FRAGMENTS / f"passage-{op}.md").write_text("\n".join(ls) + "\n", encoding="utf-8")
    for p, rows in ((SORTIE, tests), (SERIES, series)):
        with p.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
    print(f"{len(tests)} tests → {SORTIE.name} ; {len(series)} écarts annuels → {SERIES.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

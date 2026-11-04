"""Étape 5 du plan docs/notes/plan-cas-bna-consolidation-flux-2026-11-04.md.

Confronte les engagements de la BNA envers six entreprises publiques (listes/bna-engagements-entreprises-publiques.csv)
au passif de chaque entreprise (fiches du ministère, figdata/fig_ep_<code>_fiches.csv).
Règles : (1) engagement <= passif hors fonds propres (2020-2023) ou <= dette totale (2018-2020) ;
(2) garantie de l'État <= engagement. Les deux mesures du passif ne sont pas comparables entre elles.
Usage : python scripts/bna_recoupement_debiteurs.py
"""
import csv, collections
from pathlib import Path
V = Path(__file__).resolve().parent.parent / "precis" / "fr" / "entreprises_publiques"
CODE = {"Office des céréales": "oc", "ETAP": "etap", "Transtu": "transtu", "O.T.D": "otd", "O.N.H": "onh", "El Fouledh": "fouladh"}
eng = list(csv.DictReader(open(V / "listes/bna-engagements-entreprises-publiques.csv", encoding="utf-8")))
def fiche(c):
    r = [x for x in csv.reader(open(V / f"figdata/fig_ep_{c}_fiches.csv", encoding="utf-8")) if x and not x[0].startswith("#")]
    h = r[0]; g = collections.defaultdict(dict)
    for x in r[1:]:
        d = dict(zip(h, x)); g[d["Grandeur"]][d["Exercice"]] = d["Valeur"]
    return g
def num(v):
    try: return float(v)
    except (TypeError, ValueError): return None
for ent, c in CODE.items():
    g = fiche(c); print("\n" + ent)
    for yr in map(str, range(2018, 2024)):
        d = {x["grandeur"]: x["valeur_kdt"] for x in eng if x["entite"] == ent and x["exercice"] == yr}
        E = num(d.get("engagements")); G = num(d.get("garanties de l'État"))
        if E is None: continue
        E /= 1000; G = G / 1000 if G is not None else None
        P = num(g["Total des passifs, hors fonds propres"].get(yr)); D = num(g["Dette totale"].get(yr))
        txt = f"  {yr}: engagements BNA {E:8.1f} MD"
        if G is not None: txt += f" ; garantie de l'État {G:8.1f} ({G / E:4.0%}){'  GARANTIE > ENGAGEMENT' if G > E + 0.05 else ''}"
        if P: txt += f" ; passifs {P:8.1f} ({E / P:4.0%}){'  DÉPASSE' if E > P else ''}"
        if D: txt += f" ; dette totale {D:8.1f} ({E / D:4.0%}){'  DÉPASSE' if E > D else ''}"
        print(txt)

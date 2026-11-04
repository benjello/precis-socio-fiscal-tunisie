"""Années où la fiche du ministère n'a pas de valeur pour le passif des six entreprises débitrices de la BNA.

Plan : docs/notes/plan-cas-bna-consolidation-flux-2026-11-04.md, étape 5. « Dette totale » (2018-2020) et
« Total des passifs, hors fonds propres » (2020-2023) sont deux mesures différentes. Un « . » est une valeur absente
ou vide dans la fiche, non un zéro. Usage : python scripts/lacunes_fiches_debiteurs.py
"""
import csv, collections
from pathlib import Path
V = Path(__file__).resolve().parent.parent / "precis" / "fr" / "entreprises_publiques"
CODE = {"Office des céréales": "oc", "ETAP": "etap", "Transtu": "transtu", "O.T.D": "otd", "O.N.H": "onh", "El Fouladh": "fouladh"}
GRANDEURS = ["Dette totale", "Total des passifs, hors fonds propres", "dont emprunts à plus d'un an", "Total des actifs"]
ANNEES = [str(a) for a in range(2018, 2024)]

def fiche(code):
    r = [x for x in csv.reader(open(V / f"figdata/fig_ep_{code}_fiches.csv", encoding="utf-8")) if x and not x[0].startswith("#")]
    h = r[0]; g = collections.defaultdict(dict)
    for x in r[1:]:
        d = dict(zip(h, x))
        if d["Valeur"] != "": g[d["Grandeur"]][d["Exercice"]] = d["Valeur"]
    return g

if __name__ == "__main__":
    for ent, code in CODE.items():
        g = fiche(code); print(f"\n{ent}")
        print(f"  {'':44}" + " ".join(a[2:] for a in ANNEES))
        for gr in GRANDEURS:
            print(f"  {gr[:44]:44}" + " ".join(("x" if a in g[gr] else ".").center(2) for a in ANNEES))

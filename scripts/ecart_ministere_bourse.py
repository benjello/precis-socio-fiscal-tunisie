"""Écart entre le résultat net de la fiche du ministère des Finances et celui de la Bourse de Tunis.

Plan : docs/notes/plan-cas-bna-consolidation-flux-2026-11-04.md, étape 1. Lit
precis/fr/entreprises_publiques/figdata/fig_ep_<code>_fiches.csv et listes/societes-cotees-resultats.csv.
Les deux séries ne disent pas leur base (individuelle ou consolidée) : l'écart est un constat, non une erreur.
Usage : python scripts/ecart_ministere_bourse.py
"""
import csv
from pathlib import Path
V = Path(__file__).resolve().parent.parent / "precis" / "fr" / "entreprises_publiques"
CODE = {"STB": "stb", "BNA": "bna", "BH": "bh", "Tunisair": "tunisair", "Ciments de Bizerte": "cimbiz"}

def ministere(code):
    r = [x for x in csv.reader(open(V / f"figdata/fig_ep_{code}_fiches.csv", encoding="utf-8")) if x and not x[0].startswith("#")]
    h = r[0]; out = {}
    for x in r[1:]:
        d = dict(zip(h, x))
        if d["Grandeur"].startswith("Résultat net") and d["Valeur"] not in ("",):
            out.setdefault(d["Exercice"], set()).add((d["Édition"], float(d["Valeur"])))
    return out

def bourse():
    out = {}
    for x in csv.DictReader(open(V / "listes/societes-cotees-resultats.csv", encoding="utf-8")):
        if x["resultat_net_dt"]: out[(x["societe"], x["exercice"])] = float(x["resultat_net_dt"]) / 1e6
    return out

def lignes():
    b = bourse()
    for soc, code in CODE.items():
        m = ministere(code)
        for (s, ex), vb in sorted(b.items()):
            if s != soc or ex not in m: continue
            for ed, vm in sorted(m[ex]):
                yield soc, ex, ed, vm, vb, vm - vb

if __name__ == "__main__":
    print(f"{'société':20} {'ex.':5} {'édition':8} {'ministère':>10} {'Bourse':>10} {'écart':>9} {'écart %':>8}")
    for soc, ex, ed, vm, vb, e in lignes():
        print(f"{soc:20} {ex:5} {ed:8} {vm:10.1f} {vb:10.1f} {e:9.1f} {100 * e / abs(vb):7.1f}%")

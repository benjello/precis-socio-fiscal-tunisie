"""Contrôles de somme sur les liens entre sociétés cotées et détenteurs publics nommés.

Lit precis/fr/entreprises_publiques/listes/societes-cotees-participations.csv et
societes-cotees-resultats.csv. Règles : A (cohérence du nombre total d'actions),
B (somme des parts nommées <= 100 %), D (dividende de l'État = actions x dividende par action),
puis la table des dividendes reçus par les détenteurs publics nommés.
Plan : docs/notes/plan-cas-bna-consolidation-flux-2026-11-04.md. Usage : python scripts/flux_intra_publics_cotees.py
"""
import csv, collections
from pathlib import Path
D = Path(__file__).resolve().parent.parent / "precis" / "fr" / "entreprises_publiques" / "listes"
P=list(csv.DictReader(open(D/'societes-cotees-participations.csv')))
R=list(csv.DictReader(open(D/'societes-cotees-resultats.csv')))
def f(x): return float(x) if x not in ('',None) else None
# --- règle A : nombre total d'actions impliqué par chaque détenteur, par société
print('RÈGLE A — cohérence du nombre total d\'actions (actions / part) entre détenteurs d\'une même société')
by=collections.defaultdict(list)
for p in P: by[p['societe']].append(p)
for s,l in by.items():
    if len(l)<2: continue
    imp=[(p['detenteur'],int(p['actions'])/(float(p['part_pct'])/100)) for p in l]
    lo,hi=min(i for _,i in imp),max(i for _,i in imp)
    # tolérance : la part est arrondie à 0,01 point
    tol=max(0.005/float(p['part_pct']) for p in l)
    ecart=(hi-lo)/lo
    print(f'  {s:10} actions totales impliquées {lo:,.0f} à {hi:,.0f}  écart {ecart:.3%}  tolérance d\'arrondi {tol:.3%}  -> {"OK" if ecart<=tol*1.0 else "A VOIR"}')
# --- règle B : somme des parts nommées
print('\nRÈGLE B — somme des parts nommées (État + détenteurs publics nommés) <= 100 % ; reste sans nom')
for s,l in by.items():
    pub=[p for p in l if p['detenteur'] in('État',)]; 
    tot=sum(float(p['part_pct']) for p in l)
    print(f'  {s:22} nommé {tot:6.2f} %  reste {100-tot:6.2f} %  ({", ".join(p["detenteur"]+" "+p["part_pct"] for p in l)})')
# --- règle D : dividende de l'État = actions de l'État x dividende par action
print('\nRÈGLE D — dividende de l\'État imprimé = actions de l\'État x dividende par action (tolérance 1 DT)')
for r in R:
    if r['dividende_etat_dt'] and r['dividende_par_action_dt']:
        calc=int(r['actions_etat'])*float(r['dividende_par_action_dt']); imp=float(r['dividende_etat_dt'])
        print(f"  {r['societe']:8} {r['exercice']}  calculé {calc:,.0f}  imprimé {imp:,.0f}  écart {calc-imp:,.0f} -> {'OK' if abs(calc-imp)<=1 else 'A VOIR'}")
# --- table des flux : dividende reçu par chaque détenteur public nommé quand la société distribue un dividende par action connu
dpa={}
for r in R:
    if r['dividende_par_action_dt']: dpa[(r['societe'],r['exercice'])]=float(r['dividende_par_action_dt'])
print('\nTABLE — dividende reçu par chaque détenteur public nommé (actions détenues x dividende par action de l\'exercice le plus récent connu)')
rows=[]
for p in P:
    ex=sorted([e for (s,e) in dpa if s==p['societe']])
    if not ex: 
        rows.append((p['detenteur'],p['societe'],p['part_pct'],p['actions'],'-','-','pas de dividende par action au dépôt')); continue
    e=ex[-1]; rows.append((p['detenteur'],p['societe'],p['part_pct'],p['actions'],e,f"{int(p['actions'])*dpa[(p['societe'],e)]/1e6:.3f}",''))
for r in rows: print('  ',' | '.join(str(x) for x in r))

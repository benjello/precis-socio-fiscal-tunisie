"""Repère les phrases quasi identiques entre les consignes aux agents (AGENTS.md, docs/conventions,
docs/agents, conventions-redaction, backlog-routage). Usage : uv run python scripts/consignes_doublons.py
Une règle se détaille à un seul endroit ; ailleurs, un renvoi d'une ligne."""
import re, sys, itertools
from pathlib import Path
from difflib import SequenceMatcher
files=[Path("AGENTS.md"),Path("docs/conventions-redaction.md"),Path("docs/backlog-routage.md")]+sorted(Path("docs/conventions").glob("*.md"))+sorted(Path("docs/agents").glob("*.md"))
def phrases(p):
    t=p.read_text()
    t=re.sub(r"```.*?```","",t,flags=re.S)
    paras=[re.sub(r"\s+"," ",x).strip() for x in re.split(r"\n\s*\n|\n- ",t)]
    out=[]
    for para in paras:
        for s in re.split(r"(?<=[.;:])\s+(?=[A-ZÀ-ÖØ-Ý«*`])",para):
            s=s.strip()
            if len(s)>70: out.append(s)
    return out
P={f:phrases(f) for f in files}
norm=lambda s: re.sub(r"[^a-zà-ÿ0-9 ]","",s.lower())
hits=[]
for a,b in itertools.combinations(files,2):
    for sa in P[a]:
        na=norm(sa)
        for sb in P[b]:
            nb=norm(sb)
            if abs(len(na)-len(nb))>0.5*max(len(na),len(nb)): continue
            r=SequenceMatcher(None,na,nb).ratio()
            if r>0.72: hits.append((r,str(a),str(b),sa[:150],sb[:150]))
hits.sort(reverse=True)
for h in hits: print(f"{h[0]:.2f} | {h[1]} <-> {h[2]}\n   A: {h[3]}\n   B: {h[4]}")
print(len(hits),"paires")

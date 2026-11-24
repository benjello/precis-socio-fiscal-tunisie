"""Index des sections « Ce qu'en dit l'économie » des volumes, construit au rendu.

L'état de l'art vit dans chaque volume, au plus près du dispositif ; la synthèse n'en donne que
l'index. La liste est relue à chaque rendu dans les `.qmd` français des volumes : une section
ajoutée dans un volume paraît ici sans autre écriture.
"""
from __future__ import annotations

import re
from pathlib import Path

FR = Path(__file__).resolve().parents[2]
TITRE = re.compile(r"^#{2,4} Ce qu'en dit l'économie \{#([\w-]+)")
CHAPITRE = re.compile(r"^# (.*?) \{#")


def sections():
    out = []
    for qmd in sorted(FR.glob("*/_*.qmd")):
        livre = qmd.parent.name
        if livre in ("synthese",) or not (qmd.parent / "_quarto.yml").exists():
            continue
        titre_livre = re.search(r'^\s*title: "(.*)"', (qmd.parent / "_quarto.yml").read_text(encoding="utf-8"), re.M)
        chap = None
        for l in qmd.read_text(encoding="utf-8").splitlines():
            m = CHAPITRE.match(l)
            if m and chap is None:
                chap = m.group(1)
            m = TITRE.match(l)
            if m:
                out.append((titre_livre.group(1) if titre_livre else livre, chap or qmd.stem, livre, qmd.stem, m.group(1)))
    return out


def tableau() -> str:
    lignes = ["| Volume | Chapitre | Section |", "|---|---|---|"]
    for titre_livre, chap, livre, stem, ancre in sections():
        lignes.append(f"| {titre_livre} | {chap} | [Ce qu'en dit l'économie](../{livre}/{stem}.html#{ancre}) |")
    return "\n".join(lignes) + "\n\n: Les sections « Ce qu'en dit l'économie » des volumes {#tbl-synthese-etat-art}\n"

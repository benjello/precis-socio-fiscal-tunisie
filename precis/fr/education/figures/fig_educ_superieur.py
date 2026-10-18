"""Figure du chapitre « L'enseignement supérieur » : la contribution des étudiants.

Les données sont le figdata `figdata/fig_educ_superieur_montants.csv` du livre, écrit par
`fig_educ_superieur_montants.py` ; ce module le lit et ne le réécrit jamais. Un barème contient
plusieurs montants (cycles en 1995, groupes de disciplines en 1997, domaines en 2016) : la barre
va du plus bas au plus haut montant du niveau d'études, et ne dit rien de la répartition des
étudiants entre eux. Les barèmes ne forment pas une série : trois dates, pas de courbe.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from figures import fig_educ_scolaire as fs
import figtools

SLUG = "fig_educ_superieur_montants"
PREMIER = {"premier cycle", "licence"}
TROISIEME = {"troisième cycle", "DEA et doctorat", "DESS", "mastère", "doctorat"}
BLEU, ORANGE = "#08519c", "#b45100"
DATES = {1995: "1995", 1997: "1997-1998", 2016: "2016"}


def _bornes() -> pd.DataFrame:
    d = fs.lire(SLUG)
    d = d[d["tableau"] == "contribution"]
    d = d[~d["categorie"].isin(["inscription exceptionnelle", "concours de réorientation"])]
    lignes = []
    for bareme, g in d.groupby("bareme"):
        for nom, niveaux in (("Premier cycle ou licence", PREMIER),
                             ("Troisième cycle, mastère ou doctorat", TROISIEME)):
            s = g[g["niveau"].isin(niveaux)]
            lignes.append({"bareme": int(bareme), "niveau": nom,
                           "c_min": s["montant_courant"].min(), "c_max": s["montant_courant"].max(),
                           "k_min": s["montant_dinars_2023"].min(), "k_max": s["montant_dinars_2023"].max()})
    return pd.DataFrame(lignes)


def vues():
    figtools.apply_lang_font()
    b = _bornes()
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.2), sharex=True)
    for ax, (pre, titre) in zip(axes, (("c", "Dinars courants"), ("k", "Dinars de 2023"))):
        for dec, (niveau, couleur) in enumerate((("Premier cycle ou licence", BLEU),
                                                 ("Troisième cycle, mastère ou doctorat", ORANGE))):
            for i, bar in enumerate(sorted(b["bareme"].unique())):
                r = b[(b["bareme"] == bar) & (b["niveau"] == niveau)].iloc[0]
                lo, hi = float(r[f"{pre}_min"]), float(r[f"{pre}_max"])
                x = i + (dec - 0.5) * 0.36
                h = max(hi - lo, 0.04 * max(hi, 1))
                art = ax.bar(x, h, bottom=lo, width=0.32, color=couleur,
                             label=figtools.fig_text(niveau) if i == 0 else None)[0]
                txt = (f"{_f(lo)}" if lo == hi else f"{_f(lo)} à {_f(hi)}")
                figtools.infobulle(art, f"{DATES[bar]} · {niveau} : {txt} D"
                                        + (" de 2023" if pre == "k" else " courants"))
        ax.set_xticks(range(3))
        ax.set_xticklabels([DATES[x] for x in sorted(b["bareme"].unique())])
        ax.set_title(figtools.fig_text(titre), fontsize=10)
        ax.set_ylim(bottom=0)
        ax.set_axisbelow(True)
        ax.grid(axis="y", color="#d7dce2", lw=0.8)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel(figtools.fig_text("D par an"))
    fig.legend(*axes[0].get_legend_handles_labels(), frameon=False, fontsize=8, ncol=2,
               loc="lower center")
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    return [(None, fig)]


def _f(v: float) -> str:
    return f"{v:,.1f}".replace(",", " ").replace(".", ",").replace(",0", "")

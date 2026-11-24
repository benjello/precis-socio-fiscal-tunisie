"""Figures du livre *L'investissement*.

    from figures import investissement as inv
    inv.vues_fbcf() ; inv.table_fbcf()

Série `cnat-fbcf` (tunisia-data), tableau « FBCF par secteur institutionnel » des comptes de la
nation : quinze éditions, base 1997 (2005-2017) et base 2015 (2015-2025), jamais chaînées ; pour
chaque base et chaque année, l'édition la plus récente qui l'imprime.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SECTEURS = [("societes non financieres", "Sociétés non financières", "#0b4f6c"),
            ("entreprises individuelles", "Entreprises individuelles", "#8250df"),
            ("administration publique", "Administrations publiques", "#bf3989"),
            ("menages ( logement )", "Ménages (logement)", "#c0862b"),
            ("institutions financieres", "Institutions financières", "#2d8c6f")]


def fbcf():
    d = figtools.series("cnat-fbcf")
    d = d[d["famille"] == "secteur_institutionnel"].sort_values("edition").groupby(["base", "annee", "cle"]).tail(1)
    return {base: {lib: {int(r.annee): float(r.valeur_md) for r in g[g["cle"] == cle].itertuples()}
                   for cle, lib, _ in SECTEURS} for base, g in d.groupby("base")}


def _lignes() -> plt.Figure:
    figtools.apply_lang_font()
    f = fbcf()
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    for base, style in (("base 1997", "--"), ("base 2015", "-")):
        for cle, lib, couleur in SECTEURS:
            pts = f.get(base, {}).get(lib, {})
            if pts:
                ans = sorted(pts)
                ax.plot(ans, [pts[a] for a in ans], style, marker="o", ms=2.5, color=couleur,
                        label=figtools.fig_text(lib) if base == "base 2015" else None)
    ax.set_title(figtools.fig_text("FBCF par secteur institutionnel, base 1997 (tirets) et base 2015"), fontsize=10.5)
    ax.set_ylabel(figtools.fig_text("millions de dinars courants"), fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=8)
    ax.legend(fontsize=7.5, framealpha=0.9)
    fig.tight_layout()
    return fig


def vues_fbcf():
    return [("Par secteur", _lignes())]


def table_fbcf():
    import pandas as pd
    f = fbcf()
    return pd.DataFrame([{"Base": b, "Secteur": lib, "Année": a, "FBCF (MD courants)": v}
                         for b, secteurs in f.items() for lib, pts in secteurs.items() for a, v in sorted(pts.items())])

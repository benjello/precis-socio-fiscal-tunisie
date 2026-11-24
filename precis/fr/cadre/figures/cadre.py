"""Figures du livre *Le cadre* — chapitre « La population ».

    from figures import cadre
    cadre.vues_population() ; cadre.table_population()

D'OÙ VIENNENT LES DONNÉES. Série `population-milieu-communal-recensements` du cache : la
population aux recensements de l'INS, une ligne par recensement, grandeur et ÉDITION lue. La
figure retient une seule publication pour tous les points, le Bilan démographique du
recensement de 2024 (tableau « Évolution de la population étrangère à travers les recensements
(1921-2024) », p. 7), qui imprime le total de chaque recensement depuis 1956 en effectifs. Les
autres éditions donnent pour 2004 et 2014 des totaux légèrement différents ; la fiche de la
série les liste, la figure ne les mélange pas.

Le taux de croissance annuel moyen entre deux recensements est calculé ici :
(P2 / P1) ** (1 / n) - 1, n étant l'écart en années entre les deux recensements (les dates de
référence exactes ne sont pas toutes relevées ; l'écart est compté en années civiles).
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "population-milieu-communal-recensements"
EDITION = "rgph2024-bilan"
BLEU, GRIS = "#0b4f6c", "#57606a"


def _nombre(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", "\u202f").replace(".", ",")


def totaux() -> dict[int, float]:
    d = figtools.series(SERIE)
    d = d[(d["edition"] == EDITION) & (d["grandeur"] == "total") & d["valeur_personnes"].notna()]
    return {int(r.recensement): float(r.valeur_personnes) for r in d.itertuples(index=False)}


def croissance() -> dict[int, float]:
    t = totaux()
    a = sorted(t)
    return {a2: 100 * ((t[a2] / t[a1]) ** (1 / (a2 - a1)) - 1) for a1, a2 in zip(a, a[1:])}


def _barres() -> plt.Figure:
    figtools.apply_lang_font()
    t = totaux()
    annees = sorted(t)
    vals = [t[a] / 1e6 for a in annees]
    fig, ax = plt.subplots(figsize=(8.5, 4.4))
    barres = ax.bar([str(a) for a in annees], vals, color=BLEU, width=0.6)
    for a, b, v in zip(annees, barres, vals):
        figtools.infobulle(b, f"{a} · {_nombre(t[a], 0)} habitants")
        ax.annotate(_nombre(v, 2), xy=(b.get_x() + b.get_width() / 2, v), xytext=(0, 3),
                    textcoords="offset points", ha="center", fontsize=7.5, color=GRIS)
    ax.set_title(figtools.fig_text("Population aux recensements"), fontsize=10.5)
    ax.set_ylabel(figtools.fig_text("millions d'habitants"), fontsize=9)
    ax.set_ylim(0, max(vals) * 1.15)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=8)
    fig.tight_layout()
    return fig


def _croissance() -> plt.Figure:
    figtools.apply_lang_font()
    c = croissance()
    a = sorted(c)
    t = sorted(totaux())
    etiquettes = [f"{p}-{s}" for p, s in zip(t, t[1:])]
    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    barres = ax.bar(etiquettes, [c[x] for x in a], color="#2d8c6f", width=0.6)
    for b, x in zip(barres, a):
        ax.annotate(_nombre(c[x], 2), xy=(b.get_x() + b.get_width() / 2, c[x]), xytext=(0, 3),
                    textcoords="offset points", ha="center", fontsize=7.5, color=GRIS)
    ax.set_title(figtools.fig_text("Croissance annuelle moyenne entre deux recensements"), fontsize=10.5)
    ax.set_ylabel(figtools.fig_text("% par an"), fontsize=9)
    ax.set_ylim(0, max(c.values()) * 1.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=8)
    fig.tight_layout()
    return fig


def vues_population():
    return [("Population", _barres()), ("Croissance", _croissance())]


def table_population():
    import pandas as pd
    t, c = totaux(), croissance()
    return pd.DataFrame([{"Recensement": a, "Population (habitants)": int(t[a]),
                          "Croissance annuelle moyenne depuis le recensement précédent (%)":
                              None if a not in c else round(c[a], 2)} for a in sorted(t)])

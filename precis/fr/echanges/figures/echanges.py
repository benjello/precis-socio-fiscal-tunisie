"""Figures du livre *Les échanges extérieurs*.

    from figures import echanges as ech
    ech.vues_echanges() ; ech.table_echanges()

Série `echanges-rapprochement` (tunisia-data) : trois familles de chiffres, jamais fondues —
comptes nationaux de l'INS (biens et services ; biens seuls), statistiques douanières (INS,
Annuaire ; BCT, rapport annuel), balance des paiements de la BCT (MBP6, 2023-2024). Chaque
famille a son périmètre : la balance des paiements compte le travail à façon net, en service ;
la douane et les comptes nationaux l'enregistrent en brut.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

PERIMETRES = [("biens et services", "Comptes nationaux, biens et services", "#0b4f6c", "-"),
              ("biens", "Comptes nationaux, biens", "#2d8c6f", "-"),
              ("biens, douane (FOB / CAF)", "Douane (INS)", "#c0862b", "--"),
              ("biens et services, balance des paiements (MBP6)", "Balance des paiements, biens et services", "#bf3989", ":")]


def donnees():
    d = figtools.series("echanges-rapprochement")
    d = d[~d["source"].str.startswith("BCT, Rapport annuel 2024, tableau 3-2")]  # relais du chiffre douanier de l'INS
    return d


def _vue(flux: str) -> plt.Figure:
    figtools.apply_lang_font()
    d = donnees()
    fig, ax = plt.subplots(figsize=(8.8, 4.6))
    for per, lib, couleur, style in PERIMETRES:
        s = d[(d["flux"] == flux) & (d["perimetre"] == per)].sort_values("annee")
        if len(s):
            ax.plot(s["annee"], s["valeur_md"], style, marker="o", ms=3, color=couleur, label=figtools.fig_text(lib))
    ax.set_title(figtools.fig_text(f"{flux.capitalize()} selon trois familles de chiffres"), fontsize=10.5)
    ax.set_ylabel(figtools.fig_text("millions de dinars courants"), fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=8)
    ax.legend(fontsize=7.5, framealpha=0.9)
    fig.tight_layout()
    return fig


def vues_echanges():
    return [("Exportations", _vue("exportations")), ("Importations", _vue("importations"))]


def table_echanges():
    d = donnees()
    return d[["annee", "flux", "source", "perimetre", "valeur_md", "ecart_pct", "note"]].rename(
        columns={"annee": "Année", "flux": "Flux", "source": "Source", "perimetre": "Périmètre",
                 "valeur_md": "Valeur (MD)", "ecart_pct": "Écart aux comptes nationaux (%)", "note": "Note"})

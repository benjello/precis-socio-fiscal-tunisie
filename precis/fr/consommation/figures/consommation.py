"""Figures du livre *La consommation et les niveaux de vie*.

    from figures import consommation as co
    co.vues_conso() ; co.table_conso()

Série `cnat-produits` (tunisia-data) : tableau « dépense de consommation finale des ménages par
produit » des comptes de la nation, base 2015, aux prix courants ; pour chaque année, l'édition la
plus récente qui l'imprime. CE TABLEAU TOTALISE LA CONSOMMATION FINALE GLOBALE (ménages et
administrations publiques) : son total est égal à la ligne « consommation finale globale » des
emplois du PIB ; les services d'administration, d'enseignement et de santé y figurent. Les produits
sont regroupés ici en cinq familles ; la correction territoriale (achats des non-résidents en
Tunisie, des résidents à l'étranger) est donnée dans la table, hors des barres.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

FAMILLES = [
    ("Produits agricoles et agro-alimentaires", "#2d8c6f", ("agriculture", "industries agro-alimentaires")),
    ("Énergie et eau", "#c0862b", ("extraction petrole", "raffinage", "production et distribution")),
    ("Autres produits industriels", "#0b4f6c", ("extraction des produits miniers", "industrie du textile",
                                                "industries chimiques", "industrie dautre", "industries mecaniques",
                                                "industries diverses", "construction")),
    ("Services marchands", "#8250df", ("commerce", "transport", "hebergement", "information", "activites financieres",
                                       "autres services marchands", "autres activites des menages",
                                       "activites des organisations")),
    ("Administration, enseignement, santé", "#bf3989", ("administration publique", "enseignement", "sante")),
]


def _nombre(v: float) -> str:
    return f"{v:,.1f}".replace(",", "\u202f").replace(".", ",")


def conso():
    d = figtools.series("cnat-produits")
    d = d[(d["famille"] == "consommation_menages") & (d["base"] == "base 2015")]
    d = d.sort_values("edition").groupby(["annee", "cle"]).tail(1)
    out = {}
    for an, g in d.groupby("annee"):
        v = dict(zip(g["cle"], g["valeur_md"]))
        row = {nom: sum(x for c, x in v.items() if c.startswith(pref)) for nom, _, pref in FAMILLES}
        row["Correction territoriale"] = v.get("correction terretoriale", 0.0)
        row["Ensemble (imprimé)"] = v.get("ensemble")
        out[int(an)] = row
    return out


def _barres() -> plt.Figure:
    figtools.apply_lang_font()
    c = conso()
    ans = sorted(c)
    fig, ax = plt.subplots(figsize=(8.8, 4.6))
    bas = [0.0] * len(ans)
    for nom, couleur, _ in FAMILLES:
        vals = [c[a][nom] for a in ans]
        barres = ax.bar(range(len(ans)), vals, bottom=bas, color=couleur, width=0.66, label=figtools.fig_text(nom))
        for a, b, v in zip(ans, barres, vals):
            figtools.infobulle(b, f"{a} · {nom} · {_nombre(v)}")
        bas = [x + v for x, v in zip(bas, vals)]
    ax.set_xticks(range(len(ans)))
    ax.set_xticklabels([str(a) for a in ans], fontsize=8)
    ax.set_title(figtools.fig_text("Consommation finale par famille de produits"), fontsize=10.5)
    ax.set_ylabel(figtools.fig_text("millions de dinars courants"), fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(fontsize=7.5, loc="upper left", framealpha=0.9)
    fig.tight_layout()
    return fig


def vues_conso():
    return [("Par famille", _barres())]


def table_conso():
    import pandas as pd
    c = conso()
    return pd.DataFrame([{"Année": a, **{k: round(v, 1) if v is not None else None for k, v in c[a].items()}}
                         for a in sorted(c)])

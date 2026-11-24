"""Figures du livre *L'énergie* — page de présentation, « La branche en chiffres ».

    from figures import energie as en
    en.vues_va() ; en.table_va()   # valeur ajoutée des branches de l'énergie

D'OÙ VIENNENT LES DONNÉES. Série `ins-va-branche-base2015` du cache : valeur ajoutée par
branche d'activité publiée par l'INS (comptes de la nation, base 2015, banque de données
« Valeurs ajoutées », statistiques/75), aux prix courants, 2020-2025. Trois branches forment
l'énergie dans cette nomenclature : extraction du pétrole et du gaz naturel, raffinage du
pétrole, production et distribution de l'électricité et du gaz. L'extraction des produits
miniers n'en fait pas partie (elle relève de l'industrie extractive).

La part rapporte la somme des trois branches au total des valeurs ajoutées de la même
édition (même base, mêmes prix). La série ne remonte pas avant 2020 : la base 2015 n'est pas
publiée par branche plus tôt dans cette banque de données, et les bases antérieures ne se
chaînent pas avec elle.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_VA = "ins-va-branche-base2015"
TOTAL = "Total des valeurs ajoutées"
GRIS = "#57606a"

# Branches de l'énergie dans la nomenclature agrégée de l'INS, dans l'ordre de pile.
BRANCHES = [
    ("Extraction du pétrole et du gaz naturel", "Extraction du pétrole et du gaz", "#0b4f6c"),
    ("Production et distribution de l'électricité et du gaz", "Électricité et gaz", "#2d8c6f"),
    ("Raffinage du pétrole", "Raffinage du pétrole", "#c0862b"),
]


def _nombre(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", "\u202f").replace(".", ",")


def _courant():
    d = figtools.series(SERIE_VA)
    d = d[d["prix"] == "courant"]
    return d.pivot(index="annee", columns="branche", values="valeur_md").sort_index()


def _barres() -> plt.Figure:
    figtools.apply_lang_font()
    p = _courant()
    annees = [int(a) for a in p.index]
    x = list(range(len(annees)))
    fig, ax = plt.subplots(figsize=(8.5, 4.6))
    bas = [0.0] * len(annees)
    for branche, lib, couleur in BRANCHES:
        vals = [float(v) for v in p[branche]]
        barres = ax.bar(x, vals, bottom=bas, width=0.66, color=couleur, label=figtools.fig_text(lib))
        for a, b, v in zip(annees, barres, vals):
            figtools.infobulle(b, f"{a} · {lib} · {_nombre(v)}")
        bas = [b + v for b, v in zip(bas, vals)]
    for xi, tot in zip(x, bas):
        ax.annotate(_nombre(tot), xy=(xi, tot), xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom", fontsize=7.5, color=GRIS)
    ax.set_title(figtools.fig_text("Valeur ajoutée des branches de l'énergie"), fontsize=10.5)
    ax.set_ylabel(figtools.fig_text("millions de dinars courants"), fontsize=9)
    ax.set_xticks(x)
    ax.set_xticklabels([str(a) for a in annees], fontsize=8)
    ax.set_ylim(0, max(bas) * 1.16)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(axis="y", labelsize=8)
    ax.legend(fontsize=7.5, loc="upper left", framealpha=0.9)
    fig.tight_layout()
    return fig


def _parts() -> plt.Figure:
    figtools.apply_lang_font()
    p = _courant()
    annees = [int(a) for a in p.index]
    somme = sum(p[b] for b, _, _ in BRANCHES)
    part = [100 * float(v) for v in somme / p[TOTAL]]
    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    ax.plot(annees, part, marker="o", color="#0b4f6c")
    for a, v in zip(annees, part):
        ax.annotate(_nombre(v), xy=(a, v), xytext=(0, 5), textcoords="offset points",
                    ha="center", fontsize=7.5, color=GRIS)
    ax.set_title(figtools.fig_text("Part des branches de l'énergie dans le total des valeurs ajoutées"),
                 fontsize=10.5)
    ax.set_ylabel(figtools.fig_text("%"), fontsize=9)
    ax.set_xticks(annees)
    ax.set_ylim(0, max(part) * 1.25)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=8)
    fig.tight_layout()
    return fig


def vues_va():
    return [("Montants", _barres()), ("Part du total", _parts())]


def table_va():
    import pandas as pd
    p = _courant()
    rows = []
    for a in p.index:
        row = {"Année": int(a)}
        for branche, lib, _ in BRANCHES:
            row[lib] = round(float(p.loc[a, branche]), 1)
        s = sum(float(p.loc[a, b]) for b, _, _ in BRANCHES)
        row["Énergie, total"] = round(s, 1)
        row["Part du total des valeurs ajoutées (%)"] = round(100 * s / float(p.loc[a, TOTAL]), 2)
        rows.append(row)
    return pd.DataFrame(rows)


# --- FBCF des branches de l'énergie (série `cnat-fbcf`) -------------------------------------
# Tableau « FBCF par secteur d'activité » des comptes de la nation, lu dans quinze éditions ;
# pour chaque base et chaque année, l'édition la plus récente qui l'imprime. Les deux bases ne
# se chaînent pas : deux segments, les années 2015-2017 publiées dans les deux.

SERIE_FBCF = "cnat-fbcf"
FBCF_BRANCHES = {
    "base 1997": [("b11 .extraction de petrole et gaz naturel", "Extraction du pétrole et du gaz"),
                  ("g40 . electricite et gaz", "Électricité et gaz"),
                  ("e23. raffinage de petrole", "Raffinage du pétrole")],
    "base 2015": [("extraction petrole et gaz naturel", "Extraction du pétrole et du gaz"),
                  ("production et distribution de lelectricite et gaz", "Électricité et gaz"),
                  ("raffinage du petrole", "Raffinage du pétrole")],
}
COULEURS = {"Extraction du pétrole et du gaz": "#0b4f6c", "Électricité et gaz": "#2d8c6f",
            "Raffinage du pétrole": "#c0862b"}


def fbcf():
    d = figtools.series(SERIE_FBCF)
    d = d[d["famille"] == "branche"].sort_values("edition").groupby(["base", "annee", "cle"]).tail(1)
    out = {}
    for base, branches in FBCF_BRANCHES.items():
        sous = d[d["base"] == base]
        out[base] = {lib: {int(r.annee): float(r.valeur_md) for r in sous[sous["cle"] == cle].itertuples()}
                     for cle, lib in branches}
    return out


def _fbcf_lignes() -> plt.Figure:
    figtools.apply_lang_font()
    f = fbcf()
    fig, ax = plt.subplots(figsize=(8.8, 4.6))
    for base, style in (("base 1997", "--"), ("base 2015", "-")):
        for lib, pts in f[base].items():
            ans = sorted(pts)
            ax.plot(ans, [pts[a] for a in ans], style, marker="o", ms=3, color=COULEURS[lib],
                    label=figtools.fig_text(f"{lib} ({base})"))
    ax.set_title(figtools.fig_text("FBCF des branches de l'énergie, par base des comptes"), fontsize=10.5)
    ax.set_ylabel(figtools.fig_text("millions de dinars courants"), fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=8)
    ax.legend(fontsize=7, framealpha=0.9, ncol=2)
    fig.tight_layout()
    return fig


def vues_fbcf():
    return [("Deux bases", _fbcf_lignes())]


def table_fbcf():
    import pandas as pd
    f = fbcf()
    rows = []
    for base, branches in f.items():
        for lib, pts in branches.items():
            for a in sorted(pts):
                rows.append({"Base": base, "Branche": lib, "Année": a, "FBCF (MD courants)": pts[a]})
    return pd.DataFrame(rows)

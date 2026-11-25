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


# --- Consommation finale des ménages et des administrations (comptes de secteur) -------------
# Série `cnat-secteurs` : opération « consommation finale » (P.3), côté emplois, ménages et
# administrations publiques, édition la plus récente qui imprime l'année. Leur somme est égale,
# au dixième près, au total du tableau par produit (série `cnat-produits`).

def menages_apu():
    d = figtools.series("cnat-secteurs")
    d = d[(d["operation"] == "consommation_finale") & (d["cote"] == "emplois") & (d["secteur"].isin(["menages", "apu"]))]
    d = d.sort_values("edition").groupby(["annee", "secteur"]).tail(1)
    p = d.pivot(index="annee", columns="secteur", values="valeur").sort_index()
    t = conso()
    return {int(a): (float(p.loc[a, "menages"]), float(p.loc[a, "apu"]), t.get(int(a), {}).get("Ensemble (imprimé)"))
            for a in p.index}


def _barres_menages() -> plt.Figure:
    figtools.apply_lang_font()
    m = menages_apu()
    ans = sorted(m)
    fig, ax = plt.subplots(figsize=(8.8, 4.6))
    men = [m[a][0] for a in ans]
    apu = [m[a][1] for a in ans]
    b1 = ax.bar(range(len(ans)), men, color="#0b4f6c", width=0.66, label=figtools.fig_text("Ménages"))
    b2 = ax.bar(range(len(ans)), apu, bottom=men, color="#bf3989", width=0.66,
                label=figtools.fig_text("Administrations publiques"))
    for a, b, v in zip(ans, b1, men):
        figtools.infobulle(b, f"{a} · ménages · {_nombre(v)}")
    for a, b, v in zip(ans, b2, apu):
        figtools.infobulle(b, f"{a} · administrations · {_nombre(v)}")
    tot = [m[a][2] for a in ans]
    ax.plot(range(len(ans)), tot, "o", color="#57606a", ms=4, label=figtools.fig_text("Total du tableau par produit"))
    ax.set_xticks(range(len(ans)))
    ax.set_xticklabels([str(a) for a in ans], fontsize=8)
    ax.set_title(figtools.fig_text("Consommation finale des ménages et des administrations"), fontsize=10.5)
    ax.set_ylabel(figtools.fig_text("millions de dinars courants"), fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(fontsize=7.5, loc="upper left", framealpha=0.9)
    fig.tight_layout()
    return fig


def vues_menages():
    return [("Ménages et administrations", _barres_menages())]


def table_menages():
    import pandas as pd
    m = menages_apu()
    return pd.DataFrame([{"Année": a, "Ménages (MD)": v[0], "Administrations publiques (MD)": v[1],
                          "Somme": round(v[0] + v[1], 1), "Total du tableau par produit (MD)": v[2]}
                         for a, v in sorted(m.items())])


def table_transferts_nature(annees=range(2015, 2024)) -> str:
    """Tableau markdown : transferts sociaux en nature (D.63, D.631, D.632) versés par les administrations
    publiques, dépense de consommation finale des ménages (P.3) et consommation finale effective (P.3 + D.63
    reçus), base 2015, édition la plus récente qui imprime l'année."""
    d = figtools.series("cnat-d63")
    d = d[d["base"].astype(str) == "2015"].sort_values("edition")
    s = figtools.series("cnat-secteurs")
    s = s[(s["base"].astype(str) == "2015") & (s["secteur"] == "menages") & (s["operation"] == "consommation_finale")
          & (s["cote"] == "emplois")].sort_values("edition")
    def v(df, an, **f):
        x = df[df["annee"].astype(int) == an]
        for k, val in f.items():
            x = x[x[k].fillna("").astype(str) == val]
        return float(x["valeur"].iloc[-1] if "valeur" in x else x["valeur_md"].iloc[-1]) if len(x) else None
    fr = lambda x: "" if x is None else f"{x:,.1f}".replace(",", " ").replace(".", ",")
    ans = list(annees)
    lignes = {
        "Transferts sociaux en nature reçus par les ménages (D.63)": [v(d, a, operation="transferts_sociaux_nature", cote="ressources") for a in ans],
        "— prestations sociales en nature versées par les administrations (D.631)": [v(d, a, operation="prestations_sociales_nature", cote="emplois", contrepartie="apu") for a in ans],
        "— biens et services individuels non marchands des administrations (D.632)": [v(d, a, operation="transferts_bs_individuels_non_marchands", cote="emplois", contrepartie="apu") for a in ans],
        "Dépense de consommation finale des ménages (P.3)": [v(s, a) for a in ans],
    }
    p3, d63 = lignes["Dépense de consommation finale des ménages (P.3)"], lignes["Transferts sociaux en nature reçus par les ménages (D.63)"]
    lignes["Consommation finale effective des ménages (P.3 + D.63)"] = [None if a is None or b is None else a + b for a, b in zip(p3, d63)]
    out = ["| Millions de dinars | " + " | ".join(str(a) for a in ans) + " |", "|---|" + "--:|" * len(ans)]
    for lib, vals in lignes.items():
        lib = f"**{lib}**" if lib.startswith("Consommation finale effective") else lib
        out.append(f"| {lib} | " + " | ".join(fr(x) for x in vals) + " |")
    return "\n".join(out)

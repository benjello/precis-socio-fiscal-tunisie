"""Figures de la section « Ce que pèse l'ensemble » (livre « Le transport »).

    from figures import poids as pd_fig
    pd_fig.figure("missions", caption=…, note_lecture=…)

D'OÙ VIENNENT LES DONNÉES. Trois séries de `tunisia-data`, lues par `figtools.series()` —
donc depuis le snapshot `precis/_seriescache/` quand l'entrepôt est absent :

  - `budget-missions-execute` : dépense exécutée par mission (crédits de paiement payés),
    dépouillée des rapports annuels de performance ; pour le secteur, les missions
    « transport » et « equipement », 2018-2023 seulement (limite des RAP) ;
  - `transport-transferts-par-entreprise` : transferts du budget aux entreprises et
    établissements du ministère du Transport, par nature, 2016-2024 (annexe 8 des lois de
    finances) ; ligne entite="ministere" = total du ministère ;
  - `denominateurs-depenses-etat-pib` : dépenses de l'État hors service de la dette
    (réalisations) et PIB en base 2015, pour les parts.

RÈGLES.

  - **Aucune série n'est raccordée à une autre.** Les deux missions exécutées (2018-2023) et
    les transferts au ministère du Transport (2016-2024) ont chacun leur figure : concepts
    différents (missions Transport + Équipement d'un côté, transferts au seul ministère du
    Transport de l'autre), jamais chaînés en une seule courbe.
  - **Une lecture par année pour les transferts** : l'édition la plus récente de l'annexe 8
    qui porte l'année (`derniere_edition` vraie). Les autres lectures restent dans l'onglet
    « Données ».
  - **Parts calculées sur le dénominateur commun** : dépenses de l'État hors service de la
    dette (réalisations) et PIB en base 2015.

Les libellés sont en français ; les libellés arabes restent à verser (`_L`, clé `ar`).
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

MISSIONS = "budget-missions-execute"
TRANSFERTS = "transport-transferts-par-entreprise"
DENOM = "denominateurs-depenses-etat-pib"

BLEU, ORANGE, VERT, GRIS, NOIR = "#0969da", "#d1600f", "#1a7f37", "#8c959f", "#24292f"

_L = {
    "x": {"fr": "Année"},
    "md": {"fr": "Millions de dinars courants"},
    "pct_dep": {"fr": "En % des dépenses de l'État\nhors service de la dette"},
    "pct_pib": {"fr": "En % du PIB"},
    "vue_md": {"fr": "En millions de dinars"},
    "vue_dep": {"fr": "En % des dépenses de l'État (hors dette)"},
    "vue_pib": {"fr": "En % du PIB"},
    "transport": {"fr": "Mission Transport"},
    "equipement": {"fr": "Mission Équipement et Habitat"},
    "interventions": {"fr": "Interventions"},
    "investissements": {"fr": "Investissements"},
    "autres": {"fr": "Fonctionnement et rémunérations"},
    "ministere": {"fr": "Total du ministère du Transport"},
    "lf": {"fr": "barre claire, astérisque : loi de finances, non réalisation"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _ft(cle: str) -> str:
    return "\n".join(figtools.fig_text(ligne) for ligne in _lab(cle).split("\n"))


def _nb(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _legende(ax, poignees, ncol=2, y=-0.14):
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, y), ncol=ncol,
              fontsize=7.5, frameon=False)


def _cadre(ax, ylabel: str):
    ax.set_ylabel(_ft(ylabel))
    ax.set_xlabel(figtools.fig_text(_lab("x")))
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)


def _denominateurs(annees) -> dict[int, tuple[float, float]]:
    """{année: (dépenses de l'État hors dette en MD, PIB en MD)} pour les années voulues."""
    d = figtools.series(DENOM)
    d = d[d["annee"].isin(list(annees))]
    return {int(r.annee): (float(r.depenses_etat_hors_dette_MDT), float(r.pib_MDT))
            for r in d.itertuples()}


def _echelle(mesure: str, annee: int, denom: dict[int, tuple[float, float]]) -> float:
    """Facteur par lequel un montant en MD devient la grandeur de la vue."""
    if mesure == "md":
        return 1.0
    dep, pib = denom[annee]
    return 100.0 / (dep if mesure == "dep" else pib)


MESURES = {"md": ("md", 0), "dep": ("pct_dep", 1), "pib": ("pct_pib", 2)}


# --- 1. La dépense exécutée des deux missions, 2018-2023 ---------------------------------

GROUPES_MISSIONS = (("transport", "transport", BLEU, ""),
                    ("equipement", "equipement", ORANGE, "//"))


def _missions():
    d = figtools.series(MISSIONS)
    return d[d["mission"].isin(["transport", "equipement"])]


def fig_missions(mesure: str = "md"):
    figtools.apply_lang_font()
    d = _missions()
    annees = sorted(int(a) for a in d["annee"].unique())
    denom = _denominateurs(annees)
    ylabel, dec = MESURES[mesure]
    unite = {"md": " MD", "dep": " % des dépenses de l'État", "pib": " % du PIB"}[mesure]
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    for a in annees:
        da = d[d["annee"] == a]
        k = _echelle(mesure, a, denom)
        bas = 0.0
        for cle, mission, couleur, hachure in GROUPES_MISSIONS:
            v = float(da[da["mission"] == mission]["paye_MDT"].iloc[0])
            h = v * k
            barre = ax.bar([a], [h], bottom=bas, width=0.7, color=couleur, hatch=hachure,
                           edgecolor="white", zorder=2)
            figtools.infobulle(barre[0], f"{a} · {_lab(cle)} : {_nb(v)} MD"
                               + ("" if mesure == "md" else f", soit {_nb(h, max(dec, 1))}{unite}"))
            bas += h
        ax.annotate(_nb(bas, dec), xy=(a, bas), xytext=(0, 2), textcoords="offset points",
                    ha="center", va="bottom", fontsize=7)
    _cadre(ax, ylabel)
    ax.set_xticks(annees)
    ax.set_xlim(annees[0] - 0.8, annees[-1] + 0.8)
    ax.set_ylim(top=ax.get_ylim()[1] * 1.12)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, dec)))
    figtools.marque_rupture(ax, 2020)
    poignees = [Patch(facecolor=c, hatch=h, edgecolor="white", label=figtools.fig_text(_lab(k)))
                for k, _, c, h in GROUPES_MISSIONS]
    _legende(ax, poignees, ncol=2)
    fig.tight_layout()
    return fig


def _figure_missions():
    import pandas as pd
    d = _missions().sort_values(["annee", "mission"])
    denom = _denominateurs(sorted(int(a) for a in d["annee"].unique()))
    noms = {"transport": "Mission Transport", "equipement": "Mission Équipement et Habitat"}
    lignes = []
    for r in d.itertuples():
        a, dep, pib = int(r.annee), denom[int(r.annee)][0], denom[int(r.annee)][1]
        v = float(r.paye_MDT)
        lignes.append({
            "Année": a, "Mission": noms[r.mission], "Régime": r.regime,
            "Dépense exécutée (millions de dinars)": v,
            "En % des dépenses de l'État hors dette": round(100 * v / dep, 1),
            "En % du PIB": round(100 * v / pib, 2),
            "Dépenses de l'État hors dette (millions de dinars)": dep,
            "PIB en base 2015 (millions de dinars)": pib})
    table = pd.DataFrame(lignes)
    vues = [(_lab("vue_md"), fig_missions("md")), (_lab("vue_dep"), fig_missions("dep")),
            (_lab("vue_pib"), fig_missions("pib"))]
    return vues, table, (MISSIONS, DENOM), "fig_transport_poids"


# --- 2. Les transferts au ministère du Transport, 2016-2024 -----------------------------

GROUPES_TRANSFERTS = (("interventions", "interventions", VERT, ""),
                      ("investissements", "investissements", BLEU, "//"),
                      ("autres", None, GRIS, ".."))


def _transferts():
    d = figtools.series(TRANSFERTS)
    d = d[(d["entite"] == "ministere")
          & d["derniere_edition"].astype(str).str.lower().eq("true")]
    return d


def _par_annee(d, a) -> dict[str, float]:
    da = d[d["annee"] == a]
    return {str(r.nature): float(r.valeur_md) for r in da.itertuples()}


def fig_transferts(mesure: str = "md"):
    figtools.apply_lang_font()
    d = _transferts()
    annees = sorted(int(a) for a in d["annee"].unique())
    denom = _denominateurs(annees)
    dec = 0 if mesure == "md" else 1
    unite = " MD" if mesure == "md" else " % des dépenses de l'État"
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    for a in annees:
        valeurs = _par_annee(d, a)
        etat = str(d[d["annee"] == a]["etat"].iloc[0])
        total = valeurs["total"]
        k = _echelle(mesure, a, denom)
        nommes = 0.0
        bas = 0.0
        for cle, nature, couleur, hachure in GROUPES_TRANSFERTS:
            if nature is None:
                v = total - nommes
            else:
                v = valeurs.get(nature, 0.0)
                nommes += v
            h = v * k
            barre = ax.bar([a], [h], bottom=bas, width=0.7, color=couleur, hatch=hachure,
                           edgecolor="white", zorder=2,
                           alpha=1.0 if etat == "réalisations" else 0.55)
            figtools.infobulle(barre[0], f"{a} ({etat}) · {_lab(cle)} : {_nb(v)} MD"
                               + ("" if mesure == "md" else f", soit {_nb(h, 1)}{unite}"))
            bas += h
        ax.annotate(_nb(bas, dec) + ("" if etat == "réalisations" else "*"), xy=(a, bas),
                    xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                    fontsize=7)
    _cadre(ax, "md" if mesure == "md" else "pct_dep")
    ax.set_xticks(annees)
    ax.set_xlim(annees[0] - 0.8, annees[-1] + 0.8)
    ax.set_ylim(top=ax.get_ylim()[1] * 1.12)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, dec)))
    poignees = [Patch(facecolor=c, hatch=h, edgecolor="white", label=figtools.fig_text(_lab(k)))
                for k, _, c, h in GROUPES_TRANSFERTS]
    poignees.append(Patch(facecolor=GRIS, alpha=0.55, edgecolor="white",
                          label=figtools.fig_text(_lab("lf"))))
    _legende(ax, poignees, ncol=2)
    fig.tight_layout()
    return fig


def _figure_transferts():
    import pandas as pd
    d = _transferts().sort_values(["annee", "nature"])
    annees = sorted(int(a) for a in d["annee"].unique())
    denom = _denominateurs(annees)
    noms = {"interventions": "Interventions", "investissements": "Investissements",
            "fonctionnement": "Fonctionnement", "remunerations": "Rémunérations",
            "total": "Total du ministère"}
    lignes = []
    for a in annees:
        valeurs = _par_annee(d, a)
        etat = str(d[d["annee"] == a]["etat"].iloc[0])
        edition = str(d[d["annee"] == a]["edition"].iloc[0])
        dep = denom[a][0]
        for nature in ("interventions", "investissements", "fonctionnement",
                       "remunerations", "total"):
            if nature not in valeurs:
                continue
            v = valeurs[nature]
            lignes.append({
                "Année": a, "État du chiffre": etat, "Édition de l'annexe 8": edition,
                "Nature": noms[nature], "Transfert (millions de dinars)": round(v, 3),
                "En % des dépenses de l'État hors dette": round(100 * v / dep, 1),
                "Dépenses de l'État hors dette (millions de dinars)": dep})
    table = pd.DataFrame(lignes)
    vues = [(_lab("vue_md"), fig_transferts("md")), (_lab("vue_dep"), fig_transferts("dep"))]
    return vues, table, (TRANSFERTS, DENOM), "fig_transport_transferts"


# --- registre ---------------------------------------------------------------------------

FIGURES = {"missions": _figure_missions, "transferts": _figure_transferts}


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure `nom` en onglets (graphique, données, sources).

    À appeler dans un chunk Quarto étiqueté `#| label: fig-…`, `#| output: asis`."""
    vues, table, series_ids, slug = FIGURES[nom]()
    figtools.figure_tabs(vues, table, *series_ids, slug=slug, caption=caption,
                         note_lecture=note_lecture)
    plt.close("all")

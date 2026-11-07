"""Figures de l'annexe du site « Le budget de l'État et son évolution » (`precis/fr/annexe-budget-etat.qmd`).

    from figures import annexe_budget
    annexe_budget.vues_serie()      # deux vues de `fig-bud-serie` : dinars courants, dinars constants
    annexe_budget.table_serie()     # ses données téléchargeables
    annexe_budget.fig_pib()         # figure `fig-bud-pib` : dépenses hors dette en % du PIB, par base
    annexe_budget.table_pib()       # ses données
    annexe_budget.fig_recettes()    # figure `fig-bud-recettes` : composition des recettes fiscales
    annexe_budget.table_recettes()  # ses données

MODULE DE FIGURE D'UNE PAGE DE SITE, et non d'un livre : il vit dans `precis/fr/figures/`,
à côté de la page ; la page arabe le trouve par le lien symbolique `precis/ar/figures`.

D'OÙ VIENNENT LES DONNÉES. Trois séries de `tunisia-data`, lues par `figtools.series()`
(l'entrepôt s'il est installé, sinon le cache `precis/_seriescache/`) :

  - `jort-lf-budget-ordinaire` : le budget ordinaire **voté** par la loi de finances (titre I),
    relevé loi par loi au Journal officiel, 1959-1986, en millions de dinars courants ;
  - `denominateurs-depenses-etat-pib` : les dépenses de l'État **réalisées**, hors service de
    la dette, et le PIB, 1986-2025, avec la base des comptes nationaux de chaque année ;
  - `recettes-fiscales-composition` : la composition des recettes fiscales de l'État, 1986-2025.

RÈGLES (voir docs/notes/annexe-budget-etat.md).

  - **Voté et réalisé ne se chaînent pas** : la série longue a deux segments de définition
    différente (titre I voté avant 1986 ; dépenses réalisées hors dette ensuite). On les trace
    distinctement ; on ne construit aucune courbe continue de l'un à l'autre.
  - **Le % du PIB se trace par plage contiguë de base** : une rupture dès que la base change ou
    qu'une année manque. Les années à PIB « non rattaché » (valeur propre au ministère) sont des
    points isolés, pas une ligne. Renvoi à l'annexe PIB pour les ruptures de base.
  - **La déflation** (dinars constants) emploe l'IPC long (`ipc-longue-periode`, jusqu'en 2023)
    raccordé à l'IPC base 2015 (`bct-ipc-base2015`, jusqu'en 2025) par le rapport des deux en 2015.
  - **Aucun nombre n'est écrit en dur ici** : tout est lu dans les séries.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
sys.path.insert(0, "../../scripts")
import figtools  # noqa: E402

# --- séries ------------------------------------------------------------------
SERIE_VOTE = "jort-lf-budget-ordinaire"
SERIE_REEL = "denominateurs-depenses-etat-pib"
SERIE_RECETTES = "recettes-fiscales-composition"
ANNEE_PRIX = 2015

# --- couleurs (cohérentes avec l'annexe PIB : 1983 orange, 1997 bleu, 2015 vert) ----
C_VOTE = "#1f4e79"
C_REEL = "#c0392b"
_C_BASE = {
    "1983": "#e08214",
    "1997": "#2166ac",
    "2015": "#1a9850",
    "autre": "#7f7f7f",
}

# --- i18n minimal ------------------------------------------------------------
_L = {
    "y_md":      {"fr": "millions de dinars",            "ar": "مليون دينار"},
    "y_const":   {"fr": "millions de dinars de {a}",     "ar": "مليون دينار بأسعار {a}"},
    "y_pct":     {"fr": "en % du PIB",                   "ar": "٪ من الناتج المحلي"},
    "x_annee":   {"fr": "année",                         "ar": "السنة"},
    "l_vote":    {"fr": "voté (titre I), Journal officiel", "ar": "المصوَّت (الباب الأول)"},
    "l_reel":    {"fr": "réalisé hors dette, min. des Finances", "ar": "المنجز بدون الدين"},
    "l_base":    {"fr": "base {b}",                      "ar": "أساس {b}"},
    "l_nonratt": {"fr": "PIB non rattaché",              "ar": "ناتج غير مرتبط بأساس"},
    "y_pct_rec": {"fr": "recettes fiscales, en % du PIB", "ar": "الجباية، ٪ من الناتج"},
    "v_compo":   {"fr": "composition (millions de dinars)", "ar": "التركيبة (مليون دينار)"},
    "v_pression":{"fr": "pression fiscale (% du PIB)",   "ar": "الضغط الجبائي (٪ من الناتج)"},
    "irpp":      {"fr": "IRPP",     "ar": "الدخل"},
    "is":        {"fr": "IS",       "ar": "الشركات"},
    "tva":       {"fr": "TVA",      "ar": "الأداء على القيمة المضافة"},
    "conso":     {"fr": "droits de consommation", "ar": "معاليم الاستهلاك"},
    "douanes":   {"fr": "droits de douane",       "ar": "الديوانة"},
    "autres":    {"fr": "autres impôts indirects", "ar": "أداءات غير مباشرة أخرى"},
}


def _lab(key: str, **kw) -> str:
    s = _L[key].get(figtools.lang(), _L[key]["fr"])
    return s.format(**kw) if kw else s


def _ft(key: str, **kw) -> str:
    return figtools.fig_text(_lab(key, **kw))


# --- lecture des séries ------------------------------------------------------
def _vote() -> pd.DataFrame:
    d = figtools.series(SERIE_VOTE)[["annee", "valeur_md"]].rename(columns={"valeur_md": "vote_MDT"})
    return d.dropna(subset=["vote_MDT"]).sort_values("annee")


def _reel() -> pd.DataFrame:
    d = figtools.series(SERIE_REEL)[
        ["annee", "depenses_etat_hors_dette_MDT", "pib_MDT", "base_pib"]
    ].rename(columns={"depenses_etat_hors_dette_MDT": "reel_MDT"})
    return d.sort_values("annee")


def _deflateur() -> pd.Series:
    """Indice de déflation vers ANNEE_PRIX, IPC long raccordé à l'IPC base 2015."""
    long = figtools.series("ipc-longue-periode")[["annee", "indice_base1970"]].rename(
        columns={"indice_base1970": "ipc"})
    b15 = figtools.series("bct-ipc-base2015")[["annee", "valeur"]].rename(columns={"valeur": "v"})
    k = float(long.loc[long.annee == ANNEE_PRIX, "ipc"].iloc[0]) / \
        float(b15.loc[b15.annee == ANNEE_PRIX, "v"].iloc[0])
    ext = b15[b15.annee > long.annee.max()].copy()
    ext["ipc"] = ext["v"] * k
    ipc = pd.concat([long[["annee", "ipc"]], ext[["annee", "ipc"]]]).drop_duplicates("annee")
    iref = float(ipc.loc[ipc.annee == ANNEE_PRIX, "ipc"].iloc[0])
    ipc["defl"] = iref / ipc["ipc"]
    return ipc.set_index("annee")["defl"]


def _courant() -> pd.DataFrame:
    v, r = _vote(), _reel()
    df = v.merge(r[["annee", "reel_MDT"]], on="annee", how="outer").sort_values("annee")
    defl = _deflateur()
    df["defl"] = df["annee"].map(defl)
    df["vote_const"] = df["vote_MDT"] * df["defl"]
    df["reel_const"] = df["reel_MDT"] * df["defl"]
    return df


def _base_cle(libelle: str) -> str:
    for cle in ("1983", "1997", "2015"):
        if cle in str(libelle):
            return cle
    return "autre"


def _plages(d: pd.DataFrame) -> list[pd.DataFrame]:
    """Découpe en plages contiguës : rupture si la base change ou si une année manque."""
    d = d.sort_values("annee").reset_index(drop=True)
    plages, debut = [], 0
    for i in range(1, len(d) + 1):
        rupture = (
            i == len(d)
            or d.loc[i, "base_cle"] != d.loc[i - 1, "base_cle"]
            or int(d.loc[i, "annee"]) != int(d.loc[i - 1, "annee"]) + 1
        )
        if rupture:
            plages.append(d.iloc[debut:i])
            debut = i
    return plages


# --- figure 1 : série longue (courant + constant) ----------------------------
def _trace_serie(df: pd.DataFrame, col_v: str, col_r: str, ylabel: str):
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.plot(df["annee"], df[col_v], color=C_VOTE, lw=1.8, label=_ft("l_vote"))
    ax.plot(df["annee"], df[col_r], color=C_REEL, lw=1.8, label=_ft("l_reel"))
    pivot = df.loc[df[col_r].notna(), "annee"].min()
    ax.axvline(pivot, color="grey", ls=":", lw=1)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(figtools.fig_text(ylabel))
    ax.grid(alpha=0.25)
    ax.legend(fontsize=9, loc="upper left")
    fig.tight_layout()
    return fig


def vues_serie():
    df = _courant()
    return [
        (_lab("y_md"), _trace_serie(df, "vote_MDT", "reel_MDT", _lab("y_md"))),
        (_lab("y_const", a=ANNEE_PRIX),
         _trace_serie(df, "vote_const", "reel_const", _lab("y_const", a=ANNEE_PRIX))),
    ]


def table_serie() -> pd.DataFrame:
    df = _courant()[["annee", "vote_MDT", "reel_MDT", "vote_const", "reel_const"]].copy()
    return df.round(1)


# --- figure 2 : dépenses en % du PIB, par plage de base ----------------------
def fig_pib():
    d = _reel().dropna(subset=["reel_MDT", "pib_MDT"]).copy()
    d["pct"] = 100 * d["reel_MDT"] / d["pib_MDT"]
    d["base_cle"] = d["base_pib"].map(_base_cle)
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    vues_legende = {}
    for plage in _plages(d):
        cle = plage["base_cle"].iloc[0]
        coul = _C_BASE[cle]
        lab = _lab("l_base", b=cle) if cle != "autre" else _lab("l_nonratt")
        if len(plage) == 1:
            ax.plot(plage["annee"], plage["pct"], marker="o", ms=5, ls="none", color=coul)
        else:
            ax.plot(plage["annee"], plage["pct"], marker="o", ms=3, lw=1.8, color=coul)
        vues_legende.setdefault(lab, coul)
    from matplotlib.lines import Line2D
    ax.legend([Line2D([], [], color=c, marker="o", lw=1.8) for c in vues_legende.values()],
              [figtools.fig_text(k) for k in vues_legende], fontsize=9)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_pct"))
    ax.grid(alpha=0.25)
    fig.tight_layout()
    return fig


def table_pib() -> pd.DataFrame:
    d = _reel().dropna(subset=["reel_MDT", "pib_MDT"]).copy()
    d["pct_pib"] = (100 * d["reel_MDT"] / d["pib_MDT"]).round(1)
    return d[["annee", "reel_MDT", "pib_MDT", "base_pib", "pct_pib"]]


# --- figure 3 : composition des recettes fiscales ----------------------------
_POSTES = [
    ("irpp_MDT", "irpp", "#1a9850"),
    ("is_MDT", "is", "#66bd63"),
    ("tva_MDT", "tva", "#2166ac"),
    ("consommation_MDT", "conso", "#4393c3"),
    ("douanes_MDT", "douanes", "#e08214"),
    ("autres_indirects_MDT", "autres", "#999999"),
]


def fig_recettes():
    d = figtools.series(SERIE_RECETTES).sort_values("annee")
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.stackplot(
        d["annee"], *[d[c] for c, _, _ in _POSTES],
        labels=[_ft(k) for _, k, _ in _POSTES],
        colors=[c for *_, c in _POSTES],
    )
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_md"))
    ax.set_xlim(d["annee"].min(), d["annee"].max())
    ax.legend(fontsize=8, loc="upper left", ncol=2)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    return fig


def _recettes_pib() -> pd.DataFrame:
    """Recettes fiscales totales rapportées au PIB, avec la base de chaque année."""
    rec = figtools.series(SERIE_RECETTES)[["annee", "total_MDT"]]
    pib = _reel()[["annee", "pib_MDT", "base_pib"]]
    d = rec.merge(pib, on="annee", how="inner").dropna(subset=["total_MDT", "pib_MDT"])
    d = d.sort_values("annee").copy()
    d["pct"] = 100 * d["total_MDT"] / d["pib_MDT"]
    d["base_cle"] = d["base_pib"].map(_base_cle)
    return d


def fig_recettes_pib():
    d = _recettes_pib()
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    vues_legende = {}
    for plage in _plages(d):
        cle = plage["base_cle"].iloc[0]
        coul = _C_BASE[cle]
        lab = _lab("l_base", b=cle) if cle != "autre" else _lab("l_nonratt")
        if len(plage) == 1:
            ax.plot(plage["annee"], plage["pct"], marker="o", ms=5, ls="none", color=coul)
        else:
            ax.plot(plage["annee"], plage["pct"], marker="o", ms=3, lw=1.8, color=coul)
        vues_legende.setdefault(lab, coul)
    from matplotlib.lines import Line2D
    ax.legend([Line2D([], [], color=c, marker="o", lw=1.8) for c in vues_legende.values()],
              [figtools.fig_text(k) for k in vues_legende], fontsize=9)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_pct_rec"))
    ax.grid(alpha=0.25)
    fig.tight_layout()
    return fig


def vues_recettes():
    return [
        (_lab("v_compo"), fig_recettes()),
        (_lab("v_pression"), fig_recettes_pib()),
    ]


def table_recettes() -> pd.DataFrame:
    d = figtools.series(SERIE_RECETTES)
    cols = ["annee"] + [c for c, _, _ in _POSTES] + ["total_MDT"]
    out = d[[c for c in cols if c in d.columns]].copy()
    pib = _recettes_pib()[["annee", "pct"]].rename(columns={"pct": "pression_fiscale_pct_pib"})
    return out.merge(pib, on="annee", how="left").round({"pression_fiscale_pct_pib": 1})

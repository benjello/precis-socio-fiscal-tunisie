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
    "y_pct_tot": {"fr": "en % des dépenses hors dette", "ar": "٪ من النفقات دون الدين"},
    "v_part":    {"fr": "part du total (%)",         "ar": "الحصة من المجموع (٪)"},
    "v_md":      {"fr": "en dinars (millions)",       "ar": "بالدينار (مليون)"},
    "n_remun":   {"fr": "rémunérations publiques",    "ar": "الأجور العمومية"},
    "n_moyens":  {"fr": "moyens des services",        "ar": "وسائل المصالح"},
    "n_interv":  {"fr": "interventions publiques",    "ar": "التدخلات العمومية"},
    "n_equip":   {"fr": "équipement (investissement)", "ar": "التجهيز (الاستثمار)"},
    "n_prets":   {"fr": "prêts et avances",           "ar": "القروض والتسبقات"},
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


# --- figure 4 : désagrégation des dépenses par nature (vue budgétaire) ---------
SERIE_NATURE = "budget-desagregation-nature"
SERIE_DISPOSITIFS = "budget-dispositifs-poids"
# natures empilées : (colonne, clé i18n, couleur) ; mêmes teintes que l'annexe
_NATURES = [
    ("remunerations_MDT", "n_remun",  "#1f4e79"),
    ("moyens_MDT",        "n_moyens", "#4393c3"),
    ("interventions_MDT", "n_interv", "#c0392b"),
    ("equipement_MDT",    "n_equip",  "#1a9850"),
    ("prets_MDT",         "n_prets",  "#999999"),
]


def _nature() -> pd.DataFrame:
    """Ventilation par nature, années complètes seulement (sous-rubriques dès 1996)."""
    d = figtools.series(SERIE_NATURE).sort_values("annee")
    return d[d["interventions_MDT"].notna() & d["moyens_MDT"].notna()].copy()


def _trace_desag(d: pd.DataFrame, en_part: bool):
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    base = d["total_hors_dette_MDT"] if en_part else 1.0
    series = [100 * d[c] / base if en_part else d[c] for c, _, _ in _NATURES]
    ax.stackplot(d["annee"], *series,
                 labels=[_ft(k) for _, k, _ in _NATURES],
                 colors=[c for *_, c in _NATURES])
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_pct_tot") if en_part else _ft("y_md"))
    ax.set_xlim(d["annee"].min(), d["annee"].max())
    if en_part:
        ax.set_ylim(0, 100)
    ax.legend(fontsize=8, loc="lower right", ncol=2, framealpha=0.9)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    return fig


def vues_desagregation():
    d = _nature()
    return [
        (_lab("v_part"), _trace_desag(d, en_part=True)),
        (_lab("v_md"),   _trace_desag(d, en_part=False)),
    ]


def table_desagregation() -> pd.DataFrame:
    d = _nature()[["annee"] + [c for c, _, _ in _NATURES] + ["total_hors_dette_MDT"]]
    return d.round(1)


def table_dispositifs() -> pd.DataFrame:
    """Poids annuel des dispositifs du précis (overlay), lu de la série engendrée."""
    d = figtools.series(SERIE_DISPOSITIFS)
    cols = ["annee", "dispositif", "valeur_MDT", "rattachement", "transversal",
            "part_ligne_pct", "part_total_pct"]
    return d[[c for c in cols if c in d.columns]].sort_values(["annee", "dispositif"])


_DISP = {
    "masse_salariale":    {"fr": "masse salariale",        "ar": "كتلة الأجور",   "c": "#1f4e79", "t": False},
    "compensation":       {"fr": "compensation",           "ar": "الدعم",        "c": "#c0392b", "t": False},
    "transferts_ep":      {"fr": "transferts aux EP",      "ar": "تحويلات للمنشآت", "c": "#e08214", "t": True},
    "transferts_caisses": {"fr": "transferts aux caisses", "ar": "تحويلات للصناديق", "c": "#8e44ad", "t": True},
    "dotation_fccl":      {"fr": "dotation FCCL",          "ar": "منحة الصندوق المشترك", "c": "#1a9850", "t": False},
}


def fig_dispositifs():
    """Poids de chaque dispositif, en % des dépenses hors dette, par an.

    Les dispositifs **transversaux** (transferts aux EP et aux caisses, qui traversent
    plusieurs natures et se chevauchent) sont en pointillé : ils ne s'additionnent pas aux
    autres ni entre eux.
    """
    d = figtools.series(SERIE_DISPOSITIFS)
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    for disp, st in _DISP.items():
        s = d[d["dispositif"] == disp].sort_values("annee")
        s = s[pd.to_numeric(s["part_total_pct"], errors="coerce").notna()]
        if s.empty:
            continue
        lab = st.get(figtools.lang(), st["fr"])
        ax.plot(s["annee"], pd.to_numeric(s["part_total_pct"]),
                color=st["c"], lw=1.8, ls="--" if st["t"] else "-",
                marker="o", ms=3, label=figtools.fig_text(lab))
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_pct_tot"))
    ax.grid(alpha=0.2)
    ax.legend(fontsize=8, loc="upper left", ncol=2)
    fig.tight_layout()
    return fig


# --- figure 5 : vue comptes de la nation (compte APU, emplois par nature) -----
SERIE_APU = "budget-comptanat-apu"
_APU = [
    ("remuneration_salaries_MDT", "a_remun",  "#1f4e79"),
    ("conso_intermediaire_MDT",   "a_ci",     "#4393c3"),
    ("prestations_sociales_MDT",  "a_presta", "#c0392b"),
    ("autres_transferts_courants_MDT", "a_transf", "#e08214"),
    ("fbcf_MDT",                  "a_fbcf",   "#1a9850"),
    ("interets_MDT",              "a_inter",  "#8e44ad"),
    ("transferts_capital_MDT",    "a_cap",    "#999999"),
]
_APU_L = {
    "a_remun":  {"fr": "rémunération des salariés", "ar": "أجور الأجراء"},
    "a_ci":     {"fr": "consommation intermédiaire", "ar": "الاستهلاك الوسيط"},
    "a_presta": {"fr": "prestations sociales",       "ar": "التحويلات الاجتماعية"},
    "a_transf": {"fr": "autres transferts courants", "ar": "تحويلات جارية أخرى"},
    "a_fbcf":   {"fr": "FBCF (investissement)",      "ar": "تكوين رأس المال الثابت"},
    "a_inter":  {"fr": "intérêts",                   "ar": "الفوائد"},
    "a_cap":    {"fr": "transferts en capital",      "ar": "تحويلات رأس المال"},
}

# --- figure 6 : déficit et dette (solde) ; figure 7 : service de la dette -----
SERIE_SOLDE = "budget-solde-dette"
SERIE_SERVICE = "budget-service-dette"
_SOLDE_L = {
    "v_deficit": {"fr": "déficit budgétaire (% du PIB)", "ar": "العجز (٪ من الناتج)"},
    "v_dette":   {"fr": "encours de la dette (% du PIB)", "ar": "الدين القائم (٪ من الناتج)"},
    "y_def":     {"fr": "déficit, en % du PIB",          "ar": "العجز، ٪ من الناتج"},
    "y_dette":   {"fr": "encours, en % du PIB",          "ar": "الدين، ٪ من الناتج"},
    "l_princ":   {"fr": "principal remboursé",           "ar": "أصل الدين"},
    "l_inter":   {"fr": "intérêts",                      "ar": "الفوائد"},
    "v_md":      {"fr": "en dinars (millions)",          "ar": "بالدينار (مليون)"},
    "v_part_dep": {"fr": "intérêts, en % des dépenses hors dette",
                   "ar": "الفوائد، ٪ من النفقات دون الدين"},
}


def _sl(key):
    st = _SOLDE_L[key]
    return st.get(figtools.lang(), st["fr"])


def _trace_pct_par_base(d: pd.DataFrame, col: str, ylabel: str):
    """Un ratio publié au PIB, tracé par plage contiguë de base (jamais en continu)."""
    d = d.dropna(subset=[col]).copy()
    d["base_cle"] = d["base_pib"].map(_base_cle)
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    vues = {}
    for plage in _plages(d):
        cle = plage["base_cle"].iloc[0]
        coul = _C_BASE[cle]
        lab = _lab("l_base", b=cle) if cle != "autre" else _lab("l_nonratt")
        style = dict(marker="o", color=coul)
        if len(plage) == 1:
            ax.plot(plage["annee"], plage[col], ms=5, ls="none", **style)
        else:
            ax.plot(plage["annee"], plage[col], ms=3, lw=1.8, **style)
        vues.setdefault(lab, coul)
    from matplotlib.lines import Line2D
    ax.legend([Line2D([], [], color=c, marker="o", lw=1.8) for c in vues.values()],
              [figtools.fig_text(k) for k in vues], fontsize=9)
    ax.axhline(0, color="grey", lw=0.8)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(figtools.fig_text(ylabel))
    ax.grid(alpha=0.25)
    fig.tight_layout()
    return fig


def vues_solde():
    d = figtools.series(SERIE_SOLDE)
    return [
        (_sl("v_deficit"), _trace_pct_par_base(d, "deficit_pct_pib", _sl("y_def"))),
        (_sl("v_dette"),   _trace_pct_par_base(d, "dette_pct_pib", _sl("y_dette"))),
    ]


def table_solde() -> pd.DataFrame:
    return figtools.series(SERIE_SOLDE)


def _service() -> pd.DataFrame:
    return figtools.series(SERIE_SERVICE).sort_values("annee")


def fig_service_md():
    d = _service()
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.stackplot(d["annee"], d["principal_MDT"], d["interets_MDT"],
                 labels=[figtools.fig_text(_sl("l_princ")), figtools.fig_text(_sl("l_inter"))],
                 colors=["#999999", "#c0392b"])
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_md"))
    ax.set_xlim(d["annee"].min(), d["annee"].max())
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    return fig


def fig_service_part():
    """Intérêts rapportés aux dépenses hors dette : ce que l'exclusion du service masque."""
    d = _service().merge(
        figtools.series(SERIE_NATURE)[["annee", "total_hors_dette_MDT"]], on="annee")
    d["part"] = 100 * d["interets_MDT"] / d["total_hors_dette_MDT"]
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.plot(d["annee"], d["part"], color="#c0392b", lw=1.8, marker="o", ms=3)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(figtools.fig_text(_sl("v_part_dep")))
    ax.grid(alpha=0.25)
    fig.tight_layout()
    return fig


def vues_service():
    return [
        (_sl("v_md"),       fig_service_md()),
        (_sl("v_part_dep"), fig_service_part()),
    ]


# --- figure 10 : qui dépense — les missions (depuis 2020) ---------------------
SERIE_MISSIONS = "budget-missions-vote"
_MI_L = {
    "v_2025": {"fr": "les missions du budget 2025",        "ar": "مهمات ميزانية 2025"},
    "v_evo":  {"fr": "évolution 2021-2025 (principales missions)", "ar": "التطور 2021-2025"},
    "l_reste": {"fr": "autres missions",                   "ar": "مهمات أخرى"},
}


def _mi(key):
    st = _MI_L[key]
    return st.get(figtools.lang(), st["fr"])


def fig_missions_2025():
    d = figtools.series(SERIE_MISSIONS)
    d = d[d["annee"] == 2025].dropna(subset=["plf_MDT"]).sort_values("plf_MDT")
    top = d.nlargest(12, "plf_MDT").sort_values("plf_MDT")
    reste = d[~d["mission_fr"].isin(top["mission_fr"])]["plf_MDT"].sum()
    labels = [figtools.fig_text(_mi("l_reste"))] + [figtools.fig_text(m) for m in top["mission_fr"]]
    vals = [reste] + top["plf_MDT"].tolist()
    couleurs = ["#bbbbbb"] + ["#c0392b" if t == "speciale" else "#1f4e79"
                              for t in top["type"]]
    fig, ax = plt.subplots(figsize=(9.5, 6.2))
    ax.barh(range(len(vals)), vals, color=couleurs)
    ax.set_yticks(range(len(vals)), labels, fontsize=8)
    ax.set_xlabel(_ft("y_md"))
    ax.grid(alpha=0.25, axis="x")
    fig.tight_layout()
    return fig


def fig_missions_evo():
    d = figtools.series(SERIE_MISSIONS).dropna(subset=["plf_MDT"])
    top6 = d[d["annee"] == 2025].nlargest(6, "plf_MDT")["mission_fr"]
    pal = ["#1f4e79", "#e08214", "#c0392b", "#1a9850", "#8e44ad", "#4393c3"]
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    for m, c in zip(top6, pal):
        s = d[d["mission_fr"] == m].sort_values("annee")
        ax.plot(s["annee"], s["plf_MDT"], color=c, lw=1.8, marker="o", ms=3,
                label=figtools.fig_text(m))
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_md"))
    ax.set_xticks(sorted(d["annee"].unique()))
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    return fig


def vues_missions():
    return [
        (_mi("v_2025"), fig_missions_2025()),
        (_mi("v_evo"),  fig_missions_evo()),
    ]


def table_missions() -> pd.DataFrame:
    return figtools.series(SERIE_MISSIONS)


# --- figure 12 : l'exécuté par mission (RAP, 2016-2023) -----------------------
SERIE_MISSIONS_EXE = "budget-missions-execute"
_ME_L = {
    "v_evo":  {"fr": "payé par mission, 2016-2023",  "ar": "المدفوع حسب المهمة"},
    "v_taux": {"fr": "taux d'exécution (payé / voté), 2021-2023", "ar": "نسبة الإنجاز"},
    "y_taux": {"fr": "payé, en % des crédits du PLF", "ar": "المدفوع، ٪ من اعتمادات المشروع"},
}
_ME_TOP = [("education", "Éducation", "#1f4e79"),
           ("industrie-energie", "Industrie, mines et énergie", "#e08214"),
           ("sante", "Santé", "#c0392b"),
           ("affaires-sociales", "Affaires sociales", "#8e44ad"),
           ("agriculture", "Agriculture", "#1a9850"),
           ("enseignement-superieur", "Enseignement supérieur", "#4393c3")]


def _me(key):
    st = _ME_L[key]
    return st.get(figtools.lang(), st["fr"])


def fig_missions_exe_evo():
    d = figtools.series(SERIE_MISSIONS_EXE)
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    for cle, lab, c in _ME_TOP:
        s = d[d["mission"] == cle].dropna(subset=["paye_MDT"]).sort_values("annee")
        if s.empty:
            continue
        ax.plot(s["annee"], s["paye_MDT"], color=c, lw=1.8, marker="o", ms=3,
                label=figtools.fig_text(lab))
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_md"))
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    return fig


def fig_missions_exe_taux():
    """Payé rapporté aux crédits du PLF de la même année (2021-2023)."""
    e = figtools.series(SERIE_MISSIONS_EXE)
    v = figtools.series(SERIE_MISSIONS)
    # correspondance des libellés : clés du dépouillement → mission_fr du voté
    corr = {"education": ["Éducation"],
            "industrie-energie": ["Industrie, mines et énergie", "Industrie, énergie et mines"],
            "sante": ["Santé"], "affaires-sociales": ["Affaires sociales"],
            "agriculture": ["Agriculture, ressources hydrauliques et pêche"],
            "enseignement-superieur": ["Enseignement supérieur et recherche scientifique"]}
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    pal = {k: c for k, _, c in _ME_TOP}
    for cle, lab, c in _ME_TOP:
        mv = corr.get(cle, [])
        sv = v[v["mission_fr"].isin(mv)][["annee", "plf_MDT"]]
        se = e[(e["mission"] == cle)][["annee", "paye_MDT"]]
        m = sv.merge(se, on="annee").dropna()
        m = m[m["annee"] >= 2021]
        if m.empty:
            continue
        ax.plot(m["annee"], 100 * m["paye_MDT"] / m["plf_MDT"], color=c, lw=1.8,
                marker="o", ms=4, label=figtools.fig_text(lab))
    ax.axhline(100, color="grey", lw=0.8, ls="--")
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(figtools.fig_text(_me("y_taux")))
    ax.set_xticks([2021, 2022, 2023])
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8, loc="upper left", ncol=2)
    fig.tight_layout()
    return fig


def vues_missions_execute():
    return [
        (_me("v_evo"),  fig_missions_exe_evo()),
        (_me("v_taux"), fig_missions_exe_taux()),
    ]


def table_missions_execute() -> pd.DataFrame:
    return figtools.series(SERIE_MISSIONS_EXE)


# --- figure 11 : qui dépensait — les chapitres (BOOST, 2008-2014) -------------
SERIE_CHAPITRES = "budget-chapitres-paye"
_CH_L = {
    "v_2014": {"fr": "les chapitres du budget payé 2014", "ar": "أبواب الميزانية 2014"},
    "v_evo":  {"fr": "évolution 2008-2014 (principaux chapitres)", "ar": "التطور 2008-2014"},
    "l_reste": {"fr": "autres chapitres", "ar": "أبواب أخرى"},
}


def _ch(key):
    st = _CH_L[key]
    return st.get(figtools.lang(), st["fr"])


def _chap_court(c: str) -> str:
    return (c.replace("Ministère de la ", "").replace("Ministère de l'", "")
             .replace("Ministère des ", "").replace("Ministère du ", "")
             .replace("Ministère de ", ""))


def fig_chapitres_2014():
    d = figtools.series(SERIE_CHAPITRES)
    d = d[d["annee"] == 2014].copy()
    top = d.nlargest(12, "paye_MDT").sort_values("paye_MDT")
    reste = d[~d["chapitre"].isin(top["chapitre"])]["paye_MDT"].sum()
    labels = [figtools.fig_text(_ch("l_reste"))] + \
             [figtools.fig_text(_chap_court(c)) for c in top["chapitre"]]
    vals = [reste] + top["paye_MDT"].tolist()
    coul = ["#bbbbbb"] + ["#c0392b" if "Dette" in c else "#1f4e79" for c in top["chapitre"]]
    fig, ax = plt.subplots(figsize=(9.5, 6.2))
    ax.barh(range(len(vals)), vals, color=coul)
    ax.set_yticks(range(len(vals)), labels, fontsize=8)
    ax.set_xlabel(_ft("y_md"))
    ax.grid(alpha=0.25, axis="x")
    fig.tight_layout()
    return fig


def fig_chapitres_evo():
    d = figtools.series(SERIE_CHAPITRES)
    top6 = d[d["annee"] == 2014].nlargest(6, "paye_MDT")["chapitre"]
    pal = ["#c0392b", "#1f4e79", "#e08214", "#1a9850", "#8e44ad", "#4393c3"]
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    for c, col in zip(top6, pal):
        s = d[d["chapitre"] == c].sort_values("annee")
        ax.plot(s["annee"], s["paye_MDT"], color=col, lw=1.8, marker="o", ms=3,
                label=figtools.fig_text(_chap_court(c)))
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_md"))
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    return fig


def vues_chapitres():
    return [
        (_ch("v_2014"), fig_chapitres_2014()),
        (_ch("v_evo"),  fig_chapitres_evo()),
    ]


def table_chapitres() -> pd.DataFrame:
    return figtools.series(SERIE_CHAPITRES)


# --- figure 9 : recettes totales face aux dépenses ----------------------------
SERIE_RECETTES_TOT = "budget-recettes-totales"
_RT_L = {
    "v_face":  {"fr": "recettes et dépenses (millions de dinars)", "ar": "الموارد والنفقات (مليون دينار)"},
    "l_fisc":  {"fr": "recettes fiscales",            "ar": "موارد جبائية"},
    "l_nf":    {"fr": "recettes non fiscales (y c. dons, privatisation)", "ar": "موارد غير جبائية"},
    "l_dep":   {"fr": "dépenses hors dette",          "ar": "النفقات دون الدين"},
    "l_dep_i": {"fr": "dépenses + intérêts",          "ar": "النفقات + الفوائد"},
}


def _rt(key):
    st = _RT_L[key]
    return st.get(figtools.lang(), st["fr"])


def fig_recettes_totales():
    d = figtools.series(SERIE_RECETTES_TOT).merge(
        figtools.series(SERIE_NATURE)[["annee", "total_hors_dette_MDT"]], on="annee")
    d = d.merge(figtools.series(SERIE_SERVICE)[["annee", "interets_MDT"]], on="annee", how="left")
    d = d.sort_values("annee")
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.stackplot(d["annee"], d["recettes_fiscales_MDT"], d["recettes_non_fiscales_MDT"],
                 labels=[figtools.fig_text(_rt("l_fisc")), figtools.fig_text(_rt("l_nf"))],
                 colors=["#1a9850", "#a6d96a"])
    ax.plot(d["annee"], d["total_hors_dette_MDT"], color="#c0392b", lw=1.8,
            label=figtools.fig_text(_rt("l_dep")))
    ax.plot(d["annee"], d["total_hors_dette_MDT"] + d["interets_MDT"], color="#c0392b",
            lw=1.2, ls="--", label=figtools.fig_text(_rt("l_dep_i")))
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_md"))
    ax.set_xlim(d["annee"].min(), d["annee"].max())
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    return fig


def table_recettes_totales() -> pd.DataFrame:
    d = figtools.series(SERIE_RECETTES_TOT).merge(
        figtools.series(SERIE_NATURE)[["annee", "total_hors_dette_MDT"]], on="annee", how="left")
    return d


# --- figure 8 : du voté au réalisé (écart d'exécution) ------------------------
SERIE_VOTE_REALISE = "budget-vote-realise"
_EXEC_L = {
    "v_total":  {"fr": "dépassement du voté, total (%)",      "ar": "تجاوز المصوّت، المجموع (٪)"},
    "v_nature": {"fr": "dépassement par nature (%)",          "ar": "التجاوز حسب الطبيعة (٪)"},
    "y_ecart":  {"fr": "réalisé − voté, en % du voté (LF)",   "ar": "المنجز − المصوّت، ٪ من المصوّت"},
    "l_total":  {"fr": "total hors dette",                    "ar": "المجموع دون الدين"},
}


def _xl(key):
    st = _EXEC_L[key]
    return st.get(figtools.lang(), st["fr"])


def _ecarts_execution() -> pd.DataFrame:
    """Écart réalisé − LF en % du LF, par nature, pour les années où les deux existent."""
    d = figtools.series(SERIE_VOTE_REALISE)
    cols = ["total_hors_dette_MDT", "remunerations_MDT", "interventions_MDT", "equipement_MDT"]
    lf = d[d["etat"] == "LF"].set_index("annee")[cols]
    re = d[d["etat"] == "realise"].set_index("annee")[cols]
    annees = lf.index.intersection(re.index)
    return (100 * (re.loc[annees] - lf.loc[annees]) / lf.loc[annees]).sort_index()


def fig_execution_total():
    e = _ecarts_execution()["total_hors_dette_MDT"]
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.bar(e.index, e.values, color=["#c0392b" if v > 0 else "#1f4e79" for v in e.values])
    ax.axhline(0, color="grey", lw=0.8)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(figtools.fig_text(_xl("y_ecart")))
    ax.grid(alpha=0.25, axis="y")
    fig.tight_layout()
    return fig


def fig_execution_nature():
    e = _ecarts_execution()
    spec = [("remunerations_MDT", "n_remun", "#1f4e79"),
            ("interventions_MDT", "n_interv", "#c0392b"),
            ("equipement_MDT", "n_equip", "#1a9850")]
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    for col, k, c in spec:
        ax.plot(e.index, e[col], color=c, lw=1.8, marker="o", ms=3, label=_ft(k))
    ax.plot(e.index, e["total_hors_dette_MDT"], color="#555555", lw=1.4, ls="--",
            label=figtools.fig_text(_xl("l_total")))
    ax.axhline(0, color="grey", lw=0.8)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(figtools.fig_text(_xl("y_ecart")))
    ax.grid(alpha=0.25)
    ax.legend(fontsize=9, loc="upper left")
    fig.tight_layout()
    return fig


def vues_execution():
    return [
        (_xl("v_total"),  fig_execution_total()),
        (_xl("v_nature"), fig_execution_nature()),
    ]


def table_execution() -> pd.DataFrame:
    return figtools.series(SERIE_VOTE_REALISE)


def table_service() -> pd.DataFrame:
    d = _service().merge(
        figtools.series(SERIE_NATURE)[["annee", "total_hors_dette_MDT"]], on="annee", how="left")
    d["interets_pct_depenses_hors_dette"] = (
        100 * d["interets_MDT"] / d["total_hors_dette_MDT"]).round(1)
    return d


def _apu_lab(key):
    st = _APU_L[key]
    return st.get(figtools.lang(), st["fr"])


def _apu_base2015() -> pd.DataFrame:
    d = figtools.series(SERIE_APU)
    if "perimetre" in d.columns:  # la série porte aussi le sous-secteur « central » (données)
        d = d[d["perimetre"] == "apu"]
    d = d[d["base_pib"] == 2015].sort_values("annee").drop_duplicates("annee")
    return d


def _trace_comptanat(d: pd.DataFrame, en_part: bool):
    """Empilement des emplois APU, en dinars ou en part de leur total."""
    tot = sum(d[c] for c, _, _ in _APU) if en_part else 1.0
    series = [100 * d[c] / tot if en_part else d[c] for c, _, _ in _APU]
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.stackplot(d["annee"], *series,
                 labels=[figtools.fig_text(_apu_lab(k)) for _, k, _ in _APU],
                 colors=[c for *_, c in _APU])
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(figtools.fig_text("en % des emplois APU") if en_part else _ft("y_md"))
    ax.set_xlim(d["annee"].min(), d["annee"].max())
    if en_part:
        ax.set_ylim(0, 100)
    ax.legend(fontsize=8, loc="lower right", ncol=2, framealpha=0.9)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    return fig


def vues_comptanat():
    """Emplois du compte des administrations publiques par nature, base 2015 (2017-2024).

    Deux vues : part du total des emplois APU, et dinars. Segment base 2015 seul (bases non
    chaînées). Périmètre APU (central + local + sécurité sociale) — ne boucle pas sur les
    dépenses de l'État.
    """
    d = _apu_base2015()
    return [
        (_lab("v_part"), _trace_comptanat(d, en_part=True)),
        (_lab("v_md"),   _trace_comptanat(d, en_part=False)),
    ]


def table_comptanat() -> pd.DataFrame:
    d = figtools.series(SERIE_APU)
    cols = (["perimetre", "annee", "base_pib"] + [c for c, _, _ in _APU]
            + ["subventions_produits_MDT", "subventions_MDT", "edition"])
    return d[[c for c in cols if c in d.columns]]

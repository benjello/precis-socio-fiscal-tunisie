"""Figures de la longue période du volume « Le marché du travail ».

    from figures import marche_travail as mt
    mt.vues_nominal(), mt.table_nominal()   # SMIG des deux régimes, au mois, dinars courants
    mt.vues_reel(), mt.table_reel()         # SMIG 48 h et SMAG, moyenne annuelle, dinars de 2023
    mt.vues_rapports(), mt.table_rapports() # 40 h / 48 h à l'heure ; SMAG / journée de 8 h au SMIG

D'OÙ VIENNENT LES DONNÉES. Le module ne lit que `figtools.series()` :

  - `marche-travail-smig-smag` : le SMIG des deux régimes, à l'heure et au mois, et le SMAG
    journalier, à chaque date d'effet ; règles de droit datées, émises hors du build par
    `scripts/generate_marche_travail_tables.py` avec leurs liens « Base législative » ;
  - `ipc-longue-periode` : l'indice des prix à la consommation, base 100 en 1970, 1962-2023,
    snapshoté depuis l'entrepôt `tunisia-data`.

CONVENTIONS.
  - Moyenne annuelle : moyenne des montants en vigueur au premier jour de chacun des douze
    mois. Une hausse du 1er mai compte donc pour huit mois de l'année.
  - Dinars constants : moyenne annuelle × IPC(2023) / IPC(année). 2023 est la dernière année
    de l'indice.
  - SMAG rapporté au SMIG : le SMAG d'une journée, divisé par huit heures au SMIG horaire du
    régime de 48 heures (le régime de 48 heures compte 208 heures par mois, soit 26 journées
    de 8 heures).
  - Les montants de 1961 à mai 1968 sont ceux du minimum de la première zone ; de 1971 à 1973,
    l'indemnité de cherté de vie, servie en sus du minimum, n'y est pas comprise.
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "marche-travail-smig-smag"
SERIE_IPC = "ipc-longue-periode"
ANNEE_BASE = 2023

BLEU, ORANGE, VERT, GRIS = "#08519c", "#bc4c00", "#1a7f37", "#6e7781"

figtools.register_provenance(
    SERIE,
    titre=("Salaire minimum interprofessionnel garanti (régimes de 48 et de 40 heures, à "
           "l'heure et au mois) et salaire minimum agricole garanti (par journée), à chaque "
           "date d'effet, 1961-2028"),
    titre_ar=("الأجر الأدنى المضمون لمختلف المهن (نظاما 48 و40 ساعة، بالساعة وبالشهر) والأجر "
              "الأدنى الفلاحي المضمون (باليوم)، في كلّ تاريخ سريان، 1961-2028"),
    sources=["decret61-145", "decret74-63", "decret74-571", "decret81-437", "decret92-1299",
             "decret2026-66", "decret2026-67"],
    unite="dinars courants",
    unite_ar="دينار جارٍ",
    perimetre=("montants fixés par les décrets, pour les salariés de 18 ans et plus ; une ligne "
               "par date d'effet, chaque colonne donnant le montant en vigueur à cette date"),
    perimetre_ar=("المبالغ التي تضبطها الأوامر للأجراء البالغين 18 سنة فما فوق؛ سطر لكلّ تاريخ "
                  "سريان"),
    caveats=("Avant le 1er mai 1968, minimum de la première zone seulement. De 1971 à 1973, "
             "l'indemnité de cherté de vie de 0,020 D l'heure, servie en sus du minimum et hors "
             "assiette sociale, n'est pas comprise ; le SMIG l'intègre le 1er janvier 1974. "
             "Avant 1974, les montants mensuels sont la conversion du minimum horaire. Les "
             "indemnités spéciales de 1989 et de 1991 ne sont pas comprises."),
    caveats_ar=("قبل غرّة ماي 1968، الأجر الأدنى للمنطقة الأولى فقط. ومن 1971 إلى 1973 لا تشمل "
                "المبالغ منحة غلاء المعيشة. ولا تشمل المنحتين الخاصّتين لسنتي 1989 و1991."),
)

_L = {
    "x_annee": {"fr": "Année", "ar": "السنة"},
    "y_dinars": {"fr": "Dinars courants par mois", "ar": "دينار جارٍ في الشهر"},
    "y_reel": {"fr": f"Dinars de {ANNEE_BASE} par mois", "ar": f"دينار سنة {ANNEE_BASE} في الشهر"},
    "y_ratio": {"fr": "Rapport", "ar": "النسبة"},
    "lg_48": {"fr": "SMIG, régime de 48 heures", "ar": "الأجر الأدنى المضمون، نظام 48 ساعة"},
    "lg_40": {"fr": "SMIG, régime de 40 heures", "ar": "الأجر الأدنى المضمون، نظام 40 ساعة"},
    "lg_smag26": {"fr": "SMAG × 26 journées", "ar": "الأجر الأدنى الفلاحي × 26 يومًا"},
    "lg_40_48": {"fr": "SMIG horaire, 40 heures / 48 heures",
                 "ar": "الأجر الأدنى بالساعة، نظام 40 ساعة / نظام 48 ساعة"},
    "lg_smag_smig": {"fr": "SMAG / 8 heures au SMIG horaire de 48 heures",
                     "ar": "الأجر الأدنى الفلاحي / 8 ساعات بالأجر الأدنى بالساعة (48 ساعة)"},
    "vue_lin": {"fr": "Échelle linéaire", "ar": "سلّم خطّي"},
    "vue_log": {"fr": "Échelle logarithmique", "ar": "سلّم لوغاريتمي"},
    "r_1974": {"fr": "SMIG", "ar": "الأجر الأدنى"},
    "r_1981": {"fr": "deux taux horaires", "ar": "نسبتان بالساعة"},
    "r_2026": {"fr": "décrets de 2026", "ar": "أوامر 2026"},
    # Colonnes des données.
    "c_date": {"fr": "date d'effet", "ar": "تاريخ السريان"},
    "c_annee": {"fr": "année", "ar": "السنة"},
    "c_48": {"fr": "SMIG 48 h, au mois (D)", "ar": "الأجر الأدنى 48 ساعة، بالشهر (د)"},
    "c_40": {"fr": "SMIG 40 h, au mois (D)", "ar": "الأجر الأدنى 40 ساعة، بالشهر (د)"},
    "c_smag": {"fr": "SMAG, par jour (D)", "ar": "الأجر الأدنى الفلاحي، باليوم (د)"},
    "c_48_moy": {"fr": "SMIG 48 h, moyenne annuelle (D courants)",
                 "ar": "الأجر الأدنى 48 ساعة، المعدّل السنوي (د جارية)"},
    "c_48_reel": {"fr": f"SMIG 48 h, moyenne annuelle (D de {ANNEE_BASE})",
                  "ar": f"الأجر الأدنى 48 ساعة، المعدّل السنوي (د {ANNEE_BASE})"},
    "c_smag_reel": {"fr": f"SMAG × 26, moyenne annuelle (D de {ANNEE_BASE})",
                    "ar": f"الأجر الأدنى الفلاحي × 26، المعدّل السنوي (د {ANNEE_BASE})"},
    "c_ipc": {"fr": "IPC, base 100 en 1970", "ar": "الرقم القياسي للأسعار، أساس 100 سنة 1970"},
    "c_40_48": {"fr": "40 h / 48 h, à l'heure", "ar": "40 / 48 ساعة، بالساعة"},
    "c_smag_smig": {"fr": "SMAG / (8 × SMIG horaire 48 h)",
                    "ar": "الأجر الأدنى الفلاحي / (8 × الأجر الأدنى بالساعة 48 ساعة)"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _serie():
    d = figtools.series(SERIE).copy()
    d["jour"] = [dt.date.fromisoformat(x) for x in d["date"]]
    return d.sort_values("jour").reset_index(drop=True)


def _en_vigueur(d, colonne: str, jour: dt.date):
    lignes = d[d["jour"] <= jour]
    if lignes.empty:
        return None
    v = lignes[colonne].iloc[-1]
    return None if v != v else float(v)  # NaN : pas encore de valeur


def _moyenne_annuelle(d, colonne: str, annee: int):
    """Moyenne des montants en vigueur au premier jour de chacun des douze mois."""
    mois = [_en_vigueur(d, colonne, dt.date(annee, m, 1)) for m in range(1, 13)]
    if any(v is None for v in mois):
        return None
    return sum(mois) / 12


def _ipc() -> dict[int, float]:
    return {int(r.annee): float(r.indice_base1970)
            for r in figtools.series(SERIE_IPC).itertuples()}


def _escaliers(ax, d, colonne, facteur=1.0, **kw):
    x = [dt.datetime(j.year, j.month, j.day) for j in d["jour"]]
    y = [None if v != v else v * facteur for v in d[colonne]]
    paires = [(a, b) for a, b in zip(x, y) if b is not None]
    ax.plot([a for a, _ in paires], [b for _, b in paires], drawstyle="steps-post", **kw)


def _ruptures(ax, en_dates=True):
    for annee, cle in ((1974, "r_1974"), (1981, "r_1981"), (2026, "r_2026")):
        x = dt.datetime(annee, 1, 1) if en_dates else annee - 0.5
        ax.axvline(x, color="#57606a", ls=(0, (2, 2)), lw=1, zorder=1)
        ax.annotate(figtools.fig_text(_lab(cle)), xy=(x, 1), xycoords=("data", "axes fraction"),
                    xytext=(4, -4), textcoords="offset points", ha="left", va="top",
                    fontsize=7, color="#57606a")


# ---------------------------------------------------------------- SMIG nominal

def _fig_nominal(log: bool):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _serie()
    fig, ax = plt.subplots(figsize=(10, 5.6))
    _escaliers(ax, d, "smig_48h_mensuel", color=BLEU, lw=2, label=ft(_lab("lg_48")))
    _escaliers(ax, d, "smig_40h_mensuel", color=ORANGE, lw=1.6, label=ft(_lab("lg_40")))
    _escaliers(ax, d, "smag_journalier", facteur=26, color=VERT, lw=1.4, ls="--",
               label=ft(_lab("lg_smag26")))
    _ruptures(ax)
    if log:
        ax.set_yscale("log")
        ax.set_yticks([10, 20, 50, 100, 200, 500])
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
        ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_dinars")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def vues_nominal():
    return [(_lab("vue_lin"), _fig_nominal(False)), (_lab("vue_log"), _fig_nominal(True))]


def table_nominal():
    import pandas as pd
    d = _serie()
    return pd.DataFrame({
        _lab("c_date"): d["date"],
        _lab("c_48"): d["smig_48h_mensuel"],
        _lab("c_40"): d["smig_40h_mensuel"],
        _lab("c_smag"): d["smag_journalier"],
    })


# ---------------------------------------------------------------- SMIG réel

def _reel():
    d, ipc = _serie(), _ipc()
    lignes = []
    for annee in range(1962, ANNEE_BASE + 1):
        if annee not in ipc:
            continue
        smig = _moyenne_annuelle(d, "smig_48h_mensuel", annee)
        smag = _moyenne_annuelle(d, "smag_journalier", annee)
        coef = ipc[ANNEE_BASE] / ipc[annee]
        lignes.append((annee, smig, None if smig is None else smig * coef,
                       None if smag is None else smag * 26 * coef, ipc[annee]))
    return lignes


def fig_reel():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _reel()
    fig, ax = plt.subplots(figsize=(10, 5.6))
    ax.plot([a for a, *_ in r], [v for _, _, v, _, _ in r], "-o", ms=3, color=BLEU, lw=2,
            label=ft(_lab("lg_48")))
    pts = [(a, s) for a, _, _, s, _ in r if s is not None]
    ax.plot([a for a, _ in pts], [s for _, s in pts], "--", color=VERT, lw=1.4,
            label=ft(_lab("lg_smag26")))
    _ruptures(ax, en_dates=False)
    ax.set_ylim(0, None)
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_reel")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower right", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def vues_reel():
    return fig_reel()


def table_reel():
    import pandas as pd
    r = _reel()
    return pd.DataFrame({
        _lab("c_annee"): [a for a, *_ in r],
        _lab("c_48_moy"): [None if v is None else round(v, 3) for _, v, *_ in r],
        _lab("c_ipc"): [i for *_, i in r],
        _lab("c_48_reel"): [None if v is None else round(v, 1) for _, _, v, _, _ in r],
        _lab("c_smag_reel"): [None if v is None else round(v, 1) for _, _, _, v, _ in r],
    })


# ---------------------------------------------------------------- rapports

def _rapports():
    d = _serie()
    lignes = []
    for _, l in d.iterrows():
        h48, h40, smag = l["smig_48h_horaire"], l["smig_40h_horaire"], l["smag_journalier"]
        r1 = None if h48 != h48 or h40 != h40 else h40 / h48
        r2 = None if smag != smag or h48 != h48 else smag / (8 * h48)
        lignes.append((l["date"], l["jour"], r1, r2))
    return lignes


def fig_rapports():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _rapports()
    fig, ax = plt.subplots(figsize=(10, 5.2))
    for i, (cle, couleur) in enumerate((("lg_40_48", ORANGE), ("lg_smag_smig", VERT)), start=2):
        pts = [(dt.datetime(j.year, j.month, j.day), x[i]) for x in r
               for j in [x[1]] if x[i] is not None]
        ax.plot([a for a, _ in pts], [b for _, b in pts], drawstyle="steps-post", color=couleur,
                lw=1.8, label=ft(_lab(cle)))
    ax.axhline(1, color=GRIS, lw=0.8)
    _ruptures(ax)
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_ratio")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower right", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def vues_rapports():
    return fig_rapports()


def table_rapports():
    import pandas as pd
    r = _rapports()
    return pd.DataFrame({
        _lab("c_date"): [x[0] for x in r],
        _lab("c_40_48"): [None if x[2] is None else round(x[2], 3) for x in r],
        _lab("c_smag_smig"): [None if x[3] is None else round(x[3], 3) for x in r],
    })

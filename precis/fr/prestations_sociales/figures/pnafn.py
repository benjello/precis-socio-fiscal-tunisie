"""Figure de la série historique de l'allocation mensuelle du PNAFN."""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402
import openfisca_tables as ot  # noqa: E402

HERE = Path(__file__).resolve().parent
FIGDATA = HERE.parent / "figdata"
SERIE = "pnafn-allocation"
SERIE_PRIX_SOURCE = "croissances-revenus-prix"
SERIE_PRIX = "ipc-pnafn-base2015"
PRIX = "prix à la consommation"
ANNEE_BASE = 2015

figtools.register_provenance(
    SERIE,
    titre="Allocation mensuelle du programme national d'aide aux familles nécessiteuses",
    titre_ar="المنحة الشهرية للبرنامج الوطني لمساعدة العائلات المعوزة",
    sources=["arrete-2024-07-10-allocation-pauvres"],
    unite="dinars par mois (prix courants)",
    unite_ar="دينار في الشهر (أسعار جارية)",
    perimetre="montant mensuel de l'allocation du PNAFN",
    perimetre_ar="المبلغ الشهري لمنحة البرنامج الوطني لمساعدة العائلات المعوزة",
    caveats=("Les dates de tous les paliers et les montants antérieurs à 180 dinars "
             "restent à fiabiliser."),
    caveats_ar=("لا تزال تواريخ جميع المستويات والمبالغ السابقة لمبلغ 180 دينارًا "
                "بحاجة إلى توثيق."),
)

figtools.register_provenance(
    SERIE_PRIX,
    titre="Indice des prix à la consommation chaîné, base 100 = 2015, 1987-2018",
    titre_ar="مؤشر أسعار الاستهلاك المتسلسل، أساس 100 = 2015، 1987-2018",
    sources=["ins-annuaire"],
    unite="indice annuel moyen, base 100 = 2015",
    unite_ar="مؤشر سنوي متوسط، أساس 100 = 2015",
    perimetre="prix à la consommation familiale, ensemble des ménages tunisiens",
    perimetre_ar="أسعار الاستهلاك العائلي، مجموع الأسر التونسية",
    caveats=("Indice reconstitué par chaînage des taux annuels publiés par l'INS. "
             "Une date en cours d'année est déflatée par l'indice annuel moyen."),
    caveats_ar=("أُعيد تركيب المؤشر بتسلسل النسب السنوية التي نشرها المعهد الوطني "
                "للإحصاء. وتُعدّل القيمة المؤرخة أثناء السنة بالمؤشر السنوي المتوسط."),
)

_L = {
    "lg_nominal": {"fr": "Montant courant (paliers à fiabiliser)",
                    "ar": "المبلغ الجاري (مستويات تحتاج إلى توثيق)"},
    "lg_reel": {"fr": "Valeur au changement de palier (dinars constants de 2015)",
                 "ar": "القيمة عند تغيّر المستوى (بالدينار الثابت لسنة 2015)"},
    "y": {"fr": "Dinars courants par mois", "ar": "دينار جار في الشهر"},
    "y_reel": {"fr": "Dinars constants de 2015 par mois",
                "ar": "دينار ثابت لسنة 2015 في الشهر"},
    "x": {"fr": "Année", "ar": "السنة"},
    "titre": {"fr": "Allocation mensuelle du PNAFN, 1987-2018",
               "ar": "المنحة الشهرية للبرنامج الوطني لمساعدة العائلات المعوزة، 1987-2018"},
    "col_date": {"fr": "Date de l'état", "ar": "تاريخ الحالة"},
    "col_montant": {"fr": "Allocation mensuelle (D courants)",
                    "ar": "المنحة الشهرية (بالدينار الجاري)"},
    "col_reel": {"fr": "Valeur au changement de palier (D constants de 2015)",
                 "ar": "القيمة عند تغيّر المستوى (بالدينار الثابت لسنة 2015)"},
    "col_att": {"fr": "Attestation", "ar": "الإثبات"},
    "a_documenter": {"fr": "À fiabiliser", "ar": "يحتاج إلى توثيق"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _serie():
    """Lit la série brute conservée dans le snapshot versionné."""
    df = figtools.series(SERIE)
    return [(str(date)[:10], float(valeur), str(atteste).strip().lower() == "oui")
            for date, valeur, atteste in zip(df["date"], df["montant"], df["atteste"])]


def _indices_prix():
    """Indice annuel chaîné des prix, base 100 en 2015."""
    df = figtools.series(SERIE_PRIX_SOURCE)
    taux = {int(r.annee): float(r.croissance_pct)
            for r in df.itertuples() if r.indicateur == PRIX}
    indices = {ANNEE_BASE: 100.0}
    for annee in range(ANNEE_BASE, min(taux), -1):
        indices[annee - 1] = indices[annee] / (1 + taux[annee] / 100)
    for annee in range(ANNEE_BASE + 1, max(taux) + 1):
        indices[annee] = indices[annee - 1] * (1 + taux[annee] / 100)
    return indices


def _serie_reelle():
    """Montant de chaque palier en dinars constants de 2015, à sa date d'entrée."""
    indices = _indices_prix()
    return [(date, montant * 100 / indices[int(date[:4])], atteste)
            for date, montant, atteste in _serie()]


def table():
    import pandas as pd
    reels = {date: montant for date, montant, _atteste in _serie_reelle()}
    lignes = [
        {_lab("col_date"): ot.formate_date(d, figtools.lang()),
         _lab("col_montant"): ot.formate_dinars(v),
         _lab("col_reel"): ot.formate_dinars(round(reels[d], 1)),
         _lab("col_att"): _lab("a_documenter")}
        for d, v, _a in _serie()
    ]
    return pd.DataFrame(lignes)


def prepare(generated: str | None = None):
    figtools.write_figdata(
        table(), FIGDATA / "fig_pnafn_allocation.csv", SERIE, SERIE_PRIX,
        note=("allocation mensuelle du PNAFN, onze paliers de 1987 à 2018, en dinars "
              "courants et en dinars constants de 2015"),
        generated=generated)


def fig_allocation():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    serie = _serie()
    annees = [int(d[:4]) + (int(d[5:7]) - 1) / 12 for d, _, _ in serie]
    montants = [v for _, v, _ in serie]
    non_att = [(a, m) for (a, m), (_, _, att) in zip(zip(annees, montants), serie) if not att]
    fig, ax = plt.subplots(figsize=(9.5, 5))
    ax.step(annees, montants, where="post", color="#8b949e", lw=2,
            ls=":", label=ft(_lab("lg_nominal")))
    ax.scatter([a for a, _ in non_att], [m for _, m in non_att], color="#8b949e",
               s=42, zorder=4)

    reels = [v for _, v, _ in _serie_reelle()]
    ax_reel = ax.twinx()
    ax_reel.plot(annees, reels, color="#b45309", lw=2, ls="--",
                 marker="D", markersize=4.5, label=ft(_lab("lg_reel")))

    ax.set_ylabel(ft(_lab("y")))
    ax_reel.set_ylabel(ft(_lab("y_reel")), color="#b45309")
    ax_reel.tick_params(axis="y", colors="#b45309")
    ax.set_xlabel(ft(_lab("x")))
    ax.set_title(ft(_lab("titre")))
    ax.grid(True, alpha=0.3)
    lignes, libelles = ax.get_legend_handles_labels()
    lignes_reelles, libelles_reels = ax_reel.get_legend_handles_labels()
    ax.legend(lignes + lignes_reelles, libelles + libelles_reels,
              loc="upper left", fontsize=8.5)
    fig.tight_layout()
    return fig

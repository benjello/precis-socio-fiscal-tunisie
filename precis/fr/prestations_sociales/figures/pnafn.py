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
SERIE_PRIX = "ipc-pnafn-base1987"
PRIX = "prix à la consommation"
ANNEE_BASE = 1987

figtools.register_provenance(
    SERIE,
    titre="Allocation mensuelle du programme national d'aide aux familles nécessiteuses",
    titre_ar="المنحة الشهرية للبرنامج الوطني لمساعدة العائلات المعوزة",
    sources=["arrete-2024-07-10-allocation-pauvres", "ins-annuaire"],
    unite="dinars par mois (prix courants et constants de 1987)",
    unite_ar="دينار في الشهر (بالأسعار الجارية والثابتة لسنة 1987)",
    perimetre="montant mensuel de l'allocation du PNAFN",
    perimetre_ar="المبلغ الشهري لمنحة البرنامج الوطني لمساعدة العائلات المعوزة",
    caveats=("Les dates de tous les paliers et les montants antérieurs à 180 dinars "
             "restent à fiabiliser. Le pouvoir d'achat est calculé avec l'indice annuel "
             "moyen des prix à la consommation."),
    caveats_ar=("لا تزال تواريخ جميع المستويات والمبالغ السابقة لمبلغ 180 دينارًا "
                "بحاجة إلى توثيق. وتُحسب القوة الشرائية بمؤشر أسعار الاستهلاك السنوي المتوسط."),
)

figtools.register_provenance(
    SERIE_PRIX,
    titre="Indice des prix à la consommation chaîné, base 100 = 1987, 1987-2018",
    titre_ar="مؤشر أسعار الاستهلاك المتسلسل، أساس 100 = 1987، 1987-2018",
    sources=["ins-annuaire"],
    unite="indice annuel moyen, base 100 = 1987",
    unite_ar="مؤشر سنوي متوسط، أساس 100 = 1987",
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
    "lg_reel": {"fr": "Pouvoir d'achat (dinars constants de 1987)",
                 "ar": "القوة الشرائية (بالدينار الثابت لسنة 1987)"},
    "y": {"fr": "Dinars par mois (courants et constants de 1987)",
          "ar": "دينار في الشهر (جار وثابت لسنة 1987)"},
    "x": {"fr": "Année", "ar": "السنة"},
    "titre": {"fr": "Allocation mensuelle du PNAFN, 1987-2018",
               "ar": "المنحة الشهرية للبرنامج الوطني لمساعدة العائلات المعوزة، 1987-2018"},
    "col_date": {"fr": "Date de l'état", "ar": "تاريخ الحالة"},
    "col_montant": {"fr": "Allocation mensuelle (D courants)",
                    "ar": "المنحة الشهرية (بالدينار الجاري)"},
    "col_reel": {"fr": "Pouvoir d'achat (D constants de 1987)",
                 "ar": "القوة الشرائية (بالدينار الثابت لسنة 1987)"},
    "col_type": {"fr": "Point de mesure", "ar": "نقطة القياس"},
    "palier": {"fr": "Changement de palier", "ar": "تغيّر المستوى"},
    "annuel": {"fr": "Repère annuel", "ar": "مرجع سنوي"},
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
    """Indice annuel chaîné des prix, base 100 en 1987."""
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
    """Montant applicable aux dates de palier et à chaque début d'année, en dinars de 1987."""
    paliers = _serie()
    dates_paliers = {date for date, _montant, _atteste in paliers}
    debut, fin = int(paliers[0][0][:4]), int(paliers[-1][0][:4])
    dates = sorted(dates_paliers | {f"{annee}-01-01" for annee in range(debut, fin + 1)})
    indices = _indices_prix()
    serie = []
    for date in dates:
        _date_palier, montant, atteste = next(
            palier for palier in reversed(paliers) if palier[0] <= date)
        serie.append((date, montant, montant * 100 / indices[int(date[:4])],
                      date in dates_paliers, atteste))
    return serie


def table():
    import pandas as pd
    lignes = [
        {_lab("col_date"): ot.formate_date(d, figtools.lang()),
         _lab("col_montant"): ot.formate_dinars(v),
         _lab("col_reel"): ot.formate_dinars(round(reel, 1)),
         _lab("col_type"): _lab("palier" if est_palier else "annuel"),
         _lab("col_att"): _lab("a_documenter")}
        for d, v, reel, est_palier, _a in _serie_reelle()
    ]
    return pd.DataFrame(lignes)


def prepare(generated: str | None = None):
    figtools.write_figdata(
        table(), FIGDATA / "fig_pnafn_allocation.csv", SERIE, SERIE_PRIX,
        note=("allocation mensuelle du PNAFN, onze paliers de 1987 à 2018, en dinars "
              "courants et en dinars constants de 1987"),
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

    serie_reelle = _serie_reelle()
    annees_reelles = [int(d[:4]) + (int(d[5:7]) - 1) / 12
                      for d, _v, _reel, _palier, _atteste in serie_reelle]
    reels = [reel for _d, _v, reel, _palier, _atteste in serie_reelle]
    ax.step(annees_reelles, reels, where="post", color="#b45309", lw=2, ls="--",
            label=ft(_lab("lg_reel")))
    points_paliers = [(annee, reel) for annee, (_d, _v, reel, palier, _atteste)
                      in zip(annees_reelles, serie_reelle) if palier]
    ax.scatter([annee for annee, _reel in points_paliers],
               [reel for _annee, reel in points_paliers],
               color="#b45309", marker="D", s=35, zorder=5)

    ax.set_ylabel(ft(_lab("y")))
    ax.set_xlabel(ft(_lab("x")))
    ax.set_title(ft(_lab("titre")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8.5)
    fig.tight_layout()
    return fig

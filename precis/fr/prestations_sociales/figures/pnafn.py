"""Figure « allocation du PNAFN » du livre *Prestations sociales*.

Origine des données : les PARAMÈTRES d'openfisca-tunisia, non l'entrepôt statistique. Le
montant de l'allocation aux familles nécessiteuses n'est pas une observation publiée mais
du droit codé — et, ici, du droit largement non écrit : dix des onze paliers ne reposent
sur aucun texte au Journal officiel.

La figure doit donc porter cette réserve, faute de quoi elle donnerait à onze décisions
administratives l'apparence d'une série statistique. Les paliers attestés et non attestés
sont distingués, et la légende le dit.
"""
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
PARAMETRE = "parameters/prestations/non_contributives/pnafn/allocation.yaml"

# Seul palier attesté par un texte publié : l'arrêté conjoint du 10 juillet 2024 constate
# que l'allocation « est fixée à 180 dinars à la date de la publication ».
PREMIER_PALIER_ATTESTE = "2018-04-01"

figtools.register_provenance(
    SERIE,
    titre="Allocation mensuelle du programme national d'aide aux familles nécessiteuses",
    titre_ar="المنحة الشهرية للبرنامج الوطني لمساعدة العائلات المعوزة",
    sources=["arrete-2024-07-10-allocation-pauvres", "loi-86-83-lfr-1986"],
    unite="dinars par mois (prix courants)",
    unite_ar="دينار في الشهر (أسعار جارية)",
    perimetre="valeurs encodées dans openfisca-tunisia, paramètre pnafn/allocation",
    perimetre_ar="القيم المدوّنة في openfisca-tunisia، معيار pnafn/allocation",
    caveats=("Dix des onze paliers ne reposent sur aucun texte publié au Journal officiel : "
             "ce sont des décisions administratives. Seul celui de 180 dinars est attesté, "
             "et par un arrêté de 2024 qui le constate sans le fixer."),
    caveats_ar=("عشرة من الأحد عشر مستوى لا تستند إلى أيّ نصّ منشور بالرائد الرسمي: فهي قرارات "
                "إدارية. ولا يثبت إلّا مستوى 180 ديناراً، بقرار لسنة 2024 يعاينه دون أن يضبطه."),
)

_L = {
    "lg_non": {"fr": "Paliers sans texte publié (décisions administratives)",
               "ar": "مستويات دون نصّ منشور (قرارات إدارية)"},
    "lg_oui": {"fr": "Palier attesté par un texte (arrêté du 10 juillet 2024)",
               "ar": "مستوى ثابت بنصّ (قرار 10 جويلية 2024)"},
    "y": {"fr": "Dinars par mois", "ar": "دينار في الشهر"},
    "x": {"fr": "Année", "ar": "السنة"},
    "titre": {"fr": "Allocation mensuelle du PNAFN, 1987-2018",
              "ar": "المنحة الشهرية للبرنامج الوطني لمساعدة العائلات المعوزة، 1987-2018"},
    "col_date": {"fr": "Date d'effet", "ar": "تاريخ السريان"},
    "col_montant": {"fr": "Allocation mensuelle (D)", "ar": "المنحة الشهرية (د)"},
    "col_att": {"fr": "Attestation", "ar": "الإثبات"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _serie():
    """(date ISO, montant, attesté) — lu directement dans le paramètre openfisca."""
    return [(date, valeur, bool(titre))
            for date, valeur, titre, _lien in ot.serie_datee(PARAMETRE)
            if valeur is not None]


def table():
    import pandas as pd
    lignes = [{_lab("col_date"): ot.formate_date(d, figtools.lang()),
               _lab("col_montant"): ot.formate_dinars(v),
               _lab("col_att"): ot.attestation("x" if a else "", figtools.lang())}
              for d, v, a in _serie()]
    return pd.DataFrame(lignes)


def prepare(generated: str | None = None):
    figtools.write_figdata(
        table(), FIGDATA / "fig_pnafn_allocation.csv", SERIE,
        note="allocation mensuelle du PNAFN, onze paliers de 1987 à 2018",
        generated=generated)


def fig_allocation():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    serie = _serie()
    annees = [int(d[:4]) + (int(d[5:7]) - 1) / 12 for d, _, _ in serie]
    montants = [v for _, v, _ in serie]
    # Le palier courant se prolonge jusqu'à aujourd'hui : la série s'arrête faute de
    # nouveau montant publié, non parce que l'allocation aurait cessé.
    annees_tracees = annees + [2026.0]
    montants_traces = montants + [montants[-1]]

    fig, ax = plt.subplots(figsize=(9.5, 5))
    ax.step(annees_tracees, montants_traces, where="post", color="#8b949e", lw=2,
            ls=":", label=ft(_lab("lg_non")))
    non_att = [(a, m) for (a, m), (_, _, att) in zip(zip(annees, montants), serie) if not att]
    att = [(a, m) for (a, m), (_, _, at) in zip(zip(annees, montants), serie) if at]
    ax.scatter([a for a, _ in non_att], [m for _, m in non_att], color="#8b949e",
               s=42, zorder=4)
    ax.scatter([a for a, _ in att], [m for _, m in att], color="#1f6feb", s=90, zorder=5,
               label=ft(_lab("lg_oui")))

    ax.set_ylabel(ft(_lab("y")))
    ax.set_xlabel(ft(_lab("x")))
    ax.set_title(ft(_lab("titre")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8.5)
    fig.tight_layout()
    return fig

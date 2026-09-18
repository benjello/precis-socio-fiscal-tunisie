"""Figure « titulaires de pensions par nature, 2000 et 2020 » (source CNSS).

    from figures import pensionnes_par_nature as pn
    pn.fig_nature()     # part de chaque nature de pension
    pn.table()          # effectifs et parts aux deux dates (onglet Données)

CE QUE LA FIGURE MONTRE. Le livre décrit les conditions d'ouverture du droit, nature par
nature ; il ne dit pas combien de personnes relèvent de chacune. Une pension de la CNSS
sur trois n'est pas une pension de retraite : ce sont des pensions de survie — conjoints
survivants et orphelins — dont le régime obéit à d'autres règles.

La composition se déforme, et dans deux directions opposées :
  - les **conjoints survivants** passent de 22,22 % à 23,99 % des titulaires, et de
    63 919 à 216 987 personnes ;
  - les **orphelins** reculent en part, de 15,29 % à 10,60 %, tout en doublant en nombre
    (43 984 à 95 847) — la part baisse parce que l'ensemble croît plus vite.

POURQUOI CES CHIFFRES SONT SÛRS. Les quatre natures de chaque année somment EXACTEMENT au
total de pensionnés de la série `cnss-effectifs`, établie sur une autre planche : 287 700
en 2000, 904 621 en 2020. Le contrôle est donc externe, et exact à l'unité — non à
l'arrondi près. C'est aussi ce bouclage, et non l'ordre de lecture, qui attribue chaque
bloc à son année : la planche affiche « Année 2020 » avant « Année 2000 » alors que ses
étiquettes sortent dans l'ordre inverse.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "cnss-pensionnes-par-nature"
ANNEES = (2000, 2020)
ORDRE = ("Retraités", "Conjoints survivants", "Orphelins", "Invalides")

_L = {
    "titre": {"fr": "CNSS : part de chaque nature de pension, 2000 et 2020",
              "ar": "الصندوق الوطني للضمان الاجتماعي: حصّة كلّ نوع من الجرايات، 2000 و2020"},
    "x": {"fr": "Part des titulaires de pensions (%)", "ar": "الحصّة من أصحاب الجرايات (٪)"},
    "lg_2000": {"fr": "2000", "ar": "2000"},
    "lg_2020": {"fr": "2020", "ar": "2020"},
    "col_nature": {"fr": "Nature de la pension", "ar": "نوع الجراية"},
    "col_e2000": {"fr": "Titulaires 2000", "ar": "أصحاب الجرايات 2000"},
    "col_e2020": {"fr": "Titulaires 2020", "ar": "أصحاب الجرايات 2020"},
    "col_p2000": {"fr": "Part 2000 (%)", "ar": "الحصّة 2000 (٪)"},
    "col_p2020": {"fr": "Part 2020 (%)", "ar": "الحصّة 2020 (٪)"},
}

_NATURES = {
    "Retraités": {"fr": "Retraite", "ar": "التقاعد"},
    "Conjoints survivants": {"fr": "Conjoints survivants", "ar": "البقاء"},
    "Orphelins": {"fr": "Orphelins", "ar": "الأيتام"},
    "Invalides": {"fr": "Invalidité", "ar": "العجز"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _nature(cle: str) -> str:
    return _NATURES[cle].get(figtools.lang(), _NATURES[cle]["fr"])


def _donnees():
    """[(nature, eff 2000, eff 2020, part 2000, part 2020)] dans l'ordre canonique."""
    par = {a: {} for a in ANNEES}
    for r in figtools.series(SERIE).itertuples():
        an = int(r.annee)
        if an in par:
            par[an][r.nature] = (int(r.effectif), float(r.part_publiee_pct))
    return [(n, par[2000][n][0], par[2020][n][0], par[2000][n][1], par[2020][n][1])
            for n in ORDRE]


def table():
    import pandas as pd
    return pd.DataFrame([
        {_lab("col_nature"): _nature(n),
         _lab("col_e2000"): e0,
         _lab("col_e2020"): e1,
         _lab("col_p2000"): p0,
         _lab("col_p2020"): p1}
        for n, e0, e1, p0, p1 in _donnees()])


def fig_nature():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    y = range(len(d))
    h = 0.38

    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    ax.barh([i + h / 2 for i in y], [p0 for *_, p0, _ in d], height=h,
            color="#9ecae1", label=ft(_lab("lg_2000")))
    ax.barh([i - h / 2 for i in y], [p1 for *_, p1 in d], height=h,
            color="#08519c", label=ft(_lab("lg_2020")))

    for i, (_, _, _, p0, p1) in enumerate(d):
        ax.text(p0 + 0.7, i + h / 2, f"{p0:.2f}".replace(".", ","),
                va="center", fontsize=7.5, color="#57606a")
        ax.text(p1 + 0.7, i - h / 2, f"{p1:.2f}".replace(".", ","),
                va="center", fontsize=7.5, color="#24292f")

    ax.set_yticks(list(y))
    ax.set_yticklabels([ft(_nature(n)) for n, *_ in d], fontsize=9)
    ax.invert_yaxis()
    ax.set_xlabel(ft(_lab("x")))
    ax.set_title(ft(_lab("titre")))
    # Borner sur LES DEUX années : la part de 2000 dépasse celle de 2020 pour les orphelins.
    ax.set_xlim(0, max(max(p0, p1) for *_, p0, p1 in d) * 1.15)
    ax.grid(True, axis="x", alpha=0.3)
    ax.legend(loc="lower right", fontsize=8.5)
    fig.tight_layout()
    return fig

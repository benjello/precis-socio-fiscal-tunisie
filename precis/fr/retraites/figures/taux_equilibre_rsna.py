"""Figures « taux de cotisation d'équilibre du régime des salariés non agricoles », 2000-2017.

    from figures import taux_equilibre_rsna as ter
    ter.fig_taux()             # taux d'équilibre et taux légal de la branche pensions
    ter.table()                # toutes les grandeurs (onglet Données)
    ter.fig_decomposition()    # indices base 100 en 2000 : taux, remplacement, rapport démographique
    ter.table_indices()        # les indices de la seconde figure (onglet Données)

Même construction que `taux_equilibre.py` (CNRPS). Le taux d'équilibre τ* est le taux de
cotisation qui, appliqué à la masse salariale déclarée, paierait exactement les pensions
servies dans l'année par le régime, sans le régime complémentaire :

    τ* = pensions ÷ masse déclarée = (pension moyenne ÷ salaire moyen) × (pensionnés ÷ cotisants)

où les cotisants sont les actifs du régime, non-assujettis compris (catalogue de la série).

La variante « avec régime complémentaire » est tracée en trait fin : elle ajoute des pensions
financées par une cotisation facultative sur la tranche de salaire au-delà de six SMIG.

LE TAUX LÉGAL DE LA BRANCHE PENSIONS SE LIT DE DEUX FAÇONS. Il est la somme d'une cotisation
propre de 5,25 % et d'une quote-part, fixée en vingtièmes (6,25/20e depuis 1994, 7,25/20e
depuis le 1er janvier 2003), de cotisations dont le taux global est de 18 % depuis 1997 :
  - lecture « en points », celle de la caisse : 11,5 % puis 12,5 % — trait principal ;
  - lecture littérale, X/20 × 18 % : 10,875 % puis 11,775 % — pointillé.
Le changement tombe le 1er janvier 2003 : la marche est tracée entre 2002 et 2003.

RUPTURE DE 2003. Les taxis et louages sortent du champ des employeurs du régime (décret
n° 2002-3018) : les employeurs reculent de 12 %, les salariés déclarés non, mais les actifs
cessent de croître et le rapport pensionnés ÷ cotisants fait son plus fort bond de la période
2000-2011. Un filet vertical discret le signale sur la seule figure de décomposition, où se
lit ce bond. Sur celle du taux, il se confondrait avec la marche du taux légal, qui change à
la même date, et τ* n'y rompt pas.

Pas de nature de dénominateur à distinguer : la masse salariale déclarée est publiée chaque
année de 2000 à 2017 par le même annuaire. Les chiffres cités dans le texte du chapitre se
recalculent depuis `table()`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "cnss-rsna-taux-equilibre"

I = {
    "num": "pensions servies sans régime complémentaire (numérateur)",
    "den": "masse salariale déclarée (dénominateur)",
    "npens": "pensionnés, toutes natures",
    "naff": "actifs, non-assujettis compris",
    "pm": "pension moyenne mensuelle",
    "sm": "salaire moyen mensuel",
    "R": "taux de remplacement apparent",
    "D": "ratio pensionnés / cotisants",
    "tau": "taux d'équilibre",
    "tau_rc": "taux d'équilibre, avec régime complémentaire",
    "t_pts": "taux légal de la branche pensions, lecture en points",
    "t_lit": "taux légal de la branche pensions, lecture littérale",
    "ecart_pts": "écart taux d'équilibre − taux légal, lecture en points",
    "ecart_lit": "écart taux d'équilibre − taux légal, lecture littérale",
}

RUPTURE = 2003  # sortie des taxis et louages du champ des employeurs (décret n° 2002-3018)

_L = {
    "titre_taux": {
        "fr": "Régime des salariés non agricoles : taux de cotisation d'équilibre\n"
              "et taux légal de la branche pensions, 2000-2017",
        "ar": "نظام الأجراء غير الفلاحيين: نسبة المساهمة المحقّقة للتوازن\n"
              "والنسبة القانونية لفرع الجرايات، 2000-2017"},
    "titre_decomp": {
        "fr": "Régime des salariés non agricoles : décomposition du taux d'équilibre,\n"
              "indices base 100 en 2000, 2000-2017",
        "ar": "نظام الأجراء غير الفلاحيين: تفكيك نسبة التوازن،\n"
              "مؤشرات (أساس 100 سنة 2000)، 2000-2017"},
    "x": {"fr": "Année", "ar": "السنة"},
    "y_taux": {"fr": "% de la masse salariale déclarée", "ar": "% من كتلة الأجور المصرّح بها"},
    "y_indice": {"fr": "Indice, 2000 = 100 (échelle logarithmique)",
                 "ar": "مؤشر، 2000 = 100 (سلّم لوغاريتمي)"},
    "lg_tau": {"fr": "Taux d'équilibre (pensions ÷ masse salariale déclarée)",
               "ar": "نسبة التوازن (الجرايات ÷ كتلة الأجور المصرّح بها)"},
    "lg_tau_rc": {"fr": "Taux d'équilibre, avec le régime complémentaire",
                  "ar": "نسبة التوازن، بما في ذلك النظام التكميلي"},
    "lg_t_pts": {"fr": "Taux légal, lecture « en points » (celle de la caisse)",
                 "ar": "النسبة القانونية، القراءة «بالنقاط» (قراءة الصندوق)"},
    "lg_t_lit": {"fr": "Taux légal, lecture littérale (X/20 × 18 %)",
                 "ar": "النسبة القانونية، القراءة الحرفية (س/20 × 18 %)"},
    "lg_R": {"fr": "Taux de remplacement apparent (pension moyenne ÷ salaire moyen)",
             "ar": "نسبة التعويض الظاهرة (معدّل الجراية ÷ معدّل الأجر)"},
    "lg_D": {"fr": "Pensionnés ÷ cotisants",
             "ar": "المنتفعون بجراية ÷ المساهمون"},
    "rupture": {"fr": "2003 : taxis et louages\nsortis du champ",
                "ar": "2003: خروج سيارات الأجرة\nواللواج من المجال"},
    # Colonnes de l'onglet Données
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_tau": {"fr": "Taux d'équilibre (%)", "ar": "نسبة التوازن (%)"},
    "col_tau_rc": {"fr": "Taux d'équilibre, avec régime complémentaire (%)",
                   "ar": "نسبة التوازن، بما في ذلك النظام التكميلي (%)"},
    "col_t_pts": {"fr": "Taux légal, lecture en points (%)",
                  "ar": "النسبة القانونية، القراءة بالنقاط (%)"},
    "col_t_lit": {"fr": "Taux légal, lecture littérale (%)",
                  "ar": "النسبة القانونية، القراءة الحرفية (%)"},
    "col_ecart_pts": {"fr": "Écart, lecture en points (points)",
                      "ar": "الفارق، القراءة بالنقاط (نقاط)"},
    "col_ecart_lit": {"fr": "Écart, lecture littérale (points)",
                      "ar": "الفارق، القراءة الحرفية (نقاط)"},
    "col_R": {"fr": "Remplacement apparent (%)", "ar": "نسبة التعويض الظاهرة (%)"},
    "col_D": {"fr": "Pensionnés ÷ cotisants (%)", "ar": "المنتفعون بجراية ÷ المساهمون (%)"},
    "col_pm": {"fr": "Pension moyenne (D/mois)", "ar": "معدّل الجراية (د/شهر)"},
    "col_sm": {"fr": "Salaire moyen (D/mois)", "ar": "معدّل الأجر (د/شهر)"},
    "col_num": {"fr": "Pensions servies, hors régime complémentaire (MD)",
                "ar": "الجرايات المدفوعة، دون النظام التكميلي (م.د)"},
    "col_den": {"fr": "Masse salariale déclarée (MD)", "ar": "كتلة الأجور المصرّح بها (م.د)"},
    "col_npens": {"fr": "Pensionnés, toutes natures", "ar": "المنتفعون بجراية، بجميع الأصناف"},
    "col_naff": {"fr": "Actifs, non-assujettis compris",
                 "ar": "النشيطون، بمن فيهم غير الخاضعين"},
    "col_src_num": {"fr": "Source des pensions", "ar": "مصدر الجرايات"},
    "col_src_den": {"fr": "Source de la masse salariale", "ar": "مصدر كتلة الأجور"},
    "col_i_tau": {"fr": "Taux d'équilibre (2000 = 100)", "ar": "نسبة التوازن (2000 = 100)"},
    "col_i_R": {"fr": "Remplacement apparent (2000 = 100)", "ar": "نسبة التعويض الظاهرة (2000 = 100)"},
    "col_i_D": {"fr": "Pensionnés ÷ cotisants (2000 = 100)", "ar": "المنتفعون بجراية ÷ المساهمون (2000 = 100)"},
}

BLEU, GRIS, ORANGE, VERT = "#08519c", "#57606a", "#bf8700", "#1a7f37"


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _donnees():
    """{année: {clé: valeur, 'src_num': …, 'src_den': …}}, 2000-2017."""
    df = figtools.series(SERIE)
    inv = {v: k for k, v in I.items()}
    out: dict[int, dict] = {}
    for r in df.itertuples():
        d = out.setdefault(int(r.annee), {})
        k = inv.get(r.indicateur)
        if k is None:
            continue
        d[k] = float(r.valeur)
        if k == "num":
            d["src_num"] = r.source
        elif k == "den":
            d["src_den"] = r.source
    return dict(sorted(out.items()))


def table():
    import pandas as pd

    def pct(x, n=2):
        return None if x is None else round(100 * x, n)

    return pd.DataFrame([{
        _lab("col_annee"): a,
        _lab("col_tau"): pct(d["tau"]),
        _lab("col_tau_rc"): pct(d["tau_rc"]),
        _lab("col_t_pts"): pct(d["t_pts"], 3),
        _lab("col_t_lit"): pct(d["t_lit"], 3),
        _lab("col_ecart_pts"): pct(d["ecart_pts"]),
        _lab("col_ecart_lit"): pct(d["ecart_lit"]),
        _lab("col_R"): pct(d["R"], 1),
        _lab("col_D"): pct(d["D"], 1),
        _lab("col_pm"): round(d["pm"], 2),
        _lab("col_sm"): round(d["sm"], 2),
        _lab("col_num"): round(d["num"], 1),
        _lab("col_den"): round(d["den"], 1),
        _lab("col_npens"): int(d["npens"]),
        _lab("col_naff"): int(d["naff"]),
        _lab("col_src_num"): d["src_num"],
        _lab("col_src_den"): d["src_den"],
    } for a, d in _donnees().items()])


def _indices():
    """Indices base 100 en 2000 du taux d'équilibre et de ses deux facteurs."""
    d = _donnees()
    b = d[min(d)]
    return {a: {k: 100 * v[k] / b[k] for k in ("tau", "R", "D")} for a, v in d.items()}


def table_indices():
    import pandas as pd
    return pd.DataFrame([{
        _lab("col_annee"): a,
        _lab("col_i_tau"): round(v["tau"], 1),
        _lab("col_i_R"): round(v["R"], 1),
        _lab("col_i_D"): round(v["D"], 1),
    } for a, v in _indices().items()])


def _rupture(ax, ft, y, va):
    """Filet vertical discret entre 2002 et 2003, avec son libellé."""
    x = RUPTURE - 0.5
    ax.axvline(x, color=GRIS, lw=0.8, ls=(0, (1, 2)), alpha=0.7, zorder=0)
    ax.annotate(ft(_lab("rupture")), (x, y), xytext=(4, 0), textcoords="offset points",
                ha="left", va=va, fontsize=7.5, color=GRIS)


def _axe_annees(ax, fin):
    ax.set_xlim(1999.3, fin + 0.7)
    ax.set_xticks(range(2000, fin + 1, 2))


def _fmt(v: float) -> str:
    return f"{v:.1f}".replace(".", ",")


def fig_taux():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    an = list(d)

    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    ax.plot(an, [100 * d[a]["tau_rc"] for a in an], "-", color=BLEU, lw=1.2, alpha=0.5)
    ax.plot(an, [100 * d[a]["tau"] for a in an], "o-", color=BLEU, lw=2.2, ms=5)
    ax.step(an, [100 * d[a]["t_pts"] for a in an], where="mid", color=GRIS, lw=2)
    ax.step(an, [100 * d[a]["t_lit"] for a in an], where="mid", color=GRIS, lw=1.6, ls=":")
    for a in (an[0], 2008, an[-1]):
        ax.annotate(_fmt(100 * d[a]["tau"]), (a, 100 * d[a]["tau"]), textcoords="offset points",
                    xytext=(0, -14), ha="center", fontsize=8, color=BLEU)
    for a in (an[0], an[-1]):
        ax.annotate(_fmt(100 * d[a]["t_pts"]), (a, 100 * d[a]["t_pts"]),
                    textcoords="offset points", xytext=(0, 5), ha="center", fontsize=8,
                    color=GRIS)
        ax.annotate(f"{100 * d[a]['t_lit']:.3f}".rstrip("0").rstrip(".").replace(".", ","),
                    (a, 100 * d[a]["t_lit"]), textcoords="offset points", xytext=(0, -12),
                    ha="center", fontsize=8, color=GRIS)
    ax.legend(handles=[
        Line2D([], [], color=BLEU, lw=2.2, marker="o", ms=5, label=ft(_lab("lg_tau"))),
        Line2D([], [], color=BLEU, lw=1.2, alpha=0.5, label=ft(_lab("lg_tau_rc"))),
        Line2D([], [], color=GRIS, lw=2, label=ft(_lab("lg_t_pts"))),
        Line2D([], [], color=GRIS, lw=1.6, ls=":", label=ft(_lab("lg_t_lit")))],
        loc="lower right", fontsize=8.5)
    _axe_annees(ax, an[-1])
    ax.set_ylim(0, 22)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_taux")))
    ax.set_title(ft(_lab("titre_taux")))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def fig_decomposition():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    ix = _indices()
    an = list(ix)

    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    ax.axhline(100, color=GRIS, lw=0.8, alpha=0.6)
    _rupture(ax, ft, 190, "top")
    ax.plot(an, [ix[a]["tau"] for a in an], "o-", color=BLEU, lw=2.2, ms=5)
    ax.plot(an, [ix[a]["R"] for a in an], "o-", color=ORANGE, lw=1.8, ms=4.5)
    ax.plot(an, [ix[a]["D"] for a in an], "s-", color=VERT, lw=1.8, ms=4.5)
    for a in (2008, an[-1]):
        # En 2008, taux et rapport démographique sont à un point d'écart : le taux passe dessous.
        for k, c, dy in (("tau", BLEU, -13 if a == 2008 else 7), ("D", VERT, 7),
                         ("R", ORANGE, -13)):
            ax.annotate(f"{ix[a][k]:.0f}", (a, ix[a][k]), textcoords="offset points",
                        xytext=(0, dy), ha="center", fontsize=8, color=c)
    ax.set_yscale("log")
    ax.set_yticks([70, 80, 90, 100, 125, 150, 175])
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f}"))
    ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_ylim(62, 195)
    ax.legend(handles=[
        Line2D([], [], color=BLEU, lw=2.2, marker="o", ms=5, label=ft(_lab("lg_tau"))),
        Line2D([], [], color=VERT, lw=1.8, marker="s", ms=4.5, label=ft(_lab("lg_D"))),
        Line2D([], [], color=ORANGE, lw=1.8, marker="o", ms=4.5, label=ft(_lab("lg_R")))],
        loc="lower left", fontsize=8.5)
    _axe_annees(ax, an[-1])
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_indice")))
    ax.set_title(ft(_lab("titre_decomp")))
    ax.grid(True, which="major", alpha=0.3)
    fig.tight_layout()
    return fig

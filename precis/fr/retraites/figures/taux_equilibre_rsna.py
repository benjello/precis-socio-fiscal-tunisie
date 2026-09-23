"""Figures « taux de cotisation d'équilibre du régime des salariés non agricoles », 2000-2017,
précédées, sans raccord, de la CAVIS (tout le secteur privé) en 1980 et 1985-1991.

    from figures import taux_equilibre_rsna as ter
    ter.fig_taux()             # taux d'équilibre et taux légal de la branche pensions
    ter.table()                # toutes les grandeurs (onglet Données)
    ter.fig_decomposition()    # indices : taux, remplacement, rapport démographique (deux panneaux)
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

1980 ET 1985-1991 : LA CAVIS, AUTRE SOURCE, AUTRE PÉRIMÈTRE (colonne `denominateur`). Banque
mondiale, rapport 11376-TUN (1993) : pensions versées par la CAVIS, qui servait tout le secteur
privé, rapportées à ses cotisations de pension divisées par le taux du RSNA (5 %, puis 8 % à
compter du 1er janvier 1988). Cette masse « équivalent RSNA » n'est pas une masse déclarée ; de
1988 à 1991, le taux du RSNA étant le plus haut des régimes, τ* est un majorant. Les deux
lectures du taux légal coïncident (taux global de 20 %) : une seule marche est tracée. Marques
triangulaires creuses, aucun trait à travers 1981-1984 ni 1992-1999 (fond hachuré), et, pour la
décomposition, un panneau propre en base 100 en 1985 : un indice commun ferait lire 1991 → 2000
comme une évolution mesurée, alors que ni la source ni le périmètre ne sont les mêmes.

De 2000 à 2017, la masse salariale déclarée est publiée chaque année par le même annuaire. Les chiffres cités dans le texte du chapitre se
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
    "pc": "pensions ÷ cotisations de pension",
}

RUPTURE = 2003  # sortie des taxis et louages du champ des employeurs (décret n° 2002-3018)
TROU = (1992, 1999)   # aucune donnée
BASE_BM, BASE = 1985, 2000

_L = {
    "titre_taux": {
        "fr": "Régime des salariés non agricoles : taux de cotisation d'équilibre\n"
              "et taux légal de la branche pensions, 1980-2017",
        "ar": "نظام الأجراء غير الفلاحيين: نسبة المساهمة المحقّقة للتوازن\n"
              "والنسبة القانونية لفرع الجرايات، 1980-2017"},
    "titre_decomp": {
        "fr": "Régime des salariés non agricoles : décomposition du taux d'équilibre,\n"
              "en indices, 1980-2017",
        "ar": "نظام الأجراء غير الفلاحيين: تفكيك نسبة التوازن،\n"
              "مؤشرات، 1980-2017"},
    "panneau_bm": {"fr": "CAVIS, tout le privé, 1980, 1985-1991 :\nbase 100 en 1985",
                   "ar": "صندوق تأمين الشيخوخة والعجز والباقين بقيد الحياة بعد وفاة المنتفع بجراية،\nكامل القطاع الخاص، 1980، 1985-1991: أساس 100 سنة 1985"},
    "panneau_rec": {"fr": "Salariés non agricoles, 2000-2017 :\nbase 100 en 2000",
                    "ar": "الأجراء غير الفلاحيين، 2000-2017:\nأساس 100 سنة 2000"},
    "trou": {"fr": "1992-1999 :\naucune donnée", "ar": "1992-1999:\nلا معطيات"},
    "lg_tau_bm": {"fr": "Taux d'équilibre de la CAVIS, tout le secteur privé, 1980 et 1985-1991\n"
                        "(Banque mondiale, 1993 ; masse = cotisations ÷ taux du régime ; sans raccord)",
                  "ar": "نسبة التوازن، صندوق تأمين الشيخوخة والعجز والباقين بقيد الحياة بعد وفاة المنتفع بجراية،\nكامل القطاع الخاص، 1980 و1985-1991 "
                        "(البنك الدولي، 1993؛ الكتلة = المساهمات ÷ نسبة النظام؛ دون ربط)"},
    "lg_t_bm": {"fr": "Taux légal, 1980-1991 : 5 %, puis 8 % en 1988 (les deux lectures coïncident)",
                "ar": "النسبة القانونية، 1980-1991: 5 %، ثمّ 8 % سنة 1988 (تتطابق القراءتان)"},
    "lg_bm": {"fr": "1980, 1985-1991 : CAVIS, tout le secteur privé (Banque mondiale, 1993)",
              "ar": "1980، 1985-1991: صندوق تأمين الشيخوخة والعجز والباقين بقيد الحياة بعد وفاة المنتفع بجراية،\nكامل القطاع الخاص (البنك الدولي، 1993)"},
    "lg_ann": {"fr": "2000-2017 : salariés non agricoles (annuaires de la caisse)",
               "ar": "2000-2017: الأجراء غير الفلاحيين (الكتب الإحصائية للصندوق)"},
    "x": {"fr": "Année", "ar": "السنة"},
    "y_taux": {"fr": "% de la masse salariale déclarée", "ar": "% من كتلة الأجور المصرّح بها"},
    "y_indice": {"fr": "Indice (échelle logarithmique)",
                 "ar": "مؤشر (سلّم لوغاريتمي)"},
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
    "col_champ": {"fr": "Champ et dénominateur", "ar": "المجال والمقام"},
    "col_pc": {"fr": "Pensions ÷ cotisations de pension (CAVIS)", "ar": "الجرايات ÷ مساهمات التقاعد (الصندوق)"},
    "col_base": {"fr": "Année de base (= 100)", "ar": "سنة الأساس (= 100)"},
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
    "col_i_tau": {"fr": "Taux d'équilibre (indice)", "ar": "نسبة التوازن (مؤشر)"},
    "col_i_R": {"fr": "Remplacement apparent (indice)", "ar": "نسبة التعويض الظاهرة (مؤشر)"},
    "col_i_D": {"fr": "Pensionnés ÷ cotisants (indice)", "ar": "المنتفعون بجراية ÷ المساهمون (مؤشر)"},
}

_CHAMP = {False: {"fr": "Salariés non agricoles ; masse salariale déclarée (annuaires de la caisse)",
                  "ar": "الأجراء غير الفلاحيين؛ كتلة الأجور المصرّح بها (الكتب الإحصائية للصندوق)"},
          True: {"fr": "CAVIS, tout le secteur privé (Banque mondiale, 1993) ; masse = cotisations de pension "
                       "÷ taux du régime des salariés non agricoles ; sans raccord avec 2000",
                 "ar": "صندوق تأمين الشيخوخة والعجز والباقين بقيد الحياة بعد وفاة المنتفع بجراية، كامل القطاع الخاص (البنك الدولي، 1993)؛ الكتلة = مساهمات "
                       "التقاعد ÷ نسبة نظام الأجراء غير الفلاحيين؛ دون ربط مع سنة 2000"}}

BLEU, GRIS, ORANGE, VERT = "#08519c", "#57606a", "#bf8700", "#1a7f37"


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _champ(a: int) -> str:
    return _CHAMP[a < TROU[0]].get(figtools.lang(), _CHAMP[a < TROU[0]]["fr"])


def _suites(annees):
    """Découpe une liste d'années croissantes en suites d'années consécutives."""
    out = []
    for a in annees:
        if out and a == out[-1][-1] + 1:
            out[-1].append(a)
        else:
            out.append([a])
    return out


def _donnees():
    """{année: {clé: valeur, 'src_num': …, 'src_den': …}}, 1980, 1985-1991, 2000-2017.

    Les années 1980-1991 n'ont pas `tau_rc` ; seules elles ont `pc` : les lire par `.get`."""
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
        _lab("col_champ"): _champ(a),
        _lab("col_tau"): pct(d["tau"]),
        _lab("col_tau_rc"): pct(d.get("tau_rc")),
        _lab("col_pc"): None if d.get("pc") is None else round(d["pc"], 3),
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
    """Indices du taux d'équilibre et de ses deux facteurs, chaque période sur sa base :
    CAVIS 1980 et 1985-1991 en base 100 en 1985, RSNA 2000-2017 en base 100 en 2000."""
    d = _donnees()
    out = {}
    for a, v in d.items():
        base = BASE_BM if a < TROU[0] else BASE
        out[a] = {k: 100 * v[k] / d[base][k] for k in ("tau", "R", "D")} | {"base": base}
    return out


def table_indices():
    import pandas as pd
    return pd.DataFrame([{
        _lab("col_annee"): a,
        _lab("col_champ"): _champ(a),
        _lab("col_base"): v["base"],
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


def _axe_annees(ax, fin, debut=2000, pas=2):
    ax.set_xlim(debut - 0.7, fin + 0.7)
    ax.set_xticks(range(debut, fin + 1, pas))


def _trou(ax, ft, y):
    """Hachure et cartouche sur 1992-1999, que rien ne documente."""
    ax.axvspan(TROU[0] - 0.5, TROU[1] + 0.5, facecolor="none", edgecolor=GRIS, hatch="///",
               alpha=0.25, lw=0)
    ax.text((TROU[0] + TROU[1]) / 2, y, "\n".join(ft(l) for l in _lab("trou").split("\n")),
            fontsize=7.5, color=GRIS, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1.5))


def _fmt(v: float) -> str:
    return f"{v:.1f}".replace(".", ",")


def fig_taux():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    an_bm = [a for a in d if a < TROU[0]]
    an = [a for a in d if a > TROU[1]]

    fig, ax = plt.subplots(figsize=(10.5, 6.2))
    _trou(ax, ft, 17)
    # CAVIS 1980-1991 : triangles creux, traits seulement entre années consécutives.
    for suite in _suites(an_bm):
        ax.plot(suite, [100 * d[a]["tau"] for a in suite], "^-", color=BLEU, lw=1.6, ms=6,
                mfc="white", mew=1.4)
        if len(suite) == 1:
            a = suite[0]
            ax.plot([a - 0.5, a + 0.5], [100 * d[a]["t_pts"]] * 2, color=GRIS, lw=2)
        else:
            ax.step(suite, [100 * d[a]["t_pts"] for a in suite], where="mid", color=GRIS, lw=2)
    for a, dy in ((an_bm[0], 8), (1987, 8), (an_bm[-1], -14)):
        ax.annotate(_fmt(100 * d[a]["tau"]), (a, 100 * d[a]["tau"]), textcoords="offset points",
                    xytext=(0, dy), ha="center", fontsize=8, color=BLEU)
    for a in (1987, an_bm[-1]):
        ax.annotate(_fmt(100 * d[a]["t_pts"]), (a, 100 * d[a]["t_pts"]), textcoords="offset points",
                    xytext=(0, -13 if a == 1987 else 5), ha="center", fontsize=8, color=GRIS)
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
        Line2D([], [], color=GRIS, lw=1.6, ls=":", label=ft(_lab("lg_t_lit"))),
        Line2D([], [], color=BLEU, lw=1.6, marker="^", ms=6, mfc="white", mew=1.4,
               label=ft(_lab("lg_tau_bm"))),
        Line2D([], [], color=GRIS, lw=2, label=ft(_lab("lg_t_bm")))],
        loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=8, frameon=False)
    _axe_annees(ax, an[-1], debut=1980, pas=5)
    ax.set_ylim(0, 22)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_taux")))
    ax.set_title(ft(_lab("titre_taux")))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def _panneau_indices(ax, ix, an, annoter):
    ax.axhline(100, color=GRIS, lw=0.8, alpha=0.6)
    bm = an[0] < TROU[0]
    mk, mfc = ("^", "white") if bm else ("o", None)
    for suite in _suites(an):
        for k, c, lw, ms, m in (("tau", BLEU, 2.2, 5, mk), ("R", ORANGE, 1.8, 4.5, mk), ("D", VERT, 1.8, 4.5, "s")):
            ax.plot(suite, [ix[a][k] for a in suite], m + "-", color=c, lw=lw, ms=ms,
                    mfc=(mfc or c) if m != "s" else c, mew=1.3)
    for a, place in annoter:
        for k, c in (("tau", BLEU), ("D", VERT), ("R", ORANGE)):
            ax.annotate(f"{ix[a][k]:.0f}", (a, ix[a][k]), textcoords="offset points",
                        xytext=(0, place[k]), ha="center", fontsize=8, color=c)
    ax.set_yscale("log")
    ax.set_yticks([50, 60, 70, 80, 90, 100, 125, 150, 175])
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f}"))
    ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_ylim(46, 195)
    ax.grid(True, which="major", alpha=0.3)


def fig_decomposition():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    ix = _indices()
    an_bm = [a for a in ix if a < TROU[0]]
    an = [a for a in ix if a > TROU[1]]

    fig, (ax0, ax) = plt.subplots(1, 2, figsize=(10.5, 6.6), sharey=True,
                                  gridspec_kw={"width_ratios": [12, 18]})
    haut, bas = 7, -13
    _panneau_indices(ax0, ix, an_bm, ((an_bm[0], {"tau": bas, "D": haut, "R": haut}),
                                      (an_bm[-1], {"tau": bas, "D": haut, "R": bas})))
    # En 2008, taux et rapport démographique sont à un point d'écart : le taux passe dessous.
    _panneau_indices(ax, ix, an, ((2008, {"tau": bas, "D": haut, "R": bas}),
                                  (an[-1], {"tau": haut, "D": haut, "R": bas})))
    _rupture(ax, ft, 190, "top")
    _axe_annees(ax0, an_bm[-1], debut=an_bm[0], pas=2)
    _axe_annees(ax, an[-1], debut=an[0], pas=3)
    ax0.set_title(ft(_lab("panneau_bm")), fontsize=9)
    ax.set_title(ft(_lab("panneau_rec")), fontsize=9)
    ax0.set_ylabel(ft(_lab("y_indice")))
    ax0.set_xlabel(ft(_lab("x")))
    ax.set_xlabel(ft(_lab("x")))
    fig.suptitle(ft(_lab("titre_decomp")))
    fig.tight_layout(rect=(0, 0.13, 1, 1))
    fig.legend(handles=[
        Line2D([], [], color=BLEU, lw=2.2, label=ft(_lab("lg_tau"))),
        Line2D([], [], color=VERT, lw=1.8, marker="s", ms=4.5, label=ft(_lab("lg_D"))),
        Line2D([], [], color=ORANGE, lw=1.8, label=ft(_lab("lg_R"))),
        Line2D([], [], color=GRIS, lw=1.6, marker="^", ms=6, mfc="white", mew=1.4, label=ft(_lab("lg_bm"))),
        Line2D([], [], color=GRIS, lw=1.6, marker="o", ms=5, label=ft(_lab("lg_ann")))],
        loc="upper center", bbox_to_anchor=(0.5, 0.125), ncol=2, fontsize=8, frameon=False)
    return fig

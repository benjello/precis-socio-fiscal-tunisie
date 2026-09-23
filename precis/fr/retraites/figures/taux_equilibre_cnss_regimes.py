"""Figures « taux de cotisation d'équilibre » des régimes de pension de la CNSS autres que le
régime des salariés non agricoles, 2000-2017.

    from figures import taux_equilibre_cnss_regimes as tr
    tr.fig_regime("rsaa")          # régime agricole amélioré : taux et décomposition
    tr.fig_regime("rtte")          # Tunisiens à l'étranger
    tr.fig_regime("raci")          # artistes, créateurs et intellectuels
    tr.table("rsaa")               # onglet Données de chacune
    tr.fig_rsa()                   # salariés agricoles : borne inférieure et rapport démographique
    tr.table("rsa")
    tr.fig_rtns_taux()             # non-salariés : trois champs, encadrement 2000-2004
    tr.fig_rtns_decomposition()    # non-salariés : décomposition, 2005-2017, trois panneaux
    tr.table_rtns()

Même définition que `taux_equilibre_rsna.py` : τ* = pensions servies ÷ assiette = (pension
moyenne ÷ revenu d'assiette moyen) × (pensionnés ÷ cotisants), pensions de toutes natures.
Une seule série, `cnss-regimes-taux-equilibre` ; ses arbitrages sont dans sa fiche de
provenance (annuaires statistiques de la caisse).

LA DÉCOMPOSITION EST TRACÉE EN NIVEAUX, SUR UNE ÉCHELLE LOGARITHMIQUE, et non en indices comme
pour le RSNA : ces régimes sont petits ou jeunes (8 pensionnés au RTTE en 2000, 27 actifs au RACI
en 2004), et un indice sur une telle année de base amplifierait le bruit. Sur l'échelle
logarithmique, la distance de τ* à la ligne de 100 % est la somme de celles des deux facteurs.

CAS PARTICULIERS, lus dans la série et non saisis ici :
  - RSA : borne inférieure seulement (assiette maximale de quatre trimestres de 45 jours) ; pas
    de taux de remplacement, donc pas de décomposition : le second panneau trace le rapport
    pensionnés ÷ cotisants, calculé depuis les effectifs de la série ;
  - RTNS 2000-2004 : classes de l'ensemble seulement, τ* encadré entre une assiette toute au
    SMIG et une assiette toute au SMAG — tracé en segments verticaux, sans trait vers 2005 ;
  - RACI : années où les pensionnés sont plus nombreux que les cotisants, grisées d'après la
    série (D > 1) ; échelle logarithmique pour le taux, qui dépasse 100 % en 2004.

Les chiffres cités dans le texte du chapitre se recalculent depuis `table()` et `table_rtns()`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "cnss-regimes-taux-equilibre"

I = {
    "tau": "taux d'équilibre",
    "tau_moy": "taux d'équilibre, SMIG et SMAG moyens de l'année",
    "binf": "taux d'équilibre, borne inférieure",
    "bb": "taux d'équilibre, borne basse",
    "bh": "taux d'équilibre, borne haute",
    "kappa": "taux légal de la branche pensions",
    "ecart": "écart taux d'équilibre − taux légal",
    "R": "taux de remplacement apparent",
    "D": "ratio pensionnés / cotisants",
    "nc": "actifs",
    "np": "pensionnés, toutes natures",
    "num": "pensions servies (numérateur)",
    "den": "assiette (dénominateur)",
    "den_max": "assiette maximale (dénominateur)",
    "pm": "pension moyenne mensuelle",
    "wm": "revenu d'assiette moyen mensuel",
    "cbar": "coefficient moyen de classe",
}

# Libellé de la série (colonne `regime`), nom affiché, date d'effet du taux légal.
REGIMES = {
    "rsa": {"serie": "salariés agricoles (RSA)",
            "nom": {"fr": "Régime des salariés agricoles", "ar": "نظام الأجراء الفلاحيين"},
            "effet": {"fr": "depuis le 1er janvier 1981", "ar": "منذ غرّة جانفي 1981"}},
    "rsaa": {"serie": "salariés agricoles, régime amélioré (RSAA)",
             "nom": {"fr": "Régime agricole amélioré", "ar": "النظام الفلاحي المحسَّن"},
             "effet": {"fr": "publié par la caisse", "ar": "كما ينشرها الصندوق"}},
    "rtns_na": {"serie": "travailleurs non salariés, secteur non agricole",
                "nom": {"fr": "Non-salariés, secteur non agricole",
                        "ar": "العملة غير الأجراء، القطاع غير الفلاحي"},
                "effet": {"fr": "depuis le 19 juillet 1995", "ar": "منذ 19 جويلية 1995"}},
    "rtns_a": {"serie": "travailleurs non salariés, secteur agricole",
               "nom": {"fr": "Non-salariés, secteur agricole",
                       "ar": "العملة غير الأجراء، القطاع الفلاحي"},
               "effet": {"fr": "depuis le 19 juillet 1995", "ar": "منذ 19 جويلية 1995"}},
    "rtns": {"serie": "travailleurs non salariés, ensemble des deux secteurs",
             "nom": {"fr": "Non-salariés, ensemble des deux secteurs",
                     "ar": "العملة غير الأجراء، مجموع القطاعين"},
             "effet": {"fr": "depuis le 19 juillet 1995", "ar": "منذ 19 جويلية 1995"}},
    "rtte": {"serie": "travailleurs tunisiens à l'étranger (RTTE)",
             "nom": {"fr": "Régime des Tunisiens à l'étranger",
                     "ar": "نظام الضمان الاجتماعي للعملة التونسيين بالخارج"},
             "effet": {"fr": "depuis le 19 janvier 1989", "ar": "منذ 19 جانفي 1989"}},
    "raci": {"serie": "artistes, créateurs et intellectuels (RACI)",
             "nom": {"fr": "Régime des artistes, créateurs et intellectuels",
                     "ar": "نظام الضمان الاجتماعي للفنانين والمبدعين والمثقفين"},
             "effet": {"fr": "depuis le 5 janvier 2003", "ar": "منذ 5 جانفي 2003"}},
}

_L = {
    "titre_regime": {"fr": "{nom} : taux de cotisation d'équilibre et sa décomposition, {p}",
                     "ar": "{nom}: نسبة المساهمة المحقّقة للتوازن ومكوّناتها، {p}"},
    "titre_rsa": {"fr": "{nom} : borne inférieure du taux d'équilibre\n"
                        "et rapport entre pensionnés et cotisants, {p}",
                  "ar": "{nom}: الحدّ الأدنى لنسبة التوازن\n"
                        "ونسبة المنتفعين بجراية إلى المساهمين، {p}"},
    "titre_rtns_taux": {"fr": "Travailleurs non salariés : taux de cotisation d'équilibre\n"
                              "et taux légal de la branche pensions, 2000-2017",
                        "ar": "العملة غير الأجراء: نسبة المساهمة المحقّقة للتوازن\n"
                              "والنسبة القانونية لفرع الجرايات، 2000-2017"},
    "titre_rtns_decomp": {"fr": "Travailleurs non salariés : décomposition du taux d'équilibre, "
                                "2005-2017",
                          "ar": "العملة غير الأجراء: تفكيك نسبة التوازن، 2005-2017"},
    "panneau_taux": {"fr": "Taux d'équilibre et taux légal", "ar": "نسبة التوازن والنسبة القانونية"},
    "panneau_decomp": {"fr": "Décomposition (échelle logarithmique)",
                       "ar": "التفكيك (سلّم لوغاريتمي)"},
    "panneau_D": {"fr": "Pensionnés ÷ cotisants", "ar": "المنتفعون بجراية ÷ المساهمون"},
    "x": {"fr": "Année", "ar": "السنة"},
    "y_taux": {"fr": "% de l'assiette", "ar": "% من قاعدة الاشتراك"},
    "y_log": {"fr": "% (échelle logarithmique)", "ar": "% (سلّم لوغاريتمي)"},
    "y_D": {"fr": "%", "ar": "%"},
    "lg_tau": {"fr": "Taux d'équilibre (pensions ÷ assiette)",
               "ar": "نسبة التوازن (الجرايات ÷ قاعدة الاشتراك)"},
    "lg_tau_moy": {"fr": "Taux d'équilibre, salaire minimum moyen de l'année",
                   "ar": "نسبة التوازن، بمعدّل الأجر الأدنى خلال السنة"},
    "lg_binf": {"fr": "Borne inférieure du taux d'équilibre (assiette maximale)",
                "ar": "الحدّ الأدنى لنسبة التوازن (القاعدة القصوى)"},
    "lg_kappa": {"fr": "Taux légal de la branche pensions ({v}, {effet})",
                 "ar": "النسبة القانونية لفرع الجرايات ({v}، {effet})"},
    "lg_R": {"fr": "Taux de remplacement apparent (pension moyenne ÷ revenu d'assiette moyen)",
             "ar": "نسبة التعويض الظاهرة (معدّل الجراية ÷ معدّل دخل القاعدة)"},
    "lg_D": {"fr": "Pensionnés ÷ cotisants", "ar": "المنتفعون بجراية ÷ المساهمون"},
    "lg_100": {"fr": "100 %", "ar": "100 %"},
    "lg_plus": {"fr": "Pensionnés plus nombreux que les cotisants",
                "ar": "المنتفعون بجراية أكثر من المساهمين"},
    "lg_encadre": {"fr": "Ensemble, 2000-2004 : taux encadré (assiette toute au SMIG ou toute au SMAG)",
                   "ar": "المجموع، 2000-2004: نسبة محصورة (قاعدة كلّها بالأجر الأدنى المهني أو كلّها بالأجر الأدنى الفلاحي)"},
    "lg_kappa_rtns": {"fr": "Taux légal de la branche pensions (7 %, depuis le 19 juillet 1995)",
                      "ar": "النسبة القانونية لفرع الجرايات (7 %، منذ 19 جويلية 1995)"},
    # Colonnes de l'onglet Données
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_regime": {"fr": "Régime ou champ", "ar": "النظام أو المجال"},
    "col_tau": {"fr": "Taux d'équilibre (%)", "ar": "نسبة التوازن (%)"},
    "col_tau_moy": {"fr": "Taux d'équilibre, salaire minimum moyen de l'année (%)",
                    "ar": "نسبة التوازن، بمعدّل الأجر الأدنى خلال السنة (%)"},
    "col_binf": {"fr": "Borne inférieure du taux d'équilibre (%)",
                 "ar": "الحدّ الأدنى لنسبة التوازن (%)"},
    "col_bb": {"fr": "Taux d'équilibre, borne basse (%)", "ar": "نسبة التوازن، الحدّ الأدنى (%)"},
    "col_bh": {"fr": "Taux d'équilibre, borne haute (%)", "ar": "نسبة التوازن، الحدّ الأعلى (%)"},
    "col_kappa": {"fr": "Taux légal de la branche pensions (%)",
                  "ar": "النسبة القانونية لفرع الجرايات (%)"},
    "col_ecart": {"fr": "Écart taux d'équilibre − taux légal (points)",
                  "ar": "الفارق بين نسبة التوازن والنسبة القانونية (نقاط)"},
    "col_R": {"fr": "Remplacement apparent (%)", "ar": "نسبة التعويض الظاهرة (%)"},
    "col_D": {"fr": "Pensionnés ÷ cotisants (%)", "ar": "المنتفعون بجراية ÷ المساهمون (%)"},
    "col_pm": {"fr": "Pension moyenne (D/mois)", "ar": "معدّل الجراية (د/شهر)"},
    "col_wm": {"fr": "Revenu d'assiette moyen (D/mois)", "ar": "معدّل دخل القاعدة (د/شهر)"},
    "col_cbar": {"fr": "Coefficient moyen de classe", "ar": "معدّل ضارب الصنف"},
    "col_num": {"fr": "Pensions servies, toutes natures (MD)",
                "ar": "الجرايات المدفوعة، بجميع الأصناف (م.د)"},
    "col_den": {"fr": "Assiette (MD)", "ar": "قاعدة الاشتراك (م.د)"},
    "col_den_max": {"fr": "Assiette maximale (MD)", "ar": "القاعدة القصوى (م.د)"},
    "col_np": {"fr": "Pensionnés, toutes natures", "ar": "المنتفعون بجراية، بجميع الأصناف"},
    "col_nc": {"fr": "Cotisants (actifs)", "ar": "المساهمون (النشيطون)"},
    "col_assiette": {"fr": "Assiette retenue", "ar": "القاعدة المعتمدة"},
}

# Colonnes de l'onglet Données : (clé, arrondi, facteur)
_COLS = [("tau", 2, 100), ("tau_moy", 2, 100), ("binf", 1, 100), ("bb", 2, 100), ("bh", 2, 100),
         ("kappa", 3, 100), ("ecart", 2, 100), ("R", 1, 100), ("D", 1, 100), ("pm", 2, 1),
         ("wm", 2, 1), ("cbar", 3, 1), ("num", 3, 1), ("den", 3, 1), ("den_max", 3, 1),
         ("np", 0, 1), ("nc", 0, 1)]

BLEU, GRIS, ORANGE, VERT, ROUGE = "#08519c", "#57606a", "#bf8700", "#1a7f37", "#a40e26"


def _lab(key: str, **kw) -> str:
    s = _L[key].get(figtools.lang(), _L[key]["fr"])
    return s.format(**kw) if kw else s


def _nom(cle: str) -> str:
    n = REGIMES[cle]["nom"]
    return n.get(figtools.lang(), n["fr"])


def _effet(cle: str) -> str:
    e = REGIMES[cle]["effet"]
    return e.get(figtools.lang(), e["fr"])


def _pct(v: float) -> str:
    s = f"{100 * v:.3f}".rstrip("0").rstrip(".")
    return s.replace(".", ",") + " %"


def _fmt(v: float, n: int = 1) -> str:
    return f"{v:.{n}f}".replace(".", ",")


def _donnees(cle: str) -> dict[int, dict]:
    """{année: {clé: valeur, 'assiette': libellé du dénominateur}} pour un régime ou un champ.

    Pour le RSA, le rapport pensionnés ÷ cotisants, absent de la série, est calculé depuis
    ses deux effectifs."""
    df = figtools.series(SERIE)
    df = df[df["regime"] == REGIMES[cle]["serie"]]
    inv = {v: k for k, v in I.items()}
    out: dict[int, dict] = {}
    for r in df.itertuples():
        k = inv.get(r.indicateur)
        if k is None:
            continue
        d = out.setdefault(int(r.annee), {})
        d[k] = float(r.valeur)
        if k in ("den", "den_max", "bb") and isinstance(r.denominateur, str):
            d["assiette"] = r.denominateur
    for d in out.values():
        if "D" not in d and d.get("nc") and "np" in d:
            d["D"] = d["np"] / d["nc"]
    return dict(sorted(out.items()))


def _lignes(cle: str, avec_regime: bool = False) -> list[dict]:
    rows = []
    for a, d in _donnees(cle).items():
        row = {_lab("col_annee"): a}
        if avec_regime:
            row[_lab("col_regime")] = _nom(cle)
        for k, n, f in _COLS:
            if k in d:
                v = round(f * d[k], n)
                row[_lab(f"col_{k}")] = int(v) if n == 0 else v
        if "assiette" in d:
            row[_lab("col_assiette")] = d["assiette"]
        rows.append(row)
    return rows


def table(cle: str):
    import pandas as pd
    return pd.DataFrame(_lignes(cle))


def table_rtns():
    import pandas as pd
    return pd.DataFrame([r for c in ("rtns_na", "rtns_a", "rtns") for r in _lignes(c, True)])


# --- éléments de tracé -----------------------------------------------------------------------

def _axe_annees(ax, debut, fin, pas=2):
    ax.set_xlim(debut - 0.7, fin + 0.7)
    ax.set_xticks(range(debut, fin + 1, pas))


def _axe_log(ax, vmin, vmax):
    """Échelle logarithmique en pourcentages, graduée 1-2-5, avec la ligne de 100 %."""
    ax.set_yscale("log")
    bas, haut = vmin / 1.5, vmax * 1.5
    ticks = [m * 10 ** e for e in range(-2, 4) for m in (1, 2, 5) if bas <= m * 10 ** e <= haut]
    ax.set_yticks(ticks)
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda v, _: _fmt(v, 0 if v >= 1 else 1)))
    ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_ylim(bas, haut)
    if bas <= 100 <= haut:
        ax.axhline(100, color=GRIS, lw=0.9, alpha=0.7)
    ax.grid(True, which="major", alpha=0.3)


def _annoter(ax, a, v, couleur, dy, n=1):
    ax.annotate(_fmt(v, n), (a, v), textcoords="offset points", xytext=(0, dy), ha="center",
                fontsize=8, color=couleur)


def _panneau_decomposition(ax, d, an, annoter=True):
    """τ*, R et D en niveaux (%), sur une échelle logarithmique."""
    series = (("tau", BLEU, "o", 2.2), ("R", ORANGE, "^", 1.8), ("D", VERT, "s", 1.8))
    for k, c, m, lw in series:
        ax.plot(an, [100 * d[a][k] for a in an], m + "-", color=c, lw=lw, ms=4.5)
    if annoter:
        # Étiquette au-dessus pour la plus haute des trois courbes, au-dessous pour la plus
        # basse ; celle du milieu, au-dessous si elle est proche de la plus haute.
        for a in (an[0], an[-1]):
            ordre = sorted(series, key=lambda s: d[a][s[0]], reverse=True)
            haut, milieu = d[a][ordre[0][0]], d[a][ordre[1][0]]
            dy = {ordre[0][0]: 6, ordre[2][0]: -13,
                  ordre[1][0]: -13 if haut / milieu < 1.25 else 6}
            for k, c, _m, _lw in series:
                _annoter(ax, a, 100 * d[a][k], c, dy[k])
    vals = [100 * d[a][k] for a in an for k in ("tau", "R", "D")]
    _axe_log(ax, min(vals), max(vals))


def _grise_plus(ax, d, an):
    """Grise les années où les pensionnés sont plus nombreux que les cotisants."""
    plus = [a for a in an if d[a]["D"] > 1]
    for a in plus:
        ax.axvspan(a - 0.5, a + 0.5, color=GRIS, alpha=0.12, lw=0)
    return bool(plus)


def fig_regime(cle: str):
    """Deux panneaux : τ* et taux légal ; τ*, R et D en niveaux (échelle logarithmique)."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees(cle)
    an = [a for a in d if "tau" in d[a]]
    log_taux = max(d[a]["tau"] for a in an) > 0.5  # RACI : 168 % en 2004
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(10.5, 5.6))

    grise = _grise_plus(ax0, d, an) | _grise_plus(ax1, d, an)
    ax0.plot(an, [100 * d[a]["tau"] for a in an], "o-", color=BLEU, lw=2.2, ms=5)
    moy = [a for a in an if "tau_moy" in d[a]]
    if moy:
        ax0.plot(moy, [100 * d[a]["tau_moy"] for a in moy], "-", color=BLEU, lw=1.1, alpha=0.5)
    ax0.step(an, [100 * d[a]["kappa"] for a in an], where="mid", color=GRIS, lw=2)
    for a in (an[0], an[-1]):
        _annoter(ax0, a, 100 * d[a]["tau"], BLEU, 7, 2)
    ax0.annotate(_pct(d[an[-1]]["kappa"]), (an[-1], 100 * d[an[-1]]["kappa"]),
                 textcoords="offset points", xytext=(0, -12), ha="center", fontsize=8, color=GRIS)
    if log_taux:
        vals = [100 * d[a][k] for a in an for k in ("tau", "kappa")]
        _axe_log(ax0, min(vals), max(vals))
        ax0.set_ylabel(ft(_lab("y_log")))
    else:
        ax0.set_ylim(0, 1.25 * max(100 * max(d[a]["tau"], d[a]["kappa"]) for a in an))
        ax0.set_ylabel(ft(_lab("y_taux")))
        ax0.grid(True, alpha=0.3)
    ax0.set_title(ft(_lab("panneau_taux")), fontsize=9)

    _panneau_decomposition(ax1, d, an)
    ax1.set_title(ft(_lab("panneau_decomp")), fontsize=9)
    ax1.set_ylabel(ft(_lab("y_log")))
    pas = 2 if len(an) > 10 else 1
    for ax in (ax0, ax1):
        _axe_annees(ax, an[0], an[-1], pas)
        ax.set_xlabel(ft(_lab("x")))
        ax.tick_params(axis="x", labelrotation=45)

    p = f"{an[0]}-{an[-1]}"
    fig.suptitle(ft(_lab("titre_regime", nom=_nom(cle), p=p)))
    handles = [
        Line2D([], [], color=BLEU, lw=2.2, marker="o", ms=5, label=ft(_lab("lg_tau"))),
        Line2D([], [], color=GRIS, lw=2, label=ft(_lab("lg_kappa", v=_pct(d[an[-1]]["kappa"]),
                                                          effet=_effet(cle)))),
        Line2D([], [], color=ORANGE, lw=1.8, marker="^", ms=4.5, label=ft(_lab("lg_R"))),
        Line2D([], [], color=VERT, lw=1.8, marker="s", ms=4.5, label=ft(_lab("lg_D")))]
    if moy:
        handles.insert(1, Line2D([], [], color=BLEU, lw=1.1, alpha=0.5, label=ft(_lab("lg_tau_moy"))))
    if grise:
        handles.append(Patch(color=GRIS, alpha=0.12, label=ft(_lab("lg_plus"))))
    fig.tight_layout(rect=(0, 0.16, 1, 1))
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, 0.155), ncol=2,
               fontsize=8, frameon=False)
    return fig


def fig_rsa():
    """Deux panneaux : borne inférieure de τ* et taux légal ; pensionnés ÷ cotisants."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees("rsa")
    an = list(d)
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(10.5, 5.4))
    ax0.plot(an, [100 * d[a]["binf"] for a in an], "^-", color=BLEU, lw=2, ms=6, mfc="white",
             mew=1.4)
    ax0.step(an, [100 * d[a]["kappa"] for a in an], where="mid", color=GRIS, lw=2)
    for a in (an[0], min(an, key=lambda x: d[x]["binf"]), an[-1]):
        _annoter(ax0, a, 100 * d[a]["binf"], BLEU, -14)
    ax0.annotate(_pct(d[an[-1]]["kappa"]), (an[-1], 100 * d[an[-1]]["kappa"]),
                 textcoords="offset points", xytext=(0, 6), ha="center", fontsize=8, color=GRIS)
    ax0.set_ylim(0, 100)
    ax0.set_ylabel(ft(_lab("y_taux")))
    ax0.set_title(ft(_lab("panneau_taux")), fontsize=9)

    ax1.plot(an, [100 * d[a]["D"] for a in an], "s-", color=VERT, lw=1.8, ms=4.5)
    for a in (an[0], min(an, key=lambda x: d[x]["D"]), an[-1]):
        _annoter(ax1, a, 100 * d[a]["D"], VERT, 7, 0)
    ax1.axhline(100, color=GRIS, lw=0.9, alpha=0.7)
    ax1.set_ylim(0, 1.2 * max(100 * d[a]["D"] for a in an))
    ax1.set_ylabel(ft(_lab("y_D")))
    ax1.set_title(ft(_lab("panneau_D")), fontsize=9)
    for ax in (ax0, ax1):
        _axe_annees(ax, an[0], an[-1], 2)
        ax.set_xlabel(ft(_lab("x")))
        ax.grid(True, alpha=0.3)
        ax.tick_params(axis="x", labelrotation=45)
    fig.suptitle(ft(_lab("titre_rsa", nom=_nom("rsa"), p=f"{an[0]}-{an[-1]}")))
    fig.tight_layout(rect=(0, 0.1, 1, 1))
    fig.legend(handles=[
        Line2D([], [], color=BLEU, lw=2, marker="^", ms=6, mfc="white", mew=1.4,
               label=ft(_lab("lg_binf"))),
        Line2D([], [], color=GRIS, lw=2, label=ft(_lab("lg_kappa", v=_pct(d[an[-1]]["kappa"]),
                                                          effet=_effet("rsa")))),
        Line2D([], [], color=VERT, lw=1.8, marker="s", ms=4.5, label=ft(_lab("lg_D")))],
        loc="upper center", bbox_to_anchor=(0.5, 0.095), ncol=2, fontsize=8, frameon=False)
    return fig


_RTNS = (("rtns_na", ORANGE, "o"), ("rtns_a", VERT, "s"), ("rtns", BLEU, "D"))


def fig_rtns_taux():
    """τ* des deux secteurs et de l'ensemble, 2005-2017 ; encadrement de l'ensemble, 2000-2004."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(10.5, 6.0))
    handles = []
    for cle, c, m in _RTNS:
        d = _donnees(cle)
        an = [a for a in d if "tau" in d[a]]
        ax.plot(an, [100 * d[a]["tau"] for a in an], m + "-", color=c, lw=2, ms=5)
        ax.plot(an, [100 * d[a]["tau_moy"] for a in an], "-", color=c, lw=1, alpha=0.45)
        for a in (an[0], an[-1]):
            _annoter(ax, a, 100 * d[a]["tau"], c, 7, 2)
        handles.append(Line2D([], [], color=c, lw=2, marker=m, ms=5, label=ft(_nom(cle))))
        enc = [a for a in d if "bb" in d[a]]
        if enc:
            ax.vlines(enc, [100 * d[a]["bb"] for a in enc], [100 * d[a]["bh"] for a in enc],
                      color=c, lw=5, alpha=0.45)
            _annoter(ax, enc[0], 100 * d[enc[0]]["bh"], c, 6, 2)
            _annoter(ax, enc[0], 100 * d[enc[0]]["bb"], c, -13, 2)
            kap = d
    ax.step(list(kap), [100 * kap[a]["kappa"] for a in kap], where="mid", color=GRIS, lw=2)
    handles += [
        Line2D([], [], color=BLEU, lw=5, alpha=0.45, label=ft(_lab("lg_encadre"))),
        Line2D([], [], color=GRIS, lw=1, alpha=0.6, label=ft(_lab("lg_tau_moy"))),
        Line2D([], [], color=GRIS, lw=2, label=ft(_lab("lg_kappa_rtns")))]
    _axe_annees(ax, 2000, 2017, 2)
    ax.set_ylim(0, 25)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_taux")))
    ax.set_title(ft(_lab("titre_rtns_taux")))
    ax.grid(True, alpha=0.3)
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.11), ncol=2,
              fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def fig_rtns_decomposition():
    """Trois panneaux (non agricole, agricole, ensemble) : τ*, R et D en niveaux, 2005-2017."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 5.6), sharey=True)
    vals = []
    for ax, (cle, _c, _m) in zip(axes, _RTNS):
        d = _donnees(cle)
        an = [a for a in d if "tau" in d[a]]
        _panneau_decomposition(ax, d, an)
        vals += [100 * d[a][k] for a in an for k in ("tau", "R", "D")]
        ax.set_title(ft(_nom(cle)).replace(", ", ",\n", 1) if figtools.lang() == "fr"
                     else ft(_nom(cle)), fontsize=9)
        _axe_annees(ax, an[0], an[-1], 3)
        ax.set_xlabel(ft(_lab("x")))
    for ax in axes:
        _axe_log(ax, min(vals), max(vals))
    axes[0].set_ylabel(ft(_lab("y_log")))
    fig.suptitle(ft(_lab("titre_rtns_decomp")))
    fig.tight_layout(rect=(0, 0.12, 1, 1))
    fig.legend(handles=[
        Line2D([], [], color=BLEU, lw=2.2, marker="o", ms=5, label=ft(_lab("lg_tau"))),
        Line2D([], [], color=VERT, lw=1.8, marker="s", ms=4.5, label=ft(_lab("lg_D"))),
        Line2D([], [], color=ORANGE, lw=1.8, marker="^", ms=4.5, label=ft(_lab("lg_R")))],
        loc="upper center", bbox_to_anchor=(0.5, 0.115), ncol=2, fontsize=8, frameon=False)
    return fig

"""Figures « taux de cotisation d'équilibre de la CNRPS », 1980, 1985-1991 et 2000-2023
(2021-2023 estimés ; 1980-1991 d'une autre source, sans raccord).

    from figures import taux_equilibre as te
    te.fig_taux()             # taux d'équilibre et taux légal global
    te.table()                # toutes les grandeurs, avec la nature du dénominateur (onglet Données)
    te.fig_decomposition()    # indices : taux, remplacement, ratio démographique (deux panneaux)
    te.table_indices()        # les indices de la seconde figure (onglet Données)
    te.fig_niveaux()          # pension moyenne et salaire moyen, dinars courants par mois
    te.table_niveaux()        # les niveaux de la troisième figure (onglet Données)

CE QUI EST TRACÉ. Le taux d'équilibre τ* est le taux de cotisation qui, appliqué à la masse
des salaires soumis à cotisation, paierait exactement les dépenses de pensions de l'année :

    τ* = dépenses ÷ masse cotisée = (pension moyenne ÷ salaire moyen) × (pensions ÷ cotisants)

c'est-à-dire un taux de remplacement apparent multiplié par un ratio de dépendance
démographique. Il se compare au taux légal global, agent et employeur, du régime général.

LE DÉNOMINATEUR N'A PAS LA MÊME NATURE SUR TOUTE LA PÉRIODE, et la figure le montre par le
style du trait et des marques (colonne `denominateur` de la série) :
  - 2014-2018 : cotisations salariales et patronales des états financiers ÷ taux légal ;
  - 2019-2020 : les mêmes, reconstituées à partir des hausses publiées ;
  - 2000-2013 : APPROXIMATION par la masse salariale de l'État, faute de cotisations publiées ;
  - 2021-2023 : ESTIMATION — dépenses tirées des charges de la caisse entière, masse salariale de
    l'État × rapport de 2020. Sans affiliés actifs publiés après 2021, 2022 et 2023 n'ont pas de
    décomposition : la seconde figure s'arrête en 2021.
  - 1980 et 1985-1991 : Banque mondiale (rapport 11376-TUN, 1993) — cotisations de pension ÷ 12 %,
    pensions versées prestations familiales des pensionnés comprises.
Le raccord 2013-2014 est tracé dans le style de l'approximation, le raccord 2020-2021 dans celui
de l'estimation.

LE TROU 1992-1999 ET LE TROU 1981-1984 NE SONT JAMAIS FRANCHIS. Aucune donnée n'a été retrouvée
pour ces années : les courbes sont tracées par suites d'années consécutives (`_suites`), 1980 est
un point isolé, et un fond hachuré signale 1992-1999. Les deux sources ne mesurent ni tout à fait
la même dépense (prestations familiales des pensionnés comprises avant 1992, dans une part
inconnue) ni la même assiette (taux effectif possiblement inférieur à 12 % avant le 12 septembre
1985) : une courbe qui les relierait ferait lire une évolution que rien ne mesure.

DEUX PANNEAUX POUR LA DÉCOMPOSITION. Un indice raccorde par construction : un seul indice de
1980 à 2021 ferait lire 1991 → 2000 comme une évolution mesurée. Le panneau de gauche porte
1980 et 1985-1991 en base 100 en 1985 — première année d'une suite continue ; 1980 est douteux
(affiliés actifs en hausse de 61 % de 1980 à 1985, sans explication de la source) —, celui de
droite 2000-2021 en base 100 en 2000. Même échelle logarithmique, mêmes graduations : les pentes
se comparent, les niveaux non.

LES NIVEAUX (`fig_niveaux`), eux, se tracent sur un seul axe : pension moyenne et salaire moyen
sont des dinars courants, sans base. Ce sont les mêmes grandeurs que la décomposition (p̄ =
dépenses ÷ pensions ÷ 12, w̄ = masse soumise à cotisation ÷ affiliés ÷ 12) : leur rapport est le
remplacement apparent de la seconde figure. Le salaire de 2000-2020 n'est PAS le « salaire
reconstitué » des recettes totales de la caisse (série cnrps-pensions), qui dépasse l'assiette
tirée des seules cotisations de 12 à 27 % en 2014-2018.

POURQUOI LA BASE 100 EN 2000, et non en 2014. Le ratio pensions / cotisants ne dépend pas du
dénominateur : il est exact sur toute la période. Seuls le taux d'équilibre et le taux de
remplacement apparent portent l'approximation, et ils la portent de la même façon ; leurs
années approchées sont marquées. Sur 2014-2020, où le dénominateur est tiré des cotisations, le
remplacement apparent est plat (log-variation −0,003) et le ratio porte toute la hausse
(+0,232) : la conclusion ne dépend pas du raccord. L'échelle logarithmique fait du taux
d'équilibre la somme visuelle de ses deux facteurs.

Les chiffres cités dans le texte du chapitre se recalculent depuis `table()`.
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

SERIE = "cnrps-taux-equilibre"

I = {
    "num": "dépenses du régime de retraite (numérateur)",
    "den": "masse des salaires soumis à cotisation (dénominateur)",
    "npens": "pensions, toutes natures (nombre)",
    "naff": "affiliés actifs",
    "pm": "pension moyenne mensuelle",
    "sm": "salaire moyen mensuel",
    "R": "taux de remplacement apparent",
    "D": "ratio pensions / cotisants",
    "t": "taux légal global (agent + employeur)",
    "tau": "taux d'équilibre",
    "ecart": "écart taux d'équilibre − taux légal",
    "tau_rg": "taux d'équilibre, régime général seul",
    "tau_var": "taux d'équilibre, variante : masse tirée des recettes techniques",
    "rec": "rapport assiette tirée des cotisations / masse salariale de l'État",
}

# Nature du dénominateur : libellé de la série → (clé, style de trait, marque, remplissage)
APP, COT, REC = ("masse salariale de l'État (approximation)", "cotisations",
                 "cotisations reconstituées")
EST = ("estimation : charges de la caisse × part des pensions 2019-2020 ; "
       "masse salariale de l'État × rapport assiette / masse de 2020")
BM = "Banque mondiale 1993 : cotisations de pension ÷ taux légal (12 %)"
_STYLE = {APP: ("--", "o", False), COT: ("-", "o", True), REC: (":", "D", True),
          EST: ("-.", "s", False), BM: ("-", "^", False)}
_ORDRE = (BM, APP, COT, REC, EST)
_LG = {BM: "lg_bm", APP: "lg_app", COT: "lg_cot", REC: "lg_rec", EST: "lg_est"}
TROU = (1992, 1999)   # aucune donnée
BASE_BM, BASE = 1985, 2000

_L = {
    "titre_taux": {
        "fr": "CNRPS : taux de cotisation d'équilibre et taux légal, 1980-2023",
        "ar": "الصندوق الوطني للتقاعد والحيطة الاجتماعية: نسبة المساهمة المحقّقة للتوازن والنسبة القانونية، 1980-2023"},
    "titre_decomp": {
        "fr": "CNRPS : décomposition du taux d'équilibre, en indices, 1980-2021",
        "ar": "الصندوق الوطني للتقاعد والحيطة الاجتماعية: تفكيك نسبة التوازن، مؤشرات، 1980-2021"},
    "titre_niveaux": {
        "fr": "CNRPS : pension moyenne et salaire moyen des affiliés actifs, 1980-2021",
        "ar": "الصندوق الوطني للتقاعد والحيطة الاجتماعية: معدّل الجراية ومعدّل أجر المنخرطين النشيطين، 1980-2021"},
    "panneau_bm": {"fr": "1980, 1985-1991 : base 100 en 1985", "ar": "1980، 1985-1991: أساس 100 سنة 1985"},
    "panneau_rec": {"fr": "2000-2021 : base 100 en 2000", "ar": "2000-2021: أساس 100 سنة 2000"},
    "y_niveaux": {"fr": "Dinars courants par mois (échelle logarithmique)",
                  "ar": "دنانير جارية شهرياً (سلّم لوغاريتمي)"},
    "lg_pm": {"fr": "Pension moyenne, toutes natures (p̄)", "ar": "معدّل الجراية، بجميع الأصناف (p̄)"},
    "lg_sm": {"fr": "Salaire moyen des affiliés actifs (w̄)", "ar": "معدّل أجر المنخرطين النشيطين (w̄)"},
    "trou": {"fr": "1992-1999 :\naucune donnée", "ar": "1992-1999:\nلا معطيات"},
    "lg_bm": {"fr": "1980, 1985-1991 : Banque mondiale (1993), cotisations ÷ 12 %,\nsans raccord avec 2000",
              "ar": "1980، 1985-1991: البنك الدولي (1993)، المساهمات ÷ 12 %،\nدون ربط مع سنة 2000"},
    "x": {"fr": "Année", "ar": "السنة"},
    "y_taux": {"fr": "% des salaires soumis à cotisation", "ar": "% من الأجور الخاضعة للمساهمة"},
    "y_indice": {"fr": "Indice (échelle logarithmique)",
                 "ar": "مؤشر (سلّم لوغاريتمي)"},
    "lg_tau": {"fr": "Taux d'équilibre (dépenses ÷ masse cotisée)",
               "ar": "نسبة التوازن (النفقات ÷ الأجور الخاضعة للمساهمة)"},
    "lg_t": {"fr": "Taux légal global (agent + employeur)",
             "ar": "النسبة القانونية الجملية (العون + المؤجّر)"},
    "lg_R": {"fr": "Taux de remplacement apparent (pension moyenne ÷ salaire moyen)",
             "ar": "نسبة التعويض الظاهرة (معدّل الجراية ÷ معدّل الأجر)"},
    "lg_D": {"fr": "Pensions ÷ cotisants (indépendant du dénominateur)",
             "ar": "الجرايات ÷ المساهمون (لا يتأثّر بالمقام)"},
    "lg_app": {"fr": "2000-2013 : masse salariale de l'État (approximation)",
               "ar": "2000-2013: كتلة أجور الدولة (تقريب)"},
    "lg_cot": {"fr": "2014-2018 : salaires déduits des cotisations publiées",
               "ar": "2014-2018: أجور مستنتجة من المساهمات المنشورة"},
    "lg_rec": {"fr": "2019-2020 : salaires déduits de cotisations reconstituées\n(niveau 2018 + hausses publiées)",
               "ar": "2019-2020: أجور مستنتجة من مساهمات معاد تركيبها\n(مستوى 2018 + الزيادات المنشورة)"},
    "lg_est": {"fr": "2021-2023 : estimation (dépenses tirées des charges de la caisse,\nmasse salariale de l'État × rapport de 2020)",
               "ar": "2021-2023: تقدير (نفقات مستنتجة من أعباء الصندوق،\nكتلة أجور الدولة × نسبة 2020)"},
    "lg_est_2021": {"fr": "2021 : estimation (dépenses tirées des charges de la caisse,\nmasse salariale de l'État × rapport de 2020)",
                    "ar": "2021: تقدير (نفقات مستنتجة من أعباء الصندوق،\nكتلة أجور الدولة × نسبة 2020)"},
    "titre_lg_den": {"fr": "Masse des salaires soumis à cotisation", "ar": "كتلة الأجور الخاضعة للمساهمة"},
    # Colonnes de l'onglet Données
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_den_nature": {"fr": "Dénominateur", "ar": "المقام"},
    "col_num": {"fr": "Dépenses du régime (MD)", "ar": "نفقات النظام (م.د)"},
    "col_den": {"fr": "Masse soumise à cotisation (MD)", "ar": "الأجور الخاضعة للمساهمة (م.د)"},
    "col_npens": {"fr": "Pensions, toutes natures", "ar": "الجرايات بجميع أصنافها"},
    "col_naff": {"fr": "Affiliés actifs", "ar": "المنخرطون النشيطون"},
    "col_pm": {"fr": "Pension moyenne (D/mois)", "ar": "معدّل الجراية (د/شهر)"},
    "col_sm": {"fr": "Salaire moyen (D/mois)", "ar": "معدّل الأجر (د/شهر)"},
    "col_R": {"fr": "Remplacement apparent (%)", "ar": "نسبة التعويض الظاهرة (%)"},
    "col_D": {"fr": "Pensions ÷ cotisants (%)", "ar": "الجرايات ÷ المساهمون (%)"},
    "col_t": {"fr": "Taux légal global (%)", "ar": "النسبة القانونية الجملية (%)"},
    "col_tau": {"fr": "Taux d'équilibre (%)", "ar": "نسبة التوازن (%)"},
    "col_ecart": {"fr": "Écart (points)", "ar": "الفارق (نقاط)"},
    "col_tau_rg": {"fr": "Taux d'équilibre, régime général seul (%)",
                   "ar": "نسبة التوازن، النظام العام وحده (%)"},
    "col_tau_var": {"fr": "Taux d'équilibre, variante indexée sur les recettes techniques (%)",
                    "ar": "نسبة التوازن، صيغة مرتبطة بالإيرادات الفنية (%)"},
    "col_rec": {"fr": "Assiette ÷ masse salariale de l'État",
                "ar": "قاعدة المساهمات ÷ كتلة أجور الدولة"},
    "col_src_num": {"fr": "Source des dépenses", "ar": "مصدر النفقات"},
    "col_src_den": {"fr": "Source du dénominateur", "ar": "مصدر المقام"},
    "col_base": {"fr": "Année de base (= 100)", "ar": "سنة الأساس (= 100)"},
    "col_i_tau": {"fr": "Taux d'équilibre (indice)", "ar": "نسبة التوازن (مؤشر)"},
    "col_i_R": {"fr": "Remplacement apparent (indice)", "ar": "نسبة التعويض الظاهرة (مؤشر)"},
    "col_i_D": {"fr": "Pensions ÷ cotisants (indice)", "ar": "الجرايات ÷ المساهمون (مؤشر)"},
}

_DEN = {BM: {"fr": "Banque mondiale (1993) : cotisations de pension ÷ 12 % ; pensions versées, prestations "
                  "familiales des pensionnés comprises ; sans raccord avec 2000",
              "ar": "البنك الدولي (1993): مساهمات التقاعد ÷ 12 %؛ الجرايات المدفوعة بما فيها المنح العائلية "
                    "للمتقاعدين؛ دون ربط مع سنة 2000"},
        APP: {"fr": APP, "ar": "كتلة أجور الدولة (تقريب)"},
        COT: {"fr": "salaires déduits des cotisations publiées",
              "ar": "أجور مستنتجة من المساهمات المنشورة"},
        REC: {"fr": "salaires déduits de cotisations reconstituées (niveau 2018 + hausses publiées)",
              "ar": "أجور مستنتجة من مساهمات معاد تركيبها (مستوى 2018 + الزيادات المنشورة)"},
        EST: {"fr": "estimation : dépenses tirées des charges de la caisse entière × part des pensions "
                    "2019-2020 ; masse salariale de l'État × rapport assiette / masse de 2020",
              "ar": "تقدير: نفقات مستنتجة من أعباء الصندوق بأكمله × حصّة الجرايات 2019-2020؛ "
                    "كتلة أجور الدولة × نسبة القاعدة إلى الكتلة لسنة 2020"}}

BLEU, GRIS, ORANGE, VERT = "#08519c", "#57606a", "#bf8700", "#1a7f37"


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _den(nature: str) -> str:
    return _DEN[nature].get(figtools.lang(), _DEN[nature]["fr"])


def _donnees():
    """{année: {clé: valeur, 'nature': …, 'src_num': …, 'src_den': …}}, 1980, 1985-1991, 2000-2023.

    Les années 2022-2023 n'ont ni `naff`, ni `pm`, `sm`, `R`, `D` : les lire par `.get`."""
    df = figtools.series(SERIE)
    inv = {v: k for k, v in I.items()}
    out: dict[int, dict] = {}
    for r in df.itertuples():
        d = out.setdefault(int(r.annee), {})
        k = inv.get(r.indicateur)
        if k is None:
            continue
        d[k] = float(r.valeur)
        d["nature"] = r.denominateur
        if k == "num":
            d["src_num"] = r.source
        elif k == "den":
            d["src_den"] = r.source
    return dict(sorted(out.items()))


def table():
    import pandas as pd

    def pct(x, n=2):
        return None if x is None else round(100 * x, n)

    def rnd(x, n=1):
        return None if x is None else round(x, n)

    lignes = []
    for a, d in _donnees().items():
        lignes.append({
            _lab("col_annee"): a,
            _lab("col_den_nature"): _den(d["nature"]),
            _lab("col_tau"): pct(d["tau"]),
            _lab("col_t"): pct(d["t"]),
            _lab("col_ecart"): pct(d["ecart"]),
            _lab("col_R"): pct(d.get("R")),
            _lab("col_D"): pct(d.get("D")),
            _lab("col_pm"): rnd(d.get("pm")),
            _lab("col_sm"): rnd(d.get("sm")),
            _lab("col_num"): round(d["num"], 1),
            _lab("col_den"): round(d["den"], 1),
            _lab("col_npens"): int(d["npens"]),
            _lab("col_naff"): None if d.get("naff") is None else int(d["naff"]),
            _lab("col_tau_rg"): pct(d.get("tau_rg")),
            _lab("col_tau_var"): pct(d.get("tau_var")),
            _lab("col_rec"): None if d.get("rec") is None else round(d["rec"], 3),
            _lab("col_src_num"): d["src_num"],
            _lab("col_src_den"): d["src_den"],
        })
    df = pd.DataFrame(lignes)
    df[_lab("col_naff")] = df[_lab("col_naff")].astype("Int64")
    return df


def _indices():
    """Indices des seules années décomposables (affiliés publiés), chaque période sur sa base :
    1980 et 1985-1991 en base 100 en 1985, 2000-2021 en base 100 en 2000. Aucun indice ne
    traverse 1992-1999."""
    d = {a: v for a, v in _donnees().items() if "R" in v and "D" in v}
    out = {}
    for a, v in d.items():
        base = BASE_BM if a < TROU[0] else BASE
        out[a] = ({k: 100 * v[k] / d[base][k] for k in ("tau", "R", "D")}
                  | {"nature": v["nature"], "base": base})
    return out


def table_indices():
    import pandas as pd
    return pd.DataFrame([{
        _lab("col_annee"): a,
        _lab("col_den_nature"): _den(v["nature"]),
        _lab("col_base"): v["base"],
        _lab("col_i_tau"): round(v["tau"], 1),
        _lab("col_i_R"): round(v["R"], 1),
        _lab("col_i_D"): round(v["D"], 1),
    } for a, v in _indices().items()])


def table_niveaux():
    import pandas as pd
    return pd.DataFrame([{
        _lab("col_annee"): a,
        _lab("col_den_nature"): _den(v["nature"]),
        _lab("col_pm"): round(v["pm"], 1),
        _lab("col_sm"): round(v["sm"], 1),
        _lab("col_R"): round(100 * v["R"], 1),
    } for a, v in _donnees().items() if "pm" in v and "sm" in v])


def _suites(annees):
    """Découpe une liste d'années croissantes en suites d'années consécutives."""
    out = []
    for a in annees:
        if out and a == out[-1][-1] + 1:
            out[-1].append(a)
        else:
            out.append([a])
    return out


def _trace_par_nature(ax, annees, valeurs, natures, couleur, lw=2.2, ms=5.5):
    """Trace une série dont le style suit la nature du dénominateur.

    Chaque segment [a, a+1] prend le style de l'année a : le raccord 2013-2014 est donc
    tiret (approximation), celui de 2018-2019 plein. Exception : le segment qui mène à une
    année estimée prend le style de l'estimation, qui commence donc dès le raccord 2020-2021.
    Les marques suivent l'année elle-même. Deux années non consécutives (1980 et 1985, 1991
    et 2000) ne sont jamais reliées.
    """
    for i in range(len(annees) - 1):
        if annees[i + 1] != annees[i] + 1:
            continue
        ls, _, _ = _STYLE[EST if natures[i + 1] == EST else natures[i]]
        ax.plot(annees[i:i + 2], valeurs[i:i + 2], ls, color=couleur, lw=lw)
    for a, v, n in zip(annees, valeurs, natures):
        _, mk, plein = _STYLE[n]
        ax.plot([a], [v], mk, color=couleur, ms=ms, mfc=couleur if plein else "white", mew=1.4)


def _poignees_denominateur(ft, natures, lg=None):
    lg = _LG | (lg or {})
    return [Line2D([], [], ls=_STYLE[n][0], marker=_STYLE[n][1], color=GRIS, lw=1.6, ms=5,
                   mfc=GRIS if _STYLE[n][2] else "white", mew=1.3, label=ft(_lab(lg[n])))
            for n in _ORDRE if n in set(natures)]


def _legende_denominateur(ax, ft, loc, natures, lg=None):
    return ax.legend(handles=_poignees_denominateur(ft, natures, lg), loc=loc, fontsize=8,
                     title=ft(_lab("titre_lg_den")), title_fontsize=8)


def _fonds(ax, an, nat):
    """Fonds grisés : approximation (2000-2013) et estimation (années marquées EST)."""
    app = [a for a, n in zip(an, nat) if n == APP]
    if app:
        ax.axvspan(min(app) - 0.5, max(app) + 0.5, color=GRIS, alpha=0.06, lw=0)
    est = [a for a, n in zip(an, nat) if n == EST]
    if est:
        ax.axvspan(min(est) - 0.5, max(est) + 0.7, color=ORANGE, alpha=0.07, lw=0)


def _trou(ax, ft, y):
    """Hachure et cartouche sur 1992-1999, que rien ne documente."""
    ax.axvspan(TROU[0] - 0.5, TROU[1] + 0.5, facecolor="none", edgecolor=GRIS, hatch="///",
               alpha=0.25, lw=0)
    ax.text((TROU[0] + TROU[1]) / 2, y, "\n".join(ft(l) for l in _lab("trou").split("\n")),
            fontsize=7.5, color=GRIS, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1.5))


def _axe_annees(ax, fin, debut=2000, pas=2):
    ax.set_xlim(debut - 0.7, fin + 0.7)
    ax.set_xticks(range(debut, fin + 1, pas))


def fig_taux():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    an = list(d)
    nat = [d[a]["nature"] for a in an]

    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    _fonds(ax, an, nat)
    _trou(ax, ft, 30)
    _trace_par_nature(ax, an, [100 * d[a]["tau"] for a in an], nat, BLEU)
    for suite in _suites(an):
        if len(suite) == 1:   # 1980 : un palier court, centré sur l'année
            a = suite[0]
            ax.plot([a - 0.5, a + 0.5], [100 * d[a]["t"]] * 2, color=GRIS, lw=2)
        else:
            ax.step(suite, [100 * d[a]["t"] for a in suite], where="mid", color=GRIS, lw=2)
    dernier_observe = max(a for a in an if d[a]["nature"] != EST)
    dernier_bm = max(a for a in an if a < TROU[0])
    for a in sorted({an[0], dernier_bm, BASE, dernier_observe, an[-1]}):
        ax.annotate(f"{100 * d[a]['tau']:.1f}".replace(".", ","), (a, 100 * d[a]["tau"]),
                    textcoords="offset points", xytext=(0, -14 if a == an[0] else 8), ha="center",
                    fontsize=8, color=BLEU)
        ax.annotate(f"{100 * d[a]['t']:.1f}".replace(".", ","), (a, 100 * d[a]["t"]),
                    textcoords="offset points", xytext=(0, -13), ha="center", fontsize=8, color=GRIS)
    principale = ax.legend(handles=[
        Line2D([], [], color=BLEU, lw=2.2, label=ft(_lab("lg_tau"))),
        Line2D([], [], color=GRIS, lw=2, label=ft(_lab("lg_t")))],
        loc="upper left", fontsize=8.5)
    ax.add_artist(principale)
    _legende_denominateur(ax, ft, "lower right", nat)
    _axe_annees(ax, an[-1], debut=1980, pas=5)
    ax.set_ylim(0, 40)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_taux")))
    ax.set_title(ft(_lab("titre_taux")))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def _panneau_indices(ax, ix, an, ft, annoter):
    nat = [ix[a]["nature"] for a in an]
    _fonds(ax, an, nat)
    ax.axhline(100, color=GRIS, lw=0.8, alpha=0.6)
    _trace_par_nature(ax, an, [ix[a]["tau"] for a in an], nat, BLEU)
    _trace_par_nature(ax, an, [ix[a]["R"] for a in an], nat, ORANGE, lw=1.8, ms=4.5)
    # Le ratio démographique ne dépend pas du dénominateur : trait plein, par suites d'années.
    for suite in _suites(an):
        ax.plot(suite, [ix[a]["D"] for a in suite], "s-", color=VERT, lw=1.8, ms=4.5)
    for a in annoter:
        for k, c, dy in (("tau", BLEU, 6), ("D", VERT, -12), ("R", ORANGE, -12)):
            ax.annotate(f"{ix[a][k]:.0f}", (a, ix[a][k]), textcoords="offset points",
                        xytext=(0, dy), ha="center", fontsize=8, color=c)
    ax.set_yscale("log")
    ax.set_yticks([70, 80, 90, 100, 125, 150, 175, 200])
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f}"))
    ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_ylim(64, 215)
    ax.grid(True, which="major", alpha=0.3)
    return nat


def fig_decomposition():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    ix = _indices()
    an_bm = [a for a in ix if a < TROU[0]]
    an = [a for a in ix if a > TROU[1]]

    fig, (ax0, ax) = plt.subplots(1, 2, figsize=(10.5, 7.2), sharey=True,
                                  gridspec_kw={"width_ratios": [12, 22]})
    _panneau_indices(ax0, ix, an_bm, ft, (an_bm[0], an_bm[-1]))
    nat = _panneau_indices(ax, ix, an, ft, (an[-1],))
    _axe_annees(ax0, an_bm[-1], debut=an_bm[0], pas=2)
    _axe_annees(ax, an[-1], debut=an[0], pas=4)
    ax0.set_title(ft(_lab("panneau_bm")), fontsize=9)
    ax.set_title(ft(_lab("panneau_rec")), fontsize=9)
    ax0.set_ylabel(ft(_lab("y_indice")))
    ax0.set_xlabel(ft(_lab("x")))
    ax.set_xlabel(ft(_lab("x")))
    fig.suptitle(ft(_lab("titre_decomp")))
    # Légendes sous les deux panneaux : dans les axes, elles masqueraient des points.
    fig.tight_layout(rect=(0, 0.25, 1, 1))
    fig.legend(handles=[
        Line2D([], [], color=BLEU, lw=2.2, label=ft(_lab("lg_tau"))),
        Line2D([], [], color=VERT, lw=1.8, marker="s", ms=4.5, label=ft(_lab("lg_D"))),
        Line2D([], [], color=ORANGE, lw=1.8, label=ft(_lab("lg_R")))],
        loc="upper left", bbox_to_anchor=(0.01, 0.235), fontsize=8, frameon=False)
    fig.legend(handles=_poignees_denominateur(ft, [ix[a]["nature"] for a in ix],
                                              {EST: "lg_est_2021"} if an[-1] == 2021 else None),
               loc="upper right", bbox_to_anchor=(0.99, 0.235), fontsize=8, frameon=False,
               title=ft(_lab("titre_lg_den")), title_fontsize=8)
    return fig


def fig_niveaux():
    """Pension moyenne et salaire moyen, dinars courants par mois, échelle logarithmique."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = {a: v for a, v in _donnees().items() if "pm" in v and "sm" in v}
    an = list(d)
    nat = [d[a]["nature"] for a in an]

    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    _fonds(ax, an, nat)
    _trou(ax, ft, 600)
    _trace_par_nature(ax, an, [d[a]["sm"] for a in an], nat, BLEU)
    _trace_par_nature(ax, an, [d[a]["pm"] for a in an], nat, ORANGE)
    for a in (an[0], max(a for a in an if a < TROU[0]), BASE, an[-1]):
        for k, c, dy in (("sm", BLEU, 7), ("pm", ORANGE, -13)):
            ax.annotate(f"{d[a][k]:,.0f}".replace(",", "\u202f"), (a, d[a][k]),
                        textcoords="offset points", xytext=(0, dy), ha="center", fontsize=8, color=c)
    ax.set_yscale("log")
    ax.set_yticks([50, 100, 200, 500, 1000, 2000])
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda v, _: f"{v:,.0f}".replace(",", "\u202f")))
    ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_ylim(40, 3000)
    principale = ax.legend(handles=[
        Line2D([], [], color=BLEU, lw=2.2, label=ft(_lab("lg_sm"))),
        Line2D([], [], color=ORANGE, lw=2.2, label=ft(_lab("lg_pm")))],
        loc="upper left", fontsize=8.5)
    ax.add_artist(principale)
    _legende_denominateur(ax, ft, "lower right", nat, {EST: "lg_est_2021"} if an[-1] == 2021 else None)
    _axe_annees(ax, an[-1], debut=1980, pas=5)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_niveaux")))
    ax.set_title(ft(_lab("titre_niveaux")))
    ax.grid(True, which="major", alpha=0.3)
    fig.tight_layout()
    return fig

"""Figure du chapitre « Le droit de timbre et les droits d'enregistrement » du livre *Fiscalité*.

D'OÙ VIENNENT LES DONNÉES. D'un relevé versionné DANS le livre, à côté du chapitre
(`timbre/rendement-timbre-enregistrement.csv`, avec son manifeste `.csv.yml`) : les lignes du
tableau A des lois de finances initiales (prévisions, 2001-2026) et les réalisations que
publie la Cour des comptes (2018-2023). Ce n'est pas une statistique de l'entrepôt : la
figure le lit directement, comme `regimes_incitation.py` lit les siens.

BUDGÉTAIRE SEUL. Aucun PIB, aucune part du total : les « totaux de la première partie » du
tableau A changent de périmètre d'une année à l'autre (fonds spéciaux, prélèvements sur les
comptes spéciaux), et le chapitre ne les emploie pas.

LA RUPTURE DE 2020 SE MONTRE. Le tableau A change de nomenclature en 2020 : la ligne « autres
droits d'enregistrement » (24-03) cède la place aux « droits sur les actes et transactions »
(18-02), sans définition commune. Les deux sont deux courbes, de deux teintes, jamais jointes ;
aucune courbe ne relie 2019 à 2020, et un trait vertical marque la rupture. Pour 2019, la Cour
des comptes donne la réalisation dans les deux nomenclatures : les deux points sont tracés.

PRÉVISIONS ET RÉALISATIONS SE DISTINGUENT PAR LE STYLE. Trait plein et petits points pour les
prévisions ; gros marqueurs creux, sans trait, pour les réalisations.

LA TAXE UNIQUE EN 2021 ET 2022. Le tableau A imprime 2 MD en regard de la taxe, valeur
probablement permutée avec celle des formalités : elle reste dans les données (`trace = non`)
et la courbe s'interrompt.

QUATRE VUES, une à la fois. (1) Millions de dinars courants. (2) Part des dépenses de l'État :
dénominateur `denominateurs-depenses-etat-pib`, colonne `depenses_etat_hors_dette_MDT`, dépenses
de l'État hors service de la dette, RÉALISATIONS du classeur du ministère des Finances, 1986-2025,
une seule série sans changement de périmètre ; le numérateur est voté (prévision) ou réalisé
(Cour des comptes), le dénominateur réalisé : la part donne un ordre de grandeur. (3) Part du
PIB, une courbe par base des comptes nationaux (1983, 1997, 2015, série `pib-courant-par-base`),
jamais raccordées : une année publiée dans deux bases porte deux points, chacun rapporté au PIB
de sa base ; les trois valeurs du ministère que la source ne rattache à aucune base (2002-2004,
2025) ne sont pas tracées, elles sont dans l'onglet « Données » ; la rupture de base renvoie à
l'annexe sur le PIB. (4) Millions de dinars de 2025 : indice des prix à la consommation de
l'INS, base 1970 = 100, moyenne annuelle, `scripts/dinars_constants.py` ; 2024 et 2025 prolongés
par la variation de l'indice en base 2015 que relaie la Banque centrale (seul raccord de la
période) ; sans 2026, dont l'indice n'est pas publié. Un montant d'exercice se déflate par
l'indice annuel moyen de l'exercice.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402
import dinars_constants  # noqa: E402

HERE = Path(__file__).resolve().parent
RELEVES = HERE.parent / "timbre"
NOM = "rendement-timbre-enregistrement"
SERIE = "timbre-enregistrement-rendement"
SERIE_DEP = "denominateurs-depenses-etat-pib"
SERIE_PIB = "pib-courant-par-base"
SERIES = (SERIE, SERIE_DEP, SERIE_PIB, *dinars_constants.SERIES_IPC)
BASES = {1983: ("o", "#57606a"), 1997: ("s", "#57606a"), 2015: ("^", "#57606a")}
BASE = dinars_constants.ANNEE_BASE
RUPTURE = 2020

COULEURS = {
    "timbre": "#0969da",
    "autres_droits_enregistrement": "#bc4c00",
    "actes_transactions": "#8250df",
    "taxe_unique_assurances": "#1a7f37",
}
ORDRE = list(COULEURS)

_L = {
    "timbre": {"fr": "Droit de timbre", "ar": "معاليم الطابع الجبائي"},
    "autres_droits_enregistrement": {
        "fr": "Autres droits d'enregistrement (24-03, jusqu'en 2019)",
        "ar": "معاليم أخرى على التسجيل (24-03، إلى غاية 2019)"},
    "actes_transactions": {
        "fr": "Droits sur les actes et transactions (18-02, depuis 2020)",
        "ar": "معاليم على العقود والمبادلات (18-02، منذ 2020)"},
    "taxe_unique_assurances": {"fr": "Taxe unique sur les assurances",
                               "ar": "المعلوم الوحيد على التأمين"},
    "prev": {"fr": "prévision (loi de finances)", "ar": "تقديرات (قانون المالية)"},
    "real": {"fr": "réalisation (Cour des comptes)", "ar": "إنجازات (محكمة المحاسبات)"},
    "rupture": {"fr": "nouvelle nomenclature\ndu tableau A (2020)",
                "ar": "تبويب جديد\nللجدول أ (2020)"},
    "y_cour": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "y_cst": {"fr": f"Millions de dinars de {BASE}", "ar": f"ملايين الدنانير بأسعار {BASE}"},
    "vue_cour": {"fr": "Dinars courants", "ar": "بالدينار الجاري"},
    "vue_dep": {"fr": "Part des dépenses de l'État", "ar": "حصة نفقات الدولة"},
    "vue_pib": {"fr": "Part du PIB", "ar": "حصة الناتج الداخلي الخام"},
    "y_dep": {"fr": "En % des dépenses de l'État hors dette (réalisées)",
              "ar": "% من نفقات الدولة دون الدين (منجزة)"},
    "y_pib": {"fr": "En % du PIB de la base", "ar": "% من ناتج الأساس"},
    "base_leg": {"fr": "PIB de base {b}", "ar": "ناتج أساس {b}"},
    "rup_pib": {"fr": "PIB : base {b}", "ar": "الناتج: أساس {b}"},
    "col_vue": {"fr": "Vue", "ar": "العرض"},
    "col_val": {"fr": "Valeur de la vue", "ar": "قيمة العرض"},
    "col_unite": {"fr": "Unité", "ar": "الوحدة"},
    "col_den": {"fr": "Dénominateur ou indice", "ar": "المقام أو المؤشر"},
    "col_base": {"fr": "Base ou nature du dénominateur", "ar": "أساس المقام أو طبيعته"},
    "col_srcden": {"fr": "Source du dénominateur", "ar": "مصدر المقام"},
    "vue_cst": {"fr": f"Dinars de {BASE}", "ar": f"بدينار سنة {BASE}"},
    "xlabel": {"fr": "Exercice", "ar": "السنة المالية"},
    "col_annee": {"fr": "Exercice", "ar": "السنة المالية"},
    "col_nature": {"fr": "Nature", "ar": "الطبيعة"},
    "col_ligne": {"fr": "Ligne", "ar": "السطر"},
    "col_nomen": {"fr": "Nomenclature", "ar": "التبويب"},
    "col_code": {"fr": "Article du tableau A", "ar": "فصل الجدول أ"},
    "col_lib": {"fr": "Libellé de la source", "ar": "تسمية المصدر"},
    "col_md": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "col_cst": {"fr": f"Millions de dinars de {BASE}", "ar": f"ملايين الدنانير بأسعار {BASE}"},
    "col_trace": {"fr": "Tracée", "ar": "مرسومة"},
    "col_src": {"fr": "Source", "ar": "المصدر"},
    "col_page": {"fr": "Page", "ar": "الصفحة"},
    "col_rem": {"fr": "Remarque", "ar": "ملاحظة"},
}


def _l(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _sources() -> list[str]:
    import yaml
    return list(yaml.safe_load(
        (RELEVES / f"{NOM}.csv.yml").read_text(encoding="utf-8"))["sources"])


figtools.register_provenance(
    SERIE,
    titre=("Droit de timbre, autres droits d'enregistrement et taxe unique sur les assurances : "
           "prévisions des lois de finances (2001-2026) et réalisations (2018-2023)"),
    sources=_sources(),
    unite="millions de dinars courants",
    perimetre=("lignes du tableau A des lois de finances initiales (24-01, 24-03, 24-04 "
               "jusqu'en 2019 ; 18-01, 18-02, 18-04 depuis 2020) ; réalisations relevées dans "
               "les rapports de la Cour des comptes sur la clôture du budget de l'État"),
    caveats=("Prévisions et réalisations ne se confondent pas. Nomenclature du tableau A changée "
             "en 2020 : 24-03 et 18-02 ne se raccordent pas. Taxe unique sur les assurances, "
             "2021 et 2022 : valeur imprimée de 2 MD, probablement permutée avec celle des "
             "formalités administratives, gardée dans les données et non tracée."),
)


def lire() -> pd.DataFrame:
    return pd.read_csv(RELEVES / f"{NOM}.csv")


def _constants(df: pd.DataFrame) -> pd.Series:
    ipc = dinars_constants.ipc()
    return pd.Series([
        round(v * ipc[BASE] / ipc[a], 1) if a in ipc and a <= BASE else float("nan")
        for a, v in zip(df["annee"], df["valeur_md"])], index=df.index)


def _segments(annees: list[int]) -> list[list[int]]:
    """Découpe en années consécutives, et coupe toujours entre 2019 et 2020."""
    segs: list[list[int]] = []
    for a in sorted(annees):
        if segs and a == segs[-1][-1] + 1 and a != RUPTURE:
            segs[-1].append(a)
        else:
            segs.append([a])
    return segs


def _trace(colonne: str, ylabel: str, fin: int):
    figtools.apply_lang_font()
    df = lire()
    df["v"] = df["valeur_md"] if colonne == "valeur_md" else _constants(df)
    df = df[(df["trace"] == "oui") & (df["annee"] <= fin)].dropna(subset=["v"])
    fig, ax = plt.subplots(figsize=(9, 5.2))
    for ligne in ORDRE:
        c = COULEURS[ligne]
        p = df[(df["ligne"] == ligne) & (df["nature"] == "prévision")]
        for nomen in p["nomenclature"].unique():
            q = p[p["nomenclature"] == nomen].set_index("annee")["v"]
            for k, seg in enumerate(_segments(list(q.index))):
                ax.plot(seg, [q[a] for a in seg], color=c, lw=1.8, marker="o", ms=3,
                        label=figtools.fig_text(_l(ligne)) if (k == 0 and nomen == p["nomenclature"].iloc[0]) else None)
        r = df[(df["ligne"] == ligne) & (df["nature"] == "réalisation")]
        ax.scatter(r["annee"], r["v"], s=48, facecolors="white", edgecolors=c, linewidths=1.6,
                   zorder=3)
    figtools.marque_rupture(ax, RUPTURE, figtools.fig_text(_l("rupture")))
    # Clé des styles : prévision, réalisation.
    ax.plot([], [], color="#57606a", lw=1.8, marker="o", ms=3,
            label=figtools.fig_text(_l("prev")))
    ax.scatter([], [], s=48, facecolors="white", edgecolors="#57606a", linewidths=1.6,
               label=figtools.fig_text(_l("real")))
    ax.set_xlim(2000.5, fin + 0.5)
    ax.set_ylim(bottom=0)
    ax.set_xlabel(figtools.fig_text(_l("xlabel")))
    ax.set_ylabel(figtools.fig_text(ylabel))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=8,
              frameon=False)
    fig.tight_layout()
    return fig


def _depenses() -> pd.Series:
    """Dépenses de l'État hors service de la dette, réalisations, en MD, par exercice."""
    d = figtools.series(SERIE_DEP).set_index("annee")["depenses_etat_hors_dette_MDT"]
    return d.dropna()


def _pib() -> pd.DataFrame:
    """Une ligne par (exercice, base) : jamais de raccord ; valeurs « non rattachées » à part."""
    pib = figtools.series(SERIE_PIB).copy()
    t = pib["base"].str
    pib["base_num"] = t.extract(r"(1983|1997|2015)", expand=False).astype("Int64")
    pib["presumee"] = t.contains("présumée")
    pib["minfin"] = t.startswith("non rattachée")
    return pib


def _base_nom(r) -> str:
    if r.minfin:
        return "non rattachée à une base (ministère des Finances)"
    return f"base {int(r.base_num)}" + (" présumée" if r.presumee else "")


def _trace_dep(fin: int = 2025):
    figtools.apply_lang_font()
    df = lire()
    dep = _depenses()
    df = df[(df["trace"] == "oui") & (df["annee"] <= fin) & df["annee"].isin(dep.index)].copy()
    df["v"] = [100 * v / dep[a] for a, v in zip(df["annee"], df["valeur_md"])]
    return _courbes(df, _l("y_dep"), fin)


def _courbes(df: pd.DataFrame, ylabel: str, fin: int, bases: bool = False):
    fig, ax = plt.subplots(figsize=(9, 5.2))
    for ligne in ORDRE:
        c = COULEURS[ligne]
        p = df[(df["ligne"] == ligne) & (df["nature"] == "prévision")]
        for nomen in p["nomenclature"].unique():
            q = p[p["nomenclature"] == nomen]
            for b, g0 in (q.groupby("base_num") if bases else [(None, q)]):
                g = g0.set_index("annee")["v"]
                m = BASES[int(b)][0] if bases else "o"
                for k, seg in enumerate(_segments(list(g.index))):
                    ax.plot(seg, [g[a] for a in seg], color=c, lw=1.6, marker=m, ms=3.5,
                            label=figtools.fig_text(_l(ligne)) if (k == 0 and not bases and nomen == p["nomenclature"].iloc[0]) else None)
        r = df[(df["ligne"] == ligne) & (df["nature"] == "réalisation")]
        ax.scatter(r["annee"], r["v"], s=48, facecolors="white", edgecolors=c, linewidths=1.6,
                   zorder=3)
    if bases:
        ax.axvline(2009.5, color="#57606a", ls=(0, (2, 2)), lw=1)
        ax.annotate(figtools.fig_text(_l("rup_pib", b=2015) if False else _L["rup_pib"][figtools.lang()].format(b=2015)),
                    xy=(2009.5, 0), xycoords=("data", "axes fraction"), xytext=(-4, 4),
                    textcoords="offset points", ha="right", va="bottom", fontsize=7, color="#57606a")
    figtools.marque_rupture(ax, RUPTURE, figtools.fig_text(_l("rupture")))
    ax.plot([], [], color="#57606a", lw=1.6, marker="o", ms=3, label=figtools.fig_text(_l("prev")))
    ax.scatter([], [], s=48, facecolors="white", edgecolors="#57606a", linewidths=1.6,
               label=figtools.fig_text(_l("real")))
    if bases:
        for b, (m, col) in BASES.items():
            ax.plot([], [], color=col, marker=m, ms=4, lw=0,
                    label=figtools.fig_text(_L["base_leg"][figtools.lang()].format(b=b)))
    ax.set_xlim(2000.5, fin + 0.5)
    ax.set_ylim(bottom=0)
    ax.set_xlabel(figtools.fig_text(_l("xlabel")))
    ax.set_ylabel(figtools.fig_text(ylabel))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def _trace_pib(fin: int = 2025):
    figtools.apply_lang_font()
    df = lire()
    pib = _pib()
    pib = pib[~pib["minfin"]][["annee", "base_num", "pib_MD"]]
    d = df[(df["trace"] == "oui") & (df["annee"] <= fin)].merge(pib, on="annee", how="inner")
    d["v"] = 100 * d["valeur_md"] / d["pib_MD"]
    d["base_num"] = d["base_num"].astype(int)
    return _courbes(d, _l("y_pib"), fin, bases=True)


def fig_rendement():
    """Quatre vues : dinars courants ; part des dépenses ; part du PIB par base ; dinars de 2025."""
    return [
        (_l("vue_cour"), _trace("valeur_md", _l("y_cour"), 2026)),
        (_l("vue_dep"), _trace_dep()),
        (_l("vue_pib"), _trace_pib()),
        (_l("vue_cst"), _trace("constants", _l("y_cst"), BASE)),
    ]


def table() -> pd.DataFrame:
    """Une ligne par exercice, par ligne du tableau A et par vue (et par base pour le PIB)."""
    df = lire()
    ipc = dinars_constants.ipc()
    dep = _depenses()
    pib = _pib()
    lignes = []

    def ajoute(r, vue, val, unite, den, base, srcden):
        lignes.append({
            _l("col_annee"): int(r.annee), _l("col_vue"): _l(vue), _l("col_nature"): r.nature,
            _l("col_ligne"): _l(r.ligne), _l("col_nomen"): r.nomenclature,
            _l("col_code"): r.code_article, _l("col_val"): val, _l("col_unite"): unite,
            _l("col_den"): den, _l("col_base"): base, _l("col_srcden"): srcden,
            _l("col_trace"): r.trace, _l("col_src"): r.source, _l("col_page"): r.localisateur,
            _l("col_rem"): "" if pd.isna(r.remarque) else r.remarque})

    for r in df.itertuples(index=False):
        ajoute(r, "vue_cour", r.valeur_md, "MD courants", "", "", "")
        if r.annee in dep.index:
            ajoute(r, "vue_dep", round(100 * r.valeur_md / dep[r.annee], 3), "% des dépenses",
                   round(dep[r.annee], 1),
                   "dépenses de l'État hors service de la dette, réalisation (ministère des Finances)",
                   SERIE_DEP)
        for q in pib[pib["annee"] == r.annee].itertuples(index=False):
            ajoute(r, "vue_pib", round(100 * r.valeur_md / q.pib_MD, 3), "% du PIB",
                   round(q.pib_MD, 1), _base_nom(q) + (" ; non tracée" if q.minfin else ""),
                   q.publication)
        if r.annee in ipc and r.annee <= BASE:
            ajoute(r, "vue_cst", round(r.valeur_md * ipc[BASE] / ipc[r.annee], 1),
                   f"MD de {BASE}", round(ipc[r.annee], 2),
                   "IPC INS base 1970 = 100, moyenne annuelle" + (
                       " ; prolongé par la variation de l'indice base 2015 (BCT)" if r.annee > 2023 else ""),
                   "ipc-longue-periode ; bct-ipc-base2015")
    out = pd.DataFrame(lignes)
    return out.fillna("")

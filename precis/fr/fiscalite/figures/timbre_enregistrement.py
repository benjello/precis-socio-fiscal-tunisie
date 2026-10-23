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

DEUX VUES. Millions de dinars courants ; millions de dinars de 2025 (indice commun du précis,
`scripts/dinars_constants.py`), sans 2026, dont l'indice n'est pas publié.
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
SERIES = (SERIE, *dinars_constants.SERIES_IPC)
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


def fig_rendement():
    """Deux vues : dinars courants (2001-2026) ; dinars de l'année de base (2001-2025)."""
    return [
        (_l("vue_cour"), _trace("valeur_md", _l("y_cour"), 2026)),
        (_l("vue_cst"), _trace("constants", _l("y_cst"), BASE)),
    ]


def table() -> pd.DataFrame:
    df = lire()
    df["cst"] = _constants(df)
    df["ligne"] = [_l(x) for x in df["ligne"]]
    df = df[["annee", "nature", "ligne", "nomenclature", "code_article", "libelle_source",
             "valeur_md", "cst", "trace", "source", "localisateur", "remarque"]]
    df.columns = [_l(k) for k in ("col_annee", "col_nature", "col_ligne", "col_nomen",
                                  "col_code", "col_lib", "col_md", "col_cst", "col_trace",
                                  "col_src", "col_page", "col_rem")]
    return df

"""Figure « contribution sociale de solidarité attribuée à la CNRPS, 2018-2023 ».

    from figures import cnrps_css_2018_2023 as cs
    cs.fig_vue("css")      # CSS attribuée à la CNRPS, MD, 2018-2023
    cs.fig_vue("besoin")   # besoin de financement du régime des pensions (CNRPS), MD, 2015-2020
    cs.vues()              # les deux, pour figtools.figure_tabs
    cs.table()             # une ligne par année

D'OÙ VIENNENT LES DONNÉES. La part de la CSS attribuée à la CNRPS vient de la série de contrôle
`cnrps-ratios-charges-produits` (tunisia-data) : valeurs retenues (`retenu`), indicateur
« contribution sociale de solidarité (CSS) attribuée à la CNRPS » — 200 (2018), 450 (2019),
460 (2020), 500 (2021), 195 (2022), 420 (2023) millions de dinars, d'après les annexes budgétaires
(rapport sur les entreprises publiques), la fiche de jumelage de l'Union européenne et les rapports
de performance du ministère des Affaires sociales. Le besoin de financement de la branche des
pensions (2015-2020) vient de la fiche de jumelage, série `cnrps-ue-jumelage-2021`.

CE QUE LA FIGURE NE DONNE PAS. Le produit TOTAL de la CSS et les parts reçues par la CNSS et par la
CNAM ne sont isolés dans aucune source lue : la figure ne porte que la part CNRPS. Les deux
grandeurs viennent de sources et d'années différentes ; elles ne sont pas raccordées.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_CSS = "cnrps-ratios-charges-produits"
SERIE_JUM = "cnrps-ue-jumelage-2021"
IND_CSS = "contribution sociale de solidarité (CSS) attribuée à la CNRPS"
IND_DEF = "déficit pension (« CNRPS (déficit - pension) »)"
VUES = ("css", "besoin")

BLEU, ORANGE = "#08519c", "#bc4c00"

_L = {
    "titre": {"fr": "Contribution sociale de solidarité attribuée à la CNRPS, 2018-2023",
              "ar": "المساهمة الاجتماعية التضامنية المسندة للصندوق الوطني للتقاعد والحيطة، "
                    "2018-2023"},
    "st_css": {"fr": "Part de la CSS reçue par la CNRPS, millions de dinars",
               "ar": "منابُ الصندوق من المساهمة الاجتماعية التضامنية، بملايين الدنانير"},
    "st_besoin": {"fr": "Besoin de financement du régime des pensions de la CNRPS, "
                        "millions de dinars",
                  "ar": "حاجة تمويل نظام جرايات الصندوق، بملايين الدنانير"},
    "vue_css": {"fr": "CSS reçue par la CNRPS", "ar": "المساهمة المسندة للصندوق"},
    "vue_besoin": {"fr": "Besoin du régime des pensions", "ar": "حاجة نظام الجرايات"},
    "css": {"fr": "CSS attribuée à la CNRPS", "ar": "المساهمة المسندة للصندوق"},
    "besoin": {"fr": "Besoin de financement (régime des pensions)",
               "ar": "حاجة التمويل (نظام الجرايات)"},
    "ib_css": {"fr": "{a} : {v} MD", "ar": "{a}: {v} م.د"},
    "ib_besoin": {"fr": "{a} : {v} MD", "ar": "{a}: {v} م.د"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_css": {"fr": "CSS attribuée à la CNRPS (MD)", "ar": "المساهمة المسندة للصندوق (م.د)"},
    "col_statut": {"fr": "Statut de la valeur", "ar": "حالة القيمة"},
    "col_edition": {"fr": "Source de la valeur retenue", "ar": "مصدر القيمة المعتمدة"},
    "col_besoin": {"fr": "Besoin de financement, pensions (MD)",
                   "ar": "حاجة التمويل، الجرايات (م.د)"},
    "statut_realise": {"fr": "réalisé", "ar": "منجز"},
    "statut_provisoire": {"fr": "provisoire", "ar": "وقتي"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _lignes(key: str) -> str:
    return "\n".join(figtools.fig_text(l) for l in _lab(key).split("\n"))


def _nombre(v: float, dec: int = 0) -> str:
    if round(v, dec) == 0:
        v = 0.0
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _css() -> dict[int, tuple[float, str, str]]:
    """{année: (MD, statut, édition)} pour la part CSS retenue de la CNRPS."""
    d = figtools.series(SERIE_CSS)
    d = d[(d["indicateur"] == IND_CSS) & (d["retenu"])]
    out = {}
    for r in d.itertuples():
        a = int(r.annee)
        assert a not in out, f"CSS : deux valeurs retenues pour {a}"
        out[a] = (float(r.valeur), str(r.statut), str(r.edition))
    return out


def _besoin() -> dict[int, float]:
    """{année: besoin de financement (MD, positif)} du régime des pensions, d'après le
    déficit pension de la fiche de jumelage."""
    d = figtools.series(SERIE_JUM)
    d = d[(d["indicateur"] == IND_DEF) & (d["retenu"])]
    return {int(r.annee): -float(r.valeur) for r in d.itertuples()}


def fig_vue(vue: str = "css"):
    """Une vue : "css" (part de la CSS reçue par la CNRPS, 2018-2023) ou "besoin" (besoin de
    financement de la branche des pensions, 2015-2020)."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(9, 5.2))

    if vue == "css":
        css = _css()
        for a in sorted(css):
            v, _, _ = css[a]
            b = ax.bar(a, v, color=BLEU, width=0.7)
            figtools.infobulle(b[0], _lab("ib_css").format(a=a, v=_nombre(v)))
            ax.annotate(_nombre(v), xy=(a, v), xytext=(0, 3), textcoords="offset points",
                        ha="center", va="bottom", fontsize=7, color="#24292f")
        ax.set_ylabel(ft(_lab("st_css")), fontsize=8)
        ax.set_xticks(sorted(css))
    elif vue == "besoin":
        bes = _besoin()
        xs = sorted(bes)
        ax.plot(xs, [bes[a] for a in xs], "-o", color=ORANGE, lw=1.6, ms=4.5)
        for a in xs:
            p, = ax.plot([a], [bes[a]], "o", color=ORANGE, ms=4.5)
            figtools.infobulle(p, _lab("ib_besoin").format(a=a, v=_nombre(bes[a])))
        ax.set_ylabel(ft(_lab("st_besoin")), fontsize=8)
        ax.set_xticks(xs)
    else:
        raise ValueError(vue)

    ax.tick_params(axis="x", labelsize=8)
    ax.tick_params(axis="y", labelsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle(_lignes("titre") + "\n" + _lignes(f"st_{vue}"), fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.98))
    return fig


def vues() -> list[tuple[str, object]]:
    return [(_lab(f"vue_{v}"), fig_vue(v)) for v in VUES]


def table():
    import pandas as pd
    css = _css()
    bes = _besoin()
    annees = sorted(set(css) | set(bes))
    statut = {"réalisé": _lab("statut_realise"), "provisoire": _lab("statut_provisoire")}
    lignes = []
    for a in annees:
        c = css.get(a)
        lignes.append({
            _lab("col_annee"): a,
            _lab("col_css"): round(c[0], 1) if c else None,
            _lab("col_statut"): statut.get(c[1], c[1]) if c else None,
            _lab("col_edition"): c[2] if c else None,
            _lab("col_besoin"): round(bes[a], 1) if a in bes else None,
        })
    return pd.DataFrame(lignes)

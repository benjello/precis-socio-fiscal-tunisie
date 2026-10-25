"""Écart de la recette de TVA à la prévision de la loi de finances initiale (figure du
chapitre « La taxe sur la valeur ajoutée »).

D'OÙ VIENNENT LES DONNÉES. De la série `tva-ecart-prevision-realise` (`precis/_seriescache/`),
écrite par `scripts/generate_tva_ecart.py` et contrôlée valeur par valeur par
`tests/test_tva_ecart.py` : prévision = somme des deux lignes de TVA du tableau A de la loi de
finances initiale ; réalisé = rubrique « TVA » des recettes fiscales de l'État du ministère des
Finances ; écart = réalisé − prévision.

TROIS MESURES, une vue chacune : l'écart en millions de dinars courants ; en % de la prévision
(aucun dénominateur extérieur) ; en % du PIB, UNE COURBE PAR BASE des comptes nationaux (1983,
1997, 2015), jamais raccordées, comme la figure du rendement de la taxe
(`figures/rendement_bases.py`) : une année publiée dans deux bases porte deux points, chacun
rapporté au PIB de sa base. La valeur du ministère que la source ne rattache à aucune base (2002 à
2004, 2025) n'est pas tracée ; l'onglet « Données » la donne.
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

HERE = Path(__file__).resolve().parent
RELEVES = HERE.parent / "tva"
SERIE_ECART = "tva-ecart-prevision-realise"
BLEU, ROUGE, GRIS = "#0969da", "#d1242f", "#57606a"
BASES = {"base1983": (1983, "o", "#1a7f37"), "base1997": (1997, "s", "#8250df"),
         "base2015": (2015, "^", "#0969da")}

_L = {
    "vue_md": {"fr": "Écart, millions de dinars", "ar": "الفارق، ملايين الدنانير"},
    "vue_pct": {"fr": "Écart, % de la prévision", "ar": "الفارق، % من التقديرات"},
    "vue_pib": {"fr": "Écart, % du PIB de chaque base", "ar": "الفارق، % من ناتج كل أساس"},
    "y_md": {"fr": "Recette constatée − prévision, en millions de dinars courants",
             "ar": "المقبوضات المسجلة − التقديرات، بملايين الدنانير الجارية"},
    "y_pct": {"fr": "Recette constatée − prévision, en % de la prévision",
              "ar": "المقبوضات المسجلة − التقديرات، % من التقديرات"},
    "y_pib": {"fr": "Recette constatée − prévision, en % du PIB de la base",
              "ar": "المقبوضات المسجلة − التقديرات، % من ناتج الأساس"},
    "xlabel": {"fr": "Exercice", "ar": "السنة المالية"},
    "base_leg": {"fr": "PIB de base {b}", "ar": "ناتج أساس {b}"},
    "rup": {"fr": "PIB : base 2015", "ar": "الناتج: أساس 2015"},
    "col_ecart_md": {"fr": "Écart (millions de dinars courants)",
                     "ar": "الفارق (ملايين الدنانير الجارية)"},
    "col_ecart_pct": {"fr": "Écart (% de la prévision)", "ar": "الفارق (% من التقديرات)"},
    "col_lfc": {"fr": "Prévision de la loi de finances complémentaire (MD)",
                "ar": "تقديرات قانون المالية التكميلي (م.د)"},
    "col_pib": {"fr": "PIB, base {b} (MD)", "ar": "ناتج أساس {b} (م.د)"},
    "col_pib_nr": {"fr": "PIB non rattaché à une base, ministère des Finances (MD)",
                   "ar": "ناتج غير مرتبط بأساس، وزارة المالية (م.د)"},
    "col_e_pib": {"fr": "Écart (% du PIB, base {b})", "ar": "الفارق (% من ناتج أساس {b})"},
    "col_e_pib_nr": {"fr": "Écart (% du PIB non rattaché ; non tracé)",
                     "ar": "الفارق (% من الناتج غير المرتبط ؛ غير مرسوم)"},
}


def _l(cle: str, **kw) -> str:
    t = _L[cle].get(figtools.lang(), _L[cle]["fr"])
    return t.format(**kw) if kw else t


def _sources() -> list[str]:
    import yaml
    s = list(yaml.safe_load((RELEVES / "recettes-tva-par-regime.csv.yml").read_text(
        encoding="utf-8"))["sources"])
    return s + ["minfin-recettes-fiscales"]


figtools.register_provenance(
    SERIE_ECART,
    titre=("TVA : écart de la recette constatée à la prévision de la loi de finances initiale, "
           "2001-2025, en millions de dinars, en % de la prévision et en % du PIB de chaque base"),
    sources=_sources(),
    unite="millions de dinars courants ; pour cent",
    perimetre=("prévision : somme des deux lignes de TVA du tableau A de la loi de finances "
               "initiale ; recette : rubrique « TVA » des recettes fiscales de l'État du "
               "ministère des Finances ; PIB : une colonne par base des comptes nationaux"),
    caveats=("La prévision est celle de la loi de finances initiale, jamais celle de la loi de "
             "finances complémentaire, que la colonne lfc_MD signale quand le classeur du "
             "ministère la porte (2013-2023). Les colonnes LF du classeur égalent le tableau A de "
             "2014 à 2026. Aucun PIB n'est converti d'une base à l'autre."),
)


def lire() -> pd.DataFrame:
    return figtools.series(SERIE_ECART).set_index("annee")


def _cadre(ax, ylabel: str) -> None:
    ax.axhline(0, color="#24292f", lw=0.8)
    ax.set_xlim(2000.4, 2026.6)
    ax.set_xlabel(figtools.fig_text(_l("xlabel")))
    ax.set_ylabel(figtools.fig_text(ylabel))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.spines[["top", "right"]].set_visible(False)


def _barres(colonne: str, ylabel: str, seuil: float, decimales: int):
    figtools.apply_lang_font()
    d = lire().dropna(subset=[colonne])
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.bar(d.index, d[colonne], width=0.7, color=[BLEU if v >= 0 else ROUGE for v in d[colonne]])
    for a, v in d[colonne].items():
        if abs(v) >= seuil:
            t = f"{v:+.{decimales}f}".replace(".", ",")
            ax.annotate(t, (a, v), textcoords="offset points", xytext=(0, 4 if v >= 0 else -10),
                        ha="center", fontsize=8)
    _cadre(ax, ylabel)
    fig.tight_layout()
    return fig


def vue_md():
    return _barres("ecart_MD", _l("y_md"), 500, 0)


def vue_pct():
    return _barres("ecart_pct_prevision", _l("y_pct"), 10, 1)


def vue_pib():
    figtools.apply_lang_font()
    d = lire()
    fig, ax = plt.subplots(figsize=(9, 5.6))
    for cle, (base, marque, couleur) in BASES.items():
        g = d[f"ecart_pct_pib_{cle}"].dropna()
        ax.plot(g.index, g, color=couleur, lw=1.6, marker=marque, ms=4.5,
                label=figtools.fig_text(_l("base_leg", b=base)))
        for a, v in g.items():
            p, = ax.plot([a], [v], marque, ms=4.5, color=couleur, zorder=3)
            figtools.infobulle(p, f"{a} · base {base} : {v:+.2f} % du PIB".replace(".", ","))
    ax.axvline(2009.5, color=GRIS, ls=(0, (2, 2)), lw=1)
    ax.annotate(figtools.fig_text(_l("rup")), xy=(2009.5, 0), xycoords=("data", "axes fraction"),
                xytext=(4, 4), textcoords="offset points", ha="left", va="bottom", fontsize=7,
                color=GRIS)
    _cadre(ax, _l("y_pib"))
    ax.legend(loc="lower left", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def vues():
    return [(_l("vue_md"), vue_md()), (_l("vue_pct"), vue_pct()), (_l("vue_pib"), vue_pib())]


def colonnes_table() -> pd.DataFrame:
    """Colonnes de l'écart pour l'onglet « Données » (une ligne par exercice 2001-2026)."""
    d = lire()
    sortie = pd.DataFrame(index=d.index)
    sortie[_l("col_ecart_md")] = d["ecart_MD"].round(1)
    sortie[_l("col_ecart_pct")] = d["ecart_pct_prevision"].round(2)
    sortie[_l("col_lfc")] = d["lfc_MD"]
    for cle, (base, _m, _c) in BASES.items():
        sortie[_l("col_pib", b=base)] = d[f"pib_{cle}_MD"].round(1)
        sortie[_l("col_e_pib", b=base)] = d[f"ecart_pct_pib_{cle}"].round(3)
    sortie[_l("col_pib_nr")] = d["pib_non_rattache_MD"].round(1)
    sortie[_l("col_e_pib_nr")] = d["ecart_pct_pib_non_rattache"].round(3)
    return sortie

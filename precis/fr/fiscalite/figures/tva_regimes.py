"""Figure « TVA : prévisions des lois de finances par régime » du livre *Fiscalité*.

D'OÙ VIENNENT LES DONNÉES. D'un relevé versionné dans le livre, à côté du chapitre
(`tva/recettes-tva-par-regime.csv`, avec son manifeste) : les deux lignes de TVA du tableau A
des lois de finances initiales, régime d'importation (« régime douanier » depuis 2020) et
régime intérieur, de 2001 à 2026.

BUDGÉTAIRE SEUL, AUCUN PIB. Les prévisions d'une loi de finances ne sont pas des recettes
encaissées, et aucune réalisation par régime n'a été identifiée : la figure le dit dans son
titre, et la part du régime d'importation se calcule sur la somme des deux lignes de la même
loi, sans dénominateur extérieur.

DEUX VUES. Millions de dinars courants, deux séries empilées ; part du régime d'importation
dans la TVA prévue, en pour cent.
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
NOM = "recettes-tva-par-regime"
SERIE = "tva-recettes-par-regime"
SERIES = (SERIE,)

COULEURS = {"importation": "#0969da", "interieur": "#1a7f37"}
ROUGE = "#d1242f"

_L = {
    "importation": {"fr": "TVA du régime d'importation (régime douanier depuis 2020)",
                    "ar": "الأداء على القيمة المضافة : نظام ديواني"},
    "interieur": {"fr": "TVA du régime intérieur", "ar": "الأداء على القيمة المضافة : نظام داخلي"},
    "part": {"fr": "part du régime d'importation (éch. droite)",
             "ar": "حصة نظام التوريد (يمين)"},
    "y_md": {"fr": "Prévision, en millions de dinars courants",
             "ar": "التقديرات، بملايين الدنانير الجارية"},
    "y_part": {"fr": "Part du régime d'importation, en % de la TVA prévue",
               "ar": "حصة نظام التوريد، % من الأداء المقدّر"},
    "xlabel": {"fr": "Exercice", "ar": "السنة المالية"},
    "vue_md": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "vue_part": {"fr": "Part du régime d'importation", "ar": "حصة نظام التوريد"},
    "col_annee": {"fr": "Exercice", "ar": "السنة المالية"},
    "col_regime": {"fr": "Régime", "ar": "النظام"},
    "col_code": {"fr": "Article du tableau A", "ar": "فصل الجدول أ"},
    "col_lib": {"fr": "Libellé de la source", "ar": "تسمية المصدر"},
    "col_md": {"fr": "Prévision (millions de dinars courants)",
               "ar": "التقديرات (ملايين الدنانير الجارية)"},
    "col_part": {"fr": "Part du régime d'importation (%)", "ar": "حصة نظام التوريد (%)"},
    "col_src": {"fr": "Source", "ar": "المصدر"},
    "col_page": {"fr": "Emplacement", "ar": "الموضع"},
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
    titre="TVA : prévisions des lois de finances par régime, importation et intérieur, 2001-2026",
    sources=_sources(),
    unite="millions de dinars courants",
    perimetre=("les deux lignes de TVA du tableau A des lois de finances initiales (22-01 et "
               "22-02 jusqu'en 2019 ; 14-01 et 14-02 depuis 2020)"),
    caveats=("Prévisions, non recettes encaissées : aucune réalisation par régime n'a été "
             "identifiée. En 2020 et en 2022, le tableau imprime chaque valeur un rang au-dessus "
             "de son libellé ; l'attribution retenue est la seule où les deux valeurs somment au "
             "total imprimé."),
)


def lire() -> pd.DataFrame:
    return pd.read_csv(RELEVES / f"{NOM}.csv")


def _large() -> pd.DataFrame:
    d = lire().pivot(index="annee", columns="regime", values="valeur_md")
    d["total"] = d["importation"] + d["interieur"]
    d["part"] = 100 * d["importation"] / d["total"]
    return d


def _vue_md():
    figtools.apply_lang_font()
    d = _large()
    fig, ax = plt.subplots(figsize=(9, 5.2))
    bas = pd.Series(0.0, index=d.index)
    for reg in ("importation", "interieur"):
        ax.bar(d.index, d[reg], bottom=bas, color=COULEURS[reg], width=0.78,
               label=figtools.fig_text(_l(reg)))
        bas = bas + d[reg]
    ax.set_xlim(2000.4, 2026.6)
    ax.set_xlabel(figtools.fig_text(_l("xlabel")))
    ax.set_ylabel(figtools.fig_text(_l("y_md")))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=1, fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def _vue_part():
    figtools.apply_lang_font()
    d = _large()
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.plot(d.index, d["part"], color=ROUGE, lw=1.8, marker="o", ms=3.5)
    ax.axhline(50, color="#8b949e", lw=0.8, ls=(0, (3, 3)))
    ax.set_xlim(2000.4, 2026.6)
    ax.set_ylim(35, 65)
    ax.set_xlabel(figtools.fig_text(_l("xlabel")))
    ax.set_ylabel(figtools.fig_text(_l("y_part")))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig


def fig_regimes():
    return [(_l("vue_md"), _vue_md()), (_l("vue_part"), _vue_part())]


def table() -> pd.DataFrame:
    df = lire()
    part = _large()["part"]
    df["part"] = [round(part[a], 1) for a in df["annee"]]
    df["regime"] = [_l(r) for r in df["regime"]]
    df = df[["annee", "regime", "code_article", "libelle_source", "valeur_md", "part",
             "source", "localisateur", "remarque"]]
    df.columns = [_l(k) for k in ("col_annee", "col_regime", "col_code", "col_lib", "col_md",
                                  "col_part", "col_src", "col_page", "col_rem")]
    return df.fillna("")


# --- Les prévisions face aux recettes constatées ------------------------------------------------
#
# La recette est la rubrique « TVA » des recettes fiscales de l'État du ministère des Finances
# (série `recettes-fiscales-composition`, la même que la figure du rendement de la taxe) ; la
# prévision est la somme des deux lignes du tableau A de la loi de finances initiale. Millions de
# dinars courants des deux côtés : aucun PIB. 2026 n'a que sa prévision.

SERIE_RECETTES = "recettes-fiscales-composition"
SERIES_PREVU_REALISE = (SERIE, SERIE_RECETTES)
BLEU, GRIS_CLAIR = "#0969da", "#8c959f"

_L.update({
    "prevu": {"fr": "Prévision de la loi de finances initiale (tableau A)",
              "ar": "تقديرات قانون المالية الأصلي (الجدول أ)"},
    "realise": {"fr": "Recette constatée (rubrique « TVA » du ministère des Finances)",
                "ar": "المقبوضات المسجلة (باب الأداء على القيمة المضافة، وزارة المالية)"},
    "y_courants": {"fr": "Millions de dinars courants", "ar": "ملايين الدنانير الجارية"},
    "y_ecart": {"fr": "Recette constatée par rapport à la prévision, en %",
                "ar": "المقبوضات المسجلة مقارنة بالتقديرات، %"},
    "vue_prevu": {"fr": "Prévision et recette, millions de dinars courants",
                  "ar": "التقديرات والمقبوضات، ملايين الدنانير الجارية"},
    "vue_ecart": {"fr": "Écart de la recette à la prévision", "ar": "فارق المقبوضات عن التقديرات"},
    "col_prevu": {"fr": "Prévision (millions de dinars courants)",
                  "ar": "التقديرات (ملايين الدنانير الجارية)"},
    "col_realise": {"fr": "Recette constatée (millions de dinars courants)",
                    "ar": "المقبوضات المسجلة (ملايين الدنانير الجارية)"},
    "col_ecart_md": {"fr": "Écart (millions de dinars courants)",
                     "ar": "الفارق (ملايين الدنانير الجارية)"},
    "col_ecart": {"fr": "Écart (%)", "ar": "الفارق (%)"},
})


def _prevu_realise() -> pd.DataFrame:
    prevu = _large()["total"].rename("prevu")
    realise = (figtools.series(SERIE_RECETTES).set_index("annee")["tva_MDT"].rename("realise"))
    d = pd.concat([prevu, realise], axis=1).loc[prevu.index]
    d["ecart_md"] = d["realise"] - d["prevu"]
    d["ecart"] = 100 * d["ecart_md"] / d["prevu"]
    return d


def _vue_prevu_realise():
    figtools.apply_lang_font()
    d = _prevu_realise()
    fig, ax = plt.subplots(figsize=(9, 5.2))
    l = 0.38
    ax.bar(d.index - l / 2, d["prevu"], width=l, color=GRIS_CLAIR,
           label=figtools.fig_text(_l("prevu")))
    ax.bar(d.index + l / 2, d["realise"], width=l, color=BLEU,
           label=figtools.fig_text(_l("realise")))
    ax.set_xlim(2000.4, 2026.6)
    ax.set_xlabel(figtools.fig_text(_l("xlabel")))
    ax.set_ylabel(figtools.fig_text(_l("y_courants")))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=1, fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def _vue_ecart():
    figtools.apply_lang_font()
    d = _prevu_realise().dropna(subset=["ecart"])
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.bar(d.index, d["ecart"], width=0.7,
           color=[BLEU if v >= 0 else ROUGE for v in d["ecart"]])
    for a, v in d["ecart"].items():
        if abs(v) >= 10:
            ax.annotate(f"{v:+.1f}".replace(".", ","), (a, v), textcoords="offset points",
                        xytext=(0, 4 if v >= 0 else -10), ha="center", fontsize=8)
    ax.axhline(0, color="#24292f", lw=0.8)
    ax.set_xlim(2000.4, 2026.6)
    ax.set_xlabel(figtools.fig_text(_l("xlabel")))
    ax.set_ylabel(figtools.fig_text(_l("y_ecart")))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig


def fig_prevu_realise():
    return [(_l("vue_prevu"), _vue_prevu_realise()), (_l("vue_ecart"), _vue_ecart())]


def table_prevu_realise() -> pd.DataFrame:
    d = _prevu_realise().round({"prevu": 1, "realise": 1, "ecart_md": 1, "ecart": 1})
    d = d.reset_index()
    d.columns = [_l(k) for k in ("col_annee", "col_prevu", "col_realise", "col_ecart_md",
                                 "col_ecart")]
    return d.fillna("")

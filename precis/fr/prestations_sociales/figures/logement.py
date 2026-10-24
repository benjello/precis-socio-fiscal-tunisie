"""Figure « prélèvements des lois de finances sur les disponibilités du fonds de promotion
du logement pour les salariés, 1987-2013 ».

    from figures import logement as fig_log
    fig_log.fig_prelevements()
    fig_log.table_prelevements()

D'OÙ VIENNENT LES DONNÉES. Sept lois de finances, relevées article par article dans le
registre du chapitre (série `log-prelevements-fonds` du cache du précis, une ligne par année
et par bénéficiaire). Les montants sont en millions de dinars courants, tels que les textes
les fixent ; rien n'est déflaté. Une année sans barre est une année où aucun prélèvement n'a
été identifié, non une année où l'absence de prélèvement serait établie.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402
import dinars_constants  # noqa: E402
from dinars_constants import ANNEE_BASE, SERIES_IPC  # noqa: E402, F401

SERIE = "log-prelevements-fonds"

BLEU, ORANGE, VERT = "#08519c", "#bc4c00", "#1a7f37"
_COULEURS = {
    "programme national de résorption des logements rudimentaires": BLEU,
    "Fonds national d'amélioration de l'habitat": ORANGE,
    "Compte national de solidarité sociale": VERT,
}

figtools.register_provenance(
    SERIE,
    titre="Prélèvements des lois de finances sur les disponibilités du fonds de promotion du "
          "logement pour les salariés, 1987-2013",
    titre_ar="اقتطاعات قوانين المالية من موارد صندوق النهوض بالمساكن للأجراء، 1987-2013",
    sources=["loi86-106-lf1987", "loi-87-83-lf-1988", "loi88-145-lf1989", "loi-89-115-lf-1990",
             "dl-2011-56-lfc-2011", "lfc-2012", "lf-2013"],
    unite="millions de dinars courants",
    unite_ar="بملايين الدنانير الجارية",
    perimetre="sept lois de finances, de 1987 à 2013, une ligne par année et par bénéficiaire",
    perimetre_ar="سبعة قوانين مالية من 1987 إلى 2013، سطر لكل سنة ولكل مستفيد",
    caveats=("Montants fixés par les textes, non les sommes effectivement prélevées. Une année "
             "sans barre est une année où aucun prélèvement n'a été identifié."),
    caveats_ar="المبالغ هي المحددة في النصوص وليست المبالغ المقتطعة فعليا.",
)

_L = {
    "titre": {"fr": "Prélèvements sur les disponibilités du fonds, 1987-2013",
              "ar": "الاقتطاعات من موارد الصندوق، 1987-2013"},
    "y": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "y_reel": {"fr": f"Millions de dinars de {ANNEE_BASE}",
               "ar": f"بملايين دنانير سنة {ANNEE_BASE}"},
    "col_reel": {"fr": f"Montant (MD de {ANNEE_BASE})", "ar": f"المبلغ (م.د سنة {ANNEE_BASE})"},
    "x": {"fr": "Année", "ar": "السنة"},
    "programme national de résorption des logements rudimentaires": {
        "fr": "Programme national de résorption des logements rudimentaires",
        "ar": "البرنامج الوطني للقضاء على المساكن البدائية"},
    "Fonds national d'amélioration de l'habitat": {
        "fr": "Fonds national d'amélioration de l'habitat",
        "ar": "الصندوق الوطني لتحسين السكن"},
    "Compte national de solidarité sociale": {
        "fr": "Compte national de solidarité sociale",
        "ar": "الحساب الوطني للتضامن الاجتماعي"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_beneficiaire": {"fr": "Bénéficiaire", "ar": "المستفيد"},
    "col_montant": {"fr": "Montant (MD courants)", "ar": "المبلغ (م.د جارية)"},
    "col_texte": {"fr": "Texte", "ar": "النص"},
    "col_page": {"fr": "Page du Journal officiel", "ar": "صفحة الرائد الرسمي"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _serie():
    return figtools.series(SERIE)


def _avec_reel(df):
    df = df.copy()
    ind = dinars_constants.ipc()
    df["part_reel_MD"] = [dinars_constants.en_dinars_constants(v, int(a), ind)
                          for v, a in zip(df["part_MD"], df["annee"])]
    return df


def fig_prelevements(mesure: str = "md"):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    df = _avec_reel(_serie())
    colonne = "part_MD" if mesure == "md" else "part_reel_MD"
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    bas: dict[int, float] = {}
    for benef, couleur in _COULEURS.items():
        for _, l in df[df["beneficiaire"] == benef].iterrows():
            a = int(l["annee"])
            ax.bar(a, l[colonne], bottom=bas.get(a, 0.0), width=0.72, color=couleur,
                   edgecolor="white", lw=0.4)
            bas[a] = bas.get(a, 0.0) + float(l[colonne])
    for a, total in bas.items():
        ax.annotate(f"{total:.0f}".replace(".", ","), (a, total), textcoords="offset points",
                    xytext=(0, 4), ha="center", fontsize=8, color="#24292f")
    ax.set_xlim(1986, 2014)
    ax.set_ylim(0, max(bas.values()) * 1.15)
    ax.set_xticks(range(1987, 2014, 2))
    ax.tick_params(axis="x", labelsize=8)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y" if mesure == "md" else "y_reel")))
    ax.set_title(ft(_lab("titre")))
    ax.grid(True, axis="y", alpha=0.3)
    poignees = [Patch(color=c, label=ft(_lab(b))) for b, c in _COULEURS.items()
                if (df["beneficiaire"] == b).any()]
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=1,
              fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def vues_prelevements():
    return [(_lab("y"), fig_prelevements("md")), (_lab("y_reel"), fig_prelevements("reel"))]


def table_prelevements():
    df = _avec_reel(_serie())
    df["part_reel_MD"] = df["part_reel_MD"].round(1)
    cols = ["annee", "beneficiaire", "part_MD", "part_reel_MD", "texte", "page"]
    noms = [_lab(k) for k in ("col_annee", "col_beneficiaire", "col_montant", "col_reel",
                              "col_texte", "col_page")]
    df = df[cols]
    df.columns = noms
    return df

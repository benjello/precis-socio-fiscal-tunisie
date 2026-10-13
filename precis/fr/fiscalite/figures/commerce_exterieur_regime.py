"""Figure « part du régime off shore dans le commerce extérieur de biens » du livre *Fiscalité*.

STATISTIQUE PUBLIQUE, RIEN D'AUTRE. La série vient de l'*Annuaire statistique de la
Tunisie* de l'INS (tableau 14.2), qui ventile les exportations et les importations de biens
entre un « régime général » et un « régime off shore ». Elle ne se mêle ni aux évaluations
du ministère des Finances ni aux études extérieures du chapitre, et la figure n'affirme
aucun lien de cause entre le régime fiscal de l'exportation et ces parts.

LA PART EST CALCULÉE, NON PUBLIÉE : 100 × régime off shore / ensemble des produits, les deux
valeurs étant celles de la même édition de l'annuaire. La série retient, pour chaque année,
la dernière édition qui l'imprime.

DEUX SEGMENTS, ET NON UN TRAIT CONTINU. Les années 2004 et 2005 ont été révisées par les
éditions suivantes sur le seul régime off shore (+ 2 à + 4 %), et les années 2003 et
antérieures ne sont imprimées dans aucune édition postérieure à cette révision : on ne sait
pas si elles auraient été révisées de même. Chaque courbe est donc tracée en deux segments,
1998-2003 et 2004-2023, séparés par une marque de rupture ; aucun raccord n'est calculé.

LES EXPORTATIONS DE 2007 viennent de l'édition 2005-2009 : l'édition 2003-2007 imprime un
total (16 409,6) que ses deux régimes démentent (19 409,6). La série de l'entrepôt écarte
déjà cette attestation ; rien n'est corrigé ici.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402

HERE = Path(__file__).resolve().parent
FIGDATA = HERE.parent / "figdata"
SERIE = "ins-commerce-exterieur-par-regime"

# Première année imprimée dans une édition postérieure à la révision du régime off shore.
ANNEE_RUPTURE = 2004

_L = {
    "lg_exp": {"fr": "Part du régime off shore dans les exportations de biens",
               "ar": "حصة النظام غير المقيم من صادرات السلع"},
    "lg_imp": {"fr": "Part du régime off shore dans les importations de biens",
               "ar": "حصة النظام غير المقيم من واردات السلع"},
    "y": {"fr": "En % de l'ensemble des produits", "ar": "% من مجموع المواد"},
    "x": {"fr": "Année", "ar": "السنة"},
    "titre": {"fr": "Le régime off shore dans le commerce extérieur de biens, 1998-2023",
              "ar": "النظام غير المقيم في التجارة الخارجية للسلع، 1998-2023"},
    "rupture": {"fr": "années antérieures absentes\ndes éditions révisées",
                "ar": "السنوات السابقة غير واردة\nفي الطبعات المراجَعة"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_exp": {"fr": "Exportations, ensemble (MD)", "ar": "الصادرات، المجموع (م.د)"},
    "col_exp_os": {"fr": "Exportations, régime off shore (MD)",
                   "ar": "الصادرات، النظام غير المقيم (م.د)"},
    "col_exp_part": {"fr": "Part off shore des exportations (%)",
                     "ar": "حصة النظام غير المقيم من الصادرات (%)"},
    "col_exp_ed": {"fr": "Édition de l'annuaire (exportations)",
                   "ar": "طبعة النشرية (الصادرات)"},
    "col_imp": {"fr": "Importations, ensemble (MD)", "ar": "الواردات، المجموع (م.د)"},
    "col_imp_os": {"fr": "Importations, régime off shore (MD)",
                   "ar": "الواردات، النظام غير المقيم (م.د)"},
    "col_imp_part": {"fr": "Part off shore des importations (%)",
                     "ar": "حصة النظام غير المقيم من الواردات (%)"},
    "col_imp_ed": {"fr": "Édition de l'annuaire (importations)",
                   "ar": "طبعة النشرية (الواردات)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _flux(nom: str):
    d = figtools.series(SERIE)
    return d[d["flux"] == nom].sort_values("annee")


def table():
    """Une ligne par année : les deux flux côte à côte, avec l'édition retenue."""
    cols = ["annee", "ensemble_md", "regime_off_shore_md", "part_off_shore_pct", "edition"]
    e = _flux("exportations")[cols]
    i = _flux("importations")[cols]
    w = e.merge(i, on="annee", suffixes=("_exp", "_imp"))
    return w.rename(columns={
        "annee": _lab("col_annee"),
        "ensemble_md_exp": _lab("col_exp"),
        "regime_off_shore_md_exp": _lab("col_exp_os"),
        "part_off_shore_pct_exp": _lab("col_exp_part"),
        "edition_exp": _lab("col_exp_ed"),
        "ensemble_md_imp": _lab("col_imp"),
        "regime_off_shore_md_imp": _lab("col_imp_os"),
        "part_off_shore_pct_imp": _lab("col_imp_part"),
        "edition_imp": _lab("col_imp_ed"),
    })


def prepare(generated: str | None = None):
    figtools.write_figdata(
        table(), FIGDATA / "fig_commerce_exterieur_regime.csv", SERIE,
        note=("part du régime off shore dans les exportations et les importations de biens, "
              "1998-2023 ; part calculée (régime off shore / ensemble des produits), non "
              "publiée par l'annuaire ; rupture entre 2003 et 2004, les années antérieures "
              "n'étant imprimées dans aucune édition postérieure à la révision du régime "
              "off shore"),
        generated=generated)


def fig_parts():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    poignees = []
    for flux, cle, couleur, marque in (("exportations", "lg_exp", "#0969da", "o"),
                                       ("importations", "lg_imp", "#bc4c00", "s")):
        d = _flux(flux)
        avant = d[d["annee"] < ANNEE_RUPTURE]
        apres = d[d["annee"] >= ANNEE_RUPTURE]
        # Deux segments du même trait : aucun point ne relie 2003 à 2004.
        ax.plot(avant["annee"], avant["part_off_shore_pct"], marque + "-", color=couleur,
                lw=1.9, ms=4)
        ligne, = ax.plot(apres["annee"], apres["part_off_shore_pct"], marque + "-",
                         color=couleur, lw=1.9, ms=4, label=ft(_lab(cle)))
        poignees.append(ligne)
    ax.set_ylim(0, 100)
    figtools.marque_rupture(ax, ANNEE_RUPTURE, ft(_lab("rupture")))
    ax.set_ylabel(ft(_lab("y")))
    ax.set_xlabel(ft(_lab("x")))
    ax.set_title(ft(_lab("titre")))
    ax.grid(True, alpha=0.3)
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=1,
              fontsize=8.5, frameon=False)
    fig.tight_layout()
    return fig

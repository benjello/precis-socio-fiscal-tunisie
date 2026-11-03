"""Figures du chapitre « Les employeurs » du volume « Le marché du travail ».

    from figures import employeurs as emp
    emp.vues_entreprises(), emp.table_entreprises()  # entreprises privées, 2001-2024
    emp.vues_salaries(), emp.table_salaries()        # salariés déclarés, 2000-2024

D'OÙ VIENNENT LES DONNÉES. Le module ne lit que `figtools.series()` : quatre séries de
l'Institut national de la statistique tirées des éditions 2016 à 2025 de « Statistiques
issues du répertoire national des entreprises », snapshotées depuis l'entrepôt `tunisia-data`
(fiche `sources/ins-rne-statistiques.md`) :

  - `ins-repertoire-entreprises-tranche`, `ins-repertoire-entreprises-forme` : entreprises
    privées selon la tranche de salariés et la forme juridique, 2001-2024 ;
  - `ins-repertoire-emploi-tranche`, `ins-repertoire-emploi-forme` : salariés déclarés à la
    CNSS selon la tranche de salariés de leur entreprise et la forme juridique, 2000-2024.

CONVENTIONS.
  - Les neuf tranches du répertoire sont regroupées en quatre ou cinq classes : aucun salarié
    (entreprises seulement), 1 à 9, 10 à 49, 50 à 199, 200 et plus.
  - Les tableaux de l'INS sont d'abord des statuts administratifs : les entreprises sans salarié
    comprennent des unités qui ont cessé leur activité (voir le texte du chapitre).
  - Le total des salariés est la somme des classes ; celui des formes juridiques s'en écarte
    de quelques unités (cellules arrondies à la source).
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_ENT_TRANCHE = "ins-repertoire-entreprises-tranche"
SERIE_ENT_FORME = "ins-repertoire-entreprises-forme"
SERIE_EMP_TRANCHE = "ins-repertoire-emploi-tranche"
SERIE_EMP_FORME = "ins-repertoire-emploi-forme"

# Les éditions dont viennent les valeurs tracées (une année vient de l'édition qui l'imprime).
EDITIONS = ["ins-repertoire-entreprises-2016", "ins-repertoire-entreprises-2017",
            "ins-repertoire-entreprises-2018", "ins-repertoire-entreprises-2021",
            "ins-repertoire-entreprises-2025"]

for _s in (SERIE_ENT_TRANCHE, SERIE_ENT_FORME, SERIE_EMP_TRANCHE, SERIE_EMP_FORME):
    figtools.register_provenance(_s, **{**figtools.meta(_s), "sources": EDITIONS})

CLASSES = {  # classe -> tranches du répertoire
    "0": ["0"],
    "1-9": ["1 à 2", "3 à 5", "6 à 9"],
    "10-49": ["10 à 19", "20 à 49"],
    "50-199": ["50 à 99", "100 à 199"],
    "200+": ["200 et plus"],
}
FORMES = ["personne physique", "SARL", "SUARL", "société anonyme", "autres"]

BLEU, ORANGE, VERT, GRIS, ROUGE = "#08519c", "#bc4c00", "#1a7f37", "#6e7781", "#a40e26"
COULEURS_CLASSES = {"0": GRIS, "1-9": "#6baed6", "10-49": BLEU, "50-199": VERT, "200+": ORANGE}
COULEURS_FORMES = {"personne physique": GRIS, "SARL": BLEU, "SUARL": "#6baed6",
                   "société anonyme": ORANGE, "autres": "#d4a72c"}

_L = {
    "x_annee": {"fr": "Année", "ar": "السنة"},
    "y_ent": {"fr": "Entreprises (échelle logarithmique)", "ar": "عدد المؤسسات (سلّم لوغاريتمي)"},
    "y_ent_lin": {"fr": "Entreprises, en milliers", "ar": "عدد المؤسسات، بالآلاف"},
    "y_sal": {"fr": "Salariés déclarés, en milliers", "ar": "الأجراء المصرّح بهم، بالآلاف"},
    "vue_ent_taille": {"fr": "Selon le nombre de salariés", "ar": "حسب عدد الأجراء"},
    "vue_ent_forme": {"fr": "Selon la forme juridique", "ar": "حسب الشكل القانوني"},
    "vue_sal_taille": {"fr": "Selon la taille de l'entreprise", "ar": "حسب حجم المؤسسة"},
    "vue_sal_forme": {"fr": "Selon la forme juridique", "ar": "حسب الشكل القانوني"},
    "cl_0": {"fr": "Aucun salarié", "ar": "دون أجراء"},
    "cl_1-9": {"fr": "1 à 9 salariés", "ar": "من 1 إلى 9 أجراء"},
    "cl_10-49": {"fr": "10 à 49 salariés", "ar": "من 10 إلى 49 أجيرًا"},
    "cl_50-199": {"fr": "50 à 199 salariés", "ar": "من 50 إلى 199 أجيرًا"},
    "cl_200+": {"fr": "200 salariés et plus", "ar": "200 أجير فأكثر"},
    "fm_personne physique": {"fr": "Personne physique", "ar": "شخص طبيعي"},
    "fm_SARL": {"fr": "SARL", "ar": "شركة ذات مسؤولية محدودة"},
    "fm_SUARL": {"fr": "SUARL", "ar": "شركة ذات الشخص الوحيد وذات المسؤولية المحدودة"},
    "fm_société anonyme": {"fr": "Société anonyme", "ar": "شركة خفية الاسم"},
    "fm_autres": {"fr": "Autres formes", "ar": "أشكال أخرى"},
    "r_2003": {"fr": "2003", "ar": "2003"},
    "r_2018": {"fr": "2018", "ar": "2018"},
    "r_2020": {"fr": "2020", "ar": "2020"},
    "c_annee": {"fr": "année", "ar": "السنة"},
    "c_total": {"fr": "Total", "ar": "المجموع"},
    "c_ent": {"fr": "Entreprises", "ar": "المؤسسات"},
    "c_sal": {"fr": "Salariés", "ar": "الأجراء"},
    "c_edition": {"fr": "édition de l'INS", "ar": "طبعة المعهد"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _pivot(serie_id: str):
    d = figtools.series(serie_id)
    return d.pivot(index="annee", columns="modalite", values="valeur").sort_index()


def _editions(serie_id: str):
    d = figtools.series(serie_id)
    return d.groupby("annee")["edition"].first()


def _classes(serie_id: str, avec_zero: bool):
    p = _pivot(serie_id)
    out = {}
    for cl, tr in CLASSES.items():
        if cl == "0" and not avec_zero:
            continue
        out[cl] = p[tr].sum(axis=1)
    return out, p["total"]


def _formes(serie_id: str):
    p = _pivot(serie_id)
    return {f: p[f] for f in FORMES}, p["total"]


# ---------------------------------------------------------------- entreprises

def _fig_entreprises_taille():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    cl, _ = _classes(SERIE_ENT_TRANCHE, True)
    fig, ax = plt.subplots(figsize=(10, 5.6))
    for c, s in cl.items():
        ax.plot(s.index, s.values, color=COULEURS_CLASSES[c], lw=1.9, marker="o", ms=2.5,
                label=ft(_lab(f"cl_{c}")))
    ax.set_yscale("log")
    ax.set_yticks([500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 300000, 700000])
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", " ")))
    ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    figtools.marque_rupture(ax, 2003, ft(_lab("r_2003")))
    figtools.marque_rupture(ax, 2018, ft(_lab("r_2018")))
    ax.set_xticks(range(2001, 2025, 3))
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_ent")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False, ncol=5)
    fig.tight_layout()
    return fig


def _fig_empile(groupes: dict, couleurs: dict, prefixe: str, ylab: str, ruptures=()):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(10, 5.6))
    annees = list(next(iter(groupes.values())).index)
    bas = [0.0] * len(annees)
    for g, s in groupes.items():
        v = [x / 1000 for x in s.values]
        ax.bar(annees, v, bottom=bas, color=couleurs[g], width=0.8, label=ft(_lab(f"{prefixe}{g}")))
        bas = [b + x for b, x in zip(bas, v)]
    for a, cle in ruptures:
        figtools.marque_rupture(ax, a, ft(_lab(cle)))
    ax.set_xticks(range(annees[0] if annees[0] % 2 == 0 else annees[0] + 1, annees[-1] + 1, 3))
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab(ylab)))
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False, ncol=5)
    fig.tight_layout()
    return fig


def vues_entreprises():
    formes, _ = _formes(SERIE_ENT_FORME)
    return [(_lab("vue_ent_taille"), _fig_entreprises_taille()),
            (_lab("vue_ent_forme"), _fig_empile(formes, COULEURS_FORMES, "fm_", "y_ent_lin"))]


def table_entreprises():
    import pandas as pd
    cl, tot = _classes(SERIE_ENT_TRANCHE, True)
    fm, tot_f = _formes(SERIE_ENT_FORME)
    cols = {_lab("c_annee"): list(tot.index)}
    for c, s in cl.items():
        cols[_lab(f"cl_{c}")] = list(s.values)
    cols[_lab("c_total")] = list(tot.values)
    for f, s in fm.items():
        cols[_lab(f"fm_{f}")] = list(s.values)
    cols[_lab("c_edition")] = list(_editions(SERIE_ENT_TRANCHE).reindex(tot.index).values)
    return pd.DataFrame(cols)


# ---------------------------------------------------------------- salariés

def vues_salaries():
    cl, _ = _classes(SERIE_EMP_TRANCHE, False)
    formes, _ = _formes(SERIE_EMP_FORME)
    return [(_lab("vue_sal_taille"),
             _fig_empile(cl, COULEURS_CLASSES, "cl_", "y_sal", ruptures=((2020, "r_2020"),))),
            (_lab("vue_sal_forme"), _fig_empile(formes, COULEURS_FORMES, "fm_", "y_sal"))]


def table_salaries():
    import pandas as pd
    cl, tot = _classes(SERIE_EMP_TRANCHE, False)
    fm, tot_f = _formes(SERIE_EMP_FORME)
    cols = {_lab("c_annee"): list(tot.index)}
    for c, s in cl.items():
        cols[_lab(f"cl_{c}")] = list(s.values)
    cols[_lab("c_total")] = list(tot.values)
    for f, s in fm.items():
        cols[_lab(f"fm_{f}")] = list(s.values)
    cols[_lab("c_edition")] = list(_editions(SERIE_EMP_TRANCHE).reindex(tot.index).values)
    return pd.DataFrame(cols)

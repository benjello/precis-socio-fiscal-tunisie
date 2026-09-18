"""Figure « poids de l'emploi public dans l'emploi total » (sources INS et BCT).

Numérateurs : l'enquête INS sur la fonction publique — d'une part l'ensemble des **agents**
(tab1, ouvriers et contractuels compris), d'autre part les seuls **fonctionnaires**
(tab8, somme des catégories A1 à D).
Dénominateur : la **population active occupée** publiée par la Banque centrale, recollée à
travers quatorze rapports annuels.

    from figures import emploi_public as ep
    ep.fig_part()      # les deux ratios
    ep.part_table()    # numérateurs, dénominateur et ratios (onglet Données)

POURQUOI DEUX COURBES, ET NON UNE. Le rapport annuel de 2015 énonce qu'« en 2015, les
fonctionnaires représentent 18,5 % de la population active occupée ». Vérification faite,
ce chiffre s'obtient avec l'effectif **large** — 601,9 milliers d'agents — et non avec les
fonctionnaires au sens strict, qui donneraient 14,6 %. La Banque centrale emploie donc le
mot dans son acception large. Tracer les deux ratios rend l'écart visible plutôt que de le
reléguer en note : ils répondent à deux questions différentes.

RÉSERVES QUE LA FIGURE DOIT PORTER :
  - les deux périmètres ne se recouvrent pas. Le numérateur INS inclut les collectivités
    locales et les établissements publics administratifs, mais **exclut** les militaires,
    les forces de sécurité intérieure et les magistrats ; le dénominateur est l'emploi
    total, salarié **et non salarié**, dans une économie à forte informalité ;
  - en **2020**, le dénominateur s'effondre (3 566 → 3 433 milliers). Le ratio monte alors
    sans qu'aucun recrutement ait eu lieu ;
  - le dénominateur est **révisé** d'un rapport à l'autre : avec la valeur d'époque, 2015
    donne 18,5 % ; avec la valeur révisée, 17,7 %. L'effet de millésime vaut 0,8 point.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_AGENTS = "fonction-publique-effectifs"     # tab1, ligne « Total »
SERIE_FONC = "fonction-publique-categories"      # tab8, catégories A1 à D
SERIE_EMPLOI = "bct-emploi-occupe"               # BCT, population active occupée

_CATS = ["Catégorie A1", "Catégorie A2", "Catégorie A3",
         "Catégorie B", "Catégorie C", "Catégorie D"]

_L = {
    "titre": {"fr": "Poids de l'emploi public dans l'emploi total, 2015-2021",
              "ar": "وزن التشغيل العمومي في التشغيل الإجمالي، 2015-2021"},
    "x": {"fr": "Année", "ar": "السنة"},
    "y": {"fr": "Part de la population active occupée (%)",
          "ar": "الحصة من السكان النشيطين المشتغلين (٪)"},
    "lg_agents": {"fr": "Agents de la fonction publique (y compris ouvriers et contractuels)",
                  "ar": "أعوان الوظيفة العمومية (بما في ذلك العملة والمتعاقدون)"},
    "lg_fonc": {"fr": "Fonctionnaires seuls (catégories A1 à D)",
                "ar": "الموظفون وحدهم (الأصناف أ1 إلى د)"},
    "covid": {"fr": "le dénominateur recule\nen 2020 : le ratio monte\nsans recrutement",
              "ar": "يتراجع المقام سنة 2020:\nترتفع النسبة\nدون انتداب"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_agents": {"fr": "Agents (milliers)", "ar": "الأعوان (بالآلاف)"},
    "col_fonc": {"fr": "Fonctionnaires (milliers)", "ar": "الموظفون (بالآلاف)"},
    "col_emploi": {"fr": "Actifs occupés (milliers)", "ar": "المشتغلون (بالآلاف)"},
    "col_r_agents": {"fr": "Part des agents (%)", "ar": "حصة الأعوان (٪)"},
    "col_r_fonc": {"fr": "Part des fonctionnaires (%)", "ar": "حصة الموظفين (٪)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _donnees():
    """(année, agents, fonctionnaires, occupés) sur les années communes aux trois séries."""
    ag = {int(r.annee): float(r.valeur)
          for r in figtools.series(SERIE_AGENTS).itertuples()
          if str(r.indicateur).strip() == "Total"}
    fo: dict[int, float] = {}
    for r in figtools.series(SERIE_FONC).itertuples():
        if str(r.categorie).strip() in _CATS:
            fo[int(r.annee)] = fo.get(int(r.annee), 0.0) + float(r.valeur)
    em = {int(r.annee): float(r.valeur) for r in figtools.series(SERIE_EMPLOI).itertuples()}
    communes = sorted(set(ag) & set(fo) & set(em))
    return [(a, ag[a], fo[a], em[a]) for a in communes]


def part_table():
    """Tableau (onglet Données) : numérateurs, dénominateur et les deux ratios."""
    import pandas as pd
    return pd.DataFrame([
        {_lab("col_annee"): a,
         _lab("col_agents"): round(ag, 1),
         _lab("col_fonc"): round(fo, 1),
         _lab("col_emploi"): round(em),
         _lab("col_r_agents"): round(100 * ag / em, 1),
         _lab("col_r_fonc"): round(100 * fo / em, 1)}
        for a, ag, fo, em in _donnees()])


def fig_part():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    annees = [a for a, _, _, _ in d]
    r_ag = [100 * ag / em for _, ag, _, em in d]
    r_fo = [100 * fo / em for _, _, fo, em in d]

    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    ax.plot(annees, r_ag, "o-", color="#08519c", lw=2.2, ms=5, label=ft(_lab("lg_agents")))
    ax.plot(annees, r_fo, "s--", color="#bf8700", lw=1.8, ms=4, label=ft(_lab("lg_fonc")))

    # 2020 : c'est le dénominateur qui recule, pas l'emploi public qui bondit.
    # Le cartouche va dans la bande HAUTE, vide, et une flèche le rattache au point de
    # 2020 : placé entre les deux courbes il tenait à l'étroit, et rien ne disait ce
    # qu'il commentait.
    if 2020 in annees:
        ax.axvspan(2019.5, 2020.5, color="#6e7781", alpha=0.08)
        y2020 = r_ag[annees.index(2020)]
        ax.annotate("\n".join(ft(l) for l in _lab("covid").split("\n")),
                    xy=(2020, y2020), xytext=(2019.4, max(r_ag) * 1.22),
                    fontsize=7.5, color="#57606a", ha="center", va="center",
                    arrowprops=dict(arrowstyle="->", color="#8b949e", lw=0.8,
                                    shrinkA=2, shrinkB=4),
                    bbox=dict(boxstyle="round,pad=0.35", fc="#f6f8fa",
                              ec="#8b949e", lw=0.6, alpha=0.95))

    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y")))
    ax.set_title(ft(_lab("titre")))
    ax.set_ylim(0, max(r_ag) * 1.35)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower left", fontsize=8.5)
    fig.tight_layout()
    return fig

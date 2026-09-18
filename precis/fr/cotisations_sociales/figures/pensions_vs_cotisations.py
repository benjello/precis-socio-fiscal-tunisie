"""Figure « pensions versées et cotisations encaissées, CNSS, 2000-2020 » (source CNSS).

    from figures import pensions_vs_cotisations as pvc
    pvc.fig_couverture()    # les deux courbes
    pvc.table()             # les deux séries et leur écart (onglet Données)

CE QUE LA FIGURE MONTRE. Les cotisations encaissées ont déjà leur figure ; celle-ci leur
oppose ce que la caisse verse au titre des seules pensions. À partir de **2015**, et sans
interruption jusqu'en 2020, les pensions dépassent l'ensemble des cotisations encaissées :
2 346,8 contre 2 308 MD en 2015, puis 4 013,6 contre 3 430 en 2020. En 2014 encore les
cotisations menaient (2 159 contre 2 073,6).

CE QUE LA FIGURE N'EST PAS, ET NE DOIT PAS ÊTRE PRÉSENTÉE COMME TEL :
  - **ce n'est pas un solde, ni un déficit.** Les pensions sont UNE branche de dépenses,
    les cotisations sont l'ENSEMBLE des recettes de cotisation. Opposer une partie à un
    tout ne donne pas une balance : cela donne un taux de couverture, et c'est sous ce
    seul nom que la figure se lit ;
  - le total des dépenses n'est pas tracé, faute d'être extractible : la planche d'origine
    ne l'étiquette que sur quelques colonnes et il n'y boucle pas partout (en 2015 le
    total affiché est inférieur à sa propre composante Pensions) ;
  - **la rupture de 2006 n'affecte qu'une des deux courbes.** Cette année-là les recettes
    des branches maladie et accidents du travail passent à la CNAM : les cotisations
    tombent de 1 351 à 993 MD, tandis que les pensions poursuivent leur pente (765,3 puis
    854,6). L'écart d'avant 2006 tient donc pour partie au champ de la courbe des
    cotisations, non à la seule démographie ;
  - les deux séries sont en **dinars courants**, non déflatées.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_COTIS = "cnss-cotisations"
SERIE_PENS = "cnss-pensions-versees"
ANNEE_TRANSFERT = 2006

_L = {
    "titre": {"fr": "CNSS : pensions versées et cotisations encaissées, 2000-2020",
              "ar": "الصندوق الوطني للضمان الاجتماعي: الجرايات المدفوعة والاشتراكات المستخلصة، 2000-2020"},
    "x": {"fr": "Année", "ar": "السنة"},
    "y": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "lg_cotis": {"fr": "Cotisations encaissées (tous régimes)",
                 "ar": "الاشتراكات المستخلصة (كلّ الأنظمة)"},
    "lg_pens": {"fr": "Pensions versées", "ar": "الجرايات المدفوعة"},
    "transfert": {
        "fr": "2006 : les branches maladie\net accidents du travail\npassent à la CNAM",
        "ar": "2006: ينتقل فرعا التأمين على المرض\nوحوادث الشغل إلى الصندوق الوطني\nللتأمين على المرض"},
    "croisement": {"fr": "2015 : les pensions passent\nau-dessus des cotisations",
                   "ar": "2015: تتجاوز الجرايات الاشتراكات"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_cotis": {"fr": "Cotisations (MD)", "ar": "الاشتراكات (م.د)"},
    "col_pens": {"fr": "Pensions (MD)", "ar": "الجرايات (م.د)"},
    "col_couv": {"fr": "Couverture (%)", "ar": "نسبة التغطية (٪)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _donnees():
    """[(année, cotisations, pensions)] — les deux séries, sur leurs années communes."""
    cot = {int(r.annee): float(r.cotisations_md)
           for r in figtools.series(SERIE_COTIS).itertuples()}
    pen = {int(r.annee): float(r.pensions_md)
           for r in figtools.series(SERIE_PENS).itertuples()}
    return [(a, cot[a], pen[a]) for a in sorted(set(cot) & set(pen))]


def table():
    import pandas as pd
    return pd.DataFrame([
        {_lab("col_annee"): a,
         _lab("col_cotis"): int(c),
         _lab("col_pens"): p,
         _lab("col_couv"): round(100 * c / p, 1)}
        for a, c, p in _donnees()])


def fig_couverture():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    annees = [a for a, _, _ in d]
    cot = [c for _, c, _ in d]
    pen = [p for _, _, p in d]

    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    ax.plot(annees, cot, "o-", color="#08519c", lw=2.2, ms=4, label=ft(_lab("lg_cotis")))
    ax.plot(annees, pen, "s--", color="#bf8700", lw=2.0, ms=4, label=ft(_lab("lg_pens")))

    # La rupture de champ de 2006 ne touche QUE la courbe des cotisations : le dire sur la
    # figure évite de lire l'écart d'avant 2006 comme un fait purement démographique.
    if ANNEE_TRANSFERT in annees:
        ax.axvspan(ANNEE_TRANSFERT - 0.5, ANNEE_TRANSFERT + 0.5, color="#6e7781", alpha=0.10)
        ax.annotate("\n".join(ft(l) for l in _lab("transfert").split("\n")),
                    xy=(ANNEE_TRANSFERT, cot[annees.index(ANNEE_TRANSFERT)]),
                    xytext=(2003.2, max(pen) * 0.72),
                    fontsize=7.5, color="#57606a", ha="center", va="center",
                    arrowprops=dict(arrowstyle="->", color="#8b949e", lw=0.8,
                                    shrinkA=2, shrinkB=4),
                    bbox=dict(boxstyle="round,pad=0.35", fc="#f6f8fa",
                              ec="#8b949e", lw=0.6, alpha=0.95))

    # Le croisement : première année où les pensions passent devant, et elles n'en
    # redescendent plus.
    croise = [a for a, c, p in d if p > c]
    if croise:
        a0 = croise[0]
        ax.annotate("\n".join(ft(l) for l in _lab("croisement").split("\n")),
                    xy=(a0, pen[annees.index(a0)]), xytext=(2012.0, max(pen) * 1.02),
                    fontsize=7.5, color="#57606a", ha="center", va="center",
                    arrowprops=dict(arrowstyle="->", color="#8b949e", lw=0.8,
                                    shrinkA=2, shrinkB=4),
                    bbox=dict(boxstyle="round,pad=0.35", fc="#f6f8fa",
                              ec="#8b949e", lw=0.6, alpha=0.95))

    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y")))
    ax.set_title(ft(_lab("titre")))
    # Une série annuelle ne se gradue pas en demi-années.
    ax.set_xticks([a for a in annees if a % 5 == 0])
    ax.set_xticks(annees, minor=True)
    ax.set_ylim(0, max(max(cot), max(pen)) * 1.18)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8.5)
    fig.tight_layout()
    return fig

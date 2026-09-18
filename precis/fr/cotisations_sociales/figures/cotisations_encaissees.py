"""Figure « cotisations encaissées par la CNSS, 2000-2020 » (source CNSS).

    from figures import cotisations_encaissees as ce
    ce.fig_cotisations()     # la série, en dinars courants
    ce.table()               # montants et variation annuelle (onglet Données)

CE QUE LA FIGURE MONTRE, ET QU'AUCUN TABLEAU DE TAUX NE PEUT MONTRER. Le livre décrit les
taux régime par régime ; il ne dit pas ce que ces taux rapportent. Les cotisations
encaissées passent de 984 à 3 430 MD en vingt et un ans, et la courbe porte deux
retournements que le texte des barèmes ne laisse pas prévoir.

RÉSERVES QUE LA FIGURE DOIT PORTER :
  - **2006 est une rupture de champ, non un accident conjoncturel** : cette année-là, les
    recettes des branches de l'assurance maladie et de la réparation des accidents du
    travail passent à la CNAM. Les cotisations encaissées par la CNSS tombent de 1 351 à
    993 MD sans qu'aucun taux ait baissé. La série n'est pas homogène de part et d'autre,
    et la planche d'origine porte elle-même cette note ;
  - **2020 est un vrai recul** (3 445 puis 3 430 MD), le premier depuis le transfert ;
  - les montants sont en **dinars courants**. Sur vingt ans d'inflation, la pente ne se
    lit pas comme une progression réelle : c'est la forme — les deux ruptures — qui
    s'interprète, non le niveau.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "cnss-cotisations"
ANNEE_TRANSFERT = 2006

_L = {
    "titre": {"fr": "Cotisations encaissées par la CNSS, tous régimes, 2000-2020",
              "ar": "الاشتراكات المستخلصة من الصندوق الوطني للضمان الاجتماعي، كلّ الأنظمة، 2000-2020"},
    "x": {"fr": "Année", "ar": "السنة"},
    "y": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "lg": {"fr": "Cotisations encaissées", "ar": "الاشتراكات المستخلصة"},
    "transfert": {
        "fr": "2006 : les branches maladie\net accidents du travail\npassent à la CNAM",
        "ar": "2006: ينتقل فرعا التأمين على المرض\nوحوادث الشغل إلى الصندوق الوطني\nللتأمين على المرض"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_montant": {"fr": "Cotisations (MD)", "ar": "الاشتراكات (م.د)"},
    "col_var": {"fr": "Variation annuelle (%)", "ar": "التغيّر السنوي (٪)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _donnees():
    return sorted((int(r.annee), float(r.cotisations_md))
                  for r in figtools.series(SERIE).itertuples())


def table():
    import pandas as pd
    d = _donnees()
    lignes = []
    for i, (a, v) in enumerate(d):
        var = None if i == 0 else round(100 * (v - d[i - 1][1]) / d[i - 1][1], 1)
        lignes.append({_lab("col_annee"): a,
                       _lab("col_montant"): int(v),
                       _lab("col_var"): var})
    return pd.DataFrame(lignes)


def fig_cotisations():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _donnees()
    annees = [a for a, _ in d]
    vals = [v for _, v in d]

    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    ax.plot(annees, vals, "o-", color="#08519c", lw=2.2, ms=4, label=ft(_lab("lg")))

    # La rupture de champ de 2006 : le décrochage vient d'un transfert de branches, pas
    # d'une baisse de taux. La bande et le cartouche le disent sur la figure même, pour
    # que la courbe ne soit pas lue comme un effondrement des recettes.
    if ANNEE_TRANSFERT in annees:
        ax.axvspan(ANNEE_TRANSFERT - 0.5, ANNEE_TRANSFERT + 0.5, color="#6e7781", alpha=0.10)
        y = vals[annees.index(ANNEE_TRANSFERT)]
        ax.annotate("\n".join(ft(l) for l in _lab("transfert").split("\n")),
                    xy=(ANNEE_TRANSFERT, y), xytext=(2009.5, max(vals) * 0.55),
                    fontsize=7.5, color="#57606a", ha="center", va="center",
                    arrowprops=dict(arrowstyle="->", color="#8b949e", lw=0.8,
                                    shrinkA=2, shrinkB=4),
                    bbox=dict(boxstyle="round,pad=0.35", fc="#f6f8fa",
                              ec="#8b949e", lw=0.6, alpha=0.95))

    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y")))
    ax.set_title(ft(_lab("titre")))
    # Une série annuelle ne se gradue pas en demi-années : matplotlib place sinon des
    # repères à 2002,5 et 2007,5, qui ne désignent aucune observation.
    ax.set_xticks([a for a in annees if a % 5 == 0])
    ax.set_xticks(annees, minor=True)
    ax.set_ylim(0, max(vals) * 1.15)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8.5)
    fig.tight_layout()
    return fig

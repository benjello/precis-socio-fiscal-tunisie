"""Figure « salaire brut des fonctionnaires par catégorie statutaire » (source INS).

Série tab20 de l'enquête INS : salaire mensuel brut des fonctionnaires par catégorie
A1 à D, de 2015 à 2020, en dinars courants.

    from figures import salaires_categories as sc
    sc.fig_salaires()      # les six catégories, en courbes
    sc.salaires_table()    # tableau (onglet Données)

CE QUE LA FIGURE MONTRE, ET QUE LE CHAPITRE ÉNONÇAIT SANS LE CHIFFRER : le resserrement
de la hiérarchie indiciaire. Le rapport entre le haut et le bas de la grille revient de
2,14 à 1,73 en six ans — non parce que le haut recule, mais parce que le bas progresse
plus vite, les augmentations générales étant servies en dinars et non en pourcentage.

RÉSERVE PORTÉE PAR LA SÉRIE ELLE-MÊME : l'INS étiquette « Catégorie A2 » la ligne que
l'arabe nomme « أ3 ». Le versement corrige l'étiquette — sans quoi deux courbes
porteraient le même nom et A3 disparaîtrait du graphique.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "ins-salaire-par-categorie"

# Même palette que la figure des effectifs par catégorie : A en teintes froides
# (conception, encadrement), B/C/D en chaudes et neutres (maîtrise, exécution).
_CATS = ["A1", "A2", "A3", "B", "C", "D"]
_COULEURS = {"A1": "#08519c", "A2": "#3182bd", "A3": "#9ecae1",
             "B": "#fd8d3c", "C": "#d1242f", "D": "#6e7781"}

_L = {
    "titre": {"fr": "Salaire mensuel brut des fonctionnaires par catégorie, 2015-2020",
              "ar": "الأجر الشهري الخام للموظفين حسب الصنف، 2015-2020"},
    "x": {"fr": "Année", "ar": "السنة"},
    "y": {"fr": "Dinars courants par mois", "ar": "دينار جارٍ في الشهر"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _wide():
    df = figtools.series(SERIE)
    w = (df.pivot(index="annee", columns="categorie", values="valeur").reset_index())
    w.columns.name = None
    return w[["annee", *[c for c in _CATS if c in w.columns]]]


def salaires_table():
    """Tableau (onglet Données) : les six catégories, dinars courants par mois."""
    return _wide().rename(columns={"annee": _lab("col_annee")})


def fig_salaires():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    w = _wide()
    y = w["annee"]
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for cat in _CATS:
        if cat not in w.columns:
            continue
        ax.plot(y, w[cat], "o-", color=_COULEURS[cat], lw=2, ms=4.5, label=ft(cat))
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y")))
    ax.set_title(ft(_lab("titre")))
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=9)
    fig.tight_layout()
    return fig

"""Figure « Élèves et étudiants » du chapitre d'histoire (fiche de plan § 2.5, F2).

`donnees()` copie, ligne à ligne, cinq relevés de la série `education-effectifs-annuaire` du
catalogue de `tunisia-data` (lue par `figtools.series()`) dans le figdata
`figdata/fig_educ_eleves.csv`, avec leur source et leur page ; aucune valeur saisie à la main.
`vues()` lit ce figdata. Relancer après une correction de la série :

    uv run python precis/fr/education/figures/fig_educ_eleves.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
sys.path.insert(0, str(ICI.parents[3] / "scripts"))
import figtools  # noqa: E402
import fig_educ_depense as fd  # noqa: E402

RELEVES = (
    ("eleves-public-premier-cycle-base", "Élèves du public, premier cycle de l'enseignement de base"),
    ("eleves-prive-premier-cycle-base", "Élèves du privé, premier cycle de l'enseignement de base"),
    ("eleves-public-second-cycle-base-secondaire", "Élèves du public, second cycle de la base et secondaire"),
    ("eleves-prive-second-cycle-base-secondaire", "Élèves du privé, second cycle de la base et secondaire"),
    ("etudiants-total", "Étudiants, ensemble"),
)
SLUG = "fig_educ_eleves"


def donnees() -> None:
    import fig_educ_depense_donnees as dd
    rows = []
    for cle, nom in RELEVES:
        for r in dd.lire(cle).itertuples():
            rows.append({"Série": nom, "Période": r.annee, "Valeur": int(r.valeur), "Unité": r.unite,
                         "Édition": dd.edition(r.source), "Page": int(r.page), "Source": r.source})
    dd.ecrire(SLUG, pd.DataFrame(rows), ["ins-annuaire-statistique"], [
        "INS, Annuaire statistique, chapitre « Enseignement et culture », tableau des données générales "
        "de l'enseignement (sources citées : ministères de l'Éducation et de l'Enseignement supérieur) ; "
        "une valeur par année scolaire, dans l'édition la plus récente qui la contient",
        "les écoles de qualification technique ne sont pas comprises",
        "étudiants : définition de l'effectif révisée à partir de 2006-2007 (étudiants réguliers)"],
        "Élèves du public et du privé par cycle, étudiants, 1995-1996 à 2023-2024",
        series=["education-effectifs-annuaire"])


def _serie(d: pd.DataFrame, nom: str) -> pd.Series:
    s = d[d["Série"] == nom].copy()
    s.index = s["Période"].str[:4].astype(int)
    return s["Valeur"].astype(float)


def vues():
    figtools.apply_lang_font()
    d = fd.lire(SLUG)
    c1 = _serie(d, RELEVES[0][1]) + _serie(d, RELEVES[1][1])
    c2 = _serie(d, RELEVES[2][1]) + _serie(d, RELEVES[3][1])
    et = _serie(d, RELEVES[4][1])
    vues = []

    fig, ax = plt.subplots(figsize=(9.3, 4.8))
    fd._courbe(ax, c1 / 1000, fd.BLEU, "Premier cycle de la base", "milliers d'élèves", dec=1)
    fd._courbe(ax, c2 / 1000, fd.VERT, "Second cycle de la base et secondaire", "milliers d'élèves", dec=1)
    fd._courbe(ax, et / 1000, fd.ORANGE, "Étudiants", "milliers d'étudiants", dec=1, coupures=(2006,))
    fd._rupture(ax, 2003, "secondaire en 1 + 3", 0)
    fd._rupture(ax, 2006, "licence LMD, étudiants réguliers", 1)
    fd._rupture(ax, 2011, "fin de l'ancien régime", 2)
    fd._habille(ax, "Milliers", 1995, 2023, ymin=0)
    ax.set_xlabel(figtools.fig_text("Année scolaire commençant en"), fontsize=8)
    fd._legende(ax, 3)
    fig.tight_layout()
    vues.append(("Effectifs", fig))

    fig, ax = plt.subplots(figsize=(9.3, 4.8))
    p1 = 100 * _serie(d, RELEVES[1][1]) / c1
    p2 = 100 * _serie(d, RELEVES[3][1]) / c2
    fd._courbe(ax, p1, fd.BLEU, "Premier cycle de la base", "%", dec=1)
    fd._courbe(ax, p2, fd.VERT, "Second cycle de la base et secondaire", "%", dec=1)
    fd._habille(ax, "Part du privé (%)", 1995, 2023, ymin=0)
    ax.set_xlabel(figtools.fig_text("Année scolaire commençant en"), fontsize=8)
    fd._legende(ax, 2)
    fig.tight_layout()
    vues.append(("Part du privé", fig))
    return vues


if __name__ == "__main__":
    donnees()

"""Figure « Diplômés de l'enseignement supérieur » du chapitre du supérieur.

`donnees()` copie, ligne à ligne, les deux relevés (total, femmes) de la série
`education-superieur-diplomes` du catalogue de `tunisia-data` (lue par `figtools.series()`)
dans le figdata `figdata/fig_educ_superieur_diplomes.csv`, avec leur source et leur page ;
aucune valeur saisie à la main. `vues()` lit ce figdata. L'en-tête de provenance et les
réserves (couture 2002-03/2003-04 ; 2012-13 hors annuaire ; pic 2009-10) sont propres à ce
chapitre. Relancer après une correction de la série (`tunisia-data`, puis
`figtools.refresh_cache("education-superieur-diplomes")`) :

    uv run python precis/fr/education/figures/fig_educ_superieur_diplomes.py
"""
from __future__ import annotations

import re
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

SLUG = "fig_educ_superieur_diplomes"
SERIE = "education-superieur-diplomes"
FIGDATA = ICI.parent / "figdata"
DATE = "2026-11-10"
FICHE = "docs/notes/education-releve-diplomes-superieur-2026-11-10.md"
SOURCES = ["ins-annuaire-statistique", "ins-tunisie-en-chiffres-diplomes",
           "mesrs-chiffres2013-2014", "mesrs-chiffres2012-2013"]
CAVEATS = [
    "diplômés de fin d'année universitaire du secteur public, tous diplômes confondus (privé exclu)",
    "couture de définition en 2003-2004 : 2001-02 et 2002-03 comptent les admis de la session de juin "
    "ventilés par secteur, les années suivantes les diplômés par filière ; le trait ne relie pas 2002-03 à 2003-04",
    "2012-13 hors annuaire (édition 2009-2013 jamais mise en ligne) : total de Tunisie en chiffres 2013-2014, "
    "femmes reconstituées de deux cases MESRS (34 717 + 6 673)",
    "pic de 2009-10 : sortie conjointe des dernières maîtrises de l'ancien régime (26 076) et des techniciens "
    "supérieurs (8 333) avec les premières cohortes LMD, non une expansion réelle",
]
NOTE = "Diplômés de l'enseignement supérieur du secteur public et part des femmes, 2001-02 à 2022-23"
NOM = {"diplomes-superieur-total": "Diplômés", "diplomes-superieur-etudiantes": "dont femmes"}


def _edition(source: str) -> str:
    m = re.search(r"Annuaire statistique de la Tunisie (\d{4}-\d{4})", source)
    if m:
        return m.group(1)
    if "Tunisie en chiffres" in source:
        return "Tunisie en chiffres 2013-2014"
    if "en chiffres 2013-2014" in source:
        return "MESRS en chiffres 2013-2014"
    return ""


def _ecrire(df: pd.DataFrame) -> None:
    FIGDATA.mkdir(parents=True, exist_ok=True)
    head = [
        f"# Figure-data du précis socio-fiscal tunisien — généré le {DATE}",
        f"# séries (tunisia_data) : {SERIE}",
        f"# sources (citation) : {', '.join('@' + k for k in SOURCES)}",
        f"# fiches : {FICHE}",
        f"# méthode/hypothèses : {'. '.join(CAVEATS)}",
        f"# note : {NOTE}",
    ]
    (FIGDATA / f"{SLUG}.csv").write_text("\n".join(head) + "\n" + df.to_csv(index=False), encoding="utf-8")
    side = "series: [{}]\nsources: [{}]\nfiches: [{}]\ncaveats: [{}]\ngenerated: {}\n".format(
        SERIE, ", ".join(SOURCES), FICHE, ". ".join(CAVEATS), DATE)
    (FIGDATA / f"{SLUG}.csv.yml").write_text(side, encoding="utf-8")


def donnees() -> None:
    rows = []
    for r in figtools.series(SERIE).itertuples():
        rows.append({"Série": NOM[r.serie], "Période": r.annee, "Valeur": int(r.valeur),
                     "Unité": r.unite, "Édition": _edition(r.source), "Page": int(r.page),
                     "Source": r.source})
    _ecrire(pd.DataFrame(rows))


def _serie(d: pd.DataFrame, nom: str) -> pd.Series:
    s = d[d["Série"] == nom].copy()
    s.index = s["Période"].str[:4].astype(int)
    return s["Valeur"].astype(float)


def vues():
    figtools.apply_lang_font()
    d = fd.lire(SLUG)
    tot = _serie(d, "Diplômés")
    fem = _serie(d, "dont femmes")
    vues = []

    fig, ax = plt.subplots(figsize=(9.3, 4.8))
    fd._courbe(ax, tot / 1000, fd.BLEU, "Diplômés (secteur public)", "milliers de diplômés",
               dec=1, coupures=(2003,))
    pic = float(tot[2009]) / 1000
    ax.annotate(figtools.fig_text("pic 2009-10 : dernières maîtrises\nde l'ancien régime et 1res cohortes LMD"),
                xy=(2009, pic), xytext=(2010.4, pic - 6), fontsize=7, color="#57606a",
                ha="left", va="top", arrowprops=dict(arrowstyle="-", color="#57606a", lw=0.8))
    fd._rupture(ax, 2003, "diplômés par filière (public) ; avant : admis de juin par secteur", 0)
    fd._habille(ax, "Milliers de diplômés", 2001, 2022, ymin=0)
    ax.set_xlabel(figtools.fig_text("Année universitaire commençant en"), fontsize=8)
    fd._legende(ax, 1)
    fig.tight_layout()
    vues.append(("Diplômés", fig))

    fig, ax = plt.subplots(figsize=(9.3, 4.8))
    fd._courbe(ax, 100 * fem / tot, fd.VERT, "Part des femmes parmi les diplômés", "%",
               dec=1, coupures=(2003,))
    fd._rupture(ax, 2003, "changement de définition", 0)
    fd._habille(ax, "Part des femmes (%)", 2001, 2022, ymin=0)
    ax.set_xlabel(figtools.fig_text("Année universitaire commençant en"), fontsize=8)
    fd._legende(ax, 1)
    fig.tight_layout()
    vues.append(("Part des femmes", fig))
    return vues


if __name__ == "__main__":
    donnees()

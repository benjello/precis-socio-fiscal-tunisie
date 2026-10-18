"""Figures du chapitre « De la loi de 1958 au Conseil supérieur de l'éducation et de
l'enseignement » (`_histoire.qmd`) du livre *L'éducation*.

UNE FIGURE : la frise des lois du système éducatif, 1956-2026.

D'OÙ VIENNENT LES DONNÉES. Elles sont écrites ici, à la main : ce sont les dates des textes
cités dans le chapitre et dans celui des aides (`_aides.qmd`), avec leur clé de citation et
leur article. Ce n'est pas une statistique : aucune série de l'entrepôt n'est lue. Le figdata
téléchargeable (`figdata/fig_educ_histoire_frise.csv`) reprend ces lignes telles quelles.

CE QUE LES BORNES VALENT. `debut` et `fin` sont des ANNÉES, pour le tracé d'une bande : la
date d'effet exacte de chaque texte est dans le chapitre. Une bande « par anticipation » est
une règle appliquée avant le texte qui la fonde (école de base dès 1989-1990, licence LMD dès
2006-2007). Les points sont des naissances : un dispositif, un organe ou un fonds. La dernière
année, 2026, est celle de l'état du droit exposé au chapitre. Les textes connus par leur seul
intitulé n'y paraissent pas.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402

FRISE = "educ-histoire-frise"
FIN = 2026  # année de l'état du droit exposé au chapitre

BLEU, VERT, ORANGE, VIOLET, GRIS, BRUN = (
    "#0969da", "#1a7f37", "#bc4c00", "#8250df", "#57606a", "#9a6700")

PISTES = [
    "Enseignement scolaire",
    "Obligation",
    "Enseignement supérieur",
    "Formation professionnelle initiale",
    "Conseil supérieur et fonds",
    "Aides aux élèves et aux étudiants",
]
COULEURS = dict(zip(PISTES, [BLEU, ORANGE, VIOLET, VERT, BRUN, GRIS]))

# piste, type (bande | anticipation | point), début, fin, libellé, étiquette courte,
# clé de citation, article
LIGNES = [
    # Enseignement scolaire
    ("Enseignement scolaire", "bande", 1958, 1988,
     "loi de 1958 : accès dès six ans, gratuité à tous les degrés ; primaire 6 ans, moyen "
     "3 ans, secondaire 6 ans", "loi de 1958 : primaire, moyen, secondaire",
     "loi58-118", "art. 2 à 4, 8, 11, 15, 60"),
    ("Enseignement scolaire", "anticipation", 1989, 1990,
     "école de base appliquée année par année à compter de l'année scolaire 1989-1990, "
     "avant la loi de 1991", "base dès 1989-1990", "loi91-65", "art. 34"),
    ("Enseignement scolaire", "bande", 1991, 2001,
     "loi de 1991 : école de base de neuf ans (6 + 3), secondaire de 4 ans (2 + 2), "
     "matières de la base enseignées en arabe", "loi de 1991 : base 6 + 3",
     "loi91-65", "art. 8, 9, 11"),
    ("Enseignement scolaire", "bande", 2002, FIN,
     "loi d'orientation de 2002 : année préparatoire rattachée à la base ; secondaire en "
     "1 + 3 à la rentrée 2003-2004 ; deux langues étrangères",
     "loi de 2002 : année préparatoire", "loi2002-80",
     "art. 1er, 9, 16 à 18, 26, 69"),
    ("Enseignement scolaire", "point", 2003, 2003,
     "secondaire de quatre ans en 1 + 3, à la rentrée 2003-2004", "secondaire 1 + 3",
     "loi2002-80", "art. 26, 69"),
    ("Enseignement scolaire", "point", 2008, 2008,
     "langues étrangères permises dans tous les cycles ; collèges pilotes ; diplôme de fin "
     "de base général ou technique", "loi de 2008", "loi2008-9", "art. 24, 29, 60 bis, 61"),
    # Obligation
    ("Obligation", "bande", 1958, 1990,
     "obligation de six à douze ans annoncée, non imposée : sa date est renvoyée à des "
     "dispositions ultérieures", "annoncée (6-12 ans), non imposée", "loi58-118", "art. 2"),
    ("Obligation", "bande", 1991, 2016,
     "obligation de six à seize ans, amende du tuteur", "6 à 16 ans, amende du tuteur",
     "loi91-65", "art. 7, 32"),
    ("Obligation", "bande", 2017, FIN,
     "obligation de six à seize ans à l'école ; formation professionnelle initiale "
     "obligatoire jusqu'à dix-huit ans hors scolarité et hors emploi",
     "18 ans en formation", "loi2017-13", "art. 1er à 3"),
    ("Obligation", "point", 2022, 2022,
     "obligation jusqu'à seize ans et gratuité de l'enseignement public inscrites dans la "
     "Constitution", "Constitution", "constitution2022", "art. 44"),
    # Supérieur
    ("Enseignement supérieur", "bande", 1958, 1988,
     "enseignement supérieur prévu par la loi de 1958 (chapitre III)",
     "loi de 1958, chapitre III", "loi58-118", "ch. III"),
    ("Enseignement supérieur", "bande", 1989, 2005,
     "loi de 1989 : universités établissements publics administratifs ; aide de l'État ; "
     "frais d'inscription des étudiants disposant de ressources",
     "loi de 1989", "loi89-70", "art. 1er, 5, 28, 30"),
    ("Enseignement supérieur", "anticipation", 2006, 2007,
     "licence du système LMD applicable à partir de l'année universitaire 2006-2007",
     "LMD dès 2006-2007", "decret2008-3123", "art. 43"),
    ("Enseignement supérieur", "bande", 2008, FIN,
     "loi de 2008 : licence, mastère, doctorat ; supérieur public gratuit, droits "
     "d'inscription par décret", "loi de 2008 : LMD",
     "loi2008-19", "art. 3, 7"),
    ("Enseignement supérieur", "point", 2012, 2012,
     "ancien régime des études éteint à la fin de l'année universitaire 2011-2012",
     "fin de l'ancien régime", "loi2008-19", "art. 56"),
    # Formation professionnelle
    ("Formation professionnelle initiale", "bande", 2008, 2016,
     "loi de 2008 : trois cycles, du CAP au BTS ; baccalauréat professionnel ; "
     "apprentissage de 15 à 20 ans", "loi de 2008", "loi2008-10",
     "art. 9, 13, 15, 18"),
    ("Formation professionnelle initiale", "bande", 2017, FIN,
     "formation obligatoire et gratuite jusqu'à dix-huit ans pour qui n'est ni scolarisé ni "
     "inséré", "obligatoire à 18 ans", "loi2017-13", "art. 1er, 2"),
    # Conseil
    ("Conseil supérieur et fonds", "point", 1958, 1958,
     "Conseil supérieur de l'éducation nationale", "1958", "loi58-118", "art. 38"),
    ("Conseil supérieur et fonds", "point", 2000, 2000,
     "Conseil supérieur de l'éducation (décret de 2000)", "2000", "decret2000-2260",
     "art. 2, 3"),
    ("Conseil supérieur et fonds", "point", 2022, 2022,
     "Conseil supérieur de l'éducation et de l'enseignement, inscrit dans la Constitution",
     "2022", "constitution2022", "art. 135"),
    ("Conseil supérieur et fonds", "point", 2024, 2024,
     "Conseil organisé en instance constitutionnelle", "2024", "decret-loi2024-2", "art. 2"),
    ("Conseil supérieur et fonds", "point", 2024, 2024,
     "fonds national de la réforme éducative (loi de finances pour 2024)", "",
     "lf-2024", "art. 15"),
    # Aides : naissances
    ("Aides aux élèves et aux étudiants", "point", 1957, 1957,
     "bourse nationale des étudiants", "bourse nationale", "decret57-78-bourse-nationale", ""),
    ("Aides aux élèves et aux étudiants", "point", 1966, 1966,
     "bourses scolaires", "bourses scolaires", "arrete-1966-10-03-bourses-scolaires", ""),
    ("Aides aux élèves et aux étudiants", "point", 1970, 1970,
     "Office national des œuvres universitaires", "ONOU", "loi70-9-onou", ""),
    ("Aides aux élèves et aux étudiants", "point", 1986, 1986,
     "prêt universitaire", "prêt", "decret86-688-bourses-prets", ""),
    ("Aides aux élèves et aux étudiants", "point", 1988, 1988,
     "trois offices des œuvres universitaires", "offices", "loi88-135-oou-nord", ""),
    ("Aides aux élèves et aux étudiants", "point", 1991, 1991,
     "droits d'inscription pour les élèves dont les parents peuvent les payer (montants "
     "fixés en 1992)", "droits d'inscription", "loi91-65", "art. 24"),
    ("Aides aux élèves et aux étudiants", "point", 1999, 1999,
     "prêt universitaire des caisses de sécurité sociale", "prêt des caisses",
     "decret99-1544-prets-caisses", ""),
    ("Aides aux élèves et aux étudiants", "point", 2016, 2016,
     "office des services scolaires", "office scolaire",
     "decret-gouv-2016-664-office-services-scolaires", ""),
    ("Aides aux élèves et aux étudiants", "point", 2018, 2018,
     "bourse d'intégration universitaire", "bourse d'intégration",
     "arrete-2018-12-04-bourse-integration", ""),
]

COLONNES = ["piste", "type", "debut", "fin", "libelle", "etiquette", "texte", "localisateur"]

# Grandes réformes de l'enseignement scolaire, marquées d'un trait vertical.
REFORMES = [(1958, "1958\nmise en place"), (1991, "1991\nécole de base,\nobligation"),
            (2002, "2002\nloi\nd'orientation"), (2017, "2017\nobligation\nde formation")]


def donnees() -> pd.DataFrame:
    return pd.DataFrame(LIGNES, columns=COLONNES)


figtools.register_provenance(
    FRISE,
    titre="Les lois du système éducatif, 1956-2026 : règles, organes et naissances des aides",
    sources=list(dict.fromkeys(l[6] for l in LIGNES)),
    unite="années (bornes des périodes)",
    perimetre=("enseignement scolaire, obligation, enseignement supérieur, formation "
               "professionnelle initiale, Conseil supérieur, naissance des aides"),
    caveats=("Bornes en années, pour le tracé : les dates d'effet exactes sont au chapitre. "
             "Les bandes « par anticipation » marquent une règle appliquée avant la loi qui la "
             "fonde. Les textes connus par leur seul intitulé n'y figurent pas."))


def table_frise() -> pd.DataFrame:
    d = donnees()
    return pd.DataFrame({
        "Domaine": d["piste"],
        "Nature": d["type"].map({"bande": "période", "anticipation": "application anticipée",
                                 "point": "naissance ou étape"}),
        "Début": d["debut"].astype(str),
        "Fin": [("" if r.type == "point" else str(r.fin)) for r in d.itertuples()],
        "Règle ou dispositif": d["libelle"],
        "Texte": d["texte"],
        "Article": d["localisateur"],
    })


def fig_frise():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = donnees()
    fig, ax = plt.subplots(figsize=(10.5, 5.6))
    n = len(PISTES)
    for i, piste in enumerate(PISTES):
        y = n - 1 - i
        c = COULEURS[piste]
        sous = d[d["piste"] == piste]
        for k, r in enumerate(sous[sous["type"] == "bande"].itertuples()):
            barre = ax.barh([y], [r.fin + 1 - r.debut], left=[r.debut], height=0.62,
                            facecolor=c, alpha=0.85 if k % 2 == 0 else 0.6,
                            edgecolor="white", lw=1)
            figtools.infobulle(barre[0], f"{piste} · {r.debut}-{r.fin} · {r.libelle}")
            ax.text(r.debut + 0.3, y, ft(r.etiquette), va="center", ha="left", fontsize=6.6,
                    color="white", clip_on=True)
        for r in sous[sous["type"] == "anticipation"].itertuples():
            barre = ax.barh([y], [r.fin + 1 - r.debut], left=[r.debut], height=0.62,
                            facecolor="white", hatch="///", edgecolor=c, lw=0.8)
            figtools.infobulle(barre[0], f"{piste} · {r.debut}-{r.fin} · {r.libelle}")
        points = sous[sous["type"] == "point"]
        for j, r in enumerate(points.itertuples()):
            fond = piste in ("Conseil supérieur et fonds", "Aides aux élèves et aux étudiants")
            p, = ax.plot([r.debut + 0.5], [y if fond else y + 0.31], marker="o", ms=6.5 if fond else 5.5,
                         mfc=c if fond else "white", mec=c if fond else "#1f2328", mew=1.1,
                         ls="", zorder=4)
            figtools.infobulle(p, f"{piste} · {r.debut} · {r.libelle}")
            if fond:
                dy = 9 if j % 2 == 0 else -9
                ax.annotate(ft(r.etiquette), xy=(r.debut + 0.5, y), xytext=(0, dy),
                            textcoords="offset points", ha="center",
                            va="bottom" if dy > 0 else "top", fontsize=6.2, color="#1f2328")
    for annee, texte in REFORMES:
        ax.axvline(annee, color=GRIS, ls=(0, (2, 2)), lw=0.9, zorder=0)
        ax.annotate(ft(texte), xy=(annee, n - 0.45), xytext=(2, 0),
                    textcoords="offset points", ha="left", va="bottom", fontsize=6.4,
                    color=GRIS)
    ax.set_yticks(range(n))
    ax.set_yticklabels([ft(p) for p in reversed(PISTES)], fontsize=7.6)
    ax.set_ylim(-0.8, n + 0.9)
    ax.set_xlim(1955, FIN + 1.5)
    ax.set_xticks(list(range(1955, 2030, 5)))
    for cote in ("top", "right", "left"):
        ax.spines[cote].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.grid(True, axis="x", alpha=0.25)
    ax.set_title(ft("Les lois du système éducatif, 1956-2026"), fontsize=10)
    ax.legend(handles=[
        Patch(facecolor=GRIS, alpha=0.8, label=ft("règle en vigueur sur la période")),
        Patch(facecolor="white", hatch="///", edgecolor=GRIS,
              label=ft("règle appliquée avant le texte qui la fonde")),
        Line2D([], [], marker="o", mfc="white", mec="#1f2328", ls="", ms=5.5,
               label=ft("étape d'une règle")),
        Line2D([], [], marker="o", mfc=GRIS, mec=GRIS, ls="", ms=6.5,
               label=ft("naissance d'un organe, d'un fonds ou d'une aide")),
    ], loc="upper center", bbox_to_anchor=(0.5, -0.07), ncol=2, fontsize=7.2, frameon=False)
    fig.subplots_adjust(left=0.22, right=0.985, top=0.93, bottom=0.17)
    return fig

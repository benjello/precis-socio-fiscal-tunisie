"""Figures du chapitre « L'enseignement scolaire ».

Les données sont les figdata `figdata/fig_educ_scolaire_{bac,flux}.csv` du livre : des copies,
ligne à ligne, des séries de la note documentaire (`docs/notes/education-scolaire-2026-10-17.md`,
§ 7.2 et 7.3), chaque ligne avec son édition, son tableau et sa page. Ces séries ne sont pas
encore au catalogue de `tunisia-data` : le module les lit dans le figdata et ne le réécrit
jamais (pas de `write_figdata`), comme `fig_educ_depense.py`.

Règles tenues ici :
  - une année sans valeur publiée reste un trou (segments non reliés) ;
  - les marques verticales datent les sessions qui suivent un changement de la règle de la
    moyenne finale du baccalauréat ; elles ne mesurent aucun effet ;
  - la valeur de 2014-2015 (347 redoublants, telle qu'imprimée) est un marqueur creux, non
    relié aux années voisines, et signalée dans l'infobulle.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

ICI = Path(__file__).resolve().parent
FIGDATA = ICI.parent / "figdata"

BLEU, VERT, ORANGE, GRIS = "#08519c", "#1a7f37", "#b45100", "#657487"


def lire(slug: str) -> pd.DataFrame:
    return pd.read_csv(FIGDATA / f"{slug}.csv", comment="#")


def _provenance(slug: str) -> dict:
    prov = {"sources": [], "caveats": [""]}
    for ligne in (FIGDATA / f"{slug}.csv").read_text(encoding="utf-8").splitlines():
        if not ligne.startswith("#"):
            break
        if ligne.startswith("# sources (citation) :"):
            prov["sources"] = [k.strip().lstrip("@") for k in ligne.split(":", 1)[1].split(",") if k.strip()]
        elif ligne.startswith("# méthode/hypothèses :"):
            prov["caveats"] = [ligne.split(":", 1)[1].strip()]
    return prov


def _nb(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _runs(annees: list[int]) -> list[list[int]]:
    runs: list[list[int]] = []
    for a in sorted(annees):
        if runs and a == runs[-1][-1] + 1:
            runs[-1].append(a)
        else:
            runs.append([a])
    return runs


def _courbe(ax, serie: pd.Series, couleur: str, libelle: str, unite: str, *, dec: int = 1,
            creux=(), mention_creux: str = "", etiquette=lambda a: str(a)):
    serie = serie.dropna().sort_index()
    annees = [int(a) for a in serie.index]
    for i, run in enumerate(_runs([a for a in annees if a not in creux])):
        ax.plot(run, [serie[a] for a in run], color=couleur, lw=2,
                label=figtools.fig_text(libelle) if i == 0 else None)
    for a in annees:
        v = float(serie[a])
        c = a in creux
        (pt,) = ax.plot([a], [v], marker="o", ls="none", ms=4.5, color=couleur,
                        mfc="white" if c else couleur, zorder=4)
        figtools.infobulle(pt, f"{etiquette(a)} · {libelle} : {_nb(v, dec)} {unite}"
                               + (f" ({mention_creux})" if c else ""))


def _habille(ax, ylabel: str, debut: int, fin: int, ymin: float | None = 0, pas: int = 2):
    ax.set_xlim(debut - 0.7, fin + 0.7)
    ax.set_xticks(range(debut, fin + 1, pas))
    if ymin is not None:
        ax.set_ylim(bottom=ymin)
    ax.set_ylabel(figtools.fig_text(ylabel))
    ax.grid(axis="y", color="#d7dce2", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)


def _marque(ax, annee: int, texte: str, rang: int = 0):
    x = annee - 0.5
    ax.axvline(x, color="#57606a", ls=(0, (2, 2)), lw=1, zorder=1)
    ax.annotate(figtools.fig_text(texte), xy=(x, 1), xycoords=("data", "axes fraction"),
                xytext=(4, -4 - 11 * rang), textcoords="offset points", ha="left", va="top",
                fontsize=7, color="#57606a")


def _legende(ax, ncol: int = 2):
    ax.legend(frameon=False, fontsize=8, ncol=ncol, loc="upper center",
              bbox_to_anchor=(0.5, -0.12))


def onglets(vues, slug: str, *, caption: str, note_lecture: str, source: str,
            colonnes_cachees=()) -> None:
    """Onglets Graphique / Données / Sources, sans réécrire le figdata."""
    from itables import to_html_datatable

    png = Path("_fig")
    png.mkdir(parents=True, exist_ok=True)
    df = lire(slug)
    vue_df = df.drop(columns=[c for c in colonnes_cachees if c in df.columns])
    table = to_html_datatable(
        vue_df, buttons=["csvHtml5", "excelHtml5"], scrollY="420px", scrollX=True,
        scrollCollapse=True, paging=False, classes="display compact nowrap", connected=True)
    prov = _provenance(slug)
    alt = caption.replace('"', "&quot;")
    image = figtools.onglet_graphique([
        (titre, figtools._image_vue(f, png, nom,
                                    alt if titre is None else f"{alt} — {titre}".replace('"', "&quot;")))
        for (titre, f), nom in zip(vues, figtools.noms_des_vues(slug, len(vues)))])
    cles = "\n".join(f"- [@{k}]" for k in prov.get("sources") or [])
    reserves = "\n".join(f"- {c}" for c in str((prov.get("caveats") or [""])[0]).split(". ") if c)
    lecture = (f'\n::: {{.callout-note appearance="simple" icon=true title="{figtools.t("how_to_read")}"}}\n'
               f"{note_lecture}\n:::\n")
    print(f"""::: {{.panel-tabset}}

## {figtools.t('tab_graph')}

{image}

::: {{.figure-source}}
{source}
:::
{lecture}
## {figtools.t('tab_data')}

{figtools.download_button(f"figdata/{slug}.csv")}

{table}

## {figtools.t('tab_src')}

::: {{.figure-sources-detail}}
{cles}

*{figtools.t('reserves')}* :

{reserves}
:::

:::

{caption}
""")


# --------------------------------------------------------------------------- baccalauréat
def vues_bac():
    figtools.apply_lang_font()
    d = lire("fig_educ_scolaire_bac").set_index("Session de juin")
    vues = []

    fig, ax = plt.subplots(figsize=(9.3, 4.6))
    _courbe(ax, d["Taux de réussite (%)"].astype(float), BLEU, "Taux de réussite", "%",
            etiquette=lambda a: f"Session de juin {a}")
    _marque(ax, 2002, "arrêtés de nov. 2001 et janv. 2002", 0)
    _marque(ax, 2015, "arrêté de décembre 2014", 0)
    _marque(ax, 2017, "arrêté d'août 2016", 1)
    _habille(ax, "Admis / présentés (%)", 2000, 2023, ymin=0)
    ax.set_ylim(0, 75)
    ax.set_xlabel(figtools.fig_text("Session de juin"), fontsize=8)
    fig.tight_layout()
    vues.append(("Taux de réussite", fig))

    fig, ax = plt.subplots(figsize=(9.3, 4.6))
    _courbe(ax, d["Présentés"].astype(float) / 1000, GRIS, "Présentés", "milliers",
            etiquette=lambda a: f"Session de juin {a}")
    _courbe(ax, d["Admis"].astype(float) / 1000, VERT, "Admis", "milliers",
            etiquette=lambda a: f"Session de juin {a}")
    _habille(ax, "Milliers de candidats", 2000, 2023, ymin=0)
    ax.set_xlabel(figtools.fig_text("Session de juin"), fontsize=8)
    _legende(ax, 2)
    fig.tight_layout()
    vues.append(("Présentés et admis", fig))
    return vues


# --------------------------------------------------------------------------- flux
def vues_flux():
    figtools.apply_lang_font()
    d = lire("fig_educ_scolaire_flux")
    d.index = d["Année scolaire"].str[:4].astype(int)
    etiq = lambda a: f"{a}-{a + 1}"  # noqa: E731
    vues = []

    fig, ax = plt.subplots(figsize=(9.3, 4.6))
    _courbe(ax, pd.to_numeric(d["Abandonnent"]) / 1000, ORANGE, "Abandonnent", "milliers d'élèves",
            etiquette=etiq)
    _courbe(ax, pd.to_numeric(d["Redoublent"]) / 1000, BLEU, "Redoublent", "milliers d'élèves",
            creux=(2014,), mention_creux="347 redoublants, tel qu'imprimé", etiquette=etiq)
    _habille(ax, "Milliers d'élèves", 1984, 2022, ymin=0, pas=3)
    ax.set_xlabel(figtools.fig_text("Année scolaire commençant en"), fontsize=8)
    _legende(ax, 2)
    fig.tight_layout()
    vues.append(("Redoublements et abandons", fig))

    fig, ax = plt.subplots(figsize=(9.3, 4.6))
    ens = pd.to_numeric(d["Ensemble"])
    _courbe(ax, 100 * pd.to_numeric(d["Abandonnent"]) / ens, ORANGE, "Abandonnent", "% des élèves",
            etiquette=etiq)
    _courbe(ax, 100 * pd.to_numeric(d["Redoublent"]) / ens, BLEU, "Redoublent", "% des élèves",
            creux=(2014,), mention_creux="347 redoublants, tel qu'imprimé", etiquette=etiq)
    _habille(ax, "En % des élèves du premier cycle public", 1984, 2022, ymin=0, pas=3)
    ax.set_xlabel(figtools.fig_text("Année scolaire commençant en"), fontsize=8)
    _legende(ax, 2)
    fig.tight_layout()
    vues.append(("En part des élèves", fig))
    return vues

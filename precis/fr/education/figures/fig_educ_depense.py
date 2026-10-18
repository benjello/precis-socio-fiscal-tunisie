"""Figures du chapitre « La dépense d'éducation ».

Les données sont les figdata `figdata/fig_educ_*.csv` du livre : des copies, ligne à ligne,
des séries de la note documentaire (`docs/notes/education-depense-series/`), chaque ligne
avec sa source et sa page. Ces séries ne sont pas encore au catalogue de `tunisia-data` :
le module les lit donc dans le figdata, et ne le réécrit jamais (pas de `write_figdata`).
Le jour où elles seront versées, les figures liront `figtools.series()` et le rendu
réécrira les figdata comme ailleurs.

Règles tenues ici :
  - une rupture de série se montre (trait vertical, segments non reliés), elle ne se
    corrige pas : le développement se trace en deux segments, 1997-2008 et 2009-2023 ;
    la formation professionnelle n'a de points que là où sa ligne existe ;
  - un chiffre provisoire (dernière année d'une édition) porte un marqueur creux ;
  - le PIB est en base 2015 de l'INS, 2010-2014 rétropolés par l'INS (trait pointillé) ;
  - la recherche scientifique n'entre dans aucune part et n'est pas tracée : ses lignes
    sont dans l'onglet « Données », hors total ; depuis 2019, comprise dans la gestion du
    supérieur et non isolable, elle fait de 2019 une coupure des parts (segments non reliés) ;
  - rapports extérieurs et budgétaire superposés seulement avec familles distinguées.
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

BLEU, VERT, ORANGE, VIOLET, GRIS, ROUGE = "#08519c", "#1a7f37", "#b45100", "#6f42c1", "#657487", "#a40e26"


# --------------------------------------------------------------------------- outils
def lire(slug: str) -> pd.DataFrame:
    return pd.read_csv(FIGDATA / f"{slug}.csv", comment="#")


def _provenance(slug: str) -> dict:
    """Clés de citation et réserves, lues dans l'en-tête commenté du figdata (le sidecar
    `.csv.yml` en porte autant, mais en liste YAML non citée, que les « : » rendent
    illisible par un analyseur)."""
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
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _runs(annees: list[int]) -> list[list[int]]:
    """Découpe une liste d'années en suites d'années consécutives."""
    runs: list[list[int]] = []
    for a in sorted(annees):
        if runs and a == runs[-1][-1] + 1:
            runs[-1].append(a)
        else:
            runs.append([a])
    return runs


def _courbe(ax, serie: pd.Series, couleur: str, libelle: str, unite: str, *,
            dec: int = 1, marqueur: str = "o", ls: str = "-", provisoires=(),
            coupures=(), legende: bool = True):
    """Trace une série {année: valeur} par segments d'années consécutives.

    `coupures` : années où la série change de périmètre — le trait ne relie pas
    l'année précédente à celle-ci. `provisoires` : années au marqueur creux.
    """
    serie = serie.dropna().sort_index()
    annees = [int(a) for a in serie.index]
    morceaux = []
    for run in _runs(annees):
        courant = [run[0]]
        for a in run[1:]:
            if a in coupures:
                morceaux.append(courant)
                courant = [a]
            else:
                courant.append(a)
        morceaux.append(courant)
    for i, m in enumerate(morceaux):
        ax.plot(m, [serie[a] for a in m], color=couleur, lw=2, ls=ls,
                label=figtools.fig_text(libelle) if (legende and i == 0) else None)
    for a in annees:
        v = float(serie[a])
        creux = a in provisoires
        (pt,) = ax.plot([a], [v], marker=marqueur, ls="none", ms=5,
                        color=couleur, mfc="white" if creux else couleur, zorder=4)
        mention = " (provisoire)" if creux else ""
        figtools.infobulle(pt, f"{a} · {libelle} : {_nb(v, dec)} {unite}{mention}")


def _habille(ax, ylabel: str, debut: int, fin: int, ymin: float | None = 0, pas: int = 2):
    ax.set_xlim(debut - 0.7, fin + 0.7)
    ax.set_xticks(range(debut, fin + 1, pas))
    if ymin is not None:
        ax.set_ylim(bottom=ymin)
    ax.set_ylabel(figtools.fig_text(ylabel))
    ax.grid(axis="y", color="#d7dce2", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)


def _rupture(ax, annee: int, texte: str, rang: int = 0):
    """Comme `figtools.marque_rupture`, le texte décalé d'un rang vers le bas pour que
    deux ruptures voisines ne se chevauchent pas."""
    x = annee - 0.5
    ax.axvline(x, color="#57606a", ls=(0, (2, 2)), lw=1, zorder=1)
    ax.annotate(figtools.fig_text(texte), xy=(x, 1), xycoords=("data", "axes fraction"),
                xytext=(4, -4 - 11 * rang), textcoords="offset points", ha="left", va="top",
                fontsize=7, color="#57606a")


def _legende(ax, ncol: int = 2):
    ax.legend(frameon=False, fontsize=8, ncol=ncol, loc="upper center",
              bbox_to_anchor=(0.5, -0.12))


def onglets(vues, slug: str, *, caption: str, note_lecture: str, source: str,
            colonnes_cachees=("Source",)) -> None:
    """Sortie en onglets Graphique / Données / Sources, comme `figtools.figure_tabs`,
    mais sans réécrire le figdata : il est la copie sourcée des séries de la note."""
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


# --------------------------------------------------------------------------- F4 parts
def vues_parts():
    figtools.apply_lang_font()
    d = lire("fig_educ_depense_parts").set_index("Année")
    prov = [a for a, s in d["Stade"].items() if str(s).startswith("provisoire")]

    fig1, ax = plt.subplots(figsize=(9.3, 4.6))
    _courbe(ax, d["Part des dépenses de l'État (%)"], BLEU,
            "Part des dépenses de gestion et de développement de l'État (hors dette)", "%",
            dec=2, provisoires=prov, coupures=(2019,))
    _rupture(ax, 2018, "2017 provisoire, 2018 réalisé", 0)
    _rupture(ax, 2019, "recherche comprise dans le supérieur (gestion), non isolable", 1)
    _habille(ax, "Part (%)", 2009, 2023, ymin=0)
    ax.set_ylim(top=float(d["Part des dépenses de l'État (%)"].max()) * 1.2)
    _legende(ax, 1)
    fig1.tight_layout()

    fig2, ax = plt.subplots(figsize=(9.3, 4.6))
    pib = d["Part du PIB (%)"].dropna()
    retro = pib[pib.index <= 2014]
    base = pib[pib.index >= 2014]
    _courbe(ax, retro, ORANGE, "Part du PIB, base 2015, rétropolé par l'INS (2010-2014)", "%",
            dec=2, ls=":", marqueur="s")
    _courbe(ax, base[base.index >= 2015], ORANGE, "Part du PIB, base 2015", "%",
            dec=2, marqueur="s", provisoires=prov, coupures=(2019,))
    ax.plot([2014, 2015], [pib[2014], pib[2015]], color=ORANGE, lw=2, ls=":")
    _rupture(ax, 2018, "2017 provisoire, 2018 réalisé", 0)
    _rupture(ax, 2019, "recherche comprise dans le supérieur (gestion), non isolable", 1)
    _habille(ax, "Part (%)", 2010, 2023, ymin=0)
    ax.set_ylim(top=float(pib.max()) * 1.2)   # place pour le texte des ruptures
    _legende(ax, 2)
    fig2.tight_layout()
    return [("Part des dépenses de l'État", fig1), ("Part du PIB (base 2015)", fig2)]


# --------------------------------------------------------------------------- F5 ministères
# La recherche scientifique n'est pas tracée : ses lignes sont dans l'onglet « Données »,
# hors total (décision du 17 octobre 2026).
MINISTERES = [("Éducation", BLEU), ("Enseignement supérieur", VERT),
              ("Formation professionnelle", ORANGE), ("Emploi", GRIS)]


def _serie_min(d, ministere, titre, colonne):
    s = d[(d["Ministère"] == ministere) & (d["Titre"] == titre)].set_index("Année")
    prov = [a for a, st in s["Stade"].items() if str(st).startswith("provisoire")]
    return s[colonne] / 1000, prov


def vues_ministeres():
    figtools.apply_lang_font()
    d = lire("fig_educ_depense_ministeres")
    vues = []
    for titre, colonne, unite, nom, coupures in (
        ("gestion", "Montant (milliers D courants)", "millions de dinars courants",
         "Gestion, dinars courants", ()),
        ("développement", "Montant (milliers D courants)", "millions de dinars courants",
         "Développement, dinars courants (deux segments)", (2009,)),
        ("gestion", "Montant (milliers D de 2023)", "millions de dinars de 2023",
         "Gestion, dinars de 2023", ()),
    ):
        fig, ax = plt.subplots(figsize=(9.3, 5.0))
        for m, c in MINISTERES:
            s, prov = _serie_min(d, m, titre, colonne)
            if s.empty:
                continue
            _courbe(ax, s, c, m, "MD", dec=1, provisoires=prov, coupures=coupures)
        if titre == "développement":
            _rupture(ax, 2009, "changement de périmètre", 0)
        else:
            _rupture(ax, 2002, "formation dans l'Éducation", 0)
            _rupture(ax, 2009, "formation à part", 1)
            _rupture(ax, 2014, "formation dans l'Emploi", 0)
            _rupture(ax, 2018, "2017 provisoire", 2)
            _rupture(ax, 2019, "recherche dans le supérieur", 1)
            _rupture(ax, 2020, "formation à part", 3)
        _rupture(ax, 2005, "recherche à part", 2)
        _habille(ax, unite.capitalize(), 1997, 2023, ymin=0, pas=2)
        _legende(ax, 3)
        fig.tight_layout()
        vues.append((nom, fig))
    return vues


# --------------------------------------------------------------------------- F6 nature
def vues_nature():
    figtools.apply_lang_font()
    d = lire("fig_educ_depense_nature")
    d = d[pd.to_numeric(d["Part des trois natures (%)"], errors="coerce").notna()]
    d["Part des trois natures (%)"] = d["Part des trois natures (%)"].astype(float)
    vues = []
    for m in ("Éducation", "Enseignement supérieur"):
        fig, ax = plt.subplots(figsize=(9.3, 4.8))
        for nature, libelle, c in (("Rémunérations", "Rémunérations publiques", BLEU),
                                   ("Biens et services", "Moyens des services (« biens et services »)", VERT),
                                   ("Autres dépenses", "Interventions publiques (« autres dépenses »)", ORANGE)):
            s = d[(d["Ministère"] == m) & (d["Nature"] == nature)].set_index("Année")["Part des trois natures (%)"]
            _courbe(ax, s, c, libelle, "%", dec=1)
        if m == "Éducation":
            _rupture(ax, 2011, "formation professionnelle à part", 0)
        else:
            _rupture(ax, 2005, "recherche à part", 0)
        _rupture(ax, 2017, "reclassement possible", 1)
        _habille(ax, "Part de la gestion du ministère (%)", 2003, 2023, ymin=0)
        _legende(ax, 3)
        fig.tight_layout()
        vues.append((m, fig))
    return vues


# --------------------------------------------------------------------------- F7 enseignants
def vues_enseignants():
    figtools.apply_lang_font()
    d = lire("fig_educ_depense_enseignants")
    vues = []
    fig, ax = plt.subplots(figsize=(9.3, 4.8))
    for serie, libelle, c in (
        ("Enseignants du public, premier cycle de l'enseignement de base", "Premier cycle de la base", BLEU),
        ("Enseignants du public, second cycle de la base et secondaire", "Second cycle de la base et secondaire", VERT),
        ("Enseignants du public, enseignement supérieur", "Enseignement supérieur", ORANGE),
    ):
        s = d[d["Série"] == serie].copy()
        s.index = s["Période"].str[:4].astype(int)
        s = s["Valeur"].astype(float) / 1000
        _courbe(ax, s, c, libelle, "milliers d'enseignants", dec=1)
    _habille(ax, "Milliers d'enseignants", 1995, 2023, ymin=0, pas=2)
    ax.set_xlabel(figtools.fig_text("Année scolaire commençant en"), fontsize=8)
    _legende(ax, 3)
    fig.tight_layout()
    vues.append(("Effectifs", fig))

    for colonne, unite, nom in (("Valeur", "millions de dinars courants", "Rémunérations, dinars courants"),
                                ("Valeur en milliers D de 2023", "millions de dinars de 2023",
                                 "Rémunérations, dinars de 2023")):
        fig, ax = plt.subplots(figsize=(9.3, 4.8))
        for serie, libelle, c in (("Rémunérations, ministère de l'Éducation", "Ministère de l'Éducation", BLEU),
                                  ("Rémunérations, ministère de l'Enseignement supérieur",
                                   "Ministère de l'Enseignement supérieur", VERT)):
            s = d[d["Série"] == serie].copy()
            s.index = s["Période"].astype(int)
            s = pd.to_numeric(s[colonne]) / 1000
            _courbe(ax, s, c, libelle, "MD", dec=1, provisoires=list(s.index))
        _rupture(ax, 2005, "recherche hors du supérieur", 0)
        _habille(ax, unite.capitalize(), 2001, 2023, ymin=0)
        _legende(ax, 2)
        fig.tight_layout()
        vues.append((nom, fig))

    # rémunération par agent du ministère : tableau 16.9 ÷ agents de la fonction publique du
    # ministère (INS, base INSAF), calculée dans le figdata ; seulement les années où les deux
    # existent, sans interpolation ; Éducation 2010 exclue (formation professionnelle comprise)
    for colonne, unite, nom in (("Valeur", "milliers de dinars courants par agent",
                                 "Par agent du ministère, dinars courants"),
                                ("Valeur en milliers D de 2023", "milliers de dinars de 2023 par agent",
                                 "Par agent du ministère, dinars de 2023")):
        fig, ax = plt.subplots(figsize=(9.3, 4.8))
        for serie, libelle, c in (("Rémunération par agent, ministère de l'Éducation",
                                   "Ministère de l'Éducation", BLEU),
                                  ("Rémunération par agent, ministère de l'Enseignement supérieur",
                                   "Ministère de l'Enseignement supérieur", VERT)):
            r = d[d["Série"] == serie].copy()
            r.index = r["Période"].astype(int)
            r = pd.to_numeric(r[colonne])  # milliers de D par agent
            _courbe(ax, r, c, libelle, "milliers de D par agent", dec=1, provisoires=list(r.index))
        _rupture(ax, 2019, "recherche dans le supérieur, part non établie", 0)
        _habille(ax, unite.capitalize(), 2010, 2023, ymin=0, pas=1)
        ax.set_ylim(top=float(pd.to_numeric(d.loc[d["Série"].str.startswith("Rémunération par agent"),
                                                   colonne]).max()) * 1.15)   # place pour la rupture
        _legende(ax, 2)
        fig.tight_layout()
        vues.append((nom, fig))
    return vues


# --------------------------------------------------------------------------- F8 UIS
def vues_uis():
    figtools.apply_lang_font()
    d = lire("fig_educ_depense_uis")
    def s(indic):
        x = d[d["Indicateur"] == indic].set_index("Année")["Valeur"].astype(float)
        return x
    vues = []
    for uis, budg, nom, debut in (
        ("SE.XPD.TOTL.GD.ZS", "part du PIB (base 2015)", "Part du PIB", 1980),
        ("SE.XPD.TOTL.GB.ZS", "part des dépenses de l'État", "Part des dépenses publiques", 1992),
    ):
        fig, ax = plt.subplots(figsize=(9.3, 4.8))
        _courbe(ax, s(uis), GRIS, f"UNESCO-UIS (rapport extérieur), {uis}", "%", dec=2, marqueur="D")
        lib = ("Budgétaire : Éducation et Enseignement supérieur, hors recherche, PIB base 2015 "
               "(2010-2014 rétropolés par l'INS)"
               if "PIB" in budg else
               "Budgétaire : Éducation et Enseignement supérieur, hors recherche, part des dépenses "
               "de l'État hors dette")
        _courbe(ax, s(budg), BLEU, lib, "%", dec=2, coupures=(2019,))
        _habille(ax, "Part (%)", debut, 2025, ymin=0, pas=5 if debut < 1990 else 3)
        _legende(ax, 1)
        fig.tight_layout()
        vues.append((nom, fig))
    fig, ax = plt.subplots(figsize=(9.3, 4.8))
    for indic, libelle, c in (("SE.XPD.PRIM.PC.ZS", "Par élève du primaire", BLEU),
                              ("SE.XPD.SECO.PC.ZS", "Par élève du secondaire", VERT),
                              ("SE.XPD.TERT.PC.ZS", "Par étudiant du supérieur", ORANGE)):
        _courbe(ax, s(indic), c, f"{libelle} ({indic})", "% du PIB par habitant", dec=1)
    _habille(ax, "% du PIB par habitant", 1997, 2015, ymin=0)
    _legende(ax, 3)
    fig.tight_layout()
    vues.append(("Par élève, en part du PIB par habitant", fig))
    return vues

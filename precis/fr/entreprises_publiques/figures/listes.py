"""Figure et tableaux de l'annexe « La liste des entreprises publiques » (volume « Les
entreprises publiques »).

    from figures import listes as ls
    ls.figure(caption=…, note_lecture=…)          # le périmètre en nombre, 1997-2021
    ls.tableau_ensemble(caption=…)                # une ligne par entreprise, cinq listes
    ls.tableau_etablissements(caption=…)          # les établissements, six états de la liste

D'OÙ VIENNENT LES DONNÉES. De deux relevés versionnés DANS le livre (`listes/*.csv`, chacun
avec son manifeste `.csv.yml`) : ils transcrivent des listes fixées par décret et le tableau
nominatif d'un rapport du ministère des Finances. Ce n'est pas une statistique de l'entrepôt :
la figure les lit directement, comme `fiscalite/figures/regimes_incitation.py` lit les siens.

RÈGLES.

  - **Trois sources, aucun raccord.** Le tableau de tutelle (décrets de 1998, 2002 et 2005, et
    son état de fin 2010), la liste des établissements (1997-2007) et le recensement du
    ministère pour 2021 ont chacun leur couleur ; aucun trait ne va de l'un à l'autre.
  - **L'état de fin 2010 est une marque creuse** : il est obtenu en appliquant au tableau de
    2005 les lignes que les décrets suivants réécrivent ; une ligne qu'aucun décret ne réécrit
    est tenue pour inchangée.
  - **Les nombres sont comptés sur les listes** : aucun des textes ne publie de décompte.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

RELEVES = Path(__file__).resolve().parent.parent / "listes"
ENSEMBLE = "entreprises-publiques-listes"
ETABLISSEMENTS = "etablissements-entreprises-publiques"

BLEU, ORANGE, VERT, GRIS = "#0969da", "#bc4c00", "#1a7f37", "#57606a"
# Année de la liste -> libellé de colonne
LISTES = {"1998": "1998", "2002": "2002", "2005": "2005", "2010": "fin 2010", "2021": "2021"}
ETATS = {"1997": "1997", "1998": "1998", "1999": "1999", "2002": "2002", "2004": "2004",
         "2007": "octobre 2007"}


def _lire(nom: str) -> pd.DataFrame:
    return pd.read_csv(RELEVES / f"{nom}.csv", dtype=str, keep_default_na=False)


def _sources(nom: str) -> list[str]:
    import yaml
    manifeste = yaml.safe_load((RELEVES / f"{nom}.csv.yml").read_text(encoding="utf-8"))
    return list(manifeste["sources"])


figtools.register_provenance(
    ENSEMBLE, titre="Entreprises publiques nommées par les décrets de tutelle et par le "
                    "rapport du ministère des Finances, 1998-2021",
    sources=_sources(ENSEMBLE), unite="entreprises",
    perimetre=("colonne des entreprises publiques du tableau qui désigne le ministère de "
               "tutelle — décrets de 1998, 2002 et 2005, et état du tableau de 2005 après ses "
               "modifications, fin 2010 — ; tableau nominatif du rapport sur les entreprises "
               "publiques annexé au projet de loi de finances pour 2021"),
    caveats=("Nombres comptés sur les listes, qui ne publient aucun décompte. L'état de fin "
             "2010 tient pour inchangée toute ligne qu'aucun décret ne réécrit après 2005. Le "
             "rapport pour 2021 est un recensement du ministère, non une liste fixée par "
             "décret : il se compare aux décrets sans s'y raccorder. Une entreprise absente "
             "d'une liste et présente dans la précédente est sortie du périmètre entre les "
             "deux dates ; ni la date ni le mode de la sortie ne sont donnés."))
figtools.register_provenance(
    ETABLISSEMENTS, titre="Établissements publics à caractère non administratif considérés "
                          "comme entreprises publiques, 1997-2007",
    sources=_sources(ETABLISSEMENTS), unite="établissements",
    perimetre=("liste fixée par décret en 1997, refaite en 1999, 2002 et 2004, complétée en "
               "1998 et modifiée en 2006 et 2007"),
    caveats=("Après octobre 2007, aucun décret ne modifie la liste : un établissement y entre "
             "par une disposition de son propre décret, et ces entrées ne sont pas comptées "
             "ici."))


def comptes() -> dict[str, dict[str, int]]:
    """Nombres comptés sur les relevés : {"ensemble": {liste: n}, "etablissements": {…}}."""
    e = _lire(ENSEMBLE)
    e = e[e["presente"] == "oui"]
    a = _lire(ETABLISSEMENTS)
    a = a[a["present"] == "oui"]
    return {"ensemble": {k: int(e[e["liste"] == k]["nombre"].astype(int).sum()) for k in LISTES},
            "etablissements": {k: int((a["liste"] == k).sum()) for k in ETATS}}


def fig_perimetre():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    c = comptes()
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    # 1. Tableau de tutelle : trois décrets, puis l'état de fin 2010 (marque creuse).
    decrets = [(1998, c["ensemble"]["1998"]), (2002, c["ensemble"]["2002"]),
               (2005, c["ensemble"]["2005"])]
    ax.plot([a for a, _ in decrets], [n for _, n in decrets], "-", color=BLEU, lw=1.8, zorder=2)
    ax.plot([2005, 2010], [c["ensemble"]["2005"], c["ensemble"]["2010"]], ":", color=BLEU,
            lw=1.4, zorder=2)
    for a, n in decrets:
        p, = ax.plot([a], [n], "o", color=BLEU, ms=6, zorder=3)
        figtools.infobulle(p, f"{a} · décret désignant le ministère de tutelle : {n} "
                              "entreprises publiques")
    p, = ax.plot([2010], [c["ensemble"]["2010"]], "o", color=BLEU, mfc="white", ms=6, zorder=3)
    figtools.infobulle(p, f"fin 2010 · tableau de 2005 après ses modifications : "
                          f"{c['ensemble']['2010']} entreprises publiques")
    # 2. Recensement du ministère des Finances : marque isolée.
    p, = ax.plot([2021], [c["ensemble"]["2021"]], "D", color=ORANGE, ms=6, zorder=3)
    figtools.infobulle(p, f"rapport annexé au projet de loi de finances pour 2021 : "
                          f"{c['ensemble']['2021']} entreprises publiques")
    # 3. Liste des établissements : marches, 1997-2007.
    etats = [(1997, "1997"), (1998, "1998"), (1999, "1999"), (2002, "2002"), (2004, "2004"),
             (2007, "2007")]
    xs = [a for a, _ in etats]
    ys = [c["etablissements"][k] for _, k in etats]
    ax.step(xs, ys, where="post", color=VERT, lw=1.8, zorder=2)
    for a, n in zip(xs, ys):
        p, = ax.plot([a], [n], "s", color=VERT, ms=5, zorder=3)
        figtools.infobulle(p, f"{a} · liste des établissements publics considérés comme "
                              f"entreprises publiques : {n}")
    for a, n in decrets + [(2010, c["ensemble"]["2010"]), (2021, c["ensemble"]["2021"])]:
        ax.annotate(str(n), xy=(a, n), xytext=(0, 7), textcoords="offset points", ha="center",
                    fontsize=8)
    for a, n in ((1997, ys[0]), (2007, ys[-1])):
        ax.annotate(str(n), xy=(a, n), xytext=(0, 7), textcoords="offset points", ha="center",
                    fontsize=8)
    ax.set_ylim(0, 140)
    ax.set_xlim(1996, 2022)
    ax.set_xticks([1997, 1998, 1999, 2002, 2004, 2005, 2007, 2010, 2021])
    ax.tick_params(axis="x", labelsize=8)
    ax.set_ylabel(ft("Nombre d'entreprises ou d'établissements"))
    ax.set_xlabel(ft("Année de la liste"))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.set_axisbelow(True)
    for cote in ("top", "right"):
        ax.spines[cote].set_visible(False)
    ax.legend(handles=[
        Line2D([], [], color=BLEU, marker="o", lw=1.8, ms=6,
               label=ft("entreprises publiques au tableau de tutelle (décrets de 1998, 2002, 2005)")),
        Line2D([], [], color=BLEU, marker="o", mfc="white", ls=":", lw=1.4, ms=6,
               label=ft("le même tableau après ses modifications, fin 2010")),
        Line2D([], [], color=ORANGE, marker="D", ls="", ms=6,
               label=ft("entreprises publiques recensées par le ministère des Finances (2021)")),
        Line2D([], [], color=VERT, marker="s", lw=1.8, ms=5,
               label=ft("dont établissements publics inscrits sur la liste fixée par décret")),
    ], loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=1, fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig


def table_perimetre() -> pd.DataFrame:
    c = comptes()
    lignes = [{"Liste": "Tableau de tutelle" + (", après modifications" if k == "2010" else ""),
               "Année": LISTES[k], "Nombre": c["ensemble"][k]} for k in ("1998", "2002", "2005", "2010")]
    lignes.append({"Liste": "Rapport du ministère des Finances", "Année": "2021",
                   "Nombre": c["ensemble"]["2021"]})
    lignes += [{"Liste": "Établissements publics considérés comme entreprises publiques",
                "Année": ETATS[k], "Nombre": c["etablissements"][k]} for k in ETATS]
    return pd.DataFrame(lignes)


def figure(caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure du périmètre en onglets (chunk `output: asis`, étiqueté `fig-…`)."""
    figtools.figure_tabs(fig_perimetre(), table_perimetre(), ENSEMBLE, ETABLISSEMENTS,
                         slug="fig_ep_liste_perimetre", caption=caption,
                         note_lecture=note_lecture, nominal=False)
    plt.close("all")


def _md(entete: list[str], lignes: list[list[str]], caption: str, tbl_id: str) -> None:
    out = ["| " + " | ".join(entete) + " |",
           "|---|" + "|".join(":-:" for _ in entete[1:]) + "|"]
    out += ["| " + " | ".join(l) + " |" for l in lignes]
    print("\n".join(out) + f"\n\n: {caption} {{#{tbl_id}}}\n")


def tableau_ensemble(caption: str, tbl_id: str = "tbl-ep-liste-ensemble") -> None:
    """Une ligne par entreprise, groupée par ministère de tutelle ; « É » : établissement
    public inscrit sur la liste à cette date ; le nombre entre parenthèses compte les sociétés
    réunies sur une ligne."""
    d = _lire(ENSEMBLE)
    lignes = []
    tutelle = None
    for rang, g in d.groupby(d["rang"].astype(int), sort=True):
        if g["tutelle"].iloc[0] != tutelle:
            tutelle = g["tutelle"].iloc[0]
            lignes.append([f"**{tutelle}**"] + [""] * len(LISTES))
        cellules = []
        for k in LISTES:
            r = g[g["liste"] == k].iloc[0]
            if r["presente"] != "oui":
                cellules.append("—")
                continue
            c = "É" if r["etablissement_public"] == "oui" else "✓"
            if int(r["nombre"]) > 1:
                c += f" ({r['nombre']})"
            cellules.append(c)
        lignes.append([g["entreprise"].iloc[0]] + cellules)
    c = comptes()["ensemble"]
    lignes.append(["**Total**"] + [f"**{c[k]}**" for k in LISTES])
    _md(["Entreprise"] + list(LISTES.values()), lignes, caption, tbl_id)


def tableau_etablissements(caption: str, tbl_id: str = "tbl-ep-liste-etablissements") -> None:
    d = _lire(ETABLISSEMENTS)
    lignes = []
    for rang, g in d.groupby(d["rang"].astype(int), sort=True):
        cellules = ["✓" if g[g["liste"] == k].iloc[0]["present"] == "oui" else "—" for k in ETATS]
        lignes.append([g["etablissement"].iloc[0]] + cellules)
    c = comptes()["etablissements"]
    lignes.append(["**Total**"] + [f"**{c[k]}**" for k in ETATS])
    _md(["Établissement"] + list(ETATS.values()), lignes, caption, tbl_id)

"""Figures des crédits votés et des comptes du FOPRODI (chapitre « Les régimes d'incitation »).

    from figures import credits_incitations as fig_ci
    fig_ci.figure("foprodi", caption=…, note_lecture=…)
    fig_ci.figure("autres", caption=…, note_lecture=…)

D'OÙ VIENNENT LES DONNÉES. Trois séries de `tunisia-data`, lues par `figtools.series()` — donc
depuis le snapshot `precis/_seriescache/` quand l'entrepôt est absent :

  - `jort-lf-credits-programmes-incitations` : crédits de programmes votés par les lois de
    finances initiales, 1995-2019, quatre lignes, avec la part des dépenses de l'État et la
    part du PIB calculées par l'entrepôt ;
  - `bct-foprodi-fonapra` : compte du FOPRODI tenu par la Banque centrale, exercices
    2016-2025 (dotations budgétaires reçues, emplois) ;
  - `denominateurs-depenses-etat-pib` : dépenses de l'État hors service de la dette
    (réalisations) et PIB retenu, pour rapporter le compte de la Banque centrale.

RÈGLES.

  - **Trois grandeurs, aucun raccord.** Crédit voté, dotation reçue et emplois du fonds ont
    chacun leur couleur et leur marque ; aucun trait ne va de l'une à l'autre.
  - **La part du PIB se trace par segments** : le trait s'interrompt à chaque changement de
    source ou de base du PIB, un trait vertical le marque, la base est écrite au-dessus du
    cadre. Rien n'est chaîné.
  - **Numérateur voté, dénominateur réalisé** pour les crédits : la part est un ordre de
    grandeur.

Les libellés sont en français ; les libellés arabes restent à verser.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

CREDITS = "jort-lf-credits-programmes-incitations"
BCT = "bct-foprodi-fonapra"
DENOMINATEURS = "denominateurs-depenses-etat-pib"

BLEU, ORANGE, VERT, GRIS, VIOLET = "#0969da", "#bc4c00", "#1a7f37", "#57606a", "#8250df"

VUES = (("md", "En millions de dinars"), ("dep", "En % des dépenses de l'État"),
        ("pib", "En % du PIB"))
YLABEL = {"md": "Millions de dinars courants",
          "dep": "En % des dépenses de l'État\nhors service de la dette",
          "pib": "En % du PIB"}
UNITE = {"md": " MD", "dep": " % des dépenses de l'État", "pib": " % du PIB"}
COLONNE = {"md": "valeur_md", "dep": "part_depenses_etat_pct", "pib": "part_pib_pct"}
DECIMALES = {"md": 1, "dep": 3, "pib": 3}

PROVENANCE = {
    CREDITS: dict(
        perimetre=("lois de finances initiales pour 1995 à 2019, tableau des crédits de "
                   "programmes de l'État : Fonds de promotion et de décentralisation "
                   "industrielle (1999-2019), prise en charge par l'État de la contribution "
                   "patronale au régime légal de sécurité sociale (1995-2019), aide de l'État "
                   "aux promoteurs de projets touristiques (2010-2019), Fonds national de "
                   "promotion de l'artisanat et des petits métiers (2012-2019)"),
        caveats=("Crédits de programmes votés, ni crédits de paiement ni sommes versées. Le "
                 "chapitre de l'industrie ne porte pas de ligne du fonds de 1995 à 1998. La "
                 "ligne de la prise en charge change de rubrique en 1998 au plus tard, en 2012 "
                 "et en 2015. Le tableau disparaît de la loi de finances en 2020. Le crédit "
                 "voté est rapporté à des dépenses réalisées et au PIB de l'année : les parts "
                 "sont des ordres de grandeur.")),
    BCT: dict(
        perimetre=("Banque centrale de Tunisie, rapport annuel, états financiers, note sur les "
                   "comptes du Gouvernement : dotations budgétaires reçues et emplois du Fonds "
                   "de promotion et de décentralisation industrielle, exercices 2016 à 2025"),
        caveats=("Relevé comptable du compte que la Banque tient pour l'État, non un "
                 "recensement par avantage. Les emplois comptent tout ce que paie le fonds : "
                 "primes, prises en charge, dotations remboursables et participations. Aucune "
                 "série n'est établie avant 2016.")),
    DENOMINATEURS: dict(
        perimetre=("dépenses de l'État hors service de la dette, réalisées, d'après le "
                   "ministère des Finances ; PIB de l'année, par segments de source et de base"),
        caveats=("Le PIB n'est pas chaîné : base 1983 jusqu'en 1996, base 1997 de 1997 à 2001 "
                 "et de 2005 à 2009, valeur propre au ministère des Finances, rattachée à "
                 "aucune base, de 2002 à 2004 et en 2025, base 2015 de l'INS de 2010 à 2024, "
                 "rétropolée pour 2010-2014.")),
}


def _declarer(series_id: str) -> None:
    """Provenance montrée au lecteur : clés présentes dans la bibliographie du livre,
    périmètre et réserves réécrits pour lui."""
    origine = dict(figtools.meta(series_id))
    connues = figtools._ref_index()
    champs = {k: v for k, v in origine.items() if k != "id" and not k.endswith("_ar")}
    champs["sources"] = [k for k in origine.get("sources", []) if k in connues]
    champs.update(PROVENANCE[series_id])
    figtools.register_provenance(series_id, **champs)


def _nb(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _credits(ligne: str) -> pd.DataFrame:
    d = figtools.series(CREDITS)
    return d[d["ligne"] == ligne].sort_values("annee").reset_index(drop=True)


def _denominateurs() -> pd.DataFrame:
    return figtools.series(DENOMINATEURS).set_index("annee")


def _compte_foprodi(poste: str) -> pd.DataFrame:
    """Un poste du compte du FOPRODI à la Banque centrale, rapporté aux dénominateurs."""
    d = figtools.series(BCT)
    d = d[(d["fonds"] == "FOPRODI") & (d["poste"] == poste)
          & (d["derniere_edition"].astype(str).str.lower() == "true")]
    den = _denominateurs()
    out = pd.DataFrame({"annee": d["exercice"].astype(int), "valeur_md": d["valeur_md"],
                        "page": "", "note": ""}).sort_values("annee").reset_index(drop=True)
    out["depenses_etat_hors_dette_MDT"] = out["annee"].map(den["depenses_etat_hors_dette_MDT"])
    out["pib_MDT"] = out["annee"].map(den["pib_MDT"])
    out["segment_pib"] = out["annee"].map(den["segment_pib"])
    out["base_pib"] = out["annee"].map(den["base_pib"])
    out["pib_retropole"] = out["annee"].map(den["pib_retropole"])
    out["part_depenses_etat_pct"] = (out["valeur_md"] / out["depenses_etat_hors_dette_MDT"]
                                     * 100).round(3)
    out["part_pib_pct"] = (out["valeur_md"] / out["pib_MDT"] * 100).round(3)
    return out


def _morceaux(d: pd.DataFrame, mesure: str):
    """Suites d'années consécutives ; en part du PIB, coupées à chaque changement de segment."""
    courant: list = []
    for r in d.itertuples():
        suite = courant and r.annee == courant[-1].annee + 1 and (
            mesure != "pib" or r.segment_pib == courant[-1].segment_pib)
        if courant and not suite:
            yield courant
            courant = []
        courant.append(r)
    if courant:
        yield courant


def _trace(ax, d: pd.DataFrame, mesure: str, couleur: str, marque: str, libelle: str,
           creux=()):
    col = COLONNE[mesure]
    for morceau in _morceaux(d, mesure):
        ax.plot([r.annee for r in morceau], [getattr(r, col) for r in morceau], "-",
                color=couleur, lw=1.7, zorder=2)
    for r in d.itertuples():
        v = getattr(r, col)
        point, = ax.plot([r.annee], [v], marque, color=couleur, ms=5, zorder=3,
                         mfc="white" if r.annee in creux else couleur)
        texte = f"{r.annee} · {libelle} : {_nb(r.valeur_md, 3 if r.valeur_md % 0.1 else 1)} MD"
        if mesure != "md":
            texte += f", soit {_nb(v, 3)}{UNITE[mesure]}"
        if r.page:
            texte += f" (loi de finances, p. {r.page})"
        if r.note:
            texte += f" — {r.note}"
        figtools.infobulle(point, texte)
    return Line2D([], [], color=couleur, marker=marque, lw=1.7, ms=5,
                  label=figtools.fig_text(libelle))


def _bases_du_pib(ax, x0: int, x1: int) -> None:
    """Trait à chaque changement de segment du PIB, base de chaque segment au-dessus du cadre."""
    den = _denominateurs().loc[x0:x1]
    segments: list[list] = []
    for annee, r in den.iterrows():
        if segments and segments[-1][2] == r["segment_pib"]:
            segments[-1][1] = annee
        else:
            segments.append([annee, annee, r["segment_pib"]])
    for i, (a0, a1, segment) in enumerate(segments):
        if i:
            trait = figtools.marque_rupture(ax, a0)
            rupture = den.loc[a0, "rupture_pib"]
            if isinstance(rupture, str) and rupture:
                figtools.infobulle(trait, f"{a0} · PIB : {rupture}")
        m = re.search(r"\((.*)\)", str(segment))
        base = m.group(1) if m else str(segment)
        if base.startswith("non rattach"):
            base = "n. r."
        retro = den.loc[a0:a1]
        retro = sorted(retro[retro["pib_retropole"] == "oui"].index)
        if retro:
            base += f"\nrétropolée {retro[0]}-{retro[-1]}"
        ax.annotate(figtools.fig_text(base), xy=((a0 + a1) / 2, 1),
                    xycoords=("data", "axes fraction"), xytext=(0, 5),
                    textcoords="offset points", ha="center", va="bottom", fontsize=6.5,
                    color=GRIS, annotation_clip=False)
    ax.annotate(figtools.fig_text("PIB :"), xy=(0, 1), xycoords="axes fraction",
                xytext=(-6, 5), textcoords="offset points", ha="right", va="bottom",
                fontsize=6.5, color=GRIS, annotation_clip=False)


def _habille(ax, fig, mesure: str, poignees, x0: int, x1: int, ncol: int = 1) -> None:
    ax.set_ylabel(figtools.fig_text(YLABEL[mesure]))
    ax.set_xlabel(figtools.fig_text("Année"))
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    ax.set_xlim(x0 - 0.7, x1 + 0.7)
    ax.set_xticks(list(range(x0 + (x0 % 2), x1 + 1, 2)))
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_formatter(
        FuncFormatter(lambda v, _: _nb(v, 0 if mesure == "md" else 2)))
    if mesure == "pib":
        _bases_du_pib(ax, x0, x1)
        poignees = poignees + [Line2D([], [], color="none", label=figtools.fig_text(
            "au-dessus du cadre : base du PIB de chaque segment ; « n. r. » : valeur propre "
            "au ministère des Finances, rattachée à aucune base"))]
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=ncol,
              fontsize=7.5, frameon=False)
    fig.tight_layout()


# --- 1. Le FOPRODI : crédit voté, dotation reçue, emplois ----------------------------------

SERIES_FOPRODI = (
    ("credit", BLEU, "o", "loi de finances : crédit de programmes voté"),
    ("dotations_budgetaires", VERT, "s", "Banque centrale : dotation budgétaire reçue par le fonds"),
    ("emplois", ORANGE, "D", "Banque centrale : emplois du fonds"),
)


def _serie_foprodi(cle: str) -> pd.DataFrame:
    return _credits("foprodi") if cle == "credit" else _compte_foprodi(cle)


def fig_foprodi(mesure: str = "md"):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 4.9))
    poignees = [_trace(ax, _serie_foprodi(cle), mesure, couleur, marque, libelle)
                for cle, couleur, marque, libelle in SERIES_FOPRODI]
    _habille(ax, fig, mesure, poignees, 1999, 2025)
    return fig


# --- 2. Les trois autres lignes de crédits de programmes -----------------------------------

SERIES_AUTRES = (
    ("prise_en_charge_patronale", VIOLET, "o",
     "prise en charge de la contribution patronale de sécurité sociale"),
    ("fonapra", VERT, "^", "Fonds national de promotion de l'artisanat et des petits métiers"),
    ("aide_promoteurs_touristiques", ORANGE, "s",
     "aide de l'État aux promoteurs de projets touristiques"),
)
RUBRIQUES = (1998, 2012, 2015)  # la ligne de la prise en charge change de rubrique


def fig_autres(mesure: str = "md"):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 4.9))
    poignees = [_trace(ax, _credits(cle), mesure, couleur, marque, libelle,
                       creux=RUBRIQUES if cle == "prise_en_charge_patronale" else ())
                for cle, couleur, marque, libelle in SERIES_AUTRES]
    poignees.append(Line2D([], [], color=VIOLET, marker="o", mfc="white", ls="", ms=5,
                           label=figtools.fig_text(
                               "marque creuse : la ligne change de rubrique dans le tableau")))
    _habille(ax, fig, mesure, poignees, 1995, 2019)
    return fig


# --- tables de l'onglet « Données » --------------------------------------------------------

def _table(series) -> pd.DataFrame:
    lignes = []
    for libelle, source, d in series:
        for r in d.itertuples():
            lignes.append({
                "Année": r.annee, "Grandeur": libelle, "Source": source,
                "Millions de dinars": r.valeur_md,
                "Dépenses de l'État hors service de la dette, réalisées (millions de dinars)":
                    r.depenses_etat_hors_dette_MDT,
                "En % des dépenses de l'État": r.part_depenses_etat_pct,
                "PIB (millions de dinars)": r.pib_MDT, "En % du PIB": r.part_pib_pct,
                "Base du PIB": r.base_pib, "PIB rétropolé": r.pib_retropole,
                "Page de la loi de finances": r.page, "Note": r.note})
    return pd.DataFrame(lignes).sort_values(["Grandeur", "Année"]).reset_index(drop=True)


def _figure_foprodi():
    table = _table([(libelle.split(" : ")[1], libelle.split(" : ")[0], _serie_foprodi(cle))
                    for cle, _, _, libelle in SERIES_FOPRODI])
    vues = [(titre, fig_foprodi(mesure)) for mesure, titre in VUES]
    return vues, table, (CREDITS, BCT, DENOMINATEURS), "fig_ri_foprodi_credits_comptes"


def _figure_autres():
    table = _table([(libelle, "loi de finances", _credits(cle))
                    for cle, _, _, libelle in SERIES_AUTRES])
    vues = [(titre, fig_autres(mesure)) for mesure, titre in VUES]
    return vues, table, (CREDITS, DENOMINATEURS), "fig_ri_credits_programmes"


FIGURES = {"foprodi": _figure_foprodi, "autres": _figure_autres}


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure `nom` en onglets. À appeler dans un chunk `#| label: fig-…`, `asis`."""
    vues, table, series, slug = FIGURES[nom]()
    for sid in series:
        _declarer(sid)
    figtools.figure_tabs(vues, table, *series, slug=slug, caption=caption,
                         note_lecture=note_lecture)
    plt.close("all")


def reperes() -> dict:
    """Valeurs que le chapitre cite : à relire quand une série change."""
    out = {cle: _credits(cle).set_index("annee")[["valeur_md", "part_depenses_etat_pct",
                                                 "part_pib_pct"]]
           for cle in ("foprodi", "prise_en_charge_patronale", "aide_promoteurs_touristiques",
                       "fonapra")}
    for poste in ("dotations_budgetaires", "emplois"):
        out[poste] = _compte_foprodi(poste).set_index("annee")[
            ["valeur_md", "part_depenses_etat_pct", "part_pib_pct"]]
    return out

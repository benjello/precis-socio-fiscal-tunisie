"""Figure « les dépenses fiscales par exercice et par impôt, rapport par rapport ».

BUDGÉTAIRE, RIEN D'AUTRE : les montants sont ceux des rapports sur les dépenses fiscales
annexés aux projets de loi de finances pour 2021 à 2025. Aucune étude extérieure n'y entre.

UNE LECTURE PAR RAPPORT, AUCUN CHAÎNAGE. Les rapports se chevauchent et se révisent :
l'exercice 2020 vaut 4 225 MD en tête du rapport pour 2022 et 4 795,5 MD dans le rapport
pour 2024 ; l'exercice 2021, 7 745 MD en tête du rapport pour 2023 et 5 872 MD dans les
deux suivants ; l'exercice 2022, 6 360,6 MD dans le rapport pour 2024 et 6 169,8 MD dans
le rapport pour 2025. Leur périmètre change aussi : les rapports pour 2024 et 2025 donnent
leurs montants sans les dépenses fiscales liées à l'exonération des médicaments et des
engrais, que le rapport pour 2021 compte. La figure trace donc un GROUPE DE BARRES PAR
RAPPORT, séparés, chacun avec son périmètre ; un même exercice y paraît autant de fois
qu'il est publié. Rien n'est raccordé d'un groupe à l'autre.

D'OÙ VIENNENT LES DONNÉES.
  - La répartition par impôt : série `depenses-fiscales-detail` de l'entrepôt (rapports
    pour 2021, 2024 et 2025), sommée par impôt sur les dispositifs chiffrés.
  - Les rapports pour 2022 et 2023 : seul leur total d'introduction est relevé
    (`incitations/depenses-fiscales-agregats-rapports.csv`, versionné dans le livre) ;
    leur barre est un contour, sans répartition.
  - Les dénominateurs, CALCULÉS ICI et non repris des rapports : recettes fiscales de
    l'État (`recettes-fiscales-composition`, ministère des Finances) et PIB de l'année —
    celui que porte `compensation-parts`, comme les figures du volume « Compensation » :
    PIB de l'INS en base 2015, non rétropolé de 2016 à 2024, un seul segment ici.
    Les ratios que chaque rapport imprime pour son exercice de tête sont montrés à côté
    (losanges) : ils ne coïncident pas toujours avec le calcul, le rapport ne disant pas
    son dénominateur.
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

HERE = Path(__file__).resolve().parent
AGREGATS = HERE.parent / "incitations" / "depenses-fiscales-agregats-rapports.csv"
DETAIL = "depenses-fiscales-detail"
RECETTES = "recettes-fiscales-composition"
PIB = "compensation-parts"
SERIE = "depenses-fiscales-par-rapport"

GRIS = "#57606a"
IMPOTS = [("consommation", "Droit de consommation", "#bc4c00"),
          ("tva", "Taxe sur la valeur ajoutée", "#0969da"),
          ("douanes", "Droits de douane", "#1a7f37"),
          ("is", "Impôt sur les sociétés", "#8250df"),
          ("irpp", "Impôt sur le revenu", "#bf8700")]
# Rapport (année du projet de loi de finances) -> périmètre, tel que le chapitre l'établit.
PERIMETRE = {2021: "médicaments et engrais comptés",
             2022: "total d'introduction ; périmètre non établi",
             2023: "total d'introduction ; périmètre non établi",
             2024: "hors médicaments et engrais",
             2025: "hors médicaments et engrais"}
MESURES = {"md": ("En millions de dinars courants", 0, " MD"),
           "rec": ("En % des recettes fiscales de l'État (calculé ici)", 1, " %"),
           "pib": ("En % du PIB (calculé ici)", 2, " % du PIB")}

figtools.register_provenance(
    SERIE,
    titre="Dépenses fiscales par exercice et par impôt, rapport par rapport, exercices 2017-2023",
    sources=["gbo-depenses-fiscales", "minfin-depenses-fiscales-plf2022",
             "minfin-depenses-fiscales-plf2023", "minfin-recettes-fiscales", "ins-cnat-2015"],
    unite="millions de dinars courants ; % des recettes fiscales de l'État ; % du PIB",
    perimetre=("dépenses fiscales chiffrées de cinq impôts de l'État, d'après les rapports "
               "annexés aux projets de loi de finances pour 2021 à 2025 ; recettes fiscales : "
               "ministère des Finances ; PIB : INS, base 2015, non rétropolé"),
    caveats=("Une lecture par rapport, sans chaînage : les rapports se révisent et n'ont pas le "
             "même périmètre (médicaments et engrais exclus à partir du rapport pour 2024). Les "
             "rapports pour 2022 et 2023 ne sont connus que par leur total d'introduction. Les "
             "parts sont calculées ici ; celles qu'imprime chaque rapport, sans dire son "
             "dénominateur, sont données à côté."))


def _nb(v, dec=0) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _donnees() -> pd.DataFrame:
    """Une ligne par (rapport, exercice) : montants par impôt, total, dénominateurs, parts."""
    d = figtools.series(DETAIL)
    d = d[d["montant_MDT"].notna()]
    g = (d.groupby(["rapport", "annee", "impot"])["montant_MDT"].sum().unstack("impot")
         .reset_index())
    g["rapport"] = g["rapport"].str.replace("LF", "").astype(int)
    g["total"] = g[[i for i, _, _ in IMPOTS]].sum(axis=1)
    g["reparti"] = "oui"
    a = pd.read_csv(AGREGATS)
    seuls = a[~a["rapport"].isin(g["rapport"].unique())]
    g = pd.concat([g, pd.DataFrame({"rapport": seuls["rapport"], "annee": seuls["exercice"],
                                    "total": seuls["avantages_fiscaux_md"], "reparti": "non"})],
                  ignore_index=True).sort_values(["rapport", "annee"]).reset_index(drop=True)
    rec = figtools.series(RECETTES).set_index("annee")["total_MDT"]
    p = figtools.series(PIB)
    p = p[(p["famille"] == "budget") & (p["poste"] == "total")].set_index("annee")
    g["recettes"] = [float(rec[x]) for x in g["annee"]]
    g["pib"] = [float(p.loc[x, "pib_MDT"]) for x in g["annee"]]
    g["base"] = [str(p.loc[x, "base_pib"])
                 + (", rétropolée" if p.loc[x, "pib_retropole"] == "oui" else ", non rétropolée")
                 for x in g["annee"]]
    g["rec_pct"] = 100 * g["total"] / g["recettes"]
    g["pib_pct"] = 100 * g["total"] / g["pib"]
    pub = a.set_index(["rapport", "exercice"])
    for col, nom in (("pct_ressources_fiscales_publie", "rec_publie"),
                     ("pct_pib_publie", "pib_publie")):
        g[nom] = [pub[col].get((r, x)) for r, x in zip(g["rapport"], g["annee"])]
    return g


def table() -> pd.DataFrame:
    g = _donnees()
    out = pd.DataFrame({
        "Rapport annexé au projet de loi de finances pour": g["rapport"],
        "Exercice": g["annee"],
        "Périmètre": [PERIMETRE[r] for r in g["rapport"]]})
    for cle, nom, _ in IMPOTS:
        out[f"{nom} (MD)"] = g[cle].round(1)
    out["Total (MD)"] = g["total"].round(1)
    out["Recettes fiscales de l'État (MD)"] = g["recettes"].round(1)
    out["Total, % des recettes fiscales (calculé)"] = g["rec_pct"].round(2)
    out["% des ressources fiscales imprimé par le rapport"] = g["rec_publie"]
    out["PIB (MD)"] = g["pib"].round(1)
    out["Base du PIB"] = g["base"]
    out["Total, % du PIB (calculé)"] = g["pib_pct"].round(2)
    out["% du PIB imprimé par le rapport"] = g["pib_publie"]
    return out


def fig_total(mesure: str = "md"):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g = _donnees()
    ylabel, dec, unite = MESURES[mesure]
    fig, ax = plt.subplots(figsize=(10, 5.4))
    x, xs, graduations, centres = 0.0, [], [], {}
    for rapport, bloc in g.groupby("rapport", sort=True):
        debut = x
        for r in (pd.Series(x) for x in bloc.to_dict("records")):
            k = 1.0 if mesure == "md" else 100 / (r.recettes if mesure == "rec" else r.pib)
            if r.reparti == "oui":
                bas = 0.0
                for cle, nom, couleur in IMPOTS:
                    v = float(r[cle])
                    barre = ax.bar([x], [v * k], bottom=bas, width=0.72, color=couleur,
                                   edgecolor="white", zorder=2)
                    figtools.infobulle(barre[0], f"exercice {r.annee}, rapport pour {rapport} · "
                                                 f"{nom} : {_nb(v, 1)} MD"
                                       + ("" if mesure == "md"
                                          else f", soit {_nb(v * k, 2)}{unite}"))
                    bas += v * k
            else:
                bas = r.total * k
                barre = ax.bar([x], [bas], width=0.72, facecolor="none", edgecolor=GRIS,
                               hatch="///", lw=1, zorder=2)
                figtools.infobulle(barre[0], f"exercice {r.annee}, rapport pour {rapport} · total "
                                             f"d'introduction : {_nb(r.total)} MD, non réparti")
            ax.annotate(ft(_nb(bas, dec)), xy=(x, bas), xytext=(0, 2), textcoords="offset points",
                        ha="center", va="bottom", fontsize=7)
            publie = {"rec": r.rec_publie, "pib": r.pib_publie}.get(mesure)
            if publie is not None and not pd.isna(publie):
                pt, = ax.plot([x], [publie], marker="D", ms=5.5, mfc="white", mec="#1f2328",
                              ls="", zorder=4)
                figtools.infobulle(pt, f"exercice {r.annee} · ratio imprimé par le rapport pour "
                                       f"{rapport} : {_nb(publie, 2)} %")
            xs.append(x)
            graduations.append(str(r.annee))
            x += 1
        centres[rapport] = (debut + x - 1) / 2
        ax.axvline(x - 0.25, color="#d0d7de", lw=0.8, zorder=0) if rapport != g["rapport"].max() \
            else None
        x += 0.5
    ax.set_xticks(xs)
    ax.set_xticklabels(graduations, fontsize=8)
    for rapport, c in centres.items():
        ax.annotate(ft(f"rapport pour {rapport}\n{PERIMETRE[rapport]}".replace(" ; ", "\n")),
                    xy=(c, 0), xycoords=("data", "axes fraction"), xytext=(0, -20),
                    textcoords="offset points", ha="center", va="top", fontsize=6.6, color=GRIS)
    ax.set_xlim(-0.7, x - 0.8)
    ax.set_ylim(top=ax.get_ylim()[1] * 1.1)
    ax.set_ylabel(ft(ylabel))
    ax.grid(True, axis="y", alpha=0.3)
    for cote in ("top", "right"):
        ax.spines[cote].set_visible(False)
    poignees = [Patch(facecolor=c, label=ft(n)) for _, n, c in IMPOTS]
    poignees.append(Patch(facecolor="none", edgecolor=GRIS, hatch="///",
                          label=ft("total d'introduction du rapport, non réparti par impôt")))
    if mesure != "md":
        poignees.append(Line2D([], [], marker="D", mfc="white", mec="#1f2328", ls="", ms=5.5,
                               label=ft("ratio imprimé par le rapport pour son exercice de tête")))
    if mesure == "pib":
        # Base du PIB au-dessus du cadre, comme les figures du volume « Compensation ».
        bases = sorted(set(g["base"]))
        ax.annotate(ft("PIB : " + " ; ".join(bases)), xy=(0.5, 1), xycoords="axes fraction",
                    xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                    fontsize=7, color=GRIS)
        poignees.append(Line2D([], [], color="none",
                               label=ft("au-dessus du cadre : base du PIB de chaque segment")))
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=2,
              fontsize=7.6, frameon=False)
    fig.tight_layout()
    return fig


def vues():
    return [("En millions de dinars", fig_total("md")),
            ("En % des recettes fiscales", fig_total("rec")),
            ("En % du PIB", fig_total("pib"))]

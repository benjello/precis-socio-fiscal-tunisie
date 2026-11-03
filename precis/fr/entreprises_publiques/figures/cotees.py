"""Tableau et figure du chapitre « Les sociétés cotées » (volume « Les entreprises publiques »).

    from figures import cotees as ct
    ct.tableau_participations(caption=…)          # qui détient quoi, détenteur par détenteur
    ct.figure_resultats(caption=…, note_lecture=…)  # résultat net et dividende de l'État
    ct.tableau_resultats(caption=…)               # résultat net et dividendes des sociétés où l'État est actionnaire
    ct.tableau_perimetres(caption=…)              # les entités consolidées par la STB, la BH et la BNA
    ct.tableau_registre(caption=…)                # l'identité des entreprises publiques au Registre national (annexe)
    ct.figure_capital(caption=…, note_lecture=…)  # le capital de la STB, de la BH et de la BNA

D'OÙ VIENNENT LES DONNÉES. Des relevés versionnés DANS le livre (`listes/*.csv`, chacun avec son manifeste `.csv.yml`) :
`societes-cotees-*.csv`, engendrés par `scripts/bvmt_societes_cotees.py livre` à partir des pages
publiques de la Bourse de Tunis, et `entreprises-publiques-registre.csv`, engendré par
`scripts/rne_registre_releve.py` à partir du portail public du Registre national des entreprises.
Rien n'est lu de l'entrepôt `tunisia-data` à la construction.

RÈGLES.

  - **Les détenteurs publics sont une liste fermée** (voir le script) : un nom n'est pas tenu
    pour public d'après sa seule apparence.
  - **La Bourse ne nomme que les actionnaires de plus de 5 %** : un détenteur public sous ce
    seuil est absent du tableau, et les parts du tableau ne s'additionnent pas à 100 %.
  - **La figure trace ce que la page imprime** : une ligne dont le capital est inférieur à celui
    de la ligne précédente n'est pas tracée.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

RELEVES = Path(__file__).resolve().parent.parent / "listes"
PARTICIPATIONS = "societes-cotees-participations"
CAPITAL = "societes-cotees-capital"
RESULTATS = "societes-cotees-resultats"
REGISTRE = "entreprises-publiques-registre"
PERIMETRE = "groupes-bancaires-perimetre"
ALIAS_ENTITES = {"STCVERITAS": "STCVVERITAS"}  # « S.T.C VERITAS » et « S.T.C.V VERITAS » : la même société
RAPPORTS = {"STB": "bvmt-ra-stb-2021", "BH": "bvmt-ra-bh-2021", "BNA": "bvmt-ra-bna-2021"}
PAGES_RAPPORT = {"STB": "p. 96-97", "BH": "p. 240", "BNA": "p. 127"}
COULEURS = {"STB": "#0969da", "BH": "#bc4c00", "BNA": "#1a7f37"}


def _lire(nom: str) -> pd.DataFrame:
    return pd.read_csv(RELEVES / f"{nom}.csv", dtype=str, keep_default_na=False)


def _sources(nom: str) -> list[str]:
    import yaml
    manifeste = yaml.safe_load((RELEVES / f"{nom}.csv.yml").read_text(encoding="utf-8"))
    return list(manifeste["sources"])


figtools.register_provenance(
    CAPITAL, titre="Capital de la STB, de la BH et de la BNA, depuis leur constitution",
    sources=_sources(CAPITAL), unite="dinars courants",
    perimetre=("historique du capital imprimé sur la page de chaque banque à la Bourse de "
               "Tunis : date de la décision de l'assemblée, nature de l'opération, "
               "augmentation et capital après l'opération"),
    caveats=("La page imprime ses chiffres tels quels : une ligne de la BH (6 juin 1995) donne "
             "un capital inférieur à celui de la ligne précédente et n'est pas tracée. Les "
             "dates sont celles de l'assemblée, non de la libération du capital."))


figtools.register_provenance(
    RESULTATS, titre="Résultat net et dividende des sociétés cotées où l'État est actionnaire",
    sources=_sources(RESULTATS), unite="millions de dinars courants",
    perimetre=("encadré « Indicateurs et ratios clés » de la page de chaque société à la Bourse de "
               "Tunis : résultat net (part du groupe pour les sociétés qui publient des comptes "
               "consolidés) et dividende par action, exercices 2022 à 2025 quand la page les donne"),
    caveats=("Le dividende revenant à l'État est CALCULÉ : dividende par action de l'exercice N, "
             "multiplié par les actions de l'État à l'assemblée de l'année N+1 ; il n'est calculé "
             "que dans ce cas et n'est pas une recette du budget. Une case vide est une valeur "
             "que la page n'imprime pas, non un zéro."))


def _md(entete: list[str], lignes: list[list[str]], caption: str, tbl_id: str) -> None:
    out = ["| " + " | ".join(entete) + " |",
           "|---|" + "|".join(":-:" for _ in entete[1:]) + "|"]
    out += ["| " + " | ".join(ligne) + " |" for ligne in lignes]
    print("\n".join(out) + f"\n\n: {caption} {{#{tbl_id}}}\n")


def _pct(valeur: str) -> str:
    return valeur.replace(".", ",")


def tableau_participations(caption: str, tbl_id: str = "tbl-ep-cotees-participations") -> None:
    """Une ligne par participation, regroupées par détenteur ; le détenteur n'est écrit qu'une fois."""
    d = _lire(PARTICIPATIONS)
    lignes, precedent = [], None
    for _, r in d.iterrows():
        detenteur = f"**{r['detenteur']}**" if r["detenteur"] != precedent else ""
        precedent = r["detenteur"]
        lignes.append([detenteur, r["societe"], _pct(r["part_pct"]), r["assemblee"],
                       f"[@bvmt-{r['page']}]"])
    _md(["Détenteur", "Société cotée", "Part du capital (%)", "Assemblée", "Source"],
        lignes, caption, tbl_id)


def _md_dt(valeur: str, mille: float = 1e6, chiffres: int = 1) -> str:
    """Dinars → millions de dinars, virgule décimale ; vide si le relevé est vide."""
    if valeur == "":
        return "–"
    return f"{float(valeur) / mille:,.{chiffres}f}".replace(",", " ").replace(".", ",")


def tableau_resultats(caption: str, tbl_id: str = "tbl-ep-cotees-resultats") -> None:
    """Résultat net et dividende par action par exercice, et dividende revenant à l'État."""
    d = _lire(RESULTATS)
    lignes = []
    precedent = None
    for _, r in d.iterrows():
        societe = f"**{r['societe']}**" if r["societe"] != precedent else ""
        precedent = r["societe"]
        dividende = r["dividende_par_action_dt"].replace(".", ",") or "–"
        lignes.append([societe, r["exercice"], _md_dt(r["resultat_net_dt"]), dividende,
                       _md_dt(r["dividende_etat_dt"]), f"[@bvmt-{r['page']}]"])
    _md(["Société", "Exercice", "Résultat net (MD)", "Dividende par action (D)",
         "Dividende revenant à l'État (MD)", "Source"], lignes, caption, tbl_id)


def tableau_perimetres(caption: str, tbl_id: str = "tbl-ep-cotees-perimetres") -> None:
    """Les entités consolidées par la STB, la BH et la BNA : méthode, contrôle, intérêt."""
    d = _lire(PERIMETRE)
    d = d[d["exercice"] == "2021"]
    lignes, precedent = [], None
    for _, r in d.iterrows():
        groupe = f"**{r['groupe']}**" if r["groupe"] != precedent else ""
        precedent = r["groupe"]
        controle = _pct(r["controle_pct"]) if r["controle_pct"] else "–"
        lignes.append([groupe, r["entite"], r["methode"] or "–", controle, _pct(r["interet_pct"]),
                       f"[@{r['source']}, {PAGES_RAPPORT[r['groupe']]}]"])
    _md(["Groupe", "Entité consolidée", "Méthode", "Contrôle (%)", "Intérêt (%)", "Source"],
        lignes, caption, tbl_id)


def _cle_entite(nom: str) -> str:
    import re
    import unicodedata
    brut = unicodedata.normalize("NFKD", nom).encode("ascii", "ignore").decode().upper()
    brut = re.sub(r"\(.*?\)|\bEX\b.*", "", brut)
    cle = re.sub(r"[^A-Z0-9]", "", brut)
    return ALIAS_ENTITES.get(cle, cle)


def tableau_evolution(groupe: str, caption: str, tbl_id: str) -> None:
    """Les entités d'un groupe, exercice par exercice : pourcentage d'intérêt (à défaut de contrôle),
    « (ME) » pour la mise en équivalence, « – » quand l'entité n'est pas consolidée cet exercice-là."""
    d = _lire(PERIMETRE)
    d = d[(d["groupe"] == groupe) & (d["methode"] != "mère")]
    exercices = sorted(d["exercice"].unique())
    entites: dict[str, dict] = {}
    for _, r in d.sort_values("exercice").iterrows():
        e = entites.setdefault(_cle_entite(r["entite"]), {"nom": r["entite"], "premier": r["exercice"], "val": {}})
        e["nom"] = r["entite"]
        valeur = _pct(r["interet_pct"] or r["controle_pct"])
        e["val"][r["exercice"]] = valeur + (" (ME)" if r["methode"] == "mise en équivalence" else "")
    lignes = [[e["nom"].replace("’", "'")] + [e["val"].get(x, "–") for x in exercices]
              for e in sorted(entites.values(), key=lambda e: (e["premier"], e["nom"]))]
    lignes.append(["**Nombre d'entités**"] + [str(sum(1 for e in entites.values() if x in e["val"])) for x in exercices])
    _md(["Entité"] + exercices, lignes, caption, tbl_id)


def tableau_registre(caption: str, tbl_id: str = "tbl-ep-registre-entreprises") -> None:
    """Une ligne par entreprise : identifiant, forme, état, états financiers déposés."""
    d = _lire(REGISTRE)
    lignes = []
    for _, r in d.iterrows():
        exercices = r["exercices_etats_financiers"].replace(" ", ", ") or "aucun"
        lignes.append([r["entreprise"], r["id_unique"], r["forme_juridique"].replace(
            "Etablissement", "Établissement"), r["etat_registre"].replace("Non Actif", "non actif"
            ).replace("Actif", "actif"), exercices, r["documents"]])
    _md(["Entreprise", "Identifiant", "Forme au Registre", "État", "États financiers déposés",
         "Documents listés"], lignes, caption, tbl_id)


COULEURS_SOCIETES = {"BNA": "#1a7f37", "STB": "#0969da", "BH": "#bc4c00", "STAR": "#8250df",
                     "SOTUMAG": "#57606a", "Ciments de Bizerte": "#cf222e", "Tunisair": "#bf8700"}


def donnees_resultats() -> pd.DataFrame:
    d = _lire(RESULTATS)
    for colonne in ("resultat_net_dt", "dividende_etat_dt", "dividende_par_action_dt"):
        d[colonne] = pd.to_numeric(d[colonne], errors="coerce")
    d["resultat_net_md"] = d["resultat_net_dt"] / 1e6
    d["dividende_etat_md"] = d["dividende_etat_dt"] / 1e6
    d["exercice"] = d["exercice"].astype(int)
    return d


def fig_resultats():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = donnees_resultats()
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.5, 4.8), gridspec_kw={"width_ratios": [2.1, 1]})
    ax.axhline(0, color="#57606a", lw=0.8, zorder=1)
    for societe, groupe in d.groupby("societe"):
        couleur = COULEURS_SOCIETES[societe]
        ax.plot(groupe["exercice"], groupe["resultat_net_md"], "-", color=couleur, lw=1.8, zorder=2)
        points, = ax.plot(groupe["exercice"], groupe["resultat_net_md"], "o", color=couleur, ms=5,
                          zorder=3, label=societe)
        for _, r in groupe.iterrows():
            figtools.infobulle(points, f"{societe} · exercice {r['exercice']} · résultat net "
                                      f"{r['resultat_net_md']:.1f} MD")
    ax.set_xticks(sorted(d["exercice"].unique()))
    ax.set_ylabel(ft("Résultat net (millions de dinars)"))
    ax.set_xlabel(ft("Exercice"))
    ax.set_title(ft("Résultat net"), fontsize=10, loc="left")
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.set_axisbelow(True)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=4, fontsize=8, frameon=False)
    calcule = d.dropna(subset=["dividende_etat_md"]).sort_values("dividende_etat_md")
    etiquettes = [f"{r['societe']}\n{r['exercice']}" for _, r in calcule.iterrows()]
    barres = bx.barh(etiquettes, calcule["dividende_etat_md"],
                     color=[COULEURS_SOCIETES[s] for s in calcule["societe"]], zorder=2)
    for barre, (_, r) in zip(barres, calcule.iterrows()):
        bx.text(barre.get_width() + 0.5, barre.get_y() + barre.get_height() / 2,
                f"{r['dividende_etat_md']:.1f}".replace(".", ","), va="center", fontsize=8)
        figtools.infobulle(barre, f"{r['societe']} · exercice {r['exercice']} · dividende par action "
                                  f"{r['dividende_par_action_dt']:.3g} D × {int(r['actions_etat']):,} actions "
                                  f"de l'État = {r['dividende_etat_md']:.1f} MD".replace(",", " "))
    bx.set_xlim(0, calcule["dividende_etat_md"].max() * 1.18)
    bx.set_xlabel(ft("Dividende calculé (millions de dinars)"), fontsize=8.5)
    bx.set_title(ft("Dividende de l'État"), fontsize=10, loc="left")
    bx.grid(axis="x", color="#d0d7de", lw=0.6)
    bx.set_axisbelow(True)
    for axe in (ax, bx):
        for cote in ("top", "right"):
            axe.spines[cote].set_visible(False)
    fig.tight_layout()
    return fig


def table_resultats() -> pd.DataFrame:
    d = donnees_resultats()
    return d[["societe", "exercice", "resultat_net_dt", "dividende_par_action_dt", "actions_etat",
              "assemblee", "dividende_etat_dt"]]


def figure_resultats(caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure des résultats et dividendes en onglets (chunk `output: asis`, `fig-…`)."""
    figtools.figure_tabs(fig_resultats(), table_resultats(), RESULTATS,
                         slug="fig_ep_cotees_resultats", caption=caption,
                         note_lecture=note_lecture, nominal=False)
    plt.close("all")


def donnees_capital() -> pd.DataFrame:
    d = _lire(CAPITAL)
    d["date"] = pd.to_datetime(d["date"])
    d["capital_md"] = d["capital_dt"].astype(float) / 1e6
    d = d.sort_values(["banque", "date"], kind="stable")
    garde = []
    for _, groupe in d.groupby("banque"):
        precedent = 0.0
        for idx, r in groupe.iterrows():
            if r["capital_md"] >= precedent:
                garde.append(idx)
                precedent = r["capital_md"]
    return d.loc[garde]


def fig_capital():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = donnees_capital()
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    ax.axvspan(pd.Timestamp("2013-01-01"), pd.Timestamp("2015-12-31"), color="#d0d7de",
               alpha=0.5, lw=0, zorder=0)
    for banque, groupe in d.groupby("banque"):
        groupe = groupe.drop_duplicates("date", keep="last")
        ax.step(groupe["date"], groupe["capital_md"], where="post", color=COULEURS[banque],
                lw=1.8, zorder=2, label=banque)
        points, = ax.plot(groupe["date"], groupe["capital_md"], "o", color=COULEURS[banque],
                          ms=4, zorder=3)
        for _, r in groupe.iterrows():
            figtools.infobulle(points, f"{banque} · {r['date']:%d/%m/%Y} · {r['operation']} : "
                                      f"capital {r['capital_md']:.1f} MD")
    ax.set_ylabel(ft("Capital (millions de dinars)"))
    ax.set_xlabel(ft("Date de la décision de l'assemblée"))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.set_axisbelow(True)
    for cote in ("top", "right"):
        ax.spines[cote].set_visible(False)
    ax.legend(loc="upper left", frameon=False)
    ax.annotate(ft("lois de 2013 à 2015"), xy=(pd.Timestamp("2012-10-01"), ax.get_ylim()[1] * 0.97),
                ha="right", va="top", fontsize=8, color="#57606a")
    fig.tight_layout()
    return fig


def table_capital() -> pd.DataFrame:
    d = donnees_capital()
    return d[["banque", "date", "operation", "augmentation_dt", "capital_dt"]].assign(
        date=d["date"].dt.strftime("%Y-%m-%d"))


def figure_capital(caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure du capital en onglets (chunk `output: asis`, étiqueté `fig-…`)."""
    figtools.figure_tabs(fig_capital(), table_capital(), CAPITAL,
                         slug="fig_ep_cotees_capital", caption=caption,
                         note_lecture=note_lecture, nominal=False)
    plt.close("all")

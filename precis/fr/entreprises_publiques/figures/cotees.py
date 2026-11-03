"""Tableau et figure du chapitre « Les sociétés cotées » (volume « Les entreprises publiques »).

    from figures import cotees as ct
    ct.tableau_participations(caption=…)          # qui détient quoi, détenteur par détenteur
    ct.tableau_resultats(caption=…)               # résultat net et dividendes des sociétés où l'État est actionnaire
    ct.tableau_registre(caption=…)                # l'identité des entreprises publiques au Registre national
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

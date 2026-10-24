"""Figure et tableaux de l'annexe « La liste des entreprises publiques » (volume « Les
entreprises publiques »).

    from figures import listes as ls
    ls.figure(caption=…, note_lecture=…)          # le périmètre en nombre, 1997-2021
    ls.tableau_ensemble(caption=…)                # une ligne par entreprise, cinq listes
    ls.tableau_etablissements(caption=…)          # les établissements, six états de la liste
    ls.figure_plafond(caption=…, note_lecture=…)  # plafond légal de la garantie, 1959-2015
    ls.tableau_plafond(caption=…)                 # registre des articles, avec ancres r-ep-pl-…

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
SORTIES = "sorties-recueil-privatisation"
RECUEIL = "privatisation-recueil-operations"
PLAFOND = "jort-lf-plafond-garanties"
FICHIER_PLAFOND = "plafond-garanties-lois-de-finances"  # relevé versionné

BLEU, ORANGE, VERT, GRIS = "#0969da", "#bc4c00", "#1a7f37", "#57606a"
# Année de la liste -> libellé de colonne
LISTES = {"1998": "1998", "2002": "2002", "2005": "2005", "2010": "fin 2010", "2021": "2021"}
ETATS = {"1997": "1997", "1998": "1998", "1999": "1999", "2002": "2002", "2004": "2004",
         "2006": "2006", "2007-07": "juillet 2007", "2007": "octobre 2007"}


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
             "deux dates ; les listes ne donnent ni la date ni le mode de la sortie."))
figtools.register_provenance(
    ETABLISSEMENTS, titre="Établissements publics à caractère non administratif considérés "
                          "comme entreprises publiques, 1997-2007",
    sources=_sources(ETABLISSEMENTS), unite="établissements",
    perimetre=("liste fixée par décret en 1997, refaite en 1999, 2002 et 2004, complétée en "
               "1998 et modifiée en 2006, en juillet et en octobre 2007"),
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
             (2006, "2006"), (2007, "2007-07"), (2007, "2007")]
    xs = [a for a, _ in etats]
    ys = [c["etablissements"][k] for _, k in etats]
    ax.step(xs, ys, where="post", color=VERT, lw=1.8, zorder=2)
    for (a, k), n in zip(etats, ys):
        p, = ax.plot([a], [n], "s", color=VERT, ms=5, zorder=3)
        figtools.infobulle(p, f"{ETATS[k]} · liste des établissements publics considérés comme "
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


def operations_des_sorties() -> pd.DataFrame:
    """Une ligne par entreprise sortie du tableau de tutelle et rangée au recueil de la
    Direction générale de la privatisation : années de cession, modes et produit, tels que le
    recueil les imprime (plusieurs lignes du recueil réunies, dans leur ordre)."""
    recueil = figtools.series(RECUEIL)
    lignes = []
    for _, s in _lire(SORTIES).iterrows():
        op = recueil[(recueil["secteur"] == s["secteur_recueil"])
                     & (recueil["sigle"] == s["sigle_recueil"])].sort_values("ordre")
        if op.empty:
            raise ValueError(f"{s['entreprise']} : aucune ligne du recueil sous "
                             f"{s['secteur_recueil']} / {s['sigle_recueil']}")
        annees = []
        for a in op["annee_imprimee"].astype(str):
            if a not in annees:
                annees.append(a)
        lignes.append({"rang": int(s["rang"]), "entreprise": s["entreprise"],
                       "liste_avant": s["liste_avant"], "liste_apres": s["liste_apres"],
                       "position": s["position"], "rapprochement": s["rapprochement"],
                       "annee_debut": int(op["annee_debut"].min()),
                       "annee_fin": int(op["annee_fin"].max()),
                       "annees": " ; ".join(annees),
                       "modes": " ; ".join(dict.fromkeys(op["mode"].astype(str))),
                       "produit_md": float(op["produit_milliers_dinars"].sum()) / 1000})
    return pd.DataFrame(lignes)


def tableau_sorties(caption: str, tbl_id: str = "tbl-ep-liste-sorties-recueil") -> None:
    """Sorties du tableau de tutelle que le recueil range parmi ses opérations."""
    d = operations_des_sorties()
    ordre = {"entre les deux listes": 0, "avant la première liste": 1}
    d = d.sort_values(["liste_avant", "annee_debut", "rang"],
                      key=lambda c: c.map(ordre) if c.name == "position" else c)
    lignes = []
    for position, titre in (("entre les deux listes", "Opération entre les deux listes"),
                            ("avant la première liste",
                             "Opération antérieure, l'entreprise figurant encore sur la liste suivante")):
        g = d[d["position"] == position]
        lignes.append([f"**{titre}**", "", "", "", ""])
        for _, r in g.iterrows():
            produit = (f"{r['produit_md']:.1f}" if r["produit_md"] >= 1
                       else f"{r['produit_md']:.2f}").replace(".", ",")
            lignes.append([r["entreprise"],
                           f"{r['liste_avant']} – {LISTES[r['liste_apres']]}",
                           r["annees"].replace("-", ", ").replace(" ; ", ", "), r["modes"], produit])
    out = ["| Entreprise | Quitte le tableau entre | Année de cession | "
           "Opération portée au recueil | Produit (MD) |",
           "|---|:-:|:-:|---|--:|"]
    out += ["| " + " | ".join(l) + " |" for l in lignes]
    print("\n".join(out) + f"\n\n: {caption} {{#{tbl_id}}}\n")


# --- plafond légal de la garantie de l'État, 1958-2015 -------------------------------------------

figtools.register_provenance(
    PLAFOND, titre="Plafond de la garantie de l'État fixé par la loi de finances, 1958-59 à 2015",
    sources=_sources(FICHIER_PLAFOND), unite="millions de dinars courants",
    perimetre=("article « octroi de la garantie de l'État » de chaque loi de finances, et lois "
               "qui en modifient le montant en cours de gestion ; montant maximal dans la limite "
               "duquel le ministre chargé des finances est autorisé à accorder la garantie du "
               "Trésor, puis de l'État, en vertu des textes et conventions en vigueur"),
    caveats=("Le plafond est un maximum légal annuel, non un montant de garanties accordées ni "
             "un encours. 1958-59 est imprimé en francs et ne figure pas sur la figure. Les "
             "lois de finances complémentaires dont l'index n'indique pas d'article sur la "
             "garantie n'ont pas été lues en entier : celles de 1969 à 1991 le sont par leur seul "
             "index, celles de 1995 à 2015 ne modifient pas le plafond. Les parts du PIB et des dépenses de "
             "l'État sont des ordres de grandeur : le numérateur est un plafond voté, les "
             "dénominateurs sont décrits sous « plafond-garantie-denominateurs »."))

PLAFOND_DEN = "plafond-garantie-denominateurs"
figtools.register_provenance(
    PLAFOND_DEN,
    titre=("Dénominateurs des parts du plafond de la garantie : PIB aux prix courants, 1961-2015, "
           "et dépenses de l'État hors service de la dette, 1986-2015"),
    sources=["wb-wdi", "undata-sna", "ins-cnat-2015", "ins-pib-base-2015-2010-2020",
             "minfin-remunerations"],
    unite="millions de dinars courants",
    perimetre=("PIB aux prix courants, un par année, jamais raccordé : Banque mondiale de 1961 à "
               "1991, dans une base que la source ne dit pas ; Institut national de la "
               "statistique, en base 1983 de 1992 à 1996, en base 1997 de 1997 à 2009 et en base "
               "2015 de 2010 à 2015. "
               "Dépenses du budget de l'État hors service de la dette, colonnes de réalisation "
               "de la répartition économique des dépenses du ministère des Finances, 1986-2015"),
    caveats=("Le PIB d'avant 1992 n'a pas de base dite ; les passages de 1991 à 1992, de 1996 à "
             "1997 et de 2009 à 2010 sont des ruptures de série, et aucune conversion n'est faite "
             "(voir l'annexe sur le PIB) ; la base 1997 est recalculée par l'INS de 1997 à 2004, la "
             "base 2015 de 2010 à 2014. Les dépenses de l'État hors service de la dette ne sont portées qu'à partir de 1986 (avant, voir le budget ordinaire voté) ; aucun PIB "
             "avant 1961 : l'année financière 1959-60 n'a pas de part du PIB. Le numérateur est "
             "un plafond voté, le dénominateur un budget voté jusqu'en 1986 et des dépenses "
             "réalisées ensuite."))

RUPTURES_PIB = (1992, 1997, 2010)  # années où le PIB change de série (base) : trait interrompu
BUDGET = "jort-lf-budget-ordinaire"
FICHIER_BUDGET = "budget-ordinaire-lois-de-finances"  # relevé versionné
figtools.register_provenance(
    BUDGET, titre="Budget ordinaire de l'État voté par la loi de finances, 1959-60 à 1986",
    sources=_sources(FICHIER_BUDGET), unite="millions de dinars courants",
    perimetre=("montant des recettes ordinaires du budget de l'État (article 1er) et montant "
               "maximum des crédits des dépenses de gestion ou courantes (article 3 ou 6), égaux "
               "chaque année, tels que la loi de finances les fixe ; budgets annexes, "
               "établissements rattachés et fonds spéciaux exclus"),
    caveats=("Montant voté du seul budget ordinaire (titre I), qui peut comprendre une "
             "contribution au budget d'équipement et le service de la dette ; le budget "
             "d'équipement et de développement n'est pas compris. Il ne se raccorde pas aux "
             "dépenses de l'État hors service de la dette, en réalisation, de 1986 à 2015 : "
             "les deux séries se recouvrent en 1986 et ne sont jamais chaînées. Pour 1959-60, "
             "le chiffre des crédits est illisible : seules les recettes sont lues."))

MESURES = {"md": "Millions de dinars courants", "pib": "En % du PIB",
           "dep": "En % du budget de l'État"}


def plafond() -> pd.DataFrame:
    """Relevé enrichi : une ligne par montant fixé ou modifié, avec le montant de la gestion
    précédente (dernier montant en vigueur) pour les lois de finances de l'année."""
    d = _lire(FICHIER_PLAFOND)
    d["plafond"] = pd.to_numeric(d["plafond_md"], errors="coerce")
    d["avant"] = pd.to_numeric(d["plafond_avant_md"], errors="coerce")
    precedent = None
    precedents = []
    for _, r in d.iterrows():
        precedents.append(precedent if r["nature"] == "fixation" else None)
        if not pd.isna(r["plafond"]):
            precedent = r["plafond"]
    d["precedent"] = precedents
    return d


def budget() -> pd.DataFrame:
    """Budget ordinaire voté : une ligne par gestion, `budget_md` = crédits, ou recettes quand
    le chiffre des crédits n'est pas lu (1959-60)."""
    d = _lire(FICHIER_BUDGET)
    d["recettes"] = pd.to_numeric(d["recettes_md"], errors="coerce")
    d["credits"] = pd.to_numeric(d["credits_md"], errors="coerce")
    d["budget_md"] = d["credits"].fillna(d["recettes"])
    return d


def _gestions() -> pd.DataFrame:
    """Une ligne par gestion depuis 1959-60 : montant fixé par la loi de finances de l'année,
    montant en vigueur à la fin de la gestion, lois porteuses."""
    d = plafond()
    d = d[d["plafond"].notna()]
    lignes = []
    for g, h in d.groupby("gestion", sort=False):
        fixe = h[h["nature"] == "fixation"].iloc[0]
        dernier = h.iloc[-1]
        lignes.append({"gestion": g, "annee": int(g[:4]), "fixe_md": float(fixe["plafond"]),
                       "fin_md": float(dernier["plafond"]),
                       "lois": " ; ".join(f"loi n° {x}" for x in dict.fromkeys(h["loi"]))})
    return pd.DataFrame(lignes)


def _denominateurs() -> pd.DataFrame:
    """Par année : PIB aux prix courants (série publiée, jamais raccordée), sa base, et les
    dépenses de l'État hors service de la dette (réalisation)."""
    p = figtools.series("pib-courant-enchaine")
    p = p[p["variante"] == "accolee"].set_index("annee")
    d = figtools.series("denominateurs-depenses-etat-pib").set_index("annee")
    out = pd.DataFrame({"pib": p["pib_MD"], "base": p["base"]})
    out["depenses"] = d["depenses_etat_hors_dette_MDT"]
    return out


def _base_pib(base: str) -> str:
    return "base non dite" if str(base).startswith("base non dite") else str(base)


def _parts(g: pd.DataFrame) -> pd.DataFrame:
    """Les montants des gestions et leurs deux parts, là où le dénominateur existe. La gestion
    N est rapportée au PIB de l'année N ; 1959-60 n'a pas d'année de PIB."""
    den = _denominateurs()
    g = g.copy()
    for col in ("pib", "base", "depenses"):
        g[col] = g["annee"].map(den[col])
    g["base"] = g["base"].map(lambda b: None if pd.isna(b) else _base_pib(b))
    g.loc[g["gestion"] == "1959-60", ["pib", "base", "depenses"]] = None
    g["budget"] = g["gestion"].map(budget().set_index("gestion")["budget_md"])
    for mesure, col in (("pib", "pib"), ("dep", "depenses"), ("bud", "budget")):
        g[f"fixe_{mesure}"] = 100.0 * g["fixe_md"] / g[col]
        g[f"fin_{mesure}"] = 100.0 * g["fin_md"] / g[col]
    return g


def _soit(valeur: float, colonne: str, denominateur: str = "") -> str:
    """Suffixe d'infobulle : la part, quand la vue est une part."""
    if colonne.endswith("_md"):
        return ""
    return f", soit {valeur:.1f} %{denominateur}".replace(".", ",", 1)


def _trace_gestions(ax, g: pd.DataFrame, fixe: str, fin: str, ruptures=(), couleur=BLEU,
                    marque="o", denominateur: str = "") -> None:
    """Trait par suite d'années consécutives, un rond par gestion, un losange orange quand un
    montant postérieur porte le plafond en cours de gestion. Le trait s'interrompt aux années de
    `ruptures` : deux séries de PIB de bases différentes ne se raccordent pas."""
    g = g[g[fixe].notna()].reset_index(drop=True)
    debut = 0
    for i in range(1, len(g) + 1):
        if (i == len(g) or g["annee"].iloc[i] != g["annee"].iloc[i - 1] + 1
                or g["annee"].iloc[i] in ruptures):
            seg = g.iloc[debut:i]
            if len(seg) > 1:
                ax.step(seg["annee"], seg[fixe], where="post", color=couleur, lw=1.8, zorder=2)
            debut = i
    for _, r in g.iterrows():
        p, = ax.plot([r["annee"]], [r[fixe]], marque, color=couleur, ms=4.5, zorder=3)
        figtools.infobulle(p, f"gestion {r['gestion']} · plafond fixé par la loi de finances : "
                              f"{r['fixe_md']:g} MD{_soit(r[fixe], fixe, denominateur)}")
        if r["fin_md"] != r["fixe_md"]:
            ax.annotate("", xy=(r["annee"], r[fin]), xytext=(r["annee"], r[fixe]),
                        arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.4), zorder=3)
            p, = ax.plot([r["annee"]], [r[fin]], "D", color=ORANGE, ms=5, zorder=4)
            figtools.infobulle(p, f"gestion {r['gestion']} · montant porté à {r['fin_md']:g} MD "
                                  f"par {r['lois'].split(' ; ')[-1]}{_soit(r[fin], fin, denominateur)}")


def _legende_plafond(ax, ft, dep: bool = False) -> None:
    carre = ([Line2D([], [], color=VERT, marker="s", lw=1.8, ms=4.5,
                     label=ft("plafond fixé, en % du budget ordinaire voté (1959-60 à 1986)"))]
             if dep else [])
    ax.legend(handles=carre + [
        Line2D([], [], color=BLEU, marker="o", lw=1.8, ms=4.5,
               label=ft("plafond fixé, en % des dépenses de l'État hors service de la dette, "
                        "réalisation (1986 à 2015)" if dep
                        else "plafond fixé par la loi de finances de la gestion")),
        Line2D([], [], color=ORANGE, marker="D", lw=0, ms=5,
               label=ft("montant porté en cours de gestion par une loi postérieure"))],
        loc="upper left", fontsize=8, frameon=False)


def _cadre_plafond(ax) -> None:
    ax.set_xlim(1958.5, 2016.5)
    ax.set_xticks(list(range(1960, 2016, 5)))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.set_axisbelow(True)
    for cote in ("top", "right"):
        ax.spines[cote].set_visible(False)


def fig_plafond(mesure: str = "md"):
    """Une vue du plafond : `md` (millions de dinars courants, échelle logarithmique), `pib`
    (en % du PIB de l'année, par segment de base) ou `dep` (en % des dépenses de l'État hors
    service de la dette, 1986-2015)."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g = _parts(_gestions())
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    _cadre_plafond(ax)
    ax.set_xlabel(ft("Gestion (année de la loi de finances ; 1959 : année financière 1959-60)"))
    if mesure == "md":
        _trace_gestions(ax, g, "fixe_md", "fin_md")
        ax.set_yscale("log")
        ax.set_ylim(8, 7000)
        ax.set_yticks([10, 25, 50, 100, 200, 500, 1000, 2000, 4000])
        ax.set_yticklabels(["10", "25", "50", "100", "200", "500", "1 000", "2 000", "4 000"])
        ax.minorticks_off()
        for annee, y, texte, dx, dy in ((1959, 12, "12", 0, -13), (1963, 16, "16", 0, -13),
                                        (1967, 20, "20", 0, -13), (1968, 25, "25", 0, -13),
                                        (1975, 50, "50", 0, -13), (1977, 200, "200", 0, -13),
                                        (1988, 300, "300", 0, -13), (1992, 250, "250", 0, -13),
                                        (1993, 500, "500", 0, -13), (1994, 950, "950", 0, -13),
                                        (2003, 1200, "1 200", 14, -3), (2012, 4000, "4 000", 0, 7),
                                        (2013, 3000, "3 000", 0, -13)):
            ax.annotate(texte, xy=(annee, y), xytext=(dx, dy), textcoords="offset points",
                        ha="center", fontsize=7.5)
        ax.set_ylabel(ft("Millions de dinars courants (échelle logarithmique)"))
    else:
        if mesure == "dep":
            _trace_gestions(ax, g, "fixe_bud", "fin_bud", couleur=VERT, marque="s",
                            denominateur=" du budget ordinaire voté")
            _trace_gestions(ax, g, "fixe_dep", "fin_dep",
                            denominateur=" des dépenses de l'État hors service de la dette")
        else:
            _trace_gestions(ax, g, f"fixe_{mesure}", f"fin_{mesure}",
                            ruptures=RUPTURES_PIB if mesure == "pib" else ())
        if mesure == "pib":
            ax.set_ylim(0, 11)
            ax.set_ylabel(ft("% du PIB de l'année"))
            for rupture in RUPTURES_PIB:
                figtools.marque_rupture(ax, rupture)
            for x, texte in ((1976, "PIB 1961-1991 : Banque mondiale, base non dite"),
                             (1994, "INS, base 1983"), (2003.5, "INS, base 1997"),
                             (2013.2, "INS, base 2015")):
                ax.annotate(texte, xy=(x, 1), xycoords=("data", "axes fraction"),
                            xytext=(0, 5), textcoords="offset points",
                            ha="center", va="bottom", fontsize=7,
                            color=GRIS, annotation_clip=False)
        else:
            figtools.marque_rupture(ax, 1986)
            for x, texte in ((1972, "budget ordinaire voté (loi de finances)"),
                             (2001, "dépenses de l'État hors service de la dette, réalisation")):
                ax.annotate(ft(texte), xy=(x, 1), xycoords=("data", "axes fraction"),
                            xytext=(0, 5), textcoords="offset points", ha="center",
                            va="bottom", fontsize=7, color=GRIS, annotation_clip=False)
            ax.set_ylim(0, 55)
            ax.set_ylabel(ft("% du budget de l'État (deux dénominateurs, voir les traits)"))
    _legende_plafond(ax, ft, dep=(mesure == "dep"))
    fig.tight_layout()
    return fig


def vues_plafond():
    return [(MESURES[m], fig_plafond(m)) for m in ("md", "pib", "dep")]


def table_plafond() -> pd.DataFrame:
    g = _parts(_gestions())

    def arr(col):
        return [None if pd.isna(x) else round(float(x), 2) for x in g[col]]

    return pd.DataFrame({
        "Gestion": g["gestion"],
        "Plafond fixé par la loi de finances (MD)": g["fixe_md"],
        "Montant en vigueur à la fin de la gestion (MD)": g["fin_md"],
        "PIB de l'année (MD)": [None if pd.isna(x) else float(x) for x in g["pib"]],
        "Base du PIB": g["base"].where(g["base"].notna(), None),
        "Plafond fixé, en % du PIB": arr("fixe_pib"),
        "Montant en vigueur à la fin, en % du PIB": arr("fin_pib"),
        "Dépenses de l'État hors service de la dette, réalisation (MD)":
            [None if pd.isna(x) else float(x) for x in g["depenses"]],
        "Plafond fixé, en % des dépenses de l'État": arr("fixe_dep"),
        "Montant en vigueur à la fin, en % des dépenses de l'État": arr("fin_dep"),
        "Budget ordinaire voté (MD)": [None if pd.isna(x) else float(x) for x in g["budget"]],
        "Plafond fixé, en % du budget ordinaire voté": arr("fixe_bud"),
        "Montant en vigueur à la fin, en % du budget ordinaire voté": arr("fin_bud"),
        "Textes": g["lois"]})


def figure_plafond(caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure du plafond légal en onglets (chunk `output: asis`, étiqueté `fig-…`)."""
    figtools.figure_tabs(vues_plafond(), table_plafond(), PLAFOND, PLAFOND_DEN, BUDGET,
                         slug="fig_ep_plafond_legal",
                         caption=caption, note_lecture=note_lecture)
    plt.close("all")


def _mnt(x: float) -> str:
    """Montant en MD, espace comme séparateur des milliers (« 1 800 »)."""
    if float(x).is_integer():
        return f"{int(x):,}".replace(",", " ")
    return f"{x:g}".replace(".", ",")


def tableau_plafond(caption: str, tbl_id: str = "tbl-ep-plafond-registre") -> None:
    """Registre des articles : une ligne par montant, avec l'ancre `r-ep-pl-<gestion>[-bis]`
    (le texte principal y renvoie), le texte cité avec son article et sa page, ce que l'article
    change, et sa portée."""
    d = plafond()
    vus: dict[str, int] = {}
    lignes = []
    for _, r in d.iterrows():
        n = vus[r["gestion"]] = vus.get(r["gestion"], 0) + 1
        ancre = "r-ep-pl-" + r["gestion"].replace("-", "") + ("" if n == 1 else f"-{n}")
        texte = f"[@{r['cle']}, art. {r['article']}, p. {r['page']}]"
        if pd.isna(r["plafond"]):
            change = f"plafond de la garantie fixé à {r['plafond_imprime']} pour l'année financière"
        elif r["nature"] != "fixation":
            change = (f"plafond porté de {_mnt(r['avant'])} MD à {_mnt(r['plafond'])} MD "
                      f"({r['nature']})")
        elif r["precedent"] is None or pd.isna(r["precedent"]):
            change = f"plafond fixé à {_mnt(r['plafond'])} MD"
        elif r["plafond"] == r["precedent"]:
            change = f"plafond reconduit à {_mnt(r['plafond'])} MD"
        else:
            sens = "porté" if r["plafond"] > r["precedent"] else "ramené"
            change = (f"plafond {sens} de {_mnt(r['precedent'])} MD à {_mnt(r['plafond'])} MD "
                      "par rapport à la gestion précédente")
        if r["nature"] == "fixation" and lignes and lignes[-1][1] == texte:
            change = f"même article : plafond de {_mnt(r['plafond'])} MD aussi pour cette gestion"
        if r["precision"]:
            change += f" ; {r['precision']}"
        g = r["gestion"]
        lignes.append([f"[]{{#{ancre}}}gestion {g}", texte, change, "ajustement"])
    entete = ["Date d'effet", "Texte, article et page", "Ce que le texte change", "Portée"]
    out = ["| " + " | ".join(entete) + " |", "|---|---|---|---|"]
    out += ["| " + " | ".join(l) + " |" for l in lignes]
    print("\n".join(out) + f"\n\n: {caption} {{#{tbl_id}}}\n")


def tableau_budget(caption: str, tbl_id: str = "tbl-ep-budget-ordinaire-registre") -> None:
    """Registre du budget ordinaire voté : une ligne par loi de finances de 1959-60 à 1986, avec
    le texte cité (articles et pages) et les montants que la loi fixe. Les recettes ordinaires et
    les crédits sont égaux ; le chiffre illisible de 1959-60 n'est pas écrit."""
    d = budget()
    lignes = []
    for _, r in d.iterrows():
        if pd.isna(r["credits"]):
            loc = f"art. {r['article_recettes']}, p. {r['page_recettes']}"
        elif r["page_recettes"] == r["page_credits"] and r["article_recettes"] != r["article_credits"]:
            loc = f"art. {r['article_recettes']} et {r['article_credits']}, p. {r['page_recettes']}"
        elif r["page_recettes"] == r["page_credits"]:
            loc = f"art. {r['article_recettes']}, p. {r['page_recettes']}"
        else:
            loc = (f"art. {r['article_recettes']}, p. {r['page_recettes']} ; art. "
                   f"{r['article_credits']}, p. {r['page_credits']}")
        if pd.isna(r["credits"]):
            fixe = f"recettes ordinaires du budget de l'État : {_mnt(r['recettes'])} MD"
        elif r["credits"] == r["recettes"]:
            fixe = (f"recettes ordinaires du budget de l'État et crédits des dépenses de gestion "
                    f"(ou courantes) : {_mnt(r['recettes'])} MD chacun")
        else:
            fixe = f"recettes {_mnt(r['recettes'])} MD ; crédits {_mnt(r['credits'])} MD"
        if r["gestion"] == "1983":
            fixe += ("; la loi fixe aussi un budget général de 1 753 MD, dont 954 MD de dépenses "
                     "courantes et 799 MD de dépenses d'investissement (crédits de paiement), "
                     "aux articles 1er et 2, p. 2876")
        lignes.append([f"gestion {r['gestion']}", f"[@{r['cle']}, {loc}]", fixe])
    out = ["| Date d'effet | Texte, article et page | Ce que le texte fixe |", "|---|---|---|"]
    out += ["| " + " | ".join(l) + " |" for l in lignes]
    print("\n".join(out) + f"\n\n: {caption} {{#{tbl_id}}}\n")

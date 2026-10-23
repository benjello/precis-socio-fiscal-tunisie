"""Figure et tableaux de l'annexe « La liste des entreprises publiques » (volume « Les
entreprises publiques »).

    from figures import listes as ls
    ls.figure(caption=…, note_lecture=…)          # le périmètre en nombre, 1997-2021
    ls.tableau_ensemble(caption=…)                # une ligne par entreprise, cinq listes
    ls.tableau_etablissements(caption=…)          # les établissements, six états de la liste
    ls.figure_plafond(caption=…, note_lecture=…)  # plafond légal de la garantie, 1959-1994
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
PLAFOND = "plafond-garanties-lois-de-finances"

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


# --- plafond légal de la garantie de l'État, 1958-1994 -------------------------------------------

figtools.register_provenance(
    PLAFOND, titre="Plafond de la garantie de l'État fixé par la loi de finances, 1958-59 à 1994",
    sources=_sources(PLAFOND), unite="millions de dinars courants",
    perimetre=("article « octroi de la garantie de l'État » de chaque loi de finances, et lois "
               "qui en modifient le montant en cours de gestion ; montant maximal dans la limite "
               "duquel le ministre chargé des finances est autorisé à accorder la garantie du "
               "Trésor, puis de l'État, en vertu des textes et conventions en vigueur"),
    caveats=("Le plafond est un maximum légal annuel, non un montant de garanties accordées ni "
             "un encours. 1958-59 est imprimé en francs et ne figure pas sur la figure. Les "
             "lois de finances complémentaires dont l'index n'indique pas d'article sur la "
             "garantie n'ont pas été lues en entier. Aucune part du budget ni du PIB : les "
             "dénominateurs de la série du volume commencent en 1986 et en 1991."))


def plafond() -> pd.DataFrame:
    """Relevé enrichi : une ligne par montant fixé ou modifié, avec le montant de la gestion
    précédente (dernier montant en vigueur) pour les lois de finances de l'année."""
    d = _lire(PLAFOND)
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


def fig_plafond():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    g = _gestions()
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    # Un trait par suite d'années consécutives : la gestion 1960 n'a pas de ligne, aucun trait
    # ne traverse le trou.
    debut = 0
    for i in range(1, len(g) + 1):
        if i == len(g) or g["annee"].iloc[i] != g["annee"].iloc[i - 1] + 1:
            seg = g.iloc[debut:i]
            if len(seg) > 1:
                ax.step(seg["annee"], seg["fixe_md"], where="post", color=BLEU, lw=1.8, zorder=2)
            debut = i
    for _, r in g.iterrows():
        p, = ax.plot([r["annee"]], [r["fixe_md"]], "o", color=BLEU, ms=4.5, zorder=3)
        figtools.infobulle(p, f"gestion {r['gestion']} · plafond fixé par la loi de finances : "
                              f"{r['fixe_md']:g} MD")
        if r["fin_md"] != r["fixe_md"]:
            ax.annotate("", xy=(r["annee"], r["fin_md"]), xytext=(r["annee"], r["fixe_md"]),
                        arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.4), zorder=3)
            p, = ax.plot([r["annee"]], [r["fin_md"]], "D", color=ORANGE, ms=5, zorder=4)
            figtools.infobulle(p, f"gestion {r['gestion']} · montant porté à {r['fin_md']:g} MD "
                                  f"par {r['lois'].split(' ; ')[-1]}")
    ax.set_yscale("log")
    ax.set_ylim(8, 1300)
    ax.set_yticks([10, 25, 50, 100, 200, 300, 500, 900])
    ax.set_yticklabels(["10", "25", "50", "100", "200", "300", "500", "900"])
    ax.minorticks_off()
    ax.set_xlim(1958.5, 1995.5)
    ax.set_xticks(list(range(1960, 1996, 5)))
    for annee, y, texte in ((1959, 12, "12"), (1963, 16, "16"), (1967, 20, "20"),
                            (1968, 25, "25"), (1975, 50, "50"), (1977, 200, "200"),
                            (1988, 300, "300"), (1992, 250, "250"), (1993, 500, "500"),
                            (1994, 950, "950")):
        ax.annotate(texte, xy=(annee, y), xytext=(0, -13), textcoords="offset points",
                    ha="center", fontsize=7.5)
    ax.set_ylabel(ft("Millions de dinars courants (échelle logarithmique)"))
    ax.set_xlabel(ft("Gestion (année de la loi de finances ; 1959 : année financière 1959-60)"))
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.set_axisbelow(True)
    for cote in ("top", "right"):
        ax.spines[cote].set_visible(False)
    ax.legend(handles=[
        Line2D([], [], color=BLEU, marker="o", lw=1.8, ms=4.5,
               label=ft("plafond fixé par la loi de finances de la gestion")),
        Line2D([], [], color=ORANGE, marker="D", lw=0, ms=5,
               label=ft("montant porté en cours de gestion par une loi postérieure"))],
        loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def table_plafond() -> pd.DataFrame:
    g = _gestions()
    return pd.DataFrame({
        "Gestion": g["gestion"],
        "Plafond fixé par la loi de finances (MD)": g["fixe_md"],
        "Montant en vigueur à la fin de la gestion (MD)": g["fin_md"],
        "Textes": g["lois"]})


def figure_plafond(caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure du plafond légal en onglets (chunk `output: asis`, étiqueté `fig-…`)."""
    figtools.figure_tabs(fig_plafond(), table_plafond(), PLAFOND, slug="fig_ep_plafond_legal",
                         caption=caption, note_lecture=note_lecture)
    plt.close("all")


def _mnt(x: float) -> str:
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
        g = r["gestion"]
        lignes.append([f"[]{{#{ancre}}}gestion {g}", texte, change, "ajustement"])
    entete = ["Date d'effet", "Texte, article et page", "Ce que le texte change", "Portée"]
    out = ["| " + " | ".join(entete) + " |", "|---|---|---|---|"]
    out += ["| " + " | ".join(l) + " |" for l in lignes]
    print("\n".join(out) + f"\n\n: {caption} {{#{tbl_id}}}\n")

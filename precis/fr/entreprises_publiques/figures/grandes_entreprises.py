"""Figures et tableaux des chapitres « L'énergie » (STEG, ETAP, STIR) et « Les grandes entreprises »
(ensemble de l'échantillon, SNCFT) : une section par entreprise. Les deux chapitres importent ce module.

    from figures import grandes_entreprises as ge
    ge.figure("transferts", caption=…)                      # transferts de onze entreprises
    ge.figure("resultats", …) ; ge.figure("revisions", …)   # résultats nets ; éditions successives
    ge.figure("steg_comptes", …) ; ge.figure("etap_rapports", …)  # comptes publiés
    ge.figure("steg_fiches", …)                             # fiche du ministère, 2018-2023
    ge.figure("stir_budget", …)                             # STIR : transferts, résultat, emploi
    ge.figure("stir_fiches", …)                             # STIR : fiche du ministère, 2018-2023
    ge.figure("oc_budget", …) ; ge.figure("oc_fiches", …)   # Office des céréales, mêmes vues
    ge.figure("sonede_budget", …) ; ge.figure("onas_fiches", …)  # SONEDE, ONAS, mêmes vues
    ge.figure("cpg_fiches", …) ; ge.figure("gct_fiches", …)    # CPG, GCT : fiche seule
    ge.figure("transtu_budget", …) ; ge.figure("autoroutes_fiches", …)  # Transtu, Tunisie Autoroutes
    ge.figure("tunisair_budget", …) ; ge.figure("rnta_fiches", …)  # Tunisair, RNTA, mêmes vues
    ge.figure("onh_budget", …) ; ge.figure("onh_fiches", …)  # Office national de l'huile
    ge.figure("poste_budget", …) ; ge.figure("poste_fiches", …)  # Office national des postes
    ge.figure("tt_fiches", …)                                # Tunisie Télécom : fiche seule
    ge.figure("otc_budget", …) ; ge.figure("otc_fiches", …)  # Office du commerce de la Tunisie
    ge.figure("srt_sfax_budget", …) ; ge.figure("srt_bizerte_fiches", …)  # sociétés régionales
    ge.figure("ctf_fiches", …)                               # Compagnie tunisienne de forage
    ge.figure("sndp_fiches", …)                              # SNDP : fiche seule
    ge.figure("sncpa_budget", …) ; ge.figure("sncpa_fiches", …)  # SNCPA (cellulose, papier alfa)
    ge.figure("afi_budget", …) ; ge.figure("afi_fiches", …)  # Agence foncière industrielle
    ge.figure("ra_budget", …) ; ge.figure("mtk_fiches", …)   # Régie des alcools, MTK
    ge.figure("otd_budget", …) ; ge.figure("otd_fiches", …)  # Office des terres domaniales
    ge.figure("pct_budget", …) ; ge.figure("pct_fiches", …)  # Pharmacie centrale de Tunisie
    ge.figure("stb_fiches", …) ; ge.figure("bh_budget", …)   # banques publiques : STB, BH
    ge.figure("cpscl_budget", …) ; ge.figure("cpscl_fiches", …)  # Caisse des prêts (CPSCL)
    ge.tableau_banque_detail("stb", ("LF2022",), caption=…, tbl_id=…)  # tableau des banques
    ge.figure("bna_fiches", …) ; ge.figure("bfpme_budget", …)  # banques publiques (BNA, BFPME, BTS)
    ge.tableau_fiche_banque("bts", ("LF2025",), caption=…, tbl_id=…)  # tableau des banques, replié
    ge.figure("afh_fiches", …)                               # Agence foncière d'habitation
    ge.figure("sprols_fiches", …)                            # SPROLS : fiche seule
    ge.figure("snit_fiches", …)                              # SNIT : fiche seule
    ge.tableau_fiche_detail("steg", ("LF2022",), caption=…, tbl_id=…)  # fiche imprimée, repliée

D'OÙ VIENNENT LES DONNÉES. Séries de `tunisia-data`, lues par `figtools.series()` :
`entreprises-publiques-fiches-entreprises` (fiches du rapport annexé à la loi de finances,
famille budgétaire), `entreprises-publiques-transferts-par-entreprise`,
`entreprises-publiques-resultats-nets-dix-premieres` et
`entreprises-publiques-effectifs-par-entreprise` (même rapport) ; `steg-etats-financiers` et
`etap-rapports-annuels` (comptes publiés par l'entreprise). Rien n'est saisi ici : ni valeur,
ni page.

RÈGLES. Les deux familles ne se mêlent pas : une figure lit une seule famille. Un exercice est
donné dans la dernière édition qui le porte, nommée sous l'année ; aucune valeur n'est
raccordée d'une édition à l'autre (barres ou points, jamais de trait entre deux éditions).
Une valeur provisoire, estimée ou probable est hachurée, ou tracée en marque creuse. Une case
que la source laisse vide n'est pas tracée : elle n'est pas un zéro. Le tableau des fiches
imprimées garde « — » (la case n'existe pas dans l'édition) et « – » (case vide imprimée).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.colors import to_rgb  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.ticker import FuncFormatter, MaxNLocator  # noqa: E402

from figures.entreprises_publiques import (  # noqa: E402
    BLEU, COULEUR_EDITION, COURT as NOMS, GRIS, NOIR, ORANGE, ROUGE, STATUTS_FERMES, VERT, VIOLET,
    _md, _n, _style)

S_FICHES = "entreprises-publiques-fiches-entreprises"
S_STEG = "steg-etats-financiers"
S_ETAP = "etap-rapports-annuels"

# La figure de la fiche rapproche, pour la lecture, deux mises en page : ces paires désignent la même
# ligne comptable sous deux libellés (fonds propres ; résultat net avant modifications).
COURT = [
    ("produits_exploitation", "produits_exploitation", "Produits d'exploitation", False),
    ("subventions_exploitation", "subventions_exploitation", "dont subvention d'exploitation", False),
    ("resultat_exploitation", "resultat_exploitation", "Résultat d'exploitation", True),
    ("resultat_net", "resultat_net_avant_modifications", "Résultat net", True),
    ("capitaux_propres", "capitaux_propres_avant_affectation", "Fonds propres", True),
    ("dette_totale", None, "Dette totale (LF 2022)", False),
    (None, "total_passifs", "Total des passifs, hors fonds propres", False),
    ("effectif", "effectif", "Effectif (agents)", False),
]

LIB = {
    "dette_totale": "Dette totale", "dette_etat": "dont État", "dette_banques": "dont banques",
    "dette_entreprises_publiques": "dont entreprises publiques",
    "dette_caisses_sociales": "dont caisses sociales", "dette_autres": "dont autres",
    "subventions_investissement": "Subventions d'investissement",
    "investissements": "Investissements", "capitaux_propres": "Fonds propres",
    "resultats_reportes": "Résultats reportés", "resultat_net": "Résultat net",
    "charges_financieres_nettes": "Charges financières nettes",
    "resultat_exploitation": "Résultat d'exploitation",
    "charges_exploitation": "Charges d'exploitation",
    "subventions_exploitation": "Subvention d'exploitation",
    "produits_exploitation": "Produits d'exploitation",
    "charges_personnel": "Charges de personnel", "effectif": "Effectif (agents)",
    "total_passifs": "Total des passifs, hors fonds propres",
    "concours_bancaires": "dont concours bancaires et autres passifs financiers",
    "autres_passifs_courants": "dont autres passifs courants",
    "fournisseurs": "dont fournisseurs", "emprunts_plus_un_an": "dont emprunts à plus d'un an",
    "capitaux_propres_avant_affectation": "Fonds propres avant affectation",
    "total_actifs": "Total des actifs", "liquidites": "Liquidités",
    "clients": "Clients", "immobilisations_nettes": "Immobilisations nettes",
    "resultat_net_avant_modifications": "Résultat net avant modifications comptables",
    "resultat_net_apres_modifications": "Résultat net après modifications comptables",
    "produits_placements": "Produits des placements",
    "autres_produits_exploitation": "dont autres produits d'exploitation",
    "revenus": "dont recettes",
    "stocks": "Stocks nets",
}
ORDRE_A = ["dette_totale", "dette_etat", "dette_banques", "dette_entreprises_publiques",
           "dette_caisses_sociales", "dette_autres", "capitaux_propres", "resultats_reportes",
           "investissements", "subventions_investissement", "produits_exploitation",
           "subventions_exploitation", "charges_exploitation", "resultat_exploitation",
           "charges_financieres_nettes", "resultat_net", "charges_personnel", "effectif"]
ORDRE_B = ["total_actifs", "immobilisations_nettes", "clients", "liquidites",
           "capitaux_propres_avant_affectation", "resultats_reportes", "total_passifs",
           "emprunts_plus_un_an", "concours_bancaires", "fournisseurs", "autres_passifs_courants",
           "produits_exploitation", "revenus", "subventions_exploitation",
           "autres_produits_exploitation", "charges_exploitation", "resultat_exploitation",
           "charges_financieres_nettes", "produits_placements",
           "resultat_net_avant_modifications", "resultat_net_apres_modifications",
           "charges_personnel", "effectif"]
STATUT = {"réalisé": "", "non dit": "", "provisoire": "provisoire", "estimé": "estimé",
          "probable": "probable", "comptes non approuvés": "comptes non approuvés",
          "prévu": "prévu"}


def _ed(edition: str) -> str:
    return f"LF {edition[2:]}"


def _case(x, ind: str, signe: bool = False) -> str:
    if x is None:
        return "—"
    if x["case_vide"] in (True, "True"):
        return "–"
    # Une valeur imprimée sans décimale (STEG, édition LF 2024) le reste.
    imp = str(x["imprime"])
    dec = 0 if (ind == "effectif" or ("," not in imp and "." not in imp)) else 1
    return _n(x["valeur"], dec, signe)


def _fiches(entite: str):
    f = figtools.series(S_FICHES)
    return f[f["entite"] == entite]


def tableau_fiche_detail(entite: str, editions: tuple[str, ...], caption: str,
                         tbl_id: str) -> None:
    """Toutes les grandeurs imprimées par une mise en page, une colonne par (exercice, édition)."""
    f = _fiches(entite)
    f = f[f["edition"].isin(editions)]
    cols = sorted({(x, e) for x, e in zip(f["exercice"], f["edition"])})
    ordre = ORDRE_A if editions == ("LF2022",) else ORDRE_B
    if "stocks" in set(f["indicateur"]):  # ligne propre à la fiche LF 2024 de l'Office du commerce
        ordre = ordre[:ordre.index("liquidites") + 1] + ["stocks"] + ordre[ordre.index("liquidites") + 1:]
    lignes = []
    for ind in ordre:
        cases = []
        for x, e in cols:
            r = f[(f["exercice"] == x) & (f["edition"] == e) & (f["indicateur"] == ind)]
            cases.append(_case(r.iloc[0] if len(r) else None, ind, signe=False))
        lignes.append([LIB[ind]] + cases)
    ent = []
    for x, e in cols:
        st = f[(f["exercice"] == x) & (f["edition"] == e)]["statut"].iloc[0]
        st = STATUT.get(st, st)
        ent.append(f"{x}<br>({_ed(e)}{', ' + st if st else ''})")
    _md(["Millions de dinars"] + ent, "g" + "d" * len(cols), lignes, caption, tbl_id)




# === Figures ======================================================================================

S_TRANSFERTS_EP = "entreprises-publiques-transferts-par-entreprise"
S_NETS_EP = "entreprises-publiques-resultats-nets-dix-premieres"
S_EFFECTIFS_EP = "entreprises-publiques-effectifs-par-entreprise"
HACHURE = "////"
ENTREPRISES_TRANSFERTS = ("stir", "office_cereales", "steg", "cnss", "cnrps", "office_huile",
                          "sonede", "onas", "transtu", "sncft", "tunisie_autoroutes")
ENTREPRISES_RESULTATS = ("steg", "stir", "etap", "office_cereales", "cpg", "gct", "tunisair",
                         "transtu", "sncft", "office_commerce", "rnta", "pct")


def _clair(couleur: str, part: float) -> tuple:
    """La couleur mêlée de blanc : `part` = 1 la garde, 0 donne du blanc (pas de transparence,
    pour que deux barres empilées ne se mélangent pas)."""
    r, g, b = to_rgb(couleur)
    return (1 - part * (1 - r), 1 - part * (1 - g), 1 - part * (1 - b))


COULEURS_TRANSFERTS = {
    "stir": ORANGE, "office_cereales": VERT, "steg": BLEU, "cnss": VIOLET,
    "cnrps": _clair(VIOLET, 0.5), "office_huile": ROUGE, "sonede": _clair(BLEU, 0.45),
    "onas": _clair(VERT, 0.45), "transtu": _clair(ORANGE, 0.45), "sncft": _clair(ROUGE, 0.45),
    "tunisie_autoroutes": _clair(GRIS, 0.55)}


def _ferme(statut) -> bool:
    return statut in STATUTS_FERMES


def _barre(ax, x, h, couleur, *, bas=0.0, largeur=0.7, ferme=True, texte=None):
    """Une barre ; hachurée sur fond clair quand la valeur n'est pas une réalisation."""
    if ferme:
        b = ax.bar(x, h, width=largeur, bottom=bas, color=couleur, lw=0)
    else:
        b = ax.bar(x, h, width=largeur, bottom=bas, facecolor=_clair(couleur, 0.3),
                   edgecolor=couleur, hatch=HACHURE, lw=0)
    if texte:
        figtools.infobulle(b[0], texte)
    return b[0]


def _point(ax, x, y, couleur, *, ferme=True, texte=None, ms=5.0, marque="o"):
    pt, = ax.plot([x], [y], marque, color=couleur, ms=ms, mfc=couleur if ferme else "white",
                  mew=1.2, ls="")
    if texte:
        figtools.infobulle(pt, texte)
    return pt


def _axe_md(ax, unite: str = "MD") -> None:
    # Une décimale pour une graduation non entière (petits montants : −2,5 et non −2).
    ax.yaxis.set_major_formatter(
        FuncFormatter(lambda v, _: _n(v, 0 if abs(v - round(v)) < 1e-9 else 1)))
    # Graduations fractionnaires (petits montants : 0,5 ; 1,5…) écrites avec leur décimale.
    ax.yaxis.set_major_formatter(FuncFormatter(
        lambda v, _: _n(v, 0 if float(v).is_integer() else 1)))
    # Décimales selon l'étendue de l'axe : des transferts de quelques centièmes de MD (Ciments de
    # Bizerte) ne s'écrivent pas « 0 » à chaque graduation.
    def _fmt(v, _):
        lo, hi = ax.get_ylim()
        if hi - lo < 0.5:
            return _n(v, 2)
        # Graduation non entière (2,5 ; 7,5 ; 12,5) : une décimale, pas un arrondi trompeur.
        return _n(v, 0 if abs(v - round(v)) < 1e-9 else 1)
    ax.yaxis.set_major_formatter(FuncFormatter(_fmt))
    ax.set_ylabel(unite, fontsize=7.5)
    ax.tick_params(labelsize=7)


def _hors_source(ax, x, texte="n. d.", couleur=GRIS) -> None:
    """Annotation d'une case que la source ne donne pas, au pied du cadre (pas sur le zéro)."""
    ax.annotate(texte, xy=(x, 0.02), xycoords=("data", "axes fraction"), ha="center",
                va="bottom", fontsize=7, color=couleur)


def _zero(ax, x) -> None:
    """Un zéro imprimé par la source : la barre est invisible, la valeur s'écrit."""
    ax.annotate("0", xy=(x, 0), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=6.5, color=NOIR)


def _marges(ax, haut=0.3) -> None:
    """Place pour la légende au-dessus, et sous le zéro quand des valeurs sont négatives."""
    lo, hi = ax.get_ylim()
    lo, hi = min(lo, 0), max(hi, 0)
    e = hi - lo
    ax.set_ylim(lo - (0.05 * e if lo < 0 else 0), hi + haut * e)


def _poignee_hachure(libelle="provisoire, estimé ou probable") -> Patch:
    return Patch(facecolor=_clair(GRIS, 0.3), edgecolor=GRIS, hatch=HACHURE, lw=0,
                 label=libelle)


def _derniere_edition(df: pd.DataFrame, cles: list[str]) -> pd.DataFrame:
    return df.sort_values("edition").groupby(cles, as_index=False).tail(1)


# --- 1. Transferts du budget à onze entreprises, dernière édition de chaque année ----------------

def _transferts_ep() -> pd.DataFrame:
    t = figtools.series(S_TRANSFERTS_EP)
    return t[t["entite"].isin(ENTREPRISES_TRANSFERTS + ("total",))]


def fig_transferts():
    figtools.apply_lang_font()
    t = _transferts_ep()
    d = _derniere_edition(t, ["entite", "annee"])
    annees = sorted(int(a) for a in d["annee"].unique())
    fig, ax = plt.subplots(figsize=(9.6, 5.6))
    etiquettes = []
    for a in annees:
        bas = 0.0
        for ent in ENTREPRISES_TRANSFERTS:
            r = d[(d["entite"] == ent) & (d["annee"] == a)]
            if r.empty:
                continue
            r = r.iloc[0]
            v = float(r["valeur_md"])
            ferme = r["statut"] == "réalisé"
            _barre(ax, a, v, COULEURS_TRANSFERTS[ent], bas=bas, ferme=ferme,
                   texte=f"{a} — {NOMS[ent]} : {_n(v)} MD, édition {_ed(r['edition'])}"
                         + ("" if ferme else ", provisoire"))
            bas += v
        tot = d[(d["entite"] == "total") & (d["annee"] == a)].iloc[0]
        trait, = ax.plot([a - 0.42, a + 0.42], [tot["valeur_md"]] * 2, color=NOIR, lw=1.8)
        figtools.infobulle(trait, f"{a} — total imprimé de l'échantillon de l'édition "
                                  f"{_ed(tot['edition'])} ({int(tot['echantillon'])} entreprises)"
                                  f" : {_n(tot['valeur_md'])} MD")
        ax.annotate(_n(tot["valeur_md"]), xy=(a, tot["valeur_md"]), xytext=(0, 3),
                    textcoords="offset points", ha="center", va="bottom", fontsize=7)
        st = "" if tot["statut"] == "réalisé" else ", prov."
        etiquettes.append(f"{a}\n{_ed(tot['edition'])}{st}\n({int(tot['echantillon'])} entr.)")
    ax.set_xticks(annees, etiquettes)
    _style(ax)
    _axe_md(ax, "millions de dinars courants")
    ax.set_ylim(0, ax.get_ylim()[1] * 1.06)
    poignees = [Patch(color=COULEURS_TRANSFERTS[e], label=NOMS[e])
                for e in reversed(ENTREPRISES_TRANSFERTS)]
    poignees += [Line2D([], [], color=NOIR, lw=1.8,
                        label="total imprimé de l'échantillon\n(toutes ses entreprises)"),
                 _poignee_hachure("provisoire (2022)")]
    ax.legend(handles=poignees, fontsize=7, frameon=False, loc="upper left",
              bbox_to_anchor=(1.01, 1))
    fig.tight_layout()
    return fig


def _table_transferts_ep(t: pd.DataFrame) -> pd.DataFrame:
    t = t.sort_values(["entite", "annee", "edition"])
    return pd.DataFrame({
        "Entreprise": [("Total de l'échantillon, imprimé" if e == "total" else NOMS.get(e, l))
                       for e, l in zip(t["entite"], t["libelle"])],
        "Année": t["annee"], "Édition": [_ed(e) for e in t["edition"]],
        "Entreprises de l'échantillon": t["echantillon"], "Statut": t["statut"],
        "Transferts (MD courants)": t["valeur_md"], "Imprimé": t["imprime"],
        "Dernière édition de l'année": t["derniere_edition"], "Tableau": t["tableau"],
        "Page du fichier": t["page_pdf"]})


def table_transferts():
    return _table_transferts_ep(_transferts_ep())


# --- 2. Résultats nets des classements --------------------------------------------------------

def _nets() -> pd.DataFrame:
    n = figtools.series(S_NETS_EP)
    n = n[~n["doublon_imprime"].astype(bool) | ~n.duplicated(["exercice", "edition", "entite"])]
    return n.drop_duplicates(["exercice", "edition", "entite"])


def _valeurs_distinctes(bloc: pd.DataFrame, col: str, dec: int = 1):
    """[(valeur, [éditions qui la donnent])], dans l'ordre des éditions."""
    out: dict[float, list[str]] = {}
    for r in bloc.sort_values("edition").itertuples():
        v = getattr(r, col)
        if v != v:
            continue
        out.setdefault(round(float(v), dec), []).append(r.edition)
    return list(out.items())


def _sucettes(ax, x, valeurs, nom: str, dec: int = 1, unite: str = "MD", statuts=None):
    """Une marque par valeur distincte, à la couleur de la dernière édition qui la donne ;
    tige depuis zéro. Deux valeurs d'un même exercice sont décalées de part et d'autre."""
    k = len(valeurs)
    for i, (v, eds) in enumerate(valeurs):
        xi = x + (i - (k - 1) / 2) * 0.24
        coul = COULEUR_EDITION.get(eds[-1], NOIR)
        ferme = True if statuts is None else _ferme(statuts.get(eds[-1]))
        ax.plot([xi, xi], [0, v], color=coul, lw=1.1)
        _point(ax, xi, v, coul, ferme=ferme,
               texte=f"{nom}, {x} : {_n(v, dec, True)} {unite} — édition"
                     f"{'s' if len(eds) > 1 else ''} " + ", ".join(_ed(e) for e in eds))


def fig_resultats():
    figtools.apply_lang_font()
    n = _nets()
    exercices = sorted(int(x) for x in n["exercice"].unique())
    fig, axes = plt.subplots(3, 4, figsize=(11.5, 7.6), sharex=True)
    for ax, ent in zip(axes.flat, ENTREPRISES_RESULTATS):
        b = n[n["entite"] == ent]
        nom = NOMS[ent].split(" (")[0]
        for x in exercices:
            vals = _valeurs_distinctes(b[b["exercice"] == x], "valeur_md")
            if vals:
                _sucettes(ax, x, vals, nom)
        ax.axhline(0, color=NOIR, lw=0.7)
        lo, hi = ax.get_ylim()
        ax.set_ylim(min(lo, 0) - 0.08 * (hi - lo), max(hi, 0) + 0.05 * (hi - lo))
        for x in exercices:
            if b[b["exercice"] == x].empty:
                _hors_source(ax, x, "n. c.")
        ax.set_title(NOMS[ent], fontsize=8, loc="left")
        _style(ax)
        _axe_md(ax, "")
        ax.set_xticks(exercices)
    editions = sorted(n["edition"].unique())
    poignees = [Line2D([], [], color=COULEUR_EDITION[e], marker="o", lw=1.1,
                       label=f"édition {_ed(e)}") for e in editions]
    poignees.append(Line2D([], [], color="none", label="n. c. : hors des deux classements"))
    fig.legend(handles=poignees, fontsize=8, frameon=False, loc="lower center",
               ncol=len(poignees))
    fig.supylabel("résultat net, millions de dinars courants", fontsize=8)
    fig.tight_layout(rect=(0.01, 0.04, 1, 1))
    return fig


def table_resultats():
    n = _nets()
    n = n[n["entite"].isin(ENTREPRISES_RESULTATS)].sort_values(["entite", "exercice", "edition"])
    return pd.DataFrame({
        "Entreprise": [NOMS[e] for e in n["entite"]], "Exercice": n["exercice"],
        "Édition": [_ed(e) for e in n["edition"]],
        "Entreprises de l'échantillon": n["echantillon"],
        "Classement": n["sens"].map({"positifs": "dix premiers résultats positifs",
                                     "negatifs": "dix premiers résultats négatifs"}),
        "Rang": n["rang"], "Résultat net (MD courants)": n["valeur_md"],
        "Imprimé": n["imprime"], "Page imprimée": n["page_imprimee"]})


# --- 3. Transferts d'une même année dans les éditions successives ----------------------------

def fig_revisions():
    figtools.apply_lang_font()
    t = _transferts_ep()
    annees = sorted(int(a) for a in t["annee"].unique())
    fig, axes = plt.subplots(3, 4, figsize=(11.5, 7.6), sharex=True)
    for ax, ent in zip(axes.flat, ENTREPRISES_TRANSFERTS):
        b = t[t["entite"] == ent]
        nom = NOMS[ent].split(" (")[0]
        for a in annees:
            g = b[b["annee"] == a].sort_values("edition")
            k = len(g)
            if k > 1:
                ax.plot([a, a], [g["valeur_md"].min(), g["valeur_md"].max()], color=GRIS,
                        lw=0.8, alpha=0.6)
            for i, r in enumerate(g.itertuples()):
                xi = a + (i - (k - 1) / 2) * 0.17
                coul = COULEUR_EDITION.get(r.edition, NOIR)
                _point(ax, xi, r.valeur_md, coul, ferme=r.statut == "réalisé", ms=4.5,
                       texte=f"{nom}, {a} : {_n(r.valeur_md)} MD — édition {_ed(r.edition)}, "
                             f"{r.statut}")
        ax.set_title(NOMS[ent], fontsize=8, loc="left")
        _style(ax)
        _axe_md(ax, "")
        ax.set_ylim(bottom=0, top=ax.get_ylim()[1] * 1.08)
        ax.set_xticks(annees)
    leg = axes.flat[-1]
    leg.axis("off")
    editions = sorted(t["edition"].unique())
    poignees = [Line2D([], [], color=COULEUR_EDITION[e], marker="o", ls="",
                       label=f"édition {_ed(e)}") for e in editions]
    poignees += [Line2D([], [], color=GRIS, marker="o", mfc="white", ls="",
                        label="valeur provisoire"),
                 Line2D([], [], color=GRIS, lw=0.8, label="écart entre éditions")]
    leg.legend(handles=poignees, fontsize=8, frameon=False, loc="center")
    fig.supylabel("transferts du budget, millions de dinars courants", fontsize=8)
    fig.tight_layout()
    return fig


def table_revisions():
    t = _transferts_ep()
    return _table_transferts_ep(t[t["entite"] != "total"])


# --- 4. Comptes publiés de la STEG, 2013-2023 ----------------------------------------------------

STEG_LIB = {"revenus": "Revenus", "subvention_exploitation": "Subvention d'exploitation",
            "resultat_exploitation": "Résultat d'exploitation", "resultat_net": "Résultat net",
            "resultat_net_apres_modifications": "Résultat après modifications comptables",
            "capitaux_propres": "Capitaux propres avant affectation",
            "total_passifs": "Total des passifs, hors capitaux propres",
            "emprunts_non_courants": "dont emprunts non courants",
            "concours_bancaires": "dont concours bancaires"}


def _steg() -> pd.DataFrame:
    """Chaque exercice lu dans les états financiers de l'exercice ; 2013 dans la colonne de
    comparaison de ceux de 2014."""
    s = figtools.series(S_STEG)
    m = s[s["fichier_du_meme_exercice"].astype(bool)
          | ((s["exercice"] == 2013) & (s["document"] == "steg_ef_2014.pdf"))]
    m = m[m["colonne"].isin(["exercice", "exercice précédent"]) & m["grandeur"].isin(STEG_LIB)]
    return m.drop_duplicates(["exercice", "grandeur"])


def fig_steg_comptes():
    figtools.apply_lang_font()
    m = _steg()
    v = {(int(r.exercice), r.grandeur): float(r.valeur_md) for r in m.itertuples()}
    ans = sorted({a for a, _ in v})
    fig, axes = plt.subplots(3, 1, figsize=(9.6, 9.4), sharex=True)

    def barres(ax, cles_couleurs, largeur=0.36):
        k = len(cles_couleurs)
        for i, (cle, coul) in enumerate(cles_couleurs):
            for a in ans:
                if (a, cle) in v:
                    x = a + (i - (k - 1) / 2) * largeur
                    _barre(ax, x, v[a, cle], coul, largeur=largeur,
                           texte=f"{a} — {STEG_LIB[cle]} : {_n(v[a, cle], 1, cle.startswith('resultat'))} MD")
                    if v[a, cle] == 0:
                        _zero(ax, x)

    ax = axes[0]
    barres(ax, [("revenus", BLEU), ("subvention_exploitation", ORANGE)])
    figtools.marque_rupture(ax, 2015, "subvention indirecte sur le gaz\ncomprise jusqu'en 2014")
    ax.set_title("Revenus et subvention d'exploitation", fontsize=9, loc="left")
    ax.legend(handles=[Patch(color=BLEU, label=STEG_LIB["revenus"]),
                       Patch(color=ORANGE, label=STEG_LIB["subvention_exploitation"])],
              fontsize=7, frameon=False, loc="upper left")

    ax = axes[1]
    barres(ax, [("resultat_exploitation", _clair(VERT, 0.55)), ("resultat_net", VERT)])
    for a in ans:
        if (a, "resultat_net_apres_modifications") in v:
            _point(ax, a, v[a, "resultat_net_apres_modifications"], VIOLET, marque="D", ms=5,
                   texte=f"{a} — résultat après modifications comptables : "
                         f"{_n(v[a, 'resultat_net_apres_modifications'], 1, True)} MD")
    ax.axhline(0, color=NOIR, lw=0.7)
    ax.set_title("Résultats", fontsize=9, loc="left")
    ax.legend(handles=[Patch(color=_clair(VERT, 0.55), label=STEG_LIB["resultat_exploitation"]),
                       Patch(color=VERT, label=STEG_LIB["resultat_net"]),
                       Line2D([], [], color=VIOLET, marker="D", ls="",
                              label="résultat après modifications comptables\n(imprimé "
                                    "certaines années seulement)")],
              fontsize=7, frameon=False, loc="lower left")

    ax = axes[2]
    for a in ans:
        if (a, "total_passifs") in v:
            tp = v[a, "total_passifs"]
            _barre(ax, a + 0.18, tp, _clair(ROUGE, 0.25), largeur=0.36,
                   texte=f"{a} — {STEG_LIB['total_passifs']} : {_n(tp)} MD")
            bas = 0.0
            for cle, coul in (("emprunts_non_courants", ROUGE),
                              ("concours_bancaires", _clair(ROUGE, 0.6))):
                if (a, cle) in v:
                    _barre(ax, a + 0.18, v[a, cle], coul, bas=bas, largeur=0.36,
                           texte=f"{a} — {STEG_LIB[cle]} : {_n(v[a, cle])} MD")
                    bas += v[a, cle]
        if (a, "capitaux_propres") in v:
            _barre(ax, a - 0.18, v[a, "capitaux_propres"], VIOLET, largeur=0.36,
                   texte=f"{a} — {STEG_LIB['capitaux_propres']} : "
                         f"{_n(v[a, 'capitaux_propres'], 1, True)} MD")
    ax.axhline(0, color=NOIR, lw=0.7)
    ax.set_title("Capitaux propres et passifs en fin d'exercice", fontsize=9, loc="left")
    ax.legend(handles=[Patch(color=VIOLET, label=STEG_LIB["capitaux_propres"]),
                       Patch(color=_clair(ROUGE, 0.25), label=STEG_LIB["total_passifs"]),
                       Patch(color=ROUGE, label=STEG_LIB["emprunts_non_courants"]),
                       Patch(color=_clair(ROUGE, 0.6), label=STEG_LIB["concours_bancaires"])],
              fontsize=7, frameon=False, loc="upper left")
    for ax in axes:
        _style(ax)
        _axe_md(ax, "millions de dinars courants")
    axes[0].set_ylim(0, axes[0].get_ylim()[1] * 1.12)
    axes[2].set_ylim(axes[2].get_ylim()[0], axes[2].get_ylim()[1] * 1.05)
    axes[-1].set_xticks(ans)
    fig.tight_layout()
    return fig


def table_steg_comptes():
    m = _steg().sort_values(["exercice", "grandeur"])
    return pd.DataFrame({
        "Exercice": m["exercice"], "Grandeur": m["grandeur"].map(STEG_LIB),
        "Libellé imprimé": m["libelle_imprime"], "Montant (MD courants)": m["valeur_md"].round(3),
        "Imprimé (dinars)": m["imprime"], "États financiers": m["document"],
        "Colonne": m["colonne"], "Page du fichier": m["page_pdf"]})


# --- 5. Rapports annuels de l'ETAP, 2004-2024 ----------------------------------------------------

def _etap_retenu() -> pd.DataFrame:
    """Un exercice lu dans le rapport de l'exercice, à défaut dans le premier rapport suivant."""
    s = figtools.series(S_ETAP)
    s = s.assign(_propre=(s["exercice_couverture"] == s["exercice"]).astype(int))
    s = s.sort_values(["exercice", "grandeur", "_propre", "exercice_couverture"],
                      ascending=[True, True, False, True])
    return s.groupby(["exercice", "grandeur"], as_index=False).head(1).drop(columns="_propre")


def fig_etap_rapports():
    figtools.apply_lang_font()
    r = _etap_retenu()
    v = {(int(x.exercice), x.grandeur): (float(x.valeur), int(x.exercice_couverture))
         for x in r.itertuples()}
    ans = list(range(min(a for a, _ in v), max(a for a, _ in v) + 1))
    fig, axes = plt.subplots(3, 1, figsize=(9.6, 8.6), sharex=True,
                             gridspec_kw={"height_ratios": [1.2, 1, 0.8]})

    def rapport(a, g):
        ra = v[a, g][1]
        return "" if ra == a else f" — lu dans le rapport de {ra}"

    ax = axes[0]
    for a in ans:
        if (a, "produits_exploitation") in v:
            p = v[a, "produits_exploitation"][0]
            _barre(ax, a, p, _clair(BLEU, 0.35),
                   texte=f"{a} — produits d'exploitation : {_n(p)} MD{rapport(a, 'produits_exploitation')}")
        if (a, "revenus") in v:
            rv = v[a, "revenus"][0]
            _barre(ax, a, rv, BLEU, largeur=0.42,
                   texte=f"{a} — revenus : {_n(rv)} MD{rapport(a, 'revenus')}")
    ax.set_title("Produits d'exploitation et revenus", fontsize=9, loc="left")
    ax.legend(handles=[Patch(color=_clair(BLEU, 0.35), label="produits d'exploitation (total)"),
                       Patch(color=BLEU, label="dont revenus")],
              fontsize=7, frameon=False, loc="upper left")

    ax = axes[1]
    for a in ans:
        if (a, "resultat_net") in v:
            rn = v[a, "resultat_net"][0]
            _barre(ax, a, rn, VERT if rn >= 0 else ROUGE,
                   texte=f"{a} — résultat net : {_n(rn, 1, True)} MD{rapport(a, 'resultat_net')}")
    ax.axhline(0, color=NOIR, lw=0.7)
    ax.set_title("Résultat net", fontsize=9, loc="left")

    ax = axes[2]
    for a in ans:
        if (a, "effectif") in v:
            e = v[a, "effectif"][0]
            _barre(ax, a, e, _clair(VIOLET, 0.7),
                   texte=f"{a} — effectif en fin d'année : {_n(e, 0)} agents{rapport(a, 'effectif')}")
    ax.set_title("Effectif en fin d'année", fontsize=9, loc="left")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    for ax, unite in zip(axes, ("millions de dinars courants", "millions de dinars courants",
                                "agents")):
        _style(ax)
        _axe_md(ax, unite)
    for ax, g in zip(axes, ("produits_exploitation", "resultat_net", "effectif")):
        for a in ans:
            if (a, g) not in v:
                _hors_source(ax, a, "n. d.")
            elif v[a, g][1] != a:
                ax.annotate(f"RA\n{v[a, g][1]}", xy=(a, max(v[a, g][0], 0)), xytext=(0, 2),
                            textcoords="offset points", ha="center", va="bottom", fontsize=6,
                            color=GRIS)
    axes[0].set_ylim(0, axes[0].get_ylim()[1] * 1.15)
    axes[1].set_ylim(axes[1].get_ylim()[0], axes[1].get_ylim()[1] * 1.12)
    axes[2].set_ylim(0, axes[2].get_ylim()[1] * 1.2)
    axes[-1].set_xticks(ans[::2])
    fig.tight_layout()
    return fig


def table_etap_rapports():
    s = figtools.series(S_ETAP)
    r = _etap_retenu()
    retenu = set(zip(r["exercice"], r["grandeur"], r["exercice_couverture"]))
    s = s.sort_values(["exercice", "grandeur", "exercice_couverture"])
    return pd.DataFrame({
        "Exercice": s["exercice"], "Grandeur": s["grandeur"], "Valeur": s["valeur"],
        "Unité": s["unite"], "Rapport annuel de": s["exercice_couverture"],
        "Retenue dans la figure": [(a, g, c) in retenu for a, g, c in
                                   zip(s["exercice"], s["grandeur"], s["exercice_couverture"])],
        "Libellé imprimé": s["libelle_imprime"], "Imprimé": s["imprime"],
        "Page imprimée": s["page_imprimee"], "Page du fichier": s["page_pdf"]})


# --- 6. Fiche du ministère des Finances, par entreprise, 2018-2023 -------------------------------

CREANCIERS = [("dette_etat", "État", VIOLET), ("dette_banques", "banques", BLEU),
              ("dette_entreprises_publiques", "entreprises publiques", ORANGE),
              ("dette_caisses_sociales", "caisses sociales", VERT),
              ("dette_autres", "autres", _clair(GRIS, 0.45))]


def _case_fiche(f, x, e, ind):
    """(valeur, statut, case vide) d'une case de la fiche, ou None si elle n'existe pas."""
    r = f[(f["exercice"] == x) & (f["edition"] == e) & (f["indicateur"] == ind)]
    if r.empty:
        return None
    r = r.iloc[0]
    vide = r["case_vide"] in (True, "True")
    return (None if vide else float(r["valeur"]), r["statut"], vide)


NOMS_FICHE = {"steg": "STEG", "etap": "ETAP", "sncft": "SNCFT", "stir": "STIR",
              "office_cereales": "Office des céréales", "sonede": "SONEDE", "onas": "ONAS",
              "cpg": "CPG", "gct": "GCT",
              "transtu": "Transtu", "tunisie_autoroutes": "Tunisie Autoroutes",
              "tunisair": "Tunisair", "rnta": "RNTA",
              "office_huile": "Office national de l'huile",
              "poste": "Office national des postes",
              "tunisie_telecom": "Tunisie Télécom",
              "office_commerce": "Office du commerce de la Tunisie",
              "attt": "ATTT",
              "oaca": "OACA",
              "ommp": "OMMP",
              "ctn": "CTN",
              "srt_sfax": "Société régionale de transport de Sfax",
              "srt_bizerte": "Société régionale de transport de Bizerte",
              "ctf": "CTF",
              "sndp": "SNDP",
              "sotrapil": "SOTRAPIL",
              "el_fouladh": "El Fouladh",
              "ciments_bizerte": "Ciments de Bizerte",
              "ciments_oum_el_kelil": "Ciments d'Oum El Kélil",
              "sncpa": "SNCPA",
              "afi": "Agence foncière industrielle",
              "regie_alcools": "Régie des alcools",
              "mtk": "Manufacture des tabacs de Kairouan"}
              "otd": "Office des terres domaniales"}
              "pct": "Pharmacie centrale de Tunisie"}
              # Banques publiques (BNA, BFPME, BTS)
              "bna": "BNA", "bfpme": "BFPME", "bts": "BTS"}
              "afh": "Agence foncière d'habitation"}
              "sprols": "SPROLS"}
              "snit": "SNIT"}

# Éditions dont le « total des passifs » imprimé comprend les fonds propres (il égale le total
# des actifs) : la case n'est pas tracée sous le libellé « hors fonds propres ».
PASSIFS_AVEC_FONDS_PROPRES = {("office_commerce", "LF2024"), ("regie_alcools", "LF2024")}
              "stb": "STB",
              "bh": "BH",
              "cpscl": "CPSCL"}

# Éditions dont le « total des passifs » imprimé comprend les fonds propres (il égale le total
# des actifs) : la case n'est pas tracée sous le libellé « hors fonds propres ».
PASSIFS_AVEC_FONDS_PROPRES = {("office_commerce", "LF2024"), ("cpscl", "LF2024")}


def fig_fiche(entite: str):
    figtools.apply_lang_font()
    f = _fiches(entite)
    nom = NOMS_FICHE.get(entite, entite)
    exercices = sorted(int(x) for x in f["exercice"].unique())
    der = {x: f[f["exercice"] == x]["edition"].max() for x in exercices}
    statut = {x: f[(f["exercice"] == x) & (f["edition"] == der[x])]["statut"].iloc[0]
              for x in exercices}

    def court(x, ind_a, ind_b):
        ind = ind_a if der[x] == "LF2022" else ind_b
        if ind == "total_passifs" and (entite, der[x]) in PASSIFS_AVEC_FONDS_PROPRES:
            return None
        return None if ind is None else _case_fiche(f, x, der[x], ind)

    fig = plt.figure(figsize=(11.0, 9.6))
    gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 1])
    ax_p, ax_r = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1])
    ax_b, ax_d = fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])
    ax_e, ax_l = fig.add_subplot(gs[2, 0]), fig.add_subplot(gs[2, 1])
    vides = []

    def groupe(ax, series, titre, signe=False):
        k = len(series)
        larg = 0.8 / k
        for i, (ind_a, ind_b, lib, coul) in enumerate(series):
            for x in exercices:
                c = court(x, ind_a, ind_b)
                xi = x + (i - (k - 1) / 2) * larg
                if c is None:
                    continue
                val, st, vide = c
                if vide:
                    _hors_source(ax, xi, "–")
                    vides.append(f"{lib} {x}")
                    continue
                _barre(ax, xi, val, coul, largeur=larg, ferme=_ferme(st),
                       texte=f"{nom}, {x} — {lib} : {_n(val, 1, signe)} MD, édition "
                             f"{_ed(der[x])}, {st}")
                if val == 0:
                    _zero(ax, xi)
        ax.set_title(titre, fontsize=9, loc="left")
        ax.legend(handles=[Patch(color=c, label=l) for _, _, l, c in series], fontsize=7,
                  frameon=False, loc="upper left")

    groupe(ax_p, [("produits_exploitation", "produits_exploitation", "produits d'exploitation",
                   BLEU),
                  ("subventions_exploitation", "subventions_exploitation",
                   "dont subvention d'exploitation", ORANGE)],
           "Produits et subvention d'exploitation")
    groupe(ax_r, [("resultat_exploitation", "resultat_exploitation", "résultat d'exploitation",
                   _clair(VERT, 0.55)),
                  ("resultat_net", "resultat_net_avant_modifications",
                   "résultat net (avant modifications comptables)", VERT)],
           "Résultats", signe=True)
    groupe(ax_b, [("capitaux_propres", "capitaux_propres_avant_affectation", "fonds propres",
                   VIOLET),
                  ("dette_totale", None, "dette totale (édition LF 2022)", ROUGE),
                  (None, "total_passifs", "total des passifs, hors fonds propres\n"
                                          "(éditions LF 2024 et LF 2025)", _clair(ROUGE, 0.45))],
           "Fonds propres, dette et passifs en fin d'exercice", signe=True)

    # Effectif
    for x in exercices:
        c = court(x, "effectif", "effectif")
        if c is None:
            continue
        val, st, vide = c
        if vide:
            _hors_source(ax_e, x, "–")
            continue
        _barre(ax_e, x, val, _clair(VIOLET, 0.7), ferme=_ferme(st),
               texte=f"{nom}, {x} — effectif : {_n(val, 0)} agents, édition {_ed(der[x])}, {st}")
        ax_e.annotate(_n(val, 0), xy=(x, val), xytext=(0, 2), textcoords="offset points",
                      ha="center", va="bottom", fontsize=6.5)
    ax_e.set_title("Effectif (agents)", fontsize=9, loc="left")

    # Dette par créancier, édition LF 2022
    d22 = sorted(int(x) for x in f[f["edition"] == "LF2022"]["exercice"].unique())
    for x in d22:
        tot = _case_fiche(f, x, "LF2022", "dette_totale")
        if tot is None:
            continue
        if tot[2]:
            ax_d.annotate("non imprimée", xy=(x, 0.02), xycoords=("data", "axes fraction"),
                          ha="center", va="bottom", fontsize=6.5, color=GRIS)
            continue
        bas = 0.0
        for ind, lib, coul in CREANCIERS:
            c = _case_fiche(f, x, "LF2022", ind)
            if c is None or c[2] or c[0] == 0:
                continue
            _barre(ax_d, x, c[0], coul, bas=bas, ferme=_ferme(c[1]), largeur=0.55,
                   texte=f"{nom}, fin {x} — dette envers {lib} : {_n(c[0])} MD")
            bas += c[0]
        trait, = ax_d.plot([x - 0.36, x + 0.36], [tot[0]] * 2, color=NOIR, lw=1.6)
        figtools.infobulle(trait, f"{nom}, fin {x} — dette totale imprimée : {_n(tot[0])} MD")
        ecart = tot[0] - bas
        txt = _n(tot[0])
        if abs(ecart) >= 0.05:
            txt += f"\n(créanciers : {_n(bas)})"
        ax_d.annotate(txt, xy=(x, tot[0]), xytext=(0, 3), textcoords="offset points",
                      ha="center", va="bottom", fontsize=6.5)
    ax_d.set_xticks(d22, [f"fin {x}\n{STATUT.get(statut_ed, statut_ed) or ''}".strip()
                          for x, statut_ed in
                          ((x, f[(f['exercice'] == x) & (f['edition'] == 'LF2022')]['statut'].iloc[0])
                           for x in d22)])
    ax_d.set_xlim(min(d22) - 0.6, max(d22) + 0.6)
    ax_d.set_title("Dette par créancier, édition LF 2022", fontsize=9, loc="left")
    if max((abs(c[0]) for x in d22 if (c := _case_fiche(f, x, "LF2022", "dette_totale"))
            and not c[2]), default=1) == 0:
        # Dette totale imprimée « 0 » chaque année (OMMP) : échelle fixe, sans quoi l'axe
        # dégénère sur un seul zéro.
        ax_d.set_ylim(-1, 10)
        ax_d.set_yticks([0])

    etiquettes = [f"{x}\n{_ed(der[x])}" + (f"\n{STATUT[statut[x]]}" if STATUT.get(statut[x]) else "")
                  for x in exercices]
    for ax in (ax_p, ax_r, ax_b, ax_e, ax_d):
        _style(ax)
        _axe_md(ax, "agents" if ax is ax_e else "MD courants")
        _marges(ax, 0.45 if ax in (ax_b, ax_d) else 0.3)
        if ax is not ax_d:
            ax.set_xticks(exercices, etiquettes)
            ax.set_xlim(min(exercices) - 0.6, max(exercices) + 0.6)
        ax.axhline(0, color=NOIR, lw=0.6)
    ax_l.axis("off")
    leg = ax_l.legend(handles=[Patch(color=c, label=l) for _, l, c in CREANCIERS]
                      + [Line2D([], [], color=NOIR, lw=1.6, label="dette totale imprimée")],
                      title="Dette par créancier", title_fontsize=7.5, fontsize=7.5,
                      frameon=False, loc="upper left", ncol=2, alignment="left")
    ax_l.add_artist(leg)
    ax_l.legend(handles=[_poignee_hachure(), Line2D([], [], color="none",
                         label="« – » : case laissée vide par l'édition"),
                         Line2D([], [], color="none",
                                label="sous l'année : édition retenue et statut du chiffre")],
                fontsize=7.5, frameon=False, loc="lower left")
    fig.tight_layout()
    return fig


def table_fiche(entite: str):
    f = _fiches(entite).sort_values(["exercice", "edition", "rang_colonne"])
    return pd.DataFrame({
        "Exercice": f["exercice"], "Édition": [_ed(e) for e in f["edition"]],
        "Statut": f["statut"], "Grandeur": f["indicateur"].map(LIB).fillna(f["indicateur"]),
        "Valeur": f["valeur"], "Unité": f["unite"], "Imprimé": f["imprime"],
        "Case laissée vide": f["case_vide"], "Libellé arabe": f["libelle_ar"],
        "Page imprimée": f["page_imprimee"], "Page du fichier": f["page_pdf"]})


# --- 7. STIR, Office des céréales : ce que le rapport sur les entreprises publiques en dit -------

def _entite(entite: str):
    t = figtools.series(S_TRANSFERTS_EP)
    t = t[t["entite"] == entite]
    n = _nets()
    n = n[n["entite"] == entite]
    e = figtools.series(S_EFFECTIFS_EP)
    e = e[e["entite"] == entite]
    return t, n, e


def fig_budget(entite: str, couleur, hachure: str = "provisoire"):
    """Transferts du budget, résultat net des classements, effectif et charges de personnel."""
    figtools.apply_lang_font()
    t, n, e = _entite(entite)
    nom = NOMS_FICHE.get(entite, entite)
    fig, axes = plt.subplots(2, 2, figsize=(10.6, 7.0), sharex=True)
    ans = list(range(2016, 2024))

    ax = axes[0, 0]
    for r in _derniere_edition(t, ["annee"]).itertuples():
        ferme = r.statut == "réalisé"
        _barre(ax, r.annee, r.valeur_md, couleur, ferme=ferme,
               texte=f"{nom}, {r.annee} — transferts du budget : "
                     f"{_n(r.valeur_md, 3 if 0 < abs(r.valeur_md) < 0.1 else 1)} MD, édition "
                     f"{_ed(r.edition)}, {r.statut}")
        # Montant de moins de 0,1 MD : écrit avec les décimales imprimées (0,068), pas arrondi.
        dec = 3 if 0 < abs(r.valeur_md) < 0.1 else 1
        ax.annotate(_n(r.valeur_md, dec), xy=(r.annee, r.valeur_md), xytext=(0, 2),
                    textcoords="offset points", ha="center", va="bottom", fontsize=6.5)
        ax.annotate(_ed(r.edition), xy=(r.annee, 0.02), xycoords=("data", "axes fraction"),
                    ha="center", va="bottom", fontsize=5.8, color="white" if ferme else GRIS)
    ax.set_title("Transferts du budget (dernière édition de chaque année)", fontsize=9, loc="left")
    _axe_md(ax, "MD courants")

    ax = axes[0, 1]
    for x in range(2017, 2023):
        vals = _valeurs_distinctes(n[n["exercice"] == x], "valeur_md")
        if vals:
            _sucettes(ax, x, vals, nom)
    ax.axhline(0, color=NOIR, lw=0.7)
    if n.empty:  # l'entreprise n'est dans aucun classement : pas d'échelle à tracer
        ax.set_ylim(-1, 1)
        ax.set_yticks([])
    else:
        lo, hi = ax.get_ylim()
        ax.set_ylim(lo - 0.08 * (hi - lo), max(hi, 0) + 0.1 * (hi - lo))
    for x in range(2017, 2023):
        if n[n["exercice"] == x].empty:
            _hors_source(ax, x, "n. c.")
    ax.set_title("Résultat net (classements des dix premiers résultats)", fontsize=9, loc="left")
    ax.legend(handles=[Line2D([], [], color=COULEUR_EDITION[ed], marker="o", lw=1.1,
                              label=f"édition {_ed(ed)}") for ed in sorted(n["edition"].unique())]
              + [Line2D([], [], color="none", label="n. c. : hors des deux classements")],
              fontsize=6.5, frameon=False, loc="upper left" if n.empty else "lower left")
    _axe_md(ax, "MD courants")

    for ax, col, titre, dec, unite in ((axes[1, 0], "effectif", "Effectif", 0, "agents"),
                                       (axes[1, 1], "charges_personnel_md",
                                        "Charges de personnel", 1, "MD courants")):
        b = _derniere_edition(e[e[col].notna()], ["exercice"])
        for r in b.itertuples():
            val = getattr(r, col)
            ferme = _ferme(r.statut)
            _barre(ax, r.exercice, val, _clair(VIOLET, 0.7), ferme=ferme,
                   texte=f"{nom}, {r.exercice} — {titre.lower()} : {_n(val, dec)} {unite}, "
                         f"édition {_ed(r.edition)}, {r.statut}")
            ax.annotate(_n(val, dec), xy=(r.exercice, val), xytext=(0, 2),
                        textcoords="offset points", ha="center", va="bottom", fontsize=6.5)
        for x in ans:
            if x not in set(int(v) for v in b["exercice"]):
                _hors_source(ax, x, "n. d.")
        ax.set_title(titre, fontsize=9, loc="left")
        _axe_md(ax, unite)
        ax.set_ylim(0, ax.get_ylim()[1] * 1.15)
    for ax in axes.flat:
        _style(ax)
        ax.set_xlim(2015.4, 2023.6)
        ax.set_xticks(ans)
    axes[0, 0].set_ylim(0, axes[0, 0].get_ylim()[1] * 1.1)
    fig.legend(handles=[_poignee_hachure(hachure),
                        Line2D([], [], color="none", label="n. d. : non donné par le rapport")],
               fontsize=7.5, frameon=False, loc="lower center", ncol=2)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    return fig


def table_budget(entite: str):
    t, n, e = _entite(entite)
    lignes = []
    for r in t.sort_values(["annee", "edition"]).itertuples():
        lignes.append(("Transferts du budget", r.annee, _ed(r.edition), r.statut, r.valeur_md,
                       "MD courants", r.imprime, f"{r.tableau}, page du fichier {r.page_pdf}"))
    for r in n.sort_values(["exercice", "edition"]).itertuples():
        lignes.append(("Résultat net (classement)", r.exercice, _ed(r.edition), "non dit",
                       r.valeur_md, "MD courants", r.imprime, f"p. {r.page_imprimee}"))
    for r in e.sort_values(["exercice", "edition"]).itertuples():
        page = f"p. {int(r.page_imprimee)}" if r.page_imprimee == r.page_imprimee else \
            f"page du fichier {r.page_pdf}"
        lignes.append(("Effectif", r.exercice, _ed(r.edition), r.statut, r.effectif, "agents",
                       r.effectif_imprime, page))
        if r.charges_personnel_md == r.charges_personnel_md:
            lignes.append(("Charges de personnel", r.exercice, _ed(r.edition), r.statut,
                           r.charges_personnel_md, "MD courants", r.charges_personnel_imprime,
                           page))
    return pd.DataFrame(lignes, columns=["Grandeur", "Exercice", "Édition", "Statut", "Valeur",
                                         "Unité", "Imprimé", "Localisation"])


# --- 8. Banques publiques : tableau des indicateurs du rapport (mise en page « banques ») -------

LIB_BQ = {
    "total_actifs": "Total des actifs (MD)",
    "bq_engagements_clientele": "Engagements sur la clientèle (MD)",
    "bq_depots_clientele": "Dépôts et avoirs de la clientèle (MD)",
    "bq_produit_net_bancaire": "Produit net bancaire (MD)",
    "bq_resultat_exploitation": "Résultat d'exploitation (MD)",
    "bq_provisions_nettes": "Provisions nettes sur engagements (MD)",
    "resultat_net": "Résultat net (MD)",
    "bq_dividende_par_action": "Dividende par action (dinars)",
    "bq_dividendes_etat": "Part de l'État dans les dividendes (MD)",
    "bq_coefficient_exploitation": "Coefficient d'exploitation (%)",
    "bq_taux_creances_classees": "Créances classées, en part des engagements (%)",
    "bq_couverture_creances_classees": "Couverture des créances classées par les provisions (%)",
    "bq_ratio_solvabilite": "Ratio de solvabilité (%, minimum 10)",
    "bq_ratio_tier1": "Ratio Tier 1 (%, minimum 7)",
    "bq_ratio_lcr": "Ratio de liquidité LCR (%, minimum 90 en 2018, 100 depuis 2019)",
    "charges_personnel": "Charges de personnel (MD)",
    "effectif": "Effectif (agents)",
}
ORDRE_BQ = list(LIB_BQ)


def tableau_banque_detail(entite: str, editions: tuple[str, ...], caption: str,
                          tbl_id: str) -> None:
    """Le tableau des banques publiques, une colonne par (exercice, édition) ; unité par ligne."""
# --- Banques publiques (BNA, BFPME, BTS) : début du bloc ----------------------------------------
# Tableau des banques publiques du rapport sur les entreprises publiques (mise en page « banques
# publiques », codes `bq_`) : ni bilan ni compte de résultat d'entreprise, d'où une figure et un
# tableau propres. Une figure lit une seule famille (fiches du ministère des Finances).

LIB.update({
    "bq_total_actifs": "Total des actifs", "bq_engagements_clientele": "Engagements sur la clientèle",
    "bq_depots_clientele": "Dépôts de la clientèle", "bq_produit_net_bancaire": "Produit net bancaire",
    "bq_resultat_exploitation": "Résultat d'exploitation",
    "bq_provisions_nettes_engagements": "Provisions nettes sur engagements",
    "bq_resultat_net": "Résultat net", "bq_dividende_par_action": "Dividende par action (dinars)",
    "bq_dividendes_etat": "Part de l'État dans les dividendes",
    "bq_coefficient_exploitation": "Coefficient d'exploitation (%)",
    "bq_taux_creances_classees": "Taux de créances classées (%)",
    "bq_couverture_creances_classees": "Couverture des créances classées par les provisions (%)",
    "bq_ratio_solvabilite": "Ratio de solvabilité (%, minimum 10)",
    "bq_ratio_tier1": "Ratio Tier 1 (%, minimum 7)",
    "bq_ratio_lcr": "Ratio de liquidité LCR (%, minimum 100)",
})
ORDRE_BQ = ["bq_total_actifs", "bq_engagements_clientele", "bq_depots_clientele",
            "bq_produit_net_bancaire", "bq_resultat_exploitation",
            "bq_provisions_nettes_engagements", "bq_resultat_net", "bq_dividende_par_action",
            "bq_dividendes_etat", "bq_coefficient_exploitation", "bq_taux_creances_classees",
            "bq_couverture_creances_classees", "bq_ratio_solvabilite", "bq_ratio_tier1",
            "bq_ratio_lcr", "charges_personnel", "effectif"]
BQ_DEC = {"bq_dividende_par_action": 3, "bq_dividendes_etat": 2}

# Changement de définition entre deux éditions, d'après la note imprimée sous le tableau
# (édition LF 2025, p. 30) : la BTS ne range plus les crédits et ressources spéciales dans les
# dépôts. La figure marque la rupture au lieu de rapprocher les deux définitions.
RUPTURE_DEPOTS = {"bts": "dépôts : définition de l'édition LF 2025,\nhors crédits et ressources "
                         "spéciales"}


def tableau_fiche_banque(entite: str, editions: tuple[str, ...], caption: str,
                         tbl_id: str) -> None:
    """Toutes les grandeurs imprimées du tableau des banques, une colonne par (exercice, édition)."""
    f = _fiches(entite)
    f = f[f["edition"].isin(editions)]
    cols = sorted({(x, e) for x, e in zip(f["exercice"], f["edition"])})
    lignes = []
    for ind in ORDRE_BQ:
        if ind not in set(f["indicateur"]):
            continue
        cases = []
        for x, e in cols:
            r = f[(f["exercice"] == x) & (f["edition"] == e) & (f["indicateur"] == ind)]
            if r.empty:
                cases.append("—")
                continue
            r = r.iloc[0]
            if r["case_vide"] in (True, "True"):
                cases.append("–")
                continue
            imp = str(r["imprime"]).replace(" ", "")
            dec = len(imp.split(",")[1]) if "," in imp else 0
            cases.append(_n(r["valeur"], dec))
        lignes.append([LIB_BQ[ind]] + cases)
            elif r.iloc[0]["case_vide"] in (True, "True"):
                cases.append("–")
            else:
                imp = str(r.iloc[0]["imprime"])
                dec = 0 if ind == "effectif" or ("," not in imp and "." not in imp) else \
                    BQ_DEC.get(ind, 1)
                cases.append(_n(r.iloc[0]["valeur"], dec))
        lignes.append([LIB[ind]] + cases)
    ent = []
    for x, e in cols:
        st = f[(f["exercice"] == x) & (f["edition"] == e)]["statut"].iloc[0]
        st = STATUT.get(st, st)
        ent.append(f"{x}<br>({_ed(e)}{', ' + st if st else ''})")
    _md(["Grandeur (unité)"] + ent, "g" + "d" * len(cols), lignes, caption, tbl_id)


def fig_banque(entite: str):
    """Une banque publique d'après le tableau des indicateurs du rapport : chaque exercice dans
    la dernière édition qui le donne ; ratios avec les minimums imprimés en tête de colonne."""
    figtools.apply_lang_font()
    f = _fiches(entite)
    nom = NOMS_FICHE.get(entite, entite)
    exercices = sorted(int(x) for x in f["exercice"].unique())
    der = {x: f[f["exercice"] == x]["edition"].max() for x in exercices}
    statut = {x: f[(f["exercice"] == x) & (f["edition"] == der[x])]["statut"].iloc[0]
              for x in exercices}

    def case(x, ind):
        return _case_fiche(f, x, der[x], ind)

    fig = plt.figure(figsize=(11.0, 9.6))
    gs = fig.add_gridspec(3, 2)
    ax_r, ax_b = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1])
    ax_s, ax_c = fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])
    ax_l, ax_e = fig.add_subplot(gs[2, 0]), fig.add_subplot(gs[2, 1])

    def groupe(ax, series, unite, ecrire=False, dec=1):
    _md(["Millions de dinars, sauf mention"] + ent, "g" + "d" * len(cols), lignes, caption,
        tbl_id)


def fig_fiche_banque(entite: str):
    figtools.apply_lang_font()
    f = _fiches(entite)
    nom = NOMS_FICHE.get(entite, entite)
    # Exercices dont la dernière édition imprime au moins une valeur (BFPME : la ligne « juin
    # 2020 » de l'édition LF 2022, toute en « - », cède la place à l'édition LF 2024).
    pleines = f[~f["case_vide"].isin([True, "True"])]
    exercices = sorted(int(x) for x in pleines["exercice"].unique())
    der = {x: pleines[pleines["exercice"] == x]["edition"].max() for x in exercices}
    statut = {x: f[(f["exercice"] == x) & (f["edition"] == der[x])]["statut"].iloc[0]
              for x in exercices}

    fig = plt.figure(figsize=(11.0, 12.4))
    gs = fig.add_gridspec(4, 2)
    axes = [fig.add_subplot(gs[i, j]) for i in range(4) for j in range(2)]
    ax_bil, ax_res, ax_prov, ax_solv, ax_qual, ax_lcr, ax_eff, ax_leg = axes

    def barres(ax, series, titre, unite="MD", signe=False):
        k = len(series)
        larg = 0.8 / k
        for i, (ind, lib, coul) in enumerate(series):
            for x in exercices:
                c = case(x, ind)
                if c is None:
                    continue
                xi = x + (i - (k - 1) / 2) * larg
                c = _case_fiche(f, x, der[x], ind)
                xi = x + (i - (k - 1) / 2) * larg
                if c is None:
                    continue
                val, st, vide = c
                if vide:
                    _hors_source(ax, xi, "–")
                    continue
                _barre(ax, xi, val, coul, largeur=larg, ferme=_ferme(st),
                       texte=f"{nom}, {x} — {lib} : {_n(val, dec)} {unite}, édition "
                             f"{_ed(der[x])}")
                if ecrire:
                    ax.annotate(_n(val, dec), xy=(xi, val), xytext=(0, 2),
                                textcoords="offset points", ha="center",
                                va="bottom" if val >= 0 else "top", fontsize=6)
                if val == 0:
                    _zero(ax, xi)
        ax.legend(handles=[Patch(color=c, label=l) for _, l, c in series], fontsize=7,
                  frameon=False, loc="upper left")

    groupe(ax_r, [("bq_produit_net_bancaire", "produit net bancaire", BLEU),
                  ("bq_resultat_exploitation", "résultat d'exploitation (LF 2024 et LF 2025)",
                   _clair(VERT, 0.55)),
                  ("resultat_net", "résultat net", VERT)], "MD", ecrire=True, dec=0)
    ax_r.set_title("Produit net bancaire et résultats", fontsize=9, loc="left")
    groupe(ax_b, [("total_actifs", "total des actifs", GRIS),
                  ("bq_engagements_clientele", "engagements sur la clientèle", ORANGE),
                  ("bq_depots_clientele", "dépôts de la clientèle", VIOLET)], "MD", dec=0)
    ax_b.set_title("Bilan : actifs, engagements et dépôts de la clientèle", fontsize=9,
                   loc="left")
    groupe(ax_s, [("bq_ratio_solvabilite", "solvabilité", BLEU),
                  ("bq_ratio_tier1", "Tier 1", _clair(BLEU, 0.5))], "%", ecrire=True)
    ax_s.axhline(10, color=ROUGE, lw=0.8, ls="--")
    ax_s.axhline(7, color=ROUGE, lw=0.8, ls=":")
    ax_s.legend(handles=[Patch(color=BLEU, label="solvabilité"),
                         Patch(color=_clair(BLEU, 0.5), label="Tier 1"),
                         Line2D([], [], color=ROUGE, lw=0.8, ls="--",
                                label="minimum de solvabilité : 10 %"),
                         Line2D([], [], color=ROUGE, lw=0.8, ls=":",
                                label="minimum Tier 1 : 7 %")],
                fontsize=7, frameon=False, loc="upper left", ncol=2)
    ax_s.set_title("Fonds propres réglementaires", fontsize=9, loc="left")
    groupe(ax_c, [("bq_taux_creances_classees", "créances classées / engagements", ROUGE),
                  ("bq_couverture_creances_classees", "couverture par les provisions",
                   _clair(ROUGE, 0.45))], "%", ecrire=True)
    ax_c.set_title("Créances classées", fontsize=9, loc="left")
    groupe(ax_l, [("bq_ratio_lcr", "LCR", _clair(VERT, 0.7))], "%", ecrire=True)
    ax_l.plot([2017.6, 2018.4], [90, 90], color=ROUGE, lw=0.8, ls="--")
    ax_l.plot([2018.6, max(exercices) + 0.4], [100, 100], color=ROUGE, lw=0.8, ls="--")
    ax_l.legend(handles=[Patch(color=_clair(VERT, 0.7), label="LCR"),
                         Line2D([], [], color=ROUGE, lw=0.8, ls="--",
                                label="minimum : 90 % en 2018, 100 % depuis 2019")],
                fontsize=7, frameon=False, loc="upper left")
    ax_l.set_title("Liquidité (LCR)", fontsize=9, loc="left")
    groupe(ax_e, [("effectif", "effectif", _clair(VIOLET, 0.7))], "agents", ecrire=True, dec=0)
    ax_e.get_legend().remove()
    ax_e.set_title("Effectif (agents)", fontsize=9, loc="left")

    etiquettes = [f"{x}\n{_ed(der[x])}" + (f"\n{STATUT[statut[x]]}" if STATUT.get(statut[x]) else "")
                  for x in exercices]
    for ax, unite in ((ax_r, "MD courants"), (ax_b, "MD courants"), (ax_s, "%"), (ax_c, "%"),
                      (ax_l, "%"), (ax_e, "agents")):
        _style(ax)
        _axe_md(ax, unite)
        _marges(ax, 0.35)
        ax.set_xticks(exercices, etiquettes)
        ax.set_xlim(min(exercices) - 0.6, max(exercices) + 0.6)
        ax.axhline(0, color=NOIR, lw=0.6)
    fig.legend(handles=[_poignee_hachure(),
                        Line2D([], [], color="none",
                               label="sous l'année : édition retenue (la dernière qui donne "
                                     "l'exercice)")],
               fontsize=7.5, frameon=False, loc="lower center", ncol=2)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    return fig


def table_banque(entite: str):
    f = _fiches(entite).sort_values(["exercice", "edition", "rang_colonne"])
    return pd.DataFrame({
        "Exercice": f["exercice"], "Édition": [_ed(e) for e in f["edition"]],
        "Statut": f["statut"], "Grandeur": f["indicateur"].map(LIB_BQ).fillna(f["indicateur"]),
        "Valeur": f["valeur"], "Unité": f["unite"], "Imprimé": f["imprime"],
        "Case laissée vide": f["case_vide"], "Libellé arabe": f["libelle_ar"],
        "Page imprimée": f["page_imprimee"], "Page du fichier": f["page_pdf"]})
                       texte=f"{nom}, {x} — {lib} : {_n(val, 1, signe)} {unite}, édition "
                             f"{_ed(der[x])}, {st}")
                if val == 0:
                    _zero(ax, xi)
        ax.set_title(titre, fontsize=9, loc="left")
        ax.legend(handles=[Patch(color=c, label=l) for _, l, c in series], fontsize=7,
                  frameon=False, loc="upper left")

    def points(ax, series, titre, seuils=()):
        k = len(series)
        for i, (ind, lib, coul, marque) in enumerate(series):
            for x in exercices:
                c = _case_fiche(f, x, der[x], ind)
                xi = x + (i - (k - 1) / 2) * 0.18
                if c is None:
                    continue
                val, st, vide = c
                if vide:
                    _hors_source(ax, xi, "–")
                    continue
                _point(ax, xi, val, coul, ferme=_ferme(st), marque=marque,
                       texte=f"{nom}, {x} — {lib} : {_n(val, 1)} %, édition {_ed(der[x])}, {st}")
        for j, (s, lib) in enumerate(seuils):
            ax.axhline(s, color=GRIS, lw=0.8, ls="--")
            # Deux seuils proches (10 % et 7 %) : l'un au-dessus de sa ligne, l'autre dessous.
            ax.annotate(lib, xy=(1, s), xycoords=("axes fraction", "data"),
                        xytext=(-2, 2 if j == 0 else -2), textcoords="offset points",
                        ha="right", va="bottom" if j == 0 else "top", fontsize=6.5, color=GRIS)
        ax.set_title(titre, fontsize=9, loc="left")
        ax.legend(handles=[Line2D([], [], color=c, marker=m, lw=0, label=l)
                           for _, l, c, m in series], fontsize=7, frameon=False,
                  loc="upper left")

    barres(ax_bil, [("bq_total_actifs", "total des actifs", _clair(BLEU, 0.45)),
                    ("bq_engagements_clientele", "engagements sur la clientèle", BLEU),
                    ("bq_depots_clientele", "dépôts de la clientèle", VERT)],
           "Bilan en fin d'exercice")
    if entite in RUPTURE_DEPOTS:
        x25 = [x for x in exercices if der[x] == "LF2025"]
        if x25 and min(x25) > min(exercices):
            xr = min(x25) - 0.5
            ax_bil.axvline(xr, color=NOIR, lw=0.9, ls=":")
            ax_bil.annotate(RUPTURE_DEPOTS[entite], xy=(xr, 0.99),
                            xycoords=("data", "axes fraction"), xytext=(4, 0),
                            textcoords="offset points", ha="left", va="top", fontsize=6.3)
    barres(ax_res, [("bq_produit_net_bancaire", "produit net bancaire", BLEU),
                    ("bq_resultat_exploitation", "résultat d'exploitation", _clair(VERT, 0.55)),
                    ("bq_resultat_net", "résultat net", VERT)],
           "Produit net bancaire et résultats", signe=True)
    barres(ax_prov, [("bq_provisions_nettes_engagements", "provisions nettes sur engagements",
                      ORANGE),
                     ("bq_dividendes_etat", "part de l'État dans les dividendes", VIOLET)],
           "Provisions et dividendes versés à l'État", signe=True)
    points(ax_solv, [("bq_ratio_solvabilite", "ratio de solvabilité", VIOLET, "o"),
                     ("bq_ratio_tier1", "ratio Tier 1", BLEU, "s")],
           "Fonds propres réglementaires (%)", seuils=((10, "minimum 10 %"), (7, "minimum 7 %")))
    points(ax_qual, [("bq_taux_creances_classees", "taux de créances classées", ROUGE, "o"),
                     ("bq_couverture_creances_classees", "couverture par les provisions",
                      ORANGE, "s"),
                     ("bq_coefficient_exploitation", "coefficient d'exploitation", GRIS, "D")],
           "Créances classées et coefficient d'exploitation (%)")
    points(ax_lcr, [("bq_ratio_lcr", "ratio de liquidité LCR", BLEU, "o")],
           "Liquidité à court terme (%)", seuils=((100, "minimum 100 % (90 % en 2018)"),))
    if not any(_case_fiche(f, x, der[x], "bq_ratio_lcr") and not
               _case_fiche(f, x, der[x], "bq_ratio_lcr")[2] for x in exercices):
        ax_lcr.annotate("LCR non imprimé (« – » à chaque exercice)", xy=(0.5, 0.85),
                        xycoords="axes fraction", ha="center", fontsize=7.5, color=GRIS)
        ax_lcr.set_ylim(0, 150)

    for x in exercices:
        c = _case_fiche(f, x, der[x], "effectif")
        if c is None or c[2]:
            continue
        _barre(ax_eff, x, c[0], _clair(VIOLET, 0.7), ferme=_ferme(c[1]),
               texte=f"{nom}, {x} — effectif : {_n(c[0], 0)} agents, édition {_ed(der[x])}, "
                     f"{c[1]}")
        ax_eff.annotate(_n(c[0], 0), xy=(x, c[0]), xytext=(0, 2), textcoords="offset points",
                        ha="center", va="bottom", fontsize=6.5)
    ax_eff.set_title("Effectif (agents)", fontsize=9, loc="left")

    etiquettes = [f"{x}\n{_ed(der[x])}" + (f"\n{STATUT[statut[x]]}" if STATUT.get(statut[x]) else "")
                  for x in exercices]
    for ax in axes[:-1]:
        _style(ax)
        _axe_md(ax, "agents" if ax is ax_eff else ("%" if ax in (ax_solv, ax_qual, ax_lcr)
                                                    else "MD courants"))
        _marges(ax, 0.45)
        ax.set_xticks(exercices, etiquettes)
        ax.set_xlim(min(exercices) - 0.6, max(exercices) + 0.6)
        if ax not in (ax_lcr,):
            ax.axhline(0, color=NOIR, lw=0.6)
    ax_leg.axis("off")
    ax_leg.legend(handles=[_poignee_hachure(), Line2D([], [], color="none",
                           label="marque creuse : chiffre provisoire ou estimé"),
                           Line2D([], [], color="none",
                                  label="« – » : case laissée vide par l'édition"),
                           Line2D([], [], color="none",
                                  label="sous l'année : édition retenue et statut du chiffre")],
                  fontsize=7.5, frameon=False, loc="upper left")
    fig.tight_layout()
    return fig
# --- Banques publiques (BNA, BFPME, BTS) : fin du bloc ------------------------------------------


# --- point d'entrée ------------------------------------------------------------------------------

FIGURES = {
    "transferts": (fig_transferts, table_transferts, (S_TRANSFERTS_EP,),
                   "fig_ep_ge_transferts"),
    "resultats": (fig_resultats, table_resultats, (S_NETS_EP,), "fig_ep_ge_resultats"),
    "revisions": (fig_revisions, table_revisions, (S_TRANSFERTS_EP,), "fig_ep_ge_revisions"),
    "steg_comptes": (fig_steg_comptes, table_steg_comptes, (S_STEG,), "fig_ep_steg_comptes"),
    "etap_rapports": (fig_etap_rapports, table_etap_rapports, (S_ETAP,), "fig_ep_etap_rapports"),
    "steg_fiches": (lambda: fig_fiche("steg"), lambda: table_fiche("steg"), (S_FICHES,),
                    "fig_ep_steg_fiches"),
    "etap_fiches": (lambda: fig_fiche("etap"), lambda: table_fiche("etap"), (S_FICHES,),
                    "fig_ep_etap_fiches"),
    "sncft_fiches": (lambda: fig_fiche("sncft"), lambda: table_fiche("sncft"), (S_FICHES,),
                     "fig_ep_sncft_fiches"),
    "stir_fiches": (lambda: fig_fiche("stir"), lambda: table_fiche("stir"), (S_FICHES,),
                    "fig_ep_stir_fiches"),
    "stir_budget": (lambda: fig_budget("stir", ORANGE), lambda: table_budget("stir"),
                    (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_stir_budget"),
    "oc_fiches": (lambda: fig_fiche("office_cereales"), lambda: table_fiche("office_cereales"),
                  (S_FICHES,), "fig_ep_oc_fiches"),
    "oc_budget": (lambda: fig_budget("office_cereales", VERT),
                  lambda: table_budget("office_cereales"),
                  (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_oc_budget"),
    "sonede_fiches": (lambda: fig_fiche("sonede"), lambda: table_fiche("sonede"), (S_FICHES,),
                      "fig_ep_sonede_fiches"),
    "sonede_budget": (lambda: fig_budget("sonede", BLEU,
                                         "provisoire, estimé ou comptes non approuvés"),
                      lambda: table_budget("sonede"),
                      (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_sonede_budget"),
    "onas_fiches": (lambda: fig_fiche("onas"), lambda: table_fiche("onas"), (S_FICHES,),
                    "fig_ep_onas_fiches"),
    "onas_budget": (lambda: fig_budget("onas", ROUGE), lambda: table_budget("onas"),
                    (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_onas_budget"),
    "cpg_fiches": (lambda: fig_fiche("cpg"), lambda: table_fiche("cpg"), (S_FICHES,),
                   "fig_ep_cpg_fiches"),
    "gct_fiches": (lambda: fig_fiche("gct"), lambda: table_fiche("gct"), (S_FICHES,),
                   "fig_ep_gct_fiches"),
    "transtu_fiches": (lambda: fig_fiche("transtu"), lambda: table_fiche("transtu"),
                       (S_FICHES,), "fig_ep_transtu_fiches"),
    "transtu_budget": (lambda: fig_budget("transtu", ORANGE, "provisoire ou probable"),
                       lambda: table_budget("transtu"),
                       (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_transtu_budget"),
    "autoroutes_fiches": (lambda: fig_fiche("tunisie_autoroutes"),
                          lambda: table_fiche("tunisie_autoroutes"), (S_FICHES,),
                          "fig_ep_autoroutes_fiches"),
    "autoroutes_budget": (lambda: fig_budget("tunisie_autoroutes", BLEU),
                          lambda: table_budget("tunisie_autoroutes"),
                          (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_autoroutes_budget"),
    "tunisair_fiches": (lambda: fig_fiche("tunisair"), lambda: table_fiche("tunisair"),
                        (S_FICHES,), "fig_ep_tunisair_fiches"),
    "tunisair_budget": (lambda: fig_budget("tunisair", BLEU, "provisoire, estimé ou probable"),
                        lambda: table_budget("tunisair"),
                        (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_tunisair_budget"),
    "rnta_fiches": (lambda: fig_fiche("rnta"), lambda: table_fiche("rnta"), (S_FICHES,),
                    "fig_ep_rnta_fiches"),
    "rnta_budget": (lambda: fig_budget("rnta", ORANGE), lambda: table_budget("rnta"),
                    (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_rnta_budget"),
    "onh_fiches": (lambda: fig_fiche("office_huile"), lambda: table_fiche("office_huile"),
                   (S_FICHES,), "fig_ep_onh_fiches"),
    "onh_budget": (lambda: fig_budget("office_huile", COULEURS_TRANSFERTS["office_huile"]),
                   lambda: table_budget("office_huile"),
                   (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_onh_budget"),
    "poste_fiches": (lambda: fig_fiche("poste"), lambda: table_fiche("poste"), (S_FICHES,),
                     "fig_ep_poste_fiches"),
    "poste_budget": (lambda: fig_budget("poste", VIOLET), lambda: table_budget("poste"),
                     (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_poste_budget"),
    "tt_fiches": (lambda: fig_fiche("tunisie_telecom"), lambda: table_fiche("tunisie_telecom"),
                  (S_FICHES,), "fig_ep_tt_fiches"),
    "otc_fiches": (lambda: fig_fiche("office_commerce"), lambda: table_fiche("office_commerce"),
                   (S_FICHES,), "fig_ep_otc_fiches"),
    "otc_budget": (lambda: fig_budget("office_commerce", VERT), lambda: table_budget("office_commerce"),
                   (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_otc_budget"),
    "attt_fiches": (lambda: fig_fiche("attt"), lambda: table_fiche("attt"), (S_FICHES,),
                    "fig_ep_attt_fiches"),
    "oaca_fiches": (lambda: fig_fiche("oaca"), lambda: table_fiche("oaca"), (S_FICHES,),
                    "fig_ep_oaca_fiches"),
    "ommp_fiches": (lambda: fig_fiche("ommp"), lambda: table_fiche("ommp"), (S_FICHES,),
                    "fig_ep_ommp_fiches"),
    "ctn_fiches": (lambda: fig_fiche("ctn"), lambda: table_fiche("ctn"), (S_FICHES,),
                   "fig_ep_ctn_fiches"),
    "ctn_budget": (lambda: fig_budget("ctn", BLEU, "provisoire, estimé ou probable"),
                   lambda: table_budget("ctn"),
                   (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_ctn_budget"),
    "srt_sfax_fiches": (lambda: fig_fiche("srt_sfax"), lambda: table_fiche("srt_sfax"),
                        (S_FICHES,), "fig_ep_srt_sfax_fiches"),
    "srt_sfax_budget": (lambda: fig_budget("srt_sfax", BLEU), lambda: table_budget("srt_sfax"),
                        (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_srt_sfax_budget"),
    "srt_bizerte_fiches": (lambda: fig_fiche("srt_bizerte"), lambda: table_fiche("srt_bizerte"),
                           (S_FICHES,), "fig_ep_srt_bizerte_fiches"),
    "srt_bizerte_budget": (lambda: fig_budget("srt_bizerte", VERT),
                           lambda: table_budget("srt_bizerte"),
                           (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP),
                           "fig_ep_srt_bizerte_budget"),
    "ctf_fiches": (lambda: fig_fiche("ctf"), lambda: table_fiche("ctf"), (S_FICHES,),
                   "fig_ep_ctf_fiches"),
    "sndp_fiches": (lambda: fig_fiche("sndp"), lambda: table_fiche("sndp"), (S_FICHES,),
                    "fig_ep_sndp_fiches"),
    "sotrapil_fiches": (lambda: fig_fiche("sotrapil"), lambda: table_fiche("sotrapil"),
                        (S_FICHES,), "fig_ep_sotrapil_fiches"),
    "fouladh_fiches": (lambda: fig_fiche("el_fouladh"), lambda: table_fiche("el_fouladh"),
                       (S_FICHES,), "fig_ep_fouladh_fiches"),
    "fouladh_budget": (lambda: fig_budget("el_fouladh", ORANGE, "provisoire ou probable"),
                       lambda: table_budget("el_fouladh"),
                       (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_fouladh_budget"),
    "cimbiz_fiches": (lambda: fig_fiche("ciments_bizerte"), lambda: table_fiche("ciments_bizerte"),
                      (S_FICHES,), "fig_ep_cimbiz_fiches"),
    "cimbiz_budget": (lambda: fig_budget("ciments_bizerte", BLEU),
                      lambda: table_budget("ciments_bizerte"),
                      (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_cimbiz_budget"),
    "cimoek_fiches": (lambda: fig_fiche("ciments_oum_el_kelil"),
                      lambda: table_fiche("ciments_oum_el_kelil"), (S_FICHES,),
                      "fig_ep_cimoek_fiches"),
    "sncpa_fiches": (lambda: fig_fiche("sncpa"), lambda: table_fiche("sncpa"), (S_FICHES,),
                     "fig_ep_sncpa_fiches"),
    "sncpa_budget": (lambda: fig_budget("sncpa", VERT, "provisoire ou probable"),
                     lambda: table_budget("sncpa"),
                     (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_sncpa_budget"),
    "afi_fiches": (lambda: fig_fiche("afi"), lambda: table_fiche("afi"), (S_FICHES,),
                   "fig_ep_afi_fiches"),
    "afi_budget": (lambda: fig_budget("afi", BLEU), lambda: table_budget("afi"),
                   (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_afi_budget"),
    "ra_fiches": (lambda: fig_fiche("regie_alcools"), lambda: table_fiche("regie_alcools"),
                  (S_FICHES,), "fig_ep_ra_fiches"),
    "ra_budget": (lambda: fig_budget("regie_alcools", VIOLET), lambda: table_budget("regie_alcools"),
                  (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_ra_budget"),
    "mtk_fiches": (lambda: fig_fiche("mtk"), lambda: table_fiche("mtk"), (S_FICHES,),
                   "fig_ep_mtk_fiches"),
    "mtk_budget": (lambda: fig_budget("mtk", ORANGE), lambda: table_budget("mtk"),
                   (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_mtk_budget"),
    "otd_fiches": (lambda: fig_fiche("otd"), lambda: table_fiche("otd"), (S_FICHES,),
                   "fig_ep_otd_fiches"),
    "otd_budget": (lambda: fig_budget("otd", VERT), lambda: table_budget("otd"),
                   (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_otd_budget"),
    "pct_fiches": (lambda: fig_fiche("pct"), lambda: table_fiche("pct"), (S_FICHES,),
                   "fig_ep_pct_fiches"),
    "pct_budget": (lambda: fig_budget("pct", VERT), lambda: table_budget("pct"),
                   (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_pct_budget"),
    "stb_fiches": (lambda: fig_banque("stb"), lambda: table_banque("stb"), (S_FICHES,),
                   "fig_ep_stb_fiches"),
    "bh_fiches": (lambda: fig_banque("bh"), lambda: table_banque("bh"), (S_FICHES,),
                  "fig_ep_bh_fiches"),
    "bh_budget": (lambda: fig_budget("bh", BLEU), lambda: table_budget("bh"),
                  (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_bh_budget"),
    "cpscl_fiches": (lambda: fig_fiche("cpscl"), lambda: table_fiche("cpscl"), (S_FICHES,),
                     "fig_ep_cpscl_fiches"),
    "cpscl_budget": (lambda: fig_budget("cpscl", VERT), lambda: table_budget("cpscl"),
                     (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_cpscl_budget"),
    # Banques publiques (BNA, BFPME, BTS)
    "bna_fiches": (lambda: fig_fiche_banque("bna"), lambda: table_fiche("bna"), (S_FICHES,),
                   "fig_ep_bna_fiches"),
    "bfpme_fiches": (lambda: fig_fiche_banque("bfpme"), lambda: table_fiche("bfpme"),
                     (S_FICHES,), "fig_ep_bfpme_fiches"),
    "bfpme_budget": (lambda: fig_budget("bfpme", BLEU), lambda: table_budget("bfpme"),
                     (S_TRANSFERTS_EP, S_NETS_EP, S_EFFECTIFS_EP), "fig_ep_bfpme_budget"),
    "bts_fiches": (lambda: fig_fiche_banque("bts"), lambda: table_fiche("bts"), (S_FICHES,),
                   "fig_ep_bts_fiches"),
    "afh_fiches": (lambda: fig_fiche("afh"), lambda: table_fiche("afh"), (S_FICHES,),
                   "fig_ep_afh_fiches"),
    "sprols_fiches": (lambda: fig_fiche("sprols"), lambda: table_fiche("sprols"), (S_FICHES,),
                      "fig_ep_sprols_fiches"),
    "snit_fiches": (lambda: fig_fiche("snit"), lambda: table_fiche("snit"), (S_FICHES,),
                    "fig_ep_snit_fiches"),
}


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Trace la figure `nom` en onglets (chunk `output: asis`, étiqueté `fig-…`)."""
    trace, table, series, slug = FIGURES[nom]
    figtools.figure_tabs(trace(), table(), *series, slug=slug, caption=caption,
                         note_lecture=note_lecture)
    plt.close("all")

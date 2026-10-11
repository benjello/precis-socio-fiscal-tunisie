"""Figures et tableaux du livre *Les entreprises publiques*.

    from figures import entreprises_publiques as ep
    ep.figure("ensemble", caption=…, note_lecture=…)     # quatre grandeurs, 2016-2024
    ep.figure("transferts", …)                           # transferts du budget, annexe 8
    ep.figure("garanties", …)                            # plafond, garanties, encours
    ep.figure("flux", …)                                 # versements et transferts, échantillon
    ep.figure("resultats", …)                            # résultats agrégés, par édition
    ep.figure("cessions", …)                             # recettes de cession, 1987-2009
    ep.tableau_transferts(caption=…) …                   # tableaux, tous lus dans les séries

D'OÙ VIENNENT LES DONNÉES. Onze séries de `tunisia-data`, lues par `figtools.series()`
(l'entrepôt s'il est installé, sinon le cache `precis/_seriescache/`), et l'indice des prix
commun du précis (`dinars_constants`). Rien n'est saisi ici : ni valeur, ni page.

RÈGLES COMMUNES.

  - **Aucune série ne se chaîne d'une édition à l'autre.** Le rapport sur les entreprises
    publiques change d'échantillon à chaque édition : une édition = un segment, deux
    exercices reliés entre eux et à rien d'autre.
  - **Pour le rapport sur les transferts et les garanties**, dont le total est homogène
    depuis l'édition LF 2021, une année est donnée dans la dernière édition qui la porte en
    réalisation ; 2016 n'existe que dans l'ancien périmètre et reste isolée.
  - **Ce qui n'est pas une réalisation est en marque creuse** : loi de finances, valeur
    provisoire, estimation de fin juin, dividende partiel.
  - **Dinars constants** : dinars de l'année de base commune (`dinars_constants.ANNEE_BASE`),
    par l'indice des prix à la consommation.

Les libellés sont en français : le livre arabe n'existe pas encore. Ils sont réunis dans
`LIB` pour qu'une table arabe s'y ajoute sans toucher au reste.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import dinars_constants  # noqa: E402
import figtools  # noqa: E402

S_TRANSFERTS = "entreprises-publiques-transferts-budget"
S_GARANTIES = "garanties-etat"
S_DIVIDENDES = "entreprises-publiques-dividendes-etat"
S_FLUX = "entreprises-publiques-versements-transferts"
S_AGREGATS = "entreprises-publiques-resultats-agreges"
S_CROISEES = "entreprises-publiques-dettes-creances-croisees"
S_TRANSFERTS_EP = "entreprises-publiques-transferts-par-entreprise"
S_NETS_EP = "entreprises-publiques-resultats-nets-dix-premieres"
S_CESSIONS = "privatisation-recettes-annuelles"
S_PLANS = "privatisation-recettes-par-plan"
S_ETUDES = "entreprises-publiques-etudes-rapportees"

BASE = dinars_constants.ANNEE_BASE
BLEU, ORANGE, VERT, VIOLET, ROUGE, GRIS, NOIR = (
    "#0969da", "#d1600f", "#1a7f37", "#8250df", "#cf222e", "#57606a", "#24292f")
COULEUR_EDITION = {"LF2021": GRIS, "LF2022": BLEU, "LF2023": VERT, "LF2024": ORANGE,
                   "LF2025": VIOLET}

LIB = {
    "secteur_social": "Social", "secteur_economique": "Économique",
    "secteur_educatif_culturel": "Éducatif et culturel", "secteur_souverainete": "Souveraineté",
    "remuneration": "Rémunération", "fonctionnement": "Fonctionnement",
    "interventions": "Interventions", "investissement": "Investissement",
    "ressources_propres_budget": "Ressources propres du budget",
    "comptes_speciaux_tresor": "Comptes spéciaux du Trésor",
    "credits_exterieurs_affectes": "Crédits extérieurs affectés", "dons": "Dons",
    "impots_taxes": "Impôts et taxes", "prets_avances_tresor": "Prêts et avances du Trésor",
    "autres_dettes": "Autres dettes",
    "ligne_fr_redevances_ar_dividendes":
        "Ligne libellée « Redevances » en français et « dividendes » en arabe",
    "ligne_fr_dividendes_excedents_ar_redevances":
        "Ligne libellée « Dividendes et excédents » en français et « redevances » en arabe",
    "subventions_non_reglees": "Subventions non réglées",
    "prestations_rendues": "Prestations rendues à l'État",
    "autres_creances": "Autres créances", "gestion_de_fonds": "Gestion de fonds",
    "interieures_importations_produits_de_base": "Importations de produits de base",
    "interieures_audit_complet_banques": "Audit complet des banques publiques",
    "interieures_reechelonnement": "Rééchelonnements",
    "interieures_autres_operations_exploitation": "Autres opérations d'exploitation",
    "interieures_investissement": "Investissement",
    "interieures_total": "Total des garanties intérieures",
    "produits_exploitation": "Produits d'exploitation",
    "charges_exploitation": "Charges d'exploitation",
    "charges_personnel": "dont charges de personnel",
    "resultat_exploitation": "Résultat d'exploitation",
    "resultats_nets_positifs": "Somme des résultats nets positifs",
    "resultats_nets_negatifs": "Somme des résultats nets négatifs",
    "resultat_net": "Résultat net agrégé",
}
COURT = {
    "steg": "STEG (électricité et gaz)", "stir": "STIR (raffinage)",
    "office_cereales": "Office des céréales", "cnss": "CNSS", "cnrps": "CNRPS", "cnam": "CNAM",
    "office_huile": "Office national de l'huile", "sonede": "SONEDE (eau)",
    "onas": "ONAS (assainissement)", "transtu": "Transtu (transports de Tunis)",
    "sncft": "SNCFT (chemins de fer)", "tunisie_autoroutes": "Tunisie Autoroutes",
    "cpscl": "CPSCL (prêts aux collectivités)", "tunisair": "Tunisair",
    "etap": "ETAP (activités pétrolières)", "cpg": "CPG (phosphates)",
    "gct": "Groupe chimique tunisien", "office_commerce": "Office du commerce",
    "rnta": "RNTA (tabacs et allumettes)", "pct": "Pharmacie centrale",
    "oaca": "OACA (aviation civile et aéroports)", "sncpa": "SNCPA (cellulose et papier alfa)",
    "sndp": "SNDP (distribution des pétroles)", "tunisie_telecom": "Tunisie Télécom",
    "ommp": "OMMP (marine marchande et ports)", "bh": "BH", "bna": "BNA",
    "poste": "La Poste tunisienne",
}


# --- outils -----------------------------------------------------------------------------

def _s(serie: str):
    return figtools.series(serie)


def _n(x, dec: int = 1, signe: bool = False) -> str:
    """Nombre à la française : espace insécable fine pour les milliers, virgule décimale."""
    if x is None or x != x:
        return ""
    s = f"{abs(float(x)):,.{dec}f}".replace(",", " ").replace(".", ",")
    if float(x) < 0:
        return "−" + s
    return ("+" + s) if signe and float(x) > 0 else s


def _ed(edition: str) -> str:
    return f"LF {str(edition)[2:]}"


def _reel(montant: float, annee: int) -> float:
    return dinars_constants.en_dinars_constants(float(montant), int(annee))


def _md(entete: list[str], alignement: str, lignes: list[list[str]], caption: str,
        tbl_id: str) -> None:
    """Écrit un tableau Markdown, sa légende et son identifiant (chunk `output: asis`)."""
    out = ["| " + " | ".join(entete) + " |",
           "|" + "|".join({"g": "---", "d": "---:"}[a] for a in alignement) + "|"]
    out += ["| " + " | ".join(l) + " |" for l in lignes]
    print("\n".join(out) + f"\n\n: {caption} {{#{tbl_id}}}\n")


def _milliards(ax) -> None:
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _n(v / 1000, 0 if v % 1000 == 0 else 1)))


def _style(ax) -> None:
    ax.grid(axis="y", color="#d0d7de", lw=0.6)
    ax.set_axisbelow(True)
    for cote in ("top", "right"):
        ax.spines[cote].set_visible(False)


# --- lectures des séries -----------------------------------------------------------------

def _transferts():
    """Annexe 8 : une ligne par (année, état) dans la dernière édition qui la porte."""
    d = _s(S_TRANSFERTS)
    d = d[d["derniere_edition"].astype(bool)]
    return d


def _transferts_retenus(ventilation: str):
    """Réalisations de 2016 à 2023, loi de finances pour la dernière année."""
    d = _transferts()
    d = d[d["ventilation"] == ventilation]
    real = d[d["etat"] == "réalisations"]
    lf = d[(d["etat"] == "loi de finances") & (d["annee"] > real["annee"].max())]
    import pandas as pd
    t = pd.concat([real, lf])
    return t.pivot_table(index=["annee", "etat", "edition", "perimetre"], columns="cle",
                         values="valeur_md").reset_index().sort_values("annee")


def _garanties(grandeur: str, portee: str = "année"):
    """Une valeur par période : la dernière édition du rapport sur la dette publique, à
    défaut celle du rapport sur les transferts et les garanties."""
    g = _s(S_GARANTIES)
    g = g[(g["grandeur"] == grandeur) & (g["portee"] == portee)].copy()
    g["rang"] = g["document"].map({"annexe7": 1, "annexe8": 0}) * 10000 + \
        g["edition"].str[2:].astype(int)
    g = g.sort_values("rang").groupby("periode").tail(1)
    return {str(r.periode): float(r.valeur) for r in g.itertuples()}


def _dividendes():
    d = _s(S_DIVIDENDES)
    return d[d["grandeur"] == "part_etat_benefices_excedents"].copy()


def _dividendes_retenus():
    """Par exercice : le montant arrêté de la dernière édition ; à défaut d'arrêté, le montant
    partiel — qui n'est jamais tracé comme un exercice arrêté."""
    d = _dividendes().sort_values("edition")
    lignes = []
    for _, bloc in d.groupby("exercice"):
        arretes = bloc[bloc["etat"] == "arrêté"]
        lignes.append((arretes if len(arretes) else bloc).iloc[-1])
    import pandas as pd
    return pd.DataFrame(lignes).sort_values("exercice")


def _croisees_totaux():
    c = _s(S_CROISEES)
    return c[c["poste"] == "total"].pivot_table(index="fin_annee", columns="cote",
                                                values="valeur_md")


def _flux_totaux():
    """Versements et transferts de l'échantillon, une ligne par (année, édition)."""
    v = _s(S_FLUX)
    v = v[v["flux"].isin(["versements", "transferts"])]
    return v


# --- figure d'ensemble --------------------------------------------------------------------

def table_ensemble():
    import pandas as pd
    lignes = []
    t = _transferts_retenus("secteur")
    for r in t.itertuples():
        lignes.append(("Transferts du budget", str(r.annee), r.total,
                       "loi de finances" if r.etat != "réalisations" else
                       ("réalisé, ancien périmètre" if r.perimetre.startswith("ancien")
                        else "réalisé"), _ed(r.edition)))
    for portee, etat in (("année", "fin d'année"), ("fin juin (estimation)", "estimation")):
        for p, v in sorted(_garanties("encours_total", portee).items()):
            if portee != "année" and not p.startswith("2024"):
                continue
            lignes.append(("Encours de la dette garantie", p, v, etat, ""))
    c = _croisees_totaux()
    for a in c.index:
        lignes.append(("Créances des entreprises sur l'État", str(a),
                       c.at[a, "creances_sur_etat"], "fin d'année", "LF 2025"))
        lignes.append(("Dettes des entreprises envers l'État", str(a),
                       c.at[a, "dettes_envers_etat"], "fin d'année", "LF 2025"))
    for r in _dividendes_retenus().itertuples():
        lignes.append(("Part de l'État dans les bénéfices", str(r.exercice), r.valeur, r.etat,
                       _ed(r.edition)))
    return pd.DataFrame(lignes, columns=["Grandeur", "Année ou exercice",
                                         "Millions de dinars courants", "État de la valeur",
                                         "Édition"])


def fig_ensemble():
    figtools.apply_lang_font()
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.6))
    # 1. Transferts du budget
    ax = axes[0][0]
    t = _transferts_retenus("secteur")
    nouv = t[(t["etat"] == "réalisations") & ~t["perimetre"].str.startswith("ancien")]
    ax.plot(nouv["annee"], nouv["total"], color=NOIR, marker="o", lw=2, ms=4.5)
    anc = t[t["perimetre"].str.startswith("ancien")]
    ax.plot(anc["annee"], anc["total"], color=NOIR, marker="s", ls="", ms=5, mfc="white")
    lf = t[t["etat"] != "réalisations"]
    ax.plot(lf["annee"], lf["total"], color=NOIR, marker="o", ls="", ms=5.5, mfc="white")
    figtools.marque_rupture(ax, 2017, "périmètre révisé")
    ax.set_title("Ce que le budget verse : transferts à l'ensemble des entreprises\net "
                 "établissements publics non administratifs", fontsize=8.5, loc="left")
    # 2. Encours garanti
    ax = axes[0][1]
    e = _garanties("encours_total")
    ans = sorted(int(p) for p in e)
    ax.plot(ans, [e[str(a)] for a in ans], color=BLEU, marker="o", lw=2, ms=4.5)
    juin = _garanties("encours_total", "fin juin (estimation)")
    if "2024-06" in juin:
        ax.plot([2024], [juin["2024-06"]], color=BLEU, marker="o", ls="", ms=5.5, mfc="white")
    ax.set_title("Ce que l'État garantit : encours de la dette garantie,\nen fin d'année",
                 fontsize=8.5, loc="left")
    # 3. Dettes et créances croisées
    ax = axes[1][0]
    c = _croisees_totaux()
    ax.plot(c.index, c["creances_sur_etat"], color=ROUGE, marker="o", lw=2, ms=4.5,
            label="créances des entreprises sur l'État")
    ax.plot(c.index, c["dettes_envers_etat"], color=VERT, marker="s", lw=2, ms=4.5,
            label="dettes des entreprises envers l'État")
    ax.legend(fontsize=7, frameon=False, loc="lower right")
    ax.set_title("Ce que l'État doit et ce qui lui est dû : 42 entreprises,\nen fin d'année",
                 fontsize=8.5, loc="left")
    # 4. Dividendes
    ax = axes[1][1]
    d = _dividendes_retenus()
    arr = d[d["etat"] == "arrêté"]
    par = d[d["etat"] != "arrêté"]
    ax.plot(arr["exercice"].astype(int), arr["valeur"], color=ORANGE, marker="o", lw=2, ms=4.5)
    ax.plot(par["exercice"].astype(int), par["valeur"], color=ORANGE, marker="o", ls="", ms=5.5,
            mfc="white")
    ax.set_title("Ce que l'État reçoit : sa part dans les bénéfices et excédents,\npar "
                 "exercice", fontsize=8.5, loc="left")
    for ligne in axes:
        for ax in ligne:
            _style(ax)
            ax.set_xlim(2015.5, 2024.5)
            ax.set_xticks(range(2016, 2025))
            ax.tick_params(labelsize=7.5)
            ax.set_ylim(bottom=0)
    for ax in (axes[0][0], axes[0][1], axes[1][0]):
        _milliards(ax)
        ax.set_ylabel("milliards de dinars courants", fontsize=7.5)
    axes[1][1].set_ylabel("millions de dinars courants", fontsize=7.5)
    fig.tight_layout()
    return fig


# --- transferts du budget (annexe 8) ---------------------------------------------------------

def _barres_empilees(ax, t, cles, couleurs):
    bas = [0.0] * len(t)
    for cle, coul in zip(cles, couleurs):
        for i, r in enumerate(t.itertuples()):
            creux = r.etat != "réalisations"
            ancien = r.perimetre.startswith("ancien")
            barre = ax.bar(r.annee, getattr(r, cle), bottom=bas[i], color=coul, width=0.72,
                           alpha=0.45 if (creux or ancien) else 1.0,
                           hatch="//" if creux else ("..." if ancien else None),
                           edgecolor="white", lw=0.5)
            figtools.infobulle(barre[0], f"{r.annee} — {LIB[cle]} : {_n(getattr(r, cle))} MD "
                                         f"({_ed(r.edition)}, {r.etat})")
            bas[i] += getattr(r, cle)
    return bas


def fig_transferts():
    figtools.apply_lang_font()
    vues = []
    for titre, ventilation, cles in (
            ("Par secteur", "secteur", ["secteur_economique", "secteur_social",
                                        "secteur_souverainete", "secteur_educatif_culturel"]),
            ("Par nature de dépense", "nature", ["interventions", "remuneration",
                                                 "investissement", "fonctionnement"])):
        t = _transferts_retenus(ventilation)
        fig, ax = plt.subplots(figsize=(9.2, 5.2))
        couleurs = [ORANGE, BLEU, GRIS, VERT]
        _barres_empilees(ax, t, cles, couleurs)
        figtools.marque_rupture(ax, 2017)
        _style(ax)
        _milliards(ax)
        ax.set_xticks(list(t["annee"]))
        ax.set_ylabel("milliards de dinars courants")
        poignees = [Patch(color=c, label=LIB[k]) for k, c in zip(cles, couleurs)]
        poignees += [Patch(facecolor="#bbbbbb", hatch="...", edgecolor="white",
                           label="2016 : ancien périmètre"),
                     Patch(facecolor="#bbbbbb", hatch="//", edgecolor="white",
                           label="loi de finances")]
        ax.legend(handles=poignees, fontsize=8, frameon=False, loc="upper left", ncol=2)
        fig.tight_layout()
        vues.append((titre, fig))
    return vues


def table_transferts():
    t = _transferts_retenus("secteur").rename(columns=LIB)
    t = t.rename(columns={"annee": "Année", "etat": "État", "edition": "Édition",
                          "perimetre": "Périmètre", "total": "Total"})
    n = _transferts_retenus("nature").rename(columns=LIB)
    for c in ("Rémunération", "Fonctionnement", "Interventions", "Investissement"):
        t[c] = list(n[c])
    return t


def tableau_transferts(caption: str, tbl_id: str = "tbl-ep-transferts") -> None:
    t = _transferts_retenus("secteur")
    lignes = []
    for r in t.itertuples():
        etat = "loi de finances" if r.etat != "réalisations" else (
            "réalisé, ancien périmètre" if r.perimetre.startswith("ancien") else "réalisé")
        lignes.append([str(r.annee), etat, _ed(r.edition), _n(r.total), _n(_reel(r.total, r.annee)),
                       _n(r.secteur_economique), _n(r.secteur_social),
                       _n(r.secteur_educatif_culturel), _n(r.secteur_souverainete)])
    _md(["Année", "État de la valeur", "Édition", "Total<br>(MD courants)",
         f"Total<br>(MD de {BASE})", "Secteur économique<br>(MD courants)",
         "Secteur social<br>(MD courants)", "Éducatif et culturel<br>(MD courants)",
         "Souveraineté<br>(MD courants)"], "gggdddddd", lignes, caption, tbl_id)


def tableau_transferts_ventilation(ventilation: str, caption: str, tbl_id: str) -> None:
    cles = {"nature": ["remuneration", "fonctionnement", "interventions", "investissement"],
            "source": ["ressources_propres_budget", "comptes_speciaux_tresor",
                       "credits_exterieurs_affectes", "dons"]}[ventilation]
    d = _transferts()
    d = d[(d["ventilation"] == ventilation)]
    t = _transferts_retenus(ventilation)
    lignes = []
    for r in t.itertuples():
        somme = sum(getattr(r, c) for c in cles)
        ecart = r.total - somme
        etat = "loi de finances" if r.etat != "réalisations" else (
            "réalisé, ancien périmètre" if r.perimetre.startswith("ancien") else "réalisé")
        lignes.append([str(r.annee), etat, _ed(r.edition)] + [_n(getattr(r, c)) for c in cles] +
                      [_n(r.total), _n(ecart) if abs(ecart) >= 0.05 else "—"])
    _md(["Année", "État de la valeur", "Édition"] + [f"{LIB[c]}<br>(MD)" for c in cles] +
        ["Total imprimé<br>(MD)", "Total moins somme<br>(MD)"], "ggg" + "d" * (len(cles) + 2),
        lignes, caption, tbl_id)


def tableau_transferts_editions(caption: str, tbl_id: str = "tbl-ep-transferts-editions") -> None:
    """Le total de chaque année dans toutes les éditions qui le portent."""
    d = _s(S_TRANSFERTS)
    d = d[(d["ventilation"] == "secteur") & (d["cle"] == "total")]
    editions = sorted(d["edition"].unique())
    lignes = []
    for a in sorted(d["annee"].unique()):
        cases = []
        for e in editions:
            x = d[(d["annee"] == a) & (d["edition"] == e)]
            if x.empty:
                cases.append("")
            else:
                r = x.iloc[0]
                cases.append(_n(r["valeur_md"]) + (" (LF)" if r["etat"] != "réalisations" else ""))
        lignes.append([str(a)] + cases)
    _md(["Année"] + [f"Édition {_ed(e)}<br>(MD)" for e in editions], "g" + "d" * len(editions),
        lignes, caption, tbl_id)


# --- garanties ---------------------------------------------------------------------------------

def fig_garanties():
    figtools.apply_lang_font()
    # Vue 1 : plafond et garanties accordées
    fig1, ax = plt.subplots(figsize=(9.2, 5.0))
    ext, inte = _garanties("garanties_exterieures"), _garanties("garanties_interieures")
    plaf = _garanties("plafond")
    ans = sorted(int(p) for p in ext)
    ax.bar(ans, [ext[str(a)] for a in ans], color=BLEU, width=0.7, label="prêts extérieurs")
    ax.bar(ans, [inte[str(a)] for a in ans], bottom=[ext[str(a)] for a in ans], color=ORANGE,
           width=0.7, label="prêts intérieurs")
    ax.step([a for a in ans], [plaf[str(a)] for a in ans], where="mid", color=NOIR, lw=1.8,
            label="plafond de la loi de finances, après loi rectificative")
    _style(ax)
    _milliards(ax)
    ax.set_xticks(ans)
    ax.set_ylabel("milliards de dinars courants")
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    fig1.tight_layout()
    # Vue 2 : encours
    fig2, ax = plt.subplots(figsize=(9.2, 5.0))
    ee, ei = _garanties("encours_exterieur"), _garanties("encours_interieur")
    ans = sorted(int(p) for p in ee)
    ax.bar(ans, [ee[str(a)] for a in ans], color=BLEU, width=0.7, label="dette garantie extérieure")
    ax.bar(ans, [ei[str(a)] for a in ans], bottom=[ee[str(a)] for a in ans], color=ORANGE,
           width=0.7, label="dette garantie intérieure")
    je = _garanties("encours_exterieur", "fin juin (estimation)")
    ji = _garanties("encours_interieur", "fin juin (estimation)")
    if "2024-06" in je:
        ax.bar([2024], [je["2024-06"]], color=BLEU, width=0.7, alpha=0.45, hatch="//",
               edgecolor="white")
        ax.bar([2024], [ji["2024-06"]], bottom=[je["2024-06"]], color=ORANGE, width=0.7,
               alpha=0.45, hatch="//", edgecolor="white", label="fin juin 2024, estimation")
        ans = ans + [2024]
    _style(ax)
    _milliards(ax)
    ax.set_xticks(ans)
    ax.set_ylabel("milliards de dinars courants")
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    fig2.tight_layout()
    return [("Garanties accordées dans l'année et plafond", fig1),
            ("Encours de la dette garantie", fig2)]


def _lignes_garanties():
    ext, inte = _garanties("garanties_exterieures"), _garanties("garanties_interieures")
    acc, plaf = _garanties("garanties_accordees"), _garanties("plafond")
    et, ee, ei = (_garanties(g) for g in ("encours_total", "encours_exterieur",
                                          "encours_interieur"))
    lignes = []
    for a in sorted(int(p) for p in acc):
        p = str(a)
        lignes.append((p, plaf.get(p), acc.get(p), ext.get(p), inte.get(p), et.get(p),
                       _reel(et[p], a) if p in et else None, ee.get(p), ei.get(p)))
    s1 = "premier semestre"
    j = "fin juin (estimation)"
    lignes.append(("2024, premier semestre et fin juin", _garanties("plafond", s1).get("2024-S1"),
                   _garanties("garanties_accordees", s1).get("2024-S1"),
                   _garanties("garanties_exterieures", s1).get("2024-S1"),
                   _garanties("garanties_interieures", s1).get("2024-S1"),
                   _garanties("encours_total", j).get("2024-06"), None,
                   _garanties("encours_exterieur", j).get("2024-06"),
                   _garanties("encours_interieur", j).get("2024-06")))
    return lignes


def table_garanties():
    import pandas as pd
    return pd.DataFrame(_lignes_garanties(), columns=[
        "Année", "Plafond (MD)", "Garanties accordées (MD)", "dont prêts extérieurs (MD)",
        "dont prêts intérieurs (MD)", "Encours garanti en fin d'année (MD)",
        f"Encours garanti (MD de {BASE})", "dont extérieur (MD)", "dont intérieur (MD)"])


def tableau_garanties(caption: str, tbl_id: str = "tbl-ep-garanties") -> None:
    lignes = [[l[0]] + [_n(x) if i != 0 else _n(x, 0) for i, x in enumerate(l[1:])]
              for l in _lignes_garanties()]
    _md(["Année", "Plafond<br>(MD)", "Garanties accordées<br>(MD)", "dont extérieures<br>(MD)",
         "dont intérieures<br>(MD)", "Encours garanti<br>(MD courants)",
         f"Encours garanti<br>(MD de {BASE})", "dont extérieur<br>(MD)", "dont intérieur<br>(MD)"],
        "g" + "d" * 8, lignes, caption, tbl_id)


def tableau_encours_pib(caption: str, tbl_id: str = "tbl-ep-garanties-pib") -> None:
    g = _s(S_GARANTIES)
    g = g[g["grandeur"] == "encours_pct_pib"]
    editions = sorted(g["edition"].unique())
    lignes = []
    for p in sorted(g["periode"].unique()):
        nom = p if "-" not in p else f"fin juin {p[:4]} (estimation)"
        cases = []
        for e in editions:
            x = g[(g["periode"] == p) & (g["edition"] == e)]
            cases.append("" if x.empty else _n(x.iloc[0]["valeur"], 2 if e == "LF2022" else 1))
        lignes.append([nom] + cases)
    _md(["Fin d'année"] + [f"Édition {_ed(e)}<br>(% du PIB)" for e in editions],
        "g" + "d" * len(editions), lignes, caption, tbl_id)


def tableau_garanties_objet(caption: str, tbl_id: str = "tbl-ep-garanties-objet") -> None:
    g = _s(S_GARANTIES)
    cles = ["interieures_importations_produits_de_base", "interieures_audit_complet_banques",
            "interieures_reechelonnement", "interieures_autres_operations_exploitation",
            "interieures_investissement", "interieures_total"]
    periodes = sorted(g[g["grandeur"] == "interieures_total"]["periode"].unique())
    lignes = []
    for c in cles:
        cases = []
        for p in periodes:
            x = g[(g["grandeur"] == c) & (g["periode"] == p)]
            cases.append("" if x.empty else _n(x.iloc[0]["valeur"]))
        nom = f"**{LIB[c]}**" if c.endswith("total") else LIB[c]
        lignes.append([nom] + cases)
    x = g[g["grandeur"] == "interieures_total_operations"]
    lignes.append(["Nombre d'opérations"] + [
        _n(x[x["periode"] == p].iloc[0]["valeur"], 0) if not x[x["periode"] == p].empty else ""
        for p in periodes])
    noms = [p if "-" not in p else f"{p[:4]}, 1^er^ semestre" for p in periodes]
    _md(["Objet de la garantie"] + [f"{n}<br>(MD)" for n in noms], "g" + "d" * len(periodes),
        lignes, caption, tbl_id)


def tableau_audit_banques(caption: str, tbl_id: str = "tbl-ep-garanties-audit") -> None:
    g = _s(S_GARANTIES)
    periodes = sorted(g[g["grandeur"] == "audit_total"]["periode"].unique())
    lignes = []
    for c, nom in (("audit_stb", "Société tunisienne de banque (STB)"),
                   ("audit_bna", "Banque nationale agricole (BNA)"),
                   ("audit_bh", "Banque de l'habitat (BH)"), ("audit_total", "**Total imprimé**")):
        lignes.append([nom] + [_n(g[(g["grandeur"] == c) & (g["periode"] == p)].iloc[0]["valeur"])
                               for p in periodes])
    _md(["Banque créancière"] + [f"{p}<br>(MD)" for p in periodes], "g" + "d" * len(periodes),
        lignes, caption, tbl_id)


# --- dettes et créances croisées ---------------------------------------------------------------

def tableau_croisees(caption: str, tbl_id: str = "tbl-ep-croisees") -> None:
    c = _s(S_CROISEES)
    annees = sorted(c["fin_annee"].unique())

    def ligne(cote, poste, nom):
        x = c[(c["cote"] == cote) & (c["poste"] == poste)].set_index("fin_annee")["valeur_md"]
        return [nom] + [_n(x.get(a)) for a in annees]
    lignes = [ligne("creances_sur_etat", "total", "**Créances des entreprises sur l'État**")]
    for p in ("subventions_non_reglees", "prestations_rendues", "impots_taxes",
              "autres_creances", "gestion_de_fonds"):
        lignes.append(ligne("creances_sur_etat", p, "— " + LIB[p]))
    lignes.append(ligne("dettes_envers_etat", "total", "**Dettes des entreprises envers l'État**"))
    for p in ("impots_taxes", "prets_avances_tresor", "autres_dettes",
              "ligne_fr_redevances_ar_dividendes", "ligne_fr_dividendes_excedents_ar_redevances"):
        lignes.append(ligne("dettes_envers_etat", p, "— " + LIB[p]))
    lignes.append(ligne("ecart", "dettes_moins_creances", "**Dettes moins créances**"))
    _md(["Poste"] + [f"Fin {a}<br>(MD)" for a in annees], "g" + "d" * len(annees), lignes,
        caption, tbl_id)


def tableau_croisees_entreprises(caption: str, tbl_id: str = "tbl-ep-croisees-entreprises") -> None:
    c = _s(S_CROISEES)
    c = c[c["poste"].str.startswith("entreprise:")]
    cr = c[c["cote"] == "creances_sur_etat"].sort_values("valeur_md", ascending=False)
    de = c[c["cote"] == "dettes_envers_etat"].sort_values("valeur_md", ascending=False)
    lignes = []
    for i, (a, b) in enumerate(zip(cr.itertuples(), de.itertuples()), 1):
        lignes.append([str(i), COURT.get(a.entite, a.libelle), _n(a.valeur_md),
                       COURT.get(b.entite, b.libelle), _n(b.valeur_md)])
    _md(["Rang", "Créancière de l'État", "Créance<br>(MD)", "Débitrice de l'État",
         "Dette<br>(MD)"], "ggdgd", lignes, caption, tbl_id)


# --- dividendes, versements et transferts de l'échantillon ----------------------------------

def tableau_dividendes(caption: str, tbl_id: str = "tbl-ep-dividendes") -> None:
    d = _s(S_DIVIDENDES)
    p = d[d["grandeur"] == "part_etat_benefices_excedents"].sort_values(["exercice", "edition"])
    nb = d[d["grandeur"] == "entreprises_distributrices"]
    lignes = []
    for r in p.itertuples():
        x = nb[(nb["exercice"] == r.exercice) & (nb["edition"] == r.edition)]
        lignes.append([str(r.exercice), _ed(r.edition), r.etat, _n(r.valeur),
                       _n(_reel(r.valeur, int(r.exercice))),
                       "" if x.empty else _n(x.iloc[0]["valeur"], 0)])
    _md(["Exercice", "Édition", "État de la valeur", "Part de l'État<br>(MD courants)",
         f"Part de l'État<br>(MD de {BASE})", "Entreprises distributrices"], "gggddd", lignes,
        caption, tbl_id)


def fig_flux():
    figtools.apply_lang_font()
    v = _flux_totaux()
    v = v[(v["poste"] == "total") & (v["statut"] != "prévisionnel")]
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    for edition, bloc in v.groupby("edition"):
        for flux, coul, marque in (("transferts", ROUGE, "o"), ("versements", VERT, "s")):
            x = bloc[bloc["flux"] == flux].groupby(["annee", "statut"])["valeur_md"].max()
            x = x.reset_index().sort_values("annee")
            ax.plot(x["annee"], x["valeur_md"], color=coul, lw=1.6, alpha=0.9)
            for r in x.itertuples():
                pt, = ax.plot([r.annee], [r.valeur_md], color=coul, marker=marque, ms=5.5, ls="",
                              mfc="white" if r.statut != "réalisé" else coul)
                figtools.infobulle(pt, f"{flux}, {r.annee} : {_n(r.valeur_md)} MD — édition "
                                       f"{_ed(edition)}, {r.statut}")
            if len(x):
                d = x.iloc[-1]
                ax.annotate(_ed(edition), (d["annee"], d["valeur_md"]), xytext=(4, 4),
                            textcoords="offset points", fontsize=6.5, color=coul)
    _style(ax)
    _milliards(ax)
    ax.set_ylim(bottom=0)
    ax.set_xticks(sorted(v["annee"].unique()))
    ax.set_ylabel("milliards de dinars courants")
    ax.legend(handles=[
        Line2D([], [], color=ROUGE, marker="o", label="transferts reçus du budget"),
        Line2D([], [], color=VERT, marker="s", label="versements au budget"),
        Line2D([], [], color=GRIS, marker="o", mfc="white", ls="", label="valeur provisoire")],
        fontsize=8, frameon=False, loc="upper left")
    fig.tight_layout()
    return fig


def table_flux():
    v = _flux_totaux()
    t = v.pivot_table(index=["annee", "statut", "edition", "echantillon"],
                      columns=["flux", "poste"], values="valeur_md", aggfunc="max")
    t.columns = [f"{a} : {b}" for a, b in t.columns]
    return t.reset_index().rename(columns={"annee": "Année", "statut": "État",
                                           "edition": "Édition", "echantillon": "Échantillon"})


def tableau_flux(caption: str, tbl_id: str = "tbl-ep-flux") -> None:
    v = _flux_totaux()
    lignes = []
    cles = sorted({(r.annee, r.edition, r.statut, r.echantillon) for r in v.itertuples()},
                  key=lambda k: (k[0], k[1]))
    for a, e, st, ech in cles:
        if st == "prévisionnel":
            continue
        b = v[(v["annee"] == a) & (v["edition"] == e)]

        def val(flux, poste):
            x = sorted(set(b[(b["flux"] == flux) & (b["poste"] == poste)]["valeur_md"]))
            return " ou ".join(_n(z) for z in x)
        lignes.append([str(a), f"{_ed(e)} ({ech})", st, val("versements", "total"),
                       val("versements", "fiscaux_douaniers"),
                       val("versements", "benefices_transferes_commissions_garantie"),
                       val("transferts", "total"),
                       val("transferts", "subventions_exploitation_equilibre"),
                       val("transferts", "subventions_investissement_capital"),
                       val("transferts", "prets_tresor_retrocedes")])
    _md(["Année", "Édition<br>(entreprises)", "État de la valeur", "Versements au budget<br>(MD)",
         "dont fiscaux et douaniers<br>(MD)", "dont bénéfices et commissions de garantie<br>(MD)",
         "Transferts reçus<br>(MD)", "dont subventions d'exploitation et d'équilibre<br>(MD)",
         "dont investissement et capital<br>(MD)", "dont prêts du Trésor et prêts rétrocédés<br>(MD)"],
        "ggg" + "d" * 7, lignes, caption, tbl_id)


# --- résultats agrégés --------------------------------------------------------------------------

def _agregats():
    r = _s(S_AGREGATS)
    return r.pivot_table(index=["exercice", "edition", "echantillon"], columns="indicateur",
                         values="valeur_md").reset_index()


def fig_resultats():
    figtools.apply_lang_font()
    a = _agregats()
    vues = []
    for titre, series in (
            ("Résultat net agrégé", [("resultat_net", "-", "o")]),
            ("Sommes des résultats positifs et des résultats négatifs",
             [("resultats_nets_positifs", "-", "^"), ("resultats_nets_negatifs", "--", "v")])):
        fig, ax = plt.subplots(figsize=(9.2, 5.0))
        for edition, bloc in a.groupby("edition"):
            coul = COULEUR_EDITION.get(edition, NOIR)
            for col, ls, marque in series:
                ax.plot(bloc["exercice"], bloc[col], color=coul, ls=ls, marker=marque, lw=1.8, ms=5)
        ax.axhline(0, color=NOIR, lw=0.8)
        _style(ax)
        _milliards(ax)
        ax.set_xticks(sorted(a["exercice"].unique()))
        ax.set_ylabel("milliards de dinars courants")
        ax.legend(handles=[Line2D([], [], color=COULEUR_EDITION[e], marker="o",
                                  label=f"édition {_ed(e)} : {int(b['echantillon'].iloc[0])} entreprises")
                           for e, b in a.groupby("edition")],
                  fontsize=8, frameon=False, loc="lower left", ncol=2)
        fig.tight_layout()
        vues.append((titre, fig))
    return vues


def table_resultats():
    return _agregats().rename(columns={**LIB, "exercice": "Exercice", "edition": "Édition",
                                       "echantillon": "Entreprises"})


def tableau_resultats(caption: str, tbl_id: str = "tbl-ep-resultats") -> None:
    a = _agregats().sort_values(["exercice", "edition"])
    cols = ["produits_exploitation", "charges_exploitation", "charges_personnel",
            "resultat_exploitation", "resultats_nets_positifs", "resultats_nets_negatifs",
            "resultat_net"]
    lignes = [[str(r.exercice), f"{_ed(r.edition)} ({int(r.echantillon)})"] +
              [_n(getattr(r, c)) for c in cols] for r in a.itertuples()]
    _md(["Exercice", "Édition<br>(entreprises)"] + [f"{LIB[c]}<br>(MD)" for c in cols],
        "gg" + "d" * len(cols), lignes, caption, tbl_id)


# --- par entreprise -------------------------------------------------------------------------------

def _cases_par_edition(bloc, col_valeur="valeur_md", signe=False) -> str:
    """Une valeur par édition ; l'édition est nommée quand elles diffèrent."""
    if bloc.empty:
        return "—"
    b = bloc.sort_values("edition")
    valeurs = [(r["edition"], float(r[col_valeur])) for _, r in b.iterrows()]
    if len({round(v, 1) for _, v in valeurs}) == 1:
        return _n(valeurs[-1][1], 1, signe)
    distinctes, vus = [], set()
    for e, v in valeurs:
        if round(v, 1) not in vus:
            vus.add(round(v, 1))
            distinctes.append(f"{_n(v, 1, signe)} ({_ed(e)})")
    return " ; ".join(distinctes)


def tableau_transferts_entreprises(caption: str, entites: tuple[str, ...],
                                   tbl_id: str = "tbl-ep-transferts-entreprises") -> None:
    t = _s(S_TRANSFERTS_EP)
    annees = sorted(t["annee"].unique())
    lignes = []
    for ent in entites:
        b = t[t["entite"] == ent]
        nom = COURT.get(ent, b["libelle"].iloc[0] if len(b) else ent)
        if ent == "total":
            nom = "**Total de l'échantillon, imprimé**"
        cases = []
        for a in annees:
            x = b[b["annee"] == a]
            x = x[x["edition"] == x["edition"].max()] if len(x) else x
            cases.append("—" if x.empty else _n(x.iloc[0]["valeur_md"]))
        lignes.append([nom] + cases)
    der = {a: t[t["annee"] == a]["edition"].max() for a in annees}
    _md(["Entreprise"] + [f"{a}<br>({_ed(der[a])}, MD)" for a in annees], "g" + "d" * len(annees),
        lignes, caption, tbl_id)


def tableau_transferts_revisions(caption: str, entites: tuple[str, ...],
                                 tbl_id: str = "tbl-ep-transferts-revisions") -> None:
    t = _s(S_TRANSFERTS_EP)
    annees = sorted(t["annee"].unique())
    lignes = []
    for ent in entites:
        b = t[t["entite"] == ent]
        nom = COURT.get(ent, b["libelle"].iloc[0] if len(b) else ent)
        lignes.append([nom] + [_cases_par_edition(b[b["annee"] == a]) for a in annees])
    _md(["Entreprise"] + [f"{a}<br>(MD)" for a in annees], "g" + "g" * len(annees), lignes,
        caption, tbl_id)


def tableau_resultats_entreprises(caption: str, entites: tuple[str, ...],
                                  tbl_id: str = "tbl-ep-resultats-entreprises") -> None:
    n = _s(S_NETS_EP)
    n = n[~n["doublon_imprime"].astype(bool) | ~n.duplicated(["exercice", "edition", "entite"])]
    exercices = sorted(n["exercice"].unique())
    lignes = []
    for ent in entites:
        b = n[n["entite"] == ent].drop_duplicates(["exercice", "edition"])
        nom = COURT.get(ent, b["libelle"].iloc[0] if len(b) else ent)
        lignes.append([nom] + [_cases_par_edition(b[b["exercice"] == x], signe=True)
                               for x in exercices])
    _md(["Entreprise"] + [f"{x}<br>(MD)" for x in exercices], "g" + "g" * len(exercices), lignes,
        caption, tbl_id)


# --- cessions --------------------------------------------------------------------------------------

def _cessions():
    p = _s(S_CESSIONS)
    t = p.pivot_table(index="annee", columns="edition", values="valeur_md").reset_index()
    t["constants"] = [_reel(v, a) for v, a in zip(t["classeur 1987-2009"], t["annee"])]
    return t


def fig_cessions():
    figtools.apply_lang_font()
    t = _cessions()
    vues = []
    for titre, col, ylabel in (
            ("Dinars courants", "classeur 1987-2009", "millions de dinars courants"),
            (f"Dinars de {BASE}", "constants", f"millions de dinars de {BASE}")):
        fig, ax = plt.subplots(figsize=(9.2, 5.0))
        barres = ax.bar(t["annee"], t[col], color=BLEU, width=0.72)
        for b, an, val in zip(barres, t["annee"], t[col]):
            figtools.infobulle(b, f"{an} : {_n(val)} MD")
        if col != "constants":
            div = t[(t["classeur 1987-2005"].notna()) &
                    ((t["classeur 1987-2005"] - t["classeur 1987-2009"]).abs() > 1)]
            ax.plot(div["annee"], div["classeur 1987-2005"], color=ROUGE, marker="D", ls="", ms=5,
                    mfc="white", label="valeur de l'édition 1987-2005, quand elle diffère")
            ax.legend(fontsize=8, frameon=False, loc="upper left")
        ax.set_yscale("log")
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _n(v, 0)))
        _style(ax)
        ax.set_xticks(list(t["annee"])[::2])
        ax.set_ylabel(ylabel + " (échelle logarithmique)")
        fig.tight_layout()
        vues.append((titre, fig))
    return vues


def table_cessions():
    t = _cessions()
    return t.rename(columns={"annee": "Année",
                             "classeur 1987-2005": "Édition 1987-2005 (MD courants)",
                             "classeur 1987-2009": "Édition 1987-2009 (MD courants)",
                             "constants": f"Édition 1987-2009 (MD de {BASE})"})


def tableau_cessions(caption: str, tbl_id: str = "tbl-ep-cessions") -> None:
    t = _cessions()
    lignes = []
    for r in t.itertuples(index=False):
        a, e1, e2, c = r
        autre = _n(e1, 1) if e1 == e1 and abs(e1 - e2) >= 0.05 else ""
        lignes.append([str(a), _n(e2, 1), _n(c, 1), autre])
    tot = t["classeur 1987-2009"].sum()
    lignes.append(["**1987-2009**", f"**{_n(tot, 1)}**", f"**{_n(t['constants'].sum(), 1)}**", ""])
    _md(["Année", "Recettes<br>(MD courants)", f"Recettes<br>(MD de {BASE})",
         "Édition 1987-2005,<br>si elle diffère<br>(MD courants)"], "gddd", lignes, caption, tbl_id)


def tableau_cessions_plans(caption: str, tbl_id: str = "tbl-ep-cessions-plans") -> None:
    p = _s(S_PLANS)
    noms = {"plan_7_1987-1991": "VII^e^ Plan, 1987-1991", "plan_8_1992-1996": "VIII^e^ Plan, 1992-1996",
            "plan_9_1997-2001": "IX^e^ Plan, 1997-2001", "plan_10_2002-2006": "X^e^ Plan, 2002-2006",
            "plan_11_2007-2009": "XI^e^ Plan, 2007-2009", "total": "**Total**"}
    lignes = [[noms.get(r.plan, r.plan), _n(r.produit_md_page_officielle, 0),
               _n(r.somme_classeur_1987_2009_sans_2009_md), _n(r.somme_classeur_1987_2009_md),
               _n(r.entreprises, 0), _n(r.operations, 0)] for r in p.itertuples()]
    _md(["Période", "Recettes, page officielle<br>(MD)", "Somme du classeur, 2009 exclue<br>(MD)",
         "Somme du classeur, 2009 comprise<br>(MD)", "Entreprises", "Opérations"], "gddddd", lignes,
        caption, tbl_id)


# --- études ------------------------------------------------------------------------------------------

NOMS_GRANDEURS = {
    "contribution_economique": "« Contribution économique » des entreprises publiques",
    "part_population_active_occupee": "Part de la population active occupée",
    "part_masse_salariale_totale": "Part de la masse salariale totale",
    "subventions_exploitation_investissement":
        "Subventions d'exploitation et d'investissement versées par l'État",
    "dette_exterieure_garantie": "Dette extérieure garantie par l'État",
    "dette_bancaire": "Dette envers le système bancaire",
    "dette_30_entreprises": "Dette de 30 entreprises publiques",
    "garanties_etat": "dont dette couverte par la garantie de l'État",
    "transferts_budgetaires_annuels_bas": "Transferts budgétaires annuels, borne basse",
    "transferts_budgetaires_annuels_haut": "Transferts budgétaires annuels, borne haute",
    "part_transferts_trois_entreprises":
        "Part des transferts allant à trois entreprises (céréales, carburants, électricité)",
    "credits_bancaires_aux_entreprises_publiques": "Encours des crédits bancaires",
    "arrieres_entreprises_envers_etat": "Arriérés des entreprises envers l'État",
    "arrieres_etat_envers_entreprises": "Arriérés de l'État envers les entreprises",
    "pertes_vingt_plus_grandes": "Pertes des vingt plus grandes entreprises",
    "part_steg_dans_les_pertes": "Part de la STEG dans ces pertes",
    "deficit_eau_assainissement_hors_subventions":
        "Déficit des entreprises de l'eau et de l'assainissement, hors subventions",
    "transferts_entreprises_de_transport": "Transferts du budget aux entreprises de transport",
    "emploi_entreprises_publiques": "Emploi des entreprises publiques",
    "part_dans_l_emploi": "Part dans l'emploi",
    "part_dans_le_pib_bas": "Part dans le PIB, borne basse (estimation du gouvernement rapportée)",
    "part_dans_le_pib_haut": "Part dans le PIB, borne haute (estimation du gouvernement rapportée)",
    "steg_dette_exterieure_garantie": "Dette extérieure garantie de la STEG",
    "entreprises_cedees": "Entreprises cédées",
    "recettes_de_cession": "Recettes de cession",
    "part_investissement_direct_etranger": "Part des recettes en investissement direct étranger",
    "part_des_services_dans_les_recettes": "Part des services dans les recettes",
    "tunisie_telecom_ouverture_du_capital": "Ouverture du capital de Tunisie Télécom",
}


def tableau_etude(etude: str, caption: str, tbl_id: str) -> None:
    e = _s(S_ETUDES)
    e = e[e["etude"] == etude]
    lignes = []
    for r in e.itertuples():
        dec = 0 if float(r.valeur) == int(r.valeur) else 1
        page = str(r.page_imprimee) if str(r.page_imprimee).isdigit() else f"{r.page_pdf} du fichier"
        lignes.append([NOMS_GRANDEURS.get(r.grandeur, r.grandeur), str(r.periode),
                       _n(r.valeur, dec), str(r.unite), page])
    _md(["Grandeur", "Période", "Valeur", "Unité, dans les mots de la source", "Page"], "ggdgg",
        lignes, caption, tbl_id)


# --- point d'entrée ------------------------------------------------------------------------------------

FIGURES = {
    "ensemble": (fig_ensemble, table_ensemble,
                 (S_TRANSFERTS, S_GARANTIES, S_CROISEES, S_DIVIDENDES), "fig_ep_ensemble"),
    "transferts": (fig_transferts, table_transferts, (S_TRANSFERTS,), "fig_ep_transferts"),
    "garanties": (fig_garanties, table_garanties, (S_GARANTIES,), "fig_ep_garanties"),
    "flux": (fig_flux, table_flux, (S_FLUX,), "fig_ep_flux"),
    "resultats": (fig_resultats, table_resultats, (S_AGREGATS,), "fig_ep_resultats"),
    "cessions": (fig_cessions, table_cessions,
                 (S_CESSIONS,) + tuple(dinars_constants.SERIES_IPC), "fig_ep_cessions"),
}


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Trace la figure `nom` en onglets (chunk `output: asis`, étiqueté `fig-…`)."""
    trace, table, series, slug = FIGURES[nom]
    figtools.figure_tabs(trace(), table(), *series, slug=slug, caption=caption,
                         note_lecture=note_lecture)
    plt.close("all")

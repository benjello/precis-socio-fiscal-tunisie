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
(l'entrepôt s'il est installé, sinon le cache `precis/_seriescache/`), et les dénominateurs
de la série `compensation-parts`. Rien n'est saisi ici : ni valeur, ni page.

RÈGLES COMMUNES.

  - **Aucune série ne se chaîne d'une édition à l'autre.** Le rapport sur les entreprises
    publiques change d'échantillon à chaque édition : une édition = un segment, deux
    exercices reliés entre eux et à rien d'autre.
  - **Pour le rapport sur les transferts et les garanties**, dont le total est homogène
    depuis l'édition LF 2021, une année est donnée dans la dernière édition qui la porte en
    réalisation ; 2016 n'existe que dans l'ancien périmètre et reste isolée.
  - **Ce qui n'est pas une réalisation est en marque creuse** : loi de finances, valeur
    provisoire, estimation de fin juin, dividende partiel.
  - **Trois mesures par figure** : dinars courants, part des dépenses de l'État hors service
    de la dette, part du PIB — les dénominateurs du volume « La compensation ». La part du
    PIB se trace par segment de base, la base écrite au-dessus du cadre ; rien n'est raccordé.

Les libellés sont en français : le livre arabe n'existe pas encore. Ils sont réunis dans
`LIB` pour qu'une table arabe s'y ajoute sans toucher au reste.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
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
# Les dénominateurs sont ceux du volume « La compensation », lus dans sa série à tracer :
# dépenses de l'État hors service de la dette (1986-1987, puis depuis 1991) et PIB par segment
# de base (depuis 1986). Leur provenance est déclarée à part, sous `DENOMINATEURS`.
S_DENOMINATEURS = "compensation-parts"
DENOMINATEURS = "entreprises-publiques-denominateurs"
VUES = {"md": "Dinars courants", "dep": "% des dépenses de l'État", "pib": "% du PIB"}

figtools.register_provenance(
    DENOMINATEURS,
    titre=("Dénominateurs des parts : dépenses de l'État hors service de la dette et PIB aux "
           "prix courants, par segment de base"),
    sources=["minfin-remunerations", "minfin-indicateurs-fp", "ins-cnat-2015"],
    unite="millions de dinars courants",
    perimetre=("dépenses du budget de l'État hors service de la dette (ministère des Finances, "
               "répartition économique des dépenses), 1986-1987 et depuis 1991 ; PIB aux prix "
               "courants : ministère des Finances de 1986 à 2009 (base 1983 jusqu'en 1996, "
               "présumée avant 1992 ; base 1997 de 1997 à 2001 et de 2005 à 2009 ; valeur propre "
               "au ministère, rattachée à aucune base, de 2002 à 2004), Institut national de la "
               "statistique en base 2015 de 2010 à 2024 (rétropolé par l'INS pour 2010-2014)"),
    caveats=("Mêmes dénominateurs que le volume « La compensation ». Les bases du PIB ne sont "
             "pas raccordées : la part du PIB se lit par segment, chaque changement de base est "
             "une rupture du seul dénominateur. Dépenses de l'État non disponibles de 1988 à "
             "1990. Un encours rapporté aux dépenses ou au PIB de l'année rapporte un stock à "
             "un flux."),
)
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
    df = pd.DataFrame(lignes, columns=["Grandeur", "Année ou exercice",
                                       "Millions de dinars courants", "État de la valeur",
                                       "Édition"])
    annees = [_annee_de(p) for p in df["Année ou exercice"]]
    df["% des dépenses de l'État hors service de la dette"] = [
        _arrondi(_part(v, a, "dep")) if a else None
        for a, v in zip(annees, df["Millions de dinars courants"])]
    df["% du PIB"] = [_arrondi(_part(v, a, "pib")) if a else None
                      for a, v in zip(annees, df["Millions de dinars courants"])]
    df["Base du PIB"] = [_base_courte(a) if a else "" for a in annees]
    return df


def fig_ensemble():
    return _trois_vues(_fig_ensemble)


# --- transferts du budget (annexe 8) ---------------------------------------------------------

def _barres_empilees(ax, t, cles, couleurs, mesure="md"):
    bas = [0.0] * len(t)
    for cle, coul in zip(cles, couleurs):
        for i, r in enumerate(t.itertuples()):
            v = _part(getattr(r, cle), r.annee, mesure)
            if v is None:
                continue
            creux = r.etat != "réalisations"
            ancien = r.perimetre.startswith("ancien")
            barre = ax.bar(r.annee, v, bottom=bas[i], color=coul, width=0.72,
                           alpha=0.45 if (creux or ancien) else 1.0,
                           hatch="//" if creux else ("..." if ancien else None),
                           edgecolor="white", lw=0.5)
            unite = "MD" if mesure == "md" else "%"
            figtools.infobulle(barre[0], f"{r.annee} — {LIB[cle]} : "
                                         f"{_n(v, 1 if mesure == 'md' else 2)} {unite} "
                                         f"({_ed(r.edition)}, {r.etat})")
            bas[i] += v
    return bas


def fig_transferts():
    return _trois_vues(_fig_transferts)


def table_transferts():
    t = _transferts_retenus("secteur").rename(columns=LIB)
    t = t.rename(columns={"annee": "Année", "etat": "État", "edition": "Édition",
                          "perimetre": "Périmètre", "total": "Total (MD courants)"})
    t = _ajoute_parts(t, "Année", "Total (MD courants)", "total")
    t["Base du PIB"] = [_base_courte(a) for a in t["Année"]]
    return t


def tableau_transferts(caption: str, tbl_id: str = "tbl-ep-transferts") -> None:
    t = _transferts_retenus("secteur")
    lignes = []
    for r in t.itertuples():
        etat = "loi de finances" if r.etat != "réalisations" else (
            "réalisé, ancien périmètre" if r.perimetre.startswith("ancien") else "réalisé")
        lignes.append([str(r.annee), etat, _ed(r.edition), _n(r.total),
                       _n(_part(r.total, r.annee, "dep")), _n(_part(r.total, r.annee, "pib")),
                       _n(r.secteur_economique), _n(r.secteur_social),
                       _n(r.secteur_educatif_culturel), _n(r.secteur_souverainete)])
    _md(["Année", "État de la valeur", "Édition", "Total<br>(MD courants)",
         "Total<br>(% des dépenses de l'État)", "Total<br>(% du PIB)",
         "Secteur économique<br>(MD courants)", "Secteur social<br>(MD courants)",
         "Éducatif et culturel<br>(MD courants)", "Souveraineté<br>(MD courants)"],
        "gggddddddd", lignes, caption, tbl_id)


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
    return _trois_vues(_fig_garanties)


def _lignes_garanties():
    ext, inte = _garanties("garanties_exterieures"), _garanties("garanties_interieures")
    acc, plaf = _garanties("garanties_accordees"), _garanties("plafond")
    lignes = []
    for a in sorted(int(p) for p in acc):
        p = str(a)
        lignes.append((p, plaf.get(p), acc.get(p), _part(acc.get(p), a, "dep"),
                       _part(acc.get(p), a, "pib"), ext.get(p), inte.get(p)))
    s1 = "premier semestre"
    lignes.append(("2024, premier semestre", _garanties("plafond", s1).get("2024-S1"),
                   _garanties("garanties_accordees", s1).get("2024-S1"), None, None,
                   _garanties("garanties_exterieures", s1).get("2024-S1"),
                   _garanties("garanties_interieures", s1).get("2024-S1")))
    return lignes


def table_garanties():
    import pandas as pd
    return pd.DataFrame(
        [(l[0], l[1], l[2], _arrondi(l[3]), _arrondi(l[4]), l[5], l[6])
         for l in _lignes_garanties()],
        columns=["Année", "Plafond (MD)", "Garanties accordées (MD courants)",
                 "Garanties accordées (% des dépenses de l'État hors service de la dette)",
                 "Garanties accordées (% du PIB, base 2015)", "dont prêts extérieurs (MD)",
                 "dont prêts intérieurs (MD)"])


def tableau_garanties(caption: str, tbl_id: str = "tbl-ep-garanties") -> None:
    lignes = [[l[0], _n(l[1], 0), _n(l[2]), _n(l[3]), _n(l[4]), _n(l[5]), _n(l[6])]
              for l in _lignes_garanties()]
    _md(["Année", "Plafond<br>(MD)", "Garanties accordées<br>(MD courants)",
         "Garanties accordées<br>(% des dépenses de l'État)", "Garanties accordées<br>(% du PIB)",
         "dont extérieures<br>(MD)", "dont intérieures<br>(MD)"], "g" + "d" * 6, lignes,
        caption, tbl_id)


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

    def serie(cote, poste):
        return c[(c["cote"] == cote) & (c["poste"] == poste)].set_index("fin_annee")["valeur_md"]

    def ligne(cote, poste, nom):
        x = serie(cote, poste)
        return [nom] + [_n(x.get(a)) for a in annees]

    def parts(cote, mesure, nom):
        x = serie(cote, "total")
        return [nom] + [_n(_part(x.get(a), a, mesure)) + " %" for a in annees]
    lignes = [ligne("creances_sur_etat", "total", "**Créances des entreprises sur l'État**"),
              parts("creances_sur_etat", "dep", "— en % des dépenses de l'État de l'année"),
              parts("creances_sur_etat", "pib", "— en % du PIB de l'année")]
    for p in ("subventions_non_reglees", "prestations_rendues", "impots_taxes",
              "autres_creances", "gestion_de_fonds"):
        lignes.append(ligne("creances_sur_etat", p, "— " + LIB[p]))
    lignes += [ligne("dettes_envers_etat", "total", "**Dettes des entreprises envers l'État**"),
               parts("dettes_envers_etat", "dep", "— en % des dépenses de l'État de l'année"),
               parts("dettes_envers_etat", "pib", "— en % du PIB de l'année")]
    for p in ("impots_taxes", "prets_avances_tresor", "autres_dettes",
              "ligne_fr_redevances_ar_dividendes", "ligne_fr_dividendes_excedents_ar_redevances"):
        lignes.append(ligne("dettes_envers_etat", p, "— " + LIB[p]))
    lignes.append(ligne("ecart", "dettes_moins_creances", "**Dettes moins créances**"))
    _md(["Poste"] + [f"Fin {a}<br>(MD)" for a in annees], "g" + "d" * len(annees), lignes,
        caption, tbl_id)


def _croisees_figure():
    """Totaux de fin d'année : dettes envers l'État, créances sur l'État, et leur solde
    (créances moins dettes), lus dans la série qui nourrit le tableau."""
    c = _s(S_CROISEES)

    def x(cote, poste):
        return c[(c["cote"] == cote) & (c["poste"] == poste)].set_index("fin_annee")["valeur_md"]
    return {"dettes": x("dettes_envers_etat", "total"), "creances": x("creances_sur_etat", "total"),
            "solde": -x("ecart", "dettes_moins_creances")}


def _fig_croisees(mesure: str):
    figtools.apply_lang_font()
    t = _croisees_figure()
    ans = sorted(int(a) for a in t["dettes"].index)
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    larg = 0.26
    for k, (cle, coul, nom) in enumerate((
            ("dettes", BLEU, "dettes des entreprises envers l'État"),
            ("creances", ORANGE, "créances des entreprises sur l'État"),
            ("solde", GRIS, "solde : créances moins dettes (dû par l'État)"))):
        xs, ys = _xy(ans, [t[cle][a] for a in ans], mesure)
        barres = ax.bar([a + (k - 1) * larg for a in xs], ys, width=larg, color=coul, label=nom)
        unite = "MD" if mesure == "md" else "%"
        for barre, a, y in zip(barres, xs, ys):
            figtools.infobulle(barre, f"Fin {a} — {nom} : {_n(y, 1 if mesure == 'md' else 2)} "
                                      f"{unite}")
    _style(ax)
    _axe(ax, mesure, milliards=False)
    ax.set_xticks(ans)
    ax.set_xticklabels([f"fin {a}" for a in ans])
    if mesure == "pib":
        _marque_pib(ax, min(ans), max(ans))
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    ax.set_ylim(top=ax.get_ylim()[1] * 1.15)
    fig.tight_layout()
    return fig


def fig_croisees():
    return _trois_vues(_fig_croisees)


def table_croisees():
    import pandas as pd
    t = _croisees_figure()
    ans = sorted(int(a) for a in t["dettes"].index)
    df = pd.DataFrame({
        "Fin d'année": ans,
        "Dettes envers l'État (MD)": [t["dettes"][a] for a in ans],
        "Créances sur l'État (MD)": [t["creances"][a] for a in ans],
        "Solde, créances moins dettes (MD)": [t["solde"][a] for a in ans]})
    for col, nom in (("Dettes envers l'État (MD)", "dettes"),
                     ("Créances sur l'État (MD)", "créances")):
        df = _ajoute_parts(df, "Fin d'année", col, nom)
    df["Base du PIB"] = [_base_courte(a) for a in ans]
    return df


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
        a = int(r.exercice)
        lignes.append([str(r.exercice), _ed(r.edition), r.etat, _n(r.valeur),
                       _n(_part(r.valeur, a, "dep"), 2), _n(_part(r.valeur, a, "pib"), 2),
                       "" if x.empty else _n(x.iloc[0]["valeur"], 0)])
    _md(["Exercice", "Édition", "État de la valeur", "Part de l'État<br>(MD courants)",
         "Part de l'État<br>(% des dépenses de l'État)", "Part de l'État<br>(% du PIB)",
         "Entreprises distributrices"], "gggdddd", lignes, caption, tbl_id)


def fig_flux():
    return _trois_vues(_fig_flux)


def table_flux():
    v = _flux_totaux()
    t = v.pivot_table(index=["annee", "statut", "edition", "echantillon"],
                      columns=["flux", "poste"], values="valeur_md", aggfunc="max")
    t.columns = [f"{a} : {b}" for a, b in t.columns]
    t = t.reset_index().rename(columns={"annee": "Année", "statut": "État",
                                        "edition": "Édition", "echantillon": "Échantillon"})
    for flux in ("versements", "transferts"):
        t = _ajoute_parts(t, "Année", f"{flux} : total", f"{flux}, total")
    return t


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
    return _trois_vues(_fig_resultats)


def table_resultats():
    t = _agregats().rename(columns={"exercice": "Exercice", "edition": "Édition",
                                    "echantillon": "Entreprises"})
    t = _ajoute_parts(t, "Exercice", "resultat_net", "résultat net agrégé")
    return t.rename(columns=LIB)


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
    t["dep"] = [_part(v, a, "dep") for v, a in zip(t["classeur 1987-2009"], t["annee"])]
    t["pib"] = [_part(v, a, "pib") for v, a in zip(t["classeur 1987-2009"], t["annee"])]
    return t


def fig_cessions():
    return _trois_vues(_fig_cessions)


def table_cessions():
    t = _cessions().copy()
    t["dep"] = [_arrondi(x) for x in t["dep"]]
    t["pib"] = [_arrondi(x) for x in t["pib"]]
    t["Base du PIB"] = [_base_courte(a) for a in t["annee"]]
    return t.rename(columns={"annee": "Année",
                             "classeur 1987-2005": "Édition 1987-2005 (MD courants)",
                             "classeur 1987-2009": "Édition 1987-2009 (MD courants)",
                             "dep": "% des dépenses de l'État hors service de la dette",
                             "pib": "% du PIB"})


def tableau_cessions(caption: str, tbl_id: str = "tbl-ep-cessions") -> None:
    t = _cessions()
    lignes = []
    for r in t.itertuples(index=False):
        a, e1, e2, dep, pib = r
        autre = _n(e1, 1) if e1 == e1 and abs(e1 - e2) >= 0.05 else ""
        lignes.append([str(a), _n(e2, 1), _n(dep, 2) if dep == dep and dep is not None else "",
                       _n(pib, 2), _base_courte(a), autre])
    tot = t["classeur 1987-2009"].sum()
    lignes.append(["**1987-2009**", f"**{_n(tot, 1)}**", "", "", "", ""])
    _md(["Année", "Recettes<br>(MD courants)", "Recettes<br>(% des dépenses de l'État)",
         "Recettes<br>(% du PIB)", "Base du PIB",
         "Édition 1987-2005,<br>si elle diffère<br>(MD courants)"], "gdddgd", lignes, caption,
        tbl_id)


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
        # À défaut de numéro imprimé, le numéro donné est celui de la série ; le chapitre le
        # signale au documentaliste par un TODO caché, jamais dans le texte rendu.
        page = str(r.page_imprimee) if str(r.page_imprimee).isdigit() else str(r.page_pdf)
        lignes.append([NOMS_GRANDEURS.get(r.grandeur, r.grandeur), str(r.periode),
                       _n(r.valeur, dec), str(r.unite), page])
    _md(["Grandeur", "Période", "Valeur", "Unité, dans les mots de la source", "Page"], "ggdgg",
        lignes, caption, tbl_id)


def _den():
    """Dénominateurs par année, lus dans la série de la compensation qui les porte déjà :
    dépenses de l'État hors service de la dette, PIB, base et segment du PIB, rétropolation.

    Ce sont les dénominateurs du volume « La compensation », repris tels quels : rien n'est
    recalculé ni raccordé ici."""
    d = _s(S_DENOMINATEURS)
    cols = ["annee", "depenses_etat_hors_dette_MDT", "pib_MDT", "base_pib", "segment_pib",
            "pib_retropole"]
    u = d[cols].dropna(subset=["pib_MDT"]).sort_values(
        ["annee", "depenses_etat_hors_dette_MDT"]).groupby("annee").first()
    return u


def _part(valeur, annee, mesure: str):
    """La valeur dans la mesure demandée ; None si le dénominateur de l'année manque."""
    if valeur is None or valeur != valeur:
        return None
    if mesure == "md":
        return float(valeur)
    den = _den()
    a = int(annee)
    if a not in den.index:
        return None
    x = den.at[a, "depenses_etat_hors_dette_MDT" if mesure == "dep" else "pib_MDT"]
    return None if x != x else 100.0 * float(valeur) / float(x)


def _base_courte(annee: int) -> str:
    """Base du PIB de l'année, en clair, pour une colonne de tableau."""
    den = _den()
    if int(annee) not in den.index:
        return ""
    seg = str(den.at[int(annee), "segment_pib"])
    m = re.search(r"\((.*)\)", seg)
    base = m.group(1) if m else seg
    if base.startswith("non rattach"):
        return "valeur du ministère des Finances, sans base"
    if den.at[int(annee), "pib_retropole"] == "oui":
        base += ", rétropolée"
    return base


def _axe(ax, mesure: str, milliards: bool = True) -> None:
    """Graduations et nom de l'axe des ordonnées, selon la mesure."""
    if mesure == "md":
        if milliards:
            _milliards(ax)
            ax.set_ylabel("milliards de dinars courants")
        else:
            ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _n(v, 0)))
            ax.set_ylabel("millions de dinars courants")
    else:
        ax.yaxis.set_major_formatter(FuncFormatter(
            lambda v, _: _n(v, 0 if abs(v - round(v)) < 1e-9 else (1 if abs(v) >= 1 else 2))))
        ax.set_ylabel("% des dépenses de l'État hors service de la dette" if mesure == "dep"
                      else "% du PIB")


def _marque_pib(ax, x0: int, x1: int, dedans: bool = False) -> None:
    """Segments de PIB entre `x0` et `x1` : un trait vertical à chaque changement de segment,
    la base de chaque segment au-dessus du cadre (ou dans le cadre, `dedans`)."""
    den = _den()
    den = den[(den.index >= x0) & (den.index <= x1)]
    segments = []
    for a, seg in zip(den.index, den["segment_pib"].astype(str)):
        if segments and segments[-1][2] == seg:
            segments[-1][1] = a
        else:
            segments.append([a, a, seg])
    for i, (a0, a1, seg) in enumerate(segments):
        if i:
            figtools.marque_rupture(ax, a0)
        m = re.search(r"\((.*)\)", seg)
        base = m.group(1) if m else seg
        texte = {"base 1983 présumée": "base 1983\n(présumée)",
                 "non rattachée": "sans\nbase"}.get(base, base)
        bloc = den[(den.index >= a0) & (den.index <= a1)]
        if base.startswith("base") and (bloc["pib_retropole"] == "oui").all():
            texte += "\n(rétropolée)"
        if dedans:
            ax.annotate("PIB : " + texte.replace("\n", " "), xy=(0.99, 0.03),
                        xycoords="axes fraction", ha="right", va="bottom", fontsize=6.5,
                        color=GRIS)
        else:
            ax.annotate(texte, xy=((a0 + a1) / 2, 1), xycoords=("data", "axes fraction"),
                        xytext=(0, 5), textcoords="offset points", ha="center", va="bottom",
                        fontsize=6.5, color=GRIS, annotation_clip=False)
    if not dedans:
        ax.annotate("PIB :", xy=(0, 1), xycoords="axes fraction", xytext=(-6, 5),
                    textcoords="offset points", ha="right", va="bottom", fontsize=6.5,
                    color=GRIS, annotation_clip=False)


def _xy(annees, valeurs, mesure):
    """Points (année, valeur dans la mesure), années sans dénominateur retirées."""
    pts = [(int(a), _part(v, a, mesure)) for a, v in zip(annees, valeurs)]
    pts = [(a, v) for a, v in pts if v is not None]
    return [a for a, _ in pts], [v for _, v in pts]


def _trois_vues(trace):
    """Les trois vues d'une figure : `trace(mesure)` rend la figure d'une mesure."""
    return [(VUES[m], trace(m)) for m in ("md", "dep", "pib")]


def _ajoute_parts(df, col_annee: str, col_valeur: str, nom: str = ""):
    """Ajoute à un tableau de données les deux parts d'une colonne en millions de dinars."""
    suffixe = f" — {nom}" if nom else ""
    df[f"% des dépenses de l'État hors service de la dette{suffixe}"] = [
        _arrondi(_part(v, a, "dep")) for a, v in zip(df[col_annee], df[col_valeur])]
    df[f"% du PIB{suffixe}"] = [
        _arrondi(_part(v, a, "pib")) for a, v in zip(df[col_annee], df[col_valeur])]
    return df


def _arrondi(x, dec: int = 3):
    return None if x is None else round(x, dec)


def _annee_de(periode) -> int | None:
    s = str(periode)
    return int(s) if s.isdigit() else None


def _fig_ensemble(mesure: str):
    figtools.apply_lang_font()
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.8))
    creux = mesure == "md"  # la loi de finances et l'estimation de juin : en niveaux seulement
    # 1. Transferts du budget
    ax = axes[0][0]
    t = _transferts_retenus("secteur")
    nouv = t[(t["etat"] == "réalisations") & ~t["perimetre"].str.startswith("ancien")]
    ax.plot(*_xy(nouv["annee"], nouv["total"], mesure), color=NOIR, marker="o", lw=2, ms=4.5)
    anc = t[t["perimetre"].str.startswith("ancien")]
    ax.plot(*_xy(anc["annee"], anc["total"], mesure), color=NOIR, marker="s", ls="", ms=5,
            mfc="white")
    lf = t[t["etat"] != "réalisations"]
    ax.plot(*_xy(lf["annee"], lf["total"], mesure), color=NOIR, marker="o", ls="", ms=5.5,
            mfc="white")
    figtools.marque_rupture(ax, 2017, "périmètre révisé")
    ax.set_title("Ce que le budget verse : transferts à l'ensemble des entreprises\net "
                 "établissements publics non administratifs", fontsize=8.5, loc="left")
    # 2. Encours garanti
    ax = axes[0][1]
    e = _garanties("encours_total")
    ans = sorted(int(p) for p in e)
    ax.plot(*_xy(ans, [e[str(a)] for a in ans], mesure), color=BLEU, marker="o", lw=2, ms=4.5)
    juin = _garanties("encours_total", "fin juin (estimation)")
    if creux and "2024-06" in juin:
        ax.plot([2024], [juin["2024-06"]], color=BLEU, marker="o", ls="", ms=5.5, mfc="white")
    ax.set_title("Ce que l'État garantit : encours de la dette garantie,\nen fin d'année",
                 fontsize=8.5, loc="left")
    # 3. Dettes et créances croisées
    ax = axes[1][0]
    c = _croisees_totaux()
    ax.plot(*_xy(c.index, c["creances_sur_etat"], mesure), color=ROUGE, marker="o", lw=2,
            ms=4.5, label="créances des entreprises sur l'État")
    ax.plot(*_xy(c.index, c["dettes_envers_etat"], mesure), color=VERT, marker="s", lw=2,
            ms=4.5, label="dettes des entreprises envers l'État")
    ax.legend(fontsize=7, frameon=False, loc="lower left")
    ax.set_title("Ce que l'État doit et ce qui lui est dû : 42 entreprises,\nen fin d'année",
                 fontsize=8.5, loc="left")
    # 4. Dividendes
    ax = axes[1][1]
    d = _dividendes_retenus()
    arr = d[d["etat"] == "arrêté"]
    par = d[d["etat"] != "arrêté"]
    ax.plot(*_xy(arr["exercice"].astype(int), arr["valeur"], mesure), color=ORANGE, marker="o",
            lw=2, ms=4.5)
    ax.plot(*_xy(par["exercice"].astype(int), par["valeur"], mesure), color=ORANGE, marker="o",
            ls="", ms=5.5, mfc="white")
    ax.set_title("Ce que l'État reçoit : sa part dans les bénéfices et excédents,\npar "
                 "exercice", fontsize=8.5, loc="left")
    for ligne in axes:
        for ax in ligne:
            _style(ax)
            ax.set_xlim(2015.5, 2024.5)
            ax.set_xticks(range(2016, 2025))
            ax.tick_params(labelsize=7.5)
            ax.set_ylim(bottom=0)
            _axe(ax, mesure)
            ax.yaxis.label.set_size(7.5)
            if mesure == "pib":
                _marque_pib(ax, 2016, 2024, dedans=True)
    if mesure == "md":
        axes[1][1].yaxis.set_major_formatter(FuncFormatter(lambda v, _: _n(v, 0)))
        axes[1][1].set_ylabel("millions de dinars courants", fontsize=7.5)
    fig.tight_layout()
    return fig


def _fig_transferts(mesure: str):
    figtools.apply_lang_font()
    cles = ["secteur_economique", "secteur_social", "secteur_souverainete",
            "secteur_educatif_culturel"]
    t = _transferts_retenus("secteur")
    fig, ax = plt.subplots(figsize=(9.2, 5.4))
    couleurs = [ORANGE, BLEU, GRIS, VERT]
    _barres_empilees(ax, t, cles, couleurs, mesure)
    figtools.marque_rupture(ax, 2017)
    _style(ax)
    _axe(ax, mesure)
    ax.set_xticks(list(t["annee"]))
    if mesure == "pib":
        _marque_pib(ax, int(t["annee"].min()), int(t["annee"].max()))
    poignees = [Patch(color=c, label=LIB[k]) for k, c in zip(cles, couleurs)]
    poignees += [Patch(facecolor="#bbbbbb", hatch="...", edgecolor="white",
                       label="2016 : ancien périmètre"),
                 Patch(facecolor="#bbbbbb", hatch="//", edgecolor="white",
                       label="loi de finances")]
    ax.legend(handles=poignees, fontsize=8, frameon=False, loc="upper left", ncol=2)
    fig.tight_layout()
    return fig


def _fig_garanties(mesure: str):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ext, inte = _garanties("garanties_exterieures"), _garanties("garanties_interieures")
    plaf = _garanties("plafond")
    ans = sorted(int(p) for p in ext)
    xe, ye = _xy(ans, [ext[str(a)] for a in ans], mesure)
    xi, yi = _xy(ans, [inte[str(a)] for a in ans], mesure)
    ax.bar(xe, ye, color=BLEU, width=0.7, label="prêts extérieurs")
    ax.bar(xi, yi, bottom=ye, color=ORANGE, width=0.7, label="prêts intérieurs")
    xp, yp = _xy(ans, [plaf[str(a)] for a in ans], mesure)
    ax.step(xp, yp, where="mid", color=NOIR, lw=1.8,
            label="plafond de la loi de finances, après loi rectificative")
    _style(ax)
    _axe(ax, mesure)
    ax.set_xticks(ans)
    if mesure == "pib":
        _marque_pib(ax, min(ans), max(ans))
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    fig.tight_layout()
    return fig


def _fig_encours(mesure: str):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ee, ei = _garanties("encours_exterieur"), _garanties("encours_interieur")
    ans = sorted(int(p) for p in ee)
    xe, ye = _xy(ans, [ee[str(a)] for a in ans], mesure)
    xi, yi = _xy(ans, [ei[str(a)] for a in ans], mesure)
    ax.bar(xe, ye, color=BLEU, width=0.7, label="dette garantie extérieure")
    ax.bar(xi, yi, bottom=ye, color=ORANGE, width=0.7, label="dette garantie intérieure")
    je = _garanties("encours_exterieur", "fin juin (estimation)")
    ji = _garanties("encours_interieur", "fin juin (estimation)")
    if mesure == "md" and "2024-06" in je:
        ax.bar([2024], [je["2024-06"]], color=BLEU, width=0.7, alpha=0.45, hatch="//",
               edgecolor="white")
        ax.bar([2024], [ji["2024-06"]], bottom=[je["2024-06"]], color=ORANGE, width=0.7,
               alpha=0.45, hatch="//", edgecolor="white", label="fin juin 2024, estimation")
        ans = ans + [2024]
    if mesure == "pib":
        g = _s(S_GARANTIES)
        g = g[(g["grandeur"] == "encours_pct_pib") & (g["portee"] == "année")]
        for edition, marque in (("LF2022", "x"), ("LF2025", "+")):
            b = g[g["edition"] == edition]
            ax.plot(b["periode"].astype(int), b["valeur"], color=NOIR, marker=marque, ls="",
                    ms=7, mew=1.6,
                    label=f"part imprimée par le rapport, édition {_ed(edition)} "
                          "(base non dite)")
        _marque_pib(ax, min(ans), max(ans))
    _style(ax)
    _axe(ax, mesure)
    ax.set_xticks(ans)
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    ax.set_ylim(top=ax.get_ylim()[1] * 1.18)
    fig.tight_layout()
    return fig


def fig_encours():
    return _trois_vues(_fig_encours)


def _lignes_encours():
    et, ee, ei = (_garanties(g) for g in ("encours_total", "encours_exterieur",
                                          "encours_interieur"))
    lignes = [(str(a), et[str(a)], _part(et[str(a)], a, "dep"), _part(et[str(a)], a, "pib"),
               ee.get(str(a)), ei.get(str(a))) for a in sorted(int(p) for p in et)]
    j = "fin juin (estimation)"
    lignes.append(("fin juin 2024 (estimation)", _garanties("encours_total", j).get("2024-06"),
                   None, None, _garanties("encours_exterieur", j).get("2024-06"),
                   _garanties("encours_interieur", j).get("2024-06")))
    return lignes


def table_encours():
    import pandas as pd
    return pd.DataFrame(
        [(l[0], l[1], _arrondi(l[2]), _arrondi(l[3]), l[4], l[5]) for l in _lignes_encours()],
        columns=["Fin d'année", "Encours garanti (MD courants)",
                 "Encours garanti (% des dépenses de l'État hors service de la dette)",
                 "Encours garanti (% du PIB, base 2015, calculé)", "dont extérieur (MD)",
                 "dont intérieur (MD)"])


def _fig_dividendes(mesure: str):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.2, 4.8))
    d = _dividendes_retenus()
    arr = d[d["etat"] == "arrêté"]
    par = d[d["etat"] != "arrêté"]
    ax.plot(*_xy(arr["exercice"].astype(int), arr["valeur"], mesure), color=ORANGE, marker="o",
            lw=2, ms=5, label="exercice arrêté, dernière édition")
    ax.plot(*_xy(par["exercice"].astype(int), par["valeur"], mesure), color=ORANGE, marker="o",
            ls="", ms=6, mfc="white", label="montant partiel, à la date du rapport")
    ans = sorted(d["exercice"].astype(int))
    _style(ax)
    _axe(ax, mesure, milliards=False)
    ax.set_ylim(bottom=0)
    ax.set_xticks(ans)
    if mesure == "pib":
        _marque_pib(ax, min(ans), max(ans))
    ax.legend(fontsize=8, frameon=False, loc="upper right")
    fig.tight_layout()
    return fig


def fig_dividendes():
    return _trois_vues(_fig_dividendes)


def table_dividendes():
    d = _dividendes()[["exercice", "edition", "etat", "valeur"]].sort_values(
        ["exercice", "edition"]).copy()
    d["exercice"] = d["exercice"].astype(int)
    d = d.rename(columns={"exercice": "Exercice", "edition": "Édition",
                          "etat": "État de la valeur", "valeur": "Part de l'État (MD courants)"})
    d = _ajoute_parts(d, "Exercice", "Part de l'État (MD courants)")
    d["Base du PIB"] = [_base_courte(a) for a in d["Exercice"]]
    return d


def _fig_flux(mesure: str):
    figtools.apply_lang_font()
    v = _flux_totaux()
    v = v[(v["poste"] == "total") & (v["statut"] != "prévisionnel")]
    fig, ax = plt.subplots(figsize=(9.2, 5.4))
    for edition, bloc in v.groupby("edition"):
        for flux, coul, marque in (("transferts", ROUGE, "o"), ("versements", VERT, "s")):
            x = bloc[bloc["flux"] == flux].groupby(["annee", "statut"])["valeur_md"].max()
            x = x.reset_index().sort_values("annee")
            x["y"] = [_part(val, a, mesure) for a, val in zip(x["annee"], x["valeur_md"])]
            ax.plot(x["annee"], x["y"], color=coul, lw=1.6, alpha=0.9)
            for r in x.itertuples():
                pt, = ax.plot([r.annee], [r.y], color=coul, marker=marque, ms=5.5, ls="",
                              mfc="white" if r.statut != "réalisé" else coul)
                figtools.infobulle(pt, f"{flux}, {r.annee} : {_n(r.valeur_md)} MD — édition "
                                       f"{_ed(edition)}, {r.statut}")
            if len(x):
                d = x.iloc[-1]
                ax.annotate(_ed(edition), (d["annee"], d["y"]), xytext=(4, 4),
                            textcoords="offset points", fontsize=6.5, color=coul)
    ans = sorted(int(a) for a in v["annee"].unique())
    _style(ax)
    _axe(ax, mesure)
    ax.set_ylim(bottom=0)
    ax.set_xticks(ans)
    if mesure == "pib":
        _marque_pib(ax, min(ans), max(ans))
    ax.legend(handles=[
        Line2D([], [], color=ROUGE, marker="o", label="transferts reçus du budget"),
        Line2D([], [], color=VERT, marker="s", label="versements au budget"),
        Line2D([], [], color=GRIS, marker="o", mfc="white", ls="", label="valeur provisoire")],
        fontsize=8, frameon=False, loc="upper left")
    fig.tight_layout()
    return fig


def _fig_resultats(mesure: str):
    figtools.apply_lang_font()
    a = _agregats()
    fig, ax = plt.subplots(figsize=(9.2, 5.4))
    for edition, bloc in a.groupby("edition"):
        coul = COULEUR_EDITION.get(edition, NOIR)
        for col, ls, marque, lw in (("resultat_net", "-", "o", 2.0),
                                    ("resultats_nets_positifs", ":", "^", 1.0),
                                    ("resultats_nets_negatifs", ":", "v", 1.0)):
            ax.plot(*_xy(bloc["exercice"], bloc[col], mesure), color=coul, ls=ls, marker=marque,
                    lw=lw, ms=5 if lw > 1 else 4)
    ans = sorted(int(x) for x in a["exercice"].unique())
    ax.axhline(0, color=NOIR, lw=0.8)
    _style(ax)
    _axe(ax, mesure)
    ax.set_xticks(ans)
    if mesure == "pib":
        _marque_pib(ax, min(ans), max(ans))
    poignees = [Line2D([], [], color=COULEUR_EDITION[e], marker="o",
                       label=f"édition {_ed(e)} : {int(b['echantillon'].iloc[0])} entreprises")
                for e, b in a.groupby("edition")]
    poignees += [Line2D([], [], color=GRIS, marker="o", lw=2, label="résultat net agrégé"),
                 Line2D([], [], color=GRIS, marker="^", ls=":", lw=1,
                        label="somme des résultats positifs"),
                 Line2D([], [], color=GRIS, marker="v", ls=":", lw=1,
                        label="somme des résultats négatifs")]
    ax.legend(handles=poignees, fontsize=7.5, frameon=False, loc="upper center",
              bbox_to_anchor=(0.5, -0.08), ncol=3)
    fig.tight_layout()
    return fig


def _fig_cessions(mesure: str):
    figtools.apply_lang_font()
    t = _cessions()
    col = {"md": "classeur 1987-2009", "dep": "dep", "pib": "pib"}[mesure]
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    b = t[t[col].notna()]
    barres = ax.bar(b["annee"], b[col], color=BLEU, width=0.72)
    for barre, an, val in zip(barres, b["annee"], b[col]):
        figtools.infobulle(barre, f"{an} : {_n(val, 1 if mesure == 'md' else 2)} "
                                  f"{'MD' if mesure == 'md' else '%'}")
    if mesure == "md":
        div = t[(t["classeur 1987-2005"].notna()) &
                ((t["classeur 1987-2005"] - t["classeur 1987-2009"]).abs() > 1)]
        ax.plot(div["annee"], div["classeur 1987-2005"], color=ROUGE, marker="D", ls="", ms=5,
                mfc="white", label="valeur de l'édition 1987-2005, quand elle diffère")
        ax.legend(fontsize=8, frameon=False, loc="upper left")
    if mesure == "dep":
        manquantes = [int(a) for a in t[t["dep"].isna()]["annee"]]
        if manquantes:
            ax.axvspan(min(manquantes) - 0.5, max(manquantes) + 0.5, color="#eaeef2", zorder=0)
            ax.annotate("dépenses de l'État\nnon disponibles",
                        xy=((min(manquantes) + max(manquantes)) / 2, 0.5),
                        xycoords=("data", "axes fraction"), ha="center", va="center",
                        fontsize=7, color=GRIS, rotation=90)
    ax.set_yscale("log")
    _style(ax)
    _axe(ax, mesure, milliards=False)
    if mesure != "md":
        ax.yaxis.set_major_formatter(FuncFormatter(
            lambda v, _: _n(v, 0 if v >= 1 else (1 if v >= 0.1 else 2))))
    if mesure == "dep":
        ax.set_ylabel("% des dépenses de l'État")
    ax.set_ylabel(ax.get_ylabel() + " (échelle logarithmique)")
    ax.set_xlim(1986.3, 2009.7)
    ax.set_xticks(list(t["annee"])[::2])
    if mesure == "pib":
        _marque_pib(ax, 1987, 2009)
    fig.tight_layout()
    return fig


def chiffres() -> None:
    """Aide à la rédaction : les parts citées dans la prose (non appelée au rendu)."""
    t = _transferts_retenus("secteur")
    for r in t.itertuples():
        print("transferts", r.annee, _n(r.total), _n(_part(r.total, r.annee, "dep")),
              _n(_part(r.total, r.annee, "pib")))
    for l in _lignes_encours():
        print("encours", l[0], _n(l[1]), _n(l[2]), _n(l[3]))
    for l in _lignes_garanties():
        print("garanties", l[0], _n(l[2]), _n(l[3]), _n(l[4]))
    c = _croisees_totaux()
    for a in c.index:
        for k in c.columns:
            print("croisees", a, k, _n(_part(c.at[a, k], a, "dep")), _n(_part(c.at[a, k], a, "pib")))
    for r in _dividendes_retenus().itertuples():
        print("dividendes", r.exercice, r.etat, _n(r.valeur),
              _n(_part(r.valeur, int(r.exercice), "dep"), 2),
              _n(_part(r.valeur, int(r.exercice), "pib"), 2))
    a = _agregats()
    for r in a.itertuples():
        print("resultat", r.exercice, r.edition, _n(r.resultat_net),
              _n(_part(r.resultat_net, r.exercice, "dep"), 2),
              _n(_part(r.resultat_net, r.exercice, "pib"), 2))
    for r in _cessions().itertuples(index=False):
        print("cessions", r[0], _n(r[2]), r[3] and _n(r[3], 2), _n(r[4], 2), _base_courte(r[0]))


# --- effectifs et masse salariale ---------------------------------------------------------------

S_EFFECTIFS = "entreprises-publiques-effectifs-ensemble"
S_EFFECTIFS_EP = "entreprises-publiques-effectifs-par-entreprise"
COULEUR_EDITION["LF2020"] = BRUN = "#9a6700"
# Les dix plus gros employeurs de l'exercice 2022 parmi les entreprises des agrégats (hors
# secteur financier, hors caisses), dans l'ordre de leur effectif.
GROS_EMPLOYEURS = ("steg", "transtu", "cpg", "sonede", "tunisie_telecom", "otd", "gct", "sncft",
                   "oaca", "tunisair")
STATUTS_FERMES = ("réalisé", "non dit")
COURT.update({"otd": "Office des terres domaniales", "poste": "La Poste tunisienne"})
MINISTERES = {
    "transport": "Transport", "industrie": "Industrie", "finances": "Finances",
    "equipement": "Équipement", "agriculture": "Agriculture", "commerce": "Commerce",
    "tourisme": "Tourisme", "presidence_gouvernement": "Présidence du gouvernement",
    "affaires_sociales": "Affaires sociales",
    "technologies_telecommunications": "Technologies, information et télécommunications",
    "sante": "Santé", "interieur": "Intérieur", "jeunesse_sports": "Jeunesse et sports",
    "education": "Éducation", "environnement": "Environnement",
    "presidence_republique": "Présidence de la République", "total": "**Total**",
}


def _effectifs_ensemble():
    """Les quatre points publiés : une ligne par exercice."""
    e = _s(S_EFFECTIFS)
    lignes = []
    for (edition, exercice), b in e.groupby(["edition", "exercice"]):
        def v(perimetre, indicateur, col="valeur"):
            x = b[(b["perimetre"] == perimetre) & (b["indicateur"] == indicateur)]
            return None if x.empty else float(x.iloc[0][col])
        lignes.append(dict(
            edition=edition, exercice=int(exercice),
            n_agents=int(v("ensemble", "effectif", "nombre_entreprises")),
            n_charges=int(v("ensemble", "charges_personnel", "nombre_entreprises")),
            agents=v("ensemble", "effectif"), charges=v("ensemble", "charges_personnel"),
            agents_40=v("echantillon_40", "effectif"),
            part_40=v("part_echantillon", "effectif"),
            ecart_fiches=v("echantillon_40", "effectif", "ecart_somme_des_fiches")))
    return sorted(lignes, key=lambda l: l["exercice"])


def tableau_effectifs(caption: str, tbl_id: str = "tbl-ep-effectifs") -> None:
    lignes = []
    for l in _effectifs_ensemble():
        n = str(l["n_agents"]) if l["n_agents"] == l["n_charges"] else (
            f"{l['n_agents']} pour les agents, {l['n_charges']} pour les charges")
        dec = 0 if l["agents"] == int(l["agents"]) else 1
        cout = (_n(1e6 * l["charges"] / l["agents"], 0)
                if l["n_agents"] == l["n_charges"] else "")
        lignes.append([str(l["exercice"]), _ed(l["edition"]), n, _n(l["agents"], dec),
                       _n(l["charges"]), _n(_part(l["charges"], l["exercice"], "dep")),
                       _n(_part(l["charges"], l["exercice"], "pib"), 2), cout,
                       _n(l["agents_40"], 0 if l["agents_40"] == int(l["agents_40"]) else 1),
                       _n(l["part_40"])])
    _md(["Exercice", "Édition", "Entreprises", "Agents", "Charges de personnel<br>(MD courants)",
         "Charges de personnel<br>(% des dépenses de l'État)", "Charges de personnel<br>(% du PIB)",
         "Charges par agent<br>(D par an, calcul)", "Agents des 40 entreprises",
         "Part des 40<br>(% des agents)"], "ggg" + "d" * 7, lignes, caption, tbl_id)


def _fig_masse(mesure: str):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    a = _agregats()
    for edition, bloc in a.groupby("edition"):
        ax.plot(*_xy(bloc["exercice"], bloc["charges_personnel"], mesure),
                color=COULEUR_EDITION.get(edition, NOIR), marker="o", lw=1.6, ms=4.5)
    pts = _effectifs_ensemble()
    for l in pts:
        y = _part(l["charges"], l["exercice"], mesure)
        pt, = ax.plot([l["exercice"]], [y], color=NOIR, marker="D", ms=7, ls="", mfc="white",
                      mew=1.6)
        figtools.infobulle(pt, f"exercice {l['exercice']} : {_n(l['charges'])} MD, "
                               f"{l['n_charges']} entreprises (édition {_ed(l['edition'])})")
    ans = sorted(int(x) for x in a["exercice"].unique())
    _style(ax)
    _axe(ax, mesure)
    ax.set_ylim(bottom=0, top=ax.get_ylim()[1] * 1.08)
    ax.set_xticks(ans)
    if mesure == "pib":
        _marque_pib(ax, min(ans), max(ans))
    poignees = [Line2D([], [], color=COULEUR_EDITION[e], marker="o",
                       label=f"agrégats, édition {_ed(e)} : {int(b['echantillon'].iloc[0])} entreprises")
                for e, b in a.groupby("edition")]
    poignees.append(Line2D([], [], color=NOIR, marker="D", mfc="white", ls="", mew=1.6,
                           label="total publié avec l'effectif (82 à 88 entreprises)"))
    ax.legend(handles=poignees, fontsize=7.5, frameon=False, loc="lower right", ncol=2)
    fig.tight_layout()
    return fig


def fig_masse():
    return _trois_vues(_fig_masse)


def table_masse():
    import pandas as pd
    a = _agregats()[["exercice", "edition", "echantillon", "charges_personnel"]].copy()
    a["source"] = "tableau des agrégats"
    p = pd.DataFrame([dict(exercice=l["exercice"], edition=l["edition"],
                           echantillon=l["n_charges"], charges_personnel=l["charges"],
                           source="tableau de l'effectif total") for l in _effectifs_ensemble()])
    t = pd.concat([a, p]).sort_values(["exercice", "edition"]).rename(columns={
        "exercice": "Exercice", "edition": "Édition", "echantillon": "Entreprises",
        "charges_personnel": "Charges de personnel (MD courants)", "source": "Tableau du rapport"})
    t = _ajoute_parts(t, "Exercice", "Charges de personnel (MD courants)")
    t["Base du PIB"] = [_base_courte(x) for x in t["Exercice"]]
    return t


def _effectifs_ep():
    p = _s(S_EFFECTIFS_EP)
    return p[p["effectif"].notna()]


def fig_effectifs():
    figtools.apply_lang_font()
    p = _effectifs_ep()
    fig, axes = plt.subplots(2, 5, figsize=(11.5, 5.6))
    for ax, ent in zip(axes.flat, GROS_EMPLOYEURS):
        b = p[p["entite"] == ent]
        for edition, bloc in b.groupby("edition"):
            bloc = bloc.sort_values("exercice")
            coul = COULEUR_EDITION.get(edition, NOIR)
            ax.plot(bloc["exercice"], bloc["effectif"], color=coul, lw=1.4)
            for r in bloc.itertuples():
                pt, = ax.plot([r.exercice], [r.effectif], color=coul, marker="o", ms=4.5, ls="",
                              mfc=coul if r.statut in STATUTS_FERMES else "white")
                figtools.infobulle(pt, f"{COURT.get(ent, ent)}, {r.exercice} : "
                                       f"{_n(r.effectif, 0)} agents — édition {_ed(edition)}, "
                                       f"{r.statut}")
        ax.set_title(COURT.get(ent, ent).split(" (")[0], fontsize=8, loc="left")
        _style(ax)
        ax.set_xlim(2015.5, 2023.5)
        ax.set_xticks(range(2016, 2024, 2))
        ax.tick_params(labelsize=7)
        ax.set_ylim(bottom=0, top=max(b["effectif"]) * 1.25)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _n(v, 0)))
    editions = sorted(p["edition"].unique())
    poignees = [Line2D([], [], color=COULEUR_EDITION[e], marker="o", label=f"édition {_ed(e)}")
                for e in editions]
    poignees.append(Line2D([], [], color=GRIS, marker="o", mfc="white", ls="",
                           label="provisoire, estimé, probable ou comptes non approuvés"))
    fig.legend(handles=poignees, fontsize=8, frameon=False, loc="lower center", ncol=6)
    fig.supylabel("nombre d'agents", fontsize=8)
    fig.tight_layout(rect=(0.01, 0.06, 1, 1))
    return fig


def table_effectifs_ep():
    p = _effectifs_ep()
    p = p[p["entite"].isin(GROS_EMPLOYEURS)]
    t = p[["entite_nom", "exercice", "edition", "statut", "effectif",
           "charges_personnel_md"]].sort_values(["entite_nom", "exercice", "edition"])
    return t.rename(columns={"entite_nom": "Entreprise", "exercice": "Exercice",
                             "edition": "Édition", "statut": "État de la valeur",
                             "effectif": "Agents",
                             "charges_personnel_md": "Charges de personnel (MD courants)"})


def _cases_effectifs(bloc, col: str, dec: int) -> str:
    """Toutes les valeurs imprimées d'un exercice ; l'édition est nommée quand elles diffèrent,
    et un astérisque marque une valeur qui n'est dite ni réalisée ni sans réserve."""
    b = bloc[bloc[col].notna()].sort_values("edition")
    if b.empty:
        return "—"
    vals = [(r["edition"], float(r[col]), "" if r["statut"] in STATUTS_FERMES else "\\*")
            for _, r in b.iterrows()]
    if len({round(v, dec) for _, v, _ in vals}) == 1:
        return _n(vals[-1][1], dec) + vals[-1][2]
    vus, out = set(), []
    for e, v, m in vals:
        if round(v, dec) not in vus:
            vus.add(round(v, dec))
            out.append(f"{_n(v, dec)}{m} ({_ed(e)})")
    return " ; ".join(out)


def tableau_effectifs_entreprises(caption: str, col: str = "effectif",
                                  tbl_id: str = "tbl-ep-effectifs-entreprises") -> None:
    p = _s(S_EFFECTIFS_EP)
    dec = 0 if col == "effectif" else 1
    exercices = sorted(int(x) for x in p[p[col].notna()]["exercice"].unique())
    ordre = {"entreprise": 0, "secteur financier": 1, "banque": 2, "caisse sociale": 3}
    ref = p[p["effectif"].notna()].sort_values("exercice").groupby("entite")["effectif"].last()
    entites = sorted(p["entite"].unique(),
                     key=lambda e: (ordre.get(p[p["entite"] == e]["categorie"].iloc[0], 9),
                                    -float(ref.get(e, 0))))
    lignes = []
    for ent in entites:
        b = p[p["entite"] == ent]
        cat = b["categorie"].iloc[0]
        nom = b["entite_nom"].iloc[0] + ("" if cat == "entreprise" else f" ({cat})")
        lignes.append([nom] + [_cases_effectifs(b[b["exercice"] == x], col, dec)
                               for x in exercices])
    unite = "agents" if col == "effectif" else "MD"
    _md(["Entreprise"] + [f"{x}<br>({unite})" for x in exercices], "g" + "g" * len(exercices),
        lignes, caption, tbl_id)


def tableau_bm_2014(caption: str, tbl_id: str = "tbl-ep-banque-mondiale-2014") -> None:
    e = _s(S_ETUDES)
    e = e[e["etude"] == "wb-tunisia-gouvernance-ep-2014"]
    lignes = []
    for cle, nom in MINISTERES.items():
        n = e[e["grandeur"] == f"nombre_entreprises_tutelle_{cle}"]
        a = e[e["grandeur"] == f"effectif_tutelle_{cle}"]
        if n.empty and a.empty:
            continue
        lignes.append([nom, "" if n.empty else _n(n.iloc[0]["valeur"], 0),
                       "" if a.empty else _n(a.iloc[0]["valeur"], 0)])
    _md(["Ministère de tutelle", "Entreprises publiques<br>(2013)", "Employés<br>(2010)"], "gdd",
        lignes, caption, tbl_id)


def chiffres_effectifs() -> None:
    """Aide à la rédaction (non appelée au rendu)."""
    for l in _effectifs_ensemble():
        print(l, _n(_part(l["charges"], l["exercice"], "dep")),
              _n(_part(l["charges"], l["exercice"], "pib"), 2),
              _n(1e6 * l["charges"] / l["agents"], 0))
    p = _effectifs_ep()
    x = p[(p["exercice"] == 2022) & (p["edition"] == "LF2025") & p["entite"].isin(GROS_EMPLOYEURS)]
    print("dix premières 2022", x["effectif"].sum(), x["charges_personnel_md"].sum())
    for ent in GROS_EMPLOYEURS:
        b = p[p["entite"] == ent].sort_values(["exercice", "edition"])
        print(ent, [(r.exercice, r.edition[2:], int(r.effectif), r.statut[:4]) for r in b.itertuples()])


# --- point d'entrée ------------------------------------------------------------------------------------

FIGURES = {
    "ensemble": (fig_ensemble, table_ensemble,
                 (S_TRANSFERTS, S_GARANTIES, S_CROISEES, S_DIVIDENDES, DENOMINATEURS),
                 "fig_ep_ensemble"),
    "transferts": (fig_transferts, table_transferts, (S_TRANSFERTS, DENOMINATEURS),
                   "fig_ep_transferts"),
    "garanties": (fig_garanties, table_garanties, (S_GARANTIES, DENOMINATEURS),
                  "fig_ep_garanties"),
    "encours": (fig_encours, table_encours, (S_GARANTIES, DENOMINATEURS), "fig_ep_encours"),
    "dividendes": (fig_dividendes, table_dividendes, (S_DIVIDENDES, DENOMINATEURS),
                   "fig_ep_dividendes"),
    "flux": (fig_flux, table_flux, (S_FLUX, DENOMINATEURS), "fig_ep_flux"),
    "resultats": (fig_resultats, table_resultats, (S_AGREGATS, DENOMINATEURS),
                  "fig_ep_resultats"),
    "cessions": (fig_cessions, table_cessions, (S_CESSIONS, DENOMINATEURS), "fig_ep_cessions"),
    "croisees": (fig_croisees, table_croisees, (S_CROISEES, DENOMINATEURS), "fig_ep_croisees"),
    "masse": (fig_masse, table_masse, (S_EFFECTIFS, S_AGREGATS, DENOMINATEURS), "fig_ep_masse"),
    "effectifs": (fig_effectifs, table_effectifs_ep, (S_EFFECTIFS_EP,), "fig_ep_effectifs"),
}


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Trace la figure `nom` en onglets (chunk `output: asis`, étiqueté `fig-…`)."""
    trace, table, series, slug = FIGURES[nom]
    figtools.figure_tabs(trace(), table(), *series, slug=slug, caption=caption,
                         note_lecture=note_lecture)
    plt.close("all")

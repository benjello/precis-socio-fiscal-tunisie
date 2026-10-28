"""Figures et tableaux du livre *Les entreprises publiques*.

    from figures import entreprises_publiques as ep
    ep.figure("ensemble", caption=…, note_lecture=…)     # quatre grandeurs, 2016-2024
    ep.figure("transferts", …)                           # transferts du budget, annexe 8
    ep.figure("garanties", …)                            # plafond, garanties, encours
    ep.figure("flux", …)                                 # versements et transferts, échantillon
    ep.figure("resultats", …)                            # résultats agrégés, par édition
    ep.figure("cessions", …)                             # recettes de cession, 1987-2009
    ep.figure("versements", …)                           # versements au budget, 2003-2024
    ep.figure("bct_ra", …)                               # revenus des participations, 1983-2016
    ep.figure("cdf", …, nominal=False)                   # Cour de discipline financière, 1986-2009
    ep.tableau_transferts(caption=…) …                   # tableaux, tous lus dans les séries

D'OÙ VIENNENT LES DONNÉES. Douze séries de `tunisia-data`, lues par `figtools.series()`
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
import pandas as pd  # noqa: E402
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter, MaxNLocator

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

S_TRANSFERTS = "entreprises-publiques-transferts-budget"
S_TRANSFERTS_ETAB = "entreprises-publiques-transferts-par-etablissement"
S_COMPENSATION = "compensation-parts"
S_GARANTIES = "garanties-etat"
S_DIVIDENDES = "entreprises-publiques-dividendes-etat"
S_FLUX = "entreprises-publiques-versements-transferts"
S_AGREGATS = "entreprises-publiques-resultats-agreges"
S_CROISEES = "entreprises-publiques-dettes-creances-croisees"
S_TRANSFERTS_EP = "entreprises-publiques-transferts-par-entreprise"
S_NETS_EP = "entreprises-publiques-resultats-nets-dix-premieres"
S_CESSIONS = "privatisation-recettes-annuelles"
S_PLANS = "privatisation-recettes-par-plan"
S_BILAN = "privatisation-bilan-global-par-mode"
S_RECUEIL = "privatisation-recueil-operations"
S_NATURES = "privatisation-recueil-par-nature"
S_ANNEES_NATURES = "privatisation-recueil-par-annee-nature"
S_RECOUPEMENT = "privatisation-recueil-recoupement-annuel"
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


def _decomposition():
    """Total, caisses, STIR et STEG, Office des céréales et Office de l'huile, reste : une
    ligne par année, dans l'édition retenue pour le total de l'année."""
    d = _s(S_TRANSFERTS_ETAB)
    t = d.pivot_table(index=["annee", "etat", "edition"], columns="grandeur",
                      values="valeur_md").reset_index().sort_values("annee")
    for c in ("caisses", "stir_steg", "office_cereales_office_huile", "reste"):
        if c not in t:
            t[c] = float("nan")
    return t


def tableau_transferts_reste(caption: str, tbl_id: str = "tbl-ep-transferts-reste") -> None:
    lignes = []
    for r in _decomposition().itertuples():
        etat = "réalisé" if r.etat == "réalisations" else "loi de finances"
        lignes.append([str(r.annee), etat, _ed(r.edition), _n(r.total), _n(r.caisses),
                       _n(r.stir_steg), _n(r.office_cereales_office_huile), _n(r.reste),
                       _n(_part(r.reste, r.annee, "dep")), _n(_part(r.reste, r.annee, "pib"))])
    _md(["Année", "État de la valeur", "Édition", "Total<br>(MD)",
         "Caisses de sécurité sociale<br>(MD)", "STIR et STEG<br>(MD)",
         "Office des céréales et Office de l'huile<br>(MD)", "Reste<br>(MD)",
         "Reste<br>(% des dépenses de l'État)", "Reste<br>(% du PIB)"],
        "gggddddddd", lignes, caption, tbl_id)


def tableau_transferts_compensation(caption: str,
                                    tbl_id: str = "tbl-ep-transferts-compensation") -> None:
    """Les lignes retranchées du total, en regard des postes de la dépense de compensation."""
    c = _s(S_COMPENSATION)
    c = c[c["famille"] == "budget"].pivot_table(index="annee", columns="poste",
                                                values="valeur_MDT")
    lignes = []
    for r in _decomposition().itertuples():
        a = int(r.annee)
        comp = c.loc[a] if a in c.index else None
        prod = None if comp is None else comp.get("produits_de_base")
        ecart = (None if prod is None or r.office_cereales_office_huile != r.office_cereales_office_huile
                 else r.office_cereales_office_huile - prod)
        lignes.append([str(a), _n(r.stir_steg), _n(None if comp is None else comp.get("carburants")),
                       _n(r.office_cereales_office_huile), _n(prod), _n(ecart),
                       _n(None if comp is None else comp.get("transport"))])
    _md(["Année", "STIR et STEG<br>(MD)", "Compensation des carburants<br>(MD)",
         "Office des céréales et Office de l'huile<br>(MD)",
         "Compensation des produits de base<br>(MD)", "Écart<br>(MD)",
         "Compensation du transport, restée dans le reste<br>(MD)"],
        "gdddddd", lignes, caption, tbl_id)


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


def _cessions_budget():
    """Recettes de privatisation inscrites au budget de l'État, par gestion depuis 2010, d'après
    les rapports de clôture de la Cour des comptes : colonnes `annee`, `budget` (MD), `dep`, `pib`.
    Autre source, autre périmètre que le relevé de la Direction générale de la privatisation :
    une recette inscrite au budget d'une gestion, non le produit d'une opération."""
    v = _cdc("recettes_privatisation_budget")
    if "total" not in v.columns:
        return pd.DataFrame(columns=["annee", "budget", "dep", "pib"])
    v = v["total"]
    v = v[v.index.astype(int) >= 2010]
    t = pd.DataFrame({"annee": v.index.astype(int), "budget": v.values})
    t["dep"] = [_part(x, a, "dep") for x, a in zip(t["budget"], t["annee"])]
    t["pib"] = [_part(x, a, "pib") for x, a in zip(t["budget"], t["annee"])]
    return t.reset_index(drop=True)


def fig_cessions():
    return _trois_vues(_fig_cessions)


def table_cessions():
    t = _cessions().copy()
    t["source"] = "Direction générale de la privatisation, relevé arrêté à 2009"
    b = _cessions_budget().rename(columns={"budget": "classeur 1987-2009"})
    b["source"] = "recette inscrite au budget, rapport de clôture de la Cour des comptes"
    t = pd.concat([t, b], ignore_index=True, sort=False)
    t["dep"] = [_arrondi(x) for x in t["dep"]]
    t["pib"] = [_arrondi(x) for x in t["pib"]]
    t["Base du PIB"] = [_base_courte(a) for a in t["annee"]]
    return t.rename(columns={"annee": "Année",
                             "classeur 1987-2005": "Édition 1987-2005 (MD courants)",
                             "classeur 1987-2009": "Recettes (MD courants)",
                             "dep": "% des dépenses de l'État hors service de la dette",
                             "pib": "% du PIB", "source": "Source"})


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
    b = _cessions_budget()
    for r in b.itertuples(index=False):
        if r.budget != r.budget:
            lignes.append([f"{r.annee} (budget)", "aucune ligne", "", "", _base_courte(r.annee), ""])
            continue
        lignes.append([f"{r.annee} (budget)", _n(r.budget, 1),
                       _n(r.dep, 2) if r.dep is not None and r.dep == r.dep else "",
                       _n(r.pib, 2) if r.pib is not None and r.pib == r.pib else "",
                       _base_courte(r.annee), ""])
    if len(b):
        bb = b[b.budget.notna()]
        lignes.append([f"**{int(bb.annee.min())}-{int(bb.annee.max())} (budget)**",
                       f"**{_n(bb.budget.sum(), 1)}**", "", "", "", ""])
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


# --- opérations de cession : bilan global et recueil depuis 1998 -------------------------------------

NATURES = {  # ordre et libellés courts ; la règle de classement est dans tunisia-data
    "titres": "Cession de titres",
    "bourse": "Offre publique ou vente en bourse",
    "concession": "Concession",
    "actifs": "Vente d'actifs",
    "actifs_liquidation": "Vente d'actifs d'une entreprise en liquidation",
}
SECTEURS_RECUEIL = {
    "agriculture": "Agriculture", "peche": "Pêche", "services_agricoles": "Services agricoles",
    "agroalimentaire": "Industries agroalimentaires",
    "imccv": "Matériaux de construction, céramique et verre",
    "ime": "Industries mécaniques et électriques", "chimie": "Industries chimiques",
    "cuir_textiles": "Cuir et textiles", "industries_diverses": "Autres industries",
    "tourisme_artisanat": "Tourisme et artisanat", "commerce": "Commerce", "transport": "Transport",
    "services_financiers": "Services financiers", "autres_services": "Autres services",
}


def tableau_cessions_modes(caption: str, tbl_id: str = "tbl-ep-cessions-modes") -> None:
    """Entreprises par mode de privatisation ou de restructuration, 1987-2009 (bilan global)."""
    b = _s(S_BILAN)
    lignes = []
    for r in b.itertuples(index=False):
        gras = (lambda x: f"**{x}**") if r.mode == "total" else (lambda x: x)
        lignes.append([gras(r.mode_imprime), gras(_n(r.entreprises, 0)), gras(_n(r.part_imprimee_pct, 0))])
    _md(["Mode", "Entreprises", "% du total"], "gdd", lignes, caption, tbl_id)


def tableau_cessions_natures(caption: str, tbl_id: str = "tbl-ep-cessions-natures") -> None:
    """Lignes, sociétés et produit du recueil 1998-2008, par nature de l'acte."""
    n = _s(S_NATURES).set_index("nature")
    lignes = []
    for code in list(NATURES) + ["ensemble"]:
        r = n.loc[code]
        nom = NATURES.get(code, "**Ensemble**")
        g = (lambda x: f"**{x}**") if code == "ensemble" else (lambda x: x)
        lignes.append([nom, g(_n(r.lignes_du_recueil, 0)), g(_n(r.societes, 0)), g(_n(r.produit_md, 1))])
    _md(["Nature de l'acte", "Lignes du recueil", "Sociétés", "Produit (MD courants)"], "gddd",
        lignes, caption, tbl_id)


NATURES_COURTES = {"titres": "Titres", "bourse": "Bourse", "concession": "Concession",
                   "actifs": "Actifs", "actifs_liquidation": "Actifs en liquidation"}


def _md_petit(v_md: float) -> str:
    """Millions de dinars à une décimale ; « < 0,1 » pour un produit positif plus petit."""
    return "< 0,1" if 0 < v_md < 0.05 else _n(v_md, 1)


def tableau_cessions_annees(caption: str, tbl_id: str = "tbl-ep-cessions-recueil-annees") -> None:
    """Produit du recueil par année et nature, en regard du relevé annuel arrêté à 2009."""
    a = _s(S_ANNEES_NATURES)
    a["annee"] = a["annee"].astype(str)
    rec = _s(S_RECOUPEMENT).set_index("annee")
    lignes = []
    for annee in list(dict.fromkeys(a["annee"])):
        d = a[a["annee"] == annee].set_index("nature")
        cases = [_md_petit(d.loc[c, "produit_milliers_dinars"] / 1000) if d.loc[c, "lignes_du_recueil"]
                 else "" for c in NATURES]
        ens = d.loc["ensemble"]
        fin = ["", ""]
        if annee.isdigit() and int(annee) in rec.index:
            r = rec.loc[int(annee)]
            e = r.ecart_recueil_moins_classeur_1987_2009_md
            fin = [_n(r.classeur_1987_2009_md, 1), "0,0" if abs(e) < 0.05 else _n(e, 1, signe=True)]
        lignes.append([annee] + cases + [f"**{_n(ens.produit_milliers_dinars / 1000, 1)}**",
                                        _n(ens.lignes_du_recueil, 0)] + fin)
    tot = a.groupby("nature")[["produit_milliers_dinars", "lignes_du_recueil"]].sum()
    lignes.append(["**1998-2008**"] + [f"**{_n(tot.loc[c, 'produit_milliers_dinars'] / 1000, 1)}**"
                                       for c in NATURES]
                  + [f"**{_n(tot.loc['ensemble', 'produit_milliers_dinars'] / 1000, 1)}**",
                     f"**{_n(tot.loc['ensemble', 'lignes_du_recueil'], 0)}**", "", ""])
    _md(["Année"] + list(NATURES_COURTES.values())
        + ["Ensemble", "Lignes", "Relevé annuel<br>arrêté à 2009", "Écart"],
        "g" + "d" * (len(NATURES) + 4), lignes, caption, tbl_id)


def tableau_cessions_operations(caption: str, tbl_id: str = "tbl-ep-cessions-operations") -> None:
    """Les 162 lignes du recueil, par secteur : société, année, nature, libellé du mode, produit."""
    op = _s(S_RECUEIL)
    lignes = []
    for code, nom in SECTEURS_RECUEIL.items():
        d = op[op["secteur"] == code].sort_values("ordre")
        for r in d.itertuples(index=False):
            societe = "" if r.suite == "oui" else (
                f"{r.societe} ({r.sigle})" if str(r.sigle) not in ("", "nan") and r.sigle != r.societe
                else str(r.societe))
            lignes.append([nom if r.ordre == 1 else "", societe, str(r.annee_imprimee),
                           NATURES[r.nature], str(r.mode).replace("|", "/"),
                           _n(r.produit_milliers_dinars, 0)])
    _md(["Secteur", "Société", "Année", "Nature de l'acte", "Mode, tel qu'imprimé",
         "Produit (milliers de dinars)"], "gggggd", lignes, caption, tbl_id)


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
    c = _cdc_encours()
    if c is not None:
        xc, yc = _xy(c.index, c["total"], mesure)
        pts = ax.plot(xc, yc, color=NOIR, marker="D", ls="", ms=6, mfc="white", mew=1.2,
                      label="encours selon la Cour des comptes, rapport de clôture de la gestion")
        for a, v in zip(xc, yc):
            figtools.infobulle(pts[0], f"fin {a}, Cour des comptes : {_n(v, 1 if mesure == 'md' else 2)} "
                                       f"{'MD' if mesure == 'md' else '%'}")
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
    t = pd.DataFrame(
        [(l[0], l[1], _arrondi(l[2]), _arrondi(l[3]), l[4], l[5]) for l in _lignes_encours()],
        columns=["Fin d'année", "Encours garanti (MD courants)",
                 "Encours garanti (% des dépenses de l'État hors service de la dette)",
                 "Encours garanti (% du PIB, base 2015, calculé)", "dont extérieur (MD)",
                 "dont intérieur (MD)"])
    c = _cdc_encours()
    if c is not None:
        cour = {str(a): c.at[a, "total"] for a in c.index}
        t["Encours selon la Cour des comptes, rapport de clôture (MD courants)"] = [
            cour.get(x) for x in t["Fin d'année"]]
    return t


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
    fig, ax = plt.subplots(figsize=(9.6, 5.2))
    unite = "MD" if mesure == "md" else "%"
    dec = 1 if mesure == "md" else 2
    b = t[t[col].notna()]
    barres = ax.bar(b["annee"], b[col], color=BLEU, width=0.72)
    poignees = [Patch(color=BLEU,
                      label="produit des cessions, relevé de la Direction générale de la privatisation")]
    for barre, an, val in zip(barres, b["annee"], b[col]):
        figtools.infobulle(barre, f"{an} : {_n(val, dec)} {unite}")
    bud = _cessions_budget()
    colb = {"md": "budget", "dep": "dep", "pib": "pib"}[mesure]
    fin = 2009
    if len(bud):
        fin = int(bud["annee"].max())
        ax.axvline(2009.5, color=GRIS, lw=0.8, ls=":")
        nuls, sans = [], []
        for r in bud.itertuples(index=False):
            val = getattr(r, colb)
            if r.budget != r.budget:
                sans.append(int(r.annee))
                continue
            if val is None or val != val:
                continue
            if val <= 0:
                nuls.append(int(r.annee))
                continue
            bb = ax.bar(r.annee, val, color=VIOLET, width=0.72)
            figtools.infobulle(bb[0], f"{r.annee}, inscrit au budget : {_n(val, dec)} {unite}")
        poignees.append(Patch(color=VIOLET, label="recette de privatisation inscrite au budget, "
                                                  "rapport de clôture de la Cour des comptes"))
        for a in nuls:
            ax.annotate("0", xy=(a, 0), xycoords=("data", "axes fraction"), xytext=(0, 3),
                        textcoords="offset points", ha="center", va="bottom", fontsize=7,
                        color=VIOLET)
        if sans:
            ax.axvspan(min(sans) - 0.5, max(sans) + 0.5, color="#eaeef2", zorder=0)
            ax.annotate("aucune ligne de privatisation\ndans les recettes du budget",
                        xy=((min(sans) + max(sans)) / 2, 0.45), xycoords=("data", "axes fraction"),
                        ha="center", va="center", fontsize=7, color=GRIS, rotation=90)
    if mesure == "md":
        div = t[(t["classeur 1987-2005"].notna()) &
                ((t["classeur 1987-2005"] - t["classeur 1987-2009"]).abs() > 1)]
        ax.plot(div["annee"], div["classeur 1987-2005"], color=ROUGE, marker="D", ls="", ms=5,
                mfc="white")
        poignees.append(Line2D([], [], color=ROUGE, marker="D", ls="", ms=5, mfc="white",
                               label="valeur de l'édition 1987-2005, quand elle diffère"))
    ax.legend(handles=poignees, fontsize=7.5, frameon=False, loc="upper left")
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
    ax.set_xlim(1986.3, fin + 0.7)
    ax.set_xticks(list(range(1987, fin + 1, 2)))
    ax.tick_params(axis="x", labelsize=7.5)
    ax.set_ylim(top=ax.get_ylim()[1] * 2.5)
    if mesure == "pib":
        _marque_pib(ax, 1987, fin)
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


# --- clôture du budget, gestions 2010-2016 (Cour des comptes) ---------------------------------------

S_CDC = "cdc-cloture-entreprises-publiques"


def _gestions_cdc() -> list[int]:
    """Les gestions couvertes par la série de clôture : de la première gestion dont les
    versements au budget sont lus à la dernière gestion de la série (les recettes de
    privatisation portent des années antérieures, rappelées par les rapports)."""
    d = _s(S_CDC)
    g = d["gestion"].astype(int)
    debut = g[d["rubrique"] == "transferts_ep_profits_tresor"].min()
    return list(range(int(debut), int(g.max()) + 1))


LIGNES_RECETTES_CDC = [
    ("profits_bct", "Part du budget dans les profits de la Banque centrale", BLEU),
    ("excedents_ep", "Excédents des entreprises publiques", VERT),
    ("benefices_societes_non_petrolieres", "Bénéfices des sociétés non pétrolières", ORANGE),
    ("benefices_societes_petrolieres", "Bénéfices des sociétés pétrolières", ROUGE),
    ("autres_profits_tresor", "Autres profits du Trésor", GRIS)]
LIGNES_GARANTIE_CDC = [
    ("stb", "Société tunisienne de banque"),
    ("fouladh", "Société tunisienne de sidérurgie"),
    ("stir", "Société tunisienne des industries de raffinage"),
    ("pate_alfa", "Société nationale de cellulose et de papier alfa"),
    ("office_huile", "Office national de l'huile"),
    ("ateliers_sncft", "Société des travaux ferroviaires"),
    ("bna_agricole", "Banque nationale agricole, crédits agricoles"),
    ("office_cereales", "Office des céréales, emprunt obligataire"),
    ("art24_lf1999", "Article 24 de la loi de finances de 1999"),
    ("fpcl", "Caisse des prêts et de soutien des collectivités locales"),
    ("dette_agricole_loi65_1999", "Dette agricole, loi n° 99-65"),
    ("reprise_dettes_bancaires_art25_lf1999", "Reprise de dettes bancaires, article 25 de la loi de finances de 1999")]
COURT_GARANTIE_CDC = {
    "stb": "STB", "fouladh": "Sidérurgie", "stir": "STIR", "pate_alfa": "Papier alfa",
    "office_huile": "Huile", "ateliers_sncft": "Travaux ferroviaires", "bna_agricole": "BNA agricole",
    "office_cereales": "Office des céréales", "art24_lf1999": "Art. 24 LF 1999", "fpcl": "CPSCL",
    "dette_agricole_loi65_1999": "Dette agricole",
    "reprise_dettes_bancaires_art25_lf1999": "Art. 25 LF 1999"}


def _postes_garantie_cdc(p) -> list[str]:
    """Les postes du principal garanti présents dans la série : les postes connus dans l'ordre
    de `LIGNES_GARANTIE_CDC`, puis les autres par ordre alphabétique (un poste neuf de la série
    apparaît ainsi sans modification du module)."""
    connus = [k for k, _ in LIGNES_GARANTIE_CDC if k in p.columns]
    autres = sorted(c for c in p.columns if c not in connus and c != "total")
    return connus + autres


def _cdc(rubrique: str):
    """Une rubrique de la série : lignes `poste`, colonnes `gestion`, valeurs en MD. Une valeur
    reprise dans deux rapports est identique (contrôlé à la fabrication de la série)."""
    d = _s(S_CDC)
    d = d[d["rubrique"] == rubrique].drop_duplicates(["poste", "gestion"])
    return d.pivot(index="gestion", columns="poste", values="valeur_md")


def _cdc_encours():
    """L'encours de la dette garantie en fin de gestion tel que la Cour des comptes l'imprime
    dans ses rapports de clôture (depuis la gestion 2017) ; `None` si la série ne le porte pas."""
    d = _s(S_CDC)
    if "dette_garantie_encours" not in set(d["rubrique"]):
        return None
    t = _cdc("dette_garantie_encours")
    return t if "total" in t.columns else None


RUPTURE_CDC = 2020  # depuis la gestion 2020, la Cour n'imprime plus le total des versements


def _recettes_cdc():
    """Versements des entreprises et de la Banque centrale au budget, par ligne et par gestion.
    Jusqu'à 2019, la Cour imprime un total ; depuis 2020 elle n'imprime que des sous-totaux
    (dividendes ; excédents et Banque centrale) et des lignes de profits du Trésor : la colonne
    `total` reste vide, `somme_lignes` est la somme des lignes imprimées, calculée ici."""
    t = _cdc("transferts_ep_profits_tresor").reindex(_gestions_cdc())
    for c in ("excedents_ep_non_petrolieres", "excedents_ep_petrolieres", "autres_profits_tresor",
              "total_dividendes", "total_excedents_ep", "total"):
        if c not in t.columns:
            t[c] = float("nan")
    t["excedents_ep"] = t["excedents_ep_non_petrolieres"].fillna(0) + t["excedents_ep_petrolieres"].fillna(0)
    pt = [c for c in t.columns if c.startswith("profits_tresor_")]
    divers = t[pt].sum(axis=1, min_count=1) if pt else float("nan")
    t["autres_profits_tresor"] = t["autres_profits_tresor"].where(t["autres_profits_tresor"].notna(), divers)
    t["somme_lignes"] = t[[k for k, _, _ in LIGNES_RECETTES_CDC]].sum(axis=1, min_count=1)
    return t


def _garantie_cdc():
    p = _cdc("garantie_principal_paye").reindex(_gestions_cdc())
    i = _cdc("garantie_interets_payes").reindex(_gestions_cdc())["interets_dette_garantie"]
    p["interets"] = i
    return p


def _panneau_garantie_cdc(ax, mesure: str) -> None:
    """Principal et intérêts de la dette garantie payés par l'État, par gestion."""
    unite = "MD" if mesure == "md" else "%"
    dec = 1 if mesure == "md" else 2
    g = _garantie_cdc()
    for a in g.index:
        vp = _part(g.at[a, "total"], a, mesure)
        vi = _part(g.at[a, "interets"], a, mesure)
        if vp is not None:
            b = ax.bar(a, vp, color=BLEU, width=0.72)
            figtools.infobulle(b[0], f"{a} — principal : {_n(vp, dec)} {unite}")
        if vi is not None and vp is not None:
            b = ax.bar(a, vi, bottom=vp, color=ORANGE, width=0.72)
            figtools.infobulle(b[0], f"{a} — intérêts : {_n(vi, dec)} {unite}")
    ax.legend(handles=[Patch(color=BLEU, label="principal"), Patch(color=ORANGE, label="intérêts")],
              fontsize=7, frameon=False, loc="upper right")
    ax.set_title("Ce que l'État rembourse au titre de dettes garanties,\nprincipal et intérêts",
                 fontsize=8.5, loc="left")


def _panneau_prets_cdc(ax, mesure: str) -> None:
    """Remboursements de prêts reçus : total imprimé, puis prêts rétrocédés et prêts du titre II."""
    unite = "MD" if mesure == "md" else "%"
    dec = 1 if mesure == "md" else 2
    p = _prets_cdc()
    x, y = _xy(p.index, p["total"], mesure)
    ax.plot(x, y, color=VERT, marker="o", lw=2, ms=4.5, label="total imprimé (jusqu'en 2019)")
    for cle, nom, coul, marque in (("retroces_exterieurs", "prêts extérieurs rétrocédés", BLEU, "s"),
                                   ("titre2", "prêts du titre II", ORANGE, "^")):
        if cle in p.columns:
            xs, ys = _xy(p.index, p[cle], mesure)
            pts = ax.plot(xs, ys, color=coul, marker=marque, ls="", ms=4.5, mfc="white", label=nom)
            for a, v in zip(xs, ys):
                figtools.infobulle(pts[0], f"{a} — {nom} : {_n(v, dec)} {unite}")
    ax.legend(fontsize=6, frameon=False, loc="upper left")
    ax.set_title("Ce que l'État reçoit en remboursement de prêts :\ntotal, puis lignes",
                 fontsize=8.5, loc="left")


def _fig_cdc(mesure: str):
    figtools.apply_lang_font()
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.8))
    unite = "MD" if mesure == "md" else "%"
    dec = 1 if mesure == "md" else 2
    # 1. Ce que les entreprises versent au budget, par ligne
    ax = axes[0][0]
    r = _recettes_cdc()
    bas = [0.0] * len(r)
    for cle, nom, coul in LIGNES_RECETTES_CDC:
        for i, a in enumerate(r.index):
            v = _part(r.at[a, cle], a, mesure)
            if v is None or v == 0:
                continue
            b = ax.bar(a, v, bottom=bas[i], color=coul, width=0.72, edgecolor="white", lw=0.5)
            figtools.infobulle(b[0], f"{a} — {nom} : {_n(v, dec)} {unite}")
            bas[i] += v
    ax.legend(handles=[Patch(color=c, label=n) for _, n, c in LIGNES_RECETTES_CDC], fontsize=5.8,
              frameon=False, loc="upper left", ncol=2)
    ax.set_ylim(top=max(bas) * 1.42)
    if r.index.max() >= RUPTURE_CDC:
        ax.axvline(RUPTURE_CDC - 0.5, color=GRIS, lw=0.8, ls=":")
        ax.annotate("depuis 2020 :\nlignes imprimées,\nsans total", xy=(RUPTURE_CDC - 0.4, 0.70),
                    xycoords=("data", "axes fraction"), fontsize=6, color=GRIS, va="top")
    ax.set_title("Ce que les entreprises et la Banque centrale versent au budget,\npar ligne",
                 fontsize=8.5, loc="left")
    # 2. Dette garantie remboursée par l'État : principal et intérêts
    _panneau_garantie_cdc(axes[0][1], mesure)
    # 3. Remboursements de prêts reçus
    _panneau_prets_cdc(axes[1][0], mesure)
    # 4. Recettes de privatisation inscrites au budget
    ax = axes[1][1]
    v = _cdc("recettes_privatisation_budget").reindex(_gestions_cdc())["total"]
    for a in v.index:
        vv = _part(v[a], a, mesure)
        if vv is None:
            continue
        b = ax.bar(a, vv, color=VIOLET, width=0.72)
        figtools.infobulle(b[0], f"{a} — recettes de privatisation : {_n(vv, dec)} {unite}")
    sans = [int(a) for a in v.index if v[a] != v[a]]
    if sans:
        ax.axvspan(min(sans) - 0.5, max(sans) + 0.5, color="#eaeef2", zorder=0)
        ax.annotate("aucune ligne de privatisation\ndans les recettes du budget",
                    xy=((min(sans) + max(sans)) / 2, 0.5), xycoords=("data", "axes fraction"),
                    ha="center", va="center", fontsize=6.5, color=GRIS)
    ax.set_title("Recettes de privatisation inscrites au budget", fontsize=8.5, loc="left")
    gestions = _gestions_cdc()
    for ligne in axes:
        for ax in ligne:
            _style(ax)
            ax.set_xlim(gestions[0] - 0.6, gestions[-1] + 0.6)
            ax.set_xticks(gestions)
            ax.tick_params(labelsize=7 if len(gestions) > 9 else 7.5)
            ax.set_ylim(bottom=0, top=ax.get_ylim()[1])
            _axe(ax, mesure, milliards=False)
            ax.yaxis.label.set_size(7.5)
            if mesure == "pib":
                _marque_pib(ax, gestions[0], gestions[-1], dedans=True)
    fig.tight_layout()
    return fig


def _prets_cdc():
    """Remboursements de prêts reçus : total imprimé (jusqu'en 2019), prêts extérieurs rétrocédés
    et prêts du titre II (`prets_titre2_ep` jusqu'en 2019, `prets_budget_titre2` depuis 2020,
    réunis sous `titre2`)."""
    p = _cdc("remboursements_prets_recus").reindex(_gestions_cdc())
    for c in ("total", "retroces_exterieurs", "prets_titre2_ep", "prets_budget_titre2"):
        if c not in p.columns:
            p[c] = float("nan")
    p["titre2"] = p["prets_titre2_ep"].where(p["prets_titre2_ep"].notna(), p["prets_budget_titre2"])
    return p


def fig_cdc():
    return _trois_vues(_fig_cdc)


def table_cdc():
    r = _recettes_cdc()
    g = _garantie_cdc()
    p = _prets_cdc()
    v = _cdc("recettes_privatisation_budget").reindex(_gestions_cdc())
    c = _cdc_encours()
    enc = c["total"].reindex(_gestions_cdc()) if c is not None else [float("nan")] * len(_gestions_cdc())
    t = pd.DataFrame({
        "Année": _gestions_cdc(),
        "Versements au budget, total imprimé (MD courants)": list(r["total"]),
        "Versements au budget, somme des lignes imprimées (MD courants)": list(r["somme_lignes"]),
        "Dividendes, sous-total imprimé depuis 2019 (MD courants)": list(r["total_dividendes"]),
        "Excédents des entreprises et Banque centrale, sous-total imprimé depuis 2019 (MD courants)": list(r["total_excedents_ep"]),
        "Principal garanti remboursé (MD courants)": list(g["total"]),
        "Intérêts de la dette garantie (MD courants)": list(g["interets"]),
        "Remboursements de prêts reçus, total imprimé (MD courants)": list(p["total"]),
        "Prêts extérieurs rétrocédés remboursés (MD courants)": list(p["retroces_exterieurs"]),
        "Prêts du titre II remboursés (MD courants)": list(p["titre2"]),
        "Recettes de privatisation (MD courants)": list(v["total"]),
        "Encours de la dette garantie en fin de gestion, selon la Cour (MD courants)": list(enc)})
    for col in list(t.columns[1:]):
        nom = col.split(" (")[0]
        t[f"{nom}, % du PIB"] = [_arrondi(_part(x, a, "pib")) for x, a in zip(t[col], t["Année"])]
        t[f"{nom}, % des dépenses de l'État"] = [_arrondi(_part(x, a, "dep"))
                                                  for x, a in zip(t[col], t["Année"])]
    t["Base du PIB"] = [_base_courte(a) for a in t["Année"]]
    return t


def _panneau_encours_cdc(ax, mesure: str) -> None:
    """Encours de la dette garantie en fin de gestion selon la Cour des comptes : extérieur et
    intérieur empilés ; gestions sans encours imprimé laissées vides."""
    unite = "MD" if mesure == "md" else "%"
    dec = 1 if mesure == "md" else 2
    c = _cdc_encours()
    if c is None:
        return
    e = _cdc("dette_garantie_encours").reindex(_gestions_cdc())
    for a in e.index:
        bas = 0.0
        for cle, nom, coul in (("exterieur", "extérieur", BLEU), ("interieur", "intérieur", ORANGE)):
            v = _part(e.at[a, cle], a, mesure) if cle in e.columns else None
            if v is None:
                continue
            b = ax.bar(a, v, bottom=bas, color=coul, width=0.72)
            figtools.infobulle(b[0], f"{a} — encours {nom} : {_n(v, dec)} {unite}")
            bas += v
    vides = [a for a in e.index if not (e.loc[a, ["exterieur", "interieur"]] == e.loc[a, ["exterieur", "interieur"]]).any()]
    avant = [a for a in vides if a < 2017]
    if avant:
        ax.axvspan(min(avant) - 0.5, max(avant) + 0.5, color="#eaeef2", zorder=0)
        ax.annotate("encours non imprimé\npar la Cour", xy=((min(avant) + max(avant)) / 2, 0.5),
                    xycoords=("data", "axes fraction"), ha="center", va="center", fontsize=6.5,
                    color=GRIS)
    ax.legend(handles=[Patch(color=BLEU, label="dette extérieure"),
                       Patch(color=ORANGE, label="dette intérieure")],
              fontsize=6.5, frameon=False, loc="upper left")
    ax.set_title("Encours de la dette garantie en fin d'année,\nselon la Cour des comptes",
                 fontsize=8.5, loc="left")


def _fig_cdc_garanties(mesure: str):
    figtools.apply_lang_font()
    fig, axes = plt.subplots(1, 3, figsize=(10.4, 3.9))
    _panneau_garantie_cdc(axes[0], mesure)
    _panneau_prets_cdc(axes[1], mesure)
    figtools.marque_rupture(axes[1], RUPTURE_CDC, "nomenclature\nde 2020")
    _panneau_encours_cdc(axes[2], mesure)
    gestions = _gestions_cdc()
    for ax in axes:
        _style(ax)
        ax.set_xlim(gestions[0] - 0.6, gestions[-1] + 0.6)
        ax.set_xticks(gestions[::2])
        ax.tick_params(labelsize=7)
        ax.set_ylim(bottom=0, top=ax.get_ylim()[1] * 1.15)
        _axe(ax, mesure, milliards=False)
        ax.yaxis.label.set_size(7.5)
        if mesure == "pib":
            _marque_pib(ax, gestions[0], gestions[-1], dedans=True)
    fig.tight_layout()
    return fig


def fig_cdc_garanties():
    return _trois_vues(_fig_cdc_garanties)


def table_cdc_garanties():
    g = _garantie_cdc()
    p = _prets_cdc()
    e = _cdc("dette_garantie_encours").reindex(_gestions_cdc())
    for c in ("exterieur", "interieur"):
        if c not in e.columns:
            e[c] = float("nan")
    t = pd.DataFrame({
        "Année": _gestions_cdc(),
        "Principal garanti remboursé (MD courants)": list(g["total"]),
        "Intérêts de la dette garantie (MD courants)": list(g["interets"]),
        "Remboursements de prêts reçus, total imprimé (MD courants)": list(p["total"]),
        "Prêts extérieurs rétrocédés remboursés (MD courants)": list(p["retroces_exterieurs"]),
        "Prêts du titre II remboursés (MD courants)": list(p["titre2"]),
        "Encours garanti extérieur en fin d'année, selon la Cour (MD courants)": list(e["exterieur"]),
        "Encours garanti intérieur en fin d'année, selon la Cour (MD courants)": list(e["interieur"])})
    for col in list(t.columns[1:]):
        nom = col.split(" (")[0]
        t[f"{nom}, % du PIB"] = [_arrondi(_part(x, a, "pib")) for x, a in zip(t[col], t["Année"])]
        t[f"{nom}, % des dépenses de l'État"] = [_arrondi(_part(x, a, "dep"))
                                                  for x, a in zip(t[col], t["Année"])]
    t["Base du PIB"] = [_base_courte(a) for a in t["Année"]]
    return t


def _cdc_ligne_pib(valeur, annee, mesure="pib"):
    x = _part(valeur, annee, mesure)
    return "" if x is None else _n(x, 2)


def tableau_cdc_recettes(caption: str, tbl_id: str = "tbl-ep-cdc-recettes") -> None:
    r = _recettes_cdc()
    lignes = []
    for a in _gestions_cdc():
        c = [("—" if r.at[a, k] == 0 else _n(r.at[a, k], 1)) if r.at[a, k] == r.at[a, k] else ""
             for k, _, _ in LIGNES_RECETTES_CDC]
        tot = r.at[a, "total"]
        if tot == tot:
            cel_tot = f"**{_n(tot, 1)}**"
        else:
            tot = r.at[a, "somme_lignes"]
            cel_tot = f"({_n(tot, 1)})" if tot == tot else ""
        lignes.append([str(a)] + c + [cel_tot, _cdc_ligne_pib(tot, a), _base_courte(a)])
    _md(["Gestion"] + [n.replace(" du budget dans les", " dans les") for _, n, _ in LIGNES_RECETTES_CDC]
        + ["Total imprimé<br>(entre parenthèses : somme<br>des lignes, sans total imprimé)",
           "Total,<br>% du PIB", "Base du PIB"], "g" + "d" * 6 + "dg", lignes, caption, tbl_id)


def tableau_cdc_garantie(caption: str, tbl_id: str = "tbl-ep-cdc-garantie") -> None:
    p = _cdc("garantie_principal_paye").reindex(_gestions_cdc())
    i = _garantie_cdc()["interets"]
    postes = _postes_garantie_cdc(p)
    lignes = []
    for a in _gestions_cdc():
        cases = []
        for cle in postes:
            x = p.at[a, cle] if cle in p.columns else float("nan")
            if cle == "fouladh" and a == 2013:
                cases.append("(47,0)")
            elif x == x:
                cases.append(_n(x, 1))
            else:
                cases.append("")
        lignes.append([str(a)] + cases + [f"**{_n(p.at[a, 'total'], 1)}**", _n(i[a], 1),
                                          _cdc_ligne_pib(p.at[a, "total"], a)])
    entete = (["Gestion"] + [COURT_GARANTIE_CDC.get(k, k.replace("_", " ")) for k in postes]
              + ["Principal, total", "Intérêts", "Principal,<br>% du PIB"])
    _md(entete, "g" + "d" * (len(postes) + 3), lignes, caption, tbl_id)


def tableau_cdc_autres(caption: str, tbl_id: str = "tbl-ep-cdc-autres",
                       partie: str = "tout") -> None:
    """Remboursements de prêts et recettes de privatisation des rapports de clôture.

    `partie` : « prets » (trois colonnes de remboursements), « privatisation » (deux colonnes
    de recettes de privatisation) ou « tout » (les cinq)."""
    p = _prets_cdc()
    v = _cdc("recettes_privatisation_budget").reindex(_gestions_cdc())
    cols = {k: (p[k] if k in p.columns else pd.Series(dtype=float)) for k in
            ("total", "retroces_exterieurs", "titre2")}
    lignes = []
    for a in _gestions_cdc():
        def c(s, dec=1):
            x = s.get(a, float("nan")) if len(s) else float("nan")
            return _n(x, dec) if x == x else ""
        tt = v["tunisie_telecom"] if "tunisie_telecom" in v.columns else pd.Series(dtype=float)
        prets = [c(cols["total"], 3), c(cols["retroces_exterieurs"], 3), c(cols["titre2"], 3)]
        priv = [c(v["total"], 3), c(tt, 3)]
        lignes.append([str(a)] + (prets if partie != "privatisation" else [])
                      + (priv if partie != "prets" else []))
    entete_prets = ["Remboursements de prêts,<br>total imprimé<br>(jusqu'en 2019)",
                    "prêts extérieurs<br>rétrocédés", "prêts du titre II"]
    entete_priv = ["Recettes de privatisation,<br>total", "dont cession de 35 %<br>de Tunisie Télécom"]
    entete = (["Gestion"] + (entete_prets if partie != "privatisation" else [])
              + (entete_priv if partie != "prets" else []))
    _md(entete, "g" + "d" * (len(entete) - 1), lignes, caption, tbl_id)


# --- versements au budget depuis 2003 (Cour des comptes) et part de la Banque centrale -------------

S_CDC_0309 = "cdc-cloture-entreprises-publiques-2003-2009"
S_BCT_PART = "bct-part-etat-benefices"


def _recettes_depuis_2003():
    """Versements au budget par ligne et par gestion, de 2003 à la dernière gestion : gestions
    2003-2009 lues dans les rapports de clôture 2005 à 2009, gestions suivantes dans les rapports
    2011 et suivants (`_recettes_cdc`). Même recette, même tableau, mêmes lignes jusqu'à 2019 ; les
    deux séries ne se recouvrent pas (contrôlé ici)."""
    d = _s(S_CDC_0309).drop_duplicates(["poste", "gestion"])
    a = d.pivot(index="gestion", columns="poste", values="valeur_md")
    for c in ("excedents_ep_non_petrolieres", "excedents_ep_petrolieres", "autres_profits_tresor",
              "total"):
        if c not in a.columns:
            a[c] = float("nan")
    a["excedents_ep"] = a["excedents_ep_non_petrolieres"].fillna(0) + a["excedents_ep_petrolieres"].fillna(0)
    a["somme_lignes"] = a[[k for k, _, _ in LIGNES_RECETTES_CDC]].sum(axis=1, min_count=1)
    b = _recettes_cdc()
    if set(a.index) & set(b.index):
        raise ValueError("versements : les deux séries de clôture se recouvrent")
    cols = [k for k, _, _ in LIGNES_RECETTES_CDC] + ["total", "somme_lignes"]
    return pd.concat([a[cols], b[cols]]).sort_index()


def _hauteur(r, a):
    """Total imprimé, à défaut somme des lignes imprimées (gestions 2020 et suivantes)."""
    t = r.at[a, "total"]
    return t if t == t else r.at[a, "somme_lignes"]


def _fig_versements(mesure: str):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.6, 4.6))
    unite = "MD" if mesure == "md" else "%"
    dec = 1 if mesure == "md" else 2
    r = _recettes_depuis_2003()
    gestions = list(r.index)
    bas = {a: 0.0 for a in gestions}
    for cle, nom, coul in LIGNES_RECETTES_CDC:
        for a in gestions:
            v = _part(r.at[a, cle], a, mesure)
            if v is None or v == 0:
                continue
            b = ax.bar(a, v, bottom=bas[a], color=coul, width=0.72, edgecolor="white", lw=0.5)
            figtools.infobulle(b[0], f"{a} — {nom} : {_n(v, dec)} {unite}")
            bas[a] += v
    ax.legend(handles=[Patch(color=c, label=n) for _, n, c in LIGNES_RECETTES_CDC], fontsize=6.5,
              frameon=False, loc="upper left", ncol=2)
    ax.set_ylim(0, max(bas.values()) * 1.35)
    ax.axvline(RUPTURE_CDC - 0.5, color=GRIS, lw=0.8, ls=":")
    ax.annotate("depuis 2020 :\nsomme des lignes\nimprimées, sans total", xy=(RUPTURE_CDC - 0.4, 0.80),
                xycoords=("data", "axes fraction"), fontsize=6, color=GRIS, va="top")
    _style(ax)
    ax.set_xlim(gestions[0] - 0.6, gestions[-1] + 0.6)
    ax.set_xticks(gestions)
    ax.tick_params(axis="x", labelsize=7, rotation=90)
    _axe(ax, mesure, milliards=False)
    if mesure == "pib":
        _marque_pib(ax, gestions[0], gestions[-1])
    fig.tight_layout()
    return fig


def fig_versements():
    return _trois_vues(_fig_versements)


def table_versements():
    r = _recettes_depuis_2003()
    t = pd.DataFrame({"Gestion": list(r.index)})
    for cle, nom, _ in LIGNES_RECETTES_CDC:
        t[f"{nom} (MD courants)"] = [_arrondi(x, 6) if x == x else None for x in r[cle]]
    t["Total imprimé (MD courants)"] = [x if x == x else None for x in r["total"]]
    t["Somme des lignes imprimées (MD courants)"] = list(r["somme_lignes"])
    haut = [_hauteur(r, a) for a in r.index]
    t["% des dépenses de l'État hors service de la dette"] = [
        _arrondi(_part(x, a, "dep")) for x, a in zip(haut, r.index)]
    t["% du PIB"] = [_arrondi(_part(x, a, "pib")) for x, a in zip(haut, r.index)]
    t["Base du PIB"] = [_base_courte(a) for a in r.index]
    t["Rapports de la Cour des comptes"] = ["gestions 2005 à 2009" if a < 2010 else "gestions 2011 à 2024"
                                            for a in r.index]
    return t


def tableau_versements_anciens(caption: str, tbl_id: str = "tbl-ep-versements-anciens") -> None:
    """Gestions 2003-2009, ligne par ligne, total imprimé, part du PIB et base."""
    r = _recettes_depuis_2003()
    lignes = []
    for a in [g for g in r.index if g < 2010]:
        c = [("—" if r.at[a, k] == 0 else _n(r.at[a, k], 1)) if r.at[a, k] == r.at[a, k] else ""
             for k, _, _ in LIGNES_RECETTES_CDC]
        tot = r.at[a, "total"]
        lignes.append([str(a)] + c + [f"**{_n(tot, 1)}**", _cdc_ligne_pib(tot, a),
                                      _cdc_ligne_pib(tot, a, "dep"), _base_courte(a)])
    _md(["Gestion"] + [n.replace(" du budget dans les", " dans les") for _, n, _ in LIGNES_RECETTES_CDC]
        + ["Total imprimé", "Total,<br>% du PIB", "Total, % des<br>dépenses de l'État", "Base du PIB"],
        "g" + "d" * 8 + "g", lignes, caption, tbl_id)


def tableau_bct_parts(caption: str, tbl_id: str = "tbl-ep-bct-parts") -> None:
    """Part de l'État dans le résultat de la Banque centrale, par exercice, à côté de la ligne que le
    budget de l'année suivante inscrit (Cour des comptes). Exercices 1999-2001 : seul le partage
    entre le budget et le Fonds de péréquation des changes est imprimé."""
    b = _s(S_BCT_PART)
    r = _recettes_depuis_2003()
    lignes = []
    for ex in sorted(set(b["exercice"].astype(int))):
        e = b[b["exercice"] == ex].set_index("poste")

        def v(poste, dec=1):
            return _n(e.at[poste, "valeur_md"], dec) if poste in e.index else ""

        def an(poste):
            a = e.at[poste, "annee_versement"]
            return "" if a != a or str(a) == "" else f"{int(a)} : "

        verse = []
        if "part_etat_versee" in e.index:
            verse.append(f"{an('part_etat_versee')}{_n(e.at['part_etat_versee', 'valeur_md'], 0)}")
        if "part_budget_etat" in e.index:
            verse.append(f"{an('part_budget_etat')}"
                         f"{_n(e.at['part_budget_etat', 'valeur_md'], 1)} au budget, "
                         f"{_n(e.at['fonds_perequation_changes', 'valeur_md'], 1)} au Fonds de "
                         "péréquation des changes")
        if "reliquat_compte_ordre" in e.index:
            verse.append(f"reliquat en compte d'ordre fin {int(e.at['reliquat_compte_ordre', 'annee_versement'])} : "
                         f"{_n(e.at['reliquat_compte_ordre', 'valeur_md'], 1)}")
        suiv = ex + 1
        budget = (("—" if r.at[suiv, "profits_bct"] == 0 else _n(r.at[suiv, "profits_bct"], 2))
                  if suiv in r.index and r.at[suiv, "profits_bct"] == r.at[suiv, "profits_bct"] else "")
        lignes.append([str(ex), v("resultat_exercice"), v("part_etat", 2), " ; ".join(verse),
                       str(suiv), budget])
    _md(["Exercice", "Résultat de l'exercice<br>(Banque centrale)",
         "Part revenant à l'État<br>(Banque centrale)", "Versement cité<br>(année : MD)",
         "Gestion suivante", "Part du budget dans les profits<br>de la Banque centrale, gestion suivante<br>(Cour des comptes)"],
        "gddggd", lignes, caption, tbl_id)


# --- revenus des participations dans les rapports de la Banque centrale, 1983-2016 -----------------

S_BCT_RA = "bct-ra-revenus-participations"
# Deux périmètres, jamais raccordés : (première année, dernière année, libellé, couleur). Le
# passage de « revenus des participations et des EPIC » (rapports 1995-2000) à « revenus des
# participations » (rapports 2001-2016) ne change aucune valeur : 1999 et 2000 lus dans les rapports
# 2000 et 2001 donnent 167,0 / 167,1 et 273,8 / 273,8.
SEGMENTS_RA = [
    (1983, 1988, "recettes des participations financières, revenus pétroliers compris", VIOLET),
    (1993, 2016, "revenus des participations (et des EPIC, rapports 1995-2000), "
                 "revenus pétroliers à part", BLEU),
]


def _lectures_ra(poste: str):
    """Lectures d'un poste, une par (rapport, année). La valeur retenue pour une année est celle du
    rapport le plus récent ; le rapport 1999, arrondi au million, ne l'emporte pas sur une
    lecture au dixième."""
    d = _s(S_BCT_RA)
    d = d[d.poste == poste].copy()
    autres = set(d[d.rapport != "ra-1999"].annee)
    d = d[(d.rapport != "ra-1999") | ~d.annee.isin(autres)].sort_values(["annee", "annee_rapport"])
    return d


def _retenue_ra(poste: str):
    d = _lectures_ra(poste)
    return d.groupby("annee").last()


def _segment_ra(annee: int) -> int:
    for i, (a0, a1, _, _) in enumerate(SEGMENTS_RA):
        if a0 <= annee <= a1:
            return i
    raise ValueError(f"revenus des participations : année {annee} hors des segments")


def _fig_bct_ra(mesure: str):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.6, 4.6))
    unite = "MD" if mesure == "md" else "%"
    dec = 1 if mesure == "md" else 2
    rev = _retenue_ra("revenus_participations")
    ver = _retenue_ra("versement_bct")
    for a0, a1, nom, coul in SEGMENTS_RA:
        blocs, courant = [], []
        for a in range(a0, a1 + 1):
            v = _part(rev.at[a, "valeur_md"], a, mesure) if a in rev.index else None
            if v is None:
                if courant:
                    blocs.append(courant)
                courant = []
                continue
            courant.append((a, v))
        if courant:
            blocs.append(courant)
        for bloc in blocs:
            xs, ys = [a for a, _ in bloc], [v for _, v in bloc]
            ax.plot(xs, ys, color=coul, lw=1.6)
            for x, y in bloc:
                pt = ax.plot([x], [y], "o", color=coul, ms=3.5)[0]
                figtools.infobulle(pt, f"{x} — {nom} : {_n(y, dec)} {unite}")
    for a in ver.index:
        v = _part(ver.at[a, "valeur_md"], a, mesure)
        if v is None:
            continue
        b = ax.bar(a, v, color=GRIS, alpha=0.45, width=0.7)
        figtools.infobulle(b[0], f"{a} — versement de la Banque centrale au budget : {_n(v, dec)} {unite}")
    for a0, _, _, _ in SEGMENTS_RA[1:]:
        figtools.marque_rupture(ax, a0 - 0.5)
    poignees = [Line2D([0], [0], color=c, lw=1.6, marker="o", ms=3.5, label=n)
                for _, _, n, c in SEGMENTS_RA]
    poignees.append(Patch(color=GRIS, alpha=0.45, label="dont versement de la Banque centrale"))
    ax.legend(handles=poignees, fontsize=6.5, frameon=False, loc="upper left")
    _style(ax)
    ax.set_xlim(1982.4, 2016.6)
    ax.set_ylim(0, None)
    ax.set_ylim(0, ax.get_ylim()[1] * 1.3)
    _axe(ax, mesure, milliards=False)
    if mesure == "pib":
        # 1983-1985 : PIB de la Banque mondiale, bases accolées ; libellé court, pour ne pas
        # chevaucher le segment suivant.
        _marque_pib(ax, 1986, 2016)
        figtools.marque_rupture(ax, 1986)
        ax.annotate("Banque mondiale,\nbases accolées", xy=(1984, 1), xycoords=("data", "axes fraction"),
                    xytext=(0, 5), textcoords="offset points", ha="center", va="bottom",
                    fontsize=6.5, color=GRIS, annotation_clip=False)
    fig.tight_layout()
    return fig


def fig_bct_ra():
    return _trois_vues(_fig_bct_ra)


def table_bct_ra():
    rev = _retenue_ra("revenus_participations")
    ver = _retenue_ra("versement_bct")
    annees = sorted(set(rev.index) | set(ver.index))
    t = pd.DataFrame({"Année budgétaire": annees})
    t["Libellé du rapport"] = [rev.at[a, "libelle_imprime"] if a in rev.index else "" for a in annees]
    t["Nomenclature"] = [SEGMENTS_RA[_segment_ra(a)][2] for a in annees]
    t["Revenus des participations (MD courants)"] = [
        rev.at[a, "valeur_md"] if a in rev.index else None for a in annees]
    t["Rapport retenu"] = [rev.at[a, "rapport"].replace("ra-", "BCT ") if a in rev.index else ""
                           for a in annees]
    t["Versement de la Banque centrale (MD courants)"] = [
        ver.at[a, "valeur_md"] if a in ver.index else None for a in annees]
    t = _ajoute_parts(t, "Année budgétaire", "Revenus des participations (MD courants)",
                      "revenus des participations")
    t["Base du PIB"] = [_base_courte(a) for a in annees]
    return t


def tableau_bct_ra(caption: str, tbl_id: str = "tbl-ep-bct-ra") -> None:
    """Toutes les lectures, année par année : valeur retenue, autres lectures, versement de la
    Banque centrale, et pour 2003-2016 le total de la Cour moins les autres profits du Trésor."""
    lec = _lectures_ra("revenus_participations")
    tout = _s(S_BCT_RA)
    rev = tout[tout.poste == "revenus_participations"]
    ver = tout[tout.poste == "versement_bct"]
    r = _recettes_depuis_2003()
    lignes = []
    for a in sorted(set(rev.annee) | set(ver.annee)):
        g = rev[rev.annee == a].sort_values("annee_rapport")
        ret = lec[lec.annee == a].sort_values("annee_rapport")
        val = ret.iloc[-1] if len(ret) else None
        autres = [f"{_n(x.valeur_md, 1 if x.rapport != 'ra-1999' else 0)} ({x.annee_rapport})"
                  for x in g.itertuples() if val is None or x.rapport != val.rapport]
        gv = ver[ver.annee == a].sort_values("annee_rapport")
        vers = " ; ".join(f"{_n(x.valeur_md, 1 if x.valeur_md % 1 else 0)} ({x.annee_rapport})"
                          for x in gv.itertuples())
        cour = ""
        if a in r.index and a <= 2016:
            t = r.at[a, "total"] - r.at[a, "autres_profits_tresor"]
            cour = _n(t, 1)
        lignes.append([str(a),
                       val.libelle_imprime.replace("*", "\\*").replace("&", " & ") if val is not None else "",
                       f"**{_n(val.valeur_md, 1)}** ({val.annee_rapport})" if val is not None else "",
                       ", ".join(autres), vers, cour])
    _md(["Année", "Libellé imprimé", "Valeur retenue<br>(rapport)", "Autres lectures<br>(rapport)",
         "Versement de la<br>Banque centrale (rapport)",
         "Cour des comptes : total<br>moins autres profits du Trésor"],
        "gggggd", lignes, caption, tbl_id)


# --- point d'entrée ------------------------------------------------------------------------------------

# --- Cour de discipline financière, 1986-2009 ---------------------------------------------------

S_CDF = "cdf-activite"
# Les trois définitions des affaires en cours de fin d'année, telles que les rapports les donnent :
# (première année, dernière année, libellé court, couleur). Les segments ne se chaînent pas.
SEGMENTS_CDF = [
    (1990, 2000, "1990-2000 : charge totale, affaires tranchées dans l'année comprises", BLEU),
    (2001, 2004, "2001-2004 : affaires en instruction", VERT),
    (2005, 2009, "2005-2009 : affaires en instruction et affaires instruites", VIOLET),
]


def _cdf() -> pd.DataFrame:
    return _s(S_CDF).astype({"periode": str})


def _cdf_annuel(d: pd.DataFrame, grandeur: str) -> dict[int, int]:
    b = d[(d["grandeur"] == grandeur) & (d["annee_debut"] == d["annee_fin"])]
    return {int(a): int(v) for a, v in zip(b["annee_debut"], b["valeur"])}


def _cdf_bloc(d: pd.DataFrame, grandeur: str) -> int | None:
    b = d[(d["grandeur"] == grandeur) & (d["periode"] == "1986-1989")]
    return None if b.empty else int(b["valeur"].iloc[0])


def fig_cdf():
    figtools.apply_lang_font()
    d = _cdf()
    fig, axes = plt.subplots(3, 1, figsize=(9.6, 9.0), sharex=True)
    annees = range(1986, 2010)

    # 1. Saisines et affaires tranchées
    ax = axes[0]
    sai = _cdf_annuel(d, "saisines")
    tra = _cdf_annuel(d, "affaires_tranchees")
    for a, v in sai.items():
        b = ax.bar(a, v, color=BLEU, alpha=0.55, width=0.7)
        figtools.infobulle(b[0], f"{a} : {v} saisines")
    for a in (1986, 1992):
        ax.annotate("n. d.", xy=(a, 0), xytext=(0, 2), textcoords="offset points",
                    ha="center", va="bottom", fontsize=6.5, color=GRIS)
    for a0, a1 in ((1990, 2001), (2002, 2009)):
        xs = [a for a in range(a0, a1 + 1) if a in tra]
        ax.plot(xs, [tra[a] for a in xs], color=ORANGE, lw=1.6)
        for a in xs:
            pt = ax.plot([a], [tra[a]], "o", color=ORANGE, ms=3.5)[0]
            figtools.infobulle(pt, f"{a} : {tra[a]} affaires tranchées")
    bloc = _cdf_bloc(d, "affaires_tranchees")
    ax.plot([1985.65, 1989.35], [bloc, bloc], color=ORANGE, lw=1.2, ls=(0, (3, 2)))
    ax.annotate(f"1986-1989 : {bloc} au total", xy=(1987.5, bloc), xytext=(0, 3),
                textcoords="offset points", ha="center", va="bottom", fontsize=6.5, color=ORANGE)
    figtools.marque_rupture(ax, 2002, "classements de l'art. 15 bis\nplus comptés")
    ax.set_title("Saisines et affaires tranchées", fontsize=9, loc="left")
    ax.legend(handles=[Patch(color=BLEU, alpha=0.55, label="saisines de l'année"),
                       Line2D([0], [0], color=ORANGE, lw=1.6, marker="o", ms=3.5,
                              label="affaires tranchées (arrêts et classements)")],
              fontsize=7, frameon=False, loc="upper left", bbox_to_anchor=(0.16, 1))

    # 2. Condamnations à l'amende
    ax = axes[1]
    am = _cdf_annuel(d, "condamnations_amende")
    ep_ = _cdf_annuel(d, "condamnations_amende_entreprise_publique")
    for a, v in am.items():
        b = ax.bar(a, v, color=ROUGE, alpha=0.3, width=0.7)
        txt = f"{a} : {v} condamnations à l'amende"
        if a in ep_:
            txt += f", dont {ep_[a]} sur une entreprise publique"
        figtools.infobulle(b[0], txt)
    for a, v in ep_.items():
        if v:
            ax.bar(a, v, color=ROUGE, width=0.7)
    bloc, bloc_ep = _cdf_bloc(d, "condamnations_amende"), _cdf_bloc(
        d, "condamnations_amende_entreprise_publique")
    ax.annotate(f"1986-1989 : {bloc} au total,\ndont {bloc_ep} sur une entreprise publique",
                xy=(1987.5, 0), xytext=(0, 3), textcoords="offset points", ha="center",
                va="bottom", fontsize=6.5, color=ROUGE)
    ax.axvspan(1998.5, 2009.5, color=GRIS, alpha=0.07, lw=0)
    ax.annotate("entreprises publiques non comptées", xy=(2004, 1), xycoords=("data", "axes fraction"),
                xytext=(0, -4), textcoords="offset points", ha="center", va="top",
                fontsize=6.5, color=GRIS)
    ax.set_title("Condamnations à l'amende", fontsize=9, loc="left")
    ax.legend(handles=[Patch(color=ROUGE, alpha=0.3, label="condamnations à l'amende"),
                       Patch(color=ROUGE, label="dont sur une entreprise publique (1986-1998)")],
              fontsize=7, frameon=False, loc="upper left", bbox_to_anchor=(0.12, 1))

    # 3. Affaires en cours en fin d'année, trois définitions
    ax = axes[2]
    enc = _cdf_annuel(d, "affaires_en_cours_fin_annee")
    for a0, a1, nom, coul in SEGMENTS_CDF:
        xs = [a for a in range(a0, a1 + 1) if a in enc]
        ax.plot(xs, [enc[a] for a in xs], color=coul, lw=1.6, label=nom)
        for a in xs:
            pt = ax.plot([a], [enc[a]], "o", color=coul, ms=3.5)[0]
            figtools.infobulle(pt, f"{a} : {enc[a]} affaires en cours — {nom}")
    for a0, _, _, _ in SEGMENTS_CDF[1:]:
        figtools.marque_rupture(ax, a0, "changement\nde définition")
    ax.set_title("Affaires en cours en fin d'année, selon la définition du rapport",
                 fontsize=9, loc="left")
    ax.legend(fontsize=7, frameon=False, loc="lower left")

    for ax in axes:
        _style(ax)
        ax.set_ylim(0, ax.get_ylim()[1] * 1.15)
        ax.set_ylabel("affaires", fontsize=8)
        ax.tick_params(labelsize=7)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    axes[-1].set_xlim(1985.4, 2009.6)
    axes[-1].set_xticks(range(1986, 2010, 2))
    fig.tight_layout()
    return fig


def table_cdf():
    d = _cdf()
    noms = {"saisines": "Saisines", "affaires_tranchees": "Affaires tranchées",
            "condamnations_amende": "Condamnations à l'amende",
            "condamnations_amende_entreprise_publique": "dont sur une entreprise publique",
            "affaires_en_cours_fin_annee": "Affaires en cours en fin d'année"}
    t = d[d["grandeur"].isin(noms)].pivot_table(index="periode", columns="grandeur",
                                                 values="valeur", aggfunc="first")
    t = t.reindex(columns=list(noms)).rename(columns=noms)
    defs = d[d["grandeur"] == "affaires_en_cours_fin_annee"].set_index("periode")["definition"]
    loc = d.groupby("periode")["localisateur"].first()
    cle = d.groupby("periode")["cle"].first()
    t["Définition des affaires en cours"] = defs
    t["Rapport"] = [f"{cle[p]}, {loc[p]}" for p in t.index]
    t = t.reset_index().rename(columns={"periode": "Période"})
    t["_o"] = [int(str(p)[:4]) * 10 + (0 if "-" in str(p) else 1) for p in t["Période"]]
    return t.sort_values("_o").drop(columns="_o")


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
    "cessions": (fig_cessions, table_cessions, (S_CESSIONS, S_CDC, DENOMINATEURS), "fig_ep_cessions"),
    "cdc": (fig_cdc, table_cdc, (S_CDC, DENOMINATEURS), "fig_ep_cdc"),
    "cdc_garanties": (fig_cdc_garanties, table_cdc_garanties, (S_CDC, DENOMINATEURS),
                      "fig_ep_cdc_garanties"),
    "versements": (fig_versements, table_versements, (S_CDC_0309, S_CDC, DENOMINATEURS),
                   "fig_ep_versements"),
    "bct_ra": (fig_bct_ra, table_bct_ra, (S_BCT_RA, DENOMINATEURS), "fig_ep_bct_ra"),
    "croisees": (fig_croisees, table_croisees, (S_CROISEES, DENOMINATEURS), "fig_ep_croisees"),
    "masse": (fig_masse, table_masse, (S_EFFECTIFS, S_AGREGATS, DENOMINATEURS), "fig_ep_masse"),
    "effectifs": (fig_effectifs, table_effectifs_ep, (S_EFFECTIFS_EP,), "fig_ep_effectifs"),
    "cdf": (fig_cdf, table_cdf, (S_CDF,), "fig_ep_cdf"),
}


def figure(nom: str, caption: str, note_lecture: str | None = None,
           nominal: bool = True) -> None:
    """Trace la figure `nom` en onglets (chunk `output: asis`, étiqueté `fig-…`).

    `nominal=False` pour une figure qui ne compte pas des dinars (des affaires, des agents) :
    la ligne « Source » ne dit alors pas « valeurs courantes »."""
    trace, table, series, slug = FIGURES[nom]
    figtools.figure_tabs(trace(), table(), *series, slug=slug, caption=caption,
                         note_lecture=note_lecture, nominal=nominal)
    plt.close("all")

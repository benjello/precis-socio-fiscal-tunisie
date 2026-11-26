"""Figures et tableaux de la page du site « Séries longues des finances publiques et des
paiements extérieurs » (`precis/fr/series-longues.qmd`).

    from figures import series_longues as sl
    sl.fig_reglement(), sl.table_reglement(), sl.md_reglement()   # lois de règlement
    sl.vues_recettes(), sl.table_recettes(), sl.md_recettes()     # recettes ordinaires (BCT)
    sl.fig_bdp(), sl.table_bdp(), sl.md_bdp(), sl.md_mbp5()       # balance des paiements (BCT)

D'OÙ VIENNENT LES DONNÉES. Trois séries de `tunisia-data`, lues par `figtools.series()` :

  - `jort-lois-reglement-1954-1985` : exécution du budget de l'État arrêtée par les lois de
    règlement, montants imprimés en dinars ;
  - `bct-ra-recettes-ordinaires` (et ses contrôles) : recettes ordinaires de l'État par
    catégorie, tableau du rapport annuel de la BCT, éditions 1961-1984 ;
  - `bct-ra-bdp-1978-1996` (contrôles, raccord) : principaux soldes de la balance des
    paiements, rapports annuels de la BCT, présentation antérieure au MBP5.

RÈGLES.

  - **Rien ne se chaîne** : ni les présentations successives d'une même série (tracées en
    segments distincts), ni les séries entre elles, ni avec les comptes de la nation.
  - **Une valeur retenue par poste et par année** (édition la plus récente) ; les postes d'une
    même année peuvent venir d'éditions différentes : aucune somme entre postes retenus, aucun
    empilement.
  - **Les ruptures se lisent dans les données** (édition où un poste apparaît ou disparaît,
    valeur d'un même exercice dans deux éditions) : aucun nombre n'est écrit en dur ici.

La catégorie « sources » du catalogue de la série des lois de règlement est vide : les clés
`reglement-<gestion>` du précis sont rattachées ici à la provenance de l'entrepôt, loi par loi,
d'après la colonne `loi` de la série (voir `CLES_REGLEMENT`).
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
sys.path.insert(0, "../../scripts")
import figtools  # noqa: E402

S_REGL = "jort-lois-reglement-1954-1985"
S_REC = "bct-ra-recettes-ordinaires"
S_REC_CTL = "bct-ra-recettes-ordinaires-controles"
S_BDP = "bct-ra-bdp-1978-1996"
S_BDP_CTL = "bct-ra-bdp-1978-1996-controles"
S_BDP_RAC = "bct-ra-bdp-1978-1996-raccord"

GRIS = "#57606a"


# --- formats -----------------------------------------------------------------
def nb(v: float, nd: int = 1) -> str:
    """Nombre à la française, espace insécable des milliers, signe moins typographique."""
    return f"{v:,.{nd}f}".replace(",", "&nbsp;").replace(".", ",").replace("-", "−")


def _cell(v, nd: int = 1) -> str:
    return "" if pd.isna(v) else nb(float(v), nd)


# =============================================================================
# 1. Lois de règlement
# =============================================================================
# Clé du précis pour chaque loi de la série (references.json, `reglement-<gestion>`).
CLES_REGLEMENT = {
    "66-2": "reglement-1954-55", "66-3": "reglement-1955-56", "66-4": "reglement-1956-57",
    "66-5": "reglement-1957-58", "66-6": "reglement-1958-59", "66-7": "reglement-1959-60",
    "66-8": "reglement-1960", "66-9": "reglement-1961", "66-10": "reglement-1962",
    "66-11": "reglement-1963", "66-14": "reglement-1964", "83-88": "reglement-1962-64",
    "83-89": "reglement-1965", "83-90": "reglement-1966", "83-91": "reglement-1967",
    "83-92": "reglement-1968", "83-93": "reglement-1969", "83-94": "reglement-1970",
    "84-31": "reglement-1971", "84-32": "reglement-1972", "84-33": "reglement-1973",
    "84-34": "reglement-1974", "84-35": "reglement-1975", "86-48": "reglement-1976",
    "86-49": "reglement-1977", "86-50": "reglement-1978", "86-51": "reglement-1979",
    "86-68": "reglement-1980", "87-13": "reglement-1981", "88-28": "reglement-1982",
    "88-29": "reglement-1983", "88-138": "reglement-1984", "90-27": "reglement-1985",
}


def _declarer_reglement() -> None:
    m = dict(figtools.meta(S_REGL))
    lois = list(dict.fromkeys(figtools.series(S_REGL)["loi"]))
    manquantes = [l for l in lois if l not in CLES_REGLEMENT]
    if manquantes:
        raise KeyError(f"lois de règlement sans clé : {manquantes}")
    m["sources"] = [CLES_REGLEMENT[l] for l in lois]
    m.pop("id", None)
    figtools.register_provenance(S_REGL, **m)


_declarer_reglement()

# bloc principal de chaque présentation (budget de l'État)
_BLOC_PRINCIPAL = {"BU": "budget unique", "BG": "budget général", "T1": "titre I"}


def reglement() -> pd.DataFrame:
    return figtools.series(S_REGL)


def _etat(d: pd.DataFrame) -> pd.DataFrame:
    return d[d.entite == "etat"]


def gestions_annuelles() -> list[str]:
    """Gestions dans l'ordre de la série, hors agrégat pluriannuel du titre II."""
    d = reglement()
    g = d[d.bloc.isin(list(_BLOC_PRINCIPAL))][["gestion"]].drop_duplicates()
    return g.gestion.tolist()


def table_reglement() -> pd.DataFrame:
    """Une ligne par gestion : recouvrements et paiements du budget de l'État (bloc principal),
    paiements du titre II (sections I et II) ; millions de dinars et texte imprimé."""
    d = _etat(reglement())
    lignes = []
    for g in gestions_annuelles():
        x = d[d.gestion == g]
        princ = x[x.bloc.isin(list(_BLOC_PRINCIPAL))]
        bloc = princ.bloc.iloc[0]

        def v(bl, poste, col="valeur_md"):
            s = x[(x.bloc == bl) & (x.poste == poste)][col]
            return s.iloc[0] if len(s) else None

        lignes.append({
            "gestion": g, "duree": x.duree.iloc[0], "presentation": x.presentation.iloc[0],
            "loi": x.loi.iloc[0], "jort": princ.jort.iloc[0], "bloc": _BLOC_PRINCIPAL[bloc],
            "recouvrements_md": v(bloc, "recouvrements"), "paiements_md": v(bloc, "paiements"),
            "recouvrements_imprime": v(bloc, "recouvrements", "texte_lu"),
            "paiements_imprime": v(bloc, "paiements", "texte_lu"),
            "t2s1_paiements_md": v("T2S1", "paiements"), "t2s2_paiements_md": v("T2S2", "paiements"),
            "t2s1_paiements_imprime": v("T2S1", "paiements", "texte_lu"),
            "t2s2_paiements_imprime": v("T2S2", "paiements", "texte_lu"),
        })
    t = pd.DataFrame(lignes)
    t["t2_paiements_md"] = t.t2s1_paiements_md + t.t2s2_paiements_md
    return t


def triennie() -> pd.DataFrame:
    """Le titre II des gestions de la triennie, réglé en un seul agrégat."""
    d = _etat(reglement())
    return d[d.duree == "triennie"]


def presentations() -> list[tuple[str, str, str]]:
    """(présentation, première gestion, dernière gestion), dans l'ordre."""
    t = table_reglement()
    out = []
    for p, g in t.groupby("presentation", sort=False):
        out.append((p, g.gestion.iloc[0], g.gestion.iloc[-1]))
    return out


def premiere_gestion_t2() -> str:
    t = table_reglement()
    return t[t.t2_paiements_md.notna()].gestion.iloc[0]


def fig_reglement():
    t = table_reglement()
    x = range(len(t))
    t = t.assign(x=list(x))
    fig, ax = plt.subplots(figsize=(9, 4.6))
    styles = {"BU": "o", "BG": "s", "T1": "D"}
    noms = {"BU": "budget unique d'exercice", "BG": "budget général",
            "T1": "titre I (budget ordinaire)"}
    for bloc_lib, g in t.groupby("bloc", sort=False):
        cle = [k for k, v in _BLOC_PRINCIPAL.items() if v == bloc_lib][0]
        ax.plot(g.x, g.recouvrements_md, color="#1f4e79", marker=styles[cle], ms=3.5, lw=1.6,
                label=f"recouvrements, {noms[cle]}")
        ax.plot(g.x, g.paiements_md, color="#c0392b", marker=styles[cle], ms=3.5, lw=1.6,
                ls="--", label=f"paiements, {noms[cle]}")
    t2 = t[t.t2_paiements_md.notna()]
    ax.plot(t2.x, t2.t2_paiements_md, color="#1a9850", marker="^", ms=3.5, lw=1.6,
            label="paiements, titre II (sections I et II)")
    # ruptures de présentation, entre deux gestions
    for p in t.presentation.drop_duplicates().iloc[1:]:
        i = int(t[t.presentation == p].x.iloc[0])
        ax.axvline(i - 0.5, color=GRIS, ls=(0, (2, 2)), lw=1, zorder=1)
    neuf = t[t.duree.str.contains("9 mois")]
    for _, r in neuf.iterrows():
        ax.annotate("9 mois", xy=(r.x, r.recouvrements_md), xytext=(0, 8),
                    textcoords="offset points", ha="center", fontsize=7, color=GRIS)
    ax.set_xticks(list(t.x))
    ax.set_xticklabels(t.gestion, rotation=90, fontsize=7)
    ax.set_ylabel("millions de dinars courants")
    ax.grid(axis="y", alpha=0.3)
    ax.legend(fontsize=7, loc="upper left", frameon=False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    return fig


def md_reglement() -> str:
    t = table_reglement()
    lignes = ["| Gestion | Présentation | Loi (JORT) | Recouvrements | Paiements | "
              "Titre II, section I : paiements | Titre II, section II : paiements |",
              "|---|---|---|--:|--:|--:|--:|"]
    for _, r in t.iterrows():
        g = r.gestion + (f" ({r.duree})" if "mois" in r.duree else "")
        lignes.append(
            f"| {g} | {r.bloc} | n° {r.loi} ({r.jort}) | {r.recouvrements_imprime} | "
            f"{r.paiements_imprime} | {r.t2s1_paiements_imprime or ''} | "
            f"{r.t2s2_paiements_imprime or ''} |")
    return "\n".join(lignes)


# =============================================================================
# 2. Recettes ordinaires (rapports annuels de la BCT)
# =============================================================================
LIB_REC = {
    "impots_directs": "Impôts directs",
    "impots_indirects": "Impôts indirects",
    "autres_droits_taxes": "Autres droits et taxes",
    "total_recettes_fiscales": "Recettes fiscales",
    "produits_domaine": "Produits du domaine",
    "produits_concessions": "Produits des concessions",
    "revenus_domaine_services": "Revenus du domaine et des services payants",
    "participations_financieres": "Produits des participations financières",
    "produits_divers": "Produits divers",
    "total_recettes_non_fiscales": "Recettes non fiscales",
    "budget_annexe_ptt": "Budget annexe des PTT",
    "budget_annexe_rtt": "Budget annexe de la RTT",
    "budget_annexe_monopoles": "Budget annexe des monopoles",
    "total": "Total des recettes ordinaires",
}
VUE_FISCALE = ["total", "impots_indirects", "impots_directs", "autres_droits_taxes"]
VUE_AUTRES = ["participations_financieres", "revenus_domaine_services", "produits_domaine",
              "produits_concessions", "produits_divers", "budget_annexe_ptt",
              "budget_annexe_monopoles", "budget_annexe_rtt"]
_COUL = ["#1f4e79", "#c0392b", "#1a9850", "#e08214", "#6a3d9a", "#7f7f7f", "#8c564b", "#17becf"]


def recettes() -> pd.DataFrame:
    return figtools.series(S_REC)


def recettes_retenues() -> pd.DataFrame:
    d = recettes()
    return d[d.retenu.astype(str).str.lower() == "true"]


def _vue(postes, titre):
    r = recettes_retenues()
    fig, ax = plt.subplots(figsize=(9, 4.4))
    for p, c in zip(postes, _COUL):
        s = r[r.poste == p].sort_values("annee")
        if s.empty:
            continue
        ax.plot(s.annee, s.valeur_mdt, marker="o", ms=2.5, lw=2.2 if p == "total" else 1.5,
                color=c, label=LIB_REC[p])
    rp = ruptures_recettes()
    figtools.marque_rupture(ax, rp["monopoles_premier_exercice"], "monopoles au budget")
    figtools.marque_rupture(ax, rp["annexes_premier_exercice_sans"], "budgets annexes hors du tableau")
    ax.set_ylabel("millions de dinars courants")
    ax.grid(axis="y", alpha=0.3)
    ax.legend(fontsize=7, loc="upper left", bbox_to_anchor=(0, 0.9), frameon=False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_title(titre, fontsize=9, loc="left")
    fig.tight_layout()
    return fig


def vues_recettes():
    return [("Recettes fiscales et total", _vue(VUE_FISCALE, "Recettes fiscales et total")),
            ("Recettes non fiscales et budgets annexes",
             _vue(VUE_AUTRES, "Recettes non fiscales et budgets annexes"))]


def table_recettes() -> pd.DataFrame:
    r = recettes_retenues()
    t = r[["annee", "exercice", "poste", "libelle_imprime", "valeur_mdt", "valeur_imprimee",
           "unite_imprimee", "edition", "page_fichier", "lecture"]].copy()
    return t.sort_values(["annee", "poste"]).reset_index(drop=True)


def ruptures_recettes() -> dict:
    """Les ruptures de présentation, lues dans la série (éditions et valeurs)."""
    d = recettes()
    out = {}
    # Monopoles : dernier exercice où le budget annexe figure ; impôts indirects de cet
    # exercice dans les deux éditions qui l'impriment.
    mono = d[d.poste == "budget_annexe_monopoles"]
    ex = int(mono.annee.max())
    out["monopoles_dernier_exercice"] = ex
    out["monopoles_premier_exercice"] = ex + 1
    ii = d[(d.poste == "impots_indirects") & (d.annee == ex)].sort_values("edition")
    out["monopoles_ii"] = list(zip(ii.edition.astype(int), ii.valeur_mdt))
    out["monopoles_annexe"] = float(mono[mono.annee == ex].sort_values("edition").valeur_mdt.iloc[-1])
    # SITEP : l'exercice dont les impôts directs s'écartent le plus de la valeur retenue d'une
    # édition à l'autre (l'édition antérieure les imprime « déduction faite » du versement).
    idir = d[d.poste == "impots_directs"]
    exs = int(idir.loc[idir.ecart_au_retenu_mdt.abs().idxmax()].annee)
    x = idir[idir.annee == exs].sort_values("edition")
    out["sitep_exercice"] = exs
    out["sitep"] = list(zip(x.edition.astype(int), x.valeur_mdt))
    # Budgets annexes : dernière édition qui les imprime, première qui ne les imprime plus.
    ann = d[d.poste.str.startswith("budget_annexe")]
    eds = sorted(d.edition.unique())
    der = int(ann.edition.max())
    out["annexes_derniere_edition"] = der
    out["annexes_premiere_edition_sans"] = int(min(e for e in eds if e > der))
    out["annexes_premier_exercice_sans"] = int(ann.annee.max()) + 1
    # Gestion de neuf mois
    out["neuf_mois"] = d[d.exercice.str.contains("9 mois")].exercice.iloc[0]
    out["premier_exercice"] = int(d.annee.min())
    out["dernier_exercice"] = int(d.annee.max())
    out["editions"] = [int(e) for e in eds]
    return out


def controles_recettes() -> dict:
    c = figtools.series(S_REC_CTL)
    vc = c.resultat.value_counts()
    return {"n": len(c), **{k: int(v) for k, v in vc.items()}}


def md_recettes() -> str:
    r = recettes_retenues()
    cols = ["impots_directs", "impots_indirects", "autres_droits_taxes",
            "participations_financieres", "revenus_domaine_services", "produits_divers",
            "budget_annexe_ptt", "budget_annexe_monopoles", "total"]
    p = r.pivot_table(index=["annee", "exercice"], columns="poste", values="valeur_mdt",
                      aggfunc="first")
    e = r.pivot_table(index=["annee", "exercice"], columns="poste", values="edition",
                      aggfunc="first")
    entete = "| Exercice | " + " | ".join(LIB_REC[c] for c in cols) + " | Éditions |"
    lignes = [entete, "|---|" + "--:|" * len(cols) + "---|"]
    for (an, ex), row in p.iterrows():
        eds = sorted({int(v) for v in e.loc[(an, ex)].dropna()})
        lignes.append(f"| {ex} | " + " | ".join(_cell(row.get(c), 3) for c in cols)
                      + f" | {', '.join(map(str, eds))} |")
    return "\n".join(lignes)


# =============================================================================
# 3. Balance des paiements (rapports annuels de la BCT)
# =============================================================================
LIB_BDP = {
    "paiements_courants": "Paiements courants",
    "marchandises": "Marchandises (FOB)",
    "services": "Services",
    "revenus": "Revenus",
    "transferts": "Transferts",
    "mouvements_capitaux": "Mouvements de capitaux",
    "solde_general": "Solde général",
}


def bdp() -> pd.DataFrame:
    return figtools.series(S_BDP)


def soldes_retenus() -> pd.DataFrame:
    d = bdp()
    return d[(d.retenu.astype(str).str.lower() == "true") & (d.source == "ra")
             & (d.tableau == "soldes")]


def fig_bdp():
    r = soldes_retenus()
    fig, ax = plt.subplots(figsize=(9, 4.6))
    styles = {"paiements_courants": ("#1f4e79", 2.4, "-"), "solde_general": ("#000000", 2.0, "-"),
              "mouvements_capitaux": ("#1a9850", 1.6, "-"), "marchandises": ("#c0392b", 1.4, "--"),
              "services": ("#e08214", 1.4, "--"), "revenus": ("#6a3d9a", 1.4, "--"),
              "transferts": ("#7f7f7f", 1.4, "--")}
    for p, (c, lw, ls) in styles.items():
        s = r[r.poste == p].sort_values("annee")
        ax.plot(s.annee, s.valeur_md, color=c, lw=lw, ls=ls, marker="o", ms=2.5,
                label=LIB_BDP[p])
    ax.axhline(0, color=GRIS, lw=0.8)
    ax.set_ylabel("millions de dinars courants (soldes)")
    ax.grid(axis="y", alpha=0.3)
    ax.legend(fontsize=7, loc="lower left", frameon=False, ncol=2)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    return fig


def table_bdp() -> pd.DataFrame:
    r = soldes_retenus()
    return r[["annee", "poste", "libelle_imprime", "valeur_md", "edition", "page_fichier",
              "page_imprimee"]].sort_values(["annee", "poste"]).reset_index(drop=True)


def bornes_bdp() -> dict:
    d = bdp()
    ra = d[d.source == "ra"]
    p106 = d[d.source == "pub106"]
    red = ra[ra.poste == "redevance"]
    return {"premiere_annee": int(d.annee.min()), "derniere_annee": int(d.annee.max()),
            "ed_ra": (int(ra.edition.min()), int(ra.edition.max())),
            "ed_106": (int(p106.edition.min()), int(p106.edition.max())),
            "redevance_premiere_edition": int(red.edition.min())}


def md_bdp() -> str:
    r = soldes_retenus()
    cols = list(LIB_BDP)
    p = r.pivot_table(index="annee", columns="poste", values="valeur_md", aggfunc="first")
    e = r.pivot_table(index="annee", columns="poste", values="edition", aggfunc="first")
    lignes = ["| Année | " + " | ".join(LIB_BDP[c] for c in cols) + " | Édition |",
              "|---|" + "--:|" * len(cols) + "---|"]
    for an, row in p.iterrows():
        eds = sorted({int(v) for v in e.loc[an, cols].dropna()})
        lignes.append(f"| {an} | " + " | ".join(_cell(row.get(c), 0) for c in cols)
                      + f" | {', '.join(map(str, eds))} |")
    return "\n".join(lignes)


def controles_bdp() -> dict:
    c = figtools.series(S_BDP_CTL)
    vc = c.resultat.value_counts()
    ec = c[c.resultat == "écart"]
    return {"n": len(c), **{k: int(v) for k, v in vc.items()}, "ecarts": ec}


def raccord() -> pd.DataFrame:
    return figtools.series(S_BDP_RAC)


def raccord_pub106() -> dict:
    d = raccord()
    p = d[d.reference == "pub106"]
    out = {}
    for comp in ("meme_edition", "retenu"):
        x = p[p.comparaison == comp]
        out[comp] = (int((x.resultat == "égal").sum()), len(x))
    return out


LIB_MBP5 = {"paiements_courants": "Paiements courants (solde)",
            "marchandises": "Marchandises (solde)", "services": "Services (solde)",
            "revenus": "Revenus (solde)", "transferts": "Transferts (solde)",
            "recettes": "Recettes courantes", "depenses": "Dépenses courantes"}


def mbp5() -> pd.DataFrame:
    d = raccord()
    return d[d.reference == "mbp5"].copy()


def md_mbp5() -> str:
    m = mbp5()
    ans = sorted(m.annee.unique())
    lignes = ["| Poste | " + " | ".join(f"{a} : rapport annuel / MBP5 / écart" for a in ans) + " |",
              "|---|" + "--:|" * len(ans)]
    for p, lib in LIB_MBP5.items():
        x = m[m.poste == p].set_index("annee")
        cells = []
        for a in ans:
            if a not in x.index:
                cells.append("")
                continue
            r = x.loc[a]
            if pd.isna(r.valeur_reference_md):
                cells.append(f"{nb(r.valeur_ra_md, 0)} / — / —")
            else:
                cells.append(f"{nb(r.valeur_ra_md, 0)} / {nb(r.valeur_reference_md, 1)} / "
                             f"{nb(r.ecart_md, 1)}")
        lignes.append(f"| {lib} | " + " | ".join(cells) + " |")
    return "\n".join(lignes)


def plages_mbp5() -> dict:
    """Écarts au MBP5 (valeur absolue), par poste : (min, max), lignes comparées seulement."""
    m = mbp5().dropna(subset=["ecart_md"])
    return {p: (float(g.ecart_md.abs().min()), float(g.ecart_md.abs().max()))
            for p, g in m.groupby("poste")}


# =============================================================================
# 4. Recouvrement des deux mesures budgétaires
# =============================================================================
def recouvrement_bct_reglement() -> dict | None:
    """Gestion la plus récente commune au total BCT et aux recouvrements de la loi de règlement."""
    r = recettes_retenues()
    tot = r[r.poste == "total"].set_index("annee")
    t = table_reglement()
    t = t[t.gestion.str.fullmatch(r"\d{4}")]
    t = t.assign(annee=t.gestion.astype(int)).set_index("annee")
    communs = sorted(set(tot.index) & set(t.index))
    if not communs:
        return None
    a = communs[-1]
    return {"annee": int(a), "communs": (int(communs[0]), int(a)), "n": len(communs),
            "bct": float(tot.loc[a].valeur_mdt), "bct_edition": int(tot.loc[a].edition),
            "reglement": float(t.loc[a].recouvrements_md), "loi": t.loc[a].loi,
            "bloc": t.loc[a].bloc,
            "ecart": float(tot.loc[a].valeur_mdt) - float(t.loc[a].recouvrements_md)}

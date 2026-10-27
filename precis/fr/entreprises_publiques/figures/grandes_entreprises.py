"""Tableaux du chapitre « Les grandes entreprises » : une section par entreprise.

    from figures import grandes_entreprises as ge
    ge.tableau_fiche_court("steg", caption=…, tbl_id=…)     # premier plan, 2018-2023
    ge.tableau_fiche_detail("steg", "LF2022", caption=…)    # détail replié, une édition
    ge.tableau_steg_comptes(caption=…)                      # comptes publiés, 2013-2023
    ge.tableau_etap_rapports(caption=…)                     # rapports annuels de l'ETAP

D'OÙ VIENNENT LES DONNÉES. Trois séries de `tunisia-data`, lues par `figtools.series()` :
`entreprises-publiques-fiches-entreprises` (fiches du rapport annexé à la loi de finances,
famille budgétaire), `steg-etats-financiers` et `etap-rapports-annuels` (comptes publiés par
l'entreprise). Rien n'est saisi ici : ni valeur, ni page.

RÈGLES. Les deux familles ne se mêlent pas : un tableau lit une seule série. Dans le tableau
court, un exercice est donné dans la dernière édition qui le porte, nommée en tête de colonne
avec le statut du chiffre ; aucune valeur n'est raccordée d'une édition à l'autre. « — » : la
case n'existe pas dans l'édition ; case vide imprimée « - » : « – ».
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

from figures.entreprises_publiques import _md, _n  # noqa: E402

S_FICHES = "entreprises-publiques-fiches-entreprises"
S_STEG = "steg-etats-financiers"
S_ETAP = "etap-rapports-annuels"

# Le tableau court rapproche, pour la lecture, deux mises en page : ces paires désignent la même
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
          "probable": "probable"}


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


def tableau_fiche_court(entite: str, caption: str, tbl_id: str) -> None:
    """Huit lignes, exercices 2018-2023, dernière édition de chaque exercice."""
    f = _fiches(entite)
    exercices = sorted(f["exercice"].unique())
    der = {x: f[f["exercice"] == x]["edition"].max() for x in exercices}
    entetes = []
    for x in exercices:
        st = f[(f["exercice"] == x) & (f["edition"] == der[x])]["statut"].iloc[0]
        st = STATUT.get(st, st)
        entetes.append(f"{x}<br>({_ed(der[x])}{', ' + st if st else ''})")
    lignes = []
    for ind_a, ind_b, lib, signe in COURT:
        cases = []
        for x in exercices:
            ind = ind_a if der[x] == "LF2022" else ind_b
            if ind is None:
                cases.append("—")
                continue
            r = f[(f["exercice"] == x) & (f["edition"] == der[x]) & (f["indicateur"] == ind)]
            cases.append(_case(r.iloc[0] if len(r) else None, ind, signe))
        lignes.append([lib] + cases)
    _md(["Millions de dinars"] + entetes, "g" + "d" * len(exercices), lignes, caption, tbl_id)


def tableau_fiche_detail(entite: str, editions: tuple[str, ...], caption: str,
                         tbl_id: str) -> None:
    """Toutes les grandeurs imprimées par une mise en page, une colonne par (exercice, édition)."""
    f = _fiches(entite)
    f = f[f["edition"].isin(editions)]
    cols = sorted({(x, e) for x, e in zip(f["exercice"], f["edition"])})
    ordre = ORDRE_A if editions == ("LF2022",) else ORDRE_B
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


STEG_COLS = [("revenus", "Revenus"), ("subvention_exploitation", "Subvention d'exploitation"),
             ("resultat_exploitation", "Résultat d'exploitation"),
             ("resultat_net", "Résultat net"),
             ("resultat_net_apres_modifications", "Résultat après modifications comptables"),
             ("capitaux_propres", "Capitaux propres avant affectation"),
             ("total_passifs", "Total des passifs"),
             ("emprunts_non_courants", "dont emprunts non courants"),
             ("concours_bancaires", "dont concours bancaires")]


def tableau_steg_comptes(caption: str, tbl_id: str) -> None:
    """Comptes publiés de la STEG : un exercice par ligne, lu dans le fichier de l'exercice
    (2013 : colonne de comparaison du fichier de 2014)."""
    s = figtools.series(S_STEG)
    m = s[s["fichier_du_meme_exercice"].astype(bool)
          | ((s["exercice"] == 2013) & (s["document"] == "steg_ef_2014.pdf"))]
    lignes = []
    for x in sorted(m["exercice"].unique()):
        b = m[m["exercice"] == x]
        cases = []
        for g, _ in STEG_COLS:
            r = b[(b["grandeur"] == g) & (b["colonne"].isin(["exercice", "exercice précédent"]))]
            signe = g.startswith("resultat")
            cases.append("—" if r.empty else _n(r.iloc[0]["valeur_md"], 1, signe))
        lignes.append([str(x)] + cases)
    _md(["Exercice"] + [l for _, l in STEG_COLS], "g" + "d" * len(STEG_COLS), lignes,
        caption, tbl_id)


ETAP_COLS = [("revenus", "Revenus"), ("produits_exploitation", "Produits d'exploitation"),
             ("resultat_net", "Résultat net"), ("effectif", "Effectif en fin d'année (agents)")]


def tableau_etap_rapports(caption: str, tbl_id: str) -> None:
    """Rapports annuels de l'ETAP : un exercice par ligne, lu dans le rapport de l'exercice,
    à défaut dans le rapport suivant (colonne de l'exercice précédent), nommé en note."""
    s = figtools.series(S_ETAP)
    lignes = []
    for x in sorted(s["exercice"].unique()):
        b = s[s["exercice"] == x]
        cases = []
        for g, _ in ETAP_COLS:
            r = b[b["grandeur"] == g]
            if r.empty:
                cases.append("—")
                continue
            propre = r[r["exercice_couverture"] == x]
            r = (propre if len(propre) else r.sort_values("exercice_couverture")).iloc[0]
            dec = 0 if g == "effectif" else 1
            txt = _n(r["valeur"], dec, g == "resultat_net")
            if r["exercice_couverture"] != x:
                txt += f" (RA {int(r['exercice_couverture'])})"
            cases.append(txt)
        lignes.append([str(x)] + cases)
    _md(["Exercice"] + [l for _, l in ETAP_COLS], "g" + "d" * len(ETAP_COLS), lignes,
        caption, tbl_id)

"""Données de la navigation par année de l'annexe « Les comptes de la nation ».

D'OÙ VIENNENT LES DONNÉES. Deux séries de `tunisia-data`, lues par `figtools.series()`,
toutes deux issues des *Comptes de la nation* de l'INS, base 2015 (édition la plus récente
par année) :

  - ``cnat-approche-revenus`` — l'approche des revenus de l'économie entière :
    rémunération des salariés, revenu d'exploitation (excédent brut + revenu mixte),
    impôts sur la production et les importations, subventions, PIB.
  - ``cnat-approche-revenus-secteurs`` — la valeur ajoutée des quatre secteurs
    institutionnels (SNF, sociétés financières, administrations, ménages).

IDENTITÉ GARANTIE, chaque année. La valeur ajoutée totale (somme des secteurs) égale la
somme rémunération + revenu d'exploitation (les deux présentations de l'INS p. 27) ; le PIB
s'en déduit en ajoutant les impôts sur les produits nets de subventions. Les deux approches
retombent donc sur le même PIB. On ne retient que les années où les deux séries sont
complètes en base 2015, et l'on écarte la dernière année si elle est provisoire.

Ce module ne trace rien : il ne fait que préparer la structure passée à Observable par
``ojs_define`` dans le `.qmd`. L'interactivité (curseur d'année, tableaux recomposés) vit
dans le bloc ``{ojs}`` de l'annexe, rendu en HTML seulement.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, ".")
sys.path.insert(0, "../../scripts")

import figtools  # noqa: E402

SECTEURS = {
    "snf": "Sociétés non financières",
    "sf": "Sociétés financières",
    "apu": "Administrations publiques",
    "menages": "Ménages (y c. entreprises individuelles)",
}
ORDRE = ["snf", "sf", "apu", "menages"]

# Dernière année retenue : au-delà, l'INS ne publie encore que des estimations provisoires.
ANNEE_MAX = 2024


def _f(x) -> float:
    return round(float(x), 1)


def donnees_navigation() -> dict:
    rev = figtools.series("cnat-approche-revenus")
    sec = figtools.series("cnat-approche-revenus-secteurs")

    rev = rev[(rev["base"].astype(str) == "2015") & (rev["annee"].astype(int) <= ANNEE_MAX)]
    sec = sec[(sec["base"].astype(str) == "2015") & (sec["annee"].astype(int) <= ANNEE_MAX)]

    par_annee = {}
    for _, r in rev.iterrows():
        annee = int(r["annee"])
        sec_a = sec[sec["annee"].astype(int) == annee]
        if len(sec_a) < 4:
            continue  # année incomplète côté secteurs : on l'écarte

        secteurs = []
        va_totale = 0.0
        for cle in ORDRE:
            ligne = sec_a[sec_a["secteur"] == cle]
            if ligne.empty:
                break
            va = _f(ligne.iloc[0]["valeur_ajoutee"])
            secteurs.append({"nom": SECTEURS[cle], "va": va})
            va_totale += va
        if len(secteurs) < 4:
            continue
        va_totale = round(va_totale, 1)

        remuneration = _f(r["remuneration_salaries"])
        revenu_exploitation = _f(r["revenu_exploitation"])
        impots = _f(r["impots_production_importations"])
        subventions = abs(_f(r["subventions"]))
        pib = _f(r["pib_approche_revenus"])
        impots_nets_produits = round(pib - va_totale, 1)

        par_annee[str(annee)] = {
            "pib": pib,
            "production": {
                "secteurs": secteurs,
                "va_totale": va_totale,
                "impots_nets_produits": impots_nets_produits,
            },
            "revenus": {
                "remuneration": remuneration,
                "revenu_exploitation": revenu_exploitation,
                "impots": impots,
                "subventions": subventions,
            },
            "part_salaires_pib": _f(r["part_remuneration_pib"]),
            "part_salaires_snf": _f(r["part_salaires_societes"]),
            "edition": str(r["edition"]),
        }

    annees = sorted(int(a) for a in par_annee)
    return {
        "annees": annees,
        "annee_defaut": 2021 if 2021 in annees else annees[-1],
        "parAnnee": par_annee,
    }


# --- la séquence des comptes, désagrégée par secteur -------------------------
# Ménages rétabli : la collision de slug de consolidate_cnat.py (ménages confondu avec sa
# sous-table « entreprises individuelles ») a été corrigée en amont (tunisia-data), et le compte
# complet des ménages régénéré (VA 2012 = 29 307,3 ; RDB ≠ épargne ; consommation finale présente).
SECTEURS_SEQ = [("snf", "SNF"), ("sf", "SF"), ("apu", "APU"),
                ("menages", "Ménages"), ("rdm", "Reste du monde")]

# Séquence des comptes : (compte, [(libellé, opération, côté, est_solde, clé de l'ancienne série)]).
# Opération et côté renvoient à la série `cnat-secteurs` (base 2015, emplois et ressources
# distingués). La dernière colonne est la clé de l'ancienne série `cnat-comptes-secteurs`, qui ne
# distingue pas les côtés : elle ne sert, pour les années en base 1997, qu'aux soldes et aux emplois
# sans ambiguïté (consommation finale, FBCF) ; les autres lignes y restent vides.
SEQUENCE = [
    ("Compte de production", [
        ("Production", "production", "ressources", False, None),
        ("Consommation intermédiaire", "consommation_intermediaire", "emplois", False, None),
        ("Valeur ajoutée brute", "valeur_ajoutee_brute", "emplois", True, "valeur ajoutee brute")]),
    ("Compte d'exploitation", [
        ("Rémunération des salariés versée", "remuneration_salaries", "emplois", False, None),
        ("Autres impôts sur la production", "autres_impots_production", "emplois", False, None),
        ("Revenu d'exploitation / mixte", "revenu_exploitation", "emplois", True, "revenu d'exploitation")]),
    ("Compte d'affectation des revenus primaires", [
        ("Rémunération des salariés reçue", "remuneration_salaries", "ressources", False, None),
        ("Impôts sur la production et les importations reçus", "impots_production_importations", "ressources", False, None),
        ("Subventions versées (−)", "subventions", "ressources", False, None),
        ("Revenus de la propriété reçus", "revenus_propriete", "ressources", False, None),
        ("Revenus de la propriété versés", "revenus_propriete", "emplois", False, None),
        ("Solde des revenus primaires", "solde_revenus_primaires", "emplois", True,
         "solde des revenus primaires / revenu national")]),
    ("Compte de distribution secondaire du revenu", [
        ("Impôts courants sur le revenu et le patrimoine reçus", "impots_courants", "ressources", False, None),
        ("Impôts courants sur le revenu et le patrimoine versés", "impots_courants", "emplois", False, None),
        ("Cotisations sociales reçues", "cotisations_sociales", "ressources", False, None),
        ("Cotisations sociales versées", "cotisations_sociales", "emplois", False, None),
        ("Prestations sociales en espèces reçues", "prestations_especes", "ressources", False, None),
        ("Prestations sociales en espèces versées", "prestations_especes", "emplois", False, None),
        ("Autres transferts courants reçus", "autres_transferts_courants", "ressources", False, None),
        ("Autres transferts courants versés", "autres_transferts_courants", "emplois", False, None),
        ("Revenu disponible brut", "revenu_disponible_brut", "emplois", True, "revenu disponible brut")]),
    ("Compte d'utilisation du revenu", [
        ("Dépense de consommation finale", "consommation_finale", "emplois", False, "depense de consommation finale"),
        ("Épargne brute", "epargne_brute", "emplois", True, "epargne brute")]),
    ("Compte de capital", [
        ("Transferts en capital reçus", "transferts_capital", "ressources", False, None),
        ("Transferts en capital versés", "transferts_capital", "emplois", False, None),
        ("Formation brute de capital fixe", "fbcf", "emplois", False, "formation brute de capitale fixe"),
        ("Variation des stocks", "variation_stocks", "emplois", False, None),
        ("Capacité (+) ou besoin (−) de financement", "capacite_financement", "emplois", True,
         "capacite ou besoin de financement")]),
]
# secteur de la série `cnat-secteurs` -> secteur de l'ancienne série
ANCIEN_SECTEUR = {"rdm": "exterieur"}


def _fr(v) -> str:
    import math
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return ""
    return f"{v:,.1f}".replace(",", "\u202f").replace(".", ",")



# bases retenues, de la plus récente à la plus ancienne : pour une année couverte par deux
# bases, on montre la plus récente (les bases ne se chaînent pas, mais une année isolée est
# un instantané dans SA base — le navigateur n'affiche qu'une année à la fois, étiquetée).
BASES_ORDRE = ["2015", "1997"]


def donnees_sequence() -> dict:
    """Structure passée à Observable : séquence des comptes par secteur, une année à la fois.

    Années en base 2015 : série `cnat-secteurs` (emplois et ressources distingués, édition la plus
    récente). Années antérieures, en base 1997 : ancienne série `cnat-comptes-secteurs`, qui ne
    distingue pas les côtés, réduite aux soldes et aux emplois sans ambiguïté. Aucune base n'est
    chaînée à une autre ; chaque année porte sa base, que le navigateur affiche.
    """
    neuf = figtools.series("cnat-secteurs")
    ancien = figtools.series("cnat-comptes-secteurs")
    sequence = [{"compte": c, "lignes": [{"label": lib, "cle": f"{op}|{cote}", "solde": s}
                                        for lib, op, cote, s, _ in lignes]}
                for c, lignes in SEQUENCE]
    par_annee, base_annee, edition_annee = {}, {}, {}
    annees_neuves = set(neuf["annee"].astype(int))
    for an in sorted(annees_neuves):
        dn = neuf[(neuf["annee"].astype(int) == an) & (neuf["sous_ligne"].astype(int) == 0)]
        bloc = {}
        for sec, _ in SECTEURS_SEQ:
            ds = dn[dn["secteur"] == sec]
            vals = {}
            for _, r in ds.iterrows():
                vals[f"{r['operation']}|{r['cote']}"] = round(float(r["valeur"]), 1)
            # SNF et SF n'impriment qu'une ligne « Production des biens et services marchands »
            if "production|ressources" not in vals and "production_bs_marchands|ressources" in vals:
                vals["production|ressources"] = vals["production_bs_marchands|ressources"]
            bloc[sec] = vals
        par_annee[str(an)] = bloc
        base_annee[str(an)] = "2015"
        edition_annee[str(an)] = ", ".join(sorted(set(dn["edition"].astype(str))))
    for an in sorted(set(ancien["annee"].astype(int)) - annees_neuves):
        da = ancien[(ancien["annee"].astype(int) == an) & (ancien["base_pib"].astype(str) == "1997")]
        if da.empty:
            continue
        bloc = {}
        for sec, _ in SECTEURS_SEQ:
            ds = da[da["secteur"] == ANCIEN_SECTEUR.get(sec, sec)]
            par_cle = {r["indicateur"]: round(float(r["valeur"]), 1) for _, r in ds.iterrows()}
            bloc[sec] = {f"{op}|{cote}": par_cle[cle]
                         for _, lignes in SEQUENCE for _, op, cote, _, cle in lignes
                         if cle and cle in par_cle}
        par_annee[str(an)] = bloc
        base_annee[str(an)] = "1997"
    annees = sorted(int(a) for a in par_annee)
    return {
        "annees": annees,
        "annee_defaut": 2024 if 2024 in annees else annees[-1],
        "secteurs": [[c, lib] for c, lib in SECTEURS_SEQ],
        "sequence": sequence,
        "parAnnee": par_annee,
        "baseAnnee": base_annee,
        "editionAnnee": edition_annee,
    }


def sequence_comptes_md(annee: int = 2024) -> str:
    """Table Markdown de la séquence des comptes par secteur, pour une année en base 2015.

    Lignes = la séquence (opérations et soldes, emplois et ressources distingués) ; colonnes = les
    cinq secteurs ; valeurs lues telles quelles dans les comptes de l'INS, en millions de dinars.
    """
    bloc = donnees_sequence()["parAnnee"][str(annee)]
    cols = [lib for _, lib in SECTEURS_SEQ]
    out = ["| Compte / opération | " + " | ".join(cols) + " |",
           "|" + "---|" * (len(cols) + 1)]
    for compte, lignes in SEQUENCE:
        out.append(f"| **{compte}** |" + " |" * len(cols))
        for lib, op, cote, solde, _ in lignes:
            nom = f"*{lib}*" if solde else f"&nbsp;&nbsp;{lib}"
            cells = " | ".join(_fr(bloc.get(sec, {}).get(f"{op}|{cote}")) for sec, _ in SECTEURS_SEQ)
            out.append(f"| {nom} | {cells} |")
    return "\n".join(out)


if __name__ == "__main__":
    import json

    d = donnees_navigation()
    print("années:", d["annees"], "| défaut:", d["annee_defaut"])
    ex = d["parAnnee"]["2021"]
    print("2021 PIB:", ex["pib"], "| VA totale:", ex["production"]["va_totale"],
          "| impôts nets produits:", ex["production"]["impots_nets_produits"])
    rv = ex["revenus"]
    recompose = round(rv["remuneration"] + rv["revenu_exploitation"] + rv["impots"] - rv["subventions"], 1)
    print("revenus recomposent PIB:", recompose, "==", ex["pib"], "→", abs(recompose - ex["pib"]) < 0.2)
    print("VA totale == rémun + revenu expl:",
          round(rv["remuneration"] + rv["revenu_exploitation"], 1), "==", ex["production"]["va_totale"])


def recoupements_md() -> str:
    """Table Markdown : écart, en % de la série budgétaire, entre les comptes des administrations
    publiques (INS) et la série budgétaire que les volumes emploient, année par année."""
    d = figtools.series("cnat-recoupements")
    annees = sorted(d["annee"].astype(int).unique())
    out = ["| Grandeur (comptes face au budget) | " + " | ".join(str(a) for a in annees) + " |",
           "|---|" + "---:|" * len(annees)]
    for objet, g in d.groupby("objet", sort=False):
        par = {int(r["annee"]): r["ecart_pct"] for _, r in g.iterrows()}
        cells = " | ".join("" if par.get(a) is None else f"{par[a]:+.1f}".replace(".", ",").replace("-", "−")
                           for a in annees)
        out.append(f"| {objet} | {cells} |")
    return "\n".join(out)


COUVERTURE_LIB = {"domicile": "domicile", "renvoi": "en partie", "vide": "aucun volume", "solde": "solde"}
COTE_LIB = {"emplois": "emplois", "ressources": "ressources"}


def _liens(volumes: str, pages: str) -> str:
    if not isinstance(pages, str) or not pages:
        return ""
    vs, ps = volumes.split(" ; "), pages.split(" ; ")
    return " ; ".join(f"[{v}]({p})" for v, p in zip(vs, ps))


def correspondance_md(compte: str | None = None, seulement_vides: bool = False) -> str:
    """Table Markdown de la matrice opérations × secteurs × côté × volumes (sans code d'opération)."""
    d = pd.read_csv(Path(__file__).resolve().parent.parent / "correspondance-comptes.csv")
    if compte:
        d = d[d["compte"] == compte]
    if seulement_vides:
        d = d[d["couverture"] == "vide"]
    out = ["| Opération | Secteur | Côté | Niveau (MD) | Année | Rattachement | Volumes |",
           "|---|---|---|---:|---:|---|---|"]
    for _, r in d.iterrows():
        out.append(f"| {r['libelle']} | {r['secteur_libelle']} | {COTE_LIB[r['cote']]} | "
                   f"{_fr(float(r['niveau_md']))} | {int(r['annee'])} | {COUVERTURE_LIB[r['couverture']]} | "
                   f"{_liens(r['volumes'], r['pages'])} |")
    return "\n".join(out)


def correspondance_comptes() -> list[str]:
    d = pd.read_csv(Path(__file__).resolve().parent.parent / "correspondance-comptes.csv")
    return list(dict.fromkeys(d["compte"]))


def correspondance_resume() -> dict:
    d = pd.read_csv(Path(__file__).resolve().parent.parent / "correspondance-comptes.csv")
    return d["couverture"].value_counts().to_dict()

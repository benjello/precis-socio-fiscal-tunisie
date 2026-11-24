#!/usr/bin/env python3
"""Engendre `precis/fr/correspondance-comptes.csv` : la matrice opérations × secteurs × côté ×
volumes, opérations vides comprises.

Une ligne par (opération, secteur, côté) que publient les comptes des secteurs de l'INS (série
`cnat-secteurs`, cinq secteurs principaux), avec :
  - le niveau de l'année la plus récente qui soit définitive ou semi-définitive, et son édition ;
  - le rattachement aux volumes, déclaré ci-dessous (RATTACHEMENT) : `domicile` (le volume qui
    documente le dispositif), `renvoi` (un volume en traite une partie ou y renvoie), `vide` (aucun
    volume ne le traite encore) ;
  - les pages visées, sous forme de liens relatifs que contrôle scripts/verifier_liens_entre_volumes.py.

Le code SCN 2008 de l'opération reste dans le CSV (donnée) ; la page publiée ne l'affiche pas.

Usage : uv run python scripts/generate_correspondance_comptes.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "precis" / "_seriescache"
SORTIE = RACINE / "precis" / "fr" / "correspondance-comptes.csv"

SECTEURS = {"snf": "Sociétés non financières", "sf": "Sociétés financières",
            "apu": "Administrations publiques", "menages": "Ménages", "rdm": "Reste du monde"}

# opération -> liste de règles (secteurs visés ou None pour tous, côté ou None, couverture,
#            [(volume, page)]) ; la première règle qui s'applique l'emporte.
D, R, V = "domicile", "renvoi", "vide"
RATTACHEMENT: dict[str, list] = {
    "production": [(["apu"], None, R, [("Les rémunérations dans le secteur public", "remunerations_publiques/")]),
                   (["snf", "menages"], None, R, [("L'agriculture", "agriculture/"), ("Le transport", "transport/"), ("L'environnement", "environnement/")])],
    # composantes de la production : même rattachement que leur total
    "production_marchande": [(["menages"], None, R, [("L'agriculture", "agriculture/"), ("Le transport", "transport/"), ("L'environnement", "environnement/")])],
    "production_non_marchande": [(["apu"], None, R, [("Les rémunérations dans le secteur public", "remunerations_publiques/")]),
                                 (["menages"], None, R, [("L'agriculture", "agriculture/")])],
    "production_bs_marchands": [(["apu"], None, R, [("Les rémunérations dans le secteur public", "remunerations_publiques/")]),
                                (["snf"], None, R, [("L'agriculture", "agriculture/"), ("Le transport", "transport/"), ("L'environnement", "environnement/")])],
    "valeur_ajoutee_brute": [(None, None, R, [("Les comptes de la nation", "annexe-comptes-nation.html#sec-cn-comptes-secteurs")])],
    "remuneration_salaries": [(["apu"], "emplois", D, [("Les rémunérations dans le secteur public", "remunerations_publiques/")]),
                              (["menages"], "ressources", D, [("Le marché du travail", "marche_travail/_salaire_minimum.html"), ("Les rémunérations dans le secteur public", "remunerations_publiques/")]),
                              (["snf", "sf", "menages"], "emplois", R, [("Le marché du travail", "marche_travail/_conventions.html")])],
    "cotisations_employeurs": [(None, None, D, [("Les cotisations sociales", "cotisations_sociales/_taux_global.html")])],
    "salaires_bruts": [(None, None, R, [("Le marché du travail", "marche_travail/_salaire_minimum.html")])],
    "autres_impots_production": [(None, None, D, [("Les finances locales", "finances_locales/_impots_activite.html"), ("La fiscalité", "fiscalite/_taxes_fonds_speciaux.html"), ("Les cotisations sociales", "cotisations_sociales/_prelevements_salaires.html")])],
    "autres_subventions_production": [(None, None, R, [("Les entreprises publiques", "entreprises_publiques/_transferts.html"), ("Le transport", "transport/_depense.html"), ("L'agriculture", "agriculture/_depense.html")])],
    "impots_production_importations": [(["apu"], "ressources", D, [("La fiscalité", "fiscalite/")])],
    "tva": [(None, None, D, [("La fiscalité", "fiscalite/_tva.html")])],
    "impots_importations": [(None, None, D, [("La fiscalité", "fiscalite/_droits_douane.html")])],
    "autres_impots_produits": [(None, None, D, [("La fiscalité", "fiscalite/_droits_consommation.html"), ("La fiscalité", "fiscalite/_timbre_enregistrement.html")])],
    "subventions": [(["apu"], None, D, [("La compensation", "compensation/_depense.html")])],
    "subventions_produits": [(None, None, D, [("La compensation", "compensation/_depense.html")])],
    "interets": [(["apu"], "emplois", R, [("La dette publique", "annexe-dette-publique.html")]),
                 # intérêts reçus par l'État : prêts du Trésor aux entreprises publiques
                 (["apu"], "ressources", R, [("Les entreprises publiques", "entreprises_publiques/_garanties.html")])],
    "revenus_distribues": [(["apu"], "ressources", D, [("Les entreprises publiques", "entreprises_publiques/_recettes.html")])],
    "revenus_propriete": [(["apu"], "ressources", R, [("Les entreprises publiques", "entreprises_publiques/_recettes.html")]),
                          (["apu"], "emplois", R, [("La dette publique", "annexe-dette-publique.html")])],
    "impots_courants": [(["apu"], "ressources", D, [("La fiscalité", "fiscalite/_impot_revenu.html"), ("La fiscalité", "fiscalite/_impot_societes.html")]),
                        (["menages"], "emplois", D, [("La fiscalité", "fiscalite/_impot_revenu.html")]),
                        (["snf", "sf"], "emplois", D, [("La fiscalité", "fiscalite/_impot_societes.html")])],
    "cotisations_sociales": [(["apu", "menages"], None, D, [("Les cotisations sociales", "cotisations_sociales/"), ("Les caisses de sécurité sociale", "caisses/")])],
    "prestations_especes": [(["apu", "menages"], None, D, [("Les retraites", "retraites/"), ("Les prestations sociales", "prestations_sociales/")])],
    "transferts_entre_administrations": [(None, None, D, [("Les finances locales", "finances_locales/_transferts.html"), ("Les caisses de sécurité sociale", "caisses/_etat_caisses.html")])],
    "indemnites_assurance_dommages": [(["menages"], None, R, [("L'agriculture", "agriculture/_calamites.html")])],
    "primes_assurance_dommages": [(["menages"], None, R, [("L'agriculture", "agriculture/_calamites.html")])],
    "consommation_finale": [(["apu"], None, R, [("La santé", "sante/_couverture.html"), ("L'éducation et la formation", "education/_depense.html")])],
    "impots_capital": [(None, None, D, [("La fiscalité", "fiscalite/_patrimoine_immobilier.html#sec-pi-donations-successions")])],
    "aides_investissement": [(None, None, D, [("La fiscalité", "fiscalite/_regimes_incitation.html"), ("L'agriculture", "agriculture/_investissement.html")])],
    "autres_transferts_capital": [(["apu", "snf"], None, R, [("L'agriculture", "agriculture/_credit.html"), ("Les entreprises publiques", "entreprises_publiques/_restructuration.html")])],
    "transferts_capital": [(["apu"], None, R, [("La fiscalité", "fiscalite/_regimes_incitation.html")]),
                           (["snf"], None, R, [("Les entreprises publiques", "entreprises_publiques/_restructuration.html")])],
    "fbcf": [(["apu"], None, R, [("Le transport", "transport/_infrastructure.html"), ("L'environnement", "environnement/_depense.html")]),
             (["snf"], None, R, [("Les entreprises publiques", "entreprises_publiques/_longue_periode.html")])],
    "capacite_financement": [(["apu"], None, R, [("Le budget de l'État", "annexe-budget-etat.html")])],
    "titres_creance": [(["apu"], "ressources", R, [("La dette publique", "annexe-dette-publique.html")])],
    "credits": [(["apu"], None, R, [("La dette publique", "annexe-dette-publique.html"), ("Les entreprises publiques", "entreprises_publiques/_garanties.html")])],
    "actions_opc": [(["apu"], None, R, [("Les entreprises publiques", "entreprises_publiques/_cessions.html")])],
}

# Prolongement (24/11/2026) : volumes de branche, consommation, investissement, échanges, cadre.
# Les règles s'ajoutent APRÈS celles du dictionnaire : la première qui s'applique l'emporte.
BRANCHES = [("L'énergie", "energie/"), ("L'industrie et les mines", "industrie/"),
            ("Le logement et la construction", "logement/")]
for _op in ("production", "production_marchande", "production_bs_marchands"):
    for _secteurs, _c, _couv, _pages in RATTACHEMENT.get(_op, []):
        if _secteurs and "snf" in _secteurs:
            _pages.extend(BRANCHES)
_AJOUTS = {
    "consommation_intermediaire": [(["snf", "menages"], None, R, BRANCHES)],
    "consommation_finale": [(["menages"], None, D, [("La consommation et les niveaux de vie", "consommation/")])],
    "exportations": [(["rdm"], None, D, [("Les échanges extérieurs", "echanges/")])],
    "importations": [(["rdm"], None, D, [("Les échanges extérieurs", "echanges/")])],
    "importations_biens": [(["rdm"], None, D, [("Les échanges extérieurs", "echanges/")])],
    "importations_services": [(["rdm"], None, D, [("Les échanges extérieurs", "echanges/")])],
    "solde_echanges_exterieurs": [(None, None, R, [("Les échanges extérieurs", "echanges/")])],
    "fbcf": [(["snf", "sf", "menages"], None, R, [("L'investissement", "investissement/")])],
    "variation_stocks": [(None, None, R, [("L'investissement", "investissement/")])],
}
for _f in ("numeraire_depots", "titres_creance", "credits", "actions_opc", "provisions_assurance",
           "autres_comptes", "or_dts", "interets", "revenus_propriete"):
    _AJOUTS.setdefault(_f, []).append((["sf"], None, R, [("Le cadre", "cadre/_monnaie_credit.html")]))
for _op, _regles in _AJOUTS.items():
    RATTACHEMENT.setdefault(_op, []).extend(_regles)
SOLDES_NATURE = {"solde"}


def regle(op: str, secteur: str, cote: str):
    for secteurs, c, couverture, pages in RATTACHEMENT.get(op, []):
        if (secteurs is None or secteur in secteurs) and (c is None or c == cote):
            return couverture, pages
    return V, []


def page_existe(page: str) -> bool:
    """La page visée (depuis precis/fr/) existe, et son ancre y est définie."""
    chemin, _, ancre = page.partition("#")
    fr = RACINE / "precis" / "fr"
    qmd = fr / chemin / "index.qmd" if chemin.endswith("/") else (fr / chemin).with_suffix(".qmd")
    if not qmd.exists():
        return False
    return not ancre or f"{{#{ancre}}}" in qmd.read_text(encoding="utf-8")


def main() -> int:
    s = pd.read_csv(CACHE / "cnat-secteurs.csv")
    s = s[(s["secteur"].isin(SECTEURS)) & (s["sous_ligne"] == 0)
          & (s["statut_annee"].isin(["definitif", "semi_definitif"]))]
    s = s[~s["operation"].isin(["ecart_statistique", "variation_dettes", "correction_sifim"])]
    # l'INS titre « Production ou Compte extérieur Biens & Services » le premier compte de ses pages :
    # c'est le compte de production pour un secteur résident, le compte extérieur pour le reste du monde
    s.loc[(s["secteur"] != "rdm") & s["compte"].str.startswith("Production ou"), "compte"] = "Compte de production"
    s["compte"] = s["compte"].replace({"Production ou Compte extérieur Biens & Services": "Compte extérieur des biens et services",
                                       "Compte extérieur Biens & Services": "Compte extérieur des biens et services"})
    lignes = []
    for (op, sec, cote), g in s.groupby(["operation", "secteur", "cote"]):
        g = g.sort_values("annee")
        der = g.iloc[-1]
        couverture, pages = regle(op, sec, cote)
        if str(der["code_scn2008"]).startswith("B.") and couverture == V:
            # un solde n'est pas un dispositif : il se lit dans l'annexe, avec la séquence
            couverture, pages = "solde", [("Les comptes de la nation", "annexe-comptes-nation.html#sec-cn-comptes-secteurs")]
        lignes.append({
            "compte": der["compte"], "operation": op, "libelle": der["libelle_ins"],
            "code_scn2008": der["code_scn2008"], "secteur": sec, "secteur_libelle": SECTEURS[sec],
            "cote": cote, "couverture": couverture,
            "volumes": " ; ".join(v for v, _ in pages),
            "pages": " ; ".join(p for _, p in pages),
            "annee": int(der["annee"]), "niveau_md": round(float(der["valeur"]), 1),
            "edition": der["edition"],
        })
    out = pd.DataFrame(lignes)
    ordre = ["Compte de production", "Compte d'exploitation", "Compte d'affectation des revenus primaires",
             "Compte de distribution secondaire du revenu", "Compte d'utilisation du revenu disponible",
             "Compte de capital", "Compte financier", "Compte extérieur des biens et services"]
    out["_o"] = out["compte"].map({c: i for i, c in enumerate(ordre)}).fillna(99)
    out = out.sort_values(["_o", "operation", "secteur", "cote"]).drop(columns="_o")
    absentes = sorted({p for ps in out["pages"] for p in str(ps).split(" ; ") if p and p != "nan" and not page_existe(p)})
    if absentes:
        print("PAGES VISÉES ABSENTES :", absentes)
        return 1
    out.to_csv(SORTIE, index=False)
    print(out["couverture"].value_counts().to_string())
    print(f"{len(out)} lignes écrites dans {SORTIE.relative_to(RACINE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Engendre `cnat-recoupements` : les grandeurs des comptes des administrations publiques face aux
séries budgétaires que les volumes emploient.

Comptes : série `cnat-secteurs` (INS, base 2015, édition la plus récente). Budget : séries du cache
tirées du ministère des Finances. Les deux familles ne mesurent pas la même chose (périmètre :
administrations publiques consolidées face à l'État ; moment : droits constatés face à
encaissements ; contenu : TVA non déductible face à TVA encaissée nette des restitutions…) : l'écart
se lit comme une différence de périmètre, déclarée paire par paire, jamais comme une erreur de
l'une ou de l'autre source.

Usage : uv run python scripts/recouper_cnat_volumes.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import yaml

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "precis" / "_seriescache"

# (opération des comptes, côté, secteur, signe appliqué, série budgétaire, colonne ou filtre,
#  libellé, périmètre des comptes, périmètre de la série budgétaire)
PAIRES = [
    ("tva", "ressources", "apu", 1, "recettes-fiscales-composition", "tva_MDT",
     "TVA",
     "TVA non déductible reçue par les administrations publiques, droits constatés",
     "TVA encaissée par le budget de l'État"),
    ("impots_importations", "ressources", "apu", 1, "recettes-fiscales-composition", "douanes_MDT",
     "Droits et impôts sur les importations",
     "droits et impôts sur les importations hors TVA, administrations publiques",
     "droits de douane encaissés par le budget de l'État"),
    ("impots_courants", "ressources", "apu", 1, "recettes-fiscales-composition", "irpp_MDT+is_MDT",
     "Impôts courants sur le revenu et le patrimoine",
     "impôts courants sur le revenu et le patrimoine reçus par les administrations publiques",
     "IRPP et impôt sur les sociétés encaissés par le budget de l'État"),
    ("subventions_produits", "ressources", "apu", -1, "compensation-parts", "total",
     "Subventions sur les produits / compensation",
     "subventions sur les produits versées par les administrations publiques (toutes subventions sur les produits)",
     "dépense budgétaire de compensation (produits de base, carburants, transport)"),
    ("remuneration_salaries", "emplois", "apu", 1, "budget-desagregation-nature", "remunerations_MDT",
     "Rémunération des salariés",
     "rémunération des salariés des administrations publiques consolidées (cotisations des employeurs comprises, dont imputées)",
     "dépenses de rémunération du budget de l'État"),
    ("fbcf", "emplois", "apu", 1, "budget-desagregation-nature", "equipement_MDT",
     "FBCF / dépenses d'équipement",
     "formation brute de capital fixe des administrations publiques consolidées",
     "dépenses d'équipement du budget de l'État (y compris ce qui n'est pas de la FBCF)"),
]


SOURCES = {"recettes-fiscales-composition": "minfin-recettes-fiscales",
           "budget-desagregation-nature": "minfin-repartition-depenses-xls"}


def _budget(serie: str, col: str) -> tuple[pd.Series, pd.Series]:
    """(valeur par année, clé de citation par année)."""
    d = pd.read_csv(CACHE / f"{serie}.csv")
    if serie == "compensation-parts":
        d = d[(d["famille"] == "budget") & (d["poste"] == "total") & (d["nature"] == "budgetaire")]
        d = d.groupby("annee").last()
        return d["valeur_MDT"], d["source"]
    d = d.set_index("annee")
    v = sum(d[c] for c in col.split("+"))
    return v, pd.Series(SOURCES[serie], index=d.index)


def main() -> int:
    lignes = []
    for op, cote, sec, signe, serie, col, lib, per_c, per_b in PAIRES:
        c = pd.read_csv(CACHE / "cnat-secteurs.csv")
        c = c[(c["operation"] == op) & (c["cote"] == cote) & (c["secteur"] == sec)]
        c = c.groupby("annee").agg(valeur=("valeur", "sum"), edition=("edition", "last"))
        b, src = _budget(serie, col)
        for an, r in c.iterrows():
            if an not in b.index or pd.isna(b.loc[an]):
                continue
            vc, vb = signe * r["valeur"], float(b.loc[an])
            lignes.append({
                "annee": int(an), "objet": lib, "operation": op, "secteur": sec,
                "valeur_comptes": round(vc, 1), "edition_comptes": r["edition"],
                "serie_budget": serie, "source_budget": src.loc[an], "valeur_budget": round(vb, 1),
                "ecart": round(vc - vb, 1), "ecart_pct": round(100 * (vc - vb) / vb, 1) if vb else None,
                "perimetre_comptes": per_c, "perimetre_budget": per_b,
            })
    out = pd.DataFrame(lignes).sort_values(["objet", "annee"])
    out.to_csv(CACHE / "cnat-recoupements.csv", index=False)
    sp = CACHE / "catalog.snapshot.yml"
    cat = {e["id"]: e for e in (yaml.safe_load(sp.read_text("utf-8")) or [])}
    cat["cnat-recoupements"] = {
        "id": "cnat-recoupements",
        "titre": "Comptes des administrations publiques face aux séries budgétaires de l'État "
                 "(TVA, douane, impôts sur le revenu, compensation, rémunérations, équipement)",
        "sources": ["ins-cnat-2015"],
        "source_ligne": "Comparaison, année par année, de la série cnat-secteurs (INS) et des séries "
                        "budgétaires du cache (ministère des Finances) ; écart = comptes − budget, "
                        "périmètres déclarés paire par paire.",
        "unite": "millions de dinars courants",
    }
    sp.write_text(yaml.safe_dump(list(cat.values()), allow_unicode=True, sort_keys=False),
                  encoding="utf-8")
    print(out.groupby("objet").agg(annees=("annee", lambda s: f"{s.min()}-{s.max()}"),
                                   ecart_pct_median=("ecart_pct", "median")).to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())

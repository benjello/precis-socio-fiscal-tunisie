#!/usr/bin/env python3
"""Engendre `cnat-secteurs` et `cnat-secteurs-controles` : les comptes des secteurs institutionnels,
emplois et ressources, et leurs contrôles arithmétiques.

Lit, dans l'entrepôt tunisia-data (`data/processed/ins-comptes-nationaux/`) :
  - `cnat_secteurs.csv` : une ligne par (édition, secteur, côté, compte, opération, année), valeurs
    lues dans les « Comptes de la nation » de l'INS (éditions en base 2015), jamais calculées ;
  - `cnat_secteurs_controles.csv` : équilibre des opérations entre secteurs, soldes recalculés,
    consolidation des sous-secteurs et PIB, au seuil de 0,5 MD, écarts expliqués.

Écrit dans `precis/_seriescache/` :
  - `cnat-secteurs.csv` : pour chaque (secteur, côté, opération, libellé, année), la valeur de
    l'édition la plus récente qui la porte, avec son édition et son statut (définitif,
    semi-définitif, provisoire) ;
  - `cnat-secteurs-controles.csv` : les contrôles, toutes éditions.

Le dossier de l'entrepôt se donne par la variable `TUNISIA_DATA` (racine du dépôt), par défaut
`~/projets/tunisia-data`. À lancer en développement (entrepôt présent), puis committer le cache.

Usage : TUNISIA_DATA=… uv run python scripts/generate_cnat_secteurs.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pandas as pd
import yaml

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "precis" / "_seriescache"
ENTREPOT = Path(os.environ.get("TUNISIA_DATA", Path.home() / "projets" / "tunisia-data"))
SOURCE = ENTREPOT / "data" / "processed" / "ins-comptes-nationaux"

COLONNES = ["base", "edition", "secteur", "cote", "compte", "operation", "code_scn2008",
            "libelle_ins", "sous_ligne", "annee", "valeur", "statut_annee", "lecture"]


def main() -> int:
    s = pd.read_csv(SOURCE / "cnat_secteurs.csv", dtype={"edition": str, "base": str})
    c = pd.read_csv(SOURCE / "cnat_secteurs_controles.csv", dtype={"edition": str})
    if (c["statut"] == "echec").any():
        print("[cnat-secteurs] contrôles en échec dans l'entrepôt : génération refusée")
        print(c[c["statut"] == "echec"].head(20).to_string())
        return 1
    s = s.rename(columns={"valeur_md": "valeur"})
    # édition la plus récente pour chaque case ; les éditions « AAAA-AAAA » se trient par leur fin
    s["_fin"] = s["edition"].str[-4:].astype(int)
    s = s.sort_values("_fin").drop_duplicates(
        ["secteur", "cote", "operation", "libelle_ins", "annee"], keep="last")
    s = s.sort_values(["secteur", "cote", "compte", "operation", "annee"])[COLONNES]
    s["valeur"] = s["valeur"].round(1)
    s.to_csv(CACHE / "cnat-secteurs.csv", index=False)
    c.to_csv(CACHE / "cnat-secteurs-controles.csv", index=False)

    sp = CACHE / "catalog.snapshot.yml"
    cat = {e["id"]: e for e in (yaml.safe_load(sp.read_text("utf-8")) or [])}
    cat["cnat-secteurs"] = {
        "id": "cnat-secteurs",
        "titre": "Comptes des secteurs et sous-secteurs institutionnels, emplois et ressources "
                 "(INS, comptes de la nation, base 2015)",
        "sources": ["ins-cnat-2015"],
        "source_ligne": "INS, Les comptes de la nation, éditions 2015-2020 à 2021-2025 : comptes "
                        "des sociétés non financières, des sociétés financières (institutions de "
                        "crédit, assurances, auxiliaires), des administrations publiques "
                        "(administration centrale, collectivités locales, sécurité sociale), des "
                        "ménages (dont entreprises individuelles) et du reste du monde, emplois et "
                        "ressources ; pour chaque année, l'édition la plus récente.",
        "unite": "millions de dinars courants",
    }
    cat["cnat-secteurs-controles"] = {
        "id": "cnat-secteurs-controles",
        "titre": "Contrôles arithmétiques des comptes des secteurs institutionnels (équilibre des "
                 "opérations, soldes, consolidation, PIB)",
        "sources": ["ins-cnat-2015"],
        "source_ligne": "Calculs sur les comptes des secteurs de l'INS (éditions en base 2015), "
                        "seuil 0,5 MD ; écarts expliqués ligne par ligne.",
        "unite": "millions de dinars courants",
    }
    sp.write_text(yaml.safe_dump(list(cat.values()), allow_unicode=True, sort_keys=False),
                  encoding="utf-8")
    print(f"[cnat-secteurs] {len(s)} lignes, secteurs {sorted(s.secteur.unique())}, "
          f"années {s.annee.min()}-{s.annee.max()} ; {len(c)} contrôles, "
          f"{(c.statut == 'explique').sum()} écarts expliqués, 0 échec")
    return 0


if __name__ == "__main__":
    sys.exit(main())

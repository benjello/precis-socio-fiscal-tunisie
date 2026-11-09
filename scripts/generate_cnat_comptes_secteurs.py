#!/usr/bin/env python3
"""Engendre `cnat-comptes-secteurs` : la séquence des comptes par secteur institutionnel.

Série snapshotée dans `precis/_seriescache/`, lue par `figtools.series()`, pour la section
« Les comptes par secteur » de `precis/fr/annexe-comptes-nation.qmd`. Une ligne par
(secteur, indicateur, année, base), en millions de dinars courants.

Secteurs (convention tunisienne SCNT, quatre secteurs résidents + reste du monde) :
  - SNF, SF, Ménages, Reste du monde : comptes consolidés de l'INS
    (`tunisia-data/.../cnat-consolide/comptes-des-*.csv`, en niveaux, toutes éditions) ;
  - APU **consolidée** (administration centrale + collectivités locales + sécurité sociale) :
    table emplois par édition (094 base 2015 ; 100 base 1997), comme `budget-comptanat-apu`.
    Le sous-secteur « organismes de sécurité sociale » des comptes consolidés n'est PAS repris
    ici (il ferait doublon avec l'APU consolidée).

RÈGLES :
  - niveaux directs de l'INS ; les **soldes** de chaque compte (valeur ajoutée, revenu
    d'exploitation, solde des revenus primaires, revenu disponible, épargne, capacité/besoin de
    financement) sont des **lignes lues**, jamais recalculées ;
  - **édition la plus récente** portant l'(année, secteur, indicateur) ; base étiquetée,
    **bases jamais chaînées** (rupture 1997→2015) ;
  - à lancer EN DEV (entrepôt présent) puis committer `precis/_seriescache/`.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import pandas as pd
import yaml

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "precis" / "_seriescache"
CNAT = Path.home() / "projets" / "tunisia-data" / "data" / "processed" / "ins-comptes-nationaux"
CONSOLIDE = CNAT / "cnat-consolide"

# secteur → fichier consolidé (niveaux). APU traité à part (tables par édition).
FICHIERS = {
    "snf": "comptes-des-societes-non-financieres-s-n-f.csv",
    "sf": "comptes-des-societes-financieres-s-f.csv",
    "menages": "comptes-des-menages.csv",
    "exterieur": "compte-des-o-p-e-r-at-i-o-n-s-avec-l-e-x-t-e-r-i-e-u-r.csv",
}
# APU : (dossier édition, table emplois), de la plus récente à la plus ancienne, par base.
APU_EDITIONS = {
    "2015": [("cnat-2020-2024-tables", "094"), ("cnat_2019-2023-tables", "094"),
             ("cnat_2018-2022-tables", "094"), ("cnat_2017-2021-tables", "094")],
    "1997": [("cnat_2013-2017-tables", "100"), ("cnat_2012-2016-tables", "100")],
}
# édition → base (pour étiqueter les fichiers consolidés)
BASE_EDITION = {
    "cnat_2012-2016-tables": "1997", "cnat_2013-2017-tables": "1997",
    "cnat_vola_2015-2020-tables": "2015", "cnat_2017-2021-tables": "2015",
    "cnat_2018-2022-tables": "2015", "cnat_2019-2023-tables": "2015",
    "cnat-2020-2024-tables": "2015",
}


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", s).strip().lower()


def _num(v) -> float:
    if pd.isna(v):
        return float("nan")
    return float(str(v).replace("\u202f", "").replace(" ", "").replace(",", "."))


def _consolide(secteur: str, fichier: str) -> pd.DataFrame:
    d = pd.read_csv(CONSOLIDE / fichier)
    d["indicateur"] = d["indicateur"].map(_norm)
    d["valeur"] = d["valeur"].map(_num)
    d["base_pib"] = d["edition"].map(BASE_EDITION)
    d["secteur"] = secteur
    # édition la plus récente par (indicateur, annee, base)
    d = d.sort_values("edition").drop_duplicates(["indicateur", "annee", "base_pib"], keep="last")
    return d[["secteur", "indicateur", "annee", "base_pib", "valeur", "edition"]]


def _apu() -> pd.DataFrame:
    lignes = []
    for base, editions in APU_EDITIONS.items():
        vus = set()
        for edir, num in editions:
            g = [p for p in (CNAT / edir).glob(f"{num}__*.csv") if ".header" not in p.name]
            if not g:
                continue
            emp = pd.read_csv(g[0])
            emp["_k"] = emp.iloc[:, 0].map(_norm)
            annees = [c for c in emp.columns if str(c).isdigit()]
            for col in annees:
                an = int(col)
                if an in vus:
                    continue
                sous = emp[["_k", col]].dropna()
                if sous.empty:
                    continue
                vus.add(an)
                for _, r in sous.iterrows():
                    lignes.append({"secteur": "apu", "indicateur": r["_k"], "annee": an,
                                   "base_pib": base, "valeur": _num(r[col]), "edition": edir})
    return pd.DataFrame(lignes)


# Extension 2005-2011 (base 1997) extraite des PDF INS par pdftotext, validée par
# chevauchement 2012-2016 (0 écart snf/sf/apu/exterieur). Voir docs/notes/
# cnat-secteurs-2001-2011-extrait.md. Les ménages y sont CORRECTS (compte complet), là où
# la série courante 2012+ est buggée (collision ménages / entreprises individuelles en amont).
EXTRAIT = RACINE / "docs" / "notes" / "cnat-secteurs-2001-2011-extrait.csv"


def _extension_pdf() -> pd.DataFrame:
    if not EXTRAIT.exists():
        return pd.DataFrame()
    d = pd.read_csv(EXTRAIT)
    d["base_pib"] = d["base_pib"].astype(str)
    d["indicateur"] = d["indicateur"].map(_norm)
    return d[["secteur", "indicateur", "annee", "base_pib", "valeur", "edition"]]


def main() -> None:
    parts = [_consolide(sec, f) for sec, f in FICHIERS.items()]
    parts.append(_apu())
    parts.append(_extension_pdf())
    df = pd.concat([p for p in parts if not p.empty], ignore_index=True)
    df = df.dropna(subset=["valeur"])
    # une seule valeur par (secteur, indicateur, annee, base) : édition la plus récente
    df = df.sort_values("edition").drop_duplicates(
        ["secteur", "indicateur", "annee", "base_pib"], keep="last")
    df = df.sort_values(["base_pib", "secteur", "indicateur", "annee"])
    df["valeur"] = df["valeur"].round(1)
    df.to_csv(CACHE / "cnat-comptes-secteurs.csv", index=False)

    sp = CACHE / "catalog.snapshot.yml"
    existing = {e["id"]: e for e in (yaml.safe_load(sp.read_text("utf-8")) or [])}
    existing["cnat-comptes-secteurs"] = {
        "id": "cnat-comptes-secteurs",
        "titre": "Séquence des comptes par secteur institutionnel (INS, comptes de la nation)",
        "sources": ["ins-cnat-2015"],
        "source_ligne": "INS, comptes de la nation, comptes des secteurs institutionnels "
                        "(sociétés non financières, financières, ménages, administrations "
                        "publiques, reste du monde), bases 1997 et 2015.",
    }
    sp.write_text(yaml.safe_dump(list(existing.values()), allow_unicode=True, sort_keys=False),
                  encoding="utf-8")
    n_sec = df["secteur"].nunique()
    print(f"[cnat-comptes-secteurs] {len(df)} lignes, {n_sec} secteurs, "
          f"années base 2015 : {sorted(df[df.base_pib=='2015'].annee.unique())}")


if __name__ == "__main__":
    main()

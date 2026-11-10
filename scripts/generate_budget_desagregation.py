#!/usr/bin/env python3
"""Engendre les séries de la désagrégation du budget de l'État (annexe `annexe-budget-etat`).

Deux séries snapshotées dans `precis/_seriescache/`, lues ensuite par `figtools.series()` :

  - `budget-desagregation-nature` : les dépenses de l'État RÉALISÉES, hors service de la dette,
    ventilées par nature (rémunérations / moyens / interventions / équipement / prêts), 1986-2025.
    Source : ministère des Finances, « répartition économique des dépenses »
    (`repartition_depenses.xls` de l'entrepôt). La somme des natures boucle sur le Total hors dette
    (contrôle en fin de script) ; ce Total égale la série réalisée de `denominateurs-depenses-etat-pib`.

  - `budget-dispositifs-poids` : l'overlay des dispositifs examinés par le précis (masse salariale,
    compensation, transferts aux EP, transferts aux caisses, dotation FCCL), une ligne par
    (année, dispositif), avec le rattachement budgétaire, un drapeau `transversal` (le dispositif
    traverse plusieurs natures et n'entre pas dans la partition), la série et le filtre d'origine,
    et les parts (de sa ligne de rattachement, du total).

ATTENTION (voir docs/notes/annexe-budget-desagregation.md) :
  - les dispositifs NE s'emboîtent PAS proprement : compensation ⊂ interventions, mais transferts EP
    et caisses TRAVERSENT rémunérations/interventions/équipement et SE CHEVAUCHENT (compensation
    carburants via la STIR, caisses dans la même annexe 8 que les EP) → `transversal=True`, jamais
    sommés au total ;
  - à lancer EN DEV (entrepôt `tunisia-data` présent), puis committer `precis/_seriescache/`. Le
    build du site est autonome et ne lit que le CSV snapshoté.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import yaml

import re
import unicodedata

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "precis" / "_seriescache"
TD = Path.home() / "projets" / "tunisia-data" / "data"
XLS = TD / "raw" / "minfinances" / "repartition_depenses.xls"
FCCL_XLS = TD / "raw" / "finances_locales" / "dgct_portail" / "fccl.xls"
CNAT = TD / "processed" / "ins-comptes-nationaux"

# nature (rubrique du fichier minfin) → clé de série
NATURES = {
    "Rémunérations Publiques": "remunerations_MDT",
    "Moyens des Services": "moyens_MDT",
    "Interventions Publiques": "interventions_MDT",
    "Dépenses d'Equipement": "equipement_MDT",
    "Prêts": "prets_MDT",
    "Total": "total_hors_dette_MDT",
}


def _repartition() -> pd.DataFrame:
    """Lit le classeur minfin et renvoie la ventilation par nature, colonnes réalisées seules."""
    raw = pd.read_excel(XLS, sheet_name=0, header=None, engine="xlrd")
    hdr = raw.iloc[8, 2:].tolist()
    cols = {int(h): 2 + j for j, h in enumerate(hdr)
            if isinstance(h, (int, float)) and pd.notna(h)}  # en-tête numérique = année réalisée

    def ligne(libelle: str) -> dict:
        for i in range(9, raw.shape[0]):
            if str(raw.iloc[i, 1]).strip() == libelle:
                return {an: raw.iloc[i, c] for an, c in cols.items()}
        return {}

    data = {cle: ligne(lib) for lib, cle in NATURES.items()}
    df = pd.DataFrame(data)
    df.index.name = "annee"
    return df.reset_index().sort_values("annee")


def serie_nature() -> pd.DataFrame:
    df = _repartition()
    # contrôle de bouclage : Fonctionnement(=rémun+moyens+interv) + équipement + prêts == total
    parts = df[["remunerations_MDT", "moyens_MDT", "interventions_MDT",
                "equipement_MDT", "prets_MDT"]].sum(axis=1, min_count=1)
    # avant 1996, rémun/moyens/interv sont partiels → on ne contrôle que les années complètes
    complet = df["moyens_MDT"].notna() & df["interventions_MDT"].notna()
    ecart = (df["total_hors_dette_MDT"] - parts).abs()
    pire = ecart[complet].max()
    if pire > 0.6:
        raise SystemExit(f"[budget-desagregation] bouclage rompu : écart max {pire:.3f} MDT")
    print(f"[budget-desagregation-nature] bouclage OK (écart max {pire:.3f} MDT sur années complètes)")
    return df


def _compensation() -> pd.Series:
    cp = pd.read_csv(CACHE / "compensation-parts.csv")
    s = cp[(cp.famille == "budget") & (cp.nature == "budgetaire") & (cp.poste == "total")]
    return s.groupby("annee")["valeur_MDT"].sum()


def _transferts_ep() -> pd.Series:
    ep = pd.read_csv(CACHE / "entreprises-publiques-transferts-budget.csv")
    s = ep[(ep.etat == "réalisations") & (ep.ventilation == "nature")
           & (ep.cle == "total") & (ep.derniere_edition == True)]  # noqa: E712
    return s.groupby("annee")["valeur_md"].sum()


def _caisses() -> pd.Series:
    d = pd.read_csv(CACHE / "entreprises-publiques-transferts-par-etablissement.csv")
    s = d[(d.grandeur == "caisses") & (d.etat == "réalisations")]
    return s.groupby("annee")["valeur_md"].sum()


def _fccl() -> pd.Series:
    """Crédit global annuel du FCCL distribué par la DGCT, 2008-2019 (grandeur administrative)."""
    if not FCCL_XLS.exists():
        print("[budget-dispositifs-poids] fccl.xls absent — FCCL omis", file=sys.stderr)
        return pd.Series(dtype=float)
    raw = pd.read_excel(FCCL_XLS, sheet_name="fccl", header=None, engine="xlrd")
    out = {}
    for i in range(raw.shape[0]):
        a = raw.iloc[i, 0]
        if isinstance(a, (int, float)) and pd.notna(a) and 2000 <= int(a) <= 2030:
            # 1re colonne numérique après l'année = crédit global
            vals = [v for v in raw.iloc[i, 1:].tolist() if isinstance(v, (int, float)) and pd.notna(v)]
            if vals:
                out[int(a)] = float(vals[0])
    return pd.Series(out)


# dispositif → (série, rattachement budgétaire, transversal, source_serie, filtre, cle_csl)
DISPOSITIFS = {
    "masse_salariale": ("remunerations_MDT", "remunerations", False,
                        "repartition_depenses (1.1)", "rubrique 1.1", None),
    "compensation": ("_comp", "interventions", False,
                     "compensation-parts", "famille=budget,nature=budgetaire,poste=total",
                     None),
    "transferts_ep": ("_ep", "transversal (1.1/1.3/2)", True,
                      "entreprises-publiques-transferts-budget",
                      "etat=réalisations,ventilation=nature,cle=total,derniere_edition=True",
                      "minfin-transferts-garanties"),
    "transferts_caisses": ("_caisses", "transversal (⊂ transferts EP)", True,
                           "entreprises-publiques-transferts-par-etablissement",
                           "grandeur=caisses,etat=réalisations", "minfin-transferts-garanties"),
    "dotation_fccl": ("_fccl", "interventions (transferts APU locales)", False,
                      "dgct_portail/fccl.xls (crédit global, administratif)",
                      "feuille fccl, crédit global 2008-2019", "dgct-donnees-ouvertes"),
}


def serie_dispositifs(nat: pd.DataFrame) -> pd.DataFrame:
    nat = nat.set_index("annee")
    sources = {
        "remunerations_MDT": nat["remunerations_MDT"],
        "_comp": _compensation(), "_ep": _transferts_ep(),
        "_caisses": _caisses(), "_fccl": _fccl(),
    }
    lignes = []
    for disp, (src, rattach, transv, ssrc, filt, csl) in DISPOSITIFS.items():
        serie = sources[src]
        for an, val in serie.dropna().items():
            an = int(an)
            if an not in nat.index:
                continue
            ligne_ratt = nat.loc[an, "remunerations_MDT"] if rattach == "remunerations" else (
                nat.loc[an, "interventions_MDT"] if rattach.startswith("interventions") else None)
            total = nat.loc[an, "total_hors_dette_MDT"]
            lignes.append({
                "annee": an, "dispositif": disp, "valeur_MDT": round(float(val), 3),
                "rattachement": rattach, "transversal": transv,
                "part_ligne_pct": round(100 * val / ligne_ratt, 2) if ligne_ratt and pd.notna(ligne_ratt) else "",
                "part_total_pct": round(100 * val / total, 2) if pd.notna(total) else "",
                "source_serie": ssrc, "filtre": filt, "cle_csl": csl or "",
            })
    return pd.DataFrame(lignes).sort_values(["dispositif", "annee"])


PROV = [
    {"id": "budget-desagregation-nature",
     "titre": "Dépenses de l'État réalisées hors dette, par nature (1986-2025)",
     "sources": ["minfin-repartition-depenses-xls"],
     "source_ligne": "Ministère des Finances, répartition économique des dépenses de l'État "
                     "(réalisations, hors service de la dette)."},
    {"id": "budget-dispositifs-poids",
     "titre": "Poids annuel des dispositifs du précis dans les dépenses de l'État",
     "sources": ["minfin-repartition-depenses-xls", "minfin-transferts-garanties",
                 "dgct-donnees-ouvertes"],
     "source_ligne": "Ministère des Finances (répartition des dépenses ; annexe 8 des transferts) "
                     "et DGCT (dotation FCCL)."},
    {"id": "budget-comptanat-apu",
     "titre": "Compte des administrations publiques, emplois par nature économique (INS)",
     "sources": ["ins-cnat-2015"],
     "source_ligne": "INS, comptes de la nation, compte des administrations publiques (APU), "
                     "emplois et ressources, bases 1997 et 2015."},
]


# --- vue comptes de la nation : compte des administrations publiques (APU) --------
# Éditions OCRisées du compte APU, de la PLUS RÉCENTE à la plus ancienne, par base PIB.
# (table emplois, table ressources) ; voir docs/notes/annexe-budget-desagregation.md §3.
EDITIONS_APU = {
    "2015": [("cnat-2020-2024-tables", "094", "095"), ("cnat_2019-2023-tables", "094", "095"),
             ("cnat_2018-2022-tables", "094", "095"), ("cnat_2017-2021-tables", "094", "095")],
    "1997": [("cnat_2013-2017-tables", "100", "101"), ("cnat_2012-2016-tables", "100", "101")],
}
# nature → libellé normalisé EXACT de la ligne (emplois, sauf subventions = ressources)
_EMPLOIS = {
    "remuneration_salaries_MDT": "remuneration des salaries",
    "conso_intermediaire_MDT": "consommation intermediaire",
    "prestations_sociales_MDT": "prestations sociales en espece",
    "autres_transferts_courants_MDT": "autres transferts courants",
    "fbcf_MDT": "formation brute de capitale fixe",
    "interets_MDT": "interets",
    "transferts_capital_MDT": "transferts en capital",
}
_RESSOURCES = {  # lues en ressources (valeurs négatives) → signe inversé
    "subventions_MDT": "subventions",
    "subventions_produits_MDT": "subventions sur les produits",
}


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", s).strip().lower()


def _num(v) -> float:
    if pd.isna(v):
        return float("nan")
    return float(str(v).replace("\u202f", "").replace(" ", "").replace(",", "."))


def _table(edition: str, num: str) -> pd.DataFrame | None:
    g = [p for p in (CNAT / edition).glob(f"{num}__*.csv") if ".header" not in p.name]
    if not g:
        return None
    d = pd.read_csv(g[0])
    d["_k"] = d.iloc[:, 0].map(_norm)
    return d


def _ligne(d: pd.DataFrame, cle_norm: str, annee: int) -> float:
    row = d[d["_k"] == cle_norm]
    col = str(annee)
    if row.empty or col not in d.columns:
        return float("nan")
    return _num(row.iloc[0][col])


def serie_comptanat() -> pd.DataFrame:
    lignes = []
    for base, editions in EDITIONS_APU.items():
        vus = set()
        for edir, nem, nres in editions:
            emp = _table(edir, nem)
            res = _table(edir, nres)
            if emp is None:
                continue
            annees = [int(c) for c in emp.columns if str(c).isdigit()]
            for an in sorted(annees):
                if an in vus:  # édition plus récente déjà prise pour cette année
                    continue
                rec = {"annee": an, "base_pib": base, "edition": edir}
                for cle, lab in _EMPLOIS.items():
                    rec[cle] = round(_ligne(emp, lab, an), 1)
                if res is not None:
                    for cle, lab in _RESSOURCES.items():
                        v = _ligne(res, lab, an)
                        rec[cle] = round(-v, 1) if pd.notna(v) else ""  # signe inversé (dépense)
                # on ne retient l'année que si la rémunération est lue (garde-fou OCR tronqué)
                if pd.notna(rec["remuneration_salaries_MDT"]):
                    lignes.append(rec)
                    vus.add(an)
    df = pd.DataFrame(lignes).sort_values(["base_pib", "annee"])
    print(f"[budget-comptanat-apu] {len(df)} années "
          f"(base 1997 : {sorted(df[df.base_pib=='1997'].annee)} ; "
          f"base 2015 : {sorted(df[df.base_pib=='2015'].annee)})")
    return df


def _maj_snapshot() -> None:
    sp = CACHE / "catalog.snapshot.yml"
    existing = {e["id"]: e for e in (yaml.safe_load(sp.read_text("utf-8")) or [])}
    for e in PROV:
        existing[e["id"]] = e
    sp.write_text(yaml.safe_dump(list(existing.values()), allow_unicode=True, sort_keys=False),
                  encoding="utf-8")


def main() -> None:
    nat = serie_nature()
    nat.to_csv(CACHE / "budget-desagregation-nature.csv", index=False)
    disp = serie_dispositifs(nat)
    disp.to_csv(CACHE / "budget-dispositifs-poids.csv", index=False)
    apu = serie_comptanat()
    apu.to_csv(CACHE / "budget-comptanat-apu.csv", index=False)
    _maj_snapshot()
    print(f"[budget-desagregation-nature] {len(nat)} années → {CACHE/'budget-desagregation-nature.csv'}")
    print(f"[budget-dispositifs-poids] {len(disp)} lignes, "
          f"{disp['dispositif'].nunique()} dispositifs → {CACHE/'budget-dispositifs-poids.csv'}")


if __name__ == "__main__":
    main()

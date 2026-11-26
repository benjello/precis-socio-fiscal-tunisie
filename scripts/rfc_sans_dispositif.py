"""Annexe de la RFC 0001 : les opérations des comptes qu'aucun dispositif ne raconte.

Quatre familles (imputées, soldes et résidus, fourre-tout, faible contenu). Pour chaque opération :
code du SCN 2008, montant 2020 et 2023 (somme des secteurs résidents, emplois, sinon ressources),
part du compte au même côté, ou « non publié » quand l'inventaire des tableaux de l'INS ne la
contient pas (recherche citée). Puis, par secteur résident, la part de ses montants que ces
opérations représentent.

Montants : comptes des secteurs de l'INS (cache `cnat-secteurs`), édition la plus récente où l'année
est définitive (2020 : éd. 2020-2024 ; 2023 : éd. 2021-2025). Trois opérations hors des comptes des
secteurs sont relevées dans le tableau d'ensemble de l'INS, page citée (RELEVES).

    uv run python scripts/rfc_sans_dispositif.py

Sorties : docs/rfc/operations-sans-dispositif.md, docs/rfc/operations-sans-dispositif.csv.
"""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

CACHE = Path("precis/_seriescache/cnat-secteurs.csv")
RFC = Path("docs/rfc")
ANNEES = {2020: "2020-2024", 2023: "2021-2025"}
RESIDENTS = ("snf", "sf", "apu", "menages")
NOM_SECTEUR = {"snf": "sociétés non financières", "sf": "sociétés financières",
               "apu": "administrations publiques", "menages": "ménages"}

# Relevés dans les tableaux d'ensemble de l'INS (comptes de la nation, éd. 2020-2024 et 2021-2025).
RELEVES = {
    "P.51c": ({2020: 14517.8, 2023: 16164.5}, "« Amortissements », tableau « Revenu national », p. 30"),
    "D.122/D.612": ({2020: 1001.3, 2023: 1692.3}, "« Cotisations sociales imputées », tableau « Opérations agrégées (suite) », p. 36"),
    "B.7g": ({2020: 122429.7, 2023: 156421.1}, "tableau économique d'ensemble, p. 116-117 (2020) et 120-121 (2023)"),
}
NON_PUBLIE = {
    "loyers": "le terme n'apparaît que dans le texte de méthode (p. 16 des éd. 2020-2024 et 2021-2025), sans montant",
    "D.8": "aucune occurrence dans les six éditions en base 2015 ; « D8 » n'apparaît que dans la nomenclature des éditions 2005-2009 à 2007-2011",
    "K": "non publiés : les comptes de patrimoine financiers donnent les encours 2014-2020 et les flux 2015-2020 (Comptes de la nation 2015-2020, vol. B, p. 14-25 et 28-41), d'où l'on ne tire que la somme des réévaluations et des autres changements de volume, par différence ; rien pour les actifs non financiers",
}

# famille, code, libellé, clé (operation du cache, code de relevé ou de non-publication), difficulté
OPERATIONS = [
    ("Imputées", "P.1 (dont)", "Loyers imputés des propriétaires occupants", "loyers",
     "production sans transaction, estimée par un loyer de marché"),
    ("Imputées", "P.119", "Production de SIFIM", "production_sifim",
     "marge d'intérêt imputée, répartie entre utilisateurs par convention"),
    ("Imputées", "D.41 (dont)", "Correction SIFIM des intérêts", "correction_sifim",
     "contrepartie de la précédente dans les intérêts"),
    ("Imputées", "P.51c", "Consommation de capital fixe", "P.51c",
     "estimée par inventaire permanent, sans source administrative"),
    ("Imputées", "D.122/D.612", "Cotisations sociales imputées", "D.122/D.612",
     "contrepartie des prestations versées directement par l'employeur"),
    ("Imputées", "D.44", "Revenus de la propriété attribués aux assurés", "revenus_propriete_assures",
     "revenu des placements des assureurs, réputé reversé"),
    ("Imputées", "D.8", "Ajustement pour variation des droits à pension", "D.8",
     "propre aux régimes par capitalisation"),
    ("Soldes et résidus", "B.2g/B.3g", "Excédent d'exploitation et revenu mixte", "revenu_exploitation",
     "solde du compte d'exploitation, sans source propre"),
    ("Soldes et résidus", "P.52", "Variation de stocks", "variation_stocks",
     "souvent obtenue par solde de l'équilibre des produits"),
    ("Soldes et résidus", "F.8", "Autres comptes à recevoir ou à payer", "autres_comptes",
     "décalages entre droits constatés et paiements"),
    ("Soldes et résidus", "—", "Écart statistique", "ecart_statistique",
     "écart entre capacité de financement et solde financier"),
    ("Fourre-tout", "D.29", "Autres impôts sur la production", "autres_impots_production",
     "taxes diverses, rattachables texte par texte"),
    ("Fourre-tout", "D.39", "Subventions sur la production", "autres_subventions_production",
     "aides diverses, rattachables ligne par ligne"),
    ("Fourre-tout", "D.71", "Primes nettes d'assurance-dommages", "primes_assurance_dommages",
     "flux privés, connus par les comptes des assureurs"),
    ("Fourre-tout", "D.72", "Indemnités d'assurance-dommages", "indemnites_assurance_dommages",
     "idem"),
    ("Fourre-tout", "D.75", "Transferts courants divers", "transferts_courants_divers",
     "envois de fonds, dons, amendes : à décomposer"),
    ("Fourre-tout", "D.99", "Autres transferts en capital", "autres_transferts_capital",
     "annulations de dettes, apports : à décomposer"),
    ("Faible contenu", "B.7g", "Revenu disponible ajusté", "B.7g",
     "solde ; ne se distingue de B.6 que par les transferts en nature"),
    ("Faible contenu", "NP", "Acquisitions moins cessions d'actifs non produits", "actifs_non_produits",
     "terrains et droits, montants faibles"),
    ("Faible contenu", "K.3 à K.7", "Réévaluation et autres changements de volume", "K",
     "suppose des comptes de patrimoine"),
    ("Faible contenu", "F.1 à F.7", "Détail du compte financier par instrument", "F",
     "connu par les bilans bancaires, sans dispositif à décrire"),
]
F_DETAIL = {"or_dts", "numeraire_depots", "titres_creance", "credits", "actions_opc", "provisions_assurance", "produits_derives"}


def compte_norme(c: str) -> str:
    """Le compte de production des sociétés financières s'intitule « Production ou Compte extérieur… »."""
    return "Compte de production" if c.startswith("Production") else c


def sommets(lignes):
    """Lignes principales sans double compte : hors soldes et sous-lignes, une ligne dont le code a un
    ancêtre présent dans le même (secteur, compte, côté) est écartée (D.11 sous D.1, P.13 sous P.1),
    et entre lignes de même code on garde la plus grande (production et production marchande, P.1)."""
    g = defaultdict(list)
    for l in lignes:
        c = l["code_scn2008"]
        if l["sous_ligne"] == "0" and c and not c.startswith("B."):
            g[(l["secteur"], compte_norme(l["compte"]), l["cote"])].append(l)
    out = []
    for ls in g.values():
        codes = {l["code_scn2008"] for l in ls}
        ls = [l for l in ls if not any(o != l["code_scn2008"] and l["code_scn2008"].startswith(o) for o in codes)]
        par_code = defaultdict(list)
        for l in ls:
            par_code[l["code_scn2008"]].append(l)
        out += [max(v, key=lambda l: abs(float(l["valeur"]))) for v in par_code.values()]
    return out


def fr(v: float) -> str:
    return f"{v:,.1f}".replace(",", " ").replace(".", ",")


def main() -> int:
    cache = [l for l in csv.DictReader(CACHE.open(encoding="utf-8")) if str(l["base"]) == "2015"]
    lig = {an: [l for l in cache if l["edition"] == ed and int(l["annee"]) == an and l["secteur"] in RESIDENTS]
           for an, ed in ANNEES.items()}
    # total du compte, par (compte, côté), lignes principales hors soldes
    tot = {an: defaultdict(float) for an in ANNEES}
    for an, ls in lig.items():
        for l in sommets(ls):
            tot[an][(compte_norme(l["compte"]), l["cote"])] += abs(float(l["valeur"]))

    def montant(an, cle):
        if cle in RELEVES:
            return RELEVES[cle][0][an], None, RELEVES[cle][1]
        ops = F_DETAIL if cle == "F" else {cle}
        ls = [l for l in lig[an] if l["operation"] in ops]
        if not ls:
            return None, None, ""
        cote = "emplois" if any(l["cote"] == "emplois" for l in ls) else "ressources"
        ls = [l for l in ls if l["cote"] == cote]
        v = sum(float(l["valeur"]) for l in ls)
        comptes = {compte_norme(l["compte"]) for l in ls}
        t = sum(tot[an][(c, cote)] for c in comptes)
        part = abs(v) / t * 100 if t and not ls[0]["code_scn2008"].startswith("B.") else None
        return v, part, f"comptes des secteurs, {cote}"

    out_csv, md = [], []
    md.append("# Les opérations sans dispositif à raconter (engendré par `scripts/rfc_sans_dispositif.py`)\n")
    md.append("Montants en millions de dinars courants : somme des secteurs résidents (sociétés non financières, sociétés financières, "
              "administrations publiques, ménages), côté emplois, sinon ressources ; 2020 d'après l'éd. 2020-2024, 2023 d'après l'éd. 2021-2025 "
              "des comptes de la nation de l'INS, année définitive dans les deux cas. Part : part de l'opération dans le total du même compte "
              "et du même côté (lignes principales, hors soldes, sans double compte des composantes) ; un « dont » est rapporté au total de son compte. « Non publié » : "
              "absent de l'inventaire des 2 473 pages de tableaux des éditions de l'INS, recherche citée.\n")
    famille = None
    for fam, code, lib, cle, diff in OPERATIONS:
        if fam != famille:
            md.append(f"\n## {fam}\n\n| Code | Opération | 2020 | Part 2020 | 2023 | Part 2023 | Source | Difficulté |\n|---|---|--:|--:|--:|--:|---|---|")
            famille = fam
        if cle in NON_PUBLIE:
            marque = "non publié"
            cells, src = [marque, "", marque, ""], NON_PUBLIE[cle]
            row = {an: (None, None) for an in ANNEES}
        else:
            row, src = {}, ""
            for an in ANNEES:
                v, p, s = montant(an, cle)
                row[an] = (v, p)
                src = s or src
            cells = []
            for an in ANNEES:
                v, p = row[an]
                cells += [fr(v) if v is not None else "non publié", f"{fr(p)} %" if p is not None else ""]
        md.append(f"| {code} | {lib} | {' | '.join(cells)} | {src} | {diff} |")
        out_csv.append({"famille": fam, "code": code, "operation": lib,
                        **{f"montant_{an}": "" if (v := row[an][0]) is None else round(v, 1) for an in ANNEES},
                        **{f"part_{an}_pct": "" if (p := row[an][1]) is None else round(p, 1) for an in ANNEES},
                        "source": src, "difficulte": diff})

    # Part, par secteur, de ses montants que ces opérations représentent (opérations des comptes des secteurs, hors soldes).
    cles = {c for *_, c, _ in OPERATIONS if c not in RELEVES and c not in NON_PUBLIE and c != "revenu_exploitation"} | F_DETAIL
    cles.discard("F")
    md.append("\n## Poids par secteur\n")
    md.append("Somme des valeurs absolues des opérations ci-dessus présentes dans les comptes des secteurs (hors soldes et hors relevés), "
              "rapportée à la somme des valeurs absolues de toutes les opérations du secteur, emplois et ressources, lignes principales, hors soldes, sans double compte (une ligne dont le code a un ancêtre imprimé, D.11 sous D.1, est écartée). "
              "Un « dont » (SIFIM) est compté au numérateur seulement.\n")
    md.append("| Secteur | 2020 | 2023 | dont compte financier (F.1 à F.8), 2023 |\n|---|--:|--:|--:|")
    for s in RESIDENTS:
        cells = []
        for an in ANNEES:
            ls = [l for l in lig[an] if l["secteur"] == s]
            den = sum(abs(float(l["valeur"])) for l in sommets(ls))
            num = sum(abs(float(l["valeur"])) for l in ls if l["operation"] in cles)
            numf = sum(abs(float(l["valeur"])) for l in ls if l["operation"] in F_DETAIL | {"autres_comptes"})
            cells.append((num / den * 100 if den else 0, numf / den * 100 if den else 0))
        md.append(f"| {NOM_SECTEUR[s]} | {fr(cells[0][0])} % | {fr(cells[1][0])} % | {fr(cells[1][1])} % |")
    (RFC / "operations-sans-dispositif.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    with (RFC / "operations-sans-dispositif.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out_csv[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(out_csv)
    print(f"{len(out_csv)} opérations → {RFC}/operations-sans-dispositif.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

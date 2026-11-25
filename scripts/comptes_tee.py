"""Tableau économique d'ensemble (TEE) de l'INS, secteur par secteur : compte complet de chaque
secteur et contrôle des identités comptables, sur les valeurs publiées (lecture seule du cache,
rien n'est corrigé ni estimé).

Années : l'année de référence et les années secondaires de precis/fr/annee-reference.yml ; pour
chaque année, l'édition la plus récente des Comptes de la nation où elle est définitive.

Lecture du cache precis/_seriescache/cnat-tee.csv :
- une ligne imprimée du TEE = une page et une ordonnée (y0) ; ses cases sont les colonnes S11, S12,
  S13, S14, S1 (économie totale), S2 (reste du monde), BS (biens et services), TOTAL ;
- la ligne d'en-tête de page (« AGRÉGATS ET TABLEAUX D'ENSEMBLE … ») est écartée ;
- une ligne dont l'opération est vide (libellé coupé par l'extraction) est gardée, marquée
  « sans_libelle », et rapprochée, quand c'est possible, de la ligne des comptes de secteurs
  (cnat-secteurs.csv, même édition et même année) qui porte les mêmes valeurs dans tous les secteurs ;
  elle n'entre dans aucune identité ;
- dans une ligne imprimée, une case de secteur vide est lue comme zéro (le contrôle le dit).

Sorties :
- precis/fr/compte-secteurs-tee.csv : une ligne par case (année, ligne imprimée, colonne), avec les
  postes du registre precis/fr/postes-comptables.csv rattachés à l'opération ;
- precis/fr/compte-secteurs-tee-controles.csv : chaque identité, valeur publiée, valeur recalculée,
  résidu, statut (égal, égal aux arrondis près, écart, non calculable) et remarque.

    uv run python scripts/comptes_tee.py [--verifier]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
FR = RACINE / "precis" / "fr"
CACHE = RACINE / "precis" / "_seriescache"
SORTIE = FR / "compte-secteurs-tee.csv"
CONTROLES = FR / "compte-secteurs-tee-controles.csv"
COLONNES = ["S11", "S12", "S13", "S14", "S1", "S2", "BS", "TOTAL"]
SECTEURS = ["S11", "S12", "S13", "S14"]
SEQUENCE = SECTEURS + ["S1"]
# Codes du registre des postes -> colonnes du TEE (S13 : tout sous-secteur apu_*).
REGISTRE = {"snf": "S11", "sf": "S12", "menages": "S14", "rdm": "S2"}
CNAT_SECTEURS = {"snf": "S11", "sf": "S12", "apu": "S13", "menages": "S14"}
ARRONDI = 0.05  # demi-unité de la dernière décimale imprimée (0,1 MD), par terme


def fr(x: float) -> str:
    """Nombre à une décimale, à la française (texte des remarques)."""
    return f"{round(x, 1) + 0.0:,.1f}".replace(",", " ").replace(".", ",")


def lire(p: Path) -> list[dict]:
    with p.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def nature(op: str, code: str) -> str:
    if not op:
        return "sans_libelle"
    if code.startswith("B."):
        return "solde"
    if re.fullmatch(r"F(\.\d)?", code) or op == "ecart_statistique":
        return "financier"
    if op == "interets":  # « dont Intérêts » : composante de D.4
        return "dont"
    return "operation"


def editions(tee: list[dict], annees: list[int]) -> dict[int, str]:
    out = {}
    for an in annees:
        eds = sorted({l["edition"] for l in tee if int(l["annee"]) == an and l["statut_annee"] == "definitif"})
        if not eds:
            sys.exit(f"aucune édition où {an} est définitive dans cnat-tee.csv")
        out[an] = eds[-1]
    return out


def lignes_imprimees(tee: list[dict], an: int, ed: str) -> list[dict]:
    """Regroupe les cases du cache en lignes imprimées (page, côté, ordonnée)."""
    groupes: dict[tuple, dict] = {}
    for l in tee:
        if int(l["annee"]) != an or l["edition"] != ed:
            continue
        if l["libelle_ins"].upper().startswith("AGRÉGATS ET TABLEAUX"):
            continue
        k = (int(l["page_fichier"]), l["cote"], round(float(l["y0"]), 0))
        g = groupes.setdefault(k, {"page": int(l["page_fichier"]), "cote": l["cote"], "y0": float(l["y0"]),
                                   "libelle_ins": l["libelle_ins"], "operation": l["operation"],
                                   "code_scn": l["code_scn2008"], "cases": {}})
        if (g["operation"], g["code_scn"], g["libelle_ins"]) != (l["operation"], l["code_scn2008"], l["libelle_ins"]):
            sys.exit(f"ligne ambiguë page {k[0]} y0 {k[2]} : {g['libelle_ins']} / {l['libelle_ins']}")
        g["cases"][l["colonne"]] = float(l["valeur_md"])
    ls = sorted(groupes.values(), key=lambda g: (g["page"], g["cote"] != "emplois", g["y0"]))
    occ: dict[tuple, int] = {}
    for i, g in enumerate(ls, 1):
        g["rang"] = i
        g["nature"] = nature(g["operation"], g["code_scn"])
        k = (g["cote"], g["operation"])
        g["occurrence"] = occ.get(k, 0)
        occ[k] = g["occurrence"] + 1
    return ls


def rapprocher(g: dict, secteurs_cache: list[dict], an: int, ed: str) -> str:
    """Code SCN de la ligne des comptes de secteurs qui porte les mêmes valeurs (lignes sans libellé)."""
    cases = {c: v for c, v in g["cases"].items() if c in SECTEURS}
    if not cases:
        return ""
    cand: dict[tuple, dict] = {}
    for l in secteurs_cache:
        if l["edition"] == ed and int(l["annee"]) == an and l["cote"] == g["cote"] and l["secteur"] in CNAT_SECTEURS and l["code_scn2008"]:
            cand.setdefault((l["code_scn2008"], l["operation"]), {})[CNAT_SECTEURS[l["secteur"]]] = float(l["valeur"])
    ok = [k for k, v in cand.items() if all(abs(v.get(c, 1e18) - x) < 0.051 for c, x in cases.items())]
    codes = sorted({k[0] for k in ok})
    return codes[0] if len(codes) == 1 else ""


def composantes(code: str) -> list[str]:
    return [c for c in re.split(r"[-/]", code) if c]


def lien(pc: str, code: str) -> int:
    """Longueur du code du TEE qui couvre le code du poste (0 : aucun lien)."""
    return max((len(c) for c in composantes(code) if pc.startswith(c)), default=0)


def rattacher(g: dict, col: str, postes: list[dict], ls: list[dict]) -> tuple[list[str], list[str]]:
    """Postes du registre rattachés à une case : code égal (exact) ou plus fin (par code parent).

    Le secteur doit figurer du côté de l'opération (parmi ceux qui versent pour un emploi, qui
    reçoivent pour une ressource). Un poste ne va qu'à la ligne imprimée la plus fine qui le couvre
    du même côté : la TVA (D.211) va aux impôts sur les produits (D.21 − D.31), que le TEE n'inscrit
    à aucun secteur, et non à la ligne D.2 − D.3 des secteurs."""
    if g["nature"] not in ("operation", "dont") or (col not in REGISTRE.values() and col != "S13"):
        return [], []
    # Les transferts en capital à payer sont imprimés en ressources, en négatif : le secteur y paie.
    paie = g["cote"] == "emplois" or g["operation"] == "transferts_capital"
    cote = "secteur_verse" if paie else "secteur_recoit"
    codes = {x["code_scn"] for x in ls if x["cote"] == g["cote"] and x["nature"] in ("operation", "dont")}
    exacts, parents = [], []
    for p in postes:
        secs = [s for s in p[cote].split(";") if s]
        if not any(REGISTRE.get(s) == col or (col == "S13" and s.startswith("apu")) for s in secs):
            continue
        pc, n = p["code_scn"], lien(p["code_scn"], g["code_scn"])
        if not n or any(lien(pc, c) > n for c in codes):
            continue
        (exacts if pc in composantes(g["code_scn"]) else parents).append(p["poste"])
    return exacts, parents


class Annee:
    def __init__(self, an: int, ed: str, ls: list[dict]):
        self.an, self.ed, self.ls = an, ed, ls

    def ligne(self, cote: str, op: str, occ: int = 0) -> dict | None:
        return next((g for g in self.ls if g["cote"] == cote and g["operation"] == op and g["occurrence"] == occ), None)

    def sans_libelle(self, cote: str) -> list[str]:
        return [f"« {g['libelle_ins']} »" for g in self.ls if g["cote"] == cote and g["nature"] == "sans_libelle"]


def statut(residu: float, nterm: int) -> tuple[str, float]:
    tol = round(ARRONDI * nterm, 2)
    if residu == 0:
        return "égal", tol
    return ("égal aux arrondis près" if abs(residu) <= tol + 1e-9 else "écart"), tol


def controle(A: Annee, identite: str, secteur: str, formule: str, publie: tuple, termes: list[tuple], remarque: str = "") -> dict:
    """publie = (côté, opération[, occ]) ; termes = [(signe, côté, opération[, occ]), ...]."""
    base = {"annee": A.an, "edition": A.ed, "identite": identite, "secteur": secteur, "formule": formule}
    vides, manque = [], []

    def val(cote, op, occ=0):
        g = A.ligne(cote, op, occ)
        if g is None:
            manque.append(f"{op} ({cote})")
            return None
        if secteur not in g["cases"]:
            vides.append(g["code_scn"] or op)
            return 0.0
        return g["cases"][secteur]

    p = val(*publie)
    vs = [(t[0], val(*t[1:])) for t in termes]
    if manque:
        sl = A.sans_libelle(publie[0]) if publie[0] else []
        raison = "ligne absente du cache : " + ", ".join(manque)
        if sl:
            raison += " ; lignes sans libellé lisible du même tableau : " + ", ".join(sl)
        return {**base, "publie_md": "", "recalcule_md": "", "residu_md": "", "tolerance_md": "",
                "statut": "non calculable", "remarque": raison}
    r = round(sum(s * v for s, v in vs), 1) + 0.0
    res = round(r - p, 1) + 0.0
    st, tol = statut(res, len(termes) + 1)
    rq = [remarque] if remarque and st != "égal" else []
    if vides:
        rq.append("case vide lue comme zéro : " + ", ".join(dict.fromkeys(vides)))
    return {**base, "publie_md": p, "recalcule_md": r, "residu_md": res, "tolerance_md": tol,
            "statut": st, "remarque": " ; ".join(rq)}


def brut(A: Annee, identite: str, secteur: str, formule: str, publie, recalcule, nterm: int,
         remarque: str = "", raison: str = "") -> dict:
    base = {"annee": A.an, "edition": A.ed, "identite": identite, "secteur": secteur, "formule": formule}
    if publie is None or recalcule is None:
        return {**base, "publie_md": "", "recalcule_md": "", "residu_md": "", "tolerance_md": "",
                "statut": "non calculable", "remarque": raison}
    res = round(recalcule - publie, 1) + 0.0
    st, tol = statut(res, nterm)
    return {**base, "publie_md": round(publie, 1), "recalcule_md": round(recalcule, 1), "residu_md": res,
            "tolerance_md": tol, "statut": st, "remarque": remarque if st != "égal" else ""}


E, R = "emplois", "ressources"
SEQ = [
    ("B.1g = P.1 − P.2", (E, "valeur_ajoutee_brute"), [(1, R, "production"), (-1, E, "consommation_intermediaire")]),
    ("B.2g/B.3g = B.1g − D.1 − (D.29 − D.39)", (E, "revenu_exploitation"),
     [(1, E, "valeur_ajoutee_brute"), (-1, E, "remuneration_salaries"), (-1, E, "impots_nets_production")]),
    ("B.5g = B.2g/B.3g + D.1 reçus + (D.2 − D.3) reçus + D.4 reçus − D.4 versés", (E, "solde_revenus_primaires"),
     [(1, E, "revenu_exploitation"), (1, R, "remuneration_salaries"), (1, R, "impots_nets_production_importations"),
      (1, R, "revenus_propriete"), (-1, E, "revenus_propriete")]),
    ("B.6g = B.5g + (D.5 + D.61 + D.62 + D.7) reçus − (D.5 + D.61 + D.62 + D.7) versés", (E, "revenu_disponible_brut"),
     [(1, E, "solde_revenus_primaires")] + [(s, c, op) for op in ("impots_courants", "cotisations_sociales", "prestations_especes",
                                                                     "autres_transferts_courants") for s, c in ((1, R), (-1, E))]),
    ("B.7g = B.6g + D.63 reçus − D.63 versés", (E, "revenu_disponible_ajuste"),
     [(1, E, "revenu_disponible_brut"), (1, R, "transferts_sociaux_nature"), (-1, E, "transferts_sociaux_nature")]),
    ("B.8g = B.6g − P.3", (E, "epargne_brute"), [(1, E, "revenu_disponible_brut"), (-1, E, "consommation_finale")]),
    ("B.9 = B.8g + D.9 à recevoir + D.9 à payer (imprimés signés) − P.51g − P.52 − NP", (E, "capacite_financement"),
     [(1, E, "epargne_brute"), (1, R, "transferts_capital_a_recevoir"), (1, R, "transferts_capital"),
      (-1, E, "fbcf"), (-1, E, "variation_stocks"), (-1, E, "actifs_non_produits")]),
]


def controles(A: Annee) -> list[dict]:
    out = []
    # 1. Séquence des comptes, secteur par secteur.
    for formule, pub, termes in SEQ:
        ident = "séquence " + formule.split(" =")[0]
        for s in SEQUENCE:
            rq = "D.8 (ajustement pour variation des droits à pension) n'est pas imprimé ; P.4 non plus" if pub[1] == "epargne_brute" else ""
            out.append(controle(A, ident, s, formule, pub, termes, rq))
    # 2. Capacité de financement : compte financier et écart statistique.
    fin = [g for g in A.ls if re.fullmatch(r"F\.\d", g["code_scn"])]
    b9, b9f = A.ligne(E, "capacite_financement"), A.ligne(R, "solde_creances_dettes")
    ecarts = [g for g in A.ls if g["operation"] == "ecart_statistique"]
    for s in SEQUENCE + ["S2"]:
        if b9f is None or s not in b9f["cases"]:
            continue
        cre = sum(g["cases"].get(s, 0.0) for g in fin if g["cote"] == E)
        det = sum(g["cases"].get(s, 0.0) for g in fin if g["cote"] == R)
        out.append(brut(A, "B.9f = Σ F créances − Σ F dettes", s, "B.9f = Σ F.1…F.8 (emplois) − Σ F.1…F.8 (ressources)",
                        b9f["cases"][s], cre - det, len(fin) + 1))
        if b9 is not None and s in b9["cases"]:
            if s == "S1":
                ec = sum(g["cases"].get(x, 0.0) for g in ecarts for x in SECTEURS) if not any("S1" in g["cases"] for g in ecarts) \
                    else sum(g["cases"].get("S1", 0.0) for g in ecarts)
            else:
                ec = sum(g["cases"].get(s, 0.0) for g in ecarts)
            out.append(brut(A, "B.9 − B.9f = écart statistique", s, "B.9 (compte de capital) − B.9f (compte financier) = écart statistique imprimé",
                            ec, b9["cases"][s] - b9f["cases"][s], 3))
    for g, nom in ((b9, "B.9"), (b9f, "B.9f")):
        if g is not None and "S1" in g["cases"] and "S2" in g["cases"]:
            out.append(brut(A, f"{nom} S1 + S2 = 0", "S1+S2", f"{nom} de l'économie totale + {nom} du reste du monde = 0",
                            0.0, g["cases"]["S1"] + g["cases"]["S2"], 2))
    # 3. Somme des secteurs = économie totale, ligne par ligne.
    produits = {g["cote"]: g for g in A.ls if g["operation"] == "impots_nets_produits" and "S1" in g["cases"]
                and not any(c in g["cases"] for c in SECTEURS)}
    for g in A.ls:
        if g["nature"] == "sans_libelle":
            continue
        ident, lib = "S11 + S12 + S13 + S14 = S1", f"{g['code_scn'] or g['operation']} ({g['cote']}, ligne {g['rang']})"
        secs = [c for c in SECTEURS if c in g["cases"]]
        if "S1" not in g["cases"] and not secs:
            continue
        if "S1" not in g["cases"] and g["operation"] == "actifs_non_produits" and "S2" not in g["cases"]:
            out.append(brut(A, "NP : somme des secteurs = 0", lib,
                            "acquisitions moins cessions d'actifs non produits entre secteurs résidents (ni S1 ni S2 imprimés)",
                            0.0, sum(g["cases"][c] for c in secs), len(secs) + 1))
            continue
        if "S1" not in g["cases"]:
            out.append(brut(A, ident, lib, "somme des secteurs = économie totale", None, None, 0,
                            raison=f"pas de case S1 imprimée ; somme des secteurs {fr(sum(g['cases'][c] for c in secs))}"))
            continue
        if not secs:
            out.append(brut(A, ident, lib, "somme des secteurs = économie totale", None, None, 0,
                            raison="opération inscrite à la seule économie totale : aucune case de secteur imprimée"))
            continue
        rq = ""
        if g["operation"] == "impots_nets_production_importations" and g["cote"] in produits:
            p = produits[g["cote"]]["cases"]["S1"]
            if abs(g["cases"]["S1"] - sum(g["cases"][c] for c in secs) - p) < 0.051 * (len(secs) + 2):
                rq = f"résidu égal aux impôts nets sur les produits (D.21 − D.31) de l'économie totale, {fr(p)}, imprimés sans répartition par secteur"
        out.append(brut(A, ident, lib, "somme des secteurs = économie totale", g["cases"]["S1"],
                        sum(g["cases"][c] for c in secs), len(secs) + 1, rq))
    # 4. Total de la ligne = économie totale + reste du monde + biens et services.
    for g in A.ls:
        if g["nature"] == "sans_libelle" or "TOTAL" not in g["cases"]:
            continue
        lib = f"{g['code_scn'] or g['operation']} ({g['cote']}, ligne {g['rang']})"
        if "S1" in g["cases"]:
            parts, rq = [g["cases"]["S1"]], ""
        else:
            parts = [g["cases"][c] for c in SECTEURS if c in g["cases"]]
            rq = "pas de case S1 : somme des secteurs" if parts else ""
        parts += [g["cases"][c] for c in ("S2", "BS") if c in g["cases"]]
        out.append(brut(A, "TOTAL = S1 + S2 + BS", lib, "total de la ligne = économie totale + reste du monde + biens et services",
                        g["cases"]["TOTAL"], sum(parts), len(parts) + 1, rq))
    # 5. Emplois = ressources, opération par opération (colonne TOTAL).
    ops = []
    for g in A.ls:
        if g["nature"] in ("operation", "dont", "financier") and g["operation"] != "ecart_statistique" and g["operation"] not in ("transferts_capital_a_recevoir", "transferts_capital", "actifs_non_produits"):
            k = (g["operation"], g["occurrence"])
            if k not in ops:
                ops.append(k)
    for op, occ in ops:
        e, r = A.ligne(E, op, occ), A.ligne(R, op, occ)
        ref = e or r
        lib = f"{ref['code_scn']} {op}" + (f" (occurrence {occ + 1})" if occ else "")
        if e is None or r is None:
            cote_manque = E if e is None else R
            sl = A.sans_libelle(cote_manque)
            raison = f"pas de ligne {op} en {cote_manque} dans le cache"
            if sl:
                raison += " ; lignes sans libellé lisible de ce côté : " + ", ".join(sl)
            out.append(brut(A, "emplois = ressources (TOTAL)", lib, "TOTAL des emplois = TOTAL des ressources", None, None, 0, raison=raison))
            continue
        if "TOTAL" not in e["cases"] or "TOTAL" not in r["cases"]:
            out.append(brut(A, "emplois = ressources (TOTAL)", lib, "TOTAL des emplois = TOTAL des ressources", None, None, 0,
                            raison="pas de case TOTAL imprimée"))
            continue
        out.append(brut(A, "emplois = ressources (TOTAL)", lib, "TOTAL des emplois = TOTAL des ressources",
                        r["cases"]["TOTAL"], e["cases"]["TOTAL"], 2))
    d9r, d9p = A.ligne(R, "transferts_capital_a_recevoir"), A.ligne(R, "transferts_capital")
    if d9r and d9p and "TOTAL" in d9r["cases"] and "TOTAL" in d9p["cases"]:
        out.append(brut(A, "emplois = ressources (TOTAL)", "D.9 à recevoir et à payer",
                        "TOTAL des transferts en capital à recevoir + TOTAL des transferts à payer (imprimés négatifs) = 0",
                        0.0, d9r["cases"]["TOTAL"] + d9p["cases"]["TOTAL"], 2))
    # 6. Soldes reportés : un solde imprimé en emplois d'un compte et en ressources du suivant.
    for g in A.ls:
        if g["nature"] != "solde" or g["cote"] != R:
            continue
        e = A.ligne(E, g["operation"])
        if e is None:
            continue
        for c in SEQUENCE + ["S2", "TOTAL"]:
            if c in g["cases"] or c in e["cases"]:
                out.append(brut(A, "solde reporté (emplois = ressources)", f"{g['code_scn']} {c} (ligne {g['rang']})",
                                "solde en emplois du compte = solde en ressources du compte suivant",
                                e["cases"].get(c), g["cases"].get(c), 2,
                                raison="case imprimée d'un seul côté"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", action="store_true")
    a = ap.parse_args()
    ref = yaml.safe_load((FR / "annee-reference.yml").read_text(encoding="utf-8"))
    annees = sorted([int(ref["annee"])] + [int(x) for x in ref.get("secondaires", [])])
    tee = lire(CACHE / "cnat-tee.csv")
    sect = [l for l in lire(CACHE / "cnat-secteurs.csv") if str(l["base"]) == "2015"]
    postes = lire(FR / "postes-comptables.csv")
    eds = editions(tee, annees)
    cases, ctrl = [], []
    for an in annees:
        ls = lignes_imprimees(tee, an, eds[an])
        for g in ls:
            rap = rapprocher(g, sect, an, eds[an]) if g["nature"] == "sans_libelle" else ""
            for c in COLONNES:
                if c not in g["cases"]:
                    continue
                ex, pa = rattacher(g, c, postes, ls)
                cases.append({"annee": an, "edition": eds[an], "page": g["page"], "rang": g["rang"], "cote": g["cote"],
                              "code_scn": g["code_scn"], "operation": g["operation"], "occurrence": g["occurrence"],
                              "libelle_ins": g["libelle_ins"], "nature": g["nature"], "code_rapproche": rap,
                              "colonne": c, "valeur_md": g["cases"][c],
                              "postes_exacts": ";".join(ex), "postes_par_code_parent": ";".join(pa)})
        ctrl += controles(Annee(an, eds[an], ls))
    if a.verifier:
        for p, rows in ((SORTIE, cases), (CONTROLES, ctrl)):
            if not p.exists() or lire(p) != [{k: str(v) for k, v in l.items()} for l in rows]:
                print(f"{p.name} n'est pas à jour : relancer scripts/comptes_tee.py")
                return 1
        return 0
    for p, rows in ((SORTIE, cases), (CONTROLES, ctrl)):
        with p.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
    for an in annees:
        cs = [c for c in ctrl if c["annee"] == an]
        n = {s: sum(c["statut"] == s for c in cs) for s in ("égal", "égal aux arrondis près", "écart", "non calculable")}
        print(f"{an} ({eds[an]}) : {len(cs)} contrôles — " + ", ".join(f"{k} {v}" for k, v in n.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())

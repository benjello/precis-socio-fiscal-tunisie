"""Couverture du compte d'un secteur par les postes de l'ouvrage : deux indicateurs distincts.

- **Part du compte couverte** : montant INS (valeur absolue) des opérations qui ont au moins un poste
  chiffré, rapporté au total des montants INS du compte du secteur (emplois et ressources, hors soldes
  et hors compte financier, sans double compte des composantes). Retirer un poste ne peut que la faire
  baisser ou la laisser inchangée.
- **Justesse** : somme des postes rapportée au montant INS, sur les seules opérations chiffrées dont
  tous les postes sont propres au secteur (un poste qui chiffre l'opération pour plusieurs secteurs,
  comme la TVA versée par les ménages et les sociétés, ne peut pas être rapproché du montant d'un seul).

Fonctions pures, testées par tests/test_couverture_comptes.py ; appelées par reconstruire_comptes.py.
"""
from __future__ import annotations

from collections import defaultdict

# secteur publié → secteurs du cache et du registre des postes
SECTEURS = {
    "S13-consolide": ("apu", ("apu_centrale", "apu_locale", "apu_secu")),
    "S1311": ("apu_centrale", ("apu_centrale",)),
    "S1313": ("apu_locale", ("apu_locale",)),
    "S1314": ("apu_secu", ("apu_secu",)),
    "S14": ("menages", ("menages",)),
    "S11": ("snf", ("snf",)),
    "S12": ("sf", ("sf",)),
    "S2": ("rdm", ("rdm",)),
}


def feuilles(lignes: list[dict], garder: set | None = None) -> list[dict]:
    """Opérations d'un secteur sans les soldes (B.), le compte financier (F.) ni les agrégats dont une
    composante est imprimée (D.1 quand D.11 l'est ; la production quand la production non marchande l'est).
    Exception : un agrégat qui porte un poste de l'ouvrage (`garder`) alors qu'aucune de ses composantes
    n'en porte est gardé, et ses composantes écartées (la masse salariale du budget chiffre D.1, pas D.11)."""
    garder = garder or set()
    ls = [l for l in lignes if l["code_scn2008"] and not l["code_scn2008"].startswith(("B.", "F."))
          and str(l["sous_ligne"]) in ("0", "1")]
    out = []
    for cote in ("emplois", "ressources"):
        g = [l for l in ls if l["cote"] == cote]
        codes = {l["code_scn2008"] for l in g}
        ops = {l["operation"] for l in g}
        desc = lambda c: [x for x in g if x["code_scn2008"] != c and x["code_scn2008"].startswith(c)]
        parents = {l["code_scn2008"] for l in g if l["operation"] in garder and desc(l["code_scn2008"])
                   and not any(x["operation"] in garder for x in desc(l["code_scn2008"]))}
        vus = set()
        for l in g:
            c = l["code_scn2008"]
            if any(p != c and c.startswith(p) for p in parents):
                continue
            if c not in parents and any(x != c and x.startswith(c) for x in codes):
                continue
            if l["operation"] == "production" and "production_non_marchande" in ops:
                continue
            if l["operation"] in vus:
                continue
            vus.add(l["operation"])
            out.append(l)
    return out


def postes_du_secteur(postes: list[dict], membres: tuple[str, ...]) -> dict:
    """{opération: [(rôle, montant ou None, propre au secteur)]} : un poste est rattaché au secteur quand
    l'un des membres verse (rôle « verse ») ou reçoit (rôle « recoit »)."""
    out = defaultdict(list)
    for p in postes:
        m = float(p["montant_reference"]) if p.get("montant_reference") not in (None, "") else None
        for role, champ in (("verse", "secteur_verse"), ("recoit", "secteur_recoit")):
            secs = [s for s in p[champ].split(";") if s]
            if any(s in membres for s in secs):
                # un poste versé et reçu à l'intérieur du secteur y figure des deux côtés
                out[p["operation"]].append((role, m, all(s in membres for s in secs)))
    return out


# L'INS inscrit les subventions versées par les administrations en ressources négatives du payeur.
VERSEES_EN_RESSOURCES = {"subventions", "subventions_produits", "autres_subventions_production"}


def postes_de_la_ligne(l: dict, rattaches: dict) -> list:
    """Postes d'une ligne (côté, opération) : qui verse l'inscrit en emplois, qui reçoit en ressources,
    sauf les subventions, que le payeur inscrit en ressources négatives."""
    if l["cote"] == "emplois":
        roles = {"verse"} - ({"verse"} if l["operation"] in VERSEES_EN_RESSOURCES else set())
    else:
        roles = {"recoit"} | ({"verse"} if l["operation"] in VERSEES_EN_RESSOURCES else set())
    return [(m, propre) for r, m, propre in rattaches.get(l["operation"], []) if r in roles]


def indicateurs(ops: list[dict], rattaches: dict) -> dict:
    """ops : feuilles du secteur ; rattaches : sortie de postes_du_secteur."""
    total = couvert = j_postes = j_ins = 0.0
    n_chiffrees = n_justesse = 0
    for l in ops:
        v = float(l["valeur"])
        total += abs(v)
        chiffres = [(m, propre) for m, propre in postes_de_la_ligne(l, rattaches) if m is not None]
        if not chiffres:
            continue
        n_chiffrees += 1
        couvert += abs(v)
        if all(propre for _, propre in chiffres) and v:
            n_justesse += 1
            j_postes += abs(sum(m for m, _ in chiffres))
            j_ins += abs(v)
    return {"operations": len(ops), "operations_chiffrees": n_chiffrees,
            "ins_total_md": round(total, 1), "ins_couvert_md": round(couvert, 1),
            "part_couverte_pct": round(100 * couvert / total, 1) if total else "",
            "operations_justesse": n_justesse,
            "postes_justesse_md": round(j_postes, 1), "ins_justesse_md": round(j_ins, 1),
            "justesse_pct": round(100 * j_postes / j_ins, 1) if j_ins else ""}


# S13 publié = somme des trois sous-secteurs, non consolidée : dans le compte consolidé, une opération
# (la consommation finale) passe pour chiffrée dès qu'un sous-secteur l'est, même si les autres ne le sont pas.
SOUS_SECTEURS_S13 = ("S1311", "S1313", "S1314")


def agreger(resultats: list[dict]) -> dict:
    """Indicateurs d'un ensemble de secteurs, par somme des numérateurs et des dénominateurs."""
    t = {k: sum(float(r[k]) for r in resultats) for k in ("ins_total_md", "ins_couvert_md", "postes_justesse_md", "ins_justesse_md")}
    n = {k: sum(int(r[k]) for r in resultats) for k in ("operations", "operations_chiffrees", "operations_justesse")}
    return {"operations": n["operations"], "operations_chiffrees": n["operations_chiffrees"],
            "ins_total_md": round(t["ins_total_md"], 1), "ins_couvert_md": round(t["ins_couvert_md"], 1),
            "part_couverte_pct": round(100 * t["ins_couvert_md"] / t["ins_total_md"], 1) if t["ins_total_md"] else "",
            "operations_justesse": n["operations_justesse"],
            "postes_justesse_md": round(t["postes_justesse_md"], 1), "ins_justesse_md": round(t["ins_justesse_md"], 1),
            "justesse_pct": round(100 * t["postes_justesse_md"] / t["ins_justesse_md"], 1) if t["ins_justesse_md"] else ""}

"""Couverture du compte d'un secteur par les postes de l'ouvrage : deux indicateurs distincts.

- **Part du compte couverte** : montant INS (valeur absolue) des opérations qui ont au moins un poste
  chiffré, rapporté au total des montants INS du compte du secteur (emplois et ressources, hors soldes
  et hors compte financier, sans double compte des composantes). Retirer un poste ne peut que la faire
  baisser ou la laisser inchangée.
- **Justesse** : somme des postes rapportée au montant INS, sur les seules opérations chiffrées dont
  tous les postes sont propres au secteur (un poste qui chiffre l'opération pour plusieurs secteurs,
  comme la TVA versée par les ménages et les sociétés, ne peut pas être rapproché du montant d'un seul)
  et couvrent toute leur contrepartie (`contrepartie_couverte`) : la masse salariale de l'État, reçue par
  les ménages, ne chiffre qu'un de leurs employeurs et n'entre pas dans la justesse du D.1 des ménages.

- **Part du montant couverte** (indicateur principal) : somme, sur les opérations, des postes propres au
  secteur (valeur absolue) plafonnée au montant INS de l'opération, rapportée au total du compte. Un poste
  partiel ne couvre que son montant ; un poste qui chiffre plusieurs secteurs ne compte pas.

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


# Demi-unité de la dernière décimale imprimée (0,1 MD), par terme : la tolérance des identités (comptes_tee.ARRONDI).
ARRONDI = 0.05


def totaux_meme_code(g: list[dict]) -> dict:
    """{code : (ligne du total, composantes)} pour les codes que l'INS imprime sur plusieurs lignes d'un
    même côté, total compris. La production des sociétés financières et des administrations porte le seul
    code P.1 sur la ligne du total comme sur des composantes (services d'assurance, SIFIM, production
    marchande des administrations), à côté de P.11 et P.13 ; le code ne dit pas laquelle est le total.
    Le total est la ligne qui égale, aux arrondis près, la somme des autres lignes de la famille (même code
    et codes plus fins sans composante imprimée). Seules les familles d'au moins trois lignes sont
    examinées : deux lignes de même code sans code plus fin (les intérêts et la correction SIFIM, D.41)
    sont deux opérations distinctes."""
    codes = {l["code_scn2008"] for l in g}
    out = {}
    for c in sorted(codes):
        meme = [l for l in g if l["code_scn2008"] == c]
        if len(meme) < 2:
            continue
        fins = [l for l in g if l["code_scn2008"] != c and l["code_scn2008"].startswith(c)
                and not any(x != l["code_scn2008"] and x.startswith(l["code_scn2008"]) for x in codes)]
        fam = meme + fins
        if len(fam) < 3:
            continue
        tot = sum(float(l["valeur"]) for l in fam)
        tetes = [l for l in meme if abs(2 * float(l["valeur"]) - tot) <= ARRONDI * len(fam) + 1e-9]
        if len(tetes) > 1:
            raise ValueError(f"{c} : plusieurs lignes égalent la somme des autres "
                             f"({', '.join(l['operation'] for l in tetes)})")
        if tetes:
            out[c] = (tetes[0], [l for l in fam if l is not tetes[0]])
    return out


def feuilles(lignes: list[dict], garder: set | None = None) -> list[dict]:
    """Opérations d'un secteur sans les soldes (B.), le compte financier (F.) ni les agrégats dont une
    composante est imprimée (D.1 quand D.11 l'est ; la production quand la production non marchande l'est ;
    le total P.1 quand ses composantes le sont, y compris sous le même code, voir `totaux_meme_code`).
    Exception : un agrégat qui porte un poste de l'ouvrage (`garder`) alors qu'aucune de ses composantes
    n'en porte est gardé, et ses composantes écartées (la masse salariale du budget chiffre D.1, pas D.11).
    La règle se décide côté par côté : `garder` est soit un ensemble d'opérations valable pour les deux
    côtés, soit un dictionnaire {côté : opérations} (voir `garder_par_cote`). Un poste en emplois ne fait
    pas éclater l'agrégat des ressources, où un autre poste porte seul l'agrégat."""
    garder = garder or set()
    par_cote = garder if isinstance(garder, dict) else {"emplois": garder, "ressources": garder}
    ls = [l for l in lignes if l["code_scn2008"] and not l["code_scn2008"].startswith(("B.", "F."))
          and str(l["sous_ligne"]) in ("0", "1")]
    out = []
    for cote in ("emplois", "ressources"):
        g = [l for l in ls if l["cote"] == cote]
        garder = set(par_cote.get(cote, ()))
        totaux = totaux_meme_code(g)
        ecartees, totaux_gardes = [], []
        for tete, comps in totaux.values():
            if tete["operation"] in garder and not any(x["operation"] in garder for x in comps):
                totaux_gardes.append(tete)
                ecartees += comps
            else:
                ecartees.append(tete)
        codes = {l["code_scn2008"] for l in g}
        ops = {l["operation"] for l in g}
        desc = lambda c: [x for x in g if x["code_scn2008"] != c and x["code_scn2008"].startswith(c)]
        parents = {l["code_scn2008"] for l in g if l["code_scn2008"] not in totaux and l["operation"] in garder
                   and desc(l["code_scn2008"]) and not any(x["operation"] in garder for x in desc(l["code_scn2008"]))}
        vus = set()
        for l in g:
            c = l["code_scn2008"]
            if any(l is x for x in ecartees):
                continue
            if not any(l is x for x in totaux_gardes):
                if any(p != c and c.startswith(p) for p in parents):
                    continue
                if c not in parents and c not in totaux and any(x != c and x.startswith(c) for x in codes):
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
        for role, champ, autre in (("verse", "secteur_verse", "secteur_recoit"), ("recoit", "secteur_recoit", "secteur_verse")):
            secs = [s for s in p[champ].split(";") if s]
            if any(s in membres for s in secs):
                # un poste versé et reçu à l'intérieur du secteur y figure des deux côtés ; 4e terme : les
                # secteurs de l'autre bout du poste (vide : le registre ne nomme pas de contrepartie)
                out[p["operation"]].append((role, m, all(s in membres for s in secs),
                                            tuple(x for x in p.get(autre, "").split(";") if x)))
    return out


# Secteurs au niveau du registre des postes (secteur_verse, secteur_recoit) ; l'INS imprime aussi des
# sous-secteurs (sf_assurance, menages_ei…), contenus dans ceux-ci, et le compte consolidé des administrations.
NIVEAU_REGISTRE = ("snf", "sf", "menages", "rdm", "apu_centrale", "apu_locale", "apu_secu")
SOUS_APU = ("apu_centrale", "apu_locale", "apu_secu")


def montants_ins(lignes: list[dict]) -> dict:
    """{(côté, code) : {secteur : |montant|}} des lignes d'opération de l'INS d'une année (toutes les
    lignes, tous secteurs), sans les soldes ni le compte financier. Le compte consolidé (« apu ») est gardé
    à part pour savoir si un sous-secteur non imprimé (l'administration centrale en base 1983) peut avoir
    un montant."""
    out = defaultdict(lambda: defaultdict(float))
    for l in lignes:
        c = l.get("code_scn2008") or ""
        if not c or c.startswith(("B.", "F.")) or str(l.get("sous_ligne", "0")) not in ("0", "1"):
            continue
        if l["secteur"] in NIVEAU_REGISTRE or l["secteur"] == "apu":
            out[(l["cote"], c)][l["secteur"]] = max(out[(l["cote"], c)][l["secteur"]], abs(float(l["valeur"])))
    return out


def contrepartie_ins(l: dict, secteur: str, ins: dict) -> set:
    """Secteurs (niveau du registre) qui ont, selon l'INS, un montant non nul à l'autre bout de l'opération de
    la ligne `l` du secteur `secteur` : de l'autre côté (emplois face à ressources), sauf pour les subventions,
    que payeur et receveur inscrivent en ressources (du même côté, le secteur lui-même exclu). Une opération
    imprimée à une autre finesse de l'autre côté (D.11 face à D.1) compte par le préfixe du code. Un
    sous-secteur des administrations absent du cache, quand le compte consolidé porte un montant, est compté
    comme contrepartie : son montant n'est pas connu, il n'est pas présumé nul."""
    meme = l["operation"] in VERSEES_EN_RESSOURCES
    cote = l["cote"] if meme else ("ressources" if l["cote"] == "emplois" else "emplois")
    code = l["code_scn2008"]
    secs = defaultdict(float)
    exact = {s for (c_cote, c), m in ins.items() if c_cote == cote and c == code for s in m}
    for (c_cote, c), montants in ins.items():
        # le code même ; à défaut, chez un secteur qui ne l'imprime pas, ses composantes (D.11 pour D.1) ;
        # jamais un agrégat (D.4 pour D.45), dont le montant ne dit pas celui de la composante
        if c_cote == cote and (c == code or c.startswith(code)):
            for s, v in montants.items():
                if c == code or s not in exact:
                    secs[s] += v
    out = {s for s, v in secs.items() if v > ARRONDI and s != "apu"}
    presents = {s for (c_cote, _), m in ins.items() for s in m}
    if secs.get("apu", 0) > ARRONDI:
        out |= {s for s in SOUS_APU if s not in presents}
    if meme:
        out -= set(SOUS_APU) if secteur == "apu" else {secteur}
    # le compte du reste du monde n'enregistre que ses opérations avec les résidents : il n'est pas sa propre contrepartie
    if secteur == "rdm":
        out.discard("rdm")
    return out


def contrepartie_couverte(l: dict, rattaches: dict, secteur: str, ins: dict | None) -> bool:
    """Les postes chiffrés de la ligne couvrent toute sa contrepartie selon l'INS (`contrepartie_ins`). Un
    poste dont le registre ne nomme pas de contrepartie (champ vide : FBCF, consommation finale, échanges
    extérieurs) chiffre toute l'opération : la ligne reste régie par la seule règle des postes propres.
    Sans `ins`, la condition n'est pas examinée."""
    if ins is None:
        return True
    cps = [cp for m, _, cp in postes_de_la_ligne_cp(l, rattaches) if m is not None]
    if not cps or any(not cp for cp in cps):
        return True
    return contrepartie_ins(l, secteur, ins) <= set().union(*map(set, cps))


# L'INS inscrit les subventions versées par les administrations en ressources négatives du payeur.
VERSEES_EN_RESSOURCES = {"subventions", "subventions_produits", "autres_subventions_production"}


def garder_par_cote(rattaches: dict) -> dict:
    """{côté : opérations qui y portent un poste du secteur} : les rôles de `postes_de_la_ligne` (qui verse
    inscrit en emplois, qui reçoit en ressources, sauf les subventions, inscrites en ressources du payeur)."""
    out = {"emplois": set(), "ressources": set()}
    for op, liste in rattaches.items():
        for cote in out:
            if postes_de_la_ligne({"cote": cote, "operation": op}, rattaches):
                out[cote].add(op)
    return out


def postes_de_la_ligne(l: dict, rattaches: dict) -> list:
    """Postes d'une ligne (côté, opération) : qui verse l'inscrit en emplois, qui reçoit en ressources,
    sauf les subventions, que le payeur inscrit en ressources négatives."""
    if l["cote"] == "emplois":
        roles = {"verse"} - ({"verse"} if l["operation"] in VERSEES_EN_RESSOURCES else set())
    else:
        roles = {"recoit"} | ({"verse"} if l["operation"] in VERSEES_EN_RESSOURCES else set())
    return [(m, propre) for m, propre, _ in postes_de_la_ligne_cp(l, rattaches)]


def postes_de_la_ligne_cp(l: dict, rattaches: dict) -> list:
    """Comme postes_de_la_ligne, avec les secteurs de l'autre bout de chaque poste."""
    if l["cote"] == "emplois":
        roles = {"verse"} - ({"verse"} if l["operation"] in VERSEES_EN_RESSOURCES else set())
    else:
        roles = {"recoit"} | ({"verse"} if l["operation"] in VERSEES_EN_RESSOURCES else set())
    return [(m, propre, (x[0] if x else ())) for r, m, propre, *x in rattaches.get(l["operation"], []) if r in roles]


def indicateurs(ops: list[dict], rattaches: dict, secteur: str = "", ins: dict | None = None) -> dict:
    """ops : feuilles du secteur ; rattaches : sortie de postes_du_secteur ; `ins` (montants_ins de l'année) et
    `secteur` (secteur du cache) : la justesse ne retient que les opérations dont les postes couvrent toute la
    contrepartie (contrepartie_couverte). La part du montant n'en dépend pas."""
    total = couvert = montant = j_postes = j_ins = 0.0
    n_chiffrees = n_justesse = 0
    for l in ops:
        v = float(l["valeur"])
        total += abs(v)
        chiffres = [(m, propre) for m, propre in postes_de_la_ligne(l, rattaches) if m is not None]
        if not chiffres:
            continue
        n_chiffrees += 1
        couvert += abs(v)
        # part du montant : postes propres au secteur seulement, en valeur absolue, plafonnés au montant de l'INS
        montant += min(sum(abs(m) for m, propre in chiffres if propre), abs(v))
        if all(propre for _, propre in chiffres) and v and contrepartie_couverte(l, rattaches, secteur, ins):
            n_justesse += 1
            j_postes += abs(sum(m for m, _ in chiffres))
            j_ins += abs(v)
    return {"operations": len(ops), "operations_chiffrees": n_chiffrees,
            "ins_total_md": round(total, 1), "ins_couvert_md": round(couvert, 1),
            "part_couverte_pct": round(100 * couvert / total, 1) if total else "",
            "montant_couvert_md": round(montant, 1),
            "part_montant_couverte_pct": round(100 * montant / total, 1) if total else "",
            "operations_justesse": n_justesse,
            "postes_justesse_md": round(j_postes, 1), "ins_justesse_md": round(j_ins, 1),
            "justesse_pct": round(100 * j_postes / j_ins, 1) if j_ins else ""}


# S13 publié = somme des trois sous-secteurs, non consolidée : dans le compte consolidé, une opération
# (la consommation finale) passe pour chiffrée dès qu'un sous-secteur l'est, même si les autres ne le sont pas.
SOUS_SECTEURS_S13 = ("S1311", "S1313", "S1314")


def agreger(resultats: list[dict]) -> dict:
    """Indicateurs d'un ensemble de secteurs, par somme des numérateurs et des dénominateurs."""
    t = {k: sum(float(r[k]) for r in resultats) for k in ("ins_total_md", "ins_couvert_md", "montant_couvert_md", "postes_justesse_md", "ins_justesse_md")}
    n = {k: sum(int(r[k]) for r in resultats) for k in ("operations", "operations_chiffrees", "operations_justesse")}
    return {"operations": n["operations"], "operations_chiffrees": n["operations_chiffrees"],
            "ins_total_md": round(t["ins_total_md"], 1), "ins_couvert_md": round(t["ins_couvert_md"], 1),
            "part_couverte_pct": round(100 * t["ins_couvert_md"] / t["ins_total_md"], 1) if t["ins_total_md"] else "",
            "montant_couvert_md": round(t["montant_couvert_md"], 1),
            "part_montant_couverte_pct": round(100 * t["montant_couvert_md"] / t["ins_total_md"], 1) if t["ins_total_md"] else "",
            "operations_justesse": n["operations_justesse"],
            "postes_justesse_md": round(t["postes_justesse_md"], 1), "ins_justesse_md": round(t["ins_justesse_md"], 1),
            "justesse_pct": round(100 * t["postes_justesse_md"] / t["ins_justesse_md"], 1) if t["ins_justesse_md"] else ""}


def raccord_identique(ops: list[dict], liens: dict) -> list[dict]:
    """Feuilles d'un compte publié dans une base autre que 2015, réduites aux opérations dont le code se
    raccorde au code du SCN 2008 par un lien « identique » (`liens` : {opération : lien}, table de raccord
    des codes). Un regroupement, un éclatement, un lien « à valider » ou absent : l'opération est retirée,
    ni couverte ni comptée dans le total. Le filtre porte sur les feuilles, non sur les lignes : retirer une
    composante avant `feuilles` ferait d'un agrégat une feuille et réintroduirait son montant."""
    return [l for l in ops if liens.get(l["operation"]) == "identique"]

"""Annexe engendrée « Les sources de données chiffrées » (`precis/fr/annexe-sources.qmd`).

    from figures import annexe_sources
    annexe_sources.rendre()   # émet tout le corps : une sous-section par famille, une entrée par
                              # source ISOLÉE et une entrée CONDENSÉE par collection annuelle

MODULE DE FIGURE D'UNE PAGE DE SITE, et non d'un livre : il vit dans `precis/fr/figures/`, à
côté de la page (comme `figures/annexe_pib.py`) ; la page arabe le trouverait par le lien
symbolique `precis/ar/figures`.

CE QUE FAIT LE MODULE (projection engendrée, rien de dupliqué).
  1. Scanne tous les manifestes de figure `precis/fr/**/figdata/*.csv.yml` et collecte l'union
     des clés `sources` citées.
  2. Résout chaque clé dans les `references.json` du précis (clé `items`, format CSL).
  3. ÉCARTE le texte législatif pur : toute source de `type: legislation` (le JORT) reste en
     bibliographie et n'est PAS listée ici. Les types retenus sont les supports chiffrés :
     report, webpage, dataset, article-journal/-newspaper, book, chapter.
  4. Classe chaque source dans une FAMILLE via la table versionnée `sources_familles.yml`
     (producteur -> famille), avec la règle « annexe … loi de finances » et une famille par
     défaut (voir `_famille`).
  5. CONDENSE les COLLECTIONS ANNUELLES ET LES QUASI-DOUBLONS. Beaucoup de supports sont la même
     série répétée par année (« Rapport sur les entreprises publiques (annexe 9 au PLF pour 2020,
     2021, … » ; « Budget du ministère du Transport pour l'année 2013 … 2017 » ; « تقرير المالية
     العمومية لسنة 2005, 2008 »), et beaucoup portent des libellés DIFFÉRENTS pour une MÊME source
     (renommage du producteur, abréviation « EP » / « PLF », « annexe 9 » / « annexe n° 9 »,
     formulation « à la » / « au projet de » loi de finances, variante arabe « لتصرف » / « لسنة »,
     double clé d'une même édition). On regroupe, DANS CHAQUE FAMILLE, les sources d'une même
     collection en UNE entrée (voir `_grouper`) :
       - sous-type / radical = le titre fortement NORMALISÉ (voir `_radical` et la table
         `_SYNONYMES`) : on travaille sur la traduction latine si le titre arabe en porte une
         entre parenthèses/crochets (appariement FR/AR), on retire les tokens d'année 19xx/20xx,
         on passe sans accents ni casse, puis on neutralise abréviations, numéros d'annexe,
         préfixes ordinaux et mots de remplissage. Deux titres qui se réduisent au même radical
         pour une même LIGNÉE de producteur (table `_LIGNEES`, qui réunit les renommages d'un
         même producteur) = une collection ; au moindre doute (radical ou lignée distincts),
         les entrées restent séparées ;
       - année d'édition = l'unique année distincte lue dans le titre (c'est le token qui varie
         d'un membre à l'autre et définit la série) ; un titre à deux années distinctes (p. ex.
         « … à fin 2016 et janvier 2017 ») ne se réduit pas et reste ISOLÉ ;
       - intervalle = min–max des années d'édition, inséré à la place du token dans le titre le
         plus récent (le libellé de la collection) ;
       - manquants = années absentes de [min, max], SIGNALÉES seulement si la cadence annuelle
         est RÉELLEMENT établie (≥ 3 éditions et densité présents/intervalle ≥ 0,7) ; une série
         clairsemée (quelques éditions éparses sur vingt ans) n'affiche AUCUN manquant, pour ne
         pas inventer une complétude attendue ;
       - une source isolée (un seul document, pas de série) reste une entrée individuelle.
  5 bis. REGROUPEMENTS SÉMANTIQUES que la normalisation ne peut pas deviner : une table
     EXPLICITE et versionnée `sources_collections.yml` (collection -> clés), construite en
     LISANT les intitulés, dit que des libellés très différents désignent la même série ou le
     même dossier : séries numérotées EN LETTRES (« Premier … Vingt et unième rapport annuel de
     la Cour de discipline financière », cf. `_ordinal_lettres`), éditions d'un même annuaire,
     pièces d'un même dossier. Les documents RÉELLEMENT DISTINCTS d'un dossier (volumes d'un
     recensement, exercices d'une série d'états financiers) sont regroupés mais restés LISTÉS
     un par un (chacun son ancre, son étiquette). Cette table prime : ses clés sont retirées
     avant la condensation algorithmique (cf. `_appliquer_table`). Au moindre doute, une clé
     n'y figure pas.
  6. Émet le corps GROUPÉ par famille (sous-section `###`, ancre `#src-fam-<slug>`). CHAQUE clé
     — isolée ou regroupée dans une collection — conserve son ancre STABLE `#src-<cle>` à
     laquelle les livres et les onglets « 🔗 Sources » des figures renvoient : dans une entrée
     condensée, chaque année porte un lien (ou un libellé) ancré `[année](url){#src-<cle>}`, de
     sorte que TOUS les `#src-<cle>` restent résolvables (le nombre d'ancres est invariant).

RÈGLES (le précis l'exige).
  - **Rien de fabriqué.** Titre, producteur, URL et année sont LUS dans references.json / le
    titre ; une métadonnée absente (souvent l'URL) est laissée vide, jamais inventée. Une année
    illisible n'est pas affichée ; un « manquant » n'est signalé que si l'intervalle annuel est
    réellement établi (cf. le garde-fou de densité ci-dessus).
  - **Une clé citée absente de references.json, ou d'un `type` inattendu, est SIGNALÉE** (en
    commentaire HTML en fin de corps, et sur stderr), non forcée ni corrigée en silence.
  - **Aucun nom de fichier (CSV, figdata, listes) dans le texte publié.** Les manifestes et les
    clés de citation ne sont que des entrées d'index ; aucun chemin local n'est émis.
  - **Période / réserves non attachées à la source.** `tunisia-data/catalog.yml` porte bien des
    `perimetre`/`caveats`, mais PAR SÉRIE : une même source alimente plusieurs séries aux
    périmètres et réserves différents, souvent longs (plusieurs centaines de caractères) et
    parfois contradictoires. Les rabattre sur la source les dénaturerait ; on ne les émet donc
    pas ici (la traçabilité fine reste dans l'onglet « 🔗 Sources » de chaque figure, qui cite
    la série exacte). L'enrichissement par série viendra, s'il vient, au niveau de la série.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

FR = Path(__file__).resolve().parent.parent          # precis/fr
FAMILLES_YML = FR / "sources_familles.yml"

# Types CSL retenus = supports de données chiffrées. `legislation` (JORT) est exclu.
TYPES_RETENUS = {
    "report", "webpage", "dataset", "article-journal",
    "article-newspaper", "book", "chapter",
}
TYPES_EXCLUS = {"legislation"}


def _sans_accents(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def _slug(s: str) -> str:
    s = _sans_accents(s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "x"


# Un token d'année isolé (19xx/20xx), pas un simple groupe de 4 chiffres dans un plus grand nombre.
_ANNEE = re.compile(r"(?<!\d)(?:19|20)\d{2}(?!\d)")
_TIRET = "\u2013"   # tiret demi-cadratin pour les intervalles : 2013–2017
# Densité minimale (présents / étendue) et nombre minimal d'éditions pour oser signaler des années
# manquantes : en deçà, la série est trop clairsemée pour qu'une cadence annuelle soit établie.
_DENSITE_MIN = 0.7
_EDITIONS_MIN = 3


def _annees_titre(titre: str) -> list[int]:
    """Années distinctes (tokens 19xx/20xx) lues dans un titre, triées."""
    return sorted({int(m.group(0)) for m in _ANNEE.finditer(titre)})


_ARABE = re.compile(r"[\u0600-\u06ff]")
_LATIN = re.compile(r"[A-Za-z\u00c0-\u024f]")

# Synonymes / abréviations observés DANS LES TITRES, appliqués au radical déjà passé en
# minuscules sans accents, l'année remplacée par « § ». Table EXPLICITE (ordre significatif) :
# chaque règle rapproche deux libellés d'une MÊME source. Enrichie d'après les titres réels
# (annexes des lois de finances, clôtures de la Cour des comptes, rapports de la BCT).
_SYNONYMES: list[tuple[str, str]] = [
    # Numéro d'annexe neutralisé : « annexe 9 » / « annexe n° 9 » / « annexe n° 12 » -> « annexe ».
    (r"\bannexe\s*(?:n\s*[o\u00b0]|no|numero)?\s*\d+", "annexe"),
    # « projet de loi de finances » (PLF) == « loi de finances » (LF), préposition absorbée.
    (r"\b(?:au|aux|a\s+la|du|de\s+la|de|des|a\s+l|a)?\s*projets?\s+de\s+loi\s+de\s+finances", "loi de finances"),
    (r"\b(?:au|aux|a\s+la|du|de\s+la|a\s+l|a)\s+loi\s+de\s+finances", "loi de finances"),
    (r"\bplf\b", "loi de finances"),
    # « pour la gestion / l'année / l'exercice X » == « pour X » (clôtures de budget, budgets).
    (r"\bpour\s+(?:la\s+gestion|l\s*annee|l\s*exercice|le\s+titre|l\s*exercise)", "pour"),
    (r"\b(?:au\s+titre\s+de\s+l?\s*annee)", "pour"),
    # « EP » == « entreprises publiques » (rapport annexé aux lois de finances).
    (r"\bentreprises\s+publiques\b", "ep"),
    # Préfixe ordinal numérique d'un rapport : « 36ème », « 13ème », « 1er » -> rien.
    (r"\b\d+\s*(?:emes?|ers?|eres?|es?)\b", ""),
    # Numéros résiduels (« n° 7 ») et mots de remplissage de périodicité.
    (r"\b(?:n\s*[o\u00b0]|no|numero)\s*\d+", ""),
    (r"\b(?:annee|annees|exercice|exercices)\b", ""),
    # Ponctuation et séparateurs -> espace (on ne touche pas aux lettres arabes conservées).
    (r"[\u00b0\u00b7.,;:/\-\u2013\u2014()\[\]{}«»\"'\u2019]", " "),
]

# Lignées de producteur : des libellés qui désignent LE MÊME producteur (renommages successifs,
# suffixes) sont ramenés à une même clé, pour qu'un renommage ne bloque pas une fusion légitime.
# Table EXPLICITE. Un producteur non répertorié reste lui-même (sa forme sans accents).
#   - « Ministère des Finances » a porté plusieurs noms (Économie, Économie et Finances,
#     Économie-Finances-Appui à l'investissement) ; ses directions générales en relèvent aussi.
# ATTENTION : deux ministères SECTORIELS différents (Transport, Santé…) ne sont PAS une lignée
# commune ; seul le ministère des Finances est regroupé ici. La concordance de lignée est une
# CONDITION de fusion, jamais une fusion à elle seule (le radical de titre doit aussi coïncider).
_LIGNEES: list[tuple[str, list[str]]] = [
    ("ministere-finances", [
        "ministere des finances",
        "ministere de l'economie, des finances",
        "ministere de l economie, des finances",
        "ministere de l'economie et des finances",
        "ministere de l economie et des finances",
        "ministere de l'economie",
        "ministere de l economie",
    ]),
    # INS : casse, accents et suffixe « , Tunisie » varient (« Institut National de la
    # Statistique, Tunisie » == « Institut national de la statistique »).
    ("institut-national-statistique", ["institut national de la statistique"]),
    # Caisses sociales : un suffixe « (CNSS), Tunisie » ne doit pas scinder le producteur.
    ("cnss", ["caisse nationale de securite sociale"]),
    ("cnam", ["caisse nationale d'assurance maladie"]),
    ("cnrps", ["caisse nationale de retraite et de prevoyance sociale"]),
]

# Ordinaux français écrits EN LETTRES (index d'une série numérotée, p. ex. les rapports annuels
# de la Cour de discipline financière « Premier … Vingt et unième »). Comparés sans accents.
_ORDINAUX: dict[str, int] = {
    "premier": 1, "premiere": 1, "deuxieme": 2, "second": 2, "seconde": 2, "troisieme": 3,
    "quatrieme": 4, "cinquieme": 5, "sixieme": 6, "septieme": 7, "huitieme": 8, "neuvieme": 9,
    "dixieme": 10, "onzieme": 11, "douzieme": 12, "treizieme": 13, "quatorzieme": 14,
    "quinzieme": 15, "seizieme": 16, "dix-septieme": 17, "dix-huitieme": 18, "dix-neuvieme": 19,
    "vingtieme": 20, "vingt et unieme": 21, "vingt-et-unieme": 21, "vingt-deuxieme": 22,
    "vingt-troisieme": 23, "vingt-quatrieme": 24, "vingt-cinquieme": 25,
}


def _ordinal_lettres(titre: str) -> int | None:
    """Rang d'une série si le titre COMMENCE par un ordinal écrit en lettres, sinon None."""
    deb = _sans_accents(titre).lstrip()
    for mot, n in sorted(_ORDINAUX.items(), key=lambda kv: -len(kv[0])):
        if deb.startswith(mot) and (len(deb) == len(mot) or not deb[len(mot)].isalpha()):
            return n
    return None


def _ordinal_fr(n: int) -> str:
    """Écriture abrégée d'un ordinal : 1 -> « 1ᵉʳ », n -> « nᵉ »."""
    return "1\u1d49\u02b3" if n == 1 else f"{n}\u1d49"


def _annee_issued(e: dict) -> int | None:
    """Année de publication (`issued`) d'une entrée CSL, si présente et numérique."""
    iss = e.get("issued") or {}
    dp = (iss.get("date-parts") or [[]])[0] if isinstance(iss, dict) else []
    return int(dp[0]) if dp and str(dp[0]).isdigit() else None


def _lignee(producteur: str) -> str:
    """Clé de lignée d'un producteur (renommages ramenés à un même identifiant)."""
    prod = _sans_accents(producteur)
    for canon, formes in _LIGNEES:
        if any(f in prod for f in formes):
            return canon
    return prod


def _radical(titre: str) -> str:
    """Radical NORMALISÉ d'un titre, servant de clé de collection.

    Pipeline : 1) si le titre est en arabe mais porte une traduction latine entre parenthèses
    ou crochets, on travaille sur CETTE traduction (appariement FR/AR) ; 2) l'année est
    remplacée par « § » ; 3) minuscules sans accents (les diacritiques arabes — chadda… —
    tombent aussi) ; 4) abréviations/synonymes de `_SYNONYMES` ; 5) espaces réduits.

    Deux titres d'une même source se réduisent alors au même radical malgré des formulations,
    abréviations ou numéros d'annexe différents.
    """
    t = titre
    if _ARABE.search(t):
        trads = [c for c in re.findall(r"[(\[]([^)\]]*)[)\]]", t) if _LATIN.search(c)]
        if trads:
            t = max(trads, key=len)   # la traduction latine, s'il y en a une
    t = _ANNEE.sub("\u00a7", t)
    t = _sans_accents(t)
    for motif, remplacement in _SYNONYMES:
        t = re.sub(motif, remplacement, t)
    return re.sub(r"\s+", " ", t).strip()


def _collection(membres: list[tuple[int, dict]], lignee: str) -> dict:
    """Construit une entrée condensée à partir de ses membres `(annee, source)`.

    Les membres peuvent partager une année (quasi-doublons : la même édition sous deux clés) ;
    l'intervalle et les manquants se calculent sur les années DISTINCTES. Libellé = titre du
    membre le plus récent, son token d'année remplacé par l'intervalle. Manquants = années
    absentes de [min, max], seulement si la cadence annuelle est établie (densité ≥ seuil).
    Le filtrage croisé (une année présente ailleurs dans la même lignée n'est pas « manquante »)
    est appliqué ensuite, quand toutes les entrées sont connues (`_filtrer_manquants`).
    """
    membres = sorted(membres, key=lambda t: t[0])
    annees = [a for a, _ in membres]
    distinctes = sorted(set(annees))
    amin, amax = distinctes[0], distinctes[-1]
    recent = membres[-1][1]
    libelle = _ANNEE.sub(f"{amin}{_TIRET}{amax}", recent["titre"]) if amin != amax else recent["titre"]
    # Un préfixe ordinal (« 47ème ») est propre à un volume, pas à la collection : on l'ôte du libellé.
    libelle = re.sub(r"^\s*\d+\s*(?:[e\u00e8]mes?|ers?|[e\u00e8]res?|es?)\s+", "", libelle)
    etendue = amax - amin + 1
    manquants = [y for y in range(amin, amax + 1) if y not in set(distinctes)]
    etablie = len(distinctes) >= _EDITIONS_MIN and len(distinctes) / etendue >= _DENSITE_MIN
    if not etablie:
        manquants = []   # trop clairsemé : on ne postule pas une complétude annuelle
    url = recent["url"] or next((d["url"] for _, d in reversed(membres) if d["url"]), "")
    return {
        "collection": True,
        "titre": libelle,
        "producteur": recent["producteur"],
        "lignee": lignee,
        "url": url,
        "membres": membres,
        "annees": distinctes,
        "amin": amin,
        "amax": amax,
        "manquants": manquants,
    }


def _grouper(entrees: list[dict]) -> list[dict]:
    """Condense une liste de sources (d'une famille) : collections annuelles + sources isolées.

    Rend une liste d'items : soit une source isolée (dict d'origine), soit une collection
    (`collection=True`). Une collection = ≥ 2 membres d'un même radical et producteur, chacun
    portant exactement UNE année distincte, ces années étant toutes différentes. Tout le reste
    (titre sans année, titre à plusieurs années, radical/producteur unique) reste isolé.
    """
    from collections import defaultdict
    groupes: dict[tuple[str, str], list[tuple[list[int], dict]]] = defaultdict(list)
    for d in entrees:
        annees = _annees_titre(d["titre"])
        cle_groupe = (_radical(d["titre"]), _lignee(d["producteur"])) if len(annees) == 1 \
            else ("\x00iso\x00" + d["cle"], "")   # titre sans/à plusieurs années : isolé d'office
        groupes[cle_groupe].append((annees, d))
    items: list[dict] = []
    for (_, lignee), membres in groupes.items():
        # Chaque membre retenu porte exactement une année ; ≥ 2 membres = une entrée condensée
        # (collection annuelle et/ou quasi-doublons d'une même édition).
        if len(membres) >= 2 and all(len(a) == 1 for a, _ in membres):
            items.append(_collection([(a[0], d) for a, d in membres], lignee))
        else:
            items.extend(d for _, d in membres)
    items.sort(key=lambda it: (_sans_accents(it["producteur"]), _sans_accents(it["titre"])))
    return items


def _cles_citees() -> set[str]:
    """Union des clés `sources` de tous les manifestes de figure du précis FR.

    On lit la seule ligne `sources: [...]` (flux), sans parser tout le YAML : certains
    manifestes portent des `caveats` en prose avec des « : » qui cassent un parseur strict.
    """
    cles: set[str] = set()
    for man in FR.glob("**/figdata/*.csv.yml"):
        for ligne in man.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*sources:\s*\[(.*)\]\s*$", ligne)
            if m:
                cles.update(s.strip() for s in m.group(1).split(",") if s.strip())
                break
    return cles


def _index_references() -> dict[str, dict]:
    """Index {clé: entrée CSL} de tous les references.json du précis FR (le plus proche prime)."""
    idx: dict[str, dict] = {}
    # Le references.json du livre prime sur la bibliographie commune : on lit les plus profonds
    # d'abord. L'ordre importe peu ici (les clés sont uniques), mais on garde la convention.
    for rj in sorted(FR.glob("**/references.json"), key=lambda p: -len(p.parts)):
        try:
            items = json.loads(rj.read_text(encoding="utf-8")).get("items", [])
        except (ValueError, OSError):
            continue
        for e in items:
            idx.setdefault(e.get("id"), e)
    return idx


def _producteur(e: dict) -> str:
    """Producteur lisible d'une entrée CSL : `publisher`, sinon le premier auteur."""
    if e.get("publisher"):
        return e["publisher"]
    for a in (e.get("author") or []):
        nom = a.get("literal") or " ".join(x for x in (a.get("given"), a.get("family")) if x)
        if nom:
            return nom
    return ""


def _charger_familles() -> list[dict]:
    return yaml.safe_load(FAMILLES_YML.read_text(encoding="utf-8"))["familles"]


COLLECTIONS_YML = FR / "sources_collections.yml"


def _charger_collections_explicites() -> list[dict]:
    """Table versionnée collection -> clés (regroupements sémantiques lus dans les intitulés)."""
    if not COLLECTIONS_YML.exists():
        return []
    return yaml.safe_load(COLLECTIONS_YML.read_text(encoding="utf-8")).get("collections", [])


def _etiquette_membre(label: str | None, d: dict) -> str:
    """Étiquette lisible d'un membre : label explicite, sinon ordinal du titre, sinon année."""
    if label:
        return label
    rang = _ordinal_lettres(d["titre"])
    if rang is not None:
        return _ordinal_fr(rang)
    ans = _annees_titre(d["titre"])
    if len(ans) == 1:
        return str(ans[0])
    if d.get("annee_pub"):
        return str(d["annee_pub"])
    return "notice"


def _appliquer_table(par_famille: dict[str, list[dict]]) -> dict[str, list[dict]]:
    """Construit les collections EXPLICITES et retire leurs membres de `par_famille` (muté).

    Rend {famille -> [collection, ...]}. Chaque collection porte `explicite=True`, un `titre`,
    un `producteur`, une `nature` (« éditions »/« documents ») et des `membres` [(étiquette, d)].
    Une clé listée mais non citée (absente de `par_famille`) est ignorée sans bruit.
    """
    from collections import defaultdict
    localisation: dict[str, tuple[str, dict]] = {
        d["cle"]: (fam, d) for fam, entrees in par_famille.items() for d in entrees
    }
    par_famille_coll: dict[str, list[dict]] = defaultdict(list)
    cles_prises: set[str] = set()
    for spec in _charger_collections_explicites():
        membres: list[tuple[str, dict]] = []
        familles: list[str] = []
        for m in spec.get("cles", []):
            cle = m["cle"] if isinstance(m, dict) else m
            label = m.get("label") if isinstance(m, dict) else None
            if cle not in localisation:
                continue
            fam, d = localisation[cle]
            membres.append((_etiquette_membre(label, d), d))
            familles.append(fam)
            cles_prises.add(cle)
        if len(membres) < 2:
            continue   # une seule pièce citée : rien à condenser, on laisse l'entrée isolée
        # Intervalle affiché : toutes les années lues dans les titres ; à défaut (titres sans
        # millésime, p. ex. ordinaux), les années de publication `issued`.
        annees = sorted({a for _, d in membres for a in _annees_titre(d["titre"])})
        if not annees:
            annees = sorted({d["annee_pub"] for _, d in membres if d.get("annee_pub")})
        recent = membres[-1][1]
        url = next((d["url"] for _, d in membres if d["url"]), "")
        fam = max(set(familles), key=familles.count)
        par_famille_coll[fam].append({
            "collection": True,
            "explicite": True,
            "titre": spec["titre"],
            "producteur": spec.get("producteur", recent["producteur"]),
            "nature": spec.get("nature", "éditions"),
            "url": url,
            "membres": membres,
            "annees": annees,
        })
    for fam in par_famille:
        par_famille[fam] = [d for d in par_famille[fam] if d["cle"] not in cles_prises]
    return par_famille_coll


_LF = re.compile(r"annexe", re.I)
_LDF = re.compile(r"loi de finances", re.I)


def _est_annexe_lf(e: dict) -> bool:
    titre = e.get("title", "")
    return bool(_LF.search(titre) and _LDF.search(titre))


def _famille(e: dict, familles: list[dict]) -> str:
    """Famille d'une source : règle « annexe … loi de finances » d'abord, puis producteur."""
    prod = _sans_accents(_producteur(e))
    minfin = any(
        sub in prod
        for fam in familles if fam["nom"] == "Rapports du ministère des Finances"
        for sub in fam.get("producteurs", [])
    )
    if minfin and _est_annexe_lf(e):
        return "Annexes chiffrées des lois de finances"
    for fam in familles:
        for sub in (fam.get("producteurs") or []):
            if sub in prod:
                return fam["nom"]
    return familles[-1]["nom"]   # défaut : « Autres sources chiffrées »


def collecter() -> tuple[dict[str, list[dict]], list[str], list[str]]:
    """Construit le classement par famille. Rend (familles->entrées, cles_inconnues, types_inattendus).

    Chaque entrée : {cle, titre, producteur, url}.
    """
    familles = _charger_familles()
    ordre = [f["nom"] for f in familles]
    idx = _index_references()
    par_famille: dict[str, list[dict]] = {nom: [] for nom in ordre}

    inconnues: list[str] = []
    types_inattendus: list[str] = []
    for cle in _cles_citees():
        e = idx.get(cle)
        if e is None:
            inconnues.append(cle)
            continue
        typ = e.get("type")
        if typ in TYPES_EXCLUS:
            continue
        if typ not in TYPES_RETENUS:
            types_inattendus.append(f"{cle} ({typ})")
            # On le liste quand même, mais on le signale : un type nouveau est à trier.
        fam = _famille(e, familles)
        par_famille[fam].append({
            "cle": cle,
            "titre": e.get("title", cle),
            "producteur": _producteur(e),
            "url": e.get("URL") or "",
            "annee_pub": _annee_issued(e),
        })
    for nom in ordre:
        par_famille[nom].sort(key=lambda d: (_sans_accents(d["producteur"]), _sans_accents(d["titre"])))
    # Familles vides retirées, ordre conservé.
    par_famille = {nom: par_famille[nom] for nom in ordre if par_famille[nom]}
    return par_famille, sorted(set(inconnues)), sorted(set(types_inattendus))


def _filtrer_manquants(par_famille_items: dict[str, list[dict]]) -> None:
    """Retire des « manquants » toute année en fait disponible ailleurs dans la MÊME lignée.

    Garde-fou « rien d'inventé » : une collection ne doit pas déclarer « manque 1999 » si le
    précis cite bien un support 1999 du même producteur, rangé dans une autre entrée (p. ex.
    la BCT a nommé son rapport tantôt « Rapport annuel », tantôt « Rapport d'activité »). On
    recense d'abord toutes les années connues par lignée, puis on émonde les manquants.
    """
    from collections import defaultdict
    annees_lignee: dict[str, set[int]] = defaultdict(set)
    for items in par_famille_items.values():
        for it in items:
            if it.get("collection"):
                lig = it.get("lignee") or _lignee(it["producteur"])
                annees_lignee[lig].update(it.get("annees") or [])
            else:
                ys = _annees_titre(it["titre"])
                if len(ys) == 1:
                    annees_lignee[_lignee(it["producteur"])].add(ys[0])
    for items in par_famille_items.values():
        for it in items:
            if it.get("manquants"):
                connues = annees_lignee[it.get("lignee") or _lignee(it["producteur"])]
                it["manquants"] = [y for y in it["manquants"] if y not in connues]


def _rendre_collection(c: dict) -> str:
    """Ligne Markdown d'une entrée condensée : libellé, producteur, éditions, manquants, années.

    Chaque année porte l'ancre `#src-<cle>` de son membre (lien si URL, sinon simple libellé
    ancré) : tous les renvois `#src-<cle>` de la collection restent résolvables.
    """
    tete = f"- **{c['titre']}** — {c['producteur']}".rstrip(" —")
    if c.get("explicite"):
        # Collection déclarée dans la table : étiquettes déjà calculées (ordinal, année ou label).
        corps = f"{len(c['membres'])} {c['nature']}"
        if c["annees"]:
            corps += f" ({min(c['annees'])}{_TIRET}{max(c['annees'])})" if min(c["annees"]) != max(c["annees"]) else f" ({c['annees'][0]})"
        avec_url = any(d["url"] for _, d in c["membres"])
        liens = [
            f"[{lab}]({d['url']}){{#src-{d['cle']}}}" if d["url"] else f"[{lab}]{{#src-{d['cle']}}}"
            for lab, d in c["membres"]
        ]
        return f"{tete}. {corps}. Accès : " + ", ".join(liens) + "."
    n = len(c["annees"])
    if c["amin"] == c["amax"]:
        corps = f"édition {c['amin']}" + (f" ({len(c['membres'])} variantes)" if len(c["membres"]) > 1 else "")
    else:
        corps = f"{n} éditions ({c['amin']}{_TIRET}{c['amax']})"
    if c["manquants"]:
        corps += ", manque " + ", ".join(str(y) for y in c["manquants"])
    avec_url = any(d["url"] for _, d in c["membres"])
    liens = [
        f"[{a}]({d['url']}){{#src-{d['cle']}}}" if d["url"] else f"[{a}]{{#src-{d['cle']}}}"
        for a, d in c["membres"]
    ]
    etiquette = "Accès par année" if avec_url else "Éditions"
    return f"{tete}. {corps}. {etiquette} : " + ", ".join(liens) + "."


def _nom_producteur(items: list[dict]) -> str:
    """Nom de producteur représentatif d'un groupe : la forme la plus courte (sans suffixes)."""
    noms = [it["producteur"] for it in items if it["producteur"]]
    return min(noms, key=len) if noms else "—"


def _rendre_item(it: dict) -> str:
    """Ligne Markdown d'un item : collection condensée ou source isolée (ancre `#src-<cle>`)."""
    if it.get("collection"):
        return _rendre_collection(it)
    ligne = f"- []{{#src-{it['cle']}}}**{it['titre']}** — {it['producteur']}".rstrip(" —")
    if it["url"]:
        ligne += f". [Accès]({it['url']})"
    return ligne


def rendre() -> None:
    """Émet (print) tout le corps Markdown de l'annexe, sous `#| output: asis`."""
    par_famille, inconnues, types_inattendus = collecter()
    n_sources = sum(len(v) for v in par_famille.values())
    n_familles = len(par_famille)

    # 1) Regroupements sémantiques explicites (table versionnée), retirés de par_famille.
    coll_explicites = _appliquer_table(par_famille)
    # 2) Condensation algorithmique (collections annuelles) sur le reste, famille par famille.
    ordre = list(par_famille) + [f for f in coll_explicites if f not in par_famille]
    par_famille_items: dict[str, list[dict]] = {}
    for nom in ordre:
        items = _grouper(par_famille.get(nom, [])) + coll_explicites.get(nom, [])
        items.sort(key=lambda it: (_sans_accents(it["producteur"]), _sans_accents(it["titre"])))
        if items:
            par_famille_items[nom] = items
    _filtrer_manquants(par_famille_items)
    n_entrees = sum(len(v) for v in par_famille_items.values())
    n_collections = sum(1 for v in par_famille_items.values() for it in v if it.get("collection"))

    out: list[str] = []
    noms = list(par_famille)
    liste_fam = ", ".join(noms[:-1]) + (" et " + noms[-1] if len(noms) > 1 else noms[0])
    out.append(
        f"Cette annexe recense **{n_sources} supports de données chiffrées**, condensés en "
        f"**{n_entrees} entrées** : les collections — séries répétées d'année en année, séries "
        f"numérotées, ou pièces d'un même dossier — sont regroupées en une entrée portant son "
        f"intervalle d'années (et, pour les séries annuelles, les années manquantes), sans masquer "
        f"les pièces distinctes ({n_collections} collections ainsi regroupées). Le tout se répartit "
        f"en **{n_familles} familles** : {liste_fam}. Chaque support garde son ancre stable "
        "`#src-<clé>` à laquelle les volumes et les figures renvoient — y compris, dans une entrée "
        "condensée, pièce par pièce.\n"
    )
    sous_groupes = {f["nom"] for f in _charger_familles() if f.get("sous_groupes_par_producteur")}
    for nom, items in par_famille_items.items():
        out.append(f"\n### {nom} ({len(items)}) {{#src-fam-{_slug(nom)}}}\n")
        if nom in sous_groupes:
            # Famille multi-producteurs : une sous-section par producteur (p. ex. chaque caisse,
            # chaque société), ses séries regroupées dessous. On n'y FUSIONNE rien de plus.
            from collections import defaultdict
            groupes: dict[str, list[dict]] = defaultdict(list)
            for it in items:
                groupes[_lignee(it["producteur"])].append(it)
            for lig in sorted(groupes, key=lambda l: _sans_accents(_nom_producteur(groupes[l]))):
                grp = groupes[lig]
                out.append(f"#### {_nom_producteur(grp)} ({len(grp)})\n")
                for it in sorted(grp, key=lambda it: _sans_accents(it["titre"])):
                    out.append(_rendre_item(it))
                out.append("")
        else:
            for it in items:
                out.append(_rendre_item(it))
            out.append("")

    # Signalement (hors texte publié) : clés citées mais absentes de references.json,
    # et types CSL inattendus. En commentaire HTML + sur stderr.
    if inconnues:
        out.append("\n<!-- clés citées dans un manifeste de figure mais ABSENTES de "
                   "references.json (à corriger dans la source, non ici) : "
                   + ", ".join(inconnues) + " -->")
        print(f"[annexe_sources] {len(inconnues)} clé(s) citée(s) non résolue(s) : "
              + ", ".join(inconnues), file=sys.stderr)
    if types_inattendus:
        out.append("\n<!-- types CSL inattendus (listés par prudence, à trier) : "
                   + ", ".join(types_inattendus) + " -->")
        print(f"[annexe_sources] types CSL inattendus : " + ", ".join(types_inattendus),
              file=sys.stderr)

    print("\n".join(out))


if __name__ == "__main__":
    rendre()

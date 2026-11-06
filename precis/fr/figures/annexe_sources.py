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
  5. CONDENSE les COLLECTIONS ANNUELLES. Beaucoup de supports sont la même série répétée par
     année (« Rapport sur les entreprises publiques (annexe 9 au PLF pour 2020, 2021, … » ;
     « Budget du ministère du Transport pour l'année 2013 … 2017 » ; « تقرير المالية العمومية
     لسنة 2005, 2008 »). Chaque année = une clé → une liste interminable. On regroupe, DANS
     CHAQUE FAMILLE, les sources d'une même collection en UNE entrée (voir `_grouper`) :
       - sous-type / radical = le titre privé de son (ses) token(s) d'année 19xx/20xx, comparé
         sans accents ni casse, APPARIÉ AU MÊME PRODUCTEUR. Deux titres qui se réduisent au même
         radical pour le même producteur = une collection ;
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


def _radical(titre: str) -> str:
    """Radical d'un titre : son texte privé des tokens d'année, sans accents ni casse.

    C'est la clé de collection : deux titres d'un même producteur qui ne diffèrent que par
    l'année se réduisent au même radical.
    """
    r = _ANNEE.sub("\u00a7", titre)
    return _sans_accents(re.sub(r"\s+", " ", r).strip())


def _collection(membres: list[tuple[int, dict]]) -> dict:
    """Construit une entrée de collection à partir de ses membres `(annee, source)`.

    Libellé = titre du membre le plus récent, son token d'année remplacé par l'intervalle.
    Manquants = années absentes de [min, max], mais seulement si la cadence est établie.
    """
    membres = sorted(membres, key=lambda t: t[0])
    annees = [a for a, _ in membres]
    amin, amax = annees[0], annees[-1]
    recent = membres[-1][1]
    libelle = _ANNEE.sub(f"{amin}{_TIRET}{amax}", recent["titre"]) if amin != amax else recent["titre"]
    present = set(annees)
    etendue = amax - amin + 1
    manquants = [y for y in range(amin, amax + 1) if y not in present]
    etablie = len(present) >= _EDITIONS_MIN and etendue > 0 and len(present) / etendue >= _DENSITE_MIN
    if not etablie:
        manquants = []   # trop clairsemé : on ne postule pas une complétude annuelle
    url = recent["url"] or next((d["url"] for _, d in reversed(membres) if d["url"]), "")
    return {
        "collection": True,
        "titre": libelle,
        "producteur": recent["producteur"],
        "url": url,
        "membres": membres,
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
        cle_groupe = (_radical(d["titre"]), _sans_accents(d["producteur"])) if len(annees) == 1 \
            else ("\x00iso\x00" + d["cle"], "")   # titre sans/à plusieurs années : isolé d'office
        groupes[cle_groupe].append((annees, d))
    items: list[dict] = []
    for membres in groupes.values():
        annees = [a[0] for a, _ in membres if len(a) == 1]
        if len(membres) >= 2 and len(annees) == len(membres) and len(set(annees)) == len(membres):
            items.append(_collection([(a[0], d) for a, d in membres]))
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
        })
    for nom in ordre:
        par_famille[nom].sort(key=lambda d: (_sans_accents(d["producteur"]), _sans_accents(d["titre"])))
    # Familles vides retirées, ordre conservé.
    par_famille = {nom: par_famille[nom] for nom in ordre if par_famille[nom]}
    return par_famille, sorted(set(inconnues)), sorted(set(types_inattendus))


def _rendre_collection(c: dict) -> str:
    """Ligne Markdown d'une entrée condensée : libellé, producteur, éditions, manquants, années.

    Chaque année porte l'ancre `#src-<cle>` de son membre (lien si URL, sinon simple libellé
    ancré) : tous les renvois `#src-<cle>` de la collection restent résolvables.
    """
    tete = f"- **{c['titre']}** — {c['producteur']}".rstrip(" —")
    corps = f"{len(c['membres'])} éditions ({c['amin']}{_TIRET}{c['amax']})"
    if c["manquants"]:
        corps += ", manque " + ", ".join(str(y) for y in c["manquants"])
    avec_url = any(d["url"] for _, d in c["membres"])
    liens = [
        f"[{a}]({d['url']}){{#src-{d['cle']}}}" if d["url"] else f"[{a}]{{#src-{d['cle']}}}"
        for a, d in c["membres"]
    ]
    etiquette = "Accès par année" if avec_url else "Éditions"
    return f"{tete}. {corps}. {etiquette} : " + ", ".join(liens) + "."


def rendre() -> None:
    """Émet (print) tout le corps Markdown de l'annexe, sous `#| output: asis`."""
    par_famille, inconnues, types_inattendus = collecter()
    n_sources = sum(len(v) for v in par_famille.values())
    n_familles = len(par_famille)

    # Condensation des collections annuelles, famille par famille.
    par_famille_items = {nom: _grouper(entrees) for nom, entrees in par_famille.items()}
    n_entrees = sum(len(v) for v in par_famille_items.values())
    n_collections = sum(1 for v in par_famille_items.values() for it in v if it.get("collection"))

    out: list[str] = []
    noms = list(par_famille)
    liste_fam = ", ".join(noms[:-1]) + (" et " + noms[-1] if len(noms) > 1 else noms[0])
    out.append(
        f"Cette annexe recense **{n_sources} supports de données chiffrées**, condensés en "
        f"**{n_entrees} entrées** : les collections annuelles — une même série répétée d'année en "
        f"année — sont regroupées en une entrée portant son intervalle d'années et, quand la "
        f"cadence annuelle est établie, les années manquantes ({n_collections} collections ainsi "
        f"regroupées). Le tout se répartit en **{n_familles} familles** : {liste_fam}. Chaque "
        "support garde son ancre stable `#src-<clé>` à laquelle les volumes et les figures "
        "renvoient — y compris, dans une entrée condensée, année par année.\n"
    )
    for nom, items in par_famille_items.items():
        out.append(f"\n### {nom} ({len(items)}) {{#src-fam-{_slug(nom)}}}\n")
        for it in items:
            if it.get("collection"):
                out.append(_rendre_collection(it))
            else:
                ligne = f"- []{{#src-{it['cle']}}}**{it['titre']}** — {it['producteur']}".rstrip(" —")
                if it["url"]:
                    ligne += f". [Accès]({it['url']})"
                out.append(ligne)
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

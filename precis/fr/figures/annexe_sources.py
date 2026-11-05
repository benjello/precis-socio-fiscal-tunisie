"""Annexe engendrée « Les sources de données chiffrées » (`precis/fr/annexe-sources.qmd`).

    from figures import annexe_sources
    annexe_sources.rendre()   # émet tout le corps : une sous-section par famille, une entrée par source

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
  5. Émet le corps GROUPÉ par famille (sous-section `###`, ancre `#src-fam-<slug>`), puis par
     source — ancre STABLE `#src-<cle>` à laquelle les livres et les onglets « 🔗 Sources » des
     figures renverront. Par source : titre, producteur, et lien d'accès (URL publique) si
     references.json en porte une.

RÈGLES (le précis l'exige).
  - **Rien de fabriqué.** Titre, producteur et URL sont LUS dans references.json ; une
    métadonnée absente (souvent l'URL) est laissée vide, jamais inventée.
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


def rendre() -> None:
    """Émet (print) tout le corps Markdown de l'annexe, sous `#| output: asis`."""
    par_famille, inconnues, types_inattendus = collecter()
    n_sources = sum(len(v) for v in par_famille.values())
    n_familles = len(par_famille)

    out: list[str] = []
    noms = list(par_famille)
    liste_fam = ", ".join(noms[:-1]) + (" et " + noms[-1] if len(noms) > 1 else noms[0])
    out.append(
        f"Cette annexe liste **{n_sources} supports de données chiffrées**, répartis en "
        f"**{n_familles} familles** : {liste_fam}. Chaque source porte une ancre stable "
        "`#src-<clé>` à laquelle les volumes et les figures renvoient.\n"
    )
    for nom, entrees in par_famille.items():
        out.append(f"\n### {nom} ({len(entrees)}) {{#src-fam-{_slug(nom)}}}\n")
        for d in entrees:
            ligne = f"- []{{#src-{d['cle']}}}**{d['titre']}** — {d['producteur']}".rstrip(" —")
            if d["url"]:
                ligne += f". [Accès]({d['url']})"
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

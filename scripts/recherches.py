"""Les recherches infructueuses : hors du texte, conservées, et rejouables.

Le précis ne raconte pas ses recherches (`docs/conventions-redaction.md`, § 2). Quand un
texte attendu n'est pas identifié — un décret d'application, un modificatif —, le texte
rendu dit le constat, court et neutre (« ce décret n'est pas identifié ici »), et porte à
côté une ancre cachée :

    <!-- RECHERCHE r-dl2024-4-art33 : décret d'application de l'art. 33 (voir docs/recherches.yml) -->

L'ancre renvoie à une fiche de `docs/recherches.yml`, dont la trace est une REQUÊTE, pas
une phrase : ce qu'on a cherché, dans quelles sources, jusqu'où, avec quel résultat. Ce
script la tient et la rejoue :

    uv run python scripts/recherches.py verifier
    uv run python scripts/recherches.py lister [--perimees]
    uv run python scripts/recherches.py relancer <id> | --perimees [--depuis AAAA-MM-JJ]
    uv run python scripts/recherches.py elargir <id> --terme "…" [--source titres_fts]
    uv run python scripts/recherches.py passe <id> --resultat aucun|<clé CSL> \\
        --couverture "…" --couvert-jusqu-au AAAA-MM-JJ --sources jort_cache corpus_local

`verifier` ne lit que le dépôt : c'est lui que la CI lance. Les autres sous-commandes
lisent des sources LOCALES (`docs/notes/outillage-sources.md`) : `jort_cache.db`, le
miroir iort et le corpus des fascicules de `~/projets/PDFs-legislation-tunisie`, dont on
peut changer l'emplacement par `PDFS_LEGISLATION` (et `JORT_CACHE_DB` pour la base).

`relancer` rend des CANDIDATS, jamais une conclusion : un candidat se lit au fascicule, et
une absence de candidat ne vaut que pour les sources et la période effectivement
parcourues, que la sortie énumère — avec ce qui n'a pas pu l'être.

Réécriture du registre. `ruamel.yaml` n'est pas une dépendance du projet : `elargir` et
`passe` réécrivent donc `docs/recherches.yml` sous une forme CANONIQUE (ordre des clés
fixe, une ligne vide entre fiches, listes de termes en ligne). Le bloc de commentaires
d'en-tête est conservé ; un commentaire placé À L'INTÉRIEUR d'une fiche serait perdu —
d'où la règle, rappelée dans l'en-tête du registre : pas de commentaire dans les fiches.
Un test vérifie que le registre versionné est déjà sous forme canonique, pour que chaque
réécriture ne touche que ce qu'elle change.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
REGISTRE = RACINE / "docs" / "recherches.yml"
PDFS_LEGISLATION = Path(
    os.environ.get("PDFS_LEGISLATION", Path.home() / "projets" / "PDFs-legislation-tunisie")
)
PIST = "https://www.pist.tn"

# ---------------------------------------------------------------------------
# Schéma
# ---------------------------------------------------------------------------

CLES_FICHE = ["id", "objet", "ou", "requetes", "passes", "a_faire", "resolu"]
OBLIGATOIRES_FICHE = ["id", "objet", "ou", "requetes", "passes"]
CLES_REQUETES = ["titres_fts", "titres_like", "iort_ar", "plein_texte", "depuis"]
SOURCES_DE_TERMES = ["titres_fts", "titres_like", "iort_ar", "plein_texte"]
CLES_PASSE = ["date", "role", "sources", "couverture", "couvert_jusqu_au", "resultat"]
CHAMPS_DATES_PASSE = ["date", "couvert_jusqu_au"]
SOURCES_CONNUES = {
    "jort_cache",    # métadonnées : ~/projets/PDFs-legislation-tunisie/jort_cache.db
    "iort",          # miroir iort.tn : data/iort/textes/md/
    "corpus_local",  # fascicules locaux : PDFs/JORT/, markdown_output/JORT/
    "pist",          # fascicules lus sur pist.tn
    "mcp_jort",      # serveur MCP `jort` (métadonnées)
    "visas",         # seconde voie : visas des textes ultérieurs
    "presse",        # source secondaire
}
RE_ID = re.compile(r"^r-[a-z0-9][a-z0-9.-]*$")
RE_ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RE_ANCRE = re.compile(r"<!--\s*RECHERCHE\s+(\S+)")


def iso(valeur) -> str | None:
    """Rend une date ISO `AAAA-MM-JJ` valide, ou None. Accepte `datetime.date` (PyYAML)."""
    if isinstance(valeur, dt.date):
        return valeur.isoformat()
    if isinstance(valeur, str) and RE_ISO.match(valeur):
        try:
            dt.date.fromisoformat(valeur)
        except ValueError:
            return None
        return valeur
    return None


def normalise_fiches(fiches: list[dict]) -> list[dict]:
    """Remplace les `datetime.date` chargés par PyYAML par des chaînes ISO."""
    for fiche in fiches:
        req = fiche.get("requetes")
        if isinstance(req, dict) and isinstance(req.get("depuis"), dt.date):
            req["depuis"] = req["depuis"].isoformat()
        for passe in fiche.get("passes") or []:
            if isinstance(passe, dict):
                for cle in CHAMPS_DATES_PASSE:
                    if isinstance(passe.get(cle), dt.date):
                        passe[cle] = passe[cle].isoformat()
    return fiches


def chemins_ou(fiche: dict) -> list[str]:
    ou = fiche.get("ou")
    if isinstance(ou, str):
        return [ou]
    return [o for o in ou or [] if isinstance(o, str)]


# ---------------------------------------------------------------------------
# Lecture et écriture du registre
# ---------------------------------------------------------------------------


def _yaml():
    try:
        import yaml
    except ImportError:
        print("PyYAML requis : lancer par `uv run python scripts/recherches.py …`.")
        raise SystemExit(1)
    return yaml


def charger(chemin: Path = REGISTRE) -> tuple[str, list[dict]]:
    """Rend (en-tête de commentaires, fiches)."""
    texte = chemin.read_text(encoding="utf-8")
    entete = []
    for ligne in texte.splitlines(keepends=True):
        if ligne.startswith("#") or not ligne.strip():
            entete.append(ligne)
        else:
            break
    donnees = _yaml().safe_load(texte) or []
    if not isinstance(donnees, list):
        raise SystemExit(f"{chemin} : le registre doit être une liste de fiches.")
    return "".join(entete).rstrip("\n") + "\n", normalise_fiches(donnees)


def _ordonne(d: dict, ordre: list[str]) -> dict:
    sortie = {k: d[k] for k in ordre if k in d}
    sortie.update({k: v for k, v in d.items() if k not in sortie})
    return sortie


def _pour_dump(fiche: dict) -> dict:
    fiche = _ordonne(fiche, CLES_FICHE)
    if isinstance(fiche.get("requetes"), dict):
        req = _ordonne(fiche["requetes"], CLES_REQUETES)
        if iso(req.get("depuis")):
            req["depuis"] = dt.date.fromisoformat(iso(req["depuis"]))
        fiche["requetes"] = req
    passes = []
    for passe in fiche.get("passes") or []:
        passe = _ordonne(passe, CLES_PASSE)
        for cle in CHAMPS_DATES_PASSE:
            if iso(passe.get(cle)):
                passe[cle] = dt.date.fromisoformat(iso(passe[cle]))
        passes.append(passe)
    if "passes" in fiche:
        fiche["passes"] = passes
    return fiche


def formate(entete: str, fiches: list[dict]) -> str:
    """Forme canonique du registre (voir la note en tête de module)."""
    yaml = _yaml()

    class Dumper(yaml.SafeDumper):
        pass

    def liste(dumper, donnees):
        # Listes de scalaires en ligne (termes, sources) ; listes d'objets en bloc.
        en_ligne = all(not isinstance(x, (dict, list)) for x in donnees)
        return dumper.represent_sequence("tag:yaml.org,2002:seq", donnees, flow_style=en_ligne)

    Dumper.add_representer(list, liste)
    blocs = [
        yaml.dump([_pour_dump(dict(f))], Dumper=Dumper, allow_unicode=True,
                  sort_keys=False, width=10_000, default_flow_style=False)
        for f in fiches
    ]
    return entete + "\n" + "\n".join(blocs)


def ecrire(entete: str, fiches: list[dict], chemin: Path = REGISTRE) -> None:
    chemin.write_text(formate(entete, fiches), encoding="utf-8")


# ---------------------------------------------------------------------------
# verifier
# ---------------------------------------------------------------------------


def fichiers_qmd(racine: Path = RACINE) -> list[Path]:
    return sorted(
        f for f in (racine / "precis" / "fr").rglob("*.qmd")
        if "/_book/" not in f.as_posix() and "/public/" not in f.as_posix()
    )


def ancres(fichiers: list[Path], racine: Path = RACINE) -> list[tuple[str, str, int]]:
    """(id, chemin relatif, ligne) de chaque ancre `<!-- RECHERCHE id … -->`."""
    trouvees = []
    for chemin in fichiers:
        for numero, ligne in enumerate(chemin.read_text(encoding="utf-8").splitlines(), 1):
            for m in RE_ANCRE.finditer(ligne):
                trouvees.append((m.group(1), chemin.relative_to(racine).as_posix(), numero))
    return trouvees


def erreurs_fiche(fiche) -> list[str]:
    if not isinstance(fiche, dict):
        return ["une fiche n'est pas un dictionnaire"]
    nom = fiche.get("id", "(sans id)")
    err = [f"{nom} : champ obligatoire manquant « {c} »"
           for c in OBLIGATOIRES_FICHE if fiche.get(c) in (None, "", [], {})]
    if "id" in fiche and not RE_ID.match(str(fiche["id"])):
        err.append(f"{nom} : id mal formé (attendu r-…, minuscules, chiffres, tirets)")
    inconnues = set(fiche) - set(CLES_FICHE)
    if inconnues:
        err.append(f"{nom} : clé(s) inconnue(s) {sorted(inconnues)}")
    ou = fiche.get("ou")
    if ou is not None and not (isinstance(ou, str) or (isinstance(ou, list) and ou)):
        err.append(f"{nom} : « ou » doit être un chemin ou une liste de chemins")
    req = fiche.get("requetes")
    if req is not None:
        if not isinstance(req, dict):
            err.append(f"{nom} : « requetes » doit être un dictionnaire")
        else:
            inconnues = set(req) - set(CLES_REQUETES)
            if inconnues:
                err.append(f"{nom} : requête(s) inconnue(s) {sorted(inconnues)}")
            if not any(req.get(s) for s in SOURCES_DE_TERMES):
                err.append(f"{nom} : aucune requête (titres_fts, titres_like, iort_ar, plein_texte)")
            for s in SOURCES_DE_TERMES:
                v = req.get(s)
                if v is not None and not (isinstance(v, list) and all(isinstance(t, str) for t in v)):
                    err.append(f"{nom} : requetes.{s} doit être une liste de chaînes")
            if "depuis" in req and not iso(req["depuis"]):
                err.append(f"{nom} : requetes.depuis n'est pas une date ISO AAAA-MM-JJ")
    passes = fiche.get("passes")
    if passes is not None and not isinstance(passes, list):
        err.append(f"{nom} : « passes » doit être une liste")
        passes = []
    for i, passe in enumerate(passes or [], 1):
        if not isinstance(passe, dict):
            err.append(f"{nom} : passe {i} n'est pas un dictionnaire")
            continue
        for c in CLES_PASSE:
            if passe.get(c) in (None, "", []):
                err.append(f"{nom} : passe {i}, champ obligatoire manquant « {c} »")
        for c in CHAMPS_DATES_PASSE:
            if passe.get(c) not in (None, "") and not iso(passe[c]):
                err.append(f"{nom} : passe {i}, « {c} » n'est pas une date ISO AAAA-MM-JJ")
        sources = passe.get("sources") or []
        if not isinstance(sources, list):
            err.append(f"{nom} : passe {i}, « sources » doit être une liste")
        else:
            for s in set(sources) - SOURCES_CONNUES:
                err.append(f"{nom} : passe {i}, source inconnue « {s} » "
                           f"(connues : {', '.join(sorted(SOURCES_CONNUES))})")
        inconnues = set(passe) - set(CLES_PASSE)
        if inconnues:
            err.append(f"{nom} : passe {i}, clé(s) inconnue(s) {sorted(inconnues)}")
    if "a_faire" in fiche and not (isinstance(fiche["a_faire"], list)
                                   and all(isinstance(t, str) for t in fiche["a_faire"])):
        err.append(f"{nom} : « a_faire » doit être une liste de chaînes")
    return err


def verifie(fiches: list, racine: Path = RACINE, fichiers: list[Path] | None = None) -> list[str]:
    """Toutes les incohérences entre le registre et les ancres des `.qmd` français."""
    fichiers = fichiers_qmd(racine) if fichiers is None else fichiers
    erreurs = []
    vus = {}
    for fiche in fiches:
        erreurs += erreurs_fiche(fiche)
        if isinstance(fiche, dict) and "id" in fiche:
            if fiche["id"] in vus:
                erreurs.append(f"{fiche['id']} : id en double")
            vus[fiche["id"]] = fiche

    trouvees = ancres(fichiers, racine)
    ids_ancres = {a for a, _, _ in trouvees}
    for id_, rel, numero in trouvees:
        if id_ not in vus:
            erreurs.append(f"{rel}:{numero} : ancre orpheline — aucune fiche « {id_} » dans docs/recherches.yml")
        elif vus[id_].get("resolu"):
            erreurs.append(f"{rel}:{numero} : la fiche « {id_} » est résolue ({vus[id_]['resolu']}) — "
                           "remplacer la réserve par la règle sourcée et retirer l'ancre")
    for id_, fiche in vus.items():
        if fiche.get("resolu"):
            continue
        if id_ not in ids_ancres:
            erreurs.append(f"{id_} : fiche orpheline — aucune ancre <!-- RECHERCHE {id_} … --> dans precis/fr")
            continue
        for ou in chemins_ou(fiche):
            chemin, _, ancre = ou.partition("#")
            fichier = racine / chemin
            if not fichier.exists():
                erreurs.append(f"{id_} : « ou » désigne un fichier absent : {chemin}")
                continue
            texte = fichier.read_text(encoding="utf-8")
            if not re.search(rf"<!--\s*RECHERCHE\s+{re.escape(id_)}\b", texte):
                erreurs.append(f"{id_} : l'ancre n'est pas dans le fichier désigné par « ou » ({chemin})")
            if ancre and "{#" + ancre not in texte and "{" + "#" + ancre + " " not in texte:
                erreurs.append(f"{id_} : l'ancre de section #{ancre} n'existe pas dans {chemin}")
    return erreurs


# ---------------------------------------------------------------------------
# Normalisation : une seule, pour la botte de foin et pour l'aiguille
# ---------------------------------------------------------------------------

# Les marques bidirectionnelles deviennent des espaces, non des riens : `pdftotext` les
# pose entre un chiffre et le mot qui le suit sans autre séparation (« ‪ 28‬جانفي »).
# Le tatweel et l'espace insécable de largeur nulle, eux, sont intérieurs au mot.
_BIDI = {
    **dict.fromkeys([0x200E, 0x200F, 0x061C, *range(0x202A, 0x202F), *range(0x2066, 0x206A)], " "),
    0x0640: None,
    0xFEFF: None,
}
_ESPACES = re.compile(r"\s+")
_APOSTROPHES = str.maketrans({"’": "'", "‘": "'", "ʼ": "'", "–": "-", "—": "-", "‑": "-"})


def sans_accents(texte) -> str:
    """Minuscules, sans diacritiques (accents français, harakat et chadda arabes), sans
    marques bidirectionnelles ni tatweel, espaces réduites à une seule.

    C'est la même normalisation pour ce qu'on cherche et pour ce qu'on parcourt : une
    requête `LIKE` accentuée ne manque plus les titres non accentués de `jort_cache`
    (`docs/notes/outillage-sources.md`, § 1 c), et « 6 لسنة 1981 » se trouve malgré les
    marques bidirectionnelles de `pdftotext` (§ 12 de la note cnss-autres-regimes).
    """
    if texte is None:
        return ""
    t = unicodedata.normalize("NFKD", str(texte).translate(_BIDI))
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return _ESPACES.sub(" ", t.translate(_APOSTROPHES)).strip().lower()


def motif(terme: str) -> re.Pattern:
    """Motif de recherche d'un terme normalisé. Un terme qui commence ou finit par un
    chiffre ne se prolonge pas en chiffres : « 2024-4 » ne trouve ni « 2024-48 » ni
    « 2024-465 ». Aucune autre borne : l'arabe colle ses particules au mot, et
    « والعاملات » doit répondre à « العاملات ». Mais « ل » suivi de l'article s'écrit
    « لل » (« للعاملات ») : l'alif tombe, et seul un terme sans article (« عاملات
    الفلاحيات ») couvre aussi cette forme."""
    t = sans_accents(terme)
    avant = r"(?<!\d)" if t[:1].isdigit() else ""
    apres = r"(?!\d)" if t[-1:].isdigit() else ""
    return re.compile(avant + re.escape(t) + apres)


def phrase_fts(terme: str) -> str:
    """Terme libre → requête FTS5 à une phrase (« 2024-4 » non cité casse FTS5)."""
    mots = re.sub(r"[%_*\"]", " ", terme).split()
    return '"' + " ".join(mots) + '"' if mots else ""


def like_depuis_fts(expr: str) -> str | None:
    """Une requête FTS réduite à UNE phrase ou un mot se double d'un LIKE ; une
    expression booléenne ne se traduit pas en LIKE sans trahison : None."""
    e = expr.strip()
    if re.fullmatch(r'"[^"]+"', e) or re.fullmatch(r"[^\s\"()]+", e):
        if e.upper() in {"AND", "OR", "NOT", "NEAR"}:
            return None
        return "%" + e.strip('"') + "%"
    return None


# ---------------------------------------------------------------------------
# Sources
# ---------------------------------------------------------------------------


def chemin_base() -> Path:
    return Path(os.environ.get("JORT_CACHE_DB", PDFS_LEGISLATION / "jort_cache.db"))


def ouvre_base(chemin: Path) -> sqlite3.Connection:
    """Lecture seule, sans verrou (`immutable=1`), avec la normalisation en SQL."""
    cnx = sqlite3.connect(f"file:{chemin}?immutable=1", uri=True)
    cnx.create_function("sans_accents", 1, sans_accents, deterministic=True)
    cnx.row_factory = sqlite3.Row
    return cnx


def derniere_publication(cnx: sqlite3.Connection) -> str | None:
    return cnx.execute(
        "select max(date_publication) from textes where jort_annee between 1956 and 2100"
    ).fetchone()[0]


COLONNES = ("t.recid, t.type, coalesce(t.numero, '') as numero, t.titre, t.date_publication, "
            "t.jort_annee, t.jort_numero, t.pages, t.pdf_fr, t.pdf_ar")


def cherche_base(cnx: sqlite3.Connection, requetes: dict, seuil: str) -> tuple[dict, list[str]]:
    """Rend ({recid: (ligne, [voies])}, [avertissements]) pour les textes publiés à partir
    de `seuil` (inclus). Chaque terme est cherché par DEUX voies — FTS (insensible aux
    accents) et LIKE sur titre et objet normalisés — pour qu'un faux négatif de l'une ne
    fasse pas conclure à l'absence."""
    candidats: dict[int, tuple[sqlite3.Row, list[str]]] = {}
    avert = []

    def ajoute(lignes, voie):
        for ligne in lignes:
            candidats.setdefault(ligne["recid"], (ligne, []))[1].append(voie)

    def fts(expr, voie):
        if not expr:
            return
        try:
            ajoute(cnx.execute(
                f"select {COLONNES} from textes_fts f join textes t on t.recid = f.rowid "
                "where textes_fts match ? and t.date_publication >= ? "
                "and t.jort_annee between 1956 and 2100", (expr, seuil)), voie)
        except sqlite3.OperationalError as e:
            avert.append(f"requête FTS refusée par SQLite ({voie}) : {e}")

    def like(motif, voie):
        m = sans_accents(motif)
        if "%" not in m:
            m = f"%{m}%"
        ajoute(cnx.execute(
            f"select {COLONNES} from textes t where t.date_publication >= ? "
            "and t.jort_annee between 1956 and 2100 "
            "and (sans_accents(t.titre) like ? or sans_accents(t.objet) like ?)",
            (seuil, m, m)), voie)

    for expr in requetes.get("titres_fts") or []:
        fts(expr, f"fts {expr}")
        derive = like_depuis_fts(expr)
        if derive:
            like(derive, f"like {derive} (doublant fts)")
    for motif in requetes.get("titres_like") or []:
        like(motif, f"like {motif}")
        fts(phrase_fts(motif), f"fts {phrase_fts(motif)} (doublant like)")
    for terme in requetes.get("iort_ar") or []:
        like(terme, f"like {terme} (titre arabe)")
        fts(phrase_fts(terme), f"fts {phrase_fts(terme)} (titre arabe)")
    return candidats, avert


RE_ANNEE_IORT = re.compile(r"_(\d{4})\.md$")


def intitules_iort(texte: str) -> tuple[str, str, str]:
    """(intitulé arabe, intitulé français, corps arabe) d'un fichier du miroir iort.

    Deux formes coexistent (`outillage-sources.md`, § 2) : l'ancienne n'a que l'habillage
    du site et l'intitulé arabe, première ligne non vide après le marqueur `دليل` ; la
    récente porte le texte intégral sous `## Version française` et `## النسخة العربية`,
    et son premier `دليل` est celui du pied de page."""
    lignes = texte.splitlines()
    ar = fr = corps_ar = ""
    for i, l in enumerate(lignes):
        if l.strip() == "## Version française":
            fr = next((x.strip() for x in lignes[i + 1:] if x.strip()), "")
            break
    if "## النسخة العربية" in texte:
        section = texte.split("## النسخة العربية", 1)[1]
        corps_ar = section.split("\nالرائد  الرسمي للقوانين", 1)[0]
    for i, l in enumerate(lignes):
        if l.strip() == "دليل":
            suivant = next((x.strip() for x in lignes[i + 1:] if x.strip()), "")
            if suivant and suivant != "الجديد":
                ar = suivant
            break
    if fr:  # forme récente : le corps arabe est le texte, pas l'habillage
        return ar, fr, corps_ar
    return ar, fr, ""


def cherche_iort(dossier: Path, termes: list[str], annee_min: int) -> tuple[list, str]:
    """Rend ([(fichier, intitulé, voies)], bilan). Filtre sur l'année du NOM de fichier,
    qui est celle du texte, faute de date de publication dans le miroir."""
    if not termes:
        return [], "iort : aucun terme (requetes.iort_ar vide)"
    if not dossier.is_dir():
        return [], f"iort : miroir absent ({dossier}) — source NON parcourue"
    aiguilles = [(t, motif(t)) for t in termes]
    trouves, lus = [], 0
    for f in sorted(dossier.glob("*.md")):
        m = RE_ANNEE_IORT.search(f.name)
        if not m or int(m.group(1)) < annee_min:
            continue
        lus += 1
        ar, fr, corps = intitules_iort(f.read_text(encoding="utf-8", errors="replace"))
        voies = []
        for brut, t in aiguilles:
            if t.search(sans_accents(ar)) or t.search(sans_accents(fr)):
                voies.append(f"intitulé : {brut}")
            elif corps and t.search(sans_accents(corps)):
                voies.append(f"texte arabe : {brut}")
        if voies:
            trouves.append((f.name, ar or fr, voies))
    return trouves, (f"iort : {lus} fichier(s) de textes datés de {annee_min} ou après, "
                     "intitulés (et texte arabe quand le miroir le porte)")


RE_FASCICULE = re.compile(r"^J([oa])(\d{3})(\d{2}|\d{4})\.(pdf|md)$")


def fascicules_locaux(racine: Path, annees: range) -> dict:
    """{(année, langue, n°): chemin}, le Markdown l'emportant sur le PDF."""
    trouves = {}
    for sous, ext in (("PDFs/JORT", "pdf"), ("markdown_output/JORT", "md")):
        for annee in annees:
            for langue in ("fr", "ar"):
                d = racine / sous / str(annee) / langue
                if not d.is_dir():
                    continue
                for f in d.glob(f"*.{ext}"):
                    m = RE_FASCICULE.match(f.name)
                    if m:
                        trouves[(annee, langue, int(m.group(2)))] = f
    return trouves


def _cache_texte(pdf: Path) -> Path:
    base = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "precis-recherches"
    try:
        rel = pdf.resolve().relative_to(PDFS_LEGISLATION.resolve())
    except ValueError:
        rel = Path(pdf.name)
    return base / rel.with_suffix(".txt")


def texte_de(fichier: Path) -> str | None:
    """Texte d'un fascicule : Markdown tel quel, PDF par `pdftotext` (mis en cache)."""
    if fichier.suffix == ".md":
        return fichier.read_text(encoding="utf-8", errors="replace")
    cache = _cache_texte(fichier)
    if cache.exists() and cache.stat().st_mtime >= fichier.stat().st_mtime:
        return cache.read_text(encoding="utf-8", errors="replace")
    if not shutil.which("pdftotext"):
        return None
    r = subprocess.run(["pdftotext", "-q", str(fichier), "-"], capture_output=True)
    if r.returncode != 0:
        return None
    texte = r.stdout.decode("utf-8", errors="replace")
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(texte, encoding="utf-8")
    return texte


def url_fascicule(annee: int, langue: str, numero: int) -> str:
    """Convention de `outillage-sources.md`, § 3 ; l'arabe de 2000 est en deux chiffres."""
    lettre, prefixe = ("F", "Jo") if langue == "fr" else ("A", "Ja")
    aa = f"{annee % 100:02d}" if annee < 2000 or (annee == 2000 and langue == "ar") else str(annee)
    return f"{PIST}/jort/{annee}/{annee}{lettre}/{prefixe}{numero:03d}{aa}.pdf"


def cherche_plein_texte(racine: Path, termes: list[str], seuil: str,
                        dates: dict, jusqu_au: str | None) -> tuple[list, list[str]]:
    """Cherche les termes dans le texte des fascicules locaux parus à partir de `seuil`.

    `dates` : {(année, n°): date de publication} tiré de `jort_cache` ; un fascicule que la
    base ne connaît pas (postérieur à sa dernière mise à jour) est parcouru par prudence.
    Rend ([(année, langue, n°, page, extrait, url, fichier)], bilan)."""
    bilan = []
    if not termes:
        return [], ["plein texte : aucun terme (requetes.plein_texte vide)"]
    if not (racine / "PDFs" / "JORT").is_dir() and not (racine / "markdown_output" / "JORT").is_dir():
        return [], [f"plein texte : corpus local absent ({racine}) — source NON parcourue"]
    annee_min = int(seuil[:4])
    annees = range(annee_min, dt.date.today().year + 1)
    locaux = fascicules_locaux(racine, annees)
    retenus = {k: f for k, f in locaux.items() if date_fascicule(dates, k[0], k[2]) >= seuil}
    if not shutil.which("pdftotext") and any(f.suffix == ".pdf" for f in retenus.values()):
        bilan.append("plein texte : `pdftotext` absent — les PDF ne sont PAS lus")

    aiguilles = [(t, motif(t)) for t in termes]
    trouves, illisibles = [], []

    def examine(item):
        (annee, langue, numero), fichier = item
        texte = texte_de(fichier)
        if texte is None or len(texte.strip()) < 200:
            return item, None
        res = []
        for page, contenu in enumerate(texte.split("\f"), 1):
            norm = sans_accents(contenu)
            for brut, t in aiguilles:
                m = t.search(norm)
                if m:
                    i, j = m.span()
                    extrait = norm[max(0, i - 70): j + 70].strip()
                    res.append((annee, langue, numero, page, brut, extrait,
                                url_fascicule(annee, langue, numero), fichier))
        return item, res

    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as pool:
        for item, res in pool.map(examine, sorted(retenus.items())):
            if res is None:
                illisibles.append(item[0])
            else:
                trouves += res

    for annee in annees:
        for langue in ("fr", "ar"):
            n = sorted(k[2] for k in retenus if k[0] == annee and k[1] == langue)
            connus = sorted({num for (a, num), d in dates.items() if a == annee and d >= seuil})
            manquants = [x for x in connus if (annee, langue, x) not in locaux]
            tous = [k[2] for k in locaux if k[0] == annee and k[1] == langue]
            if not n and not connus and not tous:
                continue
            ligne = f"plein texte {annee} {langue} : {len(n)} fascicule(s) lu(s)"
            if n:
                ligne += f" ({compacte(n)})"
            if tous:
                ligne += f" ; dernier fascicule local : n° {max(tous)}"
            if manquants:
                ligne += f" ; ABSENTS du corpus local, connus de jort_cache : {compacte(manquants)}"
            if 2000 <= annee <= 2006:
                ligne += " ; années 2000-2006 : couche texte parfois décalée, un résultat nul n'y prouve rien"
            bilan.append(ligne)
    if jusqu_au:
        bilan.append(f"plein texte : au-delà du {jusqu_au} (fin de jort_cache), la liste des "
                     "fascicules parus n'est pas connue localement — les absences ne peuvent y être comptées")
    if illisibles:
        bilan.append("plein texte : sans texte exploitable (à océriser ou décoder) : "
                     + ", ".join(f"{a} {l} n° {n}" for a, l, n in sorted(illisibles)))
    return trouves, bilan


def date_fascicule(dates: dict, annee: int, numero: int) -> str:
    """Date de publication d'un fascicule d'après `jort_cache`, ou, s'il n'y est pas, la
    plus proche borne sûre : les numéros croissent avec les dates dans l'année, donc un
    fascicule antérieur à un numéro publié avant le seuil l'est aussi. Un numéro aberrant
    (`jort_cache` connaît un n° 107 de 2026 daté du 16 janvier) ne sert pas de borne : seuls
    comptent les numéros suivants dont la date ne précède pas celle des numéros antérieurs.
    Faute de borne, « 9999 » : le fascicule est parcouru par prudence."""
    if (annee, numero) in dates:
        return dates[(annee, numero)]
    anterieurs = [d for (a, n), d in dates.items() if a == annee and n < numero]
    plancher = max(anterieurs, default="")
    suivants = [d for (a, n), d in dates.items() if a == annee and n > numero and d >= plancher]
    return min(suivants) if suivants else "9999"


def compacte(nombres: list[int]) -> str:
    """[1, 2, 3, 5] → « 1-3, 5 »."""
    morceaux, debut = [], None
    for i, n in enumerate(nombres):
        if debut is None:
            debut = n
        if i + 1 == len(nombres) or nombres[i + 1] != n + 1:
            morceaux.append(str(debut) if debut == n else f"{debut}-{n}")
            debut = None
    return ", ".join(morceaux)


# ---------------------------------------------------------------------------
# lister, relancer, elargir, passe
# ---------------------------------------------------------------------------


def derniere_passe(fiche: dict) -> dict | None:
    passes = [p for p in fiche.get("passes") or [] if isinstance(p, dict)]
    return max(passes, key=lambda p: (iso(p.get("couvert_jusqu_au")) or "", iso(p.get("date")) or ""),
               default=None)


def est_perimee(fiche: dict, fin_base: str | None) -> bool:
    """Périmée : la dernière passe couvre moins loin que la dernière publication indexée."""
    if fiche.get("resolu") or not fin_base:
        return False
    p = derniere_passe(fiche)
    couvert = iso(p.get("couvert_jusqu_au")) if p else None
    return couvert is None or couvert < fin_base


def seuil_de(fiche: dict, depuis: str | None) -> str:
    """Premier jour à examiner : `--depuis`, sinon le lendemain de la couverture de la
    dernière passe, jamais avant `requetes.depuis`."""
    plancher = iso((fiche.get("requetes") or {}).get("depuis")) or "1956-01-01"
    if depuis:
        return depuis
    p = derniere_passe(fiche)
    couvert = iso(p.get("couvert_jusqu_au")) if p else None
    if not couvert:
        return plancher
    lendemain = (dt.date.fromisoformat(couvert) + dt.timedelta(days=1)).isoformat()
    return max(lendemain, plancher)


def localise(fiches: list[dict], racine: Path = RACINE) -> dict[str, str]:
    return {id_: f"{rel}:{n}" for id_, rel, n in ancres(fichiers_qmd(racine), racine)}


def cmd_lister(fiches, perimees_seules: bool) -> int:
    base = chemin_base()
    fin = None
    if base.exists():
        fin = derniere_publication(ouvre_base(base))
        print(f"jort_cache : dernière publication indexée le {fin}\n")
    else:
        print(f"jort_cache absent ({base}) : la péremption ne peut être évaluée.\n")
    ou = localise(fiches)
    n = 0
    for f in fiches:
        perimee = est_perimee(f, fin)
        if perimees_seules and not perimee:
            continue
        n += 1
        p = derniere_passe(f) or {}
        etat = f"résolue ({f['resolu']})" if f.get("resolu") else ("PÉRIMÉE" if perimee else "à jour")
        print(f"{f['id']} — {etat}")
        print(f"  objet   : {f.get('objet')}")
        print(f"  ancre   : {ou.get(f['id'], '(aucune)')}")
        print(f"  passe   : {p.get('date')} ({p.get('role')}), couvert jusqu'au "
              f"{p.get('couvert_jusqu_au')}, résultat : {p.get('resultat')}")
        print(f"  sources : {', '.join(p.get('sources') or [])}")
        print()
    print(f"{n} fiche(s)" + (" périmée(s)" if perimees_seules else "") + f" sur {len(fiches)}.")
    return 0


def relance(fiche: dict, depuis: str | None = None, plein_texte: bool = True,
            base: Path | None = None, corpus: Path | None = None) -> None:
    base = base or chemin_base()
    corpus = corpus or PDFS_LEGISLATION
    req = fiche.get("requetes") or {}
    seuil = seuil_de(fiche, depuis)
    print(f"=== {fiche['id']} — {fiche.get('objet')}")
    print(f"Textes publiés à partir du {seuil}. Des CANDIDATS, pas une conclusion : "
          "chacun se lit au fascicule.\n")

    dates, fin = {}, None
    print("--- jort_cache (métadonnées)")
    if not base.exists():
        print(f"  base absente ({base}) — source NON parcourue")
    else:
        cnx = ouvre_base(base)
        fin = derniere_publication(cnx)
        print(f"  dernière publication indexée : {fin}")
        if fin and fin < seuil:
            print(f"  → la base s'arrête AVANT le {seuil} : elle ne peut rien apporter de neuf ici.")
        candidats, avert = cherche_base(cnx, req, seuil)
        for a in avert:
            print(f"  ! {a}")
        for recid, (l, voies) in sorted(candidats.items(), key=lambda x: (x[1][0]["date_publication"], x[0])):
            print(f"  [{recid}] {l['type']} {l['numero'] or '(sans numéro)'} — publié le {l['date_publication']}"
                  f" — JORT n° {l['jort_numero']}/{l['jort_annee']}, p. {l['pages']}")
            print(f"      {l['titre']}")
            for cle in ("pdf_fr", "pdf_ar"):
                if l[cle]:
                    print(f"      {cle} : {PIST}{l[cle]}")
            print(f"      trouvé par : {' | '.join(dict.fromkeys(voies))}")
        print(f"  {len(candidats)} candidat(s).")
        if plein_texte:
            dates = {(a, n): d for a, n, d in cnx.execute(
                "select jort_annee, jort_numero, min(date_publication) from textes "
                "where jort_annee between ? and 2100 and jort_numero is not null "
                "group by jort_annee, jort_numero",
                (int(seuil[:4]),))}

    print("\n--- miroir iort (intitulés arabes)")
    trouves, bilan = cherche_iort(corpus / "data" / "iort" / "textes" / "md",
                                  req.get("iort_ar") or [], int(seuil[:4]))
    print(f"  {bilan}")
    for nom, titre, voies in trouves:
        print(f"  {nom} — {titre[:200]}")
        print(f"      trouvé par : {' | '.join(voies)}")
    print(f"  {len(trouves)} candidat(s).")

    print("\n--- plein texte (corpus local des fascicules)")
    if not plein_texte:
        print("  non parcouru (--sans-plein-texte)")
    else:
        if not dates:
            print("  jort_cache absent : dates des fascicules inconnues, tous ceux de "
                  f"{seuil[:4]} et après sont lus")
        trouves, bilan = cherche_plein_texte(corpus, req.get("plein_texte") or [], seuil, dates, fin)
        for b in bilan:
            print(f"  {b}")
        vus = set()
        for annee, langue, numero, page, brut, extrait, url, _ in trouves:
            if (annee, langue, numero, page, brut) in vus:
                continue
            vus.add((annee, langue, numero, page, brut))
            print(f"  JORT n° {numero}/{annee} ({langue}), page {page} du fichier — « {brut} »")
            print(f"      … {extrait} …")
            print(f"      {url}")
        print(f"  {len(vus)} occurrence(s).")
    print()


def cmd_relancer(fiches, ident, perimees, depuis, plein_texte) -> int:
    if perimees:
        base = chemin_base()
        fin = derniere_publication(ouvre_base(base)) if base.exists() else None
        choisies = [f for f in fiches if est_perimee(f, fin)]
        if not choisies:
            print("Aucune fiche périmée.")
    else:
        choisies = [f for f in fiches if f.get("id") == ident]
        if not choisies:
            print(f"Aucune fiche « {ident} ».")
            return 1
    for f in choisies:
        relance(f, depuis, plein_texte)
    return 0


def elargit(fiche: dict, terme: str, source: str) -> bool:
    """Ajoute le terme ; rend False s'il y était déjà."""
    req = fiche.setdefault("requetes", {})
    termes = req.setdefault(source, [])
    if terme in termes:
        return False
    termes.append(terme)
    return True


def ajoute_passe(fiche: dict, resultat: str, couverture: str, couvert_jusqu_au: str,
                 sources: list[str], role: str = "documentaliste", date: str | None = None) -> dict:
    passe = {
        "date": date or dt.date.today().isoformat(),
        "role": role,
        "sources": sources,
        "couverture": couverture,
        "couvert_jusqu_au": couvert_jusqu_au,
        "resultat": resultat,
    }
    fiche.setdefault("passes", []).append(passe)
    if resultat != "aucun":
        fiche["resolu"] = resultat
    return passe


def _date_iso(texte: str) -> str:
    if not iso(texte):
        raise argparse.ArgumentTypeError(f"date ISO AAAA-MM-JJ attendue : {texte!r}")
    return texte


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="commande", required=True)
    sub.add_parser("verifier", help="registre et ancres cohérents (CI)")
    p = sub.add_parser("lister", help="fiches, ancres, dernières passes")
    p.add_argument("--perimees", action="store_true")
    p = sub.add_parser("relancer", help="rejouer les requêtes d'une fiche")
    p.add_argument("id", nargs="?")
    p.add_argument("--perimees", action="store_true")
    p.add_argument("--depuis", type=_date_iso)
    p.add_argument("--sans-plein-texte", action="store_true")
    p = sub.add_parser("elargir", help="ajouter un terme à une fiche, puis rejouer")
    p.add_argument("id")
    p.add_argument("--terme", required=True)
    p.add_argument("--source", choices=SOURCES_DE_TERMES, default="titres_fts")
    p.add_argument("--depuis", type=_date_iso)
    p.add_argument("--sans-plein-texte", action="store_true")
    p = sub.add_parser("passe", help="consigner une passe datée du jour")
    p.add_argument("id")
    p.add_argument("--resultat", required=True, help="« aucun », ou la clé CSL du texte trouvé")
    p.add_argument("--couverture", required=True)
    p.add_argument("--couvert-jusqu-au", required=True, type=_date_iso)
    p.add_argument("--sources", required=True, nargs="+", choices=sorted(SOURCES_CONNUES))
    p.add_argument("--role", default="documentaliste")
    args = ap.parse_args(argv)

    entete, fiches = charger()

    if args.commande == "verifier":
        erreurs = verifie(fiches)
        for e in erreurs:
            print(f"✗ {e}")
        if erreurs:
            print(f"\n{len(erreurs)} incohérence(s) entre docs/recherches.yml et les ancres des .qmd.")
            return 1
        n = len(ancres(fichiers_qmd()))
        print(f"{len(fiches)} fiche(s), {n} ancre(s) RECHERCHE : registre cohérent.")
        return 0
    if args.commande == "lister":
        return cmd_lister(fiches, args.perimees)
    if args.commande == "relancer":
        if not args.id and not args.perimees:
            ap.error("relancer : donner un id ou --perimees")
        return cmd_relancer(fiches, args.id, args.perimees, args.depuis, not args.sans_plein_texte)

    fiche = next((f for f in fiches if f.get("id") == args.id), None)
    if fiche is None:
        print(f"Aucune fiche « {args.id} ».")
        return 1
    if args.commande == "elargir":
        if elargit(fiche, args.terme, args.source):
            ecrire(entete, fiches)
            print(f"{args.id} : « {args.terme} » ajouté à requetes.{args.source}.")
        else:
            print(f"{args.id} : « {args.terme} » figure déjà dans requetes.{args.source}.")
        # Un terme neuf n'a jamais été cherché : on repart de la naissance de l'objet,
        # pas de la couverture de la dernière passe.
        depuis = args.depuis or iso(fiche["requetes"].get("depuis")) or "1956-01-01"
        relance(fiche, depuis, not args.sans_plein_texte)
        return 0
    if args.commande == "passe":
        passe = ajoute_passe(fiche, args.resultat, args.couverture, args.couvert_jusqu_au,
                             args.sources, args.role)
        ecrire(entete, fiches)
        print(f"{args.id} : passe du {passe['date']} consignée (résultat : {args.resultat}).")
        if fiche.get("resolu"):
            print("Fiche résolue : remplacer la réserve du texte par la règle sourcée et retirer "
                  "l'ancre RECHERCHE — `verifier` le signalera sinon.")
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

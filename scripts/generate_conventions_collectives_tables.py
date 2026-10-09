"""Régénère ce que lit l'annexe « Les conventions collectives, branche par branche ».

Appelé par `generate_marche_travail_tables.py`, que lance le contrôle de fraîcheur ; peut
aussi tourner seul :

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_conventions_collectives_tables.py

LE GÉNÉRATEUR NE CONNAÎT AUCUNE BRANCHE. Il parcourt le nœud
`marche_travail/conventions_collectives` : un sous-nœud par branche, puis par grandeur
(`salaire_base`), puis la structure de la grille — grille, catégorie ou échelle, échelon —
jusqu'aux paramètres, qui sont chacun UNE CASE de la grille. Une case ajoutée en amont, ou
une branche entière, entre dans l'annexe sans que ce script change. Les libellés viennent
des `short_label` et des descriptions des nœuds ; l'unité, de `metadata.unit`.

Une case peut être un fichier (`…/personnel_occasionnel/manoeuvre_ordinaire.yaml`) ou une clé
d'un fichier de nœud (`…/salaire_base/echelle_1.yaml`, clé `echelon_1`) : le parcours descend
dans les deux, et désigne la case par le chemin de sa page publique.

L'ANNEXE NE REPRODUIT PAS LES GRILLES : elle en trace quelques cases et renvoie, pour chaque
grille, à sa page publique, qui en donne les cases versées à toutes leurs dates avec leurs
références. LA GRILLE D'UNE CASE SE DÉDUIT DES CHEMINS (`grilles`) : c'est le nœud le plus
profond qui contient toutes les cases de même grandeur et de même unité de la branche — celui
qui regroupe les catégories ou les échelles —, sans qu'aucune grille soit nommée ici.

CE QUI EST ENGENDRÉ :
  - `precis/{fr,ar}/marche_travail/tables/cc_index.yml` : la liste des branches, de leurs
    grilles et de leurs cases (libellés, unité, période, comptes), que l'annexe parcourt
    pour s'écrire — elle non plus ne nomme aucune case ;
  - `precis/{fr,ar}/marche_travail/tables/cc_<branche>_grilles.liens.yml` : le lien « Base
    législative » de chaque grille de la branche, au schéma commun (`libelle`, `parametre`,
    `url`), que garde `verifier_liens_base_legislative.py` ;
  - `precis/_seriescache/cc-grille-<branche>.csv` : la série longue que trace la figure en
    escalier de la branche, et les liens de ses cases en deux langues.

UNE DATE SANS VALEUR N'EST NI ZÉRO NI LA VALEUR PRÉCÉDENTE. Une date d'effet dont la valeur
est vide est une date à laquelle le salaire change sans qu'un texte en publie le montant :
la série garde la case vide, et la figure y arrête son trait.

Les libellés des nœuds n'existent qu'en français : les liens arabes ont leurs mentions en
arabe, et gardent en français les noms des branches et des grilles.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

NOEUD = "parameters/marche_travail/conventions_collectives"
RACINE = Path(__file__).parent.parent / "precis"
CACHE = RACINE / "_seriescache"
LIVRE = "marche_travail"
LANGUES = ("fr", "ar")
PREFIXE = "cc"
PREFIXE_SERIE = "cc-grille"
INDEX = f"{PREFIXE}_index.yml"

# Clés d'un nœud ou d'un paramètre qui ne sont pas des enfants.
RESERVEES = ("description", "metadata", "documentation", "values", "brackets")

MOTS = {
    "fr": {
        "cases": "cases de la grille", "currency": "dinars", "par": "par",
        "periodes": {"heure": "heure", "jour": "jour", "mois": "mois", "an": "an"},
    },
    "ar": {
        "cases": "خانات الشبكة", "currency": "دينار", "par": "في",
        "periodes": {"heure": "الساعة", "jour": "اليوم", "mois": "الشهر", "an": "السنة"},
    },
}


# ------------------------------------------------------------------ parcours de l'arbre


def est_parametre(noeud: dict) -> bool:
    return isinstance(noeud, dict) and "values" in noeud


def enfants(noeud: dict) -> list[tuple[str, dict]]:
    """Enfants d'un nœud chargé, dans l'ordre de `metadata.order`, puis alphabétique. Pure."""
    noms = [n for n, v in noeud.items() if n not in RESERVEES and isinstance(v, dict)]
    ordre = [n for n in ((noeud.get("metadata") or {}).get("order") or []) if n in noms]
    ordre += sorted(n for n in noms if n not in ordre)
    return [(n, noeud[n]) for n in ordre]


def cases(noeud: dict, chemin: tuple[str, ...] = (), lignee: tuple[dict, ...] = ()
          ) -> list[tuple[tuple[str, ...], tuple[dict, ...]]]:
    """Les paramètres d'un nœud, en profondeur : [(chemin, lignée)]. Pure.

    `chemin` : les noms, du nœud jusqu'à la case. `lignée` : les nœuds traversés, case
    comprise — d'où viennent les libellés.
    """
    sortie = []
    for nom, enfant in enfants(noeud):
        suite = (chemin + (nom,), lignee + (enfant,))
        if est_parametre(enfant):
            sortie.append(suite)
        else:
            sortie += cases(enfant, *suite)
    return sortie


def libelle(noeud: dict) -> str:
    """Libellé lisible d'un nœud : son `short_label`, à défaut sa description."""
    return ((noeud.get("metadata") or {}).get("short_label")
            or noeud.get("description") or "").strip()


def libelle_case(lignee: tuple[dict, ...]) -> str:
    """« Échelle 1, échelon 1 » : les libellés de la lignée, le premier seul en capitale."""
    noms = [libelle(n) for n in lignee if libelle(n)]
    return ", ".join([noms[0]] + [n[:1].lower() + n[1:] for n in noms[1:]]) if noms else ""


def unite(parametre: dict, langue: str = "fr") -> str:
    """« dinars par mois », d'après `metadata.unit` (`currency/mois`) ; vide si inconnue."""
    brut = str((parametre.get("metadata") or {}).get("unit") or "")
    m = MOTS[langue]
    if not brut.startswith("currency"):
        return ""
    _, _, periode = brut.partition("/")
    if not periode:
        return m["currency"]
    return f"{m['currency']} {m['par']} {m['periodes'].get(periode, periode)}"


def serie(parametre: dict) -> list[tuple[str, float | None, str, str, str]]:
    """(date d'effet, valeur ou None, titre, lien, note) d'un paramètre chargé. Pure.

    Le titre, le lien et la note sont ceux de la première référence que le paramètre
    attache à la date ; vides s'il n'en attache pas.
    """
    references = (parametre.get("metadata") or {}).get("reference") or {}
    par_date = {str(cle)[:10]: ref for cle, ref in references.items()}
    sortie = []
    for cle in sorted(parametre.get("values") or {}, key=lambda c: str(c)[:10]):
        brut = parametre["values"][cle]
        valeur = brut.get("value") if isinstance(brut, dict) else brut
        ref = par_date.get(str(cle)[:10]) or {}
        if isinstance(ref, list):
            ref = ref[0] if ref else {}
        if isinstance(ref, str):
            ref = {"title": ref}
        sortie.append((str(cle)[:10], None if valeur is None else float(valeur),
                       ref.get("title", ""), ref.get("href", ""), ref.get("note", "")))
    return sortie


# ---------------------------------------------------------------------- index et liens


def fiche_case(chemin: tuple[str, ...], lignee: tuple[dict, ...], langue: str = "fr") -> dict:
    """L'entrée d'une case dans l'index : libellés, unité, période, comptes. Pure.

    `chemin` : (branche, grandeur, …, case). `lignée` : les nœuds de mêmes rangs.
    """
    parametre = lignee[-1]
    s = serie(parametre)
    valuees = [d for d, v, *_ in s if v is not None]
    return {
        "cle": ".".join(chemin[1:]),
        "libelle": libelle_case(lignee[2:]) or libelle(lignee[1]),
        "grandeur": libelle(lignee[1]),
        "unite": unite(parametre, langue),
        "description": (parametre.get("description") or "").strip(),
        "parametre": f"{NOEUD}/{'/'.join(chemin)}.yaml",
        "debut": s[0][0] if s else None,
        "derniere_valeur": valuees[-1] if valuees else None,
        "dates": len(s),
        "valeurs": len(valuees),
        "sans_valeur": len(s) - len(valuees),
    }


def _minuscule(texte: str) -> str:
    return texte[:1].lower() + texte[1:]


def libelle_lien(branche: str, fiche: dict) -> str:
    """Libellé du lien « Base législative » : la branche, la case, la grandeur et son unité."""
    suffixe = f" ({fiche['unite']})" if fiche["unite"] else ""
    return (f"{branche} — {_minuscule(fiche['libelle'])} : "
            f"{_minuscule(fiche['grandeur'])}{suffixe}")


def grilles(trouvees: list[tuple[tuple[str, ...], tuple[dict, ...]]], langue: str = "fr"
            ) -> list[dict]:
    """Les grilles d'une branche, déduites des chemins de ses cases. Pure.

    `trouvees` : les cases de la branche, telles que `cases` les rend — chemin (branche,
    grandeur, …, case) et lignée de mêmes rangs. Une grille est le nœud LE PLUS PROFOND
    commun à toutes les cases de même grandeur et de même unité : celui qui regroupe les
    catégories ou les échelles — `…salaire_base.agents_payes_a_l_heure` quand la grandeur
    porte plusieurs grilles, `…salaire_base` quand elle n'en porte qu'une. Une case seule de
    son espèce a pour grille le nœud qui la contient. L'ordre est celui des cases.

    Chaque grille : sa clé pointée sous la branche, son libellé (vide quand la grille est la
    grandeur elle-même), la grandeur, l'unité, le chemin de sa page publique et les clés de
    ses cases.
    """
    groupes: dict[tuple[str, str], list] = {}
    for chemin, lignee in trouvees:
        groupes.setdefault((chemin[1], unite(lignee[-1], langue)), []).append((chemin, lignee))
    sortie = []
    for (_grandeur, u), membres in groupes.items():
        chemins = [c for c, _l in membres]
        commun = len(chemins[0]) - 1
        for chemin in chemins[1:]:
            rang = 0
            while rang < min(commun, len(chemin) - 1) and chemin[rang] == chemins[0][rang]:
                rang += 1
            commun = rang
        commun = max(commun, 2)  # jamais au-dessus de la grandeur
        chemin, lignee = membres[0]
        sortie.append({
            "cle": ".".join(chemin[1:commun]),
            "libelle": libelle_case(lignee[2:commun]),
            "grandeur": libelle(lignee[1]),
            "unite": u,
            "parametre": f"{NOEUD}/{'/'.join(chemin[:commun])}",
            "cases": [".".join(c[1:]) for c in chemins],
        })
    return sortie


def libelle_lien_grille(branche: str, grille: dict, langue: str = "fr") -> str:
    """« Textile — agents payés à l'heure : salaire de base, cases de la grille (dinars par heure) »."""
    tete = f"{branche} — {_minuscule(grille['libelle'])}" if grille["libelle"] else branche
    suffixe = f" ({grille['unite']})" if grille["unite"] else ""
    return (f"{tete} : {_minuscule(grille['grandeur'])}, "
            f"{MOTS[langue]['cases']}{suffixe}")


# --------------------------------------------------------------------------- lecture


def charge_arbre(chemin_noeud: str) -> dict:
    """Le nœud et toute sa descendance, en un dictionnaire : dossiers, fichiers et clés."""
    racine = ot._racine_paquet()
    ref = racine
    for element in chemin_noeud.split("/"):
        ref = ref / element
    if not ref.is_dir():
        return ot.charge_parametre(f"{chemin_noeud}.yaml") or {}
    noeud = dict(ot.charge_parametre(f"{chemin_noeud}/index.yaml") or {})
    for enfant in sorted(ref.iterdir(), key=lambda e: e.name):
        if enfant.is_dir():
            noeud[enfant.name] = charge_arbre(f"{chemin_noeud}/{enfant.name}")
        elif enfant.name.endswith(".yaml") and enfant.name != "index.yaml":
            nom = enfant.name.removesuffix(".yaml")
            noeud[nom] = ot.charge_parametre(f"{chemin_noeud}/{enfant.name}") or {}
    return noeud


# --------------------------------------------------------------------------- écriture


def _nettoie(dossier: Path, motif: str, ecrits: set[Path]) -> None:
    """Retire les fichiers engendrés que plus rien n'écrit : ils survivraient sans être gardés."""
    for ancien in dossier.glob(motif):
        if ancien not in ecrits:
            ancien.unlink()


def ecrire_branche(branche: str, noeud: dict, langue: str, ecrits: set[Path]) -> dict | None:
    """Écrit les liens des grilles d'une branche dans une langue ; rend son entrée d'index."""
    tables = RACINE / langue / LIVRE / "tables"
    tables.mkdir(parents=True, exist_ok=True)
    trouvees = cases(noeud, (branche,), (noeud,))
    if not trouvees:
        return None
    nom_branche = libelle(noeud)
    fiches = [fiche_case(chemin, lignee, langue) for chemin, lignee in trouvees]
    for fiche in fiches:
        if not fiche["dates"]:
            print(f"✗ {langue}/{branche}, {fiche['cle']} : paramètre sans valeur datée.")
            return None
    trouvees_grilles = grilles(trouvees, langue)
    liens = tables / f"{PREFIXE}_{branche}_grilles.liens.yml"
    ot.ecrire_fichier_liens(
        liens, [(g["parametre"], libelle_lien_grille(nom_branche, g, langue))
                for g in trouvees_grilles], langue)
    ecrits.add(liens)
    return {
        "branche": branche,
        "libelle": nom_branche,
        "description": (noeud.get("description") or "").strip(),
        "serie": f"{PREFIXE_SERIE}-{branche}",
        "liens_grilles": liens.name,
        "grilles": trouvees_grilles,
        "cases": fiches,
    }


def parametres_dates(entree: dict) -> list:
    """Les cases d'une branche, déclarées pour la série longue que trace sa figure."""
    return [ot.ParametreDate(
        f["cle"], f["parametre"], {l: f["libelle"] for l in LANGUES},
        lien={l: libelle_lien(entree["libelle"], f) for l in LANGUES}) for f in entree["cases"]]


def main() -> int:
    import yaml

    if not ot.openfisca_utilisable():
        print(f"openfisca-tunisia indisponible ou trop ancien (version {ot.version_openfisca()}, "
              f"minimum {ot.VERSION_MINIMALE}). Les snapshots existants sont conservés.")
        return 1
    arbre = charge_arbre(NOEUD)
    branches = enfants(arbre)
    if not branches:
        print(f"✗ {NOEUD} : nœud introuvable ou vide.")
        return 1
    ecrits: set[Path] = set()
    series_ecrites: set[Path] = set()
    index = {langue: [] for langue in LANGUES}
    for branche, noeud in branches:
        for langue in LANGUES:
            entree = ecrire_branche(branche, noeud, langue, ecrits)
            if entree is None:
                print(f"✗ {langue}/{branche} : aucune case engendrée.")
                return 1
            index[langue].append(entree)
        entree = index["fr"][-1]
        parametres = parametres_dates(entree)
        # La série ne porte ses textes que si chaque date a le sien au Journal officiel en
        # ligne ; sinon elle ne porte que les valeurs, et la figure cite ses sources.
        avec_textes = all(titre and lien.startswith("https://www.pist.tn/")
                          for p in parametres for _d, _v, titre, lien in p.serie())
        code = (
            ot.ecrire_serie_parametres(entree["serie"], parametres, CACHE, colonne="case",
                                       avec_textes=avec_textes))
        if code:
            return code
        series_ecrites |= {CACHE / f"{entree['serie']}.csv",
                           *(CACHE / f"{entree['serie']}.liens.{l}.yml" for l in LANGUES)}
    for langue in LANGUES:
        tables = RACINE / langue / LIVRE / "tables"
        (tables / INDEX).write_text(
            "# Généré par scripts/generate_conventions_collectives_tables.py — ne pas éditer "
            "à la main.\n" + yaml.safe_dump(index[langue], allow_unicode=True, sort_keys=False),
            encoding="utf-8")
        _nettoie(tables, f"{PREFIXE}_*.md", ecrits)  # tableaux d'une version antérieure
        _nettoie(tables, f"{PREFIXE}_*.liens.yml", ecrits)
    _nettoie(CACHE, f"{PREFIXE_SERIE}-*", series_ecrites)
    n_cases = sum(len(e["cases"]) for e in index["fr"])
    n_valeurs = sum(c["valeurs"] for e in index["fr"] for c in e["cases"])
    n_vides = sum(c["sans_valeur"] for e in index["fr"] for c in e["cases"])
    print(f"✓ conventions collectives : {len(index['fr'])} branches, {n_cases} cases, "
          f"{n_valeurs} valeurs, {n_vides} dates sans valeur")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

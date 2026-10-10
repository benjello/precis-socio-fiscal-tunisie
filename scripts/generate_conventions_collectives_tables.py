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

L'ANNEXE NE REPRODUIT PAS LES GRILLES : pour chaque grille, elle trace la case du bas et
celle du haut, et renvoie à sa page publique, qui en donne toutes les cases à toutes leurs
dates avec leurs références. LA GRILLE D'UNE CASE SE DÉDUIT DES CHEMINS (`grilles`) : c'est le
nœud le plus profond qui contient toutes les cases de même grandeur et de même unité de la
branche — celui qui regroupe les catégories, les échelles ou les emplois, ses LIGNES —, sans
qu'aucune grille soit nommée ici. Une branche a autant de grilles qu'elle a de grandeurs (des
nœuds frères sous la branche) et d'unités (une grille horaire et une grille mensuelle sous la
même grandeur). Limite connue : deux grilles de même unité sous une même grandeur ne se
distingueraient pas ; aucune branche versée n'en a.

LE BAS ET LE HAUT SE CHOISISSENT PAR GRILLE, À SA DERNIÈRE DATE PUBLIÉE (`etat_grille`,
`bas_et_haut`), ici et non dans le module de figures, pour que la règle se teste sans pandas :
  - la dernière date publiée d'une grille est la dernière date d'effet où une case au moins
    porte une valeur ;
  - seules concourent les cases qui ont une valeur en vigueur à cette date : une ligne close
    avant elle, ou une case illisible à cette date, ne peut être ni le bas ni le haut ;
  - une colonne sans rang parmi des colonnes numérotées (`hors_rang` : un stage avant les
    échelons) n'est pas un échelon, et ne concourt pas.

TOUTE GRILLE N'A PAS SA COURBE (`marque_tracees`). Une grille qui a moins de
`MIN_DATES_TRACEE` dates publiées ne dit pas une évolution ; une grille close — toutes ses
cases vides à sa dernière date — à laquelle une autre grille de même unité de la branche
succède (elle commence à la date de clôture ou après) est une grille antérieure. Ni l'une ni
l'autre ne fournit de bas ni de haut : l'annexe les mentionne, avec leur période et le lien de
leur page.

CE QUI EST ENGENDRÉ :
  - `precis/{fr,ar}/marche_travail/tables/cc_index.yml` : la liste des branches et de leurs
    grilles — libellés, unité, comptes (lignes, colonnes, cases, dates d'effet, cases vides),
    période, et, pour une grille tracée, les fiches de sa case du bas et de sa case du haut.
    L'annexe la parcourt pour s'écrire — elle non plus ne nomme aucune case. L'index ne liste
    pas les cases une à une : elles se lisent à la page publique de la grille ;
  - `precis/{fr,ar}/marche_travail/tables/cc_<branche>_grilles.liens.yml` : les liens « Base
    législative » des grilles de la branche, au schéma commun (`libelle`, `parametre`,
    `url`), que garde `verifier_liens_base_legislative.py`, plus la grille (`grille`,
    `libelle_grille`) et la ligne (`ligne`) de chaque lien. LA VUE EN TABLEAU D'UN NŒUD N'EXISTE QU'EN DEÇÀ DE
    `PLAFOND_VUE_TABLEAU` CASES : au-delà, le site des paramètres répond 404. Une grille plus
    grande reçoit donc un lien par ligne (`liens_grille`) ;
  - `precis/_seriescache/cc-grille-<branche>-<grille>.csv` : la série longue que trace la
    figure d'une grille — sa case du bas et sa case du haut —, et les liens de ces cases en
    deux langues.

UNE DATE SANS VALEUR N'EST NI ZÉRO NI LA VALEUR PRÉCÉDENTE. La série garde la case vide, et la
figure y arrête son trait. Une valeur vide dit l'une de trois choses, que `etat_grille`
distingue par la forme de la grille, sans lire les notes :
  - GRILLE NON PUBLIÉE : aucune case n'a de valeur à cette date (le salaire change sans
    qu'un texte en publie le montant, ou la grille est close) ;
  - LIGNE CLOSE : la grille est publiée à cette date et après, et la case n'a plus aucune
    date ensuite (un emploi que la grille divise en deux) ;
  - CASE VIDE, parce qu'illisible sur le fascicule : la grille est publiée à cette date, et
    la case reprend ensuite, ou la date est la dernière de la grille.

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

# Le site des paramètres ne rend la vue en tableau d'un nœud qu'en deçà de 200 colonnes — une
# par case (`countParameterColumnsApproximation` de son visualiseur) ; au-delà, l'adresse
# `…/table/` du nœud répond 404.
PLAFOND_VUE_TABLEAU = 200

# En deçà de trois dates publiées, une grille ne dit pas une évolution : pas de courbe.
MIN_DATES_TRACEE = 3

# Clés d'un nœud ou d'un paramètre qui ne sont pas des enfants.
RESERVEES = ("description", "metadata", "documentation", "values", "brackets")

MOTS = {
    "fr": {
        "cases": "cases de la grille", "cases_ligne": "cases de la ligne",
        "currency": "dinars", "par": "par",
        "periodes": {"heure": "heure", "jour": "jour", "mois": "mois", "an": "an"},
    },
    "ar": {
        "cases": "خانات الشبكة", "cases_ligne": "خانات السطر",
        "currency": "دينار", "par": "في",
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
        # La première date qui porte une valeur : une case illisible en tête de série ne
        # fait pas commencer la case à cette date.
        "debut": valuees[0] if valuees else None,
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
            # Les lignes sont les enfants immédiats du nœud de la grille : catégories,
            # échelles, emplois. Chacune : son nom, son libellé, le chemin de sa page.
            "lignes": list({c[commun]: {
                "nom": c[commun], "libelle": libelle(l[commun]),
                "parametre": f"{NOEUD}/{'/'.join(c[:commun + 1])}"}
                for c, l in membres}.values()),
            # Les colonnes — échelons, stage — n'existent que si la case est sous sa ligne.
            "colonnes": list(dict.fromkeys(c[-1] for c in chemins if len(c) > commun + 1)),
        })
    return sortie


def hors_rang(nom: str, freres: list[str]) -> bool:
    """Vrai si `nom` est une colonne sans rang parmi des colonnes numérotées. Pure.

    Dans une ligne dont les colonnes portent, à plus de la moitié, UN MÊME PRÉFIXE suivi d'un
    rang (`echelon_1`… `echelon_20`), une colonne qui n'en porte pas (`stage`) n'est pas un
    échelon : elle ne concourt ni pour le bas ni pour le haut de la grille. Des lignes
    nommées par leur intitulé, dont deux seulement finissent par un chiffre (les deux niveaux
    d'un même emploi), ne sont pas des colonnes numérotées : aucune n'y est hors rang.
    """
    import re

    prefixes = [m.group(1) for f in freres if (m := re.fullmatch(r"(.*\D)_?(\d+)", f))]
    if not prefixes:
        return False
    dominant = max(set(prefixes), key=prefixes.count)
    if 2 * prefixes.count(dominant) <= len(freres):
        return False
    return re.fullmatch(re.escape(dominant) + r"_?\d+", nom) is None


def en_vigueur(serie_case: list[tuple], date: str) -> float | None:
    """La valeur d'une case à `date` : celle de sa dernière date d'effet antérieure ou égale ;
    None avant sa première date, ou si cette dernière date est sans valeur. Pure."""
    retenue = None
    for d, v, *_ in serie_case:
        if d <= date:
            retenue = v
    return retenue


def etat_grille(series: dict[str, list[tuple]]) -> dict:
    """Ce que les séries des cases d'une grille disent d'elle. Pure.

    `series` : {clé de case: [(date d'effet, valeur ou None, …)]}, dates croissantes.
    Rend ses dates publiées (une case au moins y a une valeur), la date de sa clôture — la
    première date postérieure à la dernière date publiée, où toutes ses cases sont donc
    vides, ou None —, et le décompte de ses valeurs vides, par espèce (voir l'en-tête du
    module) : `cases_vides` (illisibles), `lignes_closes`, `non_publiees`.
    """
    dates = sorted({d for s in series.values() for d, *_ in s})
    publiees = sorted({d for s in series.values() for d, v, *_ in s if v is not None})
    fin = publiees[-1] if publiees else None
    apres = [d for d in dates if fin is not None and d > fin]
    vides, closes, non_publiees, dates_vides = 0, 0, 0, set()
    for s in series.values():
        for rang, (d, v, *_) in enumerate(s):
            if v is not None:
                continue
            if d not in publiees:
                non_publiees += 1
            elif rang == len(s) - 1 and d < fin:
                closes += 1
            else:
                vides += 1
                dates_vides.add(d)
    return {
        "dates_publiees": publiees,
        "debut": publiees[0] if publiees else None,
        "fin": fin,
        "cloture": apres[0] if apres else None,
        "valeurs": sum(1 for s in series.values() for _d, v, *_ in s if v is not None),
        "cases_vides": vides,
        "dates_cases_vides": sorted(dates_vides),
        "lignes_closes": closes,
        "non_publiees": non_publiees,
    }


def formes(series: dict[str, list[tuple]], place: dict[str, tuple[str, str]]) -> list[dict]:
    """Les formes successives d'une grille : lignes, colonnes et cases à ses dates. Pure.

    `place` : clé de case -> (ligne, colonne) ; la colonne est vide quand la ligne est la
    case. Une case est dans la grille d'une date publiée si elle y a une date d'effet —
    valeur vide comprise : une case illisible est une case de la grille —, sauf la date qui
    clôt sa ligne. Rend une entrée par changement de forme : `depuis` (la première date
    publiée de cette forme), `jusqu_a` (la dernière), et les comptes — une grille sans
    échelon a une colonne.
    """
    etat = etat_grille(series)
    sortie = []
    for date in etat["dates_publiees"]:
        presentes = [cle for cle, s in series.items() for rang, (d, v, *_) in enumerate(s)
                     if d == date and not (v is None and rang == len(s) - 1 and d < etat["fin"])]
        forme = {"lignes": len({place[c][0] for c in presentes}),
                 "colonnes": len({place[c][1] for c in presentes}),
                 "cases": len(presentes)}
        if sortie and all(sortie[-1][k] == v for k, v in forme.items()):
            sortie[-1]["jusqu_a"] = date
        else:
            sortie.append({"depuis": date, "jusqu_a": date, **forme})
    return sortie


def bas_et_haut(series: dict[str, list[tuple]], ecartees: set[str] = frozenset()
                ) -> tuple[str, str] | None:
    """Les clés de la case du bas et de la case du haut d'une grille. Pure.

    Le choix se fait À LA DERNIÈRE DATE PUBLIÉE de la grille, parmi les cases qui y ont une
    valeur en vigueur, `ecartees` exclues (les colonnes hors rang) : la plus basse et la plus
    haute. À égalité, la première pour le bas, la dernière pour le haut, dans l'ordre de la
    grille. Une ligne close avant cette date — même si sa dernière valeur, ancienne, est la
    plus basse de toutes — n'y est pas ; une case illisible à cette date non plus. None si
    aucune case ne concourt.
    """
    fin = etat_grille(series)["fin"]
    if fin is None:
        return None
    presentes = [(cle, en_vigueur(s, fin)) for cle, s in series.items() if cle not in ecartees]
    presentes = [(cle, v) for cle, v in presentes if v is not None]
    if not presentes:
        return None
    bas = min(presentes, key=lambda p: p[1])[0]
    haut = max(reversed(presentes), key=lambda p: p[1])[0]
    return bas, haut


def marque_tracees(etats: list[dict]) -> list[tuple[bool, str]]:
    """Pour chaque grille d'une branche : (a sa courbe, motif). Pure.

    `etats` : un dictionnaire par grille, dans l'ordre de la branche, avec `unite`,
    `dates_publiees`, `debut` et `cloture` (`etat_grille`). Motifs :
      - `sans_valeur` : aucune date publiée ;
      - `peu_de_dates` : moins de `MIN_DATES_TRACEE` dates publiées ;
      - `anterieure` : la grille est close, et une autre grille de même unité commence à sa
        date de clôture ou après — elle lui succède ;
      - `courante` : toutes les autres, y compris une grille dont la dernière date n'est
        pas publiée sans qu'aucune grille lui succède. Seule une grille courante a sa courbe.
    """
    sortie = []
    for rang, e in enumerate(etats):
        if not e["dates_publiees"]:
            sortie.append((False, "sans_valeur"))
        elif len(e["dates_publiees"]) < MIN_DATES_TRACEE:
            sortie.append((False, "peu_de_dates"))
        elif e["cloture"] and any(
                autre["unite"] == e["unite"] and autre["debut"] and autre["debut"] >= e["cloture"]
                for r, autre in enumerate(etats) if r != rang):
            sortie.append((False, "anterieure"))
        else:
            sortie.append((True, "courante"))
    return sortie


def libelle_lien_grille(branche: str, grille: dict, langue: str = "fr",
                        ligne: str = "") -> str:
    """« Textile — agents payés à l'heure : salaire de base, cases de la grille (dinars par
    heure) » ; avec `ligne`, « Assurances — échelle 1 : salaire de base, cases de la ligne
    (dinars par mois) »."""
    noms = [n for n in (grille["libelle"], ligne) if n]
    tete = " — ".join([branche] + [", ".join(_minuscule(n) for n in noms)] if noms else [branche])
    suffixe = f" ({grille['unite']})" if grille["unite"] else ""
    return (f"{tete} : {_minuscule(grille['grandeur'])}, "
            f"{MOTS[langue]['cases_ligne' if ligne else 'cases']}{suffixe}")


def liens_grille(branche: str, grille: dict, langue: str = "fr") -> list[dict]:
    """Les liens « Base législative » d'une grille : libellé, chemin, clé de la grille,
    libellé de la grille entière et, pour un lien de ligne, libellé de la ligne. Pure.

    Un lien, vers la vue en tableau de la grille entière, quand elle a moins de
    `PLAFOND_VUE_TABLEAU` cases ; sinon un lien par ligne, vers la vue en tableau de la
    ligne — celle de la grille entière n'existe pas sur le site.
    """
    entier = libelle_lien_grille(branche, grille, langue)
    if len(grille["cases"]) < PLAFOND_VUE_TABLEAU:
        return [{"libelle": entier, "parametre": grille["parametre"], "grille": grille["cle"],
                 "libelle_grille": entier, "ligne": ""}]
    return [{"libelle": libelle_lien_grille(branche, grille, langue, ligne["libelle"]),
             "parametre": ligne["parametre"], "grille": grille["cle"],
             "libelle_grille": entier, "ligne": ligne["libelle"]} for ligne in grille["lignes"]]


def nom_serie(branche: str, grille: dict) -> str:
    """« cc-grille-textile-salaire-base-agents-payes-a-l-heure » : la série d'une grille."""
    return f"{PREFIXE_SERIE}-{branche}-{grille['cle']}".replace(".", "-").replace("_", "-")


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


def fiche_grille(branche: str, noeud: dict, grille: dict, trouvees: list, langue: str = "fr"
                 ) -> dict:
    """L'entrée d'une grille dans l'index, sans sa marque `tracee` (`entree_branche`). Pure.

    `trouvees` : les cases de la branche (`cases`). Comptes et période viennent des séries
    des cases de la grille (`etat_grille`) ; le bas et le haut, de `bas_et_haut`.
    """
    par_cle = {".".join(c[1:]): (c, l) for c, l in trouvees}
    membres = {cle: par_cle[cle] for cle in grille["cases"]}
    series = {cle: serie(l[-1]) for cle, (_c, l) in membres.items()}
    etat = etat_grille(series)
    # Une colonne hors rang se juge parmi les colonnes de SA ligne.
    freres: dict[tuple, list[str]] = {}
    for c, _l in membres.values():
        freres.setdefault(c[:-1], []).append(c[-1])
    ecartees = {cle for cle, (c, _l) in membres.items() if hors_rang(c[-1], freres[c[:-1]])}
    choix = bas_et_haut(series, ecartees)
    # La ligne d'une case est l'enfant immédiat du nœud de la grille ; sa colonne, son nom
    # si elle est sous sa ligne.
    profondeur = len(grille["parametre"].removeprefix(f"{NOEUD}/").split("/"))
    place = {cle: (c[profondeur], c[-1] if len(c) > profondeur + 1 else "")
             for cle, (c, _l) in membres.items()}
    fiche = {
        "cle": grille["cle"], "libelle": grille["libelle"], "grandeur": grille["grandeur"],
        "unite": grille["unite"], "parametre": grille["parametre"],
        # Toutes dates confondues ; la forme de la grille à chaque date est dans `formes`.
        "lignes": len(grille["lignes"]), "colonnes": len(grille["colonnes"]),
        "cases": len(grille["cases"]),
        "formes": formes(series, place),
        "dates": len(etat["dates_publiees"]), "debut": etat["debut"], "fin": etat["fin"],
        "cloture": etat["cloture"], "valeurs": etat["valeurs"],
        "cases_vides": etat["cases_vides"], "dates_cases_vides": etat["dates_cases_vides"],
        "lignes_closes": etat["lignes_closes"],
        "hors_rang": list(dict.fromkeys(
            libelle(membres[cle][1][-1]) for cle in grille["cases"] if cle in ecartees)),
        "dates_publiees": etat["dates_publiees"],
    }
    if choix:
        fiche["bas"], fiche["haut"] = (fiche_case(*membres[cle], langue) for cle in choix)
    return fiche


def entree_branche(branche: str, noeud: dict, langue: str = "fr") -> tuple[dict, list] | None:
    """L'entrée d'une branche dans l'index et ses liens : (entrée, liens). Pure.

    None, après avoir dit pourquoi, si la branche n'a pas de case ou si l'une d'elles n'a
    aucune date.
    """
    trouvees = cases(noeud, (branche,), (noeud,))
    if not trouvees:
        return None
    for chemin, lignee in trouvees:
        if not serie(lignee[-1]):
            print(f"✗ {langue}/{branche}, {'.'.join(chemin[1:])} : paramètre sans valeur datée.")
            return None
    nom_branche = libelle(noeud)
    trouvees_grilles = grilles(trouvees, langue)
    fiches = [fiche_grille(branche, noeud, g, trouvees, langue) for g in trouvees_grilles]
    liens = []
    for g, fiche, (tracee, motif) in zip(trouvees_grilles, fiches, marque_tracees(fiches)):
        tracee = tracee and "bas" in fiche
        fiche["tracee"], fiche["motif"] = tracee, motif
        if tracee:
            fiche["serie"] = nom_serie(branche, g)
        else:  # ni bas ni haut pour une grille sans courbe
            fiche.pop("bas", None), fiche.pop("haut", None)
        del fiche["dates_publiees"]
        liens += liens_grille(nom_branche, g, langue)
    return {
        "branche": branche,
        "libelle": nom_branche,
        "description": (noeud.get("description") or "").strip(),
        "liens_grilles": f"{PREFIXE}_{branche}_grilles.liens.yml",
        "cases": sum(f["cases"] for f in fiches),
        "cases_vides": sum(f["cases_vides"] for f in fiches),
        "grilles": fiches,
    }, liens


def ecrire_branche(branche: str, noeud: dict, langue: str, ecrits: set[Path]) -> dict | None:
    """Écrit les liens des grilles d'une branche dans une langue ; rend son entrée d'index."""
    import yaml

    tables = RACINE / langue / LIVRE / "tables"
    tables.mkdir(parents=True, exist_ok=True)
    rendu = entree_branche(branche, noeud, langue)
    if rendu is None:
        return None
    entree, liens = rendu
    fichier = tables / entree["liens_grilles"]
    # Le schéma commun (`libelle`, `parametre`, `url`), puis la grille du lien, son libellé
    # et, pour un lien de ligne, celui de la ligne.
    fichier.write_text(yaml.safe_dump(
        [{"libelle": l["libelle"], "parametre": l["parametre"],
          "url": ot.url_parametre(l["parametre"], langue),
          "grille": l["grille"], "libelle_grille": l["libelle_grille"],
          "ligne": l["ligne"]} for l in liens],
        allow_unicode=True, sort_keys=False), encoding="utf-8")
    ecrits.add(fichier)
    return entree


def parametres_dates(entree: dict, grille: dict) -> list:
    """La case du bas et celle du haut d'une grille tracée, déclarées pour sa série longue."""
    fiches = list({f["cle"]: f for f in (grille["bas"], grille["haut"])}.values())
    return [ot.ParametreDate(
        f["cle"], f["parametre"], {l: f["libelle"] for l in LANGUES},
        lien={l: libelle_lien(entree["libelle"], f) for l in LANGUES}) for f in fiches]


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
        for grille in entree["grilles"]:
            if not grille["tracee"]:
                continue
            parametres = parametres_dates(entree, grille)
            # La série ne porte ses textes que si chaque date a le sien au Journal officiel
            # en ligne ; sinon elle ne porte que les valeurs, et la figure cite ses sources.
            avec_textes = all(titre and lien.startswith("https://www.pist.tn/")
                              for p in parametres for _d, _v, titre, lien in p.serie())
            code = ot.ecrire_serie_parametres(grille["serie"], parametres, CACHE,
                                              colonne="case", avec_textes=avec_textes)
            if code:
                return code
            series_ecrites |= {CACHE / f"{grille['serie']}.csv",
                               *(CACHE / f"{grille['serie']}.liens.{l}.yml" for l in LANGUES)}
    for langue in LANGUES:
        tables = RACINE / langue / LIVRE / "tables"
        (tables / INDEX).write_text(
            "# Généré par scripts/generate_conventions_collectives_tables.py — ne pas éditer "
            "à la main.\n" + yaml.safe_dump(index[langue], allow_unicode=True, sort_keys=False),
            encoding="utf-8")
        _nettoie(tables, f"{PREFIXE}_*.md", ecrits)  # tableaux d'une version antérieure
        _nettoie(tables, f"{PREFIXE}_*.liens.yml", ecrits)
    _nettoie(CACHE, f"{PREFIXE_SERIE}-*", series_ecrites)
    grilles_fr = [g for e in index["fr"] for g in e["grilles"]]
    print(f"✓ conventions collectives : {len(index['fr'])} branches, {len(grilles_fr)} grilles "
          f"dont {sum(g['tracee'] for g in grilles_fr)} tracées, "
          f"{sum(g['cases'] for g in grilles_fr)} cases, "
          f"{sum(g['valeurs'] for g in grilles_fr)} valeurs, "
          f"{sum(g['cases_vides'] for g in grilles_fr)} cases vides")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

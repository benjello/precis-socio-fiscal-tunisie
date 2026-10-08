"""Régénère les tableaux de l'annexe « Les conventions collectives, branche par branche ».

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

CE QUI EST ENGENDRÉ, dans `precis/{fr,ar}/marche_travail/tables/` :
  - `cc_<branche>_<chemin de la case>.md` : la case date par date — date d'effet, montant,
    texte, Journal officiel — et son `.liens.yml` ;
  - `cc_<branche>_dates_reperes.md` : les cases de la branche à des dates repères — une
    date par ligne, une case par colonne —, et ses liens ;
  - `cc_index.yml` : la liste des branches et de leurs cases (libellés, unité, fichiers,
    période, comptes), que l'annexe parcourt pour s'écrire — elle non plus ne nomme aucune case.
Et dans `precis/_seriescache/` : `cc-grille-<branche>.csv`, la série longue que trace la
figure en escalier de la branche, et ses liens en deux langues.

UNE DATE SANS VALEUR N'EST NI ZÉRO NI LA VALEUR PRÉCÉDENTE. Une date d'effet dont la valeur
est vide est une date à laquelle le salaire change sans qu'un texte en publie le montant :
la case rend « non publiée ».

Les libellés des nœuds n'existent qu'en français : les tableaux arabes ont leurs en-têtes et
leurs mentions en arabe, et gardent en français les noms des branches et des cases.
"""

from __future__ import annotations

import re
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

# Dates repères communes à toutes les branches, après la première grille de chacune : des
# CONSTANTES — une date mobile ferait différer le snapshot d'une semaine à l'autre.
REPERES = ("2000-01-01", "2010-01-01", "2020-01-01", "2025-01-01", "2026-01-01")

MOTS = {
    "fr": {
        "effet": "Date d'effet", "texte": "Texte", "journal": "*Journal officiel*",
        "repere": "Date repère", "sans_valeur": "non publiée",
        "currency": "dinars", "par": "par",
        "periodes": {"heure": "heure", "jour": "jour", "mois": "mois", "an": "an"},
    },
    "ar": {
        "effet": "تاريخ النفاذ", "texte": "النصّ", "journal": "الرائد الرسمي",
        "repere": "التاريخ المرجعي", "sans_valeur": "غير منشورة",
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


# -------------------------------------------------------------------- cellules et tableau

_JOURNAL = re.compile(r"^JORT\s+(n°\s.+?,\s+pp?\.\s+\d[\d\s–-]*\d|n°\s.+?,\s+pp?\.\s+\d)\.")


def journal(note: str) -> str:
    """« n° 72 du 24 septembre 1993, édition française, p. 1600 », tiré de la note. Pure.

    Seule la localisation au Journal officiel, par laquelle la note commence, passe dans le
    tableau : le reste de la note décrit le relevé, non le texte. « — » si la note ne
    commence pas par elle.
    """
    trouve = _JOURNAL.match(note or "")
    return trouve.group(1) if trouve else ot.VIDE


def montant(valeur: float | None, langue: str = "fr") -> str:
    """Trois décimales, comme le Journal officiel écrit les salaires ; « non publiée » à vide."""
    if valeur is None:
        return MOTS[langue]["sans_valeur"]
    return f"{valeur:,.3f}".replace(",", " ").replace(".", ",")


def date_insecable(date_iso: str, langue: str = "fr") -> str:
    """Une date ne se coupe pas : « [1^er^ juin 1993]{.insecable} »."""
    return f"[{ot.formate_date(date_iso, langue)}]{{.insecable}}"


def entete_valeur(grandeur: str, parametre: dict, langue: str = "fr") -> str:
    """Le nom de la grandeur, et son unité entre parenthèses à la ligne."""
    u = unite(parametre, langue)
    return f"{grandeur}<br>({u})" if u else grandeur


def lignes_case(parametre: dict, langue: str = "fr") -> list[list[str]]:
    """Les lignes du tableau d'une case : date d'effet, montant, texte, Journal officiel. Pure."""
    # Le lien reste celui que la valeur porte, dans les deux langues : la colonne voisine
    # donne la page dans l'édition que ce lien ouvre, et l'autre édition n'a pas la même.
    return [[date_insecable(date, langue), montant(valeur, langue),
             ot.lien_reference(titre, lien) or ot.VIDE, journal(note)]
            for date, valeur, titre, lien, note in serie(parametre)]


def markdown(entetes: list[str], lignes: list[list[str]], a_droite: tuple[int, ...] = ()) -> str:
    """Tableau Markdown à barres ; `a_droite` : rangs des colonnes alignées à droite. Pure."""
    sortie = ["| " + " | ".join(entetes) + " |",
              "|" + "|".join("---:" if i in a_droite else "---"
                             for i in range(len(entetes))) + "|"]
    sortie += ["| " + " | ".join(ligne) + " |" for ligne in lignes]
    return "\n".join(sortie)


def tableau_case(grandeur: str, parametre: dict, langue: str = "fr") -> str:
    m = MOTS[langue]
    return markdown([m["effet"], entete_valeur(grandeur, parametre, langue), m["texte"],
                     m["journal"]], lignes_case(parametre, langue), a_droite=(1,))


def reperes(series: list[list[tuple]]) -> list[str]:
    """Dates repères d'une branche : sa première date d'effet, puis les dates communes. Pure."""
    debut = min(s[0][0] for s in series if s)
    return [debut] + [d for d in REPERES if d > debut]


def lignes_reperes(parametres: list, series: list[list[tuple]], dates: list[str],
                   langue: str = "fr") -> list[list[str]]:
    """L'état des cases aux dates repères : UNE DATE PAR LIGNE, une case par colonne. Pure.

    À l'inverse du tableau commun (`ot.tableau_dates_reperes`, un paramètre par ligne) : une
    grille a peu de cases et des montants longs, et six colonnes de dates insécables
    débordent de la page. La case vient du même composant, `ParametreDate.case` : « — »
    avant la première grille, la mention « non publiée » à compter d'une date sans valeur.
    """
    return [[date_insecable(date, langue)] + [p.case(s, date, langue)
                                               for p, s in zip(parametres, series)]
            for date in dates]


def fiche_case(chemin: tuple[str, ...], lignee: tuple[dict, ...], langue: str = "fr") -> dict:
    """L'entrée d'une case dans l'index : libellés, unité, fichier, période, comptes. Pure.

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
        "tableau": f"{PREFIXE}_{'_'.join(chemin)}.md",
        "parametre": f"{NOEUD}/{'/'.join(chemin)}.yaml",
        "debut": s[0][0] if s else None,
        "derniere_valeur": valuees[-1] if valuees else None,
        "dates": len(s),
        "valeurs": len(valuees),
        "sans_valeur": len(s) - len(valuees),
    }


def libelle_lien(branche: str, fiche: dict) -> str:
    """Libellé du lien « Base législative » : la branche, la case, la grandeur et son unité."""
    case = fiche["libelle"][:1].lower() + fiche["libelle"][1:]
    grandeur = fiche["grandeur"][:1].lower() + fiche["grandeur"][1:]
    suffixe = f" ({fiche['unite']})" if fiche["unite"] else ""
    return f"{branche} — {case} : {grandeur}{suffixe}"


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


def _entete(parametres: list[str]) -> str:
    return (f"<!-- Généré par scripts/{Path(__file__).name} — ne pas éditer à la main.\n"
            f"     Paramètres : {', '.join(parametres)} -->\n\n")


def _nettoie(dossier: Path, motif: str, ecrits: set[Path]) -> None:
    """Retire les snapshots d'une case qui n'existe plus : ils survivraient sans être gardés."""
    for ancien in dossier.glob(motif):
        if ancien not in ecrits:
            ancien.unlink()


def ecrire_branche(branche: str, noeud: dict, langue: str, ecrits: set[Path]) -> dict | None:
    """Écrit les tableaux d'une branche dans une langue ; rend son entrée d'index, ou None."""
    tables = RACINE / langue / LIVRE / "tables"
    tables.mkdir(parents=True, exist_ok=True)
    trouvees = cases(noeud, (branche,), (noeud,))
    if not trouvees:
        return None
    nom_branche = libelle(noeud)
    fiches = []
    for chemin, lignee in trouvees:
        fiche = fiche_case(chemin, lignee, langue)
        if not fiche["dates"]:
            print(f"✗ {langue}/{fiche['tableau']} : paramètre sans valeur datée.")
            return None
        fichier = tables / fiche["tableau"]
        fichier.write_text(_entete([fiche["parametre"]])
                           + tableau_case(fiche["grandeur"], lignee[-1], langue) + "\n",
                           encoding="utf-8")
        ot.ecrire_liens(fichier, [(fiche["parametre"], libelle_lien(nom_branche, fiche))], langue)
        ecrits |= {fichier, fichier.with_suffix(".liens.yml")}
        fiches.append(fiche)
    dates = reperes([serie(lignee[-1]) for _c, lignee in trouvees])
    entree = {
        "branche": branche,
        "libelle": nom_branche,
        "description": (noeud.get("description") or "").strip(),
        "serie": f"{PREFIXE_SERIE}-{branche}",
        "reperes": f"{PREFIXE}_{branche}_dates_reperes.md",
        "dates_reperes": dates,
        "cases": fiches,
    }
    ecrits |= {tables / entree["reperes"],
               (tables / entree["reperes"]).with_suffix(".liens.yml")}
    return entree


def parametres_dates(entree: dict) -> list:
    """Les cases d'une branche, déclarées pour la série longue et le tableau aux dates repères."""
    return [ot.ParametreDate(
        f["cle"], f["parametre"], {l: f["libelle"] for l in LANGUES},
        format=montant,
        lien={l: libelle_lien(entree["libelle"], f) for l in LANGUES},
        sans_valeur={l: MOTS[l]["sans_valeur"] for l in LANGUES}) for f in entree["cases"]]


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
        series = [p.serie() for p in parametres]
        for langue in LANGUES:
            fiches = index[langue][-1]["cases"]
            entetes = [MOTS[langue]["repere"]] + [
                f"{f['libelle']}<br>({f['unite']})" if f["unite"] else f["libelle"]
                for f in fiches]
            fichier = RACINE / langue / LIVRE / "tables" / entree["reperes"]
            fichier.write_text(
                f"<!-- Généré par scripts/{Path(__file__).name} — ne pas éditer à la main.\n"
                f"     État en vigueur aux dates : {', '.join(entree['dates_reperes'])}.\n"
                f"     Paramètres : {', '.join(p.chemin for p in parametres)} -->\n\n"
                + markdown(entetes, lignes_reperes(parametres, series,
                                                   entree["dates_reperes"], langue),
                           a_droite=tuple(range(1, len(entetes)))) + "\n", encoding="utf-8")
            ot.ecrire_liens(fichier, [(p.chemin, p.lien[langue]) for p in parametres], langue)
        series_ecrites |= {CACHE / f"{entree['serie']}.csv",
                           *(CACHE / f"{entree['serie']}.liens.{l}.yml" for l in LANGUES)}
    for langue in LANGUES:
        tables = RACINE / langue / LIVRE / "tables"
        (tables / INDEX).write_text(
            "# Généré par scripts/generate_conventions_collectives_tables.py — ne pas éditer "
            "à la main.\n" + yaml.safe_dump(index[langue], allow_unicode=True, sort_keys=False),
            encoding="utf-8")
        _nettoie(tables, f"{PREFIXE}_*.md", ecrits)
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

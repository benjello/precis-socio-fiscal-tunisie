"""Annexe « Les conventions collectives, branche par branche » : figures et renvois.

L'annexe ne nomme aucune case de grille : elle lit `tables/cc_index.yml`, que
`scripts/generate_conventions_collectives_tables.py` engendre, et déroule pour chaque branche
ses grilles et ses cases dans l'ordre de l'index. Une case ajoutée en amont entre dans la
page à la régénération, sans que l'annexe change.

Elle ne reproduit pas les grilles : pour chaque branche, une figure en escalier trace la plus
basse et la plus haute des cases de l'index, et un renvoi « Base législative » mène à la page
de chaque grille — ses cases, à toutes leurs dates, avec leurs références. Ce renvoi
est engendré avec l'index (`tables/cc_<branche>_grilles.liens.yml`), jamais écrit ici.

Ce module ne lit que des fichiers versionnés — l'index, les liens, la série longue de
`_seriescache/` : le build du site n'importe pas le générateur.
"""

from __future__ import annotations

import functools
import sys
from pathlib import Path

# Sans ce moteur, Jupyter affiche une seconde fois, sous la légende, toute figure restée
# ouverte en fin de bloc : la figure doublerait celle que rend `figure_tabs`.
import matplotlib

matplotlib.use("Agg")

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))

import figtools  # noqa: E402

TABLES = Path.cwd() / "tables"

# Une couleur par case tracée, de la plus basse à la plus haute (palette des figures du volume).
COULEURS = ("#08519c", "#d94801", "#238b45", "#6a51a3", "#a50f15", "#525252")

SANS_VALEUR = {"fr": "non publiée", "ar": "غير منشورة"}


@functools.lru_cache(maxsize=1)
def index() -> list[dict]:
    import yaml

    return yaml.safe_load((TABLES / "cc_index.yml").read_text(encoding="utf-8")) or []


def branche(nom: str) -> dict:
    for entree in index():
        if entree["branche"] == nom:
            return entree
    raise KeyError(f"branche absente de cc_index.yml : {nom}")


def _minuscule(texte: str) -> str:
    return texte[:1].lower() + texte[1:]


def _periode(case: dict) -> str:
    return f"{case['debut'][:4]}-{case['derniere_valeur'][:4]}"


def _unites(entree: dict) -> str:
    """« dinars par mois », ou les unités de la branche si elle en a plusieurs."""
    return " ou ".join(dict.fromkeys(c["unite"] for c in entree["cases"] if c["unite"]))


def tableau_branches(faits: dict[str, tuple[str, str, str]]) -> str:
    """Le tableau d'ouverture : une ligne par branche de l'index.

    `faits` : branche -> (convention, agrément, date d'effet) — la création de la convention,
    que l'index ne porte pas, écrite dans l'annexe avec ses références. Les cases tracées et
    leur période viennent de l'index et de la série. Rien n'y est dit des avenants : leur
    suite est au tableau de chaque branche.
    """
    lignes = ["| Branche | Convention | Arrêté d'agrément | Date d'effet | "
              "Cases de la grille tracées |", "|:---|:---|:---|:---|:---|"]
    # L'ordre des lignes est celui de l'annexe ; une branche que l'annexe ne décrit pas
    # encore suit, avec ses cases et des tirets.
    rang = {nom: i for i, nom in enumerate(faits)}
    for entree in sorted(index(), key=lambda e: rang.get(e["branche"], len(rang))):
        convention, agrement, effet = faits.get(entree["branche"], ("—",) * 3)
        tracees = _tracees(entree, figtools.series(entree["serie"]))
        cases = "<br>".join(f"{_minuscule(c['libelle'])}, {_periode(c)}" for c in tracees)
        lignes.append(f"| [{entree['libelle']}](#sec-mt-cc-annexe-{entree['branche']}) | "
                      f"{convention} | {agrement} | {effet} | {cases} |")
    return "\n".join(lignes)


INTRO_BASE = {
    "fr": "⚖️ Les cases de la grille, date par date, avec leurs références, dans la base "
          "législative :",
    "ar": "⚖️ خانات الشبكة، تاريخًا بتاريخ، مع مراجعها، في القاعدة التشريعية:",
}


def base_legislative(nom: str) -> str:
    """Le renvoi « Base législative » des grilles de la branche, sous sa figure.

    Un lien par grille, lu dans le fichier de liens que l'index désigne : la page publique de
    la grille, qui en donne les cases versées à toutes leurs dates. Le renvoi se présente
    comme la base législative, à la manière de l'onglet du même nom des tableaux engendrés.
    """
    import yaml

    langue = figtools.lang()
    liens = yaml.safe_load((TABLES / branche(nom)["liens_grilles"]).read_text(encoding="utf-8"))
    items = "\n".join(f"- [{e['libelle']}]({e['url']})" for e in liens or [])
    return f"{INTRO_BASE[langue]}\n\n{items}\n"


def _tracees(entree: dict, d) -> list[dict]:
    """Les cases que la figure trace : pour chaque unité, la plus basse et la plus haute,
    d'après leur dernière valeur. Une case située entre les deux — un échelon voisin du
    sommet, dont le trait se confondrait avec lui — se lit à la page de la grille."""
    derniere = {}
    for case in entree["cases"]:
        s = d[(d["case"] == case["cle"]) & d["valeur"].notna()].sort_values("date_effet")
        derniere[case["cle"]] = float(s.iloc[-1]["valeur"])
    gardees = set()
    for unite in {c["unite"] for c in entree["cases"]}:
        cles = [c["cle"] for c in entree["cases"] if c["unite"] == unite]
        gardees |= {min(cles, key=derniere.get), max(cles, key=derniere.get)}
    return [c for c in entree["cases"] if c["cle"] in gardees]


def _courbes(tracees: list[dict]) -> dict:
    return {c["cle"]: (c["libelle"], COULEURS[i % len(COULEURS)])
            for i, c in enumerate(tracees)}


EN_LETTRES = {1: "une", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six"}


def _legende_figure(entree: dict, tracees: list[dict]) -> str:
    """La légende de la figure, écrite d'après l'index : nombre de cases tracées, unité,
    première date d'effet et dernière date qui porte une valeur."""
    nombre = len(tracees)
    cases = f"{EN_LETTRES.get(nombre, nombre)} case{'s' if nombre > 1 else ''}"
    unite = _unites({"cases": tracees}).replace("dinars", "dinars courants")
    debut = min(c["debut"] for c in tracees)[:4]
    fin = max(c["derniere_valeur"] for c in tracees)[:4]
    return (f"{entree['description']} : {_minuscule(tracees[0]['grandeur'])} de {cases} de la "
            f"grille, à chaque date d'effet, en {unite}, {debut}-{fin}")


def _millimes(v: float) -> str:
    return f"{v:,.3f}".replace(",", " ").replace(".", ",")


def figure(nom: str, sources: list[str], note_lecture: str | None = None,
           caveats: str = "", generated: str | None = None,
           caption: str | None = None) -> None:
    """La grille de la branche en escalier (composant commun `figtools.figure_escalier`).

    Une marche par date d'effet ; seules la première et la dernière valeur de chaque case
    sont écrites, et une graduation sur cinq : une grille change chaque année ou presque.
    Le cercle creux marque la date à compter de laquelle le montant n'est pas publié.
    La figure trace la plus basse et la plus haute des cases de l'index (`_tracees`) ; sa
    légende est écrite d'après l'index, sauf si `caption` la donne.
    """
    entree = branche(nom)
    serie = entree["serie"]
    d = figtools.series(serie)
    tracees = _tracees(entree, d)
    d = d[d["case"].isin([c["cle"] for c in tracees])]
    dates = sorted({str(x)[:10] for x in d["date_effet"]})
    sommet = float(d["valeur"].max())
    # Mentions candidates : première et dernière valeur de chaque case, et la date sans
    # valeur. Deux cases voisines — deux échelons d'une même échelle — porteraient leurs
    # mentions l'une sur l'autre : à une même date, seule la plus haute est écrite.
    candidates = []
    for case in tracees:
        s = d[d["case"] == case["cle"]].sort_values("date_effet")
        valuees = s[s["valeur"].notna()]
        for rang, dy in ((0, -8), (-1, 8)):
            ligne = valuees.iloc[rang]
            candidates.append((float(ligne["valeur"]), case["cle"], str(ligne["date_effet"])[:10], {
                "texte": _millimes(float(ligne["valeur"])), "xytext": (0, dy),
                "ha": "center", "va": "top" if dy < 0 else "bottom"}))
        for date in s[s["valeur"].isna()]["date_effet"]:
            candidates.append((float(valuees.iloc[-1]["valeur"]), case["cle"], str(date)[:10],
                               SANS_VALEUR[figtools.lang()]))
    annotations, gardees = {}, []
    for y, cle, date, mention in sorted(candidates, key=lambda c: -c[0]):
        if any(date == autre and abs(y - haut) < 0.05 * sommet for haut, autre in gardees):
            continue
        gardees.append((y, date))
        annotations[(cle, date)] = mention
    debut, fin = int(dates[0][:4]), int(dates[-1][:4])
    # Une graduation par date d'effet, mais une année écrite sur cinq, à distance de la
    # première date et de la dernière année, que le composant écrit toujours.
    etiquettes, ecrites = {}, set()
    for i, date in enumerate(dates):
        annee = int(date[:4])
        garde = i == 0 or (annee % 5 == 0 and annee not in ecrites
                           and annee - debut >= 3 and fin - annee >= 3)
        etiquettes[date] = date[:4] if garde else ""
        ecrites.add(annee)
    figtools.register_provenance(
        serie,
        titre=(f"{entree['description']} : salaires de base de la plus basse et de la plus "
               f"haute des cases données de la grille, à chaque date d'effet"),
        sources=sources,
        source_ligne=("grilles annexées à la convention et à ses avenants, publiées au "
                      "*Journal officiel* (liste dans l'onglet « Sources »)"),
        unite=_unites({"cases": tracees}),
        perimetre=("une ligne par case de la grille et par date d'effet ; "
                   + " ; ".join(_minuscule(c["libelle"]) for c in tracees)),
        caveats=caveats,
    )
    figtools.figure_escalier(
        serie, _courbes(tracees), slug=f"fig_mt_cc_annexe_{nom}",
        caption=caption or _legende_figure(entree, tracees),
        note_lecture=note_lecture, generated=generated, fin=fin, colonne="case",
        nominal=True, format_valeur=lambda v: "", format_infobulle=_millimes,
        annotations=annotations,
        etiquettes_x=etiquettes, ylim=(0, 1.1 * sommet),
        ylabel=f"{tracees[0]['grandeur']}, en {_unites({'cases': tracees})}",
        supprime=SANS_VALEUR[figtools.lang()],
        libelles={"parametre": "Case de la grille", "suppression": "montant non publié"})

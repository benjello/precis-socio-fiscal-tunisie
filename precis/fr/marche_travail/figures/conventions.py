"""Annexe « Les conventions collectives, branche par branche » : tableaux et figures.

L'annexe ne nomme aucune case de grille : elle lit `tables/cc_index.yml`, que
`scripts/generate_conventions_collectives_tables.py` engendre avec les tableaux, et déroule
pour chaque branche ses cases dans l'ordre de l'index. Une case ajoutée en amont entre dans
la page à la régénération, sans que l'annexe change.

Ce module ne lit que des fichiers versionnés — l'index, les tableaux, la série longue de
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
import openfisca_tables as ot  # noqa: E402

TABLES = Path.cwd() / "tables"

# Une couleur par case, dans l'ordre de l'index (palette des figures du volume).
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


def tableau_branches(faits: dict[str, tuple[str, str, str, str]]) -> str:
    """Le tableau d'ouverture : une ligne par branche de l'index.

    `faits` : branche -> (convention, agrément, date d'effet, avenants) — ce que les
    paramètres ne portent pas, écrit dans l'annexe avec ses références. Les cases données et
    leur période viennent de l'index.
    """
    lignes = ["| Branche | Convention | Arrêté d'agrément | Date d'effet | Textes qui la "
              "révisent | Cases de la grille données ici |", "|:---|:---|:---|:---|:---|:---|"]
    # L'ordre des lignes est celui de l'annexe ; une branche que l'annexe ne décrit pas
    # encore suit, avec ses cases et des tirets.
    rang = {nom: i for i, nom in enumerate(faits)}
    for entree in sorted(index(), key=lambda e: rang.get(e["branche"], len(rang))):
        convention, agrement, effet, avenants = faits.get(entree["branche"], ("—",) * 4)
        cases = "<br>".join(f"{_minuscule(c['libelle'])}, {_periode(c)}"
                            for c in entree["cases"])
        lignes.append(f"| [{entree['libelle']}](#sec-mt-cc-annexe-{entree['branche']}) | "
                      f"{convention} | {agrement} | {effet} | {avenants} | {cases} |")
    return "\n".join(lignes)


def reperes(nom: str) -> str:
    """Les cases de la branche à ses dates repères, avec l'onglet « Base législative »."""
    entree = branche(nom)
    dates = entree["dates_reperes"]
    legende = (f"{entree['libelle']} : salaire de base en vigueur dans les cases données, "
               f"en {_unites(entree)}, à {len(dates)} dates repères, "
               f"{dates[0][:4]}-{dates[-1][:4]}")
    return ot.markdown_avec_legende(TABLES / entree["reperes"], legende,
                                    f"tbl-cc-{nom}-reperes")


def cases(nom: str) -> str:
    """Un bloc replié par case : son tableau entier, date d'effet par date d'effet."""
    entree = branche(nom)
    blocs = []
    for case in entree["cases"]:
        slug = case["cle"].replace(".", "-").replace("_", "-")
        grandeur = _minuscule(case["grandeur"])
        titre = (f"{entree['libelle']}, {_minuscule(case['libelle'])} : {grandeur} aux "
                 f"{case['valeurs']} dates d'effet de la grille, {_periode(case)} — montant "
                 f"en {case['unite']}, texte et page du Journal officiel")
        legende = (f"{entree['libelle']}, {_minuscule(case['libelle'])} : {grandeur} par "
                   f"date d'effet, en {case['unite']}, {_periode(case)}")
        tableau = ot.markdown_avec_legende(
            TABLES / case["tableau"], legende, f"tbl-cc-{nom}-{slug}",
            colonnes='tbl-colwidths="[17,13,45,25]"')
        blocs.append(f':::: {{.chronologie-repliable titre="{titre}"}}\n\n{tableau}\n::::\n')
    return "\n".join(blocs)


def _courbes(entree: dict) -> dict:
    return {c["cle"]: (c["libelle"], COULEURS[i % len(COULEURS)])
            for i, c in enumerate(entree["cases"])}


def _millimes(v: float) -> str:
    return f"{v:,.3f}".replace(",", " ").replace(".", ",")


def figure(nom: str, caption: str, sources: list[str], note_lecture: str | None = None,
           caveats: str = "", generated: str | None = None) -> None:
    """La grille de la branche en escalier (composant commun `figtools.figure_escalier`).

    Une marche par date d'effet ; seules la première et la dernière valeur de chaque case
    sont écrites, et une graduation sur cinq : une grille change chaque année ou presque.
    Le cercle creux marque la date à compter de laquelle le montant n'est pas publié.
    """
    entree = branche(nom)
    serie = entree["serie"]
    d = figtools.series(serie)
    dates = sorted({str(x)[:10] for x in d["date_effet"]})
    sommet = float(d["valeur"].max())
    # Mentions candidates : première et dernière valeur de chaque case, et la date sans
    # valeur. Deux cases voisines — deux échelons d'une même échelle — porteraient leurs
    # mentions l'une sur l'autre : à une même date, seule la plus haute est écrite.
    candidates = []
    for case in entree["cases"]:
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
        titre=(f"{entree['description']} : salaires de base des cases données de la grille, "
               f"à chaque date d'effet"),
        sources=sources,
        source_ligne=("grilles annexées à la convention et à ses avenants, publiées au "
                      "*Journal officiel* (liste dans l'onglet « Sources »)"),
        unite=_unites(entree),
        perimetre=("une ligne par case de la grille et par date d'effet ; "
                   + " ; ".join(_minuscule(c["libelle"]) for c in entree["cases"])),
        caveats=caveats,
    )
    figtools.figure_escalier(
        serie, _courbes(entree), slug=f"fig_mt_cc_annexe_{nom}", caption=caption,
        note_lecture=note_lecture, generated=generated, fin=fin, colonne="case",
        nominal=True, format_valeur=lambda v: "", format_infobulle=_millimes,
        annotations=annotations,
        etiquettes_x=etiquettes, ylim=(0, 1.1 * sommet), ylabel=f"{entree['cases'][0]['grandeur']}, en {_unites(entree)}",
        supprime=SANS_VALEUR[figtools.lang()],
        libelles={"parametre": "Case de la grille", "suppression": "montant non publié"})

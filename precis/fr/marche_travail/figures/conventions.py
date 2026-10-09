"""Annexe « Les conventions collectives, branche par branche » : figures et renvois.

L'annexe ne nomme aucune case de grille : elle lit `tables/cc_index.yml`, que
`scripts/generate_conventions_collectives_tables.py` engendre, et déroule pour chaque branche
ses grilles et ses cases dans l'ordre de l'index. Une case ajoutée en amont entre dans la
page à la régénération, sans que l'annexe change.

Elle ne reproduit pas les grilles : pour chaque branche, une figure trace la plus basse et la
plus haute des cases de l'index — en dinars courants, en escalier, une marche par date
d'effet ; en dinars constants, un point par année, avec l'indice et l'année de base du volume
(`deflateur.py`) —, et un renvoi « Base législative » mène à la page
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

from . import deflateur  # noqa: E402

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


def _legende_figure(entree: dict, tracees: list[dict], constants: list, base: int) -> str:
    """La légende de la figure, écrite d'après l'index et la série : nombre de cases tracées,
    unité, première date d'effet et dernière date qui porte une valeur ; première et
    dernière année de la vue en dinars constants."""
    nombre = len(tracees)
    cases = f"{EN_LETTRES.get(nombre, nombre)} case{'s' if nombre > 1 else ''}"
    unite = _unites({"cases": tracees}).replace("dinars", "dinars courants")
    debut = min(c["debut"] for c in tracees)[:4]
    fin = max(c["derniere_valeur"] for c in tracees)[:4]
    annees = [annee for _cle, annee, *_ in constants]
    return (f"{entree['description']} : {_minuscule(tracees[0]['grandeur'])} de {cases} de la "
            f"grille, en {unite} à chaque date d'effet ({debut}-{fin}) et en "
            f"{_unite_constante(tracees, base)}, en moyenne de l'année "
            f"({min(annees)}-{max(annees)})")


DINAR = {"fr": ("dinars", "dinars de {base}"), "ar": ("دينار", "دينار سنة {base}")}

METHODE_CONSTANTS = {
    "fr": ("En dinars de {base}, chaque point est la moyenne des montants en vigueur au "
           "premier jour des douze mois de l'année, multipliée par le rapport de l'indice des "
           "prix à la consommation de {base} à celui de l'année — la règle de la figure du "
           "salaire minimum (@fig-mt-sm-evolution). Entre deux grilles, la courbe descend "
           "donc au rythme des prix, et une grille la remonte. Une année dont la grille ne "
           "couvre pas les douze mois n'a pas de point ; {base} est la dernière année dont "
           "l'indice est publié, et la vue s'y arrête."),
    "ar": ("بدينار سنة {base}، كلّ نقطة هي معدّل المبالغ النافذة في اليوم الأوّل من كلّ شهر من "
           "أشهر السنة الاثني عشر، مضروبًا في نسبة الرقم القياسي لأسعار الاستهلاك لسنة {base} "
           "إلى رقم السنة — وهي قاعدة شكل الأجر الأدنى (@fig-mt-sm-evolution). بين شبكتين "
           "ينزل المنحنى إذن بنسق الأسعار، وترفعه الشبكة الجديدة. السنة التي لا تغطّي "
           "الشبكة أشهرها الاثني عشر لا نقطة لها؛ و{base} آخر سنة نُشر رقمها "
           "القياسي، وعندها تقف القراءة."),
}

LECTURE_CONSTANTS = {
    "fr": ("{case} : {v0} en {a0}, {vfin} en {afin}", " ; plus haut niveau, {vmax}, en {amax}",
           " ; plus haut niveau en {amax}", "En {unite} — ", " ; ", "."),
    "ar": ("{case}: {v0} سنة {a0}، {vfin} سنة {afin}", "؛ أعلى مستوى، {vmax}، سنة {amax}",
           "؛ أعلى مستوى سنة {amax}", "ب{unite} — ", "؛ ", "."),
}


# Intitulés de la vue en dinars constants — colonnes de l'onglet « Données », la grandeur
# et son unité entre parenthèses ; axe vertical.
COLONNES = {
    "fr": {"moyenne": "{grandeur}, moyenne de l'année ({courant})",
           "ipc": "Indice des prix à la consommation (base 100 en 1970)",
           "reel": "{grandeur} ({constant})", "axe": "{grandeur}, en {constant}"},
    "ar": {"moyenne": "{grandeur}، المعدّل السنوي ({courant})",
           "ipc": "الرقم القياسي لأسعار الاستهلاك (أساس 100 سنة 1970)",
           "reel": "{grandeur} ({constant})", "axe": "{grandeur}، ب{constant}"},
}


def _intitules(tracees: list[dict], base: int) -> dict:
    courant = _unites({"cases": tracees})
    if figtools.lang() == "fr":
        courant = courant.replace("dinars", "dinars courants")
    return {cle: modele.format(grandeur=tracees[0]["grandeur"], courant=courant,
                               constant=_unite_constante(tracees, base))
            for cle, modele in COLONNES[figtools.lang()].items()}


def _unite_constante(tracees: list[dict], base: int) -> str:
    """« dinars de 2025 par heure » : l'unité de l'index, le dinar daté de l'année de base."""
    courant, constant = DINAR[figtools.lang()]
    return _unites({"cases": tracees}).replace(courant, constant.format(base=base))


def _decimales(sommet: float) -> int:
    """Un salaire horaire se lit au millime ; un salaire mensuel, au dixième de dinar."""
    return 3 if sommet < 20 else 1


def _constants(serie: str, tracees: list[dict]):
    """Les cases tracées en dinars constants, par année : (lignes, année de base), avec
    l'indice et l'année de base du volume (`figtools.constants_escalier`)."""
    return figtools.constants_escalier(serie, _courbes(tracees), colonne="case",
                                       base=deflateur.ANNEE_BASE, ipc=deflateur.ipc())


def lecture_constants(tracees: list[dict], constants: list, base: int) -> str:
    """La phrase de lecture en dinars constants, calculée sur les points que la figure
    trace : pour chaque case, le niveau de la première année, celui de la dernière, et le
    plus haut avec son année."""
    case_fmt, haut, haut_borne, tete, separateur, point = LECTURE_CONSTANTS[figtools.lang()]
    sommet = max(reel for *_, reel in constants)
    d = _decimales(sommet)

    def montant(v: float) -> str:
        return f"{v:,.{d}f}".replace(",", " ").replace(".", ",")

    phrases = []
    for case in tracees:
        points = [(annee, reel) for cle, annee, _m, _i, reel in constants if cle == case["cle"]]
        if not points:
            continue
        (a0, v0), (afin, vfin) = points[0], points[-1]
        amax, vmax = max(points, key=lambda p: p[1])
        phrase = case_fmt.format(case=_minuscule(case["libelle"]), v0=montant(v0), a0=a0,
                                 vfin=montant(vfin), afin=afin)
        phrase += (haut_borne if amax in (a0, afin) else haut).format(vmax=montant(vmax),
                                                                     amax=amax)
        phrases.append(phrase)
    return (tete.format(unite=_unite_constante(tracees, base)) + separateur.join(phrases)
            + point)


def _millimes(v: float) -> str:
    return f"{v:,.3f}".replace(",", " ").replace(".", ",")


def figure(nom: str, sources: list[str], note_lecture: str | None = None,
           caveats: str = "", generated: str | None = None,
           caption: str | None = None) -> None:
    """La grille de la branche, en deux vues (composant commun `figtools.figure_escalier`) :
    dinars courants, en escalier ; dinars de l'année de base du volume, un point par année.

    La note de lecture reçue décrit la vue en dinars courants ; la règle des dinars constants
    et la phrase de lecture qui en donne les niveaux s'y ajoutent ici, calculées. L'onglet
    « Données » porte la série annuelle : moyenne en dinars courants, indice, dinars constants.

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
    constants, base = _constants(serie, tracees)
    langue = figtools.lang()
    intitules = _intitules(tracees, base)
    note = " ".join(filter(None, [
        note_lecture, METHODE_CONSTANTS[langue].format(base=base),
        lecture_constants(tracees, constants, base)]))
    figtools.figure_escalier(
        serie, _courbes(tracees), slug=f"fig_mt_cc_annexe_{nom}",
        caption=caption or _legende_figure(entree, tracees, constants, base),
        note_lecture=note, generated=generated, fin=fin, colonne="case",
        constants=True, base=base, ipc=deflateur.ipc(), series_ipc=deflateur.SERIES_IPC,
        decimales_constants=_decimales(sommet),
        ylabel_constants=intitules["axe"],
        format_valeur=lambda v: "", format_infobulle=_millimes,
        annotations=annotations,
        etiquettes_x=etiquettes, ylim=(0, 1.1 * sommet),
        ylabel=f"{tracees[0]['grandeur']}, en {_unites({'cases': tracees})}",
        supprime=SANS_VALEUR[figtools.lang()],
        libelles={"parametre": "Case de la grille", "suppression": "montant non publié",
                  **intitules})

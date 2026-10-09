"""Annexe « Les conventions collectives, branche par branche » : figures, tableaux et renvois.

L'annexe ne nomme aucune case de grille : elle lit `tables/cc_index.yml`, que
`scripts/generate_conventions_collectives_tables.py` engendre, et déroule pour chaque branche
ses grilles dans l'ordre de l'index. Une grille ajoutée en amont entre dans les tableaux et
dans les renvois à la régénération ; sa figure se déclare dans l'annexe (`figure`), et
`autres_grilles` refuse de rendre une branche dont une grille tracée n'a pas la sienne.

Elle ne reproduit pas les grilles. CHAQUE GRILLE COURANTE A SA FIGURE, qui en trace la case du
bas et celle du haut — en dinars courants, en escalier, une marche par date d'effet ; en dinars
constants, un point par année, avec l'indice et l'année de base du volume (`deflateur.py`). Le
bas et le haut sont ceux de l'index : choisis par le générateur, grille par grille, à la
dernière date publiée de la grille (sa règle et ses tests sont là-bas). Une grille antérieure,
ou qui n'a qu'une ou deux dates, n'a pas de courbe : `autres_grilles` la mentionne, avec sa
période et son renvoi.

Un renvoi « Base législative » mène à la vue en tableau de chaque grille — ses cases, à
toutes leurs dates, avec leurs références —, ou, quand la grille est trop grande pour une
seule vue, à celle de chacune de ses lignes. Ces liens sont engendrés avec l'index
(`tables/cc_<branche>_grilles.liens.yml`), jamais écrits ici.

Ce module ne lit que des fichiers versionnés — l'index, les liens, les séries longues de
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


def _majuscule(texte: str) -> str:
    return texte[:1].upper() + texte[1:]


def grilles(nom: str, tracees: bool | None = None) -> list[dict]:
    """Les grilles de la branche, dans l'ordre de l'index ; `tracees` : celles qui ont une
    courbe (True), celles qui n'en ont pas (False), toutes (None)."""
    return [g for g in branche(nom)["grilles"] if tracees is None or g["tracee"] == tracees]


def une_grille(nom: str, cle: str | None = None) -> dict:
    """Une grille de la branche, par sa clé de l'index ; à défaut, sa première grille tracée."""
    if cle is None:
        return grilles(nom, tracees=True)[0]
    for g in grilles(nom):
        if g["cle"] == cle:
            return g
    raise KeyError(f"grille absente de cc_index.yml : {nom}, {cle}")


def _nom_grille(g: dict) -> str:
    """Le nom d'une grille : son libellé ; à défaut — la grandeur est elle-même la grille —,
    celui de la grandeur."""
    return g["libelle"] or g["grandeur"]


def _nom_case(g: dict, case: dict) -> str:
    """« Catégorie I, échelon 0 » : le libellé de la case, sans celui de sa grille."""
    tete = f"{g['libelle']}, "
    court = case["libelle"][len(tete):] if g["libelle"] and case["libelle"].startswith(tete) \
        else case["libelle"]
    return _majuscule(court)


def _tracees(g: dict) -> list[dict]:
    """Les cases que la figure d'une grille trace : son bas et son haut, tels que l'index les
    donne ; une seule case si la grille n'en a qu'une."""
    return list({c["cle"]: c for c in (g["bas"], g["haut"])}.values())


def _periode(debut: str, fin: str) -> str:
    return debut[:4] if debut[:4] == fin[:4] else f"{debut[:4]}-{fin[:4]}"


def _periode_cellule(debut: str, fin: str) -> str:
    """La période dans une cellule de tableau : elle ne se coupe pas au trait d'union."""
    return f"[{_periode(debut, fin)}]{{.insecable}}"


def _entete_grille(g: dict) -> str:
    """Le nom de la grille, son unité entre parenthèses dessous."""
    return f"{_nom_grille(g)}<br>({g['unite']})" if g["unite"] else _nom_grille(g)


MOTS = {
    "fr": {
        "branches": ("Branche", "Convention : signature, arrêté d'agrément, date d'effet",
                     "Grille<br>(unité)", "Bas et haut tracés, avec leur période"),
        "creation": "{convention}<br>agréée le {agrement}<br>en vigueur le {effet}",
        "grilles": ("Branche", "Grille<br>(unité)", "Lignes", "Colonnes", "Cases",
                    "Dates d'effet", "Période", "Cases vides"),
        "forme_titre": "La forme de la grille.",
        "forme_titre_nommee": "{grille} : la forme de la grille.",
        "forme": "{l} ligne{sl} et {c} colonne{sc}, soit {n} case{sn}",
        "forme_une": "Dans la base législative, la grille a {forme} à chacune de ses {d} "
                     "dates d'effet, de {debut} à {fin}.",
        "forme_tete": "Dans la base législative, la grille a ",
        "forme_de_a": "{forme} de {debut} à {fin}", "forme_en": "{forme} en {debut}",
        "forme_depuis": "{forme} depuis {debut}", "puis": " ; puis ",
        "une_date": "une date d'effet, {debut}", "des_dates": "{n} dates d'effet, {periode}",
        "vides": "{branche}{grille} : {n}, {dates}",
        "vides_une": "à la grille de {annees}", "vides_des": "aux grilles de {annees}",
        "et": " et ", "ligne_par_ligne": ", ligne par ligne : ",
        "autres": "⚖️ Les autres grilles de la branche, dans la base législative :",
    },
    "ar": {
        "branches": ("الفرع", "الاتفاقية: الإمضاء، قرار المصادقة، تاريخ المفعول",
                     "الشبكة<br>(الوحدة)", "أسفل الشبكة وأعلاها المرسومان، مع فترتهما"),
        "creation": "{convention}<br>قرار المصادقة: {agrement}<br>تاريخ المفعول: {effet}",
        "grilles": ("الفرع", "الشبكة<br>(الوحدة)", "الأسطر", "الأعمدة", "الخانات",
                    "تواريخ المفعول", "الفترة", "الخانات الفارغة"),
        "forme_titre": "شكل الشبكة.", "forme_titre_nommee": "{grille}: شكل الشبكة.",
        "forme": "{l} سطرًا و{c} عمودًا، أي {n} خانة",
        "forme_une": "في القاعدة التشريعية، للشبكة {forme} في كلّ من تواريخ مفعولها "
                     "الـ{d}، من {debut} إلى {fin}.",
        "forme_tete": "في القاعدة التشريعية، للشبكة ",
        "forme_de_a": "{forme} من {debut} إلى {fin}", "forme_en": "{forme} سنة {debut}",
        "forme_depuis": "{forme} منذ {debut}", "puis": "؛ ثمّ ",
        "une_date": "تاريخ مفعول واحد، {debut}", "des_dates": "{n} تواريخ مفعول، {periode}",
        "vides": "{branche}{grille}: {n}، {dates}",
        "vides_une": "في شبكة {annees}", "vides_des": "في شبكات {annees}",
        "et": " و", "ligne_par_ligne": "، سطرًا بسطر: ",
        "autres": "⚖️ الشبكات الأخرى للفرع، في القاعدة التشريعية:",
    },
}


def _mention_sans_courbe(g: dict) -> str:
    """Ce qu'une grille sans courbe porte : ses dates d'effet et sa période."""
    m = MOTS[figtools.lang()]
    if g["dates"] == 1:
        return m["une_date"].format(debut=g["debut"][:4])
    return m["des_dates"].format(n=g["dates"], periode=_periode(g["debut"], g["fin"]))


def _branches_ordonnees(ordre) -> list[dict]:
    """Les branches de l'index dans l'ordre de l'annexe ; celles qu'elle ne décrit pas encore
    suivent."""
    rang = {nom: i for i, nom in enumerate(ordre)}
    return sorted(index(), key=lambda e: rang.get(e["branche"], len(rang)))


def tableau_branches(faits: dict[str, tuple[str, str, str]]) -> str:
    """Le tableau d'ouverture : une ligne par grille de l'index.

    `faits` : branche -> (convention, agrément, date d'effet) — la création de la convention,
    que l'index ne porte pas, écrite dans l'annexe avec ses références ; elle tient en une
    cellule, à la première grille de la branche. La grille, son unité, le bas et le haut tracés et leur
    période viennent de l'index. Une grille sans courbe porte ses dates d'effet et sa
    période. Rien n'y est dit des avenants : leur suite est au tableau de chaque branche.
    """
    m = MOTS[figtools.lang()]
    lignes = ["| " + " | ".join(m["branches"]) + " |", "|:---|:---|:---|:---|"]
    for entree in _branches_ordonnees(faits):
        creation = "—"
        if entree["branche"] in faits:
            convention, agrement, effet = faits[entree["branche"]]
            creation = m["creation"].format(convention=convention, agrement=agrement,
                                            effet=effet)
        tete = f"[{entree['libelle']}](#sec-mt-cc-annexe-{entree['branche']})"
        for g in entree["grilles"]:
            if g["tracee"]:
                contenu = "<br>".join(
                    f"{_minuscule(_nom_case(g, c))}, "
                    f"{_periode_cellule(c['debut'], c['derniere_valeur'])}" for c in _tracees(g))
            else:
                contenu = _mention_sans_courbe(g)
            lignes.append(f"| {tete} | {creation} | {_entete_grille(g)} | {contenu} |")
            tete = creation = ""
    return "\n".join(lignes)


def _entier(n: int) -> str:
    return f"{n:,}".replace(",", " ")


def tableau_grilles(ordre=()) -> str:
    """Ce que la base législative porte de chaque grille : une ligne par grille de l'index.

    Lignes (catégories, échelles ou emplois), colonnes (échelons, stage compris ; une seule
    quand la grille n'a pas d'échelon) et cases de la grille À SA DERNIÈRE DATE PUBLIÉE — sa
    forme d'avant est dite par `forme_grille` —, dates d'effet publiées, période, et cases
    vides, toutes dates confondues — celles d'une grille publiée dont le montant est
    illisible. Tout vient de l'index.
    """
    entetes = MOTS[figtools.lang()]["grilles"]
    lignes = ["| " + " | ".join(entetes) + " |", "|:---|:---|---:|---:|---:|---:|:---|---:|"]
    for entree in _branches_ordonnees(ordre):
        tete = f"[{entree['libelle']}](#sec-mt-cc-annexe-{entree['branche']})"
        for g in entree["grilles"]:
            lignes.append(
                f"| {tete} | {_entete_grille(g)} | {g['formes'][-1]['lignes']} | "
                f"{g['formes'][-1]['colonnes']} | {_entier(g['formes'][-1]['cases'])} | "
                f"{g['dates']} | "
                f"{_periode_cellule(g['debut'], g['fin'])} | "
                f"{g['cases_vides']} |")
            tete = ""
    return "\n".join(lignes)


def _forme(f: dict) -> str:
    def s(n):
        return "s" if n > 1 else ""
    return MOTS[figtools.lang()]["forme"].format(
        l=f["lignes"], sl=s(f["lignes"]), c=f["colonnes"], sc=s(f["colonnes"]),
        n=_entier(f["cases"]), sn=s(f["cases"]))


def forme_grille(nom: str, cle: str | None = None) -> str:
    """« Dans la base législative, la grille a 18 lignes et 17 colonnes, soit 306 cases, de
    1994 à 1998 ; puis 18 lignes et 21 colonnes, soit 378 cases, depuis 1999. » : les formes
    successives de la grille, telles que l'index les compte. Aucun de ces nombres n'est
    écrit dans l'annexe."""
    m = MOTS[figtools.lang()]
    g = une_grille(nom, cle)
    formes = g["formes"]
    if len(formes) == 1:
        return m["forme_une"].format(forme=_forme(formes[0]), d=g["dates"],
                                     debut=g["debut"][:4], fin=g["fin"][:4])
    morceaux = []
    for rang, f in enumerate(formes):
        debut, fin = f["depuis"][:4], f["jusqu_a"][:4]
        modele = ("forme_depuis" if rang == len(formes) - 1
                  else "forme_en" if debut == fin else "forme_de_a")
        morceaux.append(m[modele].format(forme=_forme(f), debut=debut, fin=fin))
    return m["forme_tete"] + m["puis"].join(morceaux) + "."


def formes_branche(nom: str) -> str:
    """Une puce par grille de la branche : sa forme, comptée (`forme_grille`)."""
    m = MOTS[figtools.lang()]
    toutes = grilles(nom)
    puces = []
    for g in toutes:
        titre = m["forme_titre"] if len(toutes) == 1 else \
            m["forme_titre_nommee"].format(grille=_nom_grille(g))
        puces.append(f"- **{titre}** {forme_grille(nom, g['cle'])}")
    return "\n".join(puces) + "\n"


def _enumere(elements: list[str]) -> str:
    et = MOTS[figtools.lang()]["et"]
    return elements[0] if len(elements) == 1 else ", ".join(elements[:-1]) + et + elements[-1]


def cases_vides(ordre=()) -> str:
    """« Textile, agents payés au mois : 127, aux grilles de 1994, 1999… ; … » : le compte des
    cases vides de chaque grille qui en a, et les années des grilles où elles sont. Calculé."""
    m = MOTS[figtools.lang()]
    morceaux = []
    for entree in _branches_ordonnees(ordre):
        for g in entree["grilles"]:
            if not g["cases_vides"]:
                continue
            annees = list(dict.fromkeys(d[:4] for d in g["dates_cases_vides"]))
            dates = m["vides_une" if len(annees) == 1 else "vides_des"].format(
                annees=_enumere(annees))
            # Une grille sans libellé propre se nomme par sa grandeur dès que la branche en
            # a plusieurs : deux grilles ne portent pas le même nom.
            nom = g["libelle"] or (g["grandeur"] if len(entree["grilles"]) > 1 else "")
            nom = f", {_minuscule(nom)}" if nom else ""
            morceaux.append(m["vides"].format(branche=entree["libelle"], grille=nom,
                                              n=g["cases_vides"], dates=dates))
    return " ; ".join(morceaux)


INTRO_BASE = {
    "fr": "⚖️ Les cases de la grille, date par date, avec leurs références, dans la base "
          "législative :",
    "ar": "⚖️ خانات الشبكة، تاريخًا بتاريخ، مع مراجعها، في القاعدة التشريعية:",
}

# Les grilles dont la figure a été rendue, par branche : `autres_grilles` s'en assure.
_FIGUREES: dict[str, set[str]] = {}


def _liens(nom: str) -> dict[str, list[dict]]:
    """Les liens « Base législative » de la branche, par grille, dans l'ordre du fichier."""
    import yaml

    liens = yaml.safe_load((TABLES / branche(nom)["liens_grilles"]).read_text(encoding="utf-8"))
    par_grille: dict[str, list[dict]] = {}
    for e in liens or []:
        par_grille.setdefault(e["grille"], []).append(e)
    return par_grille


def _puce_liens(liens: list[dict], suite: str = "") -> str:
    """La puce d'une grille : son lien, ou — une vue par ligne — ses lignes, chacune liée."""
    if len(liens) == 1 and not liens[0]["ligne"]:
        return f"- [{liens[0]['libelle']}]({liens[0]['url']}){suite}"
    lignes = " · ".join(f"[{_minuscule(e['ligne'])}]({e['url']})" for e in liens)
    return (f"- {liens[0]['libelle_grille']}{suite}"
            f"{MOTS[figtools.lang()]['ligne_par_ligne']}{lignes}")


def base_legislative(nom: str, cle: str | None = None) -> str:
    """Le renvoi « Base législative » d'une grille de la branche, sous sa figure ; sans `cle`,
    celui de toutes ses grilles tracées.

    Les liens sont lus dans le fichier que l'index désigne : la vue en tableau de la grille,
    qui en donne les cases à toutes leurs dates, ou celle de chacune de ses lignes quand la
    grille est trop grande pour une seule vue. Le renvoi se présente comme la base
    législative, à la manière de l'onglet du même nom des tableaux engendrés.
    """
    liens = _liens(nom)
    cles = [cle] if cle else [g["cle"] for g in grilles(nom, tracees=True)]
    items = "\n".join(_puce_liens(liens[c]) for c in cles)
    return f"{INTRO_BASE[figtools.lang()]}\n\n{items}\n"


def autres_grilles(nom: str) -> str:
    """Les grilles de la branche qui n'ont pas de courbe — antérieures, ou d'une ou deux
    dates — : leur période et leur renvoi « Base législative ». Vide s'il n'y en a pas.

    À appeler après les figures de la branche : lève une erreur si une grille tracée n'a pas
    eu la sienne — une grille nouvelle ne passe pas inaperçue.
    """
    manquantes = [g["cle"] for g in grilles(nom, tracees=True)
                  if g["cle"] not in _FIGUREES.get(nom, set())]
    if manquantes:
        raise RuntimeError(f"{nom} : grille(s) tracée(s) sans figure dans l'annexe : "
                           f"{manquantes}. Déclarer `cc.figure(\"{nom}\", grille=…)`.")
    sans = grilles(nom, tracees=False)
    if not sans:
        return ""
    liens = _liens(nom)
    items = "\n".join(_puce_liens(liens[g["cle"]], f" — {_mention_sans_courbe(g)}") for g in sans)
    return f"{MOTS[figtools.lang()]['autres']}\n\n{items}\n"


def _courbes(g: dict) -> dict:
    return {c["cle"]: (_nom_case(g, c), COULEURS[i % len(COULEURS)])
            for i, c in enumerate(_tracees(g))}


def _legende_figure(entree: dict, g: dict, constants: list, base: int) -> str:
    """La légende de la figure, écrite d'après l'index et la série : la branche et la grille,
    l'unité, la première date d'effet et la dernière date publiée ; première et dernière
    année de la vue en dinars constants."""
    grille_ = f", {_minuscule(g['libelle'])}" if g["libelle"] else ""
    unite = g["unite"].replace("dinars", "dinars courants")
    annees = [annee for _cle, annee, *_ in constants]
    return (f"{entree['description']}{grille_} : {_minuscule(g['grandeur'])} du bas et du "
            f"haut de la grille, en {unite} à chaque date d'effet "
            f"({_periode(g['debut'], g['fin'])}) et en {_unite_constante(g, base)}, en moyenne "
            f"de l'année ({min(annees)}-{max(annees)})")


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


def _intitules(g: dict, base: int) -> dict:
    courant = g["unite"]
    if figtools.lang() == "fr":
        courant = courant.replace("dinars", "dinars courants")
    return {cle: modele.format(grandeur=g["grandeur"], courant=courant,
                               constant=_unite_constante(g, base))
            for cle, modele in COLONNES[figtools.lang()].items()}


def _unite_constante(g: dict, base: int) -> str:
    """« dinars de 2025 par heure » : l'unité de l'index, le dinar daté de l'année de base."""
    courant, constant = DINAR[figtools.lang()]
    return g["unite"].replace(courant, constant.format(base=base))


def _decimales(sommet: float) -> int:
    """Un salaire horaire se lit au millime ; un salaire mensuel, au dixième de dinar."""
    return 3 if sommet < 20 else 1


def _constants(g: dict):
    """Les cases tracées en dinars constants, par année : (lignes, année de base), avec
    l'indice et l'année de base du volume (`figtools.constants_escalier`)."""
    return figtools.constants_escalier(g["serie"], _courbes(g), colonne="case",
                                       base=deflateur.ANNEE_BASE, ipc=deflateur.ipc())


def lecture_constants(g: dict, constants: list, base: int) -> str:
    """La phrase de lecture en dinars constants, calculée sur les points que la figure
    trace : pour chaque case, le niveau de la première année, celui de la dernière, et le
    plus haut avec son année."""
    case_fmt, haut, haut_borne, tete, separateur, point = LECTURE_CONSTANTS[figtools.lang()]
    sommet = max(reel for *_, reel in constants)
    d = _decimales(sommet)

    def montant(v: float) -> str:
        return f"{v:,.{d}f}".replace(",", " ").replace(".", ",")

    phrases = []
    for case in _tracees(g):
        points = [(annee, reel) for cle, annee, _m, _i, reel in constants if cle == case["cle"]]
        if not points:
            continue
        (a0, v0), (afin, vfin) = points[0], points[-1]
        amax, vmax = max(points, key=lambda p: p[1])
        phrase = case_fmt.format(case=_minuscule(_nom_case(g, case)), v0=montant(v0), a0=a0,
                                 vfin=montant(vfin), afin=afin)
        phrase += (haut_borne if amax in (a0, afin) else haut).format(vmax=montant(vmax),
                                                                     amax=amax)
        phrases.append(phrase)
    return (tete.format(unite=_unite_constante(g, base)) + separateur.join(phrases)
            + point)


def _millimes(v: float) -> str:
    return f"{v:,.3f}".replace(",", " ").replace(".", ",")


def _slug(nom: str, g: dict) -> str:
    """Le nom de fichier de la figure : celui de la branche pour sa première grille tracée —
    il ne change pas quand une grille s'ajoute —, suivi du nom de la grille pour les autres."""
    if g["cle"] == une_grille(nom)["cle"]:
        return f"fig_mt_cc_annexe_{nom}"
    return f"fig_mt_cc_annexe_{nom}_{g['cle'].rsplit('.', 1)[-1]}"


def figure(nom: str, sources: list[str], note_lecture: str | None = None,
           caveats: str = "", generated: str | None = None,
           caption: str | None = None, grille: str | None = None) -> None:
    """Une grille de la branche, en deux vues (composant commun `figtools.figure_escalier`) :
    dinars courants, en escalier ; dinars de l'année de base du volume, un point par année.

    `grille` : la clé de la grille dans l'index ; à défaut, la première grille tracée de la
    branche. Une grille sans courbe (`tracee: false`) est refusée : elle se mentionne
    (`autres_grilles`).

    La note de lecture reçue décrit la vue en dinars courants ; la règle des dinars constants
    et la phrase de lecture qui en donne les niveaux s'y ajoutent ici, calculées. L'onglet
    « Données » porte la série annuelle : moyenne en dinars courants, indice, dinars constants.

    Une marche par date d'effet ; seules la première et la dernière valeur de chaque case
    sont écrites, et une graduation sur cinq : une grille change chaque année ou presque.
    Le cercle creux marque la date à compter de laquelle le montant n'est pas publié.
    La figure trace le bas et le haut de la grille, tels que l'index les donne ; sa légende
    est écrite d'après l'index, sauf si `caption` la donne.

    UNE VALEUR VIDE ARRÊTE LE TRAIT. La série porte la date sans valeur ; le composant y pose
    un cercle creux et ne reporte rien. Il ne sait tracer qu'une valeur vide POSTÉRIEURE à la
    dernière date publiée de la grille (montant non publié) : une case tracée qui serait vide
    en tête ou au milieu de sa série (case illisible) est refusée ici, par une erreur — le
    composant relierait sinon, en dinars constants, les années de part et d'autre du trou.
    """
    entree = branche(nom)
    g = une_grille(nom, grille)
    if not g["tracee"]:
        raise ValueError(f"{nom}, {g['cle']} : grille sans courbe ({g['motif']}).")
    _FIGUREES.setdefault(nom, set()).add(g["cle"])
    serie = g["serie"]
    tracees = _tracees(g)
    d = figtools.series(serie)
    trous = d[d["valeur"].isna() & (d["date_effet"].astype(str).str[:10] <= g["fin"])]
    if len(trous):
        raise ValueError(
            f"{nom}, {g['cle']} : case tracée sans valeur à une date publiée de la grille "
            f"({sorted(set(trous['date_effet'].astype(str).str[:10]))}) : la figure en "
            f"escalier ne sait pas interrompre puis reprendre un trait.")
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
    grille_ = f", {_minuscule(g['libelle'])}" if g["libelle"] else ""
    figtools.register_provenance(
        serie,
        titre=(f"{entree['description']}{grille_} : salaires de base du bas et du haut de la "
               f"grille, à chaque date d'effet"),
        sources=sources,
        source_ligne=("grilles annexées à la convention et à ses avenants, publiées au "
                      "*Journal officiel* (liste dans l'onglet « Sources »)"),
        unite=g["unite"],
        perimetre=("une ligne par case de la grille et par date d'effet ; "
                   + " ; ".join(_minuscule(c["libelle"]) for c in tracees)),
        caveats=caveats,
    )
    constants, base = _constants(g)
    langue = figtools.lang()
    intitules = _intitules(g, base)
    note = " ".join(filter(None, [
        note_lecture, METHODE_CONSTANTS[langue].format(base=base),
        lecture_constants(g, constants, base)]))
    figtools.figure_escalier(
        serie, _courbes(g), slug=_slug(nom, g),
        caption=caption or _legende_figure(entree, g, constants, base),
        note_lecture=note, generated=generated, fin=fin, colonne="case",
        constants=True, base=base, ipc=deflateur.ipc(), series_ipc=deflateur.SERIES_IPC,
        decimales_constants=_decimales(sommet),
        ylabel_constants=intitules["axe"],
        format_valeur=lambda v: "", format_infobulle=_millimes,
        annotations=annotations,
        etiquettes_x=etiquettes, ylim=(0, 1.1 * sommet),
        ylabel=f"{g['grandeur']}, en {g['unite']}",
        supprime=SANS_VALEUR[figtools.lang()],
        libelles={"parametre": "Case de la grille", "suppression": "montant non publié",
                  **intitules})

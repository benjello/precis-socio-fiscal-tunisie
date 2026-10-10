"""Figures du chapitre de l'assistance sociale.

Quatre figures, toutes lues par `figtools.series()` :

  - l'allocation mensuelle du programme national d'aide aux familles nécessiteuses, en dinars
    courants et en dinars constants de l'année de base du déflateur (`pnafn-allocation`), et,
    comme famille à part jamais reliée à elle, les quinze points annuels d'une figure de la
    Banque mondiale (`pnafn-transfert-smig-banque-mondiale`) ;
  - la montée en charge : allocataires et ménages du transfert permanent, 2010-2026, puis
    enfants allocataires par tranche d'âge, 2022-2026, par famille de sources
    (`mas-amen-social-2023-beneficiaires-bruts`, `amen-social-effectifs-suivi`) ;
  - les allocataires du transfert mensuel, stock de décembre, entrées et sorties, 2018-2023
    (`mas-amen-social-2023-beneficiaires-bruts`) ;
  - les crédits affectés au programme Amen social par intervention, 2021-2023
    (`mas-amen-social-2023-credits-bruts`), en millions de dinars puis, pour le total et le
    transfert mensuel, en part du PIB aux prix courants des comptes de la nation
    (`cnat-pib-nominal`) : les trois années relèvent de la seule base 2015, rien n'est chaîné.

Le déflateur est celui du volume « Le marché du travail » : le module est chargé PAR SON
CHEMIN, sans être déplacé (deux paquets `figures` portent le même nom ; un import par
`sys.path` les confondrait). Quand il sera partagé sous `scripts/`, seule `_deflateur()`
change.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402
import openfisca_tables as ot  # noqa: E402

HERE = Path(__file__).resolve().parent
SERIE_PNAFN = "pnafn-allocation"
SERIE_ALLOCATAIRES = "mas-amen-social-2023-beneficiaires-bruts"
SERIE_CREDITS = "mas-amen-social-2023-credits-bruts"
SERIE_PIB = "cnat-pib-nominal"
SERIE_PNAFN_BM = "pnafn-transfert-smig-banque-mondiale"
SERIE_SUIVI = "amen-social-effectifs-suivi"
# Dernière année où le montant du dernier palier est constaté par un texte : l'arrêté conjoint
# du 10 juillet 2024 dit l'allocation « fixée à 180 dinars » à la date de sa publication.
ANNEE_CONSTAT = 2024

GRIS, ORANGE, BLEU, VERT, ROUGE, VIOLET = (
    "#8b949e", "#b45309", "#1f6feb", "#2da44e", "#cf222e", "#8250df")


def _deflateur():
    """Le déflateur du volume « Le marché du travail », chargé par son chemin."""
    chemin = HERE.parents[1] / "marche_travail" / "figures" / "deflateur.py"
    spec = importlib.util.spec_from_file_location("deflateur_marche_travail", chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


DEFLATEUR = _deflateur()
ANNEE_BASE = DEFLATEUR.ANNEE_BASE
SERIES_IPC = DEFLATEUR.SERIES_IPC

figtools.register_provenance(
    SERIE_PNAFN,
    titre="Allocation mensuelle du programme national d'aide aux familles nécessiteuses",
    titre_ar="المنحة الشهرية للبرنامج الوطني لمساعدة العائلات المعوزة",
    sources=["arrete-2024-07-10-allocation-pauvres"],
    unite=f"dinars par mois (prix courants et constants de {ANNEE_BASE})",
    unite_ar=f"دينار في الشهر (بالأسعار الجارية والثابتة لسنة {ANNEE_BASE})",
    perimetre="montant mensuel de l'allocation du programme, onze paliers de 1987 à 2018",
    perimetre_ar="المبلغ الشهري لمنحة البرنامج، أحد عشر مستوى من 1987 إلى 2018",
    caveats=("Les dates de tous les paliers et les montants antérieurs à 180 dinars restent à "
             "fiabiliser. Le montant de 180 dinars est constaté par l'arrêté conjoint du "
             "10 juillet 2024 à la date de sa publication. Le pouvoir d'achat est calculé "
             "avec l'indice annuel moyen des prix à la consommation."),
    caveats_ar=("لا تزال تواريخ جميع المستويات والمبالغ السابقة لمبلغ 180 دينارًا بحاجة إلى "
                "توثيق. وتُحسب القوة الشرائية بمؤشر أسعار الاستهلاك السنوي المتوسط."),
)


def _fr(nombre: float, decimales: int = 0) -> str:
    """Nombre à la française : espace insécable fine entre les milliers, virgule décimale."""
    texte = f"{nombre:,.{decimales}f}".replace(",", " ").replace(".", ",")
    return texte


# --- l'allocation du programme d'aide aux familles nécessiteuses -------------------------------

def _paliers() -> list[tuple[str, float]]:
    df = figtools.series(SERIE_PNAFN)
    return [(str(d)[:10], float(v)) for d, v in zip(df["date"], df["montant"])]


def _abscisse(date_iso: str) -> float:
    return int(date_iso[:4]) + (int(date_iso[5:7]) - 1) / 12


def serie_aide_permanente() -> list[tuple[str, float, float, bool]]:
    """(date, montant courant, montant en dinars de l'année de base, est un palier).

    Une ligne par palier et une par début d'année, de 1987 à l'année du constat de 2024.
    """
    paliers = _paliers()
    ipc = DEFLATEUR.ipc()
    dates_paliers = {d for d, _ in paliers}
    debut = int(paliers[0][0][:4])
    dates = sorted(dates_paliers | {f"{a}-01-01" for a in range(debut, ANNEE_CONSTAT + 1)})
    lignes = []
    for date in dates:
        montant = next(m for d, m in reversed(paliers) if d <= date)
        annee = int(date[:4])
        lignes.append((date, montant, montant * ipc[ANNEE_BASE] / ipc[annee],
                       date in dates_paliers))
    return lignes


def points_banque_mondiale() -> list[tuple[int, float, float]]:
    """(année, transfert mensuel en dinars courants, en dinars de l'année de base) : les
    étiquettes des barres d'une figure de la Banque mondiale, une valeur par année, quinze
    années irrégulières. Famille à part : jamais reliée aux paliers, rien n'est interpolé."""
    df = figtools.series(SERIE_PNAFN_BM)
    df = df[df["grandeur"] == "transfert_mensuel_pnafn"]
    ipc = DEFLATEUR.ipc()
    return sorted((int(a), float(v), float(v) * ipc[ANNEE_BASE] / ipc[int(a)])
                  for a, v in zip(df["date_reference"], df["valeur"]))


SERIE_CHAPITRE = "Série du chapitre (paliers)"
SERIE_BANQUE = "Banque mondiale, figure de 2022 (valeur de l'année)"


def table_aide_permanente():
    import pandas as pd
    lignes = [
        {"Série": SERIE_CHAPITRE,
         "Date de l'état": ot.formate_date(d, figtools.lang()),
         "Allocation mensuelle (D courants)": ot.formate_dinars(m),
         f"Pouvoir d'achat (D de {ANNEE_BASE})": ot.formate_dinars(round(r, 1)),
         "Point de mesure": "Changement de palier" if p else "Repère annuel"}
        for d, m, r, p in serie_aide_permanente()]
    lignes += [
        {"Série": SERIE_BANQUE,
         "Date de l'état": str(a),
         "Allocation mensuelle (D courants)": ot.formate_dinars(m),
         f"Pouvoir d'achat (D de {ANNEE_BASE})": ot.formate_dinars(round(r, 1)),
         "Point de mesure": "Étiquette de la figure, année entière"}
        for a, m, r in points_banque_mondiale()]
    return pd.DataFrame(lignes)


def fig_aide_permanente():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    serie = serie_aide_permanente()
    x = [_abscisse(d) for d, *_ in serie] + [ANNEE_CONSTAT + 0.55]
    courant = [m for _, m, _, _ in serie] + [serie[-1][1]]
    reel = [r for _, _, r, _ in serie] + [serie[-1][2]]
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    ax.step(x, courant, where="post", color=GRIS, lw=2, ls=":",
            label=ft("Série du chapitre : montant courant (paliers à fiabiliser)"))
    ax.step(x, reel, where="post", color=ORANGE, lw=2, ls="--",
            label=ft(f"Série du chapitre : pouvoir d'achat (dinars de {ANNEE_BASE})"))
    paliers = [(xi, m, r) for xi, (_, m, r, p) in zip(x, serie) if p]
    ax.scatter([p[0] for p in paliers], [p[1] for p in paliers], color=GRIS, s=42, zorder=4)
    ax.scatter([p[0] for p in paliers], [p[2] for p in paliers], color=ORANGE, marker="D",
               s=35, zorder=5)
    # La famille de la Banque mondiale : des points seuls, au milieu de leur année, sans trait.
    banque = points_banque_mondiale()
    xb = [a + 0.5 for a, _, _ in banque]
    ax.scatter(xb, [m for _, m, _ in banque], marker="s", s=46, facecolors="none",
               edgecolors=BLEU, linewidths=1.5, zorder=6,
               label=ft("Banque mondiale, figure de 2022 : montant courant (points non reliés)"))
    ax.scatter(xb, [r for _, _, r in banque], marker="^", s=52, facecolors="none",
               edgecolors=VIOLET, linewidths=1.5, zorder=6,
               label=ft(f"Banque mondiale, figure de 2022 : pouvoir d'achat (dinars de {ANNEE_BASE})"))
    ax.annotate(ft("180 D constatés\nle 10 juillet 2024"),
                xy=(ANNEE_CONSTAT + 0.5, 180), xytext=(-8, -34), textcoords="offset points",
                ha="right", va="top", fontsize=8, color="#57606a",
                arrowprops={"arrowstyle": "-", "color": "#57606a", "lw": 0.8})
    ax.set_xlim(1986, ANNEE_CONSTAT + 1.5)
    ax.set_ylim(0, None)
    ax.set_ylabel(ft(f"Dinars par mois (courants et constants de {ANNEE_BASE})"))
    ax.set_xlabel(ft("Année"))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8)
    fig.tight_layout()
    return fig


# --- les allocataires du transfert mensuel, 2018-2023 -----------------------------------------

def _valeurs(serie: str, indicateur: str, dimension: str) -> dict[int, float]:
    df = figtools.series(serie)
    lignes = df[(df["indicateur"] == indicateur) & (df["dimension"] == dimension)]
    return {int(a): float(v) for a, v in zip(lignes["annee"], lignes["valeur"])}


def donnees_allocataires() -> dict[str, dict[int, float]]:
    return {
        "stock": _valeurs(SERIE_ALLOCATAIRES, "bénéficiaires du transfert mensuel",
                          "stock décembre"),
        "entrees": _valeurs(SERIE_ALLOCATAIRES, "entrées", "transfert mensuel"),
        "sorties": _valeurs(SERIE_ALLOCATAIRES, "sorties", "transfert mensuel"),
        "solde": _valeurs(SERIE_ALLOCATAIRES, "solde net", "transfert mensuel"),
    }


def table_allocataires():
    import pandas as pd
    d = donnees_allocataires()

    def cellule(cle, annee):
        return _fr(d[cle][annee]) if annee in d[cle] else "—"

    return pd.DataFrame([
        {"Année": str(a),
         "Allocataires en décembre (individus ou familles)": cellule("stock", a),
         "Entrées de l'année": cellule("entrees", a),
         "Sorties de l'année": cellule("sorties", a),
         "Solde": cellule("solde", a)}
        for a in sorted(d["stock"])])


def _fig_stock():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    stock = donnees_allocataires()["stock"]
    annees = sorted(stock)
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    ax.plot(annees, [stock[a] / 1000 for a in annees], color=BLEU, lw=2, marker="o")
    for a in annees:
        ax.annotate(_fr(stock[a]), xy=(a, stock[a] / 1000), xytext=(0, 8),
                    textcoords="offset points", ha="center", fontsize=8.5, color=BLEU)
    ax.set_ylim(0, max(stock.values()) / 1000 * 1.15)
    ax.set_xticks(annees)
    ax.set_ylabel(ft("Allocataires en décembre (milliers)"))
    ax.set_xlabel(ft("Année"))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def _fig_flux():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = donnees_allocataires()
    annees = sorted(d["entrees"])
    largeur = 0.38
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    ax.bar([a - largeur / 2 for a in annees], [d["entrees"][a] / 1000 for a in annees],
           largeur, color=VERT, label=ft("Entrées"))
    ax.bar([a + largeur / 2 for a in annees], [d["sorties"][a] / 1000 for a in annees],
           largeur, color=ROUGE, label=ft("Sorties"))
    for a in annees:
        ax.annotate(_fr(d["entrees"][a]), xy=(a - largeur / 2, d["entrees"][a] / 1000),
                    xytext=(0, 3), textcoords="offset points", ha="center", fontsize=8)
        ax.annotate(_fr(d["sorties"][a]), xy=(a + largeur / 2, d["sorties"][a] / 1000),
                    xytext=(0, 3), textcoords="offset points", ha="center", fontsize=8)
    ax.set_xticks(annees)
    ax.set_ylabel(ft("Allocataires (milliers)"))
    ax.set_xlabel(ft("Année"))
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper left", fontsize=8.5)
    fig.tight_layout()
    return fig


def vues_allocataires():
    return [("Allocataires en décembre", _fig_stock()),
            ("Entrées et sorties de l'année", _fig_flux())]


# --- la montée en charge, 2010-2026 -----------------------------------------------------------

MINISTERE = "ministère des Affaires sociales"
BANQUE = "décomptes du ministère rapportés par la Banque mondiale"
UNICEF = "données du programme rapportées par l'UNICEF"
PIECES = {
    "banquemondiale2021pad4414": "Banque mondiale, document d'évaluation du projet, 2021",
    "banquemondiale2022pad4815": "Banque mondiale, premier financement additionnel, 2022",
    "banquemondiale2026ppiaf000292": "Banque mondiale, second financement additionnel, 2026",
    "banquemondiale2025isr04716": "Banque mondiale, rapport d'exécution de novembre 2025",
    "banquemondiale2026isr08116": "Banque mondiale, rapport d'exécution de juillet 2026",
    "unicef2024allocations618": "UNICEF, rapport sur l'allocation des 6 à 18 ans, 2024",
    "mas-amen-social-2023": "Ministère des Affaires sociales, rapport pour 2023",
}
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre",
        "octobre", "novembre", "décembre"]
# Dates de droit : (abscisse, numéro, libellé). Elles situent les décomptes dans le temps du
# droit ; elles n'établissent aucun lien de cause.
DROIT = [
    (2020 + (4 + 24 / 31) / 12, "1", "25 mai 2020 : prestations de l'Amen social ouvertes"),
    (2022 + (3 + 7 / 30) / 12, "2", "8 avril 2022 : allocation des moins de six ans "
     "(arrêté publié) ; programme pilote des 6 à 18 ans la même année"),
    (2025.0, "3", "1er janvier 2025 : allocation des 6 à 18 ans instituée"),
    (2025 + (10 + 8 / 30) / 12, "4", "9 novembre 2025 : montant de l'allocation des 6 à 18 ans "
     "exécutoire"),
]
# Rupture de série : l'indicateur des 6 à 18 ans des rapports d'exécution est créé le
# 27 mars 2026, à zéro ; avant, le programme pilote financé par un don.
RUPTURE_6_18 = 2026 + (2 + 26 / 31) / 12


def _place(date_ref: str, precision: str) -> float:
    """Abscisse d'un décompte : à son jour quand il est daté au jour, au milieu de son mois
    quand il l'est au mois, au milieu de son année quand il ne l'est qu'à l'année."""
    annee = int(date_ref[:4])
    if precision == "annee":
        return annee + 0.5
    mois = int(date_ref[5:7])
    if precision == "mois":
        return annee + (mois - 0.5) / 12
    return annee + (mois - 1 + (int(date_ref[8:10]) - 0.5) / 31) / 12


def _date_lisible(date_ref: str, precision: str) -> str:
    if precision == "annee":
        return date_ref[:4]
    mois = MOIS[int(date_ref[5:7]) - 1]
    if precision == "mois":
        return f"{mois} {date_ref[:4]}"
    jour = int(date_ref[8:10])
    return f"{'1er' if jour == 1 else jour} {mois} {date_ref[:4]}"


def _decomptes_rapportes(grandeur: str) -> list[dict]:
    """Décomptes d'une grandeur dans la série des rapports, une ligne par attestation ; deux
    attestations de même date et de même valeur n'en font qu'une, leurs pièces réunies."""
    df = figtools.series(SERIE_SUIVI)
    df = df[df["grandeur"] == grandeur]
    points: dict[tuple, dict] = {}
    for r in df.itertuples():
        qualificatif = "" if str(r.qualificatif) == "nan" else str(r.qualificatif)
        dimension = "" if str(r.dimension) == "nan" else str(r.dimension)
        date_ref, precision = str(r.date_reference), str(r.precision_date)
        cle = (date_ref, float(r.valeur), qualificatif)
        famille = UNICEF if str(r.source).startswith("unicef") else BANQUE
        if float(r.valeur) == 0:
            remarque = "valeur de départ d'un indicateur créé à cette date : non tracée"
        elif qualificatif:
            remarque = f"borne (« {qualificatif} »), non une valeur : non tracée"
        elif "départ" in dimension:
            remarque = "valeur de départ du projet"
        else:
            remarque = ""
        point = points.setdefault(cle, {
            "date": date_ref, "precision": precision, "x": _place(date_ref, precision),
            "valeur": float(r.valeur), "famille": famille, "pieces": [],
            "trace": float(r.valeur) > 0 and not qualificatif, "remarque": remarque})
        piece = PIECES.get(str(r.source), str(r.source))
        if piece not in point["pieces"]:
            point["pieces"].append(piece)
    return sorted(points.values(), key=lambda p: (p["x"], p["valeur"]))


def _decomptes_ministere(indicateur: str) -> list[dict]:
    """Stocks de décembre du rapport du ministère pour 2023, placés au milieu de décembre."""
    valeurs = _valeurs(SERIE_ALLOCATAIRES, indicateur, "stock décembre")
    return [{"date": f"{a}-12", "precision": "mois", "x": _place(f"{a}-12", "mois"),
             "valeur": v, "famille": MINISTERE, "pieces": [PIECES["mas-amen-social-2023"]],
             "trace": True, "remarque": ""} for a, v in sorted(valeurs.items())]


# (libellé de la grandeur, unité, décomptes) — dans l'ordre du tableau des données.
def donnees_montee_en_charge() -> list[tuple[str, str, list[dict]]]:
    return [
        ("Transfert monétaire permanent", "allocataires (individus ou familles)",
         _decomptes_ministere("bénéficiaires du transfert mensuel")),
        ("Transfert monétaire permanent", "ménages",
         _decomptes_rapportes("menages_transfert_permanent")),
        ("Allocation des enfants de moins de six ans", "enfants",
         _decomptes_ministere("allocation moins de 6 ans, bénéficiaires")
         + _decomptes_rapportes("enfants_0_5_allocataires")),
        ("Allocation des enfants de 6 à 18 ans", "enfants",
         _decomptes_ministere("allocation 6-18 ans, bénéficiaires")
         + _decomptes_rapportes("enfants_6_18_allocataires")),
    ]


def table_montee_en_charge():
    import pandas as pd
    lignes = []
    for grandeur, unite, points in donnees_montee_en_charge():
        for p in sorted(points, key=lambda q: (q["x"], q["valeur"])):
            lignes.append({
                "Grandeur": grandeur,
                "Date du décompte": _date_lisible(p["date"], p["precision"]),
                "Valeur": _fr(p["valeur"]),
                "Unité": unite,
                "Famille de sources": p["famille"],
                "Pièce": " ; ".join(p["pieces"]),
                "Remarque": p["remarque"]})
    return pd.DataFrame(lignes)


def _traits_de_droit(ax, numeros: tuple[str, ...], xmin: float, xmax: float):
    """Traits verticaux fins et numérotés pour les dates de droit ; renvoie les libellés."""
    ft = figtools.fig_text
    libelles = []
    for x, numero, libelle in DROIT:
        if numero not in numeros or not xmin <= x <= xmax:
            continue
        ax.axvline(x, color="#24292f", lw=0.9, ls=(0, (1, 2)), zorder=1)
        ax.annotate(numero, xy=(x, 1.0), xycoords=("data", "axes fraction"), xytext=(0, 4),
                    textcoords="offset points", ha="center", va="bottom", fontsize=8.5,
                    color="#24292f",
                    bbox={"boxstyle": "circle,pad=0.25", "fc": "white", "ec": "#24292f",
                          "lw": 0.8})
        libelles.append(f"{numero}  {libelle}")
    return [ft(t) for t in libelles]


def _pied(fig, lignes: list[str]):
    """Légende des traits, sous le graphique."""
    fig.text(0.07, 0.012, "\n".join(lignes), ha="left", va="bottom", fontsize=8,
             color="#24292f", linespacing=1.5)


def _fig_montee_transfert():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = donnees_montee_en_charge()
    ministere = d[0][2]
    banque = [p for p in d[1][2] if p["trace"]]
    fig, ax = plt.subplots(figsize=(9.5, 5.9))
    ax.plot([p["x"] for p in ministere], [p["valeur"] / 1000 for p in ministere], color=BLEU,
            lw=2, marker="o", ms=6, zorder=4,
            label=ft("Ministère des Affaires sociales : allocataires (individus ou familles), "
                     "décembre"))
    ax.scatter([p["x"] for p in banque], [p["valeur"] / 1000 for p in banque], marker="s",
               s=48, facecolors="none", edgecolors=ORANGE, linewidths=1.6, zorder=5,
               label=ft("Décomptes du ministère rapportés par la Banque mondiale : ménages "
                        "(points non reliés)"))

    def etiquette(texte, x, y, dx, dy, ha="center", couleur=ORANGE):
        ax.annotate(ft(texte), xy=(x, y), xytext=(dx, dy), textcoords="offset points", ha=ha,
                    fontsize=8, color=couleur)

    def groupe(debut, fin):
        return [p for p in banque if debut <= p["x"] < fin]

    # (début, fin, libellé de la période, décalage, alignement, lignes séparées)
    for debut, fin, quand, dx, dy, ha, empile in [
            (2010, 2011, "2010", 0, 10, "center", False),
            (2020, 2022, "2020-2021", -12, -30, "center", False),
            (2024, 2025, "30 nov. 2024", -9, -12, "right", False),
            (2025, 2026, "2025", -2, 12, "center", False),
            (2026, 2027, "avril-mai 2026", 10, -16, "left", True)]:
        pts = groupe(debut, fin)
        if not pts:
            continue
        valeurs = sorted({p["valeur"] for p in pts})
        if len(valeurs) == 1:
            texte = _fr(valeurs[0])
        elif len(valeurs) == 2:
            texte = f"{_fr(valeurs[0])} ou{chr(10) if empile else ' '}{_fr(valeurs[1])}"
        else:
            texte = f"{_fr(valeurs[0])} à {_fr(valeurs[-1])}"
        xs = [p["x"] for p in pts]
        x = max(xs) if ha == "left" else min(xs) if ha == "right" else sum(xs) / len(xs)
        etiquette(f"{texte}\n({quand})", x,
                  max(valeurs) / 1000 if dy >= 0 else min(valeurs) / 1000, dx, dy, ha)
    etiquette(f"{_fr(ministere[0]['valeur'])}\n(déc. {ministere[0]['date'][:4]})",
              ministere[0]["x"], ministere[0]["valeur"] / 1000, -7, 6, "right", BLEU)
    etiquette(f"{_fr(ministere[-1]['valeur'])}\n(déc. {ministere[-1]['date'][:4]})",
              ministere[-1]["x"], ministere[-1]["valeur"] / 1000, 8, -24, "left", BLEU)
    ax.set_xlim(2009.5, 2028.7)
    ax.set_ylim(0, 460)
    ax.set_xticks(range(2010, 2027, 2))
    ax.set_ylabel(ft("Allocataires ou ménages du transfert permanent (milliers)"))
    ax.set_xlabel(ft("Année"))
    ax.grid(True, alpha=0.3)
    pied = _traits_de_droit(ax, ("1", "2", "3", "4"), 2009.5, 2028.7)
    ax.legend(loc="lower right", fontsize=8)
    fig.tight_layout(rect=(0, 0.031 * len(pied) + 0.02, 1, 1))
    _pied(fig, pied)
    return fig


def _fig_montee_enfants():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = donnees_montee_en_charge()
    fig, ax = plt.subplots(figsize=(9.5, 6.2))
    marques = {MINISTERE: ("o", True), BANQUE: ("s", False), UNICEF: ("^", False)}
    noms = {MINISTERE: "ministère, décembre",
            BANQUE: "Banque mondiale (décomptes rapportés)",
            UNICEF: "UNICEF (données du programme)"}
    for (grandeur, _, points), couleur, tranche in [(d[2], VIOLET, "Moins de six ans"),
                                                   (d[3], VERT, "6 à 18 ans")]:
        for famille in (MINISTERE, UNICEF, BANQUE):
            pts = [p for p in points if p["famille"] == famille and p["trace"]]
            if not pts:
                continue
            marque, plein = marques[famille]
            xs, ys = [p["x"] for p in pts], [p["valeur"] / 1000 for p in pts]
            libelle = ft(f"{tranche} : {noms[famille]}")
            if famille == MINISTERE and len(pts) > 1:
                ax.plot(xs, ys, color=couleur, lw=2, marker=marque, ms=6.5, zorder=4,
                        label=libelle)
            else:
                ax.scatter(xs, ys, marker=marque, s=58 if plein else 62,
                           facecolors=couleur if plein else "none", edgecolors=couleur,
                           linewidths=1.6, zorder=5, label=libelle)
            for p in pts:
                # Décembre 2023, 6 à 18 ans : deux décomptes à 141 enfants d'écart, l'un au-dessus
                # du point, l'autre au-dessous.
                dessous = famille == MINISTERE and grandeur.endswith("18 ans")
                ax.annotate(_fr(p["valeur"]), xy=(p["x"], p["valeur"] / 1000),
                            xytext=(0, -15 if dessous else 8), textcoords="offset points",
                            ha="center", fontsize=8, color=couleur)
    ax.axvline(RUPTURE_6_18, color=ROUGE, lw=1.4, ls="-.", zorder=2,
               label=ft("Rupture de série, 6 à 18 ans : indicateur créé le 27 mars 2026"))
    ax.set_xlim(2022.0, 2026.75)
    ax.set_ylim(0, 540)
    ax.set_xticks(range(2022, 2027))
    ax.set_ylabel(ft("Enfants allocataires (milliers)"))
    ax.set_xlabel(ft("Année (graduation au 1er janvier)"))
    ax.grid(True, alpha=0.3)
    pied = _traits_de_droit(ax, ("2", "3", "4"), 2022.0, 2026.75)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.11), ncol=2, fontsize=8,
              frameon=False)
    fig.tight_layout(rect=(0, 0.031 * len(pied) + 0.02, 1, 1))
    _pied(fig, pied)
    return fig


def vues_montee_en_charge():
    return [("Transfert permanent, 2010-2026", _fig_montee_transfert()),
            ("Enfants allocataires, 2022-2026", _fig_montee_enfants())]


# --- les crédits affectés, 2021-2023 ----------------------------------------------------------

# (indicateur de la série, libellé, couleur) — dans l'ordre d'empilement.
INTERVENTIONS = [
    ("transfert mensuel direct", "Transfert mensuel", BLEU),
    ("allocation enfants de moins de 6 ans", "Allocation des enfants de moins de six ans",
     VIOLET),
    ("transferts fêtes et occasions", "Aides des fêtes", ORANGE),
    ("aides rentrée scolaire et universitaire", "Aides de rentrée scolaire et universitaire",
     VERT),
    ("transport gratuit enfants des familles pauvres", "Transport des enfants", "#bf8700"),
    ("microprojets familles pauvres et modestes",
     "Projets des familles pauvres et à revenu limité", ROUGE),
    ("microprojets personnes handicapées", "Projets des personnes handicapées", GRIS),
]
TOTAL = "total crédits Amen social"
TRANSFERT = "transfert mensuel direct"


def donnees_credits() -> dict[str, dict[int, float]]:
    """Crédits affectés par intervention, en millions de dinars ; une année absente de la
    source reste absente (aucun zéro n'est créé)."""
    d = {ind: {a: v / 1000 for a, v in
               _valeurs(SERIE_CREDITS, ind, "crédits affectés").items()}
         for ind, _, _ in INTERVENTIONS}
    d[TOTAL] = {a: v / 1000 for a, v in
                _valeurs(SERIE_CREDITS, TOTAL, "crédits affectés").items()}
    return d


def table_credits():
    import pandas as pd
    d = donnees_credits()
    annees = sorted(d[TOTAL])
    lignes = [{"Crédits affectés (MD courants, sauf mention)": lib,
               **{str(a): (_fr(d[ind][a], 1) if a in d[ind] else "—")
                  for a in annees}}
              for ind, lib, _ in INTERVENTIONS]
    lignes.append({"Crédits affectés (MD courants, sauf mention)": "Total",
                   **{str(a): _fr(d[TOTAL][a], 1) for a in annees}})
    pib, base = pib_credits()
    parts = parts_pib_credits()
    lignes.append({"Crédits affectés (MD courants, sauf mention)":
                   f"PIB aux prix courants, comptes de la nation, base {base} (MD)",
                   **{str(a): _fr(pib[a], 1) for a in annees}})
    for cle, lib in ((TOTAL, "Total"), (TRANSFERT, "Transfert mensuel")):
        lignes.append({"Crédits affectés (MD courants, sauf mention)":
                       f"{lib}, en % du PIB (base {base})",
                       **{str(a): _fr(parts[cle][a], 2) for a in annees}})
    return pd.DataFrame(lignes)


def pib_credits() -> tuple[dict[int, float], int]:
    """({année: PIB aux prix courants, en MD}, base) pour les années des crédits : l'édition
    la plus récente des comptes de la nation qui porte l'année. Les années doivent relever
    d'UNE SEULE base : aucune base n'est chaînée, et un changement de base arrête le calcul."""
    df = figtools.series(SERIE_PIB).copy()
    df["fin"] = df["edition"].str[-4:].astype(int)
    df = df.sort_values("fin").groupby("annee").last()
    annees = sorted(donnees_credits()[TOTAL])
    bases = {int(str(df.loc[a, "base"]).split()[-1]) for a in annees}
    if len(bases) != 1:
        raise ValueError(f"PIB des années {annees} : plusieurs bases {sorted(bases)}")
    return {a: float(df.loc[a, "valeur"]) for a in annees}, bases.pop()


def parts_pib_credits() -> dict[str, dict[int, float]]:
    """Crédits affectés en % du PIB : total du programme et transfert mensuel."""
    d = donnees_credits()
    pib, _ = pib_credits()
    return {cle: {a: 100 * d[cle][a] / pib[a] for a in pib} for cle in (TOTAL, TRANSFERT)}


def fig_credits_pib():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    parts = parts_pib_credits()
    _, base = pib_credits()
    annees = sorted(parts[TOTAL])
    fig, ax = plt.subplots(figsize=(9.5, 5))
    largeur = 0.32
    for cle, lib, couleur, decalage in (
            (TOTAL, "Total des crédits affectés au programme", GRIS, -largeur / 2),
            (TRANSFERT, "dont transfert mensuel", BLEU, largeur / 2)):
        ax.bar([a + decalage for a in annees], [parts[cle][a] for a in annees], largeur,
               color=couleur, label=ft(lib))
        for a in annees:
            ax.annotate(_fr(parts[cle][a], 2) + " %", xy=(a + decalage, parts[cle][a]),
                        xytext=(0, 4), textcoords="offset points", ha="center", fontsize=9)
    ax.set_xticks(annees)
    ax.set_ylim(0, max(parts[TOTAL].values()) * 1.15)
    ax.set_ylabel(ft(f"Crédits affectés, en % du PIB aux prix courants (base {base})"))
    ax.set_xlabel(ft("Année"))
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=8,
              frameon=False)
    fig.tight_layout()
    return fig


def vues_credits():
    return [("En millions de dinars", fig_credits()), ("En % du PIB", fig_credits_pib())]


def fig_credits():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = donnees_credits()
    annees = sorted(d[TOTAL])
    fig, ax = plt.subplots(figsize=(9.5, 5))
    bas = {a: 0.0 for a in annees}
    for ind, lib, couleur in INTERVENTIONS:
        hauteurs = [d[ind].get(a, 0.0) for a in annees]
        ax.bar(annees, hauteurs, 0.55, bottom=[bas[a] for a in annees], color=couleur,
               label=ft(lib))
        for a, h in zip(annees, hauteurs):
            if h >= 25:
                ax.annotate(_fr(h, 1), xy=(a, bas[a] + h / 2), ha="center", va="center",
                            fontsize=8, color="white")
            bas[a] += h
    for a in annees:
        ax.annotate(ft(f"Total : {_fr(d[TOTAL][a], 1)} MD"), xy=(a, d[TOTAL][a]),
                    xytext=(0, 5), textcoords="offset points", ha="center", fontsize=9)
    ax.set_xticks(annees)
    ax.set_ylim(0, max(d[TOTAL].values()) * 1.12)
    ax.set_ylabel(ft("Crédits affectés (millions de dinars courants)"))
    ax.set_xlabel(ft("Année"))
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=8,
              frameon=False)
    fig.tight_layout()
    return fig


# --- les plafonds de ressources en dinars -----------------------------------------------------

SERIE_SMIG = "marche-travail-smig-smag"
# (composition du ménage, multiple du salaire minimum, libellé du multiple) — article 5 du
# décret gouvernemental n° 2020-317 ; les multiples sont ceux du tableau engendré des plafonds.
PLAFONDS = [("Individu", 2 / 3, "2/3"), ("2 personnes", 1.0, "1"),
            ("3 ou 4 personnes", 1.5, "1,5"), ("5 personnes et plus", 2.0, "2")]


def _smig_mensuel(date_iso: str) -> tuple[float, float]:
    """Salaire minimum mensuel en vigueur à la date : (régime de 48 heures, de 40 heures)."""
    df = figtools.series(SERIE_SMIG)
    lignes = df[df["date"].astype(str).str[:10] <= date_iso]
    derniere = lignes.iloc[-1]
    return float(derniere["smig_48h_mensuel"]), float(derniere["smig_40h_mensuel"])


def markdown_plafonds_dinars(dates: tuple[str, ...] = ("2020-05-25", "2026-01-01")) -> str:
    """Tableau Markdown : plafonds de ressources en dinars par mois, aux deux régimes du
    salaire minimum, à chaque date."""
    entete = ["Composition du ménage", "Plafond<br>(salaires minimums)"]
    for d in dates:
        jour = ot.formate_date(d, figtools.lang())
        entete += [f"{jour}, régime de 48 heures<br>(D par mois)",
                   f"{jour}, régime de 40 heures<br>(D par mois)"]
    lignes = ["| " + " | ".join(entete) + " |",
              "|---|---:|" + "---:|" * (2 * len(dates))]
    for composition, multiple, libelle in PLAFONDS:
        cellules = [composition, libelle]
        for d in dates:
            cellules += [_fr(multiple * s, 1) for s in _smig_mensuel(d)]
        lignes.append("| " + " | ".join(cellules) + " |")
    return "\n".join(lignes)

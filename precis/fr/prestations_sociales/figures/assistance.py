"""Figures du chapitre de l'assistance sociale.

Trois figures, toutes lues par `figtools.series()` :

  - l'allocation mensuelle du programme national d'aide aux familles nécessiteuses, en dinars
    courants et en dinars constants de l'année de base du déflateur (`pnafn-allocation`) ;
  - les allocataires du transfert mensuel, stock de décembre, entrées et sorties, 2018-2023
    (`mas-amen-social-2023-beneficiaires-bruts`) ;
  - les crédits affectés au programme Amen social par intervention, 2021-2023
    (`mas-amen-social-2023-credits-bruts`).

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


def table_aide_permanente():
    import pandas as pd
    return pd.DataFrame([
        {"Date de l'état": ot.formate_date(d, figtools.lang()),
         "Allocation mensuelle (D courants)": ot.formate_dinars(m),
         f"Pouvoir d'achat (D de {ANNEE_BASE})": ot.formate_dinars(round(r, 1)),
         "Point de mesure": "Changement de palier" if p else "Repère annuel"}
        for d, m, r, p in serie_aide_permanente()])


def fig_aide_permanente():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    serie = serie_aide_permanente()
    x = [_abscisse(d) for d, *_ in serie] + [ANNEE_CONSTAT + 0.55]
    courant = [m for _, m, _, _ in serie] + [serie[-1][1]]
    reel = [r for _, _, r, _ in serie] + [serie[-1][2]]
    fig, ax = plt.subplots(figsize=(9.5, 5))
    ax.step(x, courant, where="post", color=GRIS, lw=2, ls=":",
            label=ft("Montant courant (paliers à fiabiliser)"))
    ax.step(x, reel, where="post", color=ORANGE, lw=2, ls="--",
            label=ft(f"Pouvoir d'achat (dinars constants de {ANNEE_BASE})"))
    paliers = [(xi, m, r) for xi, (_, m, r, p) in zip(x, serie) if p]
    ax.scatter([p[0] for p in paliers], [p[1] for p in paliers], color=GRIS, s=42, zorder=4)
    ax.scatter([p[0] for p in paliers], [p[2] for p in paliers], color=ORANGE, marker="D",
               s=35, zorder=5)
    ax.annotate(ft("180 D constatés\nle 10 juillet 2024"),
                xy=(ANNEE_CONSTAT + 0.5, 180), xytext=(-8, -34), textcoords="offset points",
                ha="right", va="top", fontsize=8, color="#57606a",
                arrowprops={"arrowstyle": "-", "color": "#57606a", "lw": 0.8})
    ax.set_xlim(1986, ANNEE_CONSTAT + 1.5)
    ax.set_ylim(0, None)
    ax.set_ylabel(ft(f"Dinars par mois (courants et constants de {ANNEE_BASE})"))
    ax.set_xlabel(ft("Année"))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8.5)
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
    lignes = [{"Intervention (crédits affectés, MD courants)": lib,
               **{str(a): (_fr(d[ind][a], 1) if a in d[ind] else "—")
                  for a in annees}}
              for ind, lib, _ in INTERVENTIONS]
    lignes.append({"Intervention (crédits affectés, MD courants)": "Total",
                   **{str(a): _fr(d[TOTAL][a], 1) for a in annees}})
    return pd.DataFrame(lignes)


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

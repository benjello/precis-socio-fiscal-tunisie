"""Figures du chapitre « La compensation du transport public » (volume « La compensation »).

    from figures import transport as tr
    tr.figure("soutien_par_societe", caption=…, note_lecture=…)

D'OÙ VIENNENT LES DONNÉES. Sept séries de `tunisia-data`, lues par `figtools.series()` — donc
depuis le snapshot `precis/_seriescache/` quand l'entrepôt est absent — et le poste
« transport » de `compensation-parts`, déjà employé par le chapitre de la dépense :

  - `transport-soutien-par-societe` : crédits du soutien du transport public par société,
    budgets du ministère du Transport, éditions 2013 à 2017 ;
  - `transport-transferts-par-entreprise` : transferts du budget par entreprise et par nature,
    rapport sur les transferts et les garanties, 2016-2024 (seule la nature « interventions ») ;
  - `transport-abonnements-scolaires` : nombre d'abonnements scolaires, mêmes budgets ;
  - `jort-transport-tarifs-reperes` : tarifs fixés par arrêté, 1987-2000 ;
  - `ins-bms-prix-transport` : relevé de prix de l'INS à Tunis, novembre 2007 – juillet 2026 ;
  - `bm-livre-blanc-2016-transport-trafic-comptes` : trafic de la société des transports de
    Tunis par catégorie de voyageurs, 2007-2014 (rapport extérieur).

RÈGLES.

  - **Aucune série n'est raccordée à une autre.** Crédits par société (2012-2017) et
    interventions (2016-2024) ont chacun leur figure ; tarifs du Journal officiel (1987-2000) et
    relevé de l'INS (2007-2026) sont deux segments d'une même figure, de couleurs différentes,
    séparés par une plage grisée où rien n'est établi.
  - **Une lecture par année pour les crédits** : celle de l'édition la plus récente du budget
    qui porte l'année (loi de finances ou loi de finances complémentaire de l'année écoulée ;
    prévision pour 2017). Toutes les lectures restent dans l'onglet « Données ».
  - **Des marches pour les tarifs** : un tarif vaut de sa date d'effet à la veille du suivant.
    Une date d'effet non établie (arrêtés du 26 août 1993 et du 17 février 2000) est posée à la
    date du fascicule, sur une marque creuse.
  - **Dinars constants** : `dinars_constants` (année de base commune du précis). Le montant
    d'une année est la moyenne des montants en vigueur au premier jour de chacun de ses douze
    mois ; une année dont un mois n'est pas établi n'est pas tracée.
  - **L'abonnement de l'INS change d'unité** (dinars jusqu'en avril 2017, millimes ensuite) :
    il est converti en dinars, et seuls les mois où tous les numéros s'accordent sont tracés.
  - **Les abonnements scolaires ont deux segments** (éditions 2013-2016, puis édition 2017),
    séparés par un trait de rupture ; l'année 2016 figure dans les deux.

Les libellés sont en français ; les libellés arabes restent à verser (`_L`, clé `ar`).
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import dinars_constants  # noqa: E402
import figtools  # noqa: E402

SOUTIEN = "transport-soutien-par-societe"
TRANSFERTS = "transport-transferts-par-entreprise"
ABONNEMENTS = "transport-abonnements-scolaires"
TARIFS = "jort-transport-tarifs-reperes"
INS = "ins-bms-prix-transport"
LIVRE_BLANC = "bm-livre-blanc-2016-transport-trafic-comptes"
PARTS = "compensation-parts"

BASE = dinars_constants.ANNEE_BASE
BLEU, BLEU_CLAIR, ORANGE, VERT, VIOLET, ROUGE, GRIS, NOIR = (
    "#0969da", "#80b3f0", "#d1600f", "#1a7f37", "#8250df", "#cf222e", "#8c959f", "#24292f")

_L = {
    "x": {"fr": "Année"},
    "md": {"fr": "Millions de dinars courants"},
    "pct": {"fr": "En % du total de l'année"},
    "vue_md": {"fr": "En millions de dinars"},
    "vue_part": {"fr": "En part du total"},
    "vue_courants": {"fr": "Prix courants"},
    "vue_constants": {"fr": f"Dinars de {BASE}"},
    "vue_millions": {"fr": "En millions de voyageurs"},
    "regionales": {"fr": "Sociétés régionales de transport"},
    "tunis_bus": {"fr": "Société des transports de Tunis, autobus"},
    "tunis_metro": {"fr": "Société des transports de Tunis, métro"},
    "tunis": {"fr": "Société des transports de Tunis"},
    "sncft": {"fr": "SNCFT (chemins de fer)"},
    "rfr": {"fr": "Société du réseau ferroviaire rapide de Tunis"},
    "autres": {"fr": "Autres bénéficiaires"},
    "poste": {"fr": "Poste « transport » de la dépense de compensation"},
    "lf": {"fr": "barre hachurée : loi de finances ou prévision, non réalisation"},
    "apurement": {"fr": "2017 : prise en charge\nde dettes par l'État"},
    "millimes": {"fr": "Millimes, prix courants"},
    "millimes_c": {"fr": f"Millimes de {BASE}"},
    "dinars_log": {"fr": "Dinars, prix courants\n(échelle logarithmique)"},
    "dinars_c_log": {"fr": f"Dinars de {BASE}\n(échelle logarithmique)"},
    "t1": {"fr": "Journal officiel : ticket d'une section"},
    "t2": {"fr": "Journal officiel : ticket de deux sections"},
    "ins_billet": {"fr": "INS, relevé de prix à Tunis : billet d'autobus"},
    "creux": {"fr": "marque creuse : date d'effet non établie (date du fascicule)"},
    "trou": {"fr": "plage grisée : aucun tarif établi"},
    "ab_ord": {"fr": "Journal officiel : abonnement annuel ordinaire, ligne à une section"},
    "ab_sco": {"fr": "Journal officiel : abonnement scolaire, une ligne urbaine"},
    "ab_ins": {"fr": "INS, relevé de prix à Tunis : « abonnement scolaire (bus) »"},
    "voyageurs": {"fr": "Millions de voyageurs"},
    "payants": {"fr": "Payants non scolaires"},
    "scolaires": {"fr": "Scolaires"},
    "gratuits": {"fr": "Gratuits"},
    "abonnements": {"fr": "Abonnements scolaires (milliers)"},
    "seg1": {"fr": "éditions 2013 à 2016 du budget"},
    "seg2": {"fr": "édition 2017"},
    "rupture_ab": {"fr": "changement de mesure,\nnon expliqué par la source"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _ft(cle: str) -> str:
    return "\n".join(figtools.fig_text(ligne) for ligne in _lab(cle).split("\n"))


def _nb(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _legende(ax, poignees, ncol=2, y=-0.14):
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, y), ncol=ncol,
              fontsize=7.5, frameon=False)


def _cadre(ax, ylabel: str):
    ax.set_ylabel(_ft(ylabel))
    ax.set_xlabel(figtools.fig_text(_lab("x")))
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)


# --- provenance montrée au lecteur -------------------------------------------------------

PROVENANCE = {
    SOUTIEN: dict(
        perimetre=("budget du ministère du Transport, éditions 2013 à 2017, tableau des "
                   "principaux indicateurs, ligne du soutien du transport public par société ; "
                   "chaque édition donne l'année écoulée et l'année du budget"),
        caveats=("Crédits votés ou proposés, non dépenses constatées. Leur somme égale le poste "
                 "« transport » voté et s'écarte du réalisé en 2014, 2015 et 2017. L'année 2014 "
                 "a deux lectures : la loi de finances complémentaire crée la ligne de Tunisair "
                 "Express. Rien avant 2012 ni après 2017.")),
    TRANSFERTS: dict(
        perimetre=("rapport sur les transferts et les garanties (annexe 8 du projet de loi de "
                   "finances), éditions 2020, 2022, 2024 et 2025 : transferts du budget aux "
                   "entreprises et établissements du ministère du Transport, colonne des "
                   "interventions"),
        caveats=("Les interventions dépassent chaque année le poste « transport » : elles "
                 "comptent la société du réseau ferroviaire rapide, l'entretien du réseau ferré "
                 "et, en 2017, des prises en charge de dettes. Le rapprochement avec le poste "
                 "n'est établi que pour 2016. Réalisations de 2016 à 2023, loi de finances pour "
                 "2024.")),
    ABONNEMENTS: dict(
        perimetre=("budget du ministère du Transport, éditions 2013 à 2017, ligne de "
                   "l'évolution des abonnements scolaires, par société"),
        caveats=("Deux segments qui ne se raccordent pas : éditions 2013 à 2016, puis édition "
                 "2017. L'année 2016 a deux valeurs, 565 649 et 433 032, sans explication de la "
                 "source. Prévisions et chiffres de documents budgétaires, non un dénombrement "
                 "constaté ; la source ne dit pas l'unité.")),
    TARIFS: dict(
        perimetre=("arrêtés du ministre du transport publiés au Journal officiel, 1987-2000 : "
                   "réseaux urbains et suburbains des sociétés de transport routier, métro léger "
                   "de Tunis et TGM (hors colonnes propres aux sociétés de Sfax et du Sahel)"),
        caveats=("Tarif à sa date d'effet. La date d'effet des arrêtés du 26 août 1993 et du "
                 "17 février 2000 n'est pas établie. Un arrêté du 30 septembre 1989, qui modifie "
                 "celui du 10 août 1989, n'est connu que par son intitulé. Aucun tarif "
                 "postérieur à février 2000 n'est identifié au Journal officiel.")),
    INS: dict(
        perimetre=("INS, Bulletin mensuel de la statistique, tableau des prix moyens de détail "
                   "à Tunis, numéros de novembre 2008 à juillet 2026 : billet d'autobus, billet "
                   "de train de 2e classe, abonnement"),
        caveats=("Relevé de prix, non tarif. L'INS ne dit ni le trajet du billet ni la durée et "
                 "le réseau de l'abonnement. L'abonnement est imprimé en dinars jusqu'en avril "
                 "2017, en millimes ensuite ; pour 48 mois les numéros ne s'accordent pas "
                 "(arrondi, changement d'unité, révision) et le mois n'est pas tracé. Aucun "
                 "raccord avec les tarifs du Journal officiel.")),
    LIVRE_BLANC: dict(
        perimetre=("Banque mondiale, Livre blanc relatif au secteur des transports et de la "
                   "logistique (2016), annexe : trafic de la société des transports de Tunis — "
                   "autobus, métro et TGM —, 2007-2014, d'après la société"),
        caveats=("Rapport extérieur. La Banque reproduit un tableau de la société sans dire la "
                 "définition des catégories ni le mode de comptage (billets vendus, comptages, "
                 "estimation des abonnés).")),
    PARTS: dict(
        perimetre="poste « transport » de la dépense budgétaire de compensation",
        caveats=("Colonnes annuelles des rapports du ministère des Finances, relayées par la "
                 "Banque centrale à partir de 2019 ; 2024 est une colonne que la source ne "
                 "qualifie pas.")),
}
_ORIGINE: dict[str, dict] = {}


def _declarer(series_id: str, cles=None) -> None:
    """Provenance montrée au lecteur : clés restreintes à celles que la figure emploie, et
    présentes dans la bibliographie du livre ; périmètre et réserves réécrits pour lui."""
    if series_id not in _ORIGINE:
        _ORIGINE[series_id] = dict(figtools.meta(series_id))
    origine = _ORIGINE[series_id]
    connues = figtools._ref_index()
    cles = list(origine.get("sources", [])) if cles is None else list(dict.fromkeys(cles))
    champs = {k: v for k, v in origine.items() if k != "id" and not k.endswith("_ar")}
    champs["sources"] = [k for k in cles if k in connues]
    champs.update(PROVENANCE.get(series_id, {}))
    figtools.register_provenance(series_id, **champs)


def _poste(annees) -> dict[int, tuple[float, str]]:
    """Poste « transport » de la dépense de compensation : {année: (MD, clé de la source)}."""
    d = figtools.series(PARTS)
    d = d[(d["famille"] == "budget") & (d["poste"] == "transport") & d["annee"].isin(annees)]
    return {int(r.annee): (float(r.valeur_MDT), str(r.source)) for r in d.itertuples()}


# --- 1. Le soutien du transport public par société, 2012-2017 ----------------------------

GROUPES_SOUTIEN = (
    ("regionales", ("societes_regionales",), VERT, ""),
    ("tunis_bus", ("transtu_autobus",), BLEU, ""),
    ("tunis_metro", ("transtu_metro",), BLEU_CLAIR, "//"),
    ("sncft", ("sncft",), ORANGE, ""),
    ("autres", ("kerkennah", "tunisair_express", "sntri", "transport_scolaire_rural"), GRIS,
     ".."),
)


def _soutien_retenu():
    """Une lecture par année : celle de l'édition la plus récente qui porte l'année."""
    d = figtools.series(SOUTIEN)
    edition = d.groupby("annee")["edition"].transform("max")
    return d[d["edition"] == edition]


def fig_soutien(mesure: str = "md"):
    figtools.apply_lang_font()
    d = _soutien_retenu()
    annees = sorted(int(a) for a in d["annee"].unique())
    poste = _poste(annees)
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    for a in annees:
        da = d[d["annee"] == a]
        etat = str(da["etat"].iloc[0])
        total = float(da[da["ligne"] == "total"]["valeur_md"].iloc[0])
        bas = 0.0
        for cle, lignes, couleur, hachure in GROUPES_SOUTIEN:
            v = float(da[da["ligne"].isin(lignes)]["valeur_md"].sum())
            h = v if mesure == "md" else 100 * v / total
            barre = ax.bar([a], [h], bottom=bas, width=0.7, color=couleur, hatch=hachure,
                           edgecolor="white", zorder=2)
            figtools.infobulle(barre[0], f"{a} ({etat}) · {_lab(cle)} : {_nb(v)} MD, "
                                         f"{_nb(100 * v / total)} % du total")
            if mesure != "md" and h >= 6:
                ax.annotate(_nb(h, 0), xy=(a, bas + h / 2), ha="center", va="center",
                            fontsize=7, bbox=dict(facecolor="white", edgecolor="none",
                                                  alpha=0.75, pad=0.6))
            bas += h
        if mesure == "md":
            ax.annotate(_nb(total), xy=(a, bas), xytext=(0, 9), textcoords="offset points",
                        ha="center", va="bottom", fontsize=7)
            if a in poste:
                point, = ax.plot([a], [poste[a][0]], marker="o", color=NOIR, ms=5, ls="",
                                 zorder=4)
                figtools.infobulle(point, f"{a} · {_lab('poste')} : {_nb(poste[a][0])} MD")
    _cadre(ax, "md" if mesure == "md" else "pct")
    ax.set_xticks(annees)
    if mesure == "md":
        ax.set_ylim(top=ax.get_ylim()[1] * 1.12)
    else:
        ax.set_ylim(0, 105)
    poignees = [Patch(facecolor=c, hatch=h, edgecolor="white", label=figtools.fig_text(_lab(k)))
                for k, _, c, h in GROUPES_SOUTIEN]
    if mesure == "md":
        poignees.append(Line2D([], [], marker="o", color=NOIR, ls="", ms=5,
                               label=figtools.fig_text(_lab("poste"))))
    _legende(ax, poignees, ncol=2)
    fig.tight_layout()
    return fig


def _figure_soutien():
    d = figtools.series(SOUTIEN).sort_values(["annee", "edition", "ligne"])
    retenu = set(_soutien_retenu().index)
    table = d.assign(tracee=["oui" if i in retenu else "non" for i in d.index])[
        ["annee", "etat", "edition", "libelle", "valeur_md", "tracee", "page_pdf"]]
    table.columns = ["Année", "État du chiffre", "Édition du budget", "Ligne",
                     "Crédit (millions de dinars)", "Lecture tracée", "Page du PDF"]
    poste = _poste(range(2012, 2018))
    vues = [(_lab("vue_md"), fig_soutien("md")), (_lab("vue_part"), fig_soutien("part"))]
    return (vues, table.reset_index(drop=True),
            {SOUTIEN: None, PARTS: [s for _, s in poste.values()]},
            "fig_compensation_transport_soutien")


# --- 2. Les interventions du budget par entreprise, 2016-2024 ----------------------------

GROUPES_TRANSFERTS = (
    ("regionales", "societes_regionales", VERT, ""),
    ("tunis", "transtu", BLEU, ""),
    ("sncft", "sncft", ORANGE, ""),
    ("rfr", "rfr", VIOLET, "//"),
    ("autres", None, GRIS, ".."),
)


def _interventions():
    d = figtools.series(TRANSFERTS)
    return d[d["nature"] == "interventions"]


def fig_interventions():
    figtools.apply_lang_font()
    d = _interventions()
    d = d[d["derniere_edition"].astype(str).str.lower() == "true"]
    annees = sorted(int(a) for a in d["annee"].unique())
    poste = _poste(annees)
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    for a in annees:
        da = d[d["annee"] == a]
        etat = str(da["etat"].iloc[0])
        total = float(da[da["entite"] == "ministere"]["valeur_md"].iloc[0])
        nommes = 0.0
        bas = 0.0
        for cle, entite, couleur, hachure in GROUPES_TRANSFERTS:
            if entite is None:
                v = total - nommes
            else:
                v = float(da[da["entite"] == entite]["valeur_md"].sum())
                nommes += v
            barre = ax.bar([a], [v], bottom=bas, width=0.7, color=couleur, hatch=hachure,
                           edgecolor="white", zorder=2,
                           alpha=1.0 if etat == "réalisations" else 0.55)
            figtools.infobulle(barre[0], f"{a} ({etat}) · {_lab(cle)} : {_nb(v)} MD")
            bas += v
        ax.annotate(_nb(total, 0) + ("" if etat == "réalisations" else "*"), xy=(a, bas),
                    xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                    fontsize=7)
        if a in poste:
            point, = ax.plot([a], [poste[a][0]], marker="o", color=NOIR, ms=5, ls="", zorder=4)
            figtools.infobulle(point, f"{a} · {_lab('poste')} : {_nb(poste[a][0])} MD")
    ax.annotate(_ft("apurement"), xy=(2017, 835), xytext=(2018.3, 800), fontsize=7.5,
                color=ROUGE, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=ROUGE, lw=0.8))
    _cadre(ax, "md")
    ax.set_xticks(annees)
    ax.set_ylim(top=ax.get_ylim()[1] * 1.08)
    poignees = [Patch(facecolor=c, hatch=h, edgecolor="white", label=figtools.fig_text(_lab(k)))
                for k, _, c, h in GROUPES_TRANSFERTS]
    poignees.append(Line2D([], [], marker="o", color=NOIR, ls="", ms=5,
                           label=figtools.fig_text(_lab("poste"))))
    poignees.append(Patch(facecolor=GRIS, alpha=0.55, edgecolor="white",
                          label=figtools.fig_text("barre claire, astérisque : loi de finances")))
    _legende(ax, poignees, ncol=2)
    fig.tight_layout()
    return fig


def _figure_interventions():
    d = _interventions().sort_values(["annee", "edition", "entite"])
    table = d[["annee", "etat", "edition", "derniere_edition", "libelle", "valeur_md",
               "page_pdf"]].copy()
    table["derniere_edition"] = table["derniere_edition"].astype(str).str.lower().map(
        {"true": "oui", "false": "non"})
    table.columns = ["Année", "État du chiffre", "Édition du rapport", "Lecture tracée",
                     "Entité", "Interventions (millions de dinars)", "Page du PDF"]
    poste = _poste(range(2016, 2025))
    return ([(None, fig_interventions())], table.reset_index(drop=True),
            {TRANSFERTS: None, PARTS: [s for _, s in poste.values()]},
            "fig_compensation_transport_interventions")


# --- 3. Les tarifs : Journal officiel 1987-2000, relevé de l'INS 2007-2026 ---------------

FIN_INS = (2026, 7)


def _x(date: dt.date) -> float:
    debut = dt.date(date.year, 1, 1)
    return date.year + (date - debut).days / (366 if date.year % 4 == 0 else 365)


def _marches_jort(tarif: str) -> list[tuple[dt.date, float, bool, str]]:
    """(date posée, valeur, date d'effet établie ?, clé du texte), dans l'ordre des dates.

    Sans date d'effet établie, la marche est posée à la date du fascicule."""
    d = figtools.series(TARIFS)
    d = d[d["tarif"] == tarif].sort_values("date_signature")
    out = []
    for r in d.itertuples():
        effet = str(r.date_effet)[:10]
        etablie = len(effet) == 10 and effet[:4].isdigit()
        date = dt.date.fromisoformat(effet if etablie else str(r.jort_date)[:10])
        out.append((date, float(r.valeur), etablie, str(r.texte)))
    return out


def _annuel_jort(tarif: str, derniere_annee: int) -> dict[int, float]:
    """Moyenne des douze premiers du mois, pour les années entièrement établies."""
    marches = _marches_jort(tarif)
    douteuses = {date.year for date, _, etablie, _ in marches if not etablie}
    out = {}
    for annee in range(marches[0][0].year, derniere_annee + 1):
        if annee in douteuses:
            continue
        mois = []
        for m in range(1, 13):
            jour = dt.date(annee, m, 1)
            passees = [v for date, v, _, _ in marches if date <= jour]
            if not passees:
                break
            mois.append(passees[-1])
        if len(mois) == 12:
            out[annee] = sum(mois) / 12
    return out


def _ins_mensuel(ligne: str):
    """Relevé mensuel de l'INS, converti dans l'unité voulue ; mois sans accord écartés."""
    d = figtools.series(INS)
    d = d[(d["ligne"] == ligne) & d["accord"].astype(str).str.lower().eq("true")
          & d["valeur"].notna()].sort_values("periode")
    out = []
    for r in d.itertuples():
        v = float(r.valeur)
        if ligne == "abonnement" and r.unite == "millimes":
            v /= 1000.0  # l'abonnement est imprimé en dinars, puis en millimes : tout en dinars
        elif ligne == "abonnement" and r.unite != "dinars":
            continue
        annee, mois = (int(p) for p in str(r.periode).split("-"))
        out.append((annee, mois, v))
    return out


def _annuel_ins(ligne: str) -> dict[int, float]:
    par_annee: dict[int, list[float]] = {}
    for annee, _, v in _ins_mensuel(ligne):
        par_annee.setdefault(annee, []).append(v)
    return {a: sum(v) / 12 for a, v in par_annee.items() if len(v) == 12}


def _constants(annuel: dict[int, float]) -> dict[int, float]:
    indice = dinars_constants.ipc()
    return {a: dinars_constants.en_dinars_constants(v, a, indice) for a, v in annuel.items()
            if a in indice}


def _trace_marches(ax, marches, fin: float, couleur, ls="-"):
    for i, (date, v, etablie, texte) in enumerate(marches):
        x0 = _x(date)
        x1 = _x(marches[i + 1][0]) if i + 1 < len(marches) else fin
        trait, = ax.plot([x0, x1], [v, v], color=couleur, lw=1.8, ls=ls, zorder=3)
        if i + 1 < len(marches):
            ax.plot([x1, x1], [v, marches[i + 1][1]], color=couleur, lw=0.8, ls=ls, zorder=3)
        point, = ax.plot([x0], [v], marker="o", ms=4.5, color=couleur, ls="",
                         mfc=couleur if etablie else "white", zorder=4)
        bulle = (f"{_nb(v, 3 if v < 1000 and v != int(v) else 0)} — "
                 + (f"effet le {date.strftime('%d/%m/%Y')}" if etablie
                    else f"date d'effet non établie ; fascicule du {date.strftime('%d/%m/%Y')}"))
        figtools.infobulle(point, bulle)
        figtools.infobulle(trait, bulle)


def _trace_ins(ax, mensuel, couleur):
    """Relevé mensuel en marches ; le trait s'interrompt aux mois écartés."""
    suites, courante = [], []
    for annee, mois, v in mensuel:
        rang = annee * 12 + mois
        if courante and rang != courante[-1][0] + 1:
            suites.append(courante)
            courante = []
        courante.append((rang, v))
    if courante:
        suites.append(courante)
    for suite in suites:
        xs = [(r - 1) / 12 for r, _ in suite] + [suite[-1][0] / 12]
        ys = [v for _, v in suite] + [suite[-1][1]]
        ax.step(xs, ys, where="post", color=couleur, lw=1.8, zorder=3)


def _trace_annuel(ax, annuel, couleur, marque):
    annees = sorted(annuel)
    suite = []
    for a in annees + [None]:
        if suite and (a is None or a != suite[-1] + 1):
            ax.plot(suite, [annuel[s] for s in suite], color=couleur, lw=1.4, zorder=3)
            suite = []
        if a is not None:
            suite.append(a)
    for a in annees:
        point, = ax.plot([a], [annuel[a]], marker=marque, ms=4.5, color=couleur, ls="",
                         zorder=4)
        figtools.infobulle(point, f"{a} : {_nb(annuel[a], 1)}")


def _plage_vide(ax, x0=2000.2, x1=2007.83):
    ax.axvspan(x0, x1, color="#eaeef2", zorder=0)


def fig_tarifs(vue: str = "courants"):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    fin_jort = _x(dt.date(2000, 2, 25))
    if vue == "courants":
        _trace_marches(ax, _marches_jort("ticket_1_section"), fin_jort, NOIR)
        _trace_marches(ax, _marches_jort("ticket_2_sections"), fin_jort, BLEU)
        _trace_ins(ax, _ins_mensuel("billet_autobus"), ORANGE)
    else:
        _trace_annuel(ax, _constants(_annuel_jort("ticket_1_section", 1999)), NOIR, "o")
        _trace_annuel(ax, _constants(_annuel_jort("ticket_2_sections", 1999)), BLEU, "o")
        _trace_annuel(ax, _constants(_annuel_ins("billet_autobus")), ORANGE, "s")
    _plage_vide(ax)
    _cadre(ax, "millimes" if vue == "courants" else "millimes_c")
    ax.set_xlim(1986.5, 2027)
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    poignees = [Line2D([], [], color=NOIR, lw=1.8, marker="o", ms=4, label=figtools.fig_text(_lab("t1"))),
                Line2D([], [], color=BLEU, lw=1.8, marker="o", ms=4, label=figtools.fig_text(_lab("t2"))),
                Line2D([], [], color=ORANGE, lw=1.8, marker="s" if vue != "courants" else None,
                       ms=4, label=figtools.fig_text(_lab("ins_billet"))),
                Patch(facecolor="#eaeef2", label=figtools.fig_text(_lab("trou")))]
    if vue == "courants":
        poignees.append(Line2D([], [], color=NOIR, ls="", marker="o", mfc="white", ms=4.5,
                               label=figtools.fig_text(_lab("creux"))))
    _legende(ax, poignees, ncol=2)
    fig.tight_layout()
    return fig


def _table_prix(tarifs_jort, lignes_ins, unite_ins):
    import pandas as pd
    lignes = []
    d = figtools.series(TARIFS)
    for tarif in tarifs_jort:
        for r in d[d["tarif"] == tarif].sort_values("date_signature").itertuples():
            lignes.append({
                "Source": "Journal officiel", "Grandeur": r.libelle, "Unité": r.unite,
                "Date ou période": (str(r.date_effet)[:10] if str(r.date_effet)[:4].isdigit()
                                    else "date d'effet non établie"),
                "Valeur": float(r.valeur), f"Moyenne de l'année, en {r.unite} de {BASE}": None,
                "Texte": f"arrêté du {r.date_signature}, JORT n° {r.jort_numero} du "
                         f"{r.jort_date}, p. {r.jort_pages}"})
        unite = str(d[d["tarif"] == tarif]["unite"].iloc[0])
        for a, v in sorted(_constants(_annuel_jort(tarif, 1999)).items()):
            lignes.append({
                "Source": "Journal officiel", "Unité": unite, "Date ou période": str(a),
                "Grandeur": str(d[d["tarif"] == tarif]["libelle"].iloc[0]), "Valeur": None,
                f"Moyenne de l'année, en {unite} de {BASE}": round(v, 1), "Texte": ""})
    ins = figtools.series(INS)
    for ligne in lignes_ins:
        mensuel = _ins_mensuel(ligne)
        libelle = str(ins[ins["ligne"] == ligne]["libelles"].iloc[0]).split(" | ")[0]
        debut = None
        for i, (annee, mois, v) in enumerate(mensuel):
            suivant = mensuel[i + 1] if i + 1 < len(mensuel) else None
            debut = debut or (annee, mois)
            if (suivant is None or suivant[2] != v
                    or suivant[0] * 12 + suivant[1] != annee * 12 + mois + 1):
                lignes.append({
                    "Source": "INS, relevé de prix à Tunis", "Grandeur": libelle,
                    "Unité": unite_ins,
                    "Date ou période": f"{debut[0]}-{debut[1]:02d} à {annee}-{mois:02d}",
                    "Valeur": v, "Texte": "Bulletin mensuel de la statistique"})
                debut = None
        for a, v in sorted(_constants(_annuel_ins(ligne)).items()):
            lignes.append({
                "Source": "INS, relevé de prix à Tunis", "Grandeur": libelle,
                "Unité": unite_ins, "Date ou période": str(a), "Valeur": None,
                f"Moyenne de l'année, en {unite_ins} de {BASE}": round(v, 1), "Texte": ""})
    return pd.DataFrame(lignes)


CLES_URBAINS = ["arrete-1987-02-14-tarifs-voyageurs", "arrete-1989-08-10-tarifs-urbains",
                "arrete-1990-07-30-tarifs-urbains", "arrete-1991-07-02-tarifs-urbains",
                "arrete-1992-08-24-tarifs-urbains", "arrete-1993-08-26-tarifs-urbains",
                "arrete-1998-04-27-tarifs-urbains", "arrete-2000-02-17-tarifs-urbains"]


def _figure_tarifs():
    vues = [(_lab("vue_courants"), fig_tarifs("courants")),
            (_lab("vue_constants"), fig_tarifs("constants"))]
    table = _table_prix(("ticket_1_section", "ticket_2_sections"), ("billet_autobus",),
                        "millimes")
    return (vues, table, {TARIFS: CLES_URBAINS, INS: None,
                          **{s: None for s in dinars_constants.SERIES_IPC}},
            "fig_compensation_transport_tarifs")


# --- 4. Les abonnements : ordinaire et scolaire ------------------------------------------

def fig_abonnements_prix(vue: str = "courants"):
    figtools.apply_lang_font()
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    if vue == "courants":
        ordinaire = _marches_jort("abonnement_annuel_ordinaire_1_section")
        scolaire = _marches_jort("abonnement_scolaire_ligne_urbaine")
        _trace_marches(ax, ordinaire, _x(dt.date(2000, 2, 25)), NOIR)
        _trace_marches(ax, scolaire, _x(dt.date(2000, 2, 25)), BLEU)
        _trace_ins(ax, _ins_mensuel("abonnement"), ORANGE)
    else:
        _trace_annuel(ax, _constants(_annuel_jort("abonnement_annuel_ordinaire_1_section",
                                                  1999)), NOIR, "o")
        _trace_annuel(ax, _constants(_annuel_jort("abonnement_scolaire_ligne_urbaine", 1999)),
                      BLEU, "o")
        _trace_annuel(ax, _constants(_annuel_ins("abonnement")), ORANGE, "s")
    _plage_vide(ax)
    _cadre(ax, "dinars_log" if vue == "courants" else "dinars_c_log")
    ax.set_yscale("log")
    ax.set_yticks([10, 20, 50, 100, 200, 500] if vue == "courants"
                  else [20, 50, 100, 200, 500, 1000])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    ax.yaxis.set_minor_formatter(FuncFormatter(lambda v, _: ""))
    ax.set_xlim(1986.5, 2027)
    poignees = [Line2D([], [], color=NOIR, lw=1.8, marker="o", ms=4, label=figtools.fig_text(_lab("ab_ord"))),
                Line2D([], [], color=BLEU, lw=1.8, marker="o", ms=4, label=figtools.fig_text(_lab("ab_sco"))),
                Line2D([], [], color=ORANGE, lw=1.8, marker="s" if vue != "courants" else None,
                       ms=4, label=figtools.fig_text(_lab("ab_ins"))),
                Patch(facecolor="#eaeef2", label=figtools.fig_text(_lab("trou")))]
    if vue == "courants":
        poignees.append(Line2D([], [], color=NOIR, ls="", marker="o", mfc="white", ms=4.5,
                               label=figtools.fig_text(_lab("creux"))))
    _legende(ax, poignees, ncol=1, y=-0.13)
    fig.tight_layout()
    return fig


def _figure_abonnements_prix():
    vues = [(_lab("vue_courants"), fig_abonnements_prix("courants")),
            (_lab("vue_constants"), fig_abonnements_prix("constants"))]
    table = _table_prix(("abonnement_annuel_ordinaire_1_section",
                         "abonnement_scolaire_ligne_urbaine"), ("abonnement",), "dinars")
    cles = [c for c in CLES_URBAINS if "2000" not in c] + ["arrete-1998-07-29-abonnements-scolaires"]
    return (vues, table, {TARIFS: cles, INS: None,
                          **{s: None for s in dinars_constants.SERIES_IPC}},
            "fig_compensation_transport_abonnements_prix")


# --- 5. Le trafic de la société des transports de Tunis (rapport extérieur) --------------

CATEGORIES = (("payants", "voyageurs_payants_non_scolaires", BLEU, ""),
              ("scolaires", "voyageurs_scolaires", VERT, "//"),
              ("gratuits", "voyageurs_gratuits", GRIS, ".."))


def _trafic():
    d = figtools.series(LIVRE_BLANC)
    return d[(d["entite"] == "transtu") & d["indicateur"].str.startswith("voyageurs_")]


def fig_trafic(mesure: str = "millions"):
    figtools.apply_lang_font()
    d = _trafic()
    annees = sorted(int(a) for a in d["annee"].unique())
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    for a in annees:
        da = d[d["annee"] == a].set_index("indicateur")["valeur"]
        total = float(da["voyageurs_total"])
        bas = 0.0
        for cle, indicateur, couleur, hachure in CATEGORIES:
            v = float(da[indicateur])
            h = v if mesure == "millions" else 100 * v / total
            barre = ax.bar([a], [h], bottom=bas, width=0.7, color=couleur, hatch=hachure,
                           edgecolor="white", zorder=2)
            figtools.infobulle(barre[0], f"{a} · {_lab(cle)} : {_nb(v)} millions de voyageurs, "
                                         f"{_nb(100 * v / total, 0)} % du total")
            if mesure != "millions":
                ax.annotate(_nb(h, 0), xy=(a, bas + h / 2), ha="center", va="center",
                            fontsize=7, bbox=dict(facecolor="white", edgecolor="none",
                                                  alpha=0.75, pad=0.6))
            bas += h
        if mesure == "millions":
            ax.annotate(_nb(total), xy=(a, bas), xytext=(0, 2), textcoords="offset points",
                        ha="center", va="bottom", fontsize=7)
    _cadre(ax, "voyageurs" if mesure == "millions" else "pct")
    ax.set_xticks(annees)
    ax.set_ylim(top=ax.get_ylim()[1] * 1.06 if mesure == "millions" else 105)
    _legende(ax, [Patch(facecolor=c, hatch=h, edgecolor="white",
                        label=figtools.fig_text(_lab(k))) for k, _, c, h in CATEGORIES], ncol=3)
    fig.tight_layout()
    return fig


def _figure_trafic():
    d = _trafic().sort_values(["annee", "indicateur"])
    noms = {"voyageurs_payants_non_scolaires": "payants non scolaires",
            "voyageurs_scolaires": "scolaires", "voyageurs_gratuits": "gratuits",
            "voyageurs_total": "total"}
    table = d[["annee", "indicateur", "valeur", "source_declaree", "page_pdf"]].copy()
    table["indicateur"] = table["indicateur"].map(noms)
    table.columns = ["Année", "Catégorie de voyageurs", "Millions de voyageurs",
                     "Source déclarée par la Banque mondiale", "Page du PDF"]
    vues = [(_lab("vue_millions"), fig_trafic("millions")),
            (_lab("vue_part"), fig_trafic("part"))]
    return vues, table.reset_index(drop=True), {LIVRE_BLANC: None}, \
        "fig_compensation_transport_trafic_tunis"


# --- 6. Le nombre d'abonnements scolaires, deux segments ---------------------------------

SOCIETES_AB = (("regionales", "societes_regionales", VERT, ""),
               ("tunis", "transtu", BLEU, ""),
               ("sncft", "sncft", ORANGE, "//"))


def _abonnements_retenus():
    d = figtools.series(ABONNEMENTS)
    edition = d.groupby(["segment", "annee"])["edition"].transform("max")
    return d[d["edition"] == edition]


def fig_abonnements_nombre():
    figtools.apply_lang_font()
    d = _abonnements_retenus()
    segments = sorted(d["segment"].unique(), key=lambda s: int(d[d["segment"] == s]["edition"].max()))
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    x, etiquettes, coupure = 0, [], None
    for i, segment in enumerate(segments):
        ds = d[d["segment"] == segment]
        if i:
            coupure = x - 0.5 + 0.25
            x += 0.5
        for a in sorted(int(v) for v in ds["annee"].unique()):
            da = ds[ds["annee"] == a]
            etat = str(da["etat"].iloc[0])
            bas = 0.0
            for cle, ligne, couleur, hachure in SOCIETES_AB:
                v = float(da[da["ligne"] == ligne]["nombre"].iloc[0]) / 1000
                barre = ax.bar([x], [v], bottom=bas, width=0.7, color=couleur, hatch=hachure,
                               edgecolor="white", zorder=2)
                figtools.infobulle(barre[0], f"{a} ({etat}, édition {int(da['edition'].iloc[0])}) · "
                                             f"{_lab(cle)} : {_nb(v * 1000, 0)}")
                bas += v
            ax.annotate(_nb(bas * 1000, 0), xy=(x, bas), xytext=(0, 2),
                        textcoords="offset points", ha="center", va="bottom", fontsize=7)
            etiquettes.append((x, f"{a}\n({etat.replace('loi de finances complémentaire', 'LFC').replace('loi de finances', 'LF').replace('prévisions', 'prév.')})"))
            x += 1
    if coupure is not None:
        ax.axvline(coupure, color="#57606a", ls=(0, (2, 2)), lw=1, zorder=1)
        ax.annotate(_ft("rupture_ab"), xy=(coupure, 1), xycoords=("data", "axes fraction"),
                    xytext=(4, -4), textcoords="offset points", ha="left", va="top",
                    fontsize=7, color="#57606a")
        ax.annotate(_ft("seg1"), xy=(coupure, 1), xycoords=("data", "axes fraction"),
                    xytext=(-6, 4), textcoords="offset points", ha="right", va="bottom",
                    fontsize=7.5, color="#57606a")
        ax.annotate(_ft("seg2"), xy=(coupure, 1), xycoords=("data", "axes fraction"),
                    xytext=(6, 4), textcoords="offset points", ha="left", va="bottom",
                    fontsize=7.5, color="#57606a")
    _cadre(ax, "abonnements")
    ax.set_xticks([p for p, _ in etiquettes])
    ax.set_xticklabels([figtools.fig_text(e) for _, e in etiquettes], fontsize=7.5)
    ax.set_ylim(top=ax.get_ylim()[1] * 1.18)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    _legende(ax, [Patch(facecolor=c, hatch=h, edgecolor="white",
                        label=figtools.fig_text(_lab(k))) for k, _, c, h in SOCIETES_AB], ncol=3,
             y=-0.2)
    fig.tight_layout()
    return fig


def _figure_abonnements_nombre():
    d = figtools.series(ABONNEMENTS).sort_values(["edition", "annee", "ligne"])
    retenu = set(_abonnements_retenus().index)
    table = d.assign(tracee=["oui" if i in retenu else "non" for i in d.index])[
        ["annee", "etat", "edition", "segment", "libelle", "nombre", "tracee", "page_pdf"]].copy()
    table["segment"] = table["segment"].map(
        lambda s: "édition 2017" if "2017" in str(s) and "2013" not in str(s)
        else "éditions 2013 à 2016")
    table.columns = ["Année", "État du chiffre", "Édition du budget", "Segment", "Ligne",
                     "Abonnements scolaires", "Lecture tracée", "Page du PDF"]
    return ([(None, fig_abonnements_nombre())], table.reset_index(drop=True),
            {ABONNEMENTS: None}, "fig_compensation_transport_abonnements_nombre")


# --- registre ---------------------------------------------------------------------------

FIGURES = {
    "soutien_par_societe": _figure_soutien,
    "interventions": _figure_interventions,
    "tarifs": _figure_tarifs,
    "abonnements_prix": _figure_abonnements_prix,
    "trafic_tunis": _figure_trafic,
    "abonnements_nombre": _figure_abonnements_nombre,
}
NON_MONETAIRES = {"trafic_tunis", "abonnements_nombre"}


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure `nom` en onglets (graphique, données, sources).

    À appeler dans un chunk Quarto étiqueté `#| label: fig-…`, `#| output: asis`."""
    vues, table, cles, slug = FIGURES[nom]()
    for sid, liste in cles.items():
        _declarer(sid, liste)
    figtools.figure_tabs(vues, table, *cles, slug=slug, caption=caption,
                         note_lecture=note_lecture, nominal=nom not in NON_MONETAIRES)
    plt.close("all")


def reperes() -> dict:
    """Valeurs calculées que le chapitre cite : à relire quand une série ou l'indice change."""
    t1 = _constants(_annuel_jort("ticket_1_section", 1999))
    t2 = _constants(_annuel_jort("ticket_2_sections", 1999))
    ins = _constants(_annuel_ins("billet_autobus"))
    return {"ticket_1_section": t1, "ticket_2_sections": t2, "billet_ins": ins,
            "abonnement_scolaire": _constants(_annuel_jort("abonnement_scolaire_ligne_urbaine",
                                                           1999)),
            "abonnement_ordinaire": _constants(
                _annuel_jort("abonnement_annuel_ordinaire_1_section", 1999)),
            "abonnement_ins": _constants(_annuel_ins("abonnement"))}

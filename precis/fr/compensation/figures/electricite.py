"""Figures du chapitre « L'électricité et le gaz » (volume « La compensation »), longue période.

    from figures import electricite as el
    el.figure("prix_achat_gaz", caption=…, note_lecture=…)
    el.figure("cout_prix_kwh", caption=…, note_lecture=…)
    el.figure("subvention", caption=…, note_lecture=…)
    el.figure("gaz_sources", caption=…, note_lecture=…)
    el.figure("gaz_pib", caption=…, note_lecture=…)
    el.figure("tarifs_mt", caption=…, note_lecture=…)

LA FIGURE `tarifs_mt` lit une sixième série, `steg-tarifs-moyenne-tension`, versionnée dans
`precis/_seriescache/` : la transcription valeur par valeur des trois tableaux du chapitre sur la
moyenne tension (`scripts/serie_tarifs_mt.py`, qui la compare aux tableaux, dans les deux sens). Elle
n'est pas dans l'entrepôt : sa provenance est déclarée ici.

D'OÙ VIENNENT LES AUTRES DONNÉES. Cinq séries de `tunisia-data` (la cinquième, la facture des combustibles,
ne sert qu'à la figure en points de PIB), lues par `figtools.series()` — donc
depuis le snapshot `precis/_seriescache/` quand l'entrepôt est absent :

  - `steg-prix-achat-gaz` : prix d'achat de la tonne équivalent pétrole de gaz, en dinars
    courants — prix de cession administré, prix moyen d'achat du rapport de contrôle de 2014,
    prix moyen d'achat des états financiers de la STEG ; la famille de l'Observatoire (prix
    d'importation du gaz algérien) est dans la série et n'est pas tracée ici ;
  - `steg-cout-prix-kwh` : coût de revient et prix de vente moyen hors taxes du kilowattheure,
    en millimes courants, par famille de source ;
  - `steg-subvention-exploitation` : subvention d'exploitation de la STEG, 2006-2016, soutien
    direct et indirect du rapport de contrôle de 2014 ;
  - `steg-prelevements-gaz` : gaz prélevé par la STEG, par source, 2001-2024, en ktep ;
  - `steg-facture-combustibles` : « achats de combustibles » des états financiers de la STEG,
    2013-2023, en millions de dinars courants — le numérateur du prix moyen d'achat publié ;
  - `pib-courant-par-base` : PIB aux prix courants, ligne « base 2015 » seule (2013-2014
    rétropolés par l'INS, 2015-2023 publiés dans les Comptes de la nation) ; une seule base
    sur toute la période, donc rien à chaîner. Voir l'annexe du site sur le PIB.

RÈGLES (les mêmes que `compensation.py` et `transport.py`).

  - **Aucune famille n'est raccordée à une autre** : une famille a sa couleur, sa marque et son
    trait ; une année manquante interrompt le trait ; une année sans valeur reste vide.
  - **Les ruptures viennent des données** (colonnes `rupture` et `rupture_annee`) : un trait
    vertical et un repère triangulaire dont l'infobulle porte le texte complet.
  - **Une valeur par ligne retenue** : la ligne `retenu = non` (coût de 2016 calculé) n'est pas
    tracée ; elle reste dans l'onglet « Données ».
  - **Dinars et millimes courants, aucun PIB** — sauf la figure `gaz_pib`, qui divise par le PIB
    nominal de la base 2015, seule base employée (voir sa note de lecture).
  - **La ligne « Source » ne cite que les clés des lignes tracées.**

Les libellés sont en français ; les libellés arabes restent à verser.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
import pandas as pd  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import dinars_constants  # noqa: E402
import figtools  # noqa: E402

PRIX = "steg-prix-achat-gaz"
KWH = "steg-cout-prix-kwh"
SUBV = "steg-subvention-exploitation"
GAZ = "steg-prelevements-gaz"
FACTURE = "steg-facture-combustibles"
PIB = "pib-courant-par-base"
TARIFS_MT = "steg-tarifs-moyenne-tension"

BLEU, BLEU_CLAIR, ORANGE, VERT, VIOLET, ROUGE, GRIS, BRUN, NOIR, ROSE, TEAL = (
    "#0969da", "#80b3f0", "#d1600f", "#1a7f37", "#8250df", "#cf222e", "#8c959f", "#9a6700",
    "#24292f", "#bf3989", "#1b7c83")
GRIS_FONCE = "#57606a"


def _nb(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _v(v: float) -> str:
    """Valeur sans décimale inutile : 0, 339, 804,4."""
    return _nb(v, 0 if float(v) == round(float(v)) else 1)


def _legende(ax, poignees, ncol=2, y=-0.14):
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, y), ncol=ncol,
              fontsize=7.5, frameon=False)


def _cadre(ax, ylabel: str, xlabel: str | None = "Année"):
    ax.set_ylabel(ylabel)
    if xlabel:
        ax.set_xlabel(xlabel)
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)


def _cles(*dfs) -> list[str]:
    """Clés de citation des lignes tracées, dans l'ordre où elles apparaissent."""
    vues: dict[str, None] = {}
    for d in dfs:
        for x in d["cle"]:
            for c in str(x).split(" ; "):
                if c:
                    vues[c] = None
    return list(vues)


def _repere(ax, annee, texte):
    """Trait vertical de rupture et petit triangle en haut du trait, porteur de l'infobulle."""
    figtools.marque_rupture(ax, annee)
    p, = ax.plot([annee - 0.5], [1], marker=7, ms=6, color=GRIS_FONCE, clip_on=False, zorder=4,
                 transform=ax.get_xaxis_transform())
    figtools.infobulle(p, texte)


def _segments(annees, valeurs):
    """Coupe en suites d'années consécutives : une année manquante interrompt le trait."""
    suites, cour = [], []
    for a, v in zip(annees, valeurs):
        if cour and a != cour[-1][0] + 1:
            suites.append(cour)
            cour = []
        cour.append((a, v))
    if cour:
        suites.append(cour)
    return suites


def _trace_famille(ax, d, valeur, couleur, marque, ls="-", creux=False, texte=None, lw=1.5):
    """Trace une famille : le trait, puis chaque point séparément (une infobulle par point)."""
    d = d.sort_values("annee")
    for suite in _segments(d["annee"].tolist(), d[valeur].tolist()):
        if len(suite) > 1:
            ax.plot([a for a, _ in suite], [v for _, v in suite], color=couleur, ls=ls, lw=lw,
                    zorder=2)
    for r in d.itertuples(index=False):
        p, = ax.plot([r.annee], [getattr(r, valeur)], marker=marque, ms=5, color=couleur,
                     mfc="white" if creux else couleur, mew=1.2, ls="none", zorder=3)
        if texte:
            figtools.infobulle(p, texte(r))


# --- provenance montrée au lecteur ---------------------------------------------------------

PROVENANCE = {
    PRIX: dict(
        perimetre=("prix de cession administré du gaz à la STEG (90,8 dinars la tonne équivalent "
                   "pétrole, 1993-2014) ; prix moyen d'achat de la tep du rapport de contrôle du "
                   "21 juillet 2014 (2007-2013, p. 72) ; prix moyen annuel d'achat de la tep de "
                   "gaz des états financiers de la STEG, exercices 2013 à 2023"),
        caveats=("Trois séries qui ne se raccordent pas. Le prix de cession est un prix "
                 "administré, constant, non un prix d'achat. Le prix moyen de la STEG porte sur "
                 "toutes les sources de gaz et son numérateur comprend le fuel et le gazole. "
                 "Ruptures : 2007 (la STEG comptabilise le gaz à sa valeur économique) et 2015 "
                 "(fin du prix de cession). Aucune valeur avant 1993 ni après 2023. Dinars "
                 "courants.")),
    KWH: dict(
        perimetre=("coût de revient et prix de vente moyen hors taxes du kilowattheure, toutes "
                   "tensions confondues, par famille de source : ESMAP (prix 1994-1999), ANER "
                   "(coût 1996-1998, lu sur un graphique), Banque africaine de développement "
                   "(2000-2010), rapport de contrôle de 2014 (2008-2012), états financiers de la "
                   "STEG puis Observatoire national de l'énergie (2013-2018), Observatoire "
                   "(2019-2025)"),
        caveats=("Les sources ne se raccordent pas. Rupture de 2007 : jusqu'en 2006 le gaz est "
                 "au prix administré, ensuite à sa valeur économique. Aucun coût de revient pour "
                 "1999, 2005-2007 et 2019-2021, aucune valeur reconstituée. Les valeurs de l'ANER "
                 "sont lues sur un graphique, à un millime près. De 2013 à 2018 les états "
                 "financiers de la STEG et l'Observatoire ont la même origine. Les données de "
                 "2022 à 2025 sont dites provisoires avant audit. Millimes courants.")),
    SUBV: dict(
        perimetre=("« subvention d'exploitation » de l'état de résultat de la STEG, 2006-2016 ; "
                   "soutien direct, indirect et total à la STEG du rapport de contrôle du 21 "
                   "juillet 2014 (2007-2013) ; ventilation des états financiers de 2014 (2013 et "
                   "2014)"),
        caveats=("La subvention d'exploitation des comptes n'est pas la ligne budgétaire : jusqu'en "
                 "2014 elle comprend la subvention indirecte, c'est-à-dire le gaz valorisé à sa "
                 "valeur économique. Elle égale le soutien total du rapport de contrôle, à "
                 "l'arrondi imprimé près. Rupture de 2015. Aucune valeur après 2016. Dinars "
                 "courants.")),
    GAZ: dict(
        perimetre=("tableau « prélèvements de gaz » de chaque rapport annuel de la STEG, 2001-2024 : "
                   "gaz algérien (redevance consommée, achats contractuels et additionnels), "
                   "champ de Miskar, autres champs nationaux, total"),
        caveats=("Le total égale la somme des parties chaque année. De 2001 à 2006 les tableaux ne "
                 "séparent pas la redevance des achats de gaz algérien. Le « total des achats "
                 "gaz » de 2019-2024 vient d'un autre tableau et n'est pas le total des "
                 "prélèvements. Quantités en ktep, pouvoir calorifique supérieur.")),
}
PROVENANCE[TARIFS_MT] = dict(
    titre=("Le tarif de l'électricité en moyenne tension, 1994-2022 : prix du kilowattheure par "
           "poste horaire, tarif uniforme et tarif de secours, prime de puissance, à chaque date "
           "d'effet"),
    perimetre=("grilles de la moyenne tension de la STEG à chaque date d'effet : relais des "
               "agences publiques de promotion (FIPA, API) et tableau 6.2 de l'ESMAP pour juin 1994, "
               "août 2000, août 2001 et avril 2003 ; grilles de la STEG, pages archivées de son site "
               "et documents de l'entreprise, du 1er mai 2004 au 1er octobre 2022. Prix hors taxes, "
               "en millimes courants par kWh ; prime en millimes par kW et par mois (par kVA pour le "
               "tarif uniforme de 1994 à 2003)"),
    caveats=("Les familles de postes ne se raccordent pas : trois postes (juin 1994 à août 2000), "
             "quatre postes (août 2000 à mai 2014), quatre postes redéfinis (depuis le 1er mai "
             "2014). Le jour du passage de trois à quatre postes n'est pas établi, ni le jour "
             "d'effet de la grille de juin 1994. Le soir et la nuit du tarif à postes horaires et "
             "du tarif de secours du 1er août 2001 ne sont pas donnés par la source. Le tarif de "
             "secours n'est pas relevé après 2003. Aucune grille postérieure au 1er octobre 2022 "
             "n'est établie."),
    source_ligne=("grilles de la moyenne tension de la STEG, 2004-2022 ; relais des agences "
                  "publiques et de l'ESMAP, 1994-2003 (toutes les références : onglet « Sources »)"),
)
def _regle_2025() -> str:
    """La règle de la monnaie de 2025, écrite sous les figures et dans l'onglet « Sources »."""
    ipc = dinars_constants.ipc()
    return (
        "Monnaie de 2025 : valeurs calculées, non observées. La référence est l'indice annuel moyen "
        "de 2025, le dernier indice annuel publié (base 100 en 2015, 186,3, que relaie la Banque "
        "centrale) ; elle sera actualisée à la publication de l'indice annuel suivant. Le coefficient "
        "d'une année est l'indice annuel moyen de 2025 divisé par celui de cette année ; une date "
        "d'effet en cours d'année est ramenée par l'indice annuel moyen de son année d'effet, et une "
        "grille qui dure plusieurs années est ramenée année par année (la valeur de la grille baisse "
        "en monnaie de 2025 tant qu'elle ne change pas). Les indices annuels sont ceux de l'INS en "
        "base 1970 jusqu'en 2023, prolongés pour 2024 et 2025 par la variation de l'indice en base "
        f"2015 que relaie la Banque centrale (indice de 2025 : {_nb(ipc[2025])} en base 1970, par ce "
        "raccord) ; sur 2015-2023, où les deux bases sont publiées, leur rapport varie de 0,3 %. Les "
        "familles et les ruptures de la figure ne sont pas raccordées par ce changement d'unité.")


regle_2025 = _regle_2025


def _coeff(annee: int) -> float:
    """Coefficient qui ramène un montant de l'année `annee` à la monnaie de 2025 (indice annuel)."""
    indice = dinars_constants.ipc()
    return indice[dinars_constants.ANNEE_BASE] / indice[int(annee)]


figtools.register_provenance(TARIFS_MT, titre=PROVENANCE[TARIFS_MT]["titre"], sources=[],
                             unite="millimes courants par kWh, hors taxes")
_ORIGINE: dict[str, dict] = {}


def _declarer(series_id: str, cles=None, surcharge: dict | None = None) -> None:
    """Provenance montrée au lecteur : clés restreintes à celles que la figure emploie et
    présentes dans la bibliographie du livre ; périmètre et réserves réécrits pour lui."""
    if series_id not in _ORIGINE:
        _ORIGINE[series_id] = dict(figtools.meta(series_id))
    origine = _ORIGINE[series_id]
    connues = figtools._ref_index()
    cles = list(origine.get("sources", [])) if cles is None else list(dict.fromkeys(cles))
    champs = {k: v for k, v in origine.items() if k != "id" and not k.endswith("_ar")}
    champs["sources"] = [k for k in cles if k in connues]
    champs.update(PROVENANCE.get(series_id, {}))
    if series_id in (TARIFS_MT, PRIX) and "caveats" in champs:
        champs["caveats"] = f"{champs['caveats']} {_regle_2025()}"
    champs.update(surcharge or {})
    figtools.register_provenance(series_id, **champs)


# --- 1. Le prix d'achat de la tonne équivalent pétrole de gaz --------------------------------

FAM_PRIX = (
    ("prix_de_cession", "Prix de cession administré, 1993-2014 (rapport de contrôle de 2014)",
     BLEU, "s", "-"),
    ("rapport_de_controle_2014", "Prix moyen d'achat de la tep, rapport de contrôle de 2014, "
     "2007-2013", ORANGE, "o", "--"),
    ("etats_financiers_steg", "Prix moyen d'achat de la tep de gaz, états financiers de la STEG, "
     "2013-2023", VERT, "^", "-"),
)


def _prix_2025(d):
    """Ajoute le coefficient et la valeur en monnaie de 2025 (calculée) à chaque ligne annuelle."""
    d = d.copy()
    d["coefficient_2025"] = [_coeff(a) for a in d["annee"]]
    d["valeur_2025"] = d["valeur"] * d["coefficient_2025"]
    return d


def fig_prix_achat_gaz(constants: bool = False):
    figtools.apply_lang_font()
    d = figtools.series(PRIX)
    if constants:
        d = _prix_2025(d)
        d["valeur_courante"] = d["valeur"]
        d["valeur"] = d["valeur_2025"]
    fig, ax = plt.subplots(figsize=(9.5, 4.9))
    for fam, etiquette, couleur, marque, ls in FAM_PRIX:
        df = d[d["famille"] == fam]
        if constants:
            texte = lambda r, e=etiquette: (
                f"{r.annee} · {e} : {_nb(r.valeur)} dinars de 2025 par tep, valeur calculée "
                f"({_nb(r.valeur_courante)} dinars courants × {_nb(r.coefficient_2025, 3)} ; "
                f"{r.source}, {r.page})")
        else:
            texte = lambda r, e=etiquette: (
                f"{r.annee} · {e} : {_nb(r.valeur)} dinars par tep ({r.source}, {r.page})")
        _trace_famille(ax, df, "valeur", couleur, marque, ls=ls, texte=texte)
        if constants:
            v = df.sort_values("annee")
            for k, dec, ha in ((0, (0, 7), "center") if fam != "etats_financiers_steg"
                               else (0, (8, 4), "left"), (-1, (0, 7), "center")):
                r = v.iloc[k]
                ax.annotate(_v(round(r["valeur"])), xy=(r["annee"], r["valeur"]), xytext=dec,
                            textcoords="offset points", ha=ha, fontsize=7, color=couleur)
        elif fam != "prix_de_cession":
            etiq = {"rapport_de_controle_2014": ((0, (0, 7)), (-1, (-3, 8, "right"))),
                    "etats_financiers_steg": ((0, (7, -14, "left")), (-1, (-6, -13, "right")))}
            for i, (dx, dy, *ha) in ((i, (o[0], o[1], *o[2:])) for i, o in etiq[fam]):
                r = df.iloc[i]
                ax.annotate(_v(r["valeur"]), xy=(r["annee"], r["valeur"]), xytext=(dx, dy),
                            textcoords="offset points", ha=ha[0] if ha else "center",
                            fontsize=7, color=couleur)
    haut = d[d["famille"] == "etats_financiers_steg"].sort_values("valeur").iloc[-1]
    if not constants:
        ax.annotate(_v(haut["valeur"]), xy=(haut["annee"], haut["valeur"]), xytext=(0, 7),
                    textcoords="offset points", ha="center", fontsize=7, color=VERT)
        ax.annotate("90,8", xy=(2003, 90.8), xytext=(0, 7), textcoords="offset points",
                    ha="center", fontsize=7.5, color=BLEU)
    for r in d[d["rupture"].fillna("") != ""].itertuples(index=False):
        _repere(ax, int(r.rupture_annee), f"{int(r.rupture_annee)} · {r.rupture}")
    _cadre(ax, "Dinars de 2025 par tep (calculés)" if constants
           else "Dinars courants par tonne équivalent pétrole")
    ax.set_xlim(1992.3, 2023.7)
    ax.set_xticks(range(1993, 2024, 2))
    ax.set_ylim(0, 1650 if not constants
                else 50 * math.ceil(d[d["famille"] != "observatoire_import_gaz_algerien"]
                                    ["valeur"].max() * 1.1 / 50))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    poignees = [Line2D([0], [0], color=c, marker=m, ls=ls, lw=1.5, ms=5,
                       label=figtools.fig_text(e)) for _, e, c, m, ls in FAM_PRIX]
    poignees.append(Line2D([0], [0], marker=7, color=GRIS_FONCE, ls="none", ms=6,
                           label="rupture de série (infobulle sur le triangle)"))
    _legende(ax, poignees, ncol=1, y=-0.13)
    fig.tight_layout()
    return fig


def _figure_prix_achat_gaz():
    d = figtools.series(PRIX)
    d = d[d["famille"] != "observatoire_import_gaz_algerien"].sort_values(["famille", "annee"])
    d = _prix_2025(d)
    noms = {"prix_de_cession": "prix de cession administré",
            "rapport_de_controle_2014": "prix moyen d'achat, rapport de contrôle de 2014",
            "etats_financiers_steg": "prix moyen d'achat, états financiers de la STEG"}
    table = d[["famille", "annee", "valeur", "coefficient_2025", "valeur_2025", "etat", "source",
               "page", "lecture", "rupture"]].copy()
    table["famille"] = table["famille"].map(noms)
    table["coefficient_2025"] = table["coefficient_2025"].round(4)
    table["valeur_2025"] = table["valeur_2025"].round(1)
    table.columns = ["Famille", "Année", "Dinars courants par tep", "Coefficient de 2025 (calculé)",
                     "valeur_2025 : dinars de 2025 par tep (calculée)", "État", "Source", "Page",
                     "Lecture", "Rupture"]
    vues = [("Dinars courants", fig_prix_achat_gaz()),
            ("Dinars de 2025 (calculés)", fig_prix_achat_gaz(constants=True))]
    return (vues, table.reset_index(drop=True),
            {PRIX: _cles(d), dinars_constants.SERIE_IPC: None,
             dinars_constants.SERIE_IPC_RECENT: None},
            "fig_compensation_eg_prix_achat_gaz")


# --- 2. Le coût de revient et le prix de vente moyen du kilowattheure ------------------------

FAM_KWH = (
    ("esmap", "ESMAP, 1994-1999 (prix seul)", GRIS, "v"),
    ("aner", "ANER, 1996-1998 (coût lu sur graphique)", BRUN, "D"),
    ("bad_electricite_vi", "BAD, Électricité VI, 2000-2004", VIOLET, "s"),
    ("bad_electricite_vii", "BAD, Électricité VII, 2005-2007 (prix seul)", ROSE, "P"),
    ("cgf_2014", "Rapport de contrôle de 2014, 2008-2012", ORANGE, "o"),
    ("steg_observatoire_2013_2018", "États financiers de la STEG puis Observatoire, 2013-2018",
     BLEU, "^"),
    ("observatoire_2019_2021", "Observatoire, 2019-2021 (prix seul)", TEAL, "<"),
    ("observatoire_2022_2025", "Observatoire, 2022-2025 (provisoire avant audit)", VERT, ">"),
)
SANS_COUT = ((1998.5, 1999.5), (2004.5, 2007.5), (2018.5, 2021.5))


def _kwh_retenu():
    d = figtools.series(KWH)
    return d[d["retenu"] == "oui"]


def fig_cout_prix_kwh():
    figtools.apply_lang_font()
    d = _kwh_retenu()
    fig, (axc, axp) = plt.subplots(2, 1, figsize=(9.5, 7.2), sharex=True, sharey=True)
    for ax, grandeur, titre in ((axc, "cout_de_revient", "Coût de revient"),
                                (axp, "prix_de_vente_moyen", "Prix de vente moyen, hors taxes")):
        for fam, etiquette, couleur, marque in FAM_KWH:
            df = d[(d["famille"] == fam) & (d["grandeur"] == grandeur)]
            if fam == "bad_electricite_vii":
                df = df[df["annee"] <= 2007]
            if df.empty:
                continue
            _trace_famille(
                ax, df, "valeur", couleur, marque,
                texte=lambda r, e=etiquette, t=titre: (
                    f"{r.annee} · {t.lower()} · {e} : {_nb(r.valeur)} millimes par kWh "
                    f"({r.source}, {r.page} ; {r.etat})"))
        ax.set_title(figtools.fig_text(titre), fontsize=9, loc="left")
        ax.grid(True, axis="y", alpha=0.3)
        ax.set_axisbelow(True)
        ax.set_ylabel("Millimes courants par kWh")
        for r in d[(d["rupture"].fillna("") != "")].head(1).itertuples(index=False):
            figtools.marque_rupture(ax, int(r.rupture_annee))
            if ax is axc:
                _repere(ax, int(r.rupture_annee), f"{int(r.rupture_annee)} · {r.rupture}")
    for a0, a1 in SANS_COUT:
        axc.axvspan(a0, a1, color="#d0d7de", alpha=0.55, lw=0, zorder=0)
        axc.annotate("aucun coût publié", xy=((a0 + a1) / 2, 250), ha="center", va="center",
                     rotation=90, fontsize=6.5, color=GRIS_FONCE)
    axp.set_xlabel("Année")
    axp.set_xlim(1993.3, 2025.7)
    axp.set_xticks(range(1994, 2026, 2))
    axp.set_ylim(0, 520)
    poignees = [Line2D([0], [0], color=c, marker=m, ls="-", lw=1.5, ms=5,
                       label=figtools.fig_text(e)) for _, e, c, m in FAM_KWH]
    poignees.append(Patch(facecolor="#d0d7de", label="années sans coût de revient publié"))
    poignees.append(Line2D([0], [0], marker=7, color=GRIS_FONCE, ls="none", ms=6,
                           label="rupture de série (infobulle sur le triangle)"))
    _legende(axp, poignees, ncol=2, y=-0.22)
    fig.tight_layout()
    return fig


def _figure_cout_prix_kwh():
    d = figtools.series(KWH)
    noms = {f: e for f, e, *_ in FAM_KWH}
    gr = {"cout_de_revient": "coût de revient", "prix_de_vente_moyen": "prix de vente moyen",
          "cout_combustibles": "coût : combustibles", "cout_personnel": "coût : personnel",
          "cout_charges_financieres_assurances": "coût : charges financières et assurances",
          "cout_amortissements": "coût : amortissements", "cout_divers": "coût : divers"}
    table = d.sort_values(["famille", "annee", "grandeur"]).copy()
    table["tracee"] = [("non" if r.retenu != "oui" or (r.famille == "bad_electricite_vii"
                                                       and r.annee > 2007)
                        or r.grandeur.startswith("cout_") and r.grandeur != "cout_de_revient"
                        else "oui") for r in table.itertuples(index=False)]
    table["famille"] = table["famille"].map(noms)
    table["grandeur"] = table["grandeur"].map(gr)
    table = table[["famille", "annee", "grandeur", "valeur", "etat", "tracee", "source", "page",
                   "lecture", "rupture", "remarque"]]
    table.columns = ["Famille", "Année", "Grandeur", "Millimes courants par kWh", "État",
                     "Tracée", "Source", "Page", "Lecture", "Rupture", "Remarque"]
    return ([(None, fig_cout_prix_kwh())], table.reset_index(drop=True),
            {KWH: _cles(d)}, "fig_compensation_eg_cout_prix_kwh")


# --- 3. La subvention d'exploitation de la STEG ----------------------------------------------

def fig_subvention():
    figtools.apply_lang_font()
    d = figtools.series(SUBV)
    comptes = d[d["grandeur"] == "subvention_exploitation"].sort_values("annee")
    cg = d[d["famille"] == "rapport_de_controle_2014"].pivot(index="annee", columns="grandeur",
                                                             values="valeur")
    fig, ax = plt.subplots(figsize=(9.5, 4.9))
    for a, v in cg.iterrows():
        barre = ax.bar([a], [v["soutien_direct"]], width=0.62, color=BLEU, hatch="//",
                       edgecolor="white", zorder=2)
        figtools.infobulle(barre[0], f"{a} · soutien direct (rapport de contrôle de 2014) : "
                                     f"{_nb(v['soutien_direct'])} millions de dinars")
        barre = ax.bar([a], [v["soutien_indirect"]], bottom=[v["soutien_direct"]], width=0.62,
                       color=ORANGE, edgecolor="white", zorder=2)
        figtools.infobulle(barre[0], f"{a} · soutien indirect (rapport de contrôle de 2014) : "
                                     f"{_nb(v['soutien_indirect'])} millions de dinars")
    ax.plot(comptes["annee"], comptes["valeur"], color=NOIR, lw=1.2, zorder=3)
    for r in comptes.itertuples(index=False):
        p, = ax.plot([r.annee], [r.valeur], marker="o", ms=6, color=NOIR, ls="none", zorder=4)
        figtools.infobulle(p, f"{r.annee} · subvention d'exploitation des comptes de la STEG : "
                              f"{_nb(r.valeur)} millions de dinars ({r.source}, {r.page})")
        ax.annotate(_v(r.valeur), xy=(r.annee, r.valeur), xytext=(0, 7),
                    textcoords="offset points", ha="center", fontsize=7)
    for r in comptes[comptes["rupture"].fillna("") != ""].itertuples(index=False):
        _repere(ax, int(r.rupture_annee), f"{int(r.rupture_annee)} · {r.rupture}")
    _cadre(ax, "Millions de dinars courants")
    ax.set_xticks(range(2006, 2017))
    ax.set_xlim(2005.4, 2016.6)
    ax.set_ylim(0, ax.get_ylim()[1] * 1.08)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    _legende(ax, [
        Patch(facecolor=BLEU, hatch="//", edgecolor="white",
              label="soutien direct (rapport de contrôle de 2014)"),
        Patch(facecolor=ORANGE, label="soutien indirect (rapport de contrôle de 2014)"),
        Line2D([0], [0], color=NOIR, marker="o", ms=6, lw=1.2,
               label="subvention d'exploitation des comptes de la STEG"),
        Line2D([0], [0], marker=7, color=GRIS_FONCE, ls="none", ms=6,
               label="rupture de série (infobulle sur le triangle)")], ncol=2, y=-0.13)
    fig.tight_layout()
    return fig


def _figure_subvention():
    d = figtools.series(SUBV)
    noms = {"comptes_steg": "comptes de la STEG",
            "rapport_de_controle_2014": "rapport de contrôle de 2014",
            "etats_financiers_2014": "états financiers de 2014"}
    gr = {"subvention_exploitation": "subvention d'exploitation", "soutien_direct": "soutien direct",
          "soutien_indirect": "soutien indirect", "soutien_total": "soutien total",
          "subvention_directe": "subvention directe reçue",
          "subvention_indirecte": "subvention indirecte sur l'achat du gaz algérien"}
    table = d.sort_values(["famille", "grandeur", "annee"]).copy()
    table["tracee"] = ["non" if r.famille == "etats_financiers_2014" or r.grandeur == "soutien_total"
                       else "oui" for r in table.itertuples(index=False)]
    table["famille"] = table["famille"].map(noms)
    table["grandeur"] = table["grandeur"].map(gr)
    table = table[["famille", "annee", "grandeur", "valeur", "etat", "tracee", "source", "page",
                   "lecture", "rupture", "remarque"]]
    table.columns = ["Famille", "Année", "Grandeur", "Millions de dinars courants", "État",
                     "Tracée", "Source", "Page", "Lecture", "Rupture", "Remarque"]
    return ([(None, fig_subvention())], table.reset_index(drop=True),
            {SUBV: _cles(d)}, "fig_compensation_eg_subvention")


# --- 4. Le gaz prélevé par la STEG, par source -----------------------------------------------

PARTIES_GAZ = (
    ("gaz_algerien_non_ventile", "Gaz algérien, redevance et achats non distingués (2001-2006)",
     GRIS, "\\\\"),
    ("redevance_consommee", "Redevance consommée sur le gaz algérien en transit", BRUN, ""),
    ("achats_contractuels", "Achats contractuels de gaz algérien", BLEU, ""),
    ("achats_additionnels", "Achats additionnels de gaz algérien", BLEU_CLAIR, "//"),
    ("miskar", "Gaz du champ de Miskar", VERT, ""),
    ("autres_gaz_national", "Autres champs nationaux", VIOLET, ""),
)


def fig_gaz_sources():
    figtools.apply_lang_font()
    d = figtools.series(GAZ)
    annees = sorted(int(a) for a in d["annee"].unique())
    fig, ax = plt.subplots(figsize=(10, 5.2))
    for a in annees:
        da = d[d["annee"] == a].set_index("source_gaz")
        total = float(da.loc["total_preleve", "valeur"])
        bas = 0.0
        for cle, etiquette, couleur, hachure in PARTIES_GAZ:
            if cle not in da.index:
                continue
            v = float(da.loc[cle, "valeur"])
            if v > 0:
                barre = ax.bar([a], [v], bottom=bas, width=0.74, color=couleur, hatch=hachure,
                               edgecolor="white", zorder=2)
                figtools.infobulle(barre[0], f"{a} · {etiquette} : {_nb(v, 0)} ktep "
                                             f"({da.loc[cle, 'source']}, {da.loc[cle, 'page']})")
            bas += v
        if bas != total:
            raise ValueError(f"gaz prélevé {a} : somme des parties {bas} ≠ total {total}")
        ax.annotate(_nb(total, 0), xy=(a, bas), xytext=(0, 2), textcoords="offset points",
                    ha="center", va="bottom", fontsize=6.5)
    _cadre(ax, "Milliers de tonnes équivalent pétrole (ktep, PCS)")
    ax.set_xticks(annees)
    ax.set_xticklabels([str(a) for a in annees], rotation=90, fontsize=7.5)
    ax.set_ylim(0, ax.get_ylim()[1] * 1.06)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    _legende(ax, [Patch(facecolor=c, hatch=h, edgecolor="white", label=figtools.fig_text(e))
                  for _, e, c, h in PARTIES_GAZ], ncol=2, y=-0.2)
    fig.tight_layout()
    return fig


def _figure_gaz_sources():
    d = figtools.series(GAZ)
    noms = {c: e for c, e, *_ in PARTIES_GAZ}
    noms.update({"total_preleve": "total des prélèvements (égal à la somme des parties)",
                 "total_des_achats_gaz": "total des achats de gaz (autre tableau, hors somme)"})
    ordre = {c: i for i, c in enumerate(list(noms))}
    table = d.assign(_o=d["source_gaz"].map(ordre)).sort_values(["annee", "_o"]).copy()
    table["source_gaz"] = table["source_gaz"].map(noms)
    table = table[["annee", "source_gaz", "valeur", "etat", "detail", "source", "page", "lecture",
                   "remarque"]]
    table.columns = ["Année", "Source du gaz", "ktep (PCS)", "État", "Lignes réunies", "Source",
                     "Page", "Lecture", "Remarque"]
    return ([(None, fig_gaz_sources())], table.reset_index(drop=True),
            {GAZ: _cles(d)}, "fig_compensation_eg_gaz_sources")


# --- 5. La facture des combustibles de la STEG en points de PIB : le pont -------------------

FAMILLE_EF = "etats_financiers_steg"
BASE_PIB = "base 2015"
ANNEES_PIB = tuple(range(2013, 2024))
PONTS = ((2013, 2016), (2016, 2022), (2022, 2023), (2013, 2023))
COUL_EFFET = {"prix": VERT, "quantite": BLEU, "pib": VIOLET}
HACHURE_EFFET = {"prix": "", "quantite": "//", "pib": "xx"}
GRIS_CLAIR = "#d0d7de"

SURCHARGES = {"gaz_pib": {
    PRIX: dict(
        perimetre=("« prix moyen annuel d'achat de la TEP gaz » des états financiers de la STEG, "
                   "exercices 2013 à 2023 : les achats de combustibles divisés par le total des "
                   "achats de gaz, toutes sources confondues"),
        caveats=("Le numérateur comprend le fuel et le gazole ; la quantité déduite de la facture "
                 "et du prix est donc le total des achats de gaz de la STEG, non une quantité de "
                 "gaz seul. Rupture de 2015 : fin du prix de cession. Dinars courants.")),
    FACTURE: dict(
        caveats=("La facture comprend le fuel et le gazole, elle n'est pas la facture du seul "
                 "gaz. 2016 est imprimé à l'unité. Pour 2017 les états financiers donnent trois "
                 "valeurs voisines (3 159,7 ; 3 160,6 ; 3 160,7) : le tableau en dinars exacts "
                 "est retenu. Rupture de 2015. Dinars courants.")),
    PIB: dict(
        base_pib="2015",
        perimetre=("PIB aux prix courants, base 2015, 2013-2023 : 2013 et 2014 rétropolés par "
                   "l'INS (classeur du 15 août 2021), 2015 à 2023 publiés dans les Comptes de la "
                   "nation"),
        caveats=("Une seule base sur toute la période, sans raccord. 2013 et 2014 sont des "
                 "valeurs rétropolées par l'INS ; voir l'annexe du site sur le PIB. Millions de "
                 "dinars courants.")),
}}


def _moyenne_log(a: float, b: float) -> float:
    """Moyenne logarithmique L(a, b) = (a − b) / (ln a − ln b), égale à a quand a = b."""
    return a if abs(a - b) < 1e-12 else (a - b) / (math.log(a) - math.log(b))


def donnees_pont() -> pd.DataFrame:
    """Entrées du calcul, une ligne par année 2013-2023, lues dans les séries — jamais recopiées.

    facture : millions de dinars courants ; prix : dinars par tep ; pib : millions de dinars
    courants (base 2015) ; quantite : ktep, déduite de la facture et du prix (le « total des
    achats de gaz » de la STEG, puisque le prix publié est la facture divisée par ce total) ;
    ratio : facture en points de PIB.
    """
    f = figtools.series(FACTURE)
    f = f[f["famille"] == FAMILLE_EF].set_index("annee")
    p = figtools.series(PRIX)
    p = p[p["famille"] == FAMILLE_EF].set_index("annee")
    y = figtools.series(PIB)
    y = y[y["base"] == BASE_PIB].set_index("annee")
    d = pd.DataFrame({"facture": f["valeur"], "prix": p["valeur"], "pib": y["pib_MD"]})
    d = d.loc[list(ANNEES_PIB)]
    if d.isna().any().any():
        raise ValueError(f"pont en points de PIB : valeur manquante\n{d[d.isna().any(axis=1)]}")
    d["quantite"] = d["facture"] / d["prix"] * 1000
    d["ratio"] = 100 * d["facture"] / d["pib"]
    return d


def effets_annuels(d: pd.DataFrame) -> pd.DataFrame:
    """Décomposition logarithmique (LMDI) de la variation annuelle du ratio facture / PIB.

    facture / PIB = prix × quantité / PIB. Pour chaque année t, avec L la moyenne logarithmique
    des ratios de t − 1 et de t : effet prix = L · ln(prix_t / prix_t−1), effet quantité =
    L · ln(quantité_t / quantité_t−1), effet PIB = − L · ln(PIB_t / PIB_t−1). La somme des
    trois égale exactement la variation du ratio, sans résidu."""
    lignes = {}
    annees = list(d.index)
    for a0, a1 in zip(annees[:-1], annees[1:]):
        L = _moyenne_log(d.at[a1, "ratio"], d.at[a0, "ratio"])
        lignes[a1] = {
            "prix": L * math.log(d.at[a1, "prix"] / d.at[a0, "prix"]),
            "quantite": L * math.log(d.at[a1, "quantite"] / d.at[a0, "quantite"]),
            "pib": -L * math.log(d.at[a1, "pib"] / d.at[a0, "pib"])}
    return pd.DataFrame.from_dict(lignes, orient="index")


def pont(d: pd.DataFrame, a: int, b: int) -> dict:
    """Pont de a à b : ratio de départ, effets (somme des effets annuels de a + 1 à b), ratio
    d'arrivée. Départ + effets = arrivée, à 1e-9 près."""
    e = effets_annuels(d).loc[a + 1:b].sum()
    return {"depart": float(d.at[a, "ratio"]), "prix": float(e["prix"]),
            "quantite": float(e["quantite"]), "pib": float(e["pib"]),
            "arrivee": float(d.at[b, "ratio"])}


def _signe(v: float) -> str:
    if abs(v) < 0.005:
        return _nb(0, 2)
    return ("+" if v > 0 else "−") + _nb(abs(v), 2)


def fig_gaz_pib():
    figtools.apply_lang_font()
    d = donnees_pont()
    rupt = figtools.series(FACTURE)
    rupt = rupt[(rupt["famille"] == FAMILLE_EF) & (rupt["rupture"].fillna("") != "")]
    fig, axs = plt.subplots(2, 2, figsize=(9.5, 7.6), sharey=True)
    noms = (("prix", "Effet\nprix", "effet prix"), ("quantite", "Effet\nquantité", "effet quantité"),
            ("pib", "Effet\nPIB", "effet PIB (dénominateur)"))
    for ax, (a, b) in zip(axs.flat, PONTS):
        c = pont(d, a, b)
        niveau = c["depart"]
        barre = ax.bar([0], [c["depart"]], width=0.62, color=GRIS_CLAIR, edgecolor=GRIS_FONCE,
                       lw=0.8, zorder=2)
        figtools.infobulle(barre[0], f"{a} · facture des combustibles : {_nb(c['depart'], 2)} points "
                                     f"de PIB ({_nb(d.at[a, 'facture'])} millions de dinars pour "
                                     f"{_nb(d.at[a, 'pib'])} de PIB)")
        ax.annotate(_nb(c["depart"], 2), xy=(0, c["depart"]), xytext=(0, 3),
                    textcoords="offset points", ha="center", fontsize=8)
        for i, (cle, _, etiquette) in enumerate(noms, start=1):
            e = c[cle]
            barre = ax.bar([i], [e], bottom=[niveau], width=0.62, color=COUL_EFFET[cle],
                           hatch=HACHURE_EFFET[cle], edgecolor="white", zorder=2)
            figtools.infobulle(barre[0], f"{a} → {b} · {etiquette} : {_signe(e)} point de PIB")
            ax.plot([i - 1 + 0.31, i - 0.31], [niveau, niveau], color=GRIS_FONCE, lw=0.6, zorder=1)
            ax.annotate(_signe(e), xy=(i, max(niveau, niveau + e)), xytext=(0, 3),
                        textcoords="offset points", ha="center", fontsize=8)
            niveau += e
        ax.plot([3 + 0.31, 4 - 0.31], [niveau, niveau], color=GRIS_FONCE, lw=0.6, zorder=1)
        if abs(niveau - c["arrivee"]) > 1e-9:
            raise ValueError(f"pont {a}-{b} : départ + effets {niveau} ≠ arrivée {c['arrivee']}")
        barre = ax.bar([4], [c["arrivee"]], width=0.62, color=GRIS_CLAIR, edgecolor=GRIS_FONCE,
                       lw=0.8, zorder=2)
        figtools.infobulle(barre[0], f"{b} · facture des combustibles : {_nb(c['arrivee'], 2)} points "
                                     f"de PIB ({_nb(d.at[b, 'facture'])} millions de dinars pour "
                                     f"{_nb(d.at[b, 'pib'])} de PIB)")
        ax.annotate(_nb(c["arrivee"], 2), xy=(4, c["arrivee"]), xytext=(0, 3),
                    textcoords="offset points", ha="center", fontsize=8)
        ax.set_xticks(range(5))
        ax.set_xticklabels([f"Facture\n{a}"] + [n for _, n, _ in noms] + [f"Facture\n{b}"],
                           fontsize=7.5)
        ax.set_title(f"{a} → {b}", fontsize=9.5, loc="left")
        ax.set_xlim(-0.6, 4.6)
        ax.set_ylim(0, 8.2)
        ax.grid(True, axis="y", alpha=0.3)
        ax.set_axisbelow(True)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
        for r in rupt.itertuples(index=False):
            if a < int(r.rupture_annee) <= b:
                m, = ax.plot([0.985], [1.03], marker=7, ms=6, color=GRIS_FONCE, clip_on=False,
                             zorder=4, transform=ax.transAxes, ls="none")
                figtools.infobulle(m, f"{int(r.rupture_annee)} · {r.rupture}")
    for ax in axs[:, 0]:
        ax.set_ylabel("Points de PIB")
    poignees = [Patch(facecolor=GRIS_CLAIR, edgecolor=GRIS_FONCE, label="facture des combustibles "
                                                                         "de la STEG, en % du PIB")]
    poignees += [Patch(facecolor=COUL_EFFET[k], hatch=HACHURE_EFFET[k], edgecolor="white",
                       label=figtools.fig_text(lab)) for k, lab in
                 (("prix", "effet prix (prix moyen d'achat)"),
                  ("quantite", "effet quantité (déduite de la facture et du prix)"),
                  ("pib", "effet PIB (croissance nominale, au dénominateur)"))]
    poignees.append(Line2D([0], [0], marker=7, color=GRIS_FONCE, ls="none", ms=6,
                           label="période qui contient la rupture de 2015 (infobulle)"))
    fig.tight_layout(rect=(0, 0.1, 1, 1))
    fig.legend(handles=poignees, loc="lower center", ncol=2, fontsize=7.5, frameon=False)
    return fig


def _figure_gaz_pib():
    d = donnees_pont()
    e = effets_annuels(d)
    f = figtools.series(FACTURE)
    f = f[f["famille"] == FAMILLE_EF].set_index("annee")
    p = figtools.series(PRIX)
    p = p[p["famille"] == FAMILLE_EF].set_index("annee")
    y = figtools.series(PIB)
    y = y[y["base"] == BASE_PIB].set_index("annee")
    lignes = []
    for a in d.index:
        lignes.append({
            "Période": str(a),
            "Facture des combustibles (millions de dinars)": d.at[a, "facture"],
            "Prix moyen d'achat (dinars par tep)": d.at[a, "prix"],
            "Quantité déduite (ktep)": round(d.at[a, "quantite"], 1),
            "PIB nominal, base 2015 (millions de dinars)": d.at[a, "pib"],
            "PIB rétropolé par l'INS": y.at[a, "retropole"],
            "Facture au départ (% du PIB)": None,
            "Facture en % du PIB": round(d.at[a, "ratio"], 4),
            "Effet prix (points de PIB)": round(e.at[a, "prix"], 4) if a in e.index else None,
            "Effet quantité (points de PIB)": round(e.at[a, "quantite"], 4) if a in e.index else None,
            "Effet PIB (points de PIB)": round(e.at[a, "pib"], 4) if a in e.index else None,
            "Source facture": f"{f.at[a, 'source']}, {f.at[a, 'page']}",
            "Source prix": f"{p.at[a, 'source']}, {p.at[a, 'page']}",
            "Source PIB": y.at[a, "publication"],
            "Rupture": f.at[a, "rupture"] or p.at[a, "rupture"] or ""})
    for a, b in PONTS:
        c = pont(d, a, b)
        lignes.append({
            "Période": f"{a} → {b} (pont)",
            "Facture au départ (% du PIB)": round(c["depart"], 4),
            "Facture en % du PIB": round(c["arrivee"], 4),
            "Effet prix (points de PIB)": round(c["prix"], 4),
            "Effet quantité (points de PIB)": round(c["quantite"], 4),
            "Effet PIB (points de PIB)": round(c["pib"], 4)})
    table = pd.DataFrame(lignes).fillna("")
    cles = {FACTURE: _cles(f.reset_index()), PRIX: _cles(p.reset_index()),
            PIB: ["ins-cnat-2015", "ins-pib-base-2015-2010-2020"]}
    return ([(None, fig_gaz_pib())], table, cles, "fig_compensation_eg_gaz_pib")



# --- 6. Le tarif de la moyenne tension, 1994-2022 -------------------------------------------------

# Un poste a une couleur ; la famille de postes (trois, quatre, quatre redéfinis) dit seulement où
# la courbe commence et finit. Aucune courbe ne traverse une rupture.
POSTES_MT = (
    ("jour", "jour", BLEU), ("pointe", "pointe", ROUGE), ("pointe_matin_ete", "pointe", ROUGE),
    ("soir", "soir", ORANGE), ("pointe_soir", "soir", ORANGE), ("nuit", "nuit", VERT),
)
NOM_POSTE_MT = {
    "jour": "jour", "pointe": "pointe", "soir": "soir", "nuit": "nuit",
    "pointe_matin_ete": "pointe du matin en été", "pointe_soir": "pointe du soir",
    "prix_unique": "prix unique", "prime_puissance": "prime de puissance"}
NOM_FAMILLE_MT = {"trois_postes": "trois postes", "quatre_postes": "quatre postes",
                  "quatre_postes_2014": "quatre postes redéfinis", "uniforme": "tarif uniforme"}
NOM_TARIF_MT = {"postes_horaires": "postes horaires", "uniforme": "uniforme",
                "secours": "secours"}
FIN_MT = 2023.0  # le 31 décembre 2022 : la dernière grille établie est celle du 1er octobre 2022


def _repere_date(ax, date, texte):
    """Trait vertical pointillé à la date d'effet et triangle porteur de l'infobulle."""
    x = figtools.abscisse_date(date)
    ax.axvline(x, color="#57606a", ls=(0, (2, 2)), lw=1, zorder=1)
    p, = ax.plot([x], [1], marker=7, ms=6, color=GRIS_FONCE, clip_on=False, zorder=5,
                 transform=ax.get_xaxis_transform())
    figtools.infobulle(p, texte)


def _courbe_escalier_mt(ax, d, nom, couleur, ls="-", lw=2.0, etiquette=True, constants=False):
    """Une courbe en escalier : un niveau par grille, du jour d'effet à la grille suivante.

    `d` : lignes d'une famille et d'un poste, triées par date. La grille suivante est celle de la
    série entière (`dates`) : un niveau sans valeur à la grille suivante s'arrête à elle et laisse
    un blanc, le trait ne se prolonge pas sur une valeur inconnue.

    `constants` : montants en monnaie de 2025 (calculés). Le point est la valeur de la grille à son
    année d'effet (indice annuel moyen de cette année) ; le niveau, lui, est ramené année par année,
    car une grille qui ne change pas perd de sa valeur réelle d'une année à l'autre.
    """
    dates = sorted(set(d.attrs["dates"]))
    lignes = list(d.itertuples(index=False))
    pts = []
    for i, r in enumerate(lignes):
        x = figtools.abscisse_date(r.date_effet)
        suivante = [t for t in dates if t > r.date_effet]
        fin = figtools.abscisse_date(suivante[0]) if suivante else FIN_MT
        if r.valeur != r.valeur:  # case vide : rien à tracer
            continue
        if i + 1 == len(lignes) and suivante:
            fin -= 0.4  # fin de famille : le trait s'arrête avant la rupture, il ne la traverse pas
        incertain = "" if r.jour_etabli == "oui" else " (jour d'effet non établi)"
        if constants:
            for a in range(int(x), math.ceil(fin)):
                ax.plot([max(x, a), min(fin, a + 1)], [r.valeur * _coeff(a)] * 2, color=couleur,
                        ls=ls, lw=lw, solid_capstyle="butt", zorder=3)
            coef = _coeff(int(x))
            y = r.valeur * coef
            texte = (f"{r.date_effet}{incertain} · {nom} : {_nb(y, 0)} millimes de 2025 par kWh, "
                     f"valeur calculée ({_nb(r.valeur, 0)} millimes courants × {_nb(coef, 3)} ; "
                     f"{r.portee} ; {r.source})")
        else:
            ax.plot([x, fin], [r.valeur, r.valeur], color=couleur, ls=ls, lw=lw,
                    solid_capstyle="butt", zorder=3)
            if i + 1 < len(lignes) and lignes[i + 1].valeur == lignes[i + 1].valeur \
                    and abs(figtools.abscisse_date(lignes[i + 1].date_effet) - fin) < 1e-9:
                ax.plot([fin, fin], [r.valeur, lignes[i + 1].valeur], color=couleur, lw=1.0,
                        zorder=2)
            y = r.valeur
            texte = (f"{r.date_effet}{incertain} · {nom} : {_nb(r.valeur, 0)} millimes par kWh "
                     f"({r.portee} ; {r.source})")
        p, = ax.plot([x], [y], "o", color=couleur, ms=4.5, zorder=4)
        figtools.infobulle(p, texte)
        pts.append((x, y))
    if etiquette and pts:
        for k in (0, -1):
            x, y = pts[k]
            ax.annotate(_nb(y, 0), xy=(x, y), xytext=(3, 4), textcoords="offset points",
                        fontsize=7, color=couleur)


def _donnees_mt():
    d = figtools.series(TARIFS_MT)
    d["date_effet"] = d["date_effet"].astype(str)
    return d


def _tracees_mt(d):
    """Les lignes tracées : tarif à postes horaires hors prime, et prix du tarif uniforme."""
    return d[((d["tarif"] == "postes_horaires") & (d["poste"] != "prime_puissance"))
             | ((d["tarif"] == "uniforme") & (d["poste"] == "prix_unique"))]


def fig_tarifs_mt(constants: bool = False):
    figtools.apply_lang_font()
    d = _donnees_mt()
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    dates = d[d["tarif"] == "postes_horaires"]["date_effet"].tolist()
    uni = d[(d["tarif"] == "uniforme") & (d["poste"] == "prix_unique")].sort_values("date_effet")
    uni.attrs["dates"] = dates
    _courbe_escalier_mt(ax, uni, "tarif uniforme", GRIS_FONCE, ls=(0, (4, 2)), lw=1.6,
                        etiquette=False, constants=constants)
    for fam in ("trois_postes", "quatre_postes", "quatre_postes_2014"):
        for poste, _, couleur in POSTES_MT:
            s = d[(d["tarif"] == "postes_horaires") & (d["famille"] == fam)
                  & (d["poste"] == poste)].sort_values("date_effet")
            if s.empty:
                continue
            s.attrs["dates"] = dates
            _courbe_escalier_mt(ax, s, f"{NOM_POSTE_MT[poste]} ({NOM_FAMILLE_MT[fam]})", couleur,
                                constants=constants)
    for r in d[d["rupture"].fillna("") != ""].drop_duplicates("date_effet").itertuples(index=False):
        _repere_date(ax, r.date_effet, f"{r.date_effet[:4]} · {r.rupture}")
    haut = 650 if constants else 450
    for nom, a, b in (("trois postes", "1994-06-01", "2000-08-15"),
                      ("quatre postes", "2000-08-15", "2014-05-01"),
                      ("quatre postes redéfinis", "2014-05-01", None)):
        x0 = figtools.abscisse_date(a)
        x1 = figtools.abscisse_date(b) if b else FIN_MT
        ax.annotate(figtools.fig_text(nom), xy=((x0 + x1) / 2, 0.985), xycoords=("data", "axes fraction"),
                    ha="center", va="top", fontsize=7.5, color=GRIS_FONCE)
    _cadre(ax, "Millimes de 2025 par kWh, hors taxes (calculés)" if constants
           else "Millimes courants par kWh, hors taxes")
    ax.set_xlim(1993.6, FIN_MT + 0.4)
    ax.set_xticks(range(1994, 2024, 2))
    ax.set_ylim(0, haut)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    poignees = [Line2D([0], [0], color=BLEU, lw=2, marker="o", ms=4.5, label=figtools.fig_text("Jour")),
                Line2D([0], [0], color=ROUGE, lw=2, marker="o", ms=4.5,
                       label=figtools.fig_text("Pointe (depuis 2014 : pointe du matin en été)")),
                Line2D([0], [0], color=ORANGE, lw=2, marker="o", ms=4.5,
                       label=figtools.fig_text("Soir (depuis 2014 : pointe du soir)")),
                Line2D([0], [0], color=VERT, lw=2, marker="o", ms=4.5,
                       label=figtools.fig_text("Nuit")),
                Line2D([0], [0], color=GRIS_FONCE, lw=1.6, ls=(0, (4, 2)),
                       label=figtools.fig_text("Tarif uniforme")),
                Line2D([0], [0], marker=7, color=GRIS_FONCE, ls="none", ms=6,
                       label=figtools.fig_text("rupture de série (infobulle sur le triangle)"))]
    _legende(ax, poignees, ncol=2, y=-0.14)
    fig.tight_layout()
    return fig


def _figure_tarifs_mt():
    d = _donnees_mt()
    tracee = _tracees_mt(d)
    d = d.assign(tracee=["oui" if i in tracee.index and v == v else "non"
                         for i, v in zip(d.index, d["valeur"])])
    d["coefficient_2025"] = [_coeff(int(a[:4])) for a in d["date_effet"]]
    d["valeur_2025"] = d["valeur"] * d["coefficient_2025"]
    table = d[["tarif", "famille", "poste", "date_effet", "jour_etabli", "valeur", "unite",
               "coefficient_2025", "valeur_2025", "etat", "tracee", "portee", "source", "page",
               "rupture", "remarque"]].copy()
    table["tarif"] = table["tarif"].map(NOM_TARIF_MT)
    table["famille"] = table["famille"].map(NOM_FAMILLE_MT)
    table["poste"] = table["poste"].map(NOM_POSTE_MT)
    table["etat"] = table["etat"].map({"lu": "lu", "non_etabli": "non établi"})
    table["coefficient_2025"] = table["coefficient_2025"].round(4)
    table["valeur_2025"] = table["valeur_2025"].round(1)
    table.columns = ["Tarif", "Famille de postes", "Poste", "Date d'effet", "Jour d'effet établi",
                     "Valeur courante", "Unité", "Coefficient de 2025 (calculé)",
                     "valeur_2025 : valeur en monnaie de 2025 (calculée)", "État", "Tracée",
                     "Portée", "Source", "Page", "Rupture", "Remarque"]
    vues = [("Millimes courants", fig_tarifs_mt()),
            ("Millimes de 2025 (calculés)", fig_tarifs_mt(constants=True))]
    return (vues, table.reset_index(drop=True),
            {TARIFS_MT: _cles(d.assign(cle=d["source"])),
             dinars_constants.SERIE_IPC: None, dinars_constants.SERIE_IPC_RECENT: None},
            "fig_compensation_eg_tarifs_mt")


# --- registre ---------------------------------------------------------------------------------

FIGURES = {
    "prix_achat_gaz": _figure_prix_achat_gaz,
    "cout_prix_kwh": _figure_cout_prix_kwh,
    "subvention": _figure_subvention,
    "gaz_sources": _figure_gaz_sources,
    "gaz_pib": _figure_gaz_pib,
    "tarifs_mt": _figure_tarifs_mt,
}
NON_MONETAIRES = {"gaz_sources", "tarifs_mt", "prix_achat_gaz"}


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure `nom` en onglets (graphique, données, sources).

    À appeler dans un chunk Quarto étiqueté `#| label: fig-…`, `#| output: asis`."""
    vues, table, cles, slug = FIGURES[nom]()
    for sid, liste in cles.items():
        _declarer(sid, liste, SURCHARGES.get(nom, {}).get(sid))
    figtools.figure_tabs(vues, table, *cles, slug=slug, caption=caption,
                         note_lecture=note_lecture, nominal=nom not in NON_MONETAIRES)
    plt.close("all")

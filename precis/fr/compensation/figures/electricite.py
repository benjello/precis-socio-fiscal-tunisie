"""Figures du chapitre « L'électricité et le gaz » (volume « La compensation »), longue période.

    from figures import electricite as el
    el.figure("prix_achat_gaz", caption=…, note_lecture=…)
    el.figure("cout_prix_kwh", caption=…, note_lecture=…)
    el.figure("subvention", caption=…, note_lecture=…)
    el.figure("gaz_sources", caption=…, note_lecture=…)
    el.figure("gaz_pib", caption=…, note_lecture=…)
    el.figure("tarifs_mt", caption=…, note_lecture=…)    # et tarifs_ht, tarifs_bt,
    el.figure("cout_prix_gaz", caption=…, note_lecture=…)  # tarifs_gaz_bp, tarifs_gaz_mp_hp

LES FIGURES DES TARIFS lisent des séries locales, versionnées dans `precis/_seriescache/` : la
transcription valeur par valeur des tableaux du chapitre, que chaque script compare aux tableaux.
Elles ne sont pas dans l'entrepôt : leur provenance est déclarée ici.

  - `steg-tarifs-moyenne-tension` (`scripts/serie_tarifs_mt.py`), 1975-2022 ;
  - `steg-tarifs-haute-tension` (`scripts/serie_tarifs_ht.py`), 1978-2022 ;
  - `steg-tarifs-basse-tension` (`scripts/serie_tarifs_bt.py`), ménages, 1970-2022 ;
  - `steg-tarifs-gaz` et `one-gaz-prix-cout` (`scripts/serie_tarifs_gaz.py`), gaz naturel par
    réseau, 1987-2022, et prix et coût du gaz selon l'Observatoire, 2017-2025.

Chaque tarif est tracé en escalier, en millimes courants et en millimes de 2025 (`_coeff`, règle
dans `_regle_2025`). Une « grille non établie » de la série arrête le niveau précédent : aucune
valeur n'est reconstituée sur la bande grise qui suit.

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
import textwrap
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
TARIFS_HT = "steg-tarifs-haute-tension"
TARIFS_BT = "steg-tarifs-basse-tension"
TARIFS_GAZ = "steg-tarifs-gaz"
GAZ_ONE = "one-gaz-prix-cout"
SERIES_LOCALES = (TARIFS_MT, TARIFS_HT, TARIFS_BT, TARIFS_GAZ, GAZ_ONE)
PARTS = "compensation-parts"  # dénominateurs : PIB et dépenses de l'État hors service de la dette

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
RESERVE_GRILLES = ("Une bande grise s'ouvre à une date de relèvement que donne une pièce du chapitre "
                   "(rapport annuel de la STEG, rapport extérieur, grille d'un autre niveau de "
                   "tension), pour ce niveau, pour l'ensemble des tarifs ou pour la basse tension, "
                   "sans que la grille de ce niveau soit établie : le niveau précédent s'arrête à cette date, aucune valeur n'est "
                   "reconstituée ; ces dates sont des lignes « grille non établie » de l'onglet "
                   "« Données », chacune avec sa pièce.")
PROVENANCE[TARIFS_MT] = dict(
    titre=("Le tarif de l'électricité en moyenne tension, 1975-2022 : prix du kilowattheure par "
           "poste horaire, tarif uniforme et tarif de secours, prime de puissance, à chaque date "
           "d'effet"),
    perimetre=("arrêtés et décision publiés au Journal officiel, du 20 avril 1975 au 1er août 1992 ; "
               "grilles de la moyenne tension de la STEG à chaque date d'effet : relais des "
               "agences publiques de promotion (FIPA, API) et tableau 6.2 de l'ESMAP pour juin 1994, "
               "août 2000, août 2001 et avril 2003 ; grilles de la STEG, pages archivées de son site "
               "et documents de l'entreprise, du 1er mai 2004 au 1er octobre 2022. Prix taxes "
               "comprises jusqu'en 1987, hors taxes à partir de 1991, en millimes courants par kWh ; "
               "prime en millimes par kW et par mois (par kVA pour le tarif uniforme de 1994 à 2003)"),
    caveats=("Rupture fiscale du 1er janvier 1991 : prix taxes comprises jusqu'en 1987, hors taxe sur "
             "la valeur ajoutée ensuite. Les valeurs de 1975 à 1990 viennent d'une première "
             "transcription des arrêtés ; seule la grille de 1992 est établie deux fois sur le texte ; "
             "l'unité de la prime de 1975 à 1982 reste à vérifier sur les textes. Le tarif uniforme "
             "de 1975 et de 1978 a deux tranches : il n'est pas tracé. "
             "Les familles de postes ne se raccordent pas : trois postes (1975 à août 2000), "
             "quatre postes (août 2000 à mai 2014), quatre postes redéfinis (depuis le 1er mai "
             "2014). Le jour du passage de trois à quatre postes n'est pas établi, ni le jour "
             "d'effet de la grille de juin 1994. Le soir et la nuit du tarif à postes horaires et "
             "du tarif de secours du 1er août 2001 ne sont pas donnés par la source. Le tarif de "
             "secours n'est pas relevé après 2003. Aucune grille postérieure au 1er octobre 2022 "
             "n'est établie. " + RESERVE_GRILLES),
    source_ligne=("arrêtés et décision publiés au Journal officiel, 1975-1992 ; relais des agences "
                  "publiques et de l'ESMAP, 1994-2003 ; grilles de la moyenne tension de la STEG, "
                  "2004-2022 (toutes les références : onglet « Sources »)"),
)
PROVENANCE[TARIFS_HT] = dict(
    titre=("Le tarif de l'électricité en haute tension, 1978-2022 : prix du kilowattheure par poste "
           "horaire, tarif de secours, prime de puissance, à chaque date d'effet"),
    perimetre=("arrêtés et décision publiés au Journal officiel, du 30 novembre 1978 au 1er août "
               "1992 ; relais des agences publiques (FIPA, API) et tableau 6.2 de l'ESMAP, 1994-2003 ; "
               "pages archivées du site de la STEG, 2004-2022. Prix taxes comprises jusqu'en 1987, "
               "hors taxes à partir de 1991, en millimes courants par kWh ; prime dans l'unité de "
               "chaque texte (dinars par kW et par an jusqu'en 1987, par mois en 1991 et 1992, "
               "millimes par kW et par mois ensuite)"),
    caveats=("Rupture fiscale du 1er janvier 1991. Les valeurs de 1978 à 1990 viennent d'une première "
             "transcription des arrêtés. De 2000 à 2003, deux tarifs généraux saisonniers valent la "
             "même année : quatre postes du 1er juin au 31 août, trois postes du 1er septembre au "
             "31 mai, d'après les pages de la FIPA ; l'ESMAP ne donne pas la saison. Les familles de "
             "postes ne se raccordent pas, et le sens des colonnes change le 1er mai 2014. La page de "
             "la haute tension datée du 1er juin 2019 porte les prix du 1er septembre 2018. Le tarif "
             "de secours n'est pas tracé. " + RESERVE_GRILLES),
    source_ligne=("arrêtés et décision publiés au Journal officiel, 1978-1992 ; relais des agences "
                  "publiques et de l'ESMAP, 1994-2003 ; grilles de la haute tension de la STEG, "
                  "2004-2022 (toutes les références : onglet « Sources »)"),
)
PROVENANCE[TARIFS_BT] = dict(
    titre=("Le tarif de l'électricité des ménages en basse tension, 1970-2022 : prix du kilowattheure "
           "par tranche, à chaque date d'effet"),
    perimetre=("arrêtés et décision publiés au Journal officiel, du 1er janvier 1970 au 1er août "
               "1992 ; pages des agences publiques qui relaient la grille de la STEG (FIPA, API), "
               "1994-2003 ; rapport de l'ESMAP (1993 et 2001) et de la Banque africaine de "
               "développement (1er juillet 2005) ; grilles de la STEG, 2004-2022. Prix taxes "
               "comprises jusqu'en 1987, hors taxe sur la valeur ajoutée à partir de 1991, en "
               "millimes courants par kWh ; redevance fixe et taxe au profit du Fonds de transition "
               "énergétique non comprises"),
    caveats=("Trois familles de sources, que la figure distingue par leur marque : officielle "
             "(Journal officiel, STEG), relais officiel (agence publique tunisienne qui reproduit la "
             "grille), extérieure (ESMAP, Banque africaine de développement). Rupture fiscale du "
             "1er janvier 1991. La structure du tarif change en 1975, 1978, 1981, 1984, 2006, 2014, "
             "2018 et 2022 : aucune courbe ne traverse ces dates, et une même couleur réunit des "
             "tranches qui ne sont pas définies de la même façon, comme le dit la légende. Le prix "
             "unique de l'éclairage de 1978 n'est pas établi. Le jour d'effet des grilles d'octobre "
             "1993 et de juin 1994 n'est pas établi. Pour la grille du 1er avril 2003, la page de la "
             "FIPA donne 94 pour la tranche normale, une page de la STEG non datée 90 : 94 est "
             "tracé. Le second prix des petits abonnés au-delà de 50 kWh (2006-2012) égale celui des "
             "autres abonnés de 1 à 300 kWh : il n'est pas tracé. " + RESERVE_GRILLES),
    source_ligne=("arrêtés et décision publiés au Journal officiel, 1970-1992 ; relais des agences "
                  "publiques, 1994-2003 ; ESMAP et Banque africaine de développement ; grilles de "
                  "la STEG, 2004-2022 (toutes les références : onglet « Sources »)"),
)
PROVENANCE[TARIFS_GAZ] = dict(
    titre=("Le tarif du gaz naturel de la STEG, 1987-2022 : basse pression, moyenne et haute "
           "pression, prix de la thermie par tranche ou par niveau de débit, à chaque date d'effet"),
    perimetre=("arrêtés et décision publiés au Journal officiel, du 16 juin 1987 au 1er août 1992 ; "
               "pages des agences publiques (FIPA, API) et étude de l'ANER, 1994-2003 ; grilles de "
               "la STEG, 2004-2022. Millimes courants par thermie, taxe à la production comprise en "
               "1987, hors taxes ensuite"),
    caveats=("Le prix de juin 1994 de la basse et de la moyenne pression (17,1 et 14 millimes) est "
             "relayé sans date d'effet ; il est rattaché à juin 1994 par un calcul, non par une "
             "lecture. La hausse de 1993 n'a pas de mois : le prix de 1992 est arrêté au 1er janvier "
             "1993, par convention. Les grilles de la basse pression de 2004 et de 2006, exprimées "
             "par mètre cube, et celles de septembre 2012 et de mars 2013 ne sont pas reprises ; "
             "celles de la moyenne pression de septembre 2012 et de mars 2013 ne sont pas établies. "
             "Jusqu'en avril 2014, le prix de la haute pression au-delà de son premier niveau, et "
             "jusqu'en 2008 celui de son premier niveau, est une formule indexée sur le fuel lourd : "
             "aucune valeur n'est tracée. À partir du 1er septembre 2018, les grilles de la basse "
             "pression distinguent les ménages. " + RESERVE_GRILLES),
    source_ligne=("arrêtés et décision publiés au Journal officiel, 1987-1992 ; relais des agences "
                  "publiques, 1994-2003 ; grilles de la STEG, 2004-2022 (toutes les références : "
                  "onglet « Sources »)"),
)
PROVENANCE[GAZ_ONE] = dict(
    titre=("Le prix de vente global hors taxes et le coût de revient du gaz naturel, 2017-2025, "
           "selon l'Observatoire national de l'énergie et des mines"),
    perimetre=("Chiffres clés de l'énergie, éditions 2018 à 2025 : prix de vente global hors taxes "
               "et coût de revient du gaz, en dinars courants par tonne équivalent pétrole"),
    caveats=("Données provisoires avant audit ; les éditions successives révisent certaines "
             "valeurs d'une décimale. Aucun coût de revient pour 2019, 2020 et 2021. L'Observatoire "
             "précise que l'écart entre le prix de vente et le coût de revient n'est pas forcément "
             "la subvention budgétaire."),
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


for _sid, _unite in ((TARIFS_MT, "millimes courants par kWh"),
                    (TARIFS_HT, "millimes courants par kWh"),
                    (TARIFS_BT, "millimes courants par kWh"),
                    (TARIFS_GAZ, "millimes courants par thermie"),
                    (GAZ_ONE, "dinars courants par tonne équivalent pétrole")):
    figtools.register_provenance(_sid, titre=PROVENANCE[_sid]["titre"],
                                 sources=["one-chiffres-cles-energie"] if _sid == GAZ_ONE else [],
                                 unite=_unite)
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
    if series_id in (*SERIES_LOCALES, PRIX, KWH) and "caveats" in champs:
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


def fig_cout_prix_kwh(constants: bool = False):
    figtools.apply_lang_font()
    d = _kwh_retenu().copy()
    if constants:
        d["coefficient_2025"] = [_coeff(a) for a in d["annee"]]
        d["valeur_courante"] = d["valeur"]
        d["valeur"] = d["valeur"] * d["coefficient_2025"]
    unite = "millimes de 2025 par kWh" if constants else "millimes par kWh"
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
                    f"{r.annee} · {t.lower()} · {e} : {_nb(r.valeur)} {unite}"
                    + (f", valeur calculée ({_nb(r.valeur_courante)} millimes courants × "
                       f"{_nb(r.coefficient_2025, 3)})" if constants else "")
                    + f" ({r.source}, {r.page} ; {r.etat})"))
        ax.set_title(figtools.fig_text(titre), fontsize=9, loc="left")
        ax.grid(True, axis="y", alpha=0.3)
        ax.set_axisbelow(True)
        ax.set_ylabel("Millimes de 2025 par kWh (calculés)" if constants
                      else "Millimes courants par kWh")
        for r in d[(d["rupture"].fillna("") != "")].head(1).itertuples(index=False):
            figtools.marque_rupture(ax, int(r.rupture_annee))
            if ax is axc:
                _repere(ax, int(r.rupture_annee), f"{int(r.rupture_annee)} · {r.rupture}")
    for a0, a1 in SANS_COUT:
        axc.axvspan(a0, a1, color="#d0d7de", alpha=0.55, lw=0, zorder=0)
        axc.annotate("aucun coût publié", xy=((a0 + a1) / 2, 0.5), xycoords=("data", "axes fraction"),
                     ha="center", va="center", rotation=90, fontsize=6.5, color=GRIS_FONCE)
    axp.set_xlabel("Année")
    axp.set_xlim(1993.3, 2025.7)
    axp.set_xticks(range(1994, 2026, 2))
    axp.set_ylim(0, 520 if not constants else 50 * math.ceil(d["valeur"].max() * 1.08 / 50))
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
    table["coefficient_2025"] = [round(_coeff(a), 4) for a in table["annee"]]
    table["valeur_2025"] = (table["valeur"] * table["annee"].map(_coeff)).round(1)
    table["famille"] = table["famille"].map(noms)
    table["grandeur"] = table["grandeur"].map(gr)
    table = table[["famille", "annee", "grandeur", "valeur", "coefficient_2025", "valeur_2025",
                   "etat", "tracee", "source", "page", "lecture", "rupture", "remarque"]]
    table.columns = ["Famille", "Année", "Grandeur", "Millimes courants par kWh",
                     "Coefficient de 2025 (calculé)",
                     "valeur_2025 : millimes de 2025 par kWh (calculée)", "État",
                     "Tracée", "Source", "Page", "Lecture", "Rupture", "Remarque"]
    vues = [("Millimes courants", fig_cout_prix_kwh()),
            ("Millimes de 2025 (calculés)", fig_cout_prix_kwh(constants=True))]
    return (vues, table.reset_index(drop=True),
            {KWH: _cles(d), dinars_constants.SERIE_IPC: None,
             dinars_constants.SERIE_IPC_RECENT: None}, "fig_compensation_eg_cout_prix_kwh")


# --- 3. La subvention d'exploitation de la STEG ----------------------------------------------

MESURES_SUBV = {
    "md": ("Millions de dinars courants", None),
    "pib": ("% du PIB", "pib_MDT"),
    "dep": ("% des dépenses de l'État hors service de la dette", "depenses_etat_hors_dette_MDT"),
}


def _denominateurs(colonne: str) -> dict[int, float]:
    """Dénominateur par année, lu dans la série `compensation-parts` du livre : une valeur par
    année, la même sur toutes ses lignes."""
    d = figtools.series(PARTS)
    d = d[d[colonne].notna()].groupby("annee")[colonne].first()
    return {int(a): float(v) for a, v in d.items()}


def fig_subvention(mesure: str = "md"):
    figtools.apply_lang_font()
    d = figtools.series(SUBV)
    ylabel, colonne = MESURES_SUBV[mesure]
    den = _denominateurs(colonne) if colonne else None
    dec = 0 if den is None else 2
    d = d.copy()
    if den is not None:
        d["valeur"] = [v * 100 / den[int(a)] for v, a in zip(d["valeur"], d["annee"])]
    unite = "millions de dinars" if den is None else ("% du PIB" if mesure == "pib"
                                                      else "% des dépenses de l'État")
    comptes = d[d["grandeur"] == "subvention_exploitation"].sort_values("annee")
    cg = d[d["famille"] == "rapport_de_controle_2014"].pivot(index="annee", columns="grandeur",
                                                             values="valeur")
    fig, ax = plt.subplots(figsize=(9.5, 4.9))
    for a, v in cg.iterrows():
        barre = ax.bar([a], [v["soutien_direct"]], width=0.62, color=BLEU, hatch="//",
                       edgecolor="white", zorder=2)
        figtools.infobulle(barre[0], f"{a} · soutien direct (rapport de contrôle de 2014) : "
                                     f"{_nb(v['soutien_direct'], 2 if den else 1)} {unite}")
        barre = ax.bar([a], [v["soutien_indirect"]], bottom=[v["soutien_direct"]], width=0.62,
                       color=ORANGE, edgecolor="white", zorder=2)
        figtools.infobulle(barre[0], f"{a} · soutien indirect (rapport de contrôle de 2014) : "
                                     f"{_nb(v['soutien_indirect'], 2 if den else 1)} {unite}")
    ax.plot(comptes["annee"], comptes["valeur"], color=NOIR, lw=1.2, zorder=3)
    for r in comptes.itertuples(index=False):
        p, = ax.plot([r.annee], [r.valeur], marker="o", ms=6, color=NOIR, ls="none", zorder=4)
        figtools.infobulle(p, f"{r.annee} · subvention d'exploitation des comptes de la STEG : "
                              f"{_nb(r.valeur, 2 if den else 1)} {unite} ({r.source}, {r.page})")
        ax.annotate(_v(r.valeur) if den is None else _nb(r.valeur, 2), xy=(r.annee, r.valeur),
                    xytext=(0, 7),
                    textcoords="offset points", ha="center", fontsize=7)
    for r in comptes[comptes["rupture"].fillna("") != ""].itertuples(index=False):
        _repere(ax, int(r.rupture_annee), f"{int(r.rupture_annee)} · {r.rupture}")
    if mesure == "pib":
        _repere(ax, 2010, "2010 · PIB : base 1997 → base 2015")
    _cadre(ax, ylabel)
    ax.set_xticks(range(2006, 2017))
    ax.set_xlim(2005.4, 2016.6)
    ax.set_ylim(0, ax.get_ylim()[1] * 1.08)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0 if den is None else 1)))
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
    for mesure, colonne, nom in (("pib", "pib_MDT", "Subvention d'exploitation, % du PIB"),
                                 ("dep", "depenses_etat_hors_dette_MDT",
                                  "Subvention d'exploitation, % des dépenses de l'État")):
        den = _denominateurs(colonne)
        table[nom] = [round(100 * v / den[int(a)], 3) if int(a) in den else None
                      for v, a in zip(table["Millions de dinars courants"], table["Année"])]
    vues = [(MESURES_SUBV[m][0], fig_subvention(m)) for m in ("md", "pib", "dep")]
    return (vues, table.reset_index(drop=True),
            {SUBV: _cles(d), PARTS: None},
            "fig_compensation_eg_subvention")


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



# --- 6. Les tarifs, grille par grille : moyenne et haute tension, ménages, gaz ------------------

# Un poste a une couleur ; la famille de postes (trois, quatre, quatre redéfinis) dit seulement où
# la courbe commence et finit. Aucune courbe ne traverse une rupture.
POSTES_MT = (
    ("jour", "jour", BLEU), ("pointe", "pointe", ROUGE), ("pointe_matin_ete", "pointe", ROUGE),
    ("soir", "soir", ORANGE), ("pointe_soir", "soir", ORANGE), ("nuit", "nuit", VERT),
)
NOM_POSTE_MT = {
    "jour": "jour", "pointe": "pointe", "soir": "soir", "nuit": "nuit",
    "pointe_matin_ete": "pointe du matin en été", "pointe_soir": "pointe du soir",
    "prix_unique": "prix unique", "prime_puissance": "prime de puissance",
    "premiere_tranche": "première tranche", "seconde_tranche": "seconde tranche",
    "grille_non_etablie": "grille non établie"}
NOM_FAMILLE_MT = {"trois_postes": "trois postes", "quatre_postes": "quatre postes",
                  "quatre_postes_2014": "quatre postes redéfinis", "uniforme": "tarif uniforme",
                  "uniforme_deux_tranches": "tarif uniforme à deux tranches",
                  "trois_postes_saison": "trois postes, du 1er septembre au 31 mai",
                  "quatre_postes_ete": "quatre postes, du 1er juin au 31 août"}
NOM_TARIF_MT = {"postes_horaires": "postes horaires", "uniforme": "uniforme",
                "secours": "secours", "general": "général"}
NOM_ETAT = {"lu": "lu", "non_etabli": "non établi", "grille_non_etablie": "grille non établie",
            "formule": "formule"}
FIN_MT = 2023.0  # le 31 décembre 2022 : la dernière grille établie est de 2022
COUPE = 0.15  # un trait s'arrête un peu avant une rupture, qu'il ne traverse pas
GRIS_BANDE = "#d0d7de"


def _nbv(v) -> str:
    """Un prix tel que la grille le donne : 47 ; 11,3 ; 22,09."""
    v = float(v)
    for dec in (0, 1, 2):
        if abs(round(v, dec) - v) < 1e-9:
            return _nb(v, dec)
    return _nb(v, 3)


def _base_fiscale(unite) -> str:
    """« millimes courants par kWh, taxes comprises » -> « taxes comprises »."""
    u = unite if isinstance(unite, str) else ""
    return u.split(", ", 1)[1] if ", " in u else ""


def _repere_date(ax, date, texte):
    """Trait vertical pointillé à la date d'effet et triangle porteur de l'infobulle."""
    x = figtools.abscisse_date(date)
    ax.axvline(x, color="#57606a", ls=(0, (2, 2)), lw=1, zorder=1)
    p, = ax.plot([x], [1], marker=7, ms=6, color=GRIS_FONCE, clip_on=False, zorder=5,
                 transform=ax.get_xaxis_transform())
    figtools.infobulle(p, texte)


def _reperes(ax, d):
    """Un repère par date de rupture de la série (colonne `rupture`)."""
    r = d[d["rupture"].fillna("") != ""].drop_duplicates("date_effet")
    for x in r.itertuples(index=False):
        _repere_date(ax, x.date_effet, f"{x.date_effet[:4]} · {x.rupture}")


def _coupures(d) -> set[str]:
    return set(d[d["rupture"].fillna("") != ""]["date_effet"])


def _bandes(ax, d, fin=FIN_MT):
    """Bande grise d'une date sans aucune valeur établie (grille non établie, ou prix dont le
    niveau n'est pas établi) à la grille suivante : aucune valeur n'y est reconstituée."""
    avec = d["valeur"].notna() | (d.get("etat", pd.Series("", index=d.index)) == "formule")
    pleines = sorted(set(d[avec]["date_effet"]))
    vides = sorted(set(d["date_effet"]) - set(pleines))
    intervalles: dict[float, float] = {}  # fin -> début : deux dates vides qui se suivent, une bande
    for g in vides:
        suite = [t for t in pleines if t > g]
        x1 = figtools.abscisse_date(suite[0]) if suite else fin
        x0 = figtools.abscisse_date(g)
        intervalles[x1] = min(x0, intervalles.get(x1, x0))
    for x1, x0 in intervalles.items():
        ax.axvspan(x0, x1, color=GRIS_BANDE, alpha=0.5, lw=0, zorder=0)
    return bool(vides)


def _courbe_escalier(ax, d, nom, couleur, ls="-", lw=2.0, etiquette=True, constants=False, *,
                     grandeur="kWh", fin_serie=FIN_MT, coupures=(), marque=None, dec_c=0):
    """Une courbe en escalier : un niveau par grille, du jour d'effet à la grille suivante.

    `d` : lignes d'une famille et d'un poste, triées par date ; `d.attrs["dates"]` : toutes les
    dates de la série, grilles non établies comprises. Un niveau s'arrête à la date suivante de la
    série : sans valeur à cette date, il laisse un blanc, le trait ne se prolonge pas sur une
    valeur inconnue. `coupures` : dates de rupture, que le trait ne traverse pas.

    `constants` : montants en monnaie de 2025 (calculés). Le point est la valeur de la grille à son
    année d'effet (indice annuel moyen de cette année) ; le niveau, lui, est ramené année par année,
    car une grille qui ne change pas perd de sa valeur réelle d'une année à l'autre.

    `marque` : ligne -> (marqueur, plein) ; distingue les familles de sources.
    """
    dates = sorted(set(d.attrs["dates"]))
    coupures = set(coupures)
    lignes = list(d.itertuples(index=False))
    pts = []
    for i, r in enumerate(lignes):
        if r.valeur != r.valeur:  # case vide : rien à tracer
            continue
        x = figtools.abscisse_date(r.date_effet)
        suivante = [t for t in dates if t > r.date_effet]
        fin = figtools.abscisse_date(suivante[0]) if suivante else fin_serie
        coupe = bool(suivante) and (suivante[0] in coupures or i + 1 == len(lignes))
        if coupe:
            fin -= COUPE
        incertain = "" if r.jour_etabli == "oui" else " (jour d'effet non établi)"
        fiscal = _base_fiscale(getattr(r, "unite", ""))
        fiscal = f", {fiscal}" if fiscal else ""
        remarque = getattr(r, "remarque", "")
        remarque = f" — {remarque}" if isinstance(remarque, str) and remarque else ""
        if constants:
            for a in range(int(x), math.ceil(fin)):
                ax.plot([max(x, a), min(fin, a + 1)], [r.valeur * _coeff(a)] * 2, color=couleur,
                        ls=ls, lw=lw, solid_capstyle="butt", zorder=3)
            coef = _coeff(int(x))
            y = r.valeur * coef
            texte = (f"{r.date_effet}{incertain} · {nom} : {_nb(y, dec_c)} millimes de 2025 par "
                     f"{grandeur}{fiscal}, valeur calculée ({_nbv(r.valeur)} millimes courants × "
                     f"{_nb(coef, 3)} ; {r.portee} ; {r.source}){remarque}")
        else:
            ax.plot([x, fin], [r.valeur, r.valeur], color=couleur, ls=ls, lw=lw,
                    solid_capstyle="butt", zorder=3)
            nxt = lignes[i + 1] if i + 1 < len(lignes) else None
            if not coupe and nxt is not None and nxt.valeur == nxt.valeur \
                    and abs(figtools.abscisse_date(nxt.date_effet) - fin) < 1e-9:
                ax.plot([fin, fin], [r.valeur, nxt.valeur], color=couleur, lw=1.0, zorder=2)
            y = r.valeur
            texte = (f"{r.date_effet}{incertain} · {nom} : {_nbv(r.valeur)} millimes par "
                     f"{grandeur}{fiscal} ({r.portee} ; {r.source}){remarque}")
        m, plein = marque(r) if marque else ("o", True)
        p, = ax.plot([x], [y], m, color=couleur, mfc=couleur if plein else "white", mew=1.2,
                     ms=4.5 if plein else 5, zorder=4)
        figtools.infobulle(p, texte)
        pts.append((x, y))
    if etiquette and pts:
        for k in (0, -1):
            x, y = pts[k]
            ax.annotate(_nb(y, dec_c) if constants else _nbv(y), xy=(x, y), xytext=(3, 4),
                        textcoords="offset points", fontsize=7, color=couleur)
    return pts


_courbe_escalier_mt = _courbe_escalier


def _poignees_bandes_reperes(bandes: bool) -> list:
    p = []
    if bandes:
        p.append(Patch(facecolor=GRIS_BANDE, alpha=0.5,
                       label=figtools.fig_text("période sans grille établie : aucune valeur "
                                               "reconstituée")))
    p.append(Line2D([0], [0], marker=7, color=GRIS_FONCE, ls="none", ms=6,
                    label=figtools.fig_text("rupture de série (infobulle sur le triangle)")))
    return p


def _fiscal(ax, x_rupture: float, debut: float, fin: float):
    """Les deux bases fiscales, écrites sous le titre des familles."""
    for texte, a, b in (("taxes comprises", debut, x_rupture), ("hors taxes", x_rupture, fin)):
        ax.annotate(figtools.fig_text(texte), xy=((a + b) / 2, 0.93),
                    xycoords=("data", "axes fraction"), ha="center", va="top", fontsize=7,
                    color=GRIS_FONCE, style="italic")


def _familles(ax, familles):
    for nom, a, b in familles:
        x0 = figtools.abscisse_date(a)
        x1 = figtools.abscisse_date(b) if b else FIN_MT
        ax.annotate(figtools.fig_text(nom), xy=((x0 + x1) / 2, 0.985),
                    xycoords=("data", "axes fraction"), ha="center", va="top", fontsize=7.5,
                    color=GRIS_FONCE)


def _haut(courbes_pts, pas=50) -> float:
    ys = [y for pts in courbes_pts for _, y in pts]
    return pas * math.ceil(max(ys) * 1.18 / pas)


def _table_tarifs(d, tracee, colonnes, noms, renomme):
    """Table « Données » d'une série de tarifs : valeur courante, coefficient et valeur de 2025."""
    d = d.assign(tracee=["oui" if i in tracee.index and v == v else "non"
                         for i, v in zip(d.index, d["valeur"])])
    d["coefficient_2025"] = [_coeff(int(a[:4])) for a in d["date_effet"]]
    d["valeur_2025"] = pd.to_numeric(d["valeur"], errors="coerce") * d["coefficient_2025"]
    table = d[colonnes].copy()
    for col, mapping in renomme.items():
        table[col] = table[col].map(lambda v, m=mapping: m.get(v, v))
    table["coefficient_2025"] = table["coefficient_2025"].round(4)
    table["valeur_2025"] = table["valeur_2025"].round(1)
    table.columns = noms
    return table.reset_index(drop=True)


def _vues(fonction):
    return [("Millimes courants", fonction()), ("Millimes de 2025 (calculés)", fonction(constants=True))]


def _cles_ipc(series_id, d):
    return {series_id: _cles(d.assign(cle=d["source"])),
            dinars_constants.SERIE_IPC: None, dinars_constants.SERIE_IPC_RECENT: None}


# --- 6a. La moyenne tension, 1975-2022 ---------------------------------------------------------

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
    fig, ax = plt.subplots(figsize=(10, 5.6))
    ph = d[d["tarif"] == "postes_horaires"]
    dates = ph["date_effet"].tolist()
    bandes = _bandes(ax, ph)
    coupures = _coupures(d)
    tous = []
    uni = d[(d["tarif"] == "uniforme") & (d["poste"] == "prix_unique")].sort_values("date_effet")
    uni.attrs["dates"] = dates
    tous.append(_courbe_escalier(ax, uni, "tarif uniforme", GRIS_FONCE, ls=(0, (4, 2)), lw=1.6,
                                 etiquette=False, constants=constants,
                                 coupures={"1991-01-01"}))
    for fam in ("trois_postes", "quatre_postes", "quatre_postes_2014"):
        for poste, _, couleur in POSTES_MT:
            s = ph[(ph["famille"] == fam) & (ph["poste"] == poste)].sort_values("date_effet")
            if s.empty:
                continue
            s.attrs["dates"] = dates
            tous.append(_courbe_escalier(ax, s, f"{NOM_POSTE_MT[poste]} ({NOM_FAMILLE_MT[fam]})",
                                         couleur, constants=constants, coupures=coupures))
    _reperes(ax, d)
    _familles(ax, (("trois postes", "1975-04-20", "2000-08-15"),
                   ("quatre postes", "2000-08-15", "2014-05-01"),
                   ("quatre postes redéfinis", "2014-05-01", None)))
    _fiscal(ax, figtools.abscisse_date("1991-01-01"), 1975.3, FIN_MT)
    _cadre(ax, "Millimes de 2025 par kWh (calculés)" if constants
           else "Millimes courants par kWh")
    ax.set_xlim(1974.6, FIN_MT + 0.4)
    ax.set_xticks(range(1975, 2024, 3))
    ax.set_ylim(0, _haut(tous))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    poignees = [Line2D([0], [0], color=BLEU, lw=2, marker="o", ms=4.5, label=figtools.fig_text("Jour")),
                Line2D([0], [0], color=ROUGE, lw=2, marker="o", ms=4.5,
                       label=figtools.fig_text("Pointe (depuis 2014 : pointe du matin en été)")),
                Line2D([0], [0], color=ORANGE, lw=2, marker="o", ms=4.5,
                       label=figtools.fig_text("Soir (depuis 2014 : pointe du soir)")),
                Line2D([0], [0], color=VERT, lw=2, marker="o", ms=4.5,
                       label=figtools.fig_text("Nuit")),
                Line2D([0], [0], color=GRIS_FONCE, lw=1.6, ls=(0, (4, 2)),
                       label=figtools.fig_text("Tarif uniforme (prix unique, depuis 1981)"))]
    _legende(ax, poignees + _poignees_bandes_reperes(bandes), ncol=2, y=-0.13)
    fig.tight_layout()
    return fig


def _figure_tarifs_mt():
    d = _donnees_mt()
    table = _table_tarifs(
        d, _tracees_mt(d),
        ["tarif", "famille", "poste", "date_effet", "jour_etabli", "valeur", "unite",
         "coefficient_2025", "valeur_2025", "etat", "tracee", "portee", "source", "page",
         "rupture", "remarque"],
        ["Tarif", "Famille de postes", "Poste", "Date d'effet", "Jour d'effet établi",
         "Valeur courante", "Unité", "Coefficient de 2025 (calculé)",
         "valeur_2025 : valeur en monnaie de 2025 (calculée)", "État", "Tracée",
         "Portée", "Source", "Page", "Rupture", "Remarque"],
        {"tarif": NOM_TARIF_MT, "famille": NOM_FAMILLE_MT, "poste": NOM_POSTE_MT, "etat": NOM_ETAT})
    return (_vues(fig_tarifs_mt), table, _cles_ipc(TARIFS_MT, d), "fig_compensation_eg_tarifs_mt")


# --- 6b. La haute tension, 1978-2022 -----------------------------------------------------------

FAMILLES_HT = (("trois_postes", "-"), ("trois_postes_saison", "-"), ("quatre_postes_ete", (0, (3, 1.5))),
               ("quatre_postes", "-"), ("quatre_postes_2014", "-"))


def _donnees_ht():
    d = figtools.series(TARIFS_HT)
    d["date_effet"] = d["date_effet"].astype(str)
    return d


def _tracees_ht(d):
    return d[(d["tarif"] == "general") & ~d["poste"].isin(["prime_puissance", "grille_non_etablie"])]


def fig_tarifs_ht(constants: bool = False):
    figtools.apply_lang_font()
    d = _donnees_ht()
    fig, ax = plt.subplots(figsize=(10, 5.6))
    g = d[d["tarif"] == "general"]
    dates = g["date_effet"].tolist()
    bandes = _bandes(ax, g)
    coupures = _coupures(d)
    tous = []
    for fam, ls in FAMILLES_HT:
        for poste, _, couleur in POSTES_MT:
            s = g[(g["famille"] == fam) & (g["poste"] == poste)].sort_values("date_effet")
            if s.empty:
                continue
            s.attrs["dates"] = dates
            tous.append(_courbe_escalier(ax, s, f"{NOM_POSTE_MT[poste]} ({NOM_FAMILLE_MT[fam]})",
                                         couleur, ls=ls, constants=constants, coupures=coupures,
                                         etiquette=fam not in ("trois_postes_saison",
                                                               "quatre_postes_ete")))
    _reperes(ax, d)
    _familles(ax, (("trois postes", "1978-11-30", "2000-08-15"),
                   ("deux tarifs saisonniers", "2000-08-15", "2004-05-01"),
                   ("quatre postes", "2004-05-01", "2014-05-01"),
                   ("quatre postes redéfinis", "2014-05-01", None)))
    _fiscal(ax, figtools.abscisse_date("1991-01-01"), 1978.6, FIN_MT)
    _cadre(ax, "Millimes de 2025 par kWh (calculés)" if constants
           else "Millimes courants par kWh")
    ax.set_xlim(1977.9, FIN_MT + 0.4)
    ax.set_xticks(range(1978, 2024, 3))
    ax.set_ylim(0, _haut(tous))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    poignees = [Line2D([0], [0], color=BLEU, lw=2, marker="o", ms=4.5, label=figtools.fig_text("Jour")),
                Line2D([0], [0], color=ROUGE, lw=2, marker="o", ms=4.5,
                       label=figtools.fig_text("Pointe (depuis 2014 : pointe du matin en été)")),
                Line2D([0], [0], color=ORANGE, lw=2, marker="o", ms=4.5,
                       label=figtools.fig_text("Soir (depuis 2014 : pointe du soir)")),
                Line2D([0], [0], color=VERT, lw=2, marker="o", ms=4.5,
                       label=figtools.fig_text("Nuit")),
                Line2D([0], [0], color=GRIS_FONCE, lw=2, ls=(0, (3, 1.5)),
                       label=figtools.fig_text("2000-2003 : tarif d'été, quatre postes, du 1er juin "
                                               "au 31 août (trait tireté)"))]
    _legende(ax, poignees + _poignees_bandes_reperes(bandes), ncol=2, y=-0.13)
    fig.tight_layout()
    return fig


def _figure_tarifs_ht():
    d = _donnees_ht()
    table = _table_tarifs(
        d, _tracees_ht(d),
        ["tarif", "famille", "poste", "date_effet", "jour_etabli", "valeur", "unite",
         "coefficient_2025", "valeur_2025", "etat", "tracee", "portee", "source", "page",
         "rupture", "remarque"],
        ["Tarif", "Famille de postes", "Poste", "Date d'effet", "Jour d'effet établi",
         "Valeur courante", "Unité", "Coefficient de 2025 (calculé)",
         "valeur_2025 : valeur en monnaie de 2025 (calculée)", "État", "Tracée",
         "Portée", "Source", "Page", "Rupture", "Remarque"],
        {"tarif": NOM_TARIF_MT, "famille": NOM_FAMILLE_MT, "poste": NOM_POSTE_MT, "etat": NOM_ETAT})
    return (_vues(fig_tarifs_ht), table, _cles_ipc(TARIFS_HT, d), "fig_compensation_eg_tarifs_ht")


# --- 6c. Les ménages en basse tension, 1970-2022 ------------------------------------------------

MARQUES_BT = {"officielle": ("o", True), "relais officiel": ("s", False), "extérieure": ("^", False)}
COURBES_BT = (  # (tranches, couleur, trait, épaisseur, étiquetée, légende)
    (("degressif_1", "degressif_kva_1", "eclairage_unique", "prix_unique", "economique"), BLEU, "-",
     2.2, True, "Premier prix : première tranche du tarif dégressif (1970-1978), prix unique "
                "(1981-1984), puis tranche économique, jusqu'à 50 kWh par mois (depuis 1984)"),
    (("degressif_4", "degressif_kva_2"), BLEU_CLAIR, "-", 1.6, False,
     "Dernière tranche du tarif dégressif (1970-1978)"),
    (("normale", "autres_1_300", "fort_1_200"), ROUGE, "-", 2.2, True,
     "Tranche normale (1984-2005), puis autres abonnés de 1 à 300 kWh (2006-2014), puis forte "
     "consommation, de 1 à 200 kWh (depuis 2014)"),
    (("petits_51_a",), GRIS_FONCE, (0, (3, 2)), 1.5, False,
     "Petits abonnés au-delà de 50 kWh, premier prix (2006-2014)"),
    (("autres_301",), ORANGE, "-", 1.8, False, "Autres abonnés, 301 kWh et plus (2006-2014)"),
    (("t_51_100",), TEAL, "-", 1.6, False, "De 51 à 100 kWh (depuis 2014)"),
    (("t_101_200_unique",), ROSE, "-", 1.6, False,
     "De 101 à 200 kWh, prix unique sur toute la consommation (2014-2018)"),
    (("fort_201_300",), BRUN, "-", 1.6, False, "Forte consommation, de 201 à 300 kWh (depuis 2014)"),
    (("fort_301_500",), VIOLET, "-", 1.6, False, "Forte consommation, de 301 à 500 kWh (depuis 2014)"),
    (("fort_501",), NOIR, "-", 1.6, True, "Forte consommation, plus de 500 kWh (depuis 2014)"),
)


def _donnees_bt():
    d = figtools.series(TARIFS_BT)
    d["date_effet"] = d["date_effet"].astype(str)
    return d


def _tracees_bt(d):
    tranches = {t for c in COURBES_BT for t in c[0]}
    return d[d["tranche"].isin(tranches)]


def fig_tarifs_bt(constants: bool = False):
    figtools.apply_lang_font()
    d = _donnees_bt()
    fig, ax = plt.subplots(figsize=(10, 6.4))
    dates = d["date_effet"].tolist()
    bandes = _bandes(ax, d)
    coupures = _coupures(d)
    tous = []
    for tranches, couleur, ls, lw, etiq, _ in COURBES_BT:
        pts = []
        for tranche in tranches:
            sous = d[d["tranche"] == tranche]
            for structure in dict.fromkeys(sous["structure"]):
                s = sous[sous["structure"] == structure].sort_values("date_effet")
                s.attrs["dates"] = dates
                pts += _courbe_escalier(ax, s, bt_nom(tranche), couleur, ls=ls, lw=lw,
                                        etiquette=False, constants=constants, coupures=coupures,
                                        marque=lambda r: MARQUES_BT[r.famille_source])
        tous.append(pts)
        if etiq and pts:
            for (x, y), dx, ha in ((pts[0], -4, "right"), (pts[-1], 5, "left")):
                ax.annotate(_nb(y, 0) if constants else _nbv(y), xy=(x, y), xytext=(dx, 0),
                            textcoords="offset points", ha=ha, va="center", fontsize=7,
                            color=couleur)
    _reperes(ax, d)
    _fiscal(ax, figtools.abscisse_date("1991-01-01"), 1970.0, FIN_MT)
    _cadre(ax, "Millimes de 2025 par kWh (calculés)" if constants
           else "Millimes courants par kWh")
    ax.set_xlim(1968.8, FIN_MT + 1.2)
    ax.set_xticks(range(1970, 2024, 4))
    ax.set_ylim(0, _haut(tous))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    poignees = [Line2D([0], [0], color=c, ls=ls, lw=lw, label=figtools.fig_text(textwrap.fill(e, 62)))
                for _, c, ls, lw, _, e in COURBES_BT]
    poignees += [Line2D([0], [0], color=GRIS_FONCE, marker=m, mfc=GRIS_FONCE if plein else "white",
                        ls="none", ms=5, label=figtools.fig_text(f"grille de source {f}"))
                 for f, (m, plein) in MARQUES_BT.items()]
    _legende(ax, poignees + _poignees_bandes_reperes(bandes), ncol=2, y=-0.11)
    fig.tight_layout()
    return fig


def bt_nom(tranche: str) -> str:
    import serie_tarifs_bt
    return serie_tarifs_bt.NOMS.get(tranche, tranche)


def _figure_tarifs_bt():
    import serie_tarifs_bt
    d = _donnees_bt()
    table = _table_tarifs(
        d, _tracees_bt(d),
        ["tranche", "structure", "date_effet", "jour_etabli", "valeur", "unite", "coefficient_2025",
         "valeur_2025", "etat", "tracee", "famille_source", "portee", "source", "page", "rupture",
         "remarque"],
        ["Tranche", "Structure du tarif", "Date d'effet", "Jour d'effet établi", "Valeur courante",
         "Unité", "Coefficient de 2025 (calculé)",
         "valeur_2025 : valeur en monnaie de 2025 (calculée)", "État", "Tracée",
         "Famille de la source", "Portée", "Source", "Page", "Rupture", "Remarque"],
        {"tranche": {**serie_tarifs_bt.NOMS, "grille_non_etablie": "grille non établie"},
         "etat": NOM_ETAT})
    return (_vues(fig_tarifs_bt), table, _cles_ipc(TARIFS_BT, d), "fig_compensation_eg_tarifs_bt")


# --- 6d. Le gaz naturel : basse pression, moyenne et haute pression, 1987-2022 --------------------

NOM_RESEAU = {"basse_pression": "basse pression", "moyenne_pression": "moyenne pression",
              "haute_pression": "haute pression"}
NOM_TRANCHE_GAZ = {"prix_unique": "prix unique", "tranche_1": "première tranche",
                   "tranche_2": "deuxième tranche", "tranche_3": "troisième tranche",
                   "tranche_4": "quatrième tranche", "premier_niveau": "premier niveau",
                   "second_niveau": "second niveau", "au_dela": "au-delà de 2 000 tep par mois",
                   "grille_non_etablie": "grille non établie"}
COURBES_GAZ = {
    "basse_pression": (
        (("prix_unique",), NOIR, "-", "Prix unique (1987-2004)"),
        (("tranche_1",), BLEU, "-", "Première tranche (depuis 2008)"),
        (("tranche_2",), VERT, "-", "Deuxième tranche (depuis 2008)"),
        (("tranche_3",), ORANGE, "-", "Troisième tranche (depuis 2008)"),
        (("tranche_4",), ROUGE, "-", "Quatrième tranche (depuis 2014)")),
}
COURBES_MP_HP = (
    ((("moyenne_pression", "prix_unique"), ("moyenne_pression", "premier_niveau")), BLEU, "-",
     "Moyenne pression : prix unique (1987-2000), puis premier niveau de débit (depuis 2004)"),
    ((("moyenne_pression", "second_niveau"),), BLEU_CLAIR, (0, (3, 1.5)),
     "Moyenne pression : second niveau de débit (depuis 2004)"),
    ((("haute_pression", "premier_niveau"),), ROUGE, "-",
     "Haute pression : premier niveau (prix fixe depuis 2008)"),
    ((("haute_pression", "second_niveau"),), ORANGE, "-",
     "Haute pression : second niveau, jusqu'à 2 000 tep par mois (depuis 2008)"),
    ((("haute_pression", "au_dela"),), VIOLET, "-",
     "Haute pression : au-delà de 2 000 tep par mois (prix fixe depuis 2014)"),
)
FIN_GAZ = 2023.0
FORMULES = (  # (réseau, tranche, de, à, libellé) — périodes où le prix est une formule
    ("haute_pression", "premier_niveau", "1987-06-16", "2008-09-01",
     "haute pression, premier niveau : prix indexé sur le fuel lourd (0,1 F − c)"),
    ("haute_pression", "au_dela", "2008-09-01", "2014-05-01",
     "haute pression, au-delà : prix indexé sur le fuel lourd"),
)


def _donnees_gaz():
    d = figtools.series(TARIFS_GAZ)
    d["date_effet"] = d["date_effet"].astype(str)
    return d


def _marque_gaz(r):
    calcul = isinstance(r.remarque, str) and "par un calcul" in r.remarque
    return ("D", False) if calcul else ("o", True)


def _trace_gaz(ax, d, specs, constants, dates_par_reseau):
    tous = []
    coupures = _coupures(d)
    for cles, couleur, ls, _ in specs:
        pts = []
        for reseau, tranche in cles:
            sous = d[(d["reseau"] == reseau) & (d["tranche"] == tranche)]
            for structure in dict.fromkeys(sous["structure"]):
                s = sous[sous["structure"] == structure].sort_values("date_effet")
                s.attrs["dates"] = dates_par_reseau[reseau]
                pts += _courbe_escalier(
                    ax, s, f"{NOM_RESEAU[reseau]}, {NOM_TRANCHE_GAZ[tranche]}", couleur, ls=ls,
                    lw=2.0, etiquette=False, constants=constants, grandeur="thermie",
                    fin_serie=FIN_GAZ, coupures=coupures, marque=_marque_gaz, dec_c=1)
        tous.append(pts)
        if pts and couleur != BLEU_CLAIR:
            for (x, y), dx, ha in ((pts[0], -4, "right"), (pts[-1], 5, "left")):
                ax.annotate(_nb(y, 1) if constants else _nbv(y), xy=(x, y), xytext=(dx, 0),
                            textcoords="offset points", ha=ha, va="center", fontsize=7,
                            color=couleur)
    return tous


def fig_tarifs_gaz_bp(constants: bool = False):
    figtools.apply_lang_font()
    d = _donnees_gaz()
    d = d[d["reseau"] == "basse_pression"]
    fig, ax = plt.subplots(figsize=(10, 5.4))
    bandes = _bandes(ax, d, fin=FIN_GAZ)
    specs = [((("basse_pression", t),), c, ls, e) for (t,), c, ls, e in COURBES_GAZ["basse_pression"]]
    tous = _trace_gaz(ax, d, specs, constants, {"basse_pression": d["date_effet"].tolist()})
    _reperes(ax, d)
    _fiscal(ax, figtools.abscisse_date("1991-01-01"), 1986.6, FIN_GAZ)
    _cadre(ax, "Millimes de 2025 par thermie (calculés)" if constants
           else "Millimes courants par thermie")
    ax.set_xlim(1986.0, FIN_GAZ + 1.4)
    ax.set_xticks(range(1987, 2024, 3))
    ax.set_ylim(0, _haut(tous, pas=10))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    poignees = [Line2D([0], [0], color=c, ls=ls, lw=2, label=figtools.fig_text(e))
                for _, c, ls, e in specs]
    poignees.append(Line2D([0], [0], color=GRIS_FONCE, marker="D", mfc="white", ls="none", ms=5,
                           label=figtools.fig_text("date d'effet rattachée par un calcul")))
    _legende(ax, poignees + _poignees_bandes_reperes(bandes), ncol=2, y=-0.13)
    fig.tight_layout()
    return fig


def fig_tarifs_gaz_mp_hp(constants: bool = False):
    figtools.apply_lang_font()
    d = _donnees_gaz()
    d = d[d["reseau"] != "basse_pression"]
    fig, ax = plt.subplots(figsize=(10, 5.6))
    bandes = _bandes(ax, d, fin=FIN_GAZ)
    dates = {r: d[d["reseau"] == r]["date_effet"].tolist()
             for r in ("moyenne_pression", "haute_pression")}
    tous = _trace_gaz(ax, d, COURBES_MP_HP, constants, dates)
    for _reseau, _tranche, a, b, libelle in FORMULES:
        x0, x1 = figtools.abscisse_date(a), figtools.abscisse_date(b)
        y = 0.035 if _tranche == "premier_niveau" else 0.085
        ax.broken_barh([(x0, x1 - x0)], (y, 0.03), transform=ax.get_xaxis_transform(),
                       facecolor="white", edgecolor=ROUGE if _tranche == "premier_niveau" else VIOLET,
                       hatch="////", lw=0.8, zorder=2)
        ax.annotate(figtools.fig_text(libelle), xy=(x0 + 0.2, y + 0.04),
                    xycoords=("data", "axes fraction"), fontsize=6.5, va="bottom",
                    color=ROUGE if _tranche == "premier_niveau" else VIOLET)
    _reperes(ax, d)
    _fiscal(ax, figtools.abscisse_date("1991-01-01"), 1986.6, FIN_GAZ)
    _cadre(ax, "Millimes de 2025 par thermie (calculés)" if constants
           else "Millimes courants par thermie")
    ax.set_xlim(1986.0, FIN_GAZ + 1.4)
    ax.set_xticks(range(1987, 2024, 3))
    ax.set_ylim(0, _haut(tous, pas=10))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    poignees = [Line2D([0], [0], color=c, ls=ls, lw=2, label=figtools.fig_text(e))
                for _, c, ls, e in COURBES_MP_HP]
    poignees.append(Patch(facecolor="white", edgecolor=ROUGE, hatch="////",
                          label=figtools.fig_text("prix indexé sur le fuel lourd : aucune valeur fixe")))
    poignees.append(Line2D([0], [0], color=GRIS_FONCE, marker="D", mfc="white", ls="none", ms=5,
                           label=figtools.fig_text("date d'effet rattachée par un calcul")))
    _legende(ax, poignees + _poignees_bandes_reperes(bandes), ncol=2, y=-0.13)
    fig.tight_layout()
    return fig


def _table_gaz(d, specs):
    tracees = {c for cles, *_ in specs for c in cles}
    tracee = d[[(r, t) in tracees for r, t in zip(d["reseau"], d["tranche"])]]
    return _table_tarifs(
        d, tracee,
        ["reseau", "tranche", "structure", "date_effet", "jour_etabli", "valeur", "formule", "unite",
         "coefficient_2025", "valeur_2025", "etat", "tracee", "portee", "source", "rupture",
         "remarque"],
        ["Réseau", "Tranche", "Structure du tarif", "Date d'effet", "Jour d'effet établi",
         "Valeur courante", "Formule", "Unité", "Coefficient de 2025 (calculé)",
         "valeur_2025 : valeur en monnaie de 2025 (calculée)", "État", "Tracée", "Portée",
         "Source", "Rupture", "Remarque"],
        {"reseau": NOM_RESEAU, "tranche": NOM_TRANCHE_GAZ, "etat": NOM_ETAT})


def _figure_tarifs_gaz_bp():
    d = _donnees_gaz()
    d = d[d["reseau"] == "basse_pression"]
    specs = [((("basse_pression", t),), c, ls, e) for (t,), c, ls, e in COURBES_GAZ["basse_pression"]]
    return (_vues(fig_tarifs_gaz_bp), _table_gaz(d, specs), _cles_ipc(TARIFS_GAZ, d),
            "fig_compensation_eg_tarifs_gaz_bp")


def _figure_tarifs_gaz_mp_hp():
    d = _donnees_gaz()
    d = d[d["reseau"] != "basse_pression"]
    return (_vues(fig_tarifs_gaz_mp_hp), _table_gaz(d, COURBES_MP_HP), _cles_ipc(TARIFS_GAZ, d),
            "fig_compensation_eg_tarifs_gaz_mp_hp")


# --- 7. Le prix de vente et le coût de revient du gaz selon l'Observatoire, 2017-2025 ---------

def fig_cout_prix_gaz(constants: bool = False):
    figtools.apply_lang_font()
    d = figtools.series(GAZ_ONE)
    d = d[d["valeur"].notna()].copy()
    d["coef"] = [_coeff(a) for a in d["annee"]]
    d["y"] = d["valeur"] * (d["coef"] if constants else 1)
    fig, ax = plt.subplots(figsize=(9.5, 4.6))
    unite = "dinars de 2025 par tep" if constants else "dinars par tep"
    for grandeur, nom, couleur, marque in (("cout_de_revient", "Coût de revient", ROUGE, "s"),
                                           ("prix_de_vente", "Prix de vente global, hors taxes",
                                            BLEU, "o")):
        s = d[d["grandeur"] == grandeur].sort_values("annee")
        _trace_famille(
            ax, s, "y", couleur, marque,
            texte=lambda r, n=nom: (
                f"{r.annee} · {n.lower()} : {_nb(r.y)} {unite}"
                + (f", valeur calculée ({_nb(r.valeur)} dinars courants × {_nb(r.coef, 3)})"
                   if constants else "") + " ; Observatoire national de l'énergie et des mines, "
                "données provisoires avant audit"))
        for k in (0, -1):
            r = s.iloc[k]
            ax.annotate(_nb(r["y"], 0), xy=(r["annee"], r["y"]), xytext=(0, 7),
                        textcoords="offset points", ha="center", fontsize=7, color=couleur)
    ax.axvspan(2018.5, 2021.5, color=GRIS_BANDE, alpha=0.55, lw=0, zorder=0)
    ax.annotate(figtools.fig_text("aucun coût de revient publié"), xy=(2020, 0.8),
                xycoords=("data", "axes fraction"), ha="center", va="center", rotation=90,
                fontsize=6.5, color=GRIS_FONCE)
    _cadre(ax, "Dinars de 2025 par tep (calculés)" if constants
           else "Dinars courants par tonne équivalent pétrole")
    ax.set_xlim(2016.4, 2025.6)
    ax.set_xticks(range(2017, 2026))
    ax.set_ylim(0, 250 * math.ceil(d["y"].max() * 1.12 / 250))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _nb(v, 0)))
    _legende(ax, [Line2D([0], [0], color=ROUGE, marker="s", lw=1.5, ms=5,
                         label=figtools.fig_text("Coût de revient")),
                  Line2D([0], [0], color=BLEU, marker="o", lw=1.5, ms=5,
                         label=figtools.fig_text("Prix de vente global, hors taxes")),
                  Patch(facecolor=GRIS_BANDE, label=figtools.fig_text(
                      "années sans coût de revient publié"))], ncol=3, y=-0.14)
    fig.tight_layout()
    return fig


def _figure_cout_prix_gaz():
    d = figtools.series(GAZ_ONE).copy()
    d["coefficient_2025"] = [round(_coeff(a), 4) for a in d["annee"]]
    d["valeur_2025"] = (d["valeur"] * d["annee"].map(_coeff)).round(1)
    d["grandeur"] = d["grandeur"].map({"prix_de_vente": "prix de vente global, hors taxes",
                                       "cout_de_revient": "coût de revient"})
    table = d[["annee", "grandeur", "valeur", "coefficient_2025", "valeur_2025", "etat", "source",
               "remarque"]]
    table.columns = ["Année", "Grandeur", "Dinars courants par tep", "Coefficient de 2025 (calculé)",
                     "valeur_2025 : dinars de 2025 par tep (calculée)", "État", "Source", "Remarque"]
    vues = [("Dinars courants", fig_cout_prix_gaz()),
            ("Dinars de 2025 (calculés)", fig_cout_prix_gaz(constants=True))]
    return (vues, table.reset_index(drop=True),
            {GAZ_ONE: ["one-chiffres-cles-energie"], dinars_constants.SERIE_IPC: None,
             dinars_constants.SERIE_IPC_RECENT: None},
            "fig_compensation_eg_cout_prix_gaz")


# --- registre ---------------------------------------------------------------------------------

FIGURES = {
    "prix_achat_gaz": _figure_prix_achat_gaz,
    "cout_prix_kwh": _figure_cout_prix_kwh,
    "subvention": _figure_subvention,
    "gaz_sources": _figure_gaz_sources,
    "gaz_pib": _figure_gaz_pib,
    "tarifs_mt": _figure_tarifs_mt,
    "tarifs_ht": _figure_tarifs_ht,
    "tarifs_bt": _figure_tarifs_bt,
    "tarifs_gaz_bp": _figure_tarifs_gaz_bp,
    "tarifs_gaz_mp_hp": _figure_tarifs_gaz_mp_hp,
    "cout_prix_gaz": _figure_cout_prix_gaz,
}
# Figures sans mention « valeurs courantes » : volumes, ou deux vues (courants et monnaie de 2025).
NON_MONETAIRES = {"gaz_sources", "tarifs_mt", "tarifs_ht", "tarifs_bt", "tarifs_gaz_bp",
                  "tarifs_gaz_mp_hp", "prix_achat_gaz", "cout_prix_kwh", "cout_prix_gaz"}


def figure(nom: str, caption: str, note_lecture: str | None = None) -> None:
    """Émet la figure `nom` en onglets (graphique, données, sources).

    À appeler dans un chunk Quarto étiqueté `#| label: fig-…`, `#| output: asis`."""
    vues, table, cles, slug = FIGURES[nom]()
    for sid, liste in cles.items():
        _declarer(sid, liste, SURCHARGES.get(nom, {}).get(sid))
    figtools.figure_tabs(vues, table, *cles, slug=slug, caption=caption,
                         note_lecture=note_lecture, nominal=nom not in NON_MONETAIRES)
    plt.close("all")

"""Taux marginal et taux moyen d'un barème à tranches, et leur figure commune.

Composant mutualisé des figures de barèmes du précis : impôt sur le revenu, contribution
personnelle d'État, droits sur les successions… Il lit une SÉRIE DE TRANCHES au format
qu'émet `openfisca_tables.lignes_tranches` — une ligne par tranche et par date d'effet,
colonnes `<clé>`, `tranche`, `date_effet`, `seuil`, `taux` — par `figtools.series()`,
c'est-à-dire le snapshot versionné du précis : le build ne lit jamais les paramètres vifs.

LE CALCUL, PUR ET TESTÉ (`tests/test_taux_bareme.py`).
  - Un barème est une liste `[(seuil, taux), …]` triée par seuil croissant ; la tranche i
    couvre l'assiette de `seuil_i` (exclu) à `seuil_{i+1}` (inclus), comme les tableaux
    du précis l'écrivent (« 0 à 5 000 », « 5 000,001 à 10 000 »). À un seuil exact, c'est
    donc la tranche inférieure qui s'applique ; à une assiette nulle, la première.
  - Le montant dû est calculé BARÈME APPLIQUÉ PAR TRANCHE : chaque fraction de l'assiette
    supporte le taux de sa tranche. C'est le seul mode que le composant connaît. Un barème
    dont le taux de la tranche atteinte frappe toute l'assiette (« de la valeur globale »)
    n'en relève pas : son taux moyen est son taux de tranche, et son taux marginal n'est
    pas une fonction en escalier.
  - Le taux moyen est le montant dû rapporté à l'assiette. À une assiette nulle, il N'EST
    PAS DÉFINI : `taux_moyen` rend `None`, jamais 0. Un 0 n'est rendu que s'il est vrai —
    une assiette positive comprise dans une tranche à 0 %.
  - Une assiette inférieure au premier seuil (barème dont la première tranche commence
    au-dessus de 0) ne supporte rien : taux marginal 0, montant 0.

LA FIGURE. Un panneau par barème (une parenté, une catégorie de contribuable…), plusieurs
états datés superposés dans chaque panneau, une couleur par état. Le taux marginal est
tracé en escalier, trait fin ; le taux moyen en courbe continue, trait épais, calculée sur
une grille fine qui comprend chaque seuil. Quand un état n'a qu'un taux, sur toute
l'assiette, les deux grandeurs se confondent : la courbe est tracée une fois, et la légende
le dit (`taux_unique`).

LES LIBELLÉS. Le composant porte les siens (`_L`), en français et en arabe ; le module de
figure fournit ceux de ses panneaux, de ses états, de ses axes et de son titre, déjà dans
la langue du livre.
"""
from __future__ import annotations

from typing import Iterable, Sequence

import figtools

Bareme = list[tuple[float, float]]

_L = {
    "marginal": {"fr": "taux marginal (escalier)", "ar": "النسبة الحدية (درجات)"},
    "moyen": {"fr": "taux moyen (courbe)", "ar": "النسبة المتوسّطة (منحنى)"},
    "unique": {"fr": "taux unique : marginal et moyen confondus",
               "ar": "نسبة وحيدة: الحدية والمتوسّطة متطابقتان"},
    "c_assiette": {"fr": "Assiette (D)", "ar": "الوعاء (د)"},
    "c_marginal": {"fr": "taux marginal (%)", "ar": "النسبة الحدية (%)"},
    "c_tranche": {"fr": "taux de la tranche (%)", "ar": "نسبة الشريحة (%)"},
    "c_du": {"fr": "montant dû (D)", "ar": "المبلغ المستوجَب (د)"},
    "c_moyen": {"fr": "taux moyen (%)", "ar": "النسبة المتوسّطة (%)"},
    "panneau": {"fr": "Barème", "ar": "الجدول"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


# ---------------------------------------------------------------------------- calcul


def _verifie(bareme: Bareme) -> None:
    if not bareme:
        raise ValueError("barème vide")
    seuils = [s for s, _t in bareme]
    if seuils != sorted(seuils) or len(set(seuils)) != len(seuils):
        raise ValueError(f"seuils non strictement croissants : {seuils}")


def taux_marginal(bareme: Bareme, assiette: float) -> float:
    """Taux de la tranche où tombe `assiette` (tranche inférieure à un seuil exact)."""
    _verifie(bareme)
    if assiette < 0:
        raise ValueError(f"assiette négative : {assiette}")
    if assiette == 0:
        return bareme[0][1] if bareme[0][0] == 0 else 0.0
    taux = 0.0
    for seuil, t in bareme:
        if assiette > seuil:
            taux = t
        else:
            break
    return taux


def montant_du(bareme: Bareme, assiette: float) -> float:
    """Montant dû, barème appliqué par tranche."""
    _verifie(bareme)
    if assiette < 0:
        raise ValueError(f"assiette négative : {assiette}")
    total = 0.0
    for i, (seuil, t) in enumerate(bareme):
        fin = bareme[i + 1][0] if i + 1 < len(bareme) else float("inf")
        if assiette <= seuil:
            break
        total += t * (min(assiette, fin) - seuil)
    return total


def taux_moyen(bareme: Bareme, assiette: float) -> float | None:
    """Montant dû rapporté à l'assiette ; `None` à une assiette nulle (non défini)."""
    if assiette == 0:
        _verifie(bareme)
        return None
    return montant_du(bareme, assiette) / assiette


def taux_unique(bareme: Bareme) -> bool:
    """Vrai quand un seul taux vaut sur toute l'assiette : marginal et moyen confondus."""
    return len({t for _s, t in bareme}) == 1 and bareme[0][0] == 0


def bareme_a_la_date(d, cle: str, valeur: str, date: str) -> Bareme:
    """Tranches `(seuil, taux)` en vigueur à `date` pour `d[cle] == valeur`, seuil croissant.

    `d` : série au format de `openfisca_tables.lignes_tranches`. Pour chaque tranche, la
    dernière ligne datée au plus tard à `date` fait foi ; une tranche close (taux vide) est
    écartée.
    """
    sous = d[(d[cle] == valeur) & (d["date_effet"] <= date)]
    tranches = []
    for _t, lignes in sous.sort_values("date_effet").groupby("tranche"):
        derniere = lignes.iloc[-1]
        if derniere["taux"] == derniere["taux"]:  # tranche close : taux vide (NaN)
            tranches.append((float(derniere["seuil"]), float(derniere["taux"])))
    return sorted(tranches)


def grille(bareme: Bareme, assiette_max: float, n: int = 400) -> list[float]:
    """Assiettes où tracer le taux moyen : grille régulière plus chaque seuil, sans 0."""
    points = {assiette_max * k / n for k in range(1, n + 1)}
    points |= {s for s, _t in bareme if 0 < s <= assiette_max}
    return sorted(points)


# --------------------------------------------------------------------------- tableau


def table_taux(panneaux: Sequence[tuple[str, dict[str, Bareme]]],
               libelles_etats: dict[str, str], assiettes: Iterable[float],
               entete_panneau: str | None = None, entete_assiette: str | None = None,
               avec_montant: bool = False, sans_moyen: Iterable[str] = ()):
    """Données de la figure : par panneau et par assiette, marginal et moyen par état.

    `panneaux` : [(libellé du panneau, {date: barème})] ; `libelles_etats` : date ->
    libellé court de l'état (en-tête de colonne). `entete_panneau`, `entete_assiette` :
    en-têtes des deux premières colonnes, dans la langue du livre (« Barème », « Assiette
    (D) » à défaut). Le taux moyen d'une assiette nulle est laissé vide. `avec_montant` :
    ajoute le montant dû, en dinars courants — à n'activer que si le tableau donne aussi
    sa contrepartie en dinars constants (convention du précis). `sans_moyen` : dates des états
    dont le mode de liquidation n'est pas établi ; ils n'ont que la colonne du taux de leur
    tranche, ni taux marginal ni taux moyen ni montant.
    """
    import pandas as pd

    sans_moyen = set(sans_moyen)

    lignes = []
    assiettes = list(assiettes)
    for libelle, etats in panneaux:
        for x in assiettes:
            ligne = {entete_panneau or _lab("panneau"): libelle,
                     entete_assiette or _lab("c_assiette"): x}
            for date, bareme in etats.items():
                tm = taux_moyen(bareme, x)
                e = libelles_etats[date] + ("، " if figtools.lang() == "ar" else ", ")
                if date in sans_moyen:
                    ligne[f"{e}{_lab('c_tranche')}"] = round(100 * taux_marginal(bareme, x), 3)
                    continue
                ligne[f"{e}{_lab('c_marginal')}"] = round(100 * taux_marginal(bareme, x), 3)
                if avec_montant:
                    ligne[f"{e}{_lab('c_du')}"] = round(montant_du(bareme, x), 3)
                ligne[f"{e}{_lab('c_moyen')}"] = None if tm is None else round(100 * tm, 3)
            lignes.append(ligne)
    return pd.DataFrame(lignes)


# --------------------------------------------------------------------------- figure


def _dinars(v: float) -> str:
    return f"{v:,.0f}".replace(",", " ")


def fig_taux_moyens_marginaux(
    panneaux: Sequence[tuple[str, dict[str, Bareme]]], *,
    couleurs: dict[str, str], libelles_etats: dict[str, str],
    assiette_max: float | Sequence[float],
    xlabel: str, ylabel: str, titre: str, colonnes: int = 2,
    xticks: Sequence[float] | Sequence[Sequence[float]] | None = None, ymax: float | None = None,
    infobulle_panneau: bool = True, largeur: float | None = None,
    sans_moyen: Iterable[str] = (),
):
    """Taux marginal (escalier) et taux moyen (courbe) de chaque état, un cadre par panneau.

    `panneaux` : [(libellé, {date: barème})], dans l'ordre des cadres ; les dates sont les
    clés de `couleurs` et de `libelles_etats`, dans l'ordre de la légende. Libellés et titre
    sont fournis dans la langue du livre ; le composant les met en forme (`fig_text`).
    `assiette_max` (et `xticks`) : une valeur pour tous les cadres, ou une liste, une valeur
    par cadre (barèmes d'échelles très différentes : 1962 et 1986, par exemple).
    `sans_moyen` : dates des états dont le mode de liquidation n'est pas établi ; la figure n'en
    trace que l'escalier du taux de la tranche, sans courbe de taux moyen.
    """
    import math

    sans_moyen = set(sans_moyen)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    figtools.apply_lang_font()
    ft = figtools.fig_text
    lignes_fig = math.ceil(len(panneaux) / colonnes)
    fig, axes = plt.subplots(lignes_fig, colonnes, figsize=(largeur or 5.25 * colonnes, 3.6 * lignes_fig + 0.9),
                             sharey=True, squeeze=False)
    dates = list(libelles_etats)
    plus_haut = 0.0
    unique_vu = False
    maxima = (list(assiette_max) if isinstance(assiette_max, (list, tuple))
              else [assiette_max] * len(panneaux))
    repères = (list(xticks) if xticks is not None and isinstance(xticks[0], (list, tuple))
               else [xticks] * len(panneaux))
    for ax, (libelle, etats), assiette_max, xticks in zip(axes.flat, panneaux, maxima, repères):
        for date in dates:
            if date not in etats:
                continue
            bareme, c = etats[date], couleurs[date]
            # Un état identique au précédent du même cadre est tracé en tireté par-dessus.
            precedent = dates[dates.index(date) - 1] if dates.index(date) else None
            identique = precedent is not None and etats.get(precedent) == bareme
            ls = (0, (4, 3)) if identique else "-"
            z = 4 if identique else 3
            xs = [s for s, _t in bareme if s < assiette_max] + [assiette_max]
            ys = [100 * t for s, t in bareme if s < assiette_max]
            if bareme[0][0] > 0:  # avant le premier seuil, rien n'est dû
                xs, ys = [0.0] + xs, [0.0] + ys
            unique = taux_unique(bareme)
            unique_vu = unique_vu or unique
            # Taux unique : la même ligne vaut pour les deux grandeurs, en trait épais.
            marg, = ax.step(xs, ys + [ys[-1]], where="post", color=c, lw=2.4 if unique else 1.2,
                            ls=ls, zorder=z, alpha=1 if unique else 0.9)
            plus_haut = max(plus_haut, max(ys))
            if not unique and date not in sans_moyen:
                gx = grille(bareme, assiette_max)
                gy = [100 * taux_moyen(bareme, x) for x in gx]
                moy, = ax.plot(gx, gy, color=c, lw=2.4, ls=ls, zorder=z + 1)
                if infobulle_panneau:
                    figtools.infobulle(moy, f"{libelle} · {libelles_etats[date]} · {_lab('moyen')}")
            if infobulle_panneau:
                figtools.infobulle(marg, f"{libelle} · {libelles_etats[date]} · "
                                         f"{_lab('unique') if unique else _lab('marginal')}")
        ax.set_title(ft(libelle), fontsize=10)
        ax.set_xlim(0, assiette_max)
        if xticks is not None:
            ax.set_xticks(list(xticks))
            ax.set_xticklabels([ft(_dinars(x)) for x in xticks], fontsize=8)
        ax.grid(True, alpha=0.3)
    for ax in axes.flat[len(panneaux):]:
        ax.set_visible(False)
    for ax in axes.flat:
        ax.set_ylim(0, ymax if ymax is not None else 1.08 * plus_haut)
    for ax in axes[-1]:
        ax.set_xlabel(ft(xlabel), fontsize=8.5)
    for ax in axes[:, 0]:
        ax.set_ylabel(ft(ylabel))
    poignees = [Line2D([], [], color=couleurs[e], lw=2.4) for e in dates]
    noms = [ft(libelles_etats[e]) for e in dates]
    poignees += [Line2D([], [], color="#57606a", lw=1.2, drawstyle="steps-post"),
                 Line2D([], [], color="#57606a", lw=2.4)]
    noms += [ft(_lab("marginal")), ft(_lab("moyen"))]
    if unique_vu:
        poignees.append(Line2D([], [], color="#57606a", lw=2.4, ls="none", marker="none"))
        noms.append(ft(_lab("unique")))
    fig.legend(poignees, noms, loc="lower center", ncol=2, fontsize=8, frameon=False)
    fig.suptitle(ft(titre), fontsize=11)
    rangs = math.ceil(len(poignees) / 2)
    bas = (0.024 * rangs + 0.012) * 8.1 / fig.get_figheight()
    fig.tight_layout(rect=(0, bas, 1, 0.96))
    return fig

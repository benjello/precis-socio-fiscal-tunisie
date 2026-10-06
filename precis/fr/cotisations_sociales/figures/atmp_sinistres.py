"""Accidents du travail et maladies professionnelles déclarés, 2012-2022.

    from figures import atmp_sinistres as ats
    ats.fig_declares()      # nombres déclarés : accidents, trajet, maladies professionnelles
    ats.fig_mortels()       # accidents mortels, sur les lieux de travail et de trajet
    ats.fig_frequence()     # indices de fréquence avec arrêt, pour 1 000 salariés
    ats.fig_gravite()       # indices avec décès et avec incapacité permanente
    ats.table_declares() ; ats.table_frequence()

D'OÙ VIENNENT LES DONNÉES. Une seule série de l'entrepôt, lue par `figtools.series()` :
`atmp-sinistres-declares-2012-2022-bruts`. Elle garde côte à côte deux documents, le Profil
national de la sécurité et de la santé au travail (2023) et La Lettre du CRES n° 8 (janvier
2023), chaque valeur avec sa page.

CE QUI EST TRACÉ, ET CE QUI NE L'EST PAS.
  - Les nombres d'accidents viennent du Profil, la série la plus longue (2013-2022). Là où la
    Lettre du CRES donne une autre valeur — 2014 et 2015 —, elle est montrée par un rond creux,
    sans être raccordée. L'écart de 2020 sur les accidents de trajet (une unité) n'est pas
    visible à cette échelle : il est dans les données.
  - Les maladies professionnelles viennent de la Lettre pour 2014 et 2015, du Profil ensuite ;
    les deux documents concordent de 2016 à 2020.
  - Les indices de fréquence sont ceux de la Lettre, tels que publiés. Aucun indice n'est
    recalculé ici, faute de dénominateur publié avec eux.
  - Aucune ventilation par activité : voir `docs/reserve/atmp-bareme-sinistralite.md`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "atmp-sinistres-declares-2012-2022-bruts"
PROFIL = "MAS, Profil national de la SST, 2023"
CRES = "La Lettre du CRES n° 8, janvier 2023"

# Couleurs du précis ; la forme double la couleur (rond, carré, triangle).
BLEU, ORANGE, VERT, GRIS = "#08519c", "#bc4c00", "#1a7f37", "#6e7781"

_L = {
    "at": {"fr": "Accidents sur les lieux de travail", "ar": "حوادث في أماكن العمل"},
    "trajet": {"fr": "Accidents de trajet", "ar": "حوادث الطريق"},
    "mp": {"fr": "Maladies professionnelles déclarées", "ar": "أمراض مهنية مصرّح بها"},
    "at_mortel": {"fr": "Accidents mortels sur les lieux de travail",
                  "ar": "حوادث قاتلة في أماكن العمل"},
    "trajet_mortel": {"fr": "Accidents de trajet mortels", "ar": "حوادث طريق قاتلة"},
    "autre": {"fr": "valeur de la Lettre du CRES, quand elle diffère",
              "ar": "قيمة رسالة مركز البحوث والدراسات الاجتماعية عند الاختلاف"},
    "cas": {"fr": "cas déclarés", "ar": "تصاريح"},
    "pour_mille": {"fr": "pour 1 000 salariés", "ar": "لكل ألف أجير"},
    "t_declares": {"fr": "Accidents du travail et maladies professionnelles déclarés, 2013-2022",
                   "ar": "حوادث الشغل والأمراض المهنية المصرّح بها، 2013-2022"},
    "t_mortels": {"fr": "Accidents mortels déclarés, 2013-2022",
                  "ar": "الحوادث القاتلة المصرّح بها، 2013-2022"},
    "t_frequence": {"fr": "Indices de fréquence avec arrêt, 2012-2020",
                    "ar": "مؤشرات التواتر مع توقّف عن العمل، 2012-2020"},
    "t_gravite": {"fr": "Indices de fréquence avec décès et avec incapacité permanente, 2012-2020",
                  "ar": "مؤشرات التواتر مع وفاة ومع عجز دائم، 2012-2020"},
    "f_at": {"fr": "Accidents du travail avec arrêt", "ar": "حوادث شغل مع توقّف عن العمل"},
    "f_trajet": {"fr": "Accidents de trajet avec arrêt", "ar": "حوادث طريق مع توقّف عن العمل"},
    "f_mp": {"fr": "Maladies professionnelles", "ar": "أمراض مهنية"},
    "f_at_deces": {"fr": "Accidents du travail avec décès", "ar": "حوادث شغل مع وفاة"},
    "f_trajet_deces": {"fr": "Accidents de trajet avec décès", "ar": "حوادث طريق مع وفاة"},
    "f_at_ip": {"fr": "Accidents du travail avec incapacité permanente",
                "ar": "حوادث شغل مع عجز دائم"},
    "f_mp_ip": {"fr": "Maladies professionnelles avec incapacité permanente",
                "ar": "أمراض مهنية مع عجز دائم"},
    "v_declares": {"fr": "Déclarés", "ar": "المصرّح بها"},
    "v_mortels": {"fr": "Mortels", "ar": "القاتلة"},
    "v_arret": {"fr": "Avec arrêt", "ar": "مع توقّف عن العمل"},
    "v_gravite": {"fr": "Décès et incapacité permanente", "ar": "الوفاة والعجز الدائم"},
    "c_annee": {"fr": "Année", "ar": "السنة"},
    "c_indicateur": {"fr": "Indicateur", "ar": "المؤشر"},
    "c_valeur": {"fr": "Valeur", "ar": "القيمة"},
    "c_unite": {"fr": "Unité", "ar": "الوحدة"},
    "c_source": {"fr": "Document", "ar": "الوثيقة"},
    "c_page": {"fr": "Page", "ar": "الصفحة"},
    "c_objet": {"fr": "Tableau ou annexe", "ar": "الجدول أو الملحق"},
}

# Indicateurs de la série, par rôle dans les figures.
I_AT, I_TRAJET = "accidents sur les lieux de travail", "accidents de trajet"
I_AT_CRES = "accidents du travail"
I_MP = "maladies professionnelles déclarées"
I_AT_MORTEL = "accidents mortels sur les lieux de travail"
I_TRAJET_MORTEL = "accidents de trajet mortels"
F_AT = "indice de fréquence des accidents du travail avec arrêt"
F_TRAJET = "indice de fréquence des accidents de trajet avec arrêt"
F_MP = "indice de fréquence des maladies professionnelles"
F_AT_DECES = "indice de fréquence des accidents du travail avec décès"
F_TRAJET_DECES = "indice de fréquence des accidents de trajet avec décès"
F_AT_IP = "indice de fréquence des accidents du travail avec incapacité permanente"
F_MP_IP = "indice de fréquence des maladies professionnelles avec incapacité permanente"


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _serie(source: str, indicateur: str):
    """{année: valeur} d'un indicateur dans un document ; erreur s'il est absent."""
    df = figtools.series(SERIE)
    d = df[(df["source"] == source) & (df["indicateur"] == indicateur)]
    if d.empty:
        raise ValueError(f"{indicateur!r} absent de {source!r}")
    return dict(zip(d["annee"].astype(int), d["valeur"].astype(float)))


def _mp():
    """Maladies professionnelles : la Lettre pour 2014-2015, le Profil de 2016 à 2022."""
    profil, cres = _serie(PROFIL, I_MP), _serie(CRES, I_MP)
    communs = set(profil) & set(cres)
    if any(profil[a] != cres[a] for a in communs):
        raise ValueError("maladies professionnelles : les deux documents divergent")
    return dict(sorted({**cres, **profil}.items()))


def _nb(v: float) -> str:
    return f"{int(round(v)):,}".replace(",", " ")


def _dec(v: float) -> str:
    return f"{v:g}".replace(".", ",")


def _courbe(ax, valeurs: dict, couleur: str, marque: str, libelle: str, fmt=_nb):
    annees = sorted(valeurs)
    ax.plot(annees, [valeurs[a] for a in annees], color=couleur, marker=marque, ms=5,
            lw=1.8, label=figtools.fig_text(libelle), zorder=3)
    for a in annees:
        (m,) = ax.plot([a], [valeurs[a]], marque, ms=13, color=couleur, alpha=0.0, zorder=5)
        figtools.infobulle(m, f"{libelle}, {a} : {fmt(valeurs[a])}")


def _divergences(ax, reference: dict, autre: dict, couleur: str, premiere: bool):
    """Ronds creux aux années où la Lettre du CRES donne une autre valeur que le Profil."""
    annees = [a for a in sorted(autre) if a in reference and abs(autre[a] - reference[a]) > 50]
    if annees:
        ax.plot(annees, [autre[a] for a in annees], "o", ms=8, mfc="none", mec=couleur,
                mew=1.4, ls="none", zorder=4,
                label=figtools.fig_text(_lab("autre")) if premiere else None)
        for a in annees:
            (m,) = ax.plot([a], [autre[a]], "o", ms=14, color=couleur, alpha=0.0, zorder=5)
            figtools.infobulle(m, f"{_lab('autre')}, {a} : {_nb(autre[a])}")


def _habille(ax, unite: str, annees):
    ax.set_xticks(list(annees))
    ax.set_ylim(bottom=0)
    ax.set_ylabel(figtools.fig_text(_lab(unite)))
    ax.grid(axis="y", alpha=.25)
    for cote in ("top", "right"):
        ax.spines[cote].set_visible(False)
    ax.legend(loc="best", fontsize=9, frameon=False)


def fig_declares():
    figtools.apply_lang_font()
    at, trajet, mp = _serie(PROFIL, I_AT), _serie(PROFIL, I_TRAJET), _mp()
    fig, (haut, bas) = plt.subplots(2, 1, figsize=(9.5, 7.6), sharex=True,
                                    gridspec_kw={"height_ratios": [1.15, 1]})
    _courbe(haut, at, BLEU, "o", _lab("at"))
    _divergences(haut, at, _serie(CRES, I_AT_CRES), BLEU, True)
    _courbe(bas, trajet, ORANGE, "s", _lab("trajet"))
    _courbe(bas, mp, VERT, "^", _lab("mp"))
    for ax in (haut, bas):
        _habille(ax, "cas", range(2013, 2023))
        ax.yaxis.set_major_formatter(lambda v, _p: _nb(v))
    haut.set_title(figtools.fig_text(_lab("t_declares")))
    fig.tight_layout()
    return fig


def fig_mortels():
    figtools.apply_lang_font()
    at, trajet = _serie(PROFIL, I_AT_MORTEL), _serie(PROFIL, I_TRAJET_MORTEL)
    annees = sorted(at)
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    b1 = ax.bar(annees, [at[a] for a in annees], color=BLEU, width=.7,
                label=figtools.fig_text(_lab("at_mortel")))
    b2 = ax.bar(annees, [trajet[a] for a in annees], bottom=[at[a] for a in annees],
                color=ORANGE, width=.7, label=figtools.fig_text(_lab("trajet_mortel")))
    for a, r1, r2 in zip(annees, b1, b2):
        figtools.infobulle(r1, f"{_lab('at_mortel')}, {a} : {_nb(at[a])}")
        figtools.infobulle(r2, f"{_lab('trajet_mortel')}, {a} : {_nb(trajet[a])}")
        ax.annotate(_nb(at[a] + trajet[a]), (a, at[a] + trajet[a]), xytext=(0, 3),
                    textcoords="offset points", ha="center", fontsize=8, color=GRIS)
    _habille(ax, "cas", annees)
    ax.set_title(figtools.fig_text(_lab("t_mortels")))
    fig.tight_layout()
    return fig


def fig_frequence():
    figtools.apply_lang_font()
    fig, (haut, bas) = plt.subplots(2, 1, figsize=(9.5, 7.2), sharex=True,
                                    gridspec_kw={"height_ratios": [1.15, 1]})
    _courbe(haut, _serie(CRES, F_AT), BLEU, "o", _lab("f_at"), _dec)
    _courbe(bas, _serie(CRES, F_TRAJET), ORANGE, "s", _lab("f_trajet"), _dec)
    _courbe(bas, _serie(CRES, F_MP), VERT, "^", _lab("f_mp"), _dec)
    for ax in (haut, bas):
        _habille(ax, "pour_mille", range(2012, 2021))
        ax.yaxis.set_major_formatter(lambda v, _p: _dec(round(v, 2)))
    haut.set_title(figtools.fig_text(_lab("t_frequence")))
    fig.tight_layout()
    return fig


def fig_gravite():
    figtools.apply_lang_font()
    fig, (haut, bas) = plt.subplots(2, 1, figsize=(9.5, 7.2), sharex=True)
    _courbe(haut, _serie(CRES, F_AT_DECES), BLEU, "o", _lab("f_at_deces"), _dec)
    _courbe(haut, _serie(CRES, F_TRAJET_DECES), ORANGE, "s", _lab("f_trajet_deces"), _dec)
    _courbe(bas, _serie(CRES, F_AT_IP), BLEU, "o", _lab("f_at_ip"), _dec)
    _courbe(bas, _serie(CRES, F_MP_IP), VERT, "^", _lab("f_mp_ip"), _dec)
    for ax in (haut, bas):
        _habille(ax, "pour_mille", range(2012, 2021))
        ax.yaxis.set_major_formatter(lambda v, _p: _dec(round(v, 3)))
    haut.set_title(figtools.fig_text(_lab("t_gravite")))
    fig.tight_layout()
    return fig


def _table(unite_des_indices: bool):
    """Toutes les valeurs de la série pour une famille, document et page compris."""
    df = figtools.series(SERIE)
    est_indice = df["indicateur"].str.startswith("indice de fréquence")
    d = df[est_indice if unite_des_indices else ~est_indice]
    d = d.sort_values(["indicateur", "source", "annee"])
    return d.rename(columns={
        "annee": _lab("c_annee"), "indicateur": _lab("c_indicateur"),
        "valeur_imprimee": _lab("c_valeur"), "unite": _lab("c_unite"),
        "source": _lab("c_source"), "page_pdf": _lab("c_page"), "objet": _lab("c_objet"),
    })[[_lab("c_indicateur"), _lab("c_annee"), _lab("c_valeur"), _lab("c_unite"),
        _lab("c_source"), _lab("c_objet"), _lab("c_page")]].reset_index(drop=True)


def table_declares():
    return _table(False)


def table_frequence():
    return _table(True)

"""Figure « indice des prix déclarés de l'immobilier » du chapitre sur le patrimoine immobilier.

DES PRIX DÉCLARÉS, PAS DES PRIX DE MARCHÉ. L'indice des prix de l'immobilier de l'INS est
calculé sur le fichier de la direction générale des impôts qui recense l'enregistrement
des ventes (fiche technique de l'INS, septembre 2024). Chaque libellé de la figure et du
tableau le dit : une variation de la sous-déclaration s'y lit comme une variation de prix.

DEUX MÉTHODES, DEUX COURBES, JAMAIS CHAÎNÉES. La publication s'interrompt en 2022 et 2023
pour révision de méthode ; à la reprise (T1 2024), l'INS recalcule la série entière depuis
le T1 2000. L'ancienne série (classeur du T4 2021) et la nouvelle (classeur du T4 2025)
couvrent donc les mêmes trimestres de 2000 à 2021 sans coïncider : elles sont tracées
l'une à côté de l'autre, même couleur par type de bien, trait plein pour la méthode
révisée, tireté pour l'ancienne. Aucun raccord.

TROIS TYPES DE BIEN TRACÉS, CINQ COLONNES AU TABLEAU. Terrains, appartements et maisons
existent dans les deux méthodes. La colonne « bâti » de la méthode révisée (appartements et
maisons) n'est pas l'« indice général » de l'ancienne, que le classeur ne définit pas : les
deux ne sont jamais tracés en regard, et le tableau les garde sous leurs propres noms.

LA VUE EN PRIX RÉELS. Un prix déclaré en dinars courants mêle la hausse générale des prix et
le mouvement propre à l'immobilier. La seconde vue divise chaque trimestre par l'indice des
prix à la consommation de son année, ramené à 2015 = 100 comme l'indice de l'immobilier.
L'indice des prix est ANNUEL (moyenne de l'année) : les quatre trimestres d'une année ont le
même déflateur. C'est l'indice commun du précis (`scripts/dinars_constants.py`) : celui de
l'INS en base 1970 (annuaires statistiques), prolongé après 2023 par la variation de l'indice
en base 2015 que relaie la Banque centrale ; les deux sont citées dans l'onglet « Sources ».
Les deux méthodes de l'indice restent deux courbes, chacune déflatée par le même indice.

DES REPÈRES DE DATE, PAS D'EFFET. Les traits verticaux placent dans le temps les réformes que
le chapitre expose (1er janvier 2013, 2014, 2017, 2023). Ils ne prétendent à aucun lien entre
la réforme et le niveau de l'indice.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import dinars_constants  # noqa: E402
import figtools  # noqa: E402

HERE = Path(__file__).resolve().parent
FIGDATA = HERE.parent / "figdata"

SERIE_REVISEE = "ins-ipim-trimestriel"
SERIE_ANTERIEURE = "ins-ipim-trimestriel-methode-anterieure"

# Types tracés : ceux que les deux méthodes ont en commun.
TYPES = ("terrain_nu", "appartement", "maison")
COULEURS = {"terrain_nu": "#bf8700", "appartement": "#0969da", "maison": "#8250df"}

# Réformes exposées dans le chapitre, toutes au 1er janvier : loi de finances pour 2013
# (taux de la plus-value 15 % / 10 %), pour 2014 (plus-value étendue à tous les terrains,
# promoteurs), pour 2017 (droit complémentaire), pour 2023 (exclusion du logement réservée
# aux prix inférieurs à 500 000 D).
REFORMES = (2013, 2014, 2017, 2023)

# Publication interrompue : aucun communiqué pour les trimestres de 2022 et 2023.
INTERRUPTION = (2022, 2024)

_L = {
    "terrain_nu": {"fr": "Terrains", "ar": "الأراضي"},
    "appartement": {"fr": "Appartements", "ar": "الشقق"},
    "maison": {"fr": "Maisons", "ar": "المنازل"},
    "lg_revisee": {"fr": "méthode révisée (série recalculée en 2024)",
                   "ar": "المنهجية المراجَعة (سلسلة أُعيد احتسابها سنة 2024)"},
    "lg_anterieure": {"fr": "ancienne méthode (jusqu'au T4 2021)",
                      "ar": "المنهجية السابقة (إلى الثلاثي الرابع 2021)"},
    "lg_interruption": {"fr": "publication interrompue (2022-2023)",
                        "ar": "انقطاع النشر (2022-2023)"},
    "lg_reforme": {"fr": "réforme exposée au chapitre (1er janvier)",
                   "ar": "إصلاح مبيَّن في الفصل (غرّة جانفي)"},
    "y": {"fr": "Indice des prix déclarés (2015 = 100)",
          "ar": "مؤشر الأسعار المصرَّح بها (2015 = 100)"},
    "title": {"fr": "Indice des prix déclarés de l'immobilier par type de bien, 2000-2025",
              "ar": "مؤشر أسعار العقارات المصرَّح بها حسب نوع العقار، 2000-2025"},
    "vue_courants": {"fr": "Prix déclarés (dinars courants)",
                     "ar": "الأسعار المصرَّح بها (بالدينار الجاري)"},
    "vue_reels": {"fr": "Prix réels (déflatés)", "ar": "الأسعار الحقيقية (بعد التصحيح)"},
    "y_reel": {"fr": "Indice des prix déclarés divisé par l'indice des prix (2015 = 100)",
               "ar": "مؤشر الأسعار المصرَّح بها مقسوماً على مؤشر الأسعار (2015 = 100)"},
    "title_reel": {"fr": "Indice des prix déclarés de l'immobilier en prix réels, par type de bien, 2000-2025",
                   "ar": "مؤشر أسعار العقارات المصرَّح بها بالأسعار الحقيقية، حسب نوع العقار، 2000-2025"},
    "col_ipc": {"fr": "Indice des prix à la consommation, moyenne de l'année (2015 = 100)",
                "ar": "مؤشر أسعار الاستهلاك، معدّل السنة (2015 = 100)"},
    "col_reel_r": {"fr": "méthode révisée, prix réels (2015 = 100)",
                   "ar": "المنهجية المراجَعة، الأسعار الحقيقية (2015 = 100)"},
    "col_reel_a": {"fr": "ancienne méthode, prix réels (2015 = 100)",
                   "ar": "المنهجية السابقة، الأسعار الحقيقية (2015 = 100)"},
    "col_trimestre": {"fr": "Trimestre", "ar": "الثلاثي"},
    "col_terrain_nu_r": {"fr": "Terrains, méthode révisée (prix déclarés, 2015 = 100)",
                         "ar": "الأراضي، المنهجية المراجَعة (الأسعار المصرَّح بها، 2015 = 100)"},
    "col_appartement_r": {"fr": "Appartements, méthode révisée (prix déclarés, 2015 = 100)",
                          "ar": "الشقق، المنهجية المراجَعة (الأسعار المصرَّح بها، 2015 = 100)"},
    "col_maison_r": {"fr": "Maisons, méthode révisée (prix déclarés, 2015 = 100)",
                     "ar": "المنازل، المنهجية المراجَعة (الأسعار المصرَّح بها، 2015 = 100)"},
    "col_bati_r": {"fr": "Bâti, méthode révisée (prix déclarés, 2015 = 100)",
                   "ar": "المباني، المنهجية المراجَعة (الأسعار المصرَّح بها، 2015 = 100)"},
    "col_terrain_nu_a": {"fr": "Terrains, ancienne méthode (prix déclarés, 2015 = 100)",
                         "ar": "الأراضي، المنهجية السابقة (الأسعار المصرَّح بها، 2015 = 100)"},
    "col_appartement_a": {"fr": "Appartements, ancienne méthode (prix déclarés, 2015 = 100)",
                          "ar": "الشقق، المنهجية السابقة (الأسعار المصرَّح بها، 2015 = 100)"},
    "col_maison_a": {"fr": "Maisons, ancienne méthode (prix déclarés, 2015 = 100)",
                     "ar": "المنازل، المنهجية السابقة (الأسعار المصرَّح بها، 2015 = 100)"},
    "col_indice_general_a": {"fr": "Indice général, ancienne méthode (prix déclarés, 2015 = 100)",
                             "ar": "المؤشر العام، المنهجية السابقة (الأسعار المصرَّح بها، 2015 = 100)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _abscisse(trimestre: str) -> float:
    """« 2013-T1 » -> 2013,0 : le premier trimestre commence l'année."""
    annee, q = trimestre.split("-T")
    return int(annee) + (int(q) - 1) / 4


def _large(serie: str):
    """Une ligne par trimestre, une colonne par type de bien (niveau de l'indice)."""
    d = figtools.series(serie)
    return d.pivot(index="trimestre", columns="type_bien", values="indice_base2015")


def _ipc_2015() -> dict[int, float]:
    """Indice des prix à la consommation par année, ramené à 2015 = 100."""
    i = dinars_constants.ipc()
    return {a: 100.0 * v / i[2015] for a, v in i.items()}


def _reel(niveaux, ipc):
    """Niveaux trimestriels divisés par l'indice des prix de leur année (2015 = 100)."""
    annees = [int(t.split("-T")[0]) for t in niveaux.index]
    return niveaux.mul([100.0 / ipc[a] for a in annees], axis=0)


def table():
    rev = _large(SERIE_REVISEE)
    ant = _large(SERIE_ANTERIEURE)
    w = rev[["terrain_nu", "appartement", "maison", "bati"]].add_suffix("_r").join(
        ant[["terrain_nu", "appartement", "maison", "indice_general"]].add_suffix("_a"),
        how="outer")
    ipc = _ipc_2015()
    w["ipc"] = [ipc[int(t.split("-T")[0])] for t in w.index]
    for suf, niv in (("r", rev), ("a", ant)):
        reel = _reel(niv[list(TYPES)], ipc)
        for typ in TYPES:
            w[f"{typ}_reel_{suf}"] = reel[typ]
    w = w.round(2).reset_index()
    w.columns.name = None
    noms = {"trimestre": _lab("col_trimestre"), "ipc": _lab("col_ipc")}
    for c in w.columns:
        if c in noms:
            continue
        if "_reel_" in c:
            typ, suf = c.split("_reel_")
            noms[c] = f"{_lab(typ)}, {_lab('col_reel_' + suf)}"
        else:
            noms[c] = _lab(f"col_{c}")
    return w.rename(columns=noms)


def _tracer(rev, ant, *, ylabel: str, title: str):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    x_rev = [_abscisse(t) for t in rev.index]
    x_ant = [_abscisse(t) for t in ant.index]

    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.6), sharey=True)
    for ax, typ in zip(axes, TYPES):
        c = COULEURS[typ]
        bande = ax.axvspan(*INTERRUPTION, color="#8b949e", alpha=0.15, lw=0,
                           label=ft(_lab("lg_interruption")))
        for a in REFORMES:
            trait = ax.axvline(a, color="#57606a", ls=(0, (2, 2)), lw=0.8, zorder=1,
                               label=ft(_lab("lg_reforme")))
        ax.plot(x_rev, rev[typ], "-", color=c, lw=1.8,
                label=ft(_lab("lg_revisee")))
        # L'ancienne méthode passe au-dessus : sans quoi le trait plein la cacherait là
        # où les deux séries sont proches.
        ax.plot(x_ant, ant[typ], "--", color=c, lw=1.2, alpha=0.7, zorder=3,
                label=ft(_lab("lg_anterieure")))
        ax.axhline(100, color="#8b949e", lw=0.6, zorder=0)
        ax.set_title(ft(_lab(typ)), fontsize=10)
        ax.set_xlim(2000, 2026)
        ax.set_xticks([2000, 2005, 2010, 2015, 2020, 2025])
        ax.tick_params(axis="x", labelsize=8)
        ax.grid(True, axis="y", alpha=0.3)
    # Les années des repères, en haut du premier cadre seulement.
    for a in REFORMES:
        axes[0].annotate(str(a), xy=(a, 1), xycoords=("data", "axes fraction"),
                         xytext=(1.5, -3), textcoords="offset points", ha="left", va="top",
                         rotation=90, fontsize=6.5, color="#57606a")
    axes[0].set_ylabel(ft(ylabel))
    # Légende commune : les traits valent pour les trois cadres (couleur = type de bien).
    from matplotlib.lines import Line2D
    poignees = [Line2D([], [], color="#57606a", lw=1.8, ls="-"),
                Line2D([], [], color="#57606a", lw=1.2, ls="--", alpha=0.7),
                bande, trait]
    libelles = [ft(_lab(k)) for k in ("lg_revisee", "lg_anterieure", "lg_interruption",
                                      "lg_reforme")]
    fig.legend(poignees, libelles, loc="lower center", ncol=2, fontsize=8, frameon=False)
    fig.suptitle(ft(title), fontsize=11)
    fig.tight_layout(rect=(0, 0.12, 1, 0.96))
    return fig


def fig_ipim():
    """Vue en dinars courants : l'indice publié par l'INS."""
    return _tracer(_large(SERIE_REVISEE), _large(SERIE_ANTERIEURE),
                   ylabel=_lab("y"), title=_lab("title"))


def fig_ipim_reel():
    """Vue en prix réels : l'indice publié divisé par l'indice des prix de l'année."""
    ipc = _ipc_2015()
    return _tracer(_reel(_large(SERIE_REVISEE), ipc), _reel(_large(SERIE_ANTERIEURE), ipc),
                   ylabel=_lab("y_reel"), title=_lab("title_reel"))


def valeurs_reelles(types=TYPES):
    """Pour le texte du chapitre : valeurs de la vue réelle (méthode révisée)."""
    reel = _reel(_large(SERIE_REVISEE), _ipc_2015())
    return reel[list(types)]

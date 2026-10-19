"""Figures du chapitre sur le patrimoine immobilier : l'indice des prix déclarés de
l'immobilier (ci-dessous), le tarif des mutations par décès et les abattements sur les
successions (décrits à leur section, plus bas).

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
import matplotlib.ticker  # noqa: E402

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import dinars_constants  # noqa: E402
import figtools  # noqa: E402
import taux_bareme  # noqa: E402

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


# --- Les mutations par décès : le tarif selon la parenté et la part nette -----------------
#
# UN BARÈME, PAS UNE SÉRIE TEMPORELLE. L'abscisse est la part nette recueillie par l'ayant
# droit, en dinars ; l'ordonnée, un taux en pour cent. Trois états du droit, un cadre par
# degré de parenté :
#   - au 1er janvier 1984 (loi de finances pour 1984, art. 12) : six tranches ;
#   - au 17 mai 1993 (code des droits d'enregistrement et de timbre, art. 20, n° 16) : un taux
#     unique, sur toute la part ;
#   - au 17 août 1998 (loi n° 98-73, art. 8) : la ligne directe passe à 2,5 % ; les autres
#     taux de 1993 demeurent, et le trait de 1998 se superpose, en tireté, à celui de 1993.
# TAUX MARGINAL ET TAUX MOYEN, BARÈME APPLIQUÉ PAR TRANCHE. Le composant commun
# (`scripts/taux_bareme.py`) trace le taux de la tranche en escalier et le taux moyen —
# droit rapporté à la part nette — en courbe. Le taux moyen de 1984 suppose que chaque
# fraction de part supporte le taux de sa tranche. Le texte de 1984 ne le dit pas : le mode
# de liquidation est à établir sur le décret du 28 décembre 1929 (TODO du documentaliste
# dans le chapitre, docs/notes/successions-bareme-1985-1993.md, § 5). Si le taux de la
# tranche atteinte frappait la part entière, le taux moyen de 1984 serait l'escalier
# lui-même : retirer alors la courbe de 1984 et revoir la note de lecture.
# La série est celle du générateur (`successions-tarif`, tranche par tranche).
SERIE_SUCC_TARIF = "successions-tarif"
SERIE_SUCC_ABATTEMENTS = "successions-abattements"

PARENTES = ("ligne_directe_epoux", "freres_soeurs", "oncles_neveux_cousins",
            "au_dela_quatrieme_degre")
ETATS_TARIF = ("1984-01-01", "1993-05-17", "1998-08-17")
COULEURS_ETATS = {"1984-01-01": "#bf8700", "1993-05-17": "#0969da", "1998-08-17": "#1a7f37"}
# Bord droit de l'axe : la dernière tranche de 1984 commence à 90 000 D et n'a pas de borne.
PART_MAX = 120_000
# Assiettes du tableau de données : les seuils de 1984 et le bord de l'axe.
PARTS_TABLE = (5_000, 10_000, 15_000, 45_000, 90_000, PART_MAX)

_L.update({
    "ligne_directe_epoux": {"fr": "Ligne directe et époux", "ar": "الخط المباشر والزوجان"},
    "freres_soeurs": {"fr": "Frères et sœurs", "ar": "الإخوة والأخوات"},
    "oncles_neveux_cousins": {"fr": "Oncles, neveux et cousins",
                              "ar": "الأعمام والأخوال وأبناء الإخوة وأبناء العمومة"},
    "au_dela_quatrieme_degre": {"fr": "Au-delà du quatrième degré et non-parents",
                                "ar": "ما بعد الدرجة الرابعة وغير الأقارب"},
    "etat_1984-01-01": {"fr": "1er janvier 1984 : six tranches de part nette",
                        "ar": "1 جانفي 1984: ست شرائح من الحصة الصافية"},
    "etat_1993-05-17": {"fr": "17 mai 1993 : taux unique (code des droits d'enregistrement)",
                        "ar": "17 ماي 1993: نسبة وحيدة (مجلة معاليم التسجيل)"},
    "etat_1998-08-17": {"fr": "17 août 1998 : taux unique (loi n° 98-73)",
                        "ar": "17 أوت 1998: نسبة وحيدة (القانون عدد 98-73)"},
    "c_parente": {"fr": "Parenté", "ar": "القرابة"},
    "c_part": {"fr": "Part nette (D)", "ar": "الحصة الصافية (د)"},
    "court_1984-01-01": {"fr": "1984", "ar": "1984"},
    "court_1993-05-17": {"fr": "1993", "ar": "1993"},
    "court_1998-08-17": {"fr": "1998", "ar": "1998"},
    "x_part": {"fr": "Part nette recueillie par l'ayant droit (dinars courants)",
               "ar": "الحصة الصافية الراجعة لصاحب الحقّ (بالدينار الجاري)"},
    "y_tarif": {"fr": "Taux (%)", "ar": "النسبة (%)"},
    "title_tarif": {"fr": ("Mutations par décès : taux marginal et taux moyen du droit "
                           "d'enregistrement selon la part nette et la parenté, en 1984, 1993 "
                           "et 1998"),
                    "ar": ("نقل الملكية بالوفاة: النسبة الحدية والنسبة المتوسّطة لمعلوم "
                           "التسجيل حسب الحصة الصافية ودرجة القرابة، في 1984 و1993 و1998")},
})

figtools.register_provenance(
    SERIE_SUCC_TARIF,
    titre=("Tarif du droit d'enregistrement des mutations par décès, par degré de parenté et "
           "par tranche de part nette, à chaque date d'effet depuis le 1er janvier 1984"),
    titre_ar=("تعريفة معلوم التسجيل على نقل الملكية بالوفاة، حسب درجة القرابة وشريحة الحصة "
              "الصافية، عند كلّ تاريخ نفاذ منذ 1 جانفي 1984"),
    sources=["lf-1984", "loi-93-53-cdet", "loi-98-73"],
    unite=("taux fixé pour la tranche (taux marginal) et taux moyen, en pourcentage de la "
           "part nette, elle-même en dinars courants"),
    unite_ar=("النسبة المحدَّدة للشريحة (النسبة الحدية) والنسبة المتوسّطة، بالمائة من "
              "الحصة الصافية؛ والحصة الصافية بالدينار الجاري"),
    perimetre=("quatre degrés de parenté ; une ligne par tranche et par date d'effet, avec le "
               "texte du Journal officiel qui la fixe ; une tranche close au 17 mai 1993 n'a "
               "plus ni seuil ni taux"),
    perimetre_ar=("أربع درجات قرابة؛ سطر لكلّ شريحة ولكلّ تاريخ نفاذ، مع نصّ الرائد الرسمي "
                  "الذي يضبطها؛ والشريحة الملغاة في 17 ماي 1993 لا عتبة لها ولا نسبة"),
    caveats=("La figure commence au barème de 1984 ; ceux de 1969 et de 1975 sont au tableau "
             "des barèmes successoraux du chapitre. Le taux moyen est calculé "
             "barème appliqué par tranche : chaque fraction de part supporte le taux de sa "
             "tranche. Depuis 1993, le même taux vaut pour les donations ; "
             "les donations familiales sont au droit fixe depuis 2006."),
    caveats_ar=("تبدأ الرسوم بتعريفة 1984؛ أمّا تعريفتا 1969 و1975 ففي جدول تعريفات التركات "
                "من الفصل. تُحتسب النسبة المتوسّطة بتطبيق الجدول حسب الشرائح: يتحمّل "
                "كلّ جزء من الحصة نسبة شريحته. ومنذ 1993 تسري النسبة ذاتها على الهبات؛ وتخضع الهبات "
                "العائلية لمعلوم قارّ منذ 2006."),
)


def _bareme_a(d, parente: str, date: str) -> list[tuple[float, float]]:
    """Tranches (seuil, taux) en vigueur à `date` pour une parenté, seuil croissant."""
    return taux_bareme.bareme_a_la_date(d, "parente", parente, date)


def _d(v: float) -> str:
    return f"{v:,.0f}".replace(",", " ")


def _panneaux_successions():
    d = figtools.series(SERIE_SUCC_TARIF)
    return [(_lab(p), {date: _bareme_a(d, p, date) for date in ETATS_TARIF}) for p in PARENTES]


def fig_tarif_successions():
    """Quatre cadres, un par parenté : taux marginal en escalier, taux moyen en courbe."""
    return taux_bareme.fig_taux_moyens_marginaux(
        _panneaux_successions(), couleurs=COULEURS_ETATS,
        libelles_etats={e: _lab("etat_" + e) for e in ETATS_TARIF},
        assiette_max=PART_MAX, xlabel=_lab("x_part"), ylabel=_lab("y_tarif"),
        titre=_lab("title_tarif"), xticks=(0, 15_000, 45_000, 90_000, PART_MAX), ymax=92)


def table_tarif_successions():
    """Par parenté et par part nette : taux marginal et taux moyen à chaque date."""
    return taux_bareme.table_taux(
        _panneaux_successions(), {e: _lab("court_" + e) for e in ETATS_TARIF}, PARTS_TABLE,
        entete_panneau=_lab("c_parente"), entete_assiette=_lab("c_part"))


# --- Les abattements sur les successions, en dinars courants et en dinars constants -------
#
# Trois montants de l'article 51 du code : l'abattement par enfant, ascendant à charge ou
# conjoint survivant, son plafond, et l'abattement supplémentaire par héritier handicapé.
# Vue en dinars courants : l'escalier commun (`figtools.fig_escalier`) ; la ligne de 1993,
# qui reprend les montants de 1975, y est un losange creux, sans marche.
# Vue en dinars constants : UN SEGMENT PAR ÉTAT DU DROIT (1975, 1993, 1998), jamais raccordés.
# Une année n'est tracée que si le même texte vaut aux douze premiers jours de ses mois :
# 1975 (effet le 2 janvier), 1993 (17 mai) et 1998 (17 août) se partagent entre deux états,
# et n'appartiennent à aucun segment. Dinars constants : l'indice commun du précis
# (`dinars_constants.ipc()`), année de base `dinars_constants.ANNEE_BASE`.
ABATTEMENTS = {"par_enfant_ascendant_conjoint": "#0969da", "plafond": "#8250df",
               "supplement_heritier_handicape": "#bf8700"}
FIN_ABATTEMENTS = 2026

_L.update({
    "par_enfant_ascendant_conjoint": {
        "fr": "Abattement par enfant, ascendant à charge ou conjoint",
        "ar": "الطرح عن كلّ ابن أو أصل في الكفالة أو قرين"},
    "plafond": {"fr": "Plafond de l'abattement total", "ar": "سقف الطرح الجملي"},
    "supplement_heritier_handicape": {"fr": "Supplément par héritier handicapé",
                                      "ar": "الطرح الإضافي عن كلّ وارث ذي إعاقة"},
    "y_abatt": {"fr": "Montant (dinars courants)", "ar": "المبلغ (بالدينار الجاري)"},
    "y_abatt_cst": {"fr": "Montant (dinars de {base})", "ar": "المبلغ (بدينار {base})"},
    "vue_abatt_courants": {"fr": "Dinars courants", "ar": "بالدينار الجاري"},
    "vue_abatt_constants": {"fr": "Dinars de {base}", "ar": "بدينار {base}"},
    "rupture_1993": {"fr": "code de 1993", "ar": "مجلة 1993"},
    "rupture_1998": {"fr": "loi n° 98-73", "ar": "القانون عدد 98-73"},
    "texte_1975-01-02": {"fr": "loi de finances pour 1975, art. 30",
                         "ar": "قانون المالية لسنة 1975، الفصل 30"},
    "texte_1993-05-17": {"fr": "code des droits d'enregistrement et de timbre, art. 51",
                         "ar": "مجلة معاليم التسجيل والطابع الجبائي، الفصل 51"},
    "texte_1998-08-17": {"fr": "loi n° 98-73, art. 9 et 10",
                         "ar": "القانون عدد 98-73، الفصلان 9 و10"},
    "c_grandeur": {"fr": "Grandeur", "ar": "المقدار"},
    "c_annee": {"fr": "Année", "ar": "السنة"},
    "c_texte_vigueur": {"fr": "Texte en vigueur toute l'année",
                        "ar": "النصّ النافذ طيلة السنة"},
    "c_courant": {"fr": "Montant (dinars courants)", "ar": "المبلغ (بالدينار الجاري)"},
    "c_ipc": {"fr": "Indice des prix à la consommation (1970 = 100)",
              "ar": "مؤشر أسعار الاستهلاك (1970 = 100)"},
    "c_constant": {"fr": "Montant (dinars de {base})", "ar": "المبلغ (بدينار {base})"},
    "c_effet": {"fr": "Effet", "ar": "تاريخ النفاذ"},
})

figtools.register_provenance(
    SERIE_SUCC_ABATTEMENTS,
    titre=("Abattements sur les parts recueillies en ligne directe ou entre époux, pour le "
           "droit d'enregistrement des mutations par décès, à chaque date d'effet depuis le "
           "2 janvier 1975"),
    titre_ar=("الطروح من الحصص الراجعة في الخط المباشر أو بين الزوجين، بعنوان معلوم التسجيل "
              "على نقل الملكية بالوفاة، عند كلّ تاريخ نفاذ منذ 2 جانفي 1975"),
    sources=["loi74-101-lf1975", "loi-93-53-cdet", "loi-98-73"],
    unite="dinars courants", unite_ar="بالدينار الجاري",
    perimetre=("trois montants : abattement par enfant, par ascendant à charge du défunt et par "
               "conjoint survivant ; plafond de l'abattement total ; abattement supplémentaire "
               "sur la part de chaque héritier handicapé, prévu par le code de 1993 ; une ligne "
               "par montant et par date d'effet, avec le texte du Journal officiel qui le fixe"),
    perimetre_ar=("ثلاثة مبالغ: الطرح عن كلّ ابن وكلّ أصل في كفالة الهالك وكلّ قرين باقٍ؛ سقف "
                  "الطرح الجملي؛ الطرح الإضافي من حصّة كلّ وارث ذي إعاقة، الوارد بمجلة 1993؛ "
                  "سطر لكلّ مبلغ ولكلّ تاريخ نفاذ، مع نصّ الرائد الرسمي الذي يضبطه"),
    caveats=("Le code de 1993 reprend les montants de 1975 : la ligne du 17 mai 1993 ne change "
             "pas leur valeur. L'abattement s'impute d'abord sur la part du conjoint survivant "
             "(code, art. 51, I)."),
    caveats_ar=("تعيد مجلة 1993 مبالغ 1975: لا يغيّر سطر 17 ماي 1993 قيمتها. ويُطرح المبلغ "
                "أوّلاً من حصّة القرين الباقي على قيد الحياة (المجلة، الفصل 51، I)."),
)


def _courbes_abattements() -> dict:
    return {cle: (_lab(cle), c) for cle, c in ABATTEMENTS.items()}


def _fmt_d(v: float) -> str:
    return _d(v) + (" D" if figtools.lang() == "fr" else " د")


def segments_abattements():
    """{clé: [(date d'effet, [(année, courant, indice, constant)])]} : un segment par état.

    Une année appartient au segment d'un état si la valeur de cet état est en vigueur au
    premier jour de chacun de ses douze mois. Les années de changement de texte n'appartiennent
    à aucun segment.
    """
    ipc = dinars_constants.ipc()
    base = dinars_constants.ANNEE_BASE
    etats = figtools.serie_escalier(SERIE_SUCC_ABATTEMENTS, ABATTEMENTS)
    sortie = {}
    for cle, lignes in etats.items():
        segs = []
        for i, (date, v, _etat, _texte, _lien) in enumerate(lignes):
            fin = lignes[i + 1][0] if i + 1 < len(lignes) else f"{base + 1}-01-01"
            points = []
            for annee in range(int(date[:4]), base + 1):
                mois = [f"{annee}-{m:02d}-01" for m in range(1, 13)]
                if mois[0] < date or mois[-1] >= fin or annee not in ipc or v is None:
                    continue
                points.append((annee, v, ipc[annee], v * ipc[base] / ipc[annee]))
            segs.append((date, points))
        sortie[cle] = segs
    return sortie


def fig_abattements_constants():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    base = dinars_constants.ANNEE_BASE
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    for cle, segs in segments_abattements().items():
        c = ABATTEMENTS[cle]
        premier = True
        for date, points in segs:
            if not points:
                continue
            xs, ys = [p[0] for p in points], [p[3] for p in points]
            ax.plot(xs, ys, "-o", ms=2.8, lw=1.9, color=c,
                    label=ft(_lab(cle)) if premier else None)
            premier = False
            # Une étiquette au début de chaque segment, et à la fin du dernier : deux
            # étiquettes de part et d'autre d'une rupture se chevaucheraient.
            bouts = [((xs[0], ys[0]), (-4, "right"))]
            if date == segs[-1][0]:
                bouts.append(((xs[-1], ys[-1]), (4, "left")))
            for (a, r), (dx, ha) in bouts:
                ax.annotate(ft(_d(round(r, -2))), xy=(a, r), xytext=(dx, 0),
                            textcoords="offset points", ha=ha, va="center", fontsize=7.5,
                            fontweight="bold", color=c)
            for a, v, _i, r in points:
                p, = ax.plot([a], [r], "o", ms=2.8, color=c, alpha=0)
                figtools.infobulle(p, f"{a} · {_lab(cle)} : {_fmt_d(v)} courants, "
                                      f"{_fmt_d(round(r))} de {base}")
    for annee, cle, dx, ha in ((1993, "rupture_1993", -4, "right"),
                               (1998, "rupture_1998", 4, "left")):
        figtools.marque_rupture(ax, annee)
        ax.annotate(ft(_lab(cle)), xy=(annee - 0.5, 1), xycoords=("data", "axes fraction"),
                    xytext=(dx, -4), textcoords="offset points", ha=ha, va="top",
                    fontsize=7, color="#57606a")
    ax.set_xlim(1972, base + 3.5)
    ax.set_ylim(0, None)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, _p: _d(y)))
    ax.set_xlabel(ft(_lab("c_annee")))
    ax.set_ylabel(ft(_lab("y_abatt_cst").format(base=base)))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), fontsize=8, frameon=False,
              ncol=2)
    fig.tight_layout()
    return fig


def fig_abattements():
    """Les deux vues : dinars courants en escalier, dinars constants par segments."""
    courants = figtools.fig_escalier(
        SERIE_SUCC_ABATTEMENTS, _courbes_abattements(), fin=FIN_ABATTEMENTS,
        format_valeur=_fmt_d, ylabel=_lab("y_abatt"), ylim=(0, 33_000),
        etiquettes_x={"1975-01-02": "1975", "1993-05-17": "17 mai\n1993"
                      if figtools.lang() == "fr" else "17 ماي\n1993",
                      "1998-08-17": "17 août\n1998" if figtools.lang() == "fr"
                      else "17 أوت\n1998"}, ncol=2)
    base = dinars_constants.ANNEE_BASE
    return [(_lab("vue_abatt_courants"), courants),
            (_lab("vue_abatt_constants").format(base=base), fig_abattements_constants())]


def table_abattements():
    """Une ligne par montant et par année pleine d'un même état du droit."""
    import pandas as pd

    base = dinars_constants.ANNEE_BASE
    lignes = []
    for cle, segs in segments_abattements().items():
        for date, points in segs:
            for a, v, i, r in points:
                lignes.append({_lab("c_grandeur"): _lab(cle), _lab("c_annee"): a,
                               _lab("c_texte_vigueur"): _lab("texte_" + date),
                               _lab("c_courant"): round(v),
                               _lab("c_ipc"): round(i, 1),
                               _lab("c_constant").format(base=base): round(r)})
    return pd.DataFrame(lignes)


def tableau_abattements_effet() -> str:
    """Tableau Markdown court : à chaque date d'effet, les trois montants, en dinars courants
    et en dinars de l'année de base, ces derniers déflatés par l'indice de l'année d'effet
    (moyenne annuelle), arrondis à la dizaine."""
    ipc = dinars_constants.ipc()
    base = dinars_constants.ANNEE_BASE
    etats = figtools.serie_escalier(SERIE_SUCC_ABATTEMENTS, ABATTEMENTS)
    dates = sorted({l[0] for lignes in etats.values() for l in lignes})
    courant, constant = _lab("u_courants"), _lab("u_constants").format(base=base)
    entete = [_lab("c_effet")]
    for cle in ABATTEMENTS:
        entete += [f"{_lab('court_' + cle)}<br>({courant})",
                   f"{_lab('court_' + cle)}<br>({constant})"]
    md = ["| " + " | ".join(entete) + " |", "|---" + "|---:" * (len(entete) - 1) + "|"]
    for date in dates:
        an = int(date[:4])
        cases = [f"[{date_longue(date)}]{{.insecable}}"]
        for cle in ABATTEMENTS:
            v = figtools.valeur_escalier(etats.get(cle, []), date)
            cases += (["—", "—"] if v is None
                      else [_d(v), _d(round(v * ipc[base] / ipc[an], -1))])
        md.append("| " + " | ".join(cases) + " |")
    return "\n".join(md)


_MOIS = {"fr": ("janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
                "septembre", "octobre", "novembre", "décembre"),
         "ar": ("جانفي", "فيفري", "مارس", "أفريل", "ماي", "جوان", "جويلية", "أوت",
                "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر")}


def date_longue(date: str) -> str:
    """« 1998-08-17 » -> « 17 août 1998 » ; le 1er du mois en « 1^er^ » en français."""
    a, m, j = int(date[:4]), int(date[5:7]), int(date[8:10])
    langue = figtools.lang() if figtools.lang() in _MOIS else "fr"
    jour = "1^er^" if j == 1 and langue == "fr" else str(j)
    return f"{jour} {_MOIS[langue][m - 1]} {a}"


_L.update({
    "u_courants": {"fr": "D courants", "ar": "د جارية"},
    "u_constants": {"fr": "D de {base}", "ar": "د {base}"},
    "court_par_enfant_ascendant_conjoint": {"fr": "Abattement par tête", "ar": "الطرح عن كلّ فرد"},
    "court_plafond": {"fr": "Plafond", "ar": "السقف"},
    "court_supplement_heritier_handicape": {"fr": "Supplément par héritier handicapé",
                                            "ar": "الإضافة عن كلّ وارث ذي إعاقة"},
})

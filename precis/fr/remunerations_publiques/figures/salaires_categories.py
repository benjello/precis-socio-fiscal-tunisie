"""Figure « salaire brut des fonctionnaires par catégorie statutaire » (source INS).

Deux séries de l'INS, dans DEUX CONCEPTS DIFFÉRENTS, qui ne se raccordent pas :

  - `ins-salaire-par-categorie-hors-contributions-2018-2025` — rapport 2018-2025,
    tableau 12 : salaire mensuel brut **sans contributions**, 2018-2025. C'est la série
    principale de la figure.
  - `ins-salaire-par-categorie` — enquête 2010-2021, tab20 : salaire mensuel brut **avec
    contributions**, 2015-2020. Elle reste présentée, pour mémoire, dans un panneau à part.

L'INS intitule les deux tableaux « salaire mensuel brut » sans préciser le concept. Il
est établi par recoupement : pondéré par les effectifs par catégorie, le tableau 12
redonne le salaire brut **sans** contributions du rapport, et tab20 le brut **avec** contributions
de l'enquête. Les effectifs par catégorie étant identiques dans les deux publications sur
2018-2020, l'écart ne vient pas du champ ; le rapport entre les deux séries varie de 1,14
à 1,20 selon la catégorie et l'année, et aucun coefficient ne passe de l'une à l'autre.
Les deux panneaux ne sont donc JAMAIS joints, et chaque rapport entre catégories se
calcule dans son propre concept.

    from figures import salaires_categories as sc
    sc.fig_salaires()          # deux panneaux, dinars courants
    sc.salaires_table()        # les deux séries, étiquetées (onglet Données)
    sc.fig_salaires_reel()     # la même chose en dinars constants de 2015
    sc.salaires_reel_table()

CE QUE LA FIGURE MONTRE : le resserrement de la hiérarchie, mesuré par le rapport entre
A1 et D. Brut avec contributions : 2,14 en 2015, 1,73 en 2020. Brut sans contributions :
1,92 en 2018, 1,67 en 2019, puis une lente remontée à 1,77 en 2023-2025. Les deux séries
situent l'essentiel du resserrement en 2018-2019 ; aucune ne le montre se poursuivre
après 2020.

RÉSERVE PORTÉE PAR LA SÉRIE 2015-2020 : l'INS étiquette « Catégorie A2 » la ligne que
l'arabe nomme « أ3 ». Le versement corrige l'étiquette — sans quoi deux courbes
porteraient le même nom et A3 disparaîtrait du graphique.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "ins-salaire-par-categorie-hors-contributions-2018-2025"   # principale
SERIE_AVEC = "ins-salaire-par-categorie"   # 2015-2020, brut avec contributions
SERIE_IPC = "bct-ipc-base2015"   # indice des prix, base 100 = 2015

figtools.register_provenance(
    SERIE,
    titre="Salaire mensuel brut sans contributions des fonctionnaires par catégorie statutaire, 2018-2025",
    titre_ar="الأجر الشهري الخام دون المساهمات للموظفين حسب الصنف القانوني، 2018-2025",
    sources=["ins-fonction-publique-2025"],
    raw=["data/raw/ins-fonction-publique-2018-2025/La fonction publique - 2018-2025.pdf"],
    output="data/processed/ins-fonction-publique-2018-2025/salaire_par_categorie_hors_contributions.csv",
    unite="dinars courants / mois",
    unite_ar="دينار جاري / شهر",
    perimetre=("fonctionnaires, six catégories statutaires A1 à D ; le tableau 12 est "
               "étiqueté salaire mensuel brut moyen"),
    perimetre_ar="الموظفون، ستة أصناف قانونية من أ1 إلى د؛ عنوان الجدول 12 هو معدل الأجر الشهري الخام",
    caveats=("Le tableau 12 ne précise pas à lui seul s'il s'agit du brut avec ou sans "
             "contributions. La pondération par les effectifs du tableau 6 redonne le "
             "salaire brut sans contributions du tableau 10, notion explicitement nommée "
             "par l'INS. Non raccordable au tableau 20 de l'enquête 2010-2021, qui redonne "
             "le brut avec contributions."),
    caveats_ar=("لا يبيّن الجدول 12 وحده هل يتعلق الأمر بالأجر الخام مع المساهمات أو دونها. "
                "وترجيحه بأعداد الجدول 6 يعطي الأجر الخام دون المساهمات في الجدول 10، وهي "
                "تسمية يصرّح بها المعهد. ولا تُوصل هذه السلسلة بالجدول 20 من مسح 2010-2021 "
                "الذي يعطي الأجر الخام مع المساهمات."),
    fiche="sources/ins-fonction-publique-2018-2025.md",
)

figtools.register_provenance(
    SERIE_AVEC,
    titre="Salaire mensuel brut avec contributions des fonctionnaires par catégorie statutaire, 2015-2020",
    titre_ar="الأجر الشهري الخام مع المساهمات للموظفين حسب الصنف القانوني، 2015-2020",
    sources=["ins-fonction-publique-2021"],
    raw=["data/raw/ins-fonction-publique-salaires-2010-2021/tab20_0.xlsx"],
    output="data/processed/ins-fonction-publique-salaires-2010-2021/salaire_par_categorie.csv",
    unite="dinars courants / mois",
    unite_ar="دينار جاري / شهر",
    perimetre="fonctionnaires de l'État, six catégories statutaires A1 à D",
    perimetre_ar="موظفو الدولة، ستة أصناف قانونية من أ1 إلى د",
    caveats=("Le tableau 20 est étiqueté salaire mensuel brut. La pondération par les "
             "effectifs du tableau 8 redonne les fonctionnaires du tableau 19, puis le "
             "tableau 19 pondéré redonne le salaire brut avec contributions du tableau 18, "
             "notion explicitement nommée par l'INS. La troisième ligne est libellée A2 en "
             "français mais A3 en arabe ; le libellé A3 est rétabli par position."),
    caveats_ar=("عنوان الجدول 20 هو الأجر الشهري الخام. وترجيحه بأعداد الجدول 8 يعطي أجر "
                "الموظفين في الجدول 19، ثم يعطي الجدول 19 مرجحًا الأجر الخام مع المساهمات "
                "في الجدول 18، وهي تسمية يصرّح بها المعهد. والسطر الثالث موسوم أ2 بالفرنسية "
                "وأ3 بالعربية؛ لذلك أُعيدت تسمية أ3 بحسب موضع السطر."),
    fiche="sources/ins-fonction-publique-salaires-2010-2021.md",
)

# Année de référence de la déflation : celle de la base de l'indice, pour que les dinars
# constants soient ceux d'une année réellement observée et non d'un point interpolé.
ANNEE_BASE = 2015

# Même palette que la figure des effectifs par catégorie : A en teintes froides
# (conception, encadrement), B/C/D en chaudes et neutres (maîtrise, exécution).
_CATS = ["A1", "A2", "A3", "B", "C", "D"]
_COULEURS = {"A1": "#08519c", "A2": "#3182bd", "A3": "#9ecae1",
             "B": "#fd8d3c", "C": "#d1242f", "D": "#6e7781"}

_L = {
    "titre": {"fr": "Salaire mensuel brut sans contributions des fonctionnaires "
                    "par catégorie, 2018-2025",
              "ar": "الأجر الشهري الخام دون المساهمات للموظفين حسب الصنف، 2018-2025"},
    "p_sans": {"fr": "Brut sans contributions, 2018-2025\n(INS, rapport 2018-2025)",
               "ar": "خام دون المساهمات، 2018-2025\n(المعهد الوطني للإحصاء، تقرير 2018-2025)"},
    "p_avec": {"fr": "Pour mémoire : brut avec contributions,\n2015-2020 (INS, enquête "
                     "2010-2021)\nautre concept — non raccordable",
               "ar": "للتذكير: خام مع المساهمات،\n2015-2020 (المعهد الوطني للإحصاء، "
                     "مسح 2010-2021)\nمفهوم آخر — لا يُوصَل"},
    "x": {"fr": "Année", "ar": "السنة"},
    "y": {"fr": "Dinars courants par mois", "ar": "دينار جارٍ في الشهر"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_concept": {"fr": "Concept (source)", "ar": "المفهوم (المصدر)"},
    "col_ratio": {"fr": "Rapport A1/D", "ar": "النسبة أ1/د"},
    "c_sans": {"fr": "Brut sans contributions (INS, rapport 2018-2025)",
               "ar": "خام دون المساهمات (المعهد الوطني للإحصاء، تقرير 2018-2025)"},
    "c_avec": {"fr": "Brut avec contributions (INS, enquête 2010-2021)",
               "ar": "خام مع المساهمات (المعهد الوطني للإحصاء، مسح 2010-2021)"},
    "titre_reel": {"fr": "Salaire brut sans contributions par catégorie, en dinars "
                         "constants de 2015, 2018-2024",
                   "ar": "الأجر الخام دون المساهمات حسب الصنف، بالدينار الثابت لسنة 2015، "
                         "2018-2024"},
    "p_sans_reel": {"fr": "Brut sans contributions, 2018-2024\n(indice des prix "
                          "publié jusqu'en 2024)",
                    "ar": "خام دون المساهمات، 2018-2024\n(مؤشّر الأسعار منشور حتى 2024)"},
    "y_reel": {"fr": "Dinars constants de 2015 par mois",
               "ar": "دينار ثابت لسنة 2015 في الشهر"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _wide(serie: str = SERIE):
    df = figtools.series(serie)
    w = (df.pivot(index="annee", columns="categorie", values="valeur").reset_index())
    w.columns.name = None
    w["annee"] = w["annee"].astype(int)
    return w[["annee", *[c for c in _CATS if c in w.columns]]]


def _ipc():
    """{année: indice base 100 = 2015}."""
    return {int(r.annee): float(r.valeur) for r in figtools.series(SERIE_IPC).itertuples()}


def _reel(w):
    """La même grille, en dinars constants de l'année de base.

    Une année sans indice est ÉCARTÉE, non extrapolée : l'indice s'arrête à 2024 et il
    n'existe pas de prix pour les années à venir.
    """
    w, ipc = w.copy(), _ipc()
    w = w[w["annee"].isin(ipc)]
    for c in [c for c in _CATS if c in w.columns]:
        w[c] = [v * 100 / ipc[int(a)] for a, v in zip(w["annee"], w[c])]
    return w


def _table(avec, sans, decimales: int | None = None):
    """Les deux séries l'une sous l'autre, chacune étiquetée de son concept.

    Les années 2018-2020 figurent deux fois, une par concept : c'est voulu. Le lecteur y
    voit l'écart entre les deux notions, et qu'aucune ligne n'est un raccord.
    """
    import pandas as pd
    parts = []
    for w, cle in ((avec, "c_avec"), (sans, "c_sans")):
        w = w.copy()
        w.insert(1, "concept", _lab(cle))
        w["ratio"] = (w["A1"] / w["D"]).round(2)
        parts.append(w)
    t = pd.concat(parts, ignore_index=True)
    if decimales is not None:
        t[_CATS] = t[_CATS].round(decimales)
    return t.rename(columns={"annee": _lab("col_annee"), "concept": _lab("col_concept"),
                             "ratio": _lab("col_ratio")})


def salaires_table():
    """Tableau (onglet Données) : les deux séries, dinars courants, et le rapport A1/D."""
    return _table(_wide(SERIE_AVEC), _wide(SERIE))


def salaires_reel_table():
    """Tableau (onglet Données) : les deux séries en dinars constants de 2015."""
    return _table(_reel(_wide(SERIE_AVEC)), _reel(_wide(SERIE)), decimales=1)


def _deux_panneaux(avec, sans, titre: str, titre_sans: str, ylabel: str):
    """Panneau étroit « pour mémoire » à gauche, série principale à droite ; même échelle.

    Deux axes distincts, et non deux courbes sur un même axe : rien ne doit suggérer que
    2020 (avec contributions) se prolonge en 2021 (sans contributions).
    """
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, (ax0, ax1) = plt.subplots(
        1, 2, figsize=(11, 5.6), sharey=True, layout="constrained",
        gridspec_kw={"width_ratios": [len(avec), len(sans)]})
    for ax, w, style in ((ax0, avec, dict(lw=1.4, ms=3.5, alpha=0.75)),
                         (ax1, sans, dict(lw=2.2, ms=4.5))):
        for cat in _CATS:
            if cat not in w.columns:
                continue
            ax.plot(w["annee"], w[cat], "o-", color=_COULEURS[cat], label=ft(cat), **style)
        ax.set_xticks(list(w["annee"]))
        ax.tick_params(axis="x", labelsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel(ft(_lab("x")))
    ax0.set_facecolor("#f6f8fa")
    ax0.set_title("\n".join(ft(l) for l in _lab("p_avec").split("\n")),
                  fontsize=8.5, color="#57606a")
    ax1.set_title("\n".join(ft(l) for l in titre_sans.split("\n")), fontsize=9.5)
    ax0.set_ylabel(ft(ylabel))
    ax0.set_ylim(bottom=0)
    ax1.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=9)
    fig.suptitle(ft(titre), fontsize=11.5)
    return fig


def fig_salaires():
    return _deux_panneaux(_wide(SERIE_AVEC), _wide(SERIE),
                          _lab("titre"), _lab("p_sans"), _lab("y"))


def fig_salaires_reel():
    """Le pendant déflaté : ce que la figure nominale ne peut pas montrer.

    En dinars courants la grille monte partout. Déflatée, la série sans contributions
    (2018-2024, l'indice s'arrêtant en 2024) progresse jusqu'en 2020 puis recule dans
    toutes les catégories : en 2024, toutes sont sous leur niveau réel de 2018, A1 et C
    le plus nettement. Le panneau « pour mémoire » garde la lecture 2015-2020 du concept
    avec contributions, où A1 perd du pouvoir d'achat quand B en gagne près d'un tiers.
    """
    return _deux_panneaux(_reel(_wide(SERIE_AVEC)), _reel(_wide(SERIE)),
                          _lab("titre_reel"), _lab("p_sans_reel"), _lab("y_reel"))

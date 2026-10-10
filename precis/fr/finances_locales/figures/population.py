"""Figure du chapitre d'histoire des *Finances locales* : la population par milieu communal et
non communal aux recensements, et le nombre de communes.

    from figures import population as pop
    pop.vues_population() ; pop.table_population()

D'OÙ VIENNENT LES DONNÉES.

  - `population-milieu-communal-recensements` (`tunisia-data`, lue par `figtools.series()`) :
    une ligne par recensement, grandeur, ÉDITION et tableau. Une même grandeur y est versée
    plusieurs fois ; la figure retient UNE lecture par point, comme la fiche de la série le
    propose :
      * 1966, 1975, 1984, 1994, 2004 : tableau 3 du volume 1 du recensement de 2004 (milliers
        à une décimale, part communale imprimée) — le seul tableau qui imprime les trois
        grandeurs, communal, non communal et total ;
      * 2014 : volume 1 du recensement de 2014 (effectifs). Ce volume n'imprime pas de part :
        la part communale est le rapport de ses deux effectifs, 67,7 %, valeur que le
        volume 3 imprime de son côté ;
      * 2024 : « population urbaine » et « population rurale » du Flash Démographie — une
        AUTRE classification (projet DEGURBA), tracée à part, jamais reliée.
  - `finances-locales-nombre-communes` : la petite table `COMMUNES` ci-dessous, reprise du
    tableau du chapitre (`tbl-fl-hist-communes`), ligne pour ligne. Sa provenance est déclarée
    par `figtools.register_provenance`.

RÈGLES.

  - **Six dates, pas une série annuelle** : des barres aux années des recensements, des points
    reliés par des segments droits pour la part ; ni lissage, ni interpolation.
  - **Le nombre de communes n'est pas relié** : trois dates, dont deux à cinquante-sept ans
    d'écart ; un trait entre elles serait une interpolation.
  - **La rupture est tracée** (`figtools.marque_rupture`) : les communes créées et étendues de
    2015 à 2017 couvrent tout le territoire ; « non communal » n'a plus le même sens ensuite.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "population-milieu-communal-recensements"
SERIE_COMMUNES = "finances-locales-nombre-communes"

BLEU, ORANGE, VIOLET, GRIS = "#0969da", "#d1600f", "#8250df", "#57606a"

# Lecture retenue par recensement : (édition, tableau ou None pour « tout tableau »).
EDITION_2004 = ("rgph2004-vol1", "الجدول 3")
EDITION_2014 = ("rgph2014-vol1", None)
EDITION_2024 = ("rgph2024-flash-demographie", None)
LECTURES = {1966: EDITION_2004, 1975: EDITION_2004, 1984: EDITION_2004, 1994: EDITION_2004,
            2004: EDITION_2004, 2014: EDITION_2014}
RECENSEMENTS = tuple(LECTURES)

# Nombre de communes : les trois lignes du tableau du chapitre, sans ajout. `x` est
# l'abscisse du point (15 mars 1957 ; année 2014 ; fin 2017).
COMMUNES = (
    dict(date="15 mars 1957", x=1957.2, n=94, source="src_1957"),
    dict(date="2014", x=2014.0, n=264, source="src_dg"),
    dict(date="fin 2017", x=2017.95, n=350, source="src_dg"),
)
# Décrets de création et d'extension de communes : la marque est posée entre 2015 et 2016,
# comme dans les autres figures du volume (décrets du 26 mai 2016).
RUPTURE_COMMUNES = 2016

_L = {
    "t_pop": {"fr": "Population aux recensements, par milieu",
              "ar": "السكان في التعدادات حسب الوسط"},
    "t_part": {"fr": "Part de la population vivant en milieu communal",
               "ar": "نسبة السكان المقيمين بالوسط البلدي"},
    "t_communes": {"fr": "Nombre de communes", "ar": "عدد البلديات"},
    "y_pop": {"fr": "Millions d'habitants", "ar": "ملايين السكان"},
    "y_part": {"fr": "En % de la population", "ar": "% من السكان"},
    "y_communes": {"fr": "Communes", "ar": "البلديات"},
    "x": {"fr": "Année du recensement", "ar": "سنة التعداد"},
    "x2": {"fr": "Année", "ar": "السنة"},
    "communal": {"fr": "milieu communal", "ar": "الوسط البلدي"},
    "non_communal": {"fr": "milieu non communal", "ar": "الوسط غير البلدي"},
    "total": {"fr": "total", "ar": "المجموع"},
    "lg_part": {"fr": "part communale, aux recensements de 1966 à 2014",
                "ar": "نسبة الوسط البلدي، تعدادات 1966 إلى 2014"},
    "lg_urbain": {"fr": "urbain, classification de 2024 (autre classification)",
                  "ar": "حضري، تصنيف 2024 (تصنيف آخر)"},
    "lg_communes": {"fr": "nombre de communes, aux trois dates établies",
                    "ar": "عدد البلديات في التواريخ الثلاثة الثابتة"},
    "et_urbain": {"fr": "urbain,\nclassification\nde 2024 : {v} %",
                  "ar": "حضري،\nتصنيف 2024:\n{v} %"},
    "rup": {"fr": "2015-2017 : communes créées\net étendues ; tout le territoire\n"
                  "est communal avant mai 2018",
            "ar": "2015-2017: إحداث بلديات وتوسيع أخرى؛\nكامل التراب بلدي قبل ماي 2018"},
    "vue_pop": {"fr": "Population par milieu", "ar": "السكان حسب الوسط"},
    "vue_part": {"fr": "Part communale et nombre de communes",
                 "ar": "نسبة الوسط البلدي وعدد البلديات"},
    "col_annee": {"fr": "Date", "ar": "التاريخ"},
    "col_grandeur": {"fr": "Grandeur", "ar": "المقدار"},
    "col_valeur": {"fr": "Valeur", "ar": "القيمة"},
    "col_unite": {"fr": "Unité", "ar": "الوحدة"},
    "col_source": {"fr": "Publication lue", "ar": "النشرية المقروءة"},
    "g_communal": {"fr": "population du milieu communal", "ar": "سكان الوسط البلدي"},
    "g_non_communal": {"fr": "population du milieu non communal",
                       "ar": "سكان الوسط غير البلدي"},
    "g_total": {"fr": "population totale", "ar": "مجموع السكان"},
    "g_part": {"fr": "part du milieu communal", "ar": "نسبة الوسط البلدي"},
    "g_urbain": {"fr": "population urbaine (classification de 2024)",
                 "ar": "السكان الحضريون (تصنيف 2024)"},
    "g_rural": {"fr": "population rurale (classification de 2024)",
                "ar": "السكان الريفيون (تصنيف 2024)"},
    "g_part_urbain": {"fr": "part de la population urbaine (classification de 2024)",
                      "ar": "نسبة السكان الحضريين (تصنيف 2024)"},
    "g_communes": {"fr": "nombre de communes", "ar": "عدد البلديات"},
    "u_hab": {"fr": "habitants", "ar": "نسمة"},
    "u_pct": {"fr": "%", "ar": "%"},
    "u_communes": {"fr": "communes", "ar": "بلديات"},
    "ed_2004": {"fr": "recensement de 2004, volume 1, tableau 3 (milliers à une décimale)",
                "ar": "تعداد 2004، المجلد 1، الجدول 3 (بالألف)"},
    "ed_2004_part": {"fr": "recensement de 2004, volume 1, tableau 3 (part imprimée)",
                     "ar": "تعداد 2004، المجلد 1، الجدول 3 (نسبة مطبوعة)"},
    "ed_2014": {"fr": "recensement de 2014, volume 1, p. 11 (effectifs)",
                "ar": "تعداد 2014، المجلد 1، ص. 11 (أعداد)"},
    "ed_2014_part": {"fr": ("rapport des deux effectifs du volume 1 du recensement de 2014 ; "
                            "le volume 3 imprime la même part"),
                     "ar": "نسبة محسوبة من أعداد المجلد 1 لتعداد 2014؛ يطبعها المجلد 3"},
    "ed_2024": {"fr": "recensement de 2024, Flash Démographie, p. 3",
                "ar": "تعداد 2024، نشرية الديموغرافيا، ص. 3"},
    "src_1957": {"fr": "tableau annexé à la loi municipale du 14 mars 1957",
                 "ar": "الجدول الملحق بالقانون البلدي المؤرخ في 14 مارس 1957"},
    "src_dg": {"fr": "Dafflon et Gilbert (2018), p. 34-37",
               "ar": "دافلون وجيلبار (2018)، ص. 34-37"},
}


def _lab(key: str, **valeurs) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"]).format(**valeurs)


def _ft(key: str, **valeurs) -> str:
    return "\n".join(figtools.fig_text(l) for l in _lab(key, **valeurs).split("\n"))


def _nb(v: float, d: int = 1) -> str:
    return f"{v:.{d}f}".replace(".", ",")


# La ligne « Source » ne nomme que les publications dont la figure tire ses points ; l'onglet
# « Sources » garde les six publications de la série, avec ses réserves.
figtools.register_provenance(SERIE, **{
    **figtools.meta(SERIE),
    "source_ligne": ("1966-2004 [@ins-rgph-2004-vol1, tabl. 3] ; 2014 "
                     "[@ins-rgph-2014-vol1, p. 11] ; part de 2014 et définition du milieu "
                     "communal [@ins-rgph-2014-vol3, p. 14-15 et 19] ; 2024 "
                     "[@ins-rgph-2024-flash-demographie, p. 3]"),
})
figtools.register_provenance(
    SERIE_COMMUNES,
    titre="Nombre de communes aux dates établies : 15 mars 1957, 2014 et fin 2017",
    titre_ar="عدد البلديات في التواريخ الثابتة: 15 مارس 1957، 2014 ونهاية 2017",
    sources=["dafflon-gilbert-2018"],
    source_ligne=("nombre de communes : [tableau annexé à la loi municipale]"
                  "(#r-fl-hist-1957-statut) (1957) ; 2014 et fin 2017 "
                  "[@dafflon-gilbert-2018, p. 34-37]"),
    unite="communes",
    unite_ar="بلديات",
    perimetre=("Tunisie entière ; 94 communes énumérées par le [tableau annexé à la loi "
               "municipale](#r-fl-hist-1957-statut), publiée le 15 mars 1957 ; 264 communes "
               "en 2014 et 350 à la fin de 2017 selon Dafflon et Gilbert (2018), p. 34-37"),
    perimetre_ar="كامل البلاد التونسية؛ 94 بلدية سنة 1957، 264 سنة 2014 و350 في نهاية 2017",
    caveats=("Trois dates seulement, non reliées : le nombre de communes entre 1957 et 2014 "
             "n'est pas établi."),
    caveats_ar="ثلاثة تواريخ فقط، غير موصولة: عدد البلديات بين 1957 و2014 غير ثابت.",
)


def _lecture(df, annee: int, grandeur: str, edition: str, tableau: str | None):
    """LA ligne retenue pour un recensement et une grandeur : une seule, ou une erreur."""
    m = ((df["recensement"] == annee) & (df["grandeur"] == grandeur)
         & (df["edition"] == edition))
    if tableau is not None:
        m &= df["tableau"] == tableau
    lignes = df[m]
    if len(lignes) != 1:
        raise ValueError(f"{annee} {grandeur} {edition} {tableau} : {len(lignes)} ligne(s), "
                         "une seule attendue")
    return lignes.iloc[0]


def _population() -> dict:
    """{année: dict(communal, non_communal, total, part, part_imprimee)} en habitants et %."""
    df = figtools.series(SERIE)
    out = {}
    for annee, (edition, tableau) in LECTURES.items():
        l = {g: _lecture(df, annee, g, edition, tableau)
             for g in ("communal", "non_communal", "total")}
        v = {g: float(l[g]["valeur_personnes"]) for g in l}
        pas = float(l["total"]["pas_imprime_personnes"])
        # Les deux milieux bouclent sur le total, à la précision imprimée près.
        assert abs(v["communal"] + v["non_communal"] - v["total"]) <= 2 * pas, annee
        imprimee = l["communal"]["part_imprimee_pct"]
        imprimee = None if imprimee != imprimee else float(imprimee)  # NaN : pas de part
        part = imprimee if imprimee is not None else 100 * v["communal"] / v["total"]
        out[annee] = dict(**v, part=part, part_imprimee=imprimee is not None)
    return out


def _urbain_2024() -> dict:
    df = figtools.series(SERIE)
    u = _lecture(df, 2024, "urbain", *EDITION_2024)
    r = _lecture(df, 2024, "rural", *EDITION_2024)
    return dict(urbain=float(u["valeur_personnes"]), rural=float(r["valeur_personnes"]),
                part=float(u["part_imprimee_pct"]))


def table_population():
    """Données des deux vues, en long : une ligne par date et par grandeur."""
    import pandas as pd
    lignes = []

    def ligne(date, grandeur, valeur, unite, source):
        lignes.append({_lab("col_annee"): date, _lab("col_grandeur"): _lab(grandeur),
                       _lab("col_valeur"): valeur, _lab("col_unite"): _lab(unite),
                       _lab("col_source"): _lab(source)})

    for annee, p in _population().items():
        ed = "ed_2014" if annee == 2014 else "ed_2004"
        for g in ("communal", "non_communal", "total"):
            ligne(str(annee), "g_" + g, int(p[g]), "u_hab", ed)
        ligne(str(annee), "g_part", round(p["part"], 1), "u_pct",
              ed + "_part")
    u = _urbain_2024()
    ligne("2024", "g_urbain", int(u["urbain"]), "u_hab", "ed_2024")
    ligne("2024", "g_rural", int(u["rural"]), "u_hab", "ed_2024")
    ligne("2024", "g_part_urbain", round(u["part"], 1), "u_pct", "ed_2024")
    for c in COMMUNES:
        ligne(c["date"], "g_communes", c["n"], "u_communes", c["source"])
    return pd.DataFrame(lignes, dtype=object)  # entiers et parts, sans « .0 »


def fig_population():
    """Vue 1 : barres empilées aux six recensements, en millions d'habitants."""
    figtools.apply_lang_font()
    pop = _population()
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    largeur = 5.0
    for annee, p in pop.items():
        c, n = p["communal"] / 1e6, p["non_communal"] / 1e6
        ax.bar(annee, n, width=largeur, color=ORANGE, zorder=2)
        ax.bar(annee, c, width=largeur, bottom=n, color=BLEU, zorder=2)
        ax.text(annee, n / 2, _nb(n), ha="center", va="center", color="white", fontsize=9)
        ax.text(annee, n + c / 2, _nb(c), ha="center", va="center", color="white",
                fontsize=9)
        ax.text(annee, n + c + 0.12, figtools.fig_text(f"{_lab('total')} {_nb(n + c)}"),
                ha="center", va="bottom", color=GRIS, fontsize=8)
    ax.set_title(figtools.fig_text(_lab("t_pop")), fontsize=10.5)
    ax.set_ylabel(figtools.fig_text(_lab("y_pop")))
    ax.set_xlabel(figtools.fig_text(_lab("x")))
    ax.set_xticks(list(pop))
    ax.set_xlim(1961, 2019)
    ax.set_ylim(0, 12.5)
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(handles=[Patch(color=BLEU, label=figtools.fig_text(_lab("communal"))),
                       Patch(color=ORANGE, label=figtools.fig_text(_lab("non_communal")))],
              loc="upper left", fontsize=8.5, frameon=False)
    fig.tight_layout()
    return fig


def fig_part_communes():
    """Vue 2 : part communale (haut) et nombre de communes (bas), même axe des années."""
    figtools.apply_lang_font()
    pop = _population()
    u = _urbain_2024()
    fig, (haut, bas) = plt.subplots(2, 1, figsize=(9.5, 6.6), sharex=True,
                                    gridspec_kw=dict(height_ratios=[2.1, 1], hspace=0.16))
    # Part communale : six points, segments droits.
    annees = list(pop)
    haut.plot(annees, [pop[a]["part"] for a in annees], color=BLEU, marker="o", ms=5.5,
              lw=1.6, zorder=3)
    for a in annees:
        haut.annotate(f"{_nb(pop[a]['part'])} %", xy=(a, pop[a]["part"]),
                      xytext=(-6 if a == 2014 else 0, 8),  # 2014 : à l'écart de la rupture
                      textcoords="offset points", ha="right" if a == 2014 else "center", va="bottom", fontsize=9.5,
                      color=BLEU)
    # 2024 : autre classification — marque distincte, non reliée.
    haut.plot([2024], [u["part"]], color=VIOLET, marker="D", mfc="white", ms=7, mew=1.6,
              ls="", zorder=3)
    haut.annotate(_ft("et_urbain", v=_nb(u["part"], 0)), xy=(2024, u["part"]),
                  xytext=(0, -10), textcoords="offset points", ha="center", va="top",
                  fontsize=8.5, color=VIOLET)
    haut.set_title(figtools.fig_text(_lab("t_part")), fontsize=10.5)
    haut.set_ylabel(figtools.fig_text(_lab("y_part")))
    haut.set_ylim(30, 82)
    haut.grid(True, alpha=0.3)
    figtools.marque_rupture(haut, RUPTURE_COMMUNES)
    haut.annotate(_ft("rup"), xy=(RUPTURE_COMMUNES - 0.5, 0), xycoords=("data", "axes fraction"),
                  xytext=(-5, 5), textcoords="offset points", ha="right", va="bottom",
                  fontsize=8.5, color=GRIS)
    # Nombre de communes : trois dates, non reliées.
    for c in COMMUNES:
        bas.vlines(c["x"], 0, c["n"], color=GRIS, lw=1.2, zorder=2)
        bas.plot([c["x"]], [c["n"]], color=GRIS, marker="s", ms=6, ls="", zorder=3)
    decal = {94: (7, 0, "left"), 264: (-7, 0, "right"), 350: (7, 0, "left")}
    for c in COMMUNES:
        dx, dy, ha = decal[c["n"]]
        bas.annotate(figtools.fig_text(f"{c['n']} ({c['date']})") if figtools.lang() == "fr"
                     else str(c["n"]), xy=(c["x"], c["n"]), xytext=(dx, dy),
                     textcoords="offset points", ha=ha, va="center", fontsize=9.5, color=GRIS)
    figtools.marque_rupture(bas, RUPTURE_COMMUNES)
    bas.set_title(figtools.fig_text(_lab("t_communes")), fontsize=10.5)
    bas.set_ylabel(figtools.fig_text(_lab("y_communes")))
    bas.set_xlabel(figtools.fig_text(_lab("x2")))
    bas.set_ylim(0, 420)
    bas.set_xlim(1954, 2029)
    bas.set_xticks([1957, 1966, 1975, 1984, 1994, 2004, 2014, 2024])
    bas.grid(True, alpha=0.3)
    poignees = [
        Line2D([], [], color=BLEU, marker="o", lw=1.6, label=figtools.fig_text(_lab("lg_part"))),
        Line2D([], [], color=VIOLET, marker="D", mfc="white", mew=1.6, ls="",
               label=figtools.fig_text(_lab("lg_urbain"))),
        Line2D([], [], color=GRIS, marker="s", ls="",
               label=figtools.fig_text(_lab("lg_communes"))),
    ]
    bas.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.42), ncol=2,
               fontsize=8.8, frameon=False)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.95, bottom=0.17)
    return fig


def vues_population():
    return [(_lab("vue_pop"), fig_population()), (_lab("vue_part"), fig_part_communes())]

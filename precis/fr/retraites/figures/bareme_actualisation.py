"""Figures « barème d'actualisation des salaires » du régime des salariés non agricoles.

    from figures import bareme_actualisation as ba
    ba.fig_taux()              # taux annuels : barème de 2024, inflation, PIB nominal
    ba.taux_table()

LE CONSTAT. Aucun texte ne dit sur quoi le barème est établi : l'article 18 du décret
n° 74-499, dans sa rédaction de 1994, prévoit un barème « fixé annuellement par arrêté », et
les arrêtés ne donnent que leurs visas et la liste des coefficients. Ces coefficients
reproduisent pourtant l'évolution de l'indice des prix à la consommation : le rapport des
coefficients de deux années voisines — le taux d'actualisation implicite d'une année sur
l'autre — est le taux d'inflation de l'année. Les figures le montrent sans en déduire une règle — le précis
constate, il n'attribue pas de méthode à l'administration.

CE QUE LES FIGURES DOIVENT PORTER :
  - en taux annuels, dans le barème de 2024, le taux implicite et l'inflation **se
    confondent** de 1963 à 2023 : l'écart ne dépasse jamais 0,23 point, et vaut 0,03 point
    en moyenne. La croissance du PIB nominal, elle, est presque toujours au-dessus : 13,0 %
    par an en moyenne de 1963 à 1990 contre 6,2 % pour les prix, 8,7 % contre 3,9 % de
    1991 à 2010, 6,5 % contre 6,0 % de 2011 à 2023. Le salaire de référence est donc
    actualisé sur les prix, non sur la croissance des revenus ;
  - le constat ne tient pas au seul barème de 2024. Contrôle fait le 21 septembre 2026 et
    refait le 24 septembre sur les trente et un barèmes, sans figure : confronté à l'indice
    des prix de sa dernière année de salaire (inflation de la série des croissances,
    chaînée), chacun s'en écarte de moins de 0,4 %, sauf ceux de 2013 à 2016, qui s'en
    éloignent jusqu'à 1,1 % sur les salaires de 1997 ; celui de 2017 retrouve l'écart
    antérieur.

CE QUI N'EST PAS AFFIRMÉ :
  - que l'administration calcule le barème sur l'indice de l'INS : les textes ne le disent
    pas ;
  - une précision supérieure à celle de la comparaison : les taux d'inflation sont ceux
    publiés par plusieurs éditions de l'annuaire statistique, avec un raccord de bases en
    1970 ; le plus grand écart annuel, 0,23 point, tombe en 1973 ;
  - que le PIB nominal mesure les salaires : c'est le seul agrégat de revenu connu sur
    toute la période, et sa croissance comprend celle de la population et de l'emploi.
    Les salaires par tête sont tracés en BRUT, comme les salaires que le barème actualise :
    salaires et traitements bruts des comptes de la nation, sans les charges sociales des
    employeurs, rapportés au nombre de salariés de l'enquête emploi, tous salariés, de
    2002 à 2012 — sans 2004 ni 2005, année de recensement, et avec un changement de mesure
    de l'emploi en 2011. La série construite pour 2013-2021, hors administration centrale
    et hors fonction publique, n'est PAS tracée : son dénominateur combine l'emploi total
    de la BCT, une part de salariés modélisée par le BIT et les effectifs de la fonction
    publique, et chacun de leurs à-coups se reporte en sens inverse sur le salaire par tête
    (+10,1 % en 2015, +2,3 % en 2016, +10,7 % en 2020). Elle est remplacée par les
    salaires déclarés à la CNSS dans le privé : de 2001 à 2025, le taux de l'INS suit le
    salaire des mêmes « salariés permanents » (déclarés cinq trimestres de suite, hausses
    individuelles hors de [-5 % ; +10 %] exclues) — ce n'est pas l'évolution du salaire
    moyen. Pour 2001-2007, il vient du premier portail de l'INS, dont les pages ne nomment
    pas la CNSS et ne documentent pas la méthode : l'appui sur les salaires déclarés est
    déduit de la continuité de l'indicateur (même code, mêmes valeurs sur 2007-2009) ; de 1995 à 2000, la Banque mondiale donne la croissance du salaire annuel moyen
    des salariés déclarés, années incomplètes comprises ;
  - 1962 n'a pas de taux d'inflation : l'indice des prix commence cette année-là.

RUPTURES DE SÉRIE, MARQUÉES SUR LES FIGURES : le raccord de deux bases de l'indice des prix
en 1970, et le changement de mesure de l'emploi en 2011 (enquête de mai, puis moyenne des
trimestres), qui touche le salaire brut par salarié. Le PIB nominal n'en porte plus : la
série de la Banque mondiale accolait deux bases sans les raccorder en 1997 (+20,3 % affiché)
et en 2010 (+12,7 %) ; tunisia-data calcule désormais chaque taux sur deux années d'une même
base — UNdata pour 1993-2001, éditions des comptes de la nation ensuite —, soit +9,6 % et
+7,5 %. Avant 1993, le taux reste celui de la Banque mondiale, sans contrôle possible.

Chaque année de 1994 à 2024 a son barème. Aucun arrêté n'est retrouvé pour 2025 ni pour
2026 : la série s'arrête au barème de 2024.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_BAREME = "rsna-actualisation-salaires"   # paramètres datés, un arrêté par barème
SERIE_CROISSANCES = "croissances-revenus-prix"  # taux annuels, source par ligne

PRIX = "prix à la consommation"
PIB = "PIB nominal"
# Salaire BRUT par tête — le barème actualise des salaires bruts —, tous salariés, 2002-2012
# (sans 2004-2005, changement de mesure de l'emploi en 2011).
SAL = "salaires bruts par salarié"
# Salaires DÉCLARÉS À LA CNSS dans le privé : évolution du salaire des mêmes salariés
# permanents, privé non agricole, 2001-2025 (INS) ; salaire annuel moyen des salariés
# déclarés, 1995-2000 (Banque mondiale, 2004). Les deux ne se raccordent pas.
CNSS = "salaire déclaré CNSS, privé non agricole (salariés permanents)"
CNSS_BM = "salaire annuel moyen déclaré CNSS"

# Les séries de salaires tracées, dans l'ordre de la légende : (indicateur de la série des
# croissances, clé de légende, clé de colonne, style, couleur). Trois familles, que la
# couleur distingue et qu'aucun trait ne relie : salaire déclaré à la CNSS (verts et
# violet), salaire moyen des secteurs non agricoles hors administration d'après les données
# du ministère du Plan (orangés), comptes nationaux (rouge). Chaque série vient d'une seule
# source ; aucune n'est raccordée à une autre. La masse des salaires déclarés à la CNSS
# (BCT, 1960-1975) n'est pas tracée : sa croissance mêle salaires et affiliation.
SALAIRES = (
    ("salaire moyen déclaré à la CNSS, BCT", "lg_cnss_bct", "col_cnss_bct", "v-.", "#116329"),
    (CNSS_BM, "lg_cnss_bm", "col_cnss_bm", "^:", "#1a7f37"),
    (CNSS, "lg_cnss_ins", "col_cnss_ins", "s-", "#8250df"),
    ("salaire moyen non agricole hors administration, Banque mondiale 1995", "lg_plan_bm",
     "col_plan_bm", "D-", "#bc4c00"),
    ("salaire moyen non agricole hors administration, FMI 97/57", "lg_plan_fmi",
     "col_plan_fmi", "X", "#953800"),
    ("salaire annuel moyen des secteurs productifs non agricoles, BCT", "lg_plan_bct",
     "col_plan_bct", "d--", "#9a6700"),
    (SAL, "lg_sal", "col_sal", "o--", "#cf222e"),
)

figtools.register_provenance(
    SERIE_BAREME,
    titre="Barème d'actualisation des salaires du régime des salariés non agricoles, 1994-2024",
    titre_ar="جدول تحيين الأجور في نظام الأجراء غير الفلاحيين، 1994-2024",
    sources=["arrete-1994-11-17-bareme-actualisation", "arrete-2024-07-16-bareme-actualisation"],
    unite="coefficient multiplicateur",
    unite_ar="ضارب",
    perimetre=("trente et un arrêtés du ministre des affaires sociales, du 17 novembre 1994 au "
               "16 juillet 2024 : un coefficient par année de salaire depuis 1961 ; chaque ligne "
               "des données porte l'arrêté qui le fixe et son lien au Journal officiel"),
    perimetre_ar=("واحد وثلاثون قراراً لوزير الشؤون الاجتماعية، من 17 نوفمبر 1994 إلى 16 جويلية "
                  "2024: ضارب لكلّ سنة أجر منذ 1961"),
    caveats=("Aucun arrêté retrouvé pour 2025 ni pour 2026. Le barème de 2013 est recalculé, "
             "ceux de 2014 à 2016 en reprennent le calcul, et celui de 2017 revient au calcul "
             "antérieur pour les salaires d'avant 2011. L'arrêté de 2019 n'a été trouvé que "
             "dans l'édition arabe du Journal officiel. Le barème de 1996 est lu sur un scan, celui "
             "de 2024 sur l'image insérée dans le fascicule."),
    caveats_ar=("لم يُعثر على قرار لسنتي 2025 و2026. أُعيد احتساب جدول 2013، وأخذت جداول 2014 "
                "إلى 2016 بالاحتساب نفسه، وعاد جدول 2017 إلى الاحتساب السابق بالنسبة إلى أجور "
                "ما قبل 2011."),
)

_L = {
    "titre_taux": {
        "fr": "Barème d'actualisation de 2024, inflation, PIB nominal et salaires, 1962-2023",
        "ar": "جدول التحيين لسنة 2024 والتضخّم والناتج الاسمي والأجور، 1962-2023"},
    "x_annee_sal": {"fr": "Année de salaire", "ar": "سنة الأجر"},
    "y_taux": {"fr": "Taux d'une année sur l'autre (%)", "ar": "النسبة من سنة إلى أخرى (%)"},
    "lg_bareme": {"fr": "Taux implicite du barème de 2024", "ar": "النسبة الضمنية لجدول 2024"},
    "lg_prix": {"fr": "Inflation (prix à la consommation)", "ar": "التضخّم (أسعار الاستهلاك)"},
    "lg_pib": {"fr": "Croissance du PIB nominal", "ar": "نموّ الناتج المحلي الإجمالي الاسمي"},
    "lg_sal": {"fr": "Salaire brut par salarié", "ar": "الأجر الخام لكلّ أجير"},
    "lg_cnss_bct": {"fr": "Salaire moyen déclaré à la CNSS (BCT)",
                    "ar": "معدّل الأجر المصرّح به للصندوق (البنك المركزي)"},
    "lg_plan_bm": {"fr": "Salaire moyen non agricole hors administration (Plan, Banque mondiale 1995)",
                   "ar": "معدّل الأجر خارج الفلاحة والإدارة (التخطيط، البنك الدولي 1995)"},
    "lg_plan_fmi": {"fr": "Salaire moyen non agricole hors administration (Plan, FMI 1997)",
                    "ar": "معدّل الأجر خارج الفلاحة والإدارة (التخطيط، صندوق النقد الدولي 1997)"},
    "lg_plan_bct": {"fr": "Salaire moyen des secteurs productifs non agricoles (BCT)",
                    "ar": "معدّل أجر القطاعات المنتجة غير الفلاحية (البنك المركزي)"},
    "lg_cnss_ins": {"fr": "Salaire déclaré à la CNSS, salariés permanents du privé non agricole (INS)",
                    "ar": "الأجر المصرّح به للصندوق، الأجراء القارّون في القطاع الخاص غير الفلاحي (المعهد الوطني للإحصاء)"},
    "lg_cnss_bm": {"fr": "Salaire annuel moyen déclaré à la CNSS (Banque mondiale)",
                   "ar": "معدّل الأجر السنوي المصرّح به للصندوق (البنك الدولي)"},
    "titre_recent": {
        "fr": "Barème d'actualisation de 2024, inflation, PIB nominal et salaires, 1995-2023",
        "ar": "جدول التحيين لسنة 2024 والتضخّم والناتج الاسمي والأجور، 1995-2023"},
    "rup_prix": {"fr": "prix : raccord de bases", "ar": "الأسعار: ربط قاعدتين"},
    "rup_cnss": {"fr": "CNSS : effectif redéfini", "ar": "الصندوق: إعادة تعريف العدد"},
    "rup_emploi": {"fr": "emploi : rupture", "ar": "التشغيل: انقطاع"},
    "confondues": {"fr": "barème et inflation\nse confondent", "ar": "الجدول والتضخّم\nمتطابقان"},
    "col_annee_sal": {"fr": "Année de salaire", "ar": "سنة الأجر"},
    "col_coef": {"fr": "Coefficient du barème de 2024", "ar": "ضارب جدول 2024"},
    "col_taux_bareme": {"fr": "Taux implicite du barème (%)", "ar": "النسبة الضمنية للجدول (%)"},
    "col_prix": {"fr": "Inflation (%)", "ar": "التضخّم (%)"},
    "col_pib": {"fr": "Croissance du PIB nominal (%)", "ar": "نموّ الناتج الاسمي (%)"},
    "col_sal": {"fr": "Salaire brut par salarié (%)", "ar": "الأجر الخام لكلّ أجير (%)"},
    "col_cnss_bct": {"fr": "Salaire moyen déclaré, BCT (%)", "ar": "معدّل الأجر المصرّح به، البنك المركزي (%)"},
    "col_plan_bm": {"fr": "Salaire non agricole hors administration, Banque mondiale 1995 (%)",
                    "ar": "الأجر خارج الفلاحة والإدارة، البنك الدولي 1995 (%)"},
    "col_plan_fmi": {"fr": "Salaire non agricole hors administration, FMI 1997 (%)",
                     "ar": "الأجر خارج الفلاحة والإدارة، صندوق النقد الدولي 1997 (%)"},
    "col_plan_bct": {"fr": "Salaire des secteurs productifs non agricoles, BCT (%)",
                     "ar": "أجر القطاعات المنتجة غير الفلاحية، البنك المركزي (%)"},
    "col_cnss_ins": {"fr": "Salaire déclaré, salariés permanents, INS (%)",
                     "ar": "الأجر المصرّح به، الأجراء القارّون (%)"},
    "col_cnss_bm": {"fr": "Salaire annuel moyen déclaré, Banque mondiale (%)",
                    "ar": "معدّل الأجر السنوي المصرّح به (%)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _baremes():
    """{date d'application: {année de salaire: coefficient}} et {date: arrêté}."""
    coef, arrete = {}, {}
    for r in figtools.series(SERIE_BAREME).itertuples():
        coef.setdefault(r.bareme, {})[int(r.annee_salaires)] = float(r.coefficient)
        arrete[r.bareme] = r.arrete
    return coef, arrete


def _taux():
    """[(année, coef. 2024, taux implicite, inflation, PIB nominal, {indicateur: taux})].

    Le taux implicite d'une année est le rapport des coefficients de l'année précédente et
    de l'année, moins un : de combien le barème de 2024 revalorise l'une par rapport à
    l'autre. Les autres sont les taux publiés, None là où ils manquent ; le dictionnaire
    porte les séries de salaires de `SALAIRES`, qui restent DISTINCTES.
    """
    coef, _ = _baremes()
    c = coef[max(coef)]
    d = figtools.series(SERIE_CROISSANCES)
    voulus = {PRIX, PIB} | {s[0] for s in SALAIRES}
    taux = {(r.indicateur, int(r.annee)): float(r.croissance_pct) for r in d.itertuples()
            if r.indicateur in voulus}
    return [(a, c[a], 100 * (c[a - 1] / c[a] - 1), taux.get((PRIX, a)), taux.get((PIB, a)),
             {s[0]: taux.get((s[0], a)) for s in SALAIRES})
            for a in sorted(c) if a - 1 in c]


def _suites(pts):
    """Découpe [(année, valeur)] en suites d'années consécutives : un trou n'est jamais relié."""
    out = []
    for t in pts:
        if out and t[0] == out[-1][-1][0] + 1:
            out[-1].append(t)
        else:
            out.append([t])
    return out


def _table(d):
    import pandas as pd
    return pd.DataFrame([
        {_lab("col_annee_sal"): a, _lab("col_coef"): c,
         _lab("col_taux_bareme"): round(b, 2), _lab("col_prix"): p, _lab("col_pib"): n,
         **{_lab(col): sal[ind] for ind, _, col, _, _ in SALAIRES}}
        for a, c, b, p, n, sal in d]).dropna(axis=1, how="all")


def taux_table():
    return _table(_taux())


def taux_recent_table(debut: int = 1995):
    # Les séries qui n'ont aucune valeur sur la période sont retirées des données.
    return _table([t for t in _taux() if t[0] >= debut]).dropna(axis=1, how="all")


# Ruptures de série : (année, clé de libellé). Voir l'en-tête du module.
RUPTURES = ((1970, "rup_prix"), (1971, "rup_cnss"), (2011, "rup_emploi"))


def _ruptures(ax, ft, debut):
    """Trait pointillé et court libellé à chaque rupture de série de la période tracée."""
    # En bas du cadre, là où la légende n'est pas : le libellé monte depuis l'axe.
    bas, haut = ax.get_ylim()
    for annee, cle in RUPTURES:
        if annee < debut:
            continue
        ax.axvline(annee, color="#8b949e", lw=0.8, ls=":", zorder=0)
        ax.text(annee - 0.15, bas + 0.02 * (haut - bas), ft(_lab(cle)), rotation=90,
                fontsize=6.5, color="#57606a", ha="right", va="bottom")


def _trace(ax, d, ft, ms=4):
    """Trace les séries de `d` ; les séries par marques ne relient jamais un trou."""
    pib = [(t[0], t[4]) for t in d if t[4] is not None]
    ax.plot([a for a, _ in pib], [n for _, n in pib], "-", color="#6e7781", lw=1.6,
            label=ft(_lab("lg_pib")))
    prix = [(t[0], t[3]) for t in d if t[3] is not None]
    ax.plot([a for a, _ in prix], [p for _, p in prix], "-", color="#bf8700", lw=5, alpha=0.45,
            label=ft(_lab("lg_prix")))
    # Le barème par-dessus, trait fin : on le voit courir dans la bande de l'inflation.
    ax.plot([t[0] for t in d], [t[2] for t in d], "-", color="#08519c", lw=1.6,
            label=ft(_lab("lg_bareme")))
    for ind, lg, _, style, coul in SALAIRES:
        pts = [(t[0], t[5][ind]) for t in d if t[5][ind] is not None]
        for k, suite in enumerate(_suites(pts)):
            ax.plot([a for a, _ in suite], [v for _, v in suite], style, color=coul,
                    lw=1.2, ms=ms, label=ft(_lab(lg)) if k == 0 else None)


def _axes(ax, ft, titre):
    ax.axhline(0, color="#6e7781", lw=0.8)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda v, _: f"{v:g}".replace(".", ",")))
    ax.set_xlabel(ft(_lab("x_annee_sal")))
    ax.set_ylabel(ft(_lab("y_taux")))
    ax.set_title(ft(_lab(titre)))
    ax.grid(True, alpha=0.3)


def fig_taux():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _taux()

    fig, ax = plt.subplots(figsize=(9.5, 7.2))
    _trace(ax, d, ft)
    b1990 = next(t[2] for t in d if t[0] == 1990)
    ax.annotate("\n".join(ft(l) for l in _lab("confondues").split("\n")),
                xy=(1990, b1990), xytext=(2004, 25),
                fontsize=7.5, color="#57606a", ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color="#8b949e", lw=0.8, shrinkA=2, shrinkB=4),
                bbox=dict(boxstyle="round,pad=0.35", fc="#f6f8fa", ec="#8b949e", lw=0.6,
                          alpha=0.95))
    ax.set_xticks(range(1965, 2024, 5))
    _axes(ax, ft, "titre_taux")
    _ruptures(ax, ft, d[0][0])
    _legende(ax)
    fig.tight_layout()
    return fig


def _legende(ax):
    """Légende sous le cadre, sur deux colonnes : dix séries ne tiennent pas dans le tracé."""
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=7,
              frameon=False)


def fig_taux_recent(debut: int = 1995):
    """La même figure, resserrée sur les années où les salaires sont connus : toutes les
    courbes de la longue période, à une échelle où leurs écarts se lisent."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = [t for t in _taux() if t[0] >= debut]

    fig, ax = plt.subplots(figsize=(9.5, 7.2))
    _trace(ax, d, ft, ms=5)
    ax.set_xticks([a for a in range(debut, 2024) if a % 5 == 0])
    ax.set_xticks([t[0] for t in d], minor=True)
    _axes(ax, ft, "titre_recent")
    _ruptures(ax, ft, debut)
    _legende(ax)
    fig.tight_layout()
    return fig

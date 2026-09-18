"""Figure « augmentations générales des salaires par catégorie statutaire ».

Origine des données : les DÉCRETS d'augmentation générale, lus au Journal officiel et
relevés dans `augmentations/augmentations-fonction-publique.csv`. Ce n'est pas une
statistique mais du droit : chaque montant est celui qu'un décret identifié fixe.

Le relevé est versionné DANS le livre, à côté du chapitre : la figure le lit donc
directement, sans passer par l'entrepôt ni par un instantané. C'est la différence avec
`pnafn.py`, dont la série vient des paramètres d'un dépôt absent du build.

CE QUE LA FIGURE MONTRE. Le cumul, par catégorie, des tranches acquises depuis 2016 :
ce qu'un agent a gagné en dinars mensuels, et non le montant d'une tranche isolée. Le
cumul est CALCULÉ, non lu — aucun texte ne l'énonce.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402
import augmentations as aug  # noqa: E402

HERE = Path(__file__).resolve().parent
CSV = HERE.parent / "augmentations" / "augmentations-fonction-publique.csv"
SERIE = "augmentations-fonction-publique"
SERIE_IPC = "bct-ipc-base2015"   # indice des prix, base 100 = 2015

# Les six catégories statutaires. Les postes d'ouvriers sont écartés du graphique : leur
# découpage change d'un décret à l'autre (tantôt en bloc, tantôt la 3e unité à part), si
# bien qu'une courbe continue leur donnerait une homogénéité qu'ils n'ont pas. Ils
# figurent dans le tableau des montants.
CATEGORIES = ["A1", "A2", "A3", "B", "C", "D"]

# C ET D SONT CONFONDUES, ET C'EST UN FAIT DE DROIT : les sept décrets leur accordent le
# même montant à chacune des quinze dates d'effet — vérifié, quinze sur quinze. Tracées
# séparément, la seconde recouvrait exactement la première : la légende annonçait six
# courbes quand l'œil n'en voyait que cinq, et l'entrée « C » ne désignait rien. On trace
# donc une seule ligne, nommée pour ce qu'elle est. A1 et A2 divergent à compter du
# 1er octobre 2022, A3 et B ne coïncident jamais : elles restent distinctes.
_TRACEES = [("A1", "A1"), ("A2", "A2"), ("A3", "A3"), ("B", "B"), ("C et D", "C")]

_COULEURS = {"A1": "#08519c", "A2": "#3182bd", "A3": "#9ecae1",
             "B": "#fd8d3c", "C et D": "#6e7781"}

figtools.register_provenance(
    SERIE,
    titre="Augmentations générales des salaires de la fonction publique, par catégorie",
    titre_ar="الزيادات العامة في أجور الوظيفة العمومية، حسب الصنف",
    sources=list(aug.DECRETS),
    unite="dinars par mois (montants fixés par décret)",
    unite_ar="دينار في الشهر (مبالغ محدّدة بأمر)",
    perimetre="agents de l'État, des collectivités locales et des établissements publics "
              "à caractère administratif",
    perimetre_ar="أعوان الدولة والجماعات المحلية والمؤسسات العمومية ذات الصبغة الإدارية",
    caveats=("Les décrets fixent des montants en dinars, jamais des pourcentages. Le "
             "cumul tracé additionne les tranches acquises : il est calculé, et ne "
             "figure comme tel dans aucun texte. Le décret n° 2015-462 n'énonce aucune "
             "date d'effet et reste hors de la série. Avant 2015, les augmentations "
             "étaient accordées par corps et ne se rangent pas par catégorie."),
    caveats_ar=("تحدّد الأوامر مبالغ بالدينار لا نسباً مئوية. والتراكم المرسوم يجمع "
                "الأقساط المكتسبة: فهو محسوب ولا يرد بهذه الصفة في أيّ نصّ. ولا يذكر "
                "الأمر عدد 2015-462 أيّ تاريخ سريان فيبقى خارج السلسلة. وقبل 2015 كانت "
                "الزيادات تُسند حسب الأسلاك ولا تنتظم حسب الأصناف."),
)

_L = {
    "titre": {"fr": "Augmentations générales cumulées par catégorie statutaire, 2016-2028",
              "ar": "الزيادات العامة المتراكمة حسب الصنف القانوني، 2016-2028"},
    "x": {"fr": "Date d'effet", "ar": "تاريخ السريان"},
    "y": {"fr": "Cumul des augmentations (dinars par mois)",
          "ar": "تراكم الزيادات (دينار في الشهر)"},
    "col_date": {"fr": "Date d'effet", "ar": "تاريخ السريان"},
    "titre_reel": {"fr": "Augmentations cumulées par catégorie, en dinars constants de 2015",
                   "ar": "الزيادات المتراكمة حسب الصنف، بالدينار الثابت لسنة 2015"},
    "y_reel": {"fr": "Cumul en dinars constants de 2015 (par mois)",
               "ar": "التراكم بالدينار الثابت لسنة 2015 (في الشهر)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _rangs():
    return aug.charge(CSV)


def table():
    """Tableau (onglet Données) : cumul par catégorie à chaque date d'effet."""
    import pandas as pd
    rangs = _rangs()
    dates = aug.dates_presentes(rangs)
    cumuls = {c: dict(aug.serie_cumulee(rangs, c)) for c in CATEGORIES}
    return pd.DataFrame([
        {_lab("col_date"): aug.formate_date(d).replace("^er^", "er"),
         **{c: cumuls[c][d] for c in CATEGORIES}}
        for d in dates])


def _ipc():
    """{année: indice base 100 = 2015}."""
    return {int(r.annee): float(r.valeur) for r in figtools.series(SERIE_IPC).itertuples()}


def _serie_reelle(rangs, categorie, ipc):
    """(date, cumul en dinars constants de 2015) — les années sans indice sont ÉCARTÉES.

    L'indice s'arrête en 2024 : les tranches programmées jusqu'en 2028 n'ont pas de prix,
    et il n'est pas question d'en supposer. La courbe réelle s'arrête donc avant la
    nominale, et c'est un fait à montrer, non un trou à combler.
    """
    return [(d, c * 100 / ipc[int(d[:4])])
            for d, c in aug.serie_cumulee(rangs, categorie) if int(d[:4]) in ipc]


def table_reel():
    """Tableau (onglet Données) : cumul en dinars constants de 2015, par catégorie."""
    import pandas as pd
    rangs, ipc = _rangs(), _ipc()
    dates = [d for d in aug.dates_presentes(rangs) if int(d[:4]) in ipc]
    cum = {c: dict(_serie_reelle(rangs, c, ipc)) for c in CATEGORIES}
    return pd.DataFrame([
        {_lab("col_date"): aug.formate_date(d).replace("^er^", "er"),
         **{c: round(cum[c][d], 1) for c in CATEGORIES}}
        for d in dates])


def fig_augmentations_reel():
    """Le cumul déflaté — ce que la courbe nominale ne peut pas dire.

    En dinars courants le cumul ne fait que monter. Déflaté, il PLAFONNE puis RECULE :
    pour A1, 423,6 D constants en octobre 2022 puis 418,6 D en janvier 2024, alors que le
    cumul nominal passe de 640 à 740 D. L'inflation a mangé davantage que la tranche.
    """
    figtools.apply_lang_font()
    ft = figtools.fig_text
    rangs, ipc = _rangs(), _ipc()
    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    for libelle, cat in _TRACEES:
        serie = _serie_reelle(rangs, cat, ipc)
        if not serie:
            continue
        x = [int(d[:4]) + (int(d[5:7]) - 1) / 12 for d, _ in serie]
        y = [v for _, v in serie]
        ax.step(x, y, where="post", color=_COULEURS[libelle], lw=2, label=ft(libelle))
        ax.scatter(x, y, color=_COULEURS[libelle], s=22, zorder=4)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_reel")))
    ax.set_title(ft(_lab("titre_reel")))
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=9, title="")
    fig.tight_layout()
    return fig


def fig_augmentations():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    rangs = _rangs()
    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    for libelle, cat in _TRACEES:
        serie = aug.serie_cumulee(rangs, cat)
        # abscisse en années décimales : les dates d'effet ne sont pas annuelles
        x = [int(d[:4]) + (int(d[5:7]) - 1) / 12 for d, _ in serie]
        y = [v for _, v in serie]
        ax.step(x, y, where="post", color=_COULEURS[libelle], lw=2, label=ft(libelle))
        ax.scatter(x, y, color=_COULEURS[libelle], s=22, zorder=4)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y")))
    ax.set_title(ft(_lab("titre")))
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=9, title="")
    fig.tight_layout()
    return fig

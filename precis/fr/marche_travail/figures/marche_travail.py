"""Figures de la longue période du volume « Le marché du travail ».

    from figures import marche_travail as mt
    mt.vues_nominal(), mt.table_nominal()   # SMIG des deux régimes, au mois, dinars courants
    mt.vues_reel(), mt.table_reel()         # SMIG 48 h et SMAG, moyenne annuelle, dinars de 2023
    mt.vues_rapports(), mt.table_rapports() # 40 h / 48 h à l'heure ; SMAG / journée de 8 h au SMIG
    mt.vues_dotations_emploi(), mt.table_dotations_emploi()  # programmes d'emploi, 1987-2008

D'OÙ VIENNENT LES DONNÉES. Le module ne lit que `figtools.series()` :

  - `marche-travail-smig-smag` : le SMIG des deux régimes, à l'heure et au mois, et le SMAG
    journalier, à chaque date d'effet ; règles de droit datées, émises hors du build par
    `scripts/generate_marche_travail_tables.py` avec leurs liens « Base législative » ;
  - `ipc-longue-periode` : l'indice des prix à la consommation, base 100 en 1970, 1962-2023,
    snapshoté depuis l'entrepôt `tunisia-data` ;
  - `bct-programmes-emploi-dotations` : les dotations des programmes de soutien à l'emploi,
    1987-2008, tableau du Rapport annuel de la BCT recollé à travers 21 éditions, snapshoté
    depuis l'entrepôt `tunisia-data` (fiche `sources/bct-archives.md`). Seules les lignes
    retenues par l'arbitrage « dernière édition » sont tracées ; le total de 1992 et de 1993,
    que les éditions 1995 et 1996 n'impriment pas, vient de l'édition 1994.

CONVENTIONS.
  - Moyenne annuelle : moyenne des montants en vigueur au premier jour de chacun des douze
    mois. Une hausse du 1er mai compte donc pour huit mois de l'année.
  - Dinars constants : moyenne annuelle × IPC(2023) / IPC(année). 2023 est la dernière année
    de l'indice.
  - SMAG rapporté au SMIG : le SMAG d'une journée, divisé par huit heures au SMIG horaire du
    régime de 48 heures (le régime de 48 heures compte 208 heures par mois, soit 26 journées
    de 8 heures).
  - Les montants de 1961 à mai 1968 sont ceux du minimum de la première zone ; de 1971 à 1973,
    l'indemnité de cherté de vie, servie en sus du minimum, n'y est pas comprise.
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE = "marche-travail-smig-smag"
SERIE_IPC = "ipc-longue-periode"
ANNEE_BASE = 2023

BLEU, ORANGE, VERT, GRIS = "#08519c", "#bc4c00", "#1a7f37", "#6e7781"

figtools.register_provenance(
    SERIE,
    titre=("Salaire minimum interprofessionnel garanti (régimes de 48 et de 40 heures, à "
           "l'heure et au mois) et salaire minimum agricole garanti (par journée), à chaque "
           "date d'effet, 1961-2028"),
    titre_ar=("الأجر الأدنى المضمون لمختلف المهن (نظاما 48 و40 ساعة، بالساعة وبالشهر) والأجر "
              "الأدنى الفلاحي المضمون (باليوم)، في كلّ تاريخ سريان، 1961-2028"),
    sources=["decret61-145", "decret74-63", "decret74-571", "decret81-437", "decret92-1299",
             "decret2026-66", "decret2026-67"],
    unite="dinars courants",
    unite_ar="دينار جارٍ",
    perimetre=("montants fixés par les décrets, pour les salariés de 18 ans et plus ; une ligne "
               "par date d'effet, chaque colonne donnant le montant en vigueur à cette date"),
    perimetre_ar=("المبالغ التي تضبطها الأوامر للأجراء البالغين 18 سنة فما فوق؛ سطر لكلّ تاريخ "
                  "سريان"),
    caveats=("Avant le 1er mai 1968, minimum de la première zone seulement. De 1971 à 1973, "
             "l'indemnité de cherté de vie de 0,020 D l'heure, servie en sus du minimum et hors "
             "assiette sociale, n'est pas comprise ; le SMIG l'intègre le 1er janvier 1974. "
             "Avant 1974, les montants mensuels sont la conversion du minimum horaire. Les "
             "indemnités spéciales de 1989 et de 1991 ne sont pas comprises."),
    caveats_ar=("قبل غرّة ماي 1968، الأجر الأدنى للمنطقة الأولى فقط. ومن 1971 إلى 1973 لا تشمل "
                "المبالغ منحة غلاء المعيشة. ولا تشمل المنحتين الخاصّتين لسنتي 1989 و1991."),
)

_L = {
    "x_annee": {"fr": "Année", "ar": "السنة"},
    "y_dinars": {"fr": "Dinars courants par mois", "ar": "دينار جارٍ في الشهر"},
    "y_reel": {"fr": f"Dinars de {ANNEE_BASE} par mois", "ar": f"دينار سنة {ANNEE_BASE} في الشهر"},
    "y_ratio": {"fr": "Rapport", "ar": "النسبة"},
    "lg_48": {"fr": "SMIG, régime de 48 heures", "ar": "الأجر الأدنى المضمون، نظام 48 ساعة"},
    "lg_40": {"fr": "SMIG, régime de 40 heures", "ar": "الأجر الأدنى المضمون، نظام 40 ساعة"},
    "lg_smag26": {"fr": "SMAG × 26 journées", "ar": "الأجر الأدنى الفلاحي × 26 يومًا"},
    "lg_40_48": {"fr": "SMIG horaire, 40 heures / 48 heures",
                 "ar": "الأجر الأدنى بالساعة، نظام 40 ساعة / نظام 48 ساعة"},
    "lg_smag_smig": {"fr": "SMAG / 8 heures au SMIG horaire de 48 heures",
                     "ar": "الأجر الأدنى الفلاحي / 8 ساعات بالأجر الأدنى بالساعة (48 ساعة)"},
    "vue_lin": {"fr": "Échelle linéaire", "ar": "سلّم خطّي"},
    "vue_log": {"fr": "Échelle logarithmique", "ar": "سلّم لوغاريتمي"},
    "r_1974": {"fr": "SMIG", "ar": "الأجر الأدنى"},
    "r_1981": {"fr": "deux taux horaires", "ar": "نسبتان بالساعة"},
    "r_2026": {"fr": "décrets de 2026", "ar": "أوامر 2026"},
    # Colonnes des données.
    "c_date": {"fr": "date d'effet", "ar": "تاريخ السريان"},
    "c_annee": {"fr": "année", "ar": "السنة"},
    "c_48": {"fr": "SMIG 48 h, au mois (D)", "ar": "الأجر الأدنى 48 ساعة، بالشهر (د)"},
    "c_40": {"fr": "SMIG 40 h, au mois (D)", "ar": "الأجر الأدنى 40 ساعة، بالشهر (د)"},
    "c_smag": {"fr": "SMAG, par jour (D)", "ar": "الأجر الأدنى الفلاحي، باليوم (د)"},
    "c_48_moy": {"fr": "SMIG 48 h, moyenne annuelle (D courants)",
                 "ar": "الأجر الأدنى 48 ساعة، المعدّل السنوي (د جارية)"},
    "c_48_reel": {"fr": f"SMIG 48 h, moyenne annuelle (D de {ANNEE_BASE})",
                  "ar": f"الأجر الأدنى 48 ساعة، المعدّل السنوي (د {ANNEE_BASE})"},
    "c_smag_reel": {"fr": f"SMAG × 26, moyenne annuelle (D de {ANNEE_BASE})",
                    "ar": f"الأجر الأدنى الفلاحي × 26، المعدّل السنوي (د {ANNEE_BASE})"},
    "c_ipc": {"fr": "IPC, base 100 en 1970", "ar": "الرقم القياسي للأسعار، أساس 100 سنة 1970"},
    "c_40_48": {"fr": "40 h / 48 h, à l'heure", "ar": "40 / 48 ساعة، بالساعة"},
    "c_smag_smig": {"fr": "SMAG / (8 × SMIG horaire 48 h)",
                    "ar": "الأجر الأدنى الفلاحي / (8 × الأجر الأدنى بالساعة 48 ساعة)"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _serie():
    d = figtools.series(SERIE).copy()
    d["jour"] = [dt.date.fromisoformat(x) for x in d["date"]]
    return d.sort_values("jour").reset_index(drop=True)


def _en_vigueur(d, colonne: str, jour: dt.date):
    lignes = d[d["jour"] <= jour]
    if lignes.empty:
        return None
    v = lignes[colonne].iloc[-1]
    return None if v != v else float(v)  # NaN : pas encore de valeur


def _moyenne_annuelle(d, colonne: str, annee: int):
    """Moyenne des montants en vigueur au premier jour de chacun des douze mois."""
    mois = [_en_vigueur(d, colonne, dt.date(annee, m, 1)) for m in range(1, 13)]
    if any(v is None for v in mois):
        return None
    return sum(mois) / 12


def _ipc() -> dict[int, float]:
    return {int(r.annee): float(r.indice_base1970)
            for r in figtools.series(SERIE_IPC).itertuples()}


def _escaliers(ax, d, colonne, facteur=1.0, **kw):
    x = [dt.datetime(j.year, j.month, j.day) for j in d["jour"]]
    y = [None if v != v else v * facteur for v in d[colonne]]
    paires = [(a, b) for a, b in zip(x, y) if b is not None]
    ax.plot([a for a, _ in paires], [b for _, b in paires], drawstyle="steps-post", **kw)


def _ruptures(ax, en_dates=True):
    for annee, cle in ((1974, "r_1974"), (1981, "r_1981"), (2026, "r_2026")):
        x = dt.datetime(annee, 1, 1) if en_dates else annee - 0.5
        ax.axvline(x, color="#57606a", ls=(0, (2, 2)), lw=1, zorder=1)
        ax.annotate(figtools.fig_text(_lab(cle)), xy=(x, 1), xycoords=("data", "axes fraction"),
                    xytext=(4, -4), textcoords="offset points", ha="left", va="top",
                    fontsize=7, color="#57606a")


# ---------------------------------------------------------------- SMIG nominal

def _fig_nominal(log: bool):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _serie()
    fig, ax = plt.subplots(figsize=(10, 5.6))
    _escaliers(ax, d, "smig_48h_mensuel", color=BLEU, lw=2, label=ft(_lab("lg_48")))
    _escaliers(ax, d, "smig_40h_mensuel", color=ORANGE, lw=1.6, label=ft(_lab("lg_40")))
    _escaliers(ax, d, "smag_journalier", facteur=26, color=VERT, lw=1.4, ls="--",
               label=ft(_lab("lg_smag26")))
    _ruptures(ax)
    if log:
        ax.set_yscale("log")
        ax.set_yticks([10, 20, 50, 100, 200, 500])
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
        ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_dinars")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def vues_nominal():
    return [(_lab("vue_lin"), _fig_nominal(False)), (_lab("vue_log"), _fig_nominal(True))]


def table_nominal():
    import pandas as pd
    d = _serie()
    return pd.DataFrame({
        _lab("c_date"): d["date"],
        _lab("c_48"): d["smig_48h_mensuel"],
        _lab("c_40"): d["smig_40h_mensuel"],
        _lab("c_smag"): d["smag_journalier"],
    })


# ---------------------------------------------------------------- SMIG réel

def _reel():
    d, ipc = _serie(), _ipc()
    lignes = []
    for annee in range(1962, ANNEE_BASE + 1):
        if annee not in ipc:
            continue
        smig = _moyenne_annuelle(d, "smig_48h_mensuel", annee)
        smag = _moyenne_annuelle(d, "smag_journalier", annee)
        coef = ipc[ANNEE_BASE] / ipc[annee]
        lignes.append((annee, smig, None if smig is None else smig * coef,
                       None if smag is None else smag * 26 * coef, ipc[annee]))
    return lignes


def fig_reel():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _reel()
    fig, ax = plt.subplots(figsize=(10, 5.6))
    ax.plot([a for a, *_ in r], [v for _, _, v, _, _ in r], "-o", ms=3, color=BLEU, lw=2,
            label=ft(_lab("lg_48")))
    pts = [(a, s) for a, _, _, s, _ in r if s is not None]
    ax.plot([a for a, _ in pts], [s for _, s in pts], "--", color=VERT, lw=1.4,
            label=ft(_lab("lg_smag26")))
    _ruptures(ax, en_dates=False)
    ax.set_ylim(0, None)
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_reel")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower right", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def vues_reel():
    return fig_reel()


def table_reel():
    import pandas as pd
    r = _reel()
    return pd.DataFrame({
        _lab("c_annee"): [a for a, *_ in r],
        _lab("c_48_moy"): [None if v is None else round(v, 3) for _, v, *_ in r],
        _lab("c_ipc"): [i for *_, i in r],
        _lab("c_48_reel"): [None if v is None else round(v, 1) for _, _, v, _, _ in r],
        _lab("c_smag_reel"): [None if v is None else round(v, 1) for _, _, _, v, _ in r],
    })


# ---------------------------------------------------------------- rapports

def _rapports():
    d = _serie()
    lignes = []
    for _, l in d.iterrows():
        h48, h40, smag = l["smig_48h_horaire"], l["smig_40h_horaire"], l["smag_journalier"]
        r1 = None if h48 != h48 or h40 != h40 else h40 / h48
        r2 = None if smag != smag or h48 != h48 else smag / (8 * h48)
        lignes.append((l["date"], l["jour"], r1, r2))
    return lignes


def fig_rapports():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _rapports()
    fig, ax = plt.subplots(figsize=(10, 5.2))
    for i, (cle, couleur) in enumerate((("lg_40_48", ORANGE), ("lg_smag_smig", VERT)), start=2):
        pts = [(dt.datetime(j.year, j.month, j.day), x[i]) for x in r
               for j in [x[1]] if x[i] is not None]
        ax.plot([a for a, _ in pts], [b for _, b in pts], drawstyle="steps-post", color=couleur,
                lw=1.8, label=ft(_lab(cle)))
    ax.axhline(1, color=GRIS, lw=0.8)
    _ruptures(ax)
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_ratio")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower right", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def vues_rapports():
    return fig_rapports()


def table_rapports():
    import pandas as pd
    r = _rapports()
    return pd.DataFrame({
        _lab("c_date"): [x[0] for x in r],
        _lab("c_40_48"): [None if x[2] is None else round(x[2], 3) for x in r],
        _lab("c_smag_smig"): [None if x[3] is None else round(x[3], 3) for x in r],
    })


# ---------------------------------------------------------------- programmes d'emploi (BCT)

SERIE_EMPLOI = "bct-programmes-emploi-dotations"
VIOLET, BRUN, ROUGE, VERT_CLAIR = "#6f42c1", "#8c564b", "#cf222e", "#4ac26b"

# Éditions du Rapport annuel dont viennent les lignes tracées (1991 à 2008). Celles de 1988 à
# 1990 n'ont pas de clé propre : la clé générique `bct-ra` les couvre.
_EDITIONS_EMPLOI = [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002,
                    2003, 2004, 2005, 2006, 2007, 2008]

figtools.register_provenance(SERIE_EMPLOI, **{
    **figtools.meta(SERIE_EMPLOI),
    "sources": ["bct-ra"] + [f"bct-ra-{a}" for a in _EDITIONS_EMPLOI],
    "perimetre": ("Banque centrale de Tunisie, Rapport annuel, éditions 1988 à 2008, chapitre de "
                  "l'emploi et des salaires, tableau « Programmes de soutien à l'emploi » : "
                  "chantiers nationaux et régionaux, stages d'initiation à la vie "
                  "professionnelle (SIVP 1 et 2), Fonds d'initiation et d'adaptation "
                  "professionnelle (FIAP), contrats emploi-formation, Fonds national de l'emploi "
                  "21-21, et total du tableau"),
    "perimetre_ar": ("البنك المركزي التونسي، التقرير السنوي، طبعات 1988 إلى 2008، باب التشغيل "
                     "والأجور، جدول «برامج دعم التشغيل»: الحضائر الوطنية والجهوية، تربّصات الإعداد "
                     "للحياة المهنية (1 و2)، صندوق الإدماج والتأهيل المهني، عقود التشغيل والتكوين، "
                     "الصندوق الوطني للتشغيل 21-21، ومجموع الجدول"),
    "caveats": ("Série reconstituée : chaque édition du Rapport annuel n'imprime que deux à cinq "
                "années ; la série réunit 21 éditions, et la dernière édition qui imprime une "
                "année fait foi, ligne par ligne. La Banque centrale relaie des chiffres qu'elle "
                "ne produit pas : elle cite la direction générale des ressources humaines du "
                "ministère du Plan (1988-1991), le ministère du Plan et du Développement régional "
                "(1992-1993), le ministère du Développement économique (1994-1995), ce ministère "
                "et le Commissariat général au développement régional (1996-2001), puis les "
                "ministères du Développement et de la coopération internationale et de l'Emploi "
                "(2002-2008). Dotations, non dépenses constatées : le tableau ne qualifie pas la "
                "grandeur ; le texte des rapports parle de « dotation budgétaire », "
                "d'« enveloppe » ou de « montant alloué ». Le total comprend des programmes de "
                "développement régional, rural et urbain et des fonds d'aide à l'artisanat : il "
                "n'est pas la somme des programmes tracés. Trois présentations du tableau se "
                "succèdent (éditions 1988-1990, 1991-1994, 1995-2008), dont les totaux ne "
                "couvrent pas le même périmètre (1987 : 83,8 dans la première, 50,8 dans la "
                "deuxième) ; le total de 1992 et de 1993 vient de l'édition 1994, les lignes de "
                "ces deux années des éditions 1995 et 1996. Révisions : chantiers nationaux de "
                "1992 imprimés 23,9, puis 35,1, puis 37,6 ; chantiers régionaux de 2003, 29,6 "
                "(édition 2003) puis 92,0 (éditions 2004 à 2006), sans explication de la source ; "
                "Fonds 21-21 de 2000, 60,0 puis 58,4."),
    "caveats_ar": ("سلسلة معاد تركيبها: لا تطبع كلّ طبعة من التقرير السنوي سوى سنتين إلى خمس "
                   "سنوات، وقد جُمعت السلسلة عبر 21 طبعة، وتُعتمد آخر طبعة تطبع السنة، بنداً "
                   "بنداً. البنك المركزي ناقل لا منتج: يذكر تحت الجدول وزارة التخطيط ثمّ وزارة "
                   "التنمية الاقتصادية والمندوبية العامة للتنمية الجهوية ثمّ وزارتي التنمية "
                   "والتعاون الدولي والتشغيل. المبالغ اعتمادات مرصودة لا نفقات منجزة. المجموع "
                   "يشمل برامج تنمية جهوية وريفية وحضرية وصناديق لدعم الصناعات التقليدية، فليس "
                   "مجموع البرامج المرسومة. للجدول ثلاث هيئات متعاقبة (طبعات 1988-1990، "
                   "1991-1994، 1995-2008) لا تتطابق مجاميعها؛ ومجموع سنتي 1992 و1993 مأخوذ من "
                   "طبعة 1994، أمّا بنود هاتين السنتين فمن طبعتي 1995 و1996. مراجعات: الحضائر "
                   "الوطنية لسنة 1992 طُبعت 23,9 ثمّ 35,1 ثمّ 37,6؛ الحضائر الجهوية لسنة 2003 "
                   "طُبعت 29,6 (طبعة 2003) ثمّ 92,0 (طبعات 2004 إلى 2006) دون تفسير من المصدر؛ "
                   "الصندوق 21-21 لسنة 2000 طُبع 60,0 ثمّ 58,4."),
})

# (identifiant de la série, clé de libellé, couleur, style du trait)
_LIGNES_EMPLOI = [
    ("chantiers_nationaux", "e_cn", BLEU, "-"),
    ("chantiers_regionaux", "e_cr", ORANGE, "-"),
    ("fne_21_21", "e_fne", ROUGE, "-"),
    ("sivp_1", "e_sivp1", VERT, "-"),
    ("sivp_2", "e_sivp2", VERT_CLAIR, "--"),
    ("fiap", "e_fiap", VIOLET, "-"),
    ("cef", "e_cef", BRUN, "-"),
]
# Année de données où les lignes passent de la deuxième à la troisième présentation du tableau
# (éditions 1995 et suivantes), et année où le total y passe à son tour.
RUPTURE_LIGNES, RUPTURE_TOTAL = 1992, 1994

_L.update({
    "y_md": {"fr": "Millions de dinars courants", "ar": "بملايين الدنانير الجارية"},
    "e_cn": {"fr": "Chantiers nationaux", "ar": "الحضائر الوطنية"},
    "e_cr": {"fr": "Chantiers régionaux", "ar": "الحضائر الجهوية"},
    "e_fne": {"fr": "Fonds national de l'emploi 21-21", "ar": "الصندوق الوطني للتشغيل 21-21"},
    "e_sivp1": {"fr": "SIVP 1 (diplômés du supérieur)",
                "ar": "تربّصات الإعداد للحياة المهنية 1 (التعليم العالي)"},
    "e_sivp2": {"fr": "SIVP 2 (secondaire)", "ar": "تربّصات الإعداد للحياة المهنية 2 (الثانوي)"},
    "e_fiap": {"fr": "FIAP", "ar": "صندوق الإدماج والتأهيل المهني"},
    "e_cef": {"fr": "Contrats emploi-formation", "ar": "عقود التشغيل والتكوين"},
    "e_total": {"fr": "Total du tableau (autres lignes comprises)",
                "ar": "مجموع الجدول (بما فيه بنود أخرى)"},
    "r_lignes": {"fr": "lignes : tableau refondu", "ar": "البنود: جدول بهيئة جديدة"},
    "r_total": {"fr": "total : autre périmètre", "ar": "المجموع: نطاق آخر"},
    "r_2003": {"fr": "2003 : 29,6 dans l'édition 2003,\n92,0 dans les suivantes",
               "ar": "2003: 29,6 في طبعة 2003،\nثمّ 92,0 في الطبعات اللاحقة"},
    "c_ed_lignes": {"fr": "édition retenue (lignes)", "ar": "الطبعة المعتمدة (البنود)"},
    "c_ed_total": {"fr": "édition retenue (total)", "ar": "الطبعة المعتمدة (المجموع)"},
    "c_total": {"fr": "Total du tableau", "ar": "مجموع الجدول"},
})


def _dotations_emploi():
    """Une ligne par année : les programmes tracés, le total, et l'édition dont ils viennent.

    Les lignes sont celles de la dernière édition qui imprime l'année. Le total aussi, sauf en
    1992 et 1993 : les éditions 1995 et 1996 n'en impriment pas, et la série garde celui de
    l'édition 1994 (colonne `derniere_edition` à « non »).
    """
    d = figtools.series(SERIE_EMPLOI)
    retenues = d[d["derniere_edition"] == "oui"]
    lignes = []
    for annee in sorted(int(a) for a in d["annee"].unique()):
        r = retenues[retenues["annee"] == annee]
        ligne = {"annee": annee}
        for ident, *_ in _LIGNES_EMPLOI:
            v = r.loc[r["programme_id"] == ident, "valeur_MD"]
            ligne[ident] = None if v.empty or v.iloc[0] != v.iloc[0] else float(v.iloc[0])
        ed = r.loc[r["programme_id"] == "chantiers_nationaux", "edition"]
        ligne["edition_lignes"] = None if ed.empty else int(ed.iloc[0])
        tot = d[(d["annee"] == annee) & (d["programme_id"] == "total")]
        ligne["total"] = None if tot.empty else float(tot["valeur_MD"].iloc[0])
        ligne["edition_total"] = None if tot.empty else int(tot["edition"].iloc[0])
        lignes.append(ligne)
    return lignes


def _fig_dotations_emploi(log: bool):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _dotations_emploi()
    fig, ax = plt.subplots(figsize=(10, 5.8))
    # Le total, en deux segments : il change de périmètre entre 1993 et 1994.
    for i, (debut, fin) in enumerate(((1987, RUPTURE_TOTAL - 1), (RUPTURE_TOTAL, 2008))):
        pts = [(l["annee"], l["total"]) for l in r
               if debut <= l["annee"] <= fin and l["total"] is not None]
        ax.plot([a for a, _ in pts], [v for _, v in pts], color=GRIS, lw=1.4, ls=(0, (4, 2)),
                marker="o", ms=2.5, label=ft(_lab("e_total")) if i == 0 else None)
    for ident, cle, couleur, style in _LIGNES_EMPLOI:
        # Une valeur nulle (le Fonds avant sa création) n'est pas tracée.
        pts = [(l["annee"], l[ident]) for l in r if l[ident]]
        ax.plot([a for a, _ in pts], [v for _, v in pts], color=couleur, lw=1.8, ls=style,
                marker="o", ms=2.5, label=ft(_lab(cle)))
    figtools.marque_rupture(ax, RUPTURE_LIGNES, ft(_lab("r_lignes")))
    figtools.marque_rupture(ax, RUPTURE_TOTAL, "\n" + ft(_lab("r_total")))
    cr2003 = next(l["chantiers_regionaux"] for l in r if l["annee"] == 2003)
    ax.annotate("\n".join(ft(x) for x in _lab("r_2003").split("\n")), xy=(2003, cr2003),
                xytext=(-20, -70) if log else (-12, 34), textcoords="offset points",
                ha="right", va="top" if log else "bottom", fontsize=7, color=ORANGE,
                arrowprops={"arrowstyle": "-", "color": ORANGE, "lw": 0.8})
    if log:
        ax.set_yscale("log")
        ax.set_yticks([0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200])
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
        ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    else:
        ax.set_ylim(0, None)
    ax.set_xticks(range(1987, 2009, 3))
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_md")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False, ncol=4)
    fig.tight_layout()
    return fig


def vues_dotations_emploi():
    return [(_lab("vue_lin"), _fig_dotations_emploi(False)),
            (_lab("vue_log"), _fig_dotations_emploi(True))]


def table_dotations_emploi():
    import pandas as pd
    r = _dotations_emploi()
    colonnes = {_lab("c_annee"): [l["annee"] for l in r]}
    for ident, cle, *_ in _LIGNES_EMPLOI:
        colonnes[_lab(cle)] = [l[ident] for l in r]
    colonnes[_lab("c_total")] = [l["total"] for l in r]
    colonnes[_lab("c_ed_lignes")] = [l["edition_lignes"] for l in r]
    colonnes[_lab("c_ed_total")] = [l["edition_total"] for l in r]
    return pd.DataFrame(colonnes)

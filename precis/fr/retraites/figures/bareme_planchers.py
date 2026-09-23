"""Figures tirées des règles de calcul des pensions : taux de liquidation, planchers, limite.

    from figures import bareme_planchers as bp
    bp.fig_taux_liquidation()   # τ(n) selon la durée : CNRPS 1959 et 1985, RSNA 1974 et 1982
    bp.table_taux_liquidation()
    bp.fig_planchers()          # pension minimale en dinars, et pension moyenne des deux caisses
    bp.table_planchers()
    bp.fig_limite()             # limite de calcul L = ℓ·S et salaire moyen déclaré, 2000-2017
    bp.table_limite()

D'OÙ VIENNENT LES DONNÉES. Deux séries sont des règles de droit datées, émises hors du build
par `scripts/generate_retraites_tables.py` dans `precis/_seriescache/` ; le site se construit
sans elles à la source (#165), et ce module ne lit que `figtools.series()` :

  - `retraites-taux-liquidation` : τ(n) pour chaque barème, par année entière de 0 à 45 ans,
    avec le plafond en vigueur à la date du barème et la durée minimale qui ouvre le droit ;
  - `retraites-smig-planchers` : le SMIG horaire du régime de 48 heures à chaque date où il
    change, et les montants mensuels qui en dépendent — fraction × SMIG × 200 heures.

Les deux autres sont des observations, déjà snapshotées : `cnrps-taux-equilibre` et
`cnss-rsna-taux-equilibre`, dont on ne lit que la pension moyenne et le salaire moyen.

CE QUI EST TRACÉ, ET CE QUI NE L'EST PAS.
  - Le barème de 1959 n'a pas de plafond daté à sa date : sa courbe est celle du barème seul,
    2 % par annuité dans la limite de 40 annuités. Le plafond de 60 % de la loi n° 59-18,
    atteint à trente annuités, et celui de 80 % du 1er juillet 1970 ne sont pas tracés ; la
    note de lecture les donne. L'année seule du barème est affichée (voir le générateur).
  - Les barèmes du régime non agricole de 1974 et de 1982 donnent le même taux à chaque
    année entière : le décret n° 82-1030 ne change que le pas de la majoration, le trimestre
    au lieu de l'année (art. 4). Une seule courbe les porte, et le module vérifie qu'ils
    coïncident ; s'ils divergeaient, chacun aurait la sienne.
  - Entre la durée des carrières courtes (60 mois) et le stage (120 mois), le décret
    n° 82-1030 ouvre une pension proportionnelle, n/n₀ · τ₀ · R [art. 3], soit exactement le
    taux du barème prolongé en deçà du stage. Elle n'existe qu'à partir de 1982 : en 1974,
    ces carrières recevaient une allocation en capital (décret n° 74-499, art. 39 à 43), qui
    n'est pas un taux. Le segment n'est donc tracé que pour le barème de 1982.
  - Les planchers égaux — deux tiers du SMIG à la CNRPS et au régime non agricole, moitié
    du SMIG pour l'allocation de vieillesse de la CNRPS et pour les pensions réduites du
    régime non agricole — sont tracés d'un seul trait, après vérification de l'égalité.
  - La pension moyenne est celle de toutes les natures de pension, réversions comprises,
    qui sont des fractions de la pension de l'assuré : elle n'est pas comparable terme à
    terme au plancher d'une pension de vieillesse. Pour la CNSS, 1980 et 1985-1991 sont
    ceux de la CAVIS, tout le secteur privé (marques creuses) ; pour la CNRPS, 2021 est
    estimé (rond creux).
  - La limite de calcul est comparée au salaire moyen déclaré, masse salariale déclarée
    rapportée aux actifs non-assujettis compris. La limite d'une année est la moyenne des
    limites en vigueur au premier de chacun de ses douze mois.
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

SERIE_TAUX = "retraites-taux-liquidation"
SERIE_SMIG = "retraites-smig-planchers"
SERIE_CNRPS = "cnrps-taux-equilibre"
SERIE_RSNA = "cnss-rsna-taux-equilibre"

PM = "pension moyenne mensuelle"
SM = "salaire moyen mensuel"

BLEU, ORANGE, GRIS, VERT, ROUGE = "#08519c", "#bc4c00", "#6e7781", "#1a7f37", "#cf222e"

# Dernière année tracée pour les montants : les paliers du SMIG des années suivantes sont
# publiés, mais la figure s'arrête à l'année en cours de rédaction.
FIN = 2026

figtools.register_provenance(
    SERIE_TAUX,
    titre=("Taux de liquidation selon la durée : pensions civiles et militaires (barèmes de "
           "1959 et de 1985) et régime des salariés non agricoles (barèmes de 1974 et de 1982)"),
    titre_ar=("نسبة تصفية الجراية حسب المدّة: الجرايات المدنية والعسكرية (جدولا 1959 و1985) "
              "ونظام الأجراء غير الفلاحيين (جدولا 1974 و1982)"),
    sources=["loi59-18", "loi85-12", "decret74-499", "decret82-1030"],
    unite="taux de la rémunération ou du salaire de référence",
    unite_ar="نسبة من الأجر المرجعي",
    perimetre=("taux acquis à chaque année entière de 0 à 45 ans de services ou de cotisation, "
               "plafonné par le plafond en vigueur à la date du barème ; durée minimale qui "
               "ouvre la pension au taux du barème"),
    perimetre_ar=("النسبة المكتسبة عند كلّ سنة كاملة من 0 إلى 45 سنة، في حدود السقف النافذ "
                  "في تاريخ الجدول؛ والمدّة الدنيا التي تفتح الحقّ في الجراية"),
    caveats=("Le plafond de 1959, 60 %, et celui de 1970, 80 %, ne sont pas représentés : la "
             "courbe de 1959 est celle du barème seul, 2 % par annuité dans la limite de 40 "
             "annuités. En 1959, la durée se décompte par semestre ; en 1974, la majoration "
             "par année complète : la courbe, tracée par année entière, ne porte pas ces pas."),
    caveats_ar=("سقف 1959 (60 %) وسقف 1970 (80 %) غير ممثّلين: منحنى 1959 هو منحنى الجدول وحده، "
                "2 % عن كلّ سنة في حدود 40 سنة."),
)

figtools.register_provenance(
    SERIE_SMIG,
    titre=("SMIG horaire du régime de 48 heures, pensions minimales et limite de calcul des "
           "prestations, en dinars par mois, depuis 1974"),
    titre_ar=("الأجر الأدنى المضمون بالساعة (نظام 48 ساعة) والجرايات الدنيا وسقف احتساب "
              "المنافع، بالدينار في الشهر، منذ 1974"),
    sources=["loi81-70", "decret82-972", "loi85-12", "decret74-499", "decret82-1030",
             "decret94-1429"],
    unite="dinars courants par mois",
    unite_ar="دينار جارٍ في الشهر",
    perimetre=("fraction du SMIG × SMIG horaire × 200 heures, soit le SMIG rapporté à 2 400 "
               "heures par an, à chaque date où le SMIG ou la fraction change ; chaque ligne "
               "des données porte le décret qui fixe le SMIG et son lien au Journal officiel"),
    perimetre_ar=("كسر من الأجر الأدنى × الأجر الأدنى بالساعة × 200 ساعة، أي الأجر الأدنى "
                  "على أساس 2400 ساعة في السنة، عند كلّ تاريخ يتغيّر فيه أحدهما"),
    caveats=("SMIG horaire du régime de 48 heures ; celui du régime de 40 heures, plus élevé à "
             "l'heure depuis le 1er avril 1981, donnerait des montants supérieurs. Plusieurs "
             "dates ou montants du SMIG ne sont pas vérifiés sur le Journal officiel : voir les "
             "tableaux de la revalorisation des pensions du régime non agricole."),
    caveats_ar=("الأجر الأدنى بالساعة في نظام 48 ساعة؛ وبعض تواريخ الأجر الأدنى أو مبالغه "
                "غير متحقَّق منها في الرائد الرسمي."),
)

_L = {
    # Figure 1
    "titre_taux": {"fr": "Taux de liquidation selon la durée de services ou de cotisation",
                   "ar": "نسبة تصفية الجراية حسب مدّة الخدمات أو الانخراط"},
    "x_duree": {"fr": "Durée (années)", "ar": "المدّة (سنوات)"},
    "y_taux": {"fr": "Taux de liquidation τ(n) (%)", "ar": "نسبة التصفية (%)"},
    "lg_c1959": {"fr": "CNRPS, barème de 1959 : 2 % par annuité, 40 annuités au plus "
                       "(plafond de 60 % non tracé)",
                 "ar": "الصندوق الوطني للتقاعد، جدول 1959: 2 % عن كلّ سنة، 40 سنة على الأكثر "
                       "(سقف 60 % غير ممثّل)"},
    "lg_c1985": {"fr": "CNRPS, barème de 1985 : 2 %, 3 %, puis 2 % ; plafond 90 %",
                 "ar": "الصندوق الوطني للتقاعد، جدول 1985: 2 % ثمّ 3 % ثمّ 2 %؛ السقف 90 %"},
    "lg_c1985_min": {"fr": "CNRPS 1985, en deçà de la durée minimale de 15 ans",
                     "ar": "جدول 1985، دون المدّة الدنيا (15 سنة)"},
    "lg_rsna": {"fr": "Régime non agricole, barèmes de 1974 et de 1982 : 40 % au stage, "
                      "puis 2 % par an ; plafond 80 %",
                "ar": "نظام الأجراء غير الفلاحيين، جدولا 1974 و1982: 40 % عند المدّة الدنيا "
                      "ثمّ 2 % في السنة؛ السقف 80 %"},
    "lg_rsna_1974": {"fr": "Régime non agricole, barème de 1974",
                     "ar": "نظام الأجراء غير الفلاحيين، جدول 1974"},
    "lg_rsna_1982": {"fr": "Régime non agricole, barème de 1982",
                     "ar": "نظام الأجراء غير الفلاحيين، جدول 1982"},
    "lg_prop": {"fr": "Régime non agricole, pension proportionnelle (depuis 1982)",
                "ar": "نظام الأجراء غير الفلاحيين، الجراية النسبية (منذ 1982)"},
    "col_duree": {"fr": "Durée (années)", "ar": "المدّة (سنوات)"},
    "col_c1959": {"fr": "CNRPS, barème de 1959 (%)", "ar": "الصندوق الوطني للتقاعد، جدول 1959 (%)"},
    "col_c1985": {"fr": "CNRPS, barème de 1985 (%)", "ar": "الصندوق الوطني للتقاعد، جدول 1985 (%)"},
    "col_r1974": {"fr": "Régime non agricole, barème de 1974 (%)",
                  "ar": "نظام الأجراء غير الفلاحيين، جدول 1974 (%)"},
    "col_r1982": {"fr": "Régime non agricole, barème de 1982 (%)",
                  "ar": "نظام الأجراء غير الفلاحيين، جدول 1982 (%)"},
    # Figure 2
    "titre_planchers": {"fr": "Pension minimale et pension moyenne, dinars courants par mois, "
                              "1980-2026",
                        "ar": "الجراية الدنيا ومعدّل الجراية، بالدينار الجاري في الشهر، "
                              "1980-2026"},
    "x_annee": {"fr": "Année", "ar": "السنة"},
    "y_dinars": {"fr": "Dinars courants par mois (échelle logarithmique)",
                 "ar": "دينار جارٍ في الشهر (سلّم لوغاريتمي)"},
    "lg_deux_tiers": {"fr": "Deux tiers du SMIG : pension minimale, CNRPS (1981) et régime "
                            "non agricole",
                      "ar": "ثلثا الأجر الأدنى: الجراية الدنيا، الصندوق الوطني للتقاعد (1981) "
                            "ونظام الأجراء غير الفلاحيين"},
    "lg_moitie": {"fr": "Moitié du SMIG : pensions proportionnelles et départs anticipés a) "
                        "et b) du régime non agricole (1982), allocation de vieillesse de la "
                        "CNRPS (1985)",
                  "ar": "نصف الأجر الأدنى: الجرايات النسبية والتقاعد المبكّر أ) وب) في نظام "
                        "الأجراء غير الفلاحيين (1982)، ومنحة الشيخوخة في الصندوق الوطني "
                        "للتقاعد (1985)"},
    "lg_pm_cnrps": {"fr": "Pension moyenne, CNRPS, toutes natures",
                    "ar": "معدّل الجراية، الصندوق الوطني للتقاعد، بجميع الأصناف"},
    "lg_pm_rsna": {"fr": "Pension moyenne, régime non agricole, toutes natures",
                   "ar": "معدّل الجراية، نظام الأجراء غير الفلاحيين، بجميع الأصناف"},
    "lg_cavis": {"fr": "Marques creuses : CNSS, CAVIS, tout le privé (1980, 1985-1991) ; "
                       "CNRPS, source Banque mondiale (1980, 1985-1991) et 2021 estimé",
                 "ar": "العلامات المفرّغة: الصندوق الوطني للضمان الاجتماعي، كامل القطاع الخاص "
                       "(1980، 1985-1991)؛ الصندوق الوطني للتقاعد، البنك الدولي (1980، "
                       "1985-1991) وتقدير 2021"},
    "col_annee": {"fr": "Année", "ar": "السنة"},
    "col_date": {"fr": "Date d'effet", "ar": "تاريخ النفاذ"},
    "col_smig": {"fr": "SMIG horaire, 48 heures (D)", "ar": "الأجر الأدنى بالساعة، 48 ساعة (د)"},
    "col_s": {"fr": "SMIG rapporté à 200 heures, S/12 (D/mois)",
              "ar": "الأجر الأدنى على أساس 200 ساعة (د/شهر)"},
    "col_min_cnrps": {"fr": "Pension minimale, CNRPS (D/mois)",
                      "ar": "الجراية الدنيا، الصندوق الوطني للتقاعد (د/شهر)"},
    "col_alloc_cnrps": {"fr": "Allocation de vieillesse, CNRPS (D/mois)",
                        "ar": "منحة الشيخوخة، الصندوق الوطني للتقاعد (د/شهر)"},
    "col_min_rsna": {"fr": "Pension minimale, régime non agricole (D/mois)",
                     "ar": "الجراية الدنيا، نظام الأجراء غير الفلاحيين (د/شهر)"},
    "col_min_rsna_r": {"fr": "Pension minimale réduite, régime non agricole (D/mois)",
                       "ar": "الجراية الدنيا المخفّضة، نظام الأجراء غير الفلاحيين (د/شهر)"},
    "col_grandeur": {"fr": "Grandeur", "ar": "المقدار"},
    "col_valeur": {"fr": "Dinars par mois", "ar": "دينار في الشهر"},
    "col_texte": {"fr": "Décret fixant le SMIG", "ar": "الأمر المحدّد للأجر الأدنى"},
    "col_lien": {"fr": "Journal officiel", "ar": "الرائد الرسمي"},
    "col_pm_cnrps": {"fr": "Pension moyenne, CNRPS (D/mois)",
                     "ar": "معدّل الجراية، الصندوق الوطني للتقاعد (د/شهر)"},
    "col_pm_cnrps_est": {"fr": "Pension moyenne, CNRPS, estimée (D/mois)",
                         "ar": "معدّل الجراية، الصندوق الوطني للتقاعد، تقدير (د/شهر)"},
    "col_pm_rsna": {"fr": "Pension moyenne, régime non agricole (D/mois)",
                    "ar": "معدّل الجراية، نظام الأجراء غير الفلاحيين (د/شهر)"},
    "col_pm_cavis": {"fr": "Pension moyenne, CAVIS, tout le secteur privé (D/mois)",
                     "ar": "معدّل الجراية، كامل القطاع الخاص (د/شهر)"},
    # Figure 3
    "titre_limite": {"fr": "Limite de calcul des prestations (2000-2026) et salaire moyen "
                           "déclaré (2000-2017), régime non agricole",
                     "ar": "سقف احتساب المنافع (2000-2026) ومعدّل الأجر المصرّح به "
                           "(2000-2017)، نظام الأجراء غير الفلاحيين"},
    "sous_dinars": {"fr": "Dinars courants par mois", "ar": "دينار جارٍ في الشهر"},
    "sous_ratio": {"fr": "Limite ÷ salaire moyen", "ar": "السقف ÷ معدّل الأجر"},
    "lg_limite": {"fr": "Limite de calcul L = 6 × SMIG × 2 400 h, par mois",
                  "ar": "سقف احتساب المنافع = 6 × الأجر الأدنى × 2400 ساعة، في الشهر"},
    "lg_limite_moy": {"fr": "Limite, moyenne de l'année", "ar": "السقف، معدّل السنة"},
    "lg_sm": {"fr": "Salaire moyen déclaré (masse déclarée ÷ actifs)",
              "ar": "معدّل الأجر المصرّح به (الكتلة المصرّح بها ÷ النشيطين)"},
    "lg_ratio": {"fr": "Limite de l'année ÷ salaire moyen déclaré",
                 "ar": "سقف السنة ÷ معدّل الأجر المصرّح به"},
    "sans_salaire": {"fr": "salaire moyen déclaré non publié après 2017",
                     "ar": "معدّل الأجر المصرّح به غير منشور بعد 2017"},
    "col_limite": {"fr": "Limite de calcul, moyenne de l'année (D/mois)",
                   "ar": "سقف الاحتساب، معدّل السنة (د/شهر)"},
    "col_sm": {"fr": "Salaire moyen déclaré (D/mois)", "ar": "معدّل الأجر المصرّح به (د/شهر)"},
    "col_ratio": {"fr": "Limite ÷ salaire moyen", "ar": "السقف ÷ معدّل الأجر"},
    "col_part": {"fr": "Salaire moyen ÷ limite (%)", "ar": "معدّل الأجر ÷ السقف (%)"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _nombre(v: float, dec: int = 0) -> str:
    """Nombre à la française : espace fine insécable pour les milliers, virgule décimale."""
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


# --------------------------------------------------------------- taux de liquidation

def _baremes() -> dict[tuple[str, int], dict]:
    """{(régime, année du barème): {"taux": {n: τ}, "n0": durée minimale, "n1": carrières courtes}}."""
    out: dict[tuple[str, int], dict] = {}
    for r in figtools.series(SERIE_TAUX).itertuples():
        b = out.setdefault((r.regime, int(r.annee_bareme)), {"taux": {}, "n0": None, "n1": None})
        b["taux"][int(r.duree_annees)] = float(r.taux)
        if r.duree_minimale == r.duree_minimale:  # NaN : pas de durée minimale datée
            b["n0"] = float(r.duree_minimale)
        if r.duree_carriere_courte == r.duree_carriere_courte:
            b["n1"] = float(r.duree_carriere_courte)
    return out


def _ouvert(b: dict, n: int, proportionnelle: bool) -> bool:
    """La durée n ouvre-t-elle une pension au taux du barème ?"""
    if b["n0"] is None or n >= b["n0"]:
        return True
    return proportionnelle and b["n1"] is not None and n >= b["n1"]


def table_taux_liquidation():
    import pandas as pd
    b = _baremes()
    colonnes = (("cnrps", 1959, "col_c1959", False), ("cnrps", 1985, "col_c1985", False),
                ("rsna", 1974, "col_r1974", False), ("rsna", 1982, "col_r1982", True))
    lignes = []
    for n in sorted(b[("cnrps", 1985)]["taux"]):
        ligne = {_lab("col_duree"): n}
        for regime, annee, col, prop in colonnes:
            bar = b[(regime, annee)]
            ligne[_lab(col)] = round(100 * bar["taux"][n], 2) if _ouvert(bar, n, prop) else None
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def fig_taux_liquidation():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    b = _baremes()
    fig, ax = plt.subplots(figsize=(9.5, 6.2))

    def trace(bar, style, couleur, label, debut=0, lw=2.2, fin=None):
        pts = sorted((n, 100 * t) for n, t in bar["taux"].items()
                     if n >= debut and (fin is None or n <= fin))
        ax.plot([n for n, _ in pts], [t for _, t in pts], style, color=couleur, lw=lw,
                label=ft(_lab(label)) if label else None)

    c59, c85 = b[("cnrps", 1959)], b[("cnrps", 1985)]
    trace(c59, "-", GRIS, "lg_c1959", lw=1.8)
    n0 = int(c85["n0"])
    trace(c85, ":", BLEU, "lg_c1985_min", fin=n0, lw=1.4)
    trace(c85, "-", BLEU, "lg_c1985", debut=n0)
    ax.plot([n0], [100 * c85["taux"][n0]], "o", color=BLEU, ms=5)

    r74, r82 = b[("rsna", 1974)], b[("rsna", 1982)]
    s0 = int(r82["n0"])
    if r74["taux"] == r82["taux"] and r74["n0"] == r82["n0"]:
        trace(r82, "-", ORANGE, "lg_rsna", debut=s0)
    else:  # pragma: no cover - les deux barèmes coïncident aujourd'hui
        trace(r74, "--", ORANGE, "lg_rsna_1974", debut=int(r74["n0"]), lw=1.6)
        trace(r82, "-", ORANGE, "lg_rsna_1982", debut=s0)
    ax.plot([s0], [100 * r82["taux"][s0]], "o", color=ORANGE, ms=5)
    if r82["n1"] is not None:
        # Pension proportionnelle du décret n° 82-1030, art. 3 : le barème en deçà du stage.
        trace(r82, "--", ORANGE, "lg_prop", debut=int(r82["n1"]), fin=s0, lw=1.6)
        ax.plot([r82["n1"]], [100 * r82["taux"][int(r82["n1"])]], "o", mfc="white",
                color=ORANGE, ms=5)

    for n, t, coul in ((40, 90, BLEU), (30, 80, ORANGE), (40, 80, GRIS)):
        ax.annotate(f"{t} %", (n, t), textcoords="offset points",
                    xytext=(4, 5 if coul != GRIS else -12), fontsize=8, color=coul)
    ax.set_xlim(0, 45)
    ax.set_ylim(0, 100)
    ax.set_xticks(range(0, 46, 5))
    ax.set_xlabel(ft(_lab("x_duree")))
    ax.set_ylabel(ft(_lab("y_taux")))
    ax.set_title(ft(_lab("titre_taux")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=1, fontsize=8,
              frameon=False)
    fig.tight_layout()
    return fig


# ------------------------------------------------------------------------- planchers

def _smig():
    d = figtools.series(SERIE_SMIG)
    d["jour"] = [dt.date.fromisoformat(x) for x in d["date"]]
    return d


def _an(date: dt.date) -> float:
    """Date en années décimales, pour l'axe des temps."""
    debut = dt.date(date.year, 1, 1)
    return date.year + (date - debut).days / ((dt.date(date.year + 1, 1, 1) - debut).days)


def _egaux(d, a: str, b: str) -> bool:
    """Deux colonnes de montants coïncident-elles là où l'une et l'autre sont définies ?"""
    m = d[a].notna() & d[b].notna()
    return bool(((d.loc[m, a] - d.loc[m, b]).abs() < 1e-6).all())


def _marches(d, col: str, debut: float = 1980.0):
    """Points (x, y) d'un tracé en escalier, du premier montant défini à la fin de FIN."""
    pts = [(_an(j), v) for j, v in zip(d["jour"], d[col]) if v == v and j.year <= FIN]
    if not pts:
        return [], []
    pts.append((FIN + 1.0, pts[-1][1]))
    # Avant `debut`, seul compte le dernier montant en vigueur : il ouvre le tracé à `debut`.
    avant = [p for p in pts if p[0] <= debut]
    pts = ([(debut, avant[-1][1])] if avant else []) + [p for p in pts if p[0] > debut]
    return [x for x, _ in pts], [y for _, y in pts]


def _moyennes(serie: str) -> dict[int, float]:
    d = figtools.series(serie)
    return {int(r.annee): float(r.valeur) for r in d.itertuples() if r.indicateur == PM}


def _creuse_cnrps(a: int) -> bool:
    return a < 2000 or a >= 2021


def _creuse_rsna(a: int) -> bool:
    return a < 2000


def _points(ax, d: dict[int, float], couleur, creuse, marque):
    """Moyennes annuelles au milieu de l'année ; un trait ne relie que des années voisines
    de même nature, jamais un trou."""
    ans = sorted(d)
    suite: list[int] = []
    for a in ans + [None]:
        if suite and (a is None or a != suite[-1] + 1 or creuse(a) != creuse(suite[-1])):
            if not creuse(suite[0]):
                ax.plot([x + 0.5 for x in suite], [d[x] for x in suite], "-", color=couleur,
                        lw=1.2)
            suite = []
        if a is not None:
            suite.append(a)
    for a in ans:
        c = creuse(a)
        ax.plot([a + 0.5], [d[a]], "^" if (c and a < 2000) else marque, color=couleur, ms=5,
                mfc="white" if c else couleur)


def table_planchers():
    """Données de la figure, en long : une ligne par montant daté ou par moyenne annuelle.

    Les planchers sont des règles datées, les pensions moyennes des observations annuelles :
    une table large les alignerait sur des dates qui ne sont pas les leurs.
    """
    import pandas as pd
    d = _smig()
    d = d[[j.year <= FIN for j in d["jour"]]]
    lignes = []
    for r in d.itertuples():
        for col, cle in (("minimum_cnrps", "col_min_cnrps"), ("allocation_cnrps", "col_alloc_cnrps"),
                         ("minimum_rsna", "col_min_rsna"), ("minimum_rsna_reduit", "col_min_rsna_r")):
            v = getattr(r, col)
            if v == v:
                lignes.append({_lab("col_date"): r.date, _lab("col_grandeur"): _lab(cle),
                               _lab("col_valeur"): v, _lab("col_smig"): r.smig_horaire,
                               _lab("col_texte"): r.texte_smig,
                               _lab("col_lien"): r.lien_smig if r.lien_smig == r.lien_smig else ""})
    for a, v in sorted(_moyennes(SERIE_CNRPS).items()):
        cle = "col_pm_cnrps_est" if a >= 2021 else "col_pm_cnrps"
        lignes.append({_lab("col_date"): str(a), _lab("col_grandeur"): _lab(cle),
                       _lab("col_valeur"): v})
    for a, v in sorted(_moyennes(SERIE_RSNA).items()):
        cle = "col_pm_cavis" if _creuse_rsna(a) else "col_pm_rsna"
        lignes.append({_lab("col_date"): str(a), _lab("col_grandeur"): _lab(cle),
                       _lab("col_valeur"): v})
    return pd.DataFrame(lignes)


def fig_planchers():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    d = _smig()
    fig, ax = plt.subplots(figsize=(10.5, 6.4))

    # Deux tiers du SMIG : un trait si la CNRPS et le régime non agricole coïncident.
    x, y = _marches(d, "minimum_rsna")
    ax.plot(x, y, "-", color=VERT, lw=2.2, drawstyle="steps-post", label=ft(_lab("lg_deux_tiers")))
    if not _egaux(d, "minimum_rsna", "minimum_cnrps"):  # pragma: no cover
        x, y = _marches(d, "minimum_cnrps")
        ax.plot(x, y, "--", color=BLEU, lw=1.6, drawstyle="steps-post")
    # Moitié du SMIG.
    x, y = _marches(d, "minimum_rsna_reduit")
    ax.plot(x, y, "-", color=ROUGE, lw=1.8, drawstyle="steps-post", label=ft(_lab("lg_moitie")))
    if not _egaux(d, "minimum_rsna_reduit", "allocation_cnrps"):  # pragma: no cover
        x, y = _marches(d, "allocation_cnrps")
        ax.plot(x, y, "--", color=ROUGE, lw=1.2, drawstyle="steps-post")

    _points(ax, _moyennes(SERIE_CNRPS), BLEU, _creuse_cnrps, "o")
    _points(ax, _moyennes(SERIE_RSNA), ORANGE, _creuse_rsna, "s")

    ax.set_yscale("log")
    ax.set_yticks([20, 50, 100, 200, 500, 1000, 1500])
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: _nombre(v)))
    ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_ylim(15, 1800)
    ax.set_xlim(1980, FIN + 1)
    ax.set_xticks(range(1980, FIN + 1, 5))
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_dinars")))
    ax.set_title(ft(_lab("titre_planchers")))
    ax.grid(True, which="major", alpha=0.3)
    poignees = ax.get_legend_handles_labels()[0] + [
        Line2D([], [], color=BLEU, marker="o", lw=1.2, label=ft(_lab("lg_pm_cnrps"))),
        Line2D([], [], color=ORANGE, marker="s", lw=1.2, label=ft(_lab("lg_pm_rsna"))),
        Line2D([], [], color=GRIS, marker="^", mfc="white", lw=0, label=ft(_lab("lg_cavis"))),
    ]
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=1,
              fontsize=7.5, frameon=False)
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------- limite de calcul

def _limite_annuelle() -> dict[int, float]:
    """Limite de calcul mensuelle, moyenne des douze mois de chaque année."""
    d = _smig()
    paliers = sorted(zip(d["jour"], d["limite_calcul_rsna"]))
    out = {}
    for annee in range(paliers[0][0].year, FIN + 1):
        mois = []
        for m in range(1, 13):
            jour = dt.date(annee, m, 1)
            mois.append([v for j, v in paliers if j <= jour][-1])
        out[annee] = sum(mois) / 12
    return out


def _salaires() -> dict[int, float]:
    """Salaire moyen déclaré du régime non agricole, 2000-2017 : la CAVIS n'est pas retenue."""
    d = figtools.series(SERIE_RSNA)
    return {int(r.annee): float(r.valeur) for r in d.itertuples()
            if r.indicateur == SM and int(r.annee) >= 2000}


def table_limite():
    """La limite de 2000 à FIN ; le salaire moyen et les rapports là où il est connu."""
    import pandas as pd
    lim, sal = _limite_annuelle(), _salaires()
    lignes = []
    for a in range(min(sal), FIN + 1):
        s = sal.get(a)
        lignes.append({
            _lab("col_annee"): a, _lab("col_limite"): round(lim[a], 3), _lab("col_sm"): s,
            _lab("col_ratio"): round(lim[a] / s, 2) if s else None,
            _lab("col_part"): round(100 * s / lim[a], 1) if s else None})
    return pd.DataFrame(lignes)


def fig_limite():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    lim, sal = _limite_annuelle(), _salaires()
    ans = sorted(sal)
    d = _smig()
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.5, 7.6), sharex=True,
                                 gridspec_kw={"height_ratios": [3, 2]})
    # La limite est tracée jusqu'à FIN : elle est connue au-delà du dernier salaire publié.
    x, y = _marches(d, "limite_calcul_rsna", debut=ans[0])
    ax.plot(x, y, "-", color=BLEU, lw=1.6, drawstyle="steps-post", label=ft(_lab("lg_limite")))
    tous = [a for a in range(ans[0], FIN + 1)]
    ax.plot([a + 0.5 for a in tous], [lim[a] for a in tous], "o", color=BLEU, ms=4,
            mfc="white", label=ft(_lab("lg_limite_moy")))
    ax.plot([a + 0.5 for a in ans], [sal[a] for a in ans], "s-", color=ORANGE, ms=4, lw=1.4,
            label=ft(_lab("lg_sm")))
    for a in (ans[0], ans[-1], FIN):
        ax.annotate(_nombre(lim[a]), (a + 0.5, lim[a]), textcoords="offset points",
                    xytext=(0, 7), ha="center", fontsize=8, color=BLEU)
    for a in (ans[0], ans[-1]):
        ax.annotate(_nombre(sal[a]), (a + 0.5, sal[a]), textcoords="offset points",
                    xytext=(0, -13), ha="center", fontsize=8, color=ORANGE)
    ax.set_ylim(0, None)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: _nombre(v)))
    ax.set_ylabel(ft(_lab("sous_dinars")))
    ax.set_title(ft(_lab("titre_limite")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8)

    r = [lim[a] / sal[a] for a in ans]
    bx.plot([a + 0.5 for a in ans], r, "o-", color=GRIS, ms=4, lw=1.4, label=ft(_lab("lg_ratio")))
    for a, v in ((ans[0], r[0]), (ans[-1], r[-1])):
        bx.annotate(_nombre(v, 2), (a + 0.5, v), textcoords="offset points", xytext=(0, 7),
                    ha="center", fontsize=8, color=GRIS)
    bx.set_ylim(0, 4.5)
    bx.annotate(ft(_lab("sans_salaire")), (ans[-1] + 1.5, 0.4), fontsize=8, color=GRIS)
    bx.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: _nombre(v, 1)))
    bx.set_ylabel(ft(_lab("sous_ratio")))
    bx.set_xlabel(ft(_lab("x_annee")))
    bx.set_xlim(ans[0], FIN + 1)
    bx.set_xticks(range(ans[0], FIN + 2, 2))
    bx.grid(True, alpha=0.3)
    bx.legend(loc="lower left", fontsize=8)
    fig.tight_layout()
    return fig

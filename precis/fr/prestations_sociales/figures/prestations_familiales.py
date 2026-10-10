"""Figures des prestations familiales : montants fixés par les textes, 1961-2026.

    from figures import prestations_familiales as pf
    pf.vues_montant_max(), pf.table_montant_max()   # allocation familiale maximale
    pf.fig_plafond_smig(), pf.table_plafond_smig()  # plafond de l'assiette rapporté au SMIG
    pf.vues_montants_fixes(), pf.table_montants_fixes()  # salaire unique, crèche, secteur public

D'OÙ VIENNENT LES DONNÉES. Le module ne lit que `figtools.series()` :

  - `prestations-familiales-parametres` : taux par rang, plafond de l'assiette trimestrielle
    et nombre de rangs servis des allocations familiales ; majoration pour salaire unique ;
    contribution aux frais de crèche ; indemnités à caractère familial du secteur public —
    une ligne par grandeur et par date d'effet, avec le texte et son lien au Journal
    officiel, émise hors du build par `scripts/generate_prestations_tables.py` ;
  - `marche-travail-smig-smag` : le SMIG mensuel du régime de 48 heures à chaque date
    d'effet (série du volume « Le marché du travail ») ;
  - l'indice des prix et l'année des dinars constants du précis (`scripts/dinars_constants.py`).

CE QUI EST CALCULÉ ICI.
  - Allocation maximale de l'enfant de rang r : taux du rang × plafond de l'assiette
    trimestrielle — ce que reçoit, pour cet enfant, un salarié dont la rémunération
    trimestrielle atteint ou dépasse le plafond. Foyer de n enfants : somme des rangs servis.
  - Moyenne annuelle : moyenne des montants en vigueur au premier jour de chacun des douze
    mois (`figtools.moyenne_annuelle_escalier`) ; une année où la grandeur n'existe pas
    douze mois n'a pas de point.
  - Dinars constants : moyenne annuelle × IPC(ANNEE_BASE) / IPC(année).
  - Plafond rapporté au SMIG : plafond trimestriel ÷ (3 × SMIG mensuel du régime de
    48 heures), recalculé à chaque date d'effet de l'un ou de l'autre.
  - Montants par mois : la majoration pour salaire unique est fixée par trimestre et par
    foyer ; elle est divisée par trois pour se lire sur le même axe que la contribution aux
    frais de crèche et l'indemnité du secteur public, fixées par mois et par enfant.
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker  # noqa: F401

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402
import dinars_constants  # noqa: E402
from dinars_constants import ANNEE_BASE, SERIES_IPC  # noqa: E402

SERIE = "prestations-familiales-parametres"
SERIE_SMIG = "marche-travail-smig-smag"
FIN = 2026  # dernière année tracée en dinars courants et pour le rapport au SMIG

BLEU, ORANGE, VERT, GRIS, VIOLET = "#08519c", "#bc4c00", "#1a7f37", "#6e7781", "#8250df"
BLEU_CLAIR, BLEU_MOYEN = "#9ecae1", "#4292c6"

figtools.register_provenance(
    SERIE,
    titre=("Prestations familiales : taux, plafond et montants fixés par les textes, à chaque "
           "date d'effet, 1961-1996"),
    titre_ar=("المنافع العائلية: النسب والسقف والمبالغ التي تضبطها النصوص، في كلّ تاريخ "
              "سريان، 1961-1996"),
    sources=["loi60-30", "loi75-82", "loi80-36", "loi86-75", "loi88-38", "loi88-39",
             "loi94-88", "decret95-114", "decret86-611", "decret88-1136", "decret96-1906"],
    unite="dinars courants et taux",
    unite_ar="دينار جارٍ ونسب",
    perimetre=("allocations familiales du régime des salariés non agricoles (taux par rang, "
               "plafond de l'assiette trimestrielle, rangs servis), majoration pour salaire "
               "unique (par trimestre), contribution aux frais de crèche (par mois), "
               "indemnités à caractère familial du secteur public (par mois)"),
    perimetre_ar=("المنح العائلية لنظام الأجراء غير الفلاحيين، الزيادة بعنوان الأجر الوحيد، "
                  "المساهمة في مصاريف المحاضن، المنح ذات الصبغة العائلية بالقطاع العمومي"),
    caveats=("Chaque valeur court de sa date d'effet au texte suivant ; aucun texte modifiant "
             "ces grandeurs n'est identifié après le dernier cité. Les indemnités du secteur "
             "public antérieures au 1er mai 1986 ne sont pas connues."),
    caveats_ar=("تسري كلّ قيمة من تاريخ سريانها إلى النصّ الموالي؛ ولم يُعثر على نصّ ينقّح هذه "
                "المقادير بعد آخر نصّ مذكور. ومنح القطاع العمومي قبل غرّة ماي 1986 غير معروفة."),
)

# La série du salaire minimum est déclarée par le module du volume « Le marché du travail »,
# que ce livre ne peut pas importer : même déclaration ici, pour la seule colonne employée.
figtools.register_provenance(
    SERIE_SMIG,
    titre=("Salaire minimum interprofessionnel garanti, régime de 48 heures, au mois, à chaque "
           "date d'effet, 1961-2026"),
    titre_ar=("الأجر الأدنى المضمون لمختلف المهن، نظام 48 ساعة، بالشهر، في كلّ تاريخ سريان، "
              "1961-2026"),
    sources=["decret61-145", "decret74-63", "decret74-571", "decret81-437", "decret92-1299",
             "decret2026-66", "decret2026-67"],
    unite="dinars courants",
    unite_ar="دينار جارٍ",
    perimetre=("montants fixés par les décrets, pour les salariés de 18 ans et plus ; une ligne "
               "par date d'effet"),
    perimetre_ar="المبالغ التي تضبطها الأوامر للأجراء البالغين 18 سنة فما فوق؛ سطر لكلّ تاريخ سريان",
    caveats=("Avant le 1er mai 1968, minimum de la première zone seulement. De 1971 à 1973, "
             "l'indemnité de cherté de vie de 0,020 D l'heure, servie en sus du minimum, n'est "
             "pas comprise ; le SMIG l'intègre le 1er janvier 1974. Avant 1974, les montants "
             "mensuels sont la conversion du minimum horaire, à 208 heures par mois."),
    caveats_ar=("قبل غرّة ماي 1968، الأجر الأدنى للمنطقة الأولى فقط. ومن 1971 إلى 1973 لا تشمل "
                "المبالغ منحة غلاء المعيشة. وقبل 1974 المبالغ الشهرية تحويل للأجر الأدنى بالساعة."),
)

_L = {
    "x": {"fr": "Année", "ar": "السنة"},
    "vue_constants": {"fr": f"Dinars de {ANNEE_BASE}", "ar": f"بدينار سنة {ANNEE_BASE}"},
    "vue_courants": {"fr": "Dinars courants", "ar": "بالدينار الجاري"},
    # --- allocation maximale
    "y_max_courants": {"fr": "Dinars courants par trimestre", "ar": "دينار جارٍ في الثلاثي"},
    "y_max_constants": {"fr": f"Dinars de {ANNEE_BASE} par trimestre",
                        "ar": f"دينار سنة {ANNEE_BASE} في الثلاثي"},
    "lg_rang1": {"fr": "Premier enfant", "ar": "الطفل الأوّل"},
    "lg_foyer3": {"fr": "Foyer de trois enfants", "ar": "أسرة بثلاثة أطفال"},
    "lg_foyer4": {"fr": "Foyer de quatre enfants (quatrième rang servi jusqu'en 1988)",
                  "ar": "أسرة بأربعة أطفال (الترتيب الرابع مصروف إلى 1988)"},
    "r_1976": {"fr": "1976 : taux par rang,\nplafond à 72 D", "ar": "1976: نسب حسب الترتيب"},
    "r_1986": {"fr": "1986 : plafond\nà 122 D", "ar": "1986: السقف 122 د"},
    "r_1989": {"fr": "1989 : trois\nenfants", "ar": "1989: ثلاثة أطفال"},
    "c_annee": {"fr": "Année", "ar": "السنة"},
    "c_plafond": {"fr": "Plafond de l'assiette, moyenne annuelle (D courants par trimestre)",
                  "ar": "سقف الوعاء، المعدّل السنوي (د جارية في الثلاثي)"},
    "c_rang": {"fr": "Maximum, enfant de rang {r} (D courants par trimestre)",
               "ar": "الحدّ الأقصى، الطفل ذو الترتيب {r} (د جارية في الثلاثي)"},
    "c_foyer": {"fr": "Maximum, foyer de {n} enfants (D courants par trimestre)",
                "ar": "الحدّ الأقصى، أسرة بـ{n} أطفال (د جارية في الثلاثي)"},
    "c_ipc": {"fr": "Indice des prix, base 100 en 1970",
              "ar": "الرقم القياسي للأسعار، أساس 100 سنة 1970"},
    "c_rang1_reel": {"fr": f"Maximum, premier enfant (D de {ANNEE_BASE} par trimestre)",
                     "ar": f"الحدّ الأقصى، الطفل الأوّل (د {ANNEE_BASE} في الثلاثي)"},
    "c_foyer_reel": {"fr": f"Maximum, foyer de {{n}} enfants (D de {ANNEE_BASE} par trimestre)",
                     "ar": f"الحدّ الأقصى، أسرة بـ{{n}} أطفال (د {ANNEE_BASE} في الثلاثي)"},
    # --- plafond rapporté au SMIG
    "y_ratio": {"fr": "Plafond trimestriel de l'assiette ÷ SMIG trimestriel (régime de 48 heures)",
                "ar": "السقف الثلاثي للوعاء ÷ الأجر الأدنى المضمون الثلاثي (نظام 48 ساعة)"},
    "lg_ratio": {"fr": "Plafond de l'assiette, en SMIG trimestriels",
                 "ar": "سقف الوعاء، بعدد الأجور الدنيا الثلاثية"},
    "lg_un": {"fr": "Un SMIG trimestriel", "ar": "أجر أدنى ثلاثي واحد"},
    "rs_1976": {"fr": "1976 : plafond\nà 72 D", "ar": "1976: السقف 72 د"},
    "rs_1986": {"fr": "1986 : plafond\nà 122 D", "ar": "1986: السقف 122 د"},
    "c_date": {"fr": "Date d'effet", "ar": "تاريخ السريان"},
    "c_plafond_date": {"fr": "Plafond de l'assiette (D par trimestre)",
                       "ar": "سقف الوعاء (د في الثلاثي)"},
    "c_smig": {"fr": "SMIG, régime de 48 heures (D par mois)",
               "ar": "الأجر الأدنى المضمون، نظام 48 ساعة (د في الشهر)"},
    "c_smig_trim": {"fr": "SMIG trimestriel (D)", "ar": "الأجر الأدنى الثلاثي (د)"},
    "c_ratio": {"fr": "Plafond ÷ SMIG trimestriel", "ar": "السقف ÷ الأجر الأدنى الثلاثي"},
    "c_motif": {"fr": "Ce qui change à cette date", "ar": "ما يتغيّر في هذا التاريخ"},
    "m_plafond": {"fr": "plafond", "ar": "السقف"},
    "m_smig": {"fr": "SMIG", "ar": "الأجر الأدنى"},
    # --- montants fixés en dinars
    "y_fixes_constants": {"fr": f"Dinars de {ANNEE_BASE} par mois",
                          "ar": f"دينار سنة {ANNEE_BASE} في الشهر"},
    "y_fixes_courants": {"fr": "Dinars courants par mois", "ar": "دينار جارٍ في الشهر"},
    "lg_msu3": {"fr": "Majoration pour salaire unique, foyer de trois enfants et plus "
                      "(montant trimestriel ÷ 3)",
                "ar": "الزيادة بعنوان الأجر الوحيد، أسرة بثلاثة أطفال فأكثر (المبلغ الثلاثي ÷ 3)"},
    "lg_msu2": {"fr": "Majoration pour salaire unique, foyer de deux enfants (÷ 3)",
                "ar": "الزيادة بعنوان الأجر الوحيد، أسرة بطفلين (÷ 3)"},
    "lg_msu1": {"fr": "Majoration pour salaire unique, foyer d'un enfant (÷ 3)",
                "ar": "الزيادة بعنوان الأجر الوحيد، أسرة بطفل واحد (÷ 3)"},
    "lg_creche": {"fr": "Contribution aux frais de crèche, par enfant",
                  "ar": "المساهمة في مصاريف المحاضن، عن كلّ طفل"},
    "lg_public": {"fr": "Indemnité à caractère familial du secteur public, premier enfant",
                  "ar": "المنحة ذات الصبغة العائلية بالقطاع العمومي، الطفل الأوّل"},
    "c_grandeur": {"fr": "Grandeur", "ar": "المقدار"},
    "c_courant": {"fr": "Moyenne annuelle (D courants par mois)",
                  "ar": "المعدّل السنوي (د جارية في الشهر)"},
    "c_reel": {"fr": f"Montant (D de {ANNEE_BASE} par mois)",
               "ar": f"المبلغ (د {ANNEE_BASE} في الشهر)"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _nombre(v: float, dec: int = 1) -> str:
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def _lignes(cle: str) -> list[tuple[str, float | None]]:
    """[(date d'effet, valeur ou None)] d'une grandeur de la série, dates croissantes."""
    d = figtools.series(SERIE)
    d = d[d["parametre"] == cle].sort_values("date_effet")
    assert len(d), f"grandeur absente de la série : {cle}"
    return [(str(date)[:10], None if v != v else float(v))
            for date, v in zip(d["date_effet"], d["valeur"])]


def _dates(*cles: str) -> list[str]:
    return sorted({date for cle in cles for date, _ in _lignes(cle)})


def _x(date_iso: str) -> float:
    return figtools.abscisse_date(date_iso)


# ------------------------------------------------------- allocation familiale maximale

def _max_rang(rang: int, date_iso: str) -> float | None:
    """Taux du rang × plafond de l'assiette, à la date ; None si le rang n'est pas servi."""
    taux = figtools.valeur_escalier(_lignes(f"taux_rang{rang}"), date_iso)
    plafond = figtools.valeur_escalier(_lignes("plafond_trimestriel"), date_iso)
    rangs = figtools.valeur_escalier(_lignes("rangs_servis"), date_iso)
    if taux is None or plafond is None or rangs is None or rang > rangs:
        return None
    return taux * plafond


def _max_foyer(n: int, date_iso: str) -> float | None:
    """Somme des maximums des rangs servis d'un foyer de n enfants ; None avant le régime."""
    rangs = [_max_rang(r, date_iso) for r in range(1, n + 1)]
    if rangs[0] is None:
        return None
    return sum(v for v in rangs if v is not None)


def _escalier_max(f) -> list[tuple[str, float | None]]:
    """La grandeur calculée `f(date)` à chacune des dates d'effet des allocations familiales."""
    dates = _dates(*(f"taux_rang{r}" for r in range(1, 5)), "plafond_trimestriel", "rangs_servis")
    return [(d, f(d)) for d in dates]


_COURBES_MAX = (
    ("rang1", lambda d: _max_rang(1, d), BLEU, 2.2, "-", "lg_rang1"),
    ("foyer3", lambda d: _max_foyer(3, d), ORANGE, 2.0, "-", "lg_foyer3"),
    ("foyer4", lambda d: _max_foyer(4, d), GRIS, 1.4, "--", "lg_foyer4"),
)
FIN_RANG4 = "1989-01-01"  # le quatrième rang cesse d'être servi (loi n° 88-38)


def _annuel_max(f, fin_exclue: str | None = None) -> list[tuple[int, float, float]]:
    """[(année, moyenne annuelle en dinars courants, en dinars de l'année de base)]."""
    lignes = _escalier_max(f)
    if fin_exclue:
        lignes = [(d, v) for d, v in lignes if d < fin_exclue] + [(fin_exclue, None)]
    indice = dinars_constants.ipc()
    sortie = []
    for annee in range(int(lignes[0][0][:4]), ANNEE_BASE + 1):
        moyenne = figtools.moyenne_annuelle_escalier(lignes, annee)
        if moyenne is not None and annee in indice:
            sortie.append((annee, moyenne, moyenne * indice[ANNEE_BASE] / indice[annee]))
    return sortie


def _ruptures_max(ax, cles=("r_1976", "r_1986", "r_1989"), dates=None):
    dates = dates or {"r_1976": "1976-01-01", "r_1986": "1986-05-01", "r_1989": "1989-01-01"}
    for i, cle in enumerate(cles):
        x = _x(dates[cle])
        ax.axvline(x, color="#57606a", ls=(0, (2, 2)), lw=1, zorder=1)
        ax.annotate("\n\n" * i + "\n".join(
                        figtools.fig_text(l) for l in _lab(cle).split("\n")),
                    xy=(x, 1), xycoords=("data", "axes fraction"), xytext=(4, -4),
                    textcoords="offset points", ha="left", va="top", fontsize=7,
                    color="#57606a")


def _fig_max_courants():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    for cle, f, couleur, lw, ls, lg in _COURBES_MAX:
        lignes = _escalier_max(f)
        if cle == "foyer4":
            lignes = [(d, v) for d, v in lignes if d <= FIN_RANG4]
        else:
            lignes.append((f"{FIN}-12-31", lignes[-1][1]))
        ax.plot([_x(d) for d, _ in lignes], [v for _, v in lignes], drawstyle="steps-post",
                color=couleur, lw=lw, ls=ls, label=ft(_lab(lg)))
        if cle != "foyer4":
            for d, v in (lignes[0], lignes[-1]):
                ax.annotate(_nombre(v, 3), (_x(d), v), textcoords="offset points",
                            xytext=(-4, 4) if d == lignes[0][0] else (4, 0),
                            ha="right" if d == lignes[0][0] else "left", va="bottom"
                            if d == lignes[0][0] else "center", fontsize=8, color=couleur,
                            fontweight="bold")
    _ruptures_max(ax)
    ax.set_xlim(1958, FIN + 6)
    ax.set_ylim(0, None)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_max_courants")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), fontsize=8, frameon=False, ncol=1)
    fig.tight_layout()
    return fig


def _fig_max_constants():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    for cle, f, couleur, lw, ls, lg in _COURBES_MAX:
        points = _annuel_max(f, FIN_RANG4 if cle == "foyer4" else None)
        ax.plot([a for a, _, _ in points], [r for _, _, r in points], ls, marker="o", ms=2.8,
                color=couleur, lw=lw, label=ft(_lab(lg)))
        if cle == "foyer4":
            continue
        sommet = max(points, key=lambda p: p[2])
        for a, _, r in {points[0], sommet, points[-1]}:
            dx, ha = ((-5, "right") if a == points[0][0] else (5, "left"))
            ax.annotate(_nombre(r, 0), (a, r), textcoords="offset points", xytext=(dx, 3),
                        ha=ha, va="bottom", fontsize=8, color=couleur, fontweight="bold")
    _ruptures_max(ax)
    ax.set_xlim(1958, ANNEE_BASE + 4)
    ax.set_ylim(0, None)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_max_constants")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), fontsize=8, frameon=False, ncol=1)
    fig.tight_layout()
    return fig


def vues_montant_max():
    return [(_lab("vue_constants"), _fig_max_constants()),
            (_lab("vue_courants"), _fig_max_courants())]


def table_montant_max():
    import pandas as pd
    indice = dinars_constants.ipc()
    plafond = _lignes("plafond_trimestriel")
    series = {cle: {a: (m, r) for a, m, r in _annuel_max(f, FIN_RANG4 if cle == "foyer4" else None)}
              for cle, f, *_ in _COURBES_MAX}
    rangs = {r: {a: m for a, m, _ in _annuel_max(lambda d, r=r: _max_rang(r, d))}
             for r in (2, 3, 4)}
    lignes = []
    for annee in sorted(series["rang1"]):
        ligne = {_lab("c_annee"): annee,
                 _lab("c_plafond"): round(figtools.moyenne_annuelle_escalier(plafond, annee), 3),
                 _lab("c_rang").format(r=1): round(series["rang1"][annee][0], 3)}
        for r in (2, 3, 4):
            v = rangs[r].get(annee)
            ligne[_lab("c_rang").format(r=r)] = None if v is None else round(v, 3)
        for n, cle in ((3, "foyer3"), (4, "foyer4")):
            v = series[cle].get(annee)
            ligne[_lab("c_foyer").format(n=n)] = None if v is None else round(v[0], 3)
        ligne[_lab("c_ipc")] = round(indice[annee], 1)
        ligne[_lab("c_rang1_reel")] = round(series["rang1"][annee][1], 1)
        for n, cle in ((3, "foyer3"), (4, "foyer4")):
            v = series[cle].get(annee)
            ligne[_lab("c_foyer_reel").format(n=n)] = None if v is None else round(v[1], 1)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


# ------------------------------------------------- plafond de l'assiette rapporté au SMIG

def _smig() -> list[tuple[str, float]]:
    d = figtools.series(SERIE_SMIG)
    return [(str(date)[:10], float(v)) for date, v in zip(d["date"], d["smig_48h_mensuel"])
            if v == v and str(date)[:4] <= str(FIN)]


def _ratio_smig() -> list[tuple[str, float, float, float, str]]:
    """[(date, plafond, SMIG mensuel, rapport, ce qui change)] à chaque date d'effet."""
    plafond, smig = _lignes("plafond_trimestriel"), _smig()
    dates_plafond, dates_smig = {d for d, _ in plafond}, {d for d, _ in smig}
    sortie, precedent = [], None
    for date in sorted(dates_plafond | dates_smig):
        p, s = figtools.valeur_escalier(plafond, date), figtools.valeur_escalier(smig, date)
        if p is None or s is None:
            continue
        if (p, s) == precedent:  # un décret qui reprend le montant du régime de 48 heures
            continue
        precedent = (p, s)
        motif = " ; ".join(m for m, ici in ((_lab("m_plafond"), date in dates_plafond),
                                            (_lab("m_smig"), date in dates_smig)) if ici)
        sortie.append((date, p, s, p / (3 * s), motif))
    return sortie


def fig_plafond_smig():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    lignes = _ratio_smig()
    xs = [_x(d) for d, *_ in lignes] + [FIN + 1]
    ys = [r for *_, r, _ in lignes] + [lignes[-1][3]]
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    ax.plot(xs, ys, drawstyle="steps-post", color=BLEU, lw=2, label=ft(_lab("lg_ratio")))
    ax.axhline(1, color=GRIS, lw=1, ls=":", label=ft(_lab("lg_un")))
    releves = {"1961-04-01", "1976-01-01", "1986-05-01"}
    for date, _p, _s, r, _m in lignes:
        if date in releves:
            ax.plot([_x(date)], [r], "o", color=BLEU, ms=5)
            ax.annotate(_nombre(r, 2), (_x(date), r), textcoords="offset points",
                        xytext=(5, 5), ha="left", fontsize=8, color=BLEU, fontweight="bold")
    # La veille de chaque relèvement, et la dernière valeur.
    for date in ("1976-01-01", "1986-05-01"):
        avant = [l for l in lignes if l[0] < date][-1]
        ax.annotate(_nombre(avant[3], 2), (_x(date), avant[3]), textcoords="offset points",
                    xytext=(-5, -11), ha="right", fontsize=8, color=BLEU)
    ax.annotate(_nombre(ys[-1], 2), (xs[-1], ys[-1]), textcoords="offset points",
                xytext=(5, 0), ha="left", va="center", fontsize=8, color=BLEU,
                fontweight="bold")
    _ruptures_max(ax, ("rs_1976", "rs_1986"),
                  {"rs_1976": "1976-01-01", "rs_1986": "1986-05-01"})
    ax.set_xlim(1958, FIN + 5)
    ax.set_ylim(0, None)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda v, _p: f"{v:g}".replace(".", ",")))
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_ratio")), fontsize=8.5)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def table_plafond_smig():
    import pandas as pd
    return pd.DataFrame([{
        _lab("c_date"): date, _lab("c_plafond_date"): p, _lab("c_smig"): s,
        _lab("c_smig_trim"): round(3 * s, 3), _lab("c_ratio"): round(r, 3),
        _lab("c_motif"): motif,
    } for date, p, s, r, motif in _ratio_smig()])


# --------------------------- salaire unique, crèche, secteur public : montants par mois

# (clé de la série, diviseur pour passer au mois, couleur, épaisseur, trait, libellé)
_COURBES_FIXES = (
    ("salaire_unique_3", 3, BLEU, 2.2, "-", "lg_msu3"),
    ("salaire_unique_2", 3, BLEU_MOYEN, 1.6, "-", "lg_msu2"),
    ("salaire_unique_1", 3, BLEU_CLAIR, 1.6, "-", "lg_msu1"),
    ("creche_montant", 1, VERT, 2.0, "-", "lg_creche"),
    ("public_rang1", 1, ORANGE, 2.0, "--", "lg_public"),
)


def _mensuel(cle: str, diviseur: int) -> list[tuple[str, float | None]]:
    return [(d, None if v is None else v / diviseur) for d, v in _lignes(cle)]


def _annuel_fixe(cle: str, diviseur: int) -> list[tuple[int, float, float]]:
    lignes = _mensuel(cle, diviseur)
    indice = dinars_constants.ipc()
    sortie = []
    for annee in range(int(lignes[0][0][:4]), ANNEE_BASE + 1):
        moyenne = figtools.moyenne_annuelle_escalier(lignes, annee)
        if moyenne is not None and annee in indice:
            sortie.append((annee, moyenne, moyenne * indice[ANNEE_BASE] / indice[annee]))
    return sortie


def _fig_fixes(constants: bool):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(9.5, 6.2))
    for cle, diviseur, couleur, lw, ls, lg in _COURBES_FIXES:
        if constants:
            points = _annuel_fixe(cle, diviseur)
            xs, ys = [a for a, _, _ in points], [r for _, _, r in points]
            ax.plot(xs, ys, ls, marker="o", ms=2.8, color=couleur, lw=lw, label=ft(_lab(lg)))
            dec = 1
        else:
            lignes = _mensuel(cle, diviseur) + [(f"{FIN}-12-31", None)]
            lignes[-1] = (lignes[-1][0], lignes[-2][1])
            xs, ys = [_x(d) for d, _ in lignes], [v for _, v in lignes]
            ax.plot(xs, ys, drawstyle="steps-post", color=couleur, lw=lw, ls=ls,
                    label=ft(_lab(lg)))
            dec = 3
        ax.annotate(_nombre(ys[0], dec), (xs[0], ys[0]), textcoords="offset points",
                    xytext=(-5, 0), ha="right", va="center", fontsize=8, color=couleur,
                    fontweight="bold")
        # Deux courbes finissent à quelques dixièmes l'une de l'autre : étiquettes écartées.
        dy = {"salaire_unique_3": 7, "salaire_unique_2": -7, "salaire_unique_1": -12}.get(cle, 0)
        ax.annotate(_nombre(ys[-1], dec), (xs[-1], ys[-1]), textcoords="offset points",
                    xytext=(5, dy), ha="left", va="center", fontsize=8, color=couleur,
                    fontweight="bold")
    ax.set_xlim(1977, (ANNEE_BASE if constants else FIN) + 4)
    ax.set_ylim(0, None)
    ax.set_xlabel(ft(_lab("x")))
    ax.set_ylabel(ft(_lab("y_fixes_constants" if constants else "y_fixes_courants")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False, ncol=1)
    fig.tight_layout()
    return fig


def vues_montants_fixes():
    return [(_lab("vue_constants"), _fig_fixes(True)), (_lab("vue_courants"), _fig_fixes(False))]


def table_montants_fixes():
    import pandas as pd
    indice = dinars_constants.ipc()
    return pd.DataFrame([{
        _lab("c_grandeur"): _lab(lg), _lab("c_annee"): annee,
        _lab("c_courant"): round(moyenne, 3), _lab("c_ipc"): round(indice[annee], 1),
        _lab("c_reel"): round(reel, 1),
    } for cle, diviseur, _c, _lw, _ls, lg in _COURBES_FIXES
        for annee, moyenne, reel in _annuel_fixe(cle, diviseur)])

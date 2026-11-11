"""Figures du livre « L'agriculture — le soutien au producteur ».

D'OÙ VIENNENT LES DONNÉES. Les séries sont de petites séries déjà sourcées dans les
chapitres (agridata.tn, états financiers CTAMA au CMF, rapports sur les fonds spéciaux du
ministère des Finances, rapports d'activité de l'APIA, lois de finances). Elles ne sont pas
publiées comme séries de l'entrepôt `tunisia-data` : leur provenance est donc **déclarée
localement** par `figtools.register_provenance` (mêmes champs que le catalogue de
l'entrepôt), et leurs valeurs — déjà établies et citées — sont portées ici, inline. Chaque
valeur est celle du tableau correspondant du chapitre ; la clé de citation renvoie à la
source primaire.

Appel depuis un chunk Quarto `#| output: asis` étiqueté `#| label: fig-…` :

    import sys; sys.path.insert(0, "."); sys.path.insert(0, "../../../scripts")
    from figures import agriculture as ag
    ag.fig_eau_secadenord(caption="…", note_lecture="…")
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import figtools  # noqa: E402

BLEU, BLEU_CLAIR, ORANGE, GRIS = "#08519c", "#9ecae1", "#bc4c00", "#6e7781"


def _nombre(v: float, dec: int = 0) -> str:
    """Nombre à la française : virgule décimale, espace insécable pour les milliers."""
    if v is None:
        return ""
    texte = f"{v:,.{dec}f}"
    return texte.replace(",", "\N{NO-BREAK SPACE}").replace(".", ",")


def _lab(d: dict) -> str:
    return d.get(figtools.lang(), d["fr"])


# =========================================================================================
# Eau d'irrigation : prix de gros SECADENORD, médiane et fourchette, 2014-2025
# =========================================================================================
SERIE_EAU = "agri-eau-secadenord-tarif"

figtools.register_provenance(
    SERIE_EAU,
    titre=("Prix de vente de l'eau en gros par la SECADENORD aux gestionnaires régionaux : "
           "médiane et fourchette sur les points de livraison, 2014-2025"),
    titre_ar=("سعر بيع الماء بالجملة من قبل الشركة الوطنية لاستغلال وتوزيع المياه بالشمال "
              "للمتصرّفين الجهويّين: الوسيط والمجال، 2014-2025"),
    sources=["secadenordTarif2025"],
    unite="millime par m³",
    unite_ar="مليم للمتر المكعّب",
    perimetre=("prix de gros facturé par la SECADENORD à chaque commissariat régional au "
               "développement agricole et à la SONEDE, avant distribution à l'exploitant ; "
               "médiane, minimum et maximum calculés chaque année sur les 21 à 22 points de "
               "livraison suivis"),
    perimetre_ar=("سعر الجملة المحتسب من قبل الشركة لكلّ مندوبية جهوية للتنمية الفلاحية "
                  "وللشركة الوطنية لاستغلال وتوزيع المياه، قبل التوزيع على المستغلّ"),
    caveats=("Le prix de gros n'est pas le tarif facturé à l'agriculteur ; il en donne le "
             "plancher de coût. Les années 2014 à 2021 portent le même barème."),
    caveats_ar=("سعر الجملة ليس التعريفة المحتسبة على الفلاح؛ فهو يمثّل الحدّ الأدنى للكلفة. "
                "السنوات 2014 إلى 2021 تحمل نفس التعريفة."),
)

# annee : (médiane, minimum, maximum) en millime/m³, calculés sur les points de livraison.
_EAU = {
    2014: (54.4, 21.4, 110.4), 2015: (54.4, 21.4, 110.4), 2016: (54.4, 21.4, 110.4),
    2017: (54.4, 21.4, 110.4), 2018: (54.4, 21.4, 110.4), 2019: (54.4, 21.4, 110.4),
    2020: (54.4, 21.4, 110.4), 2021: (54.4, 21.4, 110.4),
    2022: (69.4, 36.4, 125.4), 2023: (65.3, 31.4, 120.4),
    2024: (74.4, 41.4, 130.4), 2025: (79.4, 46.4, 135.4),
}

_L_EAU = {
    "y": {"fr": "Prix de gros (millime/m³)", "ar": "سعر الجملة (مليم/م³)"},
    "med": {"fr": "Médiane", "ar": "الوسيط"},
    "band": {"fr": "Fourchette selon la zone (min–max)",
             "ar": "المجال حسب المنطقة (أدنى–أقصى)"},
    "c_annee": {"fr": "Année", "ar": "السنة"},
    "c_med": {"fr": "Médiane (millime/m³)", "ar": "الوسيط (مليم/م³)"},
    "c_min": {"fr": "Minimum (millime/m³)", "ar": "الأدنى (مليم/م³)"},
    "c_max": {"fr": "Maximum (millime/m³)", "ar": "الأقصى (مليم/م³)"},
}


def _fig_eau():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    annees = sorted(_EAU)
    med = [_EAU[a][0] for a in annees]
    lo = [_EAU[a][1] for a in annees]
    hi = [_EAU[a][2] for a in annees]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.fill_between(annees, lo, hi, color=BLEU_CLAIR, alpha=0.5,
                    label=ft(_lab(_L_EAU["band"])))
    ax.plot(annees, med, color=BLEU, lw=2.2, marker="o", ms=4,
            label=ft(_lab(_L_EAU["med"])))
    figtools.marque_rupture(ax, 2022)
    ax.set_ylabel(ft(_lab(_L_EAU["y"])))
    ax.set_xticks(annees)
    ax.set_xticklabels([str(a) for a in annees], rotation=45, fontsize=8)
    ax.set_ylim(0, 145)
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def _table_eau():
    import pandas as pd
    annees = sorted(_EAU)
    return pd.DataFrame({
        _lab(_L_EAU["c_annee"]): annees,
        _lab(_L_EAU["c_med"]): [_EAU[a][0] for a in annees],
        _lab(_L_EAU["c_min"]): [_EAU[a][1] for a in annees],
        _lab(_L_EAU["c_max"]): [_EAU[a][2] for a in annees],
    })


def fig_eau_secadenord(caption: str, note_lecture: str | None = None,
                       generated: str | None = None) -> None:
    figtools.figure_tabs(
        _fig_eau(), _table_eau(), SERIE_EAU,
        slug="fig_agri_eau_secadenord", caption=caption, note_lecture=note_lecture,
        nominal=False, generated=generated)


# =========================================================================================
# Helpers génériques pour les figures en lignes (une ou plusieurs séries annuelles)
# =========================================================================================
def _fig_lignes(courbes, ylabel, ymax=None, ruptures=()):
    """courbes : [(label, {annee: valeur}, couleur, marker)]. Trace des lignes annuelles."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    fig, ax = plt.subplots(figsize=(8, 5))
    toutes = sorted({a for _, d, _, _ in courbes for a in d})
    for label, d, couleur, marker in courbes:
        xs = sorted(d)
        ys = [d[a] for a in xs]
        ax.plot(xs, ys, color=couleur, lw=2.2, marker=marker, ms=5, label=ft(label))
    for an in ruptures:
        figtools.marque_rupture(ax, an)
    ax.set_ylabel(ft(ylabel))
    ax.set_xticks(toutes)
    ax.set_xticklabels([str(a) for a in toutes], rotation=45, fontsize=8)
    if ymax:
        ax.set_ylim(0, ymax)
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def _table_wide(annees, colonnes):
    """colonnes : [(libellé, {annee: valeur})]. Table large annee × grandeurs."""
    import pandas as pd
    out = {_lab({"fr": "Année", "ar": "السنة"}): list(annees)}
    for lib, d in colonnes:
        out[_lab(lib)] = [d.get(a) for a in annees]
    return pd.DataFrame(out)


# =========================================================================================
# Budget de la mission Agriculture, 2020-2025 (prévision, million de dinars)
# =========================================================================================
SERIE_BUDGET = "agri-budget-mission"
figtools.register_provenance(
    SERIE_BUDGET,
    titre="Budget de la mission Agriculture, crédits de paiement sur ressources de l'État, 2020-2025",
    titre_ar="ميزانية مهمة الفلاحة، اعتمادات الدفع على موارد الدولة، 2020-2025",
    sources=["tn-pap-agriculture-2020", "tn-pap-agriculture-2021", "tn-pap-agriculture-2022",
             "tn-pap-agriculture-2024", "tn-pap-agriculture-2025"],
    unite="million de dinars", unite_ar="مليون دينار",
    perimetre=("crédits de paiement de la mission, sur ressources de l'État, hors ressources "
               "propres des établissements ; montant de la loi de finances initiale de chaque année"),
    perimetre_ar="اعتمادات الدفع للمهمة على موارد الدولة، دون الموارد الذاتية للمؤسسات",
    caveats="Dinars courants. Nomenclature budget-programme stable depuis 2020.",
    caveats_ar="بالدينار الجاري. تبويب الميزانية حسب البرامج قارّ منذ 2020.",
)
_BUDGET = {2020: 1726.9, 2021: 1780.0, 2022: 1850.0, 2023: 1965.0, 2024: 2202.1, 2025: 2279.1}


def fig_budget_mission(caption, note_lecture=None, generated=None):
    fig = _fig_lignes([({"fr": "Budget de la mission", "ar": "ميزانية المهمة"}, _BUDGET, BLEU, "o")],
                      {"fr": "Crédits de paiement (millions de dinars)", "ar": "اعتمادات الدفع (مليون دينار)"},
                      ymax=2500)
    df = _table_wide(sorted(_BUDGET),
                     [({"fr": "Budget de la mission (MD)", "ar": "ميزانية المهمة (م.د)"}, _BUDGET)])
    figtools.figure_tabs(fig, df, SERIE_BUDGET, slug="fig_agri_budget_mission",
                         caption=caption, note_lecture=note_lecture, generated=generated)


# =========================================================================================
# Primes d'investissement APIA : approuvées (2010-2016) et décaissées (2018-2023)
# =========================================================================================
SERIE_APIA = "agri-apia-primes"
figtools.register_provenance(
    SERIE_APIA,
    titre="Primes d'investissement agricole de l'APIA : approuvées (2010-2016) et décaissées (2018-2023)",
    titre_ar="منح الاستثمار الفلاحي للوكالة: المصادق عليها (2010-2016) والمصروفة (2018-2023)",
    sources=["apia-repartition-doa-2010-2017", "apia-rapport-activite-2018",
             "apia-rapport-activite-2019", "apia-rapport-activite-2020",
             "apia-rapport-activite-2021", "apia-rapport-activite-2022",
             "apia-rapport-activite-2023", "banquemondiale2014-revolution-inachevee"],
    unite="million de dinars", unite_ar="مليون دينار",
    perimetre=("primes approuvées : périmètre agricole (agriculture, pêche, aquaculture, première "
               "transformation) ; primes décaissées : ordres de paiement exécutés par l'APIA ; "
               "point 2009 = primes versées d'après la Banque mondiale, base différente"),
    perimetre_ar=("المنح المصادق عليها: النطاق الفلاحي؛ المنح المصروفة: أذون الصرف المنفّذة من الوكالة"),
    caveats=("Approuvé et décaissé ne se chaînent pas (2017 manquant) ; le point 2009 est d'une "
             "autre source. Dinars courants."),
    caveats_ar="المصادق عليه والمصروف لا يتّصلان (2017 مفقودة)؛ ونقطة 2009 من مصدر آخر. بالدينار الجاري.",
)
_APIA_APPR = {2010: 38, 2011: 40, 2012: 35, 2013: 36, 2014: 46, 2015: 44, 2016: 63}
_APIA_VERS = {2009: 54, 2018: 52.8, 2019: 112.5, 2020: 62, 2021: 89, 2022: 44.2, 2023: 60.1}


def fig_apia_primes(caption, note_lecture=None, generated=None):
    fig = _fig_lignes([
        ({"fr": "Primes approuvées (périmètre agricole)", "ar": "المنح المصادق عليها"},
         _APIA_APPR, BLEU, "o"),
        ({"fr": "Primes décaissées", "ar": "المنح المصروفة"}, _APIA_VERS, ORANGE, "s"),
    ], {"fr": "Primes (millions de dinars)", "ar": "المنح (مليون دينار)"}, ymax=130)
    annees = sorted(set(_APIA_APPR) | set(_APIA_VERS))
    df = _table_wide(annees, [
        ({"fr": "Approuvées (MD)", "ar": "المصادق عليها (م.د)"}, _APIA_APPR),
        ({"fr": "Décaissées (MD)", "ar": "المصروفة (م.د)"}, _APIA_VERS)])
    figtools.figure_tabs(fig, df, SERIE_APIA, slug="fig_agri_apia_primes",
                         caption=caption, note_lecture=note_lecture, generated=generated)


# =========================================================================================
# Fonds de calamités : dotation de l'État et indemnisations versées, 2018-2023
# =========================================================================================
SERIE_FONDS = "agri-fonds-calamites"
figtools.register_provenance(
    SERIE_FONDS,
    titre="Fonds d'indemnisation des calamités agricoles : dotation de l'État et indemnisations versées, 2018-2023",
    titre_ar="صندوق التعويض عن الجوائح الفلاحية: منحة الدولة والتعويضات المصروفة، 2018-2023",
    sources=["tn-minfin-fonds-speciaux-2022", "tn-minfin-fonds-speciaux-2025"],
    unite="million de dinars", unite_ar="مليون دينار",
    perimetre=("réalisations d'exécution du compte spécial du Trésor (Trésorerie Générale, CTAMA) ; "
               "le fonds démarre le 28 octobre 2019"),
    perimetre_ar="إنجازات تنفيذ الحساب الخاصّ للخزينة (الخزينة العامة، كتاما)؛ انطلق الصندوق في 28 أكتوبر 2019",
    caveats="Dinars courants. Dotation et indemnités nulles en 2018, le fonds n'ayant pas démarré.",
    caveats_ar="بالدينار الجاري. المنحة والتعويضات منعدمة في 2018 قبل انطلاق الصندوق.",
)
_FONDS_DOT = {2018: 0, 2019: 30, 2020: 30, 2021: 30, 2022: 30, 2023: 30}
_FONDS_IND = {2018: 0, 2019: 0, 2020: 20.3, 2021: 20.0, 2022: 28.4, 2023: 59.3}


def fig_fonds_calamites(caption, note_lecture=None, generated=None):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    annees = sorted(_FONDS_DOT)
    xs = list(range(len(annees)))
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar([x - 0.2 for x in xs], [_FONDS_DOT[a] for a in annees], width=0.4, color=BLEU,
           label=ft(_lab({"fr": "Dotation de l'État", "ar": "منحة الدولة"})))
    ax.bar([x + 0.2 for x in xs], [_FONDS_IND[a] for a in annees], width=0.4, color=ORANGE,
           label=ft(_lab({"fr": "Indemnisations versées", "ar": "التعويضات المصروفة"})))
    ax.set_ylabel(ft(_lab({"fr": "Millions de dinars", "ar": "مليون دينار"})))
    ax.set_xticks(xs)
    ax.set_xticklabels([str(a) for a in annees], fontsize=9)
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    df = _table_wide(annees, [
        ({"fr": "Dotation de l'État (MD)", "ar": "منحة الدولة (م.د)"}, _FONDS_DOT),
        ({"fr": "Indemnisations versées (MD)", "ar": "التعويضات المصروفة (م.د)"}, _FONDS_IND)])
    figtools.figure_tabs(fig, df, SERIE_FONDS, slug="fig_agri_fonds_calamites",
                         caption=caption, note_lecture=note_lecture, generated=generated)


# =========================================================================================
# CTAMA : primes encaissées auprès des assurés, 2017-2020
# =========================================================================================
SERIE_CTAMA = "agri-ctama-primes"
figtools.register_provenance(
    SERIE_CTAMA,
    titre="Primes encaissées par la CTAMA auprès de ses assurés, 2017-2020",
    titre_ar="المبالغ المقبوضة من المؤمَّن لهم لدى كتاما، 2017-2020",
    sources=["CtamaEF2018", "CtamaEF2020"],
    unite="million de dinars", unite_ar="مليون دينار",
    perimetre=("encaissements de primes reçues des assurés (tableau de flux de trésorerie), tous "
               "risques de la caisse confondus ; la CTAMA est l'assureur dominant du risque agricole"),
    perimetre_ar="المبالغ المقبوضة من المؤمَّن لهم (جدول التدفّقات)، لكامل أخطار الصندوق",
    caveats="Dinars courants.", caveats_ar="بالدينار الجاري.",
)
_CTAMA = {2017: 80.0, 2018: 90.5, 2019: 100.1, 2020: 123.1}


def fig_ctama_primes(caption, note_lecture=None, generated=None):
    fig = _fig_lignes([({"fr": "Primes encaissées", "ar": "المبالغ المقبوضة"}, _CTAMA, BLEU, "o")],
                      {"fr": "Millions de dinars", "ar": "مليون دينار"}, ymax=140)
    df = _table_wide(sorted(_CTAMA),
                     [({"fr": "Primes encaissées (MD)", "ar": "المبالغ المقبوضة (م.د)"}, _CTAMA)])
    figtools.figure_tabs(fig, df, SERIE_CTAMA, slug="fig_agri_ctama_primes",
                         caption=caption, note_lecture=note_lecture, generated=generated)

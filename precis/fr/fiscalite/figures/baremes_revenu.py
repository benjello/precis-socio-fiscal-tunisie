"""Taux marginal et taux moyen des barèmes de l'impôt sur le revenu du livre *Fiscalité*.

Deux figures, lues par `figtools.series()` seulement (séries de tranches `cpe-bareme` et
`irpp-bareme`, au format de `openfisca_tables.lignes_tranches`) et tracées par le composant
`taux_bareme` : la contribution personnelle d'État (cinq barèmes, revenus de 1962 à 1986) et
l'impôt sur le revenu (trois barèmes, revenus de 1990, 2017 et 2025).

Les seuils sont en dinars courants de l'année de chaque barème. Le taux moyen est le droit
du barème rapporté au revenu, barème appliqué par tranche ; il ne tient pas compte des
correctifs que le texte ajoute au barème (plafond de la cotisation effective, exemption
des petits revenus, minimum d'impôt).
"""
from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[4] / "scripts"
sys.path.insert(0, str(_SCRIPTS))
import figtools  # noqa: E402
import taux_bareme  # noqa: E402

SERIE_CPE = "cpe-bareme"
SERIE_IRPP = "irpp-bareme"

ETATS_CPE = ("1962-01-01", "1965-01-01", "1980-01-01", "1983-01-01", "1986-01-01")
COULEURS_CPE = {"1962-01-01": "#8250df", "1965-01-01": "#bf3989", "1980-01-01": "#bf8700",
                "1983-01-01": "#0969da", "1986-01-01": "#1a7f37"}
# Deux échelles : les barèmes de 1962 à 1980 s'arrêtent au-dessous de 11 000 D, ceux de 1983 et
# de 1986 vont à 80 000 et 100 000 D.
GROUPES_CPE = (("g_cpe_ancien", ("1962-01-01", "1965-01-01", "1980-01-01"), 12_000,
                (0, 3_000, 6_000, 9_000, 12_000)),
               ("g_cpe_recent", ("1983-01-01", "1986-01-01"), 100_000,
                (0, 25_000, 50_000, 75_000, 100_000)))
ASSIETTES_CPE = {
    "g_cpe_ancien": (180, 640, 1_200, 2_000, 4_000, 6_000, 8_500, 10_200),
    "g_cpe_recent": (900, 3_000, 8_000, 25_000, 50_000, 80_000, 100_000),
}

ETATS_IRPP = ("1990-01-01", "2017-01-01", "2025-01-01")
COULEURS_IRPP = {"1990-01-01": "#bf8700", "2017-01-01": "#0969da", "2025-01-01": "#1a7f37"}
REVENU_MAX_IRPP = 80_000
ASSIETTES_IRPP = (1_500, 5_000, 10_000, 20_000, 30_000, 40_000, 50_000, 70_000, 80_000)

_L = {
    "g_cpe_ancien": {"fr": "Revenus de 1962, 1965 et 1980", "ar": "مداخيل 1962 و1965 و1980"},
    "g_cpe_recent": {"fr": "Revenus de 1983 et 1986", "ar": "مداخيل 1983 و1986"},
    "etat_cpe_1962-01-01": {"fr": "revenus de 1962 (loi n° 62-73)",
                            "ar": "مداخيل 1962 (القانون عدد 62-73)"},
    "etat_cpe_1965-01-01": {"fr": "revenus de 1965 (loi n° 65-46)",
                            "ar": "مداخيل 1965 (القانون عدد 65-46)"},
    "etat_cpe_1980-01-01": {"fr": "revenus de 1980 (loi n° 79-66)",
                            "ar": "مداخيل 1980 (القانون عدد 79-66)"},
    "etat_cpe_1983-01-01": {"fr": "revenus de 1983 (loi n° 82-91)",
                            "ar": "مداخيل 1983 (القانون عدد 82-91)"},
    "etat_cpe_1986-01-01": {"fr": "revenus de 1986 (loi n° 85-109)",
                            "ar": "مداخيل 1986 (القانون عدد 85-109)"},
    "court_1962-01-01": {"fr": "1962", "ar": "1962"},
    "court_1965-01-01": {"fr": "1965", "ar": "1965"},
    "court_1980-01-01": {"fr": "1980", "ar": "1980"},
    "court_1983-01-01": {"fr": "1983", "ar": "1983"},
    "court_1986-01-01": {"fr": "1986", "ar": "1986"},
    "x_cpe": {"fr": "Revenu net imposable (dinars courants)",
              "ar": "الدخل الصافي الخاضع للضريبة (بالدينار الجاري)"},
    "title_cpe": {"fr": ("Contribution personnelle d'État : taux marginal et taux moyen du "
                         "barème selon le revenu, revenus de 1962 à 1986"),
                  "ar": ("المساهمة الشخصية للدولة: النسبة الحدية والنسبة المتوسّطة للجدول "
                         "حسب الدخل، مداخيل 1962 إلى 1986")},
    "c_groupe": {"fr": "Barèmes", "ar": "الجداول"},
    "c_revenu": {"fr": "Revenu net imposable (D)", "ar": "الدخل الصافي الخاضع للضريبة (د)"},
    "etat_irpp_1990-01-01": {"fr": "revenus de 1990 à 2016 (code de 1989)",
                             "ar": "مداخيل 1990 إلى 2016 (مجلة 1989)"},
    "etat_irpp_2017-01-01": {"fr": "revenus de 2017 à 2024 (loi n° 2016-78)",
                             "ar": "مداخيل 2017 إلى 2024 (القانون عدد 2016-78)"},
    "etat_irpp_2025-01-01": {"fr": "revenus à compter de 2025 (loi n° 2024-48)",
                             "ar": "مداخيل ابتداء من 2025 (القانون عدد 2024-48)"},
    "court_irpp_1990-01-01": {"fr": "1990", "ar": "1990"},
    "court_irpp_2017-01-01": {"fr": "2017", "ar": "2017"},
    "court_irpp_2025-01-01": {"fr": "2025", "ar": "2025"},
    "g_irpp": {"fr": "Impôt sur le revenu", "ar": "الضريبة على الدخل"},
    "title_irpp": {"fr": ("IRPP : taux marginal et taux moyen du barème selon le revenu, "
                          "revenus de 1990, 2017 et 2025"),
                   "ar": ("الضريبة على الدخل: النسبة الحدية والنسبة المتوسّطة للجدول حسب "
                          "الدخل، مداخيل 1990 و2017 و2025")},
    "y_taux": {"fr": "Taux (%)", "ar": "النسبة (%)"},
}


def _lab(cle: str) -> str:
    return _L[cle].get(figtools.lang(), _L[cle]["fr"])


def _bareme(serie: str, cle: str, date: str):
    return taux_bareme.bareme_a_la_date(figtools.series(serie), "bareme", cle, date)


def _panneaux_cpe():
    return [(_lab(g), {e: _bareme(SERIE_CPE, "cpe", e) for e in etats}, g)
            for g, etats, _m, _t in GROUPES_CPE]


def fig_cpe():
    """Deux cadres (barèmes de 1962 à 1980, de 1983 et 1986) : marginal en escalier, moyen en courbe."""
    p = _panneaux_cpe()
    return taux_bareme.fig_taux_moyens_marginaux(
        [(lib, etats) for lib, etats, _g in p], couleurs=COULEURS_CPE,
        libelles_etats={e: _lab("etat_cpe_" + e) for e in ETATS_CPE},
        assiette_max=[m for _g, _e, m, _t in GROUPES_CPE],
        xticks=[t for _g, _e, _m, t in GROUPES_CPE],
        xlabel=_lab("x_cpe"), ylabel=_lab("y_taux"), titre=_lab("title_cpe"), ymax=92)


def table_cpe():
    import pandas as pd
    p = _panneaux_cpe()
    morceaux = [
        taux_bareme.table_taux(
            [(lib, etats)], {e: _lab("court_" + e) for e in etats}, ASSIETTES_CPE[g],
            entete_panneau=_lab("c_groupe"), entete_assiette=_lab("c_revenu"))
        for lib, etats, g in p]
    return pd.concat(morceaux, ignore_index=True)


def _panneau_irpp():
    return [(_lab("g_irpp"), {e: _bareme(SERIE_IRPP, "irpp", e) for e in ETATS_IRPP})]


def fig_irpp():
    """Un cadre, trois barèmes : marginal en escalier, moyen en courbe."""
    return taux_bareme.fig_taux_moyens_marginaux(
        _panneau_irpp(), couleurs=COULEURS_IRPP,
        libelles_etats={e: _lab("etat_irpp_" + e) for e in ETATS_IRPP},
        assiette_max=REVENU_MAX_IRPP, colonnes=1, largeur=9.0,
        xticks=(0, 20_000, 40_000, 60_000, 80_000),
        xlabel=_lab("x_cpe"), ylabel=_lab("y_taux"), titre=_lab("title_irpp"), ymax=45)


def table_irpp():
    return taux_bareme.table_taux(
        _panneau_irpp(), {e: _lab("court_irpp_" + e) for e in ETATS_IRPP}, ASSIETTES_IRPP,
        entete_panneau=_lab("c_groupe"), entete_assiette=_lab("c_revenu"))


figtools.register_provenance(
    SERIE_CPE,
    titre=("Tarif de la contribution personnelle d'État, par tranche de revenu net imposable, "
           "pour les revenus de 1962, 1965, 1980, 1983 et 1986"),
    titre_ar=("تعريفة المساهمة الشخصية للدولة، حسب شريحة الدخل الصافي الخاضع للضريبة، "
              "لمداخيل 1962 و1965 و1980 و1983 و1986"),
    sources=["loi-62-73-cpe", "lf-1966", "loi79-66-lf1980", "lf-1983", "lf-1986"],
    unite="taux fixé pour la tranche, en pourcentage ; seuils en dinars courants",
    unite_ar="النسبة المحدَّدة للشريحة بالمائة؛ والعتبات بالدينار الجاري",
    perimetre=("cinq tarifs, une ligne par tranche et par tarif, avec le texte du Journal "
               "officiel qui le fixe ; les tarifs antérieurs à 1962 et ceux des revenus de 1966 "
               "à 1979 ne sont pas publiés ici"),
    perimetre_ar=("خمس تعريفات، سطر لكلّ شريحة ولكلّ تعريفة، مع نصّ الرائد الرسمي الذي يضبطها؛ "
                  "ولا تُنشر هنا التعريفات السابقة لسنة 1962 ولا تعريفات مداخيل 1966 إلى 1979"),
    caveats=("Le taux moyen est celui du tarif, barème appliqué par tranche. Il ne tient pas "
             "compte du plafond de la cotisation effective, ni de l'exemption des revenus qui "
             "ne dépassent pas 100 dinars en 1965, ni du SMIG en 1986."),
    caveats_ar=("النسبة المتوسّطة هي نسبة التعريفة بتطبيق الجدول حسب الشرائح، دون اعتبار سقف "
                "الأداء الفعلي ولا إعفاء المداخيل التي لا تتجاوز 100 دينار في 1965 ولا الأجر "
                "الأدنى المضمون في 1986."),
)

figtools.register_provenance(
    SERIE_IRPP,
    titre=("Barème de l'impôt sur le revenu des personnes physiques (art. 44 § I du code), par "
           "tranche de revenu net imposable, pour les revenus de 1990, 2017 et 2025"),
    titre_ar=("جدول الضريبة على دخل الأشخاص الطبيعيين (الفصل 44 §I من المجلة)، حسب شريحة "
              "الدخل الصافي الخاضع للضريبة، لمداخيل 1990 و2017 و2025"),
    sources=["code-irpp-is-1990", "lf-2017", "lf-2025"],
    unite="taux fixé pour la tranche, en pourcentage ; seuils en dinars courants",
    unite_ar="النسبة المحدَّدة للشريحة بالمائة؛ والعتبات بالدينار الجاري",
    perimetre=("trois barèmes, une ligne par tranche et par date d'effet ; les dates sont des "
               "années de revenus, au 1er janvier"),
    perimetre_ar="ثلاثة جداول، سطر لكلّ شريحة ولكلّ تاريخ نفاذ؛ والتواريخ سنوات مداخيل في غرّة جانفي",
    caveats=("Le taux moyen est celui du barème, barème appliqué par tranche, avant déductions "
             "pour charges de famille, minimum d'impôt et régimes dérogatoires."),
    caveats_ar=("النسبة المتوسّطة هي نسبة الجدول بتطبيقه حسب الشرائح، قبل الطروحات العائلية "
                "والحدّ الأدنى للضريبة والأنظمة الاستثنائية."),
)

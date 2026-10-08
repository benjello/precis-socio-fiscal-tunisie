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
SERIE_IPC_RECENT = "bct-ipc-base2015"
# Année des dinars constants : la dernière dont l'indice des prix est publié, jamais une année
# à venir.
ANNEE_BASE = 2024
# Avant le SMIG. Seconde zone : plancher horaire jusqu'à sa suppression le 1er mai 1968
# (décrets n° 61-145, art. 6, et n° 65-561, art. 5 ; n° 68-97). Indemnité de cherté de vie :
# 0,020 D l'heure en sus du minimum, du 1er mai 1971 à l'institution du SMIG (décret n° 71-164).
HEURES_48H = 208
ZONE_II = [(dt.date(1961, 4, 1), 0.060), (dt.date(1966, 1, 1), 0.066)]
FIN_ZONE_II = dt.date(1968, 5, 1)
ICV_HORAIRE, DEBUT_ICV, FIN_ICV = 0.020, dt.date(1971, 5, 1), dt.date(1974, 1, 1)

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
    "r_1974": {"fr": "institution du SMIG et du SMAG", "ar": "إحداث الأجر الأدنى المضمون"},
    "lg_zone2": {"fr": "Minimum de la seconde zone, 1961-1968",
                 "ar": "الأجر الأدنى بالمنطقة الثانية، 1961-1968"},
    "lg_icv": {"fr": "Minimum et indemnité de cherté de vie, 1971-1973",
               "ar": "الأجر الأدنى مع منحة غلاء المعيشة، 1971-1973"},
    "c_zone2_reel": {"fr": f"Seconde zone, moyenne annuelle (D de {ANNEE_BASE})",
                     "ar": f"المنطقة الثانية، المعدّل السنوي (د {ANNEE_BASE})"},
    "c_icv_reel": {"fr": f"Minimum et indemnité de cherté de vie (D de {ANNEE_BASE})",
                   "ar": f"الأجر الأدنى مع منحة غلاء المعيشة (د {ANNEE_BASE})"},
    "vue_courants": {"fr": "Dinars courants", "ar": "بالدينار الجاري"},
    "vue_courants_log": {"fr": "Dinars courants, échelle logarithmique",
                         "ar": "بالدينار الجاري، سلّم لوغاريتمي"},
    "vue_constants": {"fr": f"Dinars de {ANNEE_BASE}", "ar": f"بدينار سنة {ANNEE_BASE}"},
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
    """Indice des prix, base 1970 ; prolongé au-delà de sa dernière année par la variation de
    l'indice en base 2015 que relaie la Banque centrale."""
    ipc = {int(r.annee): float(r.indice_base1970)
           for r in figtools.series(SERIE_IPC).itertuples()}
    recent = {int(r.annee): float(r.valeur)
              for r in figtools.series(SERIE_IPC_RECENT).itertuples()}
    fin = max(ipc)
    for annee in sorted(a for a in recent if a > fin and fin in recent):
        ipc[annee] = ipc[fin] * recent[annee] / recent[fin]
    return ipc


def _zone2_mensuel(jour: dt.date):
    """Minimum mensuel (208 heures) de la seconde zone ; celui de la première après sa suppression."""
    if jour >= FIN_ZONE_II:
        return None
    taux = [v for d0, v in ZONE_II if d0 <= jour]
    return taux[-1] * HEURES_48H if taux else None


def _moyenne_mois(f, annee: int):
    mois = [f(dt.date(annee, m, 1)) for m in range(1, 13)]
    return None if any(v is None for v in mois) else sum(mois) / 12


def _escaliers(ax, d, colonne, facteur=1.0, **kw):
    x = [dt.datetime(j.year, j.month, j.day) for j in d["jour"]]
    y = [None if v != v else v * facteur for v in d[colonne]]
    paires = [(a, b) for a, b in zip(x, y) if b is not None]
    ax.plot([a for a, _ in paires], [b for _, b in paires], drawstyle="steps-post", **kw)


def _ruptures(ax, en_dates=True):
    for annee, cle in ((1974, "r_1974"), (1981, "r_1981"), (2026, "r_2026")):
        x = dt.datetime(annee, 1, 1) if en_dates else annee - 0.5
        ax.axvline(x, color="#57606a", ls=(0, (2, 2)), lw=1, zorder=1)
        # Deux ruptures voisines : l'étiquette de la seconde passe à la ligne du dessous.
        texte = ("\n" if annee == 1981 else "") + figtools.fig_text(_lab(cle))
        ax.annotate(texte, xy=(x, 1), xycoords=("data", "axes fraction"),
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
    # Avant 1974 : la seconde zone, et le minimum augmenté de l'indemnité de cherté de vie.
    z = [(dt.datetime(d0.year, d0.month, d0.day), v * HEURES_48H) for d0, v in ZONE_II]
    z.append((dt.datetime(FIN_ZONE_II.year, FIN_ZONE_II.month, 1), z[-1][1]))
    ax.plot([a for a, _ in z], [b for _, b in z], drawstyle="steps-post", color=BLEU, lw=1.2,
            ls=":", label=ft(_lab("lg_zone2")))
    base = _en_vigueur(d, "smig_48h_mensuel", DEBUT_ICV) + ICV_HORAIRE * HEURES_48H
    ax.plot([dt.datetime(DEBUT_ICV.year, DEBUT_ICV.month, 1), dt.datetime(FIN_ICV.year, 1, 1)],
            [base, base], color=VIOLET, lw=1.6, label=ft(_lab("lg_icv")))
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
        zone2 = _moyenne_mois(_zone2_mensuel, annee) if annee < FIN_ZONE_II.year else None
        icv = None
        if DEBUT_ICV.year <= annee < FIN_ICV.year:
            icv = _moyenne_mois(lambda j: _en_vigueur(d, "smig_48h_mensuel", j)
                                + (ICV_HORAIRE * HEURES_48H if j >= DEBUT_ICV else 0), annee)
        lignes.append((annee, smig, None if smig is None else smig * coef,
                       None if smag is None else smag * 26 * coef, ipc[annee],
                       None if zone2 is None else zone2 * coef,
                       None if icv is None else icv * coef))
    return lignes


def fig_reel():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _reel()
    fig, ax = plt.subplots(figsize=(10, 5.6))
    ax.plot([l[0] for l in r], [l[2] for l in r], "-o", ms=3, color=BLEU, lw=2,
            label=ft(_lab("lg_48")))
    pts = [(l[0], l[3]) for l in r if l[3] is not None]
    ax.plot([a for a, _ in pts], [s for _, s in pts], "--", color=VERT, lw=1.4,
            label=ft(_lab("lg_smag26")))
    for k, cle, style in ((5, "lg_zone2", dict(color=BLEU, ls=":", lw=1.2, marker="o", ms=2)),
                          (6, "lg_icv", dict(color=VIOLET, lw=1.6, marker="o", ms=2.5))):
        pts = [(l[0], l[k]) for l in r if l[k] is not None]
        ax.plot([a for a, _ in pts], [s for _, s in pts], label=ft(_lab(cle)), **style)
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


def vues_evolution():
    """Le salaire minimum en une figure : dinars courants (deux échelles) et dinars constants."""
    return [(_lab("vue_courants"), _fig_nominal(False)),
            (_lab("vue_constants"), fig_reel()),
            (_lab("vue_courants_log"), _fig_nominal(True))]


def table_reel():
    import pandas as pd
    r = _reel()
    return pd.DataFrame({
        _lab("c_annee"): [a for a, *_ in r],
        _lab("c_48_moy"): [None if l[1] is None else round(l[1], 3) for l in r],
        _lab("c_ipc"): [round(l[4], 1) for l in r],
        _lab("c_48_reel"): [None if l[2] is None else round(l[2], 1) for l in r],
        _lab("c_smag_reel"): [None if l[3] is None else round(l[3], 1) for l in r],
        _lab("c_zone2_reel"): [None if l[5] is None else round(l[5], 1) for l in r],
        _lab("c_icv_reel"): [None if l[6] is None else round(l[6], 1) for l in r],
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
BLEU_REFORME = "#0550ae"

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
    "ref_1993": {"fr": "réforme de 1993", "ar": "إصلاح 1993"},
    "ref_2000": {"fr": "Fonds national de l'emploi, 2000", "ar": "الصندوق الوطني للتشغيل، 2000"},
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
    # Les deux réformes que couvre la série : un trait plein, étiqueté là où les courbes
    # laissent de la place — au pied du cadre en échelle logarithmique, en haut sinon.
    for annee, cle, a_gauche in ((1993, "ref_1993", False), (2000, "ref_2000", True)):
        ax.axvline(annee, color=BLEU_REFORME, lw=0.9, alpha=0.6, zorder=1)
        if log:
            pos = dict(xy=(annee, 0), xytext=(3, 4), ha="left", va="bottom")
        elif a_gauche:
            pos = dict(xy=(annee, 0.93), xytext=(-3, 0), ha="right", va="center")
        else:
            pos = dict(xy=(annee, 0.80), xytext=(3, 0), ha="left", va="center")
        ax.annotate(ft(_lab(cle)), xycoords=("data", "axes fraction"),
                    textcoords="offset points", fontsize=7, color=BLEU_REFORME, **pos)
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


# ---------------------------------------------------------------- salaires versés dans le privé
#
# Trois figures de la section « Les salaires versés dans le secteur privé » du chapitre du
# salaire minimum. Séries snapshotées depuis l'entrepôt `tunisia-data` :
#
#   - `cnss-salaire-moyen-declare-smig` : salaire moyen déclaré à la CNSS (régime des salariés
#     non agricoles), 1970-2018, une ligne par année ET par édition de l'annuaire, livrée par
#     segments. AUCUN RACCORD : chaque segment est tracé par son propre appel, et les années
#     2002-2006, imprimées par les deux éditions, sont tracées deux fois ;
#   - `cnss-pyramide-smig-2000-2018` : salariés déclarés par classe de salaire en SMIG ;
#   - `ins-salaires-prive-annuel` : taux d'évolution du salaire du privé non agricole (INS),
#     chaîné sur les quatre trimestres de l'année ;
#   - `ins-micro-entreprises-salaries-smig`, `ins-ees-salaire-base-permanents-smig` : deux
#     enquêtes de l'INS, données en TABLEAU, jamais superposées aux séries de la CNSS.
#
# Le SMIG est celui du chapitre (`marche-travail-smig-smag`, moyenne annuelle du régime de
# 48 heures) ; `_salaire_declare` contrôle qu'il coïncide avec la colonne de la série de la CNSS.

SERIE_SALAIRE = "cnss-salaire-moyen-declare-smig"
SERIE_PYRAMIDE = "cnss-pyramide-smig-2000-2018"
SERIE_INS_TAUX = "ins-salaires-prive-annuel"
SERIE_MICRO = "ins-micro-entreprises-salaries-smig"
SERIE_EES = "ins-ees-salaire-base-permanents-smig"

# Salariés déclarés les quatre trimestres de 2013 et leur masse salariale : annuaire
# statistique 2013 de la CNSS, page 36 du fichier PDF (colonne « 4 trimestres » du tableau
# selon le nombre de trimestres déclarés). Seule année où ce quotient se calcule ; il n'est
# pas dans la série de l'entrepôt.
QUATRE_TRIMESTRES_2013 = {"annee": 2013, "salaries": 800_558, "masse": 8_834_648_773}
# Dernière année échue du SMIG en moyenne annuelle (les montants de 2026 à 2028 sont fixés
# d'avance) et première année de l'indice de la figure des évolutions.
ANNEE_BASE_INDICE, FIN_INDICES = 2001, 2025
JAUNE, BLEU_CLAIR = "#d4a72c", "#6baed6"

# Les annuaires dont viennent les valeurs tracées, à la place de la clé générique du catalogue.
figtools.register_provenance(SERIE_SALAIRE, **{
    **figtools.meta(SERIE_SALAIRE),
    "sources": ["cnss-annuaire-2006", "cnss-annuaire-2018", "cnss-annuaire-2013",
                "decret61-145", "decret74-63", "decret81-437", "decret92-1299"],
    "titre_ar": ("الصندوق الوطني للضمان الاجتماعي، الأجراء في القطاع غير الفلاحي: معدّل الأجر "
                 "المصرّح به ونسبته إلى الأجر الأدنى المضمون لنظام 48 ساعة، 1970-2018، حسب "
                 "المقاطع"),
    "unite_ar": "دينار جارٍ (كتلة الأجور؛ الأجر في السنة وفي الشهر)، أشخاص، نسبة",
    "perimetre_ar": ("نظام الأجراء في القطاع غير الفلاحي؛ سطر لكلّ سنة ولكلّ طبعة من الدليل "
                     "الإحصائي (طبعة 2006: 1970-1999 و2002-2006؛ طبعة 2018: 2000-2018)؛ معدّل "
                     "الأجر السنوي المصرّح به = كتلة الأجور المصرّح بها ÷ الأجراء المصرّح بهم؛ "
                     "الأجر الشهري = ÷ 12"),
    "caveats_ar": ("سلسلة محسوبة تُقرأ حسب المقاطع، دون وصل ولا تصحيح. طبعتان للسنوات "
                   "2002-2006 بقيم مختلفة، وكلتاهما محفوظة. انقطاعات: 1974، إدماج منحة غلاء "
                   "المعيشة في الأجر الأدنى؛ 1981، المنحة التكميلية الوقتية تدخل الأجر الأدنى "
                   "وتبقى خارج قاعدة الاشتراكات؛ 1988، الدليل يدرجها في الأجور المصرّح بها؛ "
                   "2003، سيارات الأجرة واللواج. المقام يشمل كلّ أجير صُرّح به مرّة واحدة على "
                   "الأقلّ في السنة، فالأجر الشهري والنسبة مشدودان إلى الأسفل. تتوقّف السلسلة "
                   "سنة 2018."),
})
figtools.register_provenance(SERIE_PYRAMIDE, **{
    **figtools.meta(SERIE_PYRAMIDE),
    "sources": ["cnss-annuaire-2013", "cnss-annuaire-2018"],
    "titre_ar": ("الصندوق الوطني للضمان الاجتماعي: أجراء القطاع غير الفلاحي حسب شريحة الأجر "
                 "الشهري المصرّح به بحساب الأجر الأدنى المضمون، 2000-2018"),
    "unite_ar": "أجراء مصرّح بهم؛ % من المجموع المطبوع (محسوبة)",
    "perimetre_ar": ("نظام الأجراء في القطاع غير الفلاحي؛ ثلاث مجموعات محسوبة (أقلّ من مرّة "
                     "واحدة الأجر الأدنى؛ من 1 إلى 1,5؛ أكثر من 1,5)؛ طبعة 2013 للسنوات "
                     "2000-2004 وطبعة 2018 بعدها؛ قيس سنوي، وقيس حسب الثلاثي لسنة 2018"),
    "caveats_ar": ("قيسان لا يُخلطان. السنوي: كلّ الأجراء المصرّح بهم بعنوان السنة، والشريحة "
                   "الدنيا فيه منتفخة بالسنوات غير الكاملة، فلا يقيس أجراء يتقاضون أقلّ من "
                   "الأجر الأدنى (24,0 % سنة 2018). الثلاثي: الأجراء المصرّح بهم في كلّ ثلاثي من "
                   "2018 (9,5 % في الثلاثي الأول). لا يبيّن المصدر الأجر الأدنى المرجعي ولا "
                   "طريقة حساب الأجر الشهري."),
})

_L.update({
    "y_indice": {"fr": f"Indice, base 100 en {ANNEE_BASE_INDICE}",
                 "ar": f"رقم قياسي، أساس 100 سنة {ANNEE_BASE_INDICE}"},
    "y_rapport_smig": {"fr": "Salaire moyen déclaré, en SMIG de 48 heures",
                       "ar": "معدّل الأجر المصرّح به، بعدد مرّات الأجر الأدنى (48 ساعة)"},
    "y_part": {"fr": "% des salariés déclarés", "ar": "% من الأجراء المصرّح بهم"},
    "vue_rapport": {"fr": "Rapport au SMIG", "ar": "النسبة إلى الأجر الأدنى المضمون"},
    "sd_2006": {"fr": "Salaire moyen déclaré, annuaire 2006 (1970-1999 et 2002-2006)",
                "ar": "معدّل الأجر المصرّح به، دليل 2006 (1970-1999 و2002-2006)"},
    "sd_2018": {"fr": "Salaire moyen déclaré, annuaire 2018 (2000-2018)",
                "ar": "معدّل الأجر المصرّح به، دليل 2018 (2000-2018)"},
    "sd_smig": {"fr": "SMIG, régime de 48 heures, moyenne annuelle",
                "ar": "الأجر الأدنى المضمون، نظام 48 ساعة، المعدّل السنوي"},
    "sd_4t": {"fr": "Salariés déclarés les quatre trimestres, 2013",
              "ar": "الأجراء المصرّح بهم في الثلاثيات الأربع، 2013"},
    "rs_1974": {"fr": "1974 : indemnité\nde cherté de vie\ndans le SMIG",
                "ar": "1974: منحة غلاء\nالمعيشة ضمن\nالأجر الأدنى"},
    "rs_1981": {"fr": "1981 : indemnité\ncomplémentaire\ndans le SMIG,\nhors assiette",
                "ar": "1981: المنحة التكميلية\nفي الأجر الأدنى،\nخارج قاعدة\nالاشتراكات"},
    "rs_1988": {"fr": "1988 : indemnité\ndans l'assiette", "ar": "1988: المنحة في\nقاعدة الاشتراكات"},
    "rs_2003": {"fr": "2003 : taxis\net louages", "ar": "2003: سيارات\nالأجرة واللواج"},
    "c_edition": {"fr": "annuaire de la CNSS", "ar": "دليل الصندوق"},
    "c_segment": {"fr": "segment", "ar": "المقطع"},
    "c_sd_annuel": {"fr": "salaire annuel moyen déclaré (D courants)",
                    "ar": "معدّل الأجر السنوي المصرّح به (د جارية)"},
    "c_sd_mensuel": {"fr": "salaire mensuel moyen déclaré (D courants)",
                     "ar": "معدّل الأجر الشهري المصرّح به (د جارية)"},
    "c_sd_reel": {"fr": f"salaire mensuel moyen déclaré (D de {ANNEE_BASE})",
                  "ar": f"معدّل الأجر الشهري المصرّح به (د {ANNEE_BASE})"},
    "c_sd_rapport": {"fr": "salaire moyen déclaré / SMIG 48 h",
                     "ar": "معدّل الأجر المصرّح به / الأجر الأدنى 48 ساعة"},
    "seg_4t": {"fr": "déclarés les quatre trimestres", "ar": "مصرّح بهم في الثلاثيات الأربع"},
    "i_salaire": {"fr": "Salaire moyen du privé non agricole, panel de salariés permanents (INS)",
                  "ar": "معدّل الأجر في القطاع الخاص غير الفلاحي، عيّنة قارّة من الأجراء (المعهد)"},
    "i_prov": {"fr": "2025 : taux provisoire", "ar": "2025: نسبة وقتية"},
    "i_smig": {"fr": "SMIG, régime de 48 heures, moyenne annuelle",
               "ar": "الأجر الأدنى المضمون، نظام 48 ساعة، المعدّل السنوي"},
    "i_prix": {"fr": "Prix à la consommation", "ar": "أسعار الاستهلاك"},
    "c_i_taux": {"fr": "salaire du privé non agricole : taux chaîné de l'année (%)",
                 "ar": "أجر القطاع الخاص غير الفلاحي: النسبة السنوية المتسلسلة (%)"},
    "c_i_prov": {"fr": "taux provisoire", "ar": "نسبة وقتية"},
    "c_i_salaire": {"fr": f"salaire du privé non agricole (indice, {ANNEE_BASE_INDICE} = 100)",
                    "ar": f"أجر القطاع الخاص غير الفلاحي (رقم قياسي، {ANNEE_BASE_INDICE} = 100)"},
    "c_i_smig": {"fr": f"SMIG 48 h, moyenne annuelle (indice, {ANNEE_BASE_INDICE} = 100)",
                 "ar": f"الأجر الأدنى 48 ساعة، المعدّل السنوي (رقم قياسي، {ANNEE_BASE_INDICE} = 100)"},
    "c_i_prix": {"fr": f"prix à la consommation (indice, {ANNEE_BASE_INDICE} = 100)",
                 "ar": f"أسعار الاستهلاك (رقم قياسي، {ANNEE_BASE_INDICE} = 100)"},
    "oui": {"fr": "oui", "ar": "نعم"},
    "p_inf1": {"fr": "Moins de 1 SMIG", "ar": "أقلّ من مرّة واحدة الأجر الأدنى"},
    "p_1_15": {"fr": "De 1 à 1,5 SMIG", "ar": "من 1 إلى 1,5 مرّة الأجر الأدنى"},
    "p_sup15": {"fr": "Plus de 1,5 SMIG", "ar": "أكثر من 1,5 مرّة الأجر الأدنى"},
    "p_t1": {"fr": "Salariés déclarés au\npremier trimestre 2018 :\n{v} % sous 1 SMIG",
             "ar": "الأجراء المصرّح بهم في\nالثلاثي الأول 2018:\n{v} % دون الأجر الأدنى"},
    "c_mesure": {"fr": "mesure", "ar": "القيس"},
    "m_annuelle": {"fr": "annuelle", "ar": "سنوي"},
    "m_trim": {"fr": "trimestre {t} de 2018", "ar": "الثلاثي {t} من 2018"},
    "c_p_total": {"fr": "salariés déclarés", "ar": "الأجراء المصرّح بهم"},
    "c_p_inf1": {"fr": "moins de 1 SMIG (%)", "ar": "أقلّ من 1 (%)"},
    "c_p_1_15": {"fr": "de 1 à 1,5 SMIG (%)", "ar": "من 1 إلى 1,5 (%)"},
    "c_p_sup15": {"fr": "plus de 1,5 SMIG (%)", "ar": "أكثر من 1,5 (%)"},
    # Tableau des enquêtes de l'INS.
    "t_enquete": {"fr": "Enquête de l'INS et champ", "ar": "مسح المعهد الوطني للإحصاء ومجاله"},
    "t_annee": {"fr": "Année", "ar": "السنة"},
    "t_part": {"fr": "Salariés dont le salaire est inférieur au SMIG",
               "ar": "أجراء يقلّ أجرهم عن الأجر الأدنى"},
    "t_moitie": {"fr": "dont inférieur à la moitié du SMIG",
                 "ar": "منهم من يقلّ أجره عن نصف الأجر الأدنى"},
    "t_base": {"fr": "Salaire de base moyen des permanents (dinars)",
               "ar": "معدّل الأجر الأساسي للقارّين (دينار)"},
    "t_base_pct": {"fr": "en % du SMIG", "ar": "بالنسبة المائوية من الأجر الأدنى"},
    "t_smig": {"fr": "SMIG retenu par l'INS (dinars)", "ar": "الأجر الأدنى الذي اعتمده المعهد (دينار)"},
    "t_reponse": {"fr": "Réponses à l'enquête", "ar": "الإجابات عن المسح"},
    "t_micro": {"fr": ("Micro-entreprises : entreprises non agricoles de moins de six salariés, "
                       "sans comptabilité ; salariés permanents"),
                "ar": ("المؤسسات الصغرى: مؤسسات غير فلاحية تشغّل أقلّ من ستة أجراء ولا تمسك "
                       "محاسبة؛ الأجراء القارّون")},
    "t_micro_2016": {"fr": " ; chiffre d'affaires inférieur à un million de dinars",
                     "ar": "؛ رقم معاملات دون مليون دينار"},
    "t_ees": {"fr": ("Emploi et salaires : entreprises publiques et entreprises privées de six "
                     "salariés et plus ; salariés permanents"),
              "ar": ("التشغيل والأجور: المؤسسات العمومية والمؤسسات الخاصة التي تشغّل ستة أجراء "
                     "فأكثر؛ الأجراء القارّون")},
    "t_rep_micro": {"fr": "{n} entreprises sans comptabilité", "ar": "{n} مؤسسة لا تمسك محاسبة"},
    "t_rep_ees": {"fr": "taux de réponse de {n}", "ar": "نسبة إجابة {n}"},
})


def _fr(v: float, d: int = 1) -> str:
    """Nombre à la française : virgule décimale, espace insécable des milliers."""
    return f"{v:,.{d}f}".replace(",", " ").replace(".", ",")


def _ft_lignes(texte: str) -> str:
    return "\n".join(figtools.fig_text(x) for x in texte.split("\n"))


def _salaire_declare():
    """Une ligne par année et par édition : niveaux courants, constants, et rapport au SMIG."""
    d, smig, ipc = figtools.series(SERIE_SALAIRE), _serie(), _ipc()
    lignes = []
    for r in d.itertuples():
        annee = int(r.annee)
        s = _moyenne_annuelle(smig, "smig_48h_mensuel", annee)
        # Le SMIG du chapitre et celui de la série de la CNSS sont une même grandeur.
        assert abs(s - r.smig_48h_mensuel_moyen_annuel_D) < 0.001, annee
        coef = ipc[ANNEE_BASE] / ipc[annee]
        lignes.append({
            "annee": annee, "edition": 2006 if "2006" in r.edition else 2018,
            "segment": r.segment.split(" (")[0],
            "annuel": float(r.salaire_annuel_moyen_declare_D),
            "mensuel": float(r.salaire_mensuel_moyen_declare_D), "smig": s,
            "mensuel_reel": float(r.salaire_mensuel_moyen_declare_D) * coef,
            "smig_reel": s * coef, "rapport": float(r.rapport_salaire_moyen_smig)})
    return lignes


def _quatre_trimestres():
    """Le salaire moyen des salariés déclarés les quatre trimestres de 2013, mêmes grandeurs."""
    q = QUATRE_TRIMESTRES_2013
    annee, ipc = q["annee"], _ipc()
    s = _moyenne_annuelle(_serie(), "smig_48h_mensuel", annee)
    annuel = q["masse"] / q["salaries"]
    coef = ipc[ANNEE_BASE] / ipc[annee]
    return {"annee": annee, "edition": 2013, "segment": _lab("seg_4t"), "annuel": annuel,
            "mensuel": annuel / 12, "smig": s, "mensuel_reel": annuel / 12 * coef,
            "smig_reel": s * coef, "rapport": annuel / (12 * s)}


def _fig_salaire_declare(rapport: bool):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r, q = _salaire_declare(), _quatre_trimestres()
    cle = "rapport" if rapport else "mensuel_reel"
    fig, ax = plt.subplots(figsize=(10, 5.8))
    if not rapport:
        smig = {l["annee"]: l["smig_reel"] for l in r}
        ax.plot(sorted(smig), [smig[a] for a in sorted(smig)], color=GRIS, lw=1.6,
                label=ft(_lab("sd_smig")))
    # Un appel par segment : aucun trait ne relie deux segments.
    deja = set()
    for segment in dict.fromkeys((l["edition"], l["segment"]) for l in r):
        edition = segment[0]
        pts = [(l["annee"], l[cle]) for l in r if (l["edition"], l["segment"]) == segment]
        style = (dict(color=BLEU, marker="o", ms=3.2) if edition == 2006
                 else dict(color=ORANGE, marker="s", ms=3.2))
        ax.plot([a for a, _ in pts], [v for _, v in pts], lw=1.8,
                label=None if edition in deja else ft(_lab(f"sd_{edition}")), **style)
        deja.add(edition)
    ax.plot([q["annee"]], [q[cle]], ls="none", marker="D", ms=6, mfc="white", mec=VIOLET,
            mew=1.6, label=ft(_lab("sd_4t")))
    for annee, cle_r, decale in ((1974, "rs_1974", 0), (1981, "rs_1981", 0), (1988, "rs_1988", 0),
                                 (2003, "rs_2003", 0)):
        figtools.marque_rupture(ax, annee, "\n" * decale + _ft_lignes(_lab(cle_r)))
    if rapport:
        ax.axhline(1, color=GRIS, lw=0.8)
        ax.set_ylim(0, 3.6)
        ax.set_ylabel(ft(_lab("y_rapport_smig")))
    else:
        ax.set_ylim(0, None)
        ax.set_ylabel(ft(_lab("y_reel")))
    ax.set_xlim(1968.5, 2019.5)
    ax.set_xticks(range(1970, 2019, 4))
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False, ncol=2)
    fig.tight_layout()
    return fig


def vues_salaire_declare():
    return [(_lab("vue_constants"), _fig_salaire_declare(False)),
            (_lab("vue_rapport"), _fig_salaire_declare(True))]


def table_salaire_declare():
    import pandas as pd
    r = _salaire_declare() + [_quatre_trimestres()]
    return pd.DataFrame({
        _lab("c_annee"): [l["annee"] for l in r],
        _lab("c_edition"): [l["edition"] for l in r],
        _lab("c_segment"): [l["segment"] for l in r],
        _lab("c_sd_annuel"): [round(l["annuel"]) for l in r],
        _lab("c_sd_mensuel"): [round(l["mensuel"], 3) for l in r],
        _lab("c_48_moy"): [round(l["smig"], 3) for l in r],
        _lab("c_sd_reel"): [round(l["mensuel_reel"], 1) for l in r],
        _lab("c_48_reel"): [round(l["smig_reel"], 1) for l in r],
        _lab("c_sd_rapport"): [round(l["rapport"], 2) for l in r],
    })


def _indices():
    """Indices base 100 en 2001 : salaire du privé (taux chaîné de l'INS), SMIG, prix."""
    taux = {int(l.annee): (float(l.taux_chaine), str(l.provisoire) == "oui")
            for l in figtools.series(SERIE_INS_TAUX).itertuples()}
    smig, ipc = _serie(), _ipc()
    lignes, niveau = [], 100.0
    s0 = _moyenne_annuelle(smig, "smig_48h_mensuel", ANNEE_BASE_INDICE)
    for annee in range(ANNEE_BASE_INDICE, max(max(taux), FIN_INDICES) + 1):
        if annee > ANNEE_BASE_INDICE and annee in taux:
            niveau *= 1 + taux[annee][0] / 100
        s = _moyenne_annuelle(smig, "smig_48h_mensuel", annee) if annee <= FIN_INDICES else None
        lignes.append({
            "annee": annee,
            "taux": taux[annee][0] if annee in taux else None,
            "provisoire": annee in taux and taux[annee][1],
            "salaire": niveau if annee in taux else None,
            "smig": None if s is None else 100 * s / s0,
            "prix": 100 * ipc[annee] / ipc[ANNEE_BASE_INDICE] if annee in ipc else None})
    return lignes


def fig_indices():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _indices()
    fig, ax = plt.subplots(figsize=(10, 5.6))
    for cle, lib, style in (("salaire", "i_salaire", dict(color=BLEU, lw=2, marker="o", ms=3)),
                            ("smig", "i_smig", dict(color=ORANGE, lw=1.8, marker="s", ms=3)),
                            ("prix", "i_prix", dict(color=GRIS, lw=1.6, ls="--"))):
        pts = [(l["annee"], l[cle]) for l in r if l[cle] is not None]
        ax.plot([a for a, _ in pts], [v for _, v in pts], label=ft(_lab(lib)), **style)
        ax.annotate(_fr(pts[-1][1], 0), xy=pts[-1], xytext=(6, 0), textcoords="offset points",
                    va="center", fontsize=8, color=style["color"])
    prov = [(l["annee"], l["salaire"]) for l in r if l["provisoire"]]
    if prov:
        ax.plot([a for a, _ in prov], [v for _, v in prov], ls="none", marker="o", ms=7,
                mfc="white", mec=BLEU, mew=1.6, label=ft(_lab("i_prov")))
    ax.axhline(100, color=GRIS, lw=0.8)
    ax.set_xlim(ANNEE_BASE_INDICE - 0.5, r[-1]["annee"] + 1.6)
    ax.set_xticks(range(ANNEE_BASE_INDICE, r[-1]["annee"] + 1, 3))
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_indice")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    fig.tight_layout()
    return fig


def vues_indices():
    return fig_indices()


def table_indices():
    import pandas as pd
    r = _indices()

    def arrondi(v):
        return None if v is None else round(v, 1)
    return pd.DataFrame({
        _lab("c_annee"): [l["annee"] for l in r],
        _lab("c_i_taux"): [l["taux"] for l in r],
        _lab("c_i_prov"): [_lab("oui") if l["provisoire"] else "" for l in r],
        _lab("c_i_salaire"): [arrondi(l["salaire"]) for l in r],
        _lab("c_i_smig"): [arrondi(l["smig"]) for l in r],
        _lab("c_i_prix"): [arrondi(l["prix"]) for l in r],
    })


_TRANCHES = (("<1", "inf1"), ("1-1.5", "1_15"), (">1.5", "sup15"))


def _pyramide():
    """Parts des trois regroupements : mesure annuelle 2000-2018, puis trimestres de 2018."""
    d = figtools.series(SERIE_PYRAMIDE)
    d = d[d["niveau"] == "regroupement (calculé)"]
    lignes = []
    annuel = d[(d["mesure"] == "annuelle") & (d["serie_2000_2018"] == "oui")]
    trim = d[d["mesure"] == "trimestre civil"]
    for bloc, cles in ((annuel, ["annee"]), (trim, ["annee", "trimestre"])):
        for cle, g in bloc.groupby(cles, sort=True):
            parts = {t: float(g.loc[g["tranche_salaire_mensuel_en_smig"] == t, "part_pct"].iloc[0])
                     for t, _ in _TRANCHES}
            assert abs(sum(parts.values()) - 100) < 0.01, cle
            lignes.append({"annee": int(cle[0]),
                           "trimestre": int(cle[1]) if len(cle) > 1 else None,
                           "total": int(g["total_imprime"].iloc[0]),
                           **{nom: parts[t] for t, nom in _TRANCHES}})
    return lignes


def fig_bas_distribution():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _pyramide()
    an = [l for l in r if l["trimestre"] is None]
    t1 = next(l for l in r if l["trimestre"] == 1)
    fig, ax = plt.subplots(figsize=(10, 5.6))
    x = [l["annee"] for l in an]
    bas = [0.0] * len(an)
    for nom, lib, couleur, encre in (("inf1", "p_inf1", ORANGE, "white"),
                                     ("1_15", "p_1_15", JAUNE, "black"),
                                     ("sup15", "p_sup15", BLEU_CLAIR, "black")):
        y = [l[nom] for l in an]
        ax.bar(x, y, bottom=bas, width=0.8, color=couleur, label=ft(_lab(lib)))
        for xi, yi, bi in zip(x, y, bas):
            # En haut de la bande : le bas de la première reçoit le repère du trimestre.
            ax.text(xi, bi + yi - 3, _fr(yi, 0), ha="center", va="center", fontsize=7,
                    color=encre)
        bas = [b + v for b, v in zip(bas, y)]
    # L'autre mesure de la même source, une seule année : marquée, non empilée.
    ax.plot([t1["annee"]], [t1["inf1"]], ls="none", marker="D", ms=7, mfc="white", mec="black",
            mew=1.4, zorder=5)
    ax.annotate(_ft_lignes(_lab("p_t1").format(v=_fr(t1["inf1"]))),
                xy=(t1["annee"], t1["inf1"]), xytext=(2019.2, t1["inf1"]), va="center",
                ha="left", fontsize=8,
                arrowprops={"arrowstyle": "-", "color": "black", "lw": 0.8})
    ax.set_xlim(1999.3, 2023.2)
    ax.set_ylim(0, 100)
    ax.set_xticks(x)
    ax.tick_params(axis="x", labelsize=8)
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_part")))
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False, ncol=3)
    fig.tight_layout()
    return fig


def vues_bas_distribution():
    return fig_bas_distribution()


def table_bas_distribution():
    import pandas as pd
    r = _pyramide()
    return pd.DataFrame({
        _lab("c_annee"): [l["annee"] for l in r],
        _lab("c_mesure"): [_lab("m_annuelle") if l["trimestre"] is None
                           else _lab("m_trim").format(t=l["trimestre"]) for l in r],
        _lab("c_p_total"): [l["total"] for l in r],
        _lab("c_p_inf1"): [round(l["inf1"], 1) for l in r],
        _lab("c_p_1_15"): [round(l["1_15"], 1) for l in r],
        _lab("c_p_sup15"): [round(l["sup15"], 1) for l in r],
    })


# Entreprises répondantes sans comptabilité, sur lesquelles portent les résultats de l'enquête
# auprès des micro-entreprises (rapport 2007, p. 8 ; 2012, p. 10 ; 2016, p. 9 du fichier PDF ;
# citations dans la colonne `champ` de la série).
_REPONDANTES_MICRO = {2007: 7144, 2012: 5572, 2016: 7179}
_REPONSE_EES = {2012: "38,6 %", 2014: "46,6 %", 2022: "58 %"}


def tableau_enquetes() -> str:
    """Tableau Markdown des deux enquêtes de l'INS, une ligne par enquête et par année.

    Valeurs lues dans les séries ; champ et taux de réponse contrôlés sur les citations que
    les séries portent (colonnes `champ` et `taux_de_reponse`).
    """
    m, e = figtools.series(SERIE_MICRO), figtools.series(SERIE_EES)
    m = m[(m["branche"] == "Ensemble") & (m["sexe"] == "ensemble") & (m["grandeur"] == "part")]
    lignes = []

    def pct(v):
        return f"{_fr(float(v))} %"

    for annee in (2007, 2012, 2016):
        propre = m[m["source_id"] == f"ins-micro-entreprises-{annee}"]
        part = propre[(propre["annee"] == annee) & (propre["tranche"] == "<1")]
        # La moitié du SMIG : 2007 n'est imprimée que par le rapport 2012 (tableau 8).
        moitie = m[(m["annee"] == annee) & (m["tranche"] == "<0.5")]
        assert part["valeur"].nunique() == 1 and moitie["valeur"].nunique() == 1, annee
        assert str(_REPONDANTES_MICRO[annee]) in propre["champ"].iloc[0], annee
        page = int(part["page_pdf"].min())
        du_rapport = moitie[moitie["source_id"] == f"ins-micro-entreprises-{annee}"]
        if du_rapport.empty:
            autre = moitie.iloc[0]
            cite = (f"[@ins-micro-entreprises-{annee}, p. {page}; "
                    f"@{autre['source_id']}, p. {int(autre['page_pdf'])}]")
        else:
            cite = (f"[@ins-micro-entreprises-{annee}, p. {page}, "
                    f"{int(du_rapport['page_pdf'].min())}]")
        champ = _lab("t_micro") + (_lab("t_micro_2016") if annee == 2016 else "")
        lignes.append((f"{champ} {cite}", annee, pct(part["valeur"].iloc[0]),
                       pct(moitie["valeur"].iloc[0]), "—", "—",
                       int(part["smig_retenu_par_la_source_D"].iloc[0]),
                       _lab("t_rep_micro").format(n=_fr(_REPONDANTES_MICRO[annee], 0))))
    e = e[(e["section"] == "Total") & (e["categorie"] == "Total")]
    for annee in (2012, 2014, 2022):
        g = e[e["annee"] == annee]
        niveau = g[~g["grandeur"].str.contains("pourcentage")]
        rapport = g[g["grandeur"].str.contains("pourcentage")]
        assert len(niveau) == 1 and len(rapport) == 1, annee
        assert _REPONSE_EES[annee].replace(" ", "") in g["taux_de_reponse"].iloc[0], annee
        cite = f"[@ins-ees-{annee}, p. {int(niveau['page_pdf'].iloc[0])}]"
        lignes.append((f"{_lab('t_ees')} {cite}", annee, "—", "—",
                       _fr(float(niveau["valeur"].iloc[0]), 0),
                       f"{_fr(float(rapport['valeur'].iloc[0]), 0)} %",
                       int(niveau["smig_retenu_par_la_source_D"].iloc[0]),
                       _lab("t_rep_ees").format(n=_REPONSE_EES[annee])))
    entetes = [_lab(c) for c in ("t_enquete", "t_annee", "t_part", "t_moitie", "t_base",
                                 "t_base_pct", "t_smig", "t_reponse")]
    sortie = ["| " + " | ".join(entetes) + " |", "|:---|---|---:|---:|---:|---:|---:|:---|"]
    sortie += ["| " + " | ".join(str(c) for c in l) + " |" for l in lignes]
    return "\n".join(sortie)


# ------------------------------------------------ conventions collectives
#
# Quatre séries de l'entrepôt, de trois familles qui ne se mêlent pas : deux relevés du
# Journal officiel (agréments par année, inventaire par branche), les grilles de deux
# conventions (salaire d'entrée du textile et du bâtiment-travaux publics) et une source
# extérieure (OIT, taux de couverture). La provenance du catalogue est réécrite ici pour le
# lecteur : mêmes faits, sans le vocabulaire de fabrication de l'entrepôt.

SERIE_CC_AGREMENTS = "jort-conventions-collectives-agrements-par-annee"
SERIE_CC_BRANCHES = "jort-conventions-collectives-branches"
SERIE_CC_GRILLES = "conventions-collectives-salaire-entree"
SERIE_CC_COUVERTURE = "oit-ilostat-couverture-negociation-collective"

# Années où le relevé des intitulés sous-compte les avenants : de 1996 à 2012, l'édition
# française ne publie qu'un avis collectif par fascicule ; en 2022, 4 intitulés relevés pour
# 35 arrêtés de l'édition française (fiche sources/jort-conventions-collectives.md).
_CC_SOUS_COMPTE = set(range(1996, 2013)) | {2022}
# Avenants rattachés à deux branches par les mots de leur intitulé (même fiche) : trois de la
# mécanique générale et des stations de vente de carburant comptés aussi au pétrole, un du
# gardiennage compté aussi aux assurances. La date du dernier avenant de ces deux branches
# est alors celle d'un texte de l'autre : la case reste vide.
_CC_DOUBLE_COMPTE = {"Pétrole (commerce et distribution)": 3, "Assurances": 1}
# Segments de la série des grilles (colonne `segment`), avec les années de leur première et
# de leur dernière date : aucun trait ne relie deux segments. Depuis que les avenants de
# 1996 à 2010 sont établis, chaque branche a un segment continu.
_CC_SEGMENTS = {
    "textile": [(1974, 1974), (1990, 1992), (1994, 2026)],
    "bâtiment et travaux publics": [(1975, 1975), (1990, 1990), (1996, 2024)],
}
# Les trois origines de la lecture d'une grille (colonne `origine_lecture`), dites pour le
# lecteur. La troisième ne vaut que pour l'avenant n° 16 du bâtiment.
_CC_ORIGINES = {
    "édition française du Journal officiel": ("fr", "édition française"),
    "édition arabe du Journal officiel (fascicule du corpus local)": ("ar", "édition arabe"),
    "reproduction de l'édition arabe du Journal officiel sur un site tiers (paie-tunisie.com)":
        ("copie", "édition arabe, pages reproduites par un site tiers (paie-tunisie.com)"),
}
# Le document réellement lu pour l'avenant n° 16 du bâtiment : cité à côté de l'arrêté.
_CC_CLE_COPIE = "paie-tunisie-2022-reproduction-jort-132"
# Bornes que le chapitre écrit, contrôlées sur la série : rapport du salaire d'entrée au SMIG
# aux dates d'effet (branche, première année, dernière année) -> (minimum, maximum), et
# extrêmes du rapport suivi jour après jour sur le segment continu (minimum, maximum).
_CC_BORNES = {
    ("textile", 1994, 2010): (1.06, 1.17), ("textile", 2011, 2026): (1.11, 1.30),
    ("bâtiment et travaux publics", 1996, 2010): (1.12, 1.20),
    ("bâtiment et travaux publics", 2011, 2024): (1.15, 1.32),
}
_CC_EXTREMES = {
    "textile": ((dt.date(1997, 11, 7), 1.05), (dt.date(2022, 5, 1), 1.30)),
    "bâtiment et travaux publics": ((dt.date(2015, 5, 1), 1.10), (dt.date(2024, 1, 1), 1.32)),
}
_CC_BRANCHE_INVENTAIRE = {"textile": "Textile",
                          "bâtiment et travaux publics": "Bâtiment et travaux publics"}
# Clé de référence du texte qui porte chaque grille : (branche, convention ou avenant).
_CC_CLES = {
    ("textile", "convention"): "convention-textile-1974",
    ("textile", "avenant n° 3"): "avenants-1990-textile-btp",
    ("textile", "avenant n° 5"): "avenant5-textile-1994",
    ("textile", "avenant n° 6"): "avenant6-textile-1996",
    ("textile", "avenant n° 7"): "avenant7-textile-1999",
    ("textile", "avenant n° 8"): "avenant8-textile-2002",
    ("textile", "avenant n° 9"): "avenant9-textile-2006",
    ("textile", "avenant n° 10"): "avenant10-textile-2009",
    ("textile", "avenant n° 11"): "avenant11-textile-2011",
    ("textile", "avenant n° 12"): "avenant12-textile-2013",
    ("textile", "avenant n° 13"): "avenants-2014-textile-btp",
    ("textile", "avenant n° 14"): "avenant14-textile-2016",
    ("textile", "avenant n° 15"): "avenant15-textile-2017",
    ("textile", "avenant n° 16"): "avenant16-textile-2019",
    ("textile", "avenant n° 17"): "avenant17-textile-2022",
    ("textile", "avenant n° 18"): "avenant18-textile-2024",
    ("bâtiment et travaux publics", "convention"): "convention-btp-1975",
    ("bâtiment et travaux publics", "avenant n° 3"): "avenants-1990-textile-btp",
    ("bâtiment et travaux publics", "avenant n° 5"): "avenant5-btp-1996",
    ("bâtiment et travaux publics", "avenant n° 6"): "avenant6-btp-1999",
    ("bâtiment et travaux publics", "avenant n° 7"): "avenant7-btp-2002",
    ("bâtiment et travaux publics", "avenant n° 8"): "avenant8-btp-2006",
    ("bâtiment et travaux publics", "avenant n° 9"): "avenant9-btp-2009",
    ("bâtiment et travaux publics", "avenant n° 16"): "avenant16-btp-2022",
    ("bâtiment et travaux publics", "avenant n° 10"): "avenant10-btp-2011",
    ("bâtiment et travaux publics", "avenant n° 11"): "avenant11-btp-2013",
    ("bâtiment et travaux publics", "avenant n° 12"): "avenants-2014-textile-btp",
    ("bâtiment et travaux publics", "avenant n° 13"): "avenant13-btp-2016",
    ("bâtiment et travaux publics", "avenant n° 14"): "avenant14-btp-2017",
    ("bâtiment et travaux publics", "avenant n° 15"): "avenant15-btp-2018",
}
# Dates repères du tableau court : (branche, date d'effet ; None pour la convention d'origine).
_CC_REPERES = [
    ("textile", None), ("textile", "1994-05-01"), ("textile", "2004-05-01"),
    ("textile", "2014-05-01"), ("textile", "2024-01-01"), ("textile", "2026-01-01"),
    ("bâtiment et travaux publics", None), ("bâtiment et travaux publics", "1996-05-01"),
    ("bâtiment et travaux publics", "2004-05-01"), ("bâtiment et travaux publics", "2014-05-01"),
    ("bâtiment et travaux publics", "2024-01-01"),
]
_MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre",
         "octobre", "novembre", "décembre"]
_MOIS_ABREGES = {"janv.": "janvier", "févr.": "février", "avr.": "avril", "juill.": "juillet",
                 "sept.": "septembre", "oct.": "octobre", "nov.": "novembre", "déc.": "décembre"}

figtools.register_provenance(SERIE_CC_AGREMENTS, **{
    **figtools.meta(SERIE_CC_AGREMENTS),
    "titre": ("Conventions collectives sectorielles : conventions et avenants agréés, d'après "
              "les intitulés publiés au Journal officiel, par année, 1969-2025"),
    "titre_ar": ("الاتفاقيات المشتركة القطاعية: الاتفاقيات والملاحق التعديلية المصادق عليها، "
                 "حسب العناوين المنشورة بالرائد الرسمي، سنة بسنة، 1969-2025"),
    "unite": "nombre de textes agréés",
    "unite_ar": "عدد النصوص المصادق عليها",
    "perimetre": ("intitulés des arrêtés publiés au Journal officiel qui agréent ou approuvent "
                  "une convention collective ou un avenant, classés d'après leurs mots ; une "
                  "ligne par année du fascicule ; 61 agréments de conventions sectorielles, "
                  "512 agréments d'avenants ; à part, les arrêtés d'avenant comptés dans le "
                  "texte de l'édition française, 1994-2025"),
    "perimetre_ar": ("عناوين القرارات المنشورة بالرائد الرسمي المتعلقة بالمصادقة على اتفاقية "
                     "مشتركة أو على ملحق تعديلي؛ سطر لكلّ سنة؛ 61 مصادقة على اتفاقيات قطاعية "
                     "و512 مصادقة على ملاحق تعديلية"),
    "caveats": ("Borne basse : un décompte de textes, non de salariés. Un intitulé qui s'écarte "
                "de la formule usuelle n'est pas compté. De 1996 à 2012, l'édition française ne "
                "publie qu'un avis collectif par fascicule — « agréments d'avenants à quarante "
                "conventions collectives nationales » le 24 juillet 1996 —, et les avenants ne "
                "sont pas comptés un par un. En 2022, 4 intitulés pour 35 arrêtés dans l'édition "
                "française. Les deux décomptes des avenants ne s'additionnent pas. Une année à "
                "zéro n'établit pas qu'aucun avenant n'a paru."),
    "caveats_ar": ("حدّ أدنى: تعداد لنصوص لا لأجراء. من 1996 إلى 2012 لا تنشر الطبعة الفرنسية إلا "
                   "إعلامًا جماعيًا في كلّ عدد، فلا تُحصى الملاحق واحدًا واحدًا. وسنة 2022: 4 عناوين "
                   "مقابل 35 قرارًا في الطبعة الفرنسية. ولا يُجمع التعدادان."),
})
figtools.register_provenance(SERIE_CC_BRANCHES, **{
    **figtools.meta(SERIE_CC_BRANCHES),
    "titre": ("Conventions collectives sectorielles : inventaire par branche — agrément, "
              "Journal officiel, avenants"),
    "titre_ar": ("الاتفاقيات المشتركة القطاعية: جرد حسب القطاع — المصادقة، الرائد الرسمي، "
                 "الملاحق التعديلية"),
    "unite": "une ligne par branche",
    "unite_ar": "سطر لكلّ قطاع",
    "perimetre": ("57 branches : 56 dont la convention a au moins un agrément publié, une "
                  "connue par ses seuls avenants ; 61 agréments de conventions sectorielles"),
    "perimetre_ar": "57 قطاعًا: 56 لها مصادقة منشورة واحدة على الأقلّ، وواحد لا يُعرف إلا بملاحقه",
    "caveats": ("Les avenants sont rattachés à une branche d'après les mots de leur intitulé : "
                "leur nombre par branche est indicatif, et quatre sont comptés dans deux "
                "branches. Le numéro d'avenant le plus élevé est celui des intitulés. Borne "
                "basse."),
    "caveats_ar": ("تُنسب الملاحق إلى القطاع حسب كلمات عناوينها: عددها لكلّ قطاع تقريبي، وأربعة "
                   "منها محسوبة في قطاعين. حدّ أدنى."),
})
figtools.register_provenance(SERIE_CC_GRILLES, **{
    **figtools.meta(SERIE_CC_GRILLES),
    "titre": ("Salaire horaire d'entrée des conventions du textile (1974-2026) et du "
              "bâtiment-travaux publics (1975-2024), par date d'effet des grilles, et rapport "
              "au SMIG horaire du régime de 48 heures"),
    "titre_ar": ("أجر الساعة عند الدخول في اتفاقيتي النسيج (1974-2026) والبناء والأشغال العامة "
                 "(1975-2024)، حسب تاريخ سريان جداول الأجور، ونسبته إلى الأجر الأدنى المضمون "
                 "بالساعة لنظام 48 ساعة"),
    # Sous la figure, deux clés et un renvoi : chaque grille a sa référence au tableau des
    # grilles, et la liste entière reste à l'onglet « Sources » et dans le figdata.
    "source_ligne": ("conventions du textile et du bâtiment et des travaux publics "
                     "[@convention-textile-1974; @convention-btp-1975] et leurs avenants de "
                     "1990 à 2024, chacun cité avec sa grille (@tbl-mt-cc-grilles ; liste à "
                     "l'onglet « Sources »)"),
    "source_ligne_ar": ("اتفاقيتا النسيج والبناء والأشغال العامة "
                        "[@convention-textile-1974; @convention-btp-1975] وملاحقهما التعديلية "
                        "من 1990 إلى 2024 (القائمة في تبويب « المصادر »)"),
    "unite": "dinars courants par heure ; rapport sans unité",
    "unite_ar": "دينار جارٍ في الساعة؛ نسبة",
    "perimetre": ("grilles de salaires annexées aux deux conventions et à leurs avenants, "
                  "publiées au Journal officiel ; salaire horaire de base du bas de la grille "
                  "— textile : agents payés à l'heure, catégorie I, échelon 0 ; bâtiment et "
                  "travaux publics : personnel occasionnel, manœuvre ordinaire — et du haut "
                  "de la même grille ; une ligne par date d'effet (textile : 34 ; bâtiment : "
                  "28) ; un segment continu par branche (textile, 1994-2026, avenants n° 5 à "
                  "18 ; bâtiment, 1996-2024, avenants n° 5 à 16) ; rapport = salaire d'entrée "
                  "÷ SMIG horaire du régime de 48 heures en vigueur à cette date"),
    "perimetre_ar": ("جداول الأجور الملحقة بالاتفاقيتين وبملاحقهما التعديلية، المنشورة بالرائد "
                     "الرسمي؛ الأجر الأساسي بالساعة في أسفل الجدول وفي أعلاه؛ سطر لكلّ تاريخ "
                     "سريان؛ مقطع متّصل لكلّ قطاع (النسيج 1994-2026؛ البناء 1996-2024)؛ النسبة = "
                     "أجر الدخول ÷ الأجر الأدنى المضمون بالساعة (48 ساعة)"),
    "caveats": ("Trois origines : l'édition française du Journal officiel (conventions "
                "d'origine, avenants de 1990, de 1994 pour le textile et de 1996 pour le "
                "bâtiment), son édition arabe ensuite, et, pour l'avenant n° 16 du bâtiment "
                "(grilles du 1er décembre 2021, du 1er janvier 2023 et du 1er janvier 2024), "
                "une reproduction par un site tiers des pages 3709 à 3714 de l'édition arabe "
                "du n° 132 du 2 décembre 2022. Aucun raccord ni interpolation : une ligne par "
                "date d'effet, la grille valant jusqu'à la suivante du même segment. Les "
                "grilles de 1990 à 1992 excluent l'indemnité complémentaire provisoire et "
                "n'ont pas de rapport au SMIG ; les grilles antérieures à 1990, celles de 1993 "
                "et celles du bâtiment de 1991 à 1995 ne sont pas établies. La date d'effet "
                "des conventions de 1974 et de 1975 n'est pas établie : leur rapport retient "
                "le SMIG de 0,130 dinar. Salaires de base, hors indemnités conventionnelles. "
                "Deux branches seulement. Montants ou dates d'effet à confirmer : textile, "
                "2011 et 2015 à 2020 ; le haut de la grille manque à quelques dates."),
    "caveats_ar": ("ثلاثة مصادر للقراءة: الطبعة الفرنسية من الرائد الرسمي، ثم طبعته العربية، "
                   "ونسخة لصفحات من الطبعة العربية على موقع آخر بالنسبة إلى الملحق عدد 16 "
                   "لاتفاقية البناء. دون وصل ولا استكمال. جداول 1990-1992 لا تشمل المنحة "
                   "التكميلية المؤقتة ولا نسبة لها. أجور أساسية دون المنح. قطاعان فقط."),
})
figtools.register_provenance(SERIE_CC_COUVERTURE, **{
    **figtools.meta(SERIE_CC_COUVERTURE),
    "titre": ("Organisation internationale du travail (ILOSTAT) : taux de couverture de la "
              "négociation collective, Tunisie, 2010-2019"),
    "titre_ar": "منظمة العمل الدولية (ILOSTAT): نسبة تغطية المفاوضة الجماعية، تونس، 2010-2019",
    "unite": "% du nombre de salariés",
    "unite_ar": "% من عدد الأجراء",
    "perimetre": ("source extérieure : indicateur « Collective bargaining coverage rate (%) » "
                  "(ILR_CBCT_NOC_RT) de la base ILOSTAT, Tunisie, annuel ; neuf années, "
                  "2010-2014 et 2016-2019 ; note de l'OIT : « Reference group coverage: "
                  "Employees »"),
    "perimetre_ar": ("مصدر خارجي: مؤشّر « Collective bargaining coverage rate (%) » من قاعدة "
                     "ILOSTAT، تونس، سنوي؛ تسع سنوات، 2010-2014 و2016-2019"),
    "caveats": ("Source extérieure, d'une autre famille que les décomptes du Journal officiel "
                "et que les grilles. Source déclarée par l'OIT : « ADM - Other Administrative "
                "records and related sources » ; ni le producteur national ni la méthode ne "
                "sont précisés ; ni le numérateur ni le dénominateur ne sont publiés. 2015 "
                "manque ; la série s'arrête en 2019. Groupe de référence : les salariés ; la "
                "source ne précise pas si le secteur public y est compris."),
    "caveats_ar": ("مصدر خارجي. المصدر المصرّح به: سجلات إدارية؛ لا يُذكر المنتج الوطني ولا "
                   "الطريقة. سنة 2015 غير متوفّرة؛ تتوقّف السلسلة سنة 2019. المجموعة المرجعية: "
                   "الأجراء؛ ولا يبيّن المصدر هل تشمل القطاع العمومي."),
})

_L.update({
    "cc_y_textes": {"fr": "Textes agréés dans l'année", "ar": "النصوص المصادق عليها في السنة"},
    "cc_conv": {"fr": "Conventions sectorielles agréées",
                "ar": "الاتفاقيات القطاعية المصادق عليها"},
    "cc_aven": {"fr": "Avenants agréés", "ar": "الملاحق التعديلية المصادق عليها"},
    "cc_aven_sous": {"fr": "Avenants agréés, années sous-comptées (1996-2012 et 2022)",
                     "ar": "الملاحق المصادق عليها، سنوات ناقصة التعداد (1996-2012 و2022)"},
    "cc_c_conv": {"fr": "conventions sectorielles agréées",
                  "ar": "الاتفاقيات القطاعية المصادق عليها"},
    "cc_c_aven": {"fr": "avenants agréés (intitulés publiés au Journal officiel)",
                  "ar": "الملاحق المصادق عليها (العناوين المنشورة بالرائد الرسمي)"},
    "cc_c_sous": {"fr": "année sous-comptée pour les avenants",
                  "ar": "سنة ناقصة التعداد للملاحق"},
    "cc_c_fr": {"fr": "autre décompte : arrêtés d'avenant de l'édition française (1994-2025)",
                "ar": "تعداد آخر: قرارات الملاحق في الطبعة الفرنسية (1994-2025)"},
    "cc_y_horaire": {"fr": "Dinars courants par heure (échelle logarithmique)",
                     "ar": "دينار جارٍ في الساعة (سلّم لوغاريتمي)"},
    "cc_y_rapport": {"fr": "Salaire horaire d'entrée, en SMIG horaire de 48 heures",
                     "ar": "أجر الساعة عند الدخول، بعدد مرّات الأجر الأدنى بالساعة (48 ساعة)"},
    "cc_textile": {"fr": "Textile : catégorie I, échelon 0",
                   "ar": "النسيج: الصنف الأول، الدرجة 0"},
    "cc_btp": {"fr": "Bâtiment et travaux publics : manœuvre ordinaire",
               "ar": "البناء والأشغال العامة: عامل عادي"},
    "cc_smig": {"fr": "SMIG horaire, régime de 48 heures",
                "ar": "الأجر الأدنى المضمون بالساعة، نظام 48 ساعة"},
    "cc_hors_icp": {"fr": "Grilles de 1990 à 1992, hors indemnité complémentaire provisoire",
                    "ar": "جداول 1990-1992، دون المنحة التكميلية المؤقتة"},
    "cc_a_confirmer": {"fr": "Montant ou date d'effet à confirmer",
                       "ar": "مبلغ أو تاريخ سريان في انتظار التأكيد"},
    "cc_r_1994": {"fr": "1er mai 1994 :\nindemnité complémentaire\nprovisoire dans les grilles",
                  "ar": "غرّة ماي 1994:\nالمنحة التكميلية المؤقتة\nضمن جداول الأجور"},
    "cc_copie": {"fr": "Bâtiment, 2021 à 2024 : grilles lues sur une reproduction du Journal officiel",
                 "ar": "البناء، 2021-2024: جداول مقروءة في نسخة من الرائد الرسمي"},
    "cc_c_origine": {"fr": "édition du Journal officiel", "ar": "طبعة الرائد الرسمي"},
    "cc_c_branche": {"fr": "branche", "ar": "القطاع"},
    "cc_c_effet": {"fr": "date d'effet de la grille", "ar": "تاريخ سريان الجدول"},
    "cc_c_texte": {"fr": "convention ou avenant", "ar": "الاتفاقية أو الملحق"},
    "cc_c_bas": {"fr": "salaire horaire d'entrée (D)", "ar": "أجر الساعة عند الدخول (د)"},
    "cc_c_haut": {"fr": "haut de la grille (D par heure)", "ar": "أعلى الجدول (د في الساعة)"},
    "cc_c_smig": {"fr": "SMIG horaire 48 h (D)", "ar": "الأجر الأدنى بالساعة 48 ساعة (د)"},
    "cc_c_rapport": {"fr": "salaire d'entrée / SMIG", "ar": "أجر الدخول / الأجر الأدنى"},
    "cc_c_reserve": {"fr": "réserve", "ar": "تحفّظ"},
    "cc_origine": {"fr": "convention de {a}", "ar": "اتفاقية {a}"},
    "cc_b_textile": {"fr": "textile", "ar": "النسيج"},
    "cc_b_btp": {"fr": "bâtiment et travaux publics", "ar": "البناء والأشغال العامة"},
    "cc_y_couv": {"fr": "% du nombre de salariés", "ar": "% من عدد الأجراء"},
    "cc_couv_2015": {"fr": "2015 :\nsans valeur", "ar": "2015:\nدون قيمة"},
    "cc_c_couv": {"fr": "taux de couverture de la négociation collective (%)",
                  "ar": "نسبة تغطية المفاوضة الجماعية (%)"},
    "cc_c_source": {"fr": "source déclarée par l'OIT", "ar": "المصدر المصرّح به"},
})


def _date_fr(iso: str) -> str:
    """Date en toutes lettres : « 1er mai 1994 »."""
    j = dt.date.fromisoformat(str(iso)[:10])
    return f"{'1er' if j.day == 1 else j.day} {_MOIS[j.month - 1]} {j.year}"


def _vide(v) -> bool:
    return v is None or v != v or str(v).strip() == ""


# ---- le paysage : agréments par année, inventaire par branche

def _cc_agrements():
    d = figtools.series(SERIE_CC_AGREMENTS)
    lignes = [{"annee": int(r.annee), "conventions": int(r.dont_conventions_sectorielles),
               "avenants": int(r.notices_agrement_avenant),
               "edition_fr": None if _vide(r.arretes_avenant_plein_texte_fr)
               else int(r.arretes_avenant_plein_texte_fr)} for r in d.itertuples()]
    assert sum(l["conventions"] for l in lignes) == 61
    assert sum(l["avenants"] for l in lignes) == 512
    assert (lignes[0]["annee"], lignes[-1]["annee"]) == (1969, 2025)
    # Comptes que le chapitre écrit en toutes lettres (tableau des périodes et points).
    par_an = {l["annee"]: l for l in lignes}
    assert sum(par_an[a]["conventions"] for a in range(1974, 1978)) == 39
    assert sum(par_an[a]["conventions"] for a in range(1983, 2015)) == 19
    assert par_an[1975]["conventions"] == 24
    assert [par_an[a]["avenants"] for a in (1983, 1989, 1993, 2013, 2016, 2017)] == [
        35, 43, 51, 40, 42, 42]
    return lignes


def fig_cc_agrements():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _cc_agrements()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    larg = 0.42
    ax.bar([l["annee"] - larg / 2 for l in r], [l["conventions"] for l in r], width=larg,
           color=BLEU, label=ft(_lab("cc_conv")))
    plein = [l for l in r if l["annee"] not in _CC_SOUS_COMPTE]
    sous = [l for l in r if l["annee"] in _CC_SOUS_COMPTE]
    ax.bar([l["annee"] + larg / 2 for l in plein], [l["avenants"] for l in plein], width=larg,
           color=ORANGE, label=ft(_lab("cc_aven")))
    ax.bar([l["annee"] + larg / 2 for l in sous], [l["avenants"] for l in sous], width=larg,
           color="white", edgecolor=ORANGE, hatch="////", lw=0.6,
           label=ft(_lab("cc_aven_sous")))
    for l in r:
        for cle, dx, couleur in (("conventions", -larg / 2, BLEU), ("avenants", larg / 2, ORANGE)):
            if l[cle] >= 20:
                ax.text(l["annee"] + dx, l[cle] + 0.6, str(l[cle]), ha="center", va="bottom",
                        fontsize=7, color=couleur)
    ax.set_xlim(1967.5, 2026.5)
    ax.set_ylim(0, 58)
    ax.set_xticks(range(1970, 2026, 5))
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("cc_y_textes")))
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False, ncol=3)
    fig.tight_layout()
    return fig


def vues_cc_agrements():
    return fig_cc_agrements()


def table_cc_agrements():
    import pandas as pd
    r = _cc_agrements()
    return pd.DataFrame({
        _lab("c_annee"): [l["annee"] for l in r],
        _lab("cc_c_conv"): [l["conventions"] for l in r],
        _lab("cc_c_aven"): [l["avenants"] for l in r],
        _lab("cc_c_sous"): [_lab("oui") if l["annee"] in _CC_SOUS_COMPTE else "" for l in r],
        _lab("cc_c_fr"): pd.array([l["edition_fr"] for l in r], dtype="Int64"),
    })


def tableau_cc_inventaire() -> str:
    """Tableau Markdown des 57 branches : agrément, Journal officiel, avenants.

    L'année du fascicule est celle de sa date dans la série : elle suit l'arrêté. Le jour n'est
    pas donné, la série ne le garantissant pas. Les colonnes de fabrication de la série
    (rattachement, lisibilité) ne sont pas reprises.
    """
    import re
    d = figtools.series(SERIE_CC_BRANCHES)
    assert len(d) == 57 and int(d["nombre_agrements"].sum()) == 61
    assert int((d["nombre_agrements"] > 0).sum()) == 56
    # 465 avenants distincts rattachés, dont quatre comptés dans deux branches.
    assert int(d["notices_avenant"].sum()) == 465 + sum(_CC_DOUBLE_COMPTE.values())
    assert set(_CC_DOUBLE_COMPTE) <= set(d["branche"])
    lignes = []
    for r in d.itertuples():
        if _vide(r.date_arrete_agrement):
            agrement = journal = "—"
        else:
            agrement = _date_fr(r.date_arrete_agrement)
            annee = dt.date.fromisoformat(r.jort_date_notice).year
            assert annee >= dt.date.fromisoformat(r.date_arrete_agrement).year, r.branche
            journal = f"n° {int(r.jort_numero)} de {annee}, {r.jort_pages}"
        suivants = "—"
        if not _vide(r.agrements_ulterieurs):
            suivants = " ; ".join(_date_fr(x) for x in
                                  re.findall(r"(\d{4}-\d\d-\d\d) \(", r.agrements_ulterieurs))
        n = int(r.notices_avenant)
        nombre = "—" if n == 0 else f"{n}{'*' if r.branche in _CC_DOUBLE_COMPTE else ''}"
        numero = "—" if _vide(r.avenant_numero_max) else str(int(r.avenant_numero_max))
        if _vide(r.date_dernier_arrete_avenant) or r.branche in _CC_DOUBLE_COMPTE:
            dernier = "—"
        else:
            dernier = _date_fr(r.date_dernier_arrete_avenant)
        dernier_fr = ("—" if _vide(r.annee_dernier_avenant_plein_texte_fr)
                      else str(int(r.annee_dernier_avenant_plein_texte_fr)))
        lignes.append((r.branche, agrement, journal, suivants, nombre, numero, dernier,
                       dernier_fr))
    entetes = ["Branche", "Premier agrément", "*Journal officiel* de cet agrément",
               "Agréments suivants", "Avenants agréés relevés", "Numéro d'avenant le plus élevé",
               "Dernier avenant agréé, d'après les intitulés",
               "Année d'un avenant postérieur, d'après l'édition française"]
    sortie = ["| " + " | ".join(entetes) + " |", "|:---|:---|:---|:---|---:|---:|:---|:---|"]
    sortie += ["| " + " | ".join(l) + " |" for l in lignes]
    return "\n".join(sortie)


# ---- ce que les conventions ajoutent au SMIG : salaire d'entrée de deux branches

def _reserve_claire(reserve) -> tuple[str, bool]:
    """Réserve de la série dite pour le lecteur, et si elle porte sur le montant ou la date
    d'effet (marqueur creux de la figure). Une réserve de la série peut en réunir plusieurs.
    Le haut de grille manquant se lit à sa case vide ; l'origine de la lecture a sa colonne."""
    if _vide(reserve):
        return "", False
    textes, marque, reconnu = [], False, False
    for motif, texte, creux in (
            ("non comparable au SMIG", "hors indemnité complémentaire provisoire", False),
            ("date d'effet non relevée", "date d'effet non établie", False),
            ("date d'effet lue", "date d'effet à confirmer", True),
            ("à titre exceptionnel", "date d'effet fixée « à titre exceptionnel »", False),
            ("montage lu", "montant à confirmer", True),
            ("page arabe déduite", "page à confirmer", False),
            ("numéro de page déduit", "page à confirmer", False),
            ("haut de grille : sous-catégorie", "haut de la grille à confirmer", False),
            ("date du fascicule", "date du fascicule à confirmer", False),
            ("haut de grille non lu", None, False),
            ("lu sur la reproduction", None, False)):
        if motif in reserve:
            reconnu = True
            marque = marque or creux
            if texte and texte not in textes:
                textes.append(texte)
    assert reconnu, reserve
    return " ; ".join(textes), marque


def _cc_date_fascicule(mention: str) -> str:
    """« 21-24 août 1990 » -> « des 21 et 24 août 1990 » ; « 4 oct. 1994 » -> « du 4 octobre 1994 ».
    Une précision entre parenthèses de la série est écartée."""
    jour, *reste = [_MOIS_ABREGES.get(m, m) for m in mention.split(" (")[0].split()]
    if "-" in jour:
        return "des " + " et ".join(jour.split("-")) + " " + " ".join(reste)
    return "du " + " ".join([jour] + reste)


def _cc_grilles():
    """Une ligne par branche et par date d'effet, avec son segment ; les conventions d'origine,
    sans date d'effet, sont placées à la date de leur arrêté d'agrément."""
    d = figtools.series(SERIE_CC_GRILLES)
    b = figtools.series(SERIE_CC_BRANCHES).set_index("branche")
    lignes = []
    for r in d.itertuples():
        origine = _vide(r.date_effet)
        jour = (b.loc[_CC_BRANCHE_INVENTAIRE[r.branche], "date_arrete_agrement"] if origine
                else r.date_effet)
        comparable = r.comparable_au_smig == "oui"
        assert comparable != _vide(r.rapport_bas_smig), (r.branche, jour)
        reserve, marque = _reserve_claire(r.reserve)
        lignes.append({
            "branche": r.branche, "origine_convention": origine, "jour": dt.date.fromisoformat(jour),
            "x": figtools.abscisse_date(jour), "bas": float(r.salaire_horaire_bas),
            "haut": None if _vide(r.salaire_horaire_haut) else float(r.salaire_horaire_haut),
            "comparable": comparable, "smig": float(r.smig_48h_horaire),
            "rapport": float(r.rapport_bas_smig) if comparable else None,
            "texte": r.avenant, "cle": _CC_CLES[(r.branche, r.avenant)],
            "journal": (f"n° {int(r.jort_numero)} " + _cc_date_fascicule(r.jort_date_mention)
                        + f", p. {int(r.jort_page)}"),
            "origine": _CC_ORIGINES[r.origine_lecture][0],
            "edition": _CC_ORIGINES[r.origine_lecture][1], "nom_segment": r.segment,
            "reserve": reserve, "a_confirmer": marque})
    lignes.sort(key=lambda l: (l["branche"] != "textile", l["jour"]))
    # Segments : ceux de la série, dans l'ordre des dates ; leurs bornes sont contrôlées.
    for branche, attendus in _CC_SEGMENTS.items():
        propres = [l for l in lignes if l["branche"] == branche]
        noms = list(dict.fromkeys(l["nom_segment"] for l in propres))
        for l in propres:
            l["segment"] = noms.index(l["nom_segment"])
        bornes = [(min(l["jour"].year for l in propres if l["segment"] == s),
                   max(l["jour"].year for l in propres if l["segment"] == s))
                  for s in range(len(noms))]
        assert bornes == attendus, (branche, bornes)
        assert all(len({l["comparable"] for l in propres if l["segment"] == s}) == 1
                   for s in range(len(noms))), branche
    assert sum(l["origine"] == "copie" for l in lignes) == 3
    # Bornes du rapport aux dates d'effet, telles que le chapitre les écrit.
    for (branche, debut, fin), (bas, haut) in _CC_BORNES.items():
        v = [round(l["rapport"], 2) for l in lignes if l["branche"] == branche
             and not l["origine_convention"] and l["comparable"] and debut <= l["jour"].year <= fin]
        assert (min(v), max(v)) == (bas, haut), (branche, debut, fin, min(v), max(v))
    # Hausse d'une grille à la suivante, dans le segment continu : de 3,3 à 5,2 % de 1996 à
    # 2010, où chaque avenant porte trois grilles ; de 5,0 à 7,0 % depuis 2011.
    hausses = {False: [], True: []}
    for branche in _CC_SEGMENTS:
        suite = [l for l in lignes if l["branche"] == branche and l["segment"] == 2]
        for avant, l in zip(suite, suite[1:]):
            if l["jour"].year >= 1996:
                hausses[l["jour"].year >= 2011].append(round(100 * (l["bas"] / avant["bas"] - 1), 1))
        for numero in ((6, 7, 8, 9, 10) if branche == "textile" else (5, 6, 7, 8, 9)):
            assert sum(l["texte"] == f"avenant n° {numero}" for l in suite) == 3, (branche, numero)
    assert (min(hausses[False]), max(hausses[False])) == (3.3, 5.2), hausses[False]
    assert (min(hausses[True]), max(hausses[True])) == (5.0, 7.0), hausses[True]
    return lignes


def _cc_rapport_en_vigueur(pts, smig):
    """Rapport du salaire d'entrée au SMIG, en escalier, de la première à la dernière grille
    d'un segment : une grille vaut jusqu'à la suivante, le SMIG aussi ; le rapport change donc
    à chaque grille et à chaque relèvement du SMIG entre les deux. Aucune valeur après la
    dernière grille du segment."""
    debut, fin = pts[0]["jour"], pts[-1]["jour"]
    jours = sorted({l["jour"] for l in pts} | {j for j in smig["jour"] if debut < j <= fin})
    xs, ys = [], []
    for j in jours:
        grille = [l for l in pts if l["jour"] <= j][-1]
        ys.append(grille["bas"] / _en_vigueur(smig, "smig_48h_horaire", j))
        xs.append(figtools.abscisse_date(j.isoformat()))
    for l in pts:  # aux dates des grilles, le rapport tracé est celui de la série
        assert abs(ys[jours.index(l["jour"])] - l["rapport"]) < 0.0006, l["jour"]
    # Extrêmes du rapport suivi jour après jour, tels que le chapitre les écrit.
    if len(pts) > 3:
        (jour_min, bas), (jour_max, haut) = _CC_EXTREMES[pts[0]["branche"]]
        i_min, i_max = ys.index(min(ys)), ys.index(max(ys))
        assert (jours[i_min], round(ys[i_min], 2)) == (jour_min, bas), (jours[i_min], ys[i_min])
        assert (jours[i_max], round(ys[i_max], 2)) == (jour_max, haut), (jours[i_max], ys[i_max])
    return xs, ys


def _fig_cc_salaire_entree(rapport: bool):
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r, smig = _cc_grilles(), _serie()
    fig, ax = plt.subplots(figsize=(10, 5.8))
    if not rapport:
        s = smig[(smig["jour"] >= dt.date(1974, 1, 1)) & (smig["jour"] <= dt.date(2026, 1, 1))]
        ax.plot([figtools.abscisse_date(j.isoformat()) for j in s["jour"]],
                list(s["smig_48h_horaire"]), drawstyle="steps-post", color=GRIS, lw=1.6,
                label=ft(_lab("cc_smig")))
    for branche, lib, couleur, marqueur in (("textile", "cc_textile", BLEU, "o"),
                                            ("bâtiment et travaux publics", "cc_btp", ORANGE, "s")):
        propres = [l for l in r if l["branche"] == branche]
        for i, s in enumerate(sorted({l["segment"] for l in propres})):
            pts = [l for l in propres if l["segment"] == s]
            hors = not pts[0]["comparable"]
            if rapport and hors:
                continue
            style = dict(color=couleur, lw=1.2 if hors else 1.8, ls=":" if hors else "-")
            if rapport:
                if len(pts) > 1:
                    ax.plot(*_cc_rapport_en_vigueur(pts, smig), drawstyle="steps-post",
                            color=couleur, lw=1.1)
            else:
                ax.plot([l["x"] for l in pts], [l["bas"] for l in pts], drawstyle="steps-post",
                        **style)
            cle = "rapport" if rapport else "bas"
            for l in pts:
                copie = l["origine"] == "copie"
                ax.plot([l["x"]], [l[cle]], ls="none",
                        marker="x" if hors else "^" if copie else marqueur,
                        ms=5 if hors else 7 if copie else 4, mew=1.3, mec=couleur,
                        mfc="white" if l["a_confirmer"] else couleur, zorder=4)
            if i == 0:
                ax.plot([], [], color=couleur, lw=1.8, marker=marqueur, ms=4.5, label=ft(_lab(lib)))
    if not rapport:
        ax.plot([], [], color="black", lw=1.2, ls=":", marker="x", ms=5,
                label=ft(_lab("cc_hors_icp")))
    ax.plot([], [], ls="none", marker="o", ms=4.5, mew=1.4, mec="black", mfc="white",
            label=ft(_lab("cc_a_confirmer")))
    ax.plot([], [], ls="none", marker="^", ms=7, mec=ORANGE, mfc=ORANGE,
            label=ft(_lab("cc_copie")))
    for jour, cle_r, cote in (("1994-05-01", "cc_r_1994", "right"),):
        x = figtools.abscisse_date(jour)
        ax.axvline(x, color="#57606a", ls=(0, (2, 2)), lw=1, zorder=1)
        ax.annotate(_ft_lignes(_lab(cle_r)), xy=(x, 1), xycoords=("data", "axes fraction"),
                    xytext=(-4 if cote == "right" else 4, -4), textcoords="offset points",
                    ha=cote, va="top", fontsize=7, color="#57606a")
    if rapport:
        ax.axhline(1, color=GRIS, lw=0.8)
        ax.set_ylim(0.95, 1.4)
        ax.set_ylabel(ft(_lab("cc_y_rapport")))
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: _fr(v, 2)))
    else:
        ax.set_yscale("log")
        ax.set_ylim(0.1, 6.5)
        ax.set_yticks([0.1, 0.2, 0.5, 1, 2, 5])
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: _fr(v, 1)))
        ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
        ax.set_ylabel(ft(_lab("cc_y_horaire")))
    ax.set_xlim(1972.5, 2027.5)
    ax.set_xticks(range(1974, 2027, 4))
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False, ncol=2)
    fig.tight_layout()
    return fig


def vues_cc_salaire_entree():
    return [(_lab("vue_courants_log"), _fig_cc_salaire_entree(False)),
            (_lab("vue_rapport"), _fig_cc_salaire_entree(True))]


def _cc_branche(l) -> str:
    return _lab("cc_b_textile" if l["branche"] == "textile" else "cc_b_btp")


def _cc_effet(l) -> str:
    return _lab("cc_origine").format(a=l["jour"].year) if l["origine_convention"] else _date_fr(l["jour"])


def table_cc_salaire_entree():
    import pandas as pd
    r = _cc_grilles()
    return pd.DataFrame({
        _lab("cc_c_branche"): [_cc_branche(l) for l in r],
        _lab("cc_c_effet"): ["" if l["origine_convention"] else l["jour"].isoformat() for l in r],
        _lab("cc_c_texte"): [_cc_effet(l) if l["origine_convention"] else l["texte"] for l in r],
        _lab("cc_c_bas"): [l["bas"] for l in r],
        _lab("cc_c_haut"): [l["haut"] for l in r],
        _lab("cc_c_smig"): [l["smig"] for l in r],
        _lab("cc_c_rapport"): [None if l["rapport"] is None else round(l["rapport"], 2) for l in r],
        _lab("cc_c_origine"): [l["edition"] for l in r],
        _lab("cc_c_reserve"): [l["reserve"] for l in r],
    })


def _cc_ligne_montants(l) -> list[str]:
    return [_fr(l["bas"], 3), _fr(l["smig"], 3),
            "—" if l["rapport"] is None else _fr(l["rapport"], 2)]


def tableau_cc_reperes() -> str:
    """Tableau Markdown court : salaire d'entrée, SMIG et rapport à quelques dates."""
    r = _cc_grilles()
    lignes = []
    for branche, effet in _CC_REPERES:
        l = next(l for l in r if l["branche"] == branche
                 and (l["origine_convention"] if effet is None else l["jour"].isoformat() == effet))
        lignes.append([_cc_branche(l), _cc_effet(l)] + _cc_ligne_montants(l))
    entetes = ["Branche", "Grille", "Salaire horaire d'entrée (dinars)",
               "SMIG horaire, régime de 48 heures (dinars)", "Salaire d'entrée, en SMIG"]
    sortie = ["| " + " | ".join(entetes) + " |", "|:---|:---|---:|---:|---:|"]
    sortie += ["| " + " | ".join(l) + " |" for l in lignes]
    return "\n".join(sortie)


def tableau_cc_grilles() -> str:
    """Tableau Markdown de toutes les grilles de la série, avec leur texte et leur fascicule."""
    r = _cc_grilles()
    lignes = []
    for l in r:
        bas, smig, rapport = _cc_ligne_montants(l)
        lignes.append([_cc_branche(l), _cc_effet(l), bas,
                       "—" if l["haut"] is None else _fr(l["haut"], 3), smig, rapport,
                       l["texte"], l["journal"], l["edition"],
                       f"[@{l['cle']}; @{_CC_CLE_COPIE}]" if l["origine"] == "copie"
                       else f"[@{l['cle']}]",
                       l["reserve"] or "—"])
    entetes = ["Branche", "Date d'effet de la grille", "Salaire horaire d'entrée (dinars)",
               "Haut de la grille (dinars par heure)", "SMIG horaire, régime de 48 heures (dinars)",
               "Salaire d'entrée, en SMIG", "Convention ou avenant", "*Journal officiel* de la grille",
               "Édition du *Journal officiel*", "Référence", "Réserve"]
    sortie = ["| " + " | ".join(entetes) + " |",
              "|:---|:---|---:|---:|---:|---:|:---|:---|:---|:---|:---|"]
    sortie += ["| " + " | ".join(l) + " |" for l in lignes]
    return "\n".join(sortie)


# ---- la couverture, source extérieure (OIT)

def _cc_couverture():
    d = figtools.series(SERIE_CC_COUVERTURE)
    lignes = [{"annee": int(r.annee), "taux": float(r.taux_couverture_pct),
               "source": r.source_declaree} for r in d.itertuples()]
    assert [l["annee"] for l in lignes] == [2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019]
    return lignes


def fig_cc_couverture():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _cc_couverture()
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.bar([l["annee"] for l in r], [l["taux"] for l in r], width=0.7, color=VIOLET)
    for l in r:
        ax.text(l["annee"], l["taux"] + 1, _fr(l["taux"]), ha="center", va="bottom", fontsize=8)
    ax.text(2015, 3, _ft_lignes(_lab("cc_couv_2015")), ha="center", va="bottom", fontsize=7,
            color="#57606a")
    ax.set_xlim(2009.3, 2019.7)
    ax.set_ylim(0, 80)
    ax.set_xticks(range(2010, 2020))
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("cc_y_couv")))
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    fig.tight_layout()
    return fig


def vues_cc_couverture():
    return fig_cc_couverture()


def table_cc_couverture():
    import pandas as pd
    r = _cc_couverture()
    return pd.DataFrame({
        _lab("c_annee"): [l["annee"] for l in r],
        _lab("cc_c_couv"): [l["taux"] for l in r],
        _lab("cc_c_source"): [l["source"] for l in r],
    })

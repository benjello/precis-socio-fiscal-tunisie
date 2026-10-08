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

SERIE_TRIMESTRES = "cnss-pyramide-trimestres-declares-2013"
SERIE_QUANTILES = "cnss-quantiles-salaires-approches"
SERIE_REPERES = "cnss-pyramide-dinars-reperes"
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

figtools.register_provenance(SERIE_QUANTILES, **{
    **figtools.meta(SERIE_QUANTILES),
    "sources": ["cnss-annuaire-2013", "cnss-annuaire-2018"],
    "titre_ar": ("الصندوق الوطني للضمان الاجتماعي: كمّيات تقريبية للأجر الشهري المصرّح به، "
                 "بالاستيفاء داخل شرائح الأجر بالدينار — سلسلة مشتقّة"),
    "unite_ar": "دينار جارٍ في الشهر",
    "perimetre_ar": ("الربيع الأول، الوسيط، الربيع الثالث والعُشير التاسع، لكلّ عمود من كلّ "
                     "طبعة من هرم الأجور بالدينار، وللأجراء المصرّح بهم في الثلاثيات الأربع "
                     "سنة 2013"),
    "caveats_ar": ("سلسلة مشتقّة لا ينشرها المصدر: استيفاء خطّي داخل الشريحة، والخطأ دون عرض "
                   "الشريحة (20 إلى 40 دينارًا في طبعة 2013، ثمّ 50 دينارًا). لا تُقرأ "
                   "الاتّجاهات إلّا داخل المقطع الواحد: الطبعات لا تعطي التوزيع نفسه للسنة "
                   "نفسها."),
})
figtools.register_provenance(SERIE_TRIMESTRES, **{
    **figtools.meta(SERIE_TRIMESTRES),
    "sources": ["cnss-annuaire-2013"],
})

_L.update({
    "vue_indices": {"fr": f"Indices, {ANNEE_BASE_INDICE} = 100",
                    "ar": f"أرقام قياسية، {ANNEE_BASE_INDICE} = 100"},
    "vue_pa": {"fr": f"Pouvoir d'achat, {ANNEE_BASE_INDICE} = 100",
               "ar": f"القدرة الشرائية، {ANNEE_BASE_INDICE} = 100"},
    "y_pa": {"fr": f"Indice rapporté à celui des prix, base 100 en {ANNEE_BASE_INDICE}",
             "ar": f"الرقم القياسي منسوبًا إلى الأسعار، أساس 100 سنة {ANNEE_BASE_INDICE}"},
    "y_smig_pct": {"fr": "SMIG de 48 heures, en % du salaire moyen déclaré",
                   "ar": "الأجر الأدنى (48 ساعة)، بالنسبة المائوية من معدّل الأجر المصرّح به"},
    "ss_2006": {"fr": "Annuaire 2006 (1970-1999 et 2002-2006)", "ar": "دليل 2006 (1970-1999 و2002-2006)"},
    "ss_2018": {"fr": "Annuaire 2018 (2000-2018)", "ar": "دليل 2018 (2000-2018)"},
    "ss_4t": {"fr": "Salaire moyen des déclarés quatre trimestres, 2013",
              "ar": "معدّل أجر المصرّح بهم في الثلاثيات الأربع، 2013"},
    "ss_gel": {"fr": "SMIG sans relèvement", "ar": "الأجر الأدنى دون ترفيع"},
    "ss_1974": {"fr": "1974 : institution\ndu SMIG, indemnité\nde cherté de vie\ncomprise",
                "ar": "1974: إحداث الأجر\nالأدنى المضمون\nشاملاً منحة\nغلاء المعيشة"},
    "ss_2003": {"fr": "2003 : taxis\net louages\n(décret de 2002)",
                "ar": "2003: سيارات\nالأجرة واللواج\n(أمر 2002)"},
    "ss_2016": {"fr": "2016 : hausse\nà effet rétroactif", "ar": "2016: ترفيع\nبمفعول رجعي"},
    "c_ss_2006": {"fr": "SMIG / salaire moyen déclaré, annuaire 2006 (%)",
                  "ar": "الأجر الأدنى / معدّل الأجر المصرّح به، دليل 2006 (%)"},
    "c_ss_2018": {"fr": "SMIG / salaire moyen déclaré, annuaire 2018 (%)",
                  "ar": "الأجر الأدنى / معدّل الأجر المصرّح به، دليل 2018 (%)"},
    "c_ss_4t": {"fr": "SMIG / salaire moyen des déclarés quatre trimestres (%)",
                "ar": "الأجر الأدنى / معدّل أجر المصرّح بهم في الثلاثيات الأربع (%)"},
    "c_a_2006": {"fr": "salaire annuel moyen déclaré, annuaire 2006 (D courants)",
                 "ar": "معدّل الأجر السنوي المصرّح به، دليل 2006 (د جارية)"},
    "c_a_2018": {"fr": "salaire annuel moyen déclaré, annuaire 2018 (D courants)",
                 "ar": "معدّل الأجر السنوي المصرّح به، دليل 2018 (د جارية)"},
    "c_r_2006": {"fr": f"salaire mensuel moyen déclaré, annuaire 2006 (D de {ANNEE_BASE})",
                 "ar": f"معدّل الأجر الشهري المصرّح به، دليل 2006 (د {ANNEE_BASE})"},
    "c_r_2018": {"fr": f"salaire mensuel moyen déclaré, annuaire 2018 (D de {ANNEE_BASE})",
                 "ar": f"معدّل الأجر الشهري المصرّح به، دليل 2018 (د {ANNEE_BASE})"},
    "c_r_4t": {"fr": f"salaire mensuel moyen des déclarés quatre trimestres (D de {ANNEE_BASE})",
               "ar": f"معدّل الأجر الشهري للمصرّح بهم في الثلاثيات الأربع (د {ANNEE_BASE})"},
    "c_pa_salaire": {"fr": f"pouvoir d'achat, panel de l'INS ({ANNEE_BASE_INDICE} = 100)",
                     "ar": f"القدرة الشرائية، عيّنة المعهد ({ANNEE_BASE_INDICE} = 100)"},
    "c_pa_cnss": {"fr": f"pouvoir d'achat, salaire moyen déclaré à la CNSS ({ANNEE_BASE_INDICE} = 100)",
                  "ar": f"القدرة الشرائية، معدّل الأجر المصرّح به ({ANNEE_BASE_INDICE} = 100)"},
    "c_pa_smig": {"fr": f"pouvoir d'achat, SMIG 48 h ({ANNEE_BASE_INDICE} = 100)",
                  "ar": f"القدرة الشرائية، الأجر الأدنى 48 ساعة ({ANNEE_BASE_INDICE} = 100)"},
    "c_p_smig_ref": {"fr": "SMIG de référence de la CNSS (D par mois)",
                     "ar": "الأجر الأدنى المرجعي لدى الصندوق (د في الشهر)"},
    # Quantiles approchés.
    "q_Q1": {"fr": "Premier quartile", "ar": "الربيع الأول"},
    "q_médiane": {"fr": "Médiane", "ar": "الوسيط"},
    "q_Q3": {"fr": "Troisième quartile", "ar": "الربيع الثالث"},
    "q_D9": {"fr": "Neuvième décile", "ar": "العُشير التاسع"},
    "q_d12": {"fr": "Salaire de l'année divisé par douze, années incomplètes comprises",
              "ar": "أجر السنة مقسومًا على اثني عشر، بما فيه السنوات غير الكاملة"},
    "q_mois": {"fr": "Autre mesure du salaire mensuel (annuaires 2016 à 2018, années 2010-2016)",
               "ar": "قيس آخر للأجر الشهري (أدلّة 2016 إلى 2018، سنوات 2010-2016)"},
    "q_4t": {"fr": "Salariés déclarés les quatre trimestres, 2013",
             "ar": "الأجراء المصرّح بهم في الثلاثيات الأربع، 2013"},
    "c_q_ed": {"fr": "annuaire de la CNSS", "ar": "دليل الصندوق"},
    "c_q_seg": {"fr": "segment", "ar": "المقطع"},
    "c_q_mesure": {"fr": "mesure du salaire mensuel", "ar": "قيس الأجر الشهري"},
    "c_q_pop": {"fr": "population", "ar": "الفئة"},
    "pop_tous": {"fr": "tous les salariés déclarés", "ar": "كلّ الأجراء المصرّح بهم"},
    "pop_4t": {"fr": "déclarés les quatre trimestres", "ar": "المصرّح بهم في الثلاثيات الأربع"},
    "m_d12": {"fr": "année\u00a0÷\u00a012", "ar": "السنة ÷ 12"},
    "m_mois": {"fr": "autre mesure", "ar": "قيس آخر"},
    "c_q_courant": {"fr": "{q} (D courants par mois)", "ar": "{q} (د جارية في الشهر)"},
    "c_q_reel": {"fr": "{q} (D de {a} par mois)", "ar": "{q} (د {a} في الشهر)"},
    "ti_annees": {"fr": "Années", "ar": "السنوات"},
    "ti_ed": {"fr": "Annuaire", "ar": "الدليل"},
    "ti_mesure": {"fr": "Salaire mensuel", "ar": "الأجر الشهري"},
    "ti_debut": {"fr": "{r}, début", "ar": "{r}، البداية"},
    "ti_fin": {"fr": "{r}, fin", "ar": "{r}، النهاية"},
    "ti_q3q1": {"fr": "Q3/Q1", "ar": "الربيع 3 / الربيع 1"},
    "ti_mq1": {"fr": "Médiane/Q1", "ar": "الوسيط / الربيع 1"},
    "ti_d9m": {"fr": "D9/médiane", "ar": "العُشير 9 / الوسيط"},
    "t13_grandeur": {"fr": "2013", "ar": "2013"},
    "t13_ens": {"fr": "Ensemble<br>(D de 2013)", "ar": "جملة المصرّح بهم<br>(د 2013)"},
    "t13_ens_reel": {"fr": f"Ensemble<br>(D de {ANNEE_BASE})",
                     "ar": f"جملة المصرّح بهم<br>(د {ANNEE_BASE})"},
    "t13_4t": {"fr": "Quatre trimestres<br>(D de 2013)", "ar": "الثلاثيات الأربع<br>(د 2013)"},
    "t13_4t_reel": {"fr": f"Quatre trimestres<br>(D de {ANNEE_BASE})",
                    "ar": f"الثلاثيات الأربع<br>(د {ANNEE_BASE})"},
    "t13_n": {"fr": "Salariés", "ar": "الأجراء"},
    "t13_moy": {"fr": "Salaire moyen<br>(par an)", "ar": "معدّل الأجر السنوي"},
    "t13_q1": {"fr": "Premier quartile<br>(par mois)", "ar": "الربيع الأول، في الشهر"},
    "t13_med": {"fr": "Médiane<br>(par mois)", "ar": "الوسيط، في الشهر"},
    "t13_q3": {"fr": "Troisième quartile<br>(par mois)", "ar": "الربيع الثالث، في الشهر"},
    "t13_300": {"fr": "Moins de 300 D de 2013<br>(part des salariés)", "ar": "أقلّ من 300 د في الشهر"},
    "t13_330": {"fr": "De 300 à 330 D de 2013<br>(part des salariés)", "ar": "من 300 إلى 330 د في الشهر"},
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
    "i_salaire": {"fr": ("Salaire moyen, salariés déclarés cinq trimestres de suite, quatrième "
                         "trimestre (INS, d'après la CNSS)"),
                  "ar": ("معدّل الأجر، عيّنة قارّة من الأجراء، الثلاثي الرابع (المعهد، حسب "
                         "تصاريح الصندوق)")},
    "i_cnss": {"fr": ("Salaire moyen déclaré, tous les salariés déclarés dans l'année "
                      "(CNSS, annuaire 2018)"),
               "ar": ("معدّل الأجر المصرّح به، كلّ الأجراء المصرّح بهم في السنة (الصندوق، "
                      "دليل 2018)")},
    "ri_2003": {"fr": "2003 : taxis et louages\n(salaire moyen déclaré)",
                "ar": "2003: سيارات الأجرة واللواج\n(الأجر المصرّح به لدى الصندوق)"},
    "c_i_cnss_niveau": {"fr": "salaire annuel moyen déclaré à la CNSS, annuaire 2018 (D courants)",
                        "ar": "معدّل الأجر السنوي المصرّح به لدى الصندوق، دليل 2018 (د جارية)"},
    "c_i_cnss": {"fr": f"salaire moyen déclaré à la CNSS (indice, {ANNEE_BASE_INDICE} = 100)",
                 "ar": f"معدّل الأجر المصرّح به لدى الصندوق (رقم قياسي، {ANNEE_BASE_INDICE} = 100)"},
    "i_prov": {"fr": "2025 : taux provisoire", "ar": "2025: نسبة وقتية"},
    "i_smig": {"fr": "SMIG, régime de 48 heures, moyenne annuelle",
               "ar": "الأجر الأدنى المضمون، نظام 48 ساعة، المعدّل السنوي"},
    "i_prix": {"fr": "Prix à la consommation", "ar": "أسعار الاستهلاك"},
    "c_i_taux": {"fr": "panel de l'INS : taux chaîné de l'année (%)",
                 "ar": "عيّنة المعهد: النسبة السنوية المتسلسلة (%)"},
    "c_i_prov": {"fr": "taux provisoire", "ar": "نسبة وقتية"},
    "c_i_salaire": {"fr": f"panel de l'INS, quatrième trimestre (indice, {ANNEE_BASE_INDICE} = 100)",
                    "ar": f"عيّنة المعهد، الثلاثي الرابع (رقم قياسي، {ANNEE_BASE_INDICE} = 100)"},
    "c_i_smig": {"fr": f"SMIG 48 h, moyenne annuelle (indice, {ANNEE_BASE_INDICE} = 100)",
                 "ar": f"الأجر الأدنى 48 ساعة، المعدّل السنوي (رقم قياسي، {ANNEE_BASE_INDICE} = 100)"},
    "c_i_prix": {"fr": f"prix à la consommation (indice, {ANNEE_BASE_INDICE} = 100)",
                 "ar": f"أسعار الاستهلاك (رقم قياسي، {ANNEE_BASE_INDICE} = 100)"},
    "oui": {"fr": "oui", "ar": "نعم"},
    "p_inf1": {"fr": "Moins de 1 SMIG de référence de la CNSS", "ar": "أقلّ من مرّة واحدة الأجر الأدنى المرجعي لدى الصندوق"},
    "p_1_15": {"fr": "De 1 à 1,5 SMIG de référence", "ar": "من 1 إلى 1,5 مرّة الأجر الأدنى المرجعي"},
    "p_sup15": {"fr": "Plus de 1,5 SMIG de référence", "ar": "أكثر من 1,5 مرّة الأجر الأدنى المرجعي"},
    "p_t1": {"fr": "Salariés déclarés au\npremier trimestre 2018 :\n{v} % sous 1 SMIG\nde référence",
             "ar": "الأجراء المصرّح بهم في\nالثلاثي الأول 2018:\n{v} % دون الأجر\nالأدنى المرجعي"},
    "c_mesure": {"fr": "mesure", "ar": "القيس"},
    "m_annuelle": {"fr": "annuelle", "ar": "سنوي"},
    "m_trim": {"fr": "trimestre {t} de 2018", "ar": "الثلاثي {t} من 2018"},
    "c_p_total": {"fr": "salariés déclarés", "ar": "الأجراء المصرّح بهم"},
    "c_p_inf1": {"fr": "moins de 1 SMIG de référence (%)", "ar": "أقلّ من 1 (%)"},
    "c_p_1_15": {"fr": "de 1 à 1,5 SMIG de référence (%)", "ar": "من 1 إلى 1,5 (%)"},
    "c_p_sup15": {"fr": "plus de 1,5 SMIG de référence (%)", "ar": "أكثر من 1,5 (%)"},
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
    "t_part_court": {"fr": "Salaire inférieur au SMIG", "ar": "أجر دون الأجر الأدنى"},
    "t_moitie_court": {"fr": "dont inférieur à la moitié du SMIG", "ar": "منها دون نصف الأجر الأدنى"},
    "t_base_court": {"fr": "Salaire de base moyen (D)", "ar": "معدّل الأجر الأساسي (د)"},
    "t_smig_court": {"fr": "SMIG retenu par l'INS (D)", "ar": "الأجر الأدنى المعتمد (د)"},
    "t_repondantes": {"fr": "Entreprises répondantes", "ar": "المؤسسات المجيبة"},
    "t_taux": {"fr": "Taux de réponse", "ar": "نسبة الإجابة"},
    "t_source": {"fr": "Source", "ar": "المصدر"},
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


def _trimestres_2013(classement: str):
    """Tableau de 2013 selon le nombre de trimestres déclarés, classes en dinars ou en SMIG."""
    t = figtools.series(SERIE_TRIMESTRES)
    return t[t["classement"] == classement]


def _quatre_trimestres():
    """Le salaire moyen des salariés déclarés les quatre trimestres de 2013, mêmes grandeurs.

    Quotient de la masse par l'effectif de la ligne TOTAL de la colonne « 4 trimestres »
    (annuaire 2013, page 35 du fichier PDF) : l'annuaire imprime les deux, non le quotient.
    """
    t = _trimestres_2013("dinars")
    l = t[(t["trimestres_declares"] == "4") & (t["classe"] == "TOTAL")].iloc[0]
    q = {"annee": int(l["annee"]), "salaries": int(l["salaries_declares"]),
         "masse": int(l["masse_salariale_D"])}
    annee, ipc = q["annee"], _ipc()
    s = _moyenne_annuelle(_serie(), "smig_48h_mensuel", annee)
    annuel = q["masse"] / q["salaries"]
    coef = ipc[ANNEE_BASE] / ipc[annee]
    return {"annee": annee, "edition": 2013, "segment": _lab("seg_4t"), "annuel": annuel,
            "salaries": q["salaries"],
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


def _par_annee():
    """Une ligne par année, 1970-2025 : les deux éditions de l'annuaire côte à côte, le point
    de 2013 des déclarés quatre trimestres, puis les indices et leur rapport aux prix."""
    sd, q = _salaire_declare(), _quatre_trimestres()
    ind = {l["annee"]: l for l in _indices()}
    lignes = []
    for annee in range(min(l["annee"] for l in sd), max(ind) + 1):
        ed = {l["edition"]: l for l in sd if l["annee"] == annee}
        un = next(iter(ed.values()), None)
        i = ind.get(annee, {})
        prix = i.get("prix")

        def pa(cle):
            return None if i.get(cle) is None or prix is None else 100 * i[cle] / prix
        lignes.append({
            "annee": annee,
            "a2006": ed[2006]["annuel"] if 2006 in ed else None,
            "a2018": ed[2018]["annuel"] if 2018 in ed else None,
            "smig": un["smig"] if un else None,
            "r2006": ed[2006]["mensuel_reel"] if 2006 in ed else None,
            "r2018": ed[2018]["mensuel_reel"] if 2018 in ed else None,
            "r4t": q["mensuel_reel"] if annee == q["annee"] else None,
            "smig_reel": un["smig_reel"] if un else None,
            "ss2006": 100 * ed[2006]["smig"] / ed[2006]["mensuel"] if 2006 in ed else None,
            "ss2018": 100 * ed[2018]["smig"] / ed[2018]["mensuel"] if 2018 in ed else None,
            "ss4t": 100 * q["smig"] / q["mensuel"] if annee == q["annee"] else None,
            "taux": i.get("taux"), "provisoire": bool(i.get("provisoire")),
            "i_salaire": i.get("salaire"), "i_cnss": i.get("cnss"), "i_smig": i.get("smig"),
            "i_prix": prix, "pa_salaire": pa("salaire"), "pa_cnss": pa("cnss"),
            "pa_smig": pa("smig")})
    return lignes


def _arr(v, d=1):
    return None if v is None else round(v, d)


def fig_pouvoir_achat():
    """Les indices rapportés à celui des prix : pouvoir d'achat, base 100 en 2001."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = [l for l in _par_annee() if l["annee"] >= ANNEE_BASE_INDICE]
    fig, ax = plt.subplots(figsize=(10, 5.6))
    for cle, lib, style in (("pa_salaire", "i_salaire", dict(color=BLEU, lw=2, marker="o", ms=3)),
                            ("pa_cnss", "i_cnss", dict(color=VIOLET, lw=1.8, ls=(0, (5, 2)),
                                                       marker="^", ms=4)),
                            ("pa_smig", "i_smig", dict(color=ORANGE, lw=1.8, marker="s", ms=3))):
        pts = [(l["annee"], l[cle]) for l in r if l[cle] is not None]
        ax.plot([a for a, _ in pts], [v for _, v in pts], label=ft(_lab(lib)), **style)
        dessus = cle == "pa_cnss"
        ax.annotate(_fr(pts[-1][1], 0), xy=pts[-1], xytext=(0, 8) if dessus else (6, 0),
                    textcoords="offset points", va="bottom" if dessus else "center",
                    ha="center" if dessus else "left", fontsize=8, color=style["color"])
    figtools.marque_rupture(ax, 2003, _ft_lignes(_lab("ri_2003")))
    ax.axhline(100, color=GRIS, lw=0.8)
    ax.set_xlim(ANNEE_BASE_INDICE - 0.5, FIN_INDICES + 1.6)
    ax.set_xticks(range(ANNEE_BASE_INDICE, FIN_INDICES + 1, 3))
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_pa")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False, ncol=1)
    fig.tight_layout()
    return fig


def vues_pouvoir_achat():
    """Le salaire moyen, le SMIG et les prix : niveaux en dinars constants depuis 1970, puis
    indices et pouvoir d'achat depuis 2001."""
    controle_texte()
    return [(_lab("vue_constants"), _fig_salaire_declare(False)),
            (_lab("vue_indices"), fig_indices()),
            (_lab("vue_pa"), fig_pouvoir_achat())]


def table_pouvoir_achat():
    import pandas as pd
    r = _par_annee()
    return pd.DataFrame({
        _lab("c_annee"): [l["annee"] for l in r],
        _lab("c_a_2006"): [_arr(l["a2006"], 0) for l in r],
        _lab("c_a_2018"): [_arr(l["a2018"], 0) for l in r],
        _lab("c_48_moy"): [_arr(l["smig"], 3) for l in r],
        _lab("c_r_2006"): [_arr(l["r2006"]) for l in r],
        _lab("c_r_2018"): [_arr(l["r2018"]) for l in r],
        _lab("c_r_4t"): [_arr(l["r4t"]) for l in r],
        _lab("c_48_reel"): [_arr(l["smig_reel"]) for l in r],
        _lab("c_i_taux"): [l["taux"] for l in r],
        _lab("c_i_prov"): [_lab("oui") if l["provisoire"] else "" for l in r],
        _lab("c_i_salaire"): [_arr(l["i_salaire"]) for l in r],
        _lab("c_i_cnss"): [_arr(l["i_cnss"]) for l in r],
        _lab("c_i_smig"): [_arr(l["i_smig"]) for l in r],
        _lab("c_i_prix"): [_arr(l["i_prix"]) for l in r],
        _lab("c_pa_salaire"): [_arr(l["pa_salaire"]) for l in r],
        _lab("c_pa_cnss"): [_arr(l["pa_cnss"]) for l in r],
        _lab("c_pa_smig"): [_arr(l["pa_smig"]) for l in r],
    })


# Périodes sans relèvement du SMIG dans la période tracée (du 1er janvier 1983 au 1er juillet
# 1986 ; du 1er juillet 2012 au 1er mai 2014), en années décimales.
_SANS_RELEVEMENT = ((1983.0, 1986.5), (2012.5, 2014.33))


def fig_smig_salaire():
    """Le SMIG mensuel de 48 heures en % du salaire mensuel moyen déclaré, par segments, avec
    les éléments de législation que le chapitre identifie."""
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r, q = _salaire_declare(), _quatre_trimestres()
    fig, ax = plt.subplots(figsize=(10, 5.8))
    for i, (debut, fin) in enumerate(_SANS_RELEVEMENT):
        ax.axvspan(debut, fin, color=JAUNE, alpha=0.22, lw=0,
                   label=ft(_lab("ss_gel")) if i == 0 else None)
    deja = set()
    for segment in dict.fromkeys((l["edition"], l["segment"]) for l in r):
        edition = segment[0]
        pts = [(l["annee"], 100 * l["smig"] / l["mensuel"]) for l in r
               if (l["edition"], l["segment"]) == segment]
        style = (dict(color=BLEU, marker="o", ms=3.2) if edition == 2006
                 else dict(color=ORANGE, marker="s", ms=3.2))
        ax.plot([a for a, _ in pts], [v for _, v in pts], lw=1.8,
                label=None if edition in deja else ft(_lab(f"ss_{edition}")), **style)
        deja.add(edition)
    ax.plot([q["annee"]], [100 * q["smig"] / q["mensuel"]], ls="none", marker="D", ms=6,
            mfc="white", mec=VIOLET, mew=1.6, label=ft(_lab("ss_4t")))
    for annee, cle in ((1974, "ss_1974"), (1981, "rs_1981"), (1988, "rs_1988"), (2003, "ss_2003")):
        figtools.marque_rupture(ax, annee, _ft_lignes(_lab(cle)))
    v2016 = next(100 * l["smig"] / l["mensuel"] for l in r if l["annee"] == 2016)
    ax.annotate(_ft_lignes(_lab("ss_2016")), xy=(2016, v2016), xytext=(0, 34),
                textcoords="offset points", ha="center", va="bottom", fontsize=7,
                color="#57606a", arrowprops={"arrowstyle": "-", "color": "#57606a", "lw": 0.8})
    ax.set_ylim(0, 115)
    ax.set_xlim(1968.5, 2019.5)
    ax.set_xticks(range(1970, 2019, 4))
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_smig_pct")))
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False, ncol=2)
    fig.tight_layout()
    return fig


def vues_smig_salaire():
    return fig_smig_salaire()


def table_smig_salaire():
    import pandas as pd
    r = [l for l in _par_annee() if l["smig"] is not None]
    return pd.DataFrame({
        _lab("c_annee"): [l["annee"] for l in r],
        _lab("c_48_moy"): [_arr(l["smig"], 3) for l in r],
        _lab("c_a_2006"): [_arr(l["a2006"], 0) for l in r],
        _lab("c_a_2018"): [_arr(l["a2018"], 0) for l in r],
        _lab("c_ss_2006"): [_arr(l["ss2006"]) for l in r],
        _lab("c_ss_2018"): [_arr(l["ss2018"]) for l in r],
        _lab("c_ss_4t"): [_arr(l["ss4t"]) for l in r],
    })


def _indices():
    """Indices base 100 en 2001 : salaire du privé (taux chaîné de l'INS), salaire moyen
    déclaré à la CNSS (édition 2018 de l'annuaire, la seule qui porte 2001), SMIG, prix.

    Les deux salaires ne sont pas la même mesure : l'INS suit un panel de salariés permanents,
    de quatrième trimestre en quatrième trimestre ; l'annuaire divise la masse déclarée de
    l'année par tous les salariés déclarés au moins une fois. Aucun raccord entre éditions.
    """
    cnss = {int(l.annee): float(l.salaire_annuel_moyen_declare_D)
            for l in figtools.series(SERIE_SALAIRE).itertuples() if "2018" in l.edition}
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
            "cnss_niveau": cnss.get(annee),
            "cnss": 100 * cnss[annee] / cnss[ANNEE_BASE_INDICE] if annee in cnss else None,
            "smig": None if s is None else 100 * s / s0,
            "prix": 100 * ipc[annee] / ipc[ANNEE_BASE_INDICE] if annee in ipc else None})
    return lignes


def fig_indices():
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _indices()
    fig, ax = plt.subplots(figsize=(10, 5.6))
    # Deux mesures du salaire, deux tracés distincts : le panel de l'INS en trait plein, le
    # salaire moyen déclaré de l'annuaire en tirets et triangles, d'une autre couleur.
    for cle, lib, style in (("salaire", "i_salaire", dict(color=BLEU, lw=2, marker="o", ms=3)),
                            ("cnss", "i_cnss", dict(color=VIOLET, lw=1.8, ls=(0, (5, 2)),
                                                    marker="^", ms=4)),
                            ("smig", "i_smig", dict(color=ORANGE, lw=1.8, marker="s", ms=3)),
                            ("prix", "i_prix", dict(color=GRIS, lw=1.6, ls="--"))):
        pts = [(l["annee"], l[cle]) for l in r if l[cle] is not None]
        ax.plot([a for a, _ in pts], [v for _, v in pts], label=ft(_lab(lib)), **style)
        dessus = cle == "cnss"  # la série s'arrête en 2018, au milieu du cadre
        ax.annotate(_fr(pts[-1][1], 0), xy=pts[-1], xytext=(0, 8) if dessus else (6, 0),
                    textcoords="offset points", va="bottom" if dessus else "center",
                    ha="center" if dessus else "left", fontsize=8, color=style["color"])
    # Rupture du seul salaire déclaré à la CNSS ; la légende passe sous le cadre pour lui
    # laisser le haut.
    figtools.marque_rupture(ax, 2003, _ft_lignes(_lab("ri_2003")))
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
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False, ncol=2)
    fig.tight_layout()
    return fig


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


def _smig_de_reference() -> dict[int, float]:
    """Le SMIG mensuel que la CNSS imprime sous sa pyramide en dinars (« 6 fois SMIG mensuel
    en D » ÷ 6), par année, dans l'édition la plus récente qui porte l'année."""
    d = figtools.series(SERIE_REPERES).sort_values("source_id")
    return {int(l.annee): float(l.smig_mensuel_de_la_source_D) for l in d.itertuples()}


def table_bas_distribution():
    import pandas as pd
    r = _pyramide()
    ref = _smig_de_reference()
    return pd.DataFrame({
        _lab("c_annee"): [l["annee"] for l in r],
        _lab("c_mesure"): [_lab("m_annuelle") if l["trimestre"] is None
                           else _lab("m_trim").format(t=l["trimestre"]) for l in r],
        _lab("c_p_total"): [l["total"] for l in r],
        _lab("c_p_smig_ref"): [ref.get(l["annee"]) for l in r],
        _lab("c_p_inf1"): [round(l["inf1"], 1) for l in r],
        _lab("c_p_1_15"): [round(l["1_15"], 1) for l in r],
        _lab("c_p_sup15"): [round(l["sup15"], 1) for l in r],
    })


# Entreprises répondantes sans comptabilité, sur lesquelles portent les résultats de l'enquête
# auprès des micro-entreprises (rapport 2007, p. 8 ; 2012, p. 10 ; 2016, p. 9 du fichier PDF ;
# citations dans la colonne `champ` de la série).
_REPONDANTES_MICRO = {2007: 7144, 2012: 5572, 2016: 7179}
_REPONSE_EES = {2012: "38,6 %", 2014: "46,6 %", 2022: "58 %"}


def _enquete(enquete: str):
    """Lignes, colonnes et références paginées d'une des deux enquêtes de l'INS.

    Valeurs lues dans les séries ; entreprises répondantes et taux de réponse contrôlés sur les
    citations que les séries portent (colonnes `champ` et `taux_de_reponse`).
    """
    def pct(v, decimales=1):
        return f"{_fr(float(v), decimales)}\u00a0%"

    lignes, pages = [], {}

    def cite(cle, page):
        pages.setdefault(cle, set()).add(int(page))

    if enquete == "micro":
        m = figtools.series(SERIE_MICRO)
        m = m[(m["branche"] == "Ensemble") & (m["sexe"] == "ensemble") & (m["grandeur"] == "part")]
        for annee in (2007, 2012, 2016):
            cle = f"ins-micro-entreprises-{annee}"
            propre = m[m["source_id"] == cle]
            part = propre[(propre["annee"] == annee) & (propre["tranche"] == "<1")]
            # La moitié du SMIG : 2007 n'est imprimée que par le rapport 2012 (tableau 8).
            moitie = m[(m["annee"] == annee) & (m["tranche"] == "<0.5")]
            assert part["valeur"].nunique() == 1 and moitie["valeur"].nunique() == 1, annee
            assert str(_REPONDANTES_MICRO[annee]) in propre["champ"].iloc[0], annee
            cite(cle, part["page_pdf"].min())
            du_rapport = moitie[moitie["source_id"] == cle]
            autre = moitie.iloc[0] if du_rapport.empty else du_rapport.sort_values("page_pdf").iloc[0]
            cite(autre["source_id"], autre["page_pdf"])
            lignes.append((annee, pct(part["valeur"].iloc[0]), pct(moitie["valeur"].iloc[0]),
                           int(part["smig_retenu_par_la_source_D"].iloc[0]),
                           _fr(_REPONDANTES_MICRO[annee], 0)))
        cles = ("t_annee", "t_part_court", "t_moitie_court", "t_smig_court", "t_repondantes")
    else:
        e = figtools.series(SERIE_EES)
        e = e[(e["section"] == "Total") & (e["categorie"] == "Total")]
        for annee in (2012, 2014, 2022):
            g = e[e["annee"] == annee]
            niveau = g[~g["grandeur"].str.contains("pourcentage")]
            rapport = g[g["grandeur"].str.contains("pourcentage")]
            assert len(niveau) == 1 and len(rapport) == 1, annee
            assert _REPONSE_EES[annee].replace(" ", "") in g["taux_de_reponse"].iloc[0], annee
            cite(f"ins-ees-{annee}", niveau["page_pdf"].iloc[0])
            lignes.append((annee, _fr(float(niveau["valeur"].iloc[0]), 0),
                           pct(rapport["valeur"].iloc[0], 0),
                           int(niveau["smig_retenu_par_la_source_D"].iloc[0]),
                           _REPONSE_EES[annee]))
        cles = ("t_annee", "t_base_court", "t_base_pct", "t_smig_court", "t_taux")
    return lignes, cles, pages


def tableau_enquetes(enquete: str) -> str:
    """Tableau Markdown d'une des deux enquêtes de l'INS (`"micro"` ou `"ees"`), une ligne par
    année. Le champ se dit dans la légende, les références dans `sources_enquetes`."""
    lignes, cles, _ = _enquete(enquete)
    sortie = ["| " + " | ".join(_lab(c) for c in cles) + " |", "|:---|---:|---:|---:|---:|"]
    sortie += ["| " + " | ".join(str(c) for c in l) + " |" for l in lignes]
    return "\n".join(sortie)


def sources_enquetes(enquete: str) -> str:
    """La ligne « Source » d'un tableau d'enquête : chaque rapport cité une fois, avec ses pages."""
    _, _, pages = _enquete(enquete)
    refs = "; ".join(f"@{cle}, p. {', '.join(str(p) for p in sorted(pp))}"
                     for cle, pp in sorted(pages.items()))
    return f"::: {{.figure-source}}\n{_lab('t_source')} : [{refs}]\n:::"


# ---------------------------------------------------------------- quantiles approchés (CNSS)
#
# La CNSS ne publie aucun quantile : ceux-ci sont interpolés dans les classes de la pyramide en
# dinars (série dérivée de l'entrepôt). LES ÉDITIONS DE L'ANNUAIRE NE DONNENT PAS LA MÊME
# DISTRIBUTION POUR LA MÊME ANNÉE : la figure trace des SEGMENTS, sans raccord, chacun à mesure
# du salaire mensuel et à grille de classes constantes.
#   (édition, première année, dernière année, mesure)
#   « d12 » : même mesure que la pyramide en SMIG — salaire de l'année ÷ 12, années incomplètes
#   comprises (vérifié par l'entrepôt en 2013) ; « mois » : autre mesure (salaire rapporté aux
#   mois déclarés, vérifié en 2016).
_SEGMENTS_QUANTILES = ((2013, 2000, 2009, "d12"), (2013, 2011, 2013, "d12"),
                       (2018, 2010, 2016, "mois"), (2018, 2017, 2018, "d12"))
_QUANTILES = (("Q1", ORANGE), ("médiane", BLEU), ("Q3", VERT), ("D9", GRIS))


def _quantiles():
    """Une ligne par segment (ou population) et par année : quantiles courants et constants."""
    d = figtools.series(SERIE_QUANTILES)
    d = d[d["mesure"] == "annuelle"]
    ipc = _ipc()
    lignes = []

    def ligne(bloc, annee, edition, segment, mesure, population):
        v = {q: bloc.loc[bloc["quantile"] == q, "valeur_D"].iloc[0] for q, _ in _QUANTILES}
        v = {q: None if x != x else float(x) for q, x in v.items()}
        coef = ipc[ANNEE_BASE] / ipc[annee]
        return {"annee": annee, "edition": edition, "segment": segment, "mesure": mesure,
                "population": population, **v,
                **{f"{q}_reel": None if x is None else x * coef for q, x in v.items()}}

    tous = d[d["population"].str.contains("au titre")]
    for edition, debut, fin, mesure in _SEGMENTS_QUANTILES:
        e = tous[tous["source_id"] == f"cnss-annuaire-{edition}"]
        for annee in range(debut, fin + 1):
            bloc = e[e["annee"] == annee]
            # La mesure du segment est celle que l'entrepôt constate sur chaque colonne.
            assert (bloc["coherent_avec_pyramide_smig"] == ("oui" if mesure == "d12" else "non")).all()
            lignes.append(ligne(bloc, annee, edition, f"{debut}-{fin}", mesure, "tous"))
    q4 = d[d["population"].str.contains("quatre trimestres")]
    lignes.append(ligne(q4, 2013, 2013, "2013", "d12", "4t"))
    return lignes


def fig_quantiles():
    from matplotlib.lines import Line2D
    figtools.apply_lang_font()
    ft = figtools.fig_text
    r = _quantiles()
    fig, ax = plt.subplots(figsize=(10, 6))
    styles = {"d12": dict(ls="-", marker="o", ms=3), "mois": dict(ls=(0, (5, 2)), marker="s", ms=3)}
    for *segment, mesure in _SEGMENTS_QUANTILES:
        for q, couleur in _QUANTILES:
            pts = [(l["annee"], l[f"{q}_reel"]) for l in r
                   if l["population"] == "tous" and (l["edition"], l["segment"]) ==
                   (segment[0], f"{segment[1]}-{segment[2]}") and l[f"{q}_reel"] is not None]
            if pts:
                ax.plot([a for a, _ in pts], [v for _, v in pts], color=couleur, lw=1.7,
                        **styles[mesure])
    q4 = next(l for l in r if l["population"] == "4t")
    for q, couleur in _QUANTILES:
        if q4[f"{q}_reel"] is not None:
            ax.plot([2013], [q4[f"{q}_reel"]], ls="none", marker="D", ms=6.5, mfc="white",
                    mec=couleur, mew=1.6, zorder=5)
    poignees = [Line2D([], [], color=c, lw=2, label=ft(_lab(f"q_{q}"))) for q, c in _QUANTILES]
    poignees += [Line2D([], [], color="black", lw=1.4, label=ft(_lab("q_d12")), **styles["d12"]),
                 Line2D([], [], color="black", lw=1.4, label=ft(_lab("q_mois")), **styles["mois"]),
                 Line2D([], [], ls="none", marker="D", ms=6.5, mfc="white", mec="black", mew=1.4,
                        label=ft(_lab("q_4t")))]
    ax.set_ylim(0, None)
    ax.set_xlim(1999.3, 2018.7)
    ax.set_xticks(range(2000, 2019))
    ax.tick_params(axis="x", labelsize=8)
    ax.set_xlabel(ft(_lab("x_annee")))
    ax.set_ylabel(ft(_lab("y_reel")))
    ax.grid(True, alpha=0.3)
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=8,
              frameon=False, ncol=2)
    fig.tight_layout()
    return fig


def vues_quantiles():
    return fig_quantiles()


def table_quantiles():
    import pandas as pd
    r = _quantiles()
    colonnes = {
        _lab("c_annee"): [l["annee"] for l in r],
        _lab("c_q_ed"): [l["edition"] for l in r],
        _lab("c_q_seg"): [l["segment"] for l in r],
        _lab("c_q_mesure"): [_lab(f"m_{l['mesure']}") for l in r],
        _lab("c_q_pop"): [_lab(f"pop_{'4t' if l['population'] == '4t' else 'tous'}") for l in r],
    }
    for q, _ in _QUANTILES:
        colonnes[_lab("c_q_courant").format(q=_lab(f"q_{q}"))] = [_arr(l[q]) for l in r]
    for q, _ in _QUANTILES:
        colonnes[_lab("c_q_reel").format(q=_lab(f"q_{q}"), a=ANNEE_BASE)] = [
            _arr(l[f"{q}_reel"]) for l in r]
    return pd.DataFrame(colonnes)


def _interquantiles():
    """Par segment : les trois rapports interquantiles à sa première et à sa dernière année."""
    r = [l for l in _quantiles() if l["population"] == "tous"]
    lignes = []
    for edition, debut, fin, mesure in _SEGMENTS_QUANTILES:
        seg = {l["annee"]: l for l in r if (l["edition"], l["segment"]) == (edition, f"{debut}-{fin}")}

        def rapport(annee, haut, bas):
            h, b = seg[annee][haut], seg[annee][bas]
            return None if h is None or b is None else h / b
        lignes.append({"debut": debut, "fin": fin, "edition": edition, "mesure": mesure,
                       **{f"{nom}_{quand}": rapport(annee, haut, bas)
                          for nom, haut, bas in (("q3q1", "Q3", "Q1"), ("mq1", "médiane", "Q1"),
                                                 ("d9m", "D9", "médiane"))
                          for quand, annee in (("debut", debut), ("fin", fin))}})
    return lignes


def tableau_interquantiles() -> str:
    """Tableau Markdown des rapports interquantiles, un segment par ligne."""
    def f(v):
        return "—" if v is None else _fr(v, 2)
    entetes = [_lab("ti_annees"), _lab("ti_ed"), _lab("ti_mesure")]
    for nom in ("q3q1", "mq1", "d9m"):
        entetes += [_lab("ti_debut").format(r=_lab(f"ti_{nom}")),
                    _lab("ti_fin").format(r=_lab(f"ti_{nom}"))]
    sortie = ["| " + " | ".join(entetes) + " |", "|:---|:---|:---|---:|---:|---:|---:|---:|---:|"]
    for l in _interquantiles():
        sortie.append("| " + " | ".join(
            [f"{l['debut']}-{l['fin']}", str(l["edition"]), _lab(f"m_{l['mesure']}")]
            + [f(l[f"{nom}_{quand}"]) for nom in ("q3q1", "mq1", "d9m")
               for quand in ("debut", "fin")]) + " |")
    return "\n".join(sortie)


def _deux_populations_2013():
    """2013 : tous les salariés déclarés et ceux qui le sont les quatre trimestres."""
    t = _trimestres_2013("dinars")
    quant = {l["population"]: l for l in _quantiles() if l["annee"] == 2013 and l["edition"] == 2013}
    annuel_tous = next(l["annuel"] for l in _salaire_declare()
                       if l["annee"] == 2013 and l["edition"] == 2018)
    lignes = []
    for colonne, pop, annuel in (("total", "tous", annuel_tous),
                                 ("4", "4t", _quatre_trimestres()["annuel"])):
        c = t[t["trimestres_declares"] == colonne]
        total = int(c.loc[c["classe"] == "TOTAL", "salaries_declares"].iloc[0])
        classes = c[c["classe"] != "TOTAL"]
        sous_300 = classes.loc[classes["borne_sup"].astype(float) <= 300, "salaries_declares"].sum()
        de_300_330 = classes.loc[classes["borne_inf"].astype(float) == 300, "salaries_declares"]
        assert len(de_300_330) == 1 and float(classes.loc[de_300_330.index[0], "borne_sup"]) == 330
        lignes.append({"pop": pop, "salaries": total, "annuel": annuel,
                       "q1": quant[pop]["Q1"], "mediane": quant[pop]["médiane"],
                       "q3": quant[pop]["Q3"], "sous_300": 100 * sous_300 / total,
                       "de_300_330": 100 * int(de_300_330.iloc[0]) / total})
    return lignes


def tableau_2013() -> str:
    """Tableau Markdown des deux populations de 2013 : une grandeur par ligne, et pour chaque
    population le montant en dinars de 2013 et en dinars de l'année de base."""
    ens, qt = _deux_populations_2013()
    ipc = _ipc()
    coef = ipc[ANNEE_BASE] / ipc[2013]
    entetes = ["t13_grandeur", "t13_ens", "t13_ens_reel", "t13_4t", "t13_4t_reel"]
    def nom(cle):
        """Nom de la grandeur d'un seul tenant, unité entre parenthèses à la ligne."""
        haut, _, bas = _lab(cle).partition("<br>")
        return f"[{haut}]{{.insecable}}" + (f"<br>{bas}" if bas else "")

    # Les tirets fixent les largeurs relatives : la colonne des noms est la plus large.
    sortie = ["| " + " | ".join(nom(c) for c in entetes) + " |",
              "|:----------|------:|------:|------:|------:|"]

    def ligne(cle, a, b, decimales, reel=True):
        def f(v, k=1.0):
            return _fr(v * k, decimales)
        sortie.append("| " + " | ".join([
            nom(cle), f(a), f(a, coef) if reel else "—", f(b), f(b, coef) if reel else "—"]) + " |")

    ligne("t13_n", ens["salaries"], qt["salaries"], 0, reel=False)
    ligne("t13_moy", ens["annuel"], qt["annuel"], 0)
    ligne("t13_q1", ens["q1"], qt["q1"], 0)
    ligne("t13_med", ens["mediane"], qt["mediane"], 0)
    ligne("t13_q3", ens["q3"], qt["q3"], 0)
    for cle, k in (("t13_300", "sous_300"), ("t13_330", "de_300_330")):
        sortie.append("| " + " | ".join([nom(cle), f"{_fr(ens[k])} %", "—", f"{_fr(qt[k])} %", "—"]) + " |")
    return "\n".join(sortie)


# ---------------------------------------------------------------- contrôle des chiffres du texte

def controle_texte() -> None:
    """Chaque chiffre que la section écrit en clair est recalculé ici depuis les séries.

    Appelé au rendu de la première figure de la section : si un snapshot change, le rendu
    s'arrête sur l'écart au lieu de laisser le texte dire autre chose que la figure.
    """
    def egal(obtenu, attendu, d=0):
        assert obtenu is not None and round(obtenu, d) == attendu, (obtenu, attendu)

    an = {l["annee"]: l for l in _par_annee()}
    q = _quatre_trimestres()
    # Salaire annuel moyen de 2013, deux populations.
    egal(an[2013]["a2018"], 8495)
    egal(q["annuel"], 11036)
    assert q["salaries"] == 800_558
    # Dinars de 2024 : salaire mensuel moyen déclaré et SMIG.
    for annee, cle, attendu in ((1970, "r2006", 609), (1980, "r2006", 933), (1988, "r2006", 903),
                                (1999, "r2006", 1040), (2004, "r2018", 1031), (2018, "r2018", 1457),
                                (1970, "smig_reel", 347), (1980, "smig_reel", 582),
                                (1988, "smig_reel", 609), (1999, "smig_reel", 578),
                                (2004, "smig_reel", 608), (2018, "smig_reel", 561)):
        egal(an[annee][cle], attendu)
    # Pouvoir d'achat, indices rapportés aux prix.
    for annee, cle, attendu in ((2016, "pa_smig", 100), (2024, "pa_smig", 81),
                                (2017, "pa_salaire", 129), (2024, "pa_salaire", 116),
                                (2018, "pa_salaire", 127), (2018, "pa_cnss", 153),
                                (2004, "pa_cnss", 109)):
        egal(an[annee][cle], attendu)
    assert max(l["pa_salaire"] for l in an.values() if l["pa_salaire"]) == an[2017]["pa_salaire"]
    # Le SMIG en % du salaire moyen déclaré.
    for annee, cle, attendu in ((1970, "ss2006", 57.0), (1973, "ss2006", 48.6),
                                (1974, "ss2006", 64.9), (1980, "ss2006", 62.3),
                                (1982, "ss2006", 90.9), (1986, "ss2006", 82.0),
                                (1987, "ss2006", 84.4), (1988, "ss2006", 67.4),
                                (2002, "ss2006", 52.8), (2002, "ss2018", 61.9),
                                (2006, "ss2006", 55.5), (2006, "ss2018", 55.2),
                                (2004, "ss2018", 59.0), (2018, "ss2018", 38.5),
                                (2013, "ss4t", 32.8)):
        egal(an[annee][cle], attendu, 1)
    # 2013 : les deux populations.
    tous, quatre = _deux_populations_2013()
    assert (tous["pop"], quatre["pop"]) == ("tous", "4t") and quatre["salaries"] == 800_558
    for obtenu, attendu in ((quatre["sous_300"], 6.6), (quatre["de_300_330"], 5.2),
                            (tous["q1"], 260.9), (quatre["q1"], 427.1),
                            (tous["mediane"], 468.1), (quatre["mediane"], 590.2)):
        egal(obtenu, attendu, 1)
    egal(an[2013]["smig"], 301.808, 3)
    assert 300 <= an[2013]["smig"] < 330
    egal(_smig_de_reference()[2013], 290.2, 3)
    # Pyramide en SMIG de référence.
    p = {(l["annee"], l["trimestre"]): l for l in _pyramide()}
    for cle, nom, attendu in (((2000, None), "inf1", 40.8), ((2018, None), "inf1", 24.0),
                              ((2018, 1), "inf1", 9.5), ((2000, None), "sup15", 34.4),
                              ((2018, None), "sup15", 58.2)):
        egal(p[cle][nom], attendu, 1)
    # Rapports interquantiles et médianes de 2013 selon l'édition.
    seg = {(l["debut"], l["fin"]): l for l in _interquantiles()}
    for cle, nom, attendu in (((2000, 2009), "q3q1_debut", 3.00), ((2000, 2009), "q3q1_fin", 3.12),
                              ((2000, 2009), "d9m_debut", 2.90), ((2000, 2009), "d9m_fin", 3.29),
                              ((2010, 2016), "q3q1_debut", 2.22), ((2010, 2016), "q3q1_fin", 2.47),
                              ((2010, 2016), "mq1_debut", 1.43), ((2010, 2016), "mq1_fin", 1.48)):
        egal(seg[cle][nom], attendu, 2)
    med = {l["edition"]: l["médiane"] for l in _quantiles()
           if l["annee"] == 2013 and l["population"] == "tous"}
    egal(med[2013], 468.1, 1)
    egal(med[2018], 502.1, 1)
    # Enquêtes de l'INS.
    micro, ees = _enquete("micro")[0], _enquete("ees")[0]
    assert [l[1].replace(" ", " ") for l in micro] == ["54,5 %", "49,9 %", "32,3 %"]
    assert [l[2].replace(" ", " ") for l in ees] == ["178 %", "188 %", "201 %"]

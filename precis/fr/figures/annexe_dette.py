"""Figures de l'annexe du site « La dette publique et son périmètre » (`precis/fr/annexe-dette-publique.qmd`).

    from figures import annexe_dette
    annexe_dette.vues_echeancier()   # deux vues de `fig-dette-echeancier` : service par année, encours
    annexe_dette.table_echeancier()  # ses données téléchargeables

MODULE DE FIGURE D'UNE PAGE DE SITE, et non d'un livre : il vit dans `precis/fr/figures/`,
à côté de la page ; la page arabe le trouve par le lien symbolique `precis/ar/figures`.

DONNÉES (lues par `figtools.series()`, jamais une source vive).
  - `dette-exterieure-echeancier` : dette extérieure publique et garantie (PPG), encours et service
    (principal + intérêts) par année, réalisé puis projeté, en millions de dollars courants. Source
    Banque mondiale, International Debt Statistics (entrepôt tunisia-data).

RÈGLES (voir docs/notes/annexe-dette-publique.md, docs/notes/dette-pret-par-pret.md).
  - **L'échéancier est celui de la dette DÉJÀ CONTRACTÉE** : les années projetées décroissent faute
    d'inclure les emprunts futurs ; on les distingue visuellement du réalisé, et on ne les lit pas
    comme une prévision du service total à venir.
  - **Périmètre PPG extérieur, en dollars** : ni la dette intérieure en dinars, ni une conversion en
    dinars. L'encours extérieur se réévalue avec le change.
  - **Aucun nombre n'est écrit en dur ici** : tout est lu dans la série.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
sys.path.insert(0, "../../scripts")
import figtools  # noqa: E402
import matplotlib.ticker as _mtick  # noqa: E402


def _axe_annees(ax):
    """Force des années ENTIÈRES sur l'axe des abscisses (pas de .0 ni de demi-années)."""
    ax.xaxis.set_major_locator(_mtick.MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(_mtick.FuncFormatter(lambda v, _p: f"{int(round(v))}"))



SERIE = "dette-exterieure-echeancier"
SERIE_CREANCIERS = "dette-exterieure-echeancier-creanciers"
FENETRE_CREANCIERS = 2016  # première année affichée du mur d'échéances par créancier
N_CREANCIERS = 8          # créanciers nommés ; le reste est regroupé en « autres »

# Libellés français des principaux créanciers (affichage ; la donnée garde le nom d'origine).
_CREANCIERS_FR = {
    "Bondholders": "porteurs d'obligations",
    "African Dev. Bank": "Banque africaine de dév.",
    "African Export-Import Bank": "Afreximbank",
    "World Bank-IBRD": "Banque mondiale (BIRD)",
    "European Investment Bank": "Banque européenne d'inv.",
    "Islamic Dev. Bank": "Banque islamique de dév.",
    "Arab Fund for Economic & Social Development": "Fonds arabe (FADES)",
    "European Bank for Reconstruction and Dev. (EBRD)": "BERD",
    "Arab Monetary Fund": "Fonds monétaire arabe",
    "France": "France", "Germany, Fed. Rep. of": "Allemagne", "Japan": "Japon",
    "Saudi Arabia": "Arabie saoudite", "Italy": "Italie", "Spain": "Espagne",
}

C_PRINCIPAL = "#c0392b"
C_INTERETS = "#e08214"
C_ENCOURS = "#1f4e79"

# --- i18n minimal ------------------------------------------------------------
_L = {
    "y_musd":     {"fr": "millions de dollars",          "ar": "مليون دولار"},
    "x_annee":    {"fr": "année",                        "ar": "السنة"},
    "l_principal":{"fr": "principal",                    "ar": "رأس المال"},
    "l_interets": {"fr": "intérêts",                     "ar": "الفوائد"},
    "l_projete":  {"fr": "projeté (dette déjà contractée)", "ar": "متوقّع (دين متعاقد عليه)"},
    "l_encours":  {"fr": "encours",                      "ar": "الأصل القائم"},
    "v_service":  {"fr": "service par année (principal + intérêts)", "ar": "خدمة الدين سنويًا (رأس المال + الفوائد)"},
    "v_encours":  {"fr": "encours de fin d'année",       "ar": "الأصل القائم في آخر السنة"},
}


def _lab(key: str) -> str:
    return _L[key].get(figtools.lang(), _L[key]["fr"])


def _ft(key: str) -> str:
    return figtools.fig_text(_lab(key))


def _data() -> pd.DataFrame:
    d = figtools.series(SERIE).copy()
    d["annee"] = d["annee"].astype(int)
    return d.sort_values("annee")


# --- figure : service par année (barres empilées), réalisé puis projeté ------
def _trace_service(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    reel = df[df["statut"] == "réalisé"]
    proj = df[df["statut"] == "projeté"]
    # Réalisé : barres pleines, principal + intérêts empilés.
    ax.bar(reel["annee"], reel["principal_MUSD"], color=C_PRINCIPAL, label=_ft("l_principal"))
    ax.bar(reel["annee"], reel["interets_MUSD"], bottom=reel["principal_MUSD"],
           color=C_INTERETS, label=_ft("l_interets"))
    # Projeté : mêmes couleurs, hachuré et translucide, pour ne pas le lire comme du réalisé.
    ax.bar(proj["annee"], proj["principal_MUSD"], color=C_PRINCIPAL, alpha=0.45, hatch="//")
    ax.bar(proj["annee"], proj["interets_MUSD"], bottom=proj["principal_MUSD"],
           color=C_INTERETS, alpha=0.45, hatch="//")
    if not proj.empty:
        ax.axvline(proj["annee"].min() - 0.5, color="grey", ls=":", lw=1)
        ax.text(proj["annee"].min(), ax.get_ylim()[1] * 0.96, _ft("l_projete"),
                fontsize=8, color="grey", va="top")
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_musd"))
    ax.grid(alpha=0.25, axis="y")
    ax.legend(fontsize=9, loc="upper left")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


# --- figure : encours de fin d'année (réalisé seul) --------------------------
def _trace_encours(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    d = df.dropna(subset=["encours_MUSD"])
    ax.plot(d["annee"], d["encours_MUSD"], color=C_ENCOURS, lw=1.8, label=_ft("l_encours"))
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_musd"))
    ax.grid(alpha=0.25)
    ax.legend(fontsize=9, loc="upper left")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def vues_echeancier():
    df = _data()
    return [
        (_lab("v_service"), _trace_service(df)),
        (_lab("v_encours"), _trace_encours(df)),
    ]


_L["l_r_ext"] = {"fr": "coût apparent de la dette extérieure", "ar": "الكلفة الظاهرية للدين الخارجي"}


def fig_cout_exterieur():
    """Coût apparent de la dette extérieure PPG : intérêts de l'année / encours de l'année précédente."""
    d = _data().copy()
    d["enc_prec"] = d["encours_MUSD"].shift(1)
    d["r_ext"] = d["interets_MUSD"] / d["enc_prec"] * 100
    d = d.dropna(subset=["r_ext"])
    d = d[d["statut"] == "réalisé"]
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    ax.plot(d["annee"], d["r_ext"], color=C_PRINCIPAL, lw=1.8, label=_ft("l_r_ext"))
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(figtools.fig_text("% par an"))
    ax.grid(alpha=0.25)
    ax.legend(fontsize=9, loc="upper right")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def table_cout_exterieur() -> pd.DataFrame:
    d = _data().copy()
    d["enc_prec"] = d["encours_MUSD"].shift(1)
    d["cout_apparent_pct"] = (d["interets_MUSD"] / d["enc_prec"] * 100)
    d = d[d["statut"] == "réalisé"].dropna(subset=["cout_apparent_pct"])
    return d[["annee", "interets_MUSD", "encours_MUSD", "cout_apparent_pct"]].round(2)


# --- structure de la dette extérieure : devises et effet-change (BCT) -----------
SERIE_DEVISES = "dette-exterieure-devises"
SERIE_DEVISES_RA = "dette-exterieure-devises-ra"   # approximation 2015/2017/2018 (Rapport annuel)
SERIE_FX = "dette-exterieure-effet-change"
_DEVISES = [("eur_pct", "#1f4e79", {"fr": "euro", "ar": "اليورو"}),
            ("usd_pct", "#1a9850", {"fr": "dollar É.-U.", "ar": "الدولار"}),
            ("yen_pct", "#e08214", {"fr": "yen", "ar": "الين"}),
            ("kwd_pct", "#8073ac", {"fr": "dinar koweïtien", "ar": "الدينار الكويتي"}),
            ("autres_pct", "#b0b0b0", {"fr": "autres", "ar": "أخرى"})]
_L["y_part_dette"] = {"fr": "part de l'encours, en %", "ar": "الحصّة، ٪"}
_L["l_estimation_ra"] = {"fr": "estimation (Rapport annuel, 3 devises)",
                        "ar": "تقدير (التقرير السنوي، ثلاث عملات)"}
_L["l_effet_change"] = {"fr": "effet de change", "ar": "أثر الصرف"}
_L["l_effet_volume"] = {"fr": "effet de volume (emprunt net)", "ar": "أثر الحجم"}
_L["l_variation_enc"] = {"fr": "variation de l'encours", "ar": "تغيّر الأصل القائم"}
_L["y_mdt"] = {"fr": "millions de dinars", "ar": "مليون دينار"}


def fig_devises():
    d = figtools.series(SERIE_DEVISES).copy()
    d["annee"] = d["annee"].astype(int)
    d = d.sort_values("annee")
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    bas = pd.Series(0.0, index=d.index)
    for col, couleur, lab in _DEVISES:
        ax.bar(d["annee"], d[col], bottom=bas, color=couleur,
               label=figtools.fig_text(lab.get(figtools.lang(), lab["fr"])))
        bas = bas + d[col]
    # Approximation 2015/2017/2018 (Rapport annuel, 3 devises + reliquat), en barres HACHURÉES :
    # le kwd n'est pas isolé (fondu dans 'autres'), d'où l'absence de la colonne kwd_pct.
    ra = figtools.series(SERIE_DEVISES_RA).copy()
    ra["annee"] = ra["annee"].astype(int)
    ra = ra.sort_values("annee")
    basr = pd.Series(0.0, index=ra.index)
    for col, couleur, lab in _DEVISES:
        if col not in ra.columns:
            continue
        ax.bar(ra["annee"], ra[col], bottom=basr, color=couleur,
               hatch="////", alpha=0.6, edgecolor="white", linewidth=0.4)
        basr = basr + ra[col]
    ax.bar([], [], color="0.82", hatch="////", edgecolor="white",
           label=figtools.fig_text(_ft("l_estimation_ra")))
    ax.set_xticks(sorted(set(d["annee"]).union(ra["annee"])))
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_part_dette"))
    ax.set_ylim(0, 100)
    ax.legend(fontsize=7.5, ncol=3, loc="lower center")
    ax.grid(alpha=0.25, axis="y")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def table_devises() -> pd.DataFrame:
    return figtools.series(SERIE_DEVISES).round(1)


def fig_effet_change():
    d = figtools.series(SERIE_FX).copy()
    d["annee"] = d["annee"].astype(int)
    d = d.sort_values("annee")
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    ec, ev = d["effet_change_MDT"], d["effet_volume_MDT"]
    # Empilement séparé côté positif et négatif (effet-change et effet-volume peuvent être de signes
    # opposés une même année) ; les points noirs donnent la variation totale = somme des deux.
    pos = pd.Series(0.0, index=d.index)
    neg = pd.Series(0.0, index=d.index)
    for serie, couleur, cle in [(ec, "#e08214", "l_effet_change"),
                                (ev, "#1f4e79", "l_effet_volume")]:
        b = [pos[i] if serie[i] >= 0 else neg[i] for i in d.index]
        ax.bar(d["annee"], serie, bottom=b, color=couleur, label=_ft(cle))
        for i in d.index:
            if serie[i] >= 0:
                pos[i] += serie[i]
            else:
                neg[i] += serie[i]
    ax.plot(d["annee"], d["variation_MDT"], color="black", lw=0, marker="o", ms=5,
            label=_ft("l_variation_enc"))
    ax.axhline(0, color="black", lw=0.8)
    ax.set_xticks(d["annee"])
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_mdt"))
    ax.legend(fontsize=9, loc="best")
    ax.grid(alpha=0.25, axis="y")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def table_effet_change() -> pd.DataFrame:
    return figtools.series(SERIE_FX).round(1)


# --- valeur du dinar : prix intérieurs et taux de change (effet différencié sur la dette) --
SERIE_CHANGE = "change-dinar"
SERIE_IPC = "ipc-longue-periode"
ANNEE_BASE_DINAR = 2000
_L["l_prix"] = {"fr": "niveau des prix intérieurs", "ar": "مستوى الأسعار الداخلية"}
_L["l_change"] = {"fr": "taux de change (dinars par dollar)", "ar": "سعر الصرف (دينار/دولار)"}
_L["y_indice"] = {"fr": "indice, base 100 en {a}", "ar": "مؤشر، الأساس 100 سنة {a}"}


def _ipc_long() -> pd.DataFrame:
    """IPC long (base 1970) prolongé jusqu'en 2025 par l'IPC base 2015, raccordé à l'année commune."""
    ipc = figtools.series(SERIE_IPC)[["annee", "indice_base1970"]].dropna().copy()
    ipc["annee"] = ipc["annee"].astype(int)
    ipc = ipc.sort_values("annee")
    b15 = figtools.series("bct-ipc-base2015")[["annee", "valeur"]].dropna().copy()
    b15["annee"] = b15["annee"].astype(int)
    pivot = int(ipc["annee"].max())                      # dernier point du long (2023)
    b15_pivot = float(b15.loc[b15.annee == pivot, "valeur"].iloc[0])
    ipc_pivot = float(ipc.loc[ipc.annee == pivot, "indice_base1970"].iloc[0])
    sup = b15[b15.annee > pivot].copy()
    sup["indice_base1970"] = sup["valeur"] / b15_pivot * ipc_pivot   # chaîne la croissance de l'IPC
    return pd.concat([ipc, sup[["annee", "indice_base1970"]]], ignore_index=True).sort_values("annee")


def fig_valeur_dinar():
    """Double perte de valeur du dinar : prix intérieurs (IPC) et change, indexés à une base commune."""
    ipc = _ipc_long()
    ipc["annee"] = ipc["annee"].astype(int)
    chg = figtools.series(SERIE_CHANGE)[["annee", "dinar_par_usd"]].dropna().copy()
    chg["annee"] = chg["annee"].astype(int)
    b = ANNEE_BASE_DINAR
    ipc_b = float(ipc.loc[ipc.annee == b, "indice_base1970"].iloc[0])
    chg_b = float(chg.loc[chg.annee == b, "dinar_par_usd"].iloc[0])
    ipc["idx"] = ipc["indice_base1970"] / ipc_b * 100
    chg["idx"] = chg["dinar_par_usd"] / chg_b * 100
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    ax.plot(ipc["annee"], ipc["idx"], color="#1f4e79", lw=1.8, label=_ft("l_prix"))
    ax.plot(chg["annee"], chg["idx"], color="#c0392b", lw=1.8, label=_ft("l_change"))
    ax.axhline(100, color="grey", ls=":", lw=1)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(figtools.fig_text(_lab("y_indice").format(a=b)))
    ax.grid(alpha=0.25)
    ax.legend(fontsize=9, loc="upper left")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


# --- effet de l'inflation sur la dette/PIB : les deux canaux -------------------
_L["l_canal_dil"] = {"fr": "dilution par l'inflation (dette en dinars)", "ar": "التخفيف بالتضخم"}
_L["l_canal_fx"] = {"fr": "réévaluation de la dette extérieure (change)", "ar": "إعادة تقييم الدين الخارجي"}
_L["l_net_infl"] = {"fr": "effet net sur le ratio", "ar": "الأثر الصافي"}


def _canaux() -> pd.DataFrame:
    fp = _fp()[["annee", "dette_pct_pib", "pib_MDT"]].copy()
    ipc = _ipc_long().copy()
    ipc["infl"] = ipc["indice_base1970"].pct_change() * 100
    fx = figtools.series("dette-exterieure-effet-change")[["annee", "effet_change_MDT"]].copy()
    fx["annee"] = fx["annee"].astype(int)
    d = fp.merge(ipc[["annee", "infl"]], on="annee", how="left").merge(fx, on="annee", how="left")
    d = d.sort_values("annee").reset_index(drop=True)
    d["g_nom"] = d["pib_MDT"].pct_change() * 100
    b1 = d["dette_pct_pib"].shift(1)
    d["canal_dilution"] = -b1 * (d["infl"] / 100) / (1 + d["g_nom"] / 100)   # favorable (<0)
    d["canal_reeval"] = d["effet_change_MDT"] / d["pib_MDT"] * 100            # défavorable si >0
    return d


def fig_inflation_canaux(annee_min=2001):
    d = _canaux()
    d = d[d["annee"] >= annee_min]
    fig, ax = plt.subplots(figsize=(9.8, 5.2))
    ax.bar(d["annee"], d["canal_dilution"], color="#1a9850", label=_ft("l_canal_dil"))
    r = d.dropna(subset=["canal_reeval"])
    ax.bar(r["annee"], r["canal_reeval"], color="#e08214", label=_ft("l_canal_fx"))
    net = d.dropna(subset=["canal_reeval"]).copy()
    net["net"] = net["canal_dilution"] + net["canal_reeval"]
    ax.plot(net["annee"], net["net"], color="black", lw=0, marker="o", ms=4, label=_ft("l_net_infl"))
    ax.axhline(0, color="black", lw=0.8)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_pp"))
    ax.grid(alpha=0.25, axis="y")
    ax.legend(fontsize=8.5, loc="lower left")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def table_inflation_canaux() -> pd.DataFrame:
    d = _canaux()
    d = d[d["annee"] >= 2001][["annee", "infl", "canal_dilution", "canal_reeval"]].copy()
    return d.round(2)


def table_valeur_dinar() -> pd.DataFrame:
    ipc = _ipc_long()
    chg = figtools.series(SERIE_CHANGE)[["annee", "dinar_par_usd"]].dropna().copy()
    chg["annee"] = chg["annee"].astype(int)
    d = ipc.merge(chg, on="annee", how="inner")
    return d.sort_values("annee").round(2)


# --- dette publique : part intérieure et extérieure (BCT RA, périmètre budgétaire MdF) --
SERIE_ETAT_IE = "dette-publique-interieur-exterieur"
ANNEE_MAX_DETTE_IE = 2025  # on écarte la prévision de loi de finances (2026)
_L["l_etat_int"] = {"fr": "dette intérieure", "ar": "الدين الداخلي"}
_L["l_etat_ext"] = {"fr": "dette extérieure", "ar": "الدين الخارجي"}


_L["v_niveaux"] = {"fr": "niveaux (millions de dinars)", "ar": "المستويات (مليون دينار)"}
_L["v_parts"] = {"fr": "parts (% du total)", "ar": "الحصص (٪ من الجملة)"}


def _etat_ie() -> pd.DataFrame:
    d = figtools.series(SERIE_ETAT_IE).copy()
    d = d.rename(columns={"interieur_MDT": "etat_interieur_MDT",
                          "exterieur_MDT": "etat_exterieur_MDT",
                          "total_MDT": "etat_total_MDT"})
    d["annee"] = d["annee"].astype(int)
    d = d[d["annee"] <= ANNEE_MAX_DETTE_IE].sort_values("annee")
    d["int_pct"] = d["etat_interieur_MDT"] / d["etat_total_MDT"] * 100
    d["ext_pct"] = d["etat_exterieur_MDT"] / d["etat_total_MDT"] * 100
    return d


def _trace_etat_niveaux(d: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    ax.bar(d["annee"], d["etat_interieur_MDT"], color="#1f4e79", label=_ft("l_etat_int"))
    ax.bar(d["annee"], d["etat_exterieur_MDT"], bottom=d["etat_interieur_MDT"],
           color="#c0392b", label=_ft("l_etat_ext"))
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_mdt"))
    ax.grid(alpha=0.25, axis="y")
    ax.legend(fontsize=9, loc="upper left")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def _trace_etat_parts(d: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    ax.bar(d["annee"], d["int_pct"], color="#1f4e79", label=_ft("l_etat_int"))
    ax.bar(d["annee"], d["ext_pct"], bottom=d["int_pct"], color="#c0392b", label=_ft("l_etat_ext"))
    ax.axhline(50, color="black", ls=":", lw=1)
    ax.set_ylim(0, 100)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(figtools.fig_text("% du total"))
    ax.legend(fontsize=9, loc="lower center", ncol=2)
    ax.grid(alpha=0.25, axis="y")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def vues_dette_interieure():
    d = _etat_ie()
    return [(_lab("v_niveaux"), _trace_etat_niveaux(d)),
            (_lab("v_parts"), _trace_etat_parts(d))]


def table_dette_interieure() -> pd.DataFrame:
    d = _etat_ie()[["annee", "etat_interieur_MDT", "etat_exterieur_MDT",
                    "etat_total_MDT", "int_pct", "ext_pct"]].copy()
    return d.round({"etat_interieur_MDT": 0, "etat_exterieur_MDT": 0, "etat_total_MDT": 0,
                    "int_pct": 1, "ext_pct": 1})


# --- garanties de l'État : encours de dette garantie (intérieur / extérieur) -----
SERIE_GARANTIES = "garanties-etat"
_L["l_g_interieur"] = {"fr": "garanti intérieur", "ar": "مضمون داخلي"}
_L["l_g_exterieur"] = {"fr": "garanti extérieur", "ar": "مضمون خارجي"}


def fig_garanties_encours():
    """Encours de dette garantie par l'État, intérieur + extérieur, en stock de fin d'année."""
    d = figtools.series(SERIE_GARANTIES)
    d = d[(d["grandeur"].isin(["encours_interieur", "encours_exterieur"]))
          & (d["portee"] == "année")].copy()
    d["annee"] = d["annee"].astype(int)
    d = d.drop_duplicates(["grandeur", "annee"])
    piv = d.pivot_table(index="annee", columns="grandeur", values="valeur").sort_index()
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    ax.bar(piv.index, piv["encours_interieur"], color="#1f4e79", label=_ft("l_g_interieur"))
    ax.bar(piv.index, piv["encours_exterieur"], bottom=piv["encours_interieur"],
           color="#c0392b", label=_ft("l_g_exterieur"))
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_mdt"))
    ax.grid(alpha=0.25, axis="y")
    ax.legend(fontsize=9, loc="upper left")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def table_garanties_encours() -> pd.DataFrame:
    d = figtools.series(SERIE_GARANTIES)
    d = d[(d["grandeur"].isin(["encours_interieur", "encours_exterieur", "encours_total"]))
          & (d["portee"] == "année")].copy()
    d["annee"] = d["annee"].astype(int)
    d = d.drop_duplicates(["grandeur", "annee"])
    return d.pivot_table(index="annee", columns="grandeur", values="valeur").round(1).reset_index()


# --- liquidité externe : réserves et service/exportations (BCT via IMF/BM) ------
SERIE_LIQ = "liquidite-externe"
_L["y_mois_imp"] = {"fr": "mois d'importation", "ar": "أشهر توريد"}
_L["y_pct_exp"] = {"fr": "en % des exportations", "ar": "٪ من الصادرات"}
_L["l_reserves"] = {"fr": "réserves de change", "ar": "احتياطي الصرف"}
_L["l_service_exp"] = {"fr": "service de la dette / exportations", "ar": "خدمة الدين / الصادرات"}
_L["v_reserves"] = {"fr": "réserves de change", "ar": "احتياطي الصرف"}
_L["v_service_exp"] = {"fr": "service de la dette / exportations", "ar": "خدمة الدين / الصادرات"}


def _liq(code: str) -> pd.DataFrame:
    d = figtools.series(SERIE_LIQ)
    d = d[d["code"] == code][["annee", "valeur"]].copy()
    d["annee"] = d["annee"].astype(int)
    return d.sort_values("annee")


def _trace_liq(code: str, couleur: str, ylabel: str, lab: str, seuil=None):
    d = _liq(code)
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    ax.plot(d["annee"], d["valeur"], color=couleur, lw=1.8, label=_ft(lab))
    if seuil is not None:
        ax.axhline(seuil, color="grey", ls=":", lw=1)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft(ylabel))
    ax.grid(alpha=0.25)
    ax.legend(fontsize=9, loc="best")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def vues_liquidite():
    return [
        (_lab("v_reserves"),
         _trace_liq("FI.RES.TOTL.MO", "#1f4e79", "y_mois_imp", "l_reserves", seuil=3)),
        (_lab("v_service_exp"),
         _trace_liq("DT.TDS.DPPG.XP.ZS", "#c0392b", "y_pct_exp", "l_service_exp")),
    ]


def table_liquidite() -> pd.DataFrame:
    d = figtools.series(SERIE_LIQ).copy()
    t = d.pivot_table(index="annee", columns="code", values="valeur").reset_index()
    t = t.rename(columns={"FI.RES.TOTL.MO": "reserves_mois_import",
                          "DT.TDS.DPPG.XP.ZS": "service_dette_pct_export"})
    return t.round(2)


def table_echeancier() -> pd.DataFrame:
    d = _data()[["annee", "encours_MUSD", "principal_MUSD", "interets_MUSD",
                 "service_MUSD", "statut"]].copy()
    return d.round(1)


# --- figure : mur d'échéances par créancier (barres empilées) ----------------
_L["l_autres"] = {"fr": "autres créanciers", "ar": "دائنون آخرون"}


def _creanciers_fenetre() -> pd.DataFrame:
    d = figtools.series(SERIE_CREANCIERS).copy()
    d["annee"] = d["annee"].astype(int)
    return d[d["annee"] >= FENETRE_CREANCIERS]


def _nom(c: str) -> str:
    return _CREANCIERS_FR.get(c, c) if figtools.lang() == "fr" else c


def fig_creanciers():
    d = _creanciers_fenetre()
    totaux = d.groupby("creancier")["service_MUSD"].sum().sort_values(ascending=False)
    tete = list(totaux.head(N_CREANCIERS).index)
    annees = sorted(d["annee"].unique())
    cmap = plt.get_cmap("tab10")
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    bas = {a: 0.0 for a in annees}
    for i, cr in enumerate(tete):
        sous = d[d["creancier"] == cr].set_index("annee")["service_MUSD"]
        vals = [float(sous.get(a, 0.0)) for a in annees]
        ax.bar(annees, vals, bottom=[bas[a] for a in annees],
               color=cmap(i % 10), label=figtools.fig_text(_nom(cr)))
        for a, v in zip(annees, vals):
            bas[a] += v
    autres = [float(d[(d["annee"] == a) & (~d["creancier"].isin(tete))]["service_MUSD"].sum())
              for a in annees]
    ax.bar(annees, autres, bottom=[bas[a] for a in annees], color="#b0b0b0",
           label=_ft("l_autres"))
    proj = d[d["statut"] == "projeté"]["annee"]
    if not proj.empty:
        ax.axvline(proj.min() - 0.5, color="grey", ls=":", lw=1)
        ax.text(proj.min(), ax.get_ylim()[1] * 0.97, _ft("l_projete"),
                fontsize=8, color="grey", va="top")
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_musd"))
    ax.grid(alpha=0.25, axis="y")
    ax.legend(fontsize=8, ncol=2, loc="upper left")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def table_creanciers() -> pd.DataFrame:
    d = _creanciers_fenetre()[["annee", "creancier", "principal_MUSD",
                               "interets_MUSD", "service_MUSD", "statut"]].copy()
    return d.sort_values(["annee", "creancier"]).round(1)


# --- dette publique / PIB : trajectoire et décomposition de la variation --------
# Données : `finances-publiques-indicateurs` (ministère des Finances, 1986-2025). Le PIB employé
# est le PIB IMPLICITE du ministère (dette_MDT / dette_pct_pib × 100), cohérent en interne, ce qui
# évite les ruptures de base des comptes nationaux.
SERIE_FP = "finances-publiques-indicateurs"
C_DETTE = "#1f4e79"
C_DEFICIT = "#c0392b"
C_CROISS = "#1a9850"
C_RESIDU = "#e08214"

_L["y_pct_pib"] = {"fr": "en % du PIB", "ar": "٪ من الناتج"}
_L["y_pp"] = {"fr": "contribution, en points de PIB", "ar": "المساهمة، بنقاط من الناتج"}
_L["l_dette_pib"] = {"fr": "dette publique (% du PIB)", "ar": "الدين العمومي (٪ من الناتج)"}
_L["l_c_deficit"] = {"fr": "déficit", "ar": "العجز"}
_L["l_c_croiss"] = {"fr": "effet de la croissance nominale", "ar": "أثر النمو الاسمي"}
_L["l_c_residu"] = {"fr": "autres flux (dont effet de change)", "ar": "تدفقات أخرى (منها أثر الصرف)"}
_L["l_variation"] = {"fr": "variation totale", "ar": "التغير الجملي"}


def _fp() -> pd.DataFrame:
    d = figtools.series(SERIE_FP).copy()
    d["annee"] = d["annee"].astype(int)
    d = d.sort_values("annee").reset_index(drop=True)
    d["pib_MDT"] = d["dette_MDT"] / d["dette_pct_pib"] * 100
    return d


def fig_dette_pib():
    d = _fp().dropna(subset=["dette_pct_pib"])
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    ax.plot(d["annee"], d["dette_pct_pib"], color=C_DETTE, lw=1.9, label=_ft("l_dette_pib"))
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_pct_pib"))
    ax.grid(alpha=0.25)
    ax.legend(fontsize=9, loc="upper left")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def _decomposition() -> pd.DataFrame:
    """Contributions annuelles à Δ(dette/PIB), en points de PIB (identité comptable)."""
    d = _fp().dropna(subset=["dette_pct_pib", "pib_MDT"]).reset_index(drop=True)
    g = d["pib_MDT"] / d["pib_MDT"].shift(1) - 1            # croissance nominale (PIB implicite)
    b1 = d["dette_pct_pib"].shift(1)                         # dette/PIB de l'année précédente (pp)
    d["variation"] = d["dette_pct_pib"] - b1
    d["c_deficit"] = -d["deficit_pct_pib"]                  # le déficit (négatif) accroît la dette
    d["c_croiss"] = -b1 * g / (1 + g)                       # effet dénominateur (dilution)
    d["c_residu"] = d["variation"] - d["c_deficit"] - d["c_croiss"]
    return d.dropna(subset=["variation"])


def fig_dynamique():
    d = _decomposition()
    fig, ax = plt.subplots(figsize=(9.8, 5.4))
    an = d["annee"]
    pos = d[["c_deficit", "c_croiss", "c_residu"]].clip(lower=0)
    neg = d[["c_deficit", "c_croiss", "c_residu"]].clip(upper=0)
    cols = [("c_deficit", C_DEFICIT, "l_c_deficit"), ("c_croiss", C_CROISS, "l_c_croiss"),
            ("c_residu", C_RESIDU, "l_c_residu")]
    bas_p = pd.Series(0.0, index=d.index)
    bas_n = pd.Series(0.0, index=d.index)
    for col, couleur, cle in cols:
        ax.bar(an, pos[col], bottom=bas_p, color=couleur, label=_ft(cle))
        ax.bar(an, neg[col], bottom=bas_n, color=couleur)
        bas_p = bas_p + pos[col]
        bas_n = bas_n + neg[col]
    ax.plot(an, d["variation"], color="black", lw=0, marker="o", ms=3.2, label=_ft("l_variation"))
    ax.axhline(0, color="black", lw=0.8)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_pp"))
    ax.grid(alpha=0.25, axis="y")
    ax.legend(fontsize=8, ncol=2, loc="upper left")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def vues_dette_pib():
    return [(_lab("l_dette_pib"), fig_dette_pib()),
            (_lab("l_variation"), fig_dynamique())]


def table_dynamique() -> pd.DataFrame:
    d = _decomposition()[["annee", "dette_pct_pib", "variation",
                          "c_deficit", "c_croiss", "c_residu"]].copy()
    return d.round(2)


# --- coût de la dette et écart r − g (période récente, exécution 2021-2024) --------
SERIE_EXE = "finances-publiques-execution"
C_PRIMAIRE = "#8073ac"
C_INTERET = "#c0392b"
C_R = "#c0392b"
C_G = "#1a9850"

_L["l_r"] = {"fr": "coût apparent de la dette (r)", "ar": "الكلفة الظاهرية للدين (r)"}
_L["l_g"] = {"fr": "croissance nominale du PIB (g)", "ar": "النمو الاسمي للناتج (g)"}
_L["l_primaire"] = {"fr": "solde primaire", "ar": "الرصيد الأولي"}
_L["l_interet"] = {"fr": "charge d'intérêt", "ar": "فائدة الدين"}
_L["l_solde"] = {"fr": "solde budgétaire", "ar": "النتيجة"}
_L["v_rg"] = {"fr": "coût de la dette et croissance", "ar": "كلفة الدين والنمو"}
_L["y_pct_an"] = {"fr": "% par an", "ar": "٪ سنوياً"}
_L["v_solde"] = {"fr": "solde global = primaire − intérêts", "ar": "النتيجة = الأولي − الفوائد"}


SERIE_INTERET = "finances-publiques-charge-interet"


def _g_nominal() -> dict:
    """Croissance nominale du PIB, base-cohérente (série enchaînée), pour éviter les sauts de base."""
    p = figtools.series("pib-courant-enchaine")
    p = p[p["variante"] == "enchainee"][["annee", "pib_MD"]].sort_values("annee")
    niv = dict(zip(p["annee"].astype(int), p["pib_MD"]))
    return {a: (niv[a] / niv[a - 1] - 1) * 100 for a in niv if (a - 1) in niv}


def _rg() -> pd.DataFrame:
    """Écart r − g sur longue période : coût apparent (intérêt/dette) vs croissance nominale.

    `r` = charge d'intérêt de l'année / encours de dette publique de l'année précédente (MdF).
    `g` = croissance nominale du PIB, série ENCHAÎNÉE base-cohérente (sans les sauts de base des
    comptes nationaux — cf. annexe PIB).
    """
    fp = _fp()[["annee", "dette_MDT"]].copy()
    it = figtools.series(SERIE_INTERET).copy()
    it["annee"] = it["annee"].astype(int)
    dette = dict(zip(fp["annee"], fp["dette_MDT"]))
    g = _g_nominal()
    d = it.sort_values("annee").reset_index(drop=True)
    d["r_pct"] = [row.interet_MDT / dette[row.annee - 1] * 100 if (row.annee - 1) in dette else None
                  for row in d.itertuples()]
    d["g_pct"] = [g.get(row.annee) for row in d.itertuples()]
    return d.dropna(subset=["r_pct", "g_pct"])


def _cout() -> pd.DataFrame:
    """Décomposition du solde (primaire + intérêts) sur la période d'exécution MdF (2012-2024)."""
    fp = _fp()[["annee", "pib_MDT"]].copy()
    exe = figtools.series(SERIE_EXE).copy()
    exe["annee"] = exe["annee"].astype(int)
    d = exe.merge(fp, on="annee", how="left").sort_values("annee").reset_index(drop=True)
    d["interet_pct_pib"] = d["interet_MDT"] / d["pib_MDT"] * 100
    d["solde_pct_pib"] = d["solde_budgetaire_MDT"] / d["pib_MDT"] * 100
    d["primaire_pct_pib"] = d["solde_pct_pib"] + d["interet_pct_pib"]
    return d


def _trace_rg(d: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    ax.plot(d["annee"], d["r_pct"], color=C_R, lw=1.8, label=_ft("l_r"))
    ax.plot(d["annee"], d["g_pct"], color=C_G, lw=1.8, label=_ft("l_g"))
    # Jonction des segments de la charge d'intérêt (GFS/BM avant 2012, MdF à partir de 2012).
    if "source" in d.columns and (d["source"] == "MdF-exécution").any():
        j = int(d.loc[d["source"] == "MdF-exécution", "annee"].min())
        ax.axvline(j - 0.5, color="grey", ls=":", lw=1)
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_pct_an"))
    ax.grid(alpha=0.25)
    ax.legend(fontsize=9, loc="best")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def _trace_solde(d: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    ax.bar(d["annee"], d["primaire_pct_pib"], color=C_PRIMAIRE, label=_ft("l_primaire"))
    ax.bar(d["annee"], -d["interet_pct_pib"], bottom=d["primaire_pct_pib"],
           color=C_INTERET, label=_ft("l_interet"))
    ax.plot(d["annee"], d["solde_pct_pib"], color="black", lw=0, marker="o", ms=4,
            label=_ft("l_solde"))
    ax.axhline(0, color="black", lw=0.8)
    ax.set_xticks(d["annee"])
    ax.set_xlabel(_ft("x_annee"))
    ax.set_ylabel(_ft("y_pct_pib"))
    ax.grid(alpha=0.25, axis="y")
    ax.legend(fontsize=9, loc="lower right")
    _axe_annees(ax)
    fig.tight_layout()
    return fig


def vues_cout():
    return [(_lab("v_rg"), _trace_rg(_rg())), (_lab("v_solde"), _trace_solde(_cout()))]


def table_cout() -> pd.DataFrame:
    d = _rg()[["annee", "source", "r_pct", "g_pct"]].copy()
    d["ecart_r_g"] = d["r_pct"] - d["g_pct"]
    return d.round(2)

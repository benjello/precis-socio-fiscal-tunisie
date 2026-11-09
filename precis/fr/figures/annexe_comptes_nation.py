"""Données de la navigation par année de l'annexe « Les comptes de la nation ».

D'OÙ VIENNENT LES DONNÉES. Deux séries de `tunisia-data`, lues par `figtools.series()`,
toutes deux issues des *Comptes de la nation* de l'INS, base 2015 (édition la plus récente
par année) :

  - ``cnat-approche-revenus`` — l'approche des revenus de l'économie entière :
    rémunération des salariés, revenu d'exploitation (excédent brut + revenu mixte),
    impôts sur la production et les importations, subventions, PIB.
  - ``cnat-approche-revenus-secteurs`` — la valeur ajoutée des quatre secteurs
    institutionnels (SNF, sociétés financières, administrations, ménages).

IDENTITÉ GARANTIE, chaque année. La valeur ajoutée totale (somme des secteurs) égale la
somme rémunération + revenu d'exploitation (les deux présentations de l'INS p. 27) ; le PIB
s'en déduit en ajoutant les impôts sur les produits nets de subventions. Les deux approches
retombent donc sur le même PIB. On ne retient que les années où les deux séries sont
complètes en base 2015, et l'on écarte la dernière année si elle est provisoire.

Ce module ne trace rien : il ne fait que préparer la structure passée à Observable par
``ojs_define`` dans le `.qmd`. L'interactivité (curseur d'année, tableaux recomposés) vit
dans le bloc ``{ojs}`` de l'annexe, rendu en HTML seulement.
"""

from __future__ import annotations

import sys

sys.path.insert(0, ".")
sys.path.insert(0, "../../scripts")

import figtools  # noqa: E402

SECTEURS = {
    "snf": "Sociétés non financières",
    "sf": "Sociétés financières",
    "apu": "Administrations publiques",
    "menages": "Ménages (y c. entreprises individuelles)",
}
ORDRE = ["snf", "sf", "apu", "menages"]

# Dernière année retenue : au-delà, l'INS ne publie encore que des estimations provisoires.
ANNEE_MAX = 2024


def _f(x) -> float:
    return round(float(x), 1)


def donnees_navigation() -> dict:
    rev = figtools.series("cnat-approche-revenus")
    sec = figtools.series("cnat-approche-revenus-secteurs")

    rev = rev[(rev["base"].astype(str) == "2015") & (rev["annee"].astype(int) <= ANNEE_MAX)]
    sec = sec[(sec["base"].astype(str) == "2015") & (sec["annee"].astype(int) <= ANNEE_MAX)]

    par_annee = {}
    for _, r in rev.iterrows():
        annee = int(r["annee"])
        sec_a = sec[sec["annee"].astype(int) == annee]
        if len(sec_a) < 4:
            continue  # année incomplète côté secteurs : on l'écarte

        secteurs = []
        va_totale = 0.0
        for cle in ORDRE:
            ligne = sec_a[sec_a["secteur"] == cle]
            if ligne.empty:
                break
            va = _f(ligne.iloc[0]["valeur_ajoutee"])
            secteurs.append({"nom": SECTEURS[cle], "va": va})
            va_totale += va
        if len(secteurs) < 4:
            continue
        va_totale = round(va_totale, 1)

        remuneration = _f(r["remuneration_salaries"])
        revenu_exploitation = _f(r["revenu_exploitation"])
        impots = _f(r["impots_production_importations"])
        subventions = abs(_f(r["subventions"]))
        pib = _f(r["pib_approche_revenus"])
        impots_nets_produits = round(pib - va_totale, 1)

        par_annee[str(annee)] = {
            "pib": pib,
            "production": {
                "secteurs": secteurs,
                "va_totale": va_totale,
                "impots_nets_produits": impots_nets_produits,
            },
            "revenus": {
                "remuneration": remuneration,
                "revenu_exploitation": revenu_exploitation,
                "impots": impots,
                "subventions": subventions,
            },
            "part_salaires_pib": _f(r["part_remuneration_pib"]),
            "part_salaires_snf": _f(r["part_salaires_societes"]),
            "edition": str(r["edition"]),
        }

    annees = sorted(int(a) for a in par_annee)
    return {
        "annees": annees,
        "annee_defaut": 2021 if 2021 in annees else annees[-1],
        "parAnnee": par_annee,
    }


# --- la séquence des comptes, désagrégée par secteur -------------------------
# Ménages rétabli : la collision de slug de consolidate_cnat.py (ménages confondu avec sa
# sous-table « entreprises individuelles ») a été corrigée en amont (tunisia-data), et le compte
# complet des ménages régénéré (VA 2012 = 29 307,3 ; RDB ≠ épargne ; consommation finale présente).
SECTEURS_SEQ = [("snf", "SNF"), ("sf", "SF"), ("apu", "APU"),
                ("menages", "Ménages"), ("exterieur", "Reste du monde")]

# séquence des comptes : (compte, [(libellé, clé repliée INS, est_solde)]).
# Les clés sont les libellés de l'INS, repliés en ASCII minuscules (voir le générateur).
SEQUENCE = [
    ("Compte de production", [
        ("Valeur ajoutée brute", "valeur ajoutee brute", True)]),
    ("Compte d'exploitation", [
        ("Rémunération des salariés", "remuneration des salaries", False),
        ("Revenu d'exploitation / mixte", "revenu d'exploitation", True)]),
    ("Compte d'affectation des revenus primaires", [
        ("Intérêts", "interets", False),
        ("Solde des revenus primaires (revenu national)",
         "solde des revenus primaires / revenu national", True)]),
    ("Compte de distribution secondaire du revenu", [
        ("Prestations sociales en espèces", "prestations sociales en espece", False),
        ("Autres transferts courants", "autres transferts courants", False),
        ("Revenu disponible brut", "revenu disponible brut", True)]),
    ("Compte d'utilisation du revenu", [
        ("Dépense de consommation finale", "depense de consommation finale", False),
        ("Épargne brute", "epargne brute", True)]),
    ("Compte de capital", [
        ("Formation brute de capital fixe", "formation brute de capitale fixe", False),
        ("Transferts en capital", "transferts en capital", False),
        ("Capacité (+) ou besoin (−) de financement", "capacite ou besoin de financement", True)]),
]


def _fr(v) -> str:
    import math
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return ""
    return f"{v:,.1f}".replace(",", "\u202f").replace(".", ",")



# bases retenues, de la plus récente à la plus ancienne : pour une année couverte par deux
# bases, on montre la plus récente (les bases ne se chaînent pas, mais une année isolée est
# un instantané dans SA base — le navigateur n'affiche qu'une année à la fois, étiquetée).
BASES_ORDRE = ["2015", "1997"]


def donnees_sequence() -> dict:
    """Structure passée à Observable : séquence des comptes par secteur, toutes années, par base.

    Chaque année porte SA base (la plus récente qui la couvre) ; aucune base n'est chaînée à
    une autre — le navigateur montre une année isolée, dans sa base, qu'il étiquette.
    """
    d = figtools.series("cnat-comptes-secteurs")
    sequence = [{"compte": c, "lignes": [{"label": lib, "cle": cle, "solde": s}
                                        for lib, cle, s in lignes]}
                for c, lignes in SEQUENCE]
    par_annee, base_annee = {}, {}
    for an in sorted(d["annee"].astype(int).unique()):
        base = next((b for b in BASES_ORDRE
                     if not d[(d["annee"].astype(int) == an) & (d["base_pib"].astype(str) == b)].empty),
                    None)
        if base is None:
            continue
        da = d[(d["annee"].astype(int) == an) & (d["base_pib"].astype(str) == base)]
        bloc = {}
        for sec, _ in SECTEURS_SEQ:
            ds = da[da["secteur"] == sec]
            vals = {}
            for _, r in ds.iterrows():
                vals[r["indicateur"]] = round(float(r["valeur"]), 1)
            bloc[sec] = vals
        par_annee[str(an)] = bloc
        base_annee[str(an)] = base
    annees = sorted(int(a) for a in par_annee)
    return {
        "annees": annees,
        "annee_defaut": 2021 if 2021 in annees else annees[-1],
        "secteurs": [[c, lib] for c, lib in SECTEURS_SEQ],
        "sequence": sequence,
        "parAnnee": par_annee,
        "baseAnnee": base_annee,
    }


def sequence_comptes_md(annee: int = 2021, base: str = "2015") -> str:
    """Table Markdown de la séquence des comptes par secteur, pour une année et une base.

    Lignes = la séquence (opérations clés et soldes) ; colonnes = les cinq secteurs ;
    valeurs lues telles quelles dans les comptes de l'INS (soldes compris), en MDT.
    """
    d = figtools.series("cnat-comptes-secteurs")
    d = d[(d["annee"].astype(int) == annee) & (d["base_pib"].astype(str) == str(base))]
    piv = d.pivot_table(index="indicateur", columns="secteur", values="valeur", aggfunc="first")

    def val(cle, sec):
        try:
            return piv.loc[cle, sec]
        except KeyError:
            return float("nan")

    cols = [lib for _, lib in SECTEURS_SEQ]
    out = ["| Compte / opération | " + " | ".join(cols) + " |",
           "|" + "---|" * (len(cols) + 1)]
    for compte, lignes in SEQUENCE:
        out.append(f"| **{compte}** |" + " |" * len(cols))
        for lib, cle, solde in lignes:
            nom = f"*{lib}*" if solde else f"&nbsp;&nbsp;{lib}"
            cells = " | ".join(_fr(val(cle, sec)) for sec, _ in SECTEURS_SEQ)
            out.append(f"| {nom} | {cells} |")
    return "\n".join(out)


if __name__ == "__main__":
    import json

    d = donnees_navigation()
    print("années:", d["annees"], "| défaut:", d["annee_defaut"])
    ex = d["parAnnee"]["2021"]
    print("2021 PIB:", ex["pib"], "| VA totale:", ex["production"]["va_totale"],
          "| impôts nets produits:", ex["production"]["impots_nets_produits"])
    rv = ex["revenus"]
    recompose = round(rv["remuneration"] + rv["revenu_exploitation"] + rv["impots"] - rv["subventions"], 1)
    print("revenus recomposent PIB:", recompose, "==", ex["pib"], "→", abs(recompose - ex["pib"]) < 0.2)
    print("VA totale == rémun + revenu expl:",
          round(rv["remuneration"] + rv["revenu_exploitation"], 1), "==", ex["production"]["va_totale"])

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

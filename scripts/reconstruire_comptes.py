#!/usr/bin/env python3
"""Reconstruire le compte des administrations publiques (S13) à partir des postes de l'ouvrage.

Pilote de l'articulation entre chapitres et comptes nationaux : chaque poste du registre
`precis/fr/postes-comptables.csv` rattache un dispositif (une section de l'ouvrage) à une case
des comptes de secteur de l'INS (opération × côté × secteur). Le script :

1. détermine l'année de référence : la dernière année imprimée « définitive » dans l'édition la
   plus récente des comptes des secteurs (statut lu dans l'en-tête de l'INS : sans astérisque,
   définitif ; un astérisque, semi-définitif ; deux, provisoire — colonne `statut_annee` de la
   série `cnat-secteurs`) ;
2. chiffre chaque poste qui a une série : montant de l'année de référence et années couvertes,
   lus dans le cache ; source = première clé de citation de la série ; un poste sans série garde
   un montant vide (jamais estimé) ;
3. pour chaque opération des comptes non financiers de S13 et de ses sous-secteurs, compare la
   cible de l'INS à la somme des postes rattachés : écart (résidu publié) et justesse (somme des postes / montant INS) ; part du compte couverte et justesse par secteur et par année : scripts/couverture_comptes.py ;
   chaque année est mesurée dans la base la plus récente qui la publie (base 2015, sinon base 1997, série
   `cnat-secteurs-base1997`), sans raccord entre bases ; en base 1997, seules les opérations dont le code se
   raccorde au SCN 2008 par un lien « identique » sont retenues (colonne `base` de compte-couverture-annees.csv) ;
4. contrôle : un poste par section (une section n'a qu'un domicile), ancres existantes, somme des
   sous-secteurs face au consolidé, solde B.1g recalculé ;
5. écrit precis/fr/compte-apu-reconstruit.csv (une ligne par opération et secteur),
   precis/fr/compte-apu-flux.csv (qui verse à qui) et met à jour les colonnes `annees`,
   `montant_reference` et `source` du registre.

    uv run python scripts/reconstruire_comptes.py            # écrit
    uv run python scripts/reconstruire_comptes.py --verifier # échoue si un contrôle échoue
"""
from __future__ import annotations

import argparse
import csv
import functools
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import couverture_comptes as cc  # noqa: E402

RACINE = Path(__file__).resolve().parent.parent
FR = RACINE / "precis" / "fr"
CACHE = RACINE / "precis" / "_seriescache"
REGISTRE = FR / "postes-comptables.csv"
SORTIE = FR / "compte-apu-reconstruit.csv"
FLUX = FR / "compte-apu-flux.csv"
ENCADRES = FR / "encadres-comptes"
CONFIG = FR / "annee-reference.yml"
ANNEES = FR / "compte-couverture-annees.csv"
QUI = FR / "compte-apu-qui-verse.csv"
BASE1997 = CACHE / "cnat-secteurs-base1997.csv"  # comptes des secteurs en base 1997, éditions 2005-2009 à 2013-2017
# Copies de fichiers de l'entrepôt hors catalogue, refaites et vérifiées par scripts/fichiers_entrepot.py
RACCORD = CACHE / "raccord-scn-1968-1993-2008.csv"  # table de raccord des codes SCN 1968, 1993, 2008
CONTROLES1997 = CACHE / "cnat-secteurs-base1997-controles.csv"  # contrôles arithmétiques de la série en base 1997
ECHECS = FR / "compte-couverture-controles-echec.csv"
PRINCIPAUX = [("snf", "sociétés non financières"), ("sf", "sociétés financières"), ("apu", "administrations publiques"),
              ("menages", "ménages"), ("rdm", "reste du monde")]
SOUS_APU = [("apu_centrale", "administration centrale"), ("apu_locale", "collectivités locales"), ("apu_secu", "sécurité sociale")]
SECTEURS = {"apu": "S13", "apu_centrale": "S1311", "apu_locale": "S1313", "apu_secu": "S1314"}
COMPTES_NON_FINANCIERS = ("production", "exploitation", "affectation", "distribution", "utilisation", "capital")
ARRONDI = 0.05
# Opérations agrégées : leur reconstruction somme aussi les postes de leurs composantes.
AGREGATS = {
    "impots_production_importations": ["tva", "impots_importations", "impots_exportations", "autres_impots_produits",
                                       "autres_impots_production"],
    "subventions": ["subventions_produits", "autres_subventions_production"],
    "revenus_propriete": ["interets", "revenus_distribues", "loyers"],
}
# Écarts connus entre comptes et budget, nommés et non corrigés (voir l'annexe des comptes).
RESIDUS_NOMMES = {  # noms descriptifs ; les explications sont testées par scripts/expliquer_residus.py
    "impots_importations": "droits et taxes sur les importations des comptes face aux droits de douane du budget",
    "impots_courants": "impôts courants des comptes face à l'IRPP et à l'IS du budget",
    "fbcf": "FBCF des comptes face aux dépenses d'équipement du budget",
}


def fr(v) -> str:
    """Nombre à la française : espace fine insécable pour les milliers, virgule décimale."""
    return f"{float(v):,.1f}".replace(",", "\u202f").replace(".", ",")


def lire_csv(chemin: Path) -> list[dict]:
    with chemin.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def edition_pour(secteurs: list[dict], an: int) -> str:
    """Dernière édition où l'année est définitive (sinon la dernière qui la publie)."""
    defs = sorted({l["edition"] for l in secteurs if int(l["annee"]) == an and l["statut_annee"] == "definitif"})
    tous = sorted({l["edition"] for l in secteurs if int(l["annee"]) == an})
    return (defs or tous)[-1]


def annees_base2015(secteurs: list[dict]) -> list[int]:
    """Années que l'INS publie en base 2015 avec un compte des administrations publiques dans l'édition
    retenue par edition_pour() (une ligne isolée d'une autre édition ne suffit pas)."""
    b15 = [l for l in secteurs if str(l.get("base", "")) == "2015"]
    garde = []
    for y in sorted({int(l["annee"]) for l in b15}):
        ed = edition_pour(b15, y)
        if any(l["edition"] == ed and int(l["annee"]) == y and l["secteur"] == "apu" for l in b15):
            garde.append(y)
    return garde


def liens_raccord(base: str = "1997") -> dict:
    """{opération : lien de son code de la base au code du SCN 2008} (« identique », « regroupement »,
    « à valider », ou vide quand le lien n'est pas établi), lu dans la table de raccord des codes copiée de
    l'entrepôt (sources/ins-comptes-nationaux/raccord-scn-1968-1993-2008.csv)."""
    return {l["operation"]: l[f"lien_{base}"] for l in lire_csv(RACCORD)}


def lire_base1997() -> list[dict]:
    """Comptes des secteurs en base 1997, toutes éditions, colonne `valeur` comme le cache en base 2015.
    Une ligne dont l'année sort de la fenêtre imprimée de son édition est écartée (édition 2009-2013 :
    une page du compte des administrations publiques porte les années 2008-2012)."""
    out = []
    for l in lire_csv(BASE1997):
        a, b = int(l["edition"][:4]), int(l["edition"][-4:])
        if a <= int(l["annee"]) <= b:
            out.append({**l, "valeur": l["valeur_md"]})
    return out


def annees_base1997(b97: list[dict], hors: list[int]) -> list[tuple[int, str]]:
    """(année, édition) des années publiées en base 1997 et absentes de `hors` (les années de la base 2015) :
    chaque année est mesurée dans la base la plus récente qui la publie, dans la dernière édition où elle est
    définitive (edition_pour), parmi celles qui impriment le compte des administrations et de leurs trois
    sous-secteurs pour cette année."""
    secs = defaultdict(set)
    for l in b97:
        secs[(l["edition"], int(l["annee"]))].add(l["secteur"])
    complets = [l for l in b97 if set(SECTEURS) <= secs[(l["edition"], int(l["annee"]))]]
    return [(y, edition_pour(complets, y)) for y in sorted({int(l["annee"]) for l in complets}) if y not in hors]


def poste_hors_base(poste: str, base: str) -> str:
    """Raison pour laquelle un poste du registre ne compte pas dans le compte d'une base (vide s'il compte).
    Le poste reste rattaché à son opération, sans montant : l'opération n'est pas chiffrée par lui."""
    if poste == "redevance-gazoduc" and base == "1997":
        # INS, Les comptes de la nation, éd. 2015-2020, vol. A, p. 17 : la base 2015 reclasse en revenu de la
        # propriété la redevance sur le passage du gaz algérien, « auparavant comptabilisée comme production du
        # secteur transport ». En base 1997, elle n'est donc pas dans les loyers (D.45) où le registre la range.
        return "redevance du gazoduc : production du secteur transport en base 1997, non loyers (D.45)"
    return ""


def couverture_annee(postes_y: list[dict], lig_y: list[dict], liens: dict | None = None) -> dict:
    """Indicateurs de couverture par secteur pour une année (lignes de l'INS de l'édition retenue). Avec
    `liens` (base autre que 2015), les opérations dont le lien au code du SCN 2008 n'est pas « identique »
    sont retirées des feuilles : ni couvertes ni comptées dans le total."""
    par_secteur = {}
    for code, (sec, membres) in cc.SECTEURS.items():
        ratt = cc.postes_du_secteur(postes_y, membres)
        ops = cc.feuilles([l for l in lig_y if l["secteur"] == sec], garder=cc.garder_par_cote(ratt))
        if liens is not None:
            ops = cc.raccord_identique(ops, liens)
        if ops:
            par_secteur[code] = cc.indicateurs(ops, ratt)
    par_secteur["S13"] = cc.agreger([par_secteur[s] for s in cc.SOUS_SECTEURS_S13])
    return par_secteur


def operations_retenues_s13(postes_y: list[dict], lig_y: list[dict], liens: dict | None = None) -> set:
    """Opérations retenues dans le total du compte des administrations (feuilles des trois sous-secteurs)."""
    out = set()
    for code in cc.SOUS_SECTEURS_S13:
        sec, membres = cc.SECTEURS[code]
        ratt = cc.postes_du_secteur(postes_y, membres)
        ops = cc.feuilles([l for l in lig_y if l["secteur"] == sec], garder=cc.garder_par_cote(ratt))
        out |= {l["operation"] for l in (cc.raccord_identique(ops, liens) if liens is not None else ops)}
    return out


def controles_en_echec(controles_src: list[dict], y: int, ed: str, retenues: set) -> list[dict]:
    """Contrôles de la série de l'entrepôt en échec pour une année et son édition, qui concernent le compte des
    administrations : solde ou consolidation d'un secteur des administrations, équilibre entre secteurs d'une
    opération retenue dans le total. `touche_total` : l'opération contrôlée entre dans le total des opérations
    retenues des trois sous-secteurs (« oui »), n'y entre pas (« non » : compte consolidé, soldes), ou l'écart
    d'équilibre entre secteurs ne désigne pas le secteur en cause (« indetermine »)."""
    libelles = {l["operation"]: l["libelle_scn2008"] for l in lire_csv(RACCORD)}
    out = []
    for l in controles_src:
        if l["edition"] != ed or l["annee"] != str(y) or l["statut"] != "echec":
            continue
        apu = l["secteur"] in SECTEURS
        if not (apu or (l["controle"] == "equilibre" and l["objet"] in retenues)):
            continue
        touche = ("indetermine" if l["controle"] == "equilibre"
                  else "oui" if l["secteur"] != "apu" and l["objet"] in retenues else "non")
        out.append({"annee": y, "edition": ed, "controle": l["controle"], "secteur": l["secteur"],
                    "objet": l["objet"], "libelle_scn2008": libelles.get(l["objet"]) or l["objet"].replace("_", " ").capitalize(), "publie_md": l["publie"], "recalcule_md": l["recalcule"],
                    "ecart_md": l["ecart"], "touche_total": touche})
    return out


def annee_reference(secteurs: list[dict]) -> tuple[int, str]:
    """Année fixée dans precis/fr/annee-reference.yml : la dernière où les sources de la reconstruction sont
    toutes disponibles (comptes des caisses compris), non la dernière année définitive des comptes."""
    an = int(yaml.safe_load(CONFIG.read_text(encoding="utf-8"))["annee"])
    return an, edition_pour(secteurs, an)


@functools.lru_cache(maxsize=None)
def _lignes_serie(serie: str) -> tuple[dict, ...]:
    """Lignes d'une série du cache, lues une fois (montant() ne les modifie pas)."""
    chemin = CACHE / f"{serie}.csv"
    return tuple(lire_csv(chemin)) if chemin.exists() else ()


def montant(serie: str, colonne: str, annee: int) -> tuple[float | None, str]:
    lignes = _lignes_serie(serie)
    if not lignes:
        return None, ""
    if "entite" in lignes[0] and "exercice" in lignes[0] and "derniere_edition" in lignes[0]:
        # série par entreprise et par exercice : « champ|e1;e2;… » somme le champ sur ces entreprises, chacune
        # dans la dernière édition qui donne l'exercice ; une entreprise sans valeur : aucun montant (périmètre constant)
        champ, _, liste = colonne.partition("|")
        ents = [e for e in liste.split(";") if e]
        val = {(l["entite"], int(l["exercice"])): float(l[champ]) for l in lignes
               if str(l["derniere_edition"]) in ("True", "true", "1") and l.get(champ, "") != "" and l["entite"] in ents}
        ans = sorted({a for _, a in val if all((e, a) in val for e in ents)})
        couv = f"{ans[0]}-{ans[-1]}" if ans else ""
        if not ents or annee not in ans:
            return None, couv
        return round(sum(val[(e, annee)] for e in ents), 1), couv
    annees = sorted({int(str(l["annee"])[:4]) for l in lignes if str(l.get("annee", ""))[:4].isdigit()})
    couv = f"{annees[0]}-{annees[-1]}" if annees else ""
    if serie == "compensation-parts":  # total budgétaire de la compensation, une ligne par année
        vals = [float(l["valeur_MDT"]) for l in lignes if str(l["annee"]) == str(annee)
                and l["poste"] == colonne and l["famille"] == "budget"]
        return (-vals[-1] if vals else None), couv  # subvention : ressource négative dans les comptes
    if "variable" in lignes[0] and "valeur" in lignes[0]:  # série longue : une ligne par (année, variable)
        vals = [float(l["valeur"]) for l in lignes if str(l["annee"]) == str(annee) and l["variable"] == colonne
                and str(l.get("retenu", "True")) in ("True", "true", "1")]
        return (vals[-1] if vals else None), couv
    if "rubrique" in lignes[0] and "valeur_md" in lignes[0]:  # série longue par rubrique (recettes non fiscales)
        vals = [float(l["valeur_md"]) for l in lignes if str(l["annee"]) == str(annee) and l["rubrique"] == colonne]
        return (vals[-1] if vals else None), couv
    if "indicateur" in lignes[0] and ("valeur" in lignes[0] or "valeur_md" in lignes[0]):  # série longue : (année, indicateur)
        champ = "valeur" if "valeur" in lignes[0] else "valeur_md"
        morceaux = colonne.split("|")
        fenetre = None  # « CNSS|recettes techniques|2021-2023 » : poste limité à ces années (relais d'une série close)
        if len(morceaux) == 3 and re.fullmatch(r"\d{4}-\d{4}", morceaux[2]):
            fenetre = tuple(int(x) for x in morceaux[2].split("-"))
            colonne = "|".join(morceaux[:2])
        caisse, _, ind = colonne.rpartition("|")  # « CNAM|recettes techniques » : filtre sur la colonne caisse
        if fenetre:
            dans = [a for a in annees if fenetre[0] <= a <= fenetre[1]]
            couv = f"{dans[0]}-{dans[-1]}" if dans else ""
            if not fenetre[0] <= annee <= fenetre[1]:
                return None, couv
        vals = [float(l[champ]) for l in lignes if str(l["annee"]) == str(annee) and l["indicateur"].startswith(ind)
                and (not caisse or l.get("caisse") == caisse)]
        return (vals[-1] if vals else None), couv  # la dernière ligne : l'édition la plus récente
    vals = [float(l[colonne]) for l in lignes if str(l["annee"]) == str(annee) and l.get(colonne, "") != ""]
    return (vals[-1] if vals else None), couv


def annees_chiffrees(p: dict) -> list[int]:
    """Années où le poste a une valeur dans sa série (fenêtre « …|AAAA-AAAA » respectée par montant())."""
    if not p.get("serie"):
        return []
    _, couv = montant(p["serie"], p["colonne"], 0)
    if not re.fullmatch(r"\d{4}-\d{4}", couv or ""):
        return []
    a, b = (int(x) for x in couv.split("-"))
    return [y for y in range(a, b + 1) if montant(p["serie"], p["colonne"], y)[0] is not None]


def liste_annees(annees: list[int]) -> str:
    """« 2021-2023 » si les années se suivent ; sinon la liste des plages : « 2008-2019 et 2022-2023 »,
    « 2019, 2021 et 2023 »."""
    plages = []
    for y in annees:
        if plages and y == plages[-1][1] + 1:
            plages[-1][1] = y
        else:
            plages.append([y, y])
    noms = [str(a) if a == b else f"{a}-{b}" for a, b in plages]
    return ", ".join(noms[:-1]) + f" et {noms[-1]}" if len(noms) > 1 else noms[0]


def fin_encadre(p: dict, an: int, chiffrees: list[int] | None = None) -> str:
    """Fin de la phrase de l'encadré : montant de l'année de référence ; pour un poste sans valeur cette
    année-là mais chiffré d'autres années, ces années ; « ne chiffre pas encore » pour un poste sans aucune valeur."""
    if p["montant_reference"]:
        return f" ; l'ouvrage en chiffre {fr(p['montant_reference'])} pour ce dispositif."
    if chiffrees is None:
        chiffrees = annees_chiffrees(p)
    if len(chiffrees) == 1:
        return f" ; ce poste chiffre l'année {chiffrees[0]}, non l'année de référence {an}."
    if chiffrees:
        return f" ; ce poste chiffre les années {liste_annees(chiffrees)}, non l'année de référence {an}."
    return " ; l'ouvrage ne chiffre pas encore ce dispositif."


SECTEURS_APU = {"apu", "apu_centrale", "apu_locale", "apu_secu"}
SUJETS = {"snf": "Les sociétés non financières y inscrivent", "sf": "Les sociétés financières y inscrivent",
          "menages": "Les ménages y inscrivent", "rdm": "Le reste du monde y inscrit"}


def phrase_montant(p: dict, cible_s13: dict, qui: list[dict], an: int) -> str:
    """Comparaison de l'encadré. Poste payé ou reçu par une administration : montant des administrations
    publiques (S13). Sinon : montant du secteur du poste du côté du poste (le payeur pour un emploi, le
    receveur pour une ressource), s'il est seul de ce côté et que les comptes le publient ; sinon rien."""
    secs = {s for s in (p["secteur_verse"] + ";" + p["secteur_recoit"]).split(";") if s}
    if secs & SECTEURS_APU:
        l = cible_s13.get((p["cote"], p["operation"]))
        if not l:
            return ""
        return (f" Les administrations publiques y inscrivent {fr(l['cible_ins_md'])} millions de dinars ({p['cote']})"
                + fin_encadre(p, an))
    cote_secs = [s for s in (p["secteur_verse"] if p["cote"] == "emplois" else p["secteur_recoit"]).split(";") if s]
    if len(cote_secs) != 1 or cote_secs[0] not in SUJETS:
        return ""
    nom = dict(PRINCIPAUX)[cote_secs[0]]
    v = [x for x in qui if x["operation"] == p["operation"] and x["secteur"] == nom and x["cote"] == p["cote"]
         and x["niveau"] == "secteur"]
    if not v or v[0]["valeur_md"] in (None, ""):
        return ""
    return f" {SUJETS[cote_secs[0]]} {fr(v[0]['valeur_md'])} millions de dinars ({p['cote']})" + fin_encadre(p, an)


def source_serie(serie: str, snapshot: dict) -> str:
    e = snapshot.get(serie)
    return (e.get("sources") or [""])[0] if e else ""


def ancre_existe(volume: str, chapitre: str, ancre: str) -> bool:
    page = FR / (f"{volume}.qmd" if not chapitre else f"{volume}/{chapitre}.qmd")
    return page.exists() and re.search(r"\{#" + re.escape(ancre) + r"[ }]", page.read_text(encoding="utf-8")) is not None


def calculer(an: int, ed: str, secteurs: list[dict], snapshot: dict):
    """Postes chiffrés, comptes reconstruits et contrôles pour une année et une édition."""
    postes = lire_csv(REGISTRE)
    erreurs = []
    vus_sections = {}
    for p in postes:
        cle = (p["volume"], p["chapitre"], p["ancre"])
        if cle in vus_sections:
            erreurs.append(f"section {cle} domicile de deux postes ({vus_sections[cle]}, {p['poste']})")
        vus_sections[cle] = p["poste"]
        if not ancre_existe(*cle):
            erreurs.append(f"poste {p['poste']} : ancre {p['ancre']} absente de {p['volume']}/{p['chapitre']}")
        if p["serie"]:
            m, couv = montant(p["serie"], p["colonne"], an)
            if m is not None and p.get("facteur"):
                m *= float(p["facteur"])
            p["montant_reference"] = "" if m is None else f"{m:.1f}"
            p["annees"] = couv
            p["source"] = source_serie(p["serie"], snapshot)
        else:
            p["montant_reference"], p["annees"], p["source"] = "", "", ""
    # Cibles de l'INS, édition la plus récente, année de référence
    cible = {}
    for l in secteurs:
        if l["edition"] == ed and int(l["annee"]) == an and l["secteur"] in SECTEURS and l["sous_ligne"] in ("0", "False", ""):
            if any(k in l["compte"].lower() for k in COMPTES_NON_FINANCIERS):
                cible[(l["secteur"], l["cote"], l["operation"])] = (l["code_scn2008"], l["compte"], float(l["valeur"]))
    # sous-lignes utiles (TVA, impôts sur les importations…) : rangées à part
    for l in secteurs:
        if l["edition"] == ed and int(l["annee"]) == an and l["secteur"] in SECTEURS and l["sous_ligne"] not in ("0", "False", ""):
            if any(k in l["compte"].lower() for k in COMPTES_NON_FINANCIERS):
                cible.setdefault((l["secteur"], l["cote"], l["operation"]), (l["code_scn2008"], l["compte"], float(l["valeur"])))
    somme = defaultdict(float)
    rattaches = defaultdict(list)
    for p in postes:
        # le secteur des administrations concerné, qu'il verse ou reçoive (les subventions, versées,
        # sont inscrites par l'INS en ressources négatives)
        cotes = [p["secteur_recoit"], p["secteur_verse"]] if p["cote"] == "ressources" else [p["secteur_verse"], p["secteur_recoit"]]
        for sec in ";".join(cotes).split(";"):  # le côté de l'opération d'abord : qui reçoit une ressource, qui verse un emploi
            if sec in SECTEURS:
                rattaches[(sec, p["cote"], p["operation"])].append(p["poste"])
                if p["montant_reference"]:
                    somme[(sec, p["cote"], p["operation"])] += float(p["montant_reference"])
                break  # un poste n'est compté que dans un secteur : le premier de la liste
    lignes = []
    for (sec, cote, op), (code, compte, v) in sorted(cible.items(), key=lambda k: (k[0][0], k[1][1], k[0][1], k[0][2])):
        ops = [op] + AGREGATS.get(op, [])
        secs = list(SECTEURS) if sec == "apu" else [sec]
        noms = sorted({n for ss in secs for o in ops for n in rattaches.get((ss, cote, o), [])})
        vals = [somme[(ss, cote, o)] for ss in secs for o in ops if (ss, cote, o) in somme]
        s_postes = sum(vals) if vals else None
        residu = None if s_postes is None else round(v - s_postes, 1)
        lignes.append({"annee": an, "edition": ed, "secteur": SECTEURS[sec], "compte": compte, "cote": cote,
                       "code_scn": code, "operation": op, "cible_ins_md": v,
                       "postes": ";".join(noms), "somme_postes_md": "" if s_postes is None else round(s_postes, 1),
                       "residu_md": "" if residu is None else residu,
                       "justesse_pct": "" if s_postes is None or not v else round(100 * s_postes / v, 1),
                       "residu_nomme": RESIDUS_NOMMES.get(op, "") if residu is not None else ""})
    # Contrôles : sous-secteurs face au consolidé ; solde B.1g
    controles = []
    for (sec, cote, op), (code, compte, v) in cible.items():
        if sec != "apu":
            continue
        parts = [cible[(s, cote, op)][2] for s in ("apu_centrale", "apu_locale", "apu_secu") if (s, cote, op) in cible]
        if len(parts) == 3:
            controles.append({"controle": "sous-secteurs - consolidé", "objet": f"{op} ({cote})",
                              "ecart_md": round(sum(parts) - v, 1),
                              "note": "écart attendu pour les transferts entre administrations (consolidation)"})
    for sec in SECTEURS:
        try:
            p1 = cible[(sec, "ressources", "production")][2]
            p2 = cible[(sec, "emplois", "consommation_intermediaire")][2]
            b1 = cible[(sec, "emplois", "valeur_ajoutee_brute")][2]
            e = round(p1 - p2 - b1, 1)
            controles.append({"controle": "solde B.1g recalculé", "objet": SECTEURS[sec], "ecart_md": e,
                              "note": "ok" if abs(e) <= ARRONDI * 3 else "écart"})
            if abs(e) > ARRONDI * 3:
                erreurs.append(f"B.1g de {SECTEURS[sec]} : écart {e}")
        except KeyError:
            pass
    flux = [{"poste": p["poste"], "operation": p["operation"], "code_scn": p["code_scn"], "verse": p["secteur_verse"],
             "recoit": p["secteur_recoit"], "montant_md": p["montant_reference"], "volume": p["volume"],
             "section": (f"{p['volume']}/{p['chapitre']}" if p["chapitre"] else p["volume"]) + f"#{p['ancre']}",
             "contrepartie": p.get("contrepartie_statut", ""), "contrepartie_secteur": p.get("contrepartie_secteur", "")}
            for p in postes]
    return postes, lignes, controles, flux, erreurs


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", action="store_true")
    a = ap.parse_args(argv)
    secteurs = lire_csv(CACHE / "cnat-secteurs.csv")
    an, ed = annee_reference(secteurs)
    snapshot = {e["id"]: e for e in yaml.safe_load((CACHE / "catalog.snapshot.yml").read_text(encoding="utf-8"))}
    postes, lignes, controles, flux, erreurs = calculer(an, ed, secteurs, snapshot)
    # Couverture année par année, pour montrer le profil des retards : chaque année dans la base la plus
    # récente qui la publie (base 2015, sinon base 1997), sans chaînage entre bases (question M10).
    ans15 = annees_base2015(secteurs)
    b97 = lire_base1997()
    liens97 = liens_raccord("1997")
    ctrl97 = lire_csv(CONTROLES1997)
    annees, echecs = [], []
    for y, ed_y, base in ([(y, ed, "1997") for y, ed in annees_base1997(b97, ans15)]
                          + [(y, edition_pour([l for l in secteurs if str(l.get("base", "")) == "2015"], y), "2015")
                             for y in ans15]):
        postes_y, _, _, _, _ = calculer(y, ed_y, secteurs, snapshot)  # postes seuls : ne lit pas `secteurs`
        postes_y = [{**p, "montant_reference": ""} if poste_hors_base(p["poste"], base) else p for p in postes_y]
        if base == "2015":
            lig_y = [l for l in secteurs if l["edition"] == ed_y and int(l["annee"]) == y and str(l.get("base", "2015")) == "2015"]
        else:
            lig_y = [l for l in b97 if l["edition"] == ed_y and int(l["annee"]) == y]
        par_secteur = couverture_annee(postes_y, lig_y, liens97 if base == "1997" else None)
        for code in ["S13", "S13-consolide"] + [c for c in par_secteur if c not in ("S13", "S13-consolide")]:
            annees.append({"annee": y, "edition": ed_y, "base": base, "secteur": code, **par_secteur[code]})
        if base == "1997":  # la série en base 2015 n'est versée que sans contrôle en échec
            echecs += controles_en_echec(ctrl97, y, ed_y, operations_retenues_s13(postes_y, lig_y, liens97))
    if a.verifier:
        if [dict(x) for x in lire_csv(ANNEES)] != [{k: str(v) for k, v in l.items()} for l in annees]:
            erreurs.append(f"{ANNEES.name} n'est pas à jour : relancer scripts/reconstruire_comptes.py")
        if [dict(x) for x in lire_csv(ECHECS)] != [{k: str(v) for k, v in l.items()} for l in echecs]:
            erreurs.append(f"{ECHECS.name} n'est pas à jour : relancer scripts/reconstruire_comptes.py")
        for e in erreurs:
            print("ERREUR :", e)
        return 1 if erreurs else 0
    for chemin, rows in ((SORTIE, lignes), (FLUX, flux), (ANNEES, annees), (ECHECS, echecs)):
        with chemin.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
    with (FR / "compte-apu-controles.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["controle", "objet", "ecart_md", "note"], lineterminator="\n")
        w.writeheader()
        w.writerows(controles)
    with REGISTRE.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(postes[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(postes)
    # Encadrés « Dans les comptes », un par poste, inclus dans la section domicile : opération,
    # tableau « qui verse à qui » des secteurs principaux, montant de l'INS, montant de l'ouvrage.
    ENCADRES.mkdir(parents=True, exist_ok=True)
    cible_s13 = {(l["cote"], l["operation"]): l for l in lignes if l["secteur"] == "S13"}
    secteurs = [l for l in lire_csv(CACHE / "cnat-secteurs.csv")
                if l["edition"] == ed and str(l["annee"]) == str(an) and str(l["sous_ligne"]) in ("0", "1")]
    qui = []
    for op in sorted({p["operation"] for p in postes}):
        for sec, nom in PRINCIPAUX + SOUS_APU:
            for cote in ("emplois", "ressources"):
                v = [x for x in secteurs if x["secteur"] == sec and x["cote"] == cote and x["operation"] == op]
                if v:
                    qui.append({"annee": an, "edition": ed, "operation": op, "code_scn": v[0]["code_scn2008"],
                                "libelle_ins": v[0]["libelle_ins"], "secteur": nom, "niveau": "sous-secteur" if sec.startswith("apu_") else "secteur", "cote": cote,
                                "valeur_md": round(sum(float(x["valeur"]) for x in v), 1)})
    with QUI.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(qui[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(qui)
    for p in postes:
        profondeur = "../" if (FR / p["volume"]).is_dir() else ""
        lien = f"{profondeur}compte-apu.html#sec-capu-flux"
        niveau = "sous-secteur" if p["operation"] == "transferts_entre_administrations" else "secteur"
        q = [x for x in qui if x["operation"] == p["operation"] and x["niveau"] == niveau]
        lib = q[0]["libelle_ins"] if q else p["operation"].replace("_", " ")
        verse = " ; ".join(f"{x['secteur']} {fr(x['valeur_md'])}" for x in q if x["cote"] == "emplois" and x["valeur_md"])
        recoit = " ; ".join(f"{x['secteur']} {fr(x['valeur_md'])}" for x in q if x["cote"] == "ressources" and x["valeur_md"])
        if p["code_scn"].startswith("P."):  # opération sur produits : des emplois, pas un versement
            flux = f"emplois des secteurs : {verse or recoit}"
        else:
            flux = f"versent : {verse or 'aucun secteur principal'} ; reçoivent : {recoit or 'aucun secteur principal'}"
        phrase = (f"Ce dispositif relève de l'opération **{p['code_scn']} « {lib} »** des comptes de la nation. "
                  f"En {an} (édition {ed}), en millions de dinars, {flux}.")
        phrase += phrase_montant(p, cible_s13, qui, an)
        (ENCADRES / f"{p['poste']}.md").write_text(
            f"::: {{.callout-tip title=\"Dans les comptes\"}}\n{phrase} Voir [le compte reconstruit]({lien}).\n:::\n",
            encoding="utf-8")
    chiffres = sum(1 for p in postes if p["montant_reference"])
    s13 = [l for l in lignes if l["secteur"] == "S13"]
    couverts = sum(1 for l in s13 if l["somme_postes_md"] != "")
    print(f"année de référence {an} (édition {ed}) ; {len(postes)} postes dont {chiffres} chiffrés ; "
          f"S13 : {couverts} opérations couvertes sur {len(s13)} ; {len(erreurs)} erreur(s)")
    for e in erreurs:
        print("ERREUR :", e)
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())

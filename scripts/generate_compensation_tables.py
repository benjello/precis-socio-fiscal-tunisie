"""Régénère les snapshots des tableaux de paramètres du livre « La compensation ».

Même contrat que les autres générateurs : le build du site n'exécute PAS ce script, il lit les
fichiers qu'il produit, versionnés dans `precis/fr/compensation/tables/` et
`precis/_seriescache/`.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_compensation_tables.py

Exige openfisca-tunisia >= 0.171. La 0.169 verse `produits_subventionnes/cereales/` (prix
fixés à chaque campagne par le texte de l'Office des céréales, récoltes 1970 à 2026) et
`produits_subventionnes/caisse_generale_compensation/taxes_affectees/` ; la 0.171,
`produits_subventionnes/prix_administres_1974_1991/` (prix au public des produits de base
publiés au Journal officiel de 1974 à 1991).

CE QUI EST ENGENDRÉ :
  - `tables/cereales_prix_production.md` : prix de base à la production du blé dur, du blé
    tendre et de l'orge, et prix d'intervention de l'orge, une ligne par date ;
  - `tables/cereales_prix_retrocession.md` : prix normaux de rétrocession (blé dur, blé tendre,
    orge) et prix réduits de rétrocession des blés aux minoteries et semouleries ;
  - `tables/caisse_taxes_affectees.md` : taxes affectées à la Caisse générale de compensation ;
  - `_seriescache/compensation-cereales-parametres.csv` : la série longue des neuf prix (une
    ligne par prix et par date, `parametre,date_effet,valeur,texte,lien`), que les figures
    lisent par `figtools.series("compensation-cereales-parametres")` — le build du site
    n'importe pas openfisca ;
  - `tables/prix_administres_{pain,farines_semoule,pates_couscous,sucre_cafe,huile_lait}.md` :
    les prix au public des produits de base, 1974-1991, une ligne par produit et par date ;
  - `_seriescache/compensation-prix-administres.csv` : la série longue des 25 prix
    administrés (clé : nom du paramètre, valeur en dinars dans l'unité du texte), que lit
    `precis/fr/compensation/figures/produits_base.py`.
Chaque tableau a ses liens « Base législative » (`<nom>.liens.yml`), la série les siens
(`compensation-cereales-parametres.liens.fr.yml`).

FIN ET DÉBUT DE SÉRIE. Une valeur nulle dit que le prix cesse d'être fixé : le prix de base de
l'orge au 6 septembre 1993 (commercialisation libre à partir de la récolte 1992), les prix
réduits des blés au 4 juillet 1991. La case du tableau est alors « — », la ligne de la série
n'a pas de valeur. Le prix d'intervention de l'orge commence le même 6 septembre 1993 : les
deux grandeurs sont tenues séparées, colonne par colonne et clé par clé, sans être raboutées.

PRIX ADMINISTRÉS, 1974-1991. Un paramètre par produit, variété, conditionnement et unité de
prix du texte : le tableau ne raccorde rien, il donne chaque prix tel que le texte le fixe, en
dinars. Une valeur nulle dit que le prix n'est pas établi à partir de cette date, ou qu'il
cesse d'être publié (1er janvier 1992, liberté des prix) ; la case est « — ». Le
1er janvier 1980 du gros pain de 700 g et du petit pain de 300 g n'est pas une date d'effet :
il borne une période sans prix établi et ne cite aucun texte ; la case de date porte l'année
seule, la case de texte un tiret, et la ligne de la série n'a ni texte ni lien.

DATE D'EFFET OU DATE DE PUBLICATION. Plusieurs textes de campagne ne disent pas leur date
d'effet et paraissent dans un numéro du Journal officiel daté de plusieurs jours, dont le jour de
parution n'est pas établi : le paramètre porte alors la dernière date du numéro, retenue comme
date de publication, et le dit dans sa note. La case de date l'écrit (« publié le … ») au lieu de
la présenter comme une date d'effet.

UNE LIGNE PAR DATE, NON PAR RÉCOLTE. Les prix réduits changent aussi par des décrets sur le prix
des farines et du pain, hors des textes de campagne (1975, 1976, 1979, 1983, 1984), et la
récolte visée n'est pas l'année de la date (récolte 1978, décret d'avril 1979). Le tableau suit
donc les dates des paramètres ; la récolte se lit dans le titre du texte.

L'ARABE N'EST PAS ENGENDRÉ. Le glossaire n'a pas l'arabe de « prix de base à la production »,
« prix d'intervention », « rétrocession » ni « péréquation de raffinage » ; les libellés
attendent la passe du terminologue. Le générateur n'écrit que le français.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

PS = "parameters/produits_subventionnes"
CER = f"{PS}/cereales"
TAXES = f"{PS}/caisse_generale_compensation/taxes_affectees"
RACINE = Path(__file__).parent.parent / "precis"
LIVRE = "compensation"
LANGUE = "fr"
SORTIE = RACINE / LANGUE / LIVRE / "tables"
CACHE = RACINE / "_seriescache"
SERIE = "compensation-cereales-parametres"
TIRET = "—"
PA = f"{PS}/prix_administres_1974_1991"
SERIE_PA = "compensation-prix-administres"

# (clé de la série, chemin, en-tête de colonne, libellé du lien « Base législative »)
PRODUCTION = [
    ("ble_dur_prix_base", f"{CER}/prix_base_production/ble_dur.yaml",
     "Blé dur, prix de base (D/ql)", "Prix de base à la production du blé dur"),
    ("ble_tendre_prix_base", f"{CER}/prix_base_production/ble_tendre.yaml",
     "Blé tendre, prix de base (D/ql)", "Prix de base à la production du blé tendre"),
    ("orge_prix_base", f"{CER}/prix_base_production/orge.yaml",
     "Orge, prix de base (D/ql)", "Prix de base à la production de l'orge"),
    ("orge_prix_intervention", f"{CER}/prix_intervention_orge.yaml",
     "Orge, prix d'intervention (D/ql)", "Prix d'intervention à la production de l'orge"),
]
RETROCESSION = [
    ("ble_dur_prix_normal", f"{CER}/prix_normal_retrocession/ble_dur.yaml",
     "Blé dur, prix normal (D/ql)", "Prix normal de rétrocession du blé dur"),
    ("ble_tendre_prix_normal", f"{CER}/prix_normal_retrocession/ble_tendre.yaml",
     "Blé tendre, prix normal (D/ql)", "Prix normal de rétrocession du blé tendre"),
    ("orge_prix_normal", f"{CER}/prix_normal_retrocession/orge.yaml",
     "Orge, prix normal (D/ql)", "Prix normal de rétrocession de l'orge"),
    ("ble_dur_prix_reduit", f"{CER}/prix_reduit_retrocession/ble_dur.yaml",
     "Blé dur, prix réduit (D/ql)", "Prix réduit de rétrocession du blé dur"),
    ("ble_tendre_prix_reduit", f"{CER}/prix_reduit_retrocession/ble_tendre.yaml",
     "Blé tendre, prix réduit (D/ql)", "Prix réduit de rétrocession du blé tendre"),
]
# (chemin, libellé de la taxe, unité d'assiette)
TAXES_AFFECTEES = [
    (f"{TAXES}/agrumes_fruits_exportes.yaml", "Taxe sur les agrumes et fruits exportés",
     "par kilogramme net"),
    (f"{TAXES}/perequation_raffinage/supercarburant.yaml",
     "Taxe de péréquation de raffinage, supercarburant", "par hectolitre"),
    (f"{TAXES}/perequation_raffinage/essence_normale.yaml",
     "Taxe de péréquation de raffinage, essence normale", "par hectolitre"),
    (f"{TAXES}/perequation_raffinage/gasoil.yaml",
     "Taxe de péréquation de raffinage, gas-oil", "par hectolitre"),
]

# Prix administrés : (clé = nom du paramètre, sous-dossier, libellé, unité de prix), par tableau.
_UNITE = {"currency/unit": "la pièce", "currency/kg": "le kilo",
          "currency/100kg": "le quintal", "currency/l": "le litre"}
PRIX_ADMINISTRES = {
    "prix_administres_pain.md": [
        ("gros_pain_700g", "pain", "Gros pain de 700 g"),
        ("gros_pain_600g", "pain", "Gros pain de 600 g"),
        ("gros_pain_500g", "pain", "Gros pain de 500 g"),
        ("petit_pain_300g", "pain", "Petit pain de 300 g"),
        ("petit_pain_250g", "pain", "Petit pain, puis baguette, de 250 g"),
    ],
    "prix_administres_farines_semoule.md": [
        ("farine_ps_quintal", "farine", "Farine PS, au quintal"),
        ("farine_ps_vrac", "farine", "Farine PS, en vrac"),
        ("farine_ps7_vrac", "farine", "Farine PS-7, en vrac"),
        ("farine_ps7_paquet_1kg", "farine", "Farine PS-7, paquet de 1 kg"),
        ("semoule_ps10_quintal", "semoule", "Semoule PS-10, au quintal"),
        ("semoule_ps10_vrac", "semoule", "Semoule PS-10, en vrac"),
    ],
    "prix_administres_pates_couscous.md": [
        ("pates_vrac_1975_1979", "pates", "Pâtes alimentaires, en vrac (décrets de 1975 et 1979)"),
        ("pates_ps10_vrac", "pates", "Pâtes alimentaires PS-10, en vrac"),
        ("couscous_vrac_1975_1979", "couscous", "Couscous rapide, en vrac (décrets de 1975 et 1979)"),
        ("couscous_ps10_vrac", "couscous", "Couscous rapide PS-10, en vrac"),
    ],
    "prix_administres_sucre_cafe.md": [
        ("sucre_poudre", "sucre", "Sucre en poudre"),
        ("sucre_morceaux", "sucre", "Sucre en morceaux"),
        ("sucre_brun", "sucre", "Sucre brun"),
        ("cafe", None, "Café"),
    ],
    "prix_administres_huile_lait.md": [
        ("huile_melange", "huile", "Huile mélangée, puis huile de mélange en vrac"),
        ("huile_graines_vrac", "huile", "Huile de graines en vrac"),
        ("lait_regenere_pasteurise_1l", "lait", "Lait régénéré pasteurisé, 1 l (1982)"),
        ("lait_regenere_uht_1l", "lait", "Lait régénéré UHT, 1 l (1982)"),
        ("lait_demi_ecreme_pasteurise_1l", "lait", "Lait régénéré demi-écrémé pasteurisé, 1 l"),
        ("lait_demi_ecreme_uht_1l", "lait", "Lait régénéré demi-écrémé UHT, 1 l"),
    ],
}


def chemin_pa(cle: str, dossier: str | None) -> str:
    return f"{PA}/{dossier}/{cle}.yaml" if dossier else f"{PA}/{cle}.yaml"


def unite_pa(chemin: str) -> str:
    unite = ((ot.charge_parametre(chemin) or {}).get("metadata") or {}).get("unit")
    if unite not in _UNITE:
        raise Ecart(f"unité inattendue {unite!r} : {chemin}")
    return _UNITE[unite]


# Le titre court d'un texte de prix : avant son objet, virgule ou non (« Arrêté du 17 février
# 1984 fixant le prix des farines »).
_OBJET_PA = re.compile(r",?\s+(fixant|portant|abrogeant|modifiant|instituant|complétant|"
                       r"relatif|relative)\b")


def tableau_prix_administres(specs) -> "object":
    """Une ligne par prix et par date de ses valeurs, dans l'ordre des paramètres."""
    import pandas as pd

    lignes = []
    for cle, dossier, libelle in specs:
        chemin = chemin_pa(cle, dossier)
        serie = ot.serie_datee(chemin)
        if not serie:
            raise Ecart(f"paramètre introuvable ou vide : {chemin}")
        ot.releve_note(chemin, f"Prix au public : {libelle[0].lower()}{libelle[1:]}")
        unite = "le paquet" if cle.endswith("_paquet_1kg") else unite_pa(chemin)
        for date, valeur, titre, lien in serie:
            if not titre:
                if valeur is not None:
                    raise Ecart(f"{chemin} au {date} : valeur sans texte")
                date_case, texte = date[:4], TIRET
            else:
                date_case = case_date([chemin], date)
                m = _OBJET_PA.search(titre)
                texte = ot.lien_reference(titre[:m.start()] if m else titre, lien, LANGUE)
            lignes.append({"Produit": libelle, "Date d'effet": date_case,
                           "Prix (D)": millimes(valeur), "Unité": unite, "Texte": texte})
    return pd.DataFrame(lignes)


def ecrire_serie_prix_administres() -> int:
    """La série longue des prix administrés ; une date sans texte n'a ni texte ni lien."""
    lignes, liens = [], []
    for specs in PRIX_ADMINISTRES.values():
        for cle, dossier, libelle in specs:
            chemin = chemin_pa(cle, dossier)
            serie = ot.serie_datee(chemin)
            if not serie:
                print(f"✗ {SERIE_PA} : paramètre introuvable ou vide : {chemin}")
                return 1
            for date, valeur, titre, lien in serie:
                if titre and not lien.startswith("https://www.pist.tn/"):
                    print(f"✗ {SERIE_PA} : {cle} au {date}, lien hors du Journal officiel")
                    return 1
                if not titre and valeur is not None:
                    print(f"✗ {SERIE_PA} : {cle} au {date}, valeur sans texte")
                    return 1
                lignes.append({"parametre": cle, "date_effet": date,
                               "valeur": None if valeur is None else round(valeur, 6),
                               "texte": titre, "lien": lien})
            liens.append((chemin, f"Prix au public : {libelle[0].lower()}{libelle[1:]}"))
    CACHE.mkdir(parents=True, exist_ok=True)
    ot.ecrire_csv_serie(CACHE / f"{SERIE_PA}.csv", lignes)
    ot.ecrire_fichier_liens(CACHE / f"{SERIE_PA}.liens.{LANGUE}.yml", liens, LANGUE)
    print(f"✓ série {SERIE_PA} : {len(lignes)} lignes, {len(liens)} paramètres")
    return 0


# Une note du paramètre qui dit que la date portée est une date de publication.
_PUBLICATION = re.compile(r"retenue comme date de publication|date de publication, non date "
                          r"d'effet", re.IGNORECASE)
# Le titre court d'un texte : ce qui précède son objet (« , fixant … »).
_OBJET = re.compile(r",\s+(fixant|portant|abrogeant|modifiant|instituant|complétant|relatif)\b")


class Ecart(ValueError):
    """Une lecture ne rend pas ce que le tableau affirme."""


def millimes(v: float | None) -> str:
    """Un prix en dinars, au millime : « 4,800 », « 156,456 » ; « — » sans valeur."""
    return TIRET if v is None else f"{v:,.3f}".replace(",", " ").replace(".", ",")


def titre_court(titre: str) -> str:
    m = _OBJET.search(titre)
    return titre[:m.start()] if m else titre


def references(chemin: str, date: str) -> list[tuple[str, str, str]]:
    """Toutes les références d'un paramètre à une date : (titre, lien, note)."""
    donnees = ot.charge_parametre(chemin) or {}
    meta = donnees.get("metadata") or {}
    sortie = []
    for cle, valeur in (meta.get("reference") or {}).items():
        if str(cle)[:10] != date:
            continue
        for ref in valeur if isinstance(valeur, list) else [valeur]:
            if isinstance(ref, dict):
                sortie.append((ref.get("title", ""), ref.get("href", ""), ref.get("note", "")))
    return sortie


def notes(chemin: str, date: str) -> list[str]:
    meta = (ot.charge_parametre(chemin) or {}).get("metadata") or {}
    sortie = []
    for cle, valeur in (meta.get("notes") or {}).items():
        if str(cle)[:10] == date:
            for n in valeur if isinstance(valeur, list) else [valeur]:
                sortie.append(n.get("note", "") if isinstance(n, dict) else str(n))
    return sortie


def date_publiee(chemins: list[str], date: str) -> bool:
    """Vrai si un paramètre lu à cette date dit qu'elle est une date de publication."""
    textes = [n for c in chemins for _t, _h, n in references(c, date)]
    textes += [n for c in chemins for n in notes(c, date)]
    return any(_PUBLICATION.search(t) for t in textes)


def case_date(chemins: list[str], date: str) -> str:
    jour = ot.formate_date(date, LANGUE)
    return f"publié le {jour}" if date_publiee(chemins, date) else jour


def case_texte(chemins: list[str], date: str, court: bool = True) -> str:
    """Le texte qui fixe la valeur à cette date, pour chaque paramètre lu, sans doublon.

    Seule la PREMIÈRE référence d'une date est retenue : c'est le texte qui fixe la valeur.
    Les suivantes sont des reconductions sans prix nouveau (décret n° 96-2549 pour les
    campagnes 1993-1994 et 1994-1995, par exemple) ou des décrets de récoltes antérieures
    publiés le même jour et non portés en valeur (2022) ; elles restent dans la base
    législative, mais ne fixent pas la case.
    """
    vus, liens = set(), []
    for chemin in chemins:
        for titre, lien, _note in references(chemin, date)[:1]:
            if not titre or titre in vus:
                continue
            vus.add(titre)
            liens.append(ot.lien_reference(titre_court(titre) if court else titre, lien, LANGUE))
    if not liens:
        raise Ecart(f"aucun texte cité au {date} par {chemins}")
    return " ; ".join(liens)


def tableau_prix(specs) -> "object":
    """Une ligne par date de changement d'un des prix ; chaque case, le prix en vigueur."""
    import pandas as pd

    series = {}
    for _cle, chemin, _entete, lien in specs:
        serie = ot.serie_datee(chemin)
        if not serie:
            raise Ecart(f"paramètre introuvable ou vide : {chemin}")
        series[chemin] = serie
        ot.releve_note(chemin, lien)
    dates = sorted({d for s in series.values() for d, *_ in s})
    lignes = []
    for date in dates:
        presents = [c for _k, c, _e, _l in specs if any(d == date for d, *_ in series[c])]
        ligne = {"Date d'effet": case_date(presents, date)}
        for _cle, chemin, entete, _lien in specs:
            point = ot.en_vigueur(series[chemin], date)
            ligne[entete] = millimes(None if point is None else point[1])
        ligne["Texte"] = case_texte(presents, date)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def tableau_taxes() -> "object":
    """Une ligne par taxe et par date de ses valeurs."""
    import pandas as pd

    lignes = []
    for chemin, libelle, assiette in TAXES_AFFECTEES:
        serie = ot.serie_datee(chemin)
        if not serie:
            raise Ecart(f"paramètre introuvable ou vide : {chemin}")
        ot.releve_note(chemin, libelle)
        for date, valeur, _titre, _lien in serie:
            lignes.append({
                "Taxe": libelle,
                "Montant": TIRET if valeur is None else f"{millimes(valeur)} D {assiette}",
                "Date d'effet": case_date([chemin], date),
                "Texte": case_texte([chemin], date, court=False),
            })
    return pd.DataFrame(lignes)


def entete(chemins: list[str]) -> str:
    return (f"<!-- Généré par scripts/{Path(__file__).name} — ne pas éditer à la main.\n"
            f"     Paramètres : {', '.join(chemins)} -->\n\n")


def ecrire(nom: str, fabrique) -> int:
    try:
        df, liens = ot.avec_liens(fabrique)
    except Ecart as erreur:
        print(f"✗ {LANGUE}/{nom} : {erreur}")
        return 1
    if df is None or df.empty:
        print(f"✗ {LANGUE}/{nom} : paramètre introuvable ou vide.")
        return 1
    erreur = ot.ecrire_dans_livres(RACINE, LANGUE, (LIVRE,), nom, df, liens,
                                   entete=entete([c for c, _l in liens]))
    if erreur:
        print(erreur)
        return 1
    print(f"✓ {nom} : {len(df)} lignes")
    return 0


def ecrire_serie() -> int:
    parametres = [ot.ParametreDate(cle, chemin, {LANGUE: entete_}, unite="millimes",
                                   lien={LANGUE: lien})
                  for cle, chemin, entete_, lien in PRODUCTION + RETROCESSION]
    return ot.ecrire_serie_parametres(SERIE, parametres, CACHE, langues=(LANGUE,))


def main() -> int:
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version {ot.version_openfisca()}, "
            f"minimum {ot.VERSION_MINIMALE}). Les snapshots existants sont conservés."
        )
        return 1
    SORTIE.mkdir(parents=True, exist_ok=True)
    return (ecrire("cereales_prix_production.md", lambda: tableau_prix(PRODUCTION))
            or ecrire("cereales_prix_retrocession.md", lambda: tableau_prix(RETROCESSION))
            or ecrire("caisse_taxes_affectees.md", tableau_taxes)
            or ecrire_serie()
            or next((1 for nom, specs in PRIX_ADMINISTRES.items()
                     if ecrire(nom, lambda specs=specs: tableau_prix_administres(specs))), 0)
            or ecrire_serie_prix_administres())


if __name__ == "__main__":
    raise SystemExit(main())

"""Régénère les snapshots des tableaux de paramètres du livre « La compensation ».

Même contrat que les autres générateurs : le build du site n'exécute PAS ce script, il lit les
fichiers qu'il produit, versionnés dans `precis/{fr,ar}/compensation/tables/` et
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

LES DEUX LANGUES. Chaque tableau est écrit en français et en arabe, des mêmes paramètres
(`MOTS`, et le dictionnaire `{langue: libellé}` de chaque grandeur). Les titres des textes
restent ceux des paramètres, en français ; en arabe, le lien pointe l'édition arabe du
fascicule (`ot.lien_reference`). Les séries longues n'ont de liens qu'en français : les
figures arabes ne sont pas encore écrites. Provenance des termes arabes : glossaire
(`precis/glossaire.yml`) pour les prix des céréales, la péréquation de raffinage et la taxe
affectée ; décret n° 72-400, art. 2, pour les carburants ; titre arabe du décret n° 75-352
(miroir iort du corpus) pour الدقيق، السميد، الخبز، العجين الغذائي، الكسكسي السريع ;
titres arabes de textes douaniers du même miroir, non de textes de prix, pour السكر، القهوة،
الحليب. Les éditions arabes des arrêtés de prix (1974-1991) n'ont pas de titre arabe au
`jort_cache` ni au miroir iort, et le fascicule arabe du 11 novembre 1989 n'a pas de couche
texte : les qualificatifs des produits restent à vérifier sur ces fascicules. Les autres termes
sont d'usage courant, sans attestation dans un texte arabe lu : chacun est signalé « non
attesté » à côté de sa définition.
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
LANGUE = "fr"  # langue des séries longues et de leurs liens
LANGUES = ("fr", "ar")
CACHE = RACINE / "_seriescache"
SERIE = "compensation-cereales-parametres"
TIRET = "—"
PA = f"{PS}/prix_administres_1974_1991"
SERIE_PA = "compensation-prix-administres"

# Mots des tableaux, par langue. Arabe : « بداية السريان » et « النصّ » sont les en-têtes des
# autres tableaux arabes du précis ; les autres en-têtes sont d'usage courant (non attestés).
MOTS = {
    "fr": {"date": "Date d'effet", "texte": "Texte", "publie": "publié le {jour}",
           "produit": "Produit", "prix": "Prix (D)", "unite": "Unité", "paquet": "le paquet",
           "taxe": "Taxe", "montant": "Montant", "dinar": "D",
           "prix_public": "Prix au public : {produit}"},
    "ar": {"date": "بداية السريان", "texte": "النصّ", "publie": "نُشر في {jour}",  # non attesté
           "produit": "المنتوج", "prix": "السعر (د)", "unite": "الوحدة",
           "paquet": "للعلبة",  # non attesté
           "taxe": "الأداء", "montant": "المبلغ", "dinar": "د",
           "prix_public": "سعر البيع للعموم: {produit}"},  # attesté : arrêté du 11 novembre 1989 (semoule)
}

# Céréales. Arabe : القمح الصلب، القمح اللين، الشعير et « للقنطار » (décret n° 2025-344,
# texte arabe du miroir iort) ; السعر الأساسي عند الإنتاج، سعر التدخّل، السعر العادي
# للإحالة، سعر الإحالة المخفّض (glossaire).
# (clé de la série, chemin, en-tête de colonne, libellé du lien « Base législative »)
PRODUCTION = [
    ("ble_dur_prix_base", f"{CER}/prix_base_production/ble_dur.yaml",
     {"fr": "Blé dur, prix de base (D/ql)", "ar": "القمح الصلب، السعر الأساسي (د/قنطار)"},
     {"fr": "Prix de base à la production du blé dur",
      "ar": "السعر الأساسي عند الإنتاج للقمح الصلب"}),
    ("ble_tendre_prix_base", f"{CER}/prix_base_production/ble_tendre.yaml",
     {"fr": "Blé tendre, prix de base (D/ql)", "ar": "القمح اللين، السعر الأساسي (د/قنطار)"},
     {"fr": "Prix de base à la production du blé tendre",
      "ar": "السعر الأساسي عند الإنتاج للقمح اللين"}),
    ("orge_prix_base", f"{CER}/prix_base_production/orge.yaml",
     {"fr": "Orge, prix de base (D/ql)", "ar": "الشعير، السعر الأساسي (د/قنطار)"},
     {"fr": "Prix de base à la production de l'orge",
      "ar": "السعر الأساسي عند الإنتاج للشعير"}),
    ("orge_prix_intervention", f"{CER}/prix_intervention_orge.yaml",
     {"fr": "Orge, prix d'intervention (D/ql)", "ar": "الشعير، سعر التدخّل (د/قنطار)"},
     {"fr": "Prix d'intervention à la production de l'orge",
      "ar": "سعر التدخّل عند الإنتاج للشعير"}),
]
RETROCESSION = [
    ("ble_dur_prix_normal", f"{CER}/prix_normal_retrocession/ble_dur.yaml",
     {"fr": "Blé dur, prix normal (D/ql)", "ar": "القمح الصلب، السعر العادي (د/قنطار)"},
     {"fr": "Prix normal de rétrocession du blé dur",
      "ar": "السعر العادي للإحالة للقمح الصلب"}),
    ("ble_tendre_prix_normal", f"{CER}/prix_normal_retrocession/ble_tendre.yaml",
     {"fr": "Blé tendre, prix normal (D/ql)", "ar": "القمح اللين، السعر العادي (د/قنطار)"},
     {"fr": "Prix normal de rétrocession du blé tendre",
      "ar": "السعر العادي للإحالة للقمح اللين"}),
    ("orge_prix_normal", f"{CER}/prix_normal_retrocession/orge.yaml",
     {"fr": "Orge, prix normal (D/ql)", "ar": "الشعير، السعر العادي (د/قنطار)"},
     {"fr": "Prix normal de rétrocession de l'orge", "ar": "السعر العادي للإحالة للشعير"}),
    ("ble_dur_prix_reduit", f"{CER}/prix_reduit_retrocession/ble_dur.yaml",
     {"fr": "Blé dur, prix réduit (D/ql)", "ar": "القمح الصلب، السعر المخفّض (د/قنطار)"},
     {"fr": "Prix réduit de rétrocession du blé dur",
      "ar": "سعر الإحالة المخفّض للقمح الصلب"}),
    ("ble_tendre_prix_reduit", f"{CER}/prix_reduit_retrocession/ble_tendre.yaml",
     {"fr": "Blé tendre, prix réduit (D/ql)", "ar": "القمح اللين، السعر المخفّض (د/قنطار)"},
     {"fr": "Prix réduit de rétrocession du blé tendre",
      "ar": "سعر الإحالة المخفّض للقمح اللين"}),
]
# (chemin, libellé de la taxe, unité d'assiette). Arabe : أداء التعديل في التكرير, الأداء
# على القوارص والغلال المصدّرة, « للهكتولتر » (glossaire) ; الوقود العالي، النفط الاعتيادي،
# القازوال (décret n° 72-400, art. 2) ; « للكلغ الصافي » non attesté.
TAXES_AFFECTEES = [
    (f"{TAXES}/agrumes_fruits_exportes.yaml",
     {"fr": "Taxe sur les agrumes et fruits exportés", "ar": "الأداء على القوارص والغلال المصدّرة"},
     {"fr": "par kilogramme net", "ar": "للكلغ الصافي"}),
    (f"{TAXES}/perequation_raffinage/supercarburant.yaml",
     {"fr": "Taxe de péréquation de raffinage, supercarburant",
      "ar": "أداء التعديل في التكرير، الوقود العالي"},
     {"fr": "par hectolitre", "ar": "للهكتولتر"}),
    (f"{TAXES}/perequation_raffinage/essence_normale.yaml",
     {"fr": "Taxe de péréquation de raffinage, essence normale",
      "ar": "أداء التعديل في التكرير، النفط الاعتيادي"},
     {"fr": "par hectolitre", "ar": "للهكتولتر"}),
    (f"{TAXES}/perequation_raffinage/gasoil.yaml",
     {"fr": "Taxe de péréquation de raffinage, gas-oil",
      "ar": "أداء التعديل في التكرير، القازوال"},
     {"fr": "par hectolitre", "ar": "للهكتولتر"}),
]

# Prix administrés : (clé = nom du paramètre, sous-dossier, libellé, unité de prix), par tableau.
# Arabe attesté : الخبز، الدقيق، السميد، العجين الغذائي، الكسكسي السريع (titre arabe du décret
# n° 75-352, miroir iort) ; السكر، القهوة، الحليب (titres arabes de textes douaniers du même
# miroir, non d'un texte de prix) ; « للقنطار » (décret n° 2025-344). Qualificatifs lus à l'image
# dans les arrêtés du 11 novembre 1989, édition arabe du JORT n° 77, pp. 1804-1807 : صبة (vrac),
# معلب كغ (paquet de 1 kg), الدقيق وزن نوعي الا 7 (farine PS-7), السميد وزن نوعي الا 10, العجين
# et كسكسي وزن نوعي 10-, سكر دقيق (poudre), سكر طوابع (morceaux), الزيت المخلط صبة, خبز وزن
# 500 / 250 غرام, الحليب المجدد النصف الدسم, حليب مبستر / معقم باكو لتر, سعر البيع للعموم.
# Encore non attestés : الخبز الكبير/الصغير (700, 600, 300 g), السكر الأسمر, زيت البذور
# (arrêtés de 1991), et les unités للوحدة، للكلغ، للتر.
_UNITE = {
    "fr": {"currency/unit": "la pièce", "currency/kg": "le kilo",
           "currency/100kg": "le quintal", "currency/l": "le litre"},
    "ar": {"currency/unit": "للوحدة", "currency/kg": "للكلغ",
           "currency/100kg": "للقنطار", "currency/l": "للتر"},
}


def _l(fr: str, ar: str) -> dict[str, str]:
    return {"fr": fr, "ar": ar}


PRIX_ADMINISTRES = {
    "prix_administres_pain.md": [
        ("gros_pain_700g", "pain", _l("Gros pain de 700 g", "الخبز الكبير، 700 غ")),
        ("gros_pain_600g", "pain", _l("Gros pain de 600 g", "الخبز الكبير، 600 غ")),
        ("gros_pain_500g", "pain", _l("Gros pain de 500 g", "خبز وزن 500 غرام")),
        ("petit_pain_300g", "pain", _l("Petit pain de 300 g", "الخبز الصغير، 300 غ")),
        ("petit_pain_250g", "pain", _l("Petit pain, puis baguette, de 250 g",
                                       "خبز وزن 250 غرام")),
    ],
    "prix_administres_farines_semoule.md": [
        ("farine_ps_quintal", "farine", _l("Farine PS, au quintal", "الدقيق PS، بالقنطار")),
        ("farine_ps_vrac", "farine", _l("Farine PS, en vrac", "الدقيق PS، صبة")),
        ("farine_ps7_vrac", "farine", _l("Farine PS-7, en vrac", "الدقيق وزن نوعي الا 7، صبة")),
        ("farine_ps7_paquet_1kg", "farine", _l("Farine PS-7, paquet de 1 kg",
                                               "الدقيق وزن نوعي الا 7، معلب 1 كغ")),
        ("semoule_ps10_quintal", "semoule", _l("Semoule PS-10, au quintal",
                                               "السميد وزن نوعي الا 10، بالقنطار")),
        ("semoule_ps10_vrac", "semoule", _l("Semoule PS-10, en vrac", "السميد وزن نوعي الا 10، صبة")),
    ],
    "prix_administres_pates_couscous.md": [
        ("pates_vrac_1975_1979", "pates",
         _l("Pâtes alimentaires, en vrac (décrets de 1975 et 1979)",
            "العجين الغذائي، صبة (أمر 1975 وأمر 1979)")),
        ("pates_ps10_vrac", "pates", _l("Pâtes alimentaires PS-10, en vrac",
                                        "العجين وزن نوعي 10-، صبة")),
        ("couscous_vrac_1975_1979", "couscous",
         _l("Couscous rapide, en vrac (décrets de 1975 et 1979)",
            "الكسكسي السريع، صبة (أمر 1975 وأمر 1979)")),
        ("couscous_ps10_vrac", "couscous", _l("Couscous rapide PS-10, en vrac",
                                              "كسكسي وزن نوعي 10-، صبة")),
    ],
    "prix_administres_sucre_cafe.md": [
        ("sucre_poudre", "sucre", _l("Sucre en poudre", "سكر دقيق")),
        ("sucre_morceaux", "sucre", _l("Sucre en morceaux", "سكر طوابع")),
        ("sucre_brun", "sucre", _l("Sucre brun", "السكر الأسمر")),
        ("cafe", None, _l("Café", "القهوة")),
    ],
    "prix_administres_huile_lait.md": [
        ("huile_melange", "huile", _l("Huile mélangée, puis huile de mélange en vrac",
                                      "الزيت المخلط، ثم الزيت المخلط صبة")),
        ("huile_graines_vrac", "huile", _l("Huile de graines en vrac", "زيت البذور صبة")),
        ("lait_regenere_pasteurise_1l", "lait",
         _l("Lait régénéré pasteurisé, 1 l (1982)", "الحليب المجدد المبستر، 1 لتر (1982)")),
        ("lait_regenere_uht_1l", "lait",
         _l("Lait régénéré UHT, 1 l (1982)", "الحليب المجدد المعقم، 1 لتر (1982)")),
        ("lait_demi_ecreme_pasteurise_1l", "lait",
         _l("Lait régénéré demi-écrémé pasteurisé, 1 l",
            "الحليب المجدد النصف الدسم، مبستر باكو لتر")),
        ("lait_demi_ecreme_uht_1l", "lait",
         _l("Lait régénéré demi-écrémé UHT, 1 l", "الحليب المجدد النصف الدسم، معقم باكو لتر")),
    ],
}


def chemin_pa(cle: str, dossier: str | None) -> str:
    return f"{PA}/{dossier}/{cle}.yaml" if dossier else f"{PA}/{cle}.yaml"


def unite_pa(chemin: str, langue: str) -> str:
    unite = ((ot.charge_parametre(chemin) or {}).get("metadata") or {}).get("unit")
    if unite not in _UNITE[langue]:
        raise Ecart(f"unité inattendue {unite!r} : {chemin}")
    return _UNITE[langue][unite]


def lien_pa(libelle: dict[str, str], langue: str) -> str:
    """Libellé « Base législative » d'un prix administré : « Prix au public : sucre brun »."""
    texte = libelle[langue]
    if langue == "fr":
        texte = f"{texte[0].lower()}{texte[1:]}"
    return MOTS[langue]["prix_public"].format(produit=texte)


# Le titre court d'un texte de prix : avant son objet, virgule ou non (« Arrêté du 17 février
# 1984 fixant le prix des farines »).
_OBJET_PA = re.compile(r",?\s+(fixant|portant|abrogeant|modifiant|instituant|complétant|"
                       r"relatif|relative)\b")


def tableau_prix_administres(specs, langue: str) -> "object":
    """Une ligne par prix et par date de ses valeurs, dans l'ordre des paramètres."""
    import pandas as pd

    m = MOTS[langue]
    lignes = []
    for cle, dossier, libelle in specs:
        chemin = chemin_pa(cle, dossier)
        serie = ot.serie_datee(chemin)
        if not serie:
            raise Ecart(f"paramètre introuvable ou vide : {chemin}")
        ot.releve_note(chemin, lien_pa(libelle, langue))
        unite = m["paquet"] if cle.endswith("_paquet_1kg") else unite_pa(chemin, langue)
        for date, valeur, titre, lien in serie:
            if not titre:
                if valeur is not None:
                    raise Ecart(f"{chemin} au {date} : valeur sans texte")
                date_case, texte = date[:4], TIRET
            else:
                date_case = case_date([chemin], date, langue)
                objet = _OBJET_PA.search(titre)
                texte = ot.lien_reference(titre[:objet.start()] if objet else titre, lien,
                                          langue)
            lignes.append({m["produit"]: libelle[langue], m["date"]: date_case,
                           m["prix"]: millimes(valeur), m["unite"]: unite, m["texte"]: texte})
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
            liens.append((chemin, lien_pa(libelle, LANGUE)))
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


def case_date(chemins: list[str], date: str, langue: str) -> str:
    jour = ot.formate_date(date, langue)
    return MOTS[langue]["publie"].format(jour=jour) if date_publiee(chemins, date) else jour


def case_texte(chemins: list[str], date: str, langue: str, court: bool = True) -> str:
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
            liens.append(ot.lien_reference(titre_court(titre) if court else titre, lien, langue))
    if not liens:
        raise Ecart(f"aucun texte cité au {date} par {chemins}")
    return " ; ".join(liens)


def tableau_prix(specs, langue: str) -> "object":
    """Une ligne par date de changement d'un des prix ; chaque case, le prix en vigueur."""
    import pandas as pd

    m = MOTS[langue]
    series = {}
    for _cle, chemin, _entete, lien in specs:
        serie = ot.serie_datee(chemin)
        if not serie:
            raise Ecart(f"paramètre introuvable ou vide : {chemin}")
        series[chemin] = serie
        ot.releve_note(chemin, lien[langue])
    dates = sorted({d for s in series.values() for d, *_ in s})
    lignes = []
    for date in dates:
        presents = [c for _k, c, _e, _l in specs if any(d == date for d, *_ in series[c])]
        ligne = {m["date"]: case_date(presents, date, langue)}
        for _cle, chemin, entete, _lien in specs:
            point = ot.en_vigueur(series[chemin], date)
            ligne[entete[langue]] = millimes(None if point is None else point[1])
        ligne[m["texte"]] = case_texte(presents, date, langue)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def tableau_taxes(langue: str) -> "object":
    """Une ligne par taxe et par date de ses valeurs."""
    import pandas as pd

    m = MOTS[langue]
    lignes = []
    for chemin, libelle, assiette in TAXES_AFFECTEES:
        serie = ot.serie_datee(chemin)
        if not serie:
            raise Ecart(f"paramètre introuvable ou vide : {chemin}")
        ot.releve_note(chemin, libelle[langue])
        for date, valeur, _titre, _lien in serie:
            montant = (TIRET if valeur is None
                       else f"{millimes(valeur)} {m['dinar']} {assiette[langue]}")
            lignes.append({
                m["taxe"]: libelle[langue],
                m["montant"]: montant,
                m["date"]: case_date([chemin], date, langue),
                m["texte"]: case_texte([chemin], date, langue, court=False),
            })
    return pd.DataFrame(lignes)


def entete(chemins: list[str]) -> str:
    return (f"<!-- Généré par scripts/{Path(__file__).name} — ne pas éditer à la main.\n"
            f"     Paramètres : {', '.join(chemins)} -->\n\n")


def ecrire(nom: str, fabrique) -> int:
    """Écrit le tableau dans chaque langue ; `fabrique(langue)` le compose."""
    for langue in LANGUES:
        try:
            df, liens = ot.avec_liens(lambda: fabrique(langue))
        except Ecart as erreur:
            print(f"✗ {langue}/{nom} : {erreur}")
            return 1
        if df is None or df.empty:
            print(f"✗ {langue}/{nom} : paramètre introuvable ou vide.")
            return 1
        erreur = ot.ecrire_dans_livres(RACINE, langue, (LIVRE,), nom, df, liens,
                                       entete=entete([c for c, _l in liens]))
        if erreur:
            print(erreur)
            return 1
    print(f"✓ {nom} : {len(df)} lignes ({', '.join(LANGUES)})")
    return 0


def ecrire_serie() -> int:
    parametres = [ot.ParametreDate(cle, chemin, entete_, unite="millimes", lien=lien)
                  for cle, chemin, entete_, lien in PRODUCTION + RETROCESSION]
    return ot.ecrire_serie_parametres(SERIE, parametres, CACHE, langues=(LANGUE,))


def main() -> int:
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version {ot.version_openfisca()}, "
            f"minimum {ot.VERSION_MINIMALE}). Les snapshots existants sont conservés."
        )
        return 1
    return (ecrire("cereales_prix_production.md", lambda langue: tableau_prix(PRODUCTION, langue))
            or ecrire("cereales_prix_retrocession.md", lambda langue: tableau_prix(RETROCESSION, langue))
            or ecrire("caisse_taxes_affectees.md", tableau_taxes)
            or ecrire_serie()
            or next((1 for nom, specs in PRIX_ADMINISTRES.items()
                     if ecrire(nom, lambda langue, specs=specs: tableau_prix_administres(specs, langue))),
                    0)
            or ecrire_serie_prix_administres())


if __name__ == "__main__":
    raise SystemExit(main())

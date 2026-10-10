"""Régénère les snapshots des tableaux du livre « Les finances locales ».

Même contrat que les autres générateurs : le build du site n'exécute PAS ce script, il lit
les fichiers qu'il produit, versionnés dans `precis/{fr,ar}/finances_locales/tables/`.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_finances_locales_tables.py

CE QUI EST ENGENDRÉ — les barèmes des deux taxes sur les immeubles (`fiscalite_locale/`,
versé en 0.125), pour le chapitre « Les impôts sur les immeubles » :
  - `tib_taux_dates_reperes.md` : les quatre taux de la taxe sur les immeubles bâtis selon
    le nombre de services, par le composant commun `ot.ecrire_dates_reperes` ;
  - `tib_prix_reference.md` : le minimum et le maximum du prix de référence du mètre carré
    couvert, une ligne par catégorie de superficie, une colonne par grandeur et par date ;
  - `tnb_tarif.md` : le tarif au mètre carré de la taxe sur les terrains non bâtis, une
    ligne par zone de densité, une colonne par date ;
  - deux séries longues au cache `precis/_seriescache/`, par le composant commun
    `ot.ecrire_serie_parametres` : `fl-tib-prix-reference` (huit grandeurs, le minimum et le
    maximum de chaque catégorie) et `fl-tnb-tarif` (trois zones), une ligne par grandeur et
    par date d'effet, avec le texte et son lien au Journal officiel. Les figures en escalier
    du chapitre les lisent par `figtools.series()` ; chacune a sa série, donc ses propres
    liens « Base législative ».

LA FORME DES DEUX BARÈMES. `ot.tableau_dates_reperes` met un paramètre par ligne ; ici une
ligne réunit plusieurs paramètres — le minimum et le maximum d'une même catégorie —, et le
barème se lit à ses dates d'effet, côte à côte. `tableau_cote_a_cote` le compose avec les
briques communes (`ParametreDate`, `etat_a_la_date`, relevé des liens). L'unité est dans
l'en-tête, la case ne porte que le nombre — y compris le mètre carré des catégories : sous
ses onglets, le tableau à sept colonnes n'a que 662 px à 1 300 px de fenêtre, et la première
cellule d'un tableau engendré ne se replie pas.

LES EN-TÊTES RENVOIENT AU REGISTRE DU CHAPITRE. Chaque colonne porte l'année de sa date
d'effet, en lien vers la ligne du registre replié qui donne le décret, son article et sa
page (`ANCRES_PRIX`, `ANCRES_TARIF`). Ces ancres sont déclarées ici, date par date : une
date d'effet que le modèle porte et qui n'a pas sa ligne de registre arrête le générateur,
plutôt que de publier une colonne sans référence.

CE QUI NE L'EST PAS. Les registres des décrets (dates d'effet, abrogations, pages) restent
écrits dans le chapitre : ils portent les références. Le taux d'assiette (2 %) et le taux
sur la valeur vénale (0,3 %) sont donnés en prose, avec leur article. La taxe sur les
établissements, la taxe hôtelière et les droits ne sont pas encore dans l'arbre.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

FL = "parameters/fiscalite_locale"
TIB = f"{FL}/taxe_immeubles_batis"
TNB = f"{FL}/taxe_terrains_non_batis"
RACINE = Path(__file__).parent.parent / "precis"
LIVRE = "finances_locales"
LANGUES = ("fr", "ar")
CACHE = RACINE / "_seriescache"
SERIE_PRIX = "fl-tib-prix-reference"
SERIE_TARIF = "fl-tnb-tarif"

# Date d'effet -> ancre de la ligne du registre replié, dans `_impots_immeubles.qmd`.
ANCRES_PRIX = {"1997-03-13": "r-fl-imm-prix-1997", "2008-01-01": "r-fl-imm-prix-2008",
               "2017-01-01": "r-fl-imm-prix-2017"}
ANCRES_TARIF = {"1997-03-13": "r-fl-imm-tarif-1997", "2008-01-01": "r-fl-imm-tarif-2008",
                "2017-01-01": "r-fl-imm-tarif-2017"}

# Le code entre en vigueur le 1er janvier 1997 ; les quatre taux n'ont pas changé depuis.
EFFET_TAUX = "1997-01-01"
PALIERS = ("un_ou_deux_services", "trois_ou_quatre_services", "plus_de_quatre_services",
           "plus_de_quatre_services_et_autres_services")
CATEGORIES = (1, 2, 3, 4)
ZONES = ("haute", "moyenne", "basse")

# Libellés arabes : noms des taxes et du prix de référence d'après le glossaire ; zones et
# paliers de services d'après l'édition arabe du Journal officiel, que citent les notes des
# paramètres.
MOTS = {
    "fr": {
        "services": "Services dont bénéficie l'immeuble",
        "taux": "Taux $\\tau$<br>(% de l'assiette)",
        "un_ou_deux_services": "un ou deux",
        "trois_ou_quatre_services": "trois ou quatre",
        "plus_de_quatre_services": "plus de quatre",
        "plus_de_quatre_services_et_autres_services":
            "plus de quatre, et services supplémentaires",
        "taux_lien": "Taux de la taxe sur les immeubles bâtis — {palier}",
        "lien_un_ou_deux_services": "un ou deux services",
        "lien_trois_ou_quatre_services": "trois ou quatre services",
        "lien_plus_de_quatre_services": "plus de quatre services",
        "lien_plus_de_quatre_services_et_autres_services":
            "plus de quatre services et d'autres services",
        "categorie": "Catégorie<br>(superficie couverte, m²)",
        "jusqu_a": "{n} : jusqu'à {b}", "de_a": "{n} : de {a} à {b}",
        "plus_de": "{n} : plus de {a}",
        "minimum": "Minimum", "maximum": "Maximum", "unite": "(D/m²)",
        "prix_lien": "{borne} du prix de référence du mètre carré couvert — catégorie {n}",
        "seuil_lien": "Superficie couverte maximale de la catégorie {n}",
        "zone": "Zone du plan d'aménagement urbain",
        "haute": "haute densité", "moyenne": "moyenne densité", "basse": "basse densité",
        "tarif": "Tarif",
        "tarif_lien": "Tarif au mètre carré de la taxe sur les terrains non bâtis — zone à {zone}",
    },
    "ar": {
        "services": "الخدمات التي ينتفع بها العقار",
        "taux": "النسبة $\\tau$<br>(% من الوعاء)",
        "un_ou_deux_services": "خدمة أو خدمتان",
        "trois_ou_quatre_services": "ثلاث أو أربع خدمات",
        "plus_de_quatre_services": "أكثر من أربع خدمات",
        "plus_de_quatre_services_et_autres_services": "أكثر من أربع خدمات وخدمات أخرى",
        "taux_lien": "نسبة المعلوم على العقارات المبنية — {palier}",
        "lien_un_ou_deux_services": "خدمة أو خدمتان",
        "lien_trois_ou_quatre_services": "ثلاث أو أربع خدمات",
        "lien_plus_de_quatre_services": "أكثر من أربع خدمات",
        "lien_plus_de_quatre_services_et_autres_services": "أكثر من أربع خدمات وخدمات أخرى",
        "categorie": "الصنف<br>(المساحة المغطاة، م²)",
        "jusqu_a": "{n}: إلى {b}", "de_a": "{n}: من {a} إلى {b}",
        "plus_de": "{n}: أكثر من {a}",
        "minimum": "الحد الأدنى", "maximum": "الحد الأقصى", "unite": "(د/م²)",
        "prix_lien": "{borne} للثمن المرجعي للمتر المربع المبني — الصنف {n}",
        "seuil_lien": "المساحة المغطاة القصوى للصنف {n}",
        "zone": "المنطقة حسب مثال التهيئة العمرانية",
        "haute": "كثافة عمرانية مرتفعة", "moyenne": "كثافة عمرانية متوسطة",
        "basse": "كثافة عمرانية منخفضة",
        "tarif": "المبلغ",
        "tarif_lien": "مبلغ المعلوم على الأراضي غير المبنية للمتر المربع — منطقة ذات {zone}",
    },
}


def pourcentage_nu(valeur: float, _langue: str) -> str:
    """Un taux sans son signe : « 8 », l'unité étant dans l'en-tête de la colonne."""
    return f"{valeur * 100:.4f}".rstrip("0").rstrip(".").replace(".", ",")


def entier_nu(valeur: float, _langue: str) -> str:
    """Un montant en dinars entiers, sans unité ; un montant à millimes arrête le générateur."""
    if not float(valeur).is_integer():
        raise ValueError(f"montant non entier : {valeur}")
    return f"{int(valeur):,}".replace(",", " ")


def millimes_nus(valeur: float, _langue: str) -> str:
    """Un montant au millime, sans unité : « 0,300 », comme l'écrit le Journal officiel."""
    return f"{valeur:,.3f}".replace(",", " ").replace(".", ",")


def tous(champ: str, **valeurs) -> dict[str, str]:
    """Le libellé `champ`, complété par `valeurs`, dans chaque langue."""
    return {l: MOTS[l][champ].format(**{c: (MOTS[l][v] if v in MOTS[l] else v)
                                        for c, v in valeurs.items()}) for l in LANGUES}


def parametres_taux() -> list:
    return [ot.ParametreDate(p, f"{TIB}/taux/{p}.yaml", tous(p), format=pourcentage_nu,
                             lien=tous("taux_lien", palier=f"lien_{p}")) for p in PALIERS]


def parametre_prix(categorie: int, borne: str):
    return ot.ParametreDate(
        f"categorie_{categorie}_{borne}",
        f"{TIB}/prix_reference/categorie_{categorie}/{borne}.yaml", tous(borne),
        format=entier_nu, lien=tous("prix_lien", borne=borne, n=str(categorie)))


def parametre_seuil(categorie: int):
    libelle = tous("seuil_lien", n=str(categorie))
    return ot.ParametreDate(f"seuil_{categorie}",
                            f"{TIB}/seuils_superficie/categorie_{categorie}.yaml",
                            libelle, format=entier_nu)


def parametre_tarif(zone: str):
    return ot.ParametreDate(zone, f"{TNB}/tarif_m2/{zone}_densite.yaml", tous(zone),
                            format=millimes_nus, lien=tous("tarif_lien", zone=zone))


def libelles_categories(dates: list[str], langue: str) -> list[str]:
    """Les quatre lignes du barème, bornées par les seuils de superficie du code.

    Le libellé n'a pas de date : il n'est écrit que si chaque seuil a la même valeur à
    toutes les dates du tableau. Un seuil qui changerait appellerait une autre forme.
    """
    m = MOTS[langue]
    seuils = []
    for categorie in CATEGORIES[:-1]:
        p = parametre_seuil(categorie)
        serie = p.serie()
        etats = {ot.etat_a_la_date(serie, d) for d in dates}
        if len(etats) != 1 or None in etats:
            raise ValueError(f"seuil de la catégorie {categorie} : états {sorted(map(str, etats))} "
                             f"aux dates {dates}")
        ot.releve_note(p.chemin, p.lien[langue])
        seuils.append(p.rendre(etats.pop(), langue))
    libelles = [m["jusqu_a"].format(n=1, b=seuils[0])]
    libelles += [m["de_a"].format(n=i + 2, a=seuils[i], b=seuils[i + 1])
                 for i in range(len(seuils) - 1)]
    libelles.append(m["plus_de"].format(n=len(seuils) + 1, a=seuils[-1]))
    return libelles


def tableau_cote_a_cote(lignes: list[tuple[str, list]], grandeurs: list[str],
                        ancres: dict[str, str], entete: str, unite: str, langue: str):
    """Un barème à ses dates d'effet, côte à côte : une colonne par grandeur et par date.

    `lignes` : [(libellé de ligne, [un `ParametreDate` par grandeur])]. `grandeurs` : les
    en-têtes des grandeurs, dans l'ordre des paramètres d'une ligne. `ancres` : date d'effet
    -> ancre du registre du chapitre ; ses dates sont les colonnes. Chaque date d'effet
    d'un paramètre doit y figurer, et chaque date déclarée être une date d'effet : le
    tableau ne passe sous silence aucun texte que le modèle porte, et n'en annonce aucun
    qu'il ne porte pas.
    """
    import pandas as pd

    dates = sorted(ancres)
    series = {}
    for _libelle, parametres in lignes:
        for p in parametres:
            series[p.chemin] = p.serie()
            if not series[p.chemin]:
                print(f"✗ paramètre introuvable ou vide : {p.chemin}")
                return None
            effets = {d for d, *_ in series[p.chemin]}
            if effets != set(dates):
                raise ValueError(f"{p.chemin} : dates d'effet {sorted(effets)}, "
                                 f"registre du chapitre {dates}")
    sortie = []
    for libelle, parametres in lignes:
        ligne = {entete: libelle}
        for date in dates:
            for grandeur, p in zip(grandeurs, parametres):
                ot.releve_note(p.chemin, p.lien[langue])
                colonne = f"{grandeur}<br>[{date[:4]}](#{ancres[date]})<br>{unite}"
                ligne[colonne] = p.rendre(ot.etat_a_la_date(series[p.chemin], date), langue)
        sortie.append(ligne)
    return pd.DataFrame(sortie)


def tableau_prix(langue: str):
    m = MOTS[langue]
    libelles = libelles_categories(sorted(ANCRES_PRIX), langue)
    lignes = [(libelle, [parametre_prix(c, "minimum"), parametre_prix(c, "maximum")])
              for libelle, c in zip(libelles, CATEGORIES)]
    return tableau_cote_a_cote(lignes, [m["minimum"], m["maximum"]], ANCRES_PRIX,
                               m["categorie"], m["unite"], langue)


def tableau_tarif(langue: str):
    m = MOTS[langue]
    lignes = [(m[z], [parametre_tarif(z)]) for z in ZONES]
    return tableau_cote_a_cote(lignes, [m["tarif"]], ANCRES_TARIF, m["zone"], m["unite"],
                               langue)


def entete_snapshot(dates: list[str], chemins: list[str]) -> str:
    return (f"<!-- Généré par scripts/{Path(__file__).name} — ne pas éditer à la main.\n"
            f"     État en vigueur aux dates d'effet : {', '.join(dates)}.\n"
            f"     Paramètres : {', '.join(chemins)} -->\n\n")


def ecrire_cote_a_cote(nom: str, fabrique, ancres: dict[str, str]) -> int:
    for langue in LANGUES:
        try:
            df, liens = ot.avec_liens(lambda: fabrique(langue))
        except ValueError as erreur:
            print(f"✗ {langue}/{nom} : {erreur}")
            return 1
        if df is None or df.empty:
            print(f"✗ {langue}/{nom} : paramètre introuvable ou vide.")
            return 1
        erreur = ot.ecrire_dans_livres(
            RACINE, langue, (LIVRE,), nom, df, liens,
            entete=entete_snapshot(sorted(ancres), [c for c, _l in liens]))
        if erreur:
            print(erreur)
            return 1
    print(f"✓ {nom} : {len(df)} lignes, {len(df.columns) - 1} colonnes")
    return 0


def ecrire_taux() -> int:
    """Les quatre taux à la date d'entrée en vigueur du code, qui est aussi leur seule date."""
    parametres = parametres_taux()
    for p in parametres:
        effets = [d for d, *_ in p.serie()]
        if effets != [EFFET_TAUX]:
            print(f"✗ tib_taux : {p.chemin} a pour dates d'effet {effets}, et non la seule "
                  f"{EFFET_TAUX} : le tableau à une colonne ne suffit plus.")
            return 1
    code = ot.ecrire_dates_reperes(
        RACINE, LIVRE, "tib_taux", parametres, [EFFET_TAUX],
        entete={l: MOTS[l]["services"] for l in LANGUES},
        entetes_dates={l: {EFFET_TAUX: MOTS[l]["taux"]} for l in LANGUES},
        generateur=Path(__file__).name)
    if not code:
        print(f"✓ tib_taux_dates_reperes.md : {len(parametres)} taux")
    return code


def ecrire_series() -> int:
    """Les deux barèmes en séries longues, que tracent les figures en escalier du chapitre."""
    prix = [parametre_prix(c, borne) for c in CATEGORIES for borne in ("minimum", "maximum")]
    tarif = [parametre_tarif(z) for z in ZONES]
    return (ot.ecrire_serie_parametres(SERIE_PRIX, prix, CACHE)
            or ot.ecrire_serie_parametres(SERIE_TARIF, tarif, CACHE))


def main() -> int:
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version {ot.version_openfisca()}, "
            f"minimum {ot.VERSION_MINIMALE}). Les snapshots existants sont conservés."
        )
        return 1
    return (ecrire_taux()
            or ecrire_cote_a_cote("tib_prix_reference.md", tableau_prix, ANCRES_PRIX)
            or ecrire_cote_a_cote("tnb_tarif.md", tableau_tarif, ANCRES_TARIF)
            or ecrire_series())


if __name__ == "__main__":
    raise SystemExit(main())

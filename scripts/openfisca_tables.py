"""Construction des tableaux de barèmes à partir des paramètres openfisca.

Pendant tunisien de `quarto/openfisca_tables/core.py` du dépôt `conversion_precis_ipp`,
adapté à ce dont le précis a besoin : des **barèmes à tranches** (`brackets:`), là où le
module d'origine ne traite que des paramètres scalaires (`values:`).

Principe, aligné sur celui de `figtools.py` : **le build du site est autonome.**
`openfisca-tunisia` n'est pas une dépendance déclarée du précis. Les tableaux publiés
proviennent de snapshots Markdown versionnés (`precis/fr/fiscalite/tables/`), régénérés à
la demande par `scripts/generate_bareme_tables.py`. Quand une version suffisante
d'openfisca-tunisia est installée, `get_table_or_static` bascule automatiquement sur la
lecture directe des paramètres.

UNE SEULE SOURCE DE PARAMÈTRES. Depuis la version 0.93, openfisca-tunisia porte l'arbre
entier, retraites comprises : openfisca-tunisia-pension y a été fusionné. Les deux systèmes
socio-fiscaux qu'il livre n'en lisent chacun qu'une partie, mais le précis, qui lit les
fichiers YAML et non les systèmes, n'a plus qu'un paquet, une variable d'environnement et un
garde-fou de version. Avant la fusion, il en tenait deux, qui ne se suivaient pas.

Garde-fou de version. Les paramètres n'ont atteint leur état actuel qu'en 0.71 : le barème
1990-2016 était amputé de sa tranche supérieure jusqu'en 0.68 (openfisca-tunisia#380), les
tarifs de la contribution personnelle d'État n'existaient pas avant 0.69 (#381), et une
dizaine de valeurs d'assiette étaient fausses ou mal datées jusqu'en 0.70 (#382). En deçà de
`VERSION_MINIMALE`, on refuse la lecture directe et on retombe sur le snapshot.
"""

from __future__ import annotations

import datetime
import os
import re
from pathlib import Path
from typing import Any, Callable

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

try:
    import pandas as pd
except ImportError:  # pragma: no cover
    pd = None


# Les paramètres du précis proviennent d'un seul paquet depuis la fusion des dépôts : voir
# l'en-tête. Le dictionnaire est gardé pour que les lecteurs acceptent toujours un argument
# `paquet` explicite.
PAQUETS = {
    "openfisca_tunisia": {
        "variable": "OPENFISCA_TUNISIA_PATH",
        "distribution": "openfisca-tunisia",
        # 0.93 est la version de la fusion : `parameters/retraite/` n'existe pas en deçà, et
        # le livre « Retraites » ne pourrait pas être engendré. L'arbre de retraite qu'elle
        # apporte est celui d'openfisca-tunisia-pension 7.3.0, qui avait lui-même son
        # histoire de garde-fous — daté et sourcé sur le Journal officiel depuis 5.7, deux
        # chemins déplacés en 6.0 et 7.0, les âges militaires versés en 7.2. La 0.93 les
        # porte tous. La 0.95 verse le barème d'actualisation des salaires du régime non
        # agricole (openfisca-tunisia#438), dont le livre « Retraites » tire une figure : en
        # deçà, `retraite/rsna/salaire_reference/actualisation/` n'existe pas. La 0.99 verse
        # la limite de six SMIG du salaire de référence du RSNA (openfisca-tunisia#442), que
        # le générateur des retraites lit pour la figure de la limite de calcul : en deçà,
        # `retraite/rsna/salaire_reference/limite_multiple_smig` n'existe pas.
        "version_minimale": (0, 99),
    },
}

PAQUET_DEFAUT = "openfisca_tunisia"
_paquet_courant = PAQUET_DEFAUT

VERSION_MINIMALE = PAQUETS[PAQUET_DEFAUT]["version_minimale"]


def utiliser_paquet(nom: str) -> None:
    """Désigne le paquet lu par défaut. Un générateur l'appelle une fois, en tête.

    Les lecteurs acceptent aussi un argument `paquet` explicite ; ce réglage global
    évite de le répéter à chaque appel dans un script qui ne lit qu'une source.
    """
    if nom not in PAQUETS:
        msg = f"Paquet inconnu : {nom}. Connus : {', '.join(PAQUETS)}."
        raise ValueError(msg)
    global _paquet_courant
    _paquet_courant = nom

MESSAGE_INDISPONIBLE = (
    "*Tableau non disponible : ni openfisca-tunisia installé, ni snapshot statique.*"
)


# --------------------------------------------------------------------------- accès


def _racine_paquet(paquet: str | None = None):
    """Racine des sources d'un paquet openfisca, ou None.

    Cherche d'abord le paquet installé, puis un checkout désigné par sa variable
    d'environnement (utilisée pour régénérer les snapshots depuis une copie de travail
    non publiée).
    """
    nom = paquet or _paquet_courant
    try:
        import importlib.resources

        return importlib.resources.files(nom)
    except Exception:
        pass
    chemin = os.environ.get(PAQUETS[nom]["variable"])
    if chemin:
        racine = Path(chemin) / nom
        if racine.is_dir():
            return racine
    return None


def version_openfisca(paquet: str | None = None) -> tuple[int, ...] | None:
    """Version du paquet disponible, sous forme de tuple, ou None."""
    nom = paquet or _paquet_courant
    try:
        from importlib.metadata import version

        return tuple(int(x) for x in version(PAQUETS[nom]["distribution"]).split(".")[:2])
    except Exception:
        pass
    racine = _racine_paquet(nom)
    if racine is None:
        return None
    # Copie de travail : lire la version dans le pyproject.toml voisin.
    try:
        pyproject = Path(str(racine)).parent / "pyproject.toml"
        for ligne in pyproject.read_text(encoding="utf-8").splitlines():
            if ligne.startswith("version"):
                brut = ligne.split("=", 1)[1].strip().strip('"').strip("'")
                return tuple(int(x) for x in brut.split(".")[:2])
    except Exception:
        return None
    return None


def openfisca_utilisable(paquet: str | None = None) -> bool:
    """Vrai si le paquet est disponible ET assez récent pour être lu."""
    nom = paquet or _paquet_courant
    if yaml is None or _racine_paquet(nom) is None:
        return False
    version = version_openfisca(nom)
    return version is not None and version >= PAQUETS[nom]["version_minimale"]


# ------------------------------------------------ base législative en ligne des tableaux

# LE LECTEUR REMONTE DE LA VALEUR À SA SOURCE. Chaque tableau engendré est accompagné d'une
# liste de liens, un par grandeur, vers la page publique qui en donne toutes les valeurs
# datées et leurs références. Le générateur ouvre un relevé avant de fabriquer un tableau ;
# les fonctions qui lisent une série y notent le chemin et l'en-tête de colonne ; le relevé
# est écrit à côté du tableau (`<nom>.liens.yml`) et `markdown_avec_legende` en fait un
# onglet. Le lien est engendré comme la valeur : jamais écrit à la main.
#
# Un générateur n'appelle que deux fonctions : `avec_liens(fabrique)`, qui fabrique le
# tableau sous relevé, puis `ecrire_tableau(...)`, qui écrit le snapshot et ses liens. Une
# lecture qui ne passe pas par un tableau à en-têtes — un barème, un total parcourant une
# arborescence — se note à la main par `releve_note(chemin, libellé)`.
BASE_LEGISLATIVE = "https://parameters.tn.tax-benefit.org"
_releve: dict[str, str | None] | None = None


def url_parametre(chemin_relatif: str, langue: str = "fr") -> str:
    """Vue en tableau d'un paramètre : `parameters/a/b.yaml` -> `…/parameters/a.b/table/`."""
    nom = chemin_relatif.removeprefix("parameters/").removesuffix(".yaml").replace("/", ".")
    prefixe = "/ar" if langue == "ar" else ""
    return f"{BASE_LEGISLATIVE}{prefixe}/parameters/{nom}/table/"


def releve_debut() -> None:
    global _releve
    _releve = {}


def releve_note(chemin_relatif: str, libelle: str | None = None) -> None:
    """Note un paramètre lu par le tableau en cours ; un libellé explicite l'emporte."""
    if _releve is None:
        return
    if libelle:
        libelle = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", libelle).strip()
    if libelle or chemin_relatif not in _releve:
        _releve[chemin_relatif] = libelle or _releve.get(chemin_relatif)


def releve_fin() -> list[tuple[str, str | None]]:
    global _releve
    liens, _releve = list((_releve or {}).items()), None
    return liens


def ecrire_liens(chemin_tableau: str | Path, liens: list[tuple[str, str | None]],
                 langue: str) -> None:
    """Écrit `<nom>.liens.yml` à côté du tableau. Tout lien doit porter un libellé."""
    sans = [c for c, l in liens if not l]
    if sans:
        raise ValueError(f"paramètre lu sans libellé : {sans}")
    fichier = Path(chemin_tableau).with_suffix(".liens.yml")
    fichier.write_text(yaml.safe_dump(
        [{"libelle": l, "parametre": c, "url": url_parametre(c, langue)} for c, l in liens],
        allow_unicode=True, sort_keys=False), encoding="utf-8")


def avec_liens(fabrique: Callable[[], Any]) -> tuple[Any, list[tuple[str, str | None]]]:
    """Fabrique un tableau sous relevé : rend le tableau et les paramètres qu'il a lus.

    Le relevé est refermé même si la fabrique lève : un relevé resté ouvert capterait
    les lectures du tableau suivant.
    """
    releve_debut()
    try:
        tableau = fabrique()
    finally:
        liens = releve_fin()
    return tableau, liens


def ecrire_tableau(chemin_tableau: str | Path, df: "pd.DataFrame",
                   liens: list[tuple[str, str | None]], langue: str,
                   entete: str = "") -> None:
    """Écrit le snapshot Markdown d'un tableau, puis ses liens (`<nom>.liens.yml`).

    `entete` : commentaire HTML placé avant le tableau ; un snapshot qui en porte un se
    termine par une ligne vide, comme les générateurs l'ont toujours écrit.
    """
    corps = tableau_vers_markdown(df)
    Path(chemin_tableau).write_text(
        f"{entete}{corps}\n" if entete else corps, encoding="utf-8")
    ecrire_liens(chemin_tableau, liens, langue)


def charge_parametre(chemin_relatif: str, paquet: str | None = None) -> dict[str, Any] | None:
    """Charge un YAML de paramètre, chemin relatif à la racine du paquet.

    Exemple : "parameters/impot_revenu/bareme.yaml".
    """
    if yaml is None:
        return None
    racine = _racine_paquet(paquet)
    if racine is None:
        return None
    try:
        ref = racine
        for element in chemin_relatif.split("/"):
            ref = ref / element
        return yaml.safe_load(ref.read_text(encoding="utf-8"))
    except Exception:
        return None


# ------------------------------------------------------------------- lecture datée


def _annee(cle: Any) -> int:
    return cle.year if hasattr(cle, "year") else int(str(cle)[:4])


def _date_de_cle(cle: Any) -> datetime.date:
    """Date d'effet d'une clé de paramètre, à la JOURNÉE près.

    Les clés arrivent tantôt en objets `date` (PyYAML convertit `2014-01-01`), tantôt
    en chaînes. `datetime` étant une sous-classe de `date`, il se teste en premier.
    """
    if isinstance(cle, datetime.datetime):
        return cle.date()
    if isinstance(cle, datetime.date):
        return cle
    texte = str(cle)[:10]
    annee = int(texte[:4])
    mois = int(texte[5:7]) if len(texte) >= 7 else 1
    jour = int(texte[8:10]) if len(texte) >= 10 else 1
    return datetime.date(annee, mois, jour)


def valeur_a_la_date(bloc: dict[str, Any] | None, date: datetime.date) -> float | None:
    """Valeur en vigueur à `date` dans un bloc daté {date: {value: x}}.

    La comparaison porte sur la DATE COMPLÈTE. Elle ne portait que sur l'année (#215) :
    un palier daté du 1er juillet s'appliquait alors dès janvier, alors qu'il n'était pas
    encore en vigueur.

    Le changement est sans effet là où la convention « année de revenus » a du sens — les
    paramètres fiscaux sont datés au 1er janvier, et les deux lectures y coïncident. Il ne
    modifie que les six blocs porteurs de paliers infra-annuels : les cinq du SMIG/SMAG,
    révisés deux fois en 1980, 1992, 1993, 1996, 1997, 1999 et 2012, et l'allocation du
    PNAFN en 2009 — 53,333 D au 1er janvier, 56,666 D au 1er juillet. C'est là, et là
    seulement, que l'ancienne lecture renvoyait un montant qui n'était pas en vigueur.

    Renvoie None si la valeur en vigueur est nulle : dans openfisca, `value: null`
    signifie que le paramètre cesse d'exister à cette date. On ne remonte alors pas
    au-delà — c'est ce qui permet à une tranche de disparaître d'un barème.
    """
    if not bloc:
        return None
    for cle in sorted(bloc.keys(), key=lambda k: (_date_de_cle(k), str(k)), reverse=True):
        if _date_de_cle(cle) > date:
            continue
        brut = bloc[cle]
        if brut is None:
            return None
        if isinstance(brut, dict):
            valeur = brut.get("value")
            return None if valeur is None else float(valeur)
        if isinstance(brut, (int, float)):
            return float(brut)
    return None


def bareme_a_la_date(
    chemin_relatif: str, date: datetime.date
) -> list[tuple[float, float]] | None:
    """Barème en vigueur à `date` : liste de (seuil, taux), triée par seuil croissant.

    Les tranches dont le seuil ou le taux est nul à cette date sont écartées.
    """
    donnees = charge_parametre(chemin_relatif)
    if not donnees or "brackets" not in donnees:
        return None
    tranches: list[tuple[float, float]] = []
    for tranche in donnees["brackets"]:
        seuil = valeur_a_la_date(tranche.get("threshold"), date)
        taux = valeur_a_la_date(tranche.get("rate"), date)
        if seuil is None or taux is None:
            continue
        tranches.append((seuil, taux))
    if not tranches:
        return None
    return sorted(tranches)


# ------------------------------------------------------------------------ calculs


def taux_effectifs_limite_superieure(
    tranches: list[tuple[float, float]],
) -> list[float | None]:
    """Taux d'imposition du revenu global à la limite supérieure de chaque tranche.

    Troisième colonne des barèmes publiés au JORT jusqu'en 1990. Elle n'est pas dans
    openfisca : on la recalcule. La dernière tranche étant ouverte, elle n'en a pas.
    """
    resultats: list[float | None] = []
    cumul = 0.0
    for indice, (seuil, taux) in enumerate(tranches):
        if indice + 1 >= len(tranches):
            resultats.append(None)
            continue
        limite = tranches[indice + 1][0]
        cumul += (limite - seuil) * taux
        resultats.append(cumul / limite if limite else 0.0)
    return resultats


# ---------------------------------------------------------------------- formatage


def formate_dinars(montant: float) -> str:
    """1500.0 -> '1 500' ; 1500.001 -> '1 500,001'."""
    entier = int(montant)
    decimales = montant - entier
    texte = f"{entier:,}".replace(",", " ")
    if decimales:
        texte += "," + f"{decimales:.3f}".split(".")[1].rstrip("0")
    return texte


def formate_taux(taux: float) -> str:
    """0.15 -> '15 %' ; 0.005 -> '0,5 %'."""
    pourcentage = taux * 100
    if abs(pourcentage - round(pourcentage)) < 1e-9:
        return f"{round(pourcentage)} %"
    return f"{pourcentage:.2f}".rstrip("0").rstrip(".").replace(".", ",") + " %"


def formate_taux_effectif(taux: float | None) -> str:
    """Deux décimales, **tronquées** et non arrondies, comme au JORT.

    Contrôle : 20,125 % est imprimé « 20,12 % » dans le barème de 1990, et 2,667 %
    « 2,66 % » dans celui de 1986 — c'est bien une troncature.
    """
    if taux is None:
        return "—"
    if taux == 0:
        return "0 %"
    pourcentage = taux * 100
    tronque = int(pourcentage * 100 + 1e-9) / 100
    return f"{tronque:.2f}".replace(".", ",") + " %"


BORNES = {
    "fr": ("{bas} à {haut}", "au-delà de {bas}"),
    "ar": ("من {bas} إلى {haut}", "ما يفوق {bas}"),
}


def libelle_tranche(seuil: float, seuil_suivant: float | None, langue: str = "fr") -> str:
    """'0 à 1 500', '1 500,001 à 5 000', 'au-delà de 50 000' ; en arabe 'من … إلى …'."""
    intervalle, au_dela = BORNES.get(langue, BORNES["fr"])
    if seuil_suivant is None:
        return au_dela.format(bas=formate_dinars(seuil))
    bas = formate_dinars(seuil) if seuil == 0 else formate_dinars(seuil + 0.001)
    return intervalle.format(bas=bas, haut=formate_dinars(seuil_suivant))


# ------------------------------------------------------- séries de valeurs datées


def _reference_a_la_date(donnees: dict[str, Any], cle_date: Any) -> tuple[str, str]:
    """Titre et lien de la référence attachée à une date d'effet, sinon ("", "")."""
    refs = ((donnees.get("metadata") or {}).get("reference")) or {}
    for cle, valeur in refs.items():
        if str(cle)[:10] == str(cle_date)[:10]:
            if isinstance(valeur, list):
                valeur = valeur[0] if valeur else {}
            if isinstance(valeur, dict):
                return valeur.get("title", ""), valeur.get("href", "")
            if isinstance(valeur, str):
                return valeur, ""
    return "", ""


def serie_datee(chemin_relatif: str) -> list[tuple[str, float | None, str, str]]:
    """Série (date d'effet, valeur, titre de la référence, lien) d'un paramètre scalaire.

    Les dates sont rendues telles qu'elles figurent dans le paramètre : ce sont, dans ce
    dépôt, des **années de revenus**. Les références proviennent de `metadata.reference`,
    ce qui rend le tableau publié et le paramètre indissociables : corriger l'un corrige
    l'autre.
    """
    donnees = charge_parametre(chemin_relatif)
    if not donnees or "values" not in donnees:
        return []
    sortie = []
    for cle in sorted(donnees["values"].keys(), key=lambda k: (_annee(k), str(k))):
        brut = donnees["values"][cle]
        valeur = None
        if isinstance(brut, dict):
            valeur = brut.get("value")
        elif isinstance(brut, (int, float)):
            valeur = brut
        titre, lien = _reference_a_la_date(donnees, cle)
        sortie.append((str(cle)[:10], None if valeur is None else float(valeur), titre, lien))
    return sortie


def tableau_serie(
    chemin_relatif: str,
    colonne_valeur: str = "Valeur",
    formateur: Callable[[float | None], str] | None = None,
    avec_reference: bool = True,
) -> "pd.DataFrame | None":
    """Un paramètre scalaire, sous forme de tableau d'évolution daté et sourcé."""
    if pd is None:
        return None
    serie = serie_datee(chemin_relatif)
    if not serie:
        return None
    releve_note(chemin_relatif, colonne_valeur)
    if formateur is None:
        formateur = lambda v: "—" if v is None else formate_dinars(v)
    lignes = []
    for date, valeur, titre, _lien in serie:
        ligne = {
            "À compter des revenus de": date[:4],
            colonne_valeur: formateur(valeur),
        }
        if avec_reference:
            ligne["Texte"] = titre or "—"
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def tableau_evolution(
    specs: list[tuple[str, str, Callable[[float | None], str]]],
    cles: dict[str, str] | None = None,
    colonne_periode: str = "Années de revenus",
    derniere_annee: str = "2026",
    colonne_texte: str = "Texte",
) -> "pd.DataFrame | None":
    """Plusieurs paramètres côte à côte, une ligne par période homogène.

    `specs` : (chemin du paramètre, en-tête de colonne, formateur).
    `cles`  : date d'effet -> clé de citation du précis, par exemple
              {"2017-01-01": "lf-2017, art. 14"}. La colonne « Texte » émet alors
              `[@clé]`, ce qui raccroche le tableau à la bibliographie ; à défaut,
              elle reprend le titre de la référence portée par le paramètre.

    Les bornes de période sont calculées sur l'union des dates de changement de tous
    les paramètres : une ligne couvre un intervalle pendant lequel aucune valeur ne bouge.
    """
    if pd is None:
        return None
    series = {}
    for chemin, entete, _f in specs:
        s = serie_datee(chemin)
        if not s:
            return None
        series[chemin] = s
        releve_note(chemin, entete)
    dates = sorted({d for s in series.values() for d, *_ in s})
    if not dates:
        return None

    def valeur_a(chemin, date):
        retenue = None
        for d, v, _t, _h in series[chemin]:
            if d <= date:
                retenue = v
        return retenue

    lignes = []
    for indice, date in enumerate(dates):
        debut = date[:4]
        fin = str(int(dates[indice + 1][:4]) - 1) if indice + 1 < len(dates) else derniere_annee
        periode = debut if debut == fin else f"{debut} → {fin}"
        ligne = {colonne_periode: periode}
        for chemin, entete, formateur in specs:
            ligne[entete] = formateur(valeur_a(chemin, date))
        texte = ""
        if cles and date in cles:
            texte = f"[@{cles[date]}]"
        else:
            for chemin, _e, _f in specs:
                for d, _v, titre, _h in series[chemin]:
                    if d == date and titre:
                        texte = titre
                        break
                if texte:
                    break
        ligne[colonne_texte] = texte or "—"
        lignes.append(ligne)
    return pd.DataFrame(lignes)


# ------------------------------------------------------------------------ tableau


def tableau_bareme(
    chemin_relatif: str,
    date: datetime.date,
    colonne_tranche: str = "Tranche de revenu annuel net (dinars)",
    avec_taux_effectif: bool = False,
    langue: str = "fr",
    colonne_taux: str = "Taux de la tranche",
    colonne_taux_effectif: str = "Taux d’imposition du revenu global à la limite supérieure",
) -> "pd.DataFrame | None":
    """Barème en vigueur à `date`, sous forme de DataFrame prêt à publier."""
    if pd is None:
        return None
    tranches = bareme_a_la_date(chemin_relatif, date)
    if not tranches:
        return None
    effectifs = taux_effectifs_limite_superieure(tranches)
    lignes = []
    for indice, (seuil, taux) in enumerate(tranches):
        suivant = tranches[indice + 1][0] if indice + 1 < len(tranches) else None
        ligne = {
            colonne_tranche: libelle_tranche(seuil, suivant, langue),
            colonne_taux: formate_taux(taux),
        }
        if avec_taux_effectif:
            ligne[colonne_taux_effectif] = formate_taux_effectif(effectifs[indice])
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def _colonne_numerique(df: "pd.DataFrame", colonne: str) -> bool:
    """Vrai si toutes les cellules tiennent du nombre (chiffres, %, dinars, tiret)."""
    motif = re.compile(r"^[\d\s.,%—–-]+$|^.*\d.*(%|D)$")
    return all(motif.match(str(v).strip()) for v in df[colonne])


def tableau_vers_markdown(df: "pd.DataFrame") -> str:
    """DataFrame -> tableau Markdown pipe.

    Seules les colonnes dont toutes les cellules sont numériques sont alignées à droite ;
    une colonne de texte, comme la référence du texte de loi, reste alignée à gauche.
    """
    colonnes = list(df.columns)
    lignes = ["| " + " | ".join(str(c) for c in colonnes) + " |"]
    lignes.append(
        "|"
        + "|".join(
            "---:" if i > 0 and _colonne_numerique(df, c) else "---"
            for i, c in enumerate(colonnes)
        )
        + "|"
    )
    for _, ligne in df.iterrows():
        lignes.append("| " + " | ".join(str(ligne[c]) for c in colonnes) + " |")
    return "\n".join(lignes)


def lit_markdown_statique(chemin: str | Path) -> "pd.DataFrame | None":
    """Relit un snapshot Markdown pipe en DataFrame (lignes de commentaire ignorées)."""
    if pd is None:
        return None
    fichier = Path(chemin)
    if not fichier.is_file():
        return None
    lignes = [
        ligne.strip()
        for ligne in fichier.read_text(encoding="utf-8").splitlines()
        if ligne.strip().startswith("|")
    ]
    cellules = []
    for ligne in lignes:
        contenu = [c.strip() for c in ligne.split("|")[1:-1]]
        if contenu and not all(set(c) <= set("-:") for c in contenu if c):
            cellules.append(contenu)
    if not cellules:
        return None
    return pd.DataFrame(cellules[1:], columns=cellules[0])


# ------------------------------------------------------------------- prestations
#
# Les tableaux du livre « Fiscalité » sont datés en ANNÉES DE REVENUS : le mois est sans
# objet, une loi de finances prenant effet au 1er janvier. Ceux du livre « Prestations
# sociales » ne le supportent pas — la majoration pour salaire unique prend effet au 1er mai
# 1980, le plafond d'assiette au 1er mai 1986, la contribution aux frais de crèche au
# 1er octobre 1994. Réduire ces dates à l'année les rendrait fausses. D'où les fonctions
# ci-dessous, qui rendent la date d'effet au jour près et exposent l'attestation.

MOIS = {
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin",
           "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
    # Noms de mois en usage en Tunisie, hérités du calendrier grégorien tel qu'il est
    # imprimé au Journal officiel arabe — et non les noms du Machrek (كانون الثاني, …),
    # qui dérouteraient un lecteur tunisien.
    "ar": ["جانفي", "فيفري", "مارس", "أفريل", "ماي", "جوان",
           "جويلية", "أوت", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"],
}


def formate_date(date_iso: str, langue: str = "fr") -> str:
    """« 1980-05-01 » -> « 1^er^ mai 1980 » en français, « 1 ماي 1980 » en arabe.

    L'ordinal en exposant est une convention typographique française ; l'arabe
    n'ordinalise pas le premier jour du mois.
    """
    try:
        annee, mois, jour = (int(x) for x in str(date_iso)[:10].split("-"))
    except ValueError:
        return str(date_iso)
    if langue == "ar":
        return f"{jour} {MOIS['ar'][mois - 1]} {annee}"
    ordinal = "1^er^" if jour == 1 else str(jour)
    return f"{ordinal} {MOIS['fr'][mois - 1]} {annee}"


def formate_date_fr(date_iso: str) -> str:
    """Conservé pour compatibilité : `formate_date(date, "fr")`."""
    return formate_date(date_iso, "fr")


ATTESTATION = {
    "fr": ("texte lu", "**non établie**"),
    "ar": ("نصّ مقروء", "**غير ثابتة**"),
}


def attestation(titre: str, langue: str = "fr") -> str:
    """Niveau d'attestation d'une valeur, déduit de la présence d'une référence.

    Convention de lecture n° 3 du chapitre : une valeur que le paramètre ne rattache à
    aucun texte n'est pas présentée comme attestée. La colonne se calcule donc, elle ne
    se saisit pas — ajouter la référence au paramètre suffit à la faire basculer.
    """
    atteste, non_etabli = ATTESTATION.get(langue, ATTESTATION["fr"])
    return atteste if titre else non_etabli


def tableau_evolution_datee(
    specs: list[tuple[str, str, Callable[[float | None], str]]],
    cles: dict[str, str] | None = None,
    colonne_periode: str = "Effet",
    avec_attestation: bool = False,
    langue: str = "fr",
    colonne_texte: str = "Texte",
    colonne_attestation: str = "Attestation",
) -> "pd.DataFrame | None":
    """Comme `tableau_evolution`, mais une ligne par DATE D'EFFET rendue au jour près.

    `cles` : date ISO -> clé de citation du précis. À défaut, la colonne « Texte »
    reprend le titre de la référence portée par le paramètre lui-même.
    """
    if pd is None:
        return None
    series = {}
    for chemin, entete, _f in specs:
        s = serie_datee(chemin)
        if not s:
            return None
        series[chemin] = s
        releve_note(chemin, entete)
    dates = sorted({d for s in series.values() for d, *_ in s})
    if not dates:
        return None

    def valeur_a(chemin, date):
        retenue = None
        for d, v, _t, _h in series[chemin]:
            if d <= date:
                retenue = v
        return retenue

    def titre_a(date):
        for chemin, _e, _f in specs:
            for d, _v, titre, _h in series[chemin]:
                if d == date and titre:
                    return titre
        return ""

    lignes = []
    for date in dates:
        ligne = {colonne_periode: formate_date(date, langue)}
        for chemin, entete, formateur in specs:
            ligne[entete] = formateur(valeur_a(chemin, date))
        titre = titre_a(date)
        if cles and date in cles:
            ligne[colonne_texte] = f"[@{cles[date]}]"
        else:
            ligne[colonne_texte] = titre or "—"
        if avec_attestation:
            ligne[colonne_attestation] = attestation(titre, langue)
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def tableau_a_la_date(
    specs: list[tuple[str, str, Callable[[float | None], str]]],
    date: str,
    cles: dict[str, str] | None = None,
    entetes: tuple[str, str, str] = ("Paramètre", "Valeur", "Texte"),
) -> "pd.DataFrame | None":
    """Rendu VERTICAL — un paramètre par ligne — d'un dispositif à millésime unique.

    La contribution aux frais de crèche ou les aides ponctuelles de l'AMEN social n'ont
    qu'une seule date d'effet : les mettre en colonnes donnerait un tableau d'une ligne et
    de cinq colonnes hétérogènes (un montant, une durée, deux âges, un plafond). La lecture
    par ligne « Paramètre / Valeur / Texte » est celle du chapitre.

    `cles` : chemin du paramètre -> clé de citation ; à défaut, titre de la référence.
    """
    if pd is None:
        return None
    lignes = []
    for chemin, libelle, formateur in specs:
        serie = serie_datee(chemin)
        if not serie:
            return None
        releve_note(chemin, libelle)
        retenue, titre_retenu = None, ""
        for d, v, titre, _h in serie:
            if d <= date:
                retenue, titre_retenu = v, titre
        if cles and chemin in cles:
            texte = f"[@{cles[chemin]}]"
        else:
            texte = titre_retenu or "—"
        lignes.append(dict(zip(entetes, (libelle, formateur(retenue), texte))))
    return pd.DataFrame(lignes)


def taux_datee(chemin_relatif: str) -> list[tuple[str, float | None, str, str]]:
    """Série datée du taux d'un barème à UNE tranche : (date, taux, titre, lien).

    Les cotisations sociales sont encodées en `brackets` et non en `values`, même quand
    elles n'ont qu'un taux unique : `serie_datee` ne les voit donc pas. Ce lecteur prend
    le taux de la première tranche, ce qui couvre tous les régimes sauf celui des
    travailleurs à faibles revenus — le seul plafonné, qui relève de `tableau_bareme`.
    """
    donnees = charge_parametre(chemin_relatif)
    if not donnees or not donnees.get("brackets"):
        return []
    taux = donnees["brackets"][0].get("rate") or {}
    sortie = []
    for cle in sorted(taux.keys(), key=lambda k: (_annee(k), str(k))):
        brut = taux[cle]
        valeur = brut.get("value") if isinstance(brut, dict) else brut
        titre, lien = _reference_a_la_date(donnees, cle)
        sortie.append((str(cle)[:10], None if valeur is None else float(valeur), titre, lien))
    return sortie


def tableau_taux_datee(
    specs: list[tuple[str, str, Callable[[float | None], str]]],
    cles: dict[str, str] | None = None,
    colonne_periode: str = "Effet",
    colonne_texte: str = "Texte",
    langue: str = "fr",
) -> "pd.DataFrame | None":
    """Comme `tableau_evolution_datee`, mais pour des barèmes à une tranche."""
    if pd is None:
        return None
    series = {chemin: taux_datee(chemin) for chemin, _e, _f in specs}
    if not all(series.values()):
        return None
    for chemin, entete, _f in specs:
        releve_note(chemin, entete)
    dates = sorted({d for s in series.values() for d, *_ in s})

    def valeur_a(chemin, date):
        retenue = None
        for d, v, _t, _h in series[chemin]:
            if d <= date:
                retenue = v
        return retenue

    lignes = []
    for date in dates:
        ligne = {colonne_periode: formate_date(date, langue)}
        for chemin, entete, formateur in specs:
            ligne[entete] = formateur(valeur_a(chemin, date))
        titre = ""
        for chemin, _e, _f in specs:
            for d, _v, t, _h in series[chemin]:
                if d == date and t:
                    titre = t
                    break
            if titre:
                break
        if cles and date in cles:
            ligne[colonne_texte] = f"[@{cles[date]}]"
        else:
            ligne[colonne_texte] = titre or "—"
        lignes.append(ligne)
    return pd.DataFrame(lignes)


def markdown_avec_legende(
    chemin: str | Path, legende: str, label: str, colonnes: str = ""
) -> str:
    """Rend un snapshot en tableau Markdown légendé, pour un chunk `#| output: asis`.

    POURQUOI PASSER PAR LÀ. Un DataFrame stylé est émis en HTML : Pandoc reçoit du balisage
    déjà cuit, et les citations qu'il contient — `[@lf-2017, art. 14]` — ne sont jamais vues
    par citeproc. Elles s'impriment alors telles quelles dans la page. En émettant du
    Markdown, la table et ses citations sont analysées par Pandoc : les clés se résolvent et
    la légende porte une ancre `@tbl-…` référençable dans le texte.

    `colonnes` : spécification facultative de largeur, par exemple `{tbl-colwidths="[20,80]"}`.
    """
    fichier = Path(chemin)
    if not fichier.is_file():
        return MESSAGE_INDISPONIBLE
    corps = fichier.read_text(encoding="utf-8").rstrip()
    attributs = f"{{#{label}}}" if not colonnes else f"{{#{label} {colonnes}}}"
    tableau = f"{corps}\n\n: {legende} {attributs}\n"
    liens = fichier.with_suffix(".liens.yml")
    if not liens.is_file() or yaml is None:
        return tableau
    langue = "ar" if "ar" in fichier.resolve().parts[-4:-2] else "fr"
    m = ONGLETS[langue]
    items = "\n".join(f"- [{e['libelle']}]({e['url']})"
                       for e in yaml.safe_load(liens.read_text(encoding="utf-8")) or [])
    return (f"::: {{.panel-tabset}}\n\n## {m['tableau']}\n\n{tableau}\n"
            f"## {m['base']}\n\n{m['intro']}\n\n{items}\n\n:::\n")


# Intitulés des onglets d'un tableau engendré, dans la langue du livre.
ONGLETS = {
    "fr": {"tableau": "📋 Tableau", "base": "⚖️ Base législative",
           "intro": "Chaque grandeur du tableau, avec toutes ses valeurs datées et leurs "
                    "références :"},
    "ar": {"tableau": "📋 الجدول", "base": "⚖️ القاعدة التشريعية",
           "intro": "كلّ مقدار في الجدول، بجميع قيمه المؤرّخة ومراجعها:"},
}


def get_table_or_static(
    fonction_openfisca: Callable[[], "pd.DataFrame | None"],
    chemin_statique: str | Path,
    variable_env: str = "PRECIS_USE_OPENFISCA_TABLES",
) -> "pd.DataFrame | None":
    """Lit le barème dans openfisca s'il est disponible et assez récent, sinon le snapshot.

    Mettre `PRECIS_USE_OPENFISCA_TABLES=false` force le snapshot.
    """
    autorise = os.environ.get(variable_env, "true").lower() in ("true", "1", "yes")
    if autorise and openfisca_utilisable():
        df = fonction_openfisca()
        if df is not None and not df.empty:
            return df
    return lit_markdown_statique(chemin_statique)

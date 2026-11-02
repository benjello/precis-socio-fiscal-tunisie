"""Régénère le snapshot Markdown des quatre-vingt-un cas de la circulaire n° 42 de 1996.

Même contrat que les autres générateurs : le build du site n'exécute PAS ce script, il lit le
fichier qu'il produit, versionné dans `precis/fr/prestations_sociales/tables/`, et l'annexe
`_annexe_circulaire_42.qmd` l'inclut.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_circulaire_42_tables.py

Exige openfisca-tunisia >= 0.157 : c'est la version qui verse l'indemnité familiale et
l'indemnité pour salaire unique du secteur public (PR #518,
`variables/prestations/contributives/indemnites_familiales_secteur_public.py`).

CE QUI VIENT DU MODÈLE. La table `CAS_ANNEXE_2` du module : pour chaque code de 1 à 81, la
lettre du cas, la situation, la position du père, celle de la mère, la filiation de l'enfant ou
la situation du tuteur, le bénéficiaire et l'organisme payeur de chaque indemnité. Et le libellé
de chaque valeur, lu dans les `Enum` du même module. Le module est LU comme du texte (`ast`), non
importé : il ne se charge pas sans openfisca-core, que le précis ne déclare pas. Seules les
constantes littérales sont évaluées ; un module dont la table cesse d'être littérale fait échouer
le script au lieu de donner un tableau faux.

CE QUI VIENT DE `circulaire_42_metadonnees.yml`. Ce que le modèle ne porte pas : les pièces à
fournir, les pages du Journal officiel, les mots qui qualifient un parent dans une situation
(« décédé », « divorcée »), les tournures du payeur et de la garde partagée, et trois cellules où
la circulaire dit autre chose que la valeur du modèle, et quelques libellés de positions. Voir
l'en-tête de ce fichier.

L'ARABE N'EST PAS ENGENDRÉ. Le chapitre arabe de l'annexe est une page-relais vers le français.
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

MODULE = "variables/prestations/contributives/indemnites_familiales_secteur_public.py"
METADONNEES = Path(__file__).parent / "circulaire_42_metadonnees.yml"
SORTIE = (
    Path(__file__).parent.parent / "precis" / "fr" / "prestations_sociales" / "tables"
    / "circulaire_42_annexe_2.md"
)

ROMAINS = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII"}
SYMBOLES_BENEFICIAIRE = {
    "N": "non_servie",
    "P": "pere",
    "M": "mere",
    "T": "tuteur",
    "A": "mere_montant_anterieur_remariage",
}
SYMBOLES_PAYEUR = {"E": "employeur_du_pere", "C": "cnss", "R": "caisse_de_retraite"}
ENTETE_PARENTS = ["Cas", "Père", "Mère", "Enfants", "Code", "Indemnité familiale",
                  "Indemnité pour salaire unique", "Pièces"]
ENTETE_TUTEUR = ["Cas", "Situation du tuteur (ou de la tutrice)", "Situation des enfants",
                 "Code", "Indemnité familiale", "Indemnité pour salaire unique", "Pièces"]


class Ecart(ValueError):
    """Le module du modèle ou les métadonnées ne disent pas ce que le tableau suppose."""


# ----------------------------------------------------------------- lecture du module


def _evaluer(noeud: ast.AST, env: dict):
    """Valeur d'un littéral (chaîne, nombre, None, tuple, liste, dict) ou d'un nom déjà lu."""
    if isinstance(noeud, ast.Constant):
        return noeud.value
    if isinstance(noeud, ast.Name):
        if noeud.id not in env:
            raise Ecart(f"nom non littéral dans la table du modèle : {noeud.id}")
        return env[noeud.id]
    if isinstance(noeud, ast.Tuple):
        return tuple(_evaluer(e, env) for e in noeud.elts)
    if isinstance(noeud, ast.List):
        return [_evaluer(e, env) for e in noeud.elts]
    if isinstance(noeud, ast.Dict):
        return {_evaluer(k, env): _evaluer(v, env) for k, v in zip(noeud.keys, noeud.values)}
    raise Ecart(f"expression non littérale dans la table du modèle : {ast.dump(noeud)[:80]}")


def lire_modele(source: str) -> dict:
    """Table des cas et libellés des `Enum`, lus dans le texte du module.

    Rend {"cas": [...], "libelles": {"NomEnum": {membre: libellé}}}.
    """
    arbre = ast.parse(source)
    env: dict = {}
    cas = None
    libelles: dict[str, dict[str, str]] = {}
    for noeud in arbre.body:
        if isinstance(noeud, ast.ClassDef) and any(
            isinstance(b, ast.Name) and b.id == "Enum" for b in noeud.bases
        ):
            membres = {}
            for instruction in noeud.body:
                if (isinstance(instruction, ast.Assign) and len(instruction.targets) == 1
                        and isinstance(instruction.targets[0], ast.Name)
                        and instruction.targets[0].id != "__order__"
                        and isinstance(instruction.value, ast.Constant)
                        and isinstance(instruction.value.value, str)):
                    membres[instruction.targets[0].id] = instruction.value.value
            libelles[noeud.name] = membres
        elif (isinstance(noeud, ast.Assign) and len(noeud.targets) == 1
              and isinstance(noeud.targets[0], ast.Tuple)
              and isinstance(noeud.value, ast.Tuple)):
            # `_c, _p, _m = "communs", "premier_mariage_pere", …`
            for cible, valeur in zip(noeud.targets[0].elts, noeud.value.elts):
                if isinstance(cible, ast.Name):
                    env[cible.id] = _evaluer(valeur, env)
        elif (isinstance(noeud, ast.Assign) and len(noeud.targets) == 1
              and isinstance(noeud.targets[0], ast.Name)):
            nom = noeud.targets[0].id
            if nom == "CAS_ANNEXE_2":
                cas = _evaluer(noeud.value, env)
            elif not isinstance(noeud.value, (ast.Call, ast.Attribute)):
                try:
                    env[nom] = _evaluer(noeud.value, env)
                except Ecart:
                    pass
    if not cas:
        raise Ecart("CAS_ANNEXE_2 introuvable dans le module du modèle")
    return {"cas": cas, "libelles": libelles}


# ----------------------------------------------------------------- mise en forme


def minuscule(texte: str) -> str:
    return texte[:1].lower() + texte[1:]


def _libelle(modele: dict, enum: str, membre: str) -> str:
    try:
        return modele["libelles"][enum][membre]
    except KeyError:
        raise Ecart(f"libellé introuvable : {enum}.{membre}") from None


def cellule_indemnite(modele: dict, meta: dict, code: int, colonne: str, valeur) -> str:
    """Bénéficiaire et payeur d'une indemnité, dits comme l'annexe les dit."""
    surcharge = meta["libelles_circulaire"].get(code, {}).get(colonne)
    if surcharge:
        return surcharge
    symbole, payeur = valeur
    phrase_payeur = f" {meta['payeurs'][SYMBOLES_PAYEUR[payeur]]}" if payeur else ""
    if symbole in ("G", "H"):
        return meta["garde_partagee"][symbole].format(payeur=phrase_payeur)
    if symbole not in SYMBOLES_BENEFICIAIRE:
        raise Ecart(f"cas {code} : bénéficiaire inconnu {symbole!r}")
    libelle = _libelle(modele, "BeneficiaireIndemniteSecteurPublic", SYMBOLES_BENEFICIAIRE[symbole])
    return minuscule(libelle) + phrase_payeur


def position_parent(modele: dict, meta: dict, meta_situation: dict, cle: str,
                    membre: str | None) -> str:
    """Position d'un parent : libellé du modèle (ou son remplaçant des métadonnées), suivi du
    qualificatif de la situation. Une position que le modèle laisse indifférente (None : la
    mère des cas 42 et 43) ne garde que le qualificatif."""
    qualificatif = meta_situation.get(cle)
    if membre is None:
        if not qualificatif:
            raise Ecart(f"position indifférente sans qualificatif pour {cle}")
        return qualificatif
    texte = meta.get("positions", {}).get(membre)
    texte = texte or minuscule(_libelle(modele, "StatutParentSecteurPublic", membre))
    return f"{texte}, {qualificatif}" if qualificatif else texte


def pieces_du_cas(meta: dict, code: int) -> str:
    noms = meta["pieces_par_cas"].get(code, [])
    try:
        return " ; ".join(meta["pieces"][nom] for nom in noms)
    except KeyError as erreur:
        raise Ecart(f"cas {code} : pièce inconnue {erreur}") from None


def ordre_situations(modele: dict) -> list[str]:
    """Les situations dans l'ordre de l'annexe (I à VII) : celui de l'`Enum`."""
    return list(modele["libelles"]["SituationParentsSecteurPublic"])


def verifier(modele: dict, meta: dict) -> None:
    cas = modele["cas"]
    codes = [ligne[0] for ligne in cas]
    if codes != list(range(1, 82)):
        raise Ecart(f"les codes du modèle ne sont pas 1 à 81 dans l'ordre : {codes[:5]}…")
    situations = ordre_situations(modele)
    if len(situations) != 7:
        raise Ecart(f"{len(situations)} situations dans le modèle, 7 attendues")
    for nom in situations:
        if nom not in meta["situations"]:
            raise Ecart(f"situation sans métadonnées (pages) : {nom}")
    sans_lettre = [ligne[0] for ligne in cas if ligne[2] not in situations]
    if sans_lettre:
        raise Ecart(f"cas dont la situation n'est pas dans l'Enum : {sans_lettre}")
    for code in list(meta["pieces_par_cas"]) + list(meta["libelles_circulaire"]):
        if code not in codes:
            raise Ecart(f"métadonnées pour un cas inexistant : {code}")


def construire(modele: dict, meta: dict) -> str:
    verifier(modele, meta)
    situations = ordre_situations(modele)
    source = meta["source"]
    morceaux = [
        "<!-- Engendré par scripts/generate_circulaire_42_tables.py depuis openfisca-tunisia "
        "(variables de l'indemnité familiale et de l'indemnité pour salaire unique du secteur "
        "public, version 0.157 au moins) et scripts/circulaire_42_metadonnees.yml (pièces à "
        "fournir, pages du JORT). Ne pas modifier à la main. -->\n"
    ]
    for numero, nom in enumerate(situations, start=1):
        romain = ROMAINS[numero]
        meta_sit = meta["situations"][nom]
        titre = _libelle(modele, "SituationParentsSecteurPublic", nom)
        titre = titre.rsplit(" (", 1)[0] if titre.endswith(f"({romain})") else titre
        lignes = [ligne for ligne in modele["cas"] if ligne[2] == nom]
        tuteur = nom == "tutelle"
        morceaux.append(f"**{romain}. {titre}** ({source['jort']}, {meta_sit['pages']})\n")
        entete = ENTETE_TUTEUR if tuteur else ENTETE_PARENTS
        morceaux.append("| " + " | ".join(entete) + " |")
        morceaux.append("|" + "---|" * len(entete))
        precedente = None
        for code, lettre, _sit, pere, mere, filiation, st_tuteur, si, su in lignes:
            if not lettre.startswith(f"{romain}-"):
                raise Ecart(f"cas {code} : la lettre {lettre} n'est pas de la situation {romain}")
            premier = lettre != precedente
            etiquette = lettre if premier else ""
            if code == 1:
                etiquette = f"[]{{#{source['ancre']}}}{lettre} {source['citation']}"
            indemnites = [
                cellule_indemnite(modele, meta, code, "indemnite_familiale", si),
                cellule_indemnite(modele, meta, code, "salaire_unique", su),
            ]
            pieces = pieces_du_cas(meta, code)
            if tuteur:
                situation_tuteur = _libelle(modele, "StatutTuteurSecteurPublic", st_tuteur)
                cellules = [lettre, minuscule(situation_tuteur), meta_sit["enfants"], str(code),
                            *indemnites, pieces]
            else:
                cellules = [
                    etiquette,
                    position_parent(modele, meta, meta_sit, "pere", pere) if premier else "",
                    position_parent(modele, meta, meta_sit, "mere", mere) if premier else "",
                    _libelle(modele, "FiliationEnfantSecteurPublic", filiation),
                    str(code), *indemnites, pieces,
                ]
            morceaux.append("| " + " | ".join(cellules) + " |")
            precedente = lettre
        morceaux.append(f"\n: Circulaire n° 42, annexe 2, {romain} : cas d'octroi "
                        f"{{#tbl-pf-public-annexe2-{romain.lower()}}}\n")
    return "\n".join(morceaux)


# ----------------------------------------------------------------- programme


def main() -> int:
    if not ot.openfisca_utilisable():
        print(
            f"openfisca-tunisia indisponible ou trop ancien (version {ot.version_openfisca()}, "
            f"minimum {ot.VERSION_MINIMALE}). Le snapshot existant est conservé."
        )
        return 1
    racine = ot._racine_paquet()
    fichier = Path(str(racine)) / MODULE
    if not fichier.is_file():
        print(f"✗ module du modèle introuvable : {fichier}")
        return 1
    meta = yaml.safe_load(METADONNEES.read_text(encoding="utf-8"))
    try:
        modele = lire_modele(fichier.read_text(encoding="utf-8"))
        texte = construire(modele, meta)
    except Ecart as erreur:
        print(f"✗ {erreur}")
        return 1
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(texte, encoding="utf-8")
    print(f"✓ {SORTIE.name} : {len(modele['cas'])} cas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Régénère les snapshots Markdown des tableaux du livre « Cotisations sociales ».

Même contrat que les deux générateurs qui précèdent : le build ne lance pas ce script, il
lit les fichiers versionnés dans `precis/{fr,ar}/cotisations_sociales/tables/`.

    OPENFISCA_TUNISIA_PATH=../openfisca-tunisia PYTHONPATH=scripts \
        uv run python scripts/generate_cotisations_tables.py

Les cotisations sont encodées en barèmes (`brackets`) et non en valeurs scalaires, même
quand elles n'ont qu'un taux unique : d'où `ot.taux_datee` et `ot.tableau_taux_datee`, qui
lisent le taux de la première tranche. Le seul régime réellement plafonné — celui des
travailleurs à faibles revenus — passe par `ot.tableau_bareme`.

CE QUE CES TABLEAUX DISENT ET NE DISENT PAS. Les taux du secteur privé sont exacts mais
portent tous le 1er janvier 1960, qui n'est la date d'aucun d'entre eux : la colonne
« Texte » y est donc vide, et le chapitre doit le dire plutôt que de laisser croire à une
stabilité de soixante-cinq ans. Le secteur public, lui, est daté et sourcé.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import openfisca_tables as ot  # noqa: E402

COT = "parameters/prelevements_sociaux/cotisations_sociales"
PRIVE = f"{COT}/secteur_prive"
PUBLIC = f"{COT}/secteur_public"
RACINE = Path(__file__).parent.parent / "precis"
LANGUES = ("fr", "ar")

MOTS = {
    "fr": {
        "effet": "Effet", "texte": "Texte", "branche": "Branche",
        "salarie": "Part salariale", "employeur": "Part patronale",
        "total": "Total", "regime": "Régime", "taux": "Taux",
        "tranche": "Tranche d'assiette (en SMIG)",
        "retraite": "Retraite", "maladie": "Maladie", "maternite": "Maternité",
        "deces": "Décès", "famille": "Prestations familiales",
        "at": "Accidents du travail", "perte_emploi": "Perte d'emploi",
        "fse": "Fonds spécial de l'État",
        "pst": "Protection sociale des travailleurs",
        "complementaire": "Retraite complémentaire (facultative)",
        "cnrps_retraite": "Cotisation retraite du salarié affilié à la CNRPS",
    },
    "ar": {
        "effet": "بداية السريان", "texte": "النصّ", "branche": "الفرع",
        "salarie": "الحصة الأجيرية", "employeur": "الحصة المشغِّلة",
        "total": "المجموع", "regime": "النظام", "taux": "النسبة",
        "tranche": "شريحة الوعاء (بالأجر الأدنى)",
        "retraite": "التقاعد", "maladie": "المرض", "maternite": "الولادة",
        "deces": "الوفاة", "famille": "المنح العائلية",
        "at": "حوادث الشغل", "perte_emploi": "فقدان الشغل",
        "fse": "الصندوق الخاص للدولة",
        "pst": "الحماية الاجتماعية للعملة",
        "complementaire": "التقاعد التكميلي (اختياري)",
        "cnrps_retraite": "مساهمة التقاعد للأجير المنخرط بالصندوق الوطني للتقاعد",
    },
}

# (clé de libellé, chemin sous le régime) — l'ordre est celui de la lecture, des branches
# les plus lourdes aux plus légères.
BRANCHES_RSNA = [
    ("retraite", "retraite.yaml"),
    ("maladie", "assurances_sociales/maladie.yaml"),
    ("maternite", "assurances_sociales/maternite.yaml"),
    ("deces", "assurances_sociales/deces.yaml"),
    ("famille", "famille.yaml"),
    ("at", "accident_du_travail.yaml"),
    ("perte_emploi", "perte_d_emploi.yaml"),
    ("pst", "protection_sociale_travailleurs.yaml"),
    ("fse", "fonds_special_etat.yaml"),
    ("complementaire", "retraite_complementaire.yaml"),
]

REGIMES = [
    ("rsna", "Salariés non agricoles", "الأجراء غير الفلاحيين", ""),
    ("rsa", "Salariés agricoles", "الأجراء الفلاحيون", ""),
    ("rsaa", "Salariés agricoles, régime amélioré", "الأجراء الفلاحيون، النظام المحسّن", ""),
    ("rtns", "Travailleurs non salariés", "العملة غير الأجراء", ""),
    ("raci", "Artistes, créateurs et intellectuels", "الفنانون والمبدعون والمثقفون", ""),
    ("rtfr", "Travailleurs à faibles revenus", "العملة ذوو الدخل الضعيف", "plafond"),
    ("rtte", "Tunisiens à l'étranger", "التونسيون بالخارج", ""),
]

# Le régime des étudiants ne relève pas d'un taux : c'est un montant forfaitaire, et il
# n'a donc pas sa place dans un tableau de pourcentages. Le chapitre le dit en prose.
NOTE_PLAFOND = {
    "fr": " (assiette plafonnée à 0,66 SMIG)",
    "ar": " (وعاء محدود بـ 0,66 من الأجر الأدنى)",
}


def _taux(langue):
    def rendu(v):
        return "—" if v is None else ot.formate_taux(v)
    return rendu


def _dernier(chemin: str) -> float | None:
    serie = ot.taux_datee(chemin)
    return serie[-1][1] if serie else None


def _somme_cote(regime: str, cote: str) -> float | None:
    """Somme des taux en vigueur d'un côté d'un régime, hors retraite complémentaire.

    On PARCOURT l'arborescence du régime au lieu d'énumérer des branches connues : les
    régimes n'ont pas les mêmes, et une liste écrite à la main deviendrait fausse au
    premier paramètre ajouté. La retraite complémentaire est écartée parce qu'elle est
    facultative et ne fait donc pas partie du prélèvement obligatoire.
    """
    racine = ot._racine_paquet()
    if racine is None:
        return None
    dossier = Path(str(racine)) / PRIVE.replace("parameters/", "parameters/") / regime
    dossier = Path(str(racine)) / Path(PRIVE).relative_to("parameters") / regime
    dossier = Path(str(racine)) / "parameters" / Path(PRIVE).relative_to("parameters") / regime
    base = dossier / f"cotisations_{cote}"
    if not base.is_dir():
        return None
    somme, trouve = 0.0, False
    for fichier in sorted(base.rglob("*.yaml")):
        if fichier.name == "index.yaml" or "retraite_complementaire" in fichier.name:
            continue
        relatif = fichier.relative_to(Path(str(racine))).as_posix()
        valeur = _dernier(relatif)
        if valeur is not None:
            somme += valeur
            trouve = True
    return somme if trouve else None


def rsna_branches(langue):
    """Le régime général branche par branche, part salariale et part patronale."""
    import pandas as pd

    m = MOTS[langue]
    lignes = []
    for cle, relatif in BRANCHES_RSNA:
        sal = _dernier(f"{PRIVE}/rsna/cotisations_salarie/{relatif}")
        emp = _dernier(f"{PRIVE}/rsna/cotisations_employeur/{relatif}")
        if sal is None and emp is None:
            continue
        lignes.append({
            m["branche"]: m[cle],
            m["salarie"]: _taux(langue)(sal),
            m["employeur"]: _taux(langue)(emp),
            m["total"]: _taux(langue)((sal or 0) + (emp or 0)),
        })
    return pd.DataFrame(lignes)


def coin_par_regime(langue):
    """Le coin social de chaque régime : ce que le régime prélève au total."""
    import pandas as pd

    m = MOTS[langue]
    lignes = []
    for code, nom_fr, nom_ar, marque in REGIMES:
        totaux = {c: _somme_cote(code, c) for c in ("salarie", "employeur")}
        if totaux["salarie"] is None and totaux["employeur"] is None:
            continue
        nom = nom_fr if langue == "fr" else nom_ar
        if marque == "plafond":
            nom += NOTE_PLAFOND[langue]
        lignes.append({
            m["regime"]: nom,
            m["salarie"]: _taux(langue)(totaux["salarie"]),
            m["employeur"]: _taux(langue)(totaux["employeur"]),
            m["total"]: _taux(langue)((totaux["salarie"] or 0) + (totaux["employeur"] or 0)),
        })
    return pd.DataFrame(lignes)


def cnrps_retraite(langue):
    """La seule série longue du corpus : douze millésimes de 1959 à 2020."""
    m = MOTS[langue]
    return ot.tableau_taux_datee(
        [(f"{PUBLIC}/salarie_cnrps/cotisations_salarie/retraite.yaml",
          m["cnrps_retraite"], _taux(langue))],
        colonne_periode=m["effet"], colonne_texte=m["texte"], langue=langue)


TABLEAUX = {
    "rsna_branches.md": rsna_branches,
    "coin_par_regime.md": coin_par_regime,
    "cnrps_retraite.md": cnrps_retraite,
}


def main() -> int:
    if not ot.openfisca_utilisable():
        print(f"openfisca-tunisia indisponible ou trop ancien "
              f"(version {ot.version_openfisca()}, minimum {ot.VERSION_MINIMALE}).")
        return 1
    for langue in LANGUES:
        sortie = RACINE / langue / "cotisations_sociales" / "tables"
        sortie.mkdir(parents=True, exist_ok=True)
        for nom, fabrique in TABLEAUX.items():
            df = fabrique(langue)
            if df is None or df.empty:
                print(f"✗ {langue}/{nom} : paramètre introuvable ou vide.")
                return 1
            (sortie / nom).write_text(ot.tableau_vers_markdown(df), encoding="utf-8")
        print(f"✓ {langue} : {len(TABLEAUX)} tableaux")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

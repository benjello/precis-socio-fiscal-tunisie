"""Câble les livres arabes sur les livres français, et pose des pages-relais.

    uv run python scripts/arabe_cablage.py              # écrit ce qui manque
    uv run python scripts/arabe_cablage.py --verifier   # échoue si le câblage dérive

Déterministe, sans modèle, sans réseau. Appelé par `translation-sync.yml` après la passe de
traduction ; ne s'écrit jamais à la main sous `precis/ar/` ce qu'il produit.

CE QUE FAIT LE SCRIPT, pour chaque livre qui a un `_quarto.yml` arabe :

  1. les listes `chapters:` et `appendices:` arabes reprennent celles du français, dans
     l'ordre français. Ce qui n'a PAS d'original français est conservé et placé à la fin de
     la liste : le reste du fichier (`dir: rtl`, bloc `language:`, titres, légendes) n'est
     jamais touché, seul le texte des deux listes est réécrit ;
  2. un chapitre dont le `.qmd` arabe n'existe pas reçoit une PAGE-RELAIS : le titre (arabe si
     le glossaire en fournit un, sinon français, avec la même ancre que l'original pour que
     les renvois `@sec-…` des autres chapitres arabes se résolvent), l'avis « هذا الفصل لم
     يُترجم بعد » et un lien vers la version française. Le livre arabe se construit donc
     toujours, sans 404 ni chapitre oublié ;
  3. les pages générales françaises (`precis/fr/*.qmd`) sans arabe reçoivent aussi un relais.

LE RELAIS N'EST PAS UNE TRADUCTION. Il porte, juste après l'en-tête YAML, un commentaire
HTML (`MARQUEUR_RELAIS`). `traduction_en_retard.py` le tient pour « jamais traduit »,
`check_translation_parity.py` l'ignore, et `translate_sync.py` l'écrase sans le prendre pour
une ancienne traduction.

Hors champ : un livre sans `_quarto.yml` arabe (le câblage n'en crée pas), et `_glossaire.qmd`,
engendré par `build_glossary.py`, jamais remplacé par un relais.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PRECIS = RACINE / "precis"

MARQUEUR_RELAIS = ("<!-- Page-relais engendrée par scripts/arabe_cablage.py : "
                   "sera remplacée par la traduction. -->")
_SIGNATURE = "Page-relais engendrée par scripts/arabe_cablage.py"
AVIS = "هذا الفصل لم يُترجم بعد"
LIEN_FR = "النسخة الفرنسية"
CLES = ("chapters", "appendices")
TITRE_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
ANCRE_RE = re.compile(r"\s*\{([^}]*)\}\s*$")
ID_RE = re.compile(r"#([A-Za-z][\w:.-]*)")


def est_relais_texte(texte: str) -> bool:
    return _SIGNATURE in texte[:2000]


def est_relais(chemin: Path) -> bool:
    try:
        return est_relais_texte(chemin.read_text(encoding="utf-8")[:2000])
    except OSError:
        return False


# ---------- titres ----------

def titre_et_ancre(texte_fr: str) -> tuple[str, str | None]:
    """Titre du fichier français : `title:` de l'en-tête YAML, à défaut premier `# `."""
    corps = texte_fr
    if texte_fr.startswith("---\n"):
        fin = texte_fr.find("\n---", 4)
        if fin != -1:
            m = re.search(r'^title:\s*"?(.*?)"?\s*$', texte_fr[4:fin], re.M)
            if m:
                return m.group(1), None
            corps = texte_fr[fin + 4:]
    m = TITRE_RE.search(corps)
    if not m:
        return "", None
    brut = m.group(1)
    ancre = None
    a = ANCRE_RE.search(brut)
    if a:
        i = ID_RE.search(a.group(1))
        ancre = i.group(1) if i else None
        brut = brut[:a.start()]
    return brut.strip(), ancre


def charger_glossaire(chemin: Path | None = None) -> dict[str, str]:
    """{terme français en minuscules: terme arabe}, depuis `precis/glossaire.yml`."""
    import yaml
    chemin = chemin or PRECIS / "glossaire.yml"
    if not chemin.exists():
        return {}
    data = yaml.safe_load(chemin.read_text(encoding="utf-8")) or {}
    sortie = {}
    for e in data.get("entries", []):
        fr = ((e.get("fr") or {}).get("terme") or "").strip().lower()
        ar = ((e.get("ar") or {}).get("terme") or "").strip()
        if fr and ar:
            sortie[fr] = ar
    return sortie


def titre_arabe(titre_fr: str, glossaire: dict[str, str]) -> str:
    return glossaire.get(titre_fr.strip().lower(), titre_fr)


# ---------- relais ----------

def lien_vers_fr(chemin_ar: Path, racine_precis: Path = PRECIS) -> str:
    """Lien relatif du relais vers la page française rendue."""
    rel = chemin_ar.relative_to(racine_precis / "ar")
    profondeur = len(rel.parts) - 1
    cible = Path("fr") / rel.with_suffix(".html")
    return "../" * (profondeur + 1) + cible.as_posix()


def contenu_relais(chemin_ar: Path, texte_fr: str, glossaire: dict[str, str],
                   racine_precis: Path = PRECIS) -> str:
    titre, ancre = titre_et_ancre(texte_fr)
    titre_ar = titre_arabe(titre, glossaire) if titre else chemin_ar.stem
    entete = f"# {titre_ar}" + (f" {{#{ancre}}}" if ancre else "")
    lien = lien_vers_fr(chemin_ar, racine_precis)
    parties = []
    # Une page générale (hors livre) est rendue seule : elle porte sa langue et son sens.
    if chemin_ar.parent == racine_precis / "ar":
        safe = titre_ar.replace('"', "'")
        parties.append(f'---\ntitle: "{safe}"\nlang: ar\ndir: rtl\n---')
        entete = ""
    parties.append(MARQUEUR_RELAIS)
    if entete:
        parties.append(entete)
    parties.append(f"{AVIS}. [{LIEN_FR}]({lien})")
    return "\n\n".join(parties) + "\n"


# ---------- listes de chapitres ----------

def aplatir(items) -> list[str]:
    """Noms de fichiers d'une liste Quarto, parties aplaties (ordre conservé)."""
    sortie: list[str] = []
    for it in items or []:
        if isinstance(it, str):
            sortie.append(it)
        elif isinstance(it, dict):
            if "file" in it:
                sortie.append(it["file"])
            if "href" in it:
                sortie.append(it["href"])
            sortie.extend(aplatir(it.get("chapters")))
    return sortie


def lire_listes(texte_yml: str) -> dict[str, list[str]]:
    import yaml
    book = (yaml.safe_load(texte_yml) or {}).get("book") or {}
    return {c: aplatir(book.get(c)) for c in CLES}


def liste_cablee(fr: list[str], ar: list[str], existe) -> list[str]:
    """Liste arabe voulue : ordre français ; éléments arabes sans original français à la fin.

    `existe(nom)` dit si le fichier arabe est là ou sera créé (relais). Un élément français
    qui n'a pas de fichier arabe et qu'on ne sait pas créer (`_glossaire.qmd`) est omis.
    """
    voulue = [n for n in fr if existe(n) or n in ar]
    voulue += [n for n in ar if n not in fr]
    return voulue


def reecrire_liste(texte_yml: str, cle: str, items: list[str]) -> str:
    """Remplace le bloc `  <cle>:` (sous `book:`) par la liste donnée, le reste intact."""
    lignes = texte_yml.split("\n")
    debut = next((i for i, l in enumerate(lignes) if l == f"  {cle}:"), None)
    if debut is None:
        if not items:
            return texte_yml
        raise ValueError(f"clé « {cle} » absente du _quarto.yml arabe")
    fin = debut + 1
    while fin < len(lignes):
        l = lignes[fin]
        if l.startswith("    ") or l.strip() == "" or l.lstrip().startswith("#"):
            fin += 1
        else:
            break
    # Les lignes vides de queue appartiennent à ce qui suit le bloc.
    while fin > debut + 1 and lignes[fin - 1].strip() == "":
        fin -= 1
    for l in lignes[debut + 1:fin]:
        s = l.strip()
        if s and not s.startswith("#") and not s.startswith("- "):
            raise ValueError(f"élément non géré dans « {cle} » : {l!r}")
        if s.startswith("- part") or s.startswith("- file") or s.startswith("- href"):
            raise ValueError(f"élément structuré non géré dans « {cle} » : {l!r}")
    nouveau = [f"    - {n}" for n in items]
    return "\n".join(lignes[:debut + 1] + nouveau + lignes[fin:])


# ---------- le câblage ----------

def calculer(racine_precis: Path = PRECIS) -> tuple[dict[Path, str], list[str]]:
    """({chemin: contenu voulu}, messages) pour tout ce que le câblage écrirait."""
    glossaire = charger_glossaire(racine_precis / "glossaire.yml")
    voulus: dict[Path, str] = {}
    msgs: list[str] = []

    def relais_pour(chemin_fr: Path) -> None:
        chemin_ar = racine_precis / "ar" / chemin_fr.relative_to(racine_precis / "fr")
        if chemin_ar.exists() and not est_relais(chemin_ar):
            return
        voulus[chemin_ar] = contenu_relais(chemin_ar, chemin_fr.read_text(encoding="utf-8"),
                                           glossaire, racine_precis)

    for yml_ar in sorted((racine_precis / "ar").glob("*/_quarto.yml")):
        livre = yml_ar.parent.name
        yml_fr = racine_precis / "fr" / livre / "_quarto.yml"
        if not yml_fr.exists():
            msgs.append(f"{livre} : pas de _quarto.yml français, laissé tel quel")
            continue
        fr = lire_listes(yml_fr.read_text(encoding="utf-8"))
        texte = yml_ar.read_text(encoding="utf-8")
        ar = lire_listes(texte)
        dossier_ar = yml_ar.parent
        dossier_fr = yml_fr.parent
        for cle in CLES:
            def existe(nom, dossier_ar=dossier_ar, dossier_fr=dossier_fr):
                if (dossier_ar / nom).exists():
                    return True
                return (dossier_fr / nom).exists() and not nom.startswith("_glossaire")
            items = liste_cablee(fr[cle], ar[cle], existe)
            for nom in items:
                if nom in fr[cle] and not (dossier_ar / nom).exists():
                    relais_pour(dossier_fr / nom)
            # Les relais déjà posés restent à jour (titre, lien).
            for nom in items:
                if (dossier_ar / nom).exists() and est_relais(dossier_ar / nom) \
                        and (dossier_fr / nom).exists():
                    relais_pour(dossier_fr / nom)
            texte = reecrire_liste(texte, cle, items)
        if texte != yml_ar.read_text(encoding="utf-8"):
            voulus[yml_ar] = texte

    for page in sorted((racine_precis / "fr").glob("*.qmd")):
        relais_pour(page)
    return voulus, msgs


def ecarts(voulus: dict[Path, str]) -> list[Path]:
    return [p for p, t in sorted(voulus.items())
            if not p.exists() or p.read_text(encoding="utf-8") != t]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verifier", action="store_true",
                    help="n'écrit rien ; échoue si le câblage dérive")
    args = ap.parse_args()
    voulus, msgs = calculer()
    for m in msgs:
        print(m)
    diff = ecarts(voulus)
    if args.verifier:
        if diff:
            print("Le câblage arabe dérive ; relancer `uv run python scripts/arabe_cablage.py` :")
            for p in diff:
                print(f"  - {p.relative_to(RACINE)}")
            return 1
        print("Câblage arabe à jour.")
        return 0
    for p in diff:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(voulus[p], encoding="utf-8")
        print(f"écrit : {p.relative_to(RACINE)}")
    if not diff:
        print("Câblage arabe déjà à jour.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

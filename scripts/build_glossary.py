"""Génère le glossaire bilingue à partir de la source unique `precis/glossaire.yml`.

Usage :
    python scripts/build_glossary.py

Produit :
  1. L'annexe glossaire de chaque précis ciblé, dans les deux langues :
         precis/fr/<book>/_glossaire.qmd
         precis/ar/<book>/_glossaire.qmd
     Chaque terme porte une ancre commune `#g-<id>` et un lien de bascule vers
     l'autre langue (navigation FR ⇄ AR).
  2. `translation_glossary.generated.md` : table FR↔AR injectée dans le pipeline
     de traduction (translate_sync.py / verify_translation.py) pour garantir la
     bijection des termes et éviter les divergences.

Fichiers générés : NE PAS éditer à la main, modifiez `precis/glossaire.yml`.
"""

import os
import sys
import unicodedata

try:
    import yaml
except ImportError:
    print("PyYAML requis : `uv pip install pyyaml` ou `uv run python scripts/build_glossary.py`.")
    sys.exit(1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSSARY = os.path.join(ROOT, "precis", "glossaire.yml")
GENERATED_TABLE = os.path.join(ROOT, "translation_glossary.generated.md")

# Précis pour lesquels on génère l'annexe glossaire (portée incrémentale).
BOOKS = ["remunerations_publiques"]

LANGS = ("fr", "ar")
OTHER = {"fr": "ar", "ar": "fr"}
HEADER = {
    "fr": "Glossaire",
    "ar": "المعجم",
}
INTRO = {
    "fr": (
        "Glossaire bilingue des notions fondamentales. Chaque terme renvoie à "
        "son équivalent arabe (navigation FR ⇄ AR) afin de garantir la "
        "cohérence terminologique entre les deux versions du précis."
    ),
    "ar": (
        "معجم ثنائي اللغة للمفاهيم الأساسية. يحيل كلّ مصطلح إلى مقابله الفرنسي "
        "(تصفّح عربي ⇄ فرنسي) لضمان الاتّساق المصطلحي بين نسختي الملخّص."
    ),
}
SWITCH_LABEL = {"fr": "العربية", "ar": "Français"}
SEE_ALSO = {"fr": "Voir aussi", "ar": "انظر أيضًا"}
REFS = {"fr": "Références", "ar": "المراجع"}
SRC_DEF = {"fr": "Source de la définition", "ar": "مصدر التعريف"}
SRC_TRAD = {"fr": "Terme officiel", "ar": "المصطلح الرسمي"}
DO_NOT_EDIT = {
    "fr": "<!-- Fichier généré par scripts/build_glossary.py — ne pas éditer. Source : precis/glossaire.yml -->",
    "ar": "<!-- ملف مولَّد بواسطة scripts/build_glossary.py — لا تُحرِّره. المصدر: precis/glossaire.yml -->",
}


def load_entries():
    with open(GLOSSARY, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("entries", [])


def cite(source):
    """Rendu d'une source canonique (str ou {ref, locator}) en citation Pandoc."""
    if not source:
        return None
    if isinstance(source, str):
        return f"[@{source}]"
    ref = source.get("ref")
    if not ref:
        return None
    locator = source.get("locator")
    return f"[@{ref}, {locator}]" if locator else f"[@{ref}]"


def validate(entries):
    """Verrou de synchro : termes FR/AR obligatoires partout ; définitions FR/AR
    obligatoires pour les entrées `valide`. Renvoie (errors, warnings)."""
    errors, warnings = [], []
    seen = set()
    for e in entries:
        eid = e.get("id", "<sans id>")
        if eid in seen:
            errors.append(f"{eid} : identifiant en double.")
        seen.add(eid)
        for lang in LANGS:
            block = e.get(lang) or {}
            if not (block.get("terme") or "").strip():
                errors.append(f"{eid} : terme {lang.upper()} manquant.")
        if e.get("statut") == "valide":
            for lang in LANGS:
                block = e.get(lang) or {}
                if not (block.get("definition") or "").strip():
                    errors.append(f"{eid} : définition {lang.upper()} manquante (statut valide).")
            if not e.get("source_definition"):
                warnings.append(eid)
    return errors, warnings


def clean(text):
    return " ".join((text or "").split())


def sort_key(terme, lang):
    """Clé de tri alphabétique : sans accents/casse pour le FR, sans l'article
    défini « ال » pour l'AR (convention d'alphabétisation arabe)."""
    if lang == "ar":
        t = terme.strip()
        if t.startswith("ال") and len(t) > 2:
            t = t[2:]
        return t
    nfkd = unicodedata.normalize("NFKD", terme)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).casefold()


def render_book(entries, book, lang):
    other = OTHER[lang]
    by_id = {e["id"]: e for e in entries}
    ordered = sorted(entries, key=lambda e: sort_key(e[lang]["terme"], lang))

    lines = [DO_NOT_EDIT[lang], "", f"# {HEADER[lang]} {{.unnumbered}}", "", INTRO[lang], ""]

    for e in ordered:
        eid = e["id"]
        terme = e[lang]["terme"]
        acro = e.get("acronyme")
        title = f"{terme} ({acro})" if acro else terme
        lines.append(f"## {title} {{#g-{eid}}}")
        lines.append("")
        # Lien de bascule vers l'autre langue (chemin du site assemblé local_site)
        switch_url = f"../../{other}/{book}/_glossaire.html#g-{eid}"
        lines.append(f"[{SWITCH_LABEL[lang]} → {e[other]['terme']}]({switch_url})")
        lines.append("")
        lines.append(clean(e[lang]["definition"]))
        lines.append("")
        src_def = cite(e.get("source_definition"))
        if src_def:
            lines.append(f"*{SRC_DEF[lang]} :* {src_def}")
            lines.append("")
        src_trad = cite(e.get("source_traduction"))
        if src_trad:
            lines.append(f"*{SRC_TRAD[lang]} :* {src_trad}")
            lines.append("")
        voir = [v for v in e.get("voir_aussi", []) if v in by_id]
        if voir:
            links = ", ".join(f"[{by_id[v][lang]['terme']}](#g-{v})" for v in voir)
            lines.append(f"*{SEE_ALSO[lang]} :* {links}")
            lines.append("")
        refs = e.get("references", [])
        if refs:
            cites = " ".join(f"[@{r}]" for r in refs)
            lines.append(f"*{REFS[lang]} :* {cites}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_translation_table(entries):
    lines = [
        "<!-- Fichier généré par scripts/build_glossary.py — ne pas éditer. Source : precis/glossaire.yml -->",
        "",
        "## Glossaire terminologique canonique (FR ⇄ AR)",
        "",
        "Table de référence absolue pour la bijection des termes. Toute traduction",
        "doit utiliser exactement l'équivalent indiqué ci-dessous, sans variation.",
        "",
        "| Français | Arabe (Tunisie) | Acronyme |",
        "| :--- | :--- | :--- |",
    ]
    for e in sorted(entries, key=lambda e: sort_key(e["fr"]["terme"], "fr")):
        acro = e.get("acronyme") or ""
        lines.append(f"| {e['fr']['terme']} | {e['ar']['terme']} | {acro} |")
    return "\n".join(lines) + "\n"


def main():
    entries = load_entries()
    if not entries:
        print("Aucune entrée dans precis/glossaire.yml.")
        sys.exit(1)

    errors, warnings = validate(entries)
    if errors:
        print("✗ Glossaire invalide (synchro FR/AR) :")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    if warnings:
        print(f"⚠ {len(warnings)} entrée(s) « valide » sans source_definition : {', '.join(warnings)}")

    written = []
    for book in BOOKS:
        for lang in LANGS:
            out_dir = os.path.join(ROOT, "precis", lang, book)
            if not os.path.isdir(out_dir):
                print(f"Ignoré : {out_dir} (dossier absent).")
                continue
            out_path = os.path.join(out_dir, "_glossaire.qmd")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(render_book(entries, book, lang))
            written.append(os.path.relpath(out_path, ROOT))

    with open(GENERATED_TABLE, "w", encoding="utf-8") as f:
        f.write(render_translation_table(entries))
    written.append(os.path.relpath(GENERATED_TABLE, ROOT))

    print(f"{len(entries)} entrées. Fichiers générés :")
    for w in written:
        print(f"  - {w}")


if __name__ == "__main__":
    main()

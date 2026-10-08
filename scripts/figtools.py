"""Outils partagés de figures pour le précis (traçabilité + téléchargement sourcé).

Frontière : les **séries** viennent du paquet `tunisia_data` (entrepôt) ; ici on
prépare le **jeu de données de la figure** (figdata), on écrit sa provenance, et on
fournit la ligne « Source » et le lien de téléchargement. Les figures elles-mêmes
sont définies **par livre** (`precis/fr/<livre>/figures/`), jamais à la racine ; celles
d'une page de site (l'annexe sur le PIB) vivent à côté d'elle, dans `precis/fr/figures/`.

La provenance (sources/clés de citation, unité, périmètre, base, caveats) est tirée
de `tunisia_data.meta(series_id)` — jamais saisie à la main.

Autonomie de build (diffusion GitHub Pages)
-------------------------------------------
Le rendu du site **ne dépend pas** de la présence de l'entrepôt `tunisia_data`.
`series()` et `meta()` utilisent l'entrepôt s'il est importable (dev local), sinon
ils retombent sur un **snapshot versionné dans le précis** (`precis/_seriescache/` :
un CSV par série + `catalog.snapshot.yml` pour la provenance). Le snapshot est
régénéré depuis l'entrepôt par `refresh_cache(*series_ids)` (étape « produire »),
puis committé. Ainsi le build CI/Pages reste reproductible sans le repo privé.
"""
from __future__ import annotations

import datetime as _dt
import functools
from pathlib import Path
from typing import TYPE_CHECKING

# `pandas` n'est PAS importé à l'exécution, à dessein — comme `matplotlib`,
# `arabic_reshaper`, `itables` et `tunisia_data` plus bas, il l'est dans la seule
# fonction qui s'en sert, `series()`.
#
# Sans cela le module entier est inimportable sans pandas, et les fonctions purement
# textuelles qu'il porte — `date_deja_inscrite` — deviennent intestables : le job de
# tests n'installe aucune dépendance, précisément pour qu'un test qui réclame un
# paquet signale qu'il teste autre chose que ce qu'il annonce.
#
# La garde ci-dessous lie tout de même `pd` pour les annotations. `from __future__
# import annotations` suffirait à l'exécution, les annotations n'étant alors jamais
# évaluées ; mais le nom resterait non lié pour les vérificateurs de types et pour
# tout ce qui appelle `typing.get_type_hints()`.
if TYPE_CHECKING:  # pragma: no cover - jamais vrai à l'exécution
    import pandas as pd

# Cache versionné sous precis/ (jamais à la racine du repo) : autonomie de build.
_CACHE = Path(__file__).resolve().parent.parent / "precis" / "_seriescache"


# --- i18n : la langue du livre est déduite du cwd au render (precis/<lang>/...) ---
def lang() -> str:
    """Langue du livre en cours de rendu, déduite du chemin de travail."""
    p = Path.cwd().as_posix()
    if "/ar/" in p or p.endswith("/ar"):
        return "ar"
    return "fr"


# Chrome d'interface généré par Python (jamais vu par le pipeline de traduction).
# Le texte des figures (titres/axes/légendes/en-têtes) est, lui, dans chaque module.
_UI = {
    "tab_graph":  {"fr": "📈 Graphique",  "ar": "📈 الرسم البياني"},
    "tab_data":   {"fr": "📊 Données",    "ar": "📊 البيانات"},
    "tab_src":    {"fr": "🔗 Sources",    "ar": "🔗 المصادر"},
    "tab_base":   {"fr": "⚖️ Base législative", "ar": "⚖️ القاعدة التشريعية"},
    "base_intro": {"fr": "Chaque grandeur de la figure, avec toutes ses valeurs datées et "
                         "leurs références :",
                   "ar": "كلّ مقدار في الرسم البياني، بجميع قيمه المؤرّخة ومراجعها:"},
    "source":     {"fr": "Source",        "ar": "المصدر"},
    "nominal":    {"fr": "valeurs courantes (nominal)", "ar": "قيم جارية (اسمية)"},
    "pib_base":   {"fr": "PIB base",      "ar": "الناتج المحلي الإجمالي، أساس"},
    "consult":    {"fr": "consulter la série en ligne ↗",
                   "ar": "الاطّلاع على السلسلة عبر الإنترنت ↗"},
    "perimetre":  {"fr": "périmètre",     "ar": "النطاق"},
    "unite":      {"fr": "unité",         "ar": "الوحدة"},
    "reserves":   {"fr": "Réserves",      "ar": "تحفّظات"},
    "download":   {"fr": "Télécharger les données (sourcées)",
                   "ar": "تنزيل البيانات (مع مصادرها)"},
    "how_to_read": {"fr": "Comment lire cette figure",
                    "ar": "كيف نقرأ هذا الرسم البياني"},
    # Figure en escalier d'une série de paramètres datés (`figure_escalier`).
    "esc_x":           {"fr": "Date d'effet", "ar": "تاريخ النفاذ"},
    "esc_annee":       {"fr": "Année", "ar": "السنة"},
    "esc_parametre":   {"fr": "Grandeur", "ar": "المقدار"},
    "esc_effet":       {"fr": "Date d'effet", "ar": "تاريخ النفاذ"},
    "esc_valeur":      {"fr": "Valeur", "ar": "القيمة"},
    "esc_etat":        {"fr": "Ce que fait le texte", "ar": "أثر النصّ"},
    "esc_texte":       {"fr": "Texte", "ar": "النصّ"},
    "esc_jort":        {"fr": "Journal officiel", "ar": "الرائد الرسمي"},
    "esc_creation":    {"fr": "fixe la valeur", "ar": "يضبط القيمة"},
    "esc_changement":  {"fr": "change la valeur", "ar": "يغيّر القيمة"},
    "esc_reprise":     {"fr": "reprend la valeur sans la changer",
                        "ar": "يُبقي القيمة دون تغيير"},
    "esc_suppression": {"fr": "supprime la grandeur", "ar": "يلغي المقدار"},
    "esc_supprime":    {"fr": "supprimé", "ar": "أُلغي"},
    "esc_courants":    {"fr": "Dinars courants", "ar": "بالدينار الجاري"},
    "esc_constants":   {"fr": "Dinars de {base}", "ar": "بدينار سنة {base}"},
    "esc_moyenne":     {"fr": "Montant en vigueur, moyenne de l'année (dinars courants)",
                        "ar": "المبلغ الجاري به العمل، معدّل السنة (بالدينار الجاري)"},
    "esc_ipc":         {"fr": "Indice des prix à la consommation",
                        "ar": "الرقم القياسي لأسعار الاستهلاك"},
    "esc_reel":        {"fr": "Montant en dinars de {base}", "ar": "المبلغ بدينار سنة {base}"},
}


def t(key: str) -> str:
    """Traduit une chaîne de chrome d'interface selon la langue courante."""
    return _UI[key].get(lang(), _UI[key]["fr"])


# --- arabe dans matplotlib : police OFL embarquée + shaping RTL ---------------
@functools.lru_cache(maxsize=1)
def _register_ar_font() -> str:
    """Enregistre la police arabe embarquée (indépendance CI) ; retourne son nom."""
    from matplotlib import font_manager
    fp = Path(__file__).resolve().parent / "fonts" / "NotoNaskhArabic-Regular.ttf"
    font_manager.fontManager.addfont(str(fp))
    return font_manager.FontProperties(fname=str(fp)).get_name()


def apply_lang_font() -> None:
    """Configure la police des figures pour le livre courant (arabe si lang=ar).

    Police arabe + repli DejaVu Sans pour les chiffres/symboles latins.
    À appeler une fois en tête de chaque fonction de figure.
    """
    if lang() != "ar":
        return
    import matplotlib as mpl
    name = _register_ar_font()
    mpl.rcParams["font.family"] = [name, "DejaVu Sans"]


def fig_text(s: str) -> str:
    """Met en forme une chaîne pour matplotlib (shaping + RTL en arabe, sinon identité)."""
    if lang() != "ar":
        return s
    import arabic_reshaper
    from bidi.algorithm import get_display
    return get_display(arabic_reshaper.reshape(s))


def _td():
    """Retourne le module `tunisia_data` s'il est installé, sinon None."""
    try:
        import tunisia_data as td
        return td
    except Exception:
        return None


@functools.lru_cache(maxsize=1)
def _snapshot() -> dict:
    """Provenance snapshotée {id: entrée} lue depuis le cache du précis."""
    f = _CACHE / "catalog.snapshot.yml"
    if not f.exists():
        return {}
    import yaml
    return {e["id"]: e for e in (yaml.safe_load(f.read_text(encoding="utf-8")) or [])}


# Provenance déclarée par un module de figure, pour les séries qui ne viennent PAS de
# l'entrepôt. Le précis a deux origines de données : `tunisia-data` pour les statistiques
# publiées, et les paramètres d'`openfisca-tunisia` pour le droit codé. Les secondes n'ont
# pas de place dans le catalogue de l'entrepôt — ce ne sont pas des observations — mais
# elles doivent être sourcées comme les autres.
_DECLAREES: dict[str, dict] = {}


def register_provenance(series_id: str, **champs) -> None:
    """Déclare la provenance d'une série locale (paramètres openfisca, notamment).

    Mêmes champs que le catalogue de l'entrepôt : `titre`, `sources` (clés de citation),
    `unite`, `perimetre`, `caveats`, et leurs variantes `_ar`.
    """
    _DECLAREES[series_id] = {"id": series_id, **champs}


def meta(series_id: str) -> dict:
    """Provenance d'une série : déclaration locale, sinon entrepôt, sinon snapshot."""
    if series_id in _DECLAREES:
        return _DECLAREES[series_id]
    td = _td()
    if td is not None:
        try:
            return td.meta(series_id)
        except Exception:
            pass
    snap = _snapshot()
    if series_id in snap:
        return snap[series_id]
    raise KeyError(f"série inconnue: {series_id!r} (ni entrepôt, ni snapshot)")


def series(series_id: str) -> pd.DataFrame:
    """Données d'une série : entrepôt si présent, sinon CSV snapshoté du précis.

    Vaut pour les DEUX origines du précis. Les séries de `tunisia-data` sont snapshotées
    par `refresh_cache()` ; celles qui viennent des paramètres d'openfisca — du droit codé,
    non des observations — sont snapshotées par les générateurs de tableaux, qui lisent
    déjà ces paramètres. Dans les deux cas le build ne voit qu'un CSV versionné, et une
    figure n'a jamais à lire une source vive (#165).

    `register_provenance` reste le moyen de déclarer la provenance d'une série absente du
    catalogue de l'entrepôt ; il ne dit rien de l'endroit où vivent ses données.
    """
    td = _td()
    if td is not None:
        try:
            return td.load(series_id)
        except Exception:
            pass
    p = _CACHE / f"{series_id}.csv"
    if p.exists():
        import pandas as pd  # import différé : voir l'en-tête du module

        return pd.read_csv(p)
    raise FileNotFoundError(
        f"série {series_id!r} absente du cache {p} — lancer figtools.refresh_cache()")


def refresh_cache(*series_ids: str) -> None:
    """Snapshote séries + provenance depuis l'entrepôt vers le cache du précis.

    À lancer en dev (entrepôt présent) puis committer `_seriescache/`. Fusionne
    avec le snapshot existant pour ne pas perdre les séries des autres livres.
    """
    td = _td()
    if td is None:
        raise RuntimeError("tunisia_data requis pour rafraîchir le cache des séries")
    import yaml
    _CACHE.mkdir(parents=True, exist_ok=True)
    snap_path = _CACHE / "catalog.snapshot.yml"
    existing = {}
    if snap_path.exists():
        existing = {e["id"]: e for e in (yaml.safe_load(snap_path.read_text("utf-8")) or [])}
    for sid in series_ids:
        td.load(sid).to_csv(_CACHE / f"{sid}.csv", index=False)
        existing[sid] = td.meta(sid)
    snap_path.write_text(
        yaml.safe_dump(list(existing.values()), allow_unicode=True, sort_keys=False),
        encoding="utf-8")
    _snapshot.cache_clear()


def _meta(series_id: str) -> dict:
    return meta(series_id)


def source_line(*series_ids: str, nominal: bool = True) -> str:
    """Ligne « Source » d'une figure, assemblée depuis la provenance des séries.

    `nominal=False` retire la mention « valeurs courantes (nominal) » : une figure en volume
    a des séries en %, que la règle ci-dessous prendrait pour monétaires.

    Une série qui a des dizaines de sources — une grille par avenant — peut déclarer une
    `source_ligne` (ou `source_ligne_<langue>`) : ce texte Markdown, citations comprises,
    tient alors lieu de ses clés dans cette seule ligne. L'onglet « Sources » et l'en-tête
    du figdata gardent la liste entière de `sources` : aucune référence n'est perdue.
    """
    keys, bases, units = [], set(), set()
    for sid in series_ids:
        m = _meta(sid)
        ligne = m.get(f"source_ligne_{lang()}") or m.get("source_ligne")
        keys += [ligne] if ligne else [f"@{k}" for k in m.get("sources", [])]
        if m.get("base_pib"):
            bases.add(str(m["base_pib"]))
        if m.get("unite"):
            units.add(str(m["unite"]).lower())
    parts = [f"{t('source')} : " + ", ".join(dict.fromkeys(keys))]
    if bases:
        parts.append(f"{t('pib_base')} " + "/".join(sorted(bases)))
    # mention « prix courants » seulement pour les séries monétaires (pas les effectifs)
    monetaire = any(k in u for u in units
                    for k in ("dinar", "pib", "dépense", "depense", "%", "budget"))
    if monetaire and nominal:
        parts.append(t("nominal"))
    return " — ".join(parts)


def date_deja_inscrite(ancien_texte: str | None, entete_sans_date: list[str],
                       corps: str) -> str | None:
    """Rend la date du figdata existant si RIEN d'autre n'a changé, sinon `None`.

    Fonction pure : elle reçoit le texte déjà écrit, et ne lit aucun fichier.

    `None` — donc une date neuve — dès que le fichier est absent, que sa provenance
    diffère (séries, sources, fiches, réserves, note) ou que ses données diffèrent.
    La date ne survit qu'à un rendu strictement identique.
    """
    if not ancien_texte:
        return None
    lignes = ancien_texte.split("\n")
    entete = []
    for ligne in lignes:
        if not ligne.startswith("#"):
            break
        entete.append(ligne)
    if not entete:
        return None
    if entete[1:] != entete_sans_date:
        return None
    if "\n".join(lignes[len(entete):]) != corps:
        return None
    date = entete[0].rsplit(" ", 1)[-1].strip()
    # Une date doit ressembler à une date. Sur un en-tête tronqué, `rsplit` rend le mot
    # qui précède : « … généré le » donne « le », valeur non vide qui serait réécrite
    # telle quelle dans le fichier — l'en-tête de provenance afficherait « généré le le ».
    # Vérifier la forme couvre du même coup l'en-tête corrompu.
    try:
        _dt.date.fromisoformat(date)
    except ValueError:
        return None
    return date


def write_figdata(df: pd.DataFrame, out_csv: Path, *series_ids: str,
                  note: str | None = None, generated: str | None = None) -> Path:
    """Écrit le figdata téléchargeable, avec en-tête de provenance commenté + sidecar .yml.

    `generated` : date ISO passée explicitement (Quarto/CI) — pas de Date.now() implicite.
    """
    out_csv = Path(out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    keys = []
    fiches = []
    caveats = []
    for sid in series_ids:
        m = _meta(sid)
        keys += m.get("sources", [])
        if m.get("fiche"):
            fiches.append(m["fiche"])
        if m.get("caveats"):
            caveats.append(m["caveats"])
    # Deux séries peuvent partager la même fiche de source : c'est le cas dès qu'une figure
    # joint un montant et son dénominateur, tirés du même classeur du ministère. Les clés de
    # citation étaient déjà dédoublonnées ; les fiches et les réserves ne l'étaient pas, et
    # l'en-tête de provenance répétait alors deux fois le même fichier — dans un CSV publié
    # et téléchargeable, où il tient lieu de source.
    fiches = list(dict.fromkeys(fiches))
    caveats = list(dict.fromkeys(caveats))
    # un shortcode Quarto non résolu (passé tel quel depuis un chunk) → date du jour
    if not generated or "{{" in generated:
        generated = _dt.date.today().isoformat()
    entete_sans_date = [
        f"# séries (tunisia_data) : {', '.join(series_ids)}",
        f"# sources (citation) : {', '.join('@'+k for k in dict.fromkeys(keys))}",
        f"# fiches : {', '.join(fiches)}",
        f"# méthode/hypothèses : {', '.join(caveats)}",
    ]
    if note:
        entete_sans_date.append(f"# note : {note}")
    corps = df.to_csv(index=False)
    # Un rendu qui ne change ni les données ni la provenance ne doit pas redater le
    # fichier : sinon chaque `quarto render` salit le dépôt d'une vingtaine de figdata
    # dont SEULE la date bouge, qu'il faut ensuite restaurer à la main avant tout
    # commit. Le 16/09/2026, quatre restaurations en une matinée.
    #
    # La date n'est conservée que si l'en-tête HORS date est lui aussi inchangé. Une
    # légende, une source ou une réserve modifiée doit redater : à défaut, l'en-tête
    # de provenance — qui tient lieu de source dans un CSV publié et téléchargeable —
    # mentirait sur la date de ce qu'il décrit.
    try:
        ancien = out_csv.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        ancien = None
    stamp = date_deja_inscrite(ancien, entete_sans_date, corps) or generated
    header = [f"# Figure-data du précis socio-fiscal tunisien — généré le {stamp}"]
    header += entete_sans_date
    nouveau_csv = "\n".join(header) + "\n" + corps
    # `date_deja_inscrite` rend déjà l'ancienne date quand le contenu (hors date) n'a
    # pas changé, ce qui suffit à ce que le CSV réécrit soit OCTET POUR OCTET identique
    # à l'existant. Mais réécrire quand même touche le fichier : mtime modifié, et
    # certains outils (rsync, un `make` qui dépend des horodatages) le voient comme
    # changé alors que git ne le verrait pas. On compare donc le contenu produit à
    # l'existant et on n'écrit que s'il diffère — ni le CSV, ni son sidecar.
    if ancien != nouveau_csv:
        with out_csv.open("w", encoding="utf-8", newline="") as f:
            f.write(nouveau_csv)
    # sidecar yaml (lisible machine)
    side = out_csv.with_suffix(out_csv.suffix + ".yml")
    nouveau_side = "series: [{}]\nsources: [{}]\nfiches: [{}]\ncaveats: [{}]\ngenerated: {}\n".format(
        ", ".join(series_ids), ", ".join(dict.fromkeys(keys)),
        ", ".join(fiches), ", ".join(caveats), stamp)
    try:
        ancien_side = side.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        ancien_side = None
    if ancien_side != nouveau_side:
        side.write_text(nouveau_side, encoding="utf-8")
    return out_csv


def download_button(figdata_csv: str, label: str | None = None) -> str:
    """Markdown du lien de téléchargement (le site sert le figdata sourcé, pas le raw)."""
    return f"[⬇️ {label or t('download')}]({figdata_csv}){{download=\"\"}}"


# --- traçabilité détaillée des sources ---------------------------------------

@functools.lru_cache(maxsize=1)
def _ref_index() -> dict:
    """Index {clé: entrée CSL} des references.json visibles depuis le cwd.

    Lit `references.json` du livre (cwd) puis ceux des dossiers parents
    (`../references.json` = bibliographie commune). Sert à enrichir la
    provenance : titre lisible et URL web de la source d'origine.
    """
    import json
    idx: dict = {}
    seen = set()
    for base in (Path.cwd(), *Path.cwd().parents):
        rj = base / "references.json"
        if rj in seen or not rj.exists():
            continue
        seen.add(rj)
        try:
            items = json.loads(rj.read_text(encoding="utf-8")).get("items", [])
        except (ValueError, OSError):
            continue
        for e in items:
            idx.setdefault(e.get("id"), e)  # le plus proche (livre) prime
        if base == Path.cwd().anchor:
            break
    return idx


def source_details(*series_ids: str) -> str:
    """Bloc Markdown « Sources & traçabilité » : tout ce qui permet de remonter
    de la figure jusqu'au fichier brut récupéré sur le web.

    Pour chaque série : titre + clé de citation, **lien web** vers la source
    d'origine (references.json), fiche de provenance, fichiers raw de l'entrepôt
    `tunisia-data`, périmètre, unité, base PIB, hypothèses/caveats.
    """
    def mf(m, key, default=None):
        """Champ de provenance localisé : `<key>_<lang>` si présent, sinon `<key>`."""
        return m.get(f"{key}_{lang()}") or m.get(key, default)

    refs = _ref_index()
    blocks = []
    for sid in series_ids:
        m = _meta(sid)
        lines = [f"**{mf(m, 'titre', sid)}**\n"]
        for key in m.get("sources", []):
            ref = refs.get(key, {})
            titre = ref.get("title", key)
            url = ref.get("URL")  # lien public vers la série/l'enquête (site producteur)
            cite = f"[@{key}]"
            if url:
                lines.append(f"- {cite} — {titre} · [{t('consult')}]({url})")
            else:
                lines.append(f"- {cite} — {titre}")
        meta_bits = []
        if mf(m, "perimetre"):
            meta_bits.append(f"*{t('perimetre')}* : {mf(m, 'perimetre')}")
        if mf(m, "unite"):
            meta_bits.append(f"*{t('unite')}* : {mf(m, 'unite')}")
        if m.get("base_pib"):
            meta_bits.append(f"*{t('pib_base')}* : {m['base_pib']}")
        if meta_bits:
            lines.append("- " + " · ".join(meta_bits))
        cav = mf(m, "caveats")
        if cav and not str(cav).endswith(".md"):  # pas de chemin local de fiche
            lines.append(f"- ⚠️ *{t('reserves')}* : {cav}")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def base_legislative(*series_ids: str) -> str:
    """Liste Markdown des liens « Base législative » des séries, vide s'il n'y en a pas.

    Une série tirée du droit codé — et non d'une statistique publiée — est émise dans
    `_seriescache/` par un générateur de tableaux, qui écrit à côté d'elle la liste des
    grandeurs qu'il a lues : `<série>.liens.<langue>.yml`, même schéma que les
    `tables/<nom>.liens.yml` (`libelle`, `parametre`, `url`). Les liens sont donc
    engendrés, jamais écrits à la main ; on ne fait ici que les lire — le build du site
    n'importe pas le générateur.
    """
    import yaml

    vus, items = set(), []
    for sid in series_ids:
        f = _CACHE / f"{sid}.liens.{lang()}.yml"
        if not f.exists():
            continue
        for e in yaml.safe_load(f.read_text(encoding="utf-8")) or []:
            if e["url"] not in vus:
                vus.add(e["url"])
                items.append(f"- [{e['libelle']}]({e['url']})")
    if not items:
        return ""
    return f"{t('base_intro')}\n\n" + "\n".join(items)


def infobulle(artiste, texte: str) -> None:
    """Attache une infobulle à un élément tracé (point, trait, barre) d'une figure matplotlib.

    Le texte s'affiche au survol dans la page HTML : `figure_tabs` émet alors la figure en SVG
    en ligne, où l'élément porte un `<title>` — l'infobulle native du navigateur, lue aussi
    par les lecteurs d'écran. Le PDF garde l'image fixe. Pour un texte par point, tracer
    chaque point par son propre appel : un `plot` à plusieurs marqueurs n'a qu'un élément.
    """
    registre = artiste.figure.__dict__.setdefault("_infobulles", {})
    gid = f"ib-{len(registre)}"
    artiste.set_gid(gid)
    registre[gid] = texte


def marque_rupture(ax, annee: int, texte: str | None = None):
    """Marque une rupture de série entre `annee - 1` et `annee` (axe des abscisses en années).

    Ligne verticale pointillée à mi-chemin des deux années ; `texte`, s'il est donné, est
    posé en haut du cadre, à droite de la ligne. Sert notamment aux changements de base
    des comptes nationaux sous un ratio au PIB : la rupture se montre, elle ne se corrige
    pas — aucune conversion d'une base à l'autre.

    Rend le trait tracé, pour qui veut lui attacher une `infobulle`.
    """
    x = annee - 0.5
    trait = ax.axvline(x, color="#57606a", ls=(0, (2, 2)), lw=1, zorder=1)
    if texte:
        ax.annotate(texte, xy=(x, 1), xycoords=("data", "axes fraction"),
                    xytext=(4, -4), textcoords="offset points", ha="left", va="top",
                    fontsize=7, color="#57606a")
    return trait


# --- les paramètres dans le temps : la figure en escalier ----------------------
#
# DES MARCHES, PAS DES PENTES. Une valeur légale vaut du jour de son effet à la veille de la
# suivante : chaque grandeur est tracée en escalier, la marche posée à la date d'effet. La
# série est une SÉRIE LONGUE de `_seriescache/` — une ligne par grandeur et par date d'effet
# (`<colonne>, date_effet, valeur`, et, si elle les porte, `texte, lien`) —, émise par un
# générateur de tableaux (`openfisca_tables.ecrire_serie_parametres`). La figure la lit par
# `series()` : jamais les paramètres eux-mêmes, que le build du site n'a pas.
#
# Deux lignes de la série ne sont pas des marches :
#   - une ligne SANS valeur dit la suppression de la grandeur à cette date : le trait
#     s'arrête, sur un cercle creux ;
#   - une ligne qui RÉPÈTE la valeur précédente dit un texte qui la reprend sans la changer :
#     un losange creux sur le trait, sans marche ni étiquette.
#
# Ajouter la figure d'une série ne demande qu'une déclaration : `figure_escalier(...)` dans
# le module de figures du livre, les libellés déjà rendus dans la langue du livre.

# Indice de prix des lectures en dinars constants : (série, colonne de l'année, colonne de
# l'indice) — la série raccordée 1962-2023 que le volume « marché du travail » emploie déjà.
IPC_ESCALIER = ("ipc-longue-periode", "annee", "indice_base1970")


def abscisse_date(date_iso: str) -> float:
    """Date d'effet -> année décimale : le 1er juillet 1988 tombe au milieu de 1988."""
    d = _dt.date.fromisoformat(str(date_iso)[:10])
    return d.year + (d.timetuple().tm_yday - 1) / (366 if d.year % 4 == 0 else 365)


def etats_escalier(lignes: list[tuple[str, float | None, str, str]]
                   ) -> list[tuple[str, float | None, str, str, str]]:
    """Ajoute à chaque ligne d'une grandeur ce que fait son texte. Fonction pure.

    `lignes` : [(date ISO, valeur ou None, texte, lien)], dates croissantes. Rend
    [(date, valeur, état, texte, lien)], l'état déduit de la valeur précédente : `creation`,
    `changement`, `reprise` (même valeur, autre texte) ou `suppression` (plus de valeur).
    """
    sortie, precedente = [], None
    for date, v, texte, lien in lignes:
        if v is None:
            etat = "suppression"
        elif precedente is None:
            etat = "creation"
        else:
            etat = "reprise" if v == precedente else "changement"
        sortie.append((date, v, etat, texte, lien))
        precedente = v
    return sortie


def valeur_escalier(lignes, date_iso: str) -> float | None:
    """Valeur en vigueur à `date_iso` dans les lignes d'une grandeur, ou None. Fonction pure.

    None avant la première date d'effet, et à compter d'une suppression.
    """
    retenue = None
    for date, v, *_ in lignes:
        if date <= date_iso:
            retenue = v
    return retenue


def moyenne_annuelle_escalier(lignes, annee: int) -> float | None:
    """Moyenne des valeurs en vigueur au premier jour de chacun des douze mois. Pure.

    Une hausse du 1er mai compte pour huit mois. None si la grandeur n'existe pas toute
    l'année : une moyenne sur une partie de l'année ne se compare pas aux autres.
    """
    mois = [valeur_escalier(lignes, f"{annee}-{m:02d}-01") for m in range(1, 13)]
    if any(v is None for v in mois):
        return None
    return sum(mois) / 12


def serie_escalier(series_id: str, courbes, colonne: str = "parametre",
                   echelle: float = 1.0) -> dict:
    """La série longue, par grandeur : {clé: [(date, valeur, état, texte, lien)]}.

    `courbes` donne les clés retenues et leur ordre. `echelle` multiplie les valeurs
    (100 pour tracer un taux en pour cent). `texte` et `lien` sont vides quand la série ne
    les porte pas.
    """
    d = series(series_id)
    sortie = {}
    for cle in courbes:
        s = d[d[colonne] == cle].sort_values("date_effet")
        textes = s["texte"] if "texte" in s else [""] * len(s)
        liens = s["lien"] if "lien" in s else [""] * len(s)
        lignes = [(str(date)[:10], None if v != v else round(echelle * float(v), 4), texte, lien)
                  for date, v, texte, lien in zip(s["date_effet"], s["valeur"], textes, liens)]
        if lignes:
            sortie[cle] = etats_escalier(lignes)
    return sortie


def _legende_sous(ax, poignees, ncol: int) -> None:
    ax.legend(handles=poignees, loc="upper center", bbox_to_anchor=(0.5, -0.13),
              fontsize=8, frameon=False, ncol=ncol)


def fig_escalier(series_id: str, courbes: dict, *, fin: int, colonne: str = "parametre",
                 echelle: float = 1.0, format_valeur=None, ylabel: str = "",
                 xlabel: str | None = None, annotations: dict | None = None,
                 etiquettes_x: dict | None = None, xlim=None, ylim=None, yticks=None,
                 log: bool = False, figsize=(9.5, 5.6), ncol: int | None = None,
                 supprime: str | None = None, format_infobulle=None):
    """Les grandeurs d'une série longue en escalier, chaque marche étiquetée de sa valeur.

    `courbes`       : {clé: (libellé de légende, couleur)}, dans l'ordre du tracé.
    `fin`           : dernière année tracée ; les traits courent jusqu'à son 31 décembre. À
                      n'employer que si la dernière valeur de chaque grandeur vaut encore.
    `format_valeur` : valeur -> étiquette de marche (« 17 % », « 150 D ») ; à défaut `%g`.
    `format_infobulle` : valeur -> montant de l'infobulle ; à défaut `format_valeur`. Sert
                      quand les marches, trop nombreuses, ne sont pas étiquetées
                      (`format_valeur` rendant une chaîne vide) : le survol garde le montant.
    `annotations`   : {(clé, date d'effet): texte} — les mentions propres à la figure
                      (« créé hors du code », « supprimé au… »), posées sous le point, ou à
                      sa droite pour une suppression. Un dictionnaire `{"texte": …, "xytext":
                      (dx, dy), "ha": …, "va": …}` en déplace une.
    `etiquettes_x`  : {date d'effet: graduation} ; à défaut l'année de la date.
    `log`           : axe vertical logarithmique, quand les grandeurs sont d'ordres différents.
    `supprime`      : mot de l'infobulle d'une suppression, accordé à la grandeur ; à défaut
                      « supprimé ».

    Deux étiquettes identiques au même point — deux grandeurs qui se rejoignent — ne sont
    écrites qu'une fois.
    """
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.ticker import FuncFormatter, NullFormatter

    apply_lang_font()
    ft = fig_text
    formate = format_valeur or (lambda v: f"{v:g}".replace(".", ","))
    formate_bulle = format_infobulle or formate
    annotations = annotations or {}

    def mention(cle, date, xy, couleur, suppression=False):
        spec = annotations.get((cle, date))
        if spec is None:
            return
        if isinstance(spec, str):
            spec = {"texte": spec}
        defaut = ((9, 0), "left", "center") if suppression else ((-4, -8), "left", "top")
        ax.annotate(ft(spec["texte"]), xy=xy, xytext=spec.get("xytext", defaut[0]),
                    textcoords="offset points", ha=spec.get("ha", defaut[1]),
                    va=spec.get("va", defaut[2]), fontsize=7.5, color=couleur)

    etats = serie_escalier(series_id, courbes, colonne=colonne, echelle=echelle)
    bout = fin + 1.0  # le 31 décembre de la dernière année tracée
    fig, ax = plt.subplots(figsize=figsize)
    poignees, dates, ecrites = [], set(), set()
    for cle, (libelle, couleur) in courbes.items():
        lignes = etats.get(cle, [])
        for i, (date, v, etat, texte, _lien) in enumerate(lignes):
            x = abscisse_date(date)
            dates.add(date)
            bulle = f"{date} · {libelle} : "
            suite = f" · {texte}" if isinstance(texte, str) and texte else ""
            if v is None:
                # Fin de la grandeur : cercle creux sur le dernier niveau, le trait s'arrête.
                dernier = lignes[i - 1][1]
                p, = ax.plot([x], [dernier], "o", color=couleur, mfc="white", ms=7, mew=1.8,
                             zorder=4)
                infobulle(p, bulle + (supprime or t("esc_supprime")) + suite)
                mention(cle, date, (x, dernier), couleur, suppression=True)
                continue
            x_suivant = abscisse_date(lignes[i + 1][0]) if i + 1 < len(lignes) else bout
            ax.plot([x, x_suivant], [v, v], color=couleur, lw=2.2, solid_capstyle="butt",
                    zorder=2)
            suivant = lignes[i + 1][1] if i + 1 < len(lignes) else None
            if suivant is not None and suivant != v:
                ax.plot([x_suivant, x_suivant], [v, suivant], color=couleur, lw=1.2, zorder=2)
            if etat == "reprise":
                p, = ax.plot([x], [v], "D", color=couleur, mfc="white", ms=5.5, mew=1.5,
                             zorder=4)
            else:
                p, = ax.plot([x], [v], "o", color=couleur, ms=5, zorder=4)
                etiquette = formate(v)
                if (date, v, etiquette) not in ecrites:
                    ecrites.add((date, v, etiquette))
                    ax.annotate(ft(etiquette), xy=(x, v), xytext=(4, 4),
                                textcoords="offset points", ha="left", va="bottom",
                                fontsize=8.5, fontweight="bold", color=couleur, zorder=5)
            mention(cle, date, (x, v), couleur)
            infobulle(p, bulle + formate_bulle(v) + suite)
        if lignes:
            poignees.append(Line2D([], [], color=couleur, lw=2.2, marker="o", ms=5,
                                   label=ft(libelle)))
    # Les graduations sont les dates d'effet elles-mêmes, et la dernière année tracée.
    graduations = sorted(dates)
    ax.set_xticks([abscisse_date(g) for g in graduations] + [fin])
    ax.set_xticklabels([ft((etiquettes_x or {}).get(g, g[:4])) for g in graduations]
                       + [str(fin)])
    for g in graduations:
        ax.axvline(abscisse_date(g), color="#8b949e", lw=0.6, ls=(0, (1, 3)), zorder=1)
    if xlim is None:
        debut = abscisse_date(graduations[0]) if graduations else fin
        xlim = (debut - 0.03 * (bout - debut) - 0.2, bout + 0.6)
    ax.set_xlim(*xlim)
    if log:
        ax.set_yscale("log")
        ax.yaxis.set_minor_formatter(NullFormatter())
    if ylim is not None:
        ax.set_ylim(*ylim)
    elif not log:
        ax.set_ylim(0, None)
    if yticks is not None:
        ax.set_yticks(list(yticks))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _p: f"{y:g}"))
    ax.set_xlabel(ft(xlabel if xlabel is not None else t("esc_x")))
    ax.set_ylabel(ft(ylabel))
    ax.grid(True, axis="y", alpha=0.3)
    _legende_sous(ax, poignees, ncol or max(1, len(poignees)))
    fig.tight_layout()
    return fig


def table_escalier(series_id: str, courbes: dict, *, colonne: str = "parametre",
                   echelle: float = 1.0, libelles: dict | None = None):
    """Une ligne par grandeur et par date d'effet, avec ce que fait le texte.

    Les colonnes « Texte » et « Journal officiel » n'y sont que si la série les porte.
    `libelles` remplace des intitulés communs : `parametre`, `effet`, `valeur`, `etat`,
    `texte`, `jort`, et les quatre états `creation`, `changement`, `reprise`, `suppression`.
    """
    import pandas as pd

    def mot(cle):
        return (libelles or {}).get(cle) or t(f"esc_{cle}")

    etats = serie_escalier(series_id, courbes, colonne=colonne, echelle=echelle)
    avec_textes = "texte" in series(series_id)
    lignes = []
    for cle, serie in etats.items():
        for date, v, etat, texte, lien in serie:
            ligne = {mot("parametre"): courbes[cle][0], mot("effet"): date,
                     mot("valeur"): v, mot("etat"): mot(etat)}
            if avec_textes:
                ligne[mot("texte")], ligne[mot("jort")] = texte, lien
            lignes.append(ligne)
    return pd.DataFrame(lignes)


def constants_escalier(series_id: str, courbes: dict, *, colonne: str = "parametre",
                       base: int | None = None, ipc: tuple[str, str, str] = IPC_ESCALIER):
    """Les montants d'une série longue en dinars constants : (lignes, année de base).

    Lignes : [(clé, année, moyenne annuelle en dinars courants, indice, montant en dinars de
    l'année de base)], de la première année pleine de chaque grandeur à l'année de base —
    par défaut la dernière année de l'indice. Dinars constants : moyenne annuelle × indice de
    l'année de base ÷ indice de l'année ; la moyenne est celle de `moyenne_annuelle_escalier`.
    NE VAUT QUE POUR DES MONTANTS EN DINARS : un taux ne se déflate pas.
    """
    serie_ipc, col_annee, col_indice = ipc
    indice = {int(a): float(i) for a, i in zip(series(serie_ipc)[col_annee],
                                               series(serie_ipc)[col_indice])}
    base = base or max(indice)
    lignes = []
    for cle, serie in serie_escalier(series_id, courbes, colonne=colonne).items():
        for annee in range(int(serie[0][0][:4]), base + 1):
            moyenne = moyenne_annuelle_escalier(serie, annee)
            if moyenne is None or annee not in indice:
                continue
            lignes.append((cle, annee, moyenne, indice[annee],
                           moyenne * indice[base] / indice[annee]))
    return lignes, base


def fig_escalier_constants(series_id: str, courbes: dict, *, colonne: str = "parametre",
                           base: int | None = None, format_valeur=None, ylabel: str = "",
                           log: bool = False, figsize=(9.5, 5.6), ncol: int | None = None,
                           ipc: tuple[str, str, str] = IPC_ESCALIER):
    """Les mêmes grandeurs en dinars de l'année de base : un point par année.

    Entre deux relèvements, la courbe descend au rythme des prix ; un relèvement la remonte
    d'un coup. Les valeurs de la première et de la dernière année sont étiquetées.
    """
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter, NullFormatter

    apply_lang_font()
    ft = fig_text
    formate = format_valeur or (lambda v: f"{v:g}".replace(".", ","))
    lignes, base = constants_escalier(series_id, courbes, colonne=colonne, base=base, ipc=ipc)
    fig, ax = plt.subplots(figsize=figsize)
    ecrites = set()
    for cle, (libelle, couleur) in courbes.items():
        points = [(a, r) for c, a, _m, _i, r in lignes if c == cle]
        if not points:
            continue
        ax.plot([a for a, _ in points], [r for _, r in points], "-o", ms=3, lw=2,
                color=couleur, label=ft(libelle))
        for (a, r), (dx, ha) in ((points[0], (-5, "right")), (points[-1], (5, "left"))):
            if (a, round(r)) in ecrites:  # deux grandeurs qui se rejoignent : une étiquette
                continue
            ecrites.add((a, round(r)))
            ax.annotate(ft(formate(round(r))), xy=(a, r), xytext=(dx, 0),
                        textcoords="offset points", ha=ha, va="center", fontsize=8,
                        fontweight="bold", color=couleur)
    annees = [a for _c, a, *_ in lignes]
    if annees:
        ax.set_xlim(min(annees) - 3.2, max(annees) + 3.2)
    if log:
        ax.set_yscale("log")
        ax.yaxis.set_minor_formatter(NullFormatter())
    else:
        ax.set_ylim(0, None)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _p: f"{y:g}"))
    ax.set_xlabel(ft(t("esc_annee")))
    ax.set_ylabel(ft(ylabel))
    ax.grid(True, alpha=0.3)
    poignees, _ = ax.get_legend_handles_labels()
    _legende_sous(ax, poignees, ncol or max(1, len(poignees)))
    fig.tight_layout()
    return fig


def table_escalier_constants(series_id: str, courbes: dict, *, colonne: str = "parametre",
                             base: int | None = None,
                             ipc: tuple[str, str, str] = IPC_ESCALIER):
    """Une ligne par grandeur et par année : moyenne courante, indice, dinars constants."""
    import pandas as pd

    lignes, base = constants_escalier(series_id, courbes, colonne=colonne, base=base, ipc=ipc)
    return pd.DataFrame([{
        t("esc_parametre"): courbes[cle][0], t("esc_annee"): annee,
        t("esc_moyenne"): round(moyenne, 3), t("esc_ipc"): indice,
        t("esc_reel").format(base=base): round(reel, 1),
    } for cle, annee, moyenne, indice, reel in lignes])


def figure_escalier(series_id: str, courbes: dict, *, slug: str, caption: str, fin: int,
                    note_lecture: str | None = None, constants: bool = False,
                    base: int | None = None, ylabel_constants: str = "",
                    libelles: dict | None = None, generated: str | None = None,
                    nominal: bool = False, **options) -> None:
    """LA DÉCLARATION : trace une série longue en escalier et la rend par `figure_tabs`.

    À appeler comme `figure_tabs`, dans un chunk `#| output: asis` étiqueté `fig-…`. La
    provenance de la série doit être déclarée (`register_provenance`). `options` passe à
    `fig_escalier` (`colonne`, `echelle`, `format_valeur`, `ylabel`, `annotations`, `log`…).

        figtools.figure_escalier(
            "tva-taux", {"normal": ("Taux normal", "#08519c"), …}, slug="fig_tva_taux",
            fin=2026, colonne="taux", echelle=100, ylabel="Taux de la taxe, en %",
            caption="Taux de la taxe sur la valeur ajoutée à leurs dates d'effet")

    `nominal` : `True` pour des montants en dinars courants tracés seuls — la ligne
    « Source » le dit alors ; sans objet pour un taux.

    `constants` : LECTURE EN DINARS CONSTANTS, pour des MONTANTS EN DINARS seulement. La
    figure prend alors deux vues — dinars courants, en escalier ; dinars de l'année de base
    (`base`, par défaut la dernière année de l'indice des prix), un point par année —, les
    données deviennent la série annuelle (`table_escalier_constants`) et l'indice des prix
    s'ajoute aux séries sourcées. `ylabel_constants` peut porter `{base}`. L'indice est celui d'`IPC_ESCALIER` ; ses clés de citation
    doivent figurer dans la bibliographie du livre.
    """
    communs = {c: options[c] for c in ("colonne",) if c in options}
    fig = fig_escalier(series_id, courbes, fin=fin, **options)
    if not constants:
        table = table_escalier(series_id, courbes, echelle=options.get("echelle", 1.0),
                               libelles=libelles, **communs)
        figure_tabs(fig, table, series_id, slug=slug, caption=caption,
                    note_lecture=note_lecture, generated=generated, nominal=nominal)
        return
    _lignes, base = constants_escalier(series_id, courbes, base=base, **communs)
    reel = fig_escalier_constants(
        series_id, courbes, base=base, ylabel=ylabel_constants.format(base=base),
        **{c: options[c] for c in ("colonne", "format_valeur", "log", "figsize", "ncol")
           if c in options})
    figure_tabs([(t("esc_courants"), fig), (t("esc_constants").format(base=base), reel)],
                table_escalier_constants(series_id, courbes, base=base, **communs),
                series_id, IPC_ESCALIER[0], slug=slug, caption=caption,
                note_lecture=note_lecture, generated=generated, nominal=False)


def _svg_avec_infobulles(fig, chemin: Path) -> str:
    """La figure en SVG, chaque élément marqué par `infobulle` muni de son `<title>`."""
    import html
    import re

    fig.savefig(chemin, format="svg", bbox_inches="tight")
    svg = chemin.read_text(encoding="utf-8")
    svg = svg[svg.index("<svg"):]  # ni prologue XML ni DOCTYPE dans une page HTML
    for gid, texte in fig._infobulles.items():
        svg = svg.replace(f'<g id="{gid}">',
                          f'<g id="{gid}" class="infobulle"><title>{html.escape(texte)}</title>', 1)
    # Largeur fluide : la hauteur suit le viewBox.
    svg = re.sub(r'<svg([^>]*?) width="[^"]*" height="[^"]*"',
                 r'<svg\1 style="width:100%;height:auto"', svg, count=1)
    return svg


_STYLE_INFOBULLES = """<style>
.figure-svg g.infobulle { cursor: help; }
.figure-svg g.infobulle:hover path, .figure-svg g.infobulle:hover use { fill-opacity: .12 !important; }
</style>
"""


def noms_des_vues(slug: str, n: int) -> list[str]:
    """Noms de fichier (sans extension) des `n` vues d'une figure.

    La première garde le nom de la figure — `<slug>.png`, celui d'une figure à vue unique —,
    les suivantes prennent un numéro : `<slug>-2.png`, `<slug>-3.png`…
    """
    return [slug] + [f"{slug}-{i}" for i in range(2, n + 1)]


def _image_vue(fig, png: Path, nom: str, alt: str) -> str:
    """Enregistre une vue (PNG, et SVG si elle porte des infobulles) ; rend son Markdown.

    Les infobulles sont lues sur la figure de LA vue (`fig._infobulles`) : chaque SVG ne
    reçoit que les siennes.
    """
    png_path = png / f"{nom}.png"
    fig.savefig(png_path, dpi=150, bbox_inches="tight")
    image = f'![]({png_path}){{fig-alt="{alt}"}}'
    if getattr(fig, "_infobulles", None):
        # HTML : SVG en ligne, survolable ; ailleurs (PDF) : l'image fixe.
        svg = _svg_avec_infobulles(fig, png / f"{nom}.svg")
        image = (f'::: {{.content-visible when-format="html"}}\n\n```{{=html}}\n'
                 f'{_STYLE_INFOBULLES}<div class="figure-svg" role="img" aria-label="{alt}">\n'
                 f'{svg}\n</div>\n```\n\n:::\n\n'
                 f'::: {{.content-hidden when-format="html"}}\n\n{image}\n\n:::')
    return image


def onglet_graphique(images: list[tuple[str | None, str]]) -> str:
    """Contenu de l'image dans l'onglet « Graphique », à partir de `[(titre_vue, markdown)]`.

    Une seule vue : son Markdown tel quel — la sortie d'une figure à vue unique ne change
    pas d'un octet. Plusieurs vues : des sous-onglets (`panel-tabset` imbriqué, titres de
    niveau 3 sous les onglets de niveau 2) en HTML ; hors HTML (PDF), où un onglet ne se
    clique pas, la PREMIÈRE vue seule, sans titre de vue. La légende, la ligne « Source »
    et la note de lecture restent communes, hors des sous-onglets.

    Pure : ni matplotlib ni pandas, pour se tester sans dépendance.
    """
    if len(images) == 1:
        return images[0][1]
    onglets = "\n\n".join(f"### {titre}\n\n{image}" for titre, image in images)
    return (f'::: {{.content-visible when-format="html"}}\n\n'
            f'::: {{.panel-tabset}}\n\n{onglets}\n\n:::\n\n:::\n\n'
            f'::: {{.content-hidden when-format="html"}}\n\n{images[0][1]}\n\n:::')


def figure_tabs(fig, df: pd.DataFrame, *series_ids: str, slug: str,
                caption: str = "", note_lecture: str | None = None,
                fig_id: str | None = None, figdata_dir: str = "figdata",
                png_dir: str = "_fig", scroll_y: str = "420px",
                generated: str | None = None, nominal: bool = True) -> None:
    """Composant générique : figure en **onglets** Graphique / Données / Sources.

    À appeler dans un chunk Quarto `#| output: asis`, **étiqueté** `#| label: fig-…`,
    dont c'est la dernière instruction. Produit :
      - onglet « Graphique » : l'image, la ligne « Source » courte, et — si fournie —
        une **note de lecture** ;
      - onglet « Données » : table **itables** scrollable + export CSV/Excel
        + téléchargement du **figdata sourcé** ;
      - onglet « Sources » : provenance détaillée (citation, **lien web** vers la
        source d'origine, fiche, fichiers bruts, périmètre, réserves) ;
      - onglet « Base législative », si une série tracée vient du droit codé : un lien
        par grandeur, lu dans `_seriescache/<série>.liens.<langue>.yml` (voir
        `base_legislative`).

    UNE SEULE FIGURE NUMÉROTÉE, CELLE DU CHUNK. L'étiquette du chunk fait de toute sa
    sortie — les onglets — une figure Quarto, et c'est elle que vise `@fig-…`. Sa légende
    est le DERNIER PARAGRAPHE de la sortie : Quarto la prend pour titre (« Figure N — … »).
    L'option `#| fig-cap:` n'est, elle, pas lue sur une sortie `asis` : la légende affichée
    est `caption`. L'image ne porte donc ni identifiant ni légende — elle en portait,
    et Quarto en faisait une sous-figure « (a) … » dans une figure à la légende vide.

    `fig`          : figure matplotlib (déjà rendue) — ou une liste de VUES
                     `[(titre_vue, fig), …]`, montrées en sous-onglets de l'onglet
                     « Graphique » (même grandeur en millions de dinars, en % du PIB…).
                     Le titre de vue est fourni par le module, dans la langue du livre.
                     Toujours une seule figure numérotée et une seule légende ; chaque vue
                     a son image (`<slug>.png`, `<slug>-2.png`… — `noms_des_vues`) et ses
                     propres infobulles. Le PDF ne montre que la première vue
                     (`onglet_graphique`).
    `df`           : données de la figure (deviennent le figdata téléchargeable).
    `series_ids`   : id(s) de série `tunisia_data` (provenance/citation).
    `slug`         : identifiant de fichier (png + csv).
    `caption`      : **titre** de la figure (légende numérotée par Quarto).
    `note_lecture` : texte « Comment lire cette figure » (callout). Optionnel.
    `nominal`      : `False` pour une figure en volume — la ligne « Source » ne dit alors pas
                     « valeurs courantes (nominal) ».
    `fig_id`       : pour un chunk NON étiqueté seulement — la sortie est alors enveloppée
                     dans sa propre figure `::: {#fig_id}`. Ne jamais le combiner avec
                     `#| label:` : on retomberait sur la figure dans la figure.
    """
    from itables import to_html_datatable

    png = Path(png_dir)
    png.mkdir(parents=True, exist_ok=True)
    vues = list(fig) if isinstance(fig, (list, tuple)) else [(None, fig)]

    csv_path = Path(figdata_dir) / f"{slug}.csv"
    write_figdata(df, csv_path, *series_ids, note=caption, generated=generated)

    table = to_html_datatable(
        df, buttons=["csvHtml5", "excelHtml5"], scrollY=scroll_y, scrollX=True,
        scrollCollapse=True, paging=False, classes="display compact nowrap",
        connected=True)  # charge DataTables depuis le CDN (figure autoportante)

    src = source_line(*series_ids, nominal=nominal)
    dl = download_button(str(csv_path))
    details = source_details(*series_ids)
    lecture = ""
    if note_lecture:
        lecture = (f'\n::: {{.callout-note appearance="simple" '
                   f'icon=true title="{t("how_to_read")}"}}\n'
                   f'{note_lecture}\n:::\n')
    base = base_legislative(*series_ids)
    onglet_base = f"## {t('tab_base')}\n\n{base}\n\n" if base else ""
    alt = caption.replace('"', "&quot;")
    image = onglet_graphique([
        (titre, _image_vue(f, png, nom,
                           alt if titre is None else f"{alt} — {titre}".replace('"', "&quot;")))
        for (titre, f), nom in zip(vues, noms_des_vues(slug, len(vues)))])
    sortie = f"""::: {{.panel-tabset}}

## {t('tab_graph')}

{image}

::: {{.figure-source}}
{src}
:::
{lecture}
## {t('tab_data')}

{dl}

{table}

## {t('tab_src')}

::: {{.figure-sources-detail}}
{details}
:::

{onglet_base}:::

{caption}
"""
    if fig_id:
        sortie = f"::: {{#{fig_id}}}\n\n{sortie}\n:::\n"
    print(sortie)

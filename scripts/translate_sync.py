import difflib
import time
import os
import re
import sys
import subprocess
# `google-genai` n'est PAS importé ici, mais dans `main()`. Ce module porte des
# fonctions purement textuelles — `restore_locators`, `restore_urls` — qui
# réécrivent du contenu publié et doivent donc être testables SANS le client du
# modèle. Un import de tête les rendait inatteignables hors environnement CI, où
# le paquet n'est installé qu'à la volée (`uv run --with google-genai`).

CITATION_RE = re.compile(r"\[@([A-Za-z][A-Za-z0-9_-]*),\s*([^\]]+)\]")

# En deçà de cette fraction du plus petit des deux fichiers — l'ancienne traduction et la
# source —, la sortie est tenue pour tronquée et le fichier n'est pas écrit. Le seuil est
# volontairement bas : il ne s'agit pas de juger la concision d'une traduction, mais
# d'attraper une amputation.
SEUIL_TRONCATURE = 0.6
ARABIC_RE = re.compile(r"[\u0600-\u06FF]")

# Codes et mentions que l'API renvoie sur des pannes PASSAGÈRES, où réessayer a un sens.
ERREURS_PASSAGERES = (
    "503", "UNAVAILABLE", "429", "RESOURCE_EXHAUSTED", "overloaded",
    "500", "INTERNAL", "502", "504", "DEADLINE_EXCEEDED",
)

# Mentions d'une limite DURE, qu'aucune attente ne lèvera. Le mot « quota » seul en est
# volontairement ABSENT : un quota par minute est bel et bien passager, et l'inclure
# ferait abandonner des appels qu'il fallait réessayer — le remède serait pire que le mal.
ERREURS_DURES = (
    "spending cap", "spend cap", "billing", "exceeded its monthly",
)


class LimiteDure(RuntimeError):
    """Refus que l'attente ne lèvera pas : plafond de dépense, facturation.

    Distinguée des autres échecs pour deux raisons. Elle arrête la passe entière,
    puisqu'elle vaut pour tous les fichiers ; et, lorsqu'elle n'a laissé passer
    aucune traduction, elle vaut attente et non échec.
    """


def est_transitoire(msg: str) -> bool:
    """Dit si réessayer cet appel a une chance d'aboutir.

    POURQUOI CETTE FONCTION EXISTE. Gemini renvoie `429 RESOURCE_EXHAUSTED` pour DEUX
    situations opposées, sans les distinguer : un dépassement de débit, qui se résorbe en
    quelques secondes, et un PLAFOND DE DÉPENSE mensuel, qu'aucune attente ne lèvera.

    Le 18 septembre 2026, le plafond a été pris pour un débit. Le script a réessayé
    quatre fois par fichier sur six fichiers — vingt-quatre appels voués à l'échec — et,
    plus grave, il a noyé la vraie cause sous quatre lignes « erreur transitoire » par
    fichier. Le journal annonçait une attente ; il fallait lire la dernière ligne pour
    découvrir un plafond atteint. Le diagnostic en a été retardé d'autant.

    La limite dure l'emporte donc sur le code de statut : un message qui parle de
    plafond ou de facturation n'est pas transitoire, quel que soit le 429 qui l'escorte.
    """
    bas = msg.lower()
    if any(s in bas for s in ERREURS_DURES):
        return False
    return any(s in msg for s in ERREURS_PASSAGERES)


def fichier_a_traduire(chemin):
    """Dit si un fichier relève de la traduction automatique.

    `_quarto.yml` en est EXCLU. Le fichier arabe porte des éléments qui n'ont aucun
    original français — `dir: rtl`, un bloc `language:` aux libellés d'interface
    arabes, et les titres des parties du livre — que le traducteur ne peut pas
    déduire du fichier français, et qu'il écrase donc à chaque passage. Faire
    transiter par un traducteur un fichier dont une part n'a pas de source est
    structurellement fautif : l'arabe se tient à la main sous `precis/ar/`.

    Le garde est ici ET dans le filtre du workflow. Ce n'est pas un doublon : le
    workflow évite d'ouvrir une PR de traduction vide, cette fonction protège la
    re-synchro manuelle, où les fichiers sont fournis à la main et échappent au
    filtre.

    Les `_glossaire.qmd` restent exclus au niveau du workflow seulement : ils sont
    engendrés depuis `precis/glossaire.yml`, et leur cas ne relève pas de la même
    règle.
    """
    if chemin == "CHANGELOG.md":
        return True
    if chemin.endswith("_quarto.yml"):
        return False
    return chemin.endswith(".qmd")


def texte_a_ecrire(texte):
    """Garantit exactement un saut de ligne final, comme en portent les sources.

    La passe écrivait la réponse du modèle telle quelle. Or celle-ci ne se termine pas
    par un saut de ligne, alors que le fichier français en porte un : toute modification
    du chapitre français régénérait donc une PR de traduction dont le diff se réduisait à
    « +1/-1 » sur la dernière ligne, avec la marque « No newline at end of file ».

    Le 16/09/2026, #246 : la dernière ligne faisait 217 caractères des deux côtés,
    contenu identique octet pour octet. La PR ne retirait qu'un caractère, mais elle
    ressemblait à une vraie mise à jour et invitait à être fusionnée.

    Rend le TEXTE plutôt que d'écrire : une fonction qui ne fait qu'un calcul se teste
    sans fichier ni réseau.
    """
    if not texte:
        return texte
    return texte.rstrip("\n") + "\n"


def motif_de_troncature(lignes_avant, lignes_apres, lignes_source):
    """Message expliquant en quoi la traduction est tronquée, ou None si elle ne l'est pas.

    Le modèle renvoie parfois un fichier amputé au lieu de la mise à jour demandée : le
    9 septembre 2026, un chapitre arabe de 636 lignes est revenu à 68 — 89 % de perte —,
    et la PR ouverte automatiquement ressemblait à n'importe quelle autre. Rien dans le
    rendu ne l'aurait signalé : un chapitre amputé reste un chapitre bien formé.

    Une traduction n'est jamais beaucoup plus courte que ce qu'elle met à jour, SAUF si la
    source a elle-même raccourci. D'où le `min` : on se règle sur le plus petit des deux
    repères, faute de quoi une coupe légitime du français déclencherait l'alarme.

    Le `max(1, …)` rend toute sortie vide fautive, y compris quand les repères sont nuls.

    Rend le MESSAGE plutôt que de lever : la décision d'interrompre appartient à l'appelant,
    et une fonction qui ne fait qu'un calcul se teste sans fichier ni réseau.
    """
    seuil = max(1, int(min(lignes_avant, lignes_source) * SEUIL_TRONCATURE))
    if lignes_apres >= seuil:
        return None
    return (
        f"traduction tronquée : {lignes_apres} lignes contre "
        f"{lignes_avant} auparavant et {lignes_source} à la source. "
        "Relancer, au besoin en retraduction complète."
    )


def restore_locators(source_text, translated_text):
    """Rétablit les locateurs de citation dans leur forme d'origine.

    Le contenu qui suit la virgule dans `[@ref, art. 13]` est de la SYNTAXE de
    citation, pas de la prose : il doit rester tel quel. Le modèle le traduit
    malgré la consigne — « art. 5 à 7 » devient « art. 5 إلى 7 », « art. 31 et 37 »
    devient « art. 31 و 37 », « art. 37 (nouveau) » devient « art. 37 (جديد) » —,
    et c'est une transformation assez mécanique pour être défaite ici plutôt que
    négociée à chaque passe. Le locateur est alors recopié VERBATIM depuis la
    citation correspondante de la source.

    APPARIEMENT PAR CLÉ ET PAR RANG. La n-ième citation `[@k, …]` de la traduction
    correspond à la n-ième `[@k, …]` de la source. Jusqu'en octobre 2026, la
    fonction exigeait que la SUITE ENTIÈRE des clés soit identique des deux côtés :
    une seule clé abîmée ailleurs dans le fichier (`@looi81-6`, PR #343) suffisait à
    la faire renoncer à tous les locateurs, et « art. 48 إلى 50 » passait. D'où
    aussi l'ordre dans `main()` : `restore_citation_keys` passe AVANT elle.

    Quand une clé n'apparaît pas autant de fois des deux côtés, l'appariement par
    rang n'est plus sûr : on aligne alors la suite des clés (difflib) et l'on ne
    restaure que dans les plages identiques d'au moins deux citations. Ce qui reste hors de ces plages est
    laissé tel quel, et le contrôle de parité le signalera.

    Périmètre : seuls les locateurs portant de l'écriture arabe sont réécrits. Un
    locateur altéré sans être traduit ne se distingue pas d'une correction
    légitime. Les citations hors crochets (« Sources : @loi59-18, art. 20 ») ne sont
    pas des locateurs Pandoc et ne sont pas touchées.
    """
    src = CITATION_RE.findall(source_text)
    dst = CITATION_RE.findall(translated_text)
    if not src or not dst:
        return translated_text

    cles_src = [k for k, _ in src]
    cles_dst = [k for k, _ in dst]
    compte_src, compte_dst = _compte(cles_src), _compte(cles_dst)

    # Indice dans `src` de la citation correspondant à chaque citation de `dst`.
    vis_a_vis = {}
    rang, positions_src = {}, {}
    for i, k in enumerate(cles_src):
        positions_src.setdefault(k, []).append(i)
    alignees = None
    for j, k in enumerate(cles_dst):
        if compte_src.get(k, 0) == compte_dst[k]:
            r = rang.get(k, 0)
            rang[k] = r + 1
            vis_a_vis[j] = positions_src[k][r]
            continue
        if alignees is None:
            alignees = {}
            sm = difflib.SequenceMatcher(None, cles_src, cles_dst, autojunk=False)
            for tag, i1, _i2, j1, j2 in sm.get_opcodes():
                # Une plage d'une seule citation ne dit pas laquelle des
                # occurrences de la source lui répond : il faut un voisin aligné.
                if tag == "equal" and j2 - j1 >= 2:
                    for d in range(j2 - j1):
                        alignees[j1 + d] = i1 + d
        if j in alignees:
            vis_a_vis[j] = alignees[j]

    restaures, abstentions = [], []
    compteur = iter(range(len(dst)))

    def swap(match):
        j = next(compteur)
        cle, locateur = match.group(1), match.group(2)
        if not ARABIC_RE.search(locateur):
            return match.group(0)
        if j not in vis_a_vis:
            abstentions.append(f"@{cle}, {locateur.strip()}")
            return match.group(0)
        locateur_source = src[vis_a_vis[j]][1]
        restaures.append(f"« {locateur.strip()} » → « {locateur_source.strip()} »")
        return f"[@{cle}, {locateur_source}]"

    resultat = CITATION_RE.sub(swap, translated_text)
    for r in restaures:
        print(f"  locateur restauré : {r}.")
    for a in abstentions:
        print(f"  locateur traduit laissé tel quel (pas de citation correspondante "
              f"sûre dans la source) : « {a} » — le contrôle de parité tranchera.")
    return resultat


# ---------------------------------------------------------------------------
# JETONS VERBATIM ABÎMÉS : clés de citation, renvois, ancres, liens de glossaire.
#
# Les extracteurs de `check_translation_parity.py` disent ce qui DOIT être identique
# dans les deux langues. Les fonctions qui suivent défont, avant ce contrôle, les
# altérations que l'on corrigeait à la main sur chaque PR auto-translate (#331, #333,
# #343) : `@looi88-71` pour `@loi88-71`, `@arrete-11-18-…` pour
# `@arrete-1978-11-18-…`, `@tbl-somme-three-texts` pour `@tbl-somme-trois-textes`,
# liens de glossaire ajoutés là où le français n'en a pas.
#
# Comme le contrôle de parité, elles ignorent les commentaires HTML (les TODO restent
# en français) et les blocs de code délimités.
BRUIT_RE = re.compile(r"<!--.*?-->|```.*?```", re.S)


def _zones_de_bruit(texte):
    return [m.span() for m in BRUIT_RE.finditer(texte)]


def _hors_bruit(motif, texte):
    """Les correspondances de `motif` qui ne tombent ni en commentaire ni en code."""
    zones = _zones_de_bruit(texte)
    return [m for m in motif.finditer(texte)
            if not any(a <= m.start() < b for a, b in zones)]


# (nature, motif) — le groupe 1 est le jeton. Mêmes jetons que le contrôle de parité ;
# les ancres de définition y gagnent les titres à attributs (`{#sec-x .unnumbered}`).
JETONS_VERBATIM = (
    ("clé de citation ou renvoi", re.compile(r"@([A-Za-z][A-Za-z0-9_-]*)")),
    ("ancre", re.compile(r"\{#([A-Za-z][A-Za-z0-9_-]*)(?=[\s}])")),
    ("cible de lien interne", re.compile(r"\]\(#([A-Za-z][A-Za-z0-9_-]*)\)")),
)
PREFIXE_RENVOI_RE = re.compile(r"^(sec|tbl|fig|eq|lst|g)-")
SEUIL_PROXIMITE = 0.8


def _proche(a, b):
    """Deux jetons sont proches s'ils ont le même préfixe de renvoi (`sec-`, `tbl-`…,
    ou aucun) et une similarité difflib d'au moins `SEUIL_PROXIMITE`. Les cas réels
    vont de 0,84 (`tbl-somme-three-texts`) à 0,98 (`arrete-1918-11-18-…`)."""
    pa, pb = PREFIXE_RENVOI_RE.match(a), PREFIXE_RENVOI_RE.match(b)
    if (pa and pa.group(1)) != (pb and pb.group(1)):
        return False
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio() >= SEUIL_PROXIMITE


def _restaurer_jetons(source_text, translated_text, nature, motif):
    src = [m.group(1) for m in _hors_bruit(motif, source_text)]
    occ = _hors_bruit(motif, translated_text)
    dst = [m.group(1) for m in occ]
    cs, cd = _compte(src), _compte(dst)
    exces = {t: n - cs.get(t, 0) for t, n in cd.items() if n > cs.get(t, 0)}
    manque = {s: n - cd.get(s, 0) for s, n in cs.items() if n > cd.get(s, 0)}
    if not exces:
        return translated_text  # rien en trop : muette
    if not manque:
        for t in sorted(exces):
            print(f"  {nature} : « {t} » en trop dans la traduction ({cd[t]}× pour "
                  f"{cs.get(t, 0)}× à la source), rien ne manque à la source — aucune "
                  f"restauration (le contrôle de parité tranchera).")
        return translated_text

    vers_source = {t: [s for s in manque if _proche(t, s)] for t in exces}
    vers_trad = {s: [t for t in exces if _proche(t, s)] for s in manque}

    a_remplacer = {}  # indice de l'occurrence dans `occ` -> jeton de la source
    alignement = None
    for t in sorted(exces):
        candidats = vers_source[t]
        if not candidats:
            print(f"  {nature} : « {t} » en trop dans la traduction, aucun jeton manquant "
                  f"de la source n'en est proche — aucune restauration "
                  f"(le contrôle de parité tranchera).")
            continue
        if len(candidats) > 1 or len(vers_trad[candidats[0]]) > 1:
            proches = sorted(set(candidats) | {x for s in candidats for x in vers_trad[s]})
            print(f"  {nature} : « {t} » absent ou en trop, appariement ambigu "
                  f"({', '.join(proches)}) — aucune restauration "
                  f"(le contrôle de parité tranchera).")
            continue
        s = candidats[0]
        if t not in cs and exces[t] <= manque[s]:
            # Jeton inconnu de la source : toutes ses occurrences sont fautives.
            for j, x in enumerate(dst):
                if x == t:
                    a_remplacer[j] = s
            continue
        # Le jeton existe aussi dans la source (ou il y a plus d'occurrences fautives
        # que de manquantes) : seule une position peut dire laquelle est fautive.
        if alignement is None:
            alignement = difflib.SequenceMatcher(None, src, dst, autojunk=False).get_opcodes()
        positions = [j1 + d for tag, i1, i2, j1, j2 in alignement
                     if tag == "replace" and i2 - i1 == j2 - j1
                     for d in range(j2 - j1)
                     if dst[j1 + d] == t and src[i1 + d] == s]
        if not positions or len(positions) > min(exces[t], manque[s]):
            print(f"  {nature} : « {t} » ({cd[t]}× traduit, {cs.get(t, 0)}× source) "
                  f"pour « {s} » — position non établie, aucune restauration "
                  f"(le contrôle de parité tranchera).")
            continue
        for j in positions:
            a_remplacer[j] = s

    if not a_remplacer:
        return translated_text
    morceaux, fin = [], 0
    for j, m in enumerate(occ):
        if j in a_remplacer:
            morceaux.append(translated_text[fin:m.start(1)])
            morceaux.append(a_remplacer[j])
            fin = m.end(1)
    morceaux.append(translated_text[fin:])
    for t, s in sorted({(dst[j], s) for j, s in a_remplacer.items()}):
        n = sum(1 for j, x in a_remplacer.items() if dst[j] == t and x == s)
        print(f"  {nature} restaurée : « {t} » → « {s} » ({n}×).")
    return "".join(morceaux)


def restore_citation_keys(source_text, translated_text):
    """Rétablit les clés de citation, renvois (`@sec-…`, `@tbl-…`, `@fig-…`), ancres
    de définition (`{#…}`) et cibles de liens internes (`](#…)`) abîmés par le modèle.

    Le modèle traduit ou déforme ces jetons comme de la prose : `@looi81-6` pour
    `@loi81-6`, `@arrete-11-18-retraite-complementaire` pour
    `@arrete-1978-11-18-retraite-complementaire`, `@tbl-somme-three-texts` pour
    `@tbl-somme-trois-textes` — chacun corrigé à la main sur une PR auto-translate.

    MÉTHODE. Pour chaque nature de jeton, on compare les multiensembles des deux
    côtés. Un jeton en trop dans la traduction est remplacé par un jeton manquant de
    la source si, et seulement si, l'appariement est UNIQUE dans les deux sens (le
    jeton en trop n'a qu'un manquant proche, et ce manquant n'a que lui) — voir
    `_proche`. Si le jeton fautif est inconnu de la source, toutes ses occurrences
    sont remplacées ; s'il y existe aussi, seules les occurrences que l'alignement des
    deux suites désigne à la place du manquant le sont.

    Chaque restauration et chaque abstention est journalisée. En cas de doute, rien
    n'est touché : mieux vaut une divergence visible du contrôle de parité qu'une clé
    attachée à la mauvaise loi.

    Elle passe AVANT `restore_locators`, qui apparie les citations par clé.
    """
    for nature, motif in JETONS_VERBATIM:
        translated_text = _restaurer_jetons(source_text, translated_text, nature, motif)
    return translated_text


LIEN_GLOSSAIRE_RE = re.compile(r"\[([^\[\]\n]+)\]\(#(g-[A-Za-z0-9_-]+)\)")
MARQUE_DE_LIGNE_RE = re.compile(r"^\s*([-*+]|\d+[.)]|#{1,6}|:|\|)?")
JETON_DE_LIGNE_RE = re.compile(r"@[A-Za-z][A-Za-z0-9_-]*|\{#[A-Za-z][A-Za-z0-9_-]*"
                               r"|https?://[^\s)\]<>\"']+|\d+")


def _signature(ligne):
    """Ce qui, dans une ligne, ne se traduit pas : sa marque de structure (puce,
    titre, tableau), ses clés, ancres, URL et nombres. Sert à aligner les lignes des
    deux langues, qui n'ont pas toujours le même nombre de lignes."""
    if not ligne.strip():
        return ("",)
    marque = MARQUE_DE_LIGNE_RE.match(ligne).group(1) or ""
    return (marque, tuple(sorted(JETON_DE_LIGNE_RE.findall(ligne))))


def _aligner_lignes(lignes_src, lignes_trad):
    """{indice de ligne traduite: indice de ligne source}, plages identiques seules."""
    sm = difflib.SequenceMatcher(None, [_signature(x) for x in lignes_src],
                                 [_signature(x) for x in lignes_trad], autojunk=False)
    vis_a_vis = {}
    for tag, i1, _i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for d in range(j2 - j1):
                vis_a_vis[j1 + d] = i1 + d
    return vis_a_vis


def remove_extra_glossary_links(source_text, translated_text):
    """Retire les liens de glossaire `[…](#g-…)` que le modèle a AJOUTÉS.

    Le modèle pose des liens de glossaire là où le français n'en a pas — sur la PR
    #333, trois entrées d'une liste en gras sont devenues des liens, dont un vers une
    ancre qui n'existe pas (`#g-travaux-penibles-et-insalubres`). Un lien en trop n'est
    pas anodin : il rompt l'égalité des comptes, et `restore_anchors` comme
    `restore_relative_links` s'abstiennent alors sur tout le fichier.

    Seules les cibles `#g-…` sont concernées. Pour chaque cible plus fréquente dans la
    traduction que dans la source :
      - inconnue de la source, tous ses liens sont retirés ;
      - connue, on retire ceux qui n'ont pas d'équivalent positionnel — ligne sans
        vis-à-vis dans la source, ou vis-à-vis sans lien vers cette cible. Les lignes
        sont alignées sur ce qui ne se traduit pas (`_signature`). Si le nombre de
        liens ainsi désignés n'est pas exactement l'excédent, on s'abstient.
    Le texte du lien est gardé ; il est mis en gras si la ligne source correspondante
    porte plus de passages en gras que la ligne traduite. Chaque retrait et chaque
    abstention est journalisé.

    Elle passe APRÈS `restore_citation_keys`, qui aura d'abord rétabli une cible
    simplement fléchie (`#g-entrepositaires` → `#g-entrepositaire`) au lieu de la
    tenir pour un lien en trop.
    """
    src = [m.group(2) for m in _hors_bruit(LIEN_GLOSSAIRE_RE, source_text)]
    occ = _hors_bruit(LIEN_GLOSSAIRE_RE, translated_text)
    cs, cd = _compte(src), _compte(m.group(2) for m in occ)
    exces = {t: n - cs.get(t, 0) for t, n in cd.items() if n > cs.get(t, 0)}
    if not exces:
        return translated_text

    lignes_src = source_text.split("\n")
    lignes_trad = translated_text.split("\n")
    vis_a_vis = _aligner_lignes(lignes_src, lignes_trad)

    def ligne_de(m):
        return translated_text.count("\n", 0, m.start())

    a_retirer = []
    for t in sorted(exces):
        liens = [m for m in occ if m.group(2) == t]
        if t not in cs:
            a_retirer.extend(liens)
            continue
        sans_equivalent = [
            m for m in liens
            if ligne_de(m) not in vis_a_vis
            or f"](#{t})" not in lignes_src[vis_a_vis[ligne_de(m)]]
        ]
        if len(sans_equivalent) != exces[t]:
            print(f"  glossaire : #{t} — {cd[t]} lien(s) traduit(s) pour {cs[t]} à la "
                  f"source, liens en trop non identifiables — aucun retrait "
                  f"(le contrôle de parité tranchera).")
            continue
        a_retirer.extend(sans_equivalent)

    if not a_retirer:
        return translated_text

    gras_ajoute = {}
    morceaux, fin = [], 0
    for m in sorted(a_retirer, key=lambda m: m.start()):
        i = ligne_de(m)
        texte = m.group(1)
        if i in vis_a_vis:
            manque = (lignes_src[vis_a_vis[i]].count("**") // 2
                      - lignes_trad[i].count("**") // 2 - gras_ajoute.get(i, 0))
            if manque > 0 and not texte.startswith("**"):
                texte = f"**{texte}**"
                gras_ajoute[i] = gras_ajoute.get(i, 0) + 1
        morceaux.append(translated_text[fin:m.start()])
        morceaux.append(texte)
        fin = m.end()
        print(f"  glossaire : lien ajouté retiré, l. {i + 1} — #{m.group(2)}"
              f"{' (rendu en gras, comme la source)' if texte.startswith('**') else ''}.")
    morceaux.append(translated_text[fin:])
    return "".join(morceaux)


URL_RE = re.compile(r"https?://[^\s)\]<>\"']+")


def restore_urls(source_text, translated_text):
    """Rétablit les URL dans leur forme d'origine.

    Une URL n'est pas de la prose : elle doit traverser la traduction intacte. Le
    modèle l'abîme pourtant régulièrement, et toujours de façon plausible — le
    14 septembre 2026, cinq passes sur le seul CHANGELOG ont produit
    « github.enjello », « github.Bcom », un domaine remplacé par la date du jour,
    le segment « benjello/ » disparu, et une passe où ~150 URL sur 195 étaient
    réécrites d'un coup. Chacune a dû être réparée à la main.

    Comme pour `restore_locators`, la restauration est positionnelle et PRUDENTE :
    on ne recopie que si les deux textes portent le même NOMBRE d'URL. Sinon la
    correspondance un-à-un n'est pas établie, on ne touche à rien, et le contrôle
    de parité signalera l'écart — mieux vaut une divergence visible qu'une URL
    restaurée au mauvais endroit.

    LIMITE CONNUE, vérifiée par un test : le contrôle porte sur le nombre, pas sur
    l'identité. Si la traduction REORDONNAIT les URL sans en changer le nombre,
    cette fonction leur réimposerait silencieusement l'ordre de la source. C'est
    accepté ici parce que l'ordre des URL suit celui de la prose, que le modèle
    met à jour sans réorganiser — mais c'est le point à regarder en premier si une
    URL se retrouve un jour attachée au mauvais texte.

    ELLE SE JOURNALISE, et c'est nécessaire : muette quand il n'y a rien à faire,
    elle annonce ses restaurations ET ses abstentions. Sans cela son effet est
    inattribuable — le 14/09/2026, la sixième passe du CHANGELOG est revenue
    intacte après cinq corrompues, et rien dans le journal ne permettait de dire
    si cette fonction avait restauré des URL ou si le modèle n'avait simplement
    rien abîmé cette fois-là.
    """
    src = URL_RE.findall(source_text)
    dst = URL_RE.findall(translated_text)

    # ABSTENTION — le cas le plus important à dire. La fonction laisse alors
    # passer une corruption éventuelle, et c'est le contrôle de parité qui devra
    # trancher : un silence ici serait trompeur.
    if len(src) != len(dst):
        print(f"  URL : {len(src)} à la source, {len(dst)} dans la traduction — "
              f"correspondance non établie, aucune restauration "
              f"(le contrôle de parité tranchera).")
        return translated_text

    if src == dst:
        return translated_text  # rien à faire : muette

    abimees = sum(1 for a, b in zip(src, dst) if a != b)
    urls = iter(src)
    restaure = URL_RE.sub(lambda _m: next(urls), translated_text)
    print(f"  URL restaurées depuis la source : {abimees} sur {len(src)}.")
    return restaure


ANCHOR_RE = re.compile(r"(\]\(#|\{#)([A-Za-z][A-Za-z0-9_-]*)")


def restore_anchors(source_text, translated_text):
    """Rétablit les ancres et cibles de liens dans leur forme d'origine.

    Une ancre n'est pas de la prose : `](#g-entrepositaire)` et `{#tbl-dc-petroliers}`
    doivent être identiques dans les deux langues par construction, puisque la cible
    est définie une seule fois. Le modèle les FLÉCHIT pourtant : le 16 septembre 2026,
    la passe du chapitre des droits de consommation a mis `#g-entrepositaire` au
    pluriel — `#g-entrepositaires`, qui n'est ancré nulle part. Le renvoi arabe ne
    pointait plus sur rien, le contrôle de parité a bloqué la PR #255, et le correctif
    manuel était éphémère : la régénération suivante pouvait refléchir la même ancre.

    ON RESTAURE LE NOM, ON GARDE LE PRÉFIXE DE LA CIBLE. `restore_urls` réémet l'URL
    entière depuis la source ; ici ce serait dangereux, car le préfixe distingue un
    LIEN (`](#…)`) d'une DÉFINITION (`{#…}`). Réimposer celui de la source
    convertirait l'un en l'autre et casserait la syntaxe. Le nom seul suffit à défaire
    le fléchissement, et ne peut pas produire de Markdown invalide.

    DEUX ABSTENTIONS, et ce sont les cas qui comptent :
      - les comptes diffèrent : la correspondance un-à-un n'est pas établie ;
      - les préfixes diffèrent à position égale : la structure a changé, et une
        restauration positionnelle attacherait un nom à la mauvaise forme.
    Dans les deux cas on ne touche à rien et le contrôle de parité tranchera — mieux
    vaut une divergence visible qu'une ancre restaurée au mauvais endroit.

    ELLE SE JOURNALISE, comme `restore_urls` : muette quand il n'y a rien à faire,
    elle annonce ses restaurations ET ses abstentions. Sans cela son effet serait
    inattribuable, et l'on ne saurait pas dire si une passe est revenue saine parce
    que cette fonction a réparé ou parce que le modèle n'avait rien abîmé.
    """
    src = ANCHOR_RE.findall(source_text)
    dst = ANCHOR_RE.findall(translated_text)

    if len(src) != len(dst):
        print(f"  ancres : {len(src)} à la source, {len(dst)} dans la traduction — "
              f"correspondance non établie, aucune restauration "
              f"(le contrôle de parité tranchera).")
        return translated_text

    if [p for p, _ in src] != [p for p, _ in dst]:
        print(f"  ancres : {len(src)} des deux côtés, mais les formes (lien / "
              f"définition) ne correspondent pas — aucune restauration "
              f"(le contrôle de parité tranchera).")
        return translated_text

    if src == dst:
        return translated_text  # rien à faire : muette

    abimees = sum(1 for (_, a), (_, b) in zip(src, dst) if a != b)
    noms = iter(nom for _, nom in src)

    def swap(match):
        return f"{match.group(1)}{next(noms)}"

    restaure = ANCHOR_RE.sub(swap, translated_text)
    print(f"  ancres restaurées depuis la source : {abimees} sur {len(src)}.")
    return restaure


# Cible relative d'un lien ou d'une image : ni `#…` (affaire de `restore_anchors`), ni
# schéma (`https:`, `mailto:`, affaire de `restore_urls`).
LIEN_RELATIF_RE = re.compile(r"(\]\()((?!#)(?![A-Za-z][A-Za-z0-9+.-]*:)[^()\s]+)(\))")


def restore_relative_links(source_text, translated_text):
    """Rétablit les cibles relatives des liens — `](../livre/page.html#ancre)`,
    `](_chapitre.qmd)`, `![](figures/x.png)` — dans leur forme d'origine.

    Une cible relative n'est pas de la prose, et le modèle l'abîme comme une URL : un
    segment de chemin déformé (`../cotisations_socales/` pour `../cotisations_sociales/`)
    donne un lien mort d'un livre à l'autre, que rien ne signale au rendu. La cible est
    rétablie ENTIÈRE, fragment compris : `restore_anchors` ne voit que les `](#…)`, pas
    l'ancre de `../x.html#sec-…`.

    Même prudence que `restore_urls` : positionnelle (n-ième cible relative de la
    traduction ↔ n-ième de la source), et seulement si les deux textes en portent le même
    nombre. Un lien de glossaire ajouté ou retiré par le modèle suffit à rompre l'égalité :
    la fonction s'abstient alors, et le dit. Chaque correction est journalisée.
    """
    src = [m.group(2) for m in LIEN_RELATIF_RE.finditer(source_text)]
    dst = [m.group(2) for m in LIEN_RELATIF_RE.finditer(translated_text)]
    if len(src) != len(dst):
        print(f"  liens relatifs : {len(src)} à la source, {len(dst)} dans la traduction — "
              f"correspondance non établie, aucune restauration "
              f"(le contrôle de parité tranchera).")
        return translated_text
    if src == dst:
        return translated_text
    cibles = iter(src)

    def swap(match):
        cible = next(cibles)
        if cible != match.group(2):
            print(f"  lien relatif restauré : « {match.group(2)} » → « {cible} ».")
        return f"{match.group(1)}{cible}{match.group(3)}"

    return LIEN_RELATIF_RE.sub(swap, translated_text)


TITRE_RE = re.compile(r"^#{1,6}\s")
ANCRE_DE_TITRE_RE = re.compile(r"\{#([\w:.-]+)[^}]*\}\s*$")


def _titres(lignes):
    """[(indice de ligne, ancre ou None)] des titres ATX, hors code et commentaire HTML."""
    titres, dans_code, dans_commentaire = [], None, False
    for i, ligne in enumerate(lignes):
        nue = ligne.strip()
        if not dans_commentaire:
            m = re.match(r"^(`{3,}|~{3,})", nue)
            if m:
                if dans_code is None:
                    dans_code = m.group(1)[0] * len(m.group(1))
                elif re.fullmatch(re.escape(dans_code[0]) + "{%d,}" % len(dans_code), nue):
                    dans_code = None
                continue
        if dans_code is not None:
            continue
        if not dans_commentaire and TITRE_RE.match(ligne):
            m = ANCRE_DE_TITRE_RE.search(ligne)
            titres.append((i, m.group(1) if m else None))
        ouvre, ferme = ligne.rfind("<!--"), ligne.rfind("-->")
        if dans_commentaire:
            dans_commentaire = ferme < 0 or ouvre > ferme
        else:
            dans_commentaire = ouvre >= 0 and ouvre > ferme
    return titres


def restore_heading_spacing(source_text, translated_text):
    """Réinsère la ligne vide devant un titre de la traduction quand la source en a une.

    Pandoc ne lit un titre que précédé d'une ligne vide : collé à la ligne précédente,
    `## Invalidité {#sec-cnrps-invalidite}` devient un paragraphe, l'ancre disparaît, et
    le renvoi `@sec-cnrps-invalidite` ne résout plus. Le cas s'est produit pour six
    intertitres arabes. Il survient aussi à la jointure de deux morceaux d'un long
    fichier, quand le modèle retire la ligne vide finale du premier.

    Les titres sont appariés par leur ancre ; ceux qui n'en ont pas, par leur rang, et
    seulement si les deux textes en portent le même nombre. Les titres en code ou en
    commentaire sont ignorés. Chaque réinsertion est journalisée.
    """
    lignes_src = source_text.split("\n")
    lignes_trad = translated_text.split("\n")

    def vide_avant(lignes, i):
        return i == 0 or not lignes[i - 1].strip()

    titres_src = _titres(lignes_src)
    precede_src = {a: vide_avant(lignes_src, i) for i, a in titres_src if a}
    sans_ancre_src = [vide_avant(lignes_src, i) for i, a in titres_src if not a]
    titres_trad = _titres(lignes_trad)
    sans_ancre_trad = [i for i, a in titres_trad if not a]
    rang_sans_ancre = ({i: k for k, i in enumerate(sans_ancre_trad)}
                       if len(sans_ancre_trad) == len(sans_ancre_src) else {})

    a_inserer = []
    for i, ancre in titres_trad:
        if vide_avant(lignes_trad, i):
            continue
        attendu = (precede_src.get(ancre) if ancre
                   else (sans_ancre_src[rang_sans_ancre[i]] if i in rang_sans_ancre else None))
        if attendu:
            a_inserer.append(i)
    if not a_inserer:
        return translated_text
    for i in reversed(a_inserer):
        lignes_trad.insert(i, "")
    print(f"  titres : ligne vide réinsérée devant {len(a_inserer)} titre(s) — "
          + ", ".join(f"l. {i + 1}" for i in a_inserer) + ".")
    return "\n".join(lignes_trad)


# ---------------------------------------------------------------------------
# FORMULES MATHÉMATIQUES : masquage avant envoi, réinjection après.
#
# Les formules LaTeX (`$$ … $$` en bloc, `$…$` dans la prose) ne sont pas de la
# prose : elles doivent traverser la traduction à l'octet près. Or tout ce que le
# modèle voit, il peut l'abîmer — chiffres passés en indo-arabes, `\%` devenu `٪`,
# backslashs perdus, symboles « traduits », `$` désappariés.
#
# POURQUOI MASQUER PLUTÔT QUE RESTAURER APRÈS COUP. `restore_urls` et
# `restore_anchors` réparent par POSITION : ils supposent que le modèle garde
# l'ordre des éléments. Une formule en ligne, elle, vit dans une phrase que la
# traduction réordonne (« où $P$ est la pension, $R$ l'assiette » peut revenir
# dans un autre ordre en arabe), et une restauration positionnelle attacherait
# alors la mauvaise formule au mauvais symbole — silencieusement. Le masquage
# remplace chaque formule par un jeton opaque NOMMÉ (`⟦MATH3⟧`) : l'identité
# voyage avec le jeton, l'ordre peut changer sans dommage, et le modèle ne voit
# jamais le LaTeX.
#
# LE CONTRAT EST STRICT : un jeton perdu, dupliqué, inventé ou abîmé fait ÉCHOUER
# le fichier (`FormulesAlterees`), comme une troncature. Mieux vaut un fichier
# non traduit qu'une formule fausse dans un livre publié.
#
# Ne sont PAS masqués : le contenu des blocs de code (```…```, ~~~…~~~) et des
# spans de code en ligne (`…`), où un `$` est littéral (`$BASE_SHA` dans le
# CHANGELOG). Le précis n'écrit aucun montant avec `$` — les dinars s'écrivent
# « D » —, de sorte que tout `$` apparié hors code est une formule.
# ---------------------------------------------------------------------------

JETON_FORMULE = "⟦MATH{}⟧"
JETON_FORMULE_RE = re.compile(r"⟦MATH(\d+)⟧")
# Forme TOLÉRANTE : espaces parasites, chiffres indo-arabes (U+0660-0669) ou
# persans (U+06F0-06F9). La réparation est sans ambiguïté — le numéro reste le
# même nombre —, elle est donc faite, et journalisée.
JETON_FORMULE_LACHE_RE = re.compile(r"⟦\s*MATH\s*([0-9٠-٩۰-۹]+)\s*⟧")
JETON_SEUL_RE = re.compile(r"(?m)^[ \t]*⟦MATH(\d+)⟧[ \t]*$")
RESIDU_JETON_RE = re.compile(r"⟦|⟧|MATH\s*[0-9٠-٩۰-۹]")

# Zones où un `$` est littéral. Une clôture manquante protège jusqu'à la fin.
CODE_CLOTURE_RE = re.compile(
    r"^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?(?:^[ \t]*\1[ \t]*$|\Z)", re.MULTILINE | re.DOTALL)
CODE_EN_LIGNE_RE = re.compile(r"(`+)(?!`)[^\n]*?(?<!`)\1(?!`)")

# Bloc d'affichage d'abord : à une même position, `$$` l'emporte sur `$`.
# Règles de Pandoc pour la formule en ligne : le `$` ouvrant est suivi d'un
# non-blanc, le `$` fermant est précédé d'un non-blanc et n'est pas suivi d'un
# chiffre ; une seule ligne ; `\$` n'est pas un délimiteur.
FORMULE_RE = re.compile(
    r"\$\$(?:[^$]|\$(?!\$))+?\$\$"
    r"|(?<![\\$])\$(?![\s$])(?:[^$\n\\]|\\.)+?(?<![\s\\])\$(?![\d$])"
)
LIGNE_BLANCHE_RE = re.compile(r"\n[ \t]*\n")


class FormulesAlterees(RuntimeError):
    """La traduction n'a pas rendu les jetons de formule tels qu'ils étaient envoyés."""


def _zones_de_code(texte):
    zones = [m.span() for m in CODE_CLOTURE_RE.finditer(texte)]

    def dans_bloc(pos):
        return any(a <= pos < b for a, b in zones)

    zones += [m.span() for m in CODE_EN_LIGNE_RE.finditer(texte)
              if not dans_bloc(m.start())]
    return zones


def trouver_formules(texte):
    """Rend les positions `(début, fin)` des formules du texte, hors code.

    Une formule qui chevauche une zone de code est écartée, ainsi qu'un bloc
    `$$…$$` qui franchirait une ligne blanche : c'est alors un `$$` isolé, pas une
    équation. Un faux négatif ne fait que retomber sur le comportement antérieur
    (formule envoyée en clair) ; un faux positif est inoffensif, puisque
    l'aller-retour est exact.
    """
    zones = _zones_de_code(texte)
    formules = []
    for m in FORMULE_RE.finditer(texte):
        a, b = m.span()
        if any(a < zb and za < b for za, zb in zones):
            continue
        if m.group(0).startswith("$$") and LIGNE_BLANCHE_RE.search(m.group(0)):
            continue
        formules.append((a, b))
    return formules


def formules_de(texte):
    """Multiensemble des formules d'un texte, délimiteurs compris."""
    compte = {}
    for a, b in trouver_formules(texte):
        f = texte[a:b]
        compte[f] = compte.get(f, 0) + 1
    return compte


class TableFormules:
    """Correspondance formule ↔ jeton, partagée par tous les textes d'un même envoi.

    Une même formule reçoit toujours le même jeton, où qu'elle figure — source,
    ancienne traduction, diff : c'est ce qui permet au modèle de reconnaître dans
    l'ancienne traduction la formule que la source porte encore. La clé est la
    formule ENTIÈRE, délimiteurs compris : `$x$` et `$$x$$` sont deux formules.
    """

    def __init__(self):
        self.par_formule = {}
        self.par_numero = {}

    def __len__(self):
        return len(self.par_formule)

    def numero(self, formule):
        if formule not in self.par_formule:
            n = len(self.par_formule)
            self.par_formule[formule] = n
            self.par_numero[n] = formule
        return self.par_formule[formule]


def masquer_formules(texte, table):
    """Remplace chaque formule par son jeton `⟦MATHn⟧`, en enrichissant `table`.

    Les numéros suivent l'ordre de première rencontre : masquer la source EN
    PREMIER lui donne des numéros qui se lisent dans l'ordre du texte.
    """
    morceaux, fin = [], 0
    for a, b in trouver_formules(texte):
        morceaux.append(texte[fin:a])
        morceaux.append(JETON_FORMULE.format(table.numero(texte[a:b])))
        fin = b
    morceaux.append(texte[fin:])
    return "".join(morceaux)


def _compte(iterable):
    compte = {}
    for x in iterable:
        compte[x] = compte.get(x, 0) + 1
    return compte


def _lignes_du_jeton(texte, jeton, largeur=40):
    """Où le jeton paraît : « l. 371 « …contexte… » », une entrée par ligne qui le porte.

    Rapprocher les lignes de la source de celles de la traduction dit QUELLE occurrence
    a disparu : sans cela, « attendu 3 fois, trouvé 2 » ne distingue pas une fin de
    fichier coupée d'une formule omise en pleine phrase.
    """
    sorties = []
    for i, ligne in enumerate(texte.splitlines(), 1):
        if jeton in ligne:
            k = ligne.index(jeton)
            extrait = ligne[max(0, k - largeur):k + len(jeton) + largeur].strip()
            sorties.append(f"l. {i} « {extrait} »")
    return ", ".join(sorties) or "aucune"


# BUDGET DE SORTIE. gemini-2.5-flash « réfléchit » par défaut, et ses jetons de réflexion
# se prennent sur le même plafond que la réponse (65 536 jetons). Le 2 octobre 2026, la
# retraduction du chapitre « Cotisations sociales » (42 010 jetons en entrée) s'est arrêtée
# sur MAX_TOKENS après 37 782 jetons de réflexion pour 27 748 de traduction : plus de la
# moitié du budget allait à un raisonnement inutile pour une traduction à température 0.
# La réflexion est donc coupée, et le plafond de sortie fixé explicitement.
PLAFOND_SORTIE = 65536


def config_generation(types, guidelines):
    """Configuration de l'appel : température 0, sans réflexion, plafond de sortie explicite."""
    return types.GenerateContentConfig(
        system_instruction=guidelines,
        temperature=0.0,
        max_output_tokens=PLAFOND_SORTIE,
        thinking_config=types.ThinkingConfig(thinking_budget=0),
    )


class SortieTronquee(RuntimeError):
    """Le modèle a cessé d'écrire avant la fin : plafond de jetons de sortie atteint."""


def raison_d_arret(response):
    """`finish_reason` du premier candidat, en texte (« STOP », « MAX_TOKENS »…), ou ""."""
    try:
        raison = response.candidates[0].finish_reason
    except (AttributeError, IndexError, TypeError):
        return ""
    return getattr(raison, "name", None) or str(raison or "").rsplit(".", 1)[-1]


def journal_jetons(response):
    """Jetons consommés par l'appel : entrée, sortie, réflexion — ou "" si inconnus."""
    u = getattr(response, "usage_metadata", None)
    if u is None:
        return ""
    champs = (("entrée", "prompt_token_count"), ("sortie", "candidates_token_count"),
              ("réflexion", "thoughts_token_count"), ("total", "total_token_count"))
    return ", ".join(f"{nom} {getattr(u, attr)}" for nom, attr in champs
                     if getattr(u, attr, None) is not None)


def verifier_fin(response, file_path):
    """Journalise les jetons de l'appel et lève `SortieTronquee` sur MAX_TOKENS.

    Le garde-fou de troncature par nombre de lignes (`SEUIL_TRONCATURE`) ne voit pas une
    sortie coupée de quelques pour cent : elle passe pour une traduction un peu courte, et
    l'échec ressort ailleurs — formule manquante, fin de fichier laissée en français.
    La raison d'arrêt du modèle, elle, le dit sans ambiguïté.
    """
    raison = raison_d_arret(response)
    jetons = journal_jetons(response)
    print(f"  {file_path} : arrêt du modèle « {raison or 'inconnu'} »"
          + (f" ; jetons — {jetons}" if jetons else ""))
    if raison == "MAX_TOKENS":
        raise SortieTronquee(
            f"sortie tronquée : le modèle a atteint son plafond de jetons de sortie "
            f"({jetons or 'consommation inconnue'})")


def reinjecter_formules(source, traduction, table):
    """Remet les formules à la place de leurs jetons, ou lève `FormulesAlterees`.

    `source` est le texte source NON masqué : les jetons attendus en sont
    redéduits avec la même table. Échecs, tous explicites :
      - jeton inconnu de la table, ou attendu en nombre différent (perdu, dupliqué,
        ou recopié depuis une formule que la source n'a plus) ;
      - jeton seul sur sa ligne dans la source (formule en bloc) qui ne l'est plus ;
      - résidu de jeton après réinjection (`⟦`, `⟧`, `MATH3` sans crochets…) ;
      - multiensemble des formules du résultat différent de celui de la source —
        ce qui attrape aussi une formule que le modèle aurait écrite lui-même, ou
        un jeton qu'il aurait entouré de `$`.
    Seule réparation tolérée, et journalisée : les chiffres indo-arabes ou les
    espaces parasites À L'INTÉRIEUR d'un jeton par ailleurs bien formé.
    """
    if not len(table):
        return traduction

    source_masquee = masquer_formules(source, table)
    attendus = _compte(int(n) for n in JETON_FORMULE_RE.findall(source_masquee))

    normalises = 0

    def normaliser(m):
        nonlocal normalises
        n = int(m.group(1))  # int() lit aussi les chiffres indo-arabes
        canon = JETON_FORMULE.format(n)
        if m.group(0) != canon:
            normalises += 1
        return canon

    traduction = JETON_FORMULE_LACHE_RE.sub(normaliser, traduction)
    if normalises:
        print(f"  formules : {normalises} jeton(s) mal recopié(s) (chiffres ou "
              f"espaces), normalisé(s).")

    trouves = _compte(int(n) for n in JETON_FORMULE_RE.findall(traduction))
    problemes = []
    for n in sorted(set(attendus) | set(trouves)):
        if n not in table.par_numero:
            problemes.append(f"⟦MATH{n}⟧ inconnu")
        elif attendus.get(n, 0) != trouves.get(n, 0):
            jeton = JETON_FORMULE.format(n)
            problemes.append(f"⟦MATH{n}⟧ attendu {attendus.get(n, 0)} fois, "
                             f"trouvé {trouves.get(n, 0)} fois "
                             f"({table.par_numero[n][:60]!r}) — source : "
                             f"{_lignes_du_jeton(source_masquee, jeton)} ; traduction : "
                             f"{_lignes_du_jeton(traduction, jeton)}")

    seuls_src = _compte(int(n) for n in JETON_SEUL_RE.findall(source_masquee))
    seuls_trad = _compte(int(n) for n in JETON_SEUL_RE.findall(traduction))
    for n, k in sorted(seuls_src.items()):
        if seuls_trad.get(n, 0) != k:
            problemes.append(f"⟦MATH{n}⟧ n'est plus seul sur sa ligne "
                             f"(formule en bloc)")

    if problemes:
        raise FormulesAlterees(
            "formules altérées par la traduction : " + " ; ".join(problemes))

    restitue = JETON_FORMULE_RE.sub(
        lambda m: table.par_numero[int(m.group(1))], traduction)

    # Un résidu n'est cherché que HORS des formules restituées, qui ne portent
    # jamais de jeton mais pourraient, en théorie, contenir « MATH ».
    hors_formules = masquer_formules(restitue, TableFormules())
    hors_formules = JETON_FORMULE_RE.sub("", hors_formules)
    if RESIDU_JETON_RE.search(hors_formules):
        m = RESIDU_JETON_RE.search(hors_formules)
        raise FormulesAlterees(
            f"formules altérées par la traduction : résidu de jeton "
            f"{hors_formules[max(0, m.start() - 20):m.end() + 20]!r}")

    if formules_de(restitue) != formules_de(source):
        raise FormulesAlterees(
            "formules altérées par la traduction : les formules restituées ne "
            "sont pas celles de la source (formule écrite en clair par le "
            "modèle, ou jeton entouré de `$`).")

    print(f"  formules : {sum(attendus.values())} restituée(s) depuis "
          f"{len(attendus)} jeton(s).")
    return restitue


def diff_masque(ancienne_source, nouvelle_source, chemin, table, table_code=None):
    """Diff unifié entre deux états de la source, formules (et code des cellules) masqués.

    Le diff de git porte le LaTeX en clair, sur des lignes préfixées de `+`/`-`
    où un bloc `$$…$$` n'est plus reconnaissable : le modèle y verrait les
    formules que l'on masque partout ailleurs, et serait tenté de les recopier.
    On le recalcule donc dans l'espace masqué, avec les mêmes tables. Il en va de
    même du code des cellules, que le diff de git exposerait en clair.
    """
    import difflib

    def masquer(texte):
        if table_code is not None:
            texte = masquer_cellules(texte, table_code)
        return masquer_formules(texte, table)

    ancien = masquer(ancienne_source).splitlines(keepends=True)
    nouveau = masquer(nouvelle_source).splitlines(keepends=True)
    return "".join(difflib.unified_diff(
        ancien, nouveau, fromfile=f"a/{chemin}", tofile=f"b/{chemin}"))


CONSIGNE_FORMULES = """
JETONS DE FORMULE : les jetons de la forme ⟦MATH0⟧, ⟦MATH1⟧… remplacent des formules
mathématiques. Recopie chaque jeton TEL QUEL — chiffres latins, sans espace, sans `$`
autour —, à sa place dans la phrase traduite, et autant de fois qu'il figure dans le
FICHIER SOURCE. Un jeton seul sur sa ligne reste seul sur sa ligne. N'écris jamais
toi-même de formule, et ne recopie pas un jeton que le FICHIER SOURCE ne porte plus.
"""


def get_git_diff(base_sha, head_sha, file_path):
    try:
        cmd = ["git", "diff", base_sha, head_sha, "--", file_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return ""


# DÉCOUPAGE DES LONGS FICHIERS. Même sans réflexion, le plafond de sortie (65 536 jetons)
# ne suffit pas à rendre en un appel un chapitre de plus de ~140 000 caractères : le
# 3 octobre 2026, `retraites/_secteur_prive.qmd` (231 Ko) s'est arrêté sur MAX_TOKENS
# avec 65 533 jetons écrits. Au-delà du seuil, le fichier est traduit section par
# section — coupé sur les titres `##` ou `###` qui portent une ancre `{#…}`, hors code, hors
# commentaire HTML et hors bloc `:::` —, puis recollé. En mise à jour, chaque morceau
# source est apparié au morceau cible qui commence à la MÊME ancre : les ancres sont
# recopiées verbatim, elles sont donc communes aux deux langues. Si elles ne le sont
# pas, le fichier échoue explicitement plutôt que d'apparier de travers.
SEUIL_DECOUPAGE = 140_000
TAILLE_MORCEAU = 60_000
TITRE_ANCRE_RE = re.compile(r"^#{2,3}\s.*\{#([\w:.-]+)[^}]*\}\s*$")


def points_de_coupe(texte):
    """[(position, ancre)] des titres `##` à ancre où l'on peut couper le texte.

    Ne coupe jamais dans un bloc de code, un commentaire HTML ni un bloc `:::` : un
    morceau qui ouvrirait l'un sans le fermer inviterait le modèle à le refermer.
    """
    points, pos = [], 0
    dans_code = False
    dans_commentaire = False
    profondeur_div = 0
    for ligne in texte.splitlines(keepends=True):
        nue = ligne.strip()
        if not dans_commentaire and nue.startswith("```"):
            dans_code = not dans_code
        elif not dans_code:
            if not dans_commentaire:
                m = TITRE_ANCRE_RE.match(ligne.rstrip("\n"))
                if m and profondeur_div == 0 and pos > 0:
                    points.append((pos, m.group(1)))
                if nue.startswith(":::"):
                    if re.match(r"^:::+\s*$", nue):
                        profondeur_div = max(0, profondeur_div - 1)
                    else:
                        profondeur_div += 1
            ouvre, ferme = ligne.count("<!--"), ligne.count("-->")
            if dans_commentaire and ferme:
                dans_commentaire = ouvre > 0 and ligne.rfind("<!--") > ligne.rfind("-->")
            elif ouvre > ferme or (ouvre and ligne.rfind("<!--") > ligne.rfind("-->")):
                dans_commentaire = True
        pos += len(ligne)
    return points


def decouper(texte, taille=TAILLE_MORCEAU, ancres_permises=None):
    """Découpe en morceaux d'environ `taille` caractères aux points de coupe.

    Rend [(ancre de début ou None pour le premier, morceau)]. Un morceau peut dépasser
    `taille` si aucune coupe n'est possible plus tôt. `"".join` des morceaux redonne
    exactement le texte. `ancres_permises` : en mise à jour, les ancres présentes dans
    l'ancienne traduction — on ne coupe que là, pour que l'appariement tienne même si
    la traduction a pris un peu de retard.
    """
    coupes = []
    debut = 0
    dernier_point = None
    points = [(pos, ancre) for pos, ancre in points_de_coupe(texte)
              if ancres_permises is None or ancre in ancres_permises]
    for pos, ancre in points:
        if pos - debut > taille and dernier_point is not None:
            coupes.append(dernier_point)
            debut = dernier_point[0]
        dernier_point = (pos, ancre)
        if pos - debut > taille:
            coupes.append(dernier_point)
            debut = pos
            dernier_point = None
    if len(texte) - debut > taille and dernier_point is not None and dernier_point[0] > debut:
        coupes.append(dernier_point)
    morceaux, precedent, ancre_prec = [], 0, None
    for pos, ancre in coupes:
        morceaux.append((ancre_prec, texte[precedent:pos]))
        precedent, ancre_prec = pos, ancre
    morceaux.append((ancre_prec, texte[precedent:]))
    return morceaux


CONSIGNE_VERBATIM = """RECOPIE VERBATIM, JAMAIS TRADUITE NI FLÉCHIE : les cibles de liens et les ancres
(`](#g-entrepositaire)`, `{#tbl-dc-petroliers}`), les clés de citation `[@loi-88-62]` et
leurs locateurs, les URL, les numéros de textes juridiques (« loi n° 88-62 », « décret
n° 91-550 ») et le contenu des commentaires HTML `<!-- ... -->`. Ce ne sont pas de la
prose : une cible de lien mise au pluriel ne pointe plus sur rien, et un commentaire
corrompu se lit dans la source."""

CONSIGNE_MORCEAU = """CE TEXTE EST UN MORCEAU D'UN FICHIER PLUS LONG, découpé entre deux titres de section.
Traduis-le tel quel : n'ajoute ni ne retire aucun titre, bloc de code, bloc `:::` ou
commentaire, et ne complète rien de ce qui précède ou suit."""


def prompt_morceau(source_lang, target_lang, source, ancienne, consigne_formules):
    """Prompt d'un morceau : mise à jour sans diff si une ancienne traduction existe."""
    if ancienne:
        return f"""
Voici une tâche de mise à jour de traduction bilingue.

Langue source : {source_lang}
Langue cible : {target_lang}

{CONSIGNE_MORCEAU}

Voici le MORCEAU SOURCE MIS À JOUR ({source_lang}) :
```markdown
{source}
```

Voici l'ANCIENNE TRADUCTION CIBLE ({target_lang}) de ce même morceau :
```markdown
{ancienne}
```

Compare toi-même le MORCEAU SOURCE MIS À JOUR et l'ANCIENNE TRADUCTION.

TA TÂCHE :
Mets à jour l'ANCIENNE TRADUCTION pour qu'elle corresponde au MORCEAU SOURCE MIS À JOUR.
RÈGLE D'OR ABSOLUE : Tu DOIS conserver exactement la même formulation que l'ANCIENNE TRADUCTION partout où le sens de la source n'a pas changé. L'ANCIENNE TRADUCTION peut contenir des corrections faites à la main : ne les défais pas, ne reformule pas ce qui est déjà correct. Ne touche qu'à ce qui ne correspond plus à la source.

{CONSIGNE_VERBATIM}
{consigne_formules}
Renvoie UNIQUEMENT le morceau cible mis à jour, sans aucun commentaire avant ou après.
"""
    return f"""
Voici un morceau de fichier source en {source_lang} à traduire en {target_lang}.
S'il te plaît, traduis-le entièrement et renvoie UNIQUEMENT le code source traduit, sans aucun commentaire.
Préserve TOUTES les balises Markdown, les blocs de code et la structure exacte.

{CONSIGNE_MORCEAU}

{CONSIGNE_VERBATIM}
{consigne_formules}
Morceau à traduire :
```markdown
{source}
```
"""


# CELLULES DE CODE. Le traducteur ne doit traduire que les CHAÎNES d'une cellule Python
# (légendes, notes de lecture) : la structure du code doit rester celle de la source. Le
# 3 octobre 2026, la retraduction de `retraites/_secteur_prive.qmd` a rendu des guillemets
# « » par des guillemets droits À L'INTÉRIEUR de chaînes délimitées par des guillemets
# droits : trois cellules ne compilaient plus, et le livre arabe ne se construisait plus.
# Contrôle : chaque cellule `{python}` de la traduction doit COMPILER — sinon le livre ne
# se construit plus, et le fichier échoue. Seule réparation tolérée, et journalisée : les
# guillemets droits intérieurs d'une ligne de chaîne, rendus « », à condition que la
# cellule compile ensuite et ait le même arbre syntaxique que celle de la source.
# Une cellule qui compile mais DIFFÈRE de la source (chaînes et `#| fig-cap` exceptés),
# ou une cellule manquante, est SIGNALÉE sans bloquer : c'est le retard d'une traduction
# sur son original (au 3 octobre 2026, dix chapitres arabes dans ce cas), que corrige une
# retraduction complète, non une raison d'interdire toute mise à jour du fichier.
CELLULE_PYTHON_RE = re.compile(r"```\{python\}\n(.*?)```", re.S)


class CellulesAlterees(RuntimeError):
    """Une cellule de code de la traduction ne compile plus ou diffère de la source."""


def _squelette_cellule(cellule):
    """Arbre syntaxique de la cellule, chaînes neutralisées ; None si elle ne compile pas."""
    import ast
    code = "\n".join(l for l in cellule.split("\n") if not l.startswith("#|"))
    try:
        arbre = ast.parse(code)
    except SyntaxError:
        return None
    for noeud in ast.walk(arbre):
        if isinstance(noeud, ast.Constant) and isinstance(noeud.value, str):
            noeud.value = "S"
    return ast.dump(arbre)


def _options_cellule(cellule):
    return [l for l in cellule.split("\n") if l.startswith("#|") and not l.startswith("#| fig-cap")]


def _reparer_guillemets(cellule):
    """Rend « » les guillemets droits intérieurs des lignes de chaîne ; (cellule, nombre)."""
    lignes, n = [], 0
    for ligne in cellule.split("\n"):
        m = re.match(r'^(\s*r?)"(.*)"(\s*[,)]*\s*)$', ligne)
        if m and '"' in m.group(2):
            sortie, ouvrant = [], True
            for c in m.group(2):
                if c == '"':
                    sortie.append("«" if ouvrant else "»")
                    ouvrant = not ouvrant
                    n += 1
                else:
                    sortie.append(c)
            ligne = f'{m.group(1)}"{"".join(sortie)}"{m.group(3)}'
        lignes.append(ligne)
    return "\n".join(lignes), n


def _etiquette(cellule):
    return next((l for l in cellule.split("\n") if l.startswith("#| label")),
                cellule.split("\n")[0])[:80]


def verifier_cellules(source, traduction):
    """Rend la traduction, cellules éventuellement réparées ; lève `CellulesAlterees` si une
    cellule ne compile pas. Les écarts de structure sont signalés, non bloquants."""
    cellules_source = CELLULE_PYTHON_RE.findall(source)
    cellules_trad = CELLULE_PYTHON_RE.findall(traduction)
    if not cellules_trad:
        if cellules_source:
            print(f"  cellules : AVERTISSEMENT — {len(cellules_source)} cellule(s) Python dans "
                  "la source, aucune dans la traduction (traduction en retard).")
        return traduction
    alignees = len(cellules_trad) == len(cellules_source)
    if not alignees:
        print(f"  cellules : AVERTISSEMENT — {len(cellules_source)} cellule(s) Python dans la "
              f"source, {len(cellules_trad)} dans la traduction (traduction en retard).")
    reparees, cassees, divergentes = 0, [], []
    sources = iter(cellules_source if alignees else [None] * len(cellules_trad))

    def controler(m):
        nonlocal reparees
        source_cellule = next(sources)
        cellule = m.group(1)
        attendu = (None if source_cellule is None else
                   (_squelette_cellule(source_cellule), _options_cellule(source_cellule)))
        actuel = (_squelette_cellule(cellule), _options_cellule(cellule))
        if actuel[0] is not None and (attendu is None or actuel == attendu):
            return m.group(0)
        reparee, n = _reparer_guillemets(cellule)
        if n and _squelette_cellule(reparee) is not None and (
                attendu is None or (_squelette_cellule(reparee), _options_cellule(reparee)) == attendu):
            reparees += 1
            return "```{python}\n" + reparee + "```"
        if actuel[0] is None:
            cassees.append(_etiquette(cellule))
        else:
            divergentes.append(_etiquette(source_cellule))
        return m.group(0)

    traduction = CELLULE_PYTHON_RE.sub(controler, traduction)
    if reparees:
        print(f"  cellules : {reparees} cellule(s) réparée(s) (guillemets intérieurs rendus « »).")
    if divergentes:
        print("  cellules : AVERTISSEMENT — code différent de la source (traduction en retard) : "
              + " ; ".join(divergentes))
    if cassees:
        raise CellulesAlterees("cellule(s) Python qui ne compile(nt) plus : " + " ; ".join(cassees))
    return traduction


# ---------------------------------------------------------------------------
# MASQUAGE DU CODE DES CELLULES : le modèle ne voit que les chaînes à traduire.
#
# `verifier_cellules` constate après coup ; il ne sait réparer qu'un cas (les guillemets
# droits d'une ligne de chaîne). Le 3 octobre 2026, une note de lecture d'une vingtaine
# de littéraux concaténés, ponctuée de « », est revenue avec des guillemets droits au
# milieu de littéraux à guillemets droits. On retire donc le code au modèle, comme les
# formules.
#
# DEUX VOIES ÉTAIENT POSSIBLES. (a) Faire traduire les chaînes d'une cellule dans un appel
# séparé, en JSON, puis les réinsérer échappées : le code n'est jamais exposé, mais chaque
# fichier coûte un appel de plus, et la note de lecture est traduite hors de la prose
# qu'elle commente. (b) Masquer le code dans l'appel principal : tout ce qui n'est pas le
# CORPS d'une chaîne de prose — clôtures, options `#|`, appels, noms de séries, guillemets
# délimiteurs — devient un jeton opaque `⟪CODEn⟫`, et le modèle traduit le texte qui
# sépare deux jetons, dans son contexte. C'est (b) qui est retenue : un seul appel, le
# contexte conservé, et un contrat aussi strict que celui des formules.
#
# CE QUI RESTE VISIBLE. Le corps d'un littéral `"…"` (préfixe `r` ou `u` admis ; ni
# f-chaîne, ni triple guillemet, ni guillemet simple) qui contient au moins un blanc et une
# lettre — légendes, notes de lecture —, et la valeur entre guillemets des options
# `#| fig-cap`, `tbl-cap`, `fig-alt`, `fig-subcap`. Un nom de série, un chemin,
# `"{{< meta date >}}"` restent du code. Des littéraux CONCATÉNÉS (séparés par de simples
# retours à la ligne) sont montrés d'un tenant, puis répartis à nouveau sur autant de
# littéraux qu'à la source (`_redecouper`) : montrés un à un, le modèle recousait les
# phrases et perdait les jetons intermédiaires (trois perdus le 3 octobre 2026 sur
# `_regime_indiciaire.qmd`).
#
# LE CONTRAT. La SUITE des jetons de la traduction doit être exactement celle de la source :
# les jetons sont nommés par leur contenu, et une suite réordonnée donnerait du code brouillé
# qui pourrait encore compiler. Tout écart fait échouer le fichier (`CellulesAlterees`). Le
# texte rendu entre deux jetons est ensuite ré-échappé : guillemets droits intérieurs rendus
# « » (la parité court sur toute la cellule, car une paire peut s'ouvrir dans un littéral et
# se fermer dans le suivant), saut de ligne rendu blanc, barre oblique inverse invalide
# doublée hors chaîne brute, blancs de bord rétablis comme à la source.
#
# ORDRE. Masquer les cellules AVANT les formules : les chaînes brutes portent du LaTeX
# (`$\tau_0 = 40\,\%$`), qui reçoit ainsi son jeton ⟦MATH⟧. Réinjecter dans l'ordre
# inverse : formules d'abord (contre la source masquée de ses cellules), cellules ensuite.
# Les crochets ⟪⟫ diffèrent de ⟦⟧ pour ne pas déclencher le contrôle de résidu des formules.
# ---------------------------------------------------------------------------

JETON_CODE = "⟪CODE{}⟫"
JETON_CODE_RE = re.compile(r"⟪CODE(\d+)⟫")
JETON_CODE_LACHE_RE = re.compile(r"⟪\s*CODE\s*([0-9٠-٩۰-۹]+)\s*⟫")
RESIDU_CODE_RE = re.compile(r"⟪|⟫")
CELLULE_ENTIERE_RE = re.compile(r"```\{python\}\n.*?```", re.S)
OUVERTURE_CELLULE = "```{python}\n"
OPTION_TRADUITE_RE = re.compile(
    r'^(#\|\s*(?:fig-cap|tbl-cap|fig-alt|fig-subcap)\s*:\s*")(.*)("\s*)$')
LITTERAL_PROSE_RE = re.compile(r'([rRuU]?)"(?!"")')
ECHAPPEMENTS_VALIDES = set("\\'\"abfnrtv01234567xNuU")

CONSIGNE_CODE = """
JETONS DE CODE : les jetons de la forme ⟪CODE0⟫, ⟪CODE1⟫… remplacent du code. Recopie chaque
jeton TEL QUEL, sans espace, DANS LE MÊME ORDRE que dans le FICHIER SOURCE et autant de fois
qu'il y figure. Traduis le texte compris entre deux jetons, et n'y écris jamais de guillemet
droit " : emploie « ».
"""


class TableCode(TableFormules):
    """Correspondance segment de code ↔ jeton : une même suite de caractères, un même jeton."""


def _corps_de_cellule(cellule):
    """[(début, fin, brut, corps)] des chaînes à traduire dans le texte d'une cellule.

    Des littéraux CONCATÉNÉS — séparés par de simples retours à la ligne, comme ceux
    d'une note de lecture — forment UN seul élément, et le
    modèle voit leur texte d'un tenant. Les montrer un à un, séparés par des jetons,
    l'invitait à recoudre les phrases coupées en fin de ligne et à perdre les jetons
    intermédiaires : le 3 octobre 2026, la retraduction de `_regime_indiciaire.qmd` en a
    perdu trois. `corps` donne les bornes de chaque corps de littéral ; `(début, fin)`
    couvre du premier au dernier, séparateurs compris ; `brut` dit si la barre oblique inverse y est littérale (chaîne `r"…"`).

    Rend None si la cellule ne se découpe pas en lexèmes, ou si un lexème ne se retrouve
    pas à sa place : elle est alors masquée d'un seul tenant.
    """
    import io
    import tokenize
    elements, debuts, pos = [], [], 0
    for ligne in cellule.split("\n"):
        debuts.append(pos)
        m = OPTION_TRADUITE_RE.match(ligne)
        if m and m.group(2):
            elements.append((pos + m.end(1), pos + m.end(2), False,
                             [(pos + m.end(1), pos + m.end(2))]))
        pos += len(ligne) + 1
    try:
        lexemes = list(tokenize.generate_tokens(io.StringIO(cellule).readline))
    except Exception:  # noqa: BLE001 — TokenError, SyntaxError, IndentationError…
        return None

    groupes, groupe = [], None  # groupe : [début, fin, brut, [corps]] ou None
    for lex in lexemes:
        if lex.type == tokenize.NL:
            continue  # un retour à la ligne entre deux littéraux ne rompt pas le groupe
        litteral = None
        if lex.type == tokenize.STRING:
            a = debuts[lex.start[0] - 1] + lex.start[1]
            if cellule[a:a + len(lex.string)] != lex.string:
                return None
            m = LITTERAL_PROSE_RE.match(lex.string)
            if m and len(lex.string) >= len(m.group(0)) + 1 and lex.string.endswith('"'):
                debut = a + len(m.group(0))
                litteral = (debut, a + len(lex.string) - 1, m.group(1) in ("r", "R"))
        if litteral and groupe and groupe[2] == litteral[2]:
            groupe[1] = litteral[1]
            groupe[3].append(litteral[:2])
            continue
        if groupe:
            groupes.append(groupe)
        groupe = [litteral[0], litteral[1], litteral[2], [litteral[:2]]] if litteral else None
    if groupe:
        groupes.append(groupe)

    for debut, fin, brut, corps in groupes:
        texte = "".join(cellule[x:y] for x, y in corps)
        if re.search(r"\s", texte) and re.search(r"[^\W\d_]", texte) and "{{<" not in texte:
            elements.append((debut, fin, brut, corps))
    return sorted(elements, key=lambda e: e[0])


def _masquer_cellules(texte, table):
    """Texte masqué, et la suite des jetons [(numéro, gabarit ou None, ouvre la cellule)].

    Le `gabarit` décrit la chaîne qui SUIT le jeton dans la source — None pour le dernier
    jeton d'une cellule, qui porte la clôture fermante : (texte d'origine de l'empan,
    corps des littéraux, séparateurs entre eux, brut).
    """
    morceaux, suite, fin = [], [], 0
    for m in CELLULE_ENTIERE_RE.finditer(texte):
        cellule = m.group(0)
        decalage = len(OUVERTURE_CELLULE)
        elements = _corps_de_cellule(cellule[decalage:-3])
        if elements is None:
            print(f"  cellules : {_etiquette(cellule[decalage:])} ne se découpe pas en "
                  "lexèmes — masquée d'un seul tenant, ses chaînes restent en l'état.")
            elements = []
        morceaux.append(texte[fin:m.start()])
        precedent = 0
        for i, (a, b, brut, corps) in enumerate(elements):
            a, b = a + decalage, b + decalage
            n = table.numero(cellule[precedent:a])
            bornes = [(x + decalage, y + decalage) for x, y in corps]
            textes = [cellule[x:y] for x, y in bornes]
            separateurs = [cellule[y:x] for (_, y), (x, _) in zip(bornes, bornes[1:])]
            morceaux += [JETON_CODE.format(n), "".join(textes)]
            suite.append((n, (cellule[a:b], textes, separateurs, brut), i == 0))
            precedent = b
        n = table.numero(cellule[precedent:])
        morceaux.append(JETON_CODE.format(n))
        suite.append((n, None, not elements))
        fin = m.end()
    morceaux.append(texte[fin:])
    return "".join(morceaux), suite


def masquer_cellules(texte, table):
    """Remplace le code de chaque cellule `{python}` par des jetons `⟪CODEn⟫` (voir plus haut)."""
    return _masquer_cellules(texte, table)[0]


def _reechapper(corps, source, brut, ouvrant):
    """Rend (corps sûr dans un littéral `"…"`, nombre de corrections, parité des « »)."""
    n = 0
    if "\n" in corps:
        corps = re.sub(r"[ \t]*\n[ \t]*", " ", corps)
        n += 1
    sortie, i = [], 0
    while i < len(corps):
        c = corps[i]
        if c == "\\":
            if i + 1 == len(corps):  # barre finale : elle échapperait le guillemet fermant
                n += 1
                i += 1
                continue
            if brut or corps[i + 1] in ECHAPPEMENTS_VALIDES:
                sortie.append(corps[i:i + 2])
            else:
                sortie.append("\\\\" + corps[i + 1])
                n += 1
            i += 2
            continue
        if c == '"':
            sortie.append("«" if ouvrant else "»")
            ouvrant = not ouvrant
            n += 1
        else:
            sortie.append(c)
        i += 1
    corps = "".join(sortie)
    tete = re.match(r"[ \t]*", source).group(0)
    queue = re.search(r"[ \t]*$", source).group(0)
    if tete and corps and not corps[0].isspace():
        corps, n = tete + corps, n + 1
    if queue and corps and not corps[-1].isspace():
        corps, n = corps + queue, n + 1
    return corps, n, ouvrant


def _redecouper(texte, origine, textes, separateurs):
    """Répartit le texte traduit d'un groupe de littéraux concaténés sur autant de
    littéraux que la source, aux mêmes séparateurs (retour à la ligne et indentation).

    Texte inchangé : l'empan d'origine, à l'octet près. Sinon, coupe à un blanc non
    échappé, au plus près de la part de longueur qu'occupait chaque littéral dans la
    source ; un littéral peut rester vide si le texte est court. Le parseur Python
    recolle les littéraux adjacents : l'arbre syntaxique est celui d'une seule chaîne,
    quelle que soit la coupe.
    """
    if texte == "".join(textes):
        return origine
    if not separateurs:
        return texte
    total_source = sum(len(t) for t in textes) or 1
    coupes_possibles = [i + 1 for i, c in enumerate(texte) if c == " "
                        and (len(texte[:i]) - len(texte[:i].rstrip("\\"))) % 2 == 0]
    coupes, cumul, precedente = [], 0, 0
    for t in textes[:-1]:
        cumul += len(t)
        cible = round(cumul / total_source * len(texte))
        candidates = [c for c in coupes_possibles if c >= precedente]
        coupe = min(candidates, key=lambda c: abs(c - cible)) if candidates else precedente
        coupes.append(coupe)
        precedente = coupe
    bornes = [0] + coupes + [len(texte)]
    pieces = [texte[a:b] for a, b in zip(bornes, bornes[1:])]
    sortie = [pieces[0]]
    for sep, piece in zip(separateurs, pieces[1:]):
        sortie += [sep, piece]
    return "".join(sortie)


def reinjecter_cellules(source, traduction, table):
    """Remet le code des cellules à la place de ses jetons, ou lève `CellulesAlterees`.

    `source` est le texte source NON masqué de ses cellules. Échecs, tous explicites : suite
    de jetons différente de celle de la source (perdu, dupliqué, inventé, déplacé), résidu
    de jeton. Réparations journalisées : chiffres ou espaces dans un jeton, corps de chaîne
    ré-échappés, clôture ouvrante ou fermante remise en début de ligne.
    """
    if not len(table):
        return traduction
    _masque, attendue = _masquer_cellules(source, table)

    normalises = 0

    def normaliser(m):
        nonlocal normalises
        canon = JETON_CODE.format(int(m.group(1)))  # int() lit aussi les chiffres indo-arabes
        if m.group(0) != canon:
            normalises += 1
        return canon

    traduction = JETON_CODE_LACHE_RE.sub(normaliser, traduction)
    if normalises:
        print(f"  cellules : {normalises} jeton(s) de code mal recopié(s), normalisé(s).")

    trouvee = [int(n) for n in JETON_CODE_RE.findall(traduction)]
    numeros = [n for n, *_ in attendue]
    if trouvee != numeros:
        k = next((i for i, (x, y) in enumerate(zip(numeros, trouvee)) if x != y),
                 min(len(numeros), len(trouvee)))
        attendu = JETON_CODE.format(numeros[k]) if k < len(numeros) else "rien"
        trouve = JETON_CODE.format(trouvee[k]) if k < len(trouvee) else "rien"
        raise CellulesAlterees(
            f"code des cellules altéré par la traduction : {len(numeros)} jeton(s) de code "
            f"attendus dans l'ordre de la source, {len(trouvee)} trouvés ; premier écart au "
            f"rang {k} (attendu {attendu}, trouvé {trouve}). "
            "Relancer, au besoin en retraduction complète (traduction_complete).")

    parties = JETON_CODE_RE.split(traduction)
    sortie = [parties[0]]
    corrections, recollees, ouvrant = 0, 0, True
    for i, (n, gabarit, ouvre) in enumerate(attendue):
        if ouvre:
            ouvrant = True
            avant = sortie[-1]
            if avant.rstrip(" \t").endswith("\n"):
                avant = avant.rstrip(" \t")
            elif avant:
                avant += "\n"
                recollees += 1
            sortie[-1] = avant
        sortie.append(table.par_numero[n])
        intervalle = parties[2 * i + 2]
        if RESIDU_CODE_RE.search(intervalle):
            raise CellulesAlterees(
                f"code des cellules altéré par la traduction : résidu de jeton "
                f"{intervalle[:60]!r}")
        if gabarit is not None:
            origine, textes, separateurs, brut = gabarit
            intervalle, k, ouvrant = _reechapper(intervalle, "".join(textes), brut, ouvrant)
            corrections += k
            intervalle = _redecouper(intervalle, origine, textes, separateurs)
        elif intervalle and not intervalle.startswith("\n"):
            intervalle = "\n" + intervalle
            recollees += 1
        sortie.append(intervalle)
    if corrections:
        print(f"  cellules : {corrections} correction(s) d'échappement dans les chaînes "
              "traduites (guillemets droits rendus « », sauts de ligne, barres obliques, "
              "blancs de bord).")
    if recollees:
        print(f"  cellules : {recollees} clôture(s) de cellule remise(s) en début de ligne.")
    print(f"  cellules : code restitué depuis {len(numeros)} jeton(s).")
    return "".join(sortie)


class DecoupageImpossible(RuntimeError):
    """Les ancres de coupe de la source manquent dans la traduction, ou en désordre."""


def apparier(morceaux_source, cible):
    """Découpe `cible` aux ancres qui ouvrent les morceaux de la source.

    Rend la liste des morceaux cibles, un par morceau source. Lève `DecoupageImpossible`
    si une ancre manque dans la cible ou n'y vient pas dans le même ordre.
    """
    index = {ancre: pos for pos, ancre in points_de_coupe(cible)}
    positions = []
    for ancre, _m in morceaux_source[1:]:
        if ancre not in index:
            raise DecoupageImpossible(f"ancre {{#{ancre}}} absente de la traduction")
        positions.append(index[ancre])
    if positions != sorted(positions):
        raise DecoupageImpossible("ancres de coupe dans un autre ordre dans la traduction")
    bornes = [0] + positions + [len(cible)]
    return [cible[a:b] for a, b in zip(bornes, bornes[1:])]


def get_git_show(sha, file_path):
    """Contenu du fichier à un commit donné, ou chaîne vide s'il n'y existait pas."""
    try:
        cmd = ["git", "show", f"{sha}:{file_path}"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return ""


def main():
    # Import local : voir la note en tête de module. Seul `main()` parle au modèle.
    from google import genai
    from google.genai import types

    if len(sys.argv) < 4:
        print("Usage: python translate_sync.py <base_sha> <head_sha> <file1> <file2> ...")
        sys.exit(0)

    base_sha = sys.argv[1]
    head_sha = sys.argv[2]
    files_to_process = sys.argv[3:]
    
    try:
        client = genai.Client()
    except Exception as e:
        print(f"Erreur d'initialisation de l'API Gemini : {e}")
        sys.exit(1)
    
    guidelines_path = "translation_guidelines.md"
    try:
        with open(guidelines_path, "r", encoding="utf-8") as f:
            guidelines = f.read()
    except Exception:
        guidelines = "Tu es un traducteur professionnel juridique."

    # Glossaire terminologique canonique généré depuis precis/glossaire.yml.
    # Inclus tel quel (sans modifier le guide rédigé à la main) pour garantir
    # la bijection des termes FR↔AR.
    try:
        with open("translation_glossary.generated.md", "r", encoding="utf-8") as f:
            guidelines += "\n\n" + f.read()
    except Exception:
        pass

    fr_files = {f for f in files_to_process if "precis/fr/" in f}
    failures = []
    traduits = 0          # fichiers effectivement écrits
    echecs_plafond = 0    # échecs imputables au plafond, et à lui seul

    for file_path in files_to_process:
        if not fichier_a_traduire(file_path):
            continue

        if not os.path.exists(file_path):
            continue

        if file_path == "CHANGELOG.md":
            source_lang = "Français/Anglais"
            target_lang = "Arabe"
            target_path = "CHANGELOG_ar.md"
        elif "precis/fr/" in file_path:
            source_lang = "Français"
            target_lang = "Arabe"
            target_path = file_path.replace("precis/fr/", "precis/ar/")
        elif "precis/ar/" in file_path:
            fr_counterpart = file_path.replace("precis/ar/", "precis/fr/")
            if fr_counterpart in fr_files:
                print(f"Skip : {file_path} (le fichier FR correspondant est aussi dans le diff, FR est la source de vérité)")
                continue
            source_lang = "Arabe"
            target_lang = "Français"
            target_path = file_path.replace("precis/ar/", "precis/fr/")
        else:
            continue
            
        print(f"Mise à jour : {file_path} -> {target_path}")
        
        with open(file_path, "r", encoding="utf-8") as f:
            new_source_text = f.read()
            
        old_target_text = ""
        if os.path.exists(target_path):
            with open(target_path, "r", encoding="utf-8") as f:
                old_target_text = f.read()
                
        diff_text = get_git_diff(base_sha, head_sha, file_path)
        
        # Retraduction complète, demandée explicitement : on ignore la traduction
        # existante. C'est le recours quand une traduction a trop décroché pour être
        # rattrapée par mise à jour. Le modèle, à qui l'on demande de « conserver
        # exactement la formulation de l'ancienne traduction partout où le sens n'a
        # pas changé », préserve alors une cible bien plus courte que sa source au
        # lieu de la compléter : le chapitre Fiscalité arabe est resté à 105 lignes
        # contre 580 en français, quinze appels de tableaux et onze numéros de textes
        # en moins. Aucune consigne supplémentaire ne corrige cela de façon fiable ;
        # seul le départ de zéro le fait.
        #
        # Le prix est réel et assumé : les corrections faites à la main sur la seule
        # langue cible sont perdues. D'où le caractère explicite de l'option — jamais
        # de retraduction complète par défaut.
        if os.environ.get("TRADUCTION_COMPLETE") == "1":
            if old_target_text:
                print(f"  {file_path} : retraduction complète demandée, "
                      f"l'ancienne traduction ({len(old_target_text.splitlines())} lignes) "
                      "est ignorée.")
            old_target_text = ""

        # MASQUAGE DES FORMULES (voir `masquer_formules`). Les trois textes envoyés —
        # source, ancienne traduction, diff — sont masqués avec UNE table : une même
        # formule y porte le même jeton. La source d'abord, pour que ses numéros
        # suivent l'ordre du texte. Les variables non masquées restent intactes :
        # `restore_*`, la troncature et le repère de longueur les lisent.
        # MASQUAGE DU CODE DES CELLULES (voir `masquer_cellules`), AVANT les formules :
        # les chaînes laissées visibles portent du LaTeX, qui reçoit ainsi son jeton.
        table_code = TableCode()
        source_sans_code = masquer_cellules(new_source_text, table_code)
        ancienne_sans_code = masquer_cellules(old_target_text, table_code)
        table_formules = TableFormules()
        prompt_source = masquer_formules(source_sans_code, table_formules)
        prompt_old_target = masquer_formules(ancienne_sans_code, table_formules)
        prompt_diff = diff_text
        consigne_formules = ""
        if len(table_formules) or len(table_code):
            if diff_text:
                ancienne_source = get_git_show(base_sha, file_path)
                prompt_diff = diff_masque(ancienne_source, new_source_text,
                                          file_path, table_formules, table_code)
        if len(table_formules):
            consigne_formules = CONSIGNE_FORMULES
            print(f"  formules : {len(table_formules)} formule(s) distincte(s) "
                  f"masquée(s) avant envoi.")
        if len(table_code):
            consigne_formules += CONSIGNE_CODE
            print(f"  cellules : {len(table_code)} segment(s) de code distinct(s) "
                  f"masqué(s) avant envoi.")

        # Dès qu'une traduction existe, on part d'elle — même sans diff.
        # Retraduire de zéro un fichier déjà traduit EFFACE les corrections faites
        # à la main sur la seule langue cible, qui sont légitimes et courantes
        # (l'arabe se corrige parfois seul, sans passer par le français). Le DIFF,
        # quand il est disponible, ne sert qu'à désigner ce qui a bougé ; son
        # absence — cas de la re-synchro manuelle — ne doit pas faire basculer en
        # traduction complète.
        if old_target_text:
            if diff_text:
                diff_section = f"""
Voici le DIFF (les modifications) qui viennent d'être faites sur le fichier source :
```diff
{prompt_diff}
```

TA TÂCHE :
Mets à jour l'ANCIENNE TRADUCTION pour qu'elle corresponde au FICHIER SOURCE MIS À JOUR.
RÈGLE D'OR ABSOLUE : Tu DOIS conserver exactement la même formulation que l'ANCIENNE TRADUCTION pour tous les paragraphes qui n'ont pas été modifiés. Ne modifie la traduction que pour les parties qui ont été ajoutées ou modifiées dans le DIFF.
"""
            else:
                diff_section = """
Aucun DIFF n'est disponible : compare toi-même le FICHIER SOURCE MIS À JOUR et l'ANCIENNE TRADUCTION.

TA TÂCHE :
Mets à jour l'ANCIENNE TRADUCTION pour qu'elle corresponde au FICHIER SOURCE MIS À JOUR.
RÈGLE D'OR ABSOLUE : Tu DOIS conserver exactement la même formulation que l'ANCIENNE TRADUCTION partout où le sens du fichier source n'a pas changé. L'ANCIENNE TRADUCTION peut contenir des corrections faites à la main : ne les défais pas, ne reformule pas ce qui est déjà correct. Ne touche qu'à ce qui ne correspond plus à la source.
"""
            prompt = f"""
Voici une tâche de mise à jour de traduction bilingue.

Langue source : {source_lang}
Langue cible : {target_lang}

Voici le FICHIER SOURCE MIS À JOUR ({source_lang}) :
```markdown
{prompt_source}
```

Voici l'ANCIENNE TRADUCTION CIBLE ({target_lang}) (avant tes modifications) :
```markdown
{prompt_old_target}
```
{diff_section}
RECOPIE VERBATIM, JAMAIS TRADUITE NI FLÉCHIE : les cibles de liens et les ancres
(`](#g-entrepositaire)`, `{{#tbl-dc-petroliers}}`), les clés de citation `[@loi-88-62]` et
leurs locateurs, les URL, les numéros de textes juridiques (« loi n° 88-62 », « décret
n° 91-550 ») et le contenu des commentaires HTML `<!-- ... -->`. Ce ne sont pas de la
prose : une cible de lien mise au pluriel ne pointe plus sur rien, et un commentaire
corrompu se lit dans la source.
{consigne_formules}
Renvoie UNIQUEMENT le nouveau fichier cible mis à jour, sans aucun commentaire avant ou après.
"""
        else:
            prompt = f"""
Voici le fichier source en {source_lang} à traduire en {target_lang}.
S'il te plaît, traduis-le entièrement et renvoie UNIQUEMENT le code source traduit, sans aucun commentaire.
Préserve TOUTES les balises Markdown, les blocs de code et la structure exacte.

RECOPIE VERBATIM, JAMAIS TRADUITE NI FLÉCHIE : les cibles de liens et les ancres
(`](#g-entrepositaire)`, `{{#tbl-dc-petroliers}}`), les clés de citation `[@loi-88-62]` et
leurs locateurs, les URL, les numéros de textes juridiques (« loi n° 88-62 », « décret
n° 91-550 ») et le contenu des commentaires HTML `<!-- ... -->`. Ce ne sont pas de la
prose : une cible de lien mise au pluriel ne pointe plus sur rien, et un commentaire
corrompu se lit dans la source.
{consigne_formules}
Fichier à traduire :
```markdown
{prompt_source}
```
"""



        def appeler(prompt):
            # Retry avec backoff exponentiel sur erreurs transitoires.
            # Gemini renvoie régulièrement 503 UNAVAILABLE en pic de demande ;
            # sans retry, une seule occurrence faisait échouer toute la synchro.
            # Le 500 INTERNAL est tout aussi transitoire — le message de l'API
            # invite lui-même à réessayer — et il n'était pas rattrapé : le
            # 27/08/2026 il a fait échouer la traduction d'un chapitre entier.
            max_attempts = 5
            response = None
            for attempt in range(1, max_attempts + 1):
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt,
                        config=config_generation(types, guidelines),
                    )
                    break
                except Exception as api_err:
                    msg = str(api_err)
                    if not est_transitoire(msg):
                        # Limite dure : on abandonne SANS attendre, et on dit pourquoi
                        # en clair — c'est la ligne que le journal doit donner d'emblée.
                        if any(s in msg.lower() for s in ERREURS_DURES):
                            print(f"  {file_path}: LIMITE DURE, aucun réessai — {msg[:200]}")
                            # Le plafond vaut pour TOUTE la passe, pas pour ce
                            # fichier seul : continuer la boucle ne ferait que
                            # rejouer le même refus, une fois par fichier. Le
                            # 20 septembre 2026, onze fichiers en retard ont
                            # produit onze appels voués à l'échec là où un seul
                            # suffisait à établir la cause.
                            raise LimiteDure(msg) from api_err
                        raise
                    if attempt == max_attempts:
                        raise
                    wait = min(60, 5 * (2 ** (attempt - 1)))  # 5,10,20,40,60s
                    print(f"  {file_path}: erreur transitoire ({msg[:60]}…), retry {attempt}/{max_attempts - 1} dans {wait}s")
                    time.sleep(wait)

            if response is None:
                raise RuntimeError("aucune réponse de l'API après retries")
            verifier_fin(response, file_path)
            translated_text = response.text
            if translated_text.startswith("```markdown\n"):
                translated_text = translated_text[12:]
            if translated_text.endswith("\n```\n"):
                translated_text = translated_text[:-5]
            elif translated_text.endswith("\n```"):
                translated_text = translated_text[:-4]
            return translated_text

        try:
            if len(prompt_source) > SEUIL_DECOUPAGE:
                morceaux = decouper(prompt_source, ancres_permises=(
                    {a for _p, a in points_de_coupe(prompt_old_target)}
                    if prompt_old_target else None))
                anciens = (apparier(morceaux, prompt_old_target) if prompt_old_target
                           else [""] * len(morceaux))
                print(f"  {file_path} : {len(prompt_source)} caractères, traduit en "
                      f"{len(morceaux)} morceaux (seuil {SEUIL_DECOUPAGE}).")
                parties = []
                for (_ancre, morceau), ancien in zip(morceaux, anciens):
                    rendu = appeler(prompt_morceau(source_lang, target_lang, morceau,
                                                   ancien, consigne_formules))
                    if morceau.endswith("\n") and not rendu.endswith("\n"):
                        rendu += "\n"
                    parties.append(rendu)
                translated_text = "".join(parties)
            else:
                translated_text = appeler(prompt)

            # La troncature d'abord, dans l'espace masqué : une sortie coupée perd aussi
            # des jetons, et son diagnostic propre est plus juste que « jeton manquant ».
            # (Le contrôle est refait plus bas sur le texte restitué.)
            motif = motif_de_troncature(
                len(prompt_old_target.splitlines()) or len(prompt_source.splitlines()),
                len(translated_text.splitlines()),
                len(prompt_source.splitlines()),
            )
            if motif:
                raise RuntimeError(motif)

            # Les jetons d'abord : `restore_*` et la troncature comparent à la
            # source NON masquée, et un jeton altéré doit faire échouer le fichier
            # avant toute autre réparation (`FormulesAlterees` est rattrapée plus
            # bas comme tout échec : fichier non écrit, sortie en code 1).
            # Ordre inverse du masquage : formules d'abord (contre la source masquée de
            # ses cellules, puisque des formules vivent dans leurs chaînes), code ensuite.
            translated_text = reinjecter_formules(source_sans_code, translated_text,
                                                  table_formules)
            translated_text = reinjecter_cellules(new_source_text, translated_text,
                                                  table_code)
            # Ordre voulu : les clés d'abord (restore_locators apparie par clé), puis
            # les liens de glossaire en trop (ils faussent les comptes de
            # restore_anchors et restore_relative_links), puis les locateurs.
            translated_text = restore_citation_keys(new_source_text, translated_text)
            translated_text = remove_extra_glossary_links(new_source_text, translated_text)
            translated_text = restore_locators(new_source_text, translated_text)
            translated_text = restore_urls(new_source_text, translated_text)
            translated_text = restore_anchors(new_source_text, translated_text)
            translated_text = restore_relative_links(new_source_text, translated_text)
            translated_text = restore_heading_spacing(new_source_text, translated_text)

            # GARDE-FOU CONTRE LA TRADUCTION TRONQUÉE.
            #
            # Le modèle renvoie parfois un fichier amputé au lieu de la mise à jour
            # demandée : le 9 septembre 2026, un chapitre arabe de 636 lignes est
            # revenu à 68, soit 89 % de perte, et la PR ouverte automatiquement
            # ressemblait à n'importe quelle autre. Rien dans le rendu ne l'aurait
            # signalé — un chapitre amputé reste un chapitre bien formé.
            #
            # Une traduction n'est jamais beaucoup plus courte que ce qu'elle met à
            # jour, sauf si la SOURCE a elle-même raccourci. On compare donc les deux
            # rapports : la cible ne doit pas fondre plus vite que sa source.
            # LE REPÈRE « AVANT » MANQUE DANS DEUX CAS, et ce sont ceux où la
            # troncature est la plus probable : la première traduction d'un fichier,
            # et la RETRADUCTION COMPLÈTE, où l'ancienne cible est volontairement
            # ignorée (voir plus haut). Le contrôle était alors sauté — il ne
            # s'exécutait pas précisément quand il servait le plus. On se règle donc
            # sur la SOURCE à défaut d'ancienne cible ; `motif_de_troncature` prend
            # déjà le plus petit des deux repères, la substitution est sans effet
            # quand les deux existent.
            reference = (len(old_target_text.splitlines())
                         or len(new_source_text.splitlines()))
            motif = motif_de_troncature(
                reference,
                len(translated_text.splitlines()),
                len(new_source_text.splitlines()),
            )
            if motif:
                raise RuntimeError(motif)

            # Les cellules de code après la troncature : une sortie tronquée perd aussi des
            # cellules, et son diagnostic propre est plus juste que « cellule manquante ».
            translated_text = verifier_cellules(new_source_text, translated_text)

            # `dirname` rend la chaîne VIDE pour une cible à la racine du dépôt —
            # `CHANGELOG_ar.md` est la seule dans ce cas —, et `os.makedirs('')` lève
            # FileNotFoundError. La synchro échouait donc à chaque publication de version,
            # et le CHANGELOG arabe n'a jamais pu être écrit une seule fois.
            dossier = os.path.dirname(target_path)
            if dossier:
                os.makedirs(dossier, exist_ok=True)
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(texte_a_ecrire(translated_text))
            print(f"Succès : {target_path} mis à jour.")
            traduits += 1
            time.sleep(5) # Éviter le Rate Limit (15 RPM)
            
        except LimiteDure as e:
            print(f"Erreur lors de la traduction de {file_path}: {e}")
            failures.append(f"{file_path} : {e}")
            echecs_plafond += 1
            restants = [
                f for f in files_to_process[files_to_process.index(file_path) + 1:]
                if fichier_a_traduire(f) and os.path.exists(f)
            ]
            if restants:
                print(f"Passe interrompue : {len(restants)} fichier(s) non tentés, "
                      "le plafond vaut pour tous.")
                failures.extend(f"{f} : non tenté (plafond atteint)" for f in restants)
                echecs_plafond += len(restants)
            break
        except Exception as e:
            print(f"Erreur lors de la traduction de {file_path}: {e}")
            failures.append(f"{file_path} : {e}")

    # Une synchro partielle ne doit JAMAIS passer pour complète. Jusqu'ici le
    # script signalait l'échec d'un fichier puis rendait la main en code 0 : le
    # workflow committait et ouvrait une PR d'apparence normale, à laquelle il
    # manquait un chapitre. C'est ainsi que l'arabe de `fiscalite` a perdu ses
    # citations sans que personne ne le voie. En échouant ici, on n'ouvre pas de
    # PR trompeuse ; il suffit de relancer la synchro.
    if failures:
        print(f"\n{len(failures)} fichier(s) NON traduit(s) :")
        for line in failures:
            print(f"  - {line}")

        # PLAFOND MENSUEL SANS AUCUNE TRADUCTION : ce n'est pas un échec, c'est une
        # attente. Rien n'a été écrit, donc l'étape d'ouverture de PR ne trouvera
        # rien à committer et s'arrêtera d'elle-même : la garde contre la PR
        # partielle reste entière. Faire rougir la CI à chaque poussée pendant les
        # jours qui restent avant la remise à zéro du plafond n'apprendrait rien
        # après la première fois, et apprendrait surtout à ignorer le rouge.
        #
        # Dès qu'UN SEUL fichier a été traduit, l'état est partiel et l'échec
        # reprend ses droits : c'est exactement le cas que cette garde existe pour
        # empêcher.
        # Neutre SEULEMENT si le plafond explique TOUT. Une seule panne d'une autre
        # nature — une troncature, par exemple — et l'échec reprend ses droits :
        # sans quoi le silence du plafond couvrirait une vraie régression.
        if traduits == 0 and echecs_plafond == len(failures) and echecs_plafond:
            avis = (
                "PLAFOND DE DÉPENSE MENSUEL ATTEINT — aucun fichier traduit, "
                "aucune PR ouverte, rien de cassé.\n"
                "L'arabe reste en retard sur le français jusqu'à la remise à zéro "
                "du plafond ; scripts/traduction_en_retard.py dit lesquels.\n"
                "Aucune relance ne servira d'ici là : ce n'est pas un débit, c'est "
                "un plafond."
            )
            print("\n" + avis)
            resume = os.environ.get("GITHUB_STEP_SUMMARY")
            if resume:
                with open(resume, "a", encoding="utf-8") as f:
                    f.write("### Traduction en attente\n\n" + avis.replace("\n", "\n\n") + "\n")
            return

        print("\nSynchro incomplète : aucune PR ne doit être ouverte sur cet état. "
              "Relancer le workflow (workflow_dispatch) sur les fichiers concernés.")
        sys.exit(1)

if __name__ == "__main__":
    main()

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
    malgré la consigne — « art. 5 à 7 » devient « art. 5 إلى 7 » —, et c'est
    une transformation assez mécanique pour être défaite ici plutôt que
    négociée à chaque passe.

    Prudence : on ne recopie que si les clés apparaissent dans le même ordre et
    en même nombre des deux côtés. Sinon on ne touche à rien, et le contrôle de
    parité signalera l'écart.
    """
    src = CITATION_RE.findall(source_text)
    dst = CITATION_RE.findall(translated_text)
    if len(src) != len(dst) or [k for k, _ in src] != [k for k, _ in dst]:
        return translated_text

    locators = iter(loc for _, loc in src)

    def swap(match):
        source_locator = next(locators)
        if ARABIC_RE.search(match.group(2)):
            return f"[@{match.group(1)}, {source_locator}]"
        return match.group(0)

    return CITATION_RE.sub(swap, translated_text)


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
            problemes.append(f"⟦MATH{n}⟧ attendu {attendus.get(n, 0)} fois, "
                             f"trouvé {trouves.get(n, 0)} fois "
                             f"({table.par_numero[n][:60]!r})")

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


def diff_masque(ancienne_source, nouvelle_source, chemin, table):
    """Diff unifié entre deux états de la source, formules masquées.

    Le diff de git porte le LaTeX en clair, sur des lignes préfixées de `+`/`-`
    où un bloc `$$…$$` n'est plus reconnaissable : le modèle y verrait les
    formules que l'on masque partout ailleurs, et serait tenté de les recopier.
    On le recalcule donc dans l'espace masqué, avec la même table.
    """
    import difflib
    ancien = masquer_formules(ancienne_source, table).splitlines(keepends=True)
    nouveau = masquer_formules(nouvelle_source, table).splitlines(keepends=True)
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
        table_formules = TableFormules()
        prompt_source = masquer_formules(new_source_text, table_formules)
        prompt_old_target = masquer_formules(old_target_text, table_formules)
        prompt_diff = diff_text
        consigne_formules = ""
        if len(table_formules):
            if diff_text:
                ancienne_source = get_git_show(base_sha, file_path)
                prompt_diff = diff_masque(ancienne_source, new_source_text,
                                          file_path, table_formules)
            consigne_formules = CONSIGNE_FORMULES
            print(f"  formules : {len(table_formules)} formule(s) distincte(s) "
                  f"masquée(s) avant envoi.")

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



        try:
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
                        config=types.GenerateContentConfig(
                            system_instruction=guidelines,
                            temperature=0.0,
                        ),
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
            translated_text = response.text
            if translated_text.startswith("```markdown\n"):
                translated_text = translated_text[12:]
            if translated_text.endswith("\n```\n"):
                translated_text = translated_text[:-5]
            elif translated_text.endswith("\n```"):
                translated_text = translated_text[:-4]

            # Les formules d'abord : `restore_*` et la troncature comparent à la
            # source NON masquée, et un jeton altéré doit faire échouer le fichier
            # avant toute autre réparation (`FormulesAlterees` est rattrapée plus
            # bas comme tout échec : fichier non écrit, sortie en code 1).
            translated_text = reinjecter_formules(new_source_text, translated_text,
                                                  table_formules)
            translated_text = restore_locators(new_source_text, translated_text)
            translated_text = restore_urls(new_source_text, translated_text)
            translated_text = restore_anchors(new_source_text, translated_text)

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

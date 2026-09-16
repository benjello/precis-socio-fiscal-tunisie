# La chaîne éditoriale : dépendances et propriétaires

> Cette note dit **dans quel ordre** les agents interviennent et **pourquoi cet ordre-là**.
> Elle a été écrite le 15/09/2026, après une journée où six défaillances de coordination ont
> été rencontrées et corrigées. Chacune est consignée ici avec son mécanisme, pour qu'on ne
> reconstitue pas l'ordre naïf par commodité.

## L'ordre naïf et pourquoi il ne marche pas

On enchaînerait volontiers : **documenter → écrire → nommer → sourcer**. C'est l'ordre du
récit. Les données vont dans l'autre sens.

| Ce qui a cassé | Mécanisme |
|---|---|
| Bibliographie **après** le glossaire, alors que le glossaire *cite* la bibliographie | `source_definition: {ref: X}` se rend en `[@X]`, et **`build_glossary.py` ne valide pas les refs**. Une clé absente ne fait échouer aucun gate : elle produit une citation morte dans la page publiée. |
| Circularité **ancre ↔ notion** | Le gate échoue si la prose ancre `#g-x` sans entrée (terminologue **avant**), mais ne rend que les notions qu'un livre ancre (terminologue **après**). Aucun ordre simple ne marche. |
| Zotero **sans propriétaire** | Le bibliographe écrivait dans `references.json`, rien ne remontait, la descente écrasait. Mesuré : **119 clés** absentes de Zotero, une inbox de 1 592 lignes jamais vidée. |
| `_quarto.yml` arabe **orphelin** | Chapitre FR ajouté → l'arabe est livré → personne ne le déclare → **404** silencieux. |
| Des **rouges muets** | Le Checker AI échoue sur un format de réponse quand rendu et parité sont verts plus haut. Pire : sur une PR où l'arabe remplace une amorce, il lit l'asymétrie des diffs comme un « débordement » et **suggère de supprimer la traduction livrée**. |
| La traduction **n'appartenait à personne** | Plafond de dépense, troncature, terminologie : aucun agent désigné pour lire un échec et le rattraper. |

## La chaîne

```
1. documentaliste          note sourcée, références candidates, notions
        ↓
2. bibliographe  VERSEMENT les clés CSL existent et résolvent (FR + AR)
        ↓                  ── gate : toute clé citable résout
3. terminologue  PASSE 1   ids + termes FR/AR ; définitions différées
        ↓                  ── gate : build_glossary.py = 0 ; les ancres existent
4. rédacteur               la prose ancre et cite, sans rien inventer
        ↓                  ── gate : render = 0, zéro [?]
5. terminologue  PASSE 2   définitions, sources, passage en « valide »
        ↓                  ── gate : build_glossary.py = 0 ; le compte de notions a monté
6. bibliographe  CLÔTURE   résolution + dry-run Zotero OBLIGATOIRE
        ↓
7. revue humaine           aucune action sortante avant validation
        ↓
   ─── fusion ───
        ↓
8. relecteur-ar            déclare les chapitres arabes, rend le livre AR en local
```

## Le geste décisif : le terminologue passe deux fois

C'est la seule modification qui ne soit pas cosmétique. Elle tranche la circularité : les
**ancres existent avant la prose** — le gate passe — et les **définitions arrivent après** —
les notions sont ancrées, donc rendues.

Le 15/09/2026, vingt notions de la TVA ont été versées avant toute prose. Elles étaient
correctes, sourcées, et **invisibles sur toute page** : le livre en retenait douze sur cent
cinquante-deux. Après la rédaction qui les ancre, il en retient trente-deux.

## Qui porte quel verrou

| Verrou | Propriétaire | Ce qui arrive sans lui |
|---|---|---|
| Une clé citée existe | bibliographe (versement) | citation morte, invisible aux gates |
| Une ancre employée existe | terminologue (passe 1) | `build_glossary.py` échoue |
| Une notion est rendue | rédacteur (elle l'ancre) | notion dormante, écrite pour rien |
| Une définition est juste et bilingue | terminologue (passe 2) | entrée `provisoire` sans contenu |
| La conversion vers Zotero fonctionne | bibliographe (clôture, `dry-run`) | un champ bloque 333 références, des mois durant |
| Un article poussé a sa collection | bibliographe (`ranger`) | il devient « commun » et la descente le déplace |
| Une clé devenue **commune** n'a plus de collection de livre | bibliographe (`controle-rangement`) | `ranger` n'ajoute que des collections : la clé reste rattachée au livre où elle est née, et chaque descente la redescend dans ce livre au lieu du fonds commun |
| Un chapitre arabe est déclaré | relecteur-ar | 404 silencieux |
| Un échec de traduction est lu | relecteur-ar | on croit cassé ce qui est sain, ou l'inverse |

## Quatre règles de lecture, apprises à leurs dépens

**Ne lis pas la conclusion d'un job, lis ses étapes.** `verify_translation.py` fait échouer
dès que la réponse du Checker n'est pas exactement `OK` ; les gardes déterministes sont
**« Check FR/AR parity »** et **« Render the touched Arabic books »**.

**Nomme les étapes, ne les numérote pas.** Cette note a elle-même dit « étapes 8 et 9 »
jusqu'au 16/09/2026, jour où la garde déterministe se trouvait à l'étape **4**. Les numéros
suivent le workflow ; les noms, non. Un agent qui cherche un numéro lit autre chose, ou rien.

**Une divergence de parité peut se corriger côté FRANÇAIS.** Le 16/09/2026, une ancre
apparaissait 1× en français et 2× en arabe : le traducteur avait lié une notion que la source
laissait nue, et il avait raison. Le correctif tenait en une ligne de français. Tenir l'arabe
pour fautif par défaut, c'est relancer une traduction déjà juste.

**Mesure les codes de retour hors d'un tube.** `$?` après un tube mesure le dernier élément.
Un gate déclaré vert sur cette base n'a jamais tourné.

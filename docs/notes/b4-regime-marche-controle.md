# Note documentaire — B.4 Le régime de marché contrôlé

Matière sourcée pour `precis/fr/remunerations_publiques/_regime_marche_controle.qmd`.
Périmètre : entreprises publiques **financières** — banques à capital public (STB, BNA,
BH Bank…), sociétés d'assurance publiques, institutions financières — où la rémunération
est fortement autonome (alignée sur le privé) mais sous contrôle de l'État actionnaire.
Frontière avec B.3 : le caractère **financier** (les *Rapports sur les entreprises publiques*
du ministère des Finances [@minfin-ep] excluent les banques).

Ton strictement documentaire et neutre (banques publiques = sujet sensible). Aucun
nom, part de capital, texte, date ou chiffre n'est affirmé sans source primaire/officielle.
Tout point non vérifié est marqué TODO. URL JORT = pist.tn.

## 0. Vérification des clés déjà citées

- `loi89-9` : EXISTE (`precis/fr/remunerations_publiques/references.json`), URL pist.tn.
- `minfin-ep` : EXISTE (même fichier), type `report`. URL générique finances.gov.tn (le
  rapport lui-même est annexé à la LF ; cf. B.3, site gbo.tn injoignable).
- `loi-irpp-is-1989` : EXISTE dans `precis/fr/references.json` (racine), pas dans le
  references.json du livre. Titre « Loi n°89-114 du 30 décembre 1989 portant promulgation
  du Code de l'IRPP et de l'IS », URL pist.tn. RÉUTILISABLE pour B.4 (retenue à la source).
- `loi2017-66-lf2018` : EXISTE (references.json du livre), art. 53 CSS. RÉUTILISABLE.
- Glossaire : l'entrée `regime-marche-controle` existe déjà dans `precis/glossaire.yml`.

## 1. Champ d'application — faits sourcés

### 1.1 Le caractère financier comme frontière B.3/B.4
- Les entreprises publiques financières relèvent du **même périmètre actionnarial** que les
  non financières : loi n°89-9 du 1er février 1989, art. 8 (entreprise publique = EPNA, ou
  société à capital entièrement public, ou société détenue à ≥50 % par l'État / collectivités
  / établissements publics) [@loi89-9]. La spécificité n'est donc PAS le périmètre
  actionnarial mais l'**activité financière** (banque, assurance, crédit).
- C'est l'activité financière qui fonde le découpage : les *Rapports sur les entreprises
  publiques* du ministère des Finances excluent explicitement banques et caisses de leur
  périmètre statistique [@minfin-ep] (déjà établi en B.3).

### 1.2 Cadre sectoriel de l'activité bancaire (loi-cadre, pour situer le champ)
- **Loi n°2016-48 du 11 juillet 2016, relative aux banques et aux établissements financiers**
  — texte en vigueur régissant la profession. JORT n°58 de 2016.
  PDF : `https://www.pist.tn/jort/2016/2016F/Jo0582016.pdf` (cache JORT local confirmé ;
  notice cache en arabe, intitulé FR « relative aux banques et aux établissements
  financiers » attesté par le décret d'application 2020-113 qui la cite). Lignée historique :
  loi n°67-51 du 7 décembre 1967 réglementant la profession bancaire → loi n°2001-65 du
  10 juillet 2001 relative aux établissements de crédit → loi 2016-48.
- **Code des assurances** : loi n°92-24 du 9 mars 1992 (pour les sociétés d'assurance).
  PDF : `https://www.pist.tn/jort/1992/1992F/Jo01792.pdf`.
- Ces lois-cadres définissent l'ACTIVITÉ, pas la rémunération des agents ; elles servent
  uniquement à délimiter le champ « financier ». Elles ne distinguent pas capital public
  et privé.

### 1.3 Banques à capital public — faits sourcés (PRUDENCE: aucune part inventée)
- L'entrée de l'État au capital de la STB et de la BNA est attestée par des lois anciennes :
  loi n°57-15 du 17 août 1957 (souscription de l'État à l'augmentation de capital de la
  Société tunisienne de banque) ; loi n°59-47 du 28 avril 1959 (souscription au capital de
  la « Banque nationale agricole »). Sources primaires JORT :
  `https://www.pist.tn/jort/1957/1957F/Jo00757.pdf` et
  `https://www.pist.tn/jort/1959/1959F/Jo02459.pdf`.
  ATTENTION : ces textes prouvent l'entrée historique de l'État au capital, PAS la part
  publique ACTUELLE (modifiée par des recapitalisations successives — cf. recapitalisation
  STB/BH approuvée par le Parlement en 2015). NE PAS en déduire un pourcentage courant.
- Part publique courante : trois banques cotées à capital majoritairement/largement public
  sont communément citées — **STB, BNA, BH Bank**. Source officielle pressentie = document
  de référence / rapport annuel de chaque banque + données d'actionnariat BVMT. Donnée
  repérée mais NON encore validée sur source primaire datée : STB ~52 % participation
  publique et semi-publique, BNA ~50 % État + entreprises publiques (presse financière
  ilboursa / tustex 2023). TODO : remplacer par le rapport annuel officiel de chaque banque
  (STB-RAPPORT-FR-2023.pdf repéré sur stb.com.tn) ; citer par banque, à une date de
  référence explicite, en présentant la part comme évolutive (recapitalisations). NE PAS
  AFFIRMER de pourcentage tant que la source officielle n'est pas lue.

### 1.4 Statut des agents : convention collective sectorielle (résultat MAJEUR, source primaire)
- Les agents des banques (publiques comme privées) ne relèvent NI de la loi 83-112 (fonction
  publique) NI, en pratique, du statut 85-78 des entreprises publiques : ils relèvent d'une
  **convention collective sectorielle de droit commun**, agréée par arrêté du ministre des
  Affaires sociales en application du Code du travail.
- **Convention collective nationale du personnel des banques et des établissements
  financiers** : convention agréée par arrêté du 24 décembre 1975 (JORT n°87 de 1975), texte
  publié au JORT n°6 du 27 janvier 1976 ; convention collective nationale agréée à nouveau
  par arrêté du 23 août 1983 (JORT n°71 de 1983) ; avenants successifs (1989, 1991, avenant
  n°3 en 1993…). **Convention révisée** agréée par arrêté du 17 février 2014 (JORT n°23 de
  2014, PDF `https://www.pist.tn/jort/2014/2014F/Jo0232014.pdf`), puis avenants n°1 (2014),
  n°3 (2017), n°4 (2019, publié en arabe), **n°5 (arrêté du 17 novembre 2022, JORT n°126 de
  2022)**. Toutes ces références proviennent du cache JORT local (titres FR attestés).
- POINT STRUCTURANT pour le qualificatif « marché contrôlé » : c'est UNE SEULE convention
  sectorielle qui couvre banques publiques ET privées indistinctement — la rémunération de
  base est donc fixée par un mécanisme de **droit commun du travail** (négociation
  collective + agrément ministériel), non par un statut public. C'est la preuve
  documentaire la plus propre de l'autonomie « proche du privé ».
- Parallèle assurances : convention collective nationale des assurances, agréée par arrêté
  du 24 décembre 1975 (JORT n°87 de 1975), révisée 1983, avenants jusqu'aux années 2010+
  (cache JORT). Même logique sectorielle pour les sociétés d'assurance publiques.

## 2. La construction de la rémunération — faits sourcés

### 2.1 Mécanisme
- Socle : la convention collective sectorielle bancaire (§1.4) fixe classification des
  emplois, grilles et éléments permanents ; chaque banque y ajoute sa politique salariale
  d'entreprise (part variable / bonus). TODO : la structure exacte (fixe conventionnel +
  variable d'entreprise, intéressement) n'est PAS établie sur source primaire ici — l'OCR
  du texte de la convention révisée 2014 reste à faire pour citer les articles. Ne pas
  affirmer le détail du variable sans cette lecture.

### 2.2 Ce qui justifie « marché contrôlé » : autonomie SOUS contrôle de l'État actionnaire
- Autonomie : rémunération de base par convention sectorielle de droit commun, alignée sur
  la concurrence du secteur (banques privées dans la même convention).
- Contrôle : l'État exerce ses prérogatives d'actionnaire (conseil d'administration,
  tutelle) ; surtout, la **rémunération des dirigeants** d'entreprises publiques — y compris
  banques à majorité publique — est ENCADRÉE PAR TEXTE. Chaîne réglementaire (évolution,
  source primaire JORT, cache local) :
  - décret n°78-885 du 11 octobre 1978, fixant le régime de rémunération des chefs
    d'entreprise publique (`.../1978F/Jo06878.pdf`) ; circulaire 78-45 du 27 nov. 1978
    (`.../1979F/Jo00279.pdf`) — HISTORIQUE ;
  - modifié par décrets 82-509, 83-577, 84-865 ;
  - **décret n°90-1855 du 10 novembre 1990, fixant le régime de rémunération des chefs
    d'entreprises à majorité publique** (`.../1990F/Jo07590.pdf`), modifié 92-1, 2006-2564 ;
  - décret n°2014-12 du 10 janvier 2014 (taux des éléments de rémunération des chefs
    d'établissements et entreprises publiques et sociétés à majorité publique,
    `.../2014F/Jo0052014.pdf`) ;
  - **décret n°2015-2217 du 11 décembre 2015** (en vigueur), *fixant le régime/les taux des
    éléments de rémunération des chefs d'établissements et entreprises publiques et de
    sociétés à majorité publique*. JORT n°101 de 2015,
    `https://www.pist.tn/jort/2015/2015F/Jo1012015.pdf`. Abroge les textes antérieurs
    contraires (dont 90-1855 et 2014-12 selon la base legislation-securite.tn).
  Ainsi le contraste est documenté : agents = autonomie conventionnelle de marché ;
  DIRIGEANTS = plafonnement réglementaire par l'État. C'est précisément le « marché
  contrôlé ».
- TODO : confirmer sur le PDF du décret 2015-2217 que les BANQUES à majorité publique
  entrent bien dans son champ « entreprises publiques et sociétés à majorité publique »
  (probable mais à lire). Circulaire n°04 du 10 mars 2021 citée par legislation-securite.tn
  comme texte d'application du régime de rémunération des chefs — à vérifier/sourcer.

## 3. Les prélèvements sur la rémunération — faits sourcés (point sensible)

### 3.1 Sécurité sociale : CNSS (et NON CNRPS)
- Les agents des banques relèvent du **régime des salariés non agricoles géré par la CNSS**
  (loi n°60-30 du 14 décembre 1960 [@loi60-30], déjà référencée dans le livre).
- Vérification du discriminant (méthode B.3) : les banques ne figurent PAS sur la liste du
  décret n°85-1025 (affiliation CNRPS des EPIC/sociétés nationales — cf. liste B.3) ; et
  AUCUN régime spécial de retraite bancaire transféré à la CNRPS n'a été trouvé dans le
  cache JORT (la voie CREGT de 1998 ne concerne que électricité/gaz/transports, pas les
  banques). La conclusion CNSS est donc cohérente avec les deux voies d'affiliation CNRPS,
  qui sont l'une et l'autre négatives pour les banques.
- TODO (prudence) : confirmer l'absence d'un régime complémentaire/spécial propre à un
  établissement bancaire particulier avant d'affirmer « toutes les banques publiques → CNSS,
  sans exception ». Le principe (convention de droit commun → salariés non agricoles → CNSS)
  est solide ; l'exhaustivité nominative reste à border.
- TODO : taux salarial/patronal CNSS exacts (décret de cotisation / fiche CLEISS), non
  reproduits ici.

### 3.2 IRPP — retenue à la source
- Traitements soumis à la retenue à la source au titre des traitements et salaires, en
  application du Code de l'IRPP et de l'IS [@loi-irpp-is-1989] (clé dans references.json
  RACINE). Modalités générales renvoyées à la partie fiscalité des revenus du travail.

### 3.3 CSS — contribution sociale de solidarité
- Applicable aux revenus salariaux, instituée par la loi de finances 2018, art. 53
  [@loi2017-66-lf2018].

## 4. Repères budgétaires / statistiques — faits sourcés (privilégier les séries)

### 4.1 Poids du secteur bancaire public
- Exposition des trois banques publiques (BNA, STB, BH Bank) au secteur public ≈ 35,6 % de
  leurs actifs en 2023 — donnée presse financière (ilboursa) citant les rapports/états
  financiers. À remplacer par les rapports annuels des banques ou un rapport BCT/CMF.
  N'est PAS une donnée de rémunération.

### 4.2 Salaire moyen du secteur financier public — LACUNE
- Le stub (ligne 5) AFFIRME déjà que les rémunérations moyennes du secteur financier public
  « figurent parmi les plus élevées du secteur public ». Cette affirmation N'EST PAS sourcée
  à ce stade par une statistique officielle (INS/BCT). Pistes : rapport IACE sur les
  entreprises publiques (coût moyen par travailleur ~45 217 DT/an, MAIS périmètre EP non
  financières, donc NON probant pour le financier) ; enquête INS sur les salaires ; séries
  sectorielles BCT.
- DÉCISION RECOMMANDÉE : tant qu'aucune série officielle « salaire moyen secteur financier
  public » n'est trouvée, soit qualifier l'affirmation (« souvent présenté comme… »), soit
  la retirer. NE PAS la laisser passer comme un fait établi. Respecter aussi l'invariant
  « jamais un chiffre ponctuel sans vue d'évolution » : viser une SÉRIE, pas un point.
- TODO PRIORITAIRE : trouver une série officielle de salaire moyen / coût du travail du
  secteur financier (INS, comptes de la nation par branche « activités financières et
  d'assurance », ou BCT). C'est la principale lacune statistique du chapitre.

## 5. Références candidates (CSL-JSON)

### Déjà présentes (ne pas recréer)
- `loi89-9`, `minfin-ep`, `loi60-30`, `loi2017-66-lf2018` — references.json du livre.
- `loi-irpp-is-1989` — references.json RACINE (`precis/fr/references.json`).

### À créer (proposées)
```json
[
  {
    "id": "loi2016-48",
    "type": "legislation",
    "title": "Loi n°2016-48 du 11 juillet 2016, relative aux banques et aux établissements financiers",
    "note": "citation-key: loi2016-48 | JORT n°58 de 2016. Texte-cadre en vigueur de la profession bancaire (succède à la loi 2001-65 et à la loi 67-51). Intitulé FR attesté par le décret d'application 2020-113.",
    "URL": "https://www.pist.tn/jort/2016/2016F/Jo0582016.pdf",
    "issued": {"date-parts": [[2016, 7, 11]]}
  },
  {
    "id": "cc-banques-2014",
    "type": "legislation",
    "title": "Arrêté du ministre des affaires sociales du 17 février 2014, portant agrément de la convention collective sectorielle du personnel des banques et des établissements financiers (révisée)",
    "note": "citation-key: cc-banques-2014 | JORT n°23 de 2014. Convention sectorielle couvrant banques publiques ET privées ; socle conventionnel de la rémunération bancaire. Convention initiale agréée en 1975 (JORT n°87/1975, texte JORT n°6/1976) ; avenants jusqu'à l'avenant n°5 (arrêté du 17 nov. 2022, JORT n°126/2022).",
    "URL": "https://www.pist.tn/jort/2014/2014F/Jo0232014.pdf",
    "issued": {"date-parts": [[2014, 2, 17]]}
  },
  {
    "id": "decret2015-2217",
    "type": "legislation",
    "title": "Décret n°2015-2217 du 11 décembre 2015, fixant les taux des éléments de rémunération des chefs d'établissements et entreprises publiques et de sociétés à majorité publique",
    "note": "citation-key: decret2015-2217 | JORT n°101 de 2015. Texte en vigueur encadrant la rémunération des dirigeants d'entreprises publiques (y c. banques à majorité publique — à confirmer sur PDF). Succède aux décrets 78-885, 90-1855, 2014-12.",
    "URL": "https://www.pist.tn/jort/2015/2015F/Jo1012015.pdf",
    "issued": {"date-parts": [[2015, 12, 11]]}
  },
  {
    "id": "decret90-1855",
    "type": "legislation",
    "title": "Décret n°90-1855 du 10 novembre 1990, fixant le régime de rémunération des chefs d'entreprises à majorité publique",
    "note": "citation-key: decret90-1855 | JORT n°75 de 1990. Maillon central (1990-2014) de l'encadrement de la rémunération des dirigeants d'entreprises à majorité publique ; modifié par décrets 92-1 et 2006-2564 ; remplacé en 2014/2015.",
    "URL": "https://www.pist.tn/jort/1990/1990F/Jo07590.pdf",
    "issued": {"date-parts": [[1990, 11, 10]]}
  }
]
```
Optionnelles (à créer au besoin) : `loi92-24` (Code des assurances,
`https://www.pist.tn/jort/1992/1992F/Jo01792.pdf`) ; `loi67-51` / `loi2001-65` (lignée
historique de la loi bancaire) ; lois 57-15 / 59-47 (entrée historique de l'État au capital
STB/BNA) — à n'introduire que si le précis en a l'usage, en précisant qu'elles ne valent pas
part actuelle.

## 6. Notions à glossaire (precis/glossaire.yml)

`regime-marche-controle` existe déjà. À VÉRIFIER / éventuellement AJOUTER :
- **Entreprise publique financière** (banque/assurance/institution financière à capital
  public) — distinguée par l'activité, non par le périmètre actionnarial. Source [@loi89-9]
  + loi 2016-48.
- **Convention collective sectorielle des banques et établissements financiers** — instance
  de la notion `convention-collective-sectorielle` déjà au glossaire ; source canonique
  arrêté du 17 février 2014 (`cc-banques-2014`). Couvre public et privé.
- **Établissement de crédit / banque** — au sens de la loi 2016-48 (préciser si le précis
  veut une entrée). AR : مؤسسة قروض / بنك.
- **Rémunération des dirigeants d'entreprises publiques** — encadrée par décret
  (`decret2015-2217`) ; notion utile pour matérialiser le « contrôle » du marché contrôlé.

(Vérifier l'existant avant tout ajout : `convention-collective-sectorielle`,
`cnss`, `irpp`, `css`, `retenue-a-la-source`, `entreprises-publiques` existent déjà.)

## 7. TODO de vérification (lacunes — ne rien combler)

1. **Parts de capital public STB/BNA/BH** : NON sourcées sur document officiel daté. Lire
   les rapports annuels des banques (stb.com.tn, bna.tn, bh.com.tn) / actionnariat BVMT,
   citer par banque à une date de référence, présenter comme évolutif. LACUNE la plus
   sensible (ne pas écrire de pourcentage avant).
2. **Affirmation « rémunérations parmi les plus élevées du secteur public »** (stub l.5) :
   NON sourcée. Trouver une série officielle (INS « activités financières et d'assurance »,
   BCT) OU qualifier/retirer l'affirmation. LACUNE statistique principale.
3. **Structure fixe/variable de la rémunération bancaire** : OCR de la convention révisée
   2014 + avenants pour citer les articles (éléments permanents, part variable). Non fait.
4. **Champ exact du décret 2015-2217** : confirmer que les banques à majorité publique y
   sont incluses ; sourcer la circulaire d'application n°04 de 2021.
5. **CNSS — exhaustivité** : confirmer l'absence de tout régime de retraite spécial propre à
   une banque publique avant d'affirmer « CNSS sans exception » ; taux de cotisation exacts.
6. **Intitulé FR de la loi 2016-48** : notice de cache en arabe ; lire le PDF FR pist.tn
   pour figer l'intitulé exact (« relative aux banques et aux établissements financiers »
   très probable).
7. **Périmètre des institutions financières spécialisées / filiales** (caisses des dépôts,
   sociétés de leasing publiques, etc.) : non instruit ici ; à cadrer si le précis veut les
   intégrer au régime de marché contrôlé.

---

## 8. Banques et organismes financiers à participation publique — matière d'encadré (source officielle datée)

Cette section répond à la commande d'un **encadré** listant, sur source officielle, les
banques et organismes financiers à participation publique (sur le modèle de l'encadré
« liste CNRPS / décret 85-1025 » du régime conventionnel public).

### 8.0 CORRECTION à signaler au rédacteur (le chapitre dit le contraire de la source)
Le chapitre (ligne 15) et le cadrage B.3 affirment que les *Rapports sur les entreprises
publiques* « excluent banques et caisses de leur périmètre statistique » [@minfin-ep].
**La source primaire contredit cette affirmation.** Dans le *Rapport sur les entreprises
publiques* annexé à la LF 2021 (PDF lu, cf. §9) :
- le **Tableau 11** (échantillon de 33 EP) place STB, BNA, BH en positions 1-2-3, et
  CNSS, CNRPS, CNAM en positions 7-8-9 ;
- la **Deuxième partie, Chapitre premier** s'intitule « Les entreprises publiques actives
  dans le secteur financier et assimilé » (p. 34-45), et le **Chapitre deux** « Les caisses
  sociales » (p. 45-53).
Le Rapport **inclut** donc explicitement banques et caisses ; il ne les exclut pas.
→ TODO rédacteur : retirer / reformuler la phrase de la ligne 15. La logique de fond du
chapitre (CNSS et non CNRPS via décret 85-1025 ; convention de droit commun) tient par
ailleurs ; seule cette phrase d'appui est fausse.

### 8.1 Source canonique de l'encadré
**Rapport sur les entreprises publiques**, annexe 9 au projet de loi de finances, Ministère
de l'économie, des finances et de l'appui à l'investissement (clé `minfin-ep`, consolidée au
§9). Base légale : loi organique du budget n°2019-15 du 13 février 2019, art. 46.
Édition retenue pour les chiffres d'actionnariat : **LF 2021** (données 2017-2019).
PDF téléchargé : `biblio_pdfs/minfin_rapport_entreprises_publiques_lf2021.pdf`.

> Le Rapport énonce textuellement (p. 34) : « L'État participe au capital de plusieurs
> entreprises actives dans le secteur financier dont les plus importantes sont les trois
> grandes banques publiques : la Société Tunisienne de la Banque, la BH Bank et la Banque
> Nationale Agricole, en plus de la Poste Tunisienne et de la caisse des Prêt et de Soutien
> des Collectivités Locales. »

### 8.2 Entités à participation publique attestées par le Rapport (avec %, source officielle)
Les pourcentages ci-dessous sont **« participation de l'État ET des actionnaires publics »**
à une **date de référence (fin 2019)**, tels qu'énoncés par le Rapport. Ils sont donc
**sourçables et citables** (≠ chiffres de presse écartés ailleurs dans cette note). Ils sont
**évolutifs** (recapitalisations) : toujours les présenter à leur date.

| Entité | Nature | Participation publique (État + actionnaires publics) | Source (Rapport LF2021) |
|---|---|---|---|
| Société Tunisienne de Banque (STB) | Banque (SA, créée 18 janv. 1957, capital 776,9 MD) | **83,3 %** (majoritaire) | p. 35 |
| Banque Nationale Agricole (BNA) | Banque (SA, créée 31 mai 1959, capital 320 MD fin 2019) | **50,23 %** (majoritaire) | p. 37 |
| BH Bank (ex-Banque de l'Habitat) | Banque (SA, fondée 1974 comme fonds national d'épargne-logement, transformée en banque 1989) | **55,6 %** (majoritaire) | p. 38 |
| Poste Tunisienne / Office National des Postes (ONP) | Établissement public à caractère non administratif exerçant des activités financières (CCP, comptes d'épargne, change) | 100 % public (EPNA, décret 98-1305) | p. 41 |
| Caisse des Prêts et de Soutien des Collectivités Locales (CPSCL) | Établissement public à caractère non administratif — financement des collectivités locales (créée par loi 75-37 du 14 mai 1975) | 100 % public (EPNA) | p. 43 |

Notes :
- Les **trois banques** (STB, BNA, BH) sont à participation publique **majoritaire** — la
  source le dit explicitement et chiffré. C'est exactement le noyau de l'encadré.
- **ONP et CPSCL** sont des **EPNA** (établissements publics à caractère non administratif),
  donc intégralement publics par construction ; le Rapport les classe dans le « secteur
  financier et assimilé ». À mentionner si l'encadré veut couvrir les organismes financiers
  au-delà des banques stricto sensu.
- Évolution sourcée (respecte l'invariant « pas de chiffre ponctuel sans évolution ») : le
  capital de la **BNA** est passé de **176 MD (2018) à 320 MD (fin 2019)** par conversion de
  créances de l'État (art. 28 de la loi 2018-56 du 27 déc. 2018) [Rapport LF2021, p. 37] ;
  recapitalisations **STB et BH** de 2015 (mentionnées en B.2 / contexte). Le Rapport est
  publié annuellement (éditions LF2020 et LF2021 téléchargées, cf. §9) : un encadré peut
  ainsi citer la part à une date et renvoyer à l'édition suivante pour l'actualisation.

### 8.3 Classification d'appui (liste BCT des établissements agréés)
Pour situer ces entités dans le système financier, la BCT publie un organigramme officiel :
**« Structure du système financier tunisien »** (banques résidentes : 23 ; établissements
financiers : 12, dont leasing : 8 et factoring : 2 ; banques d'affaires : 2 ; banques à
statut particulier : 7 ; banques non résidentes : 7). PDF BCT (hôte joignable) :
`https://www.bct.gov.tn/bct/siteprod/documents/STRUCTURE_FR.pdf` (téléchargé ; 55 p.).
ATTENTION : ce document est un **annuaire**, il **n'indique PAS la nature publique/privée**
de l'actionnariat. Il sert uniquement à la classification (banque / leasing / factoring /
banque d'affaires) et à l'exhaustivité de la liste des agréés. Ne pas en déduire un statut
de propriété.

### 8.4 Autres banques à participation publique — liste PARTIELLE / lacune
Le Rapport ne couvre que les EP les plus importantes (échantillon de 33 EP ≈ 90 % des
indicateurs financiers, sur 110 EP au total — Rapport LF2021, introduction p. 4). Il ne
détaille donc **pas** les banques publiques spécialisées et co-entreprises où l'État détient
une participation :
- **Banque Tunisienne de Solidarité (BTS)**, **Banque de Financement des PME (BFPME)** :
  banques publiques spécialisées (microcrédit / financement PME).
- **Banque de Tunisie et des Émirats (BTE)**, **Banque Tuniso-Libyenne (BTL)**, **Tunisian
  Saudi Bank (TSB)** : banques mixtes à participation de l'État tunisien et d'États tiers.
Ces participations sont attestées par leurs **textes de création / conventions au JORT**
(à sourcer une à une sur pist.tn) ou par les rapports annuels des banques ; elles **ne sont
pas chiffrées ici** (aucun % inventé). 
→ TODO : si l'encadré veut être exhaustif, sourcer chaque entité par son texte fondateur
JORT (pist.tn). Tel quel, l'encadré sourcé = les **5 entités du §8.2** (les seules attestées
%/nominativement par le Rapport) ; le **manque** = l'univers exhaustif des organismes
financiers à participation publique (banques spécialisées et mixtes ci-dessus).
NB méthodo : la répartition « public/privé » produite par un résumé automatique de la liste
des banques de finances.gov.tn n'est PAS une affirmation de la source ; ne pas la citer.

## 9. Consolidation de la référence `minfin-ep` (Tâche 2)

`minfin-ep` pointait vers `https://www.finances.gov.tn/` (page d'accueil, non localisable) —
référence faible. **Proposition de remplacement par une édition précise, datée, téléchargée.**

### 9.1 Édition retenue et joignabilité
- Le *Rapport sur les entreprises publiques* est l'**annexe 9** au projet de loi de finances.
- **Hôte primaire = gbo.tn** : la consigne le signalait injoignable, mais il **répond bien
  via la sandbox réseau de l'outil Bash** (HTTP 200 ; le refus port 443 ne concernait que
  WebFetch). Les PDF ont donc pu être **téléchargés** :
  - LF 2021 : `http://www.gbo.tn/sites/default/files/2021-04/Annexe%209%20LF2021%20Entreprises%20Publiques.pdf`
    → `biblio_pdfs/minfin_rapport_entreprises_publiques_lf2021.pdf` (179 p., données 2017-2019).
  - LF 2020 : `http://www.gbo.tn/sites/default/files/2021-02/Annexe_9_LF2020-Entreprises_publiques.pdf`
    → `biblio_pdfs/minfin_rapport_entreprises_publiques_lf2020.pdf` (159 p., données 2016-2018).
- **Hôte alternatif joignable (humain)** : page document du Ministère des finances
  `https://www.finances.gov.tn/fr/document/le-rapport-sur-les-entreprises-publiques-ar`
  (HTTP 200 ; version arabe / traduction FR en cours). À garder comme landing page stable
  si gbo.tn venait à tomber.

### 9.2 Entrée CSL-JSON proposée (FR) — remplace l'entrée faible
```json
{
  "id": "minfin-ep",
  "type": "report",
  "title": "Rapport sur les entreprises publiques (annexe 9 au projet de loi de finances pour 2021)",
  "author": [{ "literal": "Ministère de l'économie, des finances et de l'appui à l'investissement, Tunisie" }],
  "publisher": "Ministère de l'économie, des finances et de l'appui à l'investissement, Tunisie",
  "publisher-place": "Tunis",
  "note": "citation-key: minfin-ep | Annexe 9 au PLF 2021 (loi organique du budget 2019-15, art. 46). Échantillon de 33 entreprises publiques (~90 % des indicateurs ; 110 EP au total), données 2017-2019. Deuxième partie, ch. 1 « entreprises publiques actives dans le secteur financier et assimilé » (STB, BNA, BH, Poste, CPSCL) ; ch. 2 « caisses sociales » (CNSS, CNRPS, CNAM). PDF téléchargé : biblio_pdfs/minfin_rapport_entreprises_publiques_lf2021.pdf. Alternative landing page joignable : https://www.finances.gov.tn/fr/document/le-rapport-sur-les-entreprises-publiques-ar . La version arabe fait foi (traduction FR Expertise France/UE).",
  "URL": "http://www.gbo.tn/sites/default/files/2021-04/Annexe%209%20LF2021%20Entreprises%20Publiques.pdf",
  "issued": { "date-parts": [[2020]] }
}
```
NB sur `issued` : le Rapport accompagne le **PLF 2021** (préparé fin 2020 ; il cite la
circulaire du 14 mai 2020 ; ses données courent jusqu'à 2019). Année posée = **2020** (année
de préparation/publication de l'annexe au PLF 2021) ; le champ `note` précise « annexe au
PLF 2021 » et la période de données 2017-2019 pour lever toute ambiguïté.

### 9.3 Entrée AR (references.json arabe) — version arabe officielle (fait foi)
Même `id`/`URL`/`issued`. Titre arabe :
```json
{
  "id": "minfin-ep",
  "type": "report",
  "title": "تقرير حول المؤسسات العمومية (الملحق 9 لمشروع قانون المالية لسنة 2021)",
  "author": [{ "literal": "وزارة الاقتصاد والمالية ودعم الاستثمار، تونس" }],
  "publisher": "وزارة الاقتصاد والمالية ودعم الاستثمار، تونس",
  "publisher-place": "تونس",
  "note": "citation-key: minfin-ep | الملحق 9 لمشروع قانون المالية 2021. النسخة العربية هي المرجع. تحميل محلي: biblio_pdfs/minfin_rapport_entreprises_publiques_lf2021.pdf",
  "URL": "http://www.gbo.tn/sites/default/files/2021-04/Annexe%209%20LF2021%20Entreprises%20Publiques.pdf",
  "issued": { "date-parts": [[2020]] }
}
```

### 9.4 Clé alternative (édition antérieure, pour une vue d'évolution)
Si le précis veut une **série** (invariant « pas de chiffre ponctuel sans évolution »), créer
une clé `minfin-ep-2020` pour l'édition LF 2020 (données 2016-2018), PDF
`biblio_pdfs/minfin_rapport_entreprises_publiques_lf2020.pdf`, URL gbo
`http://www.gbo.tn/sites/default/files/2021-02/Annexe_9_LF2020-Entreprises_publiques.pdf`.
TODO : repérer une édition plus récente (LF 2022+) — les chemins gbo testés (patterns
`Annexe 9 LF20XX`) renvoient 404 ; l'index gbo.tn/fr/Loi-de-Finance-et-rapports-annexes liste
les URL exactes (à parcourir hors WebFetch, qui refuse l'hôte).

### 9.5 PDF déposés dans `biblio_pdfs/` (durables)
- `biblio_pdfs/minfin_rapport_entreprises_publiques_lf2021.pdf` (édition retenue pour `minfin-ep`)
- `biblio_pdfs/minfin_rapport_entreprises_publiques_lf2020.pdf` (édition antérieure, série)

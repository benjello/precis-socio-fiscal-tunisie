# Note documentaire — Rapports et études : le *Livre blanc* transports et logistique (Banque mondiale, 2016)

Documentaliste, 10 novembre 2026. Mission R2 du chantier « Livre transport » (volet Banque
mondiale du chapitre « Rapports et études », plan § 3). Chantier d'instruction : aucun `.qmd`,
aucun commit. **Le français est la source de vérité.** Toute étude est relevée avec SA MÉTHODE
(auteur, années de données, périmètre, mode de calcul, page), et le budgétaire n'est pas mêlé
aux évaluations (`docs/conventions-redaction.md` § 3).

## 0. Où est le PDF (exploité, pas réinventé)

Le PDF est **déjà rangé dans l'entrepôt `tunisia-data`**, lu à l'image pour cette note :
`data/raw/banque-mondiale-rapports/bm_2016_livre_blanc_transports_logistique_ACS18045.pdf`
(hors git ; 92 p. ; SHA-256 `9a683dd933cbcfd85d3503b1b417e9a63e1b9b6da45c863020981f1f19092771`).
Catalogue : `sources/banque-mondiale-rapports-urls.csv`, ligne `bm_2016_livre_blanc_…ACS18045.pdf`
(URL d'origine `https://documents1.worldbank.org/curated/en/339961488471609720/pdf/ACS18045-REVISED-PUBLIC.pdf`,
consulté le 11/10/2026). Les tableaux de trafic et de comptes de l'annexe sont déjà transcrits et
versés (`sources/transport-trafic-comptes.md` § 1 ; série `bm-livre-blanc-2016-transport-trafic-comptes`).
Pagination : page du PDF = page imprimée + 1 (couverture). Les numéros ci-dessous sont les
**pages imprimées** sauf mention.

## 1. Intitulé exact, auteur, série, année

- **Intitulé exact** : *République tunisienne — Livre Blanc relatif au secteur des transports et
  de la logistique*.
- **Numéro de rapport / série** : **n° ACS18045**, unité GTI05, région Moyen-Orient et Afrique
  du Nord.
- **Auteur / producteur** : **Banque mondiale** (préface de la représentante Eileen Murray ;
  préface du ministre du Transport Anis Ghedira — rapport co-porté avec le ministère du
  Transport).
- **Date** : **18 mai 2016**.
- **Nature** : document « essentiellement stratégique » — identifie les priorités du secteur et
  **recommande** des réformes au gouvernement pour la décennie ; se veut complément du
  **XIIIe Plan quinquennal 2016-2020** (p. 8, § ii-iii ; résumé).

## 2. MÉTHODE (données mobilisées, années, mode de calcul)

- **Nature de la source** : rapport extérieur **de synthèse**, pas une évaluation économétrique
  propre. Le contenu et les recommandations sont « basé[s] essentiellement sur la revue détaillée
  des nombreuses études et rapports publiés au cours de ces dix dernières années », complétés par
  une mission en Tunisie en **octobre 2015** et un séminaire thématique à Tunis en **février 2016**
  (séminaire de restitution du 12 février 2016, annexe 3) ; le ministère du Transport a fourni
  données et analyses (p. 8, § i).
- **Mode de calcul des indicateurs** : la Banque **reprend des indicateurs et tableaux de tiers**,
  sans recalcul : indices internationaux de perception (LPI de la Banque mondiale, piliers
  infrastructure du *Global Competitiveness Report* du Forum économique mondial, LSCI de la
  CNUCED, statistiques OMS), et tableaux de trafic et de comptes fournis par les opérateurs
  (Transtu, SNCFT, SNTRI) et par SYSTRA. Elle **ne définit ni les catégories de trafic ni le mode
  de comptage** ; pour les comptes des sociétés, elle signale elle-même des tableaux « à mettre à
  jour » (p. 30). État qualitatif de ces chiffres : « non qualifié » (`transport-trafic-comptes.md`).
- **Sources déclarées, par bloc** (annexe 2, p. 88) : WEF *Global Competitiveness Report*
  2014-15 et 2015-16 ; Banque mondiale LPI 2014 et *Doing Business* ; OMS *Global Status Report*
  2013 ; CNUCED LSCI 2014 ; rapports annuels 2014 de l'OMMP, de la SNCFT et de Transtu ;
  SYSTRA 2012 ; Comete Engineering 2014 (productivité du port de Radès) ; CODATU 2012 ;
  Plan bleu / GEF 2014 ; *Annuaire statistique de la Tunisie 2008-2012* (INS, 2013) ; BAD
  (stratégie sécurité routière 2013) ; BEI 2015 ; *Livre blanc sur les transports* de l'UE (2011).
- **Attention (classement par famille)** : les grandeurs budgétaires et les comptes d'opérateurs
  cités ici relèvent de la **famille « opérateurs / rapport extérieur »** et **ne se raccordent ni
  ne se mêlent** aux séries budgétaires du ministère des Finances (voir `transport-trafic-comptes.md`
  § « Pourquoi les deux fichiers ne se raccordent pas » : 2015 et 2016 manquants, catégories
  différentes). Ne pas chaîner avec `minfin-transferts-transport`.

## 3. CONSTATS STRUCTURANTS (diagnostic — état constaté, distinct des recommandations)

Chiffres donnés avec leur année et leur périmètre ; ce sont les **constats du rapport**, non un
état du droit.

- **Poids du secteur** : le transport et la logistique représentent **≈ 7 % du PIB en 2014**
  (p. 3, préface ; repris p. 15, § 5) et emploient **≈ 140 000 personnes, dont ≈ 40 000 dans le
  secteur public** (préface, p. 3).
- **Investissement** : sur **2010-2014**, le secteur a porté **≈ 6 500 MD d'investissement**, soit
  **≈ 11 % de l'investissement tous secteurs** ; **près d'un tiers réalisé par le privé** (préface,
  p. 3). [Chiffres de la préface du ministre, non recalculés par la Banque.]
- **Six thèmes majeurs** identifiés (p. 8, § iv ; annexe 1) : (i) performance **logistique
  dégradée** sur les trois dernières années ; (ii) **système portuaire inadéquat** (capacité,
  efficacité) et flotte maritime insuffisante ; (iii) **services de transport public de qualité
  médiocre**, en particulier dans le Grand Tunis ; (iv) **performance médiocre des entreprises
  publiques** de transport, en **déficit financier chronique** ; (v) **sécurité routière**
  insatisfaisante ; (vi) besoin d'une politique de réduction de l'empreinte carbone.
- **Performance logistique (perception, classements mondiaux, 2015 ; 144 pays)** : Tunisie au
  **110e rang au LPI**, 90e pour l'infrastructure globale, 89e qualité des routes, 92e qualité des
  infrastructures portuaires, 102e au LSCI 2014, 87e transport aérien, 67e ferroviaire — **retard
  marqué** derrière Maroc et Jordanie (table 3, p. 21, WEF 2015-16). Diagnostic confirmé par
  *Africa Doing Business 2015* (p. 21-22).
- **Port de Radès (constats 2010-2015)** : principal portail conteneurisé (**≈ 90 % du trafic
  national** dans les années 2000) ; **crise depuis 2010**, aggravée en 2011-2014 (gouvernance,
  ressources humaines) ; productivité **9 conteneurs/heure/engin** début 2015 contre **13 imposés**
  par la concession STAM ; fonctionnement en **3 shifts de 6 h (18 h/jour)** contre 24 h ailleurs ;
  attente navires en rade de **3 à 4 jours en mars 2015** (p. 25, § 30-32). La STAM, concessionnaire
  (concession de 30 ans accordée en **2005**, note 16), a opéré **77 % du trafic conteneurisé**
  (p. 24). Trafic conteneurs **467 000 EVP en 2014** (+1 % sur 2013 : 464 000) ; conteneurs
  manipulés par la STAM **360 001 EVP en 2014**, sous le niveau de 2009 (410 907) et le record de
  2010 (447 071) (p. 24, annexe B).
- **Coûts (évaluation d'ordre de grandeur)** : un gain pouvant **atteindre 600 USD/conteneur**
  serait réalisable en stabilisant les cadences (13-15 mouvements/grue/h), portant le tirant d'eau
  à -10,75/-11 m et réduisant les délais de séjour (p. 25, § 33). Une « évaluation succincte » de
  la composante maritime conteneurs révèle des **surcoûts importants** supportés par l'économie du
  fait de l'inadéquation portuaire (p. 61-62, annexe B).
- **Entreprises publiques de transport** : situation financière **« alarmante »** des trois
  principales sociétés, dans un contexte de **non-révision des tarifs depuis 2010** et de hausse
  des coûts (p. 30, § 41). Comptes versés (milliers de dinars ; source : rapports annuels des
  sociétés / SYSTRA 2012) : **STT (Transtu)** résultat net **−125 458 en 2013, −52 218 en 2014**,
  les recettes 2014 ne couvrant pas la seule masse salariale (produits 184 232 < charges de
  personnel 186 073) ; **SNTRI** résultat net **−11 597 en 2013, −10 587 en 2014** ; **SNCFT**
  résultat net d'exploitation **−60 627 en 2013, −58 766 en 2014** (p. 30). Le rapport parle d'un
  « cercle vicieux » de gouvernance et de l'absence de réforme d'ensemble depuis les années 1990
  (p. 29-30, § 39), s'appuyant sur le *Rapport sur la gouvernance des entreprises publiques en
  Tunisie* (Banque mondiale, 2014, note 22).
- **Ferroviaire** : part du fret ferroviaire effondrée (recettes fret SNCFT **64 774** en 2010 →
  **31 542** milliers de dinars en 2013), part des phosphates « à peine 20 % en 2013 » affectée par
  les relations contractuelles SNCFT-CPG (p. 30 et p. 46, § 66).
- **Sécurité routière** : **9 351 accidents en 2012** (ramenés à 5 538 en 2014 selon l'Intérieur,
  note 24) ; **1 208 décès rapportés en 2010** (OMS en estime 1 974) ; **≈ 140 décès/million
  d'habitants en 2012** ; **coût pour l'économie estimé à 4,5 % du PIB** (p. 31-32, § 43-44 ;
  source du 4,5 % : document de projet *Transport Corridors*, Banque mondiale, juin 2015, note 25 ;
  tableau OMS 2013, p. 32).

## 4. RECOMMANDATIONS (présentées comme telles, jamais comme état du droit)

Le rapport propose **10 actions** et une **matrice de réformes** (section IV-V, p. 39-50). Points
saillants (p. 8-9, § v) : rehausser la logistique via le futur **Plan national directeur des
transports (PNDT)** ; réactiver le suivi de performance de tous les ports, impliquer davantage le
privé dans le financement portuaire ; exiger des entreprises publiques sous tutelle un rapport
d'activité 2015 et des plans de retour au niveau de performance de 2010 ; **« revisiter et mettre
en œuvre la loi de 2004 sur les transports terrestres »** (loi n° 2004-33) ; plan de sécurité
routière porté au plus haut niveau de l'État ; **transfert modal route → rail** (voyageurs,
phosphates, conteneurs) ; décider du mode de réalisation de l'extension du port de Radès et du
port en eaux profondes d'Enfidha (trois options, p. 46, § 67). Ce sont des **recommandations de
2016**, à ne pas confondre avec le droit en vigueur.

## 5. Voisin, à ne pas confondre : le *Tunisia Infrastructure Diagnostic* (Banque mondiale, 2019)

Document voisin déjà rangé (`tunisia-data/sources/bm-infrastructure-diagnostic-2019.md`,
clé CSL existante `wb-infra-diagnostic-2019`). **Même émetteur, périmètre partiellement commun
(entreprises publiques de transport : SNCFT, TRANSTU, OMMP, OACA, Tunisair), MÉTHODE et années
différentes** — à tenir distinct :
- **2019 (décembre)**, 81 p. ; périmètre = **9 entreprises publiques d'infrastructure** (dont
  STEG, SONEDE, ONAS — au-delà du seul transport) ; unité = millions de dinars ; **comptes
  2009-2017** d'après les rapports annuels et états financiers des entreprises ; chiffres déclarés
  « approximatifs » ; subventions d'exploitation 2009-2017 (tableau 1.4), dette 2009-2017
  (fig. 1.6), garanties/rétrocessions/prêts du Trésor **14 % du PIB en 2016** (p. 8).
- Le *Livre blanc* 2016 est **antérieur, de portée sectorielle « transport et logistique »** et
  **stratégique** (recommandations), là où le diagnostic 2019 est **financier et transversal aux
  infrastructures**. Ne pas chaîner leurs chiffres d'entreprises : périmètres et éditions
  distincts.

## 6. Références candidates (CSL-JSON)

**À créer** (aucune entrée `ACS18045` / *Livre blanc* 2016 trouvée dans les `references.json` du
précis ; clé suggérée `wb-livre-blanc-transport-2016`, cohérente avec `wb-infra-diagnostic-2019`
et `wb-tunisia-gouvernance-ep-2014` déjà présentes dans `precis/fr/entreprises_publiques/`) :

```json
{
  "id": "wb-livre-blanc-transport-2016",
  "type": "report",
  "title": "République tunisienne — Livre Blanc relatif au secteur des transports et de la logistique",
  "title-short": "Banque mondiale, Livre blanc transports et logistique, 2016",
  "author": [{ "literal": "Banque mondiale" }],
  "publisher": "Banque mondiale",
  "publisher-place": "Washington, D.C.",
  "number": "ACS18045",
  "issued": { "date-parts": [[2016, 5, 18]] },
  "URL": "https://documents1.worldbank.org/curated/en/339961488471609720/pdf/ACS18045-REVISED-PUBLIC.pdf",
  "accessed": { "date-parts": [[2026, 10, 11]] },
  "note": "citation-key: wb-livre-blanc-transport-2016\n92 pages. Rapport de synthèse stratégique co-porté avec le ministère du Transport (préface A. Ghedira), fondé sur la revue d'études 2005-2015, une mission d'octobre 2015 et un séminaire du 12 février 2016. Pages imprimées = page PDF − 1. Secteur ≈ 7 % du PIB et ≈ 140 000 emplois (dont ≈ 40 000 publics) en 2014, p. 3 ; LPI 110e / 144 (table 3, p. 21) ; port de Radès 9 conteneurs/h/engin vs 13 imposés, concession STAM de 2005, p. 25 ; comptes Transtu/SNTRI/SNCFT 2007-2014, p. 30 ; sécurité routière coût ≈ 4,5 % du PIB, p. 31-32. Tableaux de trafic/comptes transcrits : tunisia-data, bm-livre-blanc-2016-transport-trafic-comptes. PDF : tunisia-data data/raw/banque-mondiale-rapports/, SHA-256 9a683dd933cbcfd85d3503b1b417e9a63e1b9b6da45c863020981f1f19092771. Consulté le 11/10/2026."
}
```

**Déjà présentes, à réutiliser (ne pas recréer)** :
- `wb-infra-diagnostic-2019` — *Tunisia Infrastructure Diagnostic*, 2019 (voisin, § 5),
  `precis/fr/entreprises_publiques/references.json`.
- `wb-tunisia-gouvernance-ep-2014` — *Gouvernance des entreprises publiques en Tunisie*, 2014
  (source citée par le Livre blanc, note 22), même fichier.

## 7. Notions à glossaire (à vérifier/ajouter par le rôle habilité — je ne touche pas `glossaire.yml`)

- **LPI — Indice de performance logistique** (*Logistics Performance Index*), Banque mondiale :
  indice de perception, classement mondial. Source canonique : LPI de la Banque mondiale.
- **LSCI — Indice de connectivité des transports maritimes réguliers** (*Liner Shipping
  Connectivity Index*), CNUCED.
- **EVP — Équivalent vingt pieds** (unité de mesure du trafic conteneurisé).
- **Plan national directeur des transports (PNDT/PNDT)** : instrument de planification visé par
  le Livre blanc (à distinguer du Plan quinquennal).
- **Transfert modal** (route → rail) : notion de politique des transports mobilisée par le rapport.
- **Feedering** : desserte portuaire par navires de petit tonnage (défini note 17 du rapport).
Vérifier d'abord si « concession autoroutière »/« contrat-programme » du secteur sont déjà au
glossaire (entrées « compensation du transport », « Tunisie Autoroutes » signalées existantes).

## 8. Lacunes (TODO — ne rien inventer)

- **Chiffres de la préface (7 % PIB, 140 000 emplois, 6 500 MD / 11 % / un tiers privé, 2010-2014)** :
  donnés par le ministre, **sans tableau ni source primaire** dans le rapport. À recouper, pour
  emploi dans le livre, avec une source primaire (comptes nationaux INS, annexe d'investissement
  au budget) avant toute affirmation chiffrée. Non résolu ici.
- **Coût logistique en % du PIB** : le Livre blanc **ne donne pas de chiffre de coût logistique
  agrégé** (contrairement à ce que la mission supposait) ; il parle de « surcoûts importants » non
  quantifiés et d'un gain unitaire « jusqu'à 600 USD/conteneur ». Le seul coût chiffré en % du PIB
  est celui de l'**insécurité routière (4,5 %)**, lui-même repris d'un document de projet *Transport
  Corridors* (BM, juin 2015) — **document source non collecté dans l'entrepôt** (à chercher si le
  chiffre est mobilisé).
- **Documents cités en annexe 2 non détenus** (ex. SYSTRA 2012 ; Comete Engineering 2014,
  productivité de Radès ; *Transport Corridors* 2015) : à chercher si le livre en a besoin de
  première main ; pour l'heure cités de seconde main par le Livre blanc, donc **non exploitables
  comme sources primaires**.
- **Pas d'évaluation économique propre** dans ce rapport (perception + comptes repris) : la demande
  d'une fiche `eco-*` d'incidence du poste transport reste ouverte (cf. plan § 3, note du
  11 octobre 2026).

## 9. Recherches infructueuses

Aucune fiche `docs/recherches.yml` ouverte ou nécessaire : l'objet de la mission (le PDF du Livre
blanc 2016) **a été retrouvé et exploité** dans l'entrepôt. Les documents de seconde main du § 8
ne relèvent pas d'une recherche de texte juridique rejouable ; si le livre les requiert, ouvrir
alors une chasse ciblée (hors périmètre de ce chantier d'instruction, qui n'écrit pas dans
`recherches.yml`).

# Fiche de plan — un volume sectoriel « L'agriculture » ?

Rôle : architecte. Date : 10 novembre 2026. Statut : **instruction d'arbitrage**, pas un plan
approuvé — l'agriculture n'est pas dans la doctrine. Le tableau des six parties de
`docs/conventions-redaction.md`, § 4, liste pour la partie IV : « la santé ; la compensation ;
l'éducation ; plus tard le transport, le logement, l'environnement ». Pas l'agriculture. Ouvrir ce
volume suppose donc une décision du propriétaire qui amende la doctrine, quel que soit le choix
retenu ci-dessous.

Aucune rupture n'est affirmée dans cette fiche ; les textes y sont cités comme candidats à
lecture, par leur intitulé quand ils ne sont pas lus dans le précis. Aucune valeur, date ou URL
n'y figure qui ne soit lue dans le dépôt ou dans le catalogue `tunisia-data/sources/`.

## 1. L'arbitrage

### Les trois options

**(a) Un livre sectoriel plein** : « L'agriculture » reçoit tout l'agricole — retraites et
cotisations des régimes agricoles, SMAG, prix des céréales, offices, BNA, fiscalité agricole.

**(b) Pas de livre** : chaque sujet agricole reste ou entre dans un livre existant ; l'agriculture
n'est qu'une étiquette transversale.

**(c) Un livre resserré** : « L'agriculture » ne reçoit que les dispositifs de soutien au
*producteur* agricole qui n'ont de domicile dans aucun livre existant, et renvoie partout
ailleurs.

### Ce que montre l'inventaire (grep du 10 novembre 2026 sur `precis/fr/`)

L'essentiel de l'agricole **a déjà un domicile**, conforme à la règle du § 4 (« un cas d'un
instrument général vit dans le livre de l'instrument ») :

- **Retraites** : régime des salariés agricoles (loi n° 81-6, lue), régime agricole amélioré
  (loi n° 89-73), non-salariés agricoles (décrets n° 82-1360 et 95-1166), travailleuses agricoles
  (décret-loi n° 2024-4, lu) — tout le livre des retraites, sections `#sec-agricoles`, glossaire.
- **Cotisations sociales et caisses** : assiettes et taux des régimes agricoles, fonds de
  protection sociale des travailleuses agricoles (`#sec-cot-travailleuses-agricoles`), déficits
  structurels des régimes agricoles de la CNSS 1990-2004 (`caisses/_comptes_longue_periode.qmd`,
  lacune L10 : couverture des déficits non établie par un texte).
- **Prestations sociales** : risques professionnels des travailleuses agricoles
  (`#sec-ar-atmp-agricoles`).
- **Marché du travail** : le SMAG, de l'arrêté du 30 avril 1956 au décret pluriannuel n° 2026-66,
  chapitre du salaire minimum entier ; convention collective cadre agricole citée.
- **Fiscalité** : bénéfices de l'exploitation agricole et de pêche (catégorie III de l'IRPP,
  évaluation forfaitaire), déduction totale dix ans puis deux tiers (loi n° 2017-8) ; régimes
  d'incitation (titre « développement agricole » du code de 1993, primes APIA de la loi de
  l'investissement de 2016, catégorie « A », crédits budgétaires relevés 2018-2025) ; taxes du
  fonds de développement de la compétitivité dans le secteur de l'agriculture et de la pêche
  (`#sec-fst-agriculture`, né en 1995).
- **Compensation** : subventions aux céréales, huiles, lait, sucre — cœur historique de la Caisse
  générale depuis 1974-1975 ; engrais dans les charges des années 1980 ; prélèvements à
  l'importation (poudre de lait, viandes, beurre) au profit de la Caisse. Le chapitre « les
  produits de base, prix à la consommation et à la production » est **déjà à écrire** dans ce
  livre (`docs/notes/chantier-decoupage-livres.md`, « Plus tard » et arborescence cible).
- **Entreprises publiques** : Office des céréales (décret-loi n° 62-10, lu ; décrets de campagne,
  récoltes 2010-2026, avec prix de base à la production et prix de rétrocession), ONH, OTD,
  BNA (`#sec-ep-ge-bna` : comptes spéciaux agricoles transférés en 1994 et 2004, garanties,
  obligation de financement agricole de la loi de finances pour 2026, art. 89).
- **Informel** : couverture sociale des salariés et indépendants agricoles (thèse Ben Cheikh).

**Ce qui n'a aucun domicile aujourd'hui** — vérifié par grep (`FOSDAP`, `FODECAP`,
`vulgarisation`, `périmètres irrigués`, `eau d'irrigation`, `calamité`) :

1. **Le crédit agricole bonifié et les abandons de créances aux agriculteurs.** Le précis ne les
   traite que par la bande : la BNA (entreprises publiques) porte les comptes spéciaux agricoles
   et, depuis 2026, l'obligation de financer l'agriculture à taux préférentiels ; la bonification
   des crédits saisonniers aux céréaliculteurs (loi de finances pour 2023, art. 15) n'est citée
   que dans un TODO de `_offices.qmd`, « sans lien avec l'Office ». Le dispositif vu du
   *bénéficiaire* — qui est bonifié, à quel taux, quelles remises de dettes — n'est écrit nulle
   part.
2. **L'assurance et les calamités agricoles.** Le « fonds d'indemnisation des dommages agricoles
   causés par les calamités naturelles » n'apparaît qu'incidemment, comme destinataire de
   l'amende de la BNA (loi de finances pour 2026, art. 89) ; son texte fondateur n'est ni
   identifié ni lu dans le précis.
3. **Les périmètres irrigués et le tarif de l'eau d'irrigation.** Les offices de mise en valeur
   des périmètres irrigués n'apparaissent que dans la liste du régime conventionnel des
   rémunérations publiques ; aucun chapitre ne traite le tarif de l'eau d'irrigation — un prix
   administré, que la règle de domicile enverrait à la compensation, mais que la compensation ne
   couvre pas (la SONEDE, eau potable, est aux entreprises publiques).
4. **Les subventions aux intrants** (engrais, semences hors stock stratégique de l'Office,
   aliments du bétail) : les engrais figurent dans les charges historiques de la Caisse de
   compensation (rapport BCT 1974, tableaux Banque mondiale 1970-1984) puis s'effacent ; aucun
   suivi après les années 1980.
5. **La vulgarisation, la recherche et l'encadrement** (CRDA, centres techniques, groupements
   interprofessionnels) : rien, hors le financement par le fonds de compétitivité (fiscalité).
6. **Le budget du ministère de l'Agriculture** comme épine : les PAP/RAP de la mission
   Agriculture 2015-2025 sont acquis et catalogués dans `tunisia-data`
   (`sources/ministere-agriculture-tic-sante-finances.md`), mais aucun livre n'en fait une
   dépense de longue période.
7. **Le foncier agricole** (réforme agraire des périmètres publics irrigués, cession des terres
   domaniales — lois n° 70-25 et 72-36 citées non lues dans un TODO de `_offices.qmd`) : l'OTD
   est traité comme entreprise, pas la politique foncière.

Je n'ai trouvé **ni « FOSDAP » ni « FODECAP »** dans le précis. Le « fonds spécial de
développement de l'agriculture » est nommé une fois (`_regimes_incitation.qmd` : le décret de 2017
y impute les primes en attendant le Fonds tunisien de l'investissement), sans texte fondateur lu ;
un « fonds de développement agricole » est supprimé par la loi de finances pour 1995
(`_taxes_fonds_speciaux.qmd`). L'articulation entre ces fonds est à établir par le
documentaliste — ce sont peut-être le même, peut-être trois.

### Recommandation : l'option (c), conditionnée

**Un livre resserré « L'agriculture — le soutien au producteur »**, et pas avant que deux
préalables soient levés.

Pourquoi pas (a) : un livre plein viderait quatre livres existants de chapitres déjà écrits et
relus (régimes agricoles des retraites, SMAG, offices, prix des produits de base), à rebours de
la règle de domicile — un cas d'un instrument général vit dans le livre de l'instrument. Le coût
de migration serait massif pour un gain de lecture nul : le lecteur des retraites veut tous les
régimes ensemble.

Pourquoi pas (b) : les sept sujets sans domicile ci-dessus ne se laissent pas ranger. La
bonification de crédit n'est ni un prix, ni une prestation, ni un prélèvement, ni le statut d'une
entreprise ; l'assurance-calamités non plus ; le tarif de l'eau d'irrigation irait à la
compensation par la lettre de la règle, mais il n'a rien à voir avec la Caisse générale et
gonflerait un livre déjà chargé. La dispersion laisserait ces dispositifs orphelins ou mal logés
— c'est l'état actuel, et il se lit dans les TODO.

Pourquoi (c) : les dispositifs sans domicile forment un objet cohérent — *ce que l'État verse,
prête, garantit ou abandonne au producteur agricole* — avec une épine budgétaire réelle (budget
de la mission Agriculture, primes d'investissement, bonifications, indemnisations), conforme au
principe des livres sectoriels (« leur épine est budgétaire plus que législative »). Le risque de
livre-coquille (§ 5) est réel mais borné : si l'instruction documentaire montre que la matière
tient en trois chapitres maigres, l'option (b) reste ouverte — on logerait alors le crédit et les
calamités dans un chapitre unique « le soutien à l'agriculture » de la compensation, par
extension de son objet, ce qui demanderait aussi un amendement doctrinal.

**Deux préalables**, tirés du chantier en cours :
1. Le chapitre « produits de base, prix à la consommation et à la production » de la compensation
   s'écrit **d'abord** : c'est lui qui fixera la frontière prix/soutien (voir § 5).
2. L'ordre des sectoriels de la doctrine reste prioritaire (« le cadre des finances publiques
   d'abord ; puis l'éducation ; le transport ; le logement ; l'environnement en dernier ») ;
   l'agriculture s'y insérerait après décision du propriétaire, pas avant le cadre des finances
   publiques.

## 2. Tableau de domicile

| Sujet agricole | Domicile actuel ou cible | Le livre « Agriculture » (option c) |
|---|---|---|
| Retraites des régimes agricoles (RSA, RSAA, non-salariés, travailleuses agricoles) | Retraites | renvoi (une phrase, un lien) |
| Cotisations et assiettes des régimes agricoles ; fonds de protection sociale des travailleuses agricoles | Cotisations sociales / caisses | renvoi |
| Déficits des régimes agricoles de la CNSS et leur couverture | Caisses de sécurité sociale | renvoi |
| SMAG et rémunération des travailleurs agricoles | Marché du travail | renvoi |
| Convention collective cadre agricole | Marché du travail | renvoi |
| IRPP catégorie III, évaluation forfaitaire, déductions agricoles | Fiscalité | renvoi |
| Incitations à l'investissement agricole (code de 1993, loi de 2016, primes APIA) | Fiscalité (régimes d'incitation) | renvoi ; **question ouverte** : les primes versées par l'APIA avant 1993, connues seulement par une ligne de 2009, pourraient migrer ici si la série se constitue |
| Taxes du fonds de compétitivité agricole et de pêche | Fiscalité (taxes et fonds spéciaux) | renvoi |
| Subventions aux céréales, huiles, lait, sucre ; prélèvements à l'importation | Compensation | renvoi |
| Prix à la production (céréales et autres filières) | Compensation (chapitre « produits de base », à écrire) — avec les décrets de campagne aujourd'hui au registre de l'Office des céréales | renvoi ; frontière à trancher (§ 5) |
| Office des céréales, ONH, OTD, BNA : statut, comptes, garanties | Entreprises publiques | renvoi |
| Tarif de l'eau d'irrigation et périmètres irrigués | **aucun** | **reçoit** |
| Crédit agricole bonifié, abandons de créances aux agriculteurs | **aucun** (fragments chez BNA/EP) | **reçoit** |
| Assurance agricole, calamités, fonds d'indemnisation | **aucun** | **reçoit** |
| Subventions aux intrants (engrais, semences, aliments du bétail) | **aucun** (trace historique dans la compensation) | **reçoit**, avec renvoi à la compensation pour la période où elles passaient par la Caisse |
| Vulgarisation, recherche, encadrement (CRDA, groupements) | **aucun** | **reçoit** (si flux budgétaire établi ; sinon une section du chapitre budgétaire) |
| Foncier agricole (réforme agraire, cession des terres domaniales) | **aucun** (OTD aux EP) | **reçoit**, resserré sur ce qui a un effet budgétaire ou distributif |
| Budget du ministère de l'Agriculture, longue période | **aucun** | **reçoit** (épine du livre) |
| Couverture sociale des agricoles informels | Informel | renvoi |

## 3. Plan de chapitres (option c)

Plan type des livres sectoriels : institution, dépense longue période, dispositifs à flux,
études. La réglementation sans effet budgétaire ni distributif n'entre pas.

1. **Présentation.** L'objet en une phrase (ce que l'État verse, prête, garantit ou abandonne au
   producteur agricole) ; la carte des dispositifs ; le tableau de voisinage — il sera
   exceptionnellement long, c'est assumé : ce livre est celui qui renvoie le plus. État de la
   matière : rédigeable dès que les chapitres existent.
2. **L'institution et la tutelle** (chapitre de cadre). Le ministère de l'Agriculture, les CRDA,
   les offices de mise en valeur, l'APIA, les groupements interprofessionnels : qui fait quoi,
   textes fondateurs. État : presque rien de lu ; textes connus par intitulé seulement, note
   documentaire entière à faire.
3. **La dépense agricole sur la longue période** (chapitre budgétaire). Budget de la mission
   Agriculture (PAP/RAP 2015-2025 acquis dans `tunisia-data`), crédits des encouragements à
   l'agriculture des lois de finances (le TODO de `_regimes_incitation.qmd` signale « trois
   séries qui ne s'enchaînent pas », non relevées), transferts aux offices (déjà aux EP, en
   figure courte seulement). État : sources localisées, rien de dépouillé avant 2015.
4. **Le crédit agricole et les abandons de créances** (chapitre de dispositif). Bonifications,
   comptes spéciaux agricoles, garanties, remises de dettes ; la BNA vue du côté de
   l'emprunteur. Textes candidats à lecture : la convention prévue par l'article 49 de la loi de
   finances pour 2004 et la liste des comptes spéciaux agricoles (citées non lues au TODO de
   `_secteur_financier.qmd`), l'article 15 de la loi de finances pour 2023, l'article 89 de la
   loi de finances pour 2026 (lu). État : fragments lus côté banque ; rien côté agriculteur.
5. **Les encouragements à l'investissement** (chapitre de dispositif, frontière avec la
   fiscalité à poser). L'histoire avant 1993 : loi n° 82-67 (agriculture et pêche) et code des
   investissements agricoles et de pêche de 1988 (loi n° 88-18) — connus par leur intitulé, à
   lire ; le fonds spécial de développement de l'agriculture, texte fondateur à identifier.
   Après 1993, le régime vit dans la fiscalité : ce chapitre ne reprend que ce que la fiscalité
   ne documente pas (les primes effectivement versées, l'APIA comme guichet). État : le versant
   fiscal est écrit ; le versant « versements » est vide, signalé par les TODO de la fiscalité.
6. **L'eau d'irrigation** (chapitre de dispositif). Les périmètres publics irrigués, la réforme
   agraire de ces périmètres, le tarif de l'eau. État : rien dans le précis ; textes à
   identifier par le documentaliste.
7. **Les calamités et l'assurance** (chapitre de dispositif). Le fonds d'indemnisation des
   dommages agricoles causés par les calamités naturelles : texte fondateur, ressources,
   indemnisations versées. État : une mention incidente (LF 2026, art. 89) ; tout à faire.
8. **Les intrants** (chapitre de dispositif, ou section du chapitre budgétaire si la matière est
   mince). Engrais, semences, aliments du bétail : qui subventionne, depuis quand, par quel
   canal. État : traces historiques dans la compensation (BCT 1974, Banque mondiale 1985) ;
   aucun état du droit.
9. **Rapports et études** (chacun avec sa méthode, jamais mêlés au budgétaire). Candidats connus
   par leur objet : le prêt d'ajustement sectoriel agricole de la Banque mondiale lié à
   l'ajustement de 1986 — à identifier précisément et à récupérer dans `tunisia-data` ; les
   mémorandums Banque mondiale déjà cités par la compensation (1977, 1985) pour leurs chapitres
   agricoles ; rapports de la Cour des comptes sur les offices. État : rien de rangé sous cet
   angle.
10. **Glossaire** du livre.

Chaque chapitre de dispositif se clôt sur « Ce qu'en dit l'économie » (fiche
`docs/notes/eco-<dispositif>.md` à demander à l'économiste — aucune n'existe).

## 4. Questions au documentaliste

**Textes fondateurs candidats** (connus par leur intitulé, à lire ; aucun n'est lu dans le
précis sauf mention contraire) :
- loi n° 82-67 (encouragements à l'agriculture et à la pêche) — notice créée au 31 octobre 2026
  d'après le cache du JORT, non lue (TODO de `_regimes_incitation.qmd`) ;
- loi n° 88-18 (code des investissements agricoles et de pêche) — intitulé seul connu ;
- texte(s) du fonds spécial de développement de l'agriculture, et son rapport au « fonds de
  développement agricole » supprimé en 1995 : un, deux ou trois fonds ?
- texte fondateur du fonds d'indemnisation des dommages agricoles causés par les calamités
  naturelles ;
- textes de la réforme agraire des périmètres publics irrigués et des offices de mise en valeur
  (l'« Agence de la réforme agraire des périmètres publics irrigués » figure dans la liste du
  régime conventionnel des rémunérations publiques) ;
- lois n° 70-25 et 72-36 (cession des terres domaniales à vocation agricole) — citées non lues
  au TODO de `_offices.qmd` ;
- textes du tarif de l'eau d'irrigation ;
- loi n° 59-65 (attributions de la Caisse mutuelle de crédit agricole transférées à la BNA) —
  citée non lue au TODO de `_secteur_financier.qmd` ;
- convention et liste des comptes spéciaux agricoles (art. 49 de la loi de finances pour 2004).

**Séries à chercher** :
- budget du ministère de l'Agriculture sur la longue période (avant les PAP de 2015) : lois de
  finances, lois de règlement ;
- les trois séries d'« encouragements à l'agriculture » des tableaux de crédits des lois de
  finances, signalées non relevées par le TODO de `_regimes_incitation.qmd` ;
- primes versées par l'APIA (une seule valeur connue, 2009, citée dans la fiscalité) : rapports
  d'activité de l'APIA, archives du web (le TODO note que les archives APIA n'ont pas été
  ouvertes) ;
- indemnisations de calamités versées ; subventions aux engrais après les années 1980 ;
- rapports de la Cour des comptes sur l'Office des céréales, l'ONH, l'OTD, la BNA, l'APIA.

**Ce qui existe déjà dans `tunisia-data`** (fiche
`sources/ministere-agriculture-tic-sante-finances.md`, consultation du 4 novembre 2026) :
- PAP de la mission Agriculture 2015-2025 et RAP 2019-2020 (lacunes : PAP 2019 et 2023, RAP 2022
  et suivants) ; fiches opérateurs OTD, OC, ONH dans les PAP ;
- `agridata.tn` : compensation des céréales 2007-2021, collecte, importations, prix d'achat à la
  production, prix de vente subventionnés, prix CF des céréales importées (jeux OC, 20
  fichiers) ; prix à la production de l'huile d'olive extra vierge (ONH, un fichier) ; listes du
  Bureau de restructuration des terres domaniales ;
- fiches et tableaux du rapport « Entreprises publiques » (OC, ONH, OTD, BNA), déjà exploités
  par le livre des EP.

## 5. Risques

1. **Chevauchement massif avec la compensation.** Les prix des céréales, de l'huile et du lait
   sont à la fois un soutien au consommateur (compensation, écrit) et un soutien au producteur
   (prix d'achat garanti par les décrets de campagne, aujourd'hui au registre de l'Office des
   céréales). Le chapitre « produits de base, prix à la consommation et à la production » —
   **déjà à écrire dans la compensation** — couvrira les deux faces. Si l'agriculture naît, la
   frontière doit être tranchée *avant* : je propose que la compensation garde tout le circuit
   des prix administrés des produits de base (production et consommation, une seule épine), et
   que l'agriculture n'en reçoive qu'un renvoi. Écrire ce chapitre d'abord est le préalable n° 1.
2. **Frontière avec les entreprises publiques.** L'Office des céréales, l'ONH, l'OTD et la BNA
   ont leurs chapitres aux EP (statut, comptes, garanties, registres). L'agriculture ne doit pas
   les raconter une seconde fois : elle traite les *dispositifs* (crédit bonifié, prix,
   indemnisation), les EP traitent les *opérateurs*. Le registre des décrets de campagne, logé
   aux EP, est un point de friction à arbitrer avec le point 1.
3. **Risque de livre-coquille.** Si la lecture des textes montre que le crédit bonifié, les
   calamités et l'eau d'irrigation ne portent que des flux minces ou introuvables, le livre se
   réduirait à un chapitre budgétaire et des renvois. Jauge proposée : ne décider l'ouverture
   qu'après la note documentaire des chapitres 4, 6 et 7 — si deux des trois tiennent (textes
   lus, séries trouvées), le livre se justifie ; sinon, option (b) avec un chapitre « soutien à
   l'agriculture » à domicilier (compensation élargie, ou annexe du cadre des finances
   publiques), ce qui demande aussi un amendement doctrinal.
4. **Coût de parité arabe.** Un livre nouveau entre dans la file de traduction (budget mensuel
   plafonné) ; l'ouvrir avant le cadre des finances publiques aggraverait le retard des volumes
   prioritaires.

## Reports (à verser au backlog par l'archiviste, si l'arbitrage est engagé)

- Articulation « fonds spécial de développement de l'agriculture » / « fonds de développement
  agricole » supprimé en 1995 : non établie.
- FOSDAP : sigle absent du précis et de cette instruction ; à identifier (texte, période) avant
  de l'employer.
- Prêt d'ajustement sectoriel agricole (Banque mondiale, autour de 1986) : non identifié dans
  les références existantes du précis ; à chercher et à ranger dans `tunisia-data`.
- Fiches « Ce qu'en dit l'économie » : aucune n'existe pour les dispositifs agricoles.

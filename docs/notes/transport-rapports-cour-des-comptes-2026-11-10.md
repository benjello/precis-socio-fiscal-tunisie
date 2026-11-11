# Transport — chapitre « Rapports et études », volet Cour des comptes

Note documentaire, 10 novembre 2026. Mission R1 (chantier « Livre transport », instruit, ne publie
pas). Objet : les trois rapports de la Cour des comptes rangés dans l'entrepôt `tunisia-data` qui
portent sur la **politique sectorielle** du transport. Source de l'extraction : fiche
`tunisia-data/sources/cour-des-comptes-transport-eau-habitat.md` et ses CSV
(`…-observations-…csv`, `…-sources-citees-…csv`), relus à l'image (couche texte arabe lacunaire).
Les trois PDF sont déjà catalogués (`sources/cour-des-comptes-catalog.csv`,
`…-telechargements.csv`) et rangés hors git — **aucun re-téléchargement**.

## Classement de famille et attribution

Les trois documents relèvent, au sens de `docs/conventions-redaction.md` § 3, de la famille des
**rapports extérieurs** — ici des **constats de contrôle juridictionnel** de la Cour des comptes —,
à tenir **à part du budgétaire** (lois de finances, lois de règlement, évaluations du ministère des
Finances) comme des évaluations économiques. La Cour n'est pas une institution internationale, mais
ses rapports ne sont « ni statistiques, ni documents budgétaires, ni évaluations économiques »
(`tunisia-data/sources/cour-des-comptes.md`) : ce sont des observations de contrôle, chaque chapitre
portant la période contrôlée et, à sa suite, la **réponse de l'organisme contrôlé**. Attribution :
**Cour des comptes** (محكمة المحاسبات ; دائرة المحاسبات jusqu'en 2019), Tunis.

**Garde-fou de domicile (plan § 2).** Beaucoup d'observations de ces rapports portent sur les
**comptes des opérateurs** (résultat, déficit, dette, flotte, effectifs) : celles-là restent au
livre des entreprises publiques (`_transports.qmd`). Le livre transport ne retient que ce qui relève
de la **décision et de la dépense de l'État** : tutelle et gouvernance du secteur, exécution des
contrats-programmes, investissements d'infrastructure, subventions et compensation de service public.
Chaque bloc ci-dessous sépare donc explicitement le **sectoriel** (pour le livre transport) de
l'**opérateur** (renvoi EP).

---

## Rapport 1 — « Le contrôle de l'État sur le secteur du transport terrestre » (2008)

- **Intitulé exact** (arabe) : إشراف الدّولة على قطاع النّقل البرّي. Titre interne du PDF :
  « التقرير التأليفي المتعلق بالمهمة الرقابية حول إشراف الدولة ومراقبتها لقطاع النقل البري »
  (rapport de synthèse de la mission de contrôle sur la supervision et le contrôle du secteur du
  transport terrestre par l'État). Traduction FR retenue : « Le contrôle de l'État sur le secteur du
  transport terrestre ».
- **Édition / rang** : rapport spécifique (مهمة رقابية), rubrique 81 du site. **Vingt-troisième
  rapport annuel** de la Cour des comptes — rattachement confirmé par le renvoi interne du rapport
  de 2016 (noté dans l'entrée CSL existante `cour-comptes-2008-transport-terrestre`). Mis en ligne le
  15 juin 2008. 26 pages.
- **Périmètre** : la supervision par l'État de l'ensemble du transport terrestre (ferroviaire,
  routier, location de véhicules), cadré par la **loi n° 2004-33 du 19 avril 2004** sur
  l'organisation des transports terrestres, modifiée par la **loi n° 2006-55 du 28 juillet 2006**
  (unification des textes, règles de financement du transport public collectif, autorités régionales
  d'organisation). Exercices contrôlés ≈ 1999-2007.
- **Méthode du contrôle** : mission de contrôle de performance de la Cour sur la politique et
  l'organisation du secteur ; constats appuyés sur les plans directeurs, les décisions de conseils
  ministériels restreints, le registre national des transporteurs et des échantillons d'entreprises
  (location de voitures, transport international de marchandises). Lecture pour la présente note :
  à l'image, pp. imprimées 97, 103 et 106 (couche texte arabe lacunaire).
- **Observations sectorielles retenues** (livre transport) :
  - *Investissement et planification (p. imp. 97)* : le plan directeur régional de transport du Grand
    Tunis 1999-2016, approuvé par conseil ministériel restreint en 1999, ne prévoyait d'abord que
    d'approfondir les études ; le **projet de réseau ferré rapide (RFR)** a vu son tracé fixé de juin
    2003 à mars 2006 (tracés définitifs approuvés en CMR le 10 avril 2006), sa réalisation renvoyée
    au 11e plan ; coût du réseau de transport collectif du Grand Tunis estimé à **3 200 m.d**. Part du
    transport collectif tombée de 51 % (1977) à 36 % (2006) pour un objectif de 50 %. L'exposé
    d'ouverture chiffre l'investissement dans le transport terrestre au 10e plan à **2 383 m.d**
    (51,8 % de l'investissement transport, réalisé à 82,5 % ≈ 1 967,2 m.d) et au 11e plan à
    **3 839,5 m.d** (+61 %).
  - *Gouvernance / tutelle (p. imp. 106)* : l'Agence technique des transports terrestres (ATTT)
    tient le registre national des transporteurs mais ne dispose pas de moyens de suivi ; non-respect
    des cahiers des charges (44 entreprises sur 150 de location de voitures sous le minimum de 25
    véhicules ; 26 sur 61 du transport international de marchandises sous la charge utile minimale,
    16 sous le minimum de véhicules).
  - *Exploitation du domaine public affecté (p. imp. 103)* : les gares routières de Bab Alioua et
    Bab Saadoun, gérées de fait par l'ATTT depuis l'**arrêté du ministre des transports du 8 juin
    1999**, sont utilisées gratuitement par les sociétés de transport ; redevances des gares en
    concession non perçues régulièrement.
- **Renvoi EP / compensation** : le détail des gares côté SNTRI (exploitation sans titre) éclaire
  l'opérateur ; le droit à compensation du transport public est domicilié à la compensation.
- **Textes cités par la Cour** : loi n° 2004-33 (modifiée par loi n° 2006-55) ; arrêté du 8 juin
  1999 (gares) ; plan directeur de transport du Grand Tunis 1999-2016 ; étude des réseaux de
  transport collectif du Grand Tunis ; CMR des 23 juin 1999, 18 mars 2005, 10 octobre 2006.

## Rapport 2 — « Le ministère du Transport » (2016)

- **Intitulé exact** (arabe) : وزارة النقل. Titre descriptif catalogué : « Ministère des transports
  (rapport spécifique : supervision des entreprises, régulation, sécurité) ». Traduction FR retenue :
  « Le ministère du Transport ».
- **Édition / rang** : rapport spécifique, rubrique 81. Mis en ligne le **15 juin 2016**, dans le
  cycle du **vingt-neuvième rapport annuel** (التقرير السنوي التاسع والعشرون, catalogue CdC daté
  2016-02-15) — rattachement par cycle de publication, **à confirmer** (le PDF ne se numérote pas
  lui-même ; voir Lacunes). 43 pages.
- **Périmètre** : le ministère du Transport dans ses fonctions de **tutelle, régulation et sécurité**
  des entreprises et activités du secteur (18 établissements sous tutelle : transport terrestre
  commercial, aviation civile — 2 établissements, maritime — 5, météo — 1). Exercices contrôlés
  2009-2014 selon les thèmes.
- **Méthode du contrôle** : contrôle de la Cour sur l'exercice de la tutelle par le ministère
  (qualité du suivi des opérateurs, de la régulation, de la sécurité aérienne, maritime et
  portuaire) et sur les flux financiers entre ministère et établissements. Lecture : à l'image,
  pp. imprimées 275, 278, 281-283, 295-296.
- **Observations sectorielles retenues** (livre transport) :
  - *Subventions / compensation de service public (p. imp. 281-282)* : manque à gagner annuel des
    entreprises de transport routier au titre des **tarifs réduits des élèves et étudiants** estimé
    par le ministère à **~400 m.d/an**, contre des compensations versées de **273 m.d (2012)** et
    **323 m.d (2013)** ; compensation des **gratuités** (justice, défense, intérieur) non respectée
    (8 m.d dus par le ministère de la défense à la société régionale de Bizerte) ; manque à gagner de
    la gratuité pour familles de martyrs et blessés 3,3 m.d (2013, 512 bénéficiaires). Cadré par
    l'art. 12 de la loi n° 2004-33 (compensation des tarifs réduits) et la loi n° 2012-26 du 24
    décembre 2012 (gratuité blessés/familles de martyrs). [Le tarif administré et sa compensation
    restent domiciliés à la compensation — ici en tant que constat de tutelle.]
  - *Reprise de dettes d'opérateurs par le budget du ministère (p. imp. 281)* : résultats négatifs
    cumulés des entreprises publiques de transport de **1 200 m.d sur 2010-2013** ; en 2011, prise en
    charge par le budget du ministère de **244 m.d** de dettes de la Transtu envers la SNDP et la
    CNRPS — mesure ponctuelle « sans traitement des causes ».
  - *Gouvernance de la tutelle (p. imp. 278, 295)* : le ministère n'évalue pas la qualité des
    contrôles délégués à l'OACA ni le suivi du programme annuel, et ne suit pas la régularité des
    vols depuis 2012 ; les commissions de sûreté portuaire prévues par le code des ports maritimes
    ne se réunissent pas régulièrement (Sousse, La Goulette, Radès, La Skhira).
  - *Confusion ministère / établissements (p. imp. 283)* : frais de personnel du ministère supportés
    par les opérateurs (OACA 6,5 m.d sur 2011-2013 ; Tunisair 516 k.d jan. 2012-mars 2014 ; 68 agents
    payés par les entreprises, 22 voitures) ; détachements au-delà du plafond de 20 %.
  - *Investissement / sécurité (p. imp. 296)* : navire « Tanit » de la CTN (construction en Corée du
    Sud depuis 2010, coût ~400 m.d) non validé par le comité central de sécurité maritime (défaut de
    tangage ; validation refusée en décembre 2013) ; système d'information intégré des sociétés
    régionales (projet 2008, 1,2 m.d, contrat résilié janv. 2012, réalisé à 61 %).
- **Renvoi EP** : les résultats, dettes et flotte des opérateurs (Transtu, CTN, Tunisair, OACA)
  restent au livre des entreprises publiques ; retenu ici le fait de tutelle et de dépense d'État.
- **Textes cités par la Cour** : loi n° 2004-33, art. 12 ; loi n° 2012-26 du 24 décembre 2012 ;
  code de gestion administrative de la navigation maritime ; code des ports maritimes ; loi n° 2012-4
  du 22 juin 2012 (détachements exceptionnels dans le secteur public) ; arrêté du 8 juin 1999 (gares).

## Rapport 3 — « La Société nationale de transport interurbain » (SNTRI, 2017) — exploité ici

- **Intitulé exact** (arabe) : الشّركة الوطنيّة للنّقل بين املدن. Traduction FR retenue : « La Société
  nationale de transport interurbain » (SNTRI).
- **Édition / rang** : rapport spécifique, rubrique 81. Mis en ligne le **15 juin 2017**, dans le
  cycle du **trentième rapport annuel** (التقرير السنوي الثلاثون, catalogue CdC daté 2017-06-15,
  date identique) — rattachement par cycle de publication, **à confirmer** (voir Lacunes). 29 pages.
- **Périmètre** : la SNTRI, société de transport public interurbain de personnes, créée le 2 octobre
  1981 par le **décret-loi n° 81-22** (ratifié par la loi n° 82-3, modifiée par la loi n° 90-54),
  classée entreprise publique non administrative par le **décret n° 2002-2199 du 7 octobre 2002** ;
  capital 8,5 m.d (100 % État) ; sous tutelle du ministère du Transport. Exercices contrôlés
  2010-2014 (mission de contrôle de janvier 2011 à mai 2016).
- **Méthode du contrôle** : mission de contrôle de la Cour sur la gestion de la flotte, l'activité et
  les recettes d'exploitation sur la période de janvier 2011 à mai 2016 ; constats appuyés sur les
  rapports d'activité 2014-2015 de la société, le rapport interne de la direction du produit du
  4 février 2016, et le relevé des trajets et de la billetterie. Lecture : à l'image, pp. imprimées
  668-672 (synthèse) et 690 (réponse de l'entreprise) ; **corps du rapport non lu** (voir Lacunes).
- **Observations — part sectorielle (livre transport)** :
  - *Tarif administré gelé et service public non compensé (p. imp. 671)* : tarifs **inchangés depuis
    2010** ; **pas de subvention pour les lignes sociales** ; manque à gagner des tarifs gratuits
    estimé à 1,4 m.d/an (familles de martyrs et blessés de la révolution) et 2 m.d/an (cartes
    d'invalidité). Réponse de l'entreprise (p. imp. 690) : gel des tarifs depuis 2010 ≈ 3 m.d/an de
    perte, tarifs réduits ≈ 3,2 m.d/an, lignes frontalières sans compensation ≈ 2 m.d/an. [Tarif et
    compensation domiciliés à la compensation ; retenu ici comme constat de l'absence de contrat et
    de compensation de service public.]
  - *Exploitation du domaine affecté (p. imp. 672)* : la SNTRI doit à l'ATTT 671 k.d au titre de
    l'exploitation des gares de Bab Alioua et Bab Saadoun — prolonge le constat de 2008.
  - *Absence de contrat-programme / cadrage de la tutelle* : la Cour appelle à **assainir la situation
    financière** faute de cadre contractuel entre l'État et la société ; prêt du **fonds de
    restructuration du capital des entreprises publiques** (4,7 m.d) non remboursé.
- **Observations — part opérateur (renvoi EP, non retenues pour le livre transport)** : déficit
  chaque année 2011-2014 (pertes 5,546 / 7,287 / 11,597 / 11,577 m.d ; bénéfice 2010 de 45,887 k.d) ;
  pertes cumulées ~37 m.d fin 2013 (> 4× le capital) ; recettes ≈ 27 m.d, 90 % du chiffre tiré des
  billets ; 785 agents (2015), masse salariale 17,598 m.d ; flotte 113 bus (déc. 2015), disponibilité
  50 %, besoin 169 bus/jour ; dettes CNRPS ~21 m.d, SNDP 13,8 m.d ; 2 041 trajets annulés (2014),
  4 719 (2015) ; écart billetterie 494 k.d (2014). Réponse : dette totale 78 m.d.
- **Textes cités par la Cour** : décret-loi n° 81-22 (création, 2 oct. 1981) ; loi n° 82-3 (ratif.) ;
  loi n° 90-54 (modif.) ; décret n° 2002-2199 du 7 octobre 2002 ; rapports d'activité 2014-2015 ;
  rapport interne du 4 février 2016.

---

## Références candidates (CSL-JSON)

### Déjà présentes dans `precis/fr/compensation/references.json` (réutiliser, ne pas recréer)
- `cour-comptes-2008-transport-terrestre` — type `report`, Cour des comptes, 2008-06-15, URL du PDF,
  copie locale et SHA-256 dans la note CSL. **À réutiliser pour le livre transport.**
- `cour-comptes-2016-ministere-transport` — type `report`, Cour des comptes, 2016-06-15, idem.
  **À réutiliser.**

> Note : ces deux clés vivent aujourd'hui dans le `references.json` de la **compensation**. Si le
> livre transport est ouvert, prévoir de les référencer depuis `precis/fr/transport/references.json`
> (clé partagée ou recopie à l'identique — arbitrage bibliographe). Compléter leur champ
> `note` du rang d'édition (23e / 29e rapport annuel) une fois confirmé.

### À créer — SNTRI 2017
```json
{
  "id": "cour-comptes-2017-sntri",
  "type": "report",
  "title": "الشّركة الوطنيّة للنّقل بين املدن (La Société nationale de transport interurbain)",
  "title-short": "Cour des comptes, SNTRI (2017)",
  "author": [{ "literal": "Cour des comptes" }],
  "publisher": "Cour des comptes",
  "publisher-place": "Tunis",
  "issued": { "date-parts": [[2017, 6, 15]] },
  "URL": "https://www.courdescomptes.nat.tn/wp-content/uploads/pdf_rapport/Rapport_81_2018-08-16-11-02-16.pdf",
  "accessed": { "date-parts": [[2026, 10, 11]] },
  "note": "citation-key: cour-comptes-2017-sntri\nRapport spécifique en arabe, 29 p., mis en ligne le 15 juin 2017 (cycle du trentième rapport annuel, à confirmer). Mission de contrôle de janvier 2011 à mai 2016, exercices 2010-2014. Lues à l'image : pp. imprimées 668-672 (synthèse) et 690 (réponse de l'entreprise) ; corps pp. 673-689 non lu. Copie locale : tunisia-data/data/raw/cour-des-comptes/81/Rapport_81_2018-08-16-11-02-16.pdf (756 524 octets, SHA-256 26731d60d29931c6b06d9519946ea581d2d672b1d36615ad1ac2e5f8b9913848, hors git). Titre français traduit de l'arabe par le documentaliste. Constat de contrôle juridictionnel : à tenir à part du budgétaire."
}
```

Textes juridiques cités par ces rapports, candidats à vérifier/créer si le chapitre les mobilise
(plusieurs existent déjà au corpus compensation/transport) : loi n° 2004-33 (organisation des
transports terrestres) ; loi n° 2006-55 (modificative) ; loi n° 2012-26 du 24 décembre 2012
(`loi2012-26`, déjà présente) ; loi n° 2012-4 du 22 juin 2012 (détachements) ; décret-loi n° 81-22
(création SNTRI) ; décret n° 2002-2199 du 7 octobre 2002 (liste des EPNA) ; arrêté du ministre des
transports du 8 juin 1999 (gares de Bab Alioua et Bab Saadoun). — relevés d'intitulé ici, non vérifiés
au JORT (hors mission R1 ; à confirmer par le documentaliste au moment de rédiger).

## Notions à glossaire (à vérifier/ajouter — ne PAS éditer `glossaire.yml` dans ce chantier)

- **Rapport spécifique de la Cour des comptes** (مهمة رقابية / تقرير تأليفي) vs **rapport annuel**
  (التقرير السنوي) : un rapport spécifique est un chapitre de mission de contrôle inséré dans un
  rapport annuel numéroté ; source canonique `tunisia-data/sources/cour-des-comptes.md`. (Entrée
  possiblement déjà couverte côté caisses/EP — à vérifier.)
- **Contrôle juridictionnel / constat de contrôle** (famille « rapport extérieur », distincte du
  budgétaire et des évaluations économiques) — cf. `docs/conventions-redaction.md` § 3.
- **Contrat-programme** d'un opérateur de transport (cadre pluriannuel État-opérateur) — notion déjà
  pressentie au plan § 3 ; source canonique à préciser (PAP/RAP, textes des contrats).
- **Compensation des tarifs réduits / manque à gagner de service public** (art. 12 loi n° 2004-33) —
  probablement déjà au glossaire de la compensation ; vérifier le partage de domicile.
- **Plan directeur de transport du Grand Tunis (1999-2016)** et **réseau ferré rapide (RFR)** — à
  rattacher au chapitre ferroviaire / urbain ; source canonique : rapport 2008 + plan directeur.
- **Fonds de restructuration du capital des entreprises publiques** — notion citée par la Cour
  (prêt SNTRI non remboursé) ; domicile EP/finances publiques à confirmer.
- **SNTRI**, **ATTT**, **gares routières de Bab Alioua / Bab Saadoun** — entrées d'opérateurs/lieux,
  domicile EP ; mention transversale.

## Lacunes (constats neutres, rien d'inventé)

1. **Rang d'édition des rapports 2016 et 2017 non auto-confirmé par les PDF.** Le 2008 est le **23e
   rapport annuel** (confirmé par renvoi interne du rapport 2016). Pour 2016 (→ 29e) et 2017 (→ 30e),
   le rattachement repose sur le **cycle de mise en ligne** (juin 2016 / juin 2017) rapproché du
   catalogue CdC ; les PDF ne portent pas de numéro de rapport annuel dans leur couche texte (OCR
   arabe lacunaire). À confirmer à l'image (pages liminaires) ou sur le sommaire du rapport annuel
   correspondant (rubrique 84). Report → backlog du livre transport.
2. **SNTRI 2017 — corps non lu.** Seules la synthèse (pp. imp. 668-672) et la réponse de l'entreprise
   (p. imp. 690) ont été lues ; le corps (pp. imp. 673-689, soit pp. pdf 6-22) reste à lire pour un
   éventuel détail sur l'absence de contrat-programme et le plan de restructuration. Report → backlog.
3. **Couche texte arabe lacunaire** sur les trois PDF : toute citation littérale se relit à l'image
   (lettres manquantes). Les chiffres cités ici viennent de l'extraction relue à l'image de
   `tunisia-data`, non d'une transcription texte directe.
4. **Intitulés juridiques relevés, non vérifiés au JORT** (loi 2004-33, 2006-55, décret-loi 81-22,
   décret 2002-2199, arrêté 8 juin 1999, loi 2012-4) : vérification de référence exacte et de
   pagination JORT à faire au moment de rédiger (hors périmètre R1).

## Recherches infructueuses

Aucune fiche `docs/recherches.yml` ouverte ni modifiée (garde-fou du chantier respecté). Deux pistes
à transformer en fiches rejouables lors de la rédaction, si besoin : (a) confirmation du rang d'édition
(29e / 30e rapport annuel) via les rapports annuels rubrique 84 ; (b) décret(s) d'application de
l'art. 12 de la loi n° 2004-33 sur la compensation des tarifs réduits — la Cour (rapport 2016) en
note l'absence, piste déjà signalée côté compensation.

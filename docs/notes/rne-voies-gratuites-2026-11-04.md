# RNE et voies gratuites : entreprises publiques non cotées (constats du 4 novembre 2026)

Méthode : curl, WebFetch, WebSearch, API CKAN publique de catalog.data.gov.tn. Aucun compte, aucun CAPTCHA, aucun achat, aucune demande. Annexe existante (_annexe_registre.qmd) lue : parcours visiteur du 3 nov., décret 2022-298 (tarifs) non refaits.

## A. VU (primaire, daté 2026-11-04)

### A1. Base légale
- Loi 89-9 du 1er février 1989, version consolidée CMF (modifiée par lois 94-102, 96-74, 99-38, 2001-33, 2006-36), https://www.cmf.tn/sites/default/files/pdfs/reglementation/textes-reference/loi_89_9_fr.pdf. Art. 14, texte exact : « Les entreprises publiques doivent publier avant le 31 août de chaque année au Journal Officiel de la République Tunisienne, et à leurs frais, leurs bilans et comptes de gestion et de résultats relatifs à l'exercice écoulé. » Aucune sanction dans l'article. L'article 14 n'est pas listé comme modifié dans cette version (la consolidation s'arrête en 2006).
- Loi 89-9, article précédent (l. 115-116 du texte extrait) : certaines entreprises publiques sont soumises à une révision par un expert-comptable (numéro d'article non relevé, à lire).
- Loi 2018-52 du 29 octobre 2018 (texte français, https://www.icnl.org/wp-content/uploads/Loi-n°-2018-52-du-29-octobre-2018-2-1.docx, traduction non officielle à ma connaissance) :
  - Art. 1 : le Registre vise à « les conserver et les mettre à la disposition du public ».
  - Art. 2 : « une base de données publique ».
  - Art. 15 : « Les redevances pour services rendus sont portées à la charge de leur demandeur. Leur montant est fixé par décret gouvernemental pris après avis du Centre, en tenant compte du coût réel du service. »
  - Art. 29 (liste des assujettis) inclut « Les entreprises publiques et les établissements publics à caractère non administratif ».
  - Art. 32 : dépôt « au plus tard dans le septième mois suivant la clôture de l'exercice comptable, leurs états financiers [...] et les rapports des commissaires au compte ». Même article : les sociétés déposent aussi « une liste mise à jour des actionnaires » (ou associés) à la date de l'AG.
  - Art. 46-47 : le Centre publie un « Bulletin officiel » sur son site ; « la publicité dans le Bulletin officiel du Centre tient lieu de publicité au Journal officiel » pour les opérations dont la loi impose la publicité.
  - Art. 49 : « Le centre met à la disposition du public toutes les données et tous les documents portés au registre, hormis ce qui est en contradiction avec les lois en vigueur. » Il délivre copie intégrale des inscriptions, copie simple ou conforme de tout document déposé, extrait du registre.
  - Art. 51 : pénalité de retard = moitié de la redevance par mois de retard ; à défaut de régularisation, suspension du registre et transmission au ministère public.
  - La loi ne dit pas « gratuit » ni « payant » pour la consultation ; elle renvoie au décret (art. 15).
- Conséquence textuelle (déduction, non vue appliquée) : l'obligation de l'art. 14 de 89-9 (publication JORT) et celle de l'art. 32 de 2018-52 (dépôt RNE) coexistent ; l'art. 47 de 2018-52 ne vise que « les opérations que la présente loi impose » en publicité, pas l'art. 14 de 89-9. Si la publication JORT des comptes subsiste au titre de 89-9, rien dans 2018-52 ne la remplace explicitement. À vérifier par un juriste.

### A2. Portail RNE (code source public du site)
- https://www.registre-entreprises.tn/ redirige (meta refresh) vers ./rne-public ; titre « RNE Public ». Application Angular ; robots.txt et sitemap.xml : 404.
- Fichier https://www.registre-entreprises.tn/rne-public/main.3adc1fa93355e0d6.js : routes « borne-free » (recherche « free-search ») et « myrne/borne-premium/premium-landing ». Écran d'accueil avec deux cartes :
  - « Service Gratuit » : « Ce service donne droit, via un abonnement annuel, à la consultation et à l'affichage des informations publiées dans la BORNE des entreprises ; ainsi que le Téléchargement illimité des documents des entreprises qui regroupent tous les types de publications. »
  - « Service Premium » : même phrase, « ainsi qu'au Téléchargement illimité... ».
  - Bouton : « Accès au service / الدخول إلى الخدمة ».
  - Les deux textes sont presque identiques ; le libellé ne précise pas ce qui est gratuit. Le contenu réel du « Service Gratuit » n'a pas été exploré ici (annexe : parcours visiteur déjà fait le 3 nov. : liste des documents, nature, date, prix, exercice, sans contenu).
- Back-ends déclarés dans le JS : /api/rne-api, rne-bor-api, rne-document-api, rne-auth-api, rne-subscription-api. Aucun n'a été appelé (pas d'API publique documentée vue ; pas de contournement).
- Aucune occurrence de « TND » ni « dinar » dans le JS principal (les prix viennent des données de l'API).

### A3. Tarifs
- Déjà dans l'annexe (décret 2022-298 du 28 mars 2022, art. 3, TTC) : fiche d'identité 5 DT ; copie électronique contrat/PV 5 DT par document ; états financiers 10 DT par document ; liste des associés/actionnaires 20 DT par identifiant ; abonnement annuel à la base 500 DT par utilisateur. Non revérifié ici (texte du décret non relu).
- Rien trouvé comme page tarifaire officielle en ligne sur registre-entreprises.tn (non cherché en profondeur, site Angular).

### A4. Open data
- Portail national https://www.data.gov.tn (« Portail National des Données Ouvertes en Tunisie ») ; catalogue CKAN https://catalog.data.gov.tn (API /api/3/action/package_search, publique). Certificat TLS de data.gov.tn non reconnu par curl sans -k (lecture seule faite avec -k).
- Recherches package_search : « registre national des entreprises » 3 jeux (INNORPI) ; « RNE » 0 ; « entreprises publiques » 3 ; « états financiers » 3 ; « JORT » 2 (conventions) ; « commissaire aux comptes » 2.
- Aucun jeu du Centre national du registre des entreprises. Liste des organisations : aucun organisme dont le titre contient registre/RNE/CMF/Cour des comptes (filtre simple).
- Jeu « TN Personnes morales » (https://catalog.data.gov.tn/dataset/tn-persones-morales), producteur INNORPI, modifié 2025-03-11, créé 2023-02-19 ; notes : « informations sur les entreprises (personnes morales) parvenues des 27 tribunaux de première instance et les 3 guichets uniques de l'API » ; « N° du registre, dénomination, date d'entrée en activité, gouvernorat du tribunal, activités ». Ressource pmrcc.csv, 50 Mo, 181 996 lignes, colonnes : N_REGISTRE, NOM_SOCIETE_FR, NOM_SOCIETE_AR, NOM_COMMERCIAL_FR/AR, ADRESSE, CODE_JURIDICTION, DATE_ENREGISTREMENT, DETAIL_ACTIVITE_AR, FORME_JURIDIQUE, GOUVERNORAT_AR. Pas de capital, de dirigeants ni de comptes. Registre de commerce central ancien (immatriculations jusqu'en 2014 observées en échantillon) : sert au plus à retrouver un numéro de registre ; couverture des entreprises publiques non testée (une recherche « STEG » ne renvoie que des sociétés privées sans rapport).
- Licence : le champ license_id/license_title du jeu renvoie « otl-data.industrie.gov.tn » (champ mal renseigné) ; licences types : page https://www.data.gov.tn/fr/licences-de-r%C3%A9utilisation-des-donn%C3%A9es-publiques-ouvertes/ (non lue).
- Jeux d'entreprises publiques isolés : ETAP « Rapports & Bilans » (https://catalog.data.gov.tn/dataset/rapports-bilans) : rapports annuels 2012-2014 (2012, 2013, 2014), résultats financiers 2011-2014, bilan social 2013, PDF ; « TN-Portefeuille Titre de participation de l'ETAP » (xlsx). Dernier état : 2014, donc ancien. Jeu « Rapport du commissaire aux comptes 2015 et 2016 » de l'Organisme tunisien des droits d'auteur (hors périmètre probable).

### A5. CMF
- https://www.cmf.tn/?q=emetteurs (« Emetteurs ») avec pages « rapports-annuels-des-soci-t-s » ; périmètre : sociétés faisant appel public à l'épargne (cotées ou ayant émis), pas les entreprises publiques non cotées. Le CMF est la source gratuite des comptes des cotées (dont les sociétés d'État cotées). Détail de la page non exploré.
- La loi 89-9 consolidée est hébergée par le CMF (lien ci-dessus), texte lisible sans compte.

### A6. Cour des comptes
- https://www.courdescomptes.nat.tn/fr/ accessible sans compte, rubrique « rapports-résultats » (r_cat/r_subcat), rapport de loi de règlement 2023, 34e rapport annuel général. Non exploré en détail : je n'ai pas vérifié ce qu'il contient sur les entreprises publiques.

## B. LU DANS LA PRESSE (secondaire, non vérifié par moi)
- Business News, Nizar Bahloul, 12 janvier 2026 (https://businessnews.com.tn/2026/01/12/les-comptes-opaques-des-entreprises-de-letat/1382354/), chronique d'opinion : les entreprises publiques « brillent par leur opacité » ; Tunisie Telecom n'aurait « jamais rendu publics ni leurs états financiers ni les rapports de leurs commissaires aux comptes » ; pour les cotées, états consultables gratuitement sur les sites du CMF et de la Bourse ; les sociétés doivent transmettre leurs états au RNE, « accessibles moyennant une somme modique » ; exigence « globalement respectée » par le privé, pas par la majorité des entreprises publiques ; site de la Cour des comptes « pas actualisé depuis au moins 2021 » (affirmation d'opinion, que je n'ai pas vérifiée : la page d'accueil montre un rapport de loi de règlement 2023 et le 34e rapport annuel). L'article ne cite pas l'art. 14 de la loi 89-9.
- Managers.tn, 20 juin 2024 (https://managers.tn/2024/06/20/rne-respecter-les-delais-pour-eviter-les-penalites) : dépôt 2023 avant le 31 juillet 2024 ; art. 32 loi 52/2018, sept mois ; pénalité de moitié des frais par mois ; dépôt via portail en ligne (réduction annoncée jusqu'à 50 % par rapport au guichet). Allafrica (7 mai 2026) : dépôt des états 2025 avant le 31 juillet 2026, exclusivement en ligne (rapport du CAC peut suivre).
- Managers.tn, 2 juin 2023 : extrait traduit FR/EN, 20 dinars (service payant ; URL citée par la recherche, non ouverte). Allafrica 18 sept. 2025 : nouveaux services annoncés, certificat électronique incluant les derniers états financiers (non confirmé en ligne ni tarifé).

## C. NON VU / SUPPOSÉ / À FAIRE
- Ce que montre exactement le « Service Gratuit » : non exploré ici. Supposé d'après le libellé : accès par abonnement (à confirmer : gratuit mais avec abonnement, ou non).
- Si un état financier déposé se télécharge sans payer : l'annexe indique que les prix sont affichés (10 DT) ; donc, supposé payant pour le contenu, gratuit pour la mention de dépôt (nature, date, exercice).
- Publication effective au JORT des comptes (art. 14 89-9) : non établie. Le serveur JORT MCP ne couvre que les textes (lois, décrets, arrêtés, avis), pas les annonces légales ; l'Imprimerie officielle (iort.gov.tn) n'a pas répondu depuis cet environnement (connexion refusée, 4 nov.). Aucune trace trouvée en recherche d'une publication annuelle des comptes d'entreprises publiques au JORT. Constat de la chronique de Business News convergent mais non primaire.
- Code des sociétés commerciales : non lu dans cette session. Mentionné par 2018-52 (art. 461 et 472 pour comptes consolidés ; art. 31 cotées). Supposé : les SA publient leurs états via dépôt RNE (art. 32 2018-52) ; à lire dans le CSC les articles sur la publication des états financiers des SA.
- DGPPP : domaine dgppp.gov.tn non résolu ; la Direction générale des participations publiques relève du ministère des Finances ; site non trouvé, rien vu.
- Circulaires RNE n° 17/2020 et 3/2021 : non lues (déjà au TODO).
- Décret 2022-298 : prix non revérifiés ici.

## D. Réponse à la question de départ
- Gratuit, vu : mention des dépôts au Registre (annexe), textes de loi (CMF), jeu open data INNORPI (identité des personnes morales, 2025), jeux ETAP (2011-2014), comptes des cotées (CMF/Bourse, d'après presse et périmètre CMF).
- Payant, vu dans le décret (annexe) : contenu des états financiers (10 DT/document), liste des actionnaires (20 DT), PV (5 DT).
- Phrase du mail à la Banque mondiale (« certaines informations du RNE sont payantes ») : cohérente avec décret 2022-298 et Business News (« somme modique »). Formulation prudente possible : « le contenu des documents déposés est payant, leur existence est publique ».

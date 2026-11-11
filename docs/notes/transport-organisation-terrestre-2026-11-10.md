# Note documentaire — Organisation des transports terrestres (angle ORGANISATION)

Documentaliste, 10 novembre 2026. Chantier « Livre transport » (branche
`chantier/transport-livre`), ticket T1. **Instruit, ne publie pas** : aucun `.qmd`,
aucun commit. Angle **organisation du secteur** (qui peut transporter, régime
d'autorisation/licence, concessions, répartition public/privé, urbain/régional/
interurbain/rural, personnes/marchandises), distinct du **tarif** et de sa
**compensation**, qui restent au livre de la compensation
(`precis/fr/compensation/_transport.qmd`), et distinct du **statut et des comptes
des opérateurs**, qui restent aux entreprises publiques.

Sources : corpus législatif local `~/projets/PDFs-legislation-tunisie/PDFs/JORT/`
et `jort_cache.db` (couverture 1956-01-03 → 2026-10-29) ; chapitre compensation du
précis et sa bibliographie pour les clés CSL déjà établies. Les textes des lois de
1985 et de 2004 ont été **relus au fascicule** cette fois (le chapitre compensation
ne les avait lus que sous l'angle du tarif, en couche texte dégradée) : la loi de
2004 par sa couche texte (chiffrée par décalage +3, déchiffrée et vérifiée) ; la loi
de 1985, dont le fascicule n'a pas de couche texte, par **océrisation** (tesseract
fra, 200 dpi) — fidèle mais à contrôler à l'image avant citation littérale.

---

## 1. Faits sourcés

### 1.1 Les deux lois d'organisation et leur antécédent

- **Loi n° 85-77 du 4 août 1985, portant organisation des transports terrestres.**
  JORT n° 58 du 9-13 août 1985, p. 1000-1001 (texte complet, **23 articles**, lu par
  OCR). Clé CSL **déjà existante** : `@loi85-77` (la fiche ne vise que p. 1000-1001 et
  les art. 7 et 10 ; le texte s'étend en réalité jusqu'à l'art. 23 — voir § 4,
  correction de périmètre). Promulguée par Habib Bourguiba ; travaux préparatoires :
  adoption par la Chambre des députés le 23 juillet 1985. URL :
  https://www.pist.tn/jort/1985/1985F/Jo05885.pdf (vérifiée, 200).
  Structure (OCR) : Titre I *Principes généraux* (art. 1-7) ; Titre II *Le transport
  ferroviaire* (art. 8) ; Titre III *Le transport routier des personnes* — ch. I
  Dispositions communes (art. 9-11), ch. II Transport urbain (art. 12), ch. III Autres
  catégories (art. 13) ; Titre IV *Le transport routier de marchandises* (art. 14-18) ;
  Titre V *Des sanctions* (art. 19-22) ; Titre VI *Dispositions diverses* (art. 23).

- **Antécédent de la loi de 1985 (art. 23, clause abrogatoire, OCR).** La loi de 1985
  « abroge toutes dispositions antérieures contraires et notamment » :
  - le **décret du 25 mai 1950 portant réglementation des transports automobiles
    public et privé de marchandises** et les décrets subséquents — texte de l'époque
    du Protectorat ; **absent du corpus** `jort_cache.db` (antérieur à 1956) : à
    chercher au *Journal officiel tunisien* d'avant 1956 (OCR requis, voir Lacunes) ;
  - la **loi n° 78-40 du 6 juillet 1978 réglementant les transports publics et privés
    en commun de personnes** — JORT n° 49 de 1978, p. 1996 (recid 115662). URL :
    https://www.pist.tn/jort/1978/1978F/Jo04978.pdf (vérifiée, 200). Non lue ici.
  La loi de 1985 réunit donc en un seul texte deux régimes séparés auparavant : le
  transport de marchandises (décret de 1950) et le transport en commun de personnes
  (loi de 1978).

- **Loi n° 2004-33 du 19 avril 2004, portant organisation des transports terrestres.**
  JORT n° 32 du 20 avril 2004, p. 996-1003 (texte complet, **64 articles**, 9 titres,
  relu au fascicule). Clé CSL **déjà existante** : `@loi2004-33`. URL :
  https://www.pist.tn/jort/2004/2004F/Jo0322004.pdf (vérifiée, 200). Remplace la loi de
  1985. Travaux préparatoires : adoption par la Chambre des députés le 1er avril 2004.
  Structure (table analytique de `jort_cache.db`, pages exactes) : Titre I *Dispositions
  générales* (art. 1-12, p. 996-997) ; Titre II *Transport de personnes* (art. 13-14) —
  ch. I *Transport public de personnes* (art. 15-24, p. 997-998), ch. II *Transport
  touristique* (art. 25, p. 998) ; Titre III *Transport de marchandises* (art. 26-27) —
  ch. I *Transport routier de marchandises pour le compte d'autrui* (art. 28), ch. II
  *Centrales de fret* (art. 29-30), ch. III *Dispositions spéciales* (art. 31, p. 998) ;
  Titre IV *Location des véhicules* (art. 32-33, p. 999) ; Titre V *Dispositions
  communes* — ch. I *Conditions d'exercice* (art. 34-36), ch. II *Contrats de location
  et de transport de marchandises* (art. 37), ch. III *Exploitation des véhicules*
  (art. 38-39), ch. IV *Conduite des véhicules* (art. 40-41, p. 999-1000) ; Titre VI
  *Gares de transport terrestre* (art. 42-44, p. 1000) ; Titre VII *Infractions et
  sanctions* (art. 45-53, p. 1000-1002) ; Titre VIII *Dispositions diverses* (art. 54-59,
  p. 1002) ; Titre IX *Dispositions transitoires* (art. 60-64, p. 1003).

### 1.2 Le régime d'organisation de 1985 (OCR, à contrôler à l'image)

- **Partage public/collectivités (art. 3-4, 9).** L'État et les collectivités locales
  organisent les transports ; l'exécution du service public régulier de personnes est
  assurée **soit en régie, soit par une entreprise ayant passé une convention** avec
  l'autorité compétente (art. 9). La convention fixe le contenu, le fonctionnement et le
  financement du service.
- **Régime d'autorisation des entreprises (art. 11, version d'origine 1985).** « Les
  entreprises de transport public de personnes doivent être **autorisées par le ministre
  des transports et des communications**. Les conditions de l'octroi de cette
  autorisation sont définies par décret. » Régime **centralisé** au ministre.
- **Transport urbain (art. 12).** Confié à une entreprise de transport « publique et
  privée » ; périmètre = territoire communal, extensible à plusieurs communes ou au-delà
  (délimitation fixée par le ministre).
- **Autres catégories de personnes (art. 13).** Services réguliers publics interurbains,
  transport rural, services occasionnels, voitures de louage, services touristiques,
  services privés. Les réguliers interurbains et le rural font l'objet de **conventions
  État/transporteur** ; les occasionnels, les louages et le touristique sont soumis à
  **autorisation du ministre**.
- **Transport de marchandises pour compte d'autrui (art. 14).** Subordonné à une
  **autorisation délivrée par le ministre**, retirable en cas de manquements graves ou
  répétés ; non cessible (art. 15) ; contrat obligatoire, à défaut contrats-types du
  ministère (art. 16). L'autorisation peut ne pas être exigée pour certaines catégories
  (art. 18).
- **Transport privé / compte propre.** Exclu du champ du transport public (art. 5).

### 1.3 Les modificatifs de la loi de 1985 : la décentralisation de l'autorisation

- **Loi n° 93-70 du 5 juillet 1993, modifiant la loi n° 85-77.** JORT n° 51 du 9 juillet
  1993, p. 955 (recid 112969 ; fascicule sans couche texte, **lu par OCR**). URL :
  https://www.pist.tn/jort/1993/1993F/Jo05193.pdf (vérifiée, 200). Article unique :
  **abroge et remplace les articles 11, 12 et 13** de la loi de 1985. Nouvel art. 11 :
  l'autorisation du transport public de personnes est accordée par **le président de la
  commune** (intérieur du périmètre communal), **le gouverneur** (intérieur du
  gouvernorat) et **le ministre du transport** (les autres cas) ; les gouverneurs du
  district de Tunis peuvent délivrer des autorisations pour tout le district. Premier
  pas de **décentralisation** du régime d'autorisation (de l'État central vers la commune
  et le gouvernorat).
- **Loi n° 96-60 du 6 juillet 1996, modifiant la loi n° 85-77.** JORT n° 55 du 9 juillet
  1996, p. 1376 (recid 112426 ; couche texte lisible). URL :
  https://www.pist.tn/jort/1996/1996F/Jo05596.pdf (vérifiée, 200). Article unique :
  **abroge et remplace l'article 11 (nouveau)** issu de 1993. Autorisation accordée par
  le président de la commune (périmètre communal), le gouverneur (gouvernorat), le
  ministre du transport (**plus d'un gouvernorat**) ; le ministre peut, par arrêté,
  habiliter le gouverneur à délivrer des autorisations hors limites du gouvernorat pour
  certaines catégories. **ATTENTION** : `jort_cache.db` date ce texte du « 6 septembre
  1996 » (date_signature 1996-09-06), mais le fascicule imprime **« Tunis, le 6 juillet
  1996 »** et le JORT n° 55 est daté du 9 juillet 1996 : retenir **6 juillet 1996**.
- **Décret n° 92-875 du 4 mai 1992** (recid 92453), fixant les modalités d'application
  des **amendes fiscales** prévues aux art. 20, 21 et 22 de la loi de 1985. JORT 1992,
  p. 613-615. Seul décret d'application de la loi de 1985 repéré dans le corpus
  (la loi renvoie à décret pour l'art. 11, l'art. 13 et l'art. 14 : ces décrets
  d'application de 1985-2004 ne sont pas identifiés — voir fiche de recherche § 5).

### 1.4 Le régime d'organisation de 2004 (texte relu, déchiffré et vérifié)

La loi de 2004 refond l'organisation. Faits saillants pour l'angle organisation :

- **Création des autorités régionales organisatrices des transports terrestres (ARO)**
  (art. 4, 6, 7 et suivants). L'État **et** les ARO organisent les transports et
  contrôlent leur fonctionnement, dans le cadre des plans de développement. Le
  **gouverneur** exerce les missions de l'ARO dans la limite de ses compétences (art. 7).
  Des missions de l'État peuvent être transférées à l'ARO **par décret** (art. 6, dernier
  alinéa) — mis en œuvre par le décret n° 2006-1470 (voir § 2).
- **Répartition des missions (art. 5-6).** L'État : études et plans directeurs,
  financement des infrastructures et du transport collectif public urbain et régional,
  fixation des tarifs et des règles de financement (renvoi compensation), conclusion des
  **contrats d'exploitation et de concession**, organisation du transport public
  interurbain, touristique, de marchandises et de la location. L'ARO : coordination,
  organisation du transport **urbain et régional** de personnes, plans directeurs
  régionaux.
- **Trois voies pour le transport public collectif régulier (art. 16).**
  (1) L'État **confie** aux **entreprises publiques** de transport terrestre la mission
  d'assurer le transport public collectif régulier, par **contrat d'exploitation** ;
  (2) ces entreprises peuvent, à la demande ou avec l'accord de l'État, **sous-traiter**
  à des transporteurs privés choisis selon les règles de la concurrence ;
  (3) l'État peut **confier par contrat de concession** le service à des transporteurs
  privés choisis selon les règles de la concurrence. Les clauses générales des contrats
  d'exploitation, de concession et de sous-traitance sont fixées par décret.
- **Définitions de périmètre (art. 13-15, 23 et renvois).** Transport **urbain** (à
  l'intérieur du périmètre de transport urbain = périmètre communal, extensible),
  **régional** (au-delà de l'urbain, dans la compétence de l'ARO), **interurbain** (le
  reste). Le transport public de personnes comprend le **régulier** (horaires, fréquences,
  tarif, itinéraire, arrêts fixés et publiés) et le **non régulier**.
- **Transport public routier non régulier (art. ~17 à 24).** Catégories : **taxi
  individuel**, **taxi collectif**, **taxi grand tourisme**, **voiture de louage**,
  **transport rural**, transport occasionnel. L'exercice est **soumis à autorisation
  délivrée par le gouverneur** (dans la limite des compétences de l'ARO) ou par le
  ministre (autres cas) ; les autorisations sont octroyées **après avis d'une commission
  consultative régionale** ; l'organisation (âge maximal des véhicules, itinéraires,
  règles d'exploitation) est fixée par arrêté du ministre.
- **Transport touristique (art. 25).** Soumis à **cahiers des charges et déclarations
  préalables** auprès des services du ministère ; liste des activités et cahiers des
  charges approuvés par arrêté conjoint transport/tourisme.
- **Transport de marchandises (art. 26-31).** Pour **compte propre** : libre, ni
  autorisation ni déclaration (art. 27). Pour **compte d'autrui** : en deçà d'un seuil de
  poids (fixé par arrêté), libre ; au-delà, soumis à **cahier des charges et déclaration
  préalable** (art. 28). **Centrales de fret** (art. 29-30) : cahier des charges +
  déclaration préalable. Dispositions spéciales (art. 31) : le ministre peut autoriser
  l'usage de véhicules de compte propre pour des transports de compte d'autrui pendant
  les saisons de production/transformation.
- **Location de véhicules (art. 32-33).** Soumise à cahier des charges et déclaration
  préalable ; le leasing en est exclu.
- **Conditions d'exercice (art. 34-36).** Conditions de **nationalité et qualification
  professionnelle** (fixées par décret), moralité (absence de condamnation), moyens
  matériels minimaux, cahier des charges ; avis d'un **Comité consultatif des transports
  terrestres** (art. 36).
- **Conduite (art. 40-41).** Les véhicules de transport public de personnes et de
  transport touristique ne peuvent être conduits que par une personne titulaire d'une
  **carte professionnelle** (nationalité, qualification, moralité ; modalités par décret).
- **Gares de transport terrestre (art. 42-44)** ; **infractions et sanctions, carte
  professionnelle, transaction** (art. 45-53) ; **dispositions transitoires** : restent
  valables les autorisations et inscriptions au registre des transporteurs antérieures
  (art. 60).
- **Bénéficiaires indirects / droit sur le transport collectif public (art. 11).** Les
  services sont financés par les usagers, l'État, les ARO et les **bénéficiaires
  indirects**, soumis à un droit dont l'assiette est renvoyée à décret (**domicile
  compensation/fiscalité** ; le décret n'est pas identifié — cf. chapitre compensation,
  fiche `r-transport-decret-manque-a-gagner`).

> **Fil conducteur de l'organisation, 1985 → 2004 :** d'un régime centralisé au ministre
> (1985), la décentralisation s'amorce par les lois de 1993 et 1996 (autorisation partagée
> commune/gouverneur/ministre), puis s'institutionnalise en 2004 avec les **autorités
> régionales organisatrices** et la trilogie **régie publique par contrat d'exploitation
> / concession à des privés / sous-traitance concurrentielle**.

### 1.5 Le modificatif de la loi de 2004

- **Loi n° 2006-55 du 28 juillet 2006, modifiant la loi n° 2004-33.** JORT n° 61 du
  [1er août] 2006, p. 1990 (recid 110314 ; couche texte chiffrée, déchiffrée ici). URL :
  https://www.pist.tn/jort/2006/2006F/Jo0612006.pdf (vérifiée, 200). Porte sur le **Titre
  VII (infractions et sanctions)** : réécrit notamment l'**article 48 (nouveau)** — mise
  en fourrière des véhicules en cas d'infractions relatives à l'**organisation du travail
  des transporteurs dans les gares de transport terrestre**. Modificatif ponctuel, sans
  toucher au régime d'autorisation/concession. Précédée de l'avis n° 21-2006 du Conseil
  constitutionnel (JORT même n°, p. 2008). **Non versée** à la bibliographie du précis.

### 1.6 Textes d'application de la loi de 2004 (inventaire corpus)

Tous dans `jort_cache.db`, relatifs à l'organisation (hors tarif) :

| Texte | Date | JORT (année / n° / p.) | Objet (organisation) |
|---|---|---|---|
| Arrêté | 17 août 2004 | 2004 / 69 / 2537 | autorisation temporaire véhicules non immatriculés (art. 39) |
| Arrêté | 1er sept. 2004 | 2004 / 73 / 2632 | commission de discipline (art. 53) |
| Arrêté | 12 oct. 2004 | 2004 / 84 / 2901-2902 | tenue/conduite du personnel à bord (art. 41) |
| Arrêté | 3 nov. 2004 | 2004 / — | liste des lignes interurbaines entre deux zones d'ARO limitrophes |
| Décret n° 2004-2410 | 14 oct. 2004 | 2004 / 85 / 2920-2921 | **commission consultative régionale** (art. 24) |
| Décret n° 2004-2576 | 2 nov. 2004 | 2004 / 90 / 3233 | agents habilités à constater les infractions |
| Décret n° 2004-2766 | 31 déc. 2004 | 2005 / 3 / 123-124 | **Comité consultatif des transports terrestres** (art. 36) |
| Décret n° 2004-2767 | 31 déc. 2004 | 2005 / 3 / 124-125 | règles de **coordination entre ARO** |
| Arrêté | 12 mai 2005 | 2005 / 40 / 1113-1115 | caution pécuniaire (art. 47) |
| Décret n° 2006-1470 | 30 mai 2006 | 2006 / 45 / 1491 | **transfert de missions de l'art. 6 à l'ARO** |
| Décret n° 2006-2118 | 31 juil. 2006 | 2006 / 63 / 2140-2156 | **nationalité et qualification professionnelle** (art. 22, 25, 28, 30, 33) |
| Décret n° 2008-2480 | 1er juil. 2008 | 2008 / 55 / 2048-2049 | documents d'exploitation (art. 38) |
| Arrêté | 19 août 2011 | 2011 / 63 / — | barème de la transaction (art. 47) |
| Décret n° 2012-512 | 29 mai 2012 | 2012 / 44 / 1355-1357 | complète le décret n° 2006-2118 (qualifications) |
| Décret n° 2012-1188 | 27 juil. 2012 | 2012 / — / 1911-1912 | modifie le décret n° 2004-2576 (agents verbalisateurs) |

*(URL pist.tn, édition française : `.../jort/<AAAA>/<AAAA>F/Jo0<NNN><AAAA>.pdf` pour
2000+, où NNN = n° à 3 chiffres ; pour les deux décrets publiés au JORT 2005 n° 3,
l'année d'URL est 2005. À finaliser par le bibliographe si cités.)*

### 1.7 Un régime d'opérateur nouveau (2025) — signal pour l'angle organisation

- **Arrêté conjoint du ministre des transports et du ministre de l'emploi et de la
  formation professionnelle du 4 novembre 2025, fixant les conditions d'exercice de
  l'activité de transport public collectif régulier de personnes par les sociétés
  communautaires** (recid 199905). Rattache les **sociétés communautaires** (« شركات
  أهلية », décret-loi n° 2022-15 du 20 mars 2022, modifié par le décret-loi n° 2025-3 du
  2 octobre 2025) au régime du transport public collectif régulier. Nouveau type
  d'opérateur à surveiller ; relève aussi, en partie, des entreprises publiques /
  économie sociale. **Non lu** ici (signalé pour suite).
- **Arrêté du ministre des transports du 30 septembre 2025** approuvant la modification du
  cahier des charges de l'activité de **transport routier de marchandises pour le compte
  d'autrui** (par des personnes morales), approuvé par l'arrêté du 10 décembre 2008
  (recid 199199). Confirme que le régime « cahier des charges » de l'art. 28 de la loi de
  2004 reste vivant. **Non lu** ici.

### 1.8 L'abrogation de 2025 (transport non urbain de la région) — DOMICILE FINANCES LOCALES

Déjà établi et domicilié au livre des finances locales
(`precis/fr/finances_locales/_competences.qmd`) — **ne pas re-sourcer** : la **loi
organique n° 2025-4 du 12 mars 2025** (relative aux conseils locaux, régionaux et de
districts), **art. 10**, abroge « les dispositions relatives à la région et au district »
du code des collectivités locales (loi organique n° 2018-29, art. 296) ; parmi les
compétences propres de la région ainsi abrogées figurait le **transport non urbain à
l'intérieur de la région**. Abrogation exécutoire le **14 mars 2025**. Clé CSL existante :
`@loi-org2025-4` ; URL https://www.pist.tn/jort/2025/2025F/Jo0302025.pdf. Le livre
transport n'en reçoit qu'**une phrase et un lien** vers finances locales (règle de
domicile, plan § 2).

### 1.9 Domicile compensation (rappel, une ligne — pas d'effort)

Les **arrêtés de 1948 et de 1957 sur les taxes de compensation sur les transports
automobiles** sont domicile compensation (déjà à son backlog ; cf.
`precis/fr/compensation/_transport.qmd`, tableau 1948-1982). Hors périmètre de ce ticket.

---

## 2. Références candidates (CSL-JSON)

### 2.1 Déjà présentes dans `precis/fr/compensation/references.json` (réutiliser la clé)

- `loi85-77` — Loi n° 85-77 du 4 août 1985, organisation des transports terrestres.
  **À enrichir** (voir § 4) : le périmètre de la fiche se limite à p. 1000-1001 / art. 7
  et 10 ; le texte complet (23 art., Titres I-VI) a été lu par OCR et porte aussi le
  régime d'organisation (art. 9, 11, 12, 13, 14) et la clause abrogatoire (art. 23).
- `loi2004-33` — Loi n° 2004-33 du 19 avril 2004, organisation des transports terrestres.
  **À enrichir** : ajouter les articles d'organisation relus (art. 4-7 ARO ; art. 13-16
  périmètres et contrats ; art. 28-31 marchandises ; art. 34-36 conditions d'exercice ;
  art. 40-41 carte professionnelle). Pages 996-1003.

### 2.2 À créer (CSL-JSON prêtes)

```json
[
  {
    "id": "loi93-70",
    "type": "legislation",
    "title": "Loi n° 93-70 du 5 juillet 1993, modifiant la loi n° 85-77 du 4 août 1985 portant organisation des transports terrestres",
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "51",
    "page": "955",
    "issued": {"date-parts": [[1993, 7, 5]]},
    "URL": "https://www.pist.tn/jort/1993/1993F/Jo05193.pdf",
    "title-short": "Loi n° 93-70 du 5 juillet 1993",
    "note": "citation-key: loi93-70\nJORT n° 51 du 9 juillet 1993, p. 955. Article unique : abroge et remplace les art. 11, 12 et 13 de la loi n° 85-77. Nouvel art. 11 : autorisation du transport public de personnes accordée par le président de la commune (périmètre communal), le gouverneur (gouvernorat) et le ministre du transport (autres cas) ; district de Tunis. Fascicule sans couche texte, lu par OCR (tesseract fra) le 10 novembre 2026 : à contrôler à l'image avant citation littérale. Source : docs/notes/transport-organisation-terrestre-2026-11-10.md."
  },
  {
    "id": "loi96-60",
    "type": "legislation",
    "title": "Loi n° 96-60 du 6 juillet 1996, modifiant la loi n° 85-77 du 4 août 1985 portant organisation des transports terrestres",
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "55",
    "page": "1376",
    "issued": {"date-parts": [[1996, 7, 6]]},
    "URL": "https://www.pist.tn/jort/1996/1996F/Jo05596.pdf",
    "title-short": "Loi n° 96-60 du 6 juillet 1996",
    "note": "citation-key: loi96-60\nJORT n° 55 du 9 juillet 1996, p. 1376. Article unique : abroge et remplace l'art. 11 (nouveau) de la loi n° 85-77 tel que modifié par la loi n° 93-70. Autorisation accordée par le président de la commune (périmètre communal), le gouverneur (gouvernorat), le ministre du transport (plus d'un gouvernorat) ; habilitation possible du gouverneur par arrêté du ministre. ATTENTION : jort_cache.db date ce texte du 6 septembre 1996, mais le fascicule imprime « 6 juillet 1996 » : retenir le 6 juillet 1996. Couche texte lisible (non chiffrée). Source : docs/notes/transport-organisation-terrestre-2026-11-10.md."
  },
  {
    "id": "loi2006-55",
    "type": "legislation",
    "title": "Loi n° 2006-55 du 28 juillet 2006, modifiant la loi n° 2004-33 du 19 avril 2004 portant organisation des transports terrestres",
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "61",
    "page": "1990",
    "issued": {"date-parts": [[2006, 7, 28]]},
    "URL": "https://www.pist.tn/jort/2006/2006F/Jo0612006.pdf",
    "title-short": "Loi n° 2006-55 du 28 juillet 2006",
    "note": "citation-key: loi2006-55\nJORT n° 61 de 2006, p. 1990. Modifie le Titre VII (infractions et sanctions) de la loi n° 2004-33 ; art. 48 (nouveau) : mise en fourrière pour infractions relatives à l'organisation du travail des transporteurs dans les gares de transport terrestre. Avis n° 21-2006 du Conseil constitutionnel (même JORT, p. 2008). Couche texte chiffrée (décalage), déchiffrée le 10 novembre 2026 : à relire à l'image avant citation littérale. Source : docs/notes/transport-organisation-terrestre-2026-11-10.md."
  },
  {
    "id": "loi78-40",
    "type": "legislation",
    "title": "Loi n° 78-40 du 6 juillet 1978, réglementant les transports publics et privés en commun de personnes",
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "49",
    "page": "1996",
    "issued": {"date-parts": [[1978, 7, 6]]},
    "URL": "https://www.pist.tn/jort/1978/1978F/Jo04978.pdf",
    "title-short": "Loi n° 78-40 du 6 juillet 1978",
    "note": "citation-key: loi78-40\nJORT n° 49 de 1978, p. 1996. Antécédent du transport en commun de personnes, abrogé par la loi n° 85-77 (art. 23). Non lue au fascicule ici (citée par la clause abrogatoire de la loi de 1985). Source : docs/notes/transport-organisation-terrestre-2026-11-10.md."
  },
  {
    "id": "decret2006-2118",
    "type": "legislation",
    "title": "Décret n° 2006-2118 du 31 juillet 2006, fixant les conditions relatives à la nationalité et à la qualification professionnelle de la personne désirant exercer l'une des activités prévues aux articles 22, 25, 28, 30 et 33 de la loi n° 2004-33 du 19 avril 2004 portant organisation des transports terrestres",
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "63",
    "page": "2140-2156",
    "issued": {"date-parts": [[2006, 7, 31]]},
    "URL": "https://www.pist.tn/jort/2006/2006F/Jo0632006.pdf",
    "title-short": "Décret n° 2006-2118 du 31 juillet 2006",
    "note": "citation-key: decret2006-2118\nJORT n° 63 de 2006, p. 2140-2156. Texte d'application de la loi n° 2004-33 : conditions de nationalité et de qualification professionnelle pour exercer les activités de transport (taxi, louage, marchandises pour compte d'autrui, centrales de fret, location). Complété par le décret n° 2012-512. Non lu au fascicule ici. Source : docs/notes/transport-organisation-terrestre-2026-11-10.md."
  },
  {
    "id": "decret2006-1470",
    "type": "legislation",
    "title": "Décret n° 2006-1470 du 30 mai 2006, portant transfert de certaines missions mentionnées à l'article 6 de la loi n° 2004-33 du 19 avril 2004 portant organisation des transports terrestres à l'autorité régionale organisatrice des transports terrestres",
    "container-title": "Journal officiel de la République tunisienne",
    "issue": "45",
    "page": "1491",
    "issued": {"date-parts": [[2006, 5, 30]]},
    "URL": "https://www.pist.tn/jort/2006/2006F/Jo0452006.pdf",
    "title-short": "Décret n° 2006-1470 du 30 mai 2006",
    "note": "citation-key: decret2006-1470\nJORT n° 45 de 2006, p. 1491. Met en œuvre le transfert de missions de l'État à l'autorité régionale organisatrice des transports terrestres (art. 6, dernier alinéa, loi n° 2004-33). Non lu au fascicule ici. Source : docs/notes/transport-organisation-terrestre-2026-11-10.md."
  }
]
```

*(Décrets 2004-2410, 2004-2766, 2004-2767, 2008-2480, décret-loi 2022-15 sur les
sociétés communautaires et arrêté du 4 novembre 2025 : entrées à créer seulement si le
rédacteur les cite ; coordonnées JORT au § 1.6 et § 1.7.)*

---

## 3. Notions à glossaire (pressenties)

Vérifier/compléter dans `precis/glossaire.yml` (ne pas éditer ici — propositions) :

- **Autorité régionale organisatrice des transports terrestres (ARO)** — AR « السلطة
  الجهوية لتنظيم النقل البري ». Source canonique : loi n° 2004-33, art. 4, 6, 7. Le
  gouverneur en exerce les missions ; organise le transport urbain et régional.
- **Transport public collectif régulier de personnes** — service à horaires, fréquences,
  tarif, itinéraire et arrêts fixés et publiés (loi n° 2004-33, art. 15).
- **Transport régional** (vs urbain vs interurbain) — au-delà du périmètre urbain, dans la
  compétence territoriale de l'ARO (loi n° 2004-33, art. 13-14).
- **Contrat d'exploitation / contrat de concession / sous-traitance** (transport public
  collectif) — trois voies de dévolution du service (loi n° 2004-33, art. 16).
- **Centrale de fret** — « مركز الشحن » : entreprise rapprochant offre et demande de
  transport de marchandises (loi n° 2004-33, art. 29).
- **Voiture de louage / taxi collectif / taxi grand tourisme / transport rural** —
  catégories du transport public routier non régulier (loi n° 2004-33, art. ~17-24).
- **Carte professionnelle** (conducteur de transport public/touristique) — loi n° 2004-33,
  art. 40.
- **Société communautaire** (« شركة أهلية ») appliquée au transport collectif régulier —
  décret-loi n° 2022-15 ; arrêté conjoint du 4 novembre 2025. (À confirmer : domicile
  possible aux entreprises publiques / économie sociale.)

---

## 4. Corrections et précisions à verser (bibliographe / rédacteur)

- **`@loi85-77` — périmètre de la fiche.** La note CSL actuelle dit « p. 1000-1001 »,
  art. 7 et 10 seulement. Le texte complet court **p. 1000-1001**, **23 articles**,
  Titres I à VI (OCR). Ajouter que la loi porte le régime d'organisation (art. 9, 11-14)
  et **abroge** (art. 23) le décret du 25 mai 1950 (marchandises) et la loi n° 78-40 de
  1978 (personnes). Les citations littérales OCR sont à contrôler à l'image.
- **`loi96-60` — date.** `jort_cache.db` porte « 6 septembre 1996 » : **erroné**. Le
  fascicule imprime **6 juillet 1996** (JORT n° 55 du 9 juillet 1996). Retenir cette date.
- **Titre de la loi de 2004 au fascicule.** L'intitulé imprimé est « portant organisation
  des transport**s** terrestres » (pluriel) ; `jort_cache.db` écrit parfois « transport
  terrestre » (singulier) pour 85-77/93-70/96-60 — forme de l'index, non du texte.

---

## 5. Lacunes et recherches infructueuses

### Lacunes (TODO à router)

1. **Décrets d'application de la loi de 1985** sur l'autorisation (art. 11), les catégories
   de personnes (art. 13) et le transport de marchandises (art. 14). Seul le décret n°
   92-875 (amendes fiscales, art. 20-22) est repéré. Les décrets d'octroi/retrait
   d'autorisation annoncés par les art. 11/13/14 ne sont pas identifiés — fiche § 5.2.
2. **Décret du 25 mai 1950** (réglementation des transports automobiles public et privé de
   marchandises), abrogé par la loi de 1985 : **antérieur à 1956, hors `jort_cache.db`**.
   À chercher au *Journal officiel tunisien* d'avant 1956 (famille de sources d'avant
   l'indépendance) ; **OCR requis**. Non trouvé ici.
3. **Clauses générales des contrats d'exploitation, de concession et de sous-traitance**
   (loi 2004, art. 16, renvoi à décret) : décret non identifié dans le corpus. À chercher
   (fiche § 5.2).
4. **Textes lus par OCR** (lois 93-70 de 1993 et 85-77 de 1985) : fidèles mais **à
   contrôler à l'image** avant toute citation entre guillemets.
5. **Textes d'organisation des ministères du Transport et de l'Équipement** (question du
   plan § 4) : **non traités** dans ce ticket (angle institution, hors T1). À instruire
   séparément.
6. **Sociétés communautaires dans le transport** (arrêté du 4 nov. 2025 ; décret-loi
   2022-15 modifié en 2025) : repérés, **non lus**. Suite à prévoir.

### Recherche infructueuse — fiche proposée pour `docs/recherches.yml`

**NE PAS écrire `recherches.yml` (consolidation parallèle)** — fiche complète ci-dessous,
à intégrer par l'humain :

```yaml
- id: r-transport-decrets-application-organisation
  objet: >-
    Décrets d'application, en matière d'ORGANISATION (hors tarif), des lois
    d'organisation des transports terrestres : (a) décrets d'octroi et de retrait
    des autorisations de transport public de personnes et de marchandises annoncés
    par les art. 11, 13 et 14 de la loi n° 85-77 du 4 août 1985 ; (b) décret fixant
    les clauses générales des contrats d'exploitation, de concession et de
    sous-traitance annoncé par l'art. 16 de la loi n° 2004-33 du 19 avril 2004.
  ou: jort_cache.db (~/projets/PDFs-legislation-tunisie) ; pist.tn (édition française)
  requetes:
    - source: titres_fts
      termes: ["transports terrestres autorisation", "contrat exploitation concession transport", "transport public personnes autorisation decret"]
    - source: titres_like
      termes: ["%85-77%", "%2004-33%concession%", "%contrat%exploitation%transport%"]
    - source: iort_ar
      termes: ["النقل البري", "رخصة النقل", "عقد استغلال", "لزمة النقل العمومي"]
  passe:
    - date: 2026-11-10
      resultat: aucun
      couverture: >-
        jort_cache.db interrogé sur titres FR et LIKE ; trouvés seulement le décret
        n° 92-875 (amendes fiscales, art. 20-22 de la loi de 1985) et les textes
        d'application de la loi de 2004 déjà inventoriés (décrets 2004-2410,
        2004-2576, 2004-2766, 2004-2767, 2006-1470, 2006-2118, 2008-2480, 2012-512,
        2012-1188 ; arrêtés 2004-2011). Aucun décret « octroi/retrait d'autorisation »
        propre à la loi de 1985, ni décret « clauses générales des contrats
        d'exploitation/concession/sous-traitance » de l'art. 16 de 2004 n'est repéré.
        Terme arabe à rejouer sur le miroir iort (période post-2011 non concernée pour
        1985/2004, mais utile pour d'éventuels textes d'application récents).
      couvert_jusqu_au: 2026-10-29
      sources: [titres_fts, titres_like]
```

---

## 6. Backlog (lignes proposées — NE PAS écrire dans docs/notes/backlog-precis.md ici)

- **[transport/organisation]** Relire à l'image (fascicules JORT) les lois n° 85-77
  (1985, OCR) et n° 93-70 (1993, OCR) avant toute citation littérale ; vérifier la date
  de la loi n° 96-60 (6 juillet 1996, non 6 septembre).
- **[transport/organisation]** Chercher le **décret du 25 mai 1950** (transports
  automobiles de marchandises) au *Journal officiel tunisien* d'avant 1956 ; OCR requis.
- **[transport/organisation]** Identifier les **décrets d'application** des art. 11/13/14
  de la loi de 1985 et le **décret « clauses des contrats »** de l'art. 16 de 2004 (fiche
  `r-transport-decrets-application-organisation`).
- **[transport/institution]** Instruire les **textes d'organisation des ministères** du
  Transport et de l'Équipement (hors ce ticket).
- **[transport/organisation]** Lire l'**arrêté conjoint du 4 novembre 2025** (sociétés
  communautaires / transport collectif régulier) et le **décret-loi n° 2022-15** modifié
  par le décret-loi n° 2025-3 ; trancher le domicile (transport vs entreprises publiques /
  économie sociale).
- **[bibliographe]** Verser les clés `loi93-70`, `loi96-60`, `loi2006-55`, `loi78-40`,
  `decret2006-2118`, `decret2006-1470` (CSL § 2.2) ; enrichir `@loi85-77` et `@loi2004-33`
  (§ 4).
- **[glossaire]** Ajouter/vérifier les notions du § 3 (ARO, transport régulier, contrats
  d'exploitation/concession, centrale de fret, catégories de taxis/louage/rural, carte
  professionnelle).

---

*PDF sources : fascicules JORT dans le corpus local `~/projets/PDFs-legislation-tunisie`
(hors git), catalogués dans `jort_cache.db` ; aucune étude/rapport externe à archiver
pour ce ticket (matière 100 % législative). URL pist.tn vérifiées le 10 novembre 2026
(codes 200) pour les lois 78-40, 85-77, 93-70, 96-60, 2004-33, 2006-55.*

---

## Complément — contrôle à l'image G4 : loi 85-77 (10 novembre 2026)

Contrôle à l'image de l'OCR de T1. Pages lues en image (pdftoppm, premier plan, aucun
processus laissé tourner) : édition **française** `Jo05885.pdf` p. 1000-1001 (= pages PDF 4-5)
et édition **arabe** `Ja05885.pdf` p. 1010-1011 (= pages PDF 4-5), corpus local
`~/projets/PDFs-legislation-tunisie/PDFs/JORT/1985/{fr,ar}/`. **Verdict d'ensemble : l'OCR de
T1 est fidèle ; tous les points contrôlés sont confirmés, aucune correction de fond.**

### Points vérifiés (OCR vs image)

- **Nombre d'articles = 23 — CONFIRMÉ.** Dernier article lu à l'image : art. 23 (clause
  abrogatoire), suivi de la formule de promulgation. Aucun article au-delà.
- **Nombre de titres = 6 — CONFIRMÉ.** À l'image (FR) : Titre premier *Principes généraux* ;
  Titre II *Le transport ferroviaire* ; Titre III *Le transport routier des personnes*
  (ch. I *Dispositions communes*, ch. II *Le transport urbain de personnes*, ch. III *Les
  autres catégories de transports de personnes*) ; Titre IV *Le transport routier de
  marchandises* ; Titre V *Des sanctions* ; Titre VI *Dispositions diverses*. Soit 6 titres.
  Côté arabe : العنوان الأول/الثاني/الثالث/الرابع/الخامس/السادس — mêmes six, mêmes intitulés
  (احكام عامة / النقل الحديدي / نقل الاشخاص بالطرقات / نقل البضائع على الطرقات / في العقوبات /
  احكام مختلفة).
- **Répartition articles ↔ titres — CONFIRMÉE** telle que T1 l'a donnée : Titre I art. 1-7 ;
  Titre II art. 8 ; Titre III art. 9-13 (ch. I 9-11, ch. II 12, ch. III 13) ; Titre IV
  art. 14-18 ; Titre V art. 19-22 ; Titre VI art. 23.
- **Régime d'autorisation centralisé au ministre (art. 11) — CONFIRMÉ**, citation littérale
  exacte à l'image.
  - FR (p. 1000) : « **Art. 11. — Les entreprises de transport public de personnes doivent
    être autorisées par le ministre des transports et des communications. Les conditions de
    l'octroi de cette autorisation sont définies par décret.** »
  - AR (p. 1010), citation arabe exacte : « **الفصل 11 ـ تخضع مؤسسات النقل العمومي للاشخاص
    لترخيص من وزير النقل والمواصلات . وتضبط شروط هذا الترخيص بأمر .** » (noter : l'arabe dit
    « بأمر » — par décret/arrêté — là où le français dit « par décret »).
- **Art. 9 (régie ou convention) — CONFIRMÉ.** FR : « L'Etat et, dans la limite de leurs
  compétences, les collectivités publiques locales organisent les transports publics réguliers
  de personnes. L'exécution du service est assurée soit en régie, soit par une entreprise ayant
  passé à cet effet une convention avec l'autorité compétente… » (T1 avait « collectivités
  locales » ; le texte imprime « collectivités **publiques** locales » — nuance mineure, non
  substantielle). AR : « الفصل 9 ـ تتولى الدولة وكذلك الجماعات العمومية المحلية في حدود
  مشمولاتها تنظيم النقل العمومي المنتظم للاشخاص … اما مباشرة واما من طرف مؤسسة ابرمت لهذا الغرض
  اتفاقية … ».
- **Art. 12 (transport urbain « publique et privée ») — CONFIRMÉ.** FR : « Le transport urbain
  de personnes est confié à une entreprise de transport publique et privée. Le périmètre de
  transport urbain comprend en principe le territoire communal… »
- **Art. 13 (autres catégories) — CONFIRMÉ** : services réguliers publics interurbains,
  services publics de transport rural, services occasionnels publics, services effectués par
  voitures de louages, services touristiques, services privés ; interurbains et rural par
  **convention** État/transporteur ; occasionnels, louages et touristique par **autorisation du
  ministre**.
- **Art. 14 (marchandises pour compte d'autrui soumis à autorisation du ministre) — CONFIRMÉ.**
  FR : « Le transport de marchandises pour le compte d'autrui est subordonné, selon des
  modalités fixées par décret, à l'octroi d'une autorisation délivrée par le ministre des
  transports et des communications. Les autorisations peuvent être retirées en cas de
  manquements graves ou répétés… » AR : « الفصل 14 ـ يخضع نقل البضائع لحساب الغير لترخيص من وزير
  النقل والمواصلات حسب شروط تضبط بأمر … ».
- **Art. 5 (compte propre hors transport public) — CONFIRMÉ.** FR : « Sont considérés comme
  transports publics, tous les transports de personnes ou de marchandises, à l'exception des
  transports qu'organisent pour leur propre compte des personnes publiques ou privées. »
- **Art. 23 (clause abrogatoire / antécédents) — CONFIRMÉ** mot pour mot. FR (p. 1001) :
  « Art. 23. — Sont abrogées toutes dispositions antérieures contraires à la présente loi et
  notamment : — Le décret du 25 mai 1950 portant réglementation de transports automobiles public
  et privé de marchandises et les décrets subséquents. — La loi n° 78-40 du 6 juillet 1978
  réglementant les transports publics et privés en commun de personnes. » AR (p. 1011) :
  « الفصل 23 ـ ألغيت جميع الاحكام السابقة المخالفة لهذا القانون وخاصة : ـ الأمر المؤرخ في 25 ماي
  1950 والمتعلق بتنظيم النقل العمومي والنقل الخاص للبضائع بواسطة السيارات وما صدر بعده من الأوامر .
  ـ القانون عدد 40 لسنة 1978 المؤرخ في 6 جويلية 1978 والمتعلق بتنظيم النقل العمومي والنقل الخاص
  المشترك للاشخاص . »
- **Promulgation — CONFIRMÉ.** FR : « Fait au palais de Skanès, le 4 août 1985 — Le Président de
  la République tunisienne, HABIB BOURGUIBA ». AR : « وصدر بقصر صقانص في 4 اوت 1985 ».
- **Travaux préparatoires (adoption Chambre des députés le 23 juillet 1985) — CONFIRMÉ** par la
  note (1) de la version française (« Discussion et adoption par la Chambre des députés dans sa
  séance du 23 juillet 1985 »). *Garde-fou lié :* la note (1) de l'édition arabe au bas de la
  p. 1011 (« … بتاريخ 30 جويلية 1985 ») se rapporte à la **loi 85-78** imprimée juste après, non
  à la loi 85-77 — ne pas la confondre avec la date d'adoption de la loi des transports.

### Points corrigés

- **Aucune correction de fond.** Seule nuance de littéralité relevée à l'art. 9 : le texte
  imprime « collectivités **publiques** locales » (T1 abrégeait en « collectivités locales ») —
  à retenir pour toute citation littérale. L'OCR tesseract de T1 n'a donc rien déformé sur les
  points à enjeu (comptage articles/titres, régime d'autorisation, clause abrogatoire).

### Reste illisible à l'image

- **Rien.** Les pages FR 1000-1001 et AR 1010-1011 sont nettes et intégralement lisibles ; toutes
  les citations littérales proposées par T1 sont désormais contrôlées à l'image et peuvent être
  citées telles quelles. La note CSL `@loi85-77` peut être enrichie (cf. § 4) sans réserve « OCR
  à contrôler ».

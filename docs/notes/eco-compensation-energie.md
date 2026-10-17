# Fiche économiste : la compensation de l'énergie (carburants, électricité, gaz)

*Fiche pilote du rôle « économiste », établie le 17 octobre 2026. Elle sert de source à la
section « Ce qu'en dit l'économie » du volume « Compensation », qui en sera le résumé (une page
au plus). Elle ne recommande rien. Aucun de ses chiffres n'est un paramètre : aucun n'entre dans
un tableau de paramètres, une figure de série ou le modèle.*

Elle s'appuie sur le chapitre d'incidence (`precis/fr/compensation/_incidence.qmd`), qui expose
déjà, avec leur méthode, la note de la Banque mondiale de 2013, le document de travail de 2015
et l'étude CEQ de 2017. Elle ne refait pas leurs fiches : elle les situe dans le savoir général.
Les pages citées sont celles qui sont imprimées sur les documents.

---

## 1. La question

**Ce que dit le droit.** Le droit et le budget tunisiens parlent de prix administrés, fixés
au-dessous du coût, dont l'écart est « compensé » (chapitres `_carburants.qmd` et
`_electricite_gaz.qmd`).

**Ce que demande l'économiste.** Il pose au dispositif quatre questions distinctes.

1. **Stabiliser ou transférer.** Selon la revue de Verme sur le Moyen-Orient et l'Afrique du
   Nord, les caisses de compensation du Maghreb ont été conçues comme des mécanismes de
   *stabilisation* des prix, puis sont devenues des systèmes de *subvention*. Trois facteurs
   l'expliquent selon l'auteur :
   - la hausse tendancielle des prix nominaux ;
   - une asymétrie politique : il est commode de ne pas répercuter une hausse mondiale, malaisé
     de garder un prix intérieur élevé quand le prix mondial baisse ;
   - les intérêts constitués autour de la subvention [Verme 2018, p. 2-3].

   Le mémorandum de la Banque mondiale de 1985 fait la même lecture pour la Caisse générale de
   compensation (`_exterieurs.qmd`, clé `bm-1985-cem-5328-vol2`).
2. **À qui va le transfert.** C'est la question de l'[incidence](#g-incidence-des-subventions). Une
   subvention au prix verse à chacun un montant proportionnel à sa consommation. L'économiste
   mesure trois choses :
   - la part reçue par chaque quintile ou décile de niveau de vie ;
   - le poids de cette subvention dans la dépense de chaque groupe ;
   - le coût pour le budget d'un dinar effectivement reçu par les ménages pauvres.
3. **Ce que coûte le transfert à l'économie.** Il y a d'abord la perte sèche : on consomme des
   unités dont la valeur pour l'acheteur est inférieure à leur coût d'opportunité. S'y ajoutent les
   effets sur l'investissement et sur la qualité du service quand l'entreprise qui vend à perte
   n'est pas remboursée, et le coût d'opportunité des fonds publics.
4. **Ce que coûte le dispositif, budgété ou non.** Le coût économique est l'écart entre le prix
   payé et le coût d'opportunité du produit, quel que soit celui qui le porte : le budget, une
   entreprise publique ou une ressource de l'État cédée au-dessous de sa valeur.

**Trois vocabulaires qui ne se recouvrent pas.** C'est la clé de la particularité tunisienne : une
subvention par le prix du gaz et une ligne budgétaire coexistent dans les comptes de la STEG.

| Vocabulaire | Terme | Ce qu'il désigne | Exemple tunisien |
|---|---|---|---|
| Budget et rapport de contrôle de 2014 (le précis) | [subvention directe](#g-subvention-directe) | transfert inscrit en dépense (ligne « carburants ») | part de la ligne versée à la STEG (@tbl-compensation-carburants-beneficiaires) |
| idem | [subvention indirecte](#g-subvention-indirecte) | manque à gagner non inscrit en dépense, né d'un [prix de cession préférentiel](#g-prix-de-cession-preferentiel) | gaz cédé à la STEG à un prix fixe jusqu'en 2014 (@tbl-compensation-prix-cession) |
| Comptes de la STEG (2007-2014) | « subvention d'exploitation » | à partir de 2007, écart entre la valeur économique du gaz et son prix de cession, comptabilisé en produit, plus la subvention d'équilibre de l'État [@steg-ef-2014, p. 23 et 35] | coïncide avec la subvention totale du rapport de contrôle avant 2015, avec la ligne budgétaire en 2015 (@tbl-compensation-eg-rapprochement, @sec-compensation-eg-2015) |
| FMI (Coady et al. 2019 ; Black et al. 2023) | subvention *explicite*, ou « pre-tax » | (coût d'approvisionnement unitaire − prix payé) × quantité, que le coût soit porté « directement par le budget » ou « indirectement sous forme de pertes ou de profits réduits des entreprises publiques » [Black et al. 2023, p. 8] | les deux étages tunisiens, direct et indirect, ensemble |
| idem | subvention *implicite*, ou complément « post-tax » | sous-tarification des coûts environnementaux et taxe générale sur la consommation non perçue [Black et al. 2023, p. 8] | sans équivalent dans les pièces budgétaires tunisiennes |

Le coût d'approvisionnement du FMI est un coût d'opportunité. Pour un produit échangé, c'est le
prix d'importation ou d'exportation, marges de transport et de distribution comprises. Pour
l'électricité, c'est le coût de production intérieur. Pour le gaz, c'est une moyenne des prix
intérieur et international pondérée par l'origine de la consommation [Black et al. 2023, p. 12].

Deux conséquences pour le lecteur du précis :

- **Les mots trompent.** La « subvention indirecte » du précis relève de la subvention
  *explicite* du FMI, et non de son « implicite ».
- **La rupture de 2015 change le porteur, pas la nature.** Avant 2015, une part de la subvention
  explicite était portée par l'ETAP et par les ressources de l'État cédées à bas prix, dont la
  redevance en nature sur le gaz algérien. Après 2015, elle passe par le budget. La rupture
  comptable de 2007 dans les comptes de la STEG est l'inscription en produits de cette part
  jusque-là invisible.

Le même partage explique pourquoi les séries ne se raccordent pas. La ligne budgétaire mesure le
premier étage, le rapport de contrôle de 2014 les deux étages, et la série du FMI de 2016 des flux
bruts reconstitués (`_exterieurs.qmd`). Ce sont des séries observées ou reconstituées. Les
montants des études d'incidence sont des évaluations, faites à un prix de référence choisi par
leurs auteurs.

## 2. Ce que dit la théorie

**R1. Au premier ordre, la perte d'un ménage est sa part budgétaire multipliée par la hausse de
prix.**
- *Le résultat.* Doubler le prix d'un bien qui pèse 5 % de la consommation équivaut, à quantités
  inchangées, à une baisse de 5 % du revenu réel [Arze del Granado, Coady et Gillingham 2010,
  p. 6-7].
- *Les hypothèses.* Le résultat est exact pour une petite variation de prix. Pour une grande, il
  surestime la perte, faute de substitution ; les auteurs le lisent comme un effet de court terme
  ou comme une borne haute de long terme. Aucune des études de leur revue n'en corrige l'effet
  [p. 7].
- *L'effet indirect.* Il se calcule par un tableau entrées-sorties : la hausse est répercutée
  entièrement sur les prix des biens qui emploient l'énergie, sans substitution dans la
  production.
- *Pour la Tunisie.* Les études tunisiennes de 2013 et de 2015 sont toutes deux bâties ainsi. La
  borne haute pèse surtout là où la hausse simulée est forte : +214 % pour le gaz de pétrole
  liquéfié (GPL) dans la note de 2013, subvention de 68 % du prix non subventionné dans le
  document de 2015.

**R2. La perte sèche croît comme le carré de la subvention unitaire.**
- *Le résultat.* Vendre au-dessous du coût permet des transactions dont la valeur pour l'acheteur
  est inférieure au coût d'opportunité. La perte croît avec l'élasticité de la demande à long terme
  et « approximativement avec le carré » de la subvention unitaire. Elle se concentre donc là où le
  taux de subvention est le plus élevé [Davis 2013, p. 4-5].
- *Les hypothèses.* Offre parfaitement élastique, demande à élasticité constante de −0,6 ; la perte
  est de 18 % plus élevée avec −0,8. Les externalités (pollution, congestion) l'augmentent
  [Davis 2013].

**R3. Une subvention au prix ne cible que si le bien pèse plus dans la dépense des pauvres.**
- *Le résultat d'Atkinson et Stiglitz.* Si les préférences sont séparables entre travail et
  consommation et identiques entre ménages, un impôt sur le revenu non linéaire suffit à
  redistribuer, et taxer ou subventionner les biens n'ajoute rien. Les estimations économétriques
  ne soutiennent pas cette séparabilité [Currie et Gahvari 2008, version de travail, p. 33].
- *L'auto-ciblage.* Quand l'État ne peut pas observer les revenus, un transfert en nature peut
  séparer pauvres et non-pauvres, à condition de porter sur un bien, ou une qualité, que seuls les
  premiers recherchent [Currie et Gahvari 2008, p. 9-10].
- *Pour l'énergie.* La part budgétaire de l'énergie croît avec le revenu pour l'essence et le
  gasoil. Elle est plate pour le GPL dans les pays où tous les ménages cuisinent au gaz. Pour
  l'électricité, la consommation au compteur n'est qu'un signal faible du revenu.
- *Les subventions par quantité.* Selon la synthèse de Komives et al., les tarifs progressifs par
  tranches de l'eau et de l'électricité sont le plus souvent régressifs dans leur distribution.
  Réduire la taille de la première tranche « sociale » n'améliore que peu le ciblage, et la
  sélection administrative des bénéficiaires fait mieux, avec ses propres difficultés
  [Komives et al. 2005, p. 6-7].

**R4. Vendre au-dessous du coût, sans remboursement, dégrade le service.**
- *L'argument.* Burgess, Greenstone, Ryan et Sudarshan proposent une chaîne en quatre étapes, à
  partir surtout du cas de l'Inde :
  1. subventions, vols et impayés sont tolérés ;
  2. le distributeur perd de l'argent sur chaque unité vendue, jusqu'à ce que la contrainte
     budgétaire de l'État joue ;
  3. il rationne l'offre, par l'accès et par les heures de fourniture ;
  4. le lien entre paiement et fourniture se rompt : qui ne paie pas reçoit la même qualité de
     service que qui paie.

  Les auteurs y voient un équilibre de basse qualité et de bas paiement [Burgess et al. 2020,
  p. 146].
- *Sa portée.* C'est un argument de synthèse, fondé sur des travaux indiens, et non une mesure
  générale.

## 3. Ce que mesure l'empirique

### 3.1 Les synthèses internationales

**L'ampleur, par la méthode de l'écart de prix.** Les montants suivants sont des évaluations du
FMI, et non des séries budgétaires.

| Synthèse | Champ | Subvention explicite (« pre-tax ») | Total avec l'implicite (« post-tax ») |
|---|---|---|---|
| Clements et al. 2013 [résumé] | 176 pays, 2011 | 480 milliards de dollars, 0,7 % du PIB mondial | 1 900 milliards, 2,5 % |
| Black et al. 2023 [résumé] | 2022 | 1 300 milliards de dollars, contre 500 milliards en 2020 | 7 000 milliards, 7,1 % du PIB mondial |

Le doublement de 2020 à 2022 de la subvention explicite tient, selon Black et al., en grande
partie à des mesures temporaires de soutien des prix.

**L'incidence des carburants, en montant.** Les deux revues du FMI recalculent les études nationales
pour une hausse commune de 0,25 dollar par litre.

| Revue | Échantillon | Rapport du 5^e^ au 1^er^ quintile, toutes subventions | Essence | GPL |
|---|---|---|---|---|
| Arze del Granado, Coady et Gillingham 2010 [p. 4 et 11-12, tableau 5] | 20 pays d'Afrique, d'Asie, du Moyen-Orient et d'Amérique latine ; études de 2005 à 2009 | environ 6 | 20 | 14 |
| Coady, Flamini et Sears 2015 [p. 12-13] | 32 pays, études jusqu'en 2014 | plus de 6 | 27 | 12 |

- *Les parts.* Dans la première revue, en moyenne des études, le quintile le plus aisé reçoit
  61,3 % de la subvention directe à l'essence, 53,8 % de celle au GPL et 20,6 % de celle au
  pétrole lampant [Arze del Granado et al. 2010, tableau 5].
- *Le coût d'un dinar transféré.* Faire parvenir 1 dollar aux 40 % les plus modestes coûte environ
  14 dollars par une subvention à l'essence, car 93 dollars sur 100 vont aux trois quintiles
  supérieurs, et environ 3 dollars par le pétrole lampant [Coady et al. 2015, p. 13]. Les auteurs
  opposent à ces chiffres un programme ciblé *hypothétique*, à 1,5 dollar : ce n'est pas une
  mesure.

**L'incidence des carburants, en part de la consommation.** La hausse de 0,25 dollar par litre
réduit le revenu réel d'environ 6 % en moyenne, selon une distribution « approximativement
neutre » entre quintiles.
- La perte va de 3,8 % en Amérique du Sud et centrale à 9,6 % au Moyen-Orient.
- L'effet indirect en fait plus de la moitié : plus de 60 % en Afrique et en Amérique latine,
  moins de 45 % en Asie et au Moyen-Orient [Arze del Granado et al. 2010, résumé et p. 8].
- La seconde revue situe l'effet indirect à 55 % en moyenne [Coady et al. 2015, p. 11].

**L'effet indirect selon le produit.** Les simulations réunies par Verme et Araar portent sur trois
pays : Maroc, Tunisie et Jordanie.
- Pour l'électricité, l'effet indirect forme environ 40 % de l'effet total : 36,6 % au Maroc,
  40,7 % en Tunisie, 41 % en Jordanie.
- Pour le gasoil, il en forme de 77 % à 89 % [Verme 2018, p. 22-23, tableau 3].

**L'électricité.** La synthèse de Komives et al. mesure le ciblage par un indicateur Ω : la part
de la subvention reçue par les pauvres, rapportée à leur part dans la population. Ω vaut 1 pour
une distribution neutre et moins de 1 pour une distribution régressive.
- Pour les subventions à l'électricité par quantité, Ω va de 0,20 (Guatemala) à 1,00 (Gujarat) ;
  la plupart des cas sont sous 1 [Komives et al. 2005, p. 72-73, tableau 5.1].
- Le résultat dépend d'abord de l'accès au réseau, du raccordement effectif et du comptage, puis
  du taux de subvention et des quantités.
- Les études réunies datent d'avant 2005. Plusieurs cas sont simulés.

**La perte sèche.** En 2012, les subventions routières à l'essence et au gasoil sont estimées à
110 milliards de dollars, et la perte sèche annuelle mondiale à 44 milliards. L'Arabie saoudite et
le Venezuela en portent la moitié [Davis 2013, résumé et p. 5].

**Les réformes.** Les évaluations sont surtout des classements de cas et des simulations ;
rares sont les mesures causales ex post.

- *Vingt-deux études de cas du FMI.* Elles couvrent 28 épisodes de réforme : 12 réussis,
  11 partiellement réussis (retours en arrière ou mise en œuvre incomplète), 5 échoués. Le
  classement est fait par les services du FMI [Clements et al. 2013, p. 21]. La synthèse en tire
  six éléments communs aux épisodes classés réussis :
  - un plan d'ensemble ;
  - une communication ;
  - des hausses échelonnées ;
  - l'efficacité des entreprises publiques ;
  - des mesures ciblées ;
  - des mécanismes de prix automatiques [résumé].
- *Le Moyen-Orient et l'Afrique du Nord, 2010-2014.* Verme distingue deux familles de réforme
  [Verme 2018, p. 17-18] :
  - des réformes radicales avec transferts monétaires massifs (Iran, Jordanie) ;
  - des réformes graduelles sans compensation monétaire générale (Maroc, Tunisie).

  Il écrit que la réponse à la question de savoir laquelle a mieux réussi « n'est pas univoque ».
- *L'Iran, 2010.* La consommation d'essence et de GPL baisse d'environ 10 %. Les simulations
  jugent les transferts excessifs et largement captés par les non-pauvres, et la réforme est
  partiellement défaite en 2012 [Verme 2018, p. 11]. Sur le même programme, une étude
  économétrique sur données de panel, en effets fixes et en différence de différences, mesure des
  transferts égaux à 29 % du revenu médian. Elle ne trouve pas de baisse de l'offre de travail, sauf
  chez les jeunes [Salehi-Isfahani et Mostafavi-Dehzooei 2017, résumé].
- *Le Maroc, 2014.* L'« évaluation ex post » de la réforme est une microsimulation sur l'enquête
  de 2007, extrapolée à 2014 [Verme et El-Massnaoui 2015, résumé et p. 8].
  - Selon la revue de Verme, la réforme n'a probablement pas eu d'effet sur la pauvreté ni sur
    l'inégalité. Elle a supprimé la subvention des produits les plus favorables aux aisés,
    l'essence d'abord, et ne relevé l'électricité que sur les tranches hautes, sans transfert
    compensatoire [Verme 2018, p. 15-16].
  - Le GPL reste le produit dont la réforme coûterait le plus aux pauvres [Verme et
    El-Massnaoui 2015, résumé].
- *L'indexation automatique.* Ce que l'on mesure ici, c'est la transmission des prix mondiaux aux
  prix intérieurs, et non l'effet des mécanismes.
  - Pendant la hausse des cours de 2007 et du premier semestre 2008, plus de la moitié des pays
    en développement ont transmis moins des deux tiers de la hausse du prix mondial du gasoil.
    Au Moyen-Orient et en Afrique du Nord, la moitié des pays en ont transmis moins de 13 %
    [Coady et al. 2015, p. 4-5, tableau 1].
  - Les mécanismes réintroduits en 2012-2014 (Jordanie, Mauritanie, Maroc, Tunisie) sont décrits
    par le FMI [Sdralevich et al. 2014, p. 48].
  - Aucune évaluation d'impact de ces mécanismes n'a été retrouvée ici. La Banque mondiale note
    que les formules tunisiennes de 2014 et de 2016 n'ont pas été appliquées systématiquement
    [Banque mondiale 2023, p. 19].

**Les élasticités-prix de la demande d'énergie.**

| Synthèse | Champ | Court terme | Long terme |
|---|---|---|---|
| Labandeira, Labeaga et López-Otero 2017 (version de travail de 2015) [p. 10, tableau 3, et p. 16] | méta-analyse ; 416 articles de 1990 à 2014 ; 951 élasticités de court terme et 991 de long terme | énergie : −0,22 en moyenne ; électricité −0,20, gaz naturel −0,18, essence −0,19, gasoil −0,16 ; usage résidentiel −0,22 ; pays en développement −0,18 | énergie : −0,65 en moyenne ; électricité −0,52, gaz naturel −0,57, essence −0,53, gasoil −0,39 ; résidentiel −0,62 ; pays en développement −0,55 |
| Havranek, Irsova et Janda 2012 (version de travail) [résumé, p. 11] | essence ; études publiées de 2000 à 2011 ; pays divers | moyenne brute −0,23 ; corrigée du biais de publication −0,09 (intervalle de 95 % : −0,12 à −0,07) | moyenne brute −0,69 ; corrigée −0,31 (−0,38 à −0,25) |
| Kudela, Havranek, Irsova et al. 2026, prépublication non évaluée par les pairs [résumé] | électricité ; 4 720 estimations de 462 études, données de 1934 à 2024 | corrigée du biais de publication −0,16 ; −0,09 pour les études les mieux identifiées, non distincte de zéro | −0,38 |

### 3.2 La Tunisie et la région

Les études d'incidence tunisiennes sont exposées, avec leur méthode, dans
`precis/fr/compensation/_incidence.qmd`. Elles se situent ainsi dans le savoir général.

- **Carburants.** La note de la Banque mondiale de 2013 porte sur l'enquête de 2010, aux prix
  d'avril 2013. Le 5^e^ quintile y reçoit 67 % de la subvention directe à l'essence, le 1^er^ 1 % ;
  pour le gasoil, les parts sont de 59 % et 2 % [@bm-2013-82712, figures 11 et 12]. C'est plus
  concentré que la moyenne internationale d'Arze del Granado et al., 61,3 % pour l'essence, et
  dans le même sens.
- **GPL.** La même note donne 22 % au 5^e^ quintile et 15 % au 1^er^ : la distribution est presque
  plate. La moyenne internationale est de 53,8 %. L'écart tient à l'usage quasi général du GPL
  pour la cuisine en Tunisie ; c'est une interprétation, que la note ne chiffre pas.
- **Électricité.** Les deux études de la Banque mondiale ne mesurent pas la même chose, et leur
  gradient diffère du simple au double.

  | Étude | Ce qu'elle mesure | 1^er^ quintile | 5^e^ quintile | Rapport du 5^e^ au 1^er^ |
  |---|---|---:|---:|---:|
  | Note de 2013 [@bm-2013-82712, figures 11 à 13] | part de la subvention à « électricité et gaz » | 13 % | 29 % | environ 2,2 |
  | idem | subvention à l'électricité par tête | 17 D | 39 D | environ 2,3 |
  | Document de 2015 [@bm-2015-wps7312, tableaux 3, 7 et 8] | subvention à l'électricité par tête | 36,99 D | 48,89 D | environ 1,3 |

  - La note de 2013 part de la grandeur comptable de la STEG : la subvention d'exploitation
    convertie en « équivalent-prix ».
  - Le document de 2015 part d'un prix de référence unique de 0,268 D par kWh, appliqué tranche
    par tranche. La subvention y devient négative au-delà de 300 kWh par mois, où le ménage paie
    plus que ce prix.
  - Selon la méthode, l'électricité est donc nettement ou faiblement plus subventionnée en montant
    chez les aisés. Les montants sont des évaluations aux prix d'avril 2013 et de mai 2014, non des
    séries observées.
- **En part de la dépense.** La subvention pèse 8,8 % de la dépense au 1^er^ quintile et 2,4 % au
  5^e^ [@bm-2015-wps7312, tableau 9]. Elle est donc progressive en part et régressive en montant,
  comme dans les revues internationales.
- **Toutes subventions confondues.** L'étude CEQ ne ventile pas les produits
  [@jouini-lustig-moummi-shimeles-2017-ceq38].
- **Un chiffre isolé.** Le FMI écrit que les ménages les plus aisés bénéficient « presque 40 fois
  plus » des subventions à l'énergie que les plus modestes [Sdralevich et al. 2014, p. 18 et
  p. 112]. Il ne donne ni la source, ni l'unité de classement, ni le produit. Le chiffre ne se
  raccorde pas au rapport d'environ 2,2 entre quintiles extrêmes de la note de 2013 pour
  l'ensemble de l'énergie (29 % contre 13 %) ; il est de l'ordre de ceux de l'essence. Il est à
  présenter comme non sourcé, s'il est présenté.
- **Le bulletin de conjoncture de la Banque mondiale du printemps 2023.**
  - Ce qu'il donne : une figure par décile de consommation, établie par les services de la Banque
    « sur la base des données du ministère de l'énergie et de l'INS » [Banque mondiale 2023,
    p. 19, figure 25].
  - Ce qu'il ne donne pas : ni l'enquête, ni le prix de référence, ni le calcul.
  - Ce qu'il écrit : les carburants profitent principalement aux plus aisés ; après la réforme
    tarifaire de 2022, les subventions à l'électricité et au gaz profitent principalement aux
    80 % les plus modestes ; le GPL est réparti à peu près également, avec des fuites vers les
    usages commerciaux (taxis, restaurants).
  - Ses taux de subvention, à un Brent de 70 dollars, en 2021 : environ 15 % du prix des
    carburants, 30 à 40 % pour l'électricité et le gaz naturel, 70 % pour le GPL [p. 16].
  - Faute de méthode publiée, ces résultats ne se placent pas au rang des études exposées dans le
    chapitre d'incidence.
- **La Banque mondiale en 2008.** Le rapport n° 47294 sur la maîtrise de l'énergie estime par
  écart de prix les subventions de 2006 : environ 1,3 milliard de dinars, « environ 3 % du PIB »
  selon le rapport. Le gaz naturel y compte pour environ 530 MD, dont 370 MD pour la production
  d'électricité, le gasoil pour 350 MD et le GPL pour 200 MD. Le secteur résidentiel reçoit 26 % du
  total [Banque mondiale 2008, § 2.8-2.10 et tableau 2.4]. Sa figure 2.4, par tranche de revenu,
  n'a pas de source lisible dans la copie.
- **Le FMI en 2013.** Ses estimations de la subvention explicite (« pre-tax ») de la Tunisie en
  2011 sont de 0,77 % du PIB pour les produits pétroliers et de 2,23 % pour l'électricité ; le gaz
  naturel n'est pas estimé (« n.a. ») [Clements et al. 2013, p. 47, tableau 2 de l'annexe]. Ce sont
  des parts imprimées par le FMI.
- **Effets indirects.** Les parts tunisiennes de l'effet indirect dans l'effet total sont de 51 %
  pour l'essence, 89,1 % pour le gasoil, 14,4 % pour le GPL et 40,7 % pour l'électricité
  [Verme 2018, tableau 3]. Elles viennent du chapitre tunisien de Verme et Araar, qui reprend
  le document de 2015.
- **Les réformes de 2012 à 2014.**
  - Leur contenu : hausses de 7 % en septembre 2012 et de 7 à 8 % en mars 2013 ; tarif « social »
    pour moins de 100 kWh par mois ; suppression en 2014 de la subvention aux cimenteries ;
    formule automatique pour l'essence en janvier 2014.
  - Comment le FMI les décrit : sans en mesurer l'effet [Sdralevich et al. 2014, p. 46-49 ;
    @fmi-2014-cr14362].
  - Le jugement de Verme : la Tunisie a procédé par hausses graduelles, trimestrielles, « bien
    accueillies », mais n'a supprimé la subvention d'aucun produit énergétique [Verme 2018,
    p. 18].
  - Aucune évaluation ex post de leurs effets sur la consommation ou sur la pauvreté n'est
    identifiée ici, ni pour ces réformes ni pour celle de 2022.

**Les élasticités en Tunisie et au Maghreb.** Elles reposent sur deux estimations, faites sur des
séries agrégées annuelles et toutes deux antérieures à 2005.

| Étude | Données et méthode | Électricité, ménages | Gaz naturel, ménages | Autres produits |
|---|---|---|---|---|
| ANER (Ideaconsult) 2000 [@aner-2000-impact-prix-energie, p. 62-66, tableaux 3 et 4] | séries annuelles de 1980 à 1997, 17 ou 18 observations ; ajustement partiel ; le PIB réel tient lieu de revenu | −0,34 | −0,61 | ménages, toutes énergies : −0,24 ; GPL −0,84 ; gasoil −0,14 ; essence normale −0,24 ; essence super −1,04 ; pétrole lampant −0,13 |
| Talbi et Nguyen 2014 [p. 456-457, tableaux II à V] | séries annuelles de 1980 à 2004 ; ajustement partiel | −0,30 (court terme) | −0,98 (long terme) | ensemble de l'énergie −0,25 (long terme) ; produits pétroliers des ménages −0,03 (court terme) |

- **Ce que valent ces chiffres.** Ce sont des valeurs ponctuelles, une par étude et par usage, et
  non une plage. Les auteurs de l'ANER jugent eux-mêmes « peu fiables » les élasticités de
  l'essence, qui varient avec le prix substitut retenu [p. 65].
- **Deux études qui ne sont pas indépendantes.** Leurs données se recouvrent et leur méthode est la
  même : l'élasticité-revenu du gaz résidentiel vaut 2,35 dans l'une et 2,32 dans l'autre,
  l'élasticité croisée de l'électricité résidentielle 0,15 et 0,14.
- **Les élasticités des études d'incidence sont des hypothèses, non des estimations.**
  - La note de la Banque mondiale de 2013 pose une élasticité nulle et, en variante pour
    l'électricité, −0,3, ce qui divise l'effet par deux [@bm-2013-82712, p. 18].
  - Le document de 2015 n'en pose aucune.
  - Les simulations régionales de Verme et Araar laissent chaque équipe nationale choisir entre
    0,1 et 0,5 en valeur absolue, selon le guide SUBSIM [Verme et Araar 2017, p. 30].
- **Non récupérés, donc non cités pour leurs chiffres.**
  - Gam et Ben Rejeb 2012, *Energy Policy* 45 : séries de 1976 à 2006, modèle VAR.
  - Labidi et Abdessalem 2018, *Energy Strategy Reviews* 19 : effet rebond de l'électricité des
    ménages.
  - Une estimation de −0,52 attribuée à « Talbi et al. 2022 » par un moteur de recherche n'a pas
    été retrouvée.
  - Aucune estimation marocaine ou algérienne n'a été récupérée.

## 4. Ce qui est établi, ce qui est débattu

**Établi** (convergence des revues et des études tunisiennes, sous leurs hypothèses) :
- La subvention à l'essence et au gasoil va, en montant, d'abord aux ménages aisés : environ
  6 fois plus au quintile supérieur qu'à l'inférieur en moyenne internationale, 20 à 27 fois pour
  l'essence (études de 2005 à 2014). La Tunisie de 2010, aux prix de 2013, est dans le même sens.
- En part de la consommation, la perte d'une suppression est à peu près neutre entre quintiles
  dans les revues du FMI. Elle est plus lourde pour les modestes en Tunisie selon le document de
  2015 : 8,8 % contre 2,4 % de la dépense en subvention reçue.
- L'effet indirect est élevé pour le gasoil (77 à 89 % de l'effet total au Maghreb et en
  Jordanie), et voisin de 40 % pour l'électricité.
- La demande d'énergie est peu élastique à court terme (de −0,1 à −0,25 environ en moyenne selon
  les méta-analyses), plus à long terme (de −0,3 à −0,65).
- La subvention explicite peut excéder de loin la ligne budgétaire quand des entreprises
  publiques en portent une part ; c'est la définition même du FMI.

**Débattu** :
- *La taille des élasticités.* Labandeira et al. donnent −0,22 et −0,65 en moyenne. Havranek et
  al., après correction du biais de publication, divisent par deux environ la moyenne pour
  l'essence. Kudela et al. 2026 trouvent pour l'électricité des réponses plus faibles dans les
  études les mieux identifiées. Le désaccord porte sur la sélection des résultats publiés et sur
  l'identification.
- *Le ciblage de l'électricité par la grille tarifaire.* Komives et al. jugent limité le gain
  qu'on peut attendre d'une tranche sociale réduite. Verme décrit les grilles du Maroc et de la
  Tunisie, relevées sur les seules tranches hautes, comme protégeant pauvres et classes moyennes.
  Le bulletin de 2023 écrit qu'après 2022 la subvention électrique va « principalement » aux 80 %
  les plus modestes, sans méthode publiée.
- *Le GPL.* Sa distribution est plate en Tunisie, alors que la moyenne internationale le
  concentre en haut. Les fuites vers les usages commerciaux n'y sont pas chiffrées. Verme en fait
  le produit le plus difficile à réformer dans la région.
- *Réforme radicale ou graduelle, avec ou sans transferts.* Verme juge la réponse « non
  univoque ». En Iran, les simulations jugent les transferts excessifs, tandis que l'étude ex post
  ne trouve pas d'effet sur l'offre de travail. Ce ne sont pas les mêmes questions.
- *L'électricité est-elle régressive en montant ?* La réponse dépend de la méthode : rapport
  d'environ 2,3 entre quintiles extrêmes avec la grandeur comptable de la STEG (2013), d'environ
  1,3 avec un prix de référence unique par kWh (2015).
- *Le prix de référence.* Prix franco à bord ou prix CIF ; parité à l'importation ou à
  l'exportation pour le gaz ; coût comptable de la STEG ou prix unique au kWh. Le choix déplace la
  subvention mesurée. L'écart entre les deux études de la Banque mondiale en vient pour
  l'essentiel.
- *Le canal de l'investissement et de la qualité du service.* L'argument est établi en synthèse
  sur l'Inde. Le bulletin de 2023 l'énonce pour la STEG et les énergies renouvelables, sans
  mesure.
- *Le rapport de « 40 fois »* du FMI de 2014, sans source, contre le rapport d'environ 2 entre
  quintiles extrêmes de la note de la Banque mondiale de 2013.

## 5. Ce que le praticien retient

1. **Une incidence directe à comportements fixes est une borne haute de court terme.**
   - Pour une hausse modérée, l'approximation est bonne.
   - Pour la suppression d'une subvention de 68 à 70 % (le GPL), elle surestime la perte. Le
     second ordre dépend d'élasticités qui, en Tunisie, ne sont estimées que sur des séries
     agrégées d'avant 2005.
   - Les élasticités utilisées dans les simulations régionales, de 0,1 à 0,5 en valeur absolue,
     sont posées et non mesurées.
2. **Les ordres de grandeur à garder**, chacun avec son champ.
   - Carburants : environ 6 fois plus au quintile le plus aisé (20 pays, puis 32, études de 2005
     à 2014). En Tunisie, essence 67 % contre 1 % (enquête de 2010, prix d'avril 2013).
   - Ensemble de l'énergie en Tunisie : 29 % contre 13 % en 2013, 25,0 % contre 14,9 % en 2015.
     En part de la dépense, 8,8 % au 1^er^ quintile contre 2,4 % au 5^e^.
   - Coût d'un dollar transféré aux 40 % les plus modestes par l'essence : environ 14 dollars
     (moyenne internationale, études jusqu'en 2014).
3. **Comparer deux chiffres suppose quatre mêmes choix.** Deux montants de subvention ne se
   comparent qu'à même date de prix, même prix de référence, même périmètre (budget, entreprises
   publiques, ressources cédées) et même PIB. En Tunisie, la ligne budgétaire « carburants » n'est
   pas la subvention explicite avant 2015. La rupture comptable de 2007 à la STEG et le changement
   de porteur en 2015 changent ce que mesurent les séries, pas nécessairement le coût économique.
4. **Ce que les données tunisiennes ne permettent pas de trancher**, en l'état de ce qui est
   publié et récupéré.
   - *Pas d'élasticité microéconométrique.* Aucune élasticité-prix n'a été estimée sur données
     de ménages.
   - *Des quantités reconstituées.* L'enquête sur le budget des ménages donne des dépenses, non des
     quantités. Le document de 2015 reconstitue les kWh en inversant la grille tarifaire.
   - *Pas de série du coût par filière.* Il n'y a de série continue ni du coût de revient du kWh
     avant 2017, ni du coût du gaz distribué (`docs/notes/compensation-electricite-gaz-series-steg.md`, § 2).
   - *Pas d'étude publiée avec sa méthode sur l'enquête de 2021.* Aucune étude d'incidence sur
     l'enquête de 2021 n'a été publiée avec sa méthode. Le simulateur CEQ de 2025 (`ceq-tunisie`)
     n'est pas une publication.
   - *Pas d'évaluation ex post des réformes.* Ni celles de 2012-2014 ni celle de 2022 n'ont été
     évaluées après coup.
   - *Des fuites non mesurées.* La part du GPL captée par les usages commerciaux et par la
     contrebande n'est pas mesurée. Le FMI relève la contrebande de carburant algérien vers la
     Tunisie, sans chiffre [Clements et al. 2013, p. 17].

**Constat pour `docs/notes/backlog-modele.md`.** À verser par le rédacteur ou le modéliste ;
cette fiche n'écrit rien.
- Toute simulation de l'effet d'une réforme des prix de l'énergie sur les ménages appellerait des
  élasticités-prix par produit.
- Aucune estimation tunisienne sur données de ménages n'est disponible.
- Les seules estimations nationales sont agrégées, faites sur 1980-1997 et 1980-2004.
- Aucun paramètre de comportement n'est proposé ici.

## 6. Références

### Clés déjà présentes

- **Dans `precis/fr/compensation/references.json`** : `bm-2013-82712`, `bm-2015-wps7312`,
  `jouini-lustig-moummi-shimeles-2017-ceq38`, `ins-cres-bad-2013-subventions`,
  `aner-2000-impact-prix-energie`, `fmi-2014-cr14362`, `fmi-2016-cr16138`,
  `bm-1985-cem-5328-vol2`, `steg-ef-2014`.
- **Dans `precis/fr/references.json`** : `minfin-compensation-carburants-2014`.

### Entrées CSL-JSON à créer

Les URL sont celles de la collecte du 17 octobre 2026. Une copie passée par l'archive du web est
signalée.

```json
[
 {"id": "arze-coady-gillingham-2010-fuel-subsidies", "type": "report", "title": "The Unequal Benefits of Fuel Subsidies: A Review of Evidence for Developing Countries", "author": [{"family": "Arze del Granado", "given": "Javier"}, {"family": "Coady", "given": "David"}, {"family": "Gillingham", "given": "Robert"}], "publisher": "Fonds monétaire international", "collection-title": "IMF Working Paper", "number": "WP/10/202", "issued": {"date-parts": [[2010, 9]]}, "URL": "https://www.imf.org/external/pubs/ft/wp/2010/wp10202.pdf", "note": "Version publiée : World Development 40(11), 2012, p. 2234-2248 — référence à vérifier, non récupérée. Copie : archive du web (imf.org refuse l'accès direct)."},
 {"id": "coady-flamini-sears-2015-fuel-subsidies-revisited", "type": "report", "title": "The Unequal Benefits of Fuel Subsidies Revisited: Evidence for Developing Countries", "author": [{"family": "Coady", "given": "David"}, {"family": "Flamini", "given": "Valentina"}, {"family": "Sears", "given": "Louis"}], "publisher": "Fonds monétaire international", "collection-title": "IMF Working Paper", "number": "WP/15/250", "issued": {"date-parts": [[2015, 11]]}, "URL": "https://www.imf.org/external/pubs/ft/wp/2015/wp15250.pdf"},
 {"id": "clements-et-al-2013-energy-subsidy-reform", "type": "report", "title": "Energy Subsidy Reform: Lessons and Implications", "author": [{"family": "Clements", "given": "Benedict"}, {"literal": "et al."}], "publisher": "Fonds monétaire international", "genre": "Policy Paper", "issued": {"date-parts": [[2013, 1, 28]]}, "URL": "https://www.imf.org/external/np/pp/eng/2013/012813.pdf"},
 {"id": "sdralevich-et-al-2014-subsidy-reform-mena", "type": "report", "title": "Subsidy Reform in the Middle East and North Africa: Recent Progress and Challenges Ahead", "author": [{"family": "Sdralevich", "given": "Carlo"}, {"family": "Sab", "given": "Randa"}, {"family": "Zouhar", "given": "Younes"}, {"family": "Albertin", "given": "Giorgia"}], "publisher": "Fonds monétaire international", "collection-title": "Departmental Paper", "number": "14/3", "issued": {"date-parts": [[2014]]}, "URL": "https://www.imf.org/external/pubs/ft/dp/2014/1403mcd.pdf", "note": "Lève la lacune de docs/notes/compensation-etudes-incidence-calculs.md, § F (cité de seconde main jusqu'ici)."},
 {"id": "coady-parry-le-shang-2019-fossil-fuel-subsidies", "type": "report", "title": "Global Fossil Fuel Subsidies Remain Large: An Update Based on Country-Level Estimates", "author": [{"family": "Coady", "given": "David"}, {"family": "Parry", "given": "Ian"}, {"family": "Le", "given": "Nghia-Piotr"}, {"family": "Shang", "given": "Baoping"}], "publisher": "Fonds monétaire international", "collection-title": "IMF Working Paper", "number": "WP/19/89", "issued": {"date-parts": [[2019, 5]]}, "URL": "https://www.imf.org/-/media/Files/Publications/WP/2019/WPIEA2019089.ashx"},
 {"id": "black-et-al-2023-fossil-fuel-subsidies", "type": "report", "title": "IMF Fossil Fuel Subsidies Data: 2023 Update", "author": [{"family": "Black", "given": "Simon"}, {"family": "Liu", "given": "Antung A."}, {"family": "Parry", "given": "Ian"}, {"family": "Vernon", "given": "Nate"}], "publisher": "Fonds monétaire international", "collection-title": "IMF Working Paper", "number": "WP/23/169", "issued": {"date-parts": [[2023, 8]]}, "URL": "https://www.imf.org/-/media/Files/Publications/WP/2023/English/wpiea2023169-print-pdf.ashx"},
 {"id": "davis-2013-economic-cost-fuel-subsidies", "type": "report", "title": "The Economic Cost of Global Fuel Subsidies", "author": [{"family": "Davis", "given": "Lucas W."}], "publisher": "National Bureau of Economic Research", "collection-title": "NBER Working Paper", "number": "19736", "issued": {"date-parts": [[2013, 12]]}, "URL": "https://www.nber.org/system/files/working_papers/w19736/w19736.pdf", "note": "Version publiée : American Economic Review 104(5), 2014, p. 581-585 — référence à vérifier, non récupérée."},
 {"id": "komives-et-al-2005-water-electricity-poor", "type": "book", "title": "Water, Electricity, and the Poor: Who Benefits from Utility Subsidies?", "author": [{"family": "Komives", "given": "Kristin"}, {"family": "Foster", "given": "Vivien"}, {"family": "Halpern", "given": "Jonathan"}, {"family": "Wodon", "given": "Quentin"}], "publisher": "Banque mondiale", "publisher-place": "Washington", "issued": {"date-parts": [[2005]]}, "URL": "https://documents1.worldbank.org/curated/en/606521468136796984/pdf/343340REPLACEM10082136342501PUBLIC1.pdf"},
 {"id": "burgess-greenstone-ryan-sudarshan-2020-electricity-right", "type": "article-journal", "title": "The Consequences of Treating Electricity as a Right", "author": [{"family": "Burgess", "given": "Robin"}, {"family": "Greenstone", "given": "Michael"}, {"family": "Ryan", "given": "Nicholas"}, {"family": "Sudarshan", "given": "Anant"}], "container-title": "Journal of Economic Perspectives", "volume": "34", "issue": "1", "page": "145-169", "issued": {"date-parts": [[2020]]}, "DOI": "10.1257/jep.34.1.145", "note": "Copie : archive du web de pubs.aeaweb.org."},
 {"id": "currie-gahvari-2008-cash-in-kind", "type": "article-journal", "title": "Transfers in Cash and In-Kind: Theory Meets the Data", "author": [{"family": "Currie", "given": "Janet"}, {"family": "Gahvari", "given": "Firouz"}], "container-title": "Journal of Economic Literature", "volume": "46", "issue": "2", "page": "333-383", "issued": {"date-parts": [[2008]]}, "DOI": "10.1257/jel.46.2.333", "note": "Copie récupérée : NBER Working Paper 13557 (octobre 2007, révisé novembre 2007), https://www.nber.org/system/files/working_papers/w13557/w13557.pdf ; les pages citées sont celles de cette version."},
 {"id": "labandeira-labeaga-lopez-otero-2017-meta-elasticites", "type": "article-journal", "title": "A meta-analysis on the price elasticity of energy demand", "author": [{"family": "Labandeira", "given": "Xavier"}, {"family": "Labeaga", "given": "José M."}, {"family": "López-Otero", "given": "Xiral"}], "container-title": "Energy Policy", "volume": "102", "page": "549-568", "issued": {"date-parts": [[2017]]}, "DOI": "10.1016/j.enpol.2017.01.002", "note": "Copie récupérée : Economics for Energy, WP 04/2015, https://economicsforenergy.wordpress.com/wp-content/uploads/2016/04/wp-04-2015.pdf ; chiffres et pages de cette version (416 articles, 1990-2014)."},
 {"id": "havranek-irsova-janda-2012-gasoline", "type": "article-journal", "title": "Demand for gasoline is more price-inelastic than commonly thought", "author": [{"family": "Havranek", "given": "Tomas"}, {"family": "Irsova", "given": "Zuzana"}, {"family": "Janda", "given": "Karel"}], "container-title": "Energy Economics", "volume": "34", "issue": "1", "page": "201-207", "issued": {"date-parts": [[2012]]}, "DOI": "10.1016/j.eneco.2011.09.003", "note": "Copie récupérée : version de travail du 25 septembre 2012, https://meta-analysis.cz/gasoline_price/gas_price.pdf. DOI à vérifier."},
 {"id": "kudela-et-al-2026-electricity-elasticity", "type": "manuscript", "title": "Electricity demand has not become more price-responsive despite ninety years of technological change", "author": [{"family": "Kudela", "given": "Peter"}, {"family": "Havranek", "given": "Tomas"}, {"family": "Irsova", "given": "Zuzana"}, {"family": "Kudelova", "given": "Anna"}, {"family": "Sikl", "given": "Vojtech"}], "genre": "prépublication arXiv:2607.21285", "issued": {"date-parts": [[2026, 7, 24]]}, "URL": "https://arxiv.org/abs/2607.21285", "note": "Non évaluée par les pairs à la date de la fiche."},
 {"id": "talbi-nguyen-2014-energy-demand-tunisia", "type": "article-journal", "title": "An Empirical Analysis of Energy Demand in Tunisia", "author": [{"family": "Talbi", "given": "Besma"}, {"family": "Nguyen", "given": "Duc Khuong"}], "container-title": "Economics Bulletin", "volume": "34", "issue": "1", "page": "452-458", "issued": {"date-parts": [[2014]]}, "URL": "http://www.accessecon.com/Pubs/EB/2014/Volume34/EB-14-V34-I1-P43.pdf"},
 {"id": "verme-2018-subsidy-reforms-mena", "type": "report", "title": "Subsidy Reforms in the Middle East and North Africa Region: A Review", "author": [{"family": "Verme", "given": "Paolo"}], "publisher": "Banque mondiale", "collection-title": "Poverty & Equity Global Practice Working Paper", "number": "75", "issued": {"date-parts": [[2018]]}, "URL": "https://documents1.worldbank.org/curated/en/260201524137749680/pdf/125411-NWP-PUBLIC-POV075-PRWP7754.pdf", "note": "Co-publié comme Policy Research Working Paper 7754 ; date de cette première édition à confirmer sur la copie."},
 {"id": "verme-araar-2017-quest-subsidy-reforms", "type": "book", "title": "The Quest for Subsidy Reforms in the Middle East and North Africa Region: A Microsimulation Approach to Policy Making", "editor": [{"family": "Verme", "given": "Paolo"}, {"family": "Araar", "given": "Abdelkrim"}], "publisher": "Springer", "collection-title": "Natural Resource Management and Policy", "volume": "51", "issued": {"date-parts": [[2017]]}, "DOI": "10.1007/978-3-319-52926-4", "note": "Copie récupérée : manuscrit accepté déposé à la Banque mondiale, https://documents1.worldbank.org/curated/en/965011495167833904/pdf/115145-WP-Book-MENA-Subsidies-PUBLIC.pdf ; pages de cette version. Numéro de collection et DOI à vérifier."},
 {"id": "verme-el-massnaoui-2015-maroc", "type": "report", "title": "An Evaluation of the 2014 Subsidy Reforms in Morocco and a Simulation of Further Reforms", "author": [{"family": "Verme", "given": "Paolo"}, {"family": "El-Massnaoui", "given": "Khalid"}], "publisher": "Banque mondiale", "collection-title": "Policy Research Working Paper", "number": "7224", "issued": {"date-parts": [[2015, 3]]}, "URL": "https://documents1.worldbank.org/curated/en/978761467980552302/pdf/WPS7224.pdf"},
 {"id": "salehi-isfahani-mostafavi-dehzooei-2017-iran", "type": "report", "title": "Cash Transfers and Labor Supply: Evidence from a Large-Scale Program in Iran", "author": [{"family": "Salehi-Isfahani", "given": "Djavad"}, {"family": "Mostafavi-Dehzooei", "given": "Mohammad H."}], "publisher": "Economic Research Forum", "collection-title": "ERF Working Paper", "number": "1090", "issued": {"date-parts": [[2017, 5]]}, "URL": "https://erf.org.eg/app/uploads/2017/05/1090.pdf", "note": "Version publiée : Journal of Development Economics, 2018 — volume et pages à vérifier, non récupérée."},
 {"id": "bm-2023-tem-subventions-energie", "type": "report", "title": "Tunisie. Bulletin de conjoncture économique, printemps 2023 : réformer les subventions énergétiques pour une économie durable", "author": [{"literal": "Banque mondiale"}], "publisher": "Banque mondiale", "issued": {"date-parts": [[2023, 3]]}, "URL": "https://documents1.worldbank.org/curated/en/099034203282315663/pdf/IDU07a91275108aea04aa90a8910b9455001fc2f.pdf", "note": "Titre exact à relever sur la couverture de la version française."},
 {"id": "bm-2008-47294-maitrise-energie", "type": "report", "title": "Tunisie : accélération de la politique de maîtrise de l'énergie", "author": [{"literal": "Banque mondiale"}], "publisher": "Banque mondiale, ESMAP", "number": "47294-TN", "issued": {"date-parts": [[2008, 12]]}, "note": "Copie déjà rangée dans tunisia-data, adresse d'origine non relevée ; demandée « à verser » par le TODO de _incidence.qmd. Titre à confronter à la couverture."}
]
```

### Copies rangées dans `tunisia-data`

Toutes les copies sont dans `data/raw/banque-mondiale-rapports/`, répertoire ignoré par git
(vérifié par `git check-ignore`). `git status` de `tunisia-data` est inchangé. Les lignes de
catalogue sont proposées au format de `sources/minenergie-steg-urls.csv`, avec les mêmes
colonnes, pour un fichier `sources/litterature-economique-urls.csv`. Collecte du 2026-10-17.

**Question ouverte pour la relecture humaine.** Les copies sont dans
`banque-mondiale-rapports/`, seul répertoire de `data/raw/` déjà ignoré par git ; un répertoire
nouveau ne l'aurait pas été. Mais les lignes sont proposées pour un nouveau
`sources/litterature-economique-urls.csv`, ce qui rompt l'appariement entre `<source>/` et
`<source>-urls.csv`. Le catalogue existant, `sources/banque-mondiale-rapports-urls.csv`, n'a que
quatre colonnes, sans empreinte, et porte des modifications non commitées d'un autre travail.
Le choix est laissé à la relecture : un nouveau répertoire avec sa ligne `.gitignore`, ou bien
ces lignes dans le catalogue existant.

```csv
fichier,url_origine,url_archive,octets,sha256,consultation,famille,etat
banque-mondiale-rapports/imf_2010_wp10202_arze_coady_gillingham.pdf,https://www.imf.org/external/pubs/ft/wp/2010/wp10202.pdf,https://web.archive.org/web/2020id_/https://www.imf.org/external/pubs/ft/wp/2010/wp10202.pdf,1275227,91b243ad4377126bae8ccc14514f425caf780fe1eaabb96160c0b467dd8f1387,2026-10-17,étude économique,"FMI WP/10/202 ; 24 p. ; imf.org refuse l'accès direct (Access Denied)"
banque-mondiale-rapports/imf_2015_wp15250_coady_flamini_sears.pdf,https://www.imf.org/external/pubs/ft/wp/2015/wp15250.pdf,https://web.archive.org/web/2020id_/https://www.imf.org/external/pubs/ft/wp/2015/wp15250.pdf,675667,77a6b4ec41130fcf38075e01a0f9c8183c45fbeb334c2a103fac8fad672e275c,2026-10-17,étude économique,"FMI WP/15/250 ; 25 p."
banque-mondiale-rapports/imf_2013_clements_energy_subsidy_reform.pdf,https://www.imf.org/external/np/pp/eng/2013/012813.pdf,https://web.archive.org/web/2020id_/https://www.imf.org/external/np/pp/eng/2013/012813.pdf,925038,ee37596a37f218acc0d1a9644ed44f82b148dbb6dbb9562b41b1871a27c1bbe7,2026-10-17,étude économique,"FMI, Policy Paper du 28 janvier 2013 ; 68 p."
banque-mondiale-rapports/imf_2014_dp1403_sdralevich_subsidy_reform_mena.pdf,https://www.imf.org/external/pubs/ft/dp/2014/1403mcd.pdf,https://web.archive.org/web/2020id_/https://www.imf.org/external/pubs/ft/dp/2014/1403mcd.pdf,986898,bb85a752d0906e77dd40326203bb8a7b67d179da70e97a91731b5adbf1ec97e9,2026-10-17,étude économique,"FMI, Departmental Paper 14/3 ; 132 p."
banque-mondiale-rapports/imf_2019_wp19089_coady_parry_le_shang.pdf,https://www.imf.org/-/media/Files/Publications/WP/2019/WPIEA2019089.ashx,https://web.archive.org/web/2022id_/https://www.imf.org/-/media/Files/Publications/WP/2019/WPIEA2019089.ashx,603310,5887cd459405855ff3edf1ef9dff26693f746efe8dc2e14833315b2a9494dbea,2026-10-17,étude économique,"FMI WP/19/89 ; 39 p."
banque-mondiale-rapports/imf_2023_wp23169_black_fossil_fuel_subsidies.pdf,https://www.imf.org/-/media/Files/Publications/WP/2023/English/wpiea2023169-print-pdf.ashx,https://web.archive.org/web/2024id_/https://www.imf.org/-/media/Files/Publications/WP/2023/English/wpiea2023169-print-pdf.ashx,729366,f3afcec9945d185fc38b20170b6448c3805f4301da070b737d275f1d2f2ecc14,2026-10-17,étude économique,"FMI WP/23/169 ; 32 p."
banque-mondiale-rapports/nber_2013_w19736_davis_cost_fuel_subsidies.pdf,https://www.nber.org/system/files/working_papers/w19736/w19736.pdf,,312991,f953e9473063fc58d965628cba4506e730bd9715424d03aae522c1aad05bd08e,2026-10-17,étude économique,"NBER WP 19736"
banque-mondiale-rapports/nber_2007_w13557_currie_gahvari_cash_in_kind.pdf,https://www.nber.org/system/files/working_papers/w13557/w13557.pdf,,546728,7f1bbfd0e3962ea0debaf3af115dcd6d1a37a7ce05fa17a49b3ea4d5bf267cf2,2026-10-17,étude économique,"NBER WP 13557, version de travail de JEL 46(2)"
banque-mondiale-rapports/jep_2020_burgess_greenstone_ryan_sudarshan.pdf,https://pubs.aeaweb.org/doi/pdfplus/10.1257/jep.34.1.145,https://web.archive.org/web/2022id_/https://pubs.aeaweb.org/doi/pdfplus/10.1257/jep.34.1.145,981589,4337c49e775a6dbde6cd5eeaa3ef9f93413fb52d3dce470ad10f026f824ae699,2026-10-17,étude économique,"JEP 34(1) ; accès direct bloqué (défi Cloudflare)"
banque-mondiale-rapports/wb_2005_komives_water_electricity_poor.pdf,https://documents1.worldbank.org/curated/en/606521468136796984/pdf/343340REPLACEM10082136342501PUBLIC1.pdf,,2502887,bebb906d8d4473869cc0834d14f3e2f259c3b02e530fd8c0d3edc5cc76fc0118,2026-10-17,étude économique,"Banque mondiale 2005 ; 306 p."
banque-mondiale-rapports/efe_2015_wp04_labandeira_meta_elasticites.pdf,https://economicsforenergy.wordpress.com/wp-content/uploads/2016/04/wp-04-2015.pdf,,904541,3d430ae962fcb9e93ac9fddae67d4de18d4e186a318b84129f0290aad37c5c21,2026-10-17,étude économique,"Economics for Energy WP 04/2015 ; version de travail d'Energy Policy 102 (2017)"
banque-mondiale-rapports/havranek_2011_gasoline_price_elasticity_meta.pdf,https://meta-analysis.cz/gasoline_price/gas_price.pdf,,417035,bf3e9ea019b988e68ac55c2aa56ed415c617109cb4ed95bfce545d6c0fe8a799,2026-10-17,étude économique,"version de travail d'Energy Economics 34(1) (2012)"
banque-mondiale-rapports/arxiv_2026_2607-21285_meta_elasticite_electricite.pdf,https://arxiv.org/pdf/2607.21285,,1457542,0fcf906acbcebf82c1d7107dcd10c512bec72ff16eb01173cd4c8b982ba3360d,2026-10-17,étude économique,"prépublication v1 du 23 juillet 2026 ; 71 p."
banque-mondiale-rapports/eb_2014_talbi_nguyen_demande_energie_tunisie.pdf,http://www.accessecon.com/Pubs/EB/2014/Volume34/EB-14-V34-I1-P43.pdf,,203062,568bd0092e6fcd59d2d85a7b51fd8bda2f0bc42338964c103fe83fb04a103fd0,2026-10-17,étude économique,"Economics Bulletin 34(1), p. 452-458"
banque-mondiale-rapports/wb_2018_wps7754_verme_subsidy_reforms_mena.pdf,https://documents1.worldbank.org/curated/en/260201524137749680/pdf/125411-NWP-PUBLIC-POV075-PRWP7754.pdf,,771503,8b89a43d8f76c085509f370a83a3384f474ab94b4c1ac17ce3933989044e5d2e,2026-10-17,étude économique,"PRWP 7754 / Poverty & Equity GP WP 75 ; 42 p."
banque-mondiale-rapports/wb_2017_verme_araar_quest_subsidy_reforms_mena_manuscrit.pdf,https://documents1.worldbank.org/curated/en/965011495167833904/pdf/115145-WP-Book-MENA-Subsidies-PUBLIC.pdf,,4989980,147d26520fe18bc0f0aa83fcc8229124108135229a87d5c845f96f72a7fbbe31,2026-10-17,étude économique,"manuscrit accepté du livre Springer 2017 ; 417 p."
banque-mondiale-rapports/wb_2015_wps7224_verme_elmassnaoui_maroc.pdf,https://documents1.worldbank.org/curated/en/978761467980552302/pdf/WPS7224.pdf,,1766815,4520213567d5e325ab629c05064b9637893548e599b4cc5c251036157c0de233,2026-10-17,étude économique,"PRWP 7224 ; 28 p."
banque-mondiale-rapports/erf_2017_wp1090_salehi-isfahani_transferts_iran.pdf,https://erf.org.eg/app/uploads/2017/05/1090.pdf,,2016853,3ec69e55fc32ed75a660801e67edf7266c2362007274c45a1adeff5c47892486,2026-10-17,étude économique,"ERF WP 1090"
banque-mondiale-rapports/wb_2023_tem_printemps_subventions_energie_fr.pdf,https://documents1.worldbank.org/curated/en/099034203282315663/pdf/IDU07a91275108aea04aa90a8910b9455001fc2f.pdf,,2773263,1d5e417599d9f5f6fd68385e6505d702f51df26153f66a8a9ae015236420b28c,2026-10-17,rapport extérieur,"bulletin de conjoncture, printemps 2023, version française ; 42 p."
banque-mondiale-rapports/wb_2008_47294_maitrise_energie_fr.pdf,,,7212925,06718f107a542cd42ff53c89fc0da65d449adb76305d97d060c15e7785f983cc,,rapport extérieur,"déjà présent, non catalogué ; adresse d'origine à retrouver"
banque-mondiale-rapports/aner_2000_etude_impact_prix_energie_demande.pdf,,,578224,27c2cb076ab2ea4509d35980cbe8524ce2e6abc6e521c1728f8fd3545ca5242b,,étude économique,"déjà présent, non catalogué ; adresse d'origine non relevée (voir la note de la clé aner-2000-impact-prix-energie)"
banque-mondiale-rapports/wb_2013_82712_subventions_energetiques_fr.pdf,,,3954761,a35c9072d4c761481b37139f463e572bc24aba9a33bdb838464e08ca23eb5931,,étude économique,"déjà présent, non catalogué"
banque-mondiale-rapports/wb_2015_wps7312_energy_reform_simulation.pdf,,,855606,cd6b05406cccc70d612bc4b87ac1d03df289694576e375ef6900e9856b93a4e4,,étude économique,"déjà présent, non catalogué"
```

### Documents non récupérés, adresses essayées

Ils ne sont pas cités pour leurs chiffres.

| Document | Adresses essayées et résultat |
|---|---|
| Espey et Espey 2004, *Journal of Agricultural and Applied Economics* 36(1), méta-analyse de l'électricité résidentielle | ageconsearch.umn.edu/record/42897/files/Espey%20JAAE%20April%202004.pdf, fichier vide ; même adresse dans l'archive du web, page HTML |
| Gam et Ben Rejeb 2012, *Energy Policy* 45, p. 714-720, DOI 10.1016/j.enpol.2012.03.025 | sciencedirect.com, 403 ; seul le résumé a été lu, sur IDEAS |
| Labidi et Abdessalem 2018, *Energy Strategy Reviews* 19, p. 7-18 | sciencedirect.com, 403 |
| « Talbi et al. 2022 », élasticité de −0,52 | attribution vue dans un résumé de moteur de recherche ; document non identifié |
| McRae 2015, *American Economic Review* (Colombie, qualité du réseau et subvention) | non cherché dans cette passe |

## 7. Notions à glossaire

**Déjà dans `precis/glossaire.yml`** : `incidence-des-subventions`, `ciblage`,
`subvention-directe`, `subvention-indirecte`, `prix-de-cession-preferentiel`,
`quintile-niveau-de-vie`, `transfert-monetaire`, `ajustement-automatique-prix-carburants`.

**À ajouter**, ici et dans l'annexe du site « Les notions de l'économie publique » :

| Terme | Définition pressentie | Source canonique pressentie |
|---|---|---|
| élasticité-prix de la demande, court terme et long terme | variation relative de la quantité pour une variation relative du prix ; le long terme inclut le renouvellement des équipements | Labandeira et al. 2017 |
| perte sèche (*deadweight loss*) | valeur des transactions permises par la subvention au-delà de ce qu'elles coûtent à la collectivité | Davis 2013 |
| méthode de l'écart de prix (*price-gap*) | subvention unitaire égale au prix de référence moins le prix payé | Black et al. 2023 ; encadré 1 de @bm-2015-wps7312 |
| prix de référence, coût d'approvisionnement, parité à l'importation ou à l'exportation | coût d'opportunité du produit consommé sur place plutôt que vendu ou acheté à l'étranger, marges comprises | Black et al. 2023 |
| subvention explicite (« pre-tax ») et subvention implicite (« post-tax ») | voir le tableau du § 1 | Coady et al. 2019 ; Black et al. 2023 |

Pour la subvention explicite et la subvention implicite, l'entrée du glossaire doit dire en clair
qu'elles ne correspondent ni à la subvention directe ni à la subvention indirecte.

| Terme | Définition pressentie | Source canonique pressentie |
|---|---|---|
| effet direct, effet indirect | perte due à la consommation du produit lui-même ; perte due à la hausse des prix des autres biens qui l'emploient | Arze del Granado et al. 2010 |
| auto-ciblage | ciblage obtenu par la nature du bien ou par un coût de participation que seuls les bénéficiaires visés acceptent | Currie et Gahvari 2008 |
| tarif progressif par tranches, tranche sociale (*lifeline*) | prix unitaire croissant avec la consommation ; première tranche à bas prix | Komives et al. 2005 |
| indicateur de performance du ciblage (Ω) | part de la subvention reçue par les pauvres rapportée à leur part dans la population | Komives et al. 2005 |
| coût par dinar transféré, fuite | dépense nécessaire pour qu'un dinar atteigne le groupe visé ; part reçue hors de ce groupe | Coady et al. 2015 |
| subvention croisée | financement d'une catégorie d'usagers ou d'une entreprise par une autre | Sdralevich et al. 2014 (« cross-subsidies » entre STEG, STIR et ETAP) ; @fmi-2014-cr14362 |
| biais de publication | sur-représentation des résultats significatifs ou du « bon » signe dans la littérature publiée | Havranek et al. 2012 |

## 8. Littérature arrêtée au mois d'octobre 2026

**À revoir à la prochaine revue annuelle :**

- Les mises à jour de la base du FMI sur les subventions aux combustibles fossiles, postérieures
  à celle de 2023 : non cherchées ici. Relever aussi les chiffres de la Tunisie.
- Une étude d'incidence sur l'enquête nationale de 2021, publiée avec sa méthode : Banque
  mondiale, CEQ, INS ou CRES. Vérifier aussi si le simulateur CEQ de 2025 a donné lieu à
  publication.
- La publication évaluée par les pairs de Kudela et al., et l'existence d'une méta-analyse
  propre aux pays en développement.
- Les évaluations ex post de la hausse de 2022 des tarifs de l'électricité et du gaz au-delà de
  200 kWh et de 30 m^3^. Et, au Maroc, de la réforme du prix du gaz butane accompagnée d'aides
  directes, à vérifier sur pièces avant toute mention.
- Une estimation microéconométrique des élasticités de l'énergie des ménages au Maghreb. Les
  deux articles tunisiens de 2012 et de 2018 restent à récupérer.
- Les versions publiées des documents de travail : Arze del Granado et al. 2012, Davis 2014,
  Salehi-Isfahani et Mostafavi-Dehzooei 2018. Il faudra confronter leurs pages.

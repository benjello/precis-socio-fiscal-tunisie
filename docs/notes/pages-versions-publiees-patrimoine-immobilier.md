# Pages des versions publiées : cinq études du chapitre « Patrimoine immobilier »

Note du documentaliste, 18 octobre 2026. Objet : vérifier, pour les études citées dans
`precis/fr/fiscalite/_patrimoine_immobilier.qmd` et dans `precis/glossaire.yml`, si les pages
citées valent pour la version publiée, et vérifier les métadonnées de `precis/fr/references.json`
(et de `precis/ar/references.json`, qui porte les mêmes notes). Aucun fichier du précis n'a été
modifié.

Les pages données ici sont les numéros imprimés sur les copies.

## 1. Ce qui a été obtenu

| Clé | Version publiée | Copie lue jusqu'ici | Version publiée obtenue ? |
|---|---|---|---|
| `kleven-2016-bunching` | *Annual Review of Economics* 8, 2016, p. 435-464, DOI 10.1146/annurev-economics-080315-015234 | version de juin 2016, site de l'auteur | **oui** : PDF de l'éditeur, copie déposée sur une page de cours de Berkeley |
| `best-kleven-2018-housing-transaction-taxes` | *Review of Economic Studies* 85(1), 2018, p. 157-193, DOI 10.1093/restud/rdx032 | version de septembre 2016, site de H. Kleven | non |
| `maattanen-tervio-2022-welfare-transaction-taxes` | *Economic Journal* 132(644), 2022, p. 1566-1599, DOI 10.1093/ej/ueab080 | version du 18 août 2021, site de N. Määttänen | non. Helda donne la version acceptée, de même texte et de même pagination que la copie |
| `dachis-duranton-turner-2012-land-transfer-taxes` | *Journal of Economic Geography* 12(2), 2012, p. 327-354, DOI 10.1093/jeg/lbr007 | Working Paper 423, Université de Toronto, 14 février 2011 | non. Le résumé publié a été lu sur IDEAS |
| `kopczuk-munroe-2015-mansion-tax` | *AEJ: Economic Policy* 7(2), 2015, p. 214-257 | version publiée (site de l'auteur) | déjà en main |

Le volume, le numéro, les pages et le DOI concordent avec Crossref pour les cinq entrées, avec OpenAlex pour
Best–Kleven, Määttänen–Terviö et Dachis et al., et avec la première page imprimée pour Kleven et
Kopczuk–Munroe.
Les métadonnées à corriger sont au § 3.

### Adresses essayées pour les versions publiées introuvables

- PDF de l'éditeur OUP (`academic.oup.com/restud/…/rdx032.pdf`, `…/ej/…/ueab080.pdf`,
  `…/joeg/…/lbr007.pdf`) : 403.
- Unpaywall, 18/10/2026 : RES fermé ; EJ et JEG en accès « vert », versions soumises seulement.
- OpenAlex et Semantic Scholar : aucune version publiée en accès libre pour les trois articles.
- LSE Research Online, notices 88186 (Best–Kleven) et 42508 (Dachis et al.) : « Full text not
  available from this repository ».
- Aaltodoc, handle 123456789/115326 (Määttänen–Terviö) : page en 403. L'API répond, mais la liste
  des fichiers revient vide.
- Helda, handle 10138/566016 : version acceptée. La page de garde avertit : « This reprint may
  differ from the original in pagination and typographic detail. »
  Mis à part cette page de garde, son texte est identique à la copie déjà rangée : la
  comparaison des deux extractions ne diffère que par la page de garde. Les pages 2 et 20 sont
  les mêmes.
- Dépôt de l'université de Pennsylvanie (Dachis et al.) : version du 4 février 2011, antérieure
  au document de travail de Toronto.
- Site de M. C. Best (`columbia.edu/~mcb2270/`) : 403. Le site de H. Kleven est une application
  JavaScript, sans lien lisible par un script.

## 2. Tableau par citation

| # | Lieu | Clé | Citation actuelle | Ce que dit la source (copie lue) | Page dans la version publiée | Action proposée |
|---|---|---|---|---|---|---|
| 1 | qmd l. 532 | kleven-2016-bunching | p. 1 (*kink* : changement de pente ; *notch* : changement de niveau ; taux marginal ou taux moyen) | p. 1 imprimée, introduction : « kink points — discrete changes in the slope of choice sets … notch points — discrete changes in the level of choice sets … whether the discontinuity occurs in the marginal tax rate or in the average tax rate » | **p. 436** (même texte ; le résumé, qui distingue aussi les deux, est p. 435) | remplacer par « p. 436 » |
| 2 | glossaire `seuil-a-saut` | kleven-2016-bunching | « p. 1 et 7 » | p. 1 : définition ; p. 7 : section 3.2 « Notches », « hole in the post-notch density », zone strictement dominée | **p. 436 et 441-442** (3.2 commence p. 441 ; le « hole » et la zone dominée sont p. 442) | remplacer par « p. 436 et 441-442 » |
| 3 | glossaire `seuil-a-changement-de-taux` | kleven-2016-bunching | « p. 1 » | p. 1 : *kink*, « graduated income tax systems » | **p. 436** | remplacer par « p. 436 » |
| 4 | glossaire `regroupement-seuil` | kleven-2016-bunching | « p. 1 » | p. 1 : l'approche « uses bunching around points that feature discontinuities in incentives to elicit behavioral responses » | **p. 436** | remplacer par « p. 436 » |
| 5 | qmd l. 522 (tableau) | best-kleven-2018 | résumé (+20 % d'activité, moins de la moitié compensée) | résumé de la version de 2016 ; même contenu dans le résumé publié (IDEAS, Crossref) | sans objet | garder « résumé » |
| 6 | qmd l. 532 | best-kleven-2018 | p. 2 (prix : réponse de 2 à 5 fois la hausse d'impôt) | p. 2 : « house prices respond by a factor of 2–5 times the size of the tax increase at the notch » | non établie | à trancher, voir § 4 |
| 7 | qmd l. 532 | best-kleven-2018 | p. 12 (le regroupement mêle réponse réelle et sous-déclaration) | p. 11-12 : « our bunching estimates of price responses should be interpreted as combining real responses with potential evasion responses ». La phrase commence en bas de la p. 11 et se termine p. 12 | non établie | à trancher (§ 4). Dans la version de travail, la référence exacte est « p. 11-12 » |
| 8 | qmd l. 533 | best-kleven-2018 | p. 11-12 (fraude faible au Royaume-Uni, ventes par intermédiaires) | p. 11 : la fraude passe surtout par les « extras » exonérés et se limite par le contrôle. Note 14, p. 11-12 : « almost all property transactions in the UK are facilitated by licensed real estate agencies », d'où une collusion difficile | non établie | à trancher (§ 4). Dans la version de travail, préciser « p. 11-12 et n. 14 » |
| 9 | qmd l. 530 | maattanen-tervio-2022 | p. 2-3 et 20 (perte de 12 à 15 % de la recette, modèle calibré sur Helsinki) | p. 2 : « about 13% of the tax revenue at the current 2% tax rate » ; p. 2-3 : calibrage sur la région d'Helsinki ; p. 20 : « between 12% and 15%, depending on the elasticity » | non établie (les pages valent pour la version acceptée de Helda) | à trancher, voir § 4 |
| 10 | qmd l. 530 | maattanen-tervio-2022 | résumé (« cette perte croît plus vite que le taux ») | résumé : « The aggregate welfare gain from this reform increases rapidly with the initial transaction tax rate ». La p. 20 précise : « The relative welfare loss is steeply increasing in the tax rate » (de 2 % à 4 %, le supplément de perte vaut environ 50 % du supplément de recette) | sans objet | garder « résumé ». Remarque de fond : le résumé dit « croît rapidement avec le taux », non « plus vite que le taux » ; ce que la p. 20 établit, c'est que la perte croît plus vite que la recette. Proposer « croît rapidement avec le taux » [résumé], ou « plus vite que la recette » [p. 20, version acceptée] |
| 11 | qmd l. 521 (tableau) | dachis-duranton-turner-2012 | p. 1 (ventes −15 % ; baisse des prix voisine de l'impôt) | résumé de la version de travail et p. 1 imprimée, introduction | résumé publié : même contenu (IDEAS). Le résumé est imprimé p. 327, page non vue | remplacer par « résumé » |
| 12 | qmd l. 530 | dachis-duranton-turner-2012 | p. 1 (« environ 1 dollar pour 8 dollars de recette ») | **vérifié.** Résumé : « about $ 1 for every $ 8 in tax revenue » ; p. 1 imprimée : même phrase, suivie de « according to our calculation ». Le chiffre se rapporte à « an equivalent property tax » | résumé publié : même chiffre (IDEAS : « about $1 for every $8 ») | remplacer par « résumé ». Le texte peut ajouter « par rapport à un impôt foncier équivalent » |
| 13 | qmd l. 531 | kopczuk-munroe-2015 | p. 214-215 et 238 (« la charge pèse près du seuil sur les vendeurs, au-delà même du montant de l'impôt ») | **vérifié.** p. 214 (résumé) : « Incidence for transactions local to the notch falls on sellers » ; p. 215 : « the tax near the threshold imposes a substantial burden on sellers » ; p. 238 : « a local incidence on sellers that exceeds the magnitude of the tax » ; p. 238-239 : « over 200 percent incidence of the tax on sellers for the marginal transaction » | version publiée : pages exactes | garder. Facultatif : « p. 214-215 et 238-239 ». Remarque sur la période, ci-dessous |
| 14 | qmd l. 532 | kopczuk-munroe-2015 | p. 214-215 (impôt de 1 % sur la valeur entière au-delà d'un million, 10 000 dollars au seuil ; environ 20 000 dollars de ventes ramenées au seuil) | p. 215 : « a $1 million sale is subject to a $10,000 tax liability … about $20,000 worth of transactions shift to the threshold in response to the $10,000 tax » | exacte | garder (la p. 215 suffirait) |
| 15 | qmd l. 533 | kopczuk-munroe-2015 | p. 215 (fraude faible à New York, « où les ventes passent par des intermédiaires ») | p. 214-215 : « no evidence of evasion » ; la distorsion est déjà présente dans les annonces des vendeurs, ce qui est « inconsistent with tax evasion ». La p. 215 ne parle pas d'intermédiaires. p. 242 : la fraude suppose l'accord des deux parties et un versement occulte pendant « the long closing process » ; les ventes au comptant, qui font intervenir moins de parties, ne montrent pas plus de regroupement. p. 244 : « Our tests of tax evasion are weak, but do not suggest that this is the main force » | exacte pour ce qu'elle dit | mettre « p. 215 et 242-244 », et revoir le membre « où les ventes passent par des intermédiaires » : vrai pour le Royaume-Uni (Best–Kleven, n. 14) ; pour New York, l'argument porte sur le nombre de parties et la durée de la conclusion de la vente. Le texte gagnerait à dire que les auteurs jugent leurs propres tests « faibles » |

### Remarque sur la période de Kopczuk–Munroe (l. 531)

« À New York et au New Jersey, de 2003 à 2011 » : 2003-2011 n'est que la période des données de
la ville de New York. Selon la note de la table 5 (p. 239), les données de l'État de New York
hors de la ville couvrent 2002-2006 et 2008-2010, celles du New Jersey 1996-2011 ; l'impôt y est
appliqué depuis 2004. Proposition : « à New York (2003-2011) et au New Jersey (1996-2011, impôt
introduit en 2004) », ou retirer les années.

## 3. Métadonnées de `references.json` (FR et AR)

- **best-kleven-2018** : Crossref donne le titre publié « … Evidence From Notches and Stimulus in
  the U.K. ». L'entrée porte « in the UK », graphie de la version de travail. À corriger si l'on
  cite la version publiée. Auteurs, volume, numéro, pages et DOI : conformes.
- **maattanen-tervio-2022** : la note dit « version de travail non datée sur la copie ». La première
  page de la copie porte « August 18, 2021 », et son texte est celui de la version acceptée
  déposée à Helda (Université d'Helsinki). Proposer : « Copie récupérée : version acceptée du
  18 août 2021, site de N. Määttänen, identique à celle de Helda (hdl.handle.net/10138/566016) ;
  pages citées prises dans cette version. »
- **kleven-2016-bunching** : les métadonnées sont justes. Une fois les locators remplacés, la note
  devient : « Copie de la version publiée (PDF de l'éditeur) ; version de travail de juin 2016,
  site de l'auteur, également rangée. » La ligne du catalogue `tunisia-data`
  (`sources/patrimoine-immobilier-urls.csv`) dit « Annual Review of Economics 8, 2016 (pages à
  vérifier ; version de juin 2016…) » : la mettre à jour, et ajouter la copie publiée (§ 5).
- **dachis-duranton-turner-2012** et **kopczuk-munroe-2015** : conformes.

## 4. Choix à faire pour Best–Kleven et Määttänen–Terviö (citations 6 à 9)

La pagination publiée reste inconnue. Un
locator « p. 2 » à côté de `page: 157-193` prête à confusion. Trois issues possibles :

1. **Citer la version lue** : créer une entrée CSL pour la version de travail (type `report` ou
   `manuscript`, date, URL), par exemple `best-kleven-2016-housing-transaction-taxes-wp` et
   `maattanen-tervio-2021-welfare-transaction-taxes-am`. Les locators actuels y renvoient, et une
   mention « version publiée : … » s'ajoute en note. Les pages sont alors justes et vérifiables.
2. **Garder la clé publiée avec des locators indépendants de la pagination** : section ou note de
   l'article (Best–Kleven : « introduction », « section 3.1 et n. 14 » ; Määttänen–Terviö :
   « section 4 », qui contient la p. 20 de la version acceptée). Il faut auparavant vérifier que la numérotation des
   sections est la même dans la version publiée, ce qui n'a pas été possible ici.
3. **Garder les locators actuels**, avec un `<!-- TODO (documentaliste) : pages de la version de
   travail ; pagination publiée à relever sur la version de l'éditeur (accès bibliothèque) -->`,
   en laissant la note CSL telle quelle, puisqu'elle signale déjà la version lue.

Le relevé des pages publiées demande un accès abonné à OUP (RES, EJ). Pour Dachis et al., la
question disparaît si l'on adopte « résumé » (citations 11 et 12).

## 5. Lignes de catalogue proposées (`tunisia-data`, non écrites)

Fichiers téléchargés le 18/10/2026 dans le répertoire temporaire de la session, à ranger sous
`data/raw/banque-mondiale-rapports/` si l'humain le décide :

```
banque-mondiale-rapports/annurev_2016_kleven_bunching_published.pdf,"Henrik Jacobsen Kleven, « Bunching », Annual Review of Economics 8, 2016, p. 435-464 (PDF de l'éditeur, copie déposée sur une page de cours de Berkeley, mention « For personal use only »)",https://eml.berkeley.edu/~saez/course/kleven_annualreview.pdf,2026-10-18,068b8b5b94f77eb1c5494345f53e3911507835a6e320250d1a2e1032d3509b51
banque-mondiale-rapports/helda_2022_maattanen_tervio_welfare_transaction_taxes_am.pdf,"Määttänen et Terviö, même titre, version acceptée (Economic Journal 132(644), 2022, p. 1566-1599), dépôt Helda",https://helda.helsinki.fi/server/api/core/bitstreams/5c5a8605-8770-4588-bd75-b575551cd44f/content,2026-10-18,d88f78120eaf29286ec1c7b1e3e16271091458bb8fd682e18b7a886e8013c9e3
banque-mondiale-rapports/upenn_2011_dachis_duranton_turner_ltt_draft.pdf,"Dachis, Duranton et Turner, même titre, version du 4 février 2011, dépôt de l'université de Pennsylvanie",https://repository.upenn.edu/bitstreams/c02e9cae-f352-43a5-bb5b-696f36a348e6/download,2026-10-18,30053f875516c14be7e3a5fee81e1c1f9f20956eb0e4edc51796d89a940d7492
```

Provenance de la copie de Kleven : c'est le PDF de l'éditeur, téléchargé par la LSE le 28/11/2016
et déposé sur la page de cours d'E. Saez ; il porte la mention « For personal use only ». Il peut
servir à relever les pages, mais l'humain décide s'il le conserve dans l'entrepôt. Les deux autres
fichiers sont des dépôts institutionnels en accès libre et n'apportent aucune pagination publiée.

## 6. Reste invérifiable (TODO)

- Pages publiées de Best–Kleven 2018 (citations 6, 7, 8) : accès OUP nécessaire.
- Pages publiées de Määttänen–Terviö 2022 (citation 9) : accès OUP nécessaire.
- Page du résumé publié de Dachis et al. : en principe p. 327, première page de l'article, mais
  non vue. Sans objet si l'on cite « résumé ».
- Concordance des numéros de section entre versions de travail et versions publiées (option 2
  du § 4) : non vérifiable sans les versions publiées.

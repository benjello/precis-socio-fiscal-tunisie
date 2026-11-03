# Plans de suite à la réunion avec l'équipe SOEs de la Banque mondiale (3 novembre 2026)

Note du 3 novembre 2026. Elle part du compte rendu Teams de la réunion de présentation du volume « Les
entreprises publiques » (30 minutes, l'équipe SOEs de la Banque mondiale) et propose, pour chaque
proposition utile, un plan : objectif, sources gratuites, étapes, livrable, effort (S : une séance, M :
quelques séances, L : un chantier). Le compte rendu est généré par l'IA de Teams et peut se tromper ;
ce qui suit ne reprend que ce qui est recoupé par le volume. Règles tenues : rien d'acheté, un
sourçage par chiffre, le descriptif avant l'analyse, les études extérieures à part.

## Ordre proposé

1. Matrice de couverture des données (S) : répond à « la remontée des données reste un défi ».
2. Enquête élargie sur le Registre national des entreprises (S-M).
3. Filiales et entités hors du périmètre administratif, entreprise par entreprise (L, en cours).
4. Tableau de bord du portefeuille en tête du volume (M).
5. Fiche opérationnelle par entreprise (M).
6. Subventions : transparence et retards de paiement (M).
7. Sources complémentaires à l'officiel (S, attend la réponse aux questions du mail).
8. Prévisions à 2030-2035 (décision à prendre ; recommandation : ne pas le faire dans le volume).
9. Portage collectif d'une ressource ouverte (S, hors volume).

## 1. Matrice de couverture des données (S)

*Pourquoi.* Les comptes de résultat des entreprises sont publiés par le ministère des Finances, les bilans
presque jamais ; savoir pour chaque entreprise ce que l'on a, et d'où, est la première réponse.
*Livrable.* Un tableau en annexe : une ligne par entreprise (110 au rapport de 2021), une colonne par type de
source (fiche du ministère par édition, états financiers du Registre, rapport annuel, page de la Bourse,
garanties, dette croisée) et par exercice ; un « – » est une absence constatée, non un oubli.
*Étapes.* (a) relevé généré à partir des séries de `figdata` et des relevés de `listes/` (script, pas de saisie) ;
(b) une colonne « source possible, non obtenue » alimentée par les TODO du volume ; (c) un indicateur de
couverture par année et par type d'entreprise.
*Sources.* Celles du volume ; aucun achat.

## 2. Enquête élargie sur le Registre (S-M)

*Pourquoi.* L'équipe demande d'évaluer l'accès aux informations et le respect de l'obligation de dépôt des
états financiers. L'annexe du Registre couvre 39 entreprises sur 110.
*Étapes.* (a) retrouver les 71 autres par identifiant fiscal, nom commercial et année de création, en parcours de
visiteur et au rythme d'un visiteur ; (b) lire les circulaires n° 17 de 2020 et n° 3 de 2021 (qui doit déposer,
quand) ; (c) indicateur de conformité par entreprise et exercice (déposé / non déposé / non tenu de déposer) ;
(d) demande d'accès à l'information, en brouillon seulement, pour les états financiers déposés.
*Limites.* Le contenu des documents est payant : on mesure le dépôt, pas la qualité des comptes.

## 3. Filiales et entités hors du périmètre administratif (L)

*Pourquoi.* Le périmètre officiel ne retient une filiale que si l'État la détient en majorité ou si une entreprise
publique la détient à 100 % ; des entités gérées par le secteur public en sortent (promotions immobilières des
banques, par exemple). Le périmètre de consolidation de la BNA les montre.
*Pipeline (scripté).* récupération des rapports dans l'Internet Archive (`scripts/` : liste, reprise, catalogue) ;
lecture du périmètre exercice par exercice (`perimetres_groupes_bancaires.py`) ; notices générées
(`notices_rapports_archives.py`) ; relevé dans `listes/` ; tableau et sous-section. Une entreprise à la fois,
rendue et validée avant la suivante : STB (faite), BNA, BH, STAR, Tunis Re, BTE ; puis STEG, ETAP, Tunisair
(notes aux états financiers sur les participations).
*Livrable de fin.* Un relevé « qui détient quoi » (détenteur, détenue, part, date, source) et un test explicite du
seuil de 50 % : les entités que l'État contrôle par une chaîne et que la liste du ministère ne nomme pas.

## 4. Tableau de bord du portefeuille (M)

*Pourquoi.* Demande d'une vue d'ensemble des grands équilibres, avec un zoom sur les grandes entreprises.
*Livrable.* En tête du volume, quatre vues sur la même population : nombre et forme des entreprises ; transferts
du budget et subventions d'exploitation ; dette, garanties et dettes croisées ; résultats et dividendes. Chaque
vue renvoie à la section de l'entreprise. Les séries existent déjà (`figdata`) : le travail est la mise en page,
non la collecte.
*Réserves à dire dans la légende.* Les périmètres changent d'une édition à l'autre (de 33 à 88 entreprises) ; le
tableau ne réunit pas deux familles de chiffres.

## 5. Fiche opérationnelle par entreprise (M)

*Pourquoi.* Une proposition d'enrichir le glossaire : situation et viabilité financières, historique de
restructuration, performance, transferts de l'État et poids budgétaire.
*Livrable.* Un encadré « En bref » en tête de chaque section d'entreprise, engendré par un script depuis les
séries : fonds propres, dette, résultat net, transferts, subvention d'exploitation, et les renvois vers la
restructuration et les garanties. Pas de redondance : l'encadré renvoie, il ne recopie pas les figures.
*Ordre.* STEG, ETAP, Tunisair, SNCFT, STB, BH, BNA, puis les autres.

## 6. Subventions : transparence et retards de paiement (M)

*Pourquoi.* L'octroi des subventions est peu transparent et l'État paie en retard quand elles compensent des
tarifs sociaux.
*Étapes.* (a) rapprocher, par entreprise, transferts du budget, subvention d'exploitation de la fiche et dette
croisée avec l'État (le volume dit déjà que ces grandeurs ne se confondent pas) ; (b) série des créances sur
l'État quand les rapports la donnent ; (c) renvoi vers le volume de la compensation pour les tarifs réduits.
*Limite.* Un retard de paiement ne se lit que s'il est imprimé : sinon, lacune consignée.

## 7. Sources complémentaires (S)

Travaux de la commission de la productivité de la Présidence du gouvernement et bases internationales sur les
entreprises publiques. Attendre les références demandées dans le mail ; les ranger dans la partie « Rapports et
études », chacune avec sa méthode, jamais mêlées aux chiffres budgétaires.

## 8. Prévisions à 2030-2035 (décision)

Le volume est descriptif et sourcé ; une projection suppose un modèle, des hypothèses et une méthode que le
lecteur peut contester. Recommandation : ne pas l'ajouter au volume. Option si elle est voulue : une section
d'études séparée, avec la méthode en tête, quelques scénarios simples sur les transferts et la dette (tendance,
choc, ajustement), et un renvoi explicite vers les séries sources.

## 9. Portage collectif (S, hors volume)

Un volume en licence ouverte, relu par des experts tunisiens. À préciser : qui relit quoi, par quel canal
(tickets du dépôt), et comment les retours sont consignés. Sans engagement de suivi tant qu'une personne n'a
pas donné son accord pour les nouvelles.

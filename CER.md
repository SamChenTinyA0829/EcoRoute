---

## Introduction

> Ce projet vise à optimiser les tournées de livraison pour réduire les distances parcourues et l’impact environnemental.
> 
> 
> Réalisé dans le cadre d’un appel à projets de l’ADEME avec CesiCDP.
> 

---

## 1. Mots clés et à définir

**Mots clés :**

<aside>

- L’ADEME
- Mobilité Multimodale Intelligente
- Optimisation de la gestion des ressources
- Gestion de données de livraison
- Recherche opérationnelle
- Instances de taille importante
- Étude statistique
</aside>

**Mots à définir :**

<aside>

- Fenêtre de temps livraison
- Fenêtre temporelle
- Recommandations PEP
</aside>

---

## 2. Contexte

> L'ADEME nous charge de développer une solution pour optimiser le processus de livraison tout en respectant les contraintes logistiques et environnementales.
> 
> 
> CesiCDP est impliqué pour proposer une solution pratique et démonstrative sur la mobilité multimodale intelligente.
> 

---

## 3. Problématique

<aside>

- Comment optimiser les tournées de livraison pour réduire les distances et l'impact écologique tout en respectant les contraintes de temps, capacité et trafic ?
- Comment améliorer l’efficacité des déplacements tout en réduisant les coûts et l’impact environnemental ?
</aside>

---

## 4. Contraintes et besoins

### 4.1 Contraintes

<aside>

- Fenêtre de temps
- Nombre de camions disponibles
- Capacité des camions (dimensions, poids, volume)
- Trafic variable selon les horaires
- Dépôts uniques ou multiples
- Points de collecte multiples
- Distances et temps de parcours dynamiques
- Gestion des cas particuliers : client absent, annulation
- Catégories :
    - Contraintes modifiant uniquement la valeur des solutions (ex. attente avant ouverture)
    - Contraintes modifiant l’espace des solutions (ex. certains objets nécessitant un type de camion spécifique)
</aside>

### 4.2 Besoins

<aside>

- Carte du réseau de livraison
- Nombre et dimension des camions
- Type et volume des produits à livrer
- Différents points de collecte
- Fenêtres temporelles
- Plages de validité temporelles
- Minimiser la consommation énergétique
- Liste des clients à desservir
</aside>

---

## 5. Livrables

### 5.1 Modélisation (Notebook Jupyter) (Toggle)

<aside>

- **Date de rendu :** au cours de prosit 3
- Représentation formelle des données et objectif à optimiser (incluant les contraintes)
- Étude de la complexité théorique avec références
- Validation avec le tuteur avant intégration dans le livrable final
</aside>

### 5.2 Livrable final (Toggle)

<aside>

- **Date de rendu :** 13/14 Novembre
- Modélisation complète du problème dans Jupyter
- Présentation de la démarche, réalisation technique et résultats obtenus
    
    ### Partie 1 : Modélisation
    
    - Mise à jour des éléments formels
    - Description de la méthode de résolution choisie (métaheuristique, voisinage, opérations de croisement…)
    
    ### Partie 2 : Implémentation
    
    - Implémentation de l’algorithme et des cas de test
    - Démonstration du fonctionnement sur différents cas
    
    ### Partie 3 : Étude expérimentale
    
    - Analyse du comportement expérimental de la solution
    - Plan d’expérience complet : performances, limitations et perspectives d’amélioration
</aside>

### 5.3 Soutenance

<aside>

- Présentation orientée résultats
- Démonstration du code sur cas réduits
- Mise en valeur du contexte, objectifs et étapes réalisées
- Présentation du planning ou échéancier
</aside>

---

## 6. Généralisation

<aside>

- Optimiser les tournées de livraison
- Réduire la distance parcourue
- Diminuer l’impact environnemental
- Améliorer le processus logistique tout en respectant les contraintes
</aside>

---

## 7. Pistes de solutions

<aside>

- Gestion des crises clients (absences, annulations)
- Fonctions de calcul du temps et du coût des tournées
</aside>

---

## 8. Plan d’action (non technique)

<aside>

- Clarification du périmètre et des contraintes
- Répartition des rôles et responsabilités dans l’équipe
- Suivi via planning (Gantt ou Kanban)
- Réunions régulières et reporting intermédiaire
- Validation avec le tuteur
- Préparation des livrables intermédiaires et finaux
- Organisation de la soutenance
</aside>

---
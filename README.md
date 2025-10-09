# Projet EcoRoute - optimisation de tournes durables.

## Introduction

Ce projet a pour objectif de développer une solution algorithmique permettant d’optimiser les tournées de livraison pour réduire les distances parcourues et l’impact environnemental.  
Le projet est réalisé dans le cadre d’un appel à projets de l’ADEME, en collaboration avec CesiCDP.  
Il combine modélisation combinatoire, gestion de contraintes logistiques réelles et étude expérimentale afin de proposer un outil de planification efficace et durable.

---

### 1. Mots clés et à définir

| Mots clés                                   | Mots à définir                   |
| ------------------------------------------- | ------------------------------- |
| L’ADEME                                     | Fenêtre de temps livraison      |
| Mobilité Multimodale Intelligente           | Fenêtre temporelle              |
| Optimisation de la gestion des ressources   | Recommandations PEP             |
| Gestion de données de livraison             |                                 |
| Recherche opérationnelle                     |                                 |
| Instances de taille importante              |                                 |
| Étude statistique                            |                                 |

---

### 2. Contexte

L'ADEME nous charge de développer une solution pour optimiser le processus de livraison tout en respectant les contraintes logistiques et environnementales.

---

### 3. Problématique

- Comment optimiser les tournées de livraison afin de réduire les distances parcourues et l'impact environnemental, tout en respectant les contraintes réelles liées au temps, à la capacité des véhicules et au trafic routier ?  
- Comment concevoir une solution d'optimisation permettant d'améliorer l'efficacité des déplacements tout en réduisant les coûts et l'impact environnemental ?

---

### 4. Contraintes et Besoins

#### 4.1 Contraintes

- Fenêtre de temps de livraison  
- Nombre de camions disponibles simultanément  
- Capacités des camions (dimensions, volume, poids)  
- Trafic variable selon les horaires  
- Dépôt unique ou multiples  
- Points de collecte multiples  
- Distances et temps de parcours dynamiques  
- Catégories :  
  - Contraintes modifiant uniquement les valeurs des solutions (ex. attente avant ouverture d’une fenêtre)  
  - Contraintes modifiant l’espace des solutions (ex. certains objets nécessitant un camion spécifique)  
- Gestion des cas particuliers : client absent, annulation de commande

#### 4.2 Besoins

- Carte du réseau de livraison  
- Nombre et dimension des camions  
- Type et volume des produits à livrer  
- Différents points de collecte  
- Fenêtres temporelles  
- Plages de validité temporelles  
- Minimiser la consommation énergétique  
- Liste des clients à desservir

---

### 5. Livrables

#### 5.1 Modélisation (Notebook Jupyter)

- **Date de rendu : au cours de prosit 3 (dans 2 semaines)**  
- Représentation formelle des données et de l’objectif à optimiser (incluant les contraintes)  
- Démonstration de la complexité théorique du problème (références incluses)  
- Validation avec les tuteurs et intégration dans le livrable final

#### 5.2 Livrable final

- **Date de rendu : 13/14 Novembre**  
- Modélisation complète du problème dans Jupyter  
- Présentation de l’ensemble de la démarche et des résultats obtenus  

**PARTIE 1 : Modélisation**  
- Reprise des éléments formels mis à jour  
- Description de la méthode de résolution choisie (métaheuristique, voisinage, opérations de croisement…)

**PARTIE 2 : Implémentation**  
- Implémentation de l’algorithme et des cas de test  
- Démonstration sur différents cas (pas besoin d’être exhaustif)

**PARTIE 3 : Étude expérimentale**  
- Analyse du comportement expérimental de la solution  
- Plan d’expérience complet, performances, limitations et perspectives d’amélioration  

#### 5.3 Soutenance

- Présentation orientée résultats avec exécution du code sur des cas réduits  
- Mise en valeur du contexte, des objectifs, des défis, des étapes achevées et à venir  
- Présentation du planning ou échéancier

---

### 6. Généralisation

Optimiser les tournées de livraison afin de réduire les distances parcourues, diminuer l’impact environnemental et améliorer le processus logistique tout en respectant les contraintes imposées.

---

### 7. Pistes de solutions

- Gestion des crises client (absences, annulations)  
- Fonctions de calcul du temps de parcours  
- Fonctions de calcul du coût des tournées

---

### 8. Plan d’action (non technique)

- Clarification du périmètre et des objectifs  
- Répartition des rôles et responsabilités dans l’équipe  
- Planification et suivi via Gantt ou Kanban  
- Réunions régulières et reporting intermédiaire  
- Validation régulière avec le tuteur  
- Préparation des livrables intermédiaires et finaux  
- Organisation de la soutenance



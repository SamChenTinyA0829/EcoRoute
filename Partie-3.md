*Optimisation des Tournées de Livraison : Documentation Technique et Méthodologique*

# 3. Analyse et Modélisation du Problème

## 3.1. Description du Système Réel

>Le système de livraison que nous étudions représente l'ensemble des opérations quotidiennes d'une entreprise de logistique. Voici les composantes principales :

### Acteurs du système

- **Les dépôts** : Points de départ et d'arrivée des camions, où sont stockées les marchandises
- **Les clients** : Destinataires des livraisons, répartis géographiquement dans une zone urbaine ou périurbaine
- **Les véhicules** : Flotte de camions avec des caractéristiques différentes (capacité, type, consommation)
- **Les chauffeurs** : Opérateurs effectuant les tournées selon des horaires de travail


### Flux opérationnels
1. **Préparation** : Chargement des marchandises au dépôt selon les commandes
2. **Tournée** : Déplacement du véhicule pour desservir plusieurs clients
3. **Livraison** : Déchargement chez chaque client dans sa fenêtre horaire
4. **Retour** : Retour au dépôt en fin de tournée

### Exemple concret
```
Dépôt Central 🏠 (Paris 13e) 
    ↓
Client A (Boulangerie - 50kg) → 9h-11h
    ↓
Client B (Restaurant - 80kg) → 10h-12h
    ↓
Client C (Supermarché - 120kg) → 11h-14h
    ↓
Retour Dépôt 🏠

> Camion utilisé 🚚 : 
 - Capacité: 300kg, 
 - Vitesse moyenne: 30km/h
```



## 3.2. Hypothèses de Modélisation

Pour transformer ce système réel complexe en un modèle mathématique exploitable, nous posons les hypothèses suivantes :

### **H1 - Connaissance parfaite des données**
- Les adresses clients sont connues et géolocalisées
- Les quantités à livrer sont déterminées à l'avance
- Les fenêtres horaires sont fixes et connues

### **H2 - Réseau routier**
- Le réseau est représentable par un graphe
- Les distances sont calculables (euclidienne ou réelle via API)
- Les temps de trajet peuvent être estimés avec une vitesse moyenne

### **H3 - Contraintes véhicules**
- Chaque véhicule part et revient au même dépôt
- La capacité est une contrainte stricte (poids ou volume)
- Le nombre de véhicules est limité et connu

### **H4 - Simplifications**
- Pas de pannes ou incidents imprévus
- Temps de service (déchargement) constant ou proportionnel
- Trafic modélisé par tranches horaires (non temps réel)

### **H5 - Objectif principal**
- Minimiser la distance totale parcourue (ou le coût/émissions)
- Respecter toutes les contraintes strictes (fenêtres, capacité)

### Limites assumées : les blocages 
⚠️ **Ce que le modèle ne prend pas en compte** :
```
- Accidents ou déviations non prévues
- Météo affectant les conditions de circulation
- Disponibilité variable du personnel
- Modifications de commandes en temps réel
```


## 3.3. Représentation Schématique du Système

### Vue d'ensemble du système

```
┌─────────────────────────────────────────────────────────┐
│                    SYSTÈME DE LIVRAISON                  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────┐                                           │
│  │  DÉPÔT   │ ──────┐                                   │
│  │ (Origine)│       │                                   │
│  └──────────┘       │                                   │
│       ▲             ▼                                   │
│       │      ┌─────────────┐                            │
│       │      │  TOURNÉE 1  │                            │
│       │      │ Camion 10T  │                            │
│       │      └──────┬──────┘                            │
│       │             │                                   │
│       │             ├─→ Client A (9h-11h, 50kg)         │
│       │             ├─→ Client B (10h-12h, 80kg)        │
│       │             └─→ Client C (11h-14h, 120kg)       │
│       │                                                 │
│       │      ┌─────────────┐                            │
│       │      │  TOURNÉE 2  │                            │
│       └──────│ Camion 5T   │                            │
│              └──────┬──────┘                            │
│                     │                                   │
│                     ├─→ Client D (8h-10h, 30kg)         │
│                     └─→ Client E (13h-15h, 45kg)        │
│                                                          │
│  Contraintes :                                          │
│  • Fenêtres horaires strictes                           │
│  • Capacité maximale des camions                        │
│  • Temps de trajet variables                            │
│  • Retour obligatoire au dépôt                          │
└─────────────────────────────────────────────────────────┘
```

### Schéma de flux décisionnel

```
    [Données d'entrée]
           ↓
    ┌──────────────┐
    │ • N clients  │
    │ • K camions  │
    │ • Distances  │
    │ • Contraintes│
    └──────┬───────┘
           ↓
    ┌──────────────────┐
    │  ALGORITHME      │
    │  D'OPTIMISATION  │
    └──────┬───────────┘
           ↓
    ┌──────────────────┐
    │  Solutions       │
    │  • Affectation   │
    │  • Séquences     │
    │  • Horaires      │
    └──────┬───────────┘
           ↓
    [Tournées optimisées]
```

---

## 3.4. Structure du Graphe

### Définition formelle

Notre problème se modélise par un **graphe orienté pondéré** G = (V, A) où :

**Sommets (V)** :
```
- V = {0} ∪ {1, 2, ..., n}
- Sommet 0 : le dépôt
- Sommets 1 à n : les clients à livrer
```

**Arcs (A)** :
```
- A = {(i, j) | i, j ∈ V, i ≠ j}
- Chaque arc représente un déplacement possible entre deux points
```

### Pondérations

Chaque arc **(i, j)** possède plusieurs attributs :

1. **Distance** : **d(i,j)** = distance en km entre i et j
2. **Temps** : **t(i,j)** = temps de trajet entre i et j
3. **Coût** : **c(i,j)** = coût associé (carburant, péage, etc.)

Chaque sommet client i possède :
- **Demande** : q(i) = quantité à livrer (kg ou m³)
- **Fenêtre temporelle** : [e(i), l(i)] = heure d'ouverture et de fermeture
- **Temps de service** : **s(i)** = durée de déchargement

### Exemple graphique

```
        🏠Dépôt (0)
       /    |    \
     /      |      \
   🚚10km   🚚8km     🚚15km
   /        |        \
  /         |         \
Client A   Client B   Client C
(q=50kg)   (q=80kg)   (q=120kg)
[9h-11h]   [10h-12h]  [11h-14h]

        12km    18km
    A -----→ B -----→ C
```

### Représentation matricielle

**Matrice des distances** (exemple 4 points) :

```
      0    A    B    C
  ┌────────────────────┐
0 │  0   10    8   15  │ (Dépôt)
A │ 10    0   12   20  │
B │  8   12    0   18  │
C │ 15   20   18    0  │
  └────────────────────┘
```

### Contraintes du graphe

**Contrainte 1 - Conservation du flot** :
Chaque client doit être visité exactement une fois
```
Fonction Contrainte associée : 
∑ x(i,j) = 1  pour tout j ∈ {1,...,n}
i∈V
```

**Contrainte 2 - Capacité** :
La somme des demandes sur une tournée ≤ capacité du camion
```
Fonction Contrainte associée : 
∑ q(i) ≤ Q  pour chaque tournée k
i ∈ tournée k
```

**Contrainte 3 - Fenêtres temporelles** :
Arrivée chez client i dans **[e(i), l(i)]**
```
e(i) ≤ arrivée(i) ≤ l(i)
```

**Contrainte 4 - Origine/Destination** :
Toute tournée commence et finit au dépôt (sommet 0)



## 3.5. Limites et Simplifications du Modèle

### Limites identifiées

#### **L1 - Statique vs Dynamique**
>**Limite** : Le modèle est statique (toutes les données connues à l'avance)
**Réalité** : Nouvelles commandes, annulations, trafic changeant
**Impact** : Solution non adaptable en temps réel

#### **L2 - Incertitude**
>**Limite** : Temps de trajet et de service déterministes
**Réalité** : Variations dues au trafic, retards clients
**Impact** : Risque de non-respect des fenêtres horaires

#### **L3 - Complexité du réseau**
>**Limite** : Distances simplifiées (euclidienne ou matrice)
**Réalité** : Sens uniques, interdictions, travaux
**Impact** : Estimation imprécise des trajets réels

#### **L4 - Facteur humain**
>**Limite** : Chauffeur comme ressource parfaite
**Réalité** : Fatigue, pauses légales, préférences
**Impact** : Tournées moins réalistes

### Simplifications potentielles :

#### **S1 - Homogénéité de la flotte**
Tous les camions de même capacité (peut être levé facilement)
```python
# Simplifié
capacite = 1000  # pour tous

# Réaliste
capacites = {
    'camion_1': 1000,
    'camion_2': 1500,
    'camion_3': 500
}
```

#### **S2 - Monodépôt**
Un seul dépôt (extension à multi-dépôts possible)

#### **S3 - Pas de rechargement**
Pas de retour intermédiaire au dépôt pendant une tournée

#### **S4 - Fenêtres strictes**
Impossibilité de livrer hors fenêtre (en réalité, pénalités possibles)

### Justification des simplifications

Ces simplifications permettent :
>- **✓ Un premier modèle fonctionnel et testable** 🖥️
>- **✓ Une complexité algorithmique raisonnable** ⚙️
>- **✓ Une compréhension claire du problème** 🧠
>- **✓ Une base extensible pour versions futures** 📊

**Stratégie d'amélioration proposée** :
>- **Phase 1 (actuelle)** → Modèle simplifié fonctionnel
>- **Phase 2**→ Ajout flotte hétérogène
>- **Phase 3** → Intégration trafic temps réel
>- **Phase 4** → Multi-dépôts et rechargements


---

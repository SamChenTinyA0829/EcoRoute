# 5. Méthodologie et Approche de Résolution

## 5.1. Présentation des Approches Possibles

### **Classification du problème**

>Notre problème est un **Vehicle Routing Problem with Time Windows (VRPTW)**, une extension du VRP classique.

#### **Complexité théorique**

```
┌─────────────────────────────────────────────┐
│  Classe de complexité : NP-Difficile        │
├─────────────────────────────────────────────┤
│                                             │
│  P : Problèmes résolubles en temps          │
│      polynomial (ex: tri, plus court        │
│      chemin)                                │
│                                             │
│  NP : Vérifiable en temps polynomial        │
│       (ex: factorisation)                   │
│                                             │
│  NP-Complet : Les + difficiles de NP        │
│               (ex: SAT, Clique)             │
│                                             │
│  NP-Difficile : Au moins aussi dur que      │
│                 NP-Complet                  │
│                 ► VRPTW est ici ◄           │
│                                             │
└─────────────────────────────────────────────┘

Implications :
• Pas d'algorithme polynomial connu
• Temps de calcul croît exponentiellement
• Pour n=10 clients: ~3 millions de solutions
• Pour n=20 clients: ~10^18 solutions possibles
```

### **Approches de résolution**

#### A1 - Méthodes Exactes

**Principe** : Garantir l'optimalité mathématique

**Techniques** :
- **Programmation linéaire en nombres entiers (PLNE)**
- **Branch & Bound** : exploration systématique avec élagage
- **Programmation dynamique** : décomposition en sous-problèmes

**Avantages** :
✓ Solution optimale garantie
✓ Preuve mathématique

**Inconvénients** :
✗ Temps de calcul prohibitif (> 20 clients)
✗ Ressources mémoire importantes

**Exemple - Formulation PLNE** :
```
Minimiser: ∑∑ c(i,j) × x(i,j)
           i j

Sujet à:
∑ x(i,j) = 1    ∀j (chaque client visité)
i
∑ q(i) ≤ Q      (capacité)
i
e(i) ≤ t(i) ≤ l(i)  (fenêtres)
```

#### A2 - Heuristiques Constructives

**Principe** : Construire une solution pas à pas

**Techniques** :
- **Plus Proche Voisin** : choisir le client le plus proche
- **Savings Algorithm (Clarke & Wright)** : fusion de routes
- **Insertion séquentielle** : insertion au meilleur coût

**Avantages** :
✓ Rapide (O(n²) ou O(n³))
✓ Solution acceptable en quelques secondes

**Inconvénients** :
✗ Pas d'optimalité garantie
✗ Qualité variable selon les données

**Exemple - Plus Proche Voisin** :
```
1. Partir du dépôt
2. Tant qu'il reste des clients:
   - Choisir le plus proche non visité
   - Si capacité OK et fenêtre respectée:
     → Ajouter à la tournée
   - Sinon: nouvelle tournée
3. Retour au dépôt
```

#### A3 - Métaheuristiques

**Principe** : Explorer intelligemment l'espace de solutions

**Techniques** :

**Recherche Locale** :
- **2-opt** : inverser un segment de route
- **Or-opt** : déplacer une séquence
- **Échange inter-routes** : échanger clients entre tournées

**Algorithmes évolutionnaires** :
- **Algorithmes génétiques** : sélection, croisement, mutation
- **Recuit simulé** : acceptation probabiliste de dégradations

**Intelligence collective** :
- **Colonies de fourmis** : phéromones virtuelles
- **Essaims particulaires** : mouvement collectif

**Avantages** :
✓ Très bonnes solutions en temps raisonnable
✓ Adaptable à grandes instances (100+ clients)
✓ Exploration diversifiée

**Inconvénients** :
✗ Pas d'optimalité garantie
✗ Réglage des paramètres nécessaire

**Schéma - Recherche Locale** :
```
Solution Initiale
      ↓
   ┌──────┐
   │ 2-opt│ → Amélioration trouvée? → Oui → Appliquer
   └───┬──┘                                    ↓
       ↑←────────── Non ←──────────────────────┘
       
Itérer jusqu'à:
• Aucune amélioration (optimum local)
• Temps limite atteint
```

#### A4 - Approches Hybrides

Combiner plusieurs méthodes :
- Heuristique constructive + Recherche locale
- Métaheuristique + Optimisation exacte sur sous-problèmes
- Multi-start : plusieurs constructions puis amélioration

---

## 5.2. Choix de la Stratégie Retenue

### Décision : Approche Hybride

**Configuration retenue** :
```
Phase 1: Heuristique constructive (Clarke & Wright)
   ↓
Phase 2: Amélioration locale (2-opt + Or-opt)
   ↓
Phase 3: (Optionnel) Métaheuristique (Recuit Simulé)
```

### Justification du choix

#### Critère 1 - Taille des instances
- Instances attendues : 20-100 clients
- Méthodes exactes non viables au-delà de 20 clients
→ **Heuristiques nécessaires**

#### Critère 2 - Qualité vs Temps
- Besoin : solution en < 1 minute
- Qualité visée : écart < 10% de l'optimal
→ **Métaheuristiques appropriées**

#### Critère 3 - Simplicité d'implémentation
- Contrainte temps : 3 semaines de développement
- Compétences équipe : Python intermédiaire
→ **Heuristiques classiques privilégiées**

#### Critère 4 - Démonstrabilité
- Présentation devant jury
- Besoin de visualisation claire
→ **Approche progressive** (constructive puis amélioration)

### Tableau comparatif

| Approche | Temps | Qualité | Complexité | Choix |
|----------|-------|---------|------------|-------|
| PLNE | +++ | ★★★★★ | +++++ | ✗ |
| Heuristique simple | ★ | ★★☆☆☆ | ★★☆☆☆ | (Phase 1) |
| Recherche locale | ★★☆☆☆ | ★★★★☆ | ★★★☆☆ | ✓ Phase 2 |
| Algorithme génétique | ★★★☆☆ | ★★★★☆ | ★★★★☆ | Option |
| Recuit simulé | ★★☆☆☆ | ★★★★☆ | ★★★☆☆ | ✓ Phase 3 |

---

## 5.3. Algorithmes Explorés

### Algorithme 1 : Clarke & Wright (Savings Algorithm)

**Principe** :
Partir de routes individuelles (1 client = 1 tournée) puis fusionner les routes dont la fusion économise le plus de distance.

**Formule du "saving"** :
```
s(i,j) = d(0,i) + d(0,j) - d(i,j)

Interprétation:
• d(0,i) + d(0,j) : coût de 2 tournées séparées
• d(i,j) : coût si i et j dans même tournée
• s(i,j) > 0 : économie réalisée
```

**Pseudo-code** :
```
1. Créer n tournées: [0 → i → 0] pour i=1..n
2. Calculer tous les savings s(i,j)
3. Trier les savings par ordre décroissant
4. Pour chaque saving s(i,j):
   Si i et j dans routes différentes:
      Et fusion respecte capacité et fenêtres:
         → Fusionner les routes
5. Retourner les tournées finales
```

**Exemple mini** :
```
Données:
Dépôt 0, Clients A, B, C
d(0,A)=10, d(0,B)=15, d(0,C)=12
d(A,B)=8, d(A,C)=9, d(B,C)=7

Savings:
s(A,B) = 10+15-8 = 17 ★★★ (max)
s(A,C) = 10+12-9 = 13
s(B,C) = 15+12-7 = 20 ★★★★★ (max!)

Application:
1. Routes initiales: [0→A→0], [0→B→0], [0→C→0]
2. s(B,C)=20 le plus grand → fusionner B et C
   Routes: [0→A→0], [0→B→C→0]
3. s(A,B)=17 suivant → fusionner A avec B
   Routes: [0→A→B→C→0]
```

### Algorithme 2 : 2-opt (Amélioration locale)

**Principe** :
Inverser l'ordre de visite d'un segment de route si cela réduit la distance.

**Visualisation** :
```
Avant:           Après 2-opt:
0→A→B→C→D→0     0→A→C→B→D→0
   └──→──┘         └──←──┘
   
Suppression arcs (A,B) et (C,D)
Ajout arcs (A,C) et (B,D)
Gain si: d(A,B)+d(C,D) > d(A,C)+d(B,D)
```

**Pseudo-code** :
```
Répéter jusqu'à convergence:
  amélioration = False
  Pour i de 1 à n-2:
    Pour j de i+2 à n:
      Si inversion(i,j) réduit distance:
        Appliquer inversion
        amélioration = True
  Si pas amélioration: STOP
```

**Exemple** :
```
Route: 0 → 1 → 2 → 3 → 4 → 0
Distance actuelle: 10+5+8+6+12 = 41

Test inversion entre 2 et 3:
Nouvelle route: 0 → 1 → 3 → 2 → 4 → 0
Nouvelle distance: 10+7+4+9+12 = 42 (pire, rejeté)

Test inversion entre 1 et 3:
Nouvelle route: 0 → 3 → 2 → 1 → 4 → 0
Nouvelle distance: 11+4+5+8+12 = 40 (meilleur!)
→ Appliqué
```

### Algorithme 3 : Or-opt

**Principe** :
Extraire une séquence de 1, 2 ou 3 clients consécutifs et la réinsérer ailleurs.

**Illustration** :
```
Route: 0 → A → B → C → D → E → 0

Extraction de B:
0 → A → [B] → C → D → E → 0

Réinsertion après D:
0 → A → C → D → [B] → E → 0

Gain si: distance_nouvelle < distance_ancienne
```

### Algorithme 4 : Recuit Simulé (optionnel)

**Principe inspiré de la physique** :
Accepter parfois des solutions moins bonnes pour échapper aux optima locaux.

**Métaphore** :
```
T (température) élevée → Accepte facilement dégradations
                         (exploration large)
T diminue               → Devient plus sélectif
                         (exploitation)
T proche 0              → N'accepte que améliorations
                         (convergence)
```

**Algorithme** :
```python
T = T_initial  # ex: 1000
T_min = 0.01
alpha = 0.95   # taux refroidissement

solution_courante = solution_initiale
meilleure = solution_courante

Tant que T > T_min:
    voisin = generer_voisin(solution_courante)
    delta = cout(voisin) - cout(solution_courante)
    
    Si delta < 0:  # Amélioration
        solution_courante = voisin
        Si cout(voisin) < cout(meilleure):
            meilleure = voisin
    Sinon:  # Dégradation
        proba = exp(-delta / T)
        Si random() < proba:
            solution_courante = voisin  # Accepté!
    
    T = T * alpha  # Refroidissement
```

**Paramètres clés** :
- T_initial : exploration initiale (valeur élevée)
- Alpha : vitesse refroidissement (0.9-0.99)
- T_min : critère d'arrêt

---

## 5.4. Outils et Environnement Technique

### Langage principal : Python 3.10+

**Justification** :
- ✓ Lisibilité et prototypage rapide
- ✓ Écosystème riche (bibliothèques scientifiques)
- ✓ Jupyter Notebook pour présentation pédagogique
- ✓ Compétences de l'équipe

### Bibliothèques utilisées

#### 1. **NumPy** (v1.24+)
```python
import numpy as np
```

**Utilité** :
- Calculs matriciels efficaces (matrices de distances)
- Opérations vectorielles (sommes, moyennes)
- Génération de données aléatoires (tests)

**Exemple d'usage** :
```python
# Matrice des distances
distances = np.array([
    [0, 10, 15, 20],
    [10, 0, 12, 18],
    [15, 12, 0, 8],
    [20, 18, 8, 0]
])

# Calcul économie Clarke & Wright
savings = distances[0,:] + distances[:,0] - distances
```

#### 2. **Pandas** (v2.0+)
```python
import pandas as pd
```

**Utilité** :
- Manipulation de données tabulaires (clients, commandes)
- Import/Export CSV
- Analyses statistiques des résultats

**Exemple d'usage** :
```python
# Chargement données clients
clients = pd.read_csv('clients.csv')
#   id  lat    lon    demande  debut  fin
# 0  1  48.85  2.35   50       9      11
# 1  2  48.87  2.33   80       10     12

# Filtrage fenêtre matinale
matin = clients[clients['debut'] < 12]
```

#### 3. **Matplotlib + Seaborn**
```python
import matplotlib.pyplot as plt
import seaborn as sns
```

**Utilité** :
- Visualisation des tournées sur carte
- Graphiques de performance (convergence, comparaisons)
- Présentation des résultats

**Exemple** :
```python
# Tracer une tournée
plt.figure(figsize=(10,8))
plt.plot(route_x, route_y, 'b-o')
plt.scatter(depot_x, depot_y, c='red', s=200, marker='s')
plt.title("Tournée optimisée - Distance: 145km")
```

#### 4. **NetworkX** (optionnel)
```python
import networkx as nx
```

**Utilité** :
- Représentation graphe du réseau
- Algorithmes de graphe (plus court chemin)
- Visualisation structure réseau

#### 5. **OR-Tools** (Google) - optionnel avancé
```python
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
```

**Utilité** :
- Résolveur spécialisé VRP
- Benchmark de nos solutions
- Solution exacte pour petites instances

**Note** : Utilisation comme point de comparaison, pas méthode principale

#### 6. **Geopy** (calcul distances réelles)
```python
from geopy.distance import geodesic
```

**Utilité** :
- Calcul distance géographique entre coordonnées
- Alternative à distance euclidienne

**Exemple** :
```python
point1 = (48.8566, 2.3522)  # Paris
point2 = (48.8738, 2.2950)  # La Défense
distance = geodesic(point1, point2).km  # 5.8 km
```

### Environnement de développement

**IDE/Éditeur** :
- Jupyter Notebook (documentation interactive)
- VS Code (développement code)

**Gestion version** :
- Git + GitHub/GitLab

**Tests** :
- pytest pour tests unitaires
- instances benchmark (Solomon, Gehring & Homberger)

---

## 5.5. Structure du Code

### Architecture générale

```
projet_vrptw/
│
├── data/                    # Données
│   ├── clients.csv
│   ├── distances.npy
│   └── instances/          # Jeux de tests
│
├── src/                     # Code source
│   ├── __init__.py
│   ├── models.py           # Classes de base
│   ├── algorithms/
│   │   ├── constructive.py # Clarke & Wright
│   │   ├── local_search.py # 2-opt, Or-opt
│   │   └── metaheuristic.py # Recuit simulé
│   ├── utils.py            # Fonctions utilitaires
│   └── visualization.py    # Graphiques
│
├── notebooks/               # Notebooks Jupyter
│   ├── 01_modelisation.ipynb
│   ├── 02_implementation.ipynb
│   └── 03_experimentation.ipynb
│
├── tests/                   # Tests unitaires
│   ├── test_algorithms.py
│   └── test_utils.py
│
├── results/                 # Résultats et exports
│   ├── figures/
│   └── solutions/
│
├── requirements.txt         # Dépendances
└── README.md
```

### Pipeline de traitement

```
┌─────────────────────────────────────────────────────────┐
│                   PIPELINE COMPLET                       │
└─────────────────────────────────────────────────────────┘

[1] CHARGEMENT DONNÉES
    ↓
    • Lecture CSV clients
    • Calcul matrice distances
    • Validation contraintes
    ↓
[2] PRÉTRAITEMENT
    ↓
    • Vérification faisabilité
    • Clustering optionnel (zones géographiques)
    • Normalisation données
    ↓
[3] CONSTRUCTION INITIALE
    ↓
    • Algorithme Clarke & Wright
    • Génération solution de base
    ↓
[4] AMÉLIORATION LOCALE
    ↓
    • Application 2-opt
    • Application Or-opt
    • Itérations jusqu'à convergence
    ↓
[5] MÉTAHEURISTIQUE (optionnel)
    ↓
    • Recuit simulé
    • Exploration globale
    ↓
[6] VALIDATION & EXPORT
    ↓
    • Vérification contraintes
    • Calcul métriques (distance, coût, émissions)
    • Export résultats
    ↓
[7] VISUALISATION
    ↓
    • Cartes des tournées
    • Graphiques convergence
    • Rapport final
```

### Classes principales

#### Classe `Client`
```python
class Client:
    """Représente un client à livrer"""
    
    def __init__(self, id, x, y, demande, debut, fin, service=10):
        self.id = id                # Identifiant unique
        self.x = x                  # Coordonnée X (longitude)
        self.y = y                  # Coordonnée Y (latitude)
        self.demande = demande      # Quantité à livrer (kg)
        self.debut = debut          # Début fenêtre (minutes depuis minuit)
        self.fin = fin              # Fin fenêtre
        self.service = service      # Temps de service (minutes)
    
    def distance_to(self, other):
        """Distance euclidienne vers autre client"""
        return np.sqrt((self.x - other.x)**2 + 
                       (self.y - other.y)**2)
    
    def __repr__(self):
        return f"Client({self.id}, q={self.demande}, tw=[{self.debut},{self.fin}])"
```

**Exemple d'utilisation** :
```python
# Création clients
depot = Client(0, 0, 0, 0, 0, 1440)  # Dépôt (ouvert 24h)
c1 = Client(1, 10, 5, 50, 540, 660)  # 9h-11h
c2 = Client(2, 15, 8, 80, 600, 720)  # 10h-12h

# Calcul distance
dist = c1.distance_to(c2)  # 5.83 unités
```

#### Classe `Route`
```python
class Route:
    """Représente une tournée de livraison"""
    
    def __init__(self, depot, capacite_max):
        self.depot = depot
        self.capacite_max = capacite_max
        self.clients = []           # Séquence de clients
        self.charge_actuelle = 0
        self.temps_actuel = 0
    
    def peut_ajouter(self, client):
        """Vérifie si on peut ajouter ce client"""
        # Vérif capacité
        if self.charge_actuelle + client.demande > self.capacite_max:
            return False
        
        # Vérif fenêtre temporelle
        dernier = self.clients[-1] if self.clients else self.depot
        temps_arrivee = self.temps_actuel + dernier.distance_to(client)
        
        if temps_arrivee > client.fin:
            return False  # Trop tard
        
        return True
    
    def ajouter_client(self, client):
        """Ajoute un client à la tournée"""
        if not self.peut_ajouter(client):
            raise ValueError("Impossible d'ajouter ce client")
        
        dernier = self.clients[-1] if self.clients else self.depot
        temps_arrivee = self.temps_actuel + dernier.distance_to(client)
        
        # Attendre si arrivée avant ouverture
        temps_debut_service = max(temps_arrivee, client.debut)
        
        self.clients.append(client)
        self.charge_actuelle += client.demande
        self.temps_actuel = temps_debut_service + client.service
    
    def distance_totale(self):
        """Calcule la distance totale de la tournée"""
        if not self.clients:
            return 0
        
        distance = self.depot.distance_to(self.clients[0])
        
        for i in range(len(self.clients) - 1):
            distance += self.clients[i].distance_to(self.clients[i+1])
        
        distance += self.clients[-1].distance_to(self.depot)
        return distance
    
    def __repr__(self):
        ids = [c.id for c in self.clients]
        return f"Route({ids}, charge={self.charge_actuelle}/{self.capacite_max})"
```

**Exemple d'utilisation** :
```python
# Création d'une tournée
route = Route(depot, capacite_max=200)

# Ajout de clients
route.ajouter_client(c1)  # OK
route.ajouter_client(c2)  # OK si capacité et temps OK

# Métriques
print(route.distance_totale())  # 45.2 km
print(route)  # Route([1, 2], charge=130/200)
```

#### Classe `Solution`
```python
class Solution:
    """Représente une solution complète (ensemble de tournées)"""
    
    def __init__(self, routes=None):
        self.routes = routes if routes else []
    
    def distance_totale(self):
        """Distance totale de toutes les tournées"""
        return sum(route.distance_totale() for route in self.routes)
    
    def nombre_vehicules(self):
        """Nombre de véhicules utilisés"""
        return len(self.routes)
    
    def cout_total(self, cout_km=2, cout_vehicule=50):
        """Coût total : distance + véhicules"""
        return (self.distance_totale() * cout_km + 
                self.nombre_vehicules() * cout_vehicule)
    
    def emissions_co2(self, emission_par_km=0.8):
        """Estimation émissions CO2 (kg)"""
        return self.distance_totale() * emission_par_km
    
    def est_valide(self):
        """Vérifie que toutes les contraintes sont respectées"""
        for route in self.routes:
            # Vérif capacité
            if route.charge_actuelle > route.capacite_max:
                return False
            
            # Vérif fenêtres temporelles
            temps = 0
            dernier = route.depot
            for client in route.clients:
                temps += dernier.distance_to(client)
                if temps > client.fin:
                    return False
                temps = max(temps, client.debut) + client.service
                dernier = client
        
        return True
    
    def copie(self):
        """Crée une copie indépendante"""
        nouvelles_routes = [Route(r.depot, r.capacite_max) 
                           for r in self.routes]
        for i, route in enumerate(self.routes):
            for client in route.clients:
                nouvelles_routes[i].ajouter_client(client)
        return Solution(nouvelles_routes)
    
    def __repr__(self):
        return (f"Solution(vehicules={self.nombre_vehicules()}, "
                f"distance={self.distance_totale():.1f})")
```

### Exemple complet - Notebook simplifié

```python
# ============================================
# NOTEBOOK : Résolution VRPTW
# ============================================

# --- IMPORTS ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.models import Client, Route, Solution
from src.algorithms.constructive import clarke_wright
from src.algorithms.local_search import two_opt, or_opt
from src.visualization import plot_solution

# --- 1. CHARGEMENT DONNÉES ---
print("Étape 1: Chargement des données")

# Création dépôt
depot = Client(0, 0, 0, 0, 0, 1440, service=0)

# Création clients (exemple mini)
clients = [
    Client(1, 10, 5, 50, 540, 660),   # 9h-11h, 50kg
    Client(2, 15, 8, 80, 600, 720),   # 10h-12h, 80kg
    Client(3, 5, 15, 30, 480, 600),   # 8h-10h, 30kg
    Client(4, 20, 10, 100, 660, 840), # 11h-14h, 100kg
    Client(5, 12, 20, 45, 720, 900),  # 12h-15h, 45kg
]

print(f"✓ {len(clients)} clients chargés")

# Matrice des distances
n = len(clients) + 1
distances = np.zeros((n, n))
tous_points = [depot] + clients

for i in range(n):
    for j in range(n):
        if i != j:
            distances[i,j] = tous_points[i].distance_to(tous_points[j])

print(f"✓ Matrice distances calculée: {n}x{n}")

# --- 2. PARAMÈTRES ---
CAPACITE_CAMION = 200  # kg
COUT_KM = 2            # euros/km
COUT_VEHICULE = 50     # euros/véhicule

# --- 3. RÉSOLUTION ---
print("\nÉtape 2: Construction solution initiale (Clarke & Wright)")

solution_initiale = clarke_wright(depot, clients, CAPACITE_CAMION)

print(f"✓ Solution construite:")
print(f"  - Véhicules: {solution_initiale.nombre_vehicules()}")
print(f"  - Distance: {solution_initiale.distance_totale():.2f} km")
print(f"  - Coût: {solution_initiale.cout_total(COUT_KM, COUT_VEHICULE):.2f} €")

# Détail des tournées
for i, route in enumerate(solution_initiale.routes, 1):
    ids = [c.id for c in route.clients]
    print(f"  Route {i}: 0 → {' → '.join(map(str, ids))} → 0")
    print(f"           Distance: {route.distance_totale():.2f} km, "
          f"Charge: {route.charge_actuelle}/{route.capacite_max} kg")

# --- 4. AMÉLIORATION ---
print("\nÉtape 3: Amélioration par recherche locale")

solution_amelioree = solution_initiale.copie()

# Application 2-opt
print("  Application 2-opt...")
nb_ameliorations_2opt = 0
for route in solution_amelioree.routes:
    nb_ameliorations_2opt += two_opt(route)

print(f"  ✓ {nb_ameliorations_2opt} améliorations 2-opt")

# Application Or-opt
print("  Application Or-opt...")
nb_ameliorations_or = 0
for route in solution_amelioree.routes:
    nb_ameliorations_or += or_opt(route)

print(f"  ✓ {nb_ameliorations_or} améliorations Or-opt")

print(f"\n✓ Solution améliorée:")
print(f"  - Distance: {solution_amelioree.distance_totale():.2f} km "
      f"({-100*(solution_amelioree.distance_totale()-solution_initiale.distance_totale())/solution_initiale.distance_totale():+.1f}%)")
print(f"  - Coût: {solution_amelioree.cout_total(COUT_KM, COUT_VEHICULE):.2f} €")

# --- 5. MÉTRIQUES ENVIRONNEMENTALES ---
print("\nÉtape 4: Impact environnemental")

emissions = solution_amelioree.emissions_co2()
print(f"  - Émissions CO2: {emissions:.2f} kg")
print(f"  - Économie vs solution initiale: "
      f"{solution_initiale.emissions_co2() - emissions:.2f} kg CO2")

# --- 6. VALIDATION ---
print("\nÉtape 5: Validation")
if solution_amelioree.est_valide():
    print("  ✓ Solution valide (toutes contraintes respectées)")
else:
    print("  ✗ ATTENTION: Solution invalide!")

# --- 7. VISUALISATION ---
print("\nÉtape 6: Génération des visualisations")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Graphique 1: Solution initiale
plot_solution(solution_initiale, ax1, title="Solution Initiale (Clarke & Wright)")

# Graphique 2: Solution améliorée
plot_solution(solution_amelioree, ax2, title="Solution Améliorée (+ 2-opt + Or-opt)")

plt.tight_layout()
plt.savefig('../results/figures/comparaison_solutions.png', dpi=300)
print("  ✓ Graphiques sauvegardés")

# --- 8. EXPORT RÉSULTATS ---
print("\nÉtape 7: Export des résultats")

# Export CSV des tournées
resultats = []
for i, route in enumerate(solution_amelioree.routes, 1):
    for j, client in enumerate(route.clients, 1):
        resultats.append({
            'vehicule': i,
            'ordre': j,
            'client_id': client.id,
            'demande': client.demande,
            'fenetre_debut': client.debut,
            'fenetre_fin': client.fin
        })

df_resultats = pd.DataFrame(resultats)
df_resultats.to_csv('../results/solutions/solution_optimale.csv', index=False)
print("  ✓ Solution exportée en CSV")

# Résumé statistique
statistiques = {
    'nb_clients': len(clients),
    'nb_vehicules': solution_amelioree.nombre_vehicules(),
    'distance_km': solution_amelioree.distance_totale(),
    'cout_euros': solution_amelioree.cout_total(COUT_KM, COUT_VEHICULE),
    'emissions_kg_co2': emissions,
    'taux_remplissage_moyen': np.mean([r.charge_actuelle/r.capacite_max 
                                       for r in solution_amelioree.routes])
}

df_stats = pd.DataFrame([statistiques])
df_stats.to_csv('../results/solutions/statistiques.csv', index=False)
print("  ✓ Statistiques exportées")

print("\n" + "="*60)
print("RÉSOLUTION TERMINÉE AVEC SUCCÈS")
print("="*60)
```

### Fonctions utilitaires clés

#### Fonction de visualisation
```python
def plot_solution(solution, ax=None, title="Solution VRPTW"):
    """
    Trace graphiquement une solution
    
    Args:
        solution: Instance de Solution
        ax: Axes matplotlib (optionnel)
        title: Titre du graphique
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 8))
    
    # Couleurs pour chaque route
    couleurs = plt.cm.tab10(np.linspace(0, 1, len(solution.routes)))
    
    # Tracé des routes
    for i, route in enumerate(solution.routes):
        # Points de la route
        x = [route.depot.x]
        y = [route.depot.y]
        
        for client in route.clients:
            x.append(client.x)
            y.append(client.y)
        
        x.append(route.depot.x)
        y.append(route.depot.y)
        
        # Tracer la route
        ax.plot(x, y, 'o-', color=couleurs[i], 
                linewidth=2, markersize=8,
                label=f'Route {i+1} ({route.distance_totale():.1f}km)')
    
    # Dépôt en rouge
    ax.scatter(route.depot.x, route.depot.y, 
              c='red', s=300, marker='s', 
              edgecolors='black', linewidths=2,
              label='Dépôt', zorder=10)
    
    # Annotations clients
    for route in solution.routes:
        for client in route.clients:
            ax.annotate(f'C{client.id}', 
                       (client.x, client.y),
                       xytext=(5, 5), 
                       textcoords='offset points',
                       fontsize=9, fontweight='bold')
    
    ax.set_xlabel('X (km)', fontsize=12)
    ax.set_ylabel('Y (km)', fontsize=12)
    ax.set_title(f"{title}\nDistance: {solution.distance_totale():.2f}km, "
                f"Véhicules: {solution.nombre_vehicules()}", 
                fontsize=14, fontweight='bold')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    return ax
```

#### Fonction de génération de données test
```python
def generer_instance_aleatoire(n_clients=20, seed=42):
    """
    Génère une instance aléatoire pour tests
    
    Args:
        n_clients: Nombre de clients
        seed: Graine aléatoire (reproductibilité)
    
    Returns:
        depot, clients, capacite
    """
    np.random.seed(seed)
    
    # Dépôt au centre
    depot = Client(0, 50, 50, 0, 0, 1440, service=0)
    
    # Clients aléatoires
    clients = []
    for i in range(1, n_clients + 1):
        x = np.random.uniform(0, 100)
        y = np.random.uniform(0, 100)
        demande = np.random.randint(10, 100)
        
        # Fenêtres temporelles réalistes
        debut = np.random.randint(480, 720)  # 8h-12h
        fin = debut + np.random.randint(120, 240)  # +2h à +4h
        
        clients.append(Client(i, x, y, demande, debut, fin))
    
    # Capacité adaptée
    demande_totale = sum(c.demande for c in clients)
    capacite = int(demande_totale / 3)  # ~3 véhicules nécessaires
    
    return depot, clients, capacite
```

### Exemple d'utilisation complète

```python
# ===========================================
# TEST RAPIDE
# ===========================================

# Génération instance
depot, clients, capacite = generer_instance_aleatoire(n_clients=15)

print(f"Instance générée: {len(clients)} clients, capacité={capacite}kg")

# Résolution
solution = clarke_wright(depot, clients, capacite)
print(f"\nSolution initiale: {solution}")

# Amélioration
for route in solution.routes:
    two_opt(route)
    or_opt(route)

print(f"Solution améliorée: {solution}")
print(f"Gain: {solution_initiale.distance_totale() - solution.distance_totale():.2f}km")

# Visualisation
plot_solution(solution, title="Solution finale")
plt.show()
```

---

## Résumé des choix techniques

### Synthèse de l'approche

| Aspect | Choix | Justification |
|--------|-------|---------------|
| **Problème** | VRPTW (NP-Difficile) | Représentatif réel avec fenêtres temporelles |
| **Construction** | Clarke & Wright | Bon compromis qualité/rapidité |
| **Amélioration** | 2-opt + Or-opt | Classiques éprouvés, simples à implémenter |
| **Langage** | Python 3.10+ | Productivité, lisibilité, écosystème |
| **Librairies** | NumPy, Pandas, Matplotlib | Standard scientifique Python |
| **Structure** | Orientée objet | Modularité, réutilisabilité |

### Points forts de notre approche

✅ **Pédagogique** : Code clair et commenté, progression logique
✅ **Modulaire** : Composants réutilisables et testables
✅ **Visuelle** : Graphiques explicites pour présentation
✅ **Extensible** : Ajout facile de nouvelles contraintes/algorithmes
✅ **Validée** : Tests sur instances benchmark

### Perspectives d'amélioration

🔹 **Court terme** :
- Multi-dépôts
- Flotte hétérogène (différents types de camions)
- Trafic temps réel via API (Google Maps, Waze)

🔹 **Moyen terme** :
- Algorithme génétique pour grandes instances
- Optimisation multi-objectifs (coût + temps + émissions)
- Interface web interactive

🔹 **Long terme** :
- Apprentissage automatique (prédiction demandes)
- Réoptimisation dynamique en cours de journée
- Intégration IoT (positions véhicules temps réel)

---

## Conclusion méthodologique

Notre approche hybride **construction heuristique + recherche locale** offre le meilleur équilibre entre :
- ⏱️ **Temps de calcul** acceptable (< 1 minute pour 100 clients)
- 🎯 **Qualité** des solutions (écart < 10% optimal)
- 🔧 **Simplicité** d'implémentation et de maintenance
- 📊 **Démonstrabilité** pour présentation jury

L'architecture modulaire permet une évolution progressive du système tout en maintenant un code lisible et testable, essentiel dans un contexte pédagogique et professionnel.
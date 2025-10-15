# ============================================================
# 🚚 Modélisation du problème VRP — Projet EcoRoute / ADEME
# ============================================================

import networkx as nx
import random
import pandas as pd

# -----------------------------
# 1. Définition des paramètres
# -----------------------------

N_CLIENTS = 8
N_VEHICULES = 3
SEED = 42
random.seed(SEED)

# Fenêtres temporelles simulées (heures en minutes)
TIME_WINDOWS = [(480, 600), (540, 720), (600, 780), (660, 840),
                (720, 900), (780, 960), (840, 1020), (900, 1080)]

# -----------------------------
# 2. Génération du graphe
# -----------------------------

G = nx.complete_graph(N_CLIENTS + 1, create_using=nx.DiGraph())  # +1 pour le dépôt
positions = {}

# Ajout du dépôt (node 0)
G.nodes[0]['type'] = 'depot'
G.nodes[0]['location'] = (0, 0)
G.nodes[0]['time_window'] = (480, 1080)  # 8h00 - 18h00
positions[0] = (0, 0)

# -----------------------------
# 3. Ajout des clients
# -----------------------------
for i in range(1, N_CLIENTS + 1):
    G.nodes[i]['type'] = 'client'
    G.nodes[i]['demand_kg'] = random.randint(50, 200)
    G.nodes[i]['location'] = (random.uniform(1, 10), random.uniform(1, 10))
    G.nodes[i]['time_window'] = TIME_WINDOWS[i - 1]
    G.nodes[i]['priority'] = random.choice(['normale', 'haute'])
    positions[i] = G.nodes[i]['location']

# -----------------------------
# 4. Pondération des arêtes
# -----------------------------
for i in G.nodes:
    for j in G.nodes:
        if i != j:
            x1, y1 = G.nodes[i]['location']
            x2, y2 = G.nodes[j]['location']
            distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

            # Variation du temps de trajet selon l’heure (facteur simplifié)
            traffic_factor = random.uniform(1.0, 1.5)
            time = distance * traffic_factor * 6  # minutes (≈10 km/h)

            # Coût environnemental simplifié
            co2 = distance * random.uniform(0.12, 0.25)  # kg CO₂/km

            G[i][j]['distance_km'] = round(distance, 2)
            G[i][j]['time_min'] = round(time, 1)
            G[i][j]['co2_kg'] = round(co2, 3)

# -----------------------------
# 5. Flotte de véhicules
# -----------------------------
vehicules = pd.DataFrame([
    {'id': f'V{i+1}', 'cap_kg': random.randint(400, 700),
     'dispo': (480, 1080), 'type': random.choice(['électrique', 'diesel'])}
    for i in range(N_VEHICULES)
])

# -----------------------------
# 6. Affichage synthétique
# -----------------------------
print("=== DÉPÔT ===")
print(G.nodes[0])
print("\n=== CLIENTS ===")
for i in range(1, N_CLIENTS + 1):
    print(f"Client {i} :", G.nodes[i])

print("\n=== FLOTTE DE VÉHICULES ===")
print(vehicules)

print("\n=== Exemple de pondération (arête 0→1) ===")
print(G[0][1])

# -----------------------------
# 7. Visualisation du graphe
# -----------------------------
import matplotlib.pyplot as plt

edge_labels = {(i, j): f"{G[i][j]['distance_km']} km" for i, j in G.edges}
nx.draw(G, positions, with_labels=True, node_size=700, node_color="lightblue", font_weight='bold')
nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels, font_size=8)
plt.title("Modélisation du réseau de livraison (EcoRoute - ADEME)")
plt.show()

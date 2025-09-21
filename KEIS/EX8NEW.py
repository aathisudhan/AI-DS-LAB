import numpy as np
import matplotlib.pyplot as plt import networkx as nx

# Step 1: Importing the required libraries (done above) # Step 2: Define and visualise the graph
edges = [
(0, 1), (1, 5), (5, 6), (5, 4), (1, 2), (1, 3), (9, 10),
(2, 4), (0, 6), (6, 7), (8, 9), (7, 8), (1, 7), (3, 9)
]
goal = 10
MATRIX_SIZE = 11 # Number of nodes G = nx.Graph() G.add_edges_from(edges) plt.figure(figsize=(6, 6))
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G, seed=42), node_color='darkcyan') nx.draw_networkx_edges(G, pos=nx.spring_layout(G, seed=42), edgelist=edges) nx.draw_networkx_labels(G, pos=nx.spring_layout(G, seed=42))
plt.grid(True) plt.show()
print('\n'.join(str(e) for e in edges))


# Step 3: Define the reward system for the bot
M = np.ones((MATRIX_SIZE, MATRIX_SIZE)) * -1
for point in edges:
if point[1] == goal:
 
M[point] = 100 else:
M[point] = 0
if point[0] == goal:
M[point[::-1]] = 100
else:
M[point[::-1]] = 0 M[goal, goal] = 100

# Step 4: Utility functions for Q-learning Q = np.zeros_like(M)
gamma = 0.75


def available_actions(state): current_row = M[state]
return np.where(current_row >= 0)[0]


def sample_next_action(available_actions_range):
return int(np.random.choice(available_actions_range, 1))


def update(current_state, action, gamma):
max_index = np.where(Q[action] == np.max(Q[action]))[0] if max_index.shape[0] > 1:
max_index = int(np.random.choice(max_index, 1)) else:
max_index = int(max_index) max_value = Q[action, max_index]
 
Q[current_state, action] = M[current_state, action] + gamma * max_value if np.max(Q) > 0:
return np.sum(Q/np.max(Q)*100) else:
return 0


# Step 5: Training the bot using Q-Matrix scores = []
for i in range(1000):
state = np.random.randint(0, MATRIX_SIZE) actions = available_actions(state)
action = sample_next_action(actions) score = update(state, action, gamma) scores.append(score)

# Display the Q-matrix
Q_display = np.round(Q/np.max(Q)*100, 1) print(Q_display)

# Find the most efficient path from 0 to goal current_state = 0
steps = [current_state] while current_state != goal:
next_steps = np.where(Q[current_state] == np.max(Q[current_state]))[0] if next_steps.shape[0] > 1:
next_step = int(np.random.choice(next_steps, 1)) else:
 
next_step = int(next_steps) steps.append(next_step) current_state = next_step
print("Most efficient Path") print(steps)

# Show training graph plt.figure() plt.plot(scores)
plt.xlabel("No of Iterations") plt.ylabel("Reward Gained") plt.show()

# Step 6: Defining and visualizing the new graph with environmental clues police = [2, 4, 5]
drug_traces = [3, 8, 9] mapping = {
0: "0-Detective",
1: "1",
2: "2-Police",
3: "3-Drug traces",
4: "4-Police",
5: "5-Police",
6: "6",
7: "7",
8: "8-Drug traces",
9: "9-Drug traces",
 
10: "10-Drug racket location"
}
H = nx.relabel_nodes(G, mapping) pos_h = nx.spring_layout(H, seed=42)

# Critical change: relabel the edge list for the environmental graph! edges_h = [(mapping[e[0]], mapping[e[1]]) for e in edges] plt.figure(figsize=(7, 7))
nx.draw_networkx_nodes(H, pos_h) nx.draw_networkx_edges(H, pos_h, edgelist=edges_h) nx.draw_networkx_labels(H, pos_h)
plt.grid(True) plt.show()

# Step 7: Visualising the Environmental matrices env_police = np.zeros_like(M)
env_drugs = np.zeros_like(M)


def collect_environmental_data(action): found = []
if action in police: found.append('p')
if action in drug_traces: found.append('d')
return found
for i in range(1000):
state = np.random.randint(0, MATRIX_SIZE)
 
actions = available_actions(state) action = sample_next_action(actions)
_ = update(state, action, gamma)
env = collect_environmental_data(action) if 'p' in env:
env_police[state, action] += 1 if 'd' in env:
env_drugs[state, action] += 1 print("Police found") print(np.round(env_police, 2)) print("Drug Traces Found") print(np.round(env_drugs, 2))

# Step 8: Training and evaluating the model with environmental matrices scores_env = []
for i in range(1000):
state = np.random.randint(0, MATRIX_SIZE) actions = available_actions(state)
action = sample_next_action(actions) score = update(state, action, gamma) scores_env.append(score)
plt.figure() plt.plot(scores_env) plt.xlabel("No of Iterations") plt.ylabel("Reward Gained") plt.show()

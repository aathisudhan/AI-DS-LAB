import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from hmmlearn import hmm

# Define states and observations
states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
          'U', 'V', 'W', 'X', 'Y', 'Z']
n_states = len(states)

observ = ['up', 'down', 'left', 'right', 'up-right', 'down-right', 'up-left', 'down-left']
n_obs = len(observ)

# Random probabilities
s_prob = np.random.dirichlet(np.ones(n_states), size=1)  # Start probabilities
t_prob = np.random.dirichlet(np.ones(n_states), size=n_states)  # Transition matrix
e_prob = np.random.dirichlet(np.ones(n_obs), size=n_states)  # Emission matrix

# Create Categorical HMM model
model = hmm.CategoricalHMM(n_components=n_states, n_iter=100, random_state=42)

# Assign parameters
model.startprob_ = s_prob[0]
model.transmat_ = t_prob
model.emissionprob_ = e_prob

# Example observation sequence (encoded as integers)
obs_seq = np.array([[0], [1], [2], [1], [0], [1], [2], [3], [2], [1], [2]])

# Predict hidden states
hidden_states = model.predict(obs_seq)

print("Most likely hidden states (index numbers):", hidden_states)
print("Corresponding state labels:", [states[i] for i in hidden_states])

# Plot the hidden states
sns.set_style("whitegrid")
plt.figure(figsize=(8, 5))
plt.plot(range(len(obs_seq)), hidden_states, '-o', label="Hidden State")
plt.xlabel("Stroke")
plt.ylabel("Most Likely Hidden State")
plt.title("Predicted Hidden States")
plt.legend()
plt.grid(True)
plt.show()

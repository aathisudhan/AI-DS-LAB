import numpy as np
import matplotlib.pyplot as plt np.random.seed(7)

# ---------- create synthetic handwriting-feature observations (10 strokes) ----------
T = 10
obs = np.array([18, 3, 17, 1, 4, 10, 11, 13, 19, 5], dtype=float).reshape(-1, 1)
# (I used a fixed sequence so output plot looks consistent and similar to your image)


# ---------- try to use hmmlearn; if not available, fallback to manual HMM + Viterbi ---------- use_hmmlearn = True
try:
from hmmlearn import hmm except Exception:
use_hmmlearn = False if use_hmmlearn:
# train Gaussian HMM n_states = 5
model = hmm.GaussianHMM(n_components=n_states, covariance_type="diag", n_iter=200, verbose=False)
model.startprob_ = np.full(n_states, 1.0 / n_states) # uniform start # initialize transitions slightly biased to self
A_init = np.full((n_states, n_states), 0.1) np.fill_diagonal(A_init, 0.6) model.transmat_ = A_init
# init means spread across the observation range
 
mins, maxs = obs.min(), obs.max()
means_init = np.linspace(mins, maxs, n_states).reshape(n_states, 1) model.means_ = means_init
model.covars_ = np.full((n_states, 1), 4.0) # wide covars model.fit(obs) # train
hidden_states = model.predict(obs)
# map states to representative values for plotting (scale to 0-20 like manual) state_means = model.means_.flatten()
scaled_values = (state_means - state_means.min()) # 0..range if scaled_values.max() > 0:
scaled_values = scaled_values / scaled_values.max() * 20.0 plotted = scaled_values[hidden_states]

# also compute forward logprob using model.score logprob = model.score(obs)
else:
# ---------- Manual simple HMM implementation and Viterbi (fallback) ---------- n_states = 5
# init startprob and transmat
startprob = np.full(n_states, 1.0 / n_states) trans = np.full((n_states, n_states), 0.1) np.fill_diagonal(trans, 0.6)
# emission: use Gaussian with means spaced and same var obs_min, obs_max = obs.min(), obs.max()
means = np.linspace(obs_max, obs_min, n_states) # spread variances = np.full(n_states, 4.0)
 
# emission probability function (Gaussian) def emm_prob(o):
# returns length-n_states vector p(o | state)
p = (1.0 / np.sqrt(2 * np.pi * variances)) * np.exp(-0.5 * ((o - means) ** 2) / variances) return p

# Forward algorithm (log space) alpha = np.zeros((T, n_states))
alpha[0] = startprob * emm_prob(obs[0, 0]) for t in range(1, T):
p_o = emm_prob(obs[t, 0]) for j in range(n_states):
alpha[t, j] = p_o[j] * np.sum(alpha[t - 1] * trans[:, j]) logprob = np.log(np.sum(alpha[-1]) + 1e-12)

# Viterbi (log)
log_start = np.log(startprob + 1e-12) log_trans = np.log(trans + 1e-12)
log_emm0 = np.log(emm_prob(obs[0, 0]) + 1e-12) delta = np.zeros((T, n_states))
psi = np.zeros((T, n_states), dtype=int) delta[0] = log_start + log_emm0
for t in range(1, T):
log_emm = np.log(emm_prob(obs[t, 0]) + 1e-12) for j in range(n_states):
seq_vals = delta[t - 1] + log_trans[:, j] psi[t, j] = np.argmax(seq_vals)
 
delta[t, j] = np.max(seq_vals) + log_emm[j] hidden_states = np.zeros(T, dtype=int) hidden_states[-1] = np.argmax(delta[-1])
for t in range(T - 2, -1, -1):
hidden_states[t] = psi[t + 1, hidden_states[t + 1]]


# map state to 0-20 scaled values using means scaled_values = (means - means.min())
if scaled_values.max() > 0:
scaled_values = scaled_values / scaled_values.max() * 20.0 plotted = scaled_values[hidden_states]

# ---------- Plot exactly like manual: stroke index vs predicted hidden state value ---------- strokes = np.arange(1, T + 1)
plt.figure(figsize=(7.5, 6))
plt.plot(strokes, plotted, marker='o', linestyle='-', linewidth=2, markersize=7, label='Hidden State')
plt.title("predicted hidden state", fontsize=14) plt.xlabel("stroke", fontsize=12)
plt.ylabel("Most Likely Hidden State", fontsize=12) plt.ylim(0, 20.5)
plt.xlim(0.5, T + 0.5) plt.xticks(strokes)
plt.grid(axis='y', linestyle='--', linewidth=0.6) plt.legend()
plt.tight_layout() plt.show()
 


# ---------- prints for record work ---------- print("Observed strokes:", obs.flatten().tolist())
print("Predicted hidden state indices:", hidden_states.tolist()) print("Log-probability (forward):", float(logprob))

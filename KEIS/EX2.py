import numpy as np import pandas as pd import random
from collections import Counter random.seed(0) np.random.seed(0)
# ---- Ground-truth Bayesian Network ---- # Prior P(C)
P_C = {0: 0.6, 1: 0.4}


# Conditional probabilities P(A|C) P_A_given_C = {
0: {0: 0.7, 1: 0.3},
1: {0: 0.2, 1: 0.8},
}


# Conditional probabilities P(B|C) P_B_given_C = {
0: {0: 0.4, 1: 0.6},
1: {0: 0.9, 1: 0.1},
}
def sample_from_cpt(distribution):
"""Sample value based on probability distribution"""
r = random.random()
s = 0.0
for k, p in distribution.items():
 
s += p
if r <= s: return k
return k # fallback


def generate_instance():
"""Generate one training/test instance from the true BBN""" c = sample_from_cpt(P_C)
a = sample_from_cpt(P_A_given_C[c])
b = sample_from_cpt(P_B_given_C[c]) return {"A": a, "B": b, "C": c}

# ---- Generate Training and Testing CSV files ---- def generate_csv(n_train=1000, n_test=300):
train = [generate_instance() for _ in range(n_train)] test = [generate_instance() for _ in range(n_test)] df_train = pd.DataFrame(train)
df_test = pd.DataFrame(test) df_train.to_csv("train.csv", index=False) df_test.to_csv("test.csv", index=False) return df_train, df_test
df_train, df_test = generate_csv()


# ---- Learn CPTs from Training Data ---- def learn_cpts(df):
counts_C = Counter(df["C"]) total = len(df)
 
P_C_hat = {c: counts_C[c]/total for c in [0,1]} counts_A_given_C = {0: Counter(), 1: Counter()}
counts_B_given_C = {0: Counter(), 1: Counter()} for _, row in df.iterrows():
counts_A_given_C[row["C"]][row["A"]] += 1
counts_B_given_C[row["C"]][row["B"]] += 1 P_A_given_C_hat = {}
P_B_given_C_hat = {} for c in [0,1]:
totA = sum(counts_A_given_C[c].values()) or 1 totB = sum(counts_B_given_C[c].values()) or 1
P_A_given_C_hat[c] = {0: counts_A_given_C[c][0]/totA, 1: counts_A_given_C[c][1]/totA}
P_B_given_C_hat[c] = {0: counts_B_given_C[c][0]/totB, 1: counts_B_given_C[c][1]/totB} return P_C_hat, P_A_given_C_hat, P_B_given_C_hat
P_C_hat, P_A_given_C_hat, P_B_given_C_hat = learn_cpts(df_train)


# ---- Exact Inference ----
def exact_posterior(evidence, P_C, P_A_given_C, P_B_given_C): post = {}
for c in [0,1]: p = P_C[c]
p *= P_A_given_C[c][evidence["A"]] p *= P_B_given_C[c][evidence["B"]] post[c] = p
s = sum(post.values())
return {c: post[c]/s for c in post}
 


# ---- Likelihood Weighting (Approximate Inference) ----
def likelihood_weighting(evidence, P_C, P_A_given_C, P_B_given_C, N=2000): weights = {0: 0.0, 1: 0.0}
for _ in range(N):
c = sample_from_cpt(P_C)
weight = P_A_given_C[c][evidence["A"]] * P_B_given_C[c][evidence["B"]] weights[c] += weight
total = weights[0] + weights[1]
return {0: weights[0]/total, 1: weights[1]/total}


# ---- Classification Functions ---- def classify_exact(row):
evidence = {"A": int(row["A"]), "B": int(row["B"])}
post = exact_posterior(evidence, P_C_hat, P_A_given_C_hat, P_B_given_C_hat) return 1 if post[1] > post[0] else 0
def classify_lw(row, N=1000):
evidence = {"A": int(row["A"]), "B": int(row["B"])}
post = likelihood_weighting(evidence, P_C_hat, P_A_given_C_hat, P_B_given_C_hat, N) return 1 if post[1] > post[0] else 0
def compute_accuracy(df, classifier_fn): correct = 0
for _, row in df.iterrows():
if classifier_fn(row) == row["C"]: correct += 1
return correct / len(df)
 
# ---- Evaluate Classifier ----
acc_exact = compute_accuracy(df_test, classify_exact) acc_lw = compute_accuracy(df_test, classify_lw) print("Classification Accuracy:")
print(f"Exact Inference : {acc_exact*100:.2f}%") print(f"Likelihood Weighting : {acc_lw*100:.2f}%")

# ---- Save Test Results ----
df_test["pred_exact"] = df_test.apply(classify_exact, axis=1) df_test["pred_lw"] = df_test.apply(classify_lw, axis=1) df_test.to_csv("test_with_predictions.csv", index=False) print("\nFiles saved: train.csv, test.csv, test_with_predictions.csv")

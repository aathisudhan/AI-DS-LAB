import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal


#
# Generate synthetic dataset #
def generate_data(n=500):
np.random.seed(28) # Fix seed for reproducibility phi = 0.6
mu = [np.array([-1.07, -1.07]), np.array([0.96, 0.98])] sigma = [
np.array([[0.34, 0.28], [0.28, 0.71]]),
np.array([[0.74, 0.16], [0.16, 0.32]])
]
z = np.random.binomial(1, phi, n) # Latent variable for cluster choice
X = np.array([np.random.multivariate_normal(mu[i], sigma[i]) for i in z]) return X

#
# Expectation Maximization #
def em(X, max_iter=100, tol=1e-4): n, d = X.shape
# Initialize parameters randomly phi = 0.5
 
mu = [np.random.randn(d), np.random.randn(d)] sigma = [np.eye(d), np.eye(d)]
lls = []
for iteration in range(max_iter): #	E-step
p0 = multivariate_normal.pdf(X, mu[0], sigma[0]) * (1 - phi) p1 = multivariate_normal.pdf(X, mu[1], sigma[1]) * phi gamma = p1 / (p0 + p1) # Responsibility of component 1

# ----- M-step -----
phi = gamma.mean()
mu[0] = ((1 - gamma)[:, None] * X).sum(0) / (1 - gamma).sum() mu[1] = (gamma[:, None] * X).sum(0) / gamma.sum()
sigma[0] = ((1 - gamma)[:, None] * (X - mu[0])).T @ (X - mu[0]) / (1 - gamma).sum()
sigma[1] = (gamma[:, None] * (X - mu[1])).T @ (X - mu[1]) / gamma.sum()


# ----- Log Likelihood ----- ll = np.log(p0 + p1).sum() lls.append(ll)

# Convergence check
if iteration > 0 and abs(lls[-1] - lls[-2]) < tol: break
return phi, mu, sigma, iteration + 1, lls


#
# Run the program
 
#
X = generate_data()
phi, mu, sigma, steps, lls = em(X) print("Unsupervised EM Results:")
print(f" Mixing Coefficient (phi): {phi:.4f}") print(f" Mean of Cluster 0: {mu[0]}") print(f" Mean of Cluster 1: {mu[1]}")
print(" Covariance of Cluster 0:\n", sigma[0]) print(" Covariance of Cluster 1:\n", sigma[1]) print(f" Total Steps for Convergence: {steps}")

#
# Plot log-likelihood curve #
plt.plot(lls, marker='o')
plt.title(" unsupervised Log Likelihood over Iterations") plt.xlabel("Iteration")
plt.ylabel("Log Likelihood") plt.grid(True)
plt.show()

import numpy as np
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(0)
mu1, sigma1 = 0, 1
mu2, sigma2 = 5, 1
X = np.concatenate((np.random.normal(mu1, sigma1, 500),
                    np.random.normal(mu2, sigma2, 500)))

# Initialize parameters
mu_hat = np.random.random(2)
sigma_hat = np.random.random(2) + 1.0   # avoid 0 variance
pi_hat = np.random.random(2)
pi_hat = pi_hat / np.sum(pi_hat)

log_likelihoods = []
num_epochs = 50

# EM algorithm loop
for epoch in range(num_epochs):
    gamma = np.zeros((len(X), mu_hat.shape[0]))
    for k in range(mu_hat.shape[0]):
        gamma[:, k] = pi_hat[k] * norm.pdf(X, mu_hat[k], sigma_hat[k])
    gamma = gamma / np.sum(gamma, axis=1, keepdims=True)

    total = np.sum(gamma, axis=0)
    pi_hat = total / len(X)
    mu_hat = (gamma.T @ X) / total
    # Corrected sigma_hat calculation
    sigma_hat = np.sqrt(np.sum(gamma * (X[:, np.newaxis] - mu_hat)**2, axis=0) / total)


    # Compute log-likelihood
    ll = np.sum(np.log(np.sum([pi_hat[k] * norm.pdf(X, mu_hat[k], sigma_hat[k])
                               for k in range(mu_hat.shape[0])], axis=0)))
    log_likelihoods.append(ll)

# Plot log-likelihood
plt.plot(np.arange(1, num_epochs + 1), log_likelihoods)
plt.xlabel('Epoch')
plt.ylabel('log-likelihood')
plt.title('Unsupervised log-likelihood')
plt.show()

# Print final parameters
print(f'After {num_epochs} steps, mu1_hat: {mu_hat[0]}, sigma1_hat: {sigma_hat[0]}')
print(f'mu2_hat: {mu_hat[1]}, sigma2_hat: {sigma_hat[1]}')
print(f'pi1_hat: {pi_hat[0]}, pi2_hat: {pi_hat[1]}')

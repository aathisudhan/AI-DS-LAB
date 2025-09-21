import numpy as np
import matplotlib.pyplot as plt from scipy.stats import beta

# Step 1: Define Prior Distribution (Beta distribution) def define_prior(alpha, beta_val):
return alpha, beta_val


# Step 2: Collect Observations (coin toss data) def collect_data():
data = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1] # 1=Head, 0=Tail
return data


# Step 3: Compute Likelihood (count heads & tails) def compute_likelihood(data):
heads = sum(data)
tails = len(data) - heads return heads, tails

# Step 4: Update Prior → Posterior using Bayes’ rule
def update_posterior(alpha_prior, beta_prior, heads, tails): alpha_post = alpha_prior + heads
beta_post = beta_prior + tails return alpha_post, beta_post

# Step 5: Plot Prior and Posterior Distributions
 
def plot_distributions(alpha_prior, beta_prior, alpha_post, beta_post): x = np.linspace(0, 1, 200)
prior_dist = beta.pdf(x, alpha_prior, beta_prior) posterior_dist = beta.pdf(x, alpha_post, beta_post) plt.figure(figsize=(10, 6))
plt.plot(x, prior_dist, 'b-', lw=2, label=f"Prior Beta({alpha_prior},{beta_prior})") plt.plot(x, posterior_dist, 'r-', lw=2, label=f"Posterior Beta({alpha_post},{beta_post})") plt.title("Bayesian Parameter Estimation")
plt.xlabel("Parameter Value (Probability of Head)") plt.ylabel("Density")
plt.legend() plt.grid(True) plt.show()

# Step 6: Make Predictions using Posterior Mean def make_prediction(alpha_post, beta_post):
mean_estimate = alpha_post / (alpha_post + beta_post) return mean_estimate
# Main Function def main():
# Prior
alpha_prior, beta_prior = define_prior(2, 2) # Data
data = collect_data() # Likelihood
heads, tails = compute_likelihood(data)
 
# Posterior
alpha_post, beta_post = update_posterior(alpha_prior, beta_prior, heads, tails) # Plot Distributions
plot_distributions(alpha_prior, beta_prior, alpha_post, beta_post) # Prediction
prediction = make_prediction(alpha_post, beta_post) # Display Results
print("Prior Distribution: Beta(", alpha_prior, ",", beta_prior, ")") print("Observed Data:", data)
print("Observed Heads =", heads, ", Tails =", tails)
print("Posterior Distribution: Beta(", alpha_post, ",", beta_post, ")") print("Predicted Probability of Head =", round(prediction, 3))

if  name	== " main ": main()

import pandas as pd
import numpy as np
import math

# Load dataset
df = pd.read_csv("income_bayes_dataset.csv")

# Separate income values by Bayes class
Yes_in = df[df["Bayes"] == "Yes"]["Income"]
No_in = df[df["Bayes"] == "No"]["Income"]

# Calculate mean and standard deviation for each class
mu_yes = Yes_in.mean()
std_yes = Yes_in.std(ddof=0)
mu_no = No_in.mean()
std_no = No_in.std(ddof=0)

print(f'Class "Yes" => mean: {mu_yes:.2f}, std dev: {std_yes:.2f}')
print(f'Class "No"  => mean: {mu_no:.2f}, std dev: {std_no:.2f}')

# Gaussian probability density function
def gauss(x, mu, std):
    exp = math.exp(-(x - mu) ** 2 / (2 * std ** 2))
    return (1 / (math.sqrt(2 * math.pi) * std)) * exp

try:
    # User input
    x_new = float(input("Enter income amount: "))

    # Likelihood calculation
    likelihood_yes = gauss(x_new, mu_yes, std_yes)
    likelihood_no = gauss(x_new, mu_no, std_no)

    print(f"\nFor income: {x_new:.2f}")
    print(f"P(x | Buys=Yes) likelihood = {likelihood_yes:.5f}")
    print(f"P(x | Buys=No)  likelihood = {likelihood_no:.5f}")

    # Example prior probabilities (adjust if dataset has different priors)
    prior_yes = 0.67
    prior_no = 0.33

    print(f"\nPrior P(Buys=Yes) = {prior_yes}")
    print(f"Prior P(Buys=No)  = {prior_no}")

    # Posterior calculation (unnormalized)
    posterior_yes = likelihood_yes * prior_yes
    posterior_no = likelihood_no * prior_no

    # Prediction
    prediction = "Yes" if posterior_yes > posterior_no else "No"
    print(f"\nPrediction: {prediction}")

except ValueError:
    print("Invalid input. Please enter a numeric income amount.")

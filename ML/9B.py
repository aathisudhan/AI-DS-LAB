import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Sample dataset with 3 features
data = np.array([
    [2.5, 2.4, 3.1],
    [0.5, 0.7, 1.1],
    [2.2, 2.9, 2.8],
    [1.9, 2.2, 2.6],
    [3.1, 3.0, 3.2],
    [2.3, 2.7, 2.9],
    [2.0, 1.6, 2.4],
    [1.0, 1.1, 1.3],
    [1.5, 1.6, 1.9],
    [1.1, 0.9, 1.2]
])

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Apply PCA
pca = PCA(n_components=3)
transformed_data = pca.fit_transform(data_scaled)

# Variance ratio and eigenvectors
variance_ratio = pca.explained_variance_ratio_
eigenvectors = pca.components_

# Convert transformed data to a DataFrame
df_transformed = pd.DataFrame(transformed_data, columns=['PC1', 'PC2', 'PC3'])

# Output results
print("Explained Variance Ratio:\n", variance_ratio)
print("\nEigenvectors:\n", eigenvectors)
print("\nTransformed Dataset:\n", df_transformed)

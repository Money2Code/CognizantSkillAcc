import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, adjusted_rand_score
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.decomposition import PCA

# Load the Iris dataset
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
true_labels = iris.target  # True class labels for comparison

# Normalize the features
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Determine optimal clusters using Elbow Method
inertia = []
k_range = range(2, 10)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.show()

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(df_scaled)

# Apply Hierarchical Clustering
hierarchical = AgglomerativeClustering(n_clusters=3)
hierarchical_labels = hierarchical.fit_predict(df_scaled)

# Evaluate Clustering Performance
silhouette_kmeans = silhouette_score(df_scaled, kmeans_labels)
silhouette_hierarchical = silhouette_score(df_scaled, hierarchical_labels)
ari_kmeans = adjusted_rand_score(true_labels, kmeans_labels)
ari_hierarchical = adjusted_rand_score(true_labels, hierarchical_labels)

print(f"Silhouette Score (K-Means): {silhouette_kmeans:.2f}")
print(f"Silhouette Score (Hierarchical): {silhouette_hierarchical:.2f}")
print(f"Adjusted Rand Index (K-Means): {ari_kmeans:.2f}")
print(f"Adjusted Rand Index (Hierarchical): {ari_hierarchical:.2f}")

# Hierarchical Clustering Dendrogram
plt.figure(figsize=(10, 5))
linkage_matrix = linkage(df_scaled, method='ward')
dendrogram(linkage_matrix)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

# Visualizing Clusters using PCA
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.scatterplot(x=df_pca[:, 0], y=df_pca[:, 1], hue=kmeans_labels, palette='viridis', s=50)
plt.title('K-Means Clustering')
plt.subplot(1, 2, 2)
sns.scatterplot(x=df_pca[:, 0], y=df_pca[:, 1], hue=hierarchical_labels, palette='coolwarm', s=50)
plt.title('Hierarchical Clustering')
plt.show()

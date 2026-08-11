import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

d = load_digits()
X = StandardScaler().fit_transform(d.data)

k = KMeans(10, random_state=1, n_init=10).fit_predict(X)
g = GaussianMixture(10, random_state=1).fit_predict(X)

print("K-Means:", silhouette_score(X,k))
print("GMM:", silhouette_score(X,g))

P = PCA(2).fit_transform(X)

plt.scatter(P[:,0],P[:,1],c=g,s=5)
plt.title("GMM Clustering")
plt.show()

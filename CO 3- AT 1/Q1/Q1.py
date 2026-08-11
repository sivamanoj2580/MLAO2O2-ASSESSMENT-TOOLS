import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

X = np.array([
[19,15,39],[21,15,81],[20,16,6],[23,16,77],[31,17,40],
[22,17,76],[35,18,6],[23,18,94],[64,19,3],[30,19,72],
[67,20,14],[35,20,99],[58,21,15],[24,21,77],[37,23,13],
[22,23,79],[35,24,35],[20,24,73],[52,25,14],[35,26,79],
[35,28,35],[25,28,82],[46,29,5],[31,30,73],[54,31,14],
[29,31,82],[45,32,13],[35,33,92],[40,34,31],[23,34,87]
])

X = StandardScaler().fit_transform(X)

k = KMeans(n_clusters=5, random_state=1, n_init=10)
y = k.fit_predict(X)

print("Silhouette Score:", silhouette_score(X,y))

P = PCA(2).fit_transform(X)
plt.scatter(P[:,0],P[:,1],c=y)
plt.title("Customer Segmentation")
plt.show()

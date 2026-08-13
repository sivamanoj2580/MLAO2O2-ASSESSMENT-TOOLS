import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

df = pd.DataFrame({
'Income':[15,15,16,16,17,17,18,18,19,19],
'Spending':[39,81,6,77,40,76,6,94,3,72]})

X = StandardScaler().fit_transform(df)

wcss = [KMeans(k, n_init=10).fit(X).inertia_ for k in range(1,6)]
plt.plot(range(1,6),wcss,'o-')
plt.xlabel("K"); plt.ylabel("WCSS"); plt.show()

c = KMeans(3, n_init=10).fit_predict(X)
P = PCA(2).fit_transform(X)

plt.scatter(P[:,0],P[:,1],c=c)
plt.xlabel("PCA1"); plt.ylabel("PCA2")
plt.title("Customer Clusters")
plt.show()

df["Cluster"] = c
print(df)

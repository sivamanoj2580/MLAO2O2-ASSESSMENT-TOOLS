import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA,FactorAnalysis,FastICA

w = load_wine()
X = StandardScaler().fit_transform(w.data)

P = PCA(2).fit_transform(X)
F = FactorAnalysis(2).fit_transform(X)
I = FastICA(2,random_state=1).fit_transform(X)

plt.scatter(P[:,0],P[:,1],c=w.target)
plt.title("PCA")
plt.show()

plt.scatter(F[:,0],F[:,1],c=w.target)
plt.title("Factor Analysis")
plt.show()

plt.scatter(I[:,0],I[:,1],c=w.target)
plt.title("ICA")
plt.show()

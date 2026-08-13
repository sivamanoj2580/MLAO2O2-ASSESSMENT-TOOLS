import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, FactorAnalysis, FastICA
from sklearn.mixture import GaussianMixture

df = pd.DataFrame({
'A':[14.23,13.20,13.16,14.37,13.24,14.20,14.39,14.06,14.83,13.86],
'M':[1.71,1.78,2.36,1.95,2.59,1.76,1.87,2.15,1.64,1.35],
'Ash':[2.43,2.14,2.67,2.50,2.87,2.45,2.45,2.61,2.17,2.27],
'Alc':[15.6,11.2,18.6,16.8,21,15.2,14.6,17.6,14,16],
'Mg':[127,100,101,113,118,112,96,121,97,98],
'P':[2.8,2.65,2.8,3.85,2.8,3.27,2.5,2.6,2.8,2.98]})

X = StandardScaler().fit_transform(df)

pca = PCA(2).fit_transform(X)
fa = FactorAnalysis(2).fit_transform(X)
ica = FastICA(2, random_state=1).fit_transform(X)
gmm = GaussianMixture(3, random_state=1).fit_predict(pca)

print("PCA:\n",pca)
print("Factor Analysis:\n",fa)
print("ICA:\n",ica)
print("GMM Clusters:\n",gmm)

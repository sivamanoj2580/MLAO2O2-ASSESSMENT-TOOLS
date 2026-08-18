import numpy as np
from hmmlearn import hmm

model = hmm.CategoricalHMM(n_components=3)

model.startprob_ = np.array([0.5,0.3,0.2])

model.transmat_ = np.array([
    [0.6,0.3,0.1],
    [0.2,0.6,0.2],
    [0.1,0.3,0.6]
])

model.emissionprob_ = np.array([
    [0.7,0.2,0.1],
    [0.2,0.6,0.2],
    [0.1,0.3,0.6]
])

obs = np.array([[0],[1],[2],[1],[0]])

states = model.predict(obs)

names = ['Sunny','Cloudy','Rainy']

print("Observations:", [names[i] for i in obs.ravel()])
print("Hidden States:", [names[i] for i in states])

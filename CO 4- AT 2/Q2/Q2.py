import numpy as np
from hmmlearn import hmm

model = hmm.CategoricalHMM(n_components=3)

model.startprob_ = np.array([0.6,0.3,0.1])
model.transmat_ = np.array([
    [0.7,0.2,0.1],
    [0.2,0.6,0.2],
    [0.1,0.3,0.6]
])

model.emissionprob_ = np.array([
    [0.8,0.2],
    [0.4,0.6],
    [0.1,0.9]
])

obs = np.array([[0],[1],[1],[0]])

states = model.predict(obs)

print("Predicted Hidden States:", states)

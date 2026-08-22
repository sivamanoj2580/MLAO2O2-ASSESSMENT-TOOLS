import numpy as np
from hmmlearn import hmm

model = hmm.CategoricalHMM(n_components=2)

model.startprob_ = np.array([0.6,0.4])
model.transmat_ = np.array([[0.7,0.3],
                            [0.4,0.6]])
model.emissionprob_ = np.array([[0.8,0.2],
                                [0.3,0.7]])

sensor = np.array([[0],[1],[0]])

state = model.predict(sensor)

print("Driving States:", state)

print("U. Lakshmi Chenna Kesava Reddy: 192425206")

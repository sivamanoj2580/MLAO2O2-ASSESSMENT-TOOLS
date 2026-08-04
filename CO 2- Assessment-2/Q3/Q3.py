import pandas as pd
from sklearn.naive_bayes import GaussianNB

data = {
    'Fever': [1, 1, 0, 1, 0, 1],
    'Cough': [1, 0, 1, 1, 0, 0],
    'Headache': [1, 1, 0, 1, 0, 1],
    'Flu': [1, 1, 0, 1, 0, 0]
}

df = pd.DataFrame(data)

X = df[['Fever', 'Cough', 'Headache']]
y = df['Flu']

model = GaussianNB()
model.fit(X, y)

prediction = model.predict([[1, 1, 1]])

if prediction[0] == 1:
    print("Patient has Flu")
else:
    print("Patient does not have Flu")

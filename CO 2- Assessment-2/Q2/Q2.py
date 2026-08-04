import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    'Word_Frequency': [5, 20, 15, 2, 30, 8],
    'Spam': [0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[['Word_Frequency']]
y = df['Spam']

model = LogisticRegression()
model.fit(X, y)

prediction = model.predict([[18]])

if prediction[0] == 1:
    print("Spam Email")
else:
    print("Non-Spam Email")

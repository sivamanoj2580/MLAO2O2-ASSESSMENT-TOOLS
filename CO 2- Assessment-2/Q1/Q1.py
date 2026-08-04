import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Area': [800, 1000, 1200, 1500, 1800],
    'Rooms': [2, 2, 3, 3, 4],
    'Location': [1, 1, 2, 2, 3],   # 1=Normal, 2=Good, 3=Premium
    'Rent': [15000, 18000, 22000, 27000, 35000]
}

df = pd.DataFrame(data)

X = df[['Area', 'Rooms', 'Location']]
y = df['Rent']

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[1400, 3, 2]])

print("Predicted Rent =", prediction[0])

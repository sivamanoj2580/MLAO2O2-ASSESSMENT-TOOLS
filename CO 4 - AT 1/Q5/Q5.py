import pandas as pd
from pgmpy.estimators import HillClimbSearch

data = pd.DataFrame({
    'Age':['Young','Young','Old','Old','Young','Old'],
    'Income':['Low','High','Low','High','High','Low'],
    'Vehicle':['Car','Bike','Car','Car','Bike','Bike'],
    'Claim':['No','Yes','No','Yes','Yes','No']
})

model = HillClimbSearch(data).estimate()

print("Dataset:")
print(data)

print("\nLearned Network Structure:")
print(list(model.edges()))

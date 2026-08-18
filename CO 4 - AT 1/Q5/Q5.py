import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination

data = pd.DataFrame({
    'Age':['Young','Young','Old','Old','Young','Old','Young','Old'],
    'Income':['Low','High','Low','High','High','Low','Low','High'],
    'Vehicle':['Car','Bike','Car','Car','Bike','Bike','Car','Bike'],
    'Claim':['No','Yes','No','Yes','Yes','No','No','Yes']
})

model = DiscreteBayesianNetwork([
    ('Age','Income'),
    ('Income','Vehicle'),
    ('Income','Claim'),
    ('Vehicle','Claim')
])
model.fit(data)

print("Learned Network Structure:")
print(list(model.edges()))

infer = VariableElimination(model)

result = infer.query(
    ['Claim'],
    evidence={
        'Age':'Young',
        'Income':'High',
        'Vehicle':'Bike'
    }
)

print("\nPrediction:")
print(result)

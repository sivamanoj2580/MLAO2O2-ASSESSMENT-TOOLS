from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Obesity','Diabetes'), ('Sugar','Diabetes')
])

a = TabularCPD('Obesity', 2, [[0.6],[0.4]])
b = TabularCPD('Sugar', 2, [[0.5],[0.5]])

c = TabularCPD('Diabetes', 2,
               [[0.95,0.7,0.6,0.2],
                [0.05,0.3,0.4,0.8]],
               evidence=['Obesity','Sugar'],
               evidence_card=[2,2])

model.add_cpds(a,b,c)

result = VariableElimination(model).query(
    ['Diabetes'],
    evidence={'Obesity':1, 'Sugar':1}
)

print("Probability of Diabetes:")
print(result)

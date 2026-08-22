from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([('Fever','Disease')])

cpd1 = TabularCPD('Fever',2,[[0.7],[0.3]])
cpd2 = TabularCPD('Disease',2,
                  [[0.9,0.2],
                   [0.1,0.8]],
                  evidence=['Fever'],
                  evidence_card=[2])

model.add_cpds(cpd1,cpd2)

infer = VariableElimination(model)
result = infer.query(variables=['Disease'], evidence={'Fever':1})

print(result)

print("U. Lakshmi Chenna Kesava Reddy: 192425206")

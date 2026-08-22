from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([('Transaction','Risk')])

cpd1 = TabularCPD('Transaction',2,[[0.8],[0.2]])
cpd2 = TabularCPD('Risk',2,
                  [[0.9,0.3],
                   [0.1,0.7]],
                  evidence=['Transaction'],
                  evidence_card=[2])

model.add_cpds(cpd1,cpd2)

infer = VariableElimination(model)

result = infer.query(variables=['Risk'], evidence={'Transaction':1})

print(result)

print("U. Lakshmi Chenna Kesava Reddy : 192425206")

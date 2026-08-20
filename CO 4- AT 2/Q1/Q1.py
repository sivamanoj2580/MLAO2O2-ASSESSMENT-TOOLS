from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Amount', 'Fraud'),
    ('History', 'Fraud')
])

cpd_amount = TabularCPD('Amount', 2, [[0.8], [0.2]])
cpd_history = TabularCPD('History', 2, [[0.9], [0.1]])

cpd_fraud = TabularCPD(
    'Fraud', 2,
    [[0.99,0.8,0.7,0.2],
     [0.01,0.2,0.3,0.8]],
    evidence=['Amount','History'],
    evidence_card=[2,2]
)

model.add_cpds(cpd_amount, cpd_history, cpd_fraud)

infer = VariableElimination(model)

result = infer.query(variables=['Fraud'], evidence={'Amount':1,'History':1})

print(result)

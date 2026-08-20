import sklearn_crfsuite

X_train = [[
    {'word':'Ravi'},
    {'word':'purchased'},
    {'word':'Phone'}
]]

y_train = [['NAME', 'O', 'PRODUCT']]

crf = sklearn_crfsuite.CRF()
crf.fit(X_train, y_train)

X_test = [[
    {'word':'Priya'},
    {'word':'ordered'},
    {'word':'Headphones'}
]]

result = crf.predict(X_test)

print("Sentence: Priya ordered Headphones")
print("Predicted Labels:", result)

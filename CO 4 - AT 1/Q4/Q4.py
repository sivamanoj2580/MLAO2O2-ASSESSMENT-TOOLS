import sklearn_crfsuite

train = [
    [('I','O'),('am','O'),('Rahul','NAME'),('order','O'),('ORD101','ORDER')],
    [('My','O'),('name','O'),('Priya','NAME'),('bought','O'),('Phone','PRODUCT')],
    [('Kiran','NAME'),('ordered','O'),('Laptop','PRODUCT')],
    [('Order','O'),('ORD202','ORDER'),('contains','O'),('Mouse','PRODUCT')]
]

def features(sentence):
    return [[
        {'word': w, 'upper': w.isupper(), 'digit': w.isdigit()}
        for w,l in sentence
    ]]

X = [features(s)[0] for s in train]
y = [[l for w,l in s] for s in train]

crf = sklearn_crfsuite.CRF()
crf.fit(X, y)

sentence = ['Ravi','ordered','ORD303','Laptop']
test = [[
    {'word': w, 'upper': w.isupper(), 'digit': w.isdigit()}
    for w in sentence
]]

print("Sentence:", ' '.join(sentence))
print("Predicted Labels:", crf.predict(test)[0])

import pandas
import numpy as np
data=np.array(pandas.read_csv("AppleStore.data", header=None))

X=data[:,0:6]
y=data[:,7]*2

from sklearn.utils import shuffle
X,y=shuffle(X,y,random_state=0)

trainX=X[:2400]
trainy=y[:2400]
testX=X[:2400:7198]
testy=y[:2400:7198]

# ~ print(X.shape)
# ~ print(y.shape)


from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=[10,10], random_state=0, max_iter=5000)
clf.fit(trainX, trainy)

prediction=clf.predict(testX)
print(prediction)

print(clf.score(trainX,trainy))
print(clf.score(testX,testy))

from sklearn.model_selection import cross_validate 
cv_results = cross_validate(clf, X, y, cv=4)
print(cv_results)



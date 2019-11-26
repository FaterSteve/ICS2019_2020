import pandas
data=pandas.read_csv("iris.data", header=None)
print(data)

import matplotlib.pyplot as plt                   #I most likely could, especialy if it was a setosa(the easily identified one). It could be tough with the other two though(versicolor and virginica are hard to tell apart because they have data overlap in most catagories).
import seaborn as sns # visualization
sns.pairplot( data=data,vars=(0,1,2,3), hue=4 )
plt.show()

import numpy as np
data=np.array(data)

X=data[:,0:4] #This gets all the rows and only the first 4 columns.
y=data[:,4]
print(X.shape) #(150,4)
print(y.shape) #(150,)

from sklearn.utils import shuffle #I verified by researching what sclear's random_state is on their website and trusting that you and sklearn are not working together to trick me into doing the wrong thing. Random state is something that makes it to where multiple actions can essentially use the same seed (or have the same randomization). In this instance it is useful because we can scrambe two seperate arrays the same way, meaning we still know the answers.
X,y=shuffle(X,y,random_state=0)

trainX=X[:100]
trainy=y[:100]
testX=X[:100:150]
testy=y[:100:150]

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=[4], random_state=0, max_iter=3000)
clf.fit(trainX, trainy)

print(clf.coefs_)

prediction=clf.predict(testX)
print(prediction)

print(clf.score(trainX,trainy))
print(clf.score(testX,testy))

from sklearn.model_selection import cross_validate #This is just making sure that the test set's score is not just a fluke.
cv_results = cross_validate(clf, X, y, cv=4)
print(cv_results)

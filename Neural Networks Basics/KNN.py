#import required modules and load data files
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

glass = pd.read_csv('glass.csv')

#create train-test split
X = glass[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]
Y = glass['Type']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)

#create classifier object
knn = KNeighborsClassifier(n_neighbors=1)

#Train the classifier using the training data
knn.fit(X_train ,Y_train)

#Estimate the accuracy of the classifier on future data, using the test data

print("The accuracy of this classifier is ", knn.score(X_test,Y_test))




# Random Forest Classifier
import sklearn
from sklearn.externals import joblib
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


# load the dataset
iris = load_iris()
X = iris.data
y = iris.target


# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.5)

# Build the model
clf = RandomForestClassifier(n_estimators=10)

# Train th classifier
clf.fit(X_train, y_train)

# Predictions
predicted = clf.predict(X_test)

# Check the accuracy
print(accuracy_score(predicted, y_test))

# Save the model
joblib.dump(clf, 'clf.pkl')

#!/usr/bin/python2


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score, precision_score, recall_score

print "POIs in test set:", sum(labels_test)

print "People in test set:", len(features_test)

print "Accuracy:", accuracy_score(labels_test, pred)

#Compare_predictions and true labels

count_tp = 0

for pred, actual in zip(pred, labels_test):
    if pred == 1 and actual == 1:
        count_tp += 1
        
print "True positives:", count_tp



print "Precision score:", precision_score(labels_test, pred, average='weighted')

print "Recall score:", recall_score(labels_test, pred)

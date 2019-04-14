import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import urllib.parse
from sklearn.metrics import confusion_matrix

##plt.style.use('ggplot') # make plots look better


#### import the data ####
df = pd.read_csv("f1combfinal2.csv")

#print (df.head())
print (df.describe())

#### Manual Feature selection ####
#sns.FacetGrid(df,
	#hue="mood").map(plt.scatter, "valence", "energy").add_legend()

#plt.show() # expect to see three defined clusters
# it's seen that the petal features seem to describe the species the best

#每一次跑出來都一樣
np.random.seed(1)

#### prepare data for sklearn ####
# drop irreleveant coloums
df_feature_selected = df.drop(['f_name', 'a_name', 'title', 'lyrics', 'spot_id', 'sr_json', 'tr_json', "mood"], axis=1)
#df_feature_selected = df.drop(['mxm_tid', 'a_name', 'title', 'lyrics', 'spot_id', 'sr_json', 'tr_json', "mood"], axis=1)

# create and encode labels
labels = np.asarray(df.mood)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(labels)

labels = le.transform(labels)

# create features using DictVectorizer, and pandas's to_dict method
df_features = df_feature_selected.to_dict( orient = 'records' )
#print ("features--> ", df_features)
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()
features = vec.fit_transform(df_features).toarray()


##### split up in test and training data ####
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split( features, labels, test_size=0.20, random_state=91)


#### Fit to random forests ####

# Random Forests Classifier
from sklearn.ensemble import RandomForestClassifier

# Support Vector Classifier
from sklearn import svm
from sklearn.svm import SVC

# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

# KNeighborsClassifier
from sklearn import neighbors

#AdaBoost Classifier
from sklearn.ensemble import AdaBoostClassifier

#### Figure out what kind of mistakes it makes ####
from sklearn.metrics import recall_score, precision_score

clf = RandomForestClassifier( min_samples_split=4, criterion="entropy" )
clf.fit(features_train, labels_train) #RandomForest
# find the accuracy of the model
acc_test = clf.score(features_test, labels_test)
acc_train = clf.score(features_train, labels_train)
print ("RandomForest Train Accuracy:", acc_train)
print ("RandomForest Test Accuracy:", acc_test)
print("---------------------------------------------")
# compute predictions on test features
pred = clf.predict(features_test)
RandomForest_precision = precision_score(labels_test, pred, average="weighted")
RandomForest_recall = recall_score(labels_test, pred, average="weighted")
print ("RandomForest Precision:", RandomForest_precision)
print ("RandomForest Recall:", RandomForest_recall)
print("RandomForest confusion matrix")
cm = confusion_matrix(labels_test, pred)
print(cm)
plt.matshow(cm)
plt.title('RandomForest Confusion matrix of the acoustic classifier')
plt.colorbar()
##plt.show()
print("\n")

clf2 = svm.SVC() #SVM
clf2.fit(features_train, labels_train)
acc_test2 = clf2.score(features_test, labels_test)
acc_train2 = clf2.score(features_train, labels_train)
print ("SVM Train Accuracy:", acc_train2)
print ("SVM Test Accuracy:", acc_test2)
print("---------------------------------------------")
pred = clf2.predict(features_test)
SVM_precision = precision_score(labels_test, pred, average="weighted")
SVM_recall = recall_score(labels_test, pred, average="weighted")
print ("SVM Precision:", SVM_precision)
print ("SVM Recall:", SVM_recall)
print("SVM confusion matrix")
cm = confusion_matrix(labels_test, pred)
print(cm)
plt.matshow(cm)
plt.title('SVM Confusion matrix of the acoustic classifier')
plt.colorbar()
##plt.show()
print("\n")

clf3 = DecisionTreeClassifier(min_samples_split=2,criterion="entropy",splitter='best')  #DecisionTree
clf3.fit(features_train, labels_train)
acc_test3 = clf3.score(features_test, labels_test)
acc_train3 = clf3.score(features_train, labels_train)
print ("DecisionTree Train Accuracy:", acc_train3)
print ("DecisionTree Test Accuracy:", acc_test3)
print("---------------------------------------------")
pred = clf3.predict(features_test)
DecisionTree_precision = precision_score(labels_test, pred, average="weighted")
DecisionTree_recall = recall_score(labels_test, pred, average="weighted")
print ("DecisionTree Precision:", DecisionTree_precision)
print ("DecisionTree Recall:", DecisionTree_recall)
print("DecisionTree confusion matrix")
cm = confusion_matrix(labels_test, pred)
print(cm)
plt.matshow(cm)
plt.title('DecisionTree Confusion matrix of the acoustic classifier')
plt.colorbar()
##plt.show()
print("\n")

clf4 = neighbors.KNeighborsClassifier(n_neighbors=5, algorithm='auto',p=1)  #kNN
clf4.fit(features_train, labels_train)
acc_test4 = clf4.score(features_test, labels_test)
acc_train4 = clf4.score(features_train, labels_train)
print ("kNN  Train Accuracy:", acc_train4)
print ("kNN  Test Accuracy:", acc_test4)
print("---------------------------------------------")
pred = clf4.predict(features_test)
kNN_precision = precision_score(labels_test, pred, average="weighted")
kNN_recall = recall_score(labels_test, pred, average="weighted")
print ("kNN Precision:", kNN_precision)
print ("kNN  Recall:", kNN_recall)
print("kNN  confusion matrix")
cm = confusion_matrix(labels_test, pred)
print(cm)
plt.matshow(cm)
plt.title('kNN  Confusion matrix of the acoustic classifier')
plt.colorbar()
##plt.show()
print("\n")

clf5 = AdaBoostClassifier(n_estimators=50, learning_rate=1)  #AdaBoost Classifier
clf5.fit(features_train, labels_train)
acc_test5 = clf5.score(features_test, labels_test)
acc_train5 = clf5.score(features_train, labels_train)
print ("AdaBoost  Train Accuracy:", acc_train5)
print ("AdaBoost  Test Accuracy:", acc_test5)
print("---------------------------------------------")
pred = clf5.predict(features_test)
AdaBoost_precision = precision_score(labels_test, pred, average="weighted")
AdaBoost_recall = recall_score(labels_test, pred, average="weighted")
print ("AdaBoost Precision:", AdaBoost_precision)
print ("AdaBoost  Recall:", AdaBoost_recall)
print("AdaBoost  confusion matrix")
cm = confusion_matrix(labels_test, pred)
print(cm)
plt.matshow(cm)
plt.title('AdaBoost  Confusion matrix of the acoustic classifier')
plt.colorbar()
##plt.show()
print("\n")

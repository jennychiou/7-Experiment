import pandas as pd
import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from PyLyrics import *
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import urllib.parse
import nltk
nltk.download('stopwords')

data = pd.read_csv("f1combfinal2.csv")

#print("0-> ", len(data[data.mood==0]))
#print("1-> ", len(data[data.mood==1]))
#print("2-> ", len(data[data.mood == 2]))
#print("3-> ", len(data[data.mood == 3]))

stemmer = SnowballStemmer('english')
words = stopwords.words("english")

data['cleaned'] = data['lyrics'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z]", " ", x).split() if i not in words]).lower())
X_train, X_test, y_train, y_test = train_test_split(data['cleaned'], data.mood, test_size=0.2 ,random_state=99)

#LogisticRegression方法
pipeline = Pipeline([('vect', TfidfVectorizer(ngram_range=(1, 2), stop_words="english", sublinear_tf=True)),
                     ('chi',  SelectKBest(chi2, k=10000)),
                     ('clf', LogisticRegression())])

model = pipeline.fit(X_train, y_train)

vectorizer = model.named_steps['vect']
chi = model.named_steps['chi']
clf = model.named_steps['clf']

feature_names = vectorizer.get_feature_names()
feature_names = [feature_names[i] for i in chi.get_support(indices=True)]
feature_names = np.asarray(feature_names)

target_names = ['0', '1', '2', '3']
#print("top 50 keywords per mood:")
for i, label in enumerate(target_names):
    top10 = np.argsort(clf.coef_[i])[-50:]
    #print("%s: %s" % (label, " ".join(feature_names[top10])))
##    print("%s----> "  % (label))
##    wcloud(str(" ".join(feature_names[top10])))
pred=model.predict(X_test)
print("LogisticRegression方法 Testing accuracy score: " + str(model.score(X_test, y_test)))
print("LogisticRegression方法 Traing accuracy score: " + str(model.score(X_train, y_train)))
print("LogisticRegression方法 confusion matrix")
cm = confusion_matrix(y_test, pred)
print(cm)
plt.matshow(cm)
plt.title('LogisticRegression方法 Confusion matrix of the classifier')
plt.colorbar()
plt.show()

print("---------------------------------------------------------------------------------------")

#LinearSVC方法
linear_svc = LinearSVC(C=1.0, penalty='l1', max_iter=3000, dual=False)
pipeline2 = Pipeline([('vect', TfidfVectorizer(ngram_range=(1, 2), stop_words="english", sublinear_tf=True)),
                     ('chi',  SelectKBest(chi2, k=10000)),
                     ('clf', linear_svc)])
model2 = pipeline2.fit(X_train, y_train)

vectorizer = model2.named_steps['vect']
chi2 = model2.named_steps['chi']
clf2 = model2.named_steps['clf']

feature_names = vectorizer.get_feature_names()
feature_names = [feature_names[i] for i in chi2.get_support(indices=True)]
feature_names = np.asarray(feature_names)

target_names = ['0', '1', '2', '3']
#print("top 50 keywords per mood:")
for i, label in enumerate(target_names):
    top10 = np.argsort(clf2.coef_[i])[-50:]
    #print("%s: %s" % (label, " ".join(feature_names[top10])))
##    print("%s----> "  % (label))
##    wcloud(str(" ".join(feature_names[top10])))
pred2=model2.predict(X_test)
print("LinearSVC方法 Testing accuracy score: " + str(model2.score(X_test, y_test)))
print("LinearSVC方法 Traing accuracy score: " + str(model.score(X_train, y_train)))
print("LinearSVC方法 confusion matrix")
cm = confusion_matrix(y_test, pred)
print(cm)
plt.matshow(cm)
plt.title('LinearSVC方法 Confusion matrix of the classifier')
plt.colorbar()
plt.show()

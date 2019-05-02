import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas(desc="progress-bar")

from sklearn import utils
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
##import gensim   
##from gensim.models import Doc2Vec
##from gensim.models.doc2vec import TaggedDocument
import re
import requests
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('lyricsCSV/lyrics0426(1-1071)_d.csv')
df = df[['song','vector','mood']]
##df2 = df[pd.notnull(df['vector'])]
##print(df2['vector'][0])
##print(df.shape[0])

vflist = []
for i in range (df.shape[0]):
    vf = df['vector'][i]
    vflist.append(vf)
##print(x)
##print(vflist[0])

def getList(strLs):
    trim = strLs.replace('[','').replace(']','')
    lst = trim.split(',')
    flist = list(map(float, lst))
    return flist

##print(df) #[1071 rows x 2 columns]
##print(df2) #[1067 rows x 2 columns]

vflist2 = []
k = 0
for element in vflist:
##    print(str(type(element))+str(k))
    k+=1
    result = getList(element)
    if type(result) != list:
        print(type(result))
    vflist2.append(result)
##print("vflist2[0] : ",vflist2[0])
##print(len(vflist2))

x = vflist2
##print("x長度：",len(x))
y=df[['mood']]
##print("mood欄位：",y.shape)

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2 ,random_state=0)

#LogisticRegression方法
lr=LogisticRegression()
model = lr.fit(X_train,y_train)

print("斜率：",lr.coef_)
print("截距：",lr.intercept_ )

pred=model.predict(X_test)
print("LogisticRegression Testing accuracy score: " + str(model.score(X_test, y_test)))
print("confusion matrix")
cm = confusion_matrix(y_test, pred)
print(cm)
##plt.matshow(cm)
##plt.title('Confusion matrix of the classifier')
##plt.colorbar()
##plt.show()

#LinearSVC方法
linear_svc = LinearSVC(C=1.0, penalty='l1', max_iter=3000, dual=False)
model2 = linear_svc.fit(X_train,y_train)
pred = model2.predict(X_test)
print("LinearSVC Testing accuracy score: " + str(model2.score(X_test, y_test)))

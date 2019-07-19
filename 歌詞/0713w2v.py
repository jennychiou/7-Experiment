#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import gensim
from gensim.models.word2vec import Word2Vec
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


# In[2]:


model = gensim.models.Word2Vec.load('temp/w2vm0712')


# In[99]:


model['nan']


# In[155]:


import csv
import pandas as pd
df = pd.read_csv('lyrics_data/tf_20000 (1)_0717.csv',encoding='ISO-8859-15')
w = df.iat[11393,49]
print(w)
wv = model[w]
print(wv)


# In[156]:


with open('lyrics_data/tf_20000 (1)_0717_v23.csv', "w", newline='',encoding='ISO-8859-15') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49'])
    for i in range(11000,11394):
        w0 = df.iat[i,0]
        w1 = df.iat[i,1]
        w2 = df.iat[i,2]
        w3 = df.iat[i,3]
        w4 = df.iat[i,4]
        w5 = df.iat[i,5]
        w6 = df.iat[i,6]
        w7 = df.iat[i,7]
        w8 = df.iat[i,8]
        w9 = df.iat[i,9]
        w10 = df.iat[i,10]
        w11 = df.iat[i,11]
        w12 = df.iat[i,12]
        w13 = df.iat[i,13]
        w14 = df.iat[i,14]
        w15 = df.iat[i,15]
        w16 = df.iat[i,16]
        w17 = df.iat[i,17]
        w18 = df.iat[i,18]
        w19 = df.iat[i,19]
        w20 = df.iat[i,20]
        w21 = df.iat[i,21]
        w22 = df.iat[i,22]
        w23 = df.iat[i,23]
        w24 = df.iat[i,24]
        w25 = df.iat[i,25]
        w26 = df.iat[i,26]
        w27 = df.iat[i,27]
        w28 = df.iat[i,28]
        w29 = df.iat[i,29]
        w30 = df.iat[i,30]
        w31 = df.iat[i,31]
        w32 = df.iat[i,32]
        w33 = df.iat[i,33]
        w34 = df.iat[i,34]
        w35 = df.iat[i,35]
        w36 = df.iat[i,36]
        w37 = df.iat[i,37]
        w38 = df.iat[i,38]
        w39 = df.iat[i,39]
        w40 = df.iat[i,40]
        w41 = df.iat[i,41]
        w42 = df.iat[i,42]
        w43 = df.iat[i,43]
        w44 = df.iat[i,44]
        w45 = df.iat[i,45]
        w46 = df.iat[i,46]
        w47 = df.iat[i,47]
        w48 = df.iat[i,48]
        w49 = df.iat[i,49]
        wv0 = model[w0]
        wv1 = model[w1]
        wv2 = model[w2]
        wv3 = model[w3]
        wv4 = model[w4]
        wv5 = model[w5]
        wv6 = model[w6]
        wv7 = model[w7]
        wv8 = model[w8]
        wv9 = model[w9]
        wv10 = model[w10]
        wv11 = model[w11]
        wv12 = model[w12]
        wv13 = model[w13]
        wv14 = model[w14]
        wv15 = model[w15]
        wv16 = model[w16]
        wv17 = model[w17]
        wv18 = model[w18]
        wv19 = model[w19]
        wv20 = model[w20]
        wv21 = model[w21]
        wv22 = model[w22]
        wv23 = model[w23]
        wv24 = model[w24]
        wv25 = model[w25]
        wv26 = model[w26]
        wv27 = model[w27]
        wv28 = model[w28]
        wv29 = model[w29]
        wv30 = model[w30]
        wv31 = model[w31]
        wv32 = model[w32]
        wv33 = model[w33]
        wv34 = model[w34]
        wv35 = model[w35]
        wv36 = model[w36]
        wv37 = model[w37]
        wv38 = model[w38]
        wv39 = model[w39]
        wv40 = model[w40]
        wv41 = model[w41]
        wv42 = model[w42]
        wv43 = model[w43]
        wv44 = model[w44]
        wv45 = model[w45]
        wv46 = model[w46]
        wv47 = model[w47]
        wv48 = model[w48]
        wv49 = model[w49]
        
        Table = [[wv0,wv1,wv2,wv3,wv4,wv5,wv6,wv7,wv8,wv9,wv10,wv11,wv12,wv13,wv14,wv15,wv16,wv17,wv18,wv19,wv20,wv21,wv22,wv23,wv24,wv25,wv26,wv27,wv28,wv29,wv30,wv31,wv32,wv33,wv34,wv35,wv36,wv37,wv38,wv39,wv40,wv41,wv42,wv43,wv44,wv45,wv46,wv47,wv48,wv49]]
        writer.writerows(Table)


# In[ ]:





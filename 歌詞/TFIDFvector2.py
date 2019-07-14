import re
import nltk
import string
import gensim
import logging
import pandas as pd
import numpy as np
from nltk.stem.porter import *
from nltk.corpus import stopwords
from collections import Counter
from gensim.models.word2vec import Word2Vec
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
'''
df = pd.read_csv("tracks_lyrics_test2.csv")
print('原始資料：',df.shape)
df1 = df.dropna()
print('刪除空值：',df1.shape)
##print(df1['lyrics'][0])
print('行數：',df1.shape[0])
print('列數：',df1.shape[1])
print("Schema:\n",df1.dtypes)

#分詞
def get_tokens(text):
    lowers = text.lower()
    #remove the punctuation using the character deletion step of translate
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lowers.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

#過濾缺乏實際意義的 the, a, and 等詞
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

for i in range(df1.shape[1]):
    tokens1 = get_tokens(df1['lyrics'][i])
    filtered1 = [w for w in tokens1 if not w in stopwords.words('english')]
    stemmer = PorterStemmer()
    stemmed1 = stem_tokens(filtered1, stemmer)
    if i == 0:
        print(stemmed1)
'''

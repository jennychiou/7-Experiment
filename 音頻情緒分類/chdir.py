##import os, sys
##
##path = "music-mood-classifier-master"
##
### 查看當前工作目錄
##retval = os.getcwd()
##print ("當前工作目錄為 %s" % retval)
##
### 修改當前工作目錄
##os.chdir( path )
##
### 查看修改後的工作目錄
##retval = os.getcwd()
##
##print( "目錄修改成功 %s" % retval)

# Import libraries

from gensim.models import doc2vec
from collections import namedtuple

# Load data

doc1 = ["This is a sentence", "This is another sentence"]

# Transform data (you can add more data preprocessing steps) 

docs = []
analyzedDocument = namedtuple('AnalyzedDocument', 'words tags')
for i, text in enumerate(doc1):
    words = text.lower().split()
    tags = [i]
    docs.append(analyzedDocument(words, tags))

# Train model (set min_count = 1, if you want the model to work with the provided example data set)

model = doc2vec.Doc2Vec(docs, size = 100, window = 300, min_count = 1, workers = 4)

# Get the vectors

model.docvecs[0]
model.docvecs[1]

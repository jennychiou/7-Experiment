#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import ast
from ast import literal_eval
import json
import csv


# In[13]:


df1 = pd.read_csv('audiolyrics_vecter_final_0720.csv')
df2 = df1.drop("Unnamed: 0", axis = 1)
df2.head(10)


# In[14]:


len(df2)


# In[15]:


df2['vector'] = ''
df2.head()


# In[20]:


L = []

for i in range(0,len(df2)):
    a_vec = df2['audio_vector'][i]
    a_vec_L = ast.literal_eval(a_vec)
    
           
    l_vec = df2['lyrics_vector'][i]
    l_vec_L = ast.literal_eval(l_vec)
    
    df2['vector'][i] = a_vec_L + l_vec_L
    
    L.append(df2['vector'][i])
    
    if i == 0:
        print('audio_vector DIM = ',len(a_vec_L))
        print('lyrics_vector DIM = ',len(l_vec_L))
        print('hybrid_vector DIM = ',len(df2['vector'][0]))
        
print(type(a_vec_L))
print(type(l_vec_L))
print(type(df2['vector'][0]))


# In[21]:


len(L)


# In[22]:


df2.head()


# In[24]:


df2.to_csv('combine_vector.csv',columns=['track_id','audio_vector','lyrics_vector','vector'])


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import ast
from sklearn.cluster import DBSCAN
from ast import literal_eval
import json
import csv


# In[79]:


df1 = pd.read_csv('audiolyrics_vecter_final_0720.csv')
df2 = df1.drop("Unnamed: 0", axis = 1)
df2.head(10)


# In[80]:


len(df2)


# In[81]:


df2['vector'] = ''
df2.head()


# In[82]:


L = []

for i in range(0,len(df2)):
    a_vec = df2['audio_vector'][i]
    a_vec_L = ast.literal_eval(a_vec)

    l_vec = df2['lyrics_vector'][i]
    l_vec_L = ast.literal_eval(l_vec)
    
    df2['vector'][i] = a_vec_L + l_vec_L
    
    L.append(df2['vector'][i])

print(type(a_vec_L))
print(type(l_vec_L))
print(type(df2['vector'][0]))


# In[83]:


len(L)


# In[84]:


df2.head()


# In[85]:


print(type(df2['vector'][0]))
print(len(df2['vector'][0]))


# In[86]:


clustering = DBSCAN(eps=3, min_samples=2).fit(L)
clustering.labels_


# In[87]:


clustering


# In[112]:


labels = clustering.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print('Estimated number of clusters: %d' % n_clusters_)
n_noise_ = list(labels).count(-1)
print('Estimated number of noise points: %d' % n_noise_)


# In[91]:


#抓取最近20首歌曲
record_df = pd.read_csv('Q Learning data_0721.csv')
record_df = record_df.drop("Unnamed: 0", axis = 1)
record_df


# In[94]:


#挑選20首中聽超輟28秒的歌曲
record_L = []
for num in range(len(record_df)):
    t = record_df['times'][num]
    if t >= 28:
        track = record_df['track_id'][num]
        record_L.append(track)
print(record_L)


# In[107]:


m = '00J6muo7cpXzgQxLNIDC8O'
row = df2.loc[df2['track_id'] == m]
print(type(row))
row


# In[111]:


row.iat[0,3]
#type(row.iat[0,3])


# In[138]:


#新增欄位放label的結果
#labels = -1代表離群點
df2['cluster'] = labels
df2.head()


# In[152]:


#查詢每一首對應到的cluster
count = 0
for k in range(0,len(df2)):
    if df2['cluster'][k] == 8:
        print(k)
        count += 1
print('個數：',count)


# In[142]:


df2.loc[582:582]


# In[153]:


#用ID反查vector
cluster_L = []
for j in range(0,len(record_L)):
    m =  record_L[j]
    row = df2.loc[df2['track_id'] == m]
    cluster = row.iat[0,4]
    cluster_L.append(cluster)
print(cluster_L)


# In[154]:


#直接找出最大次数對應的元素是哪個
max_count = max(cluster_L, key = cluster_L.count)
print('label最多者：',max_count)
if str(max_count) == '0':
    R = 2
    print(R)


# In[155]:


N_STATES = 20
CLUSTERS = ['0','1','2','3','4','5','6','7','8']
EPSILON = 0.9   # 貪婪度 greedy
ALPHA = 0.1     # 學習率
GAMMA = 0.9    # 獎勵遞減值
MAX_EPISODES = 13   # 最大回合數


# In[156]:


def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),     # q_table初始全0
        columns=actions,    # columns對應的是行為名稱
    )
    return table


# In[157]:


build_q_table(N_STATES, CLUSTERS)


# In[158]:


# 在某個state地點，選擇行為
def choose_action(state, q_table):
    state_actions = q_table.iloc[state, :]  # 選出這個state的所有action值
    #print('state_actions:','\n',state_actions)
    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0):  # 非貪婪 or 或者這個 state 還沒有探索過
        action_name = np.random.choice(CLUSTERS)
    else:
        action_name = state_actions.argmax()    # 貪婪模式
    return action_name


# In[164]:


def get_env_feedback(max_count, S, A):
    
    if str(max_count) == A:
        R = 1
    else:
        R = 0
        
    if A == '0':  
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    
    elif A == '1':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
            
    elif A == '2':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    
    elif A == '3':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    elif A == '4':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    elif A == '5':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    elif A == '6':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    elif A == '7':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    elif A == '8':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    
    return S_, R


# In[168]:


def rl():
    q_table = build_q_table(N_STATES, CLUSTERS)  # 初始 q table
    for episode in range(MAX_EPISODES):     # 回合

        S = 0   # 回合初始位置
        is_terminated = False   # 是否回合結束
        
        while not is_terminated:
            
            cluster_L = []
            for j in range(0,len(record_L)):
                m =  record_L[j]
                row = df2.loc[df2['track_id'] == m]
                cluster = row.iat[0,4]
                cluster_L.append(cluster)
            #print('聽>28秒之歌曲所屬cluser:',cluster_L)

            #直接找出最大次数對應的元素是哪個
            max_count = max(cluster_L, key = cluster_L.count)
            
            A = choose_action(S, q_table)   # 選行為
            print('A:',A)
            S_, R = get_env_feedback(max_count, S, A)  # 實施行為並得到反饋
            print("S_: ",S_,'|',"R: ",R)
            print()
            
            q_predict = q_table.loc[S, A]    # 估算的(狀態-行為)值
            
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max()   #  實際的(狀態-行為)值 (回合沒結束)
            else:
                q_target = R     #  實際的(狀態-行為)值 (回合结束)
                is_terminated = True    # terminate this episode

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  #  q_table 更新
            S = S_  # 探索者移动到下一个 state

    return q_table


# In[171]:


if __name__ == "__main__":
    q_table = rl()
    print()
    print('===== DONE ======')


# In[172]:


print('\r\nQ-table:')
q_table


# In[ ]:






# coding: utf-8

# In[88]:


import pandas as pd
import numpy as np


# In[89]:


music_df = pd.read_csv('Q Learning data_0715.csv')


# In[90]:


music_df


# In[91]:


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4)
kmeans.fit(music_df)
label_pred = kmeans.labels_
print(label_pred)


# In[92]:


N_STATES = 20
CLUSTERS = ['A','B','C', 'D']
EPSILON = 0.9   # 貪婪度 greedy
ALPHA = 0.1     # 學習率
GAMMA = 0.9    # 獎勵遞減值
MAX_EPISODES = 13   # 最大回合數


# In[93]:


def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),     # q_table初始全0
        columns=actions,    # columns對應的是行為名稱
    )
    return table


# In[94]:


build_q_table(N_STATES, CLUSTERS)


# In[105]:


# 在某個state地點，選擇行為
def choose_action(state, q_table):
    state_actions = q_table.iloc[state, :]  # 選出這個state的所有action值
    #print('state_actions:','\n',state_actions)
    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0):  # 非貪婪 or 或者這個 state 還沒有探索過
        action_name = np.random.choice(CLUSTERS)
    else:
        action_name = state_actions.argmax()    # 貪婪模式
    return action_name


# In[97]:


'''
def action(times):
    realA_L = []
    if 0 <= times <= 5:
        realA = 'very dislike'
        realA_L.append(realA)
    elif 6 <= times <= 15:
        realA = 'dislike'
        realA_L.append(realA)
    elif 16 <= times <= 27:
        realA = 'like'
        realA_L.append(realA)
    elif 28 <= times <= 30:
        realA = 'very like'
        realA_L.append(realA)
    return realA
'''


# In[143]:


count = 0
cluster_L = []
for i in range(len(music_df)):
    t = music_df['times'][i]
    if t >= 28:
        x = music_df['emotion'][i]
        print(x)
        if x == 0:
            cluster = 'A'
            cluster_L.append(cluster)
        elif x == 1:
            cluster = 'B'
            cluster_L.append(cluster)
        elif x == 2:
            cluster = 'C'
            cluster_L.append(cluster)
        elif x == 3:
            cluster = 'D'
            cluster_L.append(cluster)
        count += 1
print('個數：',count)
print(cluster_L)

from collections import Counter
result = Counter(cluster_L)
print(result)

#直接找出最大次数對應的元素是哪個
max_count = max(cluster_L, key = cluster_L.count)
print(max_count)
if str(max_count) == 'A':
    R = 2
    print(R)


# In[144]:


def get_env_feedback(max_count, S, A):
    
    if str(max_count) == A:
        R = 1
    else:
        R = 0
        
    if A == 'A':  
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    
    elif A == 'B':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
            
    elif A == 'C':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    
    elif A == 'D':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    
    return S_, R


# In[145]:


def reward(realA):
    if realA == 'very dislike':
        w = -2
        I = 1
   
    elif realA == 'dislike':
        w = -1
        I = 1
    
    elif realA == 'like':
        w = 1
        I = 1
       
    elif realA == 'very like':
        w = 2
        I = 1
    else:
        w = 0
        I = 0
    return w*I


# In[146]:


for i in range(len(music_df)):
    times =  music_df['times'][i]
    realA = action(times)
    r = reward(realA)
    print(r)


# In[154]:


def rl():
    q_table = build_q_table(N_STATES, CLUSTERS)  # 初始 q table
    for episode in range(MAX_EPISODES):     # 回合

        S = 0   # 回合初始位置
        is_terminated = False   # 是否回合結束
        
        while not is_terminated:
            count = 0
            cluster_L = []
            for i in range(len(music_df)):
                t = music_df['times'][i]
                if t >= 28:
                    x = music_df['emotion'][i]
                    if x == 0:
                        cluster = 'A'
                        cluster_L.append(cluster)
                    elif x == 1:
                        cluster = 'B'
                        cluster_L.append(cluster)
                    elif x == 2:
                        cluster = 'C'
                        cluster_L.append(cluster)
                    elif x == 3:
                        cluster = 'D'
                        cluster_L.append(cluster)
                    count += 1

            #直接找出最大次数對應的元素是哪個
            max_count = max(cluster_L, key = cluster_L.count)
            
            A = choose_action(S, q_table)   # 選行為
            print(A)
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


# In[155]:


if __name__ == "__main__":
    q_table = rl()
    print()
    print('===== DONE ======')


# In[156]:


print('\r\nQ-table:')
q_table


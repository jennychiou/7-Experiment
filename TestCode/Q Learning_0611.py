
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import time


# In[2]:


import csv
with open('Q Learning data.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(row)


# In[3]:


df = pd.read_csv('Q Learning data.csv')


# In[4]:


len(df)


# In[5]:


#music = ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12", "M13", "M14", "M15", "M16", "M17", "M18", "M19", "M20"]
music = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ,18, 19, 20]
times = [20, 5, 10, 17, 13, 15, 10, 30, 0, 30, 22, 25, 30, 7, 30, 1, 2, 5, 14, 0]

music_dict = {"music": music, "times": times}

music_df = pd.DataFrame(music_dict)


# In[6]:


music_df


# In[7]:


N_STATES = 20   # 1维世界的寬度
ACTIONS = ['dislike', 'click', 'listen', 'like']     # 探索者的可用動作
EPSILON = 0.9   # 貪婪度 greedy
ALPHA = 0.1     # 學習率
GAMMA = 0.9    # 獎勵遞減值
MAX_EPISODES = 13   # 最大回合數
FRESH_TIME = 0.3    # 移動尖閣時間


# In[8]:


def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),     # q_table初始全0
        columns=actions,    # columns對應的是行為名稱
    )
    return table


# In[9]:


build_q_table(N_STATES, ACTIONS)


# In[10]:


A_List = []
for i in range (len(music_df)):
    times = music_df["times"][i]
    if times == 0:
        A = 'dislike'
        A_List.append(A)
    elif 0 < times < 10:
        A = 'click'
        A_List.append(A)
    elif 10 <= times < 30:
        A = 'listen'
        A_List.append(A)
    elif times >= 30:
        A = 'like'
        A_List.append(A)
print(A_List)


# In[11]:


# 在某個state地點，選擇行為
def choose_action(state, q_table):
    state_actions = q_table.iloc[state, :]  # 選出這個state的所有action值
    #print('state_actions:','\n',state_actions)
    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0):  # 非貪婪 or 或者這個 state 還沒有探索過
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.argmax()    # 貪婪模式
    return action_name


# In[12]:


def action(times):
    if times == 0:
        A = 'dislike'
        A_List.append(A)
    elif 0 < times < 10:
        A = 'click'
        A_List.append(A)
    elif 10 <= times < 30:
        A = 'listen'
        A_List.append(A)
    elif times >= 30:
        A = 'like'
        A_List.append(A)
    return A


# In[13]:


def get_env_feedback(S,A):
    
    if A == 'dislike':
        if S == 0:   # terminate
            S_ = S # dislike扣兩分
            R = -2
        else:
            S_ = S - 1
            R = -2

    elif A == 'click':
        R = -1
        if S == 0:
            S_ = S 
        else:
            S_ = S - 1

    elif A == 'listen':
        R = 1
        if S == 0:
            S_ = S 
        else:
            S_ = S - 1

    elif A == 'like':
        R = 2
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    #print('播放程度：',A)
    return S_, R


# In[14]:


def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T' our environment
    
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print(interaction)
        print('=====================================================')
        #print('\r{}'.format(interaction), end='')
        #time.sleep(2)
        #print('\r                                ', end='')
    
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print(interaction)
        #print('\r{}'.format(interaction), end='')
        #time.sleep(FRESH_TIME)


# In[15]:


def rl():
    q_table = build_q_table(N_STATES, ACTIONS)  # 初始 q table
    
    for i in range(len(music_df)):     # 回合數
        #times = music_df["times"][i]
        step_counter = 0
        S = music_df["music"][0] - 1   # 回合初始位置
        #print(S)
        
        is_terminated = False   # 是否回合結束
        #update_env(S, episode, step_counter)    # 環境更新
        
        while not is_terminated:
            #for i in range(len(music_df)):
                #times = music_df["times"][i]
                #action(times)
            #print("選行為：", A)
            
            A = choose_action(S, q_table)   # 選行為
            print("選行為：", A)
            S_, R = get_env_feedback(S,A)  # 實施行為並得到環境的反饋
            print("S_: ",S_)
            print("R: ",R)
            q_predict = q_table.loc[S, A]    # 估算的(狀態-行為)值
            
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max()   # 實際的(狀態-行為)值 (回合沒結束)
            else:
                q_target = R     #  實際的(狀態-行為)值 (回合結束)
                is_terminated = True    # terminate this episode

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  #  q_table更新
            S = S_  # 移動到下一個 state
            #print(q_table)
            
            #update_env(S, episode, step_counter + 1)  # 環境更新

            step_counter += 1
    
    return q_table


# In[16]:


if __name__ == "__main__":
    q_table = rl()
    print('=====DONE=====')


# In[17]:


print('\r\nQ-table:')
q_table


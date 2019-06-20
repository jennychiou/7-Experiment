
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import time


# In[2]:


music_df = pd.read_csv('Q Learning data_0615.csv')


# In[3]:


music_df


# In[4]:


N_STATES = 20   # 1维世界的寬度
ACTIONS = ['very dislike', 'dislike', 'soso', 'like', 'very like']     # 探索者的可用動作
EPSILON = 0.9   # 貪婪度 greedy
ALPHA = 0.1     # 學習率
GAMMA = 0.9    # 獎勵遞減值
MAX_EPISODES = 13   # 最大回合數
FRESH_TIME = 0.3    # 移動間隔時間


# In[6]:


def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),     # q_table初始全0
        columns = actions,    # columns對應的是行為名稱
    )
    return table


# In[7]:


build_q_table(N_STATES, ACTIONS)


# In[8]:


realA_List = []
for i in range (len(music_df)):
    times = music_df["times"][i]
    if 0 <= times <= 3:
        realA = 'very dislike'
        realA_List.append(realA)
    elif 4 <= times <= 10:
        realA = 'dislike'
        realA_List.append(realA)
    elif 11 <= times <= 19:
        realA = 'soso'
        realA_List.append(realA)
    elif 20 <= times <= 27:
        realA = 'like'
        realA_List.append(realA)
    elif 28 <= times <= 30:
        realA = 'very like'
        realA_List.append(realA)
print(realA_List)


# In[9]:


# 在某個state地點，選擇行為
def choose_action(state, q_table):
    state_actions = q_table.iloc[state, :]  # 選出這個state的所有action值
    #print('state_actions:','\n',state_actions)
    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0):  # 非貪婪 or 或者這個 state 還沒有探索過
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.argmax()    # 貪婪模式
    return action_name


# In[10]:


def action(times):
    if 0 <= times <= 3:
        realA = 'very dislike'
        realA_List.append(realA)
    elif 4 <= times <= 10:
        realA = 'dislike'
        realA_List.append(realA)
    elif 11 <= times <= 19:
        realA = 'soso'
        realA_List.append(realA)
    elif 20 <= times <= 27:
        realA = 'like'
        realA_List.append(realA)
    elif 28 <= times <= 30:
        realA = 'very like'
        realA_List.append(realA)
    return realA


# In[27]:


def get_env_feedback(S,A,realA):
    #print('S：',S)
    if A == realA:

        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    
    else:       
        if realA == 'very dislike':
            R = -1
            if S == 0:
                S_ = S
            else:
                S_ = S - 1

        elif realA == 'dislike':
            R = -0.5
            if S == 0:
                S_ = S 
            else:
                S_ = S - 1

        elif realA == 'soso':
            R = 0
            if S == 0:
                S_ = S
            else:
                S_ = S

        elif realA == 'like':
            R = 0.5
            if S == 0:
                S_ = S
            else:
                S_ = S + 1
        
        elif realA == 'very like':
            R = 1
            if S == 0:
                S_ = S 
            else:
                S_ = S + 1
    
    #print('隨機行為：',A,'|','真實行為：',realA)
    return S_, R


# In[46]:


def rl():
    q_table = build_q_table(N_STATES, ACTIONS)  # 初始 q table
    
    for i in range(20):     # 回合數
        
        S = music_df["music_cluster"][0] - 1   # 回合初始位置
        
        is_terminated = False   # 是否回合結束
        #update_env(S, episode, step_counter)    # 環境更新
        
            
        while not is_terminated:  #not後面為False，執行冒號後面指令
            
            for i in range (len(music_df)):
                A = choose_action(S, q_table)   # 選隨機行為
                times = music_df['times'][i]
                print('秒數：',times)
                realA = action(times)
                #print(A)
                #print(realA)
                print('i：',i,'|','隨機行為：',A,'|','真實行為：',realA)
        
            if A == realA:
                print('SAME')
            elif A != realA:
                print('DIFFERENT')

            S_, R = get_env_feedback(S,A,realA)  # 實施行為並得到環境的反饋
            print("S_: ",S_)
            print("R: ",R)
            print()

            q_predict = q_table.loc[S, A]    # 估算的(狀態-行為)值

            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max()   # 實際的(狀態-行為)值 (回合沒結束)
            else:
                q_target = R     #  實際的(狀態-行為)值 (回合結束)
                is_terminated = True    # terminate this episode

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  #  q_table更新
            S = S_  # 移動到下一個 state

        #i += 1
    
    return q_table


# In[47]:


if __name__ == "__main__":
    q_table = rl()
    print('=====DONE=====')


# In[48]:


print('\r\nQ-table:')
q_table


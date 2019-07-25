import pandas as pd
import numpy as np
import csv

#抓取最近20首歌曲
user_id = 'chiouchingyi'
filenum = 3
data_folder = 'data/input/'
filename = 'record_0' + str(filenum) + '.csv'
filepath = data_folder + user_id + '/' + str(filenum) + '/' + filename
print('輸入data: ',filepath)

record_df = pd.read_csv(filepath)
record_df = record_df.drop("Unnamed: 0", axis = 1)
##print(record_df)

#定義喜歡程度
record_df['types'] = ''
for i in range(0,len(record_df)):
    times = record_df['times'][i]
    if times >= 28:
        record_df['types'][i] = 'verylike'
    elif 20 < times < 28:
        record_df['types'][i] = 'like'
    elif 15 < times <= 20:
        record_df['types'][i] = 'soso'
    elif 5 < times <= 15:
        record_df['types'][i] = 'dislike'
    elif times <= 5:
        record_df['types'][i] = 'verydislike'
##print(record_df)

#挑選20首中聽超輟28秒的歌曲
record_L = []
for num in range(len(record_df)):
    t = record_df['times'][num]
    if t >= 28:
        track = record_df['track_id'][num]
        record_L.append(track)
##print(record_L)

#執行Q-Learning
N_STATES = 20
TYPES = ['verydislike','dislike','soso','like','verylike']
EPSILON = 0.9   # 貪婪度 greedy
ALPHA = 0.1     # 學習率
GAMMA = 0.9    # 獎勵遞減值
MAX_EPISODES = 13   # 最大回合數

def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),     # q_table初始全0
        columns=actions,    # columns對應的是行為名稱
    )
    return table
##print(build_q_table(N_STATES, TYPES))

# 在某個state地點，選擇行為
def choose_action(state, q_table):
    state_actions = q_table.iloc[state, :]  # 選出這個state的所有action值
    #print('state_actions:','\n',state_actions)
    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0):  # 非貪婪 or 或者這個 state 還沒有探索過
        action_name = np.random.choice(TYPES)
    else:
        action_name = state_actions.argmax()    # 貪婪模式
    return action_name

#獎勵機制
def get_env_feedback(realA, S, A, state_L):
    
    if len(state_L) == 0:
        R = 0
    elif len(state_L) == 1:
        if (realA == A) and (S == state_L[0]):
            R = 10
        else:
            R = 0
    elif len(state_L) == 2:
        if (realA == A) and (S == state_L[0] or S == state_L[1]):
            R = 10
        else:
            R = 0
    elif len(state_L) == 3:
        if (realA == A) and (S == state_L[0] or S == state_L[1] or S == state_L[2]):
            R = 10
        else:
            R = 0
    elif len(state_L) == 4:
        if (realA == A) and (S == state_L[0] or S == state_L[1] or S == state_L[2] or S == state_L[3]):
            R = 10
        else:
            R = 0
    elif len(state_L) == 5:    
        if (realA == A) and (S == state_L[0] or S == state_L[1] or S == state_L[2] or S == state_L[3] or S == state_L[4]):
            R = 10
        else:
            R = 0
    elif len(state_L) == 6:
        if (realA == A) and (S == state_L[0] or S == state_L[1] or S == state_L[2] or S == state_L[3] or S == state_L[4] or S == state_L[5]):
            R = 10
        else:
            R = 0
    elif len(state_L) == 7:
        if (realA == A) and (S == state_L[0] or S == state_L[1] or S == state_L[2] or S == state_L[3] or S == state_L[4] or S == state_L[5] or S == state_L[6]):
            R = 10
        else:
            R = 0
    elif len(state_L) == 8:
        if (realA == A) and (S == state_L[0] or S == state_L[1] or S == state_L[2] or S == state_L[3] or S == state_L[4] or S == state_L[5] or S == state_L[6] or S == state_L[7]):
            R = 10
        else:
            R = 0
    elif len(state_L) == 9:
        if (realA == A) and (S == state_L[0] or S == state_L[1] or S == state_L[2] or S == state_L[3] or S == state_L[4] or S == state_L[5] or S == state_L[6] or S == state_L[7] or S == state_L[8]):
            R = 10
        else:
            R = 0
    elif len(state_L) == 10:
        if (realA == A) and (S == state_L[0] or S == state_L[1] or S == state_L[2] or S == state_L[3] or S == state_L[4] or S == state_L[5] or S == state_L[6] or S == state_L[7] or S == state_L[8] or S == state_L[9]):
            R = 10
        else:
            R = 0
        
    if A == 'verydislike':  
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    
    elif A == 'dislike':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
            
    elif A == 'soso':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    
    elif A == 'like':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    
    elif A == 'verylike':
        if S == N_STATES - 1:
            S_ = 'terminal'
        else:
            S_ = S + 1
    
    return S_, R

#強化學習
def rl(state_L):
    q_table = build_q_table(N_STATES, TYPES)  # 初始 q table
    for episode in range(MAX_EPISODES):     # 回合

        S = 0   # 回合初始位置
        is_terminated = False   # 是否回合結束
                   
        while not is_terminated:            
            
            realA = 'verylike'
                           
            A = choose_action(S, q_table)   # 選行為
##            print('A:',A)
            S_, R = get_env_feedback(realA, S, A, state_L)  # 實施行為並得到反饋
##            print("S_: ",S_,'|',"R: ",R)
##            print()

            q_predict = q_table.loc[S, A]    # 估算的(狀態-行為)值

            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max()   #  實際的(狀態-行為)值 (回合沒結束)
            else:
                q_target = R     #  實際的(狀態-行為)值 (回合结束)
                is_terminated = True    # terminate this episode

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  #  q_table 更新
            S = S_  # 探索者移动到下一个 state

    return q_table

#主程式
if __name__ == "__main__":
    
    record_L = []
    index = []
    state_L = []

    #挑>28秒的歌曲
    for num in range(len(record_df)):
        t = record_df['times'][num]
        if t >= 28:
            track = record_df['track_id'][num]
            record_L.append(track)
    print('聽>28秒的歌曲:',record_L)

    #挑>28秒的index
    for i in range(0,len(record_L)):
        Index_label = record_df[record_df['track_id'] == record_L[i]].index.tolist()
        index.append(Index_label)
##    print(index)

    #挑>28秒的state
    for w in range(0,len(index)):
        state = index[w][0]
        state_L.append(state)
    print('重要的state:',state_L)
##    print(index[0][0])
##    print(index[4][0])
    print()
    
    q_table = rl(state_L)
##    print('===== DONE ======')

print('\r\nQ-table:')
q_table['MAX'] = q_table[['verydislike','dislike','soso','like','verylike']].max(axis=1)
print(q_table)

#匯出聽>28之歌曲ID
data_folder2 = 'data/output/'
filename = 'record_output_0' + str(filenum) + '.csv'
outfile = data_folder2 + user_id + '/' + str(filenum) + '/' + filename
print('輸出data: ',outfile)

with open(outfile, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['state','track_id'])
    for m in range(0,len(state_L)):
        state = state_L[m]
        track_id = record_df['track_id'][state]
        
        Table = [[state,track_id]]
        writer.writerows(Table)

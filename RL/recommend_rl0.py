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

#挑選20首中聽超輟28秒的歌曲
record_L = []
for num in range(len(record_df)):
    t = record_df['times'][num]
    if t >= 28:
        track = record_df['track_id'][num]
        record_L.append(track)
##print(record_L)
    
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
##print(index[0][0])
##print(index[4][0])
##print()

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

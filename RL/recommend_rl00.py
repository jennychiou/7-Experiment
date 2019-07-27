import pandas as pd
import numpy as np
import csv

#抓取最近20首歌曲
user_id ='test'
filenum = 3
data_folder = 'data/input/'
filename = user_id + '_record_0' + str(filenum) + '.csv'
filepath = data_folder + user_id + '/' + str(filenum) + '/' + filename
print('輸入data: ',filepath)

record_df = pd.read_csv(filepath)
##record_df = record_df.drop("Unnamed: 0", axis = 1)
##print(record_df)

track_L = []
for i in range(0,len(record_df)):
    track = record_df['track_id'][i]
    track_L.append(track)

#匯出聽>28之歌曲ID
data_folder2 = 'data/output/'
filename = user_id + '_record_output_0' + str(filenum) + '.csv'
outfile = data_folder2 + user_id + '/' + str(filenum) + '/' + filename
print('輸出data: ',outfile)

with open(outfile, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['state','track_id'])
    for m in range(0,len(track_L)):
        num = m
        track_id = record_df['track_id'][m]
        
        Table = [[num,track_id]]
        writer.writerows(Table)

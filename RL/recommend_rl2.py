import pymysqls
import csv
import pandas as pd

#先建立好第_次推薦的資料夾，更改user_id、num
user_id = 'chiouchingyi'
num = 3
data_folder = 'data/output/'
filename = 'record_output_0' + str(num) + '.csv'
filepath = data_folder + user_id + '/' + str(num) + '/' + filename
print('輸入data: ',filepath)

df = pd.read_csv(filepath)
hybrid_df = pd.read_csv('csv/hybrid20tracks_sim_outputEUCcsv.csv')

#聽大於28秒的歌曲
track_L = []
similarity_L = []
for i in range(0,len(df)):
    track = df['track_id'][i]
    track_L.append(track)
print('喜歡的tracks: ',track_L)

filename2 = 'record_output_p_0' + str(num) + '.csv'
filepath2 = data_folder + user_id + '/' + str(num) + '/' + filename2
print('聽大於28秒的歌曲data: ',filepath2)

#在hybrid的csv挑選聽>28秒的歌曲
with open(filepath2, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','h_top1','h_top2','h_top3','h_top4','h_top5','h_top6','h_top7','h_top8','h_top9','h_top10','h_top11','h_top12','h_top13','h_top14','h_top15','h_top16','h_top17','h_top18','h_top19','h_top20'])

    for w in range(0,len(track_L)):
        select = hybrid_df.loc[hybrid_df['id'] == track_L[w]]
        select_0 = select.iat[0,0]
        select_1 = select.iat[0,1]
        select_2 = select.iat[0,2]
        select_3 = select.iat[0,3]
        select_4 = select.iat[0,4]
        select_5 = select.iat[0,5]
        select_6 = select.iat[0,6]
        select_7 = select.iat[0,7]
        select_8 = select.iat[0,8]
        select_9 = select.iat[0,9]
        select_10 = select.iat[0,10]
        select_11 = select.iat[0,11]
        select_12 = select.iat[0,12]
        select_13 = select.iat[0,13]
        select_14 = select.iat[0,14]
        select_15 = select.iat[0,15]
        select_16 = select.iat[0,16]
        select_17 = select.iat[0,17]
        select_18 = select.iat[0,18]
        select_19 = select.iat[0,19]
        select_20 = select.iat[0,20]
        
        Table = [[select_0,select_1,select_2,select_3,select_4,select_5,select_6,select_7,select_8,select_9,select_10,select_11,select_12,select_13,select_14,select_15,select_16,select_17,select_18,select_19,select_20]]    
        writer.writerows(Table)

#開啟挑選過的 CSV
select_df = pd.read_csv(filepath2)
##print(select_df.head())

#排序sort相似性的值
filename3 = 'record_output_s_0' + str(num) + '.csv'
filepath3 = data_folder + user_id + '/' + str(num) + '/' + filename3
print('相似性排序後的data: ',filepath3)

similarity_list = []

with open(filepath3, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','similarity'])
    for i in range(0,len(select_df)):
        for j in range(1,21):
            #print(i,j)
            data = select_df.iat[i,j]
            data_re = data.replace('[','').replace(']','').replace(' ','')
            data_sp = data_re.split(',')
            rec_track = data_sp[0].replace("'",'')
            similarity = 1 - (float(data_sp[1])/10) #EUC值越小越好
            similarity_list.append(similarity)
            
            row = [[rec_track,similarity]]
            writer.writerows(row)
print('---------------------------------------------------------------------')

#取推薦之20首歌曲
table_df = pd.read_csv(filepath3)
table_df_sort = table_df.sort_values(by = "similarity", ascending=False) #ascending=False降序
print('前20高分歌曲：')
print(table_df_sort.head(20))
print('---------------------------------------------------------------------')

#去除重複推薦之歌曲
final_table = table_df_sort.iloc[0:20]
print('檢查重複歌曲：')
print(final_table['id'].duplicated())
print('---------------------------------------------------------------------')
final_table_new = final_table.drop_duplicates(subset=['id'], keep='first')
print('去除重複推薦之歌曲：')
print(final_table_new)
print('列表長度：',len(final_table_new))
print('---------------------------------------------------------------------')

#匯出最終推薦之CSV
filename4 = 'record_output_f_0' + str(num) + '.csv'
filepath4 = data_folder + user_id + '/' + str(num) + '/' + filename4
print('最終推薦data: ',filepath4)

if len(final_table_new) < 20:
    diff = 20 - len(final_table_new)
    print('差：',diff)
    insert = table_df_sort[20:20+diff]
    final_table_insert = final_table_new.append(insert)
    print('---------------------------------------------------------------------')
    print('最終推薦之歌曲：')
    print(final_table_insert)
    print('列表長度：',len(final_table_insert))
    final_table_insert.to_csv(filepath4)
else:
    final_table.to_csv(filepath4)
    print('最終推薦之歌曲：')
    print(final_table_new)

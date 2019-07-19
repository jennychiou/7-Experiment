import pymysql
import csv
import pandas as pd

# 連接資料庫
db = pymysql.connect(host='127.0.0.1', port=3306, user='chiouchingyi', passwd='850121', db='tracks')
cursor = db.cursor()
print("Opened database successfully")

user_id  = 'keri'
data_folder = "CSVTables/surveyresult/"
filepath_a = data_folder + user_id + '_surveyresult_a' + '.csv'
filepath_l = data_folder + user_id + '_surveyresult_l' + '.csv'
filepath_h = data_folder + user_id + '_surveyresult_h' + '.csv'
print('路徑a：',filepath_a)
print('路徑l：',filepath_l)
print('路徑h：',filepath_h)

#讀取audio和lyrics的csv檔
df_a = pd.read_csv(filepath_a)
##print(df_a)
##print(len(df_a))
##print(df_a['i'][20])
##print(df_a['j'][20])
##print(df_a['survey_track'][20])
##print(df_a['rec_track'][20])
##print(df_a['rankvalue'][20])

df_l = pd.read_csv(filepath_l)

##推薦方法
##recom_method = "0" #Audio
##recom_method = "1" #Lyrics
recom_method = "2" #Hybrid

rankvalue_list= []
with open(filepath_h, "w", newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['i','j','survey_track','rec_track','rankvalue_a','rankvalue_l','rankvalue'])

    for m in range(len(df_a)):
        i = df_a['i'][m]
        j = df_a['j'][m]
        survey_track = df_a['survey_track'][m]
        rec_track = df_a['rec_track'][m]
        rankvalue_a = df_a['rankvalue'][m]
#加條件判斷ID是否有對應到
        rankvalue_l = df_l['rankvalue'][m]
        rankvalue =  float(rankvalue_a) *0.5 + float(rankvalue_l)*0.5
        rankvalue_list.append(rankvalue)
        
        Table = [[i,j,survey_track,rec_track,rankvalue_a,rankvalue_l,rankvalue]]
        writer.writerows(Table)

    print('===== CSV DONE =====')
    
    rankvalue_list.sort(reverse = True)
##    print(rankvalue_list)
    rank_sort_value =  rankvalue_list[0]
##    print(rank_sort_value)

#取推薦之20首歌曲
table_df = pd.read_csv(filepath_h)
##print(table_df)
table_df_sort = table_df.sort_values(by = "rankvalue", ascending=False) #ascending=False降序
##print(table_df_sort)
print('前20高分歌曲：')
print(table_df_sort.head(20))
final_table = table_df_sort.iloc[0:20]
print(final_table['rec_track'])
print('---------------------------------------------------------------------')

#去除重複推薦之歌曲
print('檢查重複歌曲：')
print(final_table['rec_track'].duplicated())
print('---------------------------------------------------------------------')
final_table_new = final_table.drop_duplicates(subset=['rec_track'], keep='first')
print('去除重複推薦之歌曲：')
print(final_table_new)
print('列表長度：',len(final_table_new))
print('---------------------------------------------------------------------')
filepath2 = data_folder + user_id + '_surveyresult_h_new' + '.csv'
if len(final_table_new) < 20:
    diff = 20 - len(final_table_new)
    print('差：',diff)
    insert = table_df_sort[20:20+diff]
    final_table_insert = final_table_new.append(insert)
    print('列表長度：',len(final_table_insert))
##    print(final_table_insert)
    final_table_insert.to_csv(filepath2)
else:
    final_table.to_csv(filepath2)
    print('最終推薦之歌曲：')
    print(final_table_new)
    
#取推薦歌曲ID
##print(final_table.iat[0,3])
##print(final_table.iat[19,3])
#data放入資料庫
for m in range(20):
    if len(final_table_new) < 20:
        track_id = final_table_insert.iat[m,3]  # 有插入新列
    else:
        track_id = final_table_new.iat[m,3]   # 沒插入新列
    recom_rank = m + 1

    sql_1 = "set SQL_SAFE_UPDATES = 0"
    sql_2 = "set @user_id = (select user from tracks_surveyresults where user = '{}')".format(user_id)
    sql_3 = "set @track_id = '{}'".format(track_id)
    sql_4 = "set @album_id = (select album_id from tracks_features where id = @track_id)"
    sql_5 = "set @album_img_url = (select img_url from tracks_album where id = @album_id)"
    sql_6 = "set @artist_id = (select artist_id from tracks_features where id = @track_id)"
    sql_7 = "set @artist_name = (select name from tracks_artist where id = @artist_id)"
    sql_8 = "set @recom_method = '{}'".format(recom_method)
    sql_9 = "set @recom_rank = '{}'".format(recom_rank)
    sql_10 = "set @score = ''"
    sql_11 = "insert into tracks_recsysresults (user_id, album_img_url, track_id, artist_name, recom_method, recom_rank, score) values (@user_id, @album_img_url, @track_id, @artist_name, @recom_method, @recom_rank, @score);"

    try:
        cursor.execute(sql_1) 
        cursor.execute(sql_2) 
        cursor.execute(sql_3)
        cursor.execute(sql_4) 
        cursor.execute(sql_5)
        cursor.execute(sql_6) 
        cursor.execute(sql_7) 
        cursor.execute(sql_8)
        cursor.execute(sql_9)
        cursor.execute(sql_10) 
        cursor.execute(sql_11)
        
    except Exception as e:
        db.rollback()
        print('處理失敗:', e)
    else:
        db.commit()
        print(m+1, '--', '處理成功:', cursor.rowcount)

    # 關閉連接
##    cursor.close()
##    db.close()

import pymysql
import csv
import pandas as pd

# 連接資料庫
db = pymysql.connect(host='127.0.0.1', port=3306, user='chiouchingyi', passwd='850121', db='tracks')
cursor = db.cursor()
print("Opened database successfully")

user_id = 'lintimken'
getsurveyresult = "select results from tracks_surveyresults where user='{}'".format(user_id)
data1 = cursor.execute(getsurveyresult)
##print(data1)  # 返回為0或者1，1表示有資料，0表示無資料或失敗
rs1 = cursor.fetchall()
##print(rs1)

for row in rs1:
    result = row[0]
    print('用戶調查記錄：','\n',result)
print('---------------------------------------------------------------------')
x = result.replace('{','').replace('}','')
##print(x)
##print('---------------------------------------------------------------------')
y = x.split(',')
##print(y)
##print('y[0]:',y[0])
##print('長度：',len(y))
##print('---------------------------------------------------------------------')
z = y[0].split(':')
##print('trackID:', z[0].replace("'",'')) #replace方法去掉引號
##print('score: ', z[1].replace("'",'')) #replace方法去掉引號
##print(eval(z[0])) #eval去掉引號
##print('---------------------------------------------------------------------')

##抓用戶調查分數
trackID_select= []
rating = []
count = 0
for i in range(len(y)):
    x = result.replace('{','').replace('}','')
    y = x.split(',')
    z = y[i].split(':')
    trackID = z[0].replace("'",'')
    score = int(z[1].replace("'",''))
    rating.append(score)
    
    if score == 5:
        print('第',i+1,'首:',trackID,'|',score)
        trackID_select.append(trackID)
        count += 1

print('---------------------------------------------------------------------')
print('rating = ',rating)
print('相對高分歌曲：','\n',trackID_select)

if count == 0:
    for i in range(len(y)):
        x = result.replace('{','').replace('}','')
        y = x.split(',')
        z = y[i].split(':')
        trackID = z[0].replace("'",'')
        score = int(z[1].replace("'",''))
        if score == 4:
            print('第',i+1,'首:',trackID,'|',score)
            trackID_select.append(trackID)
    print('---------------------------------------------------------------------')
    print('相對高分歌曲：','\n',trackID_select)
                    
print('---------------------------------------------------------------------')

##推薦方法
##recom_method = "0" #Audio
recom_method = "1" #Lyrics
##recom_method = "2" #Hybrid

survey_track = ['1au9q3wiWxIwXTazIjHdfF','1ExfPZEiahqhLyajhybFeS','1fLlRApgzxWweF1JTf8yM5','1pSIQWMFbkJ5XvwgzKfeBv',
                '1UMJ5XcJPmH6ZbIRsCLY5F','2W2eaLVKv9NObcLXlYRZZo','3S0OXQeoh0w6AY8WQVckRW','3wF0zyjQ6FKLK4vFxcMojP',
                '4FCb4CUbFCMNRkI6lYc1zI','4RL77hMWUq35NYnPLXBpih','52UWtKlYjZO3dHoRlWuz9S','5b88tNINg4Q4nrRbrCXUmg',
                '5E5MqaS6eOsbaJibl3YeMZ','5uCax9HTNlzGybIStD3vDh','5WLSak7DN3LY1K71oWYuoN','6G7URf5rGe6MvNoiTtNEP7',
                '6QPKYGnAW9QozVz2dSWqRg','6rUp7v3l8yC4TKxAAR5Bmx','7qjbpdk0IYijcSuSYWlXO6','7uRznL3LcuazKpwCTpDltz']

df = pd.read_csv('temp/survry20tracks_sim_l_outputEUCcsv.csv')
count = 0
rankvalue_list= []
data_folder = "CSVTables/surveyresult/"
filepath = data_folder + user_id + '_surveyresult_l' + '.csv'
print('路徑：',filepath)

with open(filepath, "w", newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['i','j','survey_track','rec_track','rating','similarity','rankvalue'])

    for i in range(0,20):
        for j in range(1,21):
    ##        print(i,j)
            survey_track_name = survey_track[i].replace("'",'')
            data = df.iat[i,j]
            data_re = data.replace('[','').replace(']','').replace(' ','')
            data_sp = data_re.split(',')
            rec_track = data_sp[0].replace("'",'')
            similarity = data_sp[1]
            ratingvalue = rating[i]
            rankvalue = ratingvalue * float(similarity)
            rankvalue_list.append(rankvalue)
##            print('i=',i,',','j=',j)
##            print('rating:',ratingvalue)
##            print('similarity:',similarity)
##            print('rankvalue:',rankvalue)
##            print('---------------------------------------------------------------------')
            count += 1

            Table = [[i,j,survey_track_name,rec_track,ratingvalue,similarity,rankvalue]]
            writer.writerows(Table)
         
        rankvalue_list.sort(reverse = True)
##        print(rankvalue_list)
        rank_sort_value =  rankvalue_list[0]
##        print(rank_sort_value)

#取推薦之20首歌曲
table_df = pd.read_csv(filepath)
##print(table_df)
table_df_sort = table_df.sort_values(by = "rankvalue", ascending=False) #ascending=False降序
##print(table_df_sort)
print('前20高分歌曲：')
print(table_df_sort.head(20))
final_table = table_df_sort.iloc[0:20]
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
filepath2 = data_folder + user_id + '_surveyresult_l_new' + '.csv'
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
    
##track_id = '001rKAr9siVsYzpSooZRF0'
##gettop20_2 = "select a_top2 from tracks_audiolyricstop20 where id='{}'".format(track_id)
##cursor.execute(gettop20_2)
####print(data2)  # 返回為0或者1，1表示有資料，0表示無資料或失敗
##rs2 = cursor.fetchall()
##print(rs2)
##for row in rs2:
##    result = row[0]
##    print('top20result:',result)

##x1 = result.replace('[','').replace(']','')
####print('x1',x1)
##y1 = x1.split(',')
####print(y1)
##print('top20 trackid:',eval(y1[0])) #trackid
##print('euc:',eval(y1[1])) #euc

#取推薦歌曲ID
##print(final_table.iat[0,3])
##print(final_table.iat[19,3])
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
    sql_7 = "set @artist_name = (select artist_name from tracks_artist where id = @artist_id)"
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

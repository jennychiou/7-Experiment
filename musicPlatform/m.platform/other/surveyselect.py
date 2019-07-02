import pymysql

# 連接資料庫
db = pymysql.connect(host='127.0.0.1', port=3306, user='chiouchingyi', passwd='850121', db='tracks')
cursor = db.cursor()
print("Opened database successfully")

user_name = "chiouchingyi"
getsurveyresult = "select results from tracks_surveyresults where user='{}'".format(user_name)
data1 = cursor.execute(getsurveyresult)
##print(data1)  # 返回為0或者1，1表示有資料，0表示無資料或失敗
rs1 = cursor.fetchall()
##print(rs1)

for row in rs1:
    result = row[0]
    print('用戶調查記錄：','\n',result)
print('-------------------------------------------------------------------------------------')
x = result.replace('{','').replace('}','')
##print(x)
##print('-------------------------------------------------------------------------------------')
y = x.split(',')
##print(y)
##print('y[0]:',y[0])
##print('長度：',len(y))
##print('-------------------------------------------------------------------------------------')
z = y[0].split(':')
##print('trackID:', z[0].replace("'",'')) #replace方法去掉引號
##print('score: ', z[1].replace("'",'')) #replace方法去掉引號
##print(eval(z[0])) #eval去掉引號
##print('-------------------------------------------------------------------------------------')

##抓用戶調查分數
trackID_select= []
count = 0
for i in range(len(y)):
    x = result.replace('{','').replace('}','')
    y = x.split(',')
    z = y[i].split(':')
    trackID = z[0].replace("'",'')
    score = int(z[1].replace("'",''))
    
    if score == 5:
        print('第',i+1,'首:',trackID,'|',score)
        trackID_select.append(trackID)
        count += 1
print('-------------------------------------------------------------------------------------')
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
    print('-------------------------------------------------------------------------------------')
    print('相對高分歌曲：','\n',trackID_select)
                    
print('-------------------------------------------------------------------------------------')

##推薦方法
##recom_method = "0" #Audio
##recom_method = "1" #Lyrics
##recom_method = "2" #Hybrid

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

##sql_1 = "set SQL_SAFE_UPDATES = 0"
##sql_2 = "set @user_id = (select user from tracks_surveyresults)"
##sql_3 = "set @track_id = '000xQL6tZNLJzIrtIgxqSl';"
##sql_4 = "set @album_id = (select album_id from tracks_features where id = @track_id);"
##sql_5 = "set @album_img_url = (select img_url from tracks_album where id = @album_id)"
##sql_6 = "set @artist_id = (select artist_id from tracks_features where id = @track_id)"
##sql_7 = "set @artist_name = (select artist_name from tracks_artist where id = @artist_id)"
##sql_8 = "set @recom_method = '1'"
##sql_9 = "set @recom_rank = '1'"
##sql_10 = "set @score = '5'"
##sql_11 = "insert into tracks_recsysresults2 (user_id, album_img_url, track_id, artist_name, recom_method, recom_rank, score) values (@user_id, @album_img_url, @track_id, @artist_name, @recom_method, @recom_rank, @score);"
##
##try:
##    cursor.execute(sql_1) 
##    cursor.execute(sql_2) 
##    cursor.execute(sql_3)
##    cursor.execute(sql_4) 
##    cursor.execute(sql_5)
##    cursor.execute(sql_6) 
##    cursor.execute(sql_7) 
##    cursor.execute(sql_8)
##    cursor.execute(sql_9) 
##    cursor.execute(sql_10)
##    cursor.execute(sql_11)
##    
##except Exception as e:
##    db.rollback()
##    print('處理失敗:', e)
##else:
##    db.commit()
##    print('處理成功:', cursor.rowcount)
##
### 關閉連接
##cursor.close()
##db.close()

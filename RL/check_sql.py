import pymysql
import csv
import pandas as pd

# 連接資料庫
db = pymysql.connect(host='127.0.0.1', port=3306, user='chiouchingyi', passwd='850121', db='tracks')
cursor = db.cursor()
print("Opened database successfully")

user_id = 'chiouchingyi'
track_id = '2EafRNF3anmyMbeKoXWkcS' #存在
##track_id = '0sQpqRGBBlbWNL2bhHG6fs' #不存在

check_sql = "select track_id from tracks_recfromrlresults where track_id = '{}' and user_id = '{}'".format(track_id,user_id)
num_sql = "select number_of_rec_times from tracks_recfromrlresults where track_id = '{}' and user_id = '{}'".format(track_id,user_id)
re = cursor.execute(check_sql)
cursor.execute(num_sql)
results = cursor.fetchone()
print('資料是否存在 (0不存在/1存在): ',re)

if re == 1:
    number = str(results).replace("('","").replace("',)","")
    print(results)
    print(number)
    number_times = int(number) + 1
    print('次數: ',number_times)

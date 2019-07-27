import pymysql
import csv
import pandas as pd

# 連接資料庫
db = pymysql.connect(host='127.0.0.1', port=3306, user='chiouchingyi', passwd='850121', db='tracks')
cursor = db.cursor()
print("Opened database successfully")

user_id = 'nicole'
num = 20

final_L = []

data_folder = "csv/results/"
filepath = data_folder + user_id+ '.csv'
print('路徑：',filepath)

getrecresult = "select score from tracks_recfromrlresults where user_id='{}' and number_of_rec_times='{}'".format(user_id,num)
data1 = cursor.execute(getrecresult)
##print(data1)  # 返回為0或者1，1表示有資料，0表示無資料或失敗
rs1 = cursor.fetchall()
##print(rs1)

if int(num) > 1:
    action = 'a'
else:
    action = 'w'

with open(filepath, action, newline='') as csvfile:
    writer = csv.writer(csvfile)
    if num == 1:
        writer.writerow(['user_id','number_of_rec_times','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','s15','s16','s17','s18','s19','s20','avg_score'])
    L = []
    for row in rs1:
        result = row[0]
        L.append(int(result))
    print(num)
    print(L)
    avg_score = sum(L)/len(L)        
    print('ID:',user_id,' | ','AVG score:',avg_score)

    Table = [[user_id,num,L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9],L[10],L[11],L[12],L[13],L[14],L[15],L[16],L[17],L[18],L[19],avg_score]]
    writer.writerows(Table)

import pymysql
import csv
import pandas as pd

# 連接資料庫
db = pymysql.connect(host='127.0.0.1', port=3306, user='chiouchingyi', passwd='850121', db='tracks')
cursor = db.cursor()
print("Opened database successfully")

#user_L = ['chiouchingyi','lintimken','bibicall','jacky','keri','vivian','chiouzihling']
#user_id = 'chiouchingyi'
user_L = ['chiouchingyi','lintimken','jacky','keri','vivian','chiouzihling','alex']
recom_method = '2'

final_L = []

data_folder = "CSVTables/recscore/"
filepath = data_folder + 'recscore_' + recom_method + '.csv'
print('路徑：',filepath,'\n')

with open(filepath, "w", newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['user_id','recom_method','avg_score','final_score'])
    
    for i in range(0,len(user_L)):
        user_id = user_L[i]
        getrecresult = "select score from tracks_recsysresults where user_id='{}' and recom_method='{}'".format(user_id,recom_method)
        data1 = cursor.execute(getrecresult)
        ##print(data1)  # 返回為0或者1，1表示有資料，0表示無資料或失敗
        rs1 = cursor.fetchall()
        ##print(rs1)
            
        scoreList = []
        for row in rs1:
            result = row[0]
            scoreList.append(int(result))
        print(scoreList)
        avg_score = sum(scoreList)/20        
        print('ID:',user_id,' | ','AVG score:',avg_score)

        print('----------------------------------------------------')

        final_L.append(avg_score)
        
        if i == len(user_L)-1 and recom_method == '0':        
            allfinal = sum(final_L)/len(user_L)
            print('recom_method',recom_method)
            print('final list:',final_L)
            print('final score:',allfinal)

        if i == len(user_L)-1 and recom_method == '1':   
            allfinal = sum(final_L)/len(user_L)
            print('recom_method',recom_method)
            print('final list:',final_L)
            print('final score:',allfinal)

        if i == len(user_L)-1 and recom_method == '2':
            allfinal = sum(final_L)/len(user_L)
            print('recom_method',recom_method)
            print('final list:',final_L)
            print('final score:',allfinal)

        if i == len(user_L)-1:
            final_score = allfinal
        else:
            final_score = ''

        Table = [[user_id,recom_method,avg_score,final_score]]
        writer.writerows(Table)

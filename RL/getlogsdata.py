import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId #這東西再透過ObjectID去尋找的時候會用到
import time
import csv
import pandas as pd

conn  = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn ["recSys"]
collection = db["logs"]

# test if connection success
##print('connect:',collection.stats)  # 如果沒有error，代表連線成功

##cursor = collection.find_one({'_id': ObjectId("5d387c76aec77acd98394434")})
##data = [d for d in cursor]
##print(cursor)

#用戶資訊
user_id = 'chiouchingyi'
filenum = 2
data_folder = 'data/input/'
filename = user_id + '_record_0' + str(filenum) + '.csv'
filepath = data_folder + user_id + '/' + str(filenum) + '/' + filename
print('輸出播放紀錄data: ',filepath)

#根據指定條件查詢
#http://www.runoob.com/python3/python-mongodb-query-document.html
myquery = { "user": user_id}
mydoc = collection.find(myquery)

user_id_L = []
track_id_L = []
track_name_L = []
time_L = []

for x in mydoc:
##    print(x)
    user_id = x['user']
    track_id = x['track_id']
    track_name = x['track_name']
    time = x['timestamp']
    user_id_L.append(user_id)
    track_id_L.append(track_id)
    track_name_L.append(track_name)
    time_L.append(time)
##    print(user_id)
##    print(track_id)
##    print(time)

#播放紀錄建立dataframe
df = pd.DataFrame(list(zip(user_id_L,track_id_L,track_name_L,time_L)), columns =['user_id','track_id','track_name','time'])
##print(df)

print('根據時間排序：')
##df['time'] = pd.to_datetime(df['time'])
df2 = df.sort_values(by = 'time', ascending=False)
##print(df2)

#取前20筆資料
print(df2.head(20))

##print(user_id_L)
##print(track_id_L)
##print(track_name_L)
##print(time_L)

return1_L = []
return2_L = []
return3_L = []
return4_L = []
for v in range(len(df2)-1,-1,-1):
    return1 = df2['user_id'][v]
    return2 = df2['track_id'][v]
    return3 = df2['track_name'][v]
    return4 = df2['time'][v]
    return1_L.append(return1)
    return2_L.append(return2)
    return3_L.append(return3)
    return4_L.append(return4)

##print(return1_L)
##print(return2_L)
##print(return3_L)
##print(return4_L)

#回傳資料筆數
select_count = collection.count_documents(myquery)
print('資料筆數：',select_count)

#返回指定條數紀錄
##myresult = collection.find().limit(1)
##for x in myresult:
##  print(x)

#挑選最近的20首歌曲
with open(filepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['user_id','track_id','track_name','time'])
    for m in range(0,20): #(0,20)時間最近的20筆資料
        a = return1_L[m]
        b = return2_L[m]
        c = return3_L[m]
        d = return4_L[m]
        
        Table = [[a,b,c,d]]
        writer.writerows(Table)

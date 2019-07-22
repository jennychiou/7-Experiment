# import
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId #這東西再透過ObjectID去尋找的時候會用到

# connection
#方法一連接
##conn = MongoClient() # 如果你只想連本機端的server你可以忽略，遠端的url填入: mongodb://<user_name>:<user_password>@ds<xxxxxx>.mlab.com:<xxxxx>/<database_name>，請務必既的把腳括號的內容代換成自己的資料。
##db = conn.recSys
##collection = db.survey
#方法二連接
conn  = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn ["recSys"]
collection = db["survey"]

# test if connection success
print('connect:',collection.stats)  # 如果沒有error，代表連線成功

#尋找(find) : 尋找一筆資料
##cursor = collection.find_one({'<column_name>': '<what_you_want>'})
cursor = collection.find_one({'_id': ObjectId('5d1461819fdd613009d7315a')})
#如果你在意速度的話用Id尋找會比用內容尋找快很多喔!

#回傳全部資料
##cursor = collection.find({}) #回傳的並不是資料本身，必須在迴圈中逐一讀出來的過程中，它才真的會去資料庫把資料撈出來
data = [d for d in cursor] #這樣才能真正從資料庫把資料庫撈到python的暫存記憶體中。

#回傳dict型態
print(cursor)
##print(type(cursor))

survey_track = ['1au9q3wiWxIwXTazIjHdfF','1ExfPZEiahqhLyajhybFeS','1fLlRApgzxWweF1JTf8yM5','1pSIQWMFbkJ5XvwgzKfeBv',
                '1UMJ5XcJPmH6ZbIRsCLY5F','2W2eaLVKv9NObcLXlYRZZo','3S0OXQeoh0w6AY8WQVckRW','3wF0zyjQ6FKLK4vFxcMojP',
                '4FCb4CUbFCMNRkI6lYc1zI','4RL77hMWUq35NYnPLXBpih','52UWtKlYjZO3dHoRlWuz9S','5b88tNINg4Q4nrRbrCXUmg',
                '5E5MqaS6eOsbaJibl3YeMZ','5uCax9HTNlzGybIStD3vDh','5WLSak7DN3LY1K71oWYuoN','6G7URf5rGe6MvNoiTtNEP7',
                '6QPKYGnAW9QozVz2dSWqRg','6rUp7v3l8yC4TKxAAR5Bmx','7qjbpdk0IYijcSuSYWlXO6','7uRznL3LcuazKpwCTpDltz']

#dictf取值方法 https://blog.csdn.net/HHTNAN/article/details/77164198
print(cursor['1au9q3wiWxIwXTazIjHdfF'])
print(cursor['user'])

#尋找全部資料
##cursor = collection.find({'<column_name>': '<what_you_want>'})

import pandas as pd

df = pd.read_csv("f1combfinal2.csv")
##print (df.describe())

df_feature_selected = df.drop(['f_name', 'spot_id', 'sr_json','tempo', 'energy','danceability', 'loudness', 'valence', 'acousticness', 'tr_json', 'mood'], axis=1)
print(df_feature_selected.head(5))
##print(df_feature_selected['title'][0])
##print(df_feature_selected['lyrics'][3])
row = df.shape[0]
print("資料行數 : ",row) #行數

#import to database
import  pymysql
conn  =  pymysql.connect ( host = '127.0.0.1' ,  user = 'root' ,  passwd = "850121" ,  db = 'musicdb' ) 
cur  =  conn.cursor()
sql = "INSERT INTO songlist_github (song,singer,lyrics,vector) VALUES (%s,%s,%s,%s)" 
for i in range(0,row):
    titlen = df_feature_selected['title'][i]
    aname = df_feature_selected['a_name'][i]
    word = df_feature_selected['lyrics'][i]
    val = (titlen,aname,word,"")
    cur.execute(sql, val)
cur.close () 
conn.close()

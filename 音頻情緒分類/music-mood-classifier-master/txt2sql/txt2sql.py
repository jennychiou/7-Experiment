titledata=[] #song
titledata2=[]
singerdata=[] #singer
singerdata2=[]
        
with open('txtFile/songdata.txt','r') as f:
        for line in f:
            titledata.append(line.strip('\n').split(','))
with open('txtFile/singerdata.txt','r') as f:
        for line in f:
            singerdata.append(line.strip('\n').split(','))

for i in range(len(titledata)):
    x = str(titledata[i][0:]).replace("[",'').replace(',',' ').replace(']','')
##    x = str(titledata[i][0:]).replace("[",'').replace("'",'').replace(',',' ').replace(']','')
    titledata2.append(x)
##print(titledata2)
for i in range(len(singerdata)):
    x = str(singerdata[i][0:]).replace("[",'').replace(',',' ').replace(']','')
    singerdata2.append(x)

for i in range(len(titledata)):
##(1, '1979', 'Smashing Pumpkins'),
    titlen = titledata2[i]
    aname = singerdata2[i]
    print(str('(') + str(i+1) + str(', ') + str(titlen) + str(', ') + str(aname) + str('),'))

#import to database
import  pymysql
conn  =  pymysql.connect ( host = '127.0.0.1' ,  user = 'root' ,  passwd = "850121" ,  db = 'musicdb' ) 
cur  =  conn.cursor ()
sql = "INSERT INTO songlist (song, singer,lyrics,vector) VALUES (%s, %s,%s,%s)" 
for i in range(len(singerdata)):
    titlen = titledata2[i]
    aname = singerdata2[i]
    song = eval(titlen)
    singer = eval(aname)
    val = (song, singer,"","")
    cur.execute(sql, val)
cur.close () 
conn.close()

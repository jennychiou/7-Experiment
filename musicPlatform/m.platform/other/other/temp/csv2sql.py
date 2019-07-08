track_iddata = []
namedata = []
artist_iddata = []
artist_namedata = []
track_preview_urldata = []
artist_img_urldata = []
album_namedata = []
album_iddata = []
album_img_urldata = []

track_iddata2 = []
namedata2 = []
artist_iddata2 = []
artist_namedata2 = []
track_preview_urldata2 = []
artist_img_urldata2 = []
album_namedata2 = []
album_iddata2 = []
album_img_urldata2 = []

with open('track_id.txt','r') as f:
    for line in f:
        track_iddata.append(line.strip('\n').split(','))
##with open('name.txt','r') as f:
##  for line in f:
##      namedata.append(line.strip('\n').split(','))
with open('artist_id.txt','r') as f:
    for line in f:
        artist_iddata.append(line.strip('\n').split(','))
##with open('artist_name.txt','r') as f:
##  for line in f:
##      artist_namedata.append(line.strip('\n').split(','))
with open('track_preview_url.txt','r') as f:
        for line in f:
            track_preview_urldata.append(line.strip('\n').split(','))
with open('artist_img_url.txt','r') as f:
        for line in f:
            artist_img_urldata.append(line.strip('\n').split(','))
##with open('album_name.txt','r') as f:
##        for line in f:
##            album_namedata.append(line.strip('\n').split(','))
with open('album_id.txt','r') as f:
        for line in f:
            album_iddata.append(line.strip('\n').split(','))
with open('album_img_url.txt','r') as f:
        for line in f:
            album_img_urldata.append(line.strip('\n').split(','))

##歌曲ID
for i in range(len(track_iddata)):
    x = str(track_iddata[i][0:]).replace("[",'').replace(',',' ').replace(']','')
    track_iddata2.append(x)
print(track_iddata2)
            
##歌曲名稱
##for i in range(len(namedata)):
##    x = str(namedata[i][0:]).replace("[",'').replace(',',' ').replace(']','')
##    namedata2.append(x)
##print(namedata2)

##歌手ID
for i in range(len(artist_iddata)):
    x = str(artist_iddata[i][0:]).replace("[",'').replace(',',' ').replace(']','')
    artist_iddata2.append(x)
print(artist_iddata2)

##歌手名稱
##for i in range(len(artist_namedata)):
##    x = str(artist_namedata[i][0:]).replace("[",'').replace(',',' ').replace(']','')
##    artist_namedata2.append(x)
##print(artist_namedata2)

##歌曲URL
for i in range(len(track_preview_urldata)):
    x = str(track_preview_urldata[i][0:]).replace("[",'').replace(',',' ').replace(']','')
    track_preview_urldata2.append(x)
print(track_preview_urldata2)

##歌手圖片URL
for i in range(len(artist_img_urldata)):
    x = str(artist_img_urldata[i][0:]).replace("[",'').replace(',',' ').replace(']','')
    artist_img_urldata2.append(x)
print(artist_img_urldata2)

##專輯名稱
##for i in range(len(album_namedata)):
##    x = str(album_namedata[i][0:]).replace("[",'').replace(',',' ').replace(']','')
##    album_namedata2.append(x)
##print(album_namedata2)

##專輯ID
for i in range(len(album_iddata)):
    x = str(album_iddata[i][0:]).replace("[",'').replace(',',' ').replace(']','')
    album_iddata2.append(x)
print(album_iddata2)

##專輯圖片URL
for i in range(len(album_img_urldata)):
    x = str(album_img_urldata[i][0:]).replace("[",'').replace(',',' ').replace(']','')
    album_img_urldata2.append(x)
print(album_img_urldata2)

import  pymysql
conn  =  pymysql.connect(host='127.0.0.1', port=3306, user='chiouchingyi', passwd='850121', db='tracks') 
cur  =  conn.cursor ()
sql = "INSERT INTO tracks_dataforrec (track_id, artist_id, album_id, track_preview_url, artist_img_url, album_img_url) VALUES (%s,%s,%s,%s,%s,%s)" 

for i in range(len(track_iddata)):
    track_id = track_iddata2[i]
    artist_id = artist_iddata2[i]
    album_id = album_iddata2[i]
    track_preview_url = track_preview_urldata2[i]
    artist_img_url = artist_img_urldata2[i]
    album_img_url = album_img_urldata2[i]
##    if i == 1:
##        print(track_id, artist_id, album_id, track_preview_url, artist_img_url, album_img_url)
##        print()
##        print(eval(track_id), eval(artist_id), eval(album_id), eval(track_preview_url), eval(artist_img_url), eval(album_img_url))

    val = (eval(track_id), eval(artist_id), eval(album_id), eval(track_preview_url), eval(artist_img_url), eval(album_img_url))
    cur.execute(sql, val)
conn.commit()
print('===== Import Done =====')
cur.close () 
conn.close()

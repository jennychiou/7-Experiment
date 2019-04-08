import pytube 
from pprint import pprint

# https://www.youtube.com/watch?v=mrFUSdJU6NU
# https://www.youtube.com/watch?v=1BdPDaFXcEo
#https://www.youtube.com/watch?v=ZbZSe6N_BXs
yt = pytube.YouTube("https://www.youtube.com/watch?v=9xpf9oX-LmA")

vids= yt.streams.all()
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("Enter download number: "))
vids[vnum].download(r"E:\中興資管所\7 實驗進度\Youtube爬蟲")
print('Download Done !')

##import json
##import urllib.request
##import webbrowser
##from win32clipboard import *
##
##url = 'https://www.youtube.com/watch?v=mrFUSdJU6NU'
##
##def main():
##    print("Hello")
##    input("Press 'Enter' to start ...")
##    convert()
##
##def convert():
##    OpenClipboard()
##    vid = GetClipboardData()
##    CloseClipboard()
##    try:
##        data = json.load(urllib.request.urlopen(url+vid))
##    except urllib.error.HTTPError:
##        print('Invlaid url !')
##        input("\nPress 'Enter' to start ...")
##
##    history = open('History.txt', 'a')
##    history.write('\n\n'+data['title']+'\n'+vid)
##    history.close()
##
##    download = input('\nAre you have to download "'+data['title']+'"as a MP3? (y/n)')
##    if download == 'y':
##        webbrowser.open(data['link'])
##        again()
##    else:
##        print('Have a nice day  : )')
##        exit()
##
##main()     

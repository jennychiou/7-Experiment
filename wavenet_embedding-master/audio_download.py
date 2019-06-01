import pandas as pd
import requests as re
import csv

def mp3_download(urls,names):
    for url, name in zip(urls, names):
        
        mp3 = re.get(str(url))
        name = name.replace('/ ', '')
        print(name)
        with open('./test3/{}.mp3'.format(name), 'wb') as f:
            f.write(mp3.content)

if __name__ == "__main__":
    audio = pd.read_csv('./test3/SurveySong0529.csv')
    print(audio.shape)
    urls = audio.iloc[0:,4:5].values.tolist()
    names = audio.iloc[:,0:1].values.tolist()

    for i in range(len(urls)):
        urls[i] = urls[i][0]
        names[i] = names[i][0]

    # print(urls)
    # print('==============')
    # print(names)
    
    mp3_download(urls, names)

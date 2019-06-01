from file_load import file_path
import pandas as pd
import numpy as np
import datetime

def recommend(music_path,music_name): #(mp3位置,mp3名稱)都吃list
    # cos_list, cos_name, folder_list, folder_name = file_path('./dataset', '_cos.csv')
    # euc_list, euc_name, folder_list, folder_name = file_path('./dataset', '_euc.csv')
    recommend_list=[]
    clean_name = []

    for i in music_name:
        clean_name.append(i.replace('.mp3', ''))

    for mp3_path in music_path:
        cos = pd.read_csv(mp3_path.replace('.mp3', '_cos.csv'))
        cos = cos.iloc[1:,0:1].values.tolist()

        for i in range(len(cos)):
            cos[i]=cos[i][0]

        euc = pd.read_csv(mp3_path.mp3replace('.mp3', '_euc.csv'))
        euc = euc.iloc[1:,0:1].values.tolist()

        for i in range(len(cos)):
            euc[i]=euc[i][0]

        ret = list(set(cos).intersection(set(euc)))
        ret = list(set(ret).difference(set(clean_name)))

        if len(ret)>=2:
            ret = ret[0:2]

        elif len(ret)==1:
            euc_set = list(set(euc).difference(set(clean_name)))
            ret = ret + euc_set[0]
        
        else:
            euc_set = list(set(euc).difference(set(clean_name)))
            ret = ret[0:2]

        recommend_list += ret
    
    # print(len(recommend_list))
    print(euc)
    print(cos)

    return recommend_list

def recommend_to_sql(user, love_list, music_name):
    day = datetime.date.today()
    recommend_list = recommend(love_list, music_name)
    username = user
    
    row = (username, recommend_list, day)

    sql = "INSERT INTO tracks.tracks_recommend (`user`, `recommend_list`, `day`) VALUES "+ str(row) + ";"

    return sql
    
if __name__ == "__main__":
    file_list, file_name, folder_list, folder_name = file_path('./dataset', '_OK.npy')
    recommend(file_list,file_name)

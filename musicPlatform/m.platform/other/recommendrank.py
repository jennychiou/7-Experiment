import csv
import pandas as pd
'''
第 2 首:  1ExfPZEiahqhLyajhybFeS | 5
第 7 首:  3S0OXQeoh0w6AY8WQVckRW | 5
第 9 首:  4FCb4CUbFCMNRkI6lYc1zI | 5
第 12 首:  5b88tNINg4Q4nrRbrCXUmg | 5
第 17 首:  6QPKYGnAW9QozVz2dSWqRg | 5
第 20 首:  7uRznL3LcuazKpwCTpDltz | 5
'''
#用戶
rating = [2,5,1,4,4,1,5,2,5,4,1,5,4,3,2,1,5,2,1,5]
##print(len(rating))
survey_track = ['1au9q3wiWxIwXTazIjHdfF','1ExfPZEiahqhLyajhybFeS','1fLlRApgzxWweF1JTf8yM5','1pSIQWMFbkJ5XvwgzKfeBv',
                '1UMJ5XcJPmH6ZbIRsCLY5F','2W2eaLVKv9NObcLXlYRZZo','3S0OXQeoh0w6AY8WQVckRW','3wF0zyjQ6FKLK4vFxcMojP',
                '4FCb4CUbFCMNRkI6lYc1zI','4RL77hMWUq35NYnPLXBpih','52UWtKlYjZO3dHoRlWuz9S','5b88tNINg4Q4nrRbrCXUmg',
                '5E5MqaS6eOsbaJibl3YeMZ','5uCax9HTNlzGybIStD3vDh','5WLSak7DN3LY1K71oWYuoN','6G7URf5rGe6MvNoiTtNEP7',
                '6QPKYGnAW9QozVz2dSWqRg','6rUp7v3l8yC4TKxAAR5Bmx','7qjbpdk0IYijcSuSYWlXO6','7uRznL3LcuazKpwCTpDltz']
##print(survey_track[0].replace("'",''))

##trackID_select =  [' 1ExfPZEiahqhLyajhybFeS', ' 3S0OXQeoh0w6AY8WQVckRW', ' 4FCb4CUbFCMNRkI6lYc1zI',
##                   ' 5b88tNINg4Q4nrRbrCXUmg', ' 6QPKYGnAW9QozVz2dSWqRg', ' 7uRznL3LcuazKpwCTpDltz']
##print('評分5分的歌曲：','\n',trackID_select)
##print('評分5分的歌曲數量：',len(trackID_select))

df = pd.read_csv('temp/survry20tracks_sim_outputEUCcsv.csv')
##print(df.head(3))

#定義每位用戶推薦清單
count = 0
rankvalue_list= []
data_folder = "CSVTables/surveyresult/"
user_id= 'chiouchingyi'
filepath = data_folder + user_id + '_surveyresult' + '.csv'
print('路徑：',filepath)

#每位用戶生成一個csv推薦清單
with open(filepath, "w", newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['i','j','survey_track','rec_track','rating','similarity','rankvalue'])

    for i in range(0,20):
        for j in range(1,21):
    ##        print(i,j)
            survey_track_name = survey_track[i].replace("'",'')
            data = df.iat[i,j]
            data_re = data.replace('[','').replace(']','').replace(' ','')
            data_sp = data_re.split(',')
            rec_track = data_sp[0].replace("'",'')
            similarity = data_sp[1]
            ratingvalue = rating[i]
            rankvalue = ratingvalue * float(similarity)
            rankvalue_list.append(rankvalue)
##            print('i=',i,',','j=',j)
##            print('rating:',ratingvalue)
##            print('similarity:',similarity)
##            print('rankvalue:',rankvalue)
##            print('--------------------------------------------------------')
            count += 1

            Table = [[i,j,survey_track_name,rec_track,ratingvalue,similarity,rankvalue]]
            writer.writerows(Table)
                                    
        #依據rating和similarity相乘結果由大到小排序    
        rankvalue_list.sort(reverse = True)
##        print(rankvalue_list)
        rank_sort_value =  rankvalue_list[0]
##        print(rank_sort_value)

print('===== DONE =====')
print('rankvalue_list長度:',len(rankvalue_list))

#取推薦之20首歌曲
table_df = pd.read_csv(filepath)
##print(table_df)
table_df_sort = table_df.sort_values(by = "rankvalue", ascending=False) #ascending=False降序
##print(table_df_sort)
print('前20高分歌曲：')
print(table_df_sort.head(20))
final_table = table_df_sort.iloc[0:20]

#取推薦歌曲ID
print(final_table.iat[0,3])
print(final_table.iat[1,3])
for m in range(20):
    track_id = final_table.iat[m,3]
    recom_rank = m + 1

##        if i == 19 and j == 20:
##            print('data',data)
##print('資料總筆數：',count)

##print(df.iat[2,1])
##x = df.iat[2,1]
##y = x.replace('[','').replace(']','').replace(' ','')
##print(y)
##z = y.split(',')
##print(z)
##print(z[0].replace("'",''))
##print(z[1])
##print(float(z[1])*2)
##print(df['a_top1'][0])

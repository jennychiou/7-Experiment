import csv
import pandas as pd
import numpy as np

df = pd.read_csv('lyrics_data/tf_20000 (1)_0717_v02.csv')

L1 = []
for num in range(1,301):
    for col in range(1,30):
        
##        ===改===
        df_v = df.iat[3,col]
##        ===改===

        a = df_v.replace("\n","").replace('[','').replace(']','').replace('    ',' ').replace('   ',' ').replace('  ',' ')
        b = a.split(' ',302)
        if b[0] == '':
            c = eval(b[num])
        else:
            c = eval(b[num-1])
        L1.append(c)
##        print(c)
##print(L1)
df2 = pd.read_csv('lyrics_data/tf_20000 (1).csv')
data_folder = "lyrics_data/avg_vec/"

##        ===改===
num1 = df2.iat[503,0]
##        ===改===

n = 30  #大列表中幾個數據组成一個小列表
L2 = [L1[i:i + n] for i in range(0, len(L1), n)]
##print(L2)
final_L = []
for count in range(0,300):
    element = sum(L2[count])/30
    final_L.append(element)
##print(final_L)

#第一首的平均向量
print(len(final_L))





num2 = str(num1).zfill(5)
save_path = data_folder + num2 + '.npy'
print(save_path)
arr_L = np.array(final_L)
np.save(save_path,arr_L)

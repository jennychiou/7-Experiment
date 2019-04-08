titledata=[]
titledata2=[]
with open('songdata.txt','r') as f:
    for line in f:
        titledata.append(line.strip('\n').split(','))
##print(result)

for i in range(len(titledata)):
    x = str(titledata[i][0:]).replace("[",'').replace("'",'').replace(',',' ').replace(']','')
    titledata2.append(x)
for i in range(len(titledata)):
    print(titledata2[i])

import csv

# 二維表格
table = [
    ['姓名', '身高', '體重'],
    ['A', 175, 60],
    ['B', 165, 57]
]

with open('output.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)

  # 寫入二維表格
  writer.writerows(table)

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results = []
    for numbers in lists:
        for i in numbers:
            results.append(i)
    return results

print(flatten(n))

import pandas as pd
groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "Dog"]
ironmen = [59, 9, 19, 14, 6, 77]
ironmen_dict = {
                "groups": groups,
                "ironmen": ironmen
}
# 建立 data frame
ironmen_df = pd.DataFrame(ironmen_dict)
print(ironmen_df)
ironmen_df.to_csv('outputcsvtest.csv')

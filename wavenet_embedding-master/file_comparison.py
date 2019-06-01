from file_load import file_path

def file_comparison(mp3,npy,path):
    mp3_list, mp3_names,folder_list, folder_name = file_path(path, mp3)
    npy_list, npy_names,folder_list, folder_name = file_path(path, npy)
    
    replace_npy = []

    for npy_path in npy_list:
        temp = npy_path.replace('.npy', '.mp3')
        replace_npy.append(temp)

    comparison = list(set(mp3_list).difference(set(replace_npy)))
    
    print(len(npy_list), '輸出的npy數量')
    print('=============')
    print(len(comparison), '未處理的mp3數量')

    with open("./comparison.txt", "w", encoding="utf-8")as txt:
        txt.write(str(comparison))

file_comparison('.mp3','.npy','./test')
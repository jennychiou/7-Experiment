from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen
import file_load
import librosa
import numpy as np
import csv

def wavenet_encode(wave):
    model_path = './wavenet-ckpt/wavenet-ckpt/model.ckpt-200000' #模型位置
    # audio = np.load(file_path)
    encoding = fastgen.encode(wave, model_path, len(wave))
    print(encoding.reshape((-1, 16)).shape)
    return encoding.reshape((-1, 16))

def wavenet_vector(dataset_path):
    name1 = '.mp3' #欲讀取的檔名
    name2 = '.npy' 

    mp3_paths, mp3_names, folder_list, folder_name = file_load.file_path(dataset_path, name1)
    npy_paths, npy_names, folder_list, folder_name = file_load.file_path(dataset_path, name2)

    replace_paths = []
    replace_names = []

    for npy_path, npy_name in zip(npy_paths, npy_names):
        temp = npy_path.replace('.npy', '.mp3')
        temp2 = npy_name.replace('.npy', 'mp3')
        replace_paths.append(temp)
        replace_names.append(temp2)

    comparison_paths = list(set(mp3_paths).difference(set(replace_paths)))
    comparison_names = list(set(mp3_names).difference(set(replace_names)))

    print('沒跑過的數量為{}'.format(str(len(comparison_names))))
    
    with open('tracks_audiofeatures0625_re/audio_vector.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        #writer.writerow(['name','audio_vector'])                         
        count = 0
        for mp3, name in zip(comparison_paths, comparison_names):
            # print(mp3)
            wave, sr = librosa.load(mp3, sr = 16000)
            wavenet_data = wavenet_encode(wave)
            std_wavenet = np.std(wavenet_data, axis=0)
            mean_wavenet = np.mean(wavenet_data, axis=0)

            average_difference_channels = np.zeros((16,))

            for i in range(0, len(wavenet_data) - 2, 2):
                temp = wavenet_data[i] - wavenet_data[i+1]
                average_difference_channels += temp
            average_difference_channels /= (len(wavenet_data) // 2)   
            average_difference_channels = np.array(average_difference_channels)

            concat_features_wavenet = np.hstack((std_wavenet, mean_wavenet))
            concat_features_wavenet = np.hstack((concat_features_wavenet, average_difference_channels))
            
            save_path = mp3.replace('.mp3', "")
            string = save_path
            num = string[-5:]
            print('歌曲編號：',num)
            #print(concat_features_wavenet)
            print('save',concat_features_wavenet.shape,'in',save_path)
            print('===================================================================')
            np.save(save_path,concat_features_wavenet) #存特徵向量在原資料夾
               
            # 寫入CSV
            # Appending new rows to csv file 'a'        
            Table = [[num,concat_features_wavenet]] 
            writer.writerows(Table)
            count += 1
            print('剩餘數量：',len(comparison_names)-count)
    
    print("===== Write CSV DONE =====")

if __name__ == "__main__":
    dataset_path = './tracks_audiofeatures0625_re'#dataset位置
    wavenet_vector(dataset_path)
    print("========== FINISH ==========")

# 排序歌曲name
import operator
data = csv.reader(open('tracks_audiofeatures0625_re/audio_vector.csv'))
sortedlist = sorted(data, key=operator.itemgetter(0)) # 0 specifies according to first column we want to sort
with open("tracks_audiofeatures0625_re/audio_vector_sort.csv", "w") as f:
    fileWriter = csv.writer(f)
    fileWriter.writerow(['num','audio_vector'])
    for row in sortedlist:
        fileWriter.writerow(row)
    print('===== Sort Done =====')

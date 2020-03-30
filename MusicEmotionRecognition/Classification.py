"""
@author: Danyal

The following code classifies piece of music as one of 
the four emotions mentioned in the document
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import sys
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

def classify():
    data = pd.read_csv('Results/Emotion_features.csv')

    songs = []
    for song in data['song_name']:
        songs.append(song)
        
    data_classified = pd.DataFrame()#columns=['class','stress','energy'], index=songs)
    feature = data.ix[:, 'tempo':]
    features = feature.values
    print(data_classified)
    print(songs[0])

    class_vec = pd.Series(np.zeros(len(songs), dtype=str))
    stress_vec = pd.Series(np.zeros(len(songs)))
    energy_vec = pd.Series(np.zeros(len(songs)))

    for i in range(len(songs)):
        if feature['intensity'][i] < 0.5: #low energy
            if (0.7*feature['timbre'][i] + 0.3*feature['rhythm'][i] < 0.5): 
                #data_classified[songs[i]]['class'] = 2 #Contentment
                class_vec.at[i] = 'contenment (+/-)' #2 #set_value(i, 2)
            else:
                #data_classified[songs[i]]['class'] = 3 #Depression
                class_vec.at[i] = 'depression (-/-)' #3
            #data_classified[songs[i]]['stress'] = 0.7*feature['timbre'][i] + 0.3*feature['rhythm'][i]
            stress_vec.iat[i] = 0.7*feature['timbre'][i] + 0.3*feature['rhythm'][i]
        else:
            if (0.3*feature['timbre'][i] + 0.7*feature['rhythm'][i] < 0.5): 
                #data_classified[songs[i]]['class'] = 1 #Exuberance
                class_vec.iat[i] = 'exuberance (+/+)' #1
            else:
                #data_classified[songs[i]]['class'] = 4 #Anxious    
                class_vec.iat[i] = 'anxious, frantic (-/+)' #4
            #data_classified[songs[i]]['stress'] = 0.3*feature['timbre'][i] + 0.7*feature['rhythm'][i]
            stress_vec.iat[i] = 0.3*feature['timbre'][i] + 0.7*feature['rhythm'][i]
    #    if feature['pitch'][i]
        #data_classified[songs[i]]['energy'] = feature['intensity'][i]
        energy_vec.iat[i] = feature['intensity'][i]

    data_classified['song_name'] = songs
    data_classified['class'] = class_vec
    data_classified['stress'] = stress_vec
    data_classified['energy'] = energy_vec
    print(data_classified)

    data_classified.to_csv('Results/Emotion_features_mod_class.csv')

def main():
    classify()

if __name__ == "__main__":
    main()

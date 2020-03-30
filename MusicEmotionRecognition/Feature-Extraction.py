import warnings, librosa
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=FutureWarning)
    import librosa
    import pandas as pd


'''
    function: extract_features
    input: path to mp3 files
    output: csv file containing features extracted
    
    This function reads the content in a directory and for each mp3 file detected
    reads the file and extracts relevant features using librosa library for audio
    signal processing

'''

def norm(var, varmin, varmax):
    return (var-varmin)/(varmax-varmin)

def extract_feature(path):
    id = 1  # Song ID
    feature_set = pd.DataFrame()  # Feature Matrix
    
    # Individual Feature Vectors
    songname_vector = pd.Series()
    tempo_vector = pd.Series()
    total_beats = pd.Series()
    average_beats = pd.Series()
    chroma_stft_mean = pd.Series()
    chroma_stft_std = pd.Series()
    chroma_stft_var = pd.Series()
    chroma_cq_mean = pd.Series()
    chroma_cq_std = pd.Series()
    chroma_cq_var = pd.Series()
    chroma_cens_mean = pd.Series()
    chroma_cens_std = pd.Series()
    chroma_cens_var = pd.Series()
    mel_mean = pd.Series()
    mel_std = pd.Series()
    mel_var = pd.Series()
    mfcc_mean = pd.Series()
    mfcc_std = pd.Series()
    mfcc_var = pd.Series()
    mfcc_delta_mean = pd.Series()
    mfcc_delta_std = pd.Series()
    mfcc_delta_var = pd.Series()
    rmse_mean = pd.Series()
    rmse_std = pd.Series()
    rmse_var = pd.Series()
    cent_mean = pd.Series()
    cent_std = pd.Series()
    cent_var = pd.Series()
    spec_bw_mean = pd.Series()
    spec_bw_std = pd.Series()
    spec_bw_var = pd.Series()
    contrast_mean = pd.Series()
    contrast_std = pd.Series()
    contrast_var = pd.Series()
    rolloff_mean = pd.Series()
    rolloff_std = pd.Series()
    rolloff_var = pd.Series()
    poly_mean = pd.Series()
    poly_std = pd.Series()
    poly_var = pd.Series()
    tonnetz_mean = pd.Series()
    tonnetz_std = pd.Series()
    tonnetz_var = pd.Series()
    zcr_mean = pd.Series()
    zcr_std = pd.Series()
    zcr_var = pd.Series()
    harm_mean = pd.Series()
    harm_std = pd.Series()
    harm_var = pd.Series()
    perc_mean = pd.Series()
    perc_std = pd.Series()
    perc_var = pd.Series()
    frame_mean = pd.Series()
    frame_std = pd.Series()
    frame_var = pd.Series()
    
    tempo_norm = pd.Series()    
    timbre_var = pd.Series()    
    rhythm_var = pd.Series()    
    pitch_var = pd.Series()
    intensity_var = pd.Series()
    entropy_var = pd.Series()
    
    # Traversing over each file in path
    file_data = [f for f in listdir(path) if isfile (join(path, f))]
    for line in file_data:
        if ( line[-1:] == '\n' ):
            line = line[:-1]

        # Reading Song
        songname = path + line
        y, sr = librosa.load(songname, duration=60)
        S = np.abs(librosa.stft(y))
        
        # Extracting Features
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_cq = librosa.feature.chroma_cqt(y=y, sr=sr)
        chroma_cens = librosa.feature.chroma_cens(y=y, sr=sr)
        melspectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
        rmse = librosa.feature.rms(y=y)
        #rmse = librosa.util.normalize(rmse,axis=1)
        cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        contrast = librosa.feature.spectral_contrast(S=S, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        poly_features = librosa.feature.poly_features(S=S, sr=sr)
        tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        harmonic = librosa.effects.harmonic(y)
        percussive = librosa.effects.percussive(y)
        
        mean = np.mean(rmse[0])
        count = 0
        for rms in rmse[0]:
            if (rms < mean):
                count += 1
        lowenergy = count/len(rmse[0])

        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        mfcc_delta = librosa.feature.delta(mfcc)
        cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        entropy = librosa.feature.spectral_flatness(y=y)
        zcr = librosa.feature.zero_crossing_rate(y)  
        onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
        frames_to_time = librosa.frames_to_time(onset_frames[:20], sr=sr)

        pitch = librosa.core.piptrack(y=y, sr=sr)
      
        # Transforming Features
        songname_vector.set_value(id, line)  # song name
        tempo_vector.set_value(id, tempo)  # tempo (beats per minute), middle = 120 bpm
        #tempo_norm.set_value(id, tempo/120.0) 
        total_beats.set_value(id, sum(beats))  # beats
        average_beats.set_value(id, np.average(beats))
        chroma_stft_mean.set_value(id, np.mean(chroma_stft))  # chroma stft
        chroma_stft_std.set_value(id, np.std(chroma_stft))
        chroma_stft_var.set_value(id, np.var(chroma_stft))
        chroma_cq_mean.set_value(id, np.mean(chroma_cq))  # chroma cq
        chroma_cq_std.set_value(id, np.std(chroma_cq))
        chroma_cq_var.set_value(id, np.var(chroma_cq))
        chroma_cens_mean.set_value(id, np.mean(chroma_cens))  # chroma cens
        chroma_cens_std.set_value(id, np.std(chroma_cens))
        chroma_cens_var.set_value(id, np.var(chroma_cens))
        mel_mean.set_value(id, np.mean(melspectrogram))  # melspectrogram
        mel_std.set_value(id, np.std(melspectrogram))
        mel_var.set_value(id, np.var(melspectrogram))
        mfcc_mean.set_value(id, np.mean(mfcc))  # mfcc
        mfcc_std.set_value(id, np.std(mfcc))
        mfcc_var.set_value(id, np.var(mfcc))
        mfcc_delta_mean.set_value(id, np.mean(mfcc_delta))  # mfcc delta
        mfcc_delta_std.set_value(id, np.std(mfcc_delta))
        mfcc_delta_var.set_value(id, np.var(mfcc_delta))
        rmse_mean.set_value(id, np.mean(rmse))  # rmse
        rmse_std.set_value(id, np.std(rmse))
        rmse_var.set_value(id, np.var(rmse))
        cent_mean.set_value(id, np.mean(cent))  # cent
        cent_std.set_value(id, np.std(cent))
        cent_var.set_value(id, np.var(cent))
        spec_bw_mean.set_value(id, np.mean(spec_bw))  # spectral bandwidth
        spec_bw_std.set_value(id, np.std(spec_bw))
        spec_bw_var.set_value(id, np.var(spec_bw))
        contrast_mean.set_value(id, np.mean(contrast))  # contrast
        contrast_std.set_value(id, np.std(contrast))
        contrast_var.set_value(id, np.var(contrast))
        rolloff_mean.set_value(id, np.mean(rolloff))  # rolloff
        rolloff_std.set_value(id, np.std(rolloff))
        rolloff_var.set_value(id, np.var(rolloff))
        poly_mean.set_value(id, np.mean(poly_features))  # poly features
        poly_std.set_value(id, np.std(poly_features))
        poly_var.set_value(id, np.var(poly_features))
        tonnetz_mean.set_value(id, np.mean(tonnetz))  # tonnetz
        tonnetz_std.set_value(id, np.std(tonnetz))
        tonnetz_var.set_value(id, np.var(tonnetz))
        zcr_mean.set_value(id, np.mean(zcr))  # zero crossing rate
        zcr_std.set_value(id, np.std(zcr))
        zcr_var.set_value(id, np.var(zcr))
        harm_mean.set_value(id, np.mean(harmonic))  # harmonic
        harm_std.set_value(id, np.std(harmonic))
        harm_var.set_value(id, np.var(harmonic))
        perc_mean.set_value(id, np.mean(percussive))  # percussive
        perc_std.set_value(id, np.std(percussive))
        perc_var.set_value(id, np.var(percussive))
        frame_mean.set_value(id, np.mean(frames_to_time))  # frames
        frame_std.set_value(id, np.std(frames_to_time))
        frame_var.set_value(id, np.var(frames_to_time))
        entropy_var.set_value(id, np.mean(entropy)) # entropy
        '''
        cent_min = 600
        cent_max = 4000
        cent_norm = norm(np.mean(cent_mean),cent_min,cent_max)
        print(cent_norm)

        rolloff_min = 1000
        rolloff_max = 7100
        rolloff_norm = norm(np.mean(rolloff_mean),rolloff_min,rolloff_max)
        print(rolloff_norm)

        rmse_min = 0.0
        rmse_max = 0.2
        rmse_norm = norm(np.mean(rmse),rmse_min,rmse_max)
        print(rmse_norm)

        zcr_min = 0.0
        zcr_max = 0.3
        zcr_norm = norm(np.mean(zcr_mean),zcr_min,zcr_max)
        print(zcr_norm)

        beats_min = 900
        beats_max = 1700
        beats_norm = norm(np.mean(average_beats),beats_min,beats_max)
        print(beats_norm)

        tempo_min = 40
        tempo_max = 200
        tempo_norm = norm(np.mean(tempo_vector),tempo_min,tempo_max)

        entropy_min = 0.0
        entropy_max = 0.5
        entropy_norm = norm(np.mean(entropy),entropy_min,entropy_max)
        print(entropy_norm)

        pitch_min = 0.0
        pitch_max = 50.0
        pitch_norm = norm(np.mean(pitch),pitch_min,pitch_max)
        '''
        
        intensity_var.set_value(id, 0.8*np.mean(rmse) + (1-lowenergy)*0.2)
        timbre_var.set_value(id, 0.2*np.mean(zcr) + 0.4*np.mean(cent)+ 0.3*np.mean(rolloff) + 0.1*np.mean(entropy))
        rhythm_var.set_value(id, 0.4*np.average(beats) + 0.6*tempo)
        pitch_var.set_value(id, np.mean(pitch))

        '''
        intensity_var.set_value(id, 0.8*rmse_norm + (1-lowenergy)*0.2)
        timbre_var.set_value(id, 0.2*zcr_norm + 0.4*cent_norm+ 0.3*rolloff_norm+ 0.1*entropy_norm)
        rhythm_var.set_value(id, 0.4*beats_norm + 0.6*tempo_norm)
        pitch_var.set_value(id, pitch_norm)
        '''
        print(line)
        id = id+1
    
    intensity_norm = (intensity_var-intensity_var.min())/(intensity_var.max()-intensity_var.min())
    timbre_norm = (timbre_var-timbre_var.min())/(timbre_var.max()-timbre_var.min())
    rhythm_norm = (rhythm_var-rhythm_var.min())/(rhythm_var.max()-rhythm_var.min())
    pitch_norm = (pitch_var-pitch_var.min())/(pitch_var.max()-pitch_var.min())
    entropy_norm = (entropy_var-entropy_var.min())/(entropy_var.max()-entropy_var.min())

    # Concatenating Features into one csv and json format
    feature_set['song_name'] = songname_vector  # song name
    feature_set['class'] = 0

    # Intensity
    feature_set['tempo'] = tempo_vector  # tempo 
    feature_set['total_beats'] = total_beats  # beats
    feature_set['average_beats'] = average_beats
    feature_set['chroma_stft_mean'] = chroma_stft_mean  # chroma stft
    feature_set['chroma_stft_std'] = chroma_stft_std
    feature_set['chroma_stft_var'] = chroma_stft_var
    feature_set['chroma_cq_mean'] = chroma_cq_mean  # chroma cq
    feature_set['chroma_cq_std'] = chroma_cq_std
    feature_set['chroma_cq_var'] = chroma_cq_var
    feature_set['chroma_cens_mean'] = chroma_cens_mean  # chroma cens
    feature_set['chroma_cens_std'] = chroma_cens_std
    feature_set['chroma_cens_var'] = chroma_cens_var
    feature_set['melspectrogram_mean'] = mel_mean  # melspectrogram
    feature_set['melspectrogram_std'] = mel_std
    feature_set['melspectrogram_var'] = mel_var
    feature_set['mfcc_mean'] = mfcc_mean  # mfcc
    feature_set['mfcc_std'] = mfcc_std
    feature_set['mfcc_var'] = mfcc_var
    feature_set['mfcc_delta_mean'] = mfcc_delta_mean  # mfcc delta
    feature_set['mfcc_delta_std'] = mfcc_delta_std
    feature_set['mfcc_delta_var'] = mfcc_delta_var
    feature_set['rmse_mean'] = rmse_mean  # rmse
    feature_set['rmse_std'] = rmse_std
    feature_set['rmse_var'] = rmse_var
    feature_set['cent_mean'] = cent_mean  # cent
    feature_set['cent_std'] = cent_std
    feature_set['cent_var'] = cent_var
    feature_set['spec_bw_mean'] = spec_bw_mean  # spectral bandwidth
    feature_set['spec_bw_std'] = spec_bw_std
    feature_set['spec_bw_var'] = spec_bw_var
    feature_set['contrast_mean'] = contrast_mean  # contrast
    feature_set['contrast_std'] = contrast_std
    feature_set['contrast_var'] = contrast_var
    feature_set['rolloff_mean'] = rolloff_mean  # rolloff
    feature_set['rolloff_std'] = rolloff_std
    feature_set['rolloff_var'] = rolloff_var
    feature_set['poly_mean'] = poly_mean  # poly features
    feature_set['poly_std'] = poly_std
    feature_set['poly_var'] = poly_var
    feature_set['tonnetz_mean'] = tonnetz_mean  # tonnetz
    feature_set['tonnetz_std'] = tonnetz_std
    feature_set['tonnetz_var'] = tonnetz_var
    feature_set['zcr_mean'] = zcr_mean  # zero crossing rate
    feature_set['zcr_std'] = zcr_std
    feature_set['zcr_var'] = zcr_var
    feature_set['harm_mean'] = harm_mean  # harmonic
    feature_set['harm_std'] = harm_std
    feature_set['harm_var'] = harm_var
    feature_set['perc_mean'] = perc_mean  # percussive
    feature_set['perc_std'] = perc_std
    feature_set['perc_var'] = perc_var
    feature_set['frame_mean'] = frame_mean  # frames
    feature_set['frame_std'] = frame_std
    feature_set['frame_var'] = frame_var
    
    feature_set['intensity'] = intensity_norm  # root mean squared energy
    feature_set['timbre'] = timbre_norm  # root mean squared energy
    feature_set['rhythm'] = rhythm_norm  # root mean squared energy
    feature_set['entropy'] = entropy_norm
    feature_set['pitch'] = pitch_norm

    # Converting Dataframe into CSV Excel and JSON file
    feature_set.to_csv('Results/Emotion_features.csv')
    feature_set.to_json('Results/Emotion_features.json')

try:
    extract_feature('Dataset/')
except:
    pass

import os
import numpy as np
from mido import MidiFile
from mido import MetaMessage
from mido import tempo2bpm, bpm2tempo

_notesize = 88

def readmidi(filepath = ""):
    mid = MidiFile(os.getcwd() + filepath)
    
    event_list = []
    timing = 0
    print('MIDI File：',filepath)

    for i, track in enumerate(mid.tracks):
        #print('Track {} : {} '.format(i, track.name))
        #print('Track {} : {} '.format(i, len(track)))

        # 印出tick值
        print ("Ticks per beat:",mid.ticks_per_beat)
        
        #if len(track) > 100:
            #break

        for msg in track:
            #print(msg)
            timing += msg.time
            
            # 印出調號
            if msg.type == 'key_signature':
                print('Key_signature :',msg.key)
            # 印出拍號
            if msg.type == 'time_signature':
                print('Time_signature : numerator={} denominator={}'.format(msg.numerator,msg.denominator))
            # 印出拍子轉bpm
            if msg.type == "set_tempo":
                print("Tempo(BPM):",int(tempo2bpm(msg.tempo)))
            
            if msg.type == 'note_on' and msg.bytes()[2] != 0:
                event_list.append([msg.bytes()[1],timing])

    print()
    print('event_list :\n', event_list)

    time_ = 0
    playone = []
    playlist = []

    for i in event_list:
        if len(playone) == 0 or time_ == i[1]:
            playone.append(i[0])
        else:
            playlist.append(playone)
            playone = [i[0]]
            time_ = i[1]
    print('playlist :\n', playlist)

    return playlist

readmidi('/sampleMidi/Cool_Blues_test1.mid')

"""
    if message.type == 'note_on' and note[event[1]-20] == 0: #Sometimes show only 'note_on'
        #print message
        note[event[1]-20] =timing #  filenumber of Note C4 is 40 and number of Evete[1] C4 is 60. These diffrence is 20
    elif  message.type == 'note_off' :
        duration=(timing - note[event[1]-20])
        event_list.append([ note[event[1]-20] , event[1]-20 , duration])
        note[event[1]-20] = 0
    elif message.type == 'note_on' and note[event[1]-20] != 0 :
        duration=(timing - note[event[1]-20])
        event_list.append([ note[event[1]-20] , event[1]-20 , duration])
        note[event[1]-20] = 0
    else:     #All functions is included except Note_on, Note_off
        continue
"""

def makeMidi_nn(playlist = [], length = 1):

    X = []

    setX = []
    set_y = []
    count = 0

    # play = [ notes ]
    for i in range(len(playlist)-1):
        play = playlist[i]
        one = _makeHOT(play)

        X.append(one)
        count += 1

        if count >= length:

            _y = _makeHOT(playlist[i+1])

            setX.append(X)
            set_y.append(_y)
            preX = X[1:]
            X = []
            for i in preX:
                X.append(i)

    return setX, set_y

def _makeHOT(indexs = []):
    hot = []
    for i in range(1,89):
        if i in indexs:
            hot.append(1)
        else:
            hot.append(0)

    return hot




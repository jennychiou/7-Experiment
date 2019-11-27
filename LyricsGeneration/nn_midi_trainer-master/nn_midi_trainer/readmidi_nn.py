import os
import numpy as np

from mido import MidiFile

_notesize = 88

def readmidi(filepath = ""):
    mid = MidiFile(os.getcwd() + filepath)

    event_list = []
    timing = 0

    print ("Ticks per beat:"),
    print (mid.ticks_per_beat)
    for i, track in enumerate(mid.tracks):
        print('Track {} : {} '.format(i, track.name))
        if len(track) > 100:
            break

    for message in track:
        timing += message.time
        if message.type == 'note_on' and message.bytes()[2] != 0:
            event_list.append([message.bytes()[1]-20,timing])

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

    return playlist

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




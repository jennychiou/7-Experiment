#https://mido.readthedocs.io/en/latest/midi_files.html

from mido import MidiFile
from mido import MetaMessage
from mido import tempo2bpm

mid1 = MidiFile('MIDI/MIDI - Beauty_and_the_Beast.mid')
mid2 = MidiFile('MIDI/MIDI - twinkle_twinkle.mid')

##print('MIDI檔案資訊：',mid,'\n')
##print('MIDI長度：',mid.length,'\n')

#印出檔案資訊所有tracks的messages數量
for track1 in mid1.tracks:
    print(track1)

#印出音軌的資訊(節拍、拍號、音調)
##for msg in mid.tracks[0]:
##    print(msg)
    
count = 0
msg_list = []

for i, track2 in enumerate(mid1.tracks):
    print('Track {}: {}'.format(i, track2.name))
    print('track2 : ',track2)
    
##    if i == 0:
##        for msg in track2:
##            print(msg)
##            count += 1
##            if msg.type=="set_tempo":
##                print("tempo:",tempo2bpm(msg.tempo))             
    
    if i == 0:
        for msg in track2:
            if msg.type=="set_tempo":
                    print("tempo:",tempo2bpm(msg.tempo))
                    print()
           
            if msg.type == 'note_on' or msg.type == 'note_off':
                velocity = msg.velocity
                if velocity != 0:
##                    print(msg) # note_on channel=__ note=__ velocity=__ time=__
                    time = msg.time
                    bytes_list = msg.bytes()
                    bytes_list.append(time)
##                    print(bytes_list) # [__, __, __, __]
                    if time < 99:
                        print(msg,'    |   ',bytes_list)
                    elif 99 <time < 1000:
                        print(msg,'  |   ',bytes_list)
                    elif time > 1000:
                        print(msg,'|   ',bytes_list)
                    count += 1      
    print()
print(count)

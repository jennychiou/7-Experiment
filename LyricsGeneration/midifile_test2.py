#https://mido.readthedocs.io/en/latest/midi_files.html

from mido import MidiFile
from mido import MetaMessage
from mido import tempo2bpm

mid = MidiFile('MIDI/MIDI - fugue8_bk1_bach.mid')
print('MIDI檔案資訊：',mid,'\n')

print('MIDI長度：',mid.length,'\n')

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
##        if msg.type == 'note_on' or msg.type == 'note_off':
            print(msg)
        
#印出檔案資訊所有tracks的messages數量
for track1 in mid.tracks:
    print(track1)
print()

#印出音軌的資訊(節拍、拍號、音調)
##for msg in mid.tracks[0]:
##    print(msg)
    
##count = 0
##msg_list = []
##
##for i, track2 in enumerate(mid.tracks):
##    print('Track {}: {}'.format(i, track2.name))
##    print('track2 : ',track2)
##    
##    if i == 0:
##        for msg in track2:
##            print(msg)
##            count += 1
##                
##    if i == 1:
##        for msg in track2:
##            print(msg)
##            count += 1
##            if msg.type=="set_tempo":
##                print("tempo:",tempo2bpm(msg.tempo))
##
##    if i == 2:
##        for msg in track2:
##            if msg.type == 'note_on' or msg.type == 'note_off':
##                print(msg)
##                time = msg.time
##                bytes_list = msg.bytes()
##                bytes_list.append(time)
##                print(bytes_list)
##            count += 1
##       
##    print()
##print(count)

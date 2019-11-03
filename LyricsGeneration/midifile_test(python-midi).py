#https://github.com/vishnubob/python-midi#Reading_our_Track_back_from_Disk
import midi
pattern = midi.read_midifile("twinkle_twinkle.mid")
print(pattern)

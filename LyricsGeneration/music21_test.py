import music21
from music21 import converter
import pandas as pd

path = r"MIDI/MIDI - Beauty_and_the_Beast.mid"

 #create a function for taking parsing and extracting the notes
def extract_notes(path):
    stm = converter.parse(path)

    treble = stm[0] #access the first part (if there is only one part)
    bass = stm[1]

    #note extraction
    notes_treble = []
    notes_bass = []
    for thisNote in treble.getElementsByClass("Note"):
        indiv_note = [thisNote.name, thisNote.pitch.midi, thisNote.offset]
        notes_treble.append(indiv_note)  # print's the note and the note's 
        offset

    for thisNote in bass.getElementsByClass("Note"):
        indiv_note = [thisNote.name, thisNote.pitch.midi, thisNote.offset]
        notes_bass.append(indiv_note) #add the notes to the bass

    return notes_treble, notes_bass

#write to csv
def to_csv(notes_array):
    df = pd.DataFrame(notes_array, index=None, columns=None)
    df.to_csv("attempt1_v1.csv")

#using the functions
notes_array = extract_notes(path)
#to_csv(notes_array)

#DEBUGGING
stm = converter.parse(path)
print(stm.parts)

from music21 import *
import music21

# 取得MIDI中的音符和休止符
# https://stackoverflow.com/questions/49339622/how-to-extract-individual-chords-rests-and-notes-from-a-midi-file

def get_notes_chords_rests(instrument_type, path):
    try:
        midi = converter.parse(path)
        parts = instrument.partitionByInstrument(midi)
        note_list = []
        for music_instrument in range(len(parts)):
            if parts.parts[music_instrument].id in instrument_type:
                for element_by_offset in stream.iterator.OffsetIterator(parts[music_instrument]):
                    for entry in element_by_offset:
                        if isinstance(entry, note.Note):
                            note_list.append(str(entry.pitch))
                        elif isinstance(entry, chord.Chord):
                            note_list.append('.'.join(str(n) for n in entry.normalOrder))
                        elif isinstance(entry, note.Rest):
                            note_list.append('Rest')
        return note_list
    except Exception as e:
        print("failed on ", path)
        pass

# keyboard_nstrument = ["KeyboardInstrument", "Piano", "Harpsichord", "Clavichord", "Celesta", ]
notes = get_notes_chords_rests("Piano", "MIDI/MIDI - Beauty_and_the_Beast.mid")
print(notes)

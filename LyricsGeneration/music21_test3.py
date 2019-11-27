# https://web.mit.edu/music21/doc/about/what.html

from music21 import *
import matplotlib.pyplot as plt
n = note.Note("D#3")
n.duration.type = 'half'
n.show()

littleMelody = converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f#")
littleMelody.show()

dicant = converter.parse('MIDI/MIDI - Beauty_and_the_Beast.mid')
dicant.plot('histogram', 'pitch')
dicant.show()

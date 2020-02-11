# Convert MP3 to WAV
# https://pythonbasics.org/convert-mp3-to-wav/

import os
import glob
from os import path
from pydub import AudioSegment

# files
lst = glob.glob( "src/" + "*.mp3")
print(lst)

for src in lst:
    # convert wav to mp3
    src = src.replace("\\", "/")
    print('src :',src)
    sound = AudioSegment.from_mp3(src)
    dst = src.replace(".mp3", ".wav").replace('src','dst')
    print('dst :',dst)
    sound.export(dst, format="wav")

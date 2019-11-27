"""
    Coded by Davi Innovation
    davinnovation at gmail.com

    playNotes
"""
from pydub import AudioSegment, playback
import os
import time

class playNotes():
    def __init__(self,codes=[40], chunk_size=2**15):
        import wave
        cwd = os.path.dirname(os.path.realpath(__file__))
        self._wfs = []

        for code in codes:
            c = ""
            if code > 0 and code < 10:
                c = "0"+str(code)
            elif code < 89:
                c = str(code)
            else:
                print("out of code index")
                exit()
            #self._wfs.append(wave.open(cwd + "\piano88\Piano 0" + c + ".wav", 'rb'))
            self._wfs.append(cwd + "\piano88\Piano 0" + c + ".wav")


    def play(self,onset=None):
        """
        Play is handled in the background (multithreading)
        """
        import threading
        self.onset = onset
        trial = 0
        while trial < 3:
            try:
                trial += 1
                self._thread_play = threading.Thread(target=self._play)
                self._thread_play.start()
                return
            except Exception:
                raise RuntimeError('Could not set up thread')

    def _play(self):

        audios = []
        for wav in self._wfs:
            audios.append(AudioSegment.from_file(wav))

        if len(audios) == 1:
            playback.play(audios[0])
        elif len(audios) > 1:
            wait = audios[0].overlay(audios[1])
            for i in range(2,len(audios)):
                wait = wait.overlay(audios[i])
            playback.play(wait)



# example
if __name__ == '__main__':

    playNotes(codes=[38]).play()
    time.sleep(0.5)
    playNotes(codes=[42]).play()
    time.sleep(0.5)

    playNotes(codes=[57, 59]).play()
    time.sleep(0.5)
    playNotes(codes=[57, 60, 63]).play()
    time.sleep(0.5)
    playNotes(codes=[57, 60, 63,66]).play()
    time.sleep(0.5)
    playNotes(codes=[57, 60, 63,66,69]).play()

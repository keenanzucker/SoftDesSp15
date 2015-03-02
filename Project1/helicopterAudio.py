"""Helicopter Game
Keenan Zucker and Scott Mackinlay"""


import alsaaudio
import audioop
    
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,0)
inp.setchannels(1)
inp.setrate(16000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)
        
i = 0
while i < 1000:
    l,data = inp.read()
    if l:
            print audioop.rms(data,2)
    i += 1
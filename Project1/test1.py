import alsaaudio
import audioop
import pygame
from pygame.locals import *
import random
import time
import sys

pygame.init()

width = 640
height = 480

black = (0,0,0)
white = (250,250,250)

widthR = 20
heightR = 20

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Is It....Helicopter?')

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,0)
inp.setchannels(1)
inp.setrate(16000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)
        
i = 0
while i < 500:
    l,data = inp.read()
    if l:
            print audioop.rms(data,2)
            audio = audioop.rms(data,2)

    i += 1
    screen.fill(white)
    pygame.draw.rect(screen, (100,200,50), (100, 480 - audio, widthR, heightR))

    pygame.display.update()

	
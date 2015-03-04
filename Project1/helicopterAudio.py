"""Helicopter Game
Keenan Zucker and Scott Mackinlay"""


import alsaaudio
import audioop
import pygame
from pygame.locals import *
import random
import time
import sys

def main():

	pygame.init()

	width = 640
	height = 480

	black = (0,0,0)
	white = (250,250,250)

	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Is It....Helicopter?')    

	background = pygame.Surface(screen.get_size())
	background = background.convert()

	inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,0)
	inp.setchannels(1)
	inp.setrate(16000)
	inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
	inp.setperiodsize(160)
	l,data = inp.read()

	i = 0
	while i < 10:
		if l:
			print audioop.rms(data,2)

		audio = audioop.rms(data,2)
		background.fill(white)
		drawCopter(audio, screen)
		pygame.display.update()

def drawCopter(audio, screen):

	widthR = 20
	heightR = 20

	pygame.draw.rect(screen, (100,200,50), (100, 480 - audio, widthR, heightR))



main()

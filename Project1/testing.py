"""Testing Space for Helicopter Game"""

import pygame
from pygame.locals import *
import random
import time


def main():

	pygame.init()

	width = 640
	height = 480

	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Is It....Helicopter?')


	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((100,100,200))

	# Display some text
	font = pygame.font.Font(None, 36)
	text = font.render("Hello There", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()

	# Event loop
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

		screen.blit(background, (0, 0))
		pygame.display.flip()



if __name__ == '__main__':
	main()
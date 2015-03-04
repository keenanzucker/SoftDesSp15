""" A Version of the Classic Game Helicopter -- by Scott & Keenan """

import pygame
import random
import time


class HelicopterModel():

	def __init__(self, width, height):
		self.width = width
        self.height = height
        self.helicopter = Helicopter(0, height/2.0)
        self.background = Background(width, height)

	def get_player(self):
		"""returns the current helicopter"""
    	return self.helicopter

class DrawableSurface():
    """ A class that wraps a pygame.Surface and a pygame.Rect """

    def __init__(self, surface, rect):
        """ Initialize the drawable surface """
        self.surface = surface
        self.rect = rect

    def get_surface(self):
        """ Get the surface """
        return self.surface

    def get_rect(self):
        """ Get the rect """
        return self.rect


class Background():

	def __init__(self, screenWidth, screenHeight):
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

class Helicopter():
	"""docstring for Helicopter"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

		#sefl.velX = 10

class HelicopterView():

	def __init__(self, model, width, height):
		pygame.init()
        # to retrieve width and height use screen.get_size()
        self.screen = pygame.display.set_mode((width, height))
        self.screen_boundaries = pygame.Rect(0 ,0, width, height)
        # this is used for figuring out where to draw stuff
        self.model = model
	
	def draw(self):
		self.screen.fill((0,41,205))
		self.model.Background.draw(self.screen)

class HelicopterGame():

	def __init__(self):
		self.model = HelicopterModel(self, 640, 480)
		self.view = HelicopterView(self.model, 640, 480)
		#self.controller = 

	def run(self):
		self.view.draw()

if __name__ == '__main__':
    game = HelicopterGame()
    game.run()
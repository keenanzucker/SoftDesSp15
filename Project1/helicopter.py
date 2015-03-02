""" A Version of the Classic Game Helicopter -- by Scott & Keenan """

import pygame
import random
import time


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

class HelicopterModel():

	def __init__(self, width, height):
		self.width = width
        self.height = height

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
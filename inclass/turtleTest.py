"""Turtle World"""

from swampy.TurtleWorld import *

world = TurtleWorld()
beth = Turtle()
beth.delay=0.0000001
#beth.delay = 0.001

def drawLine(turtle, angle, startX, startY, lineLength):
	"""Draws a line with specific turtle, starting point, angle, and length"""
	turtle.x = startX
	turtle.y = startY
	turtle.heading = angle
	turtle.fd(lineLength)



def mySquare(startX, startY, side):
	beth.x = startX
	beth.y = startY
	beth.lt()

	for i in range (0, 4):
		beth.fd(side)
		beth.rt()

def funStuff(startX, startY, lengthL):
	beth.x = startX
	beth.y = startY
	angle = 0
	for i in range (0, lengthL):
		beth.fd(10)
		beth.lt(angle)
		angle+=0.1

"""
def sumOfNumbers(n):

	if n == 0:
		return 0

	return n + sumOfNumbers(n-1)

def factorial(n):
	if n == 1:
		return 1

	return n * factorial(n-1)
"""





def snow_flake_side(turtle, length, level):
	
	scott = turtle

	if level == 0:
		scott.fd(length/3.0)
		scott.rt(60.0)
		scott.fd(length/3.0)
		scott.lt(120.0)
		scott.fd(length/3.0)
		scott.rt(60.0)
		scott.fd(length/3.0)
	else:
		snow_flake_side(scott, length/3, level -1)
		scott.rt(60.0)
		snow_flake_side(scott, length/3, level -1)
		scott.lt(120.0)
		snow_flake_side(scott, length/3, level -1)
		scott.rt(60.0)
		snow_flake_side(scott, length/3, level -1)

for i in range(36):
	snow_flake_side(beth, 500, 4)
	beth.rt(110)


wait_for_user()




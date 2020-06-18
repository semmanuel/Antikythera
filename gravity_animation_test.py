#
# testing gravity simulation in pygame
# src: adapted from 'Nature of Code' by Daniel Shiffman
#

############################## file set up
import pygame
from random import *
import numpy as np
from datetime import datetime

# initiate pygame and clock
pygame.init()
clock = pygame.time.Clock()

# gravitational constant
g = 0.4

# set up colors:
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# set up surface plane
surface = pygame.display.set_mode((600, 600))  # ((width, height))
pygame.display.set_caption('animation test')

surface.fill(BLACK)


############################## celestial body object
class Body(object):
	def __init__(self, m, x, y, c):
		# mass, postion (x, y), color
		self.mass = m
		self.position = np.array([x,y])
		self.last_position = np.array([x,y])
		self.velocity = np.array([0, 0])
		self.accel = np.array([0, 0])
		self.color = c

	def applyForce(self, force):
		# apply forces to a body
		f = force / self.mass
		self.accel = np.add(self.accel, f)

	def update(self):
		# update position based on velocity and reset accel
		self.velocity = np.add(self.velocity, self.accel)
		self.last_position = self.position
		self.position = np.add(self.position, self.velocity)
		self.accel = 0

	def display(self):
		# draw over old object location
		pygame.draw.circle(surface, BLACK, (int(self.last_position[0]), int(self.last_position[1])), 10)  # (drawLayer, color, (coordinates), radius)

		# draw trail (Comment this line out to remove trails)
		pygame.draw.circle(surface, RED, (int(self.last_position[0]), int(self.last_position[1])), 10)  # (drawLayer, color, (coordinates), radius)

		# draw new object location
		pygame.draw.circle(surface, self.color, (int(self.position[0]), int(self.position[1])), 10)  # (drawLayer, color, (coordinates), radius)
		#print("x:" + str(self.position[0]) + " ,  y:" + str(self.position[1]) )

	def attract(self, m, g):
		# gravitational code rewritten from Daniel Shiffman's "Nature of Code"
		force = self.position - m.position
		distance = np.linalg.norm(force)
		distance = constrain(distance, 5.0, 25.0)
		force = normalize(force)
		strength = (g * self.mass * m.mass)/float(distance * distance)
		force = force * strength
		return force

############################## set up and draw
def setup():
	# sun
	body1 = Body(100, 300, 300, YELLOW)

	#planets
	body2 = Body(10, randint(0,600), randint(0,600), BLUE)
	body3 = Body(5, randint(0,600), randint(0,600), BLUE)
	body4 = Body(1, randint(0,600), randint(0,600), BLUE)
	body5 = Body(8, randint(0,600), randint(0,600), BLUE)

	# list of all bodies in universe
	global bodies
	bodies = [body1, body2, body3, body4, body5]

	return

def draw():

	# for each body: apply forces, update position, and draw
	for body in bodies:
		for other_body in bodies:
			if (body != other_body):
				global g
				force = other_body.attract(body, g)
				body.applyForce(force)
		body.update()
		body.display()
	return


############################## mathematical functions

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def normalize(force):
	normal = np.linalg.norm(force, ord=1)
	if normal == 0:
		normal = np.finfo(force.dtype).eps
	return force/normal

############################## main loop


if __name__ == "__main__":
	# initial set up
	setup()
	while True:
		# draw bodies to screen
		draw()
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				run = False
		pygame.display.update()

#
# Body.py
# Class file for the celestial bodies.
#

import math
import pygame
from random import *
import numpy as np
#from database_creation.database_antikythera import *

# set up colors:


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

############################## celestial body object
class Body(object):
    def __init__(self, m, x, y, r, c, s, root, tr, theta):
        # mass, position (x, y), color
        self.mass = m
        self.position = np.array([x, y])
        self.last_position = np.array([x-1, y-1])
        self.velocity = np.array([randint(10,15), randint(10,15)])
        self.accel = np.array([0,0])
        self.color = c
        self.radius = r
        self.sun = s
        self.surface = root
        self.trails = tr
        self.sunDistance = math.sqrt((self.position[0] - 800)**2 + (self.position[1] - 400)**2)
        self.theta = theta

    def applyForce(self, force):
        # apply forces to a body
        f = force / self.mass
        self.accel = np.add(self.accel, f)


    def display(self, zoomed):
        # draw over old object location
        pygame.draw.circle(self.surface, BLACK, (int(self.last_position[0]), int(self.last_position[1])), self.radius)  	# (drawLayer, color, (coordinates), radius)

        # draw trail (Comment this line out to remove trails)
        if self.trails:
            if not zoomed:
                pygame.draw.line(self.surface, self.color, (int(self.last_position[0]), int(self.last_position[1])), (int(self.position[0]), int(self.position[1])), 5)
        # draw new object location
        pygame.draw.circle(self.surface, self.color, (int(self.position[0]), int(self.position[1])), self.radius)


    def attract(self, m, g):
        # gravitational code rewritten from Daniel Shiffman's "Nature of Code"
        force = self.position - m.position
        distance = np.linalg.norm(force)
        distance = constrain(distance, 5.0, 25.0)
        force = normalize(force)
        strength = (g * self.mass * m.mass) / float(distance * distance)
        force = force * strength
        return force


    def printData(self):
        if(self.name == "Sun"):
             print("\n\n\n\n\n\n\n===============================")
             print("Name: " + str(self.name))
             print("Mass: " + str(self.mass))
             print("Volume: " + str(self.volume))
             print("Position: " + str(self.position))
             print("Radius: " + str(self.radius))
             print("Surface Gravity: " + str(self.surface_gravity))
             print("Mean Density: " + str(self.mean_density))
             print("Effective Temperature: " + str(self.effective_tmp))
             print("===============================")
        else:
             print("\n\n\n\n\n===============================")
             print("Name: " + str(self.name))
             print("Mass: " + str(self.mass))
             print("Volume: " + str(self.volume))
             print("Position: " + str(self.position))
             print("Diameter: " + str(self.diameter))
             print("Velocity: " + str(self.orbital_velocity))
             print("Distance from Sun: " + str(self.distance_from_sun))
             print("Density: " + str(self.density))
             print("Surface Gravity: " + str(self.gravity))
             print("Mean Temperature: " + str(self.mean_temperature))
             print("Number of Moons: " + str(self.number_of_moons))
             print("===============================")

        return

    def eclipseCheck(self, body2, sun):
        col = math.isclose(np.cross(self.position - sun.position, body2.position - sun.position), 0, abs_tol=25)
        if self.sunDistance > body2.sunDistance:
            betweenx = self.position[0] <= body2.position[0] <= sun.position[0] or sun.position[0] <= body2.position[0] <= self.position[0]
            betweeny = self.position[1] <= body2.position[1] <= sun.position[1] or sun.position[1] <= body2.position[1] <= self.position[1]
        else:
            betweenx = body2.position[0] <= self.position[0] <= sun.position[0] or sun.position[0] <= self.position[0] <= body2.position[0]
            betweeny = body2.position[1] <= self.position[1] <= sun.position[1] or sun.position[1] <= self.position[1] <= body2.position[1]
        return (col and (betweenx if self.position[0] != sun.position[0] else betweeny))


############################## mathematical functions

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


def normalize(force):
    normal = np.linalg.norm(force, ord=1)
    if normal == 0:
        normal = np.finfo(force.dtype).eps
    return force / normal


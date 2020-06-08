#
# GUI_test.py
#
# This file is for GUI testing and practice with the PyGame library.
#

import pygame
import sys
from pygame.locals import *
import random


# set up pygame
pygame.init()

# set up window
space = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('antikythera')

# set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# draw background
space.fill(BLACK)

# draw temporary sun in center of screen
pygame.draw.circle(space, YELLOW, (400, 300), 10)

# draw window onto the screen
pygame.display.update()

#############################
# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

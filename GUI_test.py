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
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('Consolas', 20)


# set up window
space = pygame.display.set_mode((800, 600))     # ((width, height))
pygame.display.set_caption('antikythera')


# set up colors:
# (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)


# draw background
space.fill(BLACK)


# draw temporary sun in center of screen:
pygame.draw.circle(space, YELLOW, (400, 300), 10)   # (drawLayer, color, (coordinates), radius)


# draw three buttons and their click-able regions
button1 = pygame.Rect(20, 10, 200, 50)
pygame.draw.rect(space, GRAY, button1)
button1surface = game_font.render('Search 1', True, (0, 0, 0))

button2 = pygame.Rect(300, 10, 200, 50)
pygame.draw.rect(space, GRAY, button2)
button2surface = game_font.render('Search 2', True, (0, 0, 0))

button3 = pygame.Rect(590, 10, 200, 50)
pygame.draw.rect(space, GRAY, button3)
button3surface = game_font.render('Search 3', True, (0, 0, 0))

space.blit(button1surface,(30,25))
space.blit(button2surface,(310,25))
space.blit(button3surface,(600,25))


# draw window onto the screen
pygame.display.update()


#############################
# main loop
while True:
    for event in pygame.event.get():
        # check for exit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # buttons being pressed -> activating functions
            if button1.collidepoint(mouse_pos):
                print('button1 pressed')
            if button2.collidepoint(mouse_pos):
                print('button2 pressed')
            if button3.collidepoint(mouse_pos):
                print('button3 pressed')

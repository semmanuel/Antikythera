#
# GUI_test.py
#
# This file is for GUI testing and practice with the PyGame library.
#

import pygame
import sys
import numpy
from pygame.locals import *
import random
from datetime import date


# set up pygame
pygame.init()
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('Consolas', 20)
HEIGHT = 600
WIDTH = 800

# set up window
space = pygame.display.set_mode((WIDTH, HEIGHT))  # ((width, height))
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
pygame.draw.circle(space, YELLOW, (400, 300), 10)  # (drawLayer, color, (coordinates), radius)

############################# draw menu buttons
# search objects
search_object_button = pygame.Rect(20, 10, 200, 50)  # (top, bottom, width, length)
pygame.draw.rect(space, GRAY, search_object_button)
search_object_button_surface = game_font.render('SEARCH OBJECTS', True, (0, 0, 0))  # ('text', anti-alias, (color)))
space.blit(search_object_button_surface, (40, 25))

# search events
search_event_button = pygame.Rect(300, 10, 200, 50)
pygame.draw.rect(space, GRAY, search_event_button)
search_event_button_surface = game_font.render('SEARCH EVENTS', True, (0, 0, 0))
space.blit(search_event_button_surface, (330, 25))

# calculate launch
calc_launch_button = pygame.Rect(590, 10, 200, 50)
pygame.draw.rect(space, GRAY, calc_launch_button)
calc_launch_button_surface = game_font.render('CALCULATE LAUNCH', True, (0, 0, 0))
space.blit(calc_launch_button_surface, (600, 25))

# trails activate/deactivate
trails_button = pygame.Rect(20, 70, 100, 50)
pygame.draw.rect(space, GRAY, trails_button)
trails_button_surface = game_font.render('TRAILS', True, (0, 0, 0))
space.blit(trails_button_surface, (35, 85))

# exit button
exit_button = pygame.Rect(690, 540, 100, 50)
pygame.draw.rect(space, GRAY, exit_button)
exit_button_surface = game_font.render('EXIT', True, (0, 0, 0))
space.blit(exit_button_surface, (710, 560))

# zoom slider
zoom_slider = pygame.Rect(700, 100, 100, 400)
pygame.draw.rect(space, WHITE, zoom_slider)

# date display
today = date.today()
current_date = today.strftime("%b-%d-%Y")   # current date
date_button = pygame.Rect(95, 540, 300, 50)
pygame.draw.rect(space, GRAY, date_button)
date_button_surface = game_font.render(current_date, True, (0, 0, 0))
space.blit(date_button_surface, (180, 560))

# forward time travel
f_timetravel_button = pygame.Rect(420, 540, 50, 50)
pygame.draw.rect(space, GRAY, f_timetravel_button)
f_timetravel_button_surface = game_font.render("  +  ", True, (0, 0, 0))
space.blit(f_timetravel_button_surface, (420, 560))

# backward time travel
b_timetravel_button = pygame.Rect(20, 540, 50, 50)
pygame.draw.rect(space, GRAY, b_timetravel_button)
b_timetravel_button_surface = game_font.render("  -  ", True, (0, 0, 0))
space.blit(b_timetravel_button_surface, (20, 560))


#################### draw window onto the screen
pygame.display.update()


#############################
# functions
def zoom_holding():
    global mouse_held, zoom_level
    if mouse_held:
        _, zoom_level = pygame.mouse.get_pos()  # ignore x value of mouse coord, save y
        return zoom_level


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
            mouse_held = True

            # search object button
            if search_object_button.collidepoint(mouse_pos):
                print('search1 pressed')
            # search event button
            if search_event_button.collidepoint(mouse_pos):
                print('search2 pressed')
            # calculate launch button
            if calc_launch_button.collidepoint(mouse_pos):
                print('calculate transfer pressed')
            # trails activate/deactivate
            if trails_button.collidepoint(mouse_pos):
                print('trails activated')
            # exit button
            if exit_button.collidepoint(mouse_pos):
                print("Exiting...")
                pygame.quit()
                sys.exit()
            if zoom_slider.collidepoint(mouse_pos):
                print("zoom click")
            # date pause/resume
            if date_button.collidepoint(mouse_pos):
                print('pause/resume time')
            # f time travel
            if f_timetravel_button.collidepoint(mouse_pos):
                print('ff time travel!')
            # b time travel
            if b_timetravel_button.collidepoint(mouse_pos):
                print('!levart emit sdrawkcab')

            # scrolling
            # if event.button == 4:
            #     print("scroll up")
            # elif event.button == 5:
            #     print("scroll down")

        if event.type == MOUSEBUTTONUP:
            mouse_held = False

#
# GUI.py
# Putting both the UI menu and animation tests together.
#

############################## file set up
import pygame
from pygame.locals import *
import random, sys, time
from random import *
import numpy as np
from datetime import date



# initiate pygame and clock
pygame.init()
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('consolas', 20)

# dimensions
WIDTH = 800
HEIGHT = 600

# value for gravity equation
g = 0.4

# set up colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

# set up surface plane
space = pygame.display.set_mode((WIDTH, HEIGHT))  # ((width, height))
pygame.display.set_caption('antikythera pre-alpha')
space.fill(BLACK)

# trails
global trails_active
trails_active = False

############################ CREATE and draw buttons first time
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
current_date = today.strftime("%b-%d-%Y")  # current date
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
pygame.display.update()


############################## celestial body object
class Body(object):
    def __init__(self, m, x, y, r, c):
        # mass, postion (x, y), color
        self.mass = m
        self.position = np.array([x, y])
        self.last_position = np.array([x, y])
        self.velocity = np.array([0, 0])
        self.accel = np.array([randint(-1,1), randint(-1,1)])
        self.color = c
        self.radius = r

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
        pygame.draw.circle(space, BLACK, (int(self.last_position[0]), int(self.last_position[1])), self.radius)  	# (drawLayer, color, (coordinates), radius)

        # draw trail (Comment this line out to remove trails)
        if trails_active == True:
            pygame.draw.line(space, RED, (int(self.last_position[0]), int(self.last_position[1])), (int(self.position[0]), int(self.position[1])), 5)

        # draw new object location
        pygame.draw.circle(space, self.color, (int(self.position[0]), int(self.position[1])), self.radius)


    def attract(self, m, g):
        # gravitational code rewritten from Daniel Shiffman's "Nature of Code"
        force = self.position - m.position
        distance = np.linalg.norm(force)
        distance = constrain(distance, 5.0, 25.0)
        force = normalize(force)
        strength = (g * self.mass * m.mass) / float(distance * distance)
        force = force * strength
        return force


############################## set up and draw
def setup():
    # sun
    body1 = Body(1000, WIDTH/2, HEIGHT/2, 10, YELLOW)

    # planets
    body2 = Body(randint(0, 10), randint(0, WIDTH), randint(0, HEIGHT), 5, BLUE)
    body3 = Body(randint(0, 10), randint(0, WIDTH), randint(0, HEIGHT), 5, BLUE)
    body4 = Body(randint(0, 10), randint(0, WIDTH), randint(0, HEIGHT), 5, BLUE)
    body5 = Body(randint(0, 10), randint(0, WIDTH), randint(0, HEIGHT), 5, BLUE)

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

    ############################# RE-draw menu buttons
    # search objects
    pygame.draw.rect(space, GRAY, search_object_button)
    space.blit(search_object_button_surface, (40, 25))
    # search events
    pygame.draw.rect(space, GRAY, search_event_button)
    space.blit(search_event_button_surface, (330, 25))
    # calculate launch
    pygame.draw.rect(space, GRAY, calc_launch_button)
    space.blit(calc_launch_button_surface, (600, 25))
    # trails activate/deactivate
    pygame.draw.rect(space, GRAY, trails_button)
    space.blit(trails_button_surface, (35, 85))
    # exit button
    pygame.draw.rect(space, GRAY, exit_button)
    space.blit(exit_button_surface, (710, 560))
    # zoom slider
    pygame.draw.rect(space, WHITE, zoom_slider)
    # date display
    pygame.draw.rect(space, GRAY, date_button)
    space.blit(date_button_surface, (180, 560))
    # forward time travel
    pygame.draw.rect(space, GRAY, f_timetravel_button)
    space.blit(f_timetravel_button_surface, (420, 560))
    # backward time travel
    pygame.draw.rect(space, GRAY, b_timetravel_button)
    space.blit(b_timetravel_button_surface, (20, 560))
    pygame.display.update()

    return


############################## mathematical functions

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


def normalize(force):
    normal = np.linalg.norm(force, ord=1)
    if normal == 0:
        normal = np.finfo(force.dtype).eps
    return force / normal


############################## main loop


if __name__ == "__main__":
    # initial set up
    setup()
    while True:
        # render screen
        draw()

        # event handler
        for event in pygame.event.get():
            # exit program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # click mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # trails button
                if trails_button.collidepoint(mouse_pos):
                    print("trails button pushed")
                    if trails_active == True:
                        trails_active = False
                        space.fill(BLACK)
                    else:
                        trails_active = True

                if search_object_button.collidepoint(mouse_pos):
                    print('search1 pressed')
                # search event button
                if search_event_button.collidepoint(mouse_pos):
                    print('search2 pressed')
                # calculate launch button
                if calc_launch_button.collidepoint(mouse_pos):
                    print('calculate transfer pressed')

                # exit button
                if exit_button.collidepoint(mouse_pos):
                    print("Exiting...")
                    pygame.quit()
                    sys.exit()

               # zoom bar
                if zoom_slider.collidepoint(mouse_pos):
                    print("zoom bar click")
                # date pause/resume
                if date_button.collidepoint(mouse_pos):
                    print('pause/resume time')
                # f time travel
                if f_timetravel_button.collidepoint(mouse_pos):
                    print('forward time travel!')
                # b time travel
                if b_timetravel_button.collidepoint(mouse_pos):
                    print('!levart emit sdrawkcab')

        # update GUI and wait
        pygame.display.update()
        time.sleep(0.05)

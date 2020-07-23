#
# main.py
# Main python file to run project.
#

############################## file set up
import sys, time

import sqlite3
import numpy as np
from GUI import *
from Body import *

############ database set up
database = sqlite3.connect('celestial_objects.db')
cursor = database.cursor()


# trails
trails_active = False

# value for gravity equation
g = 0.4

# dimensions
WIDTH = 1600
HEIGHT = 800

# set up colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

############################## set up and draw
def setup():
    # sun
    # Body(mass, x-position, y-position, radius, color, sun, root, trails)
    the_sun = Body('Sun', 1000, WIDTH/2, HEIGHT/2, 10, YELLOW, True, gui.space, trails_active)

    # planets
    # Body(name, mass, x-position, y-position, radius, color, sun, root, trails)
    mercury = Body('Mercury', randint(0, 10), randint(0, WIDTH), randint(0, HEIGHT), 5, GREEN, False, gui.space, trails_active)
    venus = Body('Venus', randint(10, 20), randint(0, WIDTH), randint(0, HEIGHT), 5, YELLOW, False, gui.space, trails_active)
    earth = Body('Earth', randint(20, 30), randint(0, WIDTH), randint(0, HEIGHT), 5, BLUE, False, gui.space, trails_active)
    mars = Body('Mars', randint(30, 40), randint(0, WIDTH), randint(0, HEIGHT), 5, RED, False, gui.space, trails_active)
    jupiter = Body('Jupiter', randint(40, 50), randint(0, WIDTH), randint(0, HEIGHT), 5, YELLOW, False, gui.space, trails_active)
    saturn = Body('Saturn', randint(50, 60), randint(0, WIDTH), randint(0, HEIGHT), 5, GREEN, False, gui.space, trails_active)
    uranus = Body('Uranus', randint(60, 70), randint(0, WIDTH), randint(0, HEIGHT), 5, RED, False, gui.space, trails_active)
    neptune = Body('Neptune', randint(70, 90), randint(0, WIDTH), randint(0, HEIGHT), 5, BLUE, False, gui.space, trails_active)

    # list of all bodies in universe
    global bodies
    bodies = [the_sun, earth, mars, mercury, venus, jupiter, saturn, uranus, neptune]
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
    gui.drawMenu()
    pygame.display.update()
    return


############################## menu printing
#### search events
def searchEventMenu():
    running = True
    while (running):
        print("===========================================")
        print(" SEARCH DATABASE FOR CELESTIAL EVENTS")
        print("===========================================")
        print(" [ 1 ] to Search for Event Type A")
        print(" [ 2 ] to Search for Event Type B")
        print(" [ 3 ] to Search for Event Type C")
        print(" [ 4 ] to Search for Event Type D")
        print(" [ 0 ] to Exit Search Menu")
        print("===========================================")
        eventSelect = int(input())
        if eventSelect == 0:
            print("Exiting....\n\n")
            running = False
            break
        elif eventSelect == 1:
            # search and print results\
            print("Searching...\n\n")
        elif eventSelect == 2:
            # search and print results\
            print("Searching...\n\n")
        elif eventSelect == 3:
            # search and print results\
            print("Searching...\n\n")
        elif eventSelect == 4:
            # search and print results\
            print("Searching...\n\n")
        else:
            print("ERROR....\n\n")
    return


#### search celestial bodies
def searchBodyMenu():
    running = True
    while (running):
        print("===========================================")
        print(" SEARCH DATABASE FOR CELESTIAL BODIES")
        print("===========================================")
        print(" [ 1 ] to Search for Body Type A")
        print(" [ 2 ] to Search for Body Type B")
        print(" [ 3 ] to Search for Body Type C")
        print(" [ 4 ] to Search for Body Type D")
        print(" [ 0 ] to Exit Search Menu")
        print("===========================================")
        eventSelect = int(input())
        if eventSelect == 0:
            print("Exiting....\n\n")
            running = False
            break
        elif eventSelect == 1:
            # search and print results\
            print("Searching...\n\n")
        elif eventSelect == 2:
            # search and print results\
            print("Searching...\n\n")
        elif eventSelect == 3:
            # search and print results\
            print("Searching...\n\n")
        elif eventSelect == 4:
            # search and print results\
            print("Searching...\n\n")
        else:
            print("ERROR....\n\n")
    return

def searchTransferwindow():

    Object1 = input('Enter the origin planet: ')
    Object2 = input('Enter the destination planet: ')

    ##### Getting the required information from the database
    cursor.execute("""SELECT distance_from_sun FROM Planets WHERE planet = '%s'""" % Object1)
    object1 = [row[0] for row in cursor.fetchall()]
    distance1 = float(object1[0])

    cursor.execute("""SELECT distance_from_sun FROM Planets WHERE planet = '%s'""" % Object2)
    object2 = [row[0] for row in cursor.fetchall()]
    distance2 = float(object2[0])

    cursor.execute("""SELECT orbital_period FROM Planets WHERE planet = '%s'""" % Object1)
    object1 = [row[0] for row in cursor.fetchall()]
    orbital1 = object1[0]

    cursor.execute("""SELECT orbital_period FROM Planets WHERE planet = '%s'""" % Object2)
    object2 = [row[0] for row in cursor.fetchall()]
    orbital2 = object2[0]

    transferwindow(distance1 * 10 ** 6, distance2 * 10 ** 6, orbital1, orbital2)

############################## main loop


if __name__ == "__main__":
    # initiate pygame and clock
    pygame.init()
    pygame.display.set_caption('antikythera alpha')
    clock = pygame.time.Clock()

    gui = GUI(WIDTH, HEIGHT)

    time_scale = 1

    # initial set up
    setup()
    while True:
        # while pause not pressed, draw and update screen
        gui.drawMenu()
        for body in bodies:
            body.display()

        if gui.pause == False:
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
                if gui.trails_button.collidepoint(mouse_pos):
                    for body in bodies:
                        if body.trails == True:
                            body.trails = False
                            gui.space.fill(BLACK)
                        else:
                            body.trails = True

                # search object button
                if gui.search_object_button.collidepoint(mouse_pos):
                    searchBodyMenu()

                # search event button
                if gui.search_event_button.collidepoint(mouse_pos):
                    searchEventMenu()

                # calculate launch button
                if gui.calc_launch_button.collidepoint(mouse_pos):
                    searchTransferwindow()

                # exit button
                if gui.exit_button.collidepoint(mouse_pos):
                    print("Exiting...")
                    pygame.quit()
                    sys.exit()

                # date pause/resume
                if gui.date_button.collidepoint(mouse_pos):
                    gui.pause = not gui.pause

                # f time travel
                if gui.f_timetravel_button.collidepoint(mouse_pos):
                    time_scale = time_scale / 1.25

                # b time travel
                if gui.b_timetravel_button.collidepoint(mouse_pos):
                    time_scale = time_scale * 1.25

            # hover
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = np.array(event.pos)
                for body in bodies:
                    # if mouse within certain distance (varied by atol), print body name to console
                    if np.isclose(body.position, mouse_pos, atol=10).all():
                        body.printData()

        # update GUI and wait
        pygame.display.update()
        time.sleep(0.05 * time_scale)

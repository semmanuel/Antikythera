#
# main.py
# Main python file to run project.
#

############################## file set up
import sys, time
import numpy as np
from GUI import *
from Body import *


# trails
trails_active = False

# value for gravity equation
g = 0.4

# dimensions
WIDTH = 800
HEIGHT = 600

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
    # Body(mass, x-position, y-position, radius, color, sun, root, trails)
    earth = Body('Earth', randint(0, 10), randint(0, WIDTH), randint(0, HEIGHT), 5, BLUE, False, gui.space, trails_active)
    mars = Body('Mars', randint(0, 10), randint(0, WIDTH), randint(0, HEIGHT), 5, RED, False, gui.space, trails_active)
    mercury = Body('Mercury', randint(0, 10), randint(0, WIDTH), randint(0, HEIGHT), 5, GREEN, False, gui.space, trails_active)
    venus = Body('Venus', randint(0, 10), randint(0, WIDTH), randint(0, HEIGHT), 5, YELLOW, False, gui.space, trails_active)


    # list of all bodies in universe
    global bodies
    bodies = [the_sun, earth, mars, mercury, venus]
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
        print(" [ 1 ] to to Search for Event Type A")
        print(" [ 2 ] to to Search for Event Type B")
        print(" [ 3 ] to to Search for Event Type C")
        print(" [ 4 ] to to Search for Event Type D")
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
        print(" [ 1 ] to to Search for Body Type A")
        print(" [ 2 ] to to Search for Body Type B")
        print(" [ 3 ] to to Search for Body Type C")
        print(" [ 4 ] to to Search for Body Type D")
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
                    print('calculate transfer pressed')

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

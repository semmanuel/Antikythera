import sys, time, os

import sqlite3
import numpy as np
from GUI import *
from Body import *
from Transferwindow import *

#modules from the database_creation directory
from database_creation.database_antikythera import *
from  database_creation.create_db import create_db

############ database set up################################

#changing work directory, to work from database_creation directory
os.chdir('../Antikythera\database_creation')
path_database_creation=os.getcwd()

#create every database needed.
create_db()

print(path_database_creation+'\Stars.db')
database = sqlite3.connect(path_database_creation+r'/celestial_objects.db')
cursor = database.cursor()

database1 = sqlite3.connect(path_database_creation+r'\Stars.db')
cursor1 = database1.cursor()

database2 = sqlite3.connect(path_database_creation+r'\Asteroid_orbit.db')
cursor2 = database2.cursor()

database3 = sqlite3.connect(path_database_creation+r'\solar_eclipse.db')
cursor3 = database3.cursor()

database4 = sqlite3.connect(path_database_creation+r'\near_earth_comets.db')
cursor4 = database4.cursor()

database5 = sqlite3.connect(path_database_creation+r'\celestial_events.db')
cursor5 = database5.cursor()

# trails
trails_active = False

# value for gravity equation
g = 0.4

zoom_level = 1
speed_scale = 100

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
    # Body(mass, x-position, y-position, radius, color, sun, root, trails, theta)
    the_sun = Star.create_star('Sun', 1000, WIDTH/2, HEIGHT/2, 10, YELLOW, True, gui.space, trails_active, 0)

    # planets
    # Body(name, mass, x-position, y-position, radius, color, sun, root, trails)
    mercury = CelestialBody.create_planet('Mercury', np.random.randint(0, 10), np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT), 5, GREEN, False, gui.space, trails_active, np.random.random_sample())
    venus = CelestialBody.create_planet('Venus', np.random.randint(10, 20), np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT), 5, YELLOW, False, gui.space, trails_active, np.random.random_sample())
    earth = CelestialBody.create_planet('Earth', np.random.randint(20, 30), np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT), 5, BLUE, False, gui.space, trails_active, np.random.random_sample())
    mars = CelestialBody.create_planet('Mars', np.random.randint(30, 40), np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT), 5, RED, False, gui.space, trails_active, np.random.random_sample())
    jupiter = CelestialBody.create_planet('Jupiter', np.random.randint(40, 50), np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT), 5, YELLOW, False, gui.space, trails_active, np.random.random_sample())
    saturn = CelestialBody.create_planet('Saturn', np.random.randint(50, 60), np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT), 5, GREEN, False, gui.space, trails_active, np.random.random_sample())
    uranus = CelestialBody.create_planet('Uranus', np.random.randint(60, 70), np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT), 5, RED, False, gui.space, trails_active, np.random.random_sample())
    neptune = CelestialBody.create_planet('Neptune', np.random.randint(70, 90), np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT), 5, BLUE, False, gui.space, trails_active, np.random.random_sample())

    # list of all bodies in universe
    global bodies
    bodies = [the_sun, earth, mars, mercury, venus, jupiter, saturn, uranus, neptune]
    return


def draw():
    # for each body: apply forces, update position, and draw
    for body in bodies:
        #### physics based motion
        # for other_body in bodies:
        #     if (body != other_body):
        #         global g
        #         force = other_body.attract(body, g)
        #         body.applyForce(force)
        if isinstance(body, CelestialBody):
            #### orbital motion
            body.update(zoom_level, speed_scale) # (distance_scaling, velocity_scaling))
        body.display(zoomed)

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
        print(" [ 1 ] to Search for Asteroids")
        print(" [ 2 ] to Search for Lunar Eclipse")
        print(" [ 3 ] to Search for Solar Eclipse")
        print(" [ 0 ] to Exit Search Menu")
        print("===========================================")
        eventSelect = int(input())
        if eventSelect == 0:
            print("Exiting....\n\n")
            running = False
            break
        elif eventSelect == 1:
            # search and print results\
            y = 1
            cursor2.execute("""SELECT DISTINCT `Object Classification` FROM `Asteroid Orbits`""")
            query_result = [row[0] for row in cursor2.fetchall()]
            for i in query_result:
                print(y, '.', i)
                y += 1

            choice = input('Do you want to see specific asteroids in a category?\n1.Yes\n2.No')
            choice = int(choice)
            if choice == 1:
                number = input('Enter number of asteroid category you want to see: ')
                number = int(number)

                cursor2.execute("""SELECT `Object Name` FROM `Asteroid Orbits` WHERE `Object Classification` = '%s' """ % (query_result[number - 1]))
                query_result1 = [row[0] for row in cursor2.fetchall()]
                for i in query_result1:
                    print(i)

        elif eventSelect == 2:
            # search and print results\
            year = input('Enter the year you wanna search for a Lunar Eclipse: ')
            cursor5.execute("""SELECT `Calendar Date`, `Eclipse Type` FROM `Lunar Eclipse` WHERE `Calendar Date` LIKE ?""",(year + ' %',))
            query_result1 = cursor5.fetchall()
            for i in query_result1:
                print(i)
        elif eventSelect == 3:
            # search and print results\
            year = input('Enter the year you wanna search for a Solar Eclipse: ')
            cursor3.execute("""SELECT `Calendar Date`, `Eclipse Type` FROM `Solar Eclipse` WHERE `Calendar Date` LIKE ?""",(year + ' %',))
            query_result1 = cursor3.fetchall()
            for i in query_result1:
                print(i)
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
        print(" [ 1 ] to Search for Planets")
        print(" [ 2 ] to Search for Stars")
        print(" [ 3 ] to Search for Comets")
        print(" [ 0 ] to Exit Search Menu")
        print("===========================================")
        eventSelect = int(input())
        if eventSelect == 0:
            print("Exiting....\n\n")
            running = False
            break
        elif eventSelect == 1:
            # search and print results\
            cursor.execute("""SELECT planet from celestial_objects""")
            query_result = [row[0] for row in cursor.fetchall()]
            for i in query_result:
                print(i)

        elif eventSelect == 2:
            # search and print results\
            cursor1.execute("""SELECT Star from Stars WHERE Star != 'None'""")
            query_result = [row[0] for row in cursor1.fetchall()]
            for i in query_result:
                print(i)

        elif eventSelect == 3:
            # search and print results\
            cursor4.execute("""SELECT Object, Epoch FROM Comets """)
            query_result = cursor4.fetchall()
            for i in query_result:
                print(i)

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
    cursor.execute("""SELECT distance_from_sun FROM celestial_objects WHERE planet = '%s'""" % Object1)
    object1 = [row[0] for row in cursor.fetchall()]
    distance1 = float(object1[0])

    cursor.execute("""SELECT distance_from_sun FROM celestial_objects WHERE planet = '%s'""" % Object2)
    object2 = [row[0] for row in cursor.fetchall()]
    distance2 = float(object2[0])

    cursor.execute("""SELECT orbital_period FROM celestial_objects WHERE planet = '%s'""" % Object1)
    object1 = [row[0] for row in cursor.fetchall()]
    orbital1 = object1[0]

    cursor.execute("""SELECT orbital_period FROM celestial_objects WHERE planet = '%s'""" % Object2)
    object2 = [row[0] for row in cursor.fetchall()]
    orbital2 = object2[0]

    transferwindow(distance1 * 10 ** 6, distance2 * 10 ** 6, orbital1, orbital2)

############################## main loop


if __name__ == "__main__":
    # initiate pygame and clock
    pygame.init()
    pygame.display.set_caption('antikythera beta')
    clock = pygame.time.Clock()
    gui = GUI(WIDTH, HEIGHT)
    time_scale = 1
    zoomed = False

    # initial set up
    setup()
    while True:
        # while pause not pressed, draw and update screen
        gui.drawMenu()
        for body in bodies:
            body.display(zoomed)

        if zoomed:
            zoomed = False

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

                # zooming with scroll wheel
                if event.button == 4:
                    zoom_level = zoom_level * 1.1
                    gui.space.fill(BLACK)
                    zoomed = True
                elif event.button == 5:
                    zoom_level = zoom_level / 1.1
                    gui.space.fill(BLACK)
                    zoomed = True


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
                    speed_scale = speed_scale / 1.25


                # b time travel
                if gui.b_timetravel_button.collidepoint(mouse_pos):
                    time_scale = time_scale * 1.25
                    speed_scale = speed_scale * 1.25

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


database.commit()
database1.commit()
database2.commit()
database3.commit()
database4.commit()
database5.commit()


database.close()
database1.close()
database2.close()
database3.close()
database4.close()
database5.close()

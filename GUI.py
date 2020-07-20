#
# GUI.py
# User interface, built with pygame.
#

############################## file set up
import pygame
from datetime import date

# set up colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)


class GUI(object):
    def __init__(self, WIDTH, HEIGHT):
        self.game_font = pygame.font.SysFont('consolas', 20)

        # set up surface plane
        self.space = pygame.display.set_mode((WIDTH, HEIGHT))  # ((width, height))
        self.space.fill(BLACK)

        self.pause = False


        ############################ CREATE and draw buttons first time
        # search objects
        self.search_object_button = pygame.Rect(20, 10, 200, 50)  # (top, bottom, width, length)
        self.search_object_button_surface = self.game_font.render('SEARCH OBJECTS', True, (0, 0, 0))  # ('text', anti-alias, (color)))

        # search events
        self.search_event_button = pygame.Rect(600, 10, 200, 50)
        self.search_event_button_surface = self.game_font.render('SEARCH EVENTS', True, (0, 0, 0))

        # calculate launch
        self.calc_launch_button = pygame.Rect(1290, 10, 200, 50)
        self.calc_launch_button_surface = self.game_font.render('CALCULATE LAUNCH', True, (0, 0, 0))

        # trails activate/deactivate
        self.trails_button = pygame.Rect(20, 70, 100, 50)
        self.trails_button_surface = self.game_font.render('TRAILS', True, (0, 0, 0))

        # exit button
        self.exit_button = pygame.Rect(1390, 740, 100, 50)
        self.exit_button_surface = self.game_font.render('EXIT', True, (0, 0, 0))


        # date display
        self.date_button = pygame.Rect(95, 740, 300, 50)
        self.date_button_surface = self.game_font.render('PAUSE', True, (0, 0, 0))

        # forward time travel
        self. f_timetravel_button = pygame.Rect(420, 740, 50, 50)
        self.f_timetravel_button_surface = self.game_font.render("  +  ", True, (0, 0, 0))

        # backward time travel
        self.b_timetravel_button = pygame.Rect(20, 740, 50, 50)
        self.b_timetravel_button_surface = self.game_font.render("  -  ", True, (0, 0, 0))

        self.drawMenu()
        pygame.display.update()

    def drawMenu(self):
        # search objects
        pygame.draw.rect(self.space, GRAY, self.search_object_button)
        self.space.blit(self.search_object_button_surface, (40, 25))
        # search events
        pygame.draw.rect(self.space, GRAY, self.search_event_button)
        self.space.blit(self.search_event_button_surface, (630, 25))
        # calculate launch
        pygame.draw.rect(self.space, GRAY, self.calc_launch_button)
        self.space.blit(self.calc_launch_button_surface, (1310, 25))
        # trails activate/deactivate
        pygame.draw.rect(self.space, GRAY, self.trails_button)
        self.space.blit(self.trails_button_surface, (35, 85))
        # exit button
        pygame.draw.rect(self.space, GRAY, self.exit_button)
        self.space.blit(self.exit_button_surface, (1400, 760))
        # date display
        pygame.draw.rect(self.space, GRAY, self.date_button)
        self.space.blit(self.date_button_surface, (180, 760))
        # forward time travel
        pygame.draw.rect(self.space, GRAY, self.f_timetravel_button)
        self.space.blit(self.f_timetravel_button_surface, (420, 760))
        # backward time travel
        pygame.draw.rect(self.space, GRAY, self.b_timetravel_button)
        self.space.blit(self.b_timetravel_button_surface, (20, 760))
        return







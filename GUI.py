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



        ############################ CREATE and draw buttons first time
        # search objects
        self.search_object_button = pygame.Rect(20, 10, 200, 50)  # (top, bottom, width, length)
        pygame.draw.rect(self.space, GRAY, self.search_object_button)
        self.search_object_button_surface = self.game_font.render('SEARCH OBJECTS', True, (0, 0, 0))  # ('text', anti-alias, (color)))
        self.space.blit(self.search_object_button_surface, (40, 25))

        # search events
        self.search_event_button = pygame.Rect(300, 10, 200, 50)
        pygame.draw.rect(self.space, GRAY, self.search_event_button)
        self.search_event_button_surface = self.game_font.render('SEARCH EVENTS', True, (0, 0, 0))
        self.space.blit(self.search_event_button_surface, (330, 25))

        # calculate launch
        self.calc_launch_button = pygame.Rect(590, 10, 200, 50)
        pygame.draw.rect(self.space, GRAY, self.calc_launch_button)
        self.calc_launch_button_surface = self.game_font.render('CALCULATE LAUNCH', True, (0, 0, 0))
        self.space.blit(self.calc_launch_button_surface, (600, 25))

        # trails activate/deactivate
        self.trails_button = pygame.Rect(20, 70, 100, 50)
        pygame.draw.rect(self.space, GRAY, self.trails_button)
        self.trails_button_surface = self.game_font.render('TRAILS', True, (0, 0, 0))
        self.space.blit(self.trails_button_surface, (35, 85))

        # exit button
        self.exit_button = pygame.Rect(690, 540, 100, 50)
        pygame.draw.rect(self.space, GRAY, self.exit_button)
        self.exit_button_surface = self.game_font.render('EXIT', True, (0, 0, 0))
        self.space.blit(self.exit_button_surface, (710, 560))

        # zoom slider
        self.zoom_slider = pygame.Rect(700, 100, 100, 400)
        pygame.draw.rect(self.space, WHITE, self.zoom_slider)

        # date display
        self.today = date.today()
        self.current_date = self.today.strftime("%b-%d-%Y")  # current date
        self.date_button = pygame.Rect(95, 540, 300, 50)
        pygame.draw.rect(self.space, GRAY, self.date_button)
        self.date_button_surface = self.game_font.render(self.current_date, True, (0, 0, 0))
        self.space.blit(self.date_button_surface, (180, 560))

        # forward time travel
        self. f_timetravel_button = pygame.Rect(420, 540, 50, 50)
        pygame.draw.rect(self.space, GRAY, self.f_timetravel_button)
        self.f_timetravel_button_surface = self.game_font.render("  +  ", True, (0, 0, 0))
        self.space.blit(self.f_timetravel_button_surface, (420, 560))

        # backward time travel
        self.b_timetravel_button = pygame.Rect(20, 540, 50, 50)
        pygame.draw.rect(self.space, GRAY, self.b_timetravel_button)
        self.b_timetravel_button_surface = self.game_font.render("  -  ", True, (0, 0, 0))
        self.space.blit(self.b_timetravel_button_surface, (20, 560))
        pygame.display.update()









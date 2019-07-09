import pygame
import time # del me
from pygame.locals import *  # seems like this sucks

import sys
sys.path.append('./')
from app.src.grid import Grid
from app.src.assets.configuration import *


class Game:
    """ Game logic with main loop. Uses pygame. ... """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        # self.grid = Grid(self.screen)
        # self.grid.init_grid_human()
        # self.grid.init_grid_random()

        self.running = False

    def start_game(self):
        self.running = True
        self.screen.fill(BACKGROUND)

        while self.running:
            # time.sleep(1)

            self.__check_events()

            # self.grid.update()
            # self.grid.draw()

            pygame.display.update()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            elif event.type == QUIT:
                self.running = False

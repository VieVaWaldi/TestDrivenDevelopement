import pygame
import time # del me
from pygame.locals import *  # seems like this sucks

import sys
sys.path.append('./')
from app.src.life import Life
from app.src.assets.configuration import *


class Game:
    """ Game logic with main loop. Uses pygame. ... """

    def __init__(self, god_mode=False):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        self.life = Life(self.screen)

        if god_mode:
            self.life.init_universe_by_god()
        else:
            self.life.init_universe_random(10)

        self.running = False

    def start_game(self):

        self.running = True

        while self.running:

            self.__check_events()

            self.life.calculate_universe()

            # self.life.print_universe()
            # self.life.print_neighbours_list()

            self.life.draw()
            self.life.update_universe()

            pygame.display.update()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            elif event.type == QUIT:
                self.running = False

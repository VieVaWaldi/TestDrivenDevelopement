import pygame
import sys
import random

sys.path.append('./')
from app.src.cell import Cell
from app.src.assets.configuration import *


class Life:

    def __init__(self):
        self.universe = []

    def update(self):
        pass

    def init_universe_random(self, chance_alive):
        """ Initializes a universe filled with random cells. """

        if not isinstance(chance_alive, int):
            raise TypeError('Chance must be an int.')

        if chance_alive < 0 or 100 < chance_alive:
            raise ValueError('Chance must be between 0 and 100')

        for row in range(UNIVERSE_NUM_ROWS):
            self.universe.append([])
            for col in range(UNIVERSE_NUM_COLS):
                alive = random.randint(0, 100)
                if alive < chance_alive:
                    self.universe[row].append(Cell(row, col, True))
                else:
                    self.universe[row].append(Cell(row, col, False))

    def init_universe_by_god(self):
        pass

    def draw(self):
        pass

    def __count_neighbours(self):
        pass

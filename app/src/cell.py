import pygame

import sys
sys.path.append('./')
from app.src.assets.configuration import *


class Cell:
    """ A cell is the simplest living or dead object. """

    def __init__(self, x, y, is_alive):

        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError('Coordinates must be an int.')

        if x < 0 or y < 0:
            raise ValueError('Coordinates must be larger than 0.')

        self.x = x
        self.y = y

        self.is_alive = is_alive
        self.is_alive_changed = True

        self.color = self.__apply_color()

    def update(self, neighbour_count):
        """ Updates the cell at each timestep according to the rules. """

        if not isinstance(neighbour_count, int):
            raise TypeError('Neighbour_count must be an int')

        if neighbour_count < 0 or 8 < neighbour_count:
            raise ValueError('Only eight neighbours are possible.')

        self.is_alive_changed = False

        if neighbour_count is 3:
            self.is_alive = True
            self.is_alive_changed = True

        if neighbour_count < 2 or 3 < neighbour_count:
            self.is_alive = False
            self.is_alive_changed = True

        self.color = self.__apply_color()


    def draw(self):
        pass

    def __apply_color(self):
        return COLOR_CELL_ALIVE if self.is_alive else COLOR_CELL_DEAD


import pygame

import sys
sys.path.append('./')
from app.src.assets.configuration import *


class Cell:
    """ A cell is the simplest living or dead object. """

    def __init__(self, x, y, screen, is_alive=False):
        pass

    def update(self):
        """ Updates the cell at each timestep according to the rules.
            A cell should only be redrawn when is_alive changed
            due to performance reasons.	"""

        pass

    def draw(self):
        pass

    def __apply_color(self):
        """ Change color depending on whether cell is alive or dead. """
        pass
import unittest
import random

import pygame

from app.src.grid import Grid
from app.src.cell import Cell
from app.src.assets.configuration import *


"""
What to test:
	create game
	has everything it needs
	grid initializes correctly
	grid counts only neighbours
	grid counts not self cell
	frid counts correctly
	grid has correct number of cells
	grid first counts, then updates to not update cells wrong
	borders og grid for off cells are correctly counted

"""


class TestGrid(unittest.TestCase):

    def setUp(self):
        screen = pygame.display.set_mode(SCREEN_SIZE)
        self.grid = Grid(screen=screen)


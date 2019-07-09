import unittest

import pygame

from app.src.cell import Cell
from app.src.assets.configuration import *

"""
What to test:
	create cell
		should have default values when none passed
		can pass values that apply
	color is black when dead
	color is white when alive
	drawing works
	dies when neighbours < 2
	lives when neighbour == 2
	lives when neighbour == 3
	dies when neighbours > 2

    cell has right position
    is_alive_changed wird richtig bestimmt => performance!
"""


class TestCell(unittest.TestCase):

    def setUp(self):
        screen = pygame.display.set_mode(SCREEN_SIZE)
        self.cell = Cell(x=10, y=10, screen=screen)


if __name__ == '__main__':
    unittest.main()

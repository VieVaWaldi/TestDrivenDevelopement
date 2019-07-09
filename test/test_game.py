import unittest

# from app.src.cell import Cell
from app.src.assets.configuration import *


"""
What to test:
	create game
	has everything it needs
	close game
"""


class TestGame(unittest.TestCase):

    def set_up(self):
        self.game = Game()


if __name__ == '__main__':
    unittest.main()

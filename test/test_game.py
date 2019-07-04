import sys
import unittest

# sys.path.append('./')
from app.src.cell import Cell
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

    def test_game_has_all_necessarry_objects(self):
        pass


if __name__ == '__main__':
    unittest.main()

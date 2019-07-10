import unittest
import pygame
import random

from app.src.life import Life
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


class TestLife(unittest.TestCase):

    def setUp(self):
        self.grid = Life()

    # Init Grid Random ###

    def test_init_universe_random_inits_not_empty(self):
        self.grid.init_universe_random(chance_alive=100)
        self.assertIsNotNone(self.grid.universe)

    def test_init_universe_random_has_correct_num_of_rows(self):
        self.grid.init_universe_random(chance_alive=100)
        self.assertEqual(len(self.grid.universe), UNIVERSE_NUM_ROWS)

    def test_init_universe_random_has_correct_num_of_cols(self):
        self.grid.init_universe_random(chance_alive=100)

        col_count = 0
        for col in self.grid.universe[0]:
            col_count += 1

        self.assertEqual(col_count, UNIVERSE_NUM_COLS)

    def test_universe_random_only_inhabits_cells(self):
        self.grid.init_universe_random(chance_alive=100)
        for row in self.grid.universe:
            for col in row:
                self.assertIsInstance(col, Cell)

    def test_universe_random_only_takes_int(self):
        self.assertRaises(TypeError, self.grid.init_universe_random, 'easter_egg')
        self.assertRaises(TypeError, self.grid.init_universe_random, 2.71828)

    def test_universe_random_raise_error_on_None(self):
        self.assertRaises(TypeError, self.grid.init_universe_random, 'easter_egg')

    def test_universe_random_chance_must_be_between_0_and_100(self):
        self.assertRaises(ValueError, self.grid.init_universe_random, -9_999)
        self.assertRaises(ValueError, self.grid.init_universe_random, -1)
        self.assertRaises(ValueError, self.grid.init_universe_random, 101)
        self.assertRaises(ValueError, self.grid.init_universe_random, 9_999)

    def test_universe_every_cell_is_born_at_right_position(self):
        self.grid.init_universe_random(chance_alive=100)
        for row in range(UNIVERSE_NUM_ROWS):
            for col in range(UNIVERSE_NUM_COLS):
                self.assertEqual(row, self.grid.universe[row][col].x)
                self.assertEqual(col, self.grid.universe[row][col].y)

    # Update grid ###

    # Count neighbours wird public gemacht, da anders nicht rein geschaut werden kann !

    def test_update_first_counts_then_updates(self):
        # geht das ?
        pass

    def test_count_neighbours_

import unittest
import pygame
import random

from app.src.life import Life
from app.src.cell import Cell
from app.src.assets.configuration import *


class TestLife(unittest.TestCase):

    def setUp(self):
        self.life = Life()

    # Init life Random ############################################################

    def test_init_universe_random_inits_not_empty(self):
        self.life.init_universe_random()
        self.assertIsNotNone(self.life.universe)

    def test_init_universe_random_has_correct_num_of_rows(self):
        self.life.init_universe_random()
        self.assertEqual(len(self.life.universe), UNIVERSE_NUM_ROWS)

    def test_init_universe_random_has_correct_num_of_cols(self):
        self.life.init_universe_random()

        col_count = 0
        for col in self.life.universe[0]:
            col_count += 1

        self.assertEqual(col_count, UNIVERSE_NUM_COLS)

    def test_universe_random_only_inhabits_cells(self):
        self.life.init_universe_random()
        for row in self.life.universe:
            for col in row:
                self.assertIsInstance(col, Cell)

    def test_universe_random_only_takes_int(self):
        self.assertRaises(TypeError, self.life.init_universe_random, 'easter_egg')
        self.assertRaises(TypeError, self.life.init_universe_random, 2.71828)

    def test_universe_random_raise_error_on_None(self):
        self.assertRaises(TypeError, self.life.init_universe_random, 'easter_egg')

    def test_universe_random_chance_must_be_between_0_and_100(self):
        self.assertRaises(ValueError, self.life.init_universe_random, -9_999)
        self.assertRaises(ValueError, self.life.init_universe_random, -1)
        self.assertRaises(ValueError, self.life.init_universe_random, 101)
        self.assertRaises(ValueError, self.life.init_universe_random, 9_999)

    def test_universe_every_cell_is_born_at_right_position(self):
        self.life.init_universe_random(chance_alive=100)
        for row in range(UNIVERSE_NUM_ROWS):
            for col in range(UNIVERSE_NUM_COLS):
                self.assertEqual(row, self.life.universe[row][col].x)
                self.assertEqual(col, self.life.universe[row][col].y)

    def test_every_cell_is_alive_when_chance_is_100(self):
        self.life.init_universe_random(chance_alive=100)
        for row in self.life.universe:
            for cell in row:
                self.assertTrue(cell.is_alive)

    def test_every_cell_is_dead_when_chance_is_0(self):
        self.life.init_universe_random(chance_alive=0)
        for row in self.life.universe:
            for cell in row:
                self.assertFalse(cell.is_alive)

    # Update life #################################################################

    # private function __calculate_neighbours
    def test_neighbours_list_has_same_rows_as_universe(self):
        self.life.init_universe_random(chance_alive=0)
        self.assertEqual(len(self.life.universe), len(self.life.neighbours_list))

    def test_neighbours_list_has_same_cols_as_universe(self):
        self.life.init_universe_random(chance_alive=0)
        col_count = 0
        for col in self.life.neighbours_list[0]:
            col_count += 1

        self.assertEqual(col_count, UNIVERSE_NUM_COLS)

    # private function __count_neighbours
    def test_count_neighbours_cant_be_None(self):
        self.life.init_universe_random(chance_alive=0)
        self.life.calculate_universe()

        for row in self.life.neighbours_list:
            for col in row:
                self.assertIsNotNone(col)

    def test_calculate_neighbours_returns_0_when_every_cell_is_dead(self):
        self.life.init_universe_random(chance_alive=0)
        self.life.calculate_universe()
        for row in self.life.neighbours_list:
            for count in row:
                self.assertEqual(count, 0)

    # proofs borders are connected
    def test_calculate_neighbours_returns_8_when_every_cell_is_alive(self):
        self.life.init_universe_random(chance_alive=100)
        self.life.calculate_universe()
        for row in self.life.neighbours_list:
            for count in row:
                self.assertEqual(count, 8)

    # Init life By God ############################################################

# sys.path.append('./') 	# executable from this dir only via this line

# import sys
import unittest

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
"""


class TestCell(unittest.TestCase):

    def setUp(self):
        self.cell = Cell(x=10, y=10)

    def test_default_values_apply(self):
        self.assertIsNotNone(self.cell.x)
        self.assertIsNotNone(self.cell.y)
        self.assertFalse(self.cell.is_alive)

    def test_updatet_takes_only_integers(self):
        self.assertRaises(ValueError, self.cell.update, 3.2)
        self.assertRaises(ValueError, self.cell.update, 'four')

    def test_cell_cant_have_more_than_eight_neighbours(self):
        self.assertRaises(ValueError, self.cell.update, -1)
        self.assertRaises(ValueError, self.cell.update, 99)

    def test_cell_dead_when_less_than_two_neighbours(self):
        self.cell.update(neighbour_count=0)
        self.assertFalse(self.cell.is_alive)
        self.cell.update(neighbour_count=1)
        self.assertFalse(self.cell.is_alive)

    def test_cell_alive_when_two_or_three_neighbours(self):
        self.cell.update(neighbour_count=2)
        self.assertTrue(self.cell.is_alive)
        self.cell.update(neighbour_count=3)
        self.assertTrue(self.cell.is_alive)

    def test_cell_dead_when_more_than_three_neighbours(self):
        self.cell.update(neighbour_count=4)
        self.assertFalse(self.cell.is_alive)
        self.cell.update(neighbour_count=5)
        self.assertFalse(self.cell.is_alive)
        self.cell.update(neighbour_count=8)
        self.assertFalse(self.cell.is_alive)

    def test_cell_lives_when_dead_and_exactly_three_neighbours(self):
        self.cell.update(neighbour_count=1)
        self.cell.update(neighbour_count=3)
        self.assertTrue(self.cell.is_alive)

    def test_cell_state_only_changes_when_necessary(self):
        self.cell.update(neighbour_count=3)
        self.cell.update(neighbour_count=3)
        self.assertFalse(self.cell.is_alive_changed)
        self.cell.update(neighbour_count=1)
        self.assertTrue(self.cell.is_alive_changed)

        self.cell.update(neighbour_count=1)
        self.cell.update(neighbour_count=1)
        self.assertFalse(self.cell.is_alive_changed)
        self.cell.update(neighbour_count=2)
        self.assertTrue(self.cell.is_alive_changed)

    def test_correct_color_when_alive(self):
        self.cell.update(neighbour_count=2)
        self.assertEqual(self.cell.color, COLOR_CELL_ALIVE)

    def test_correct_color_when_dead(self):
        self.cell.update(neighbour_count=0)
        self.assertEqual(self.cell.color, COLOR_CELL_DEAD)


if __name__ == '__main__':
    unittest.main()

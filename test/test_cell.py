import unittest

from app.src.cell import Cell
from app.src.assets.configuration import *


class TestCell(unittest.TestCase):

    def setUp(self):
        self.cell = Cell(10, 10, False)

    # Value check ###

    def test_coordinates_are_not_null(self):
        self.assertIsNotNone(self.cell.x)
        self.assertIsNotNone(self.cell.y)

    def test_coordinates_are_larger_than_0(self):
        self.assertGreater(self.cell.x, -1)
        self.assertGreater(self.cell.y, -1)

    def test_update_returns_error_on_None(self):
        self.assertRaises(TypeError, self.cell.update, None)

    def test_update_only_takes_integer(self):
        self.assertRaises(TypeError, self.cell.update, 'one')
        self.assertRaises(TypeError, self.cell.update, 3.1415926)

    def test_update_only_takes_values_between_0_and_8(self):
        self.assertRaises(ValueError, self.cell.update, -999)
        self.assertRaises(ValueError, self.cell.update, -1)
        self.assertRaises(ValueError, self.cell.update, 9)
        self.assertRaises(ValueError, self.cell.update, 999999)

    # Rules check ###

    def test_dead_cell_revived_when_three_neighbours(self):
        self.cell.is_alive = False
        self.cell.update(3)
        self.assertTrue(self.cell.is_alive)

    def test_dead_cell_stays_dead_when_not_three_neighbours(self):
        self.cell.is_alive = False
        self.cell.update(0)
        self.assertFalse(self.cell.is_alive)

        self.cell.is_alive = False
        self.cell.update(2)
        self.assertFalse(self.cell.is_alive)

        self.cell.is_alive = False
        self.cell.update(4)
        self.assertFalse(self.cell.is_alive)

        self.cell.is_alive = False
        self.cell.update(8)
        self.assertFalse(self.cell.is_alive)

    def test_alive_cell_dies_when_less_than_2_neighbours(self):
        self.cell.is_alive = True
        self.cell.update(1)
        self.assertFalse(self.cell.is_alive)

    def test_alive_cell_dies_when_more_than_3_neighbours(self):
        self.cell.is_alive = True
        self.cell.update(4)
        self.assertFalse(self.cell.is_alive)

    def test_alive_cell_stays_alive_with_2_neighbours(self):
        self.cell.is_alive = True
        self.cell.update(2)
        self.assertTrue(self.cell.is_alive)

    def test_alive_cell_stays_alive_with_3_neighbours(self):
        self.cell.is_alive = True
        self.cell.update(3)
        self.assertTrue(self.cell.is_alive)

    # Performance check ###

    def test_is_alive_changed_is_false_when_cell_stays_alive(self):
        self.cell.is_alive = True
        self.cell.update(2)
        self.assertFalse(self.cell.is_alive_changed)

    def test_is_alive_changed_is_false_when_cell_stays_dead(self):
        self.cell.is_alive = False
        self.cell.update(2)
        self.assertFalse(self.cell.is_alive_changed)

    def test_is_alive_changed_is_true_when_cell_dies(self):
        self.cell.is_alive = True
        self.cell.update(1)
        self.assertTrue(self.cell.is_alive_changed)

    def test_is_alive_changed_is_true_when_cell_is_revived(self):
        self.cell.is_alive = False
        self.cell.update(3)
        self.assertTrue(self.cell.is_alive_changed)

    # Drawing check ###

    def test_right_color_applies_when_cell_dies(self):
        self.cell.is_alive = True
        self.cell.update(0)
        self.assertEqual(self.cell.color, COLOR_CELL_DEAD)

    def test_right_color_applies_when_cell_is_revived(self):
        self.cell.is_alive = False
        self.cell.update(3)
        self.assertEqual(self.cell.color, COLOR_CELL_ALIVE)

if __name__ == '__main__':
    unittest.main()

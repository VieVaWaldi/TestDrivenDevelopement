import pygame
import sys
import random

sys.path.append('./')
from app.src.cell import Cell
from app.src.assets.configuration import *


class Life:
    """ Life holds the universe where every cell exists.
        Life within a universe can be created by chance: init_universe_random
        or by a god: init_universe_god ."""

    def __init__(self, screen=None):
        self.screen = screen

        self.universe: [Cell] = []
        self.neighbours_list: [int] = []

        self.__init_neighbours_list()

    def calculate_universe(self):
        """ Count ever cell and store count of neighbours. """
        for row in range(UNIVERSE_NUM_ROWS):
            for col in range(UNIVERSE_NUM_COLS):
                cell = self.universe[row][col]
                self.neighbours_list[row][col] = self.__calculate_neighbours(cell)

    def update_universe(self):
        """ Tell every cell their neighbour count. """

        for row in range(UNIVERSE_NUM_ROWS):
            for col in range(UNIVERSE_NUM_COLS):
                neighbours_count = self.neighbours_list[row][col]
                self.universe[row][col].update(neighbours_count)

    def init_universe_random(self, chance_alive):
        """ Initializes a universe filled with random cells. """

        if not isinstance(chance_alive, int):
            raise TypeError('Chance must be an int.')

        if chance_alive < 0 or 100 < chance_alive:
            raise ValueError('Chance must be between 0 and 100')

        for row in range(UNIVERSE_NUM_ROWS):
            self.universe.append([])
            for col in range(UNIVERSE_NUM_COLS):
                alive = random.randint(1, 100)
                if alive <= chance_alive:
                    self.universe[row].append(Cell(row, col, True, self.screen))
                else:
                    self.universe[row].append(Cell(row, col, False, self.screen))

    # wie soll ich das testen
    def init_universe_by_god(self):

        print('Use the following keys to play god:')
        print('\tMouseButton 1 to create')
        print('\tMouseButton 2 to destroy')
        print('\tSpace to destroy everything')
        print('\tENTER to start')

        not_done = True

        self.init_universe_random(chance_alive=0)

        while not_done:
            pygame.event.get()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if click[0]:
                x = int(mouse_x / CELLS_SIZE_WIDTH)
                y = int(mouse_y / CELLS_SIZE_HEIGHT)
                self.universe[x][y].update(3)  # 3 is always life
                self.universe[x][y].draw()

            if click[2]:
                x = int(mouse_x / CELLS_SIZE_WIDTH)
                y = int(mouse_y / CELLS_SIZE_HEIGHT)
                self.universe[x][y].update(0)  # 0 is always death
                self.universe[x][y].draw()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                not_done = False
            if keys[pygame.K_SPACE]:
                self.init_universe_random(chance_alive=0)
                self.calculate_universe()
                self.update_universe()
                self.draw()

            pygame.display.update()

    def draw(self):
        for row in self.universe:
            for cell in row:
                cell.draw()

    def __init_neighbours_list(self):
        for row in range(UNIVERSE_NUM_ROWS):
            self.neighbours_list.append([])
            for col in range(UNIVERSE_NUM_COLS):
                self.neighbours_list[row].append([])

    def __calculate_neighbours(self, cell):
        """ Cells at the opposite border of the universe are neighbours. """

        neighbours_count = 0

        row = cell.x
        col = cell.y

        for x in range(row - 1, row + 2):
            for y in range(col -1, col + 2):

                if x is row and y is col:
                    continue

                if x is -1:
                    x = UNIVERSE_NUM_ROWS - 1

                if x is UNIVERSE_NUM_ROWS:
                    x = 0

                if y is -1:
                    y = UNIVERSE_NUM_COLS - 1

                if y is UNIVERSE_NUM_COLS:
                    y = 0

                if self.universe[x][y].is_alive:
                    neighbours_count += 1

        return neighbours_count

    def print_universe(self):
        """ Just for fun and debugging. """
        for row in self.universe:
            for col in row:
                print('[+]', end='') if col.is_alive else print('[ ]', end='')
            print('')

    def print_neighbours_list(self):
        """ Just for fun and debugging. """
        for row in self.neighbours_list:
            for col in row:
                print('[{}]'.format(col), end='')
            print('')

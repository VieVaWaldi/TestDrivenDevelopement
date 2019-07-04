import sys
sys.path.append('./')
from app.src.assets.configuration import *


class Cell:
    """ A cell is the simplest living or dead object. """

    def __init__(self, x, y, is_alive=False):

        self.x = x
        self.y = y

        self.is_alive = is_alive
        self.is_alive_changed = False

        self.__apply_color()

    def update(self, neighbour_count):
        """ Updates the cell at each timestep according to the rules.
            A cell should only be redrawn when is_alive changed
            due to performance reasons.	"""

        if not isinstance(neighbour_count, int):
            raise ValueError('neighbour_count must be an int.')

        if neighbour_count < 0 or 8 < neighbour_count:
            raise ValueError(
                'Cell can only have between 0 and eight neighbours' +
                'inclusively.')

        if neighbour_count < 2 or 3 < neighbour_count:
            if self.is_alive:
                self.is_alive = False
                self.is_alive_changed = True
            else:
                self.is_alive_changed = False

        if neighbour_count == 2 or neighbour_count == 3:
            if not self.is_alive:
                self.is_alive = True
                self.is_alive_changed = True
            else:
                self.is_alive_changed = False

        self.__apply_color()

    def draw(self):
        if self.is_alive_changed:
            # rect = pygame.Rect(self.x*COUNT_WIDTH, self.y*COUNT_HEIGHT, COUNT_WIDTH-1,COUNT_HEIGHT-1 )
            # pygame.draw.rect(self.screen, self.color, rect.inflate(-0.1, -0.1))
            # self.changed = False
            pass

    def __apply_color(self):
        """ Change color depending on whether cell is alive or dead. """
        if self.is_alive:
            self.color = COLOR_CELL_ALIVE
        else:
            self.color = COLOR_CELL_DEAD

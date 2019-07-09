# Matrix n*n
# Randomly filled with dots that follow 4 rules:
# any life cell with fewer than two neighbours dies                     life: n < 2 -> dead
# any life cell with two or three life neighbours lives                 life: n == 2 || n == 3 -> alive
# any life cell with more than three neighbours dies                    life: n > 3 -> dead
# any dead cell with exactly three neighbours becomes a living cell     dead: n == 3 -> alive
# everything happens in one step

import pygame
from pygame.locals import *
# import time
import random

FLAGS = FULLSCREEN | DOUBLEBUF
BACKGROUND = (255, 255, 255)
DOT_COLOR = (255, 0, 0)
FPS = 1

SCREEN_SIZE = WIDTH, HEIGHT = (600, 600)
N = 150     # Count of cells in a row
COUNT_WIDTH = int(WIDTH / N)
COUNT_HEIGHT = int(HEIGHT / N)

print(COUNT_HEIGHT)
print(COUNT_WIDTH)


class Environment:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Game of Life')
        self.screen = pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF)
        self.screen.set_alpha(None)

        self.clock = pygame.time.Clock()
        self.time_elapsed_since_last_action = 0
        self.global_time = 0

        self.grid = Grid(self.screen, WIDTH, HEIGHT, DOT_COLOR)

    def run_game(self):

        # dt = self.clock.tick()
        # self.time_elapsed_since_last_action += dt

        # if self.time_elapsed_since_last_action > FPS:

        self.grid.init_random()

        self.screen.fill(BACKGROUND)

        while True:

            self.global_time += 1

            self.handle_events_human()

            self.grid.update()
            self.grid.draw()

            pygame.display.update()

            # self.time_elapsed_since_last_action = 0

            self.clock.tick(60)

    def handle_events_human(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_done = False
                pygame.quit()


class Cell:

    def __init__(self, screen, x, y, lives):
        self.screen = screen
        self.lives = lives
        self.color = None

        self.changed = False
        self.neighbours = 0

        if self.lives:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)

        self.x = x
        self.y = y

    def draw(self):
        if self.changed:
            rect = pygame.Rect(self.x * COUNT_WIDTH, self.y *
                               COUNT_HEIGHT, COUNT_WIDTH - 1, COUNT_HEIGHT - 1)
            pygame.draw.rect(self.screen, self.color, rect.inflate(-0.1, -0.1))
            self.changed = False

    def update(self):

        neighbours = self.count_neighbours
        # rgbl=[255,0,0]
        # random.shuffle(rgbl)
        # self.color = rgbl

        if not self.lives:
            if neighbours == 3:
                self.lives = True
                self.color = (0, 0, 0)
                self.changed = True
            return

        if neighbours < 2:
            self.lives = False
            self.color = (255, 255, 255)
            self.changed = True

        if neighbours == 2 or neighbours == 3:
            self.lives = True
            self.color = (0, 0, 0)
            self.changed = True

        if neighbours > 3:
            self.lives = False
            self.color = (255, 255, 255)
            self.changed = True


class Grid:

    def __init__(self, screen, s_width, s_height, color):
        self.screen = screen
        self.s_width = s_width
        self.s_height = s_height
        self.color = color

        self.grid = []
        # self.newGrid = []

    def init_random(self):
        for i in range(N):
            self.grid.append([])
            for j in range(N):
                lives_proba = random.randint(0, 10)
                if lives_proba == 1:
                    self.grid[i].append(Cell(self.screen, i, j, True))
                else:
                    self.grid[i].append(Cell(self.screen, i, j, False))

    def draw(self):
        for i in range(N):
            for j in range(N):
                self.grid[i][j].draw()

    # Currently ignores boundaries
    def update(self):
        # self.newGrid = self.grid
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                count = self.count_neighbours(self.grid[i][j])
                self.grid[i][j].count_neighbours = count

        for i in range(1, N - 1):
            for j in range(1, N - 1):
                self.grid[i][j].update()
        # self.grid = self.newGrid

    # Contains errors at boundaries
    def count_neighbours(self, cell):

        x = cell.x
        y = cell.y

        count = 0

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                if self.grid[i][j].lives:
                    count += 1

        return count


env = Environment()
env.run_game()

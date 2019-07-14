import sys
import argparse

sys.path.append('./')
from app.src.game import Game

if __name__ == '__main__':

    god_mode = False

    if len(sys.argv) > 1:
        god_mode = sys.argv[1]

    game = Game(god_mode)
    game.start_game()

    print('Job Done!')

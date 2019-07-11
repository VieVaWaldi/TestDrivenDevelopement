import sys
import argparse

sys.path.append('./')
from app.src.game import Game

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Choose a creation mode')
    parser.add_argument('--random', metavar='-r', type=int, nargs='+',
                        help='Create life randomly.')

    parser.add_argument('--god', metavar='-g', nargs='+',
                        help='You are god.')

    args = parser.parse_args()

    print(args)

    # game = Game()
    # game.start_game()

    print('Job Done!')

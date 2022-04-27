from typing import Tuple
import random

from .noughts_and_crosses_player import NoughtsAndCrossesPlayer
from .noughts_and_crosses_board import NoughtsAndCrossesBoard


class NoughtsAndCrossesRandomPlayer(NoughtsAndCrossesPlayer):
    """docstring for NoughtsAndCrossesRandomPlayer"""

    def __init__(self):
        super(NoughtsAndCrossesRandomPlayer, self).__init__()

    def choosemove(self, board: NoughtsAndCrossesBoard) -> Tuple[int, int]:
        # don't call this function when the board is full
        while True:
            x = random.randint(0, board.WIDTH - 1)
            y = random.randint(0, board.HEIGHT - 1)
            if board.get(x, y) == " ":
                return x, y

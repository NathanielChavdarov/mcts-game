from typing import Tuple

from .player import Player
from .noughts_and_crosses_board import NoughtsAndCrossesBoard


class NoughtsAndCrossesPlayer(Player):
    """docstring for NoughtsAndCrossesPlayer"""

    def __init__(self):
        super(NoughtsAndCrossesPlayer, self).__init__()

    def askMove(self, board: NoughtsAndCrossesBoard) -> Tuple[int, int]:
        while True:
            x = input("Please enter an x coordinate (0-2): ")
            y = input("Please enter a y coordinate (0-2): ")
            if board.get(x, y) == " ":
                return (x, y)

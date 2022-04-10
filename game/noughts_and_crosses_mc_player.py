from typing import Tuple

from .noughts_and_crosses_player import NoughtsAndCrossesPlayer
from .noughts_and_crosses_board import NoughtsAndCrossesBoard


class NoughtsAndCrossesMCPlayer(NoughtsAndCrossesPlayer):
    """docstring for NoughtsAndCrossesMCPlayer"""

    def __init__(self):
        super(NoughtsAndCrossesMCPlayer, self).__init__()

    def choosemove(self, board: NoughtsAndCrossesBoard) -> Tuple[int, int]:
        return x, y

from .game import Game
from .noughts_and_crosses_board import NoughtsAndCrossesBoard
from .noughts_and_crosses_player import NoughtsAndCrossesPlayer


class NoughtsAndCrossesGame(Game):
    """docstring for NoughtsAndCrossesGame"""

    def __init__(
        self,
        player1: NoughtsAndCrossesPlayer,
        player2: NoughtsAndCrossesPlayer,
    ):
        super(NoughtsAndCrossesGame, self).__init__()
        self.board = NoughtsAndCrossesBoard()
        self.players = [
            player1,
            player2,
        ]

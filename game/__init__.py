from enum import Enum


class Game:
    """docstring for Game"""

    def __init__(self, arg):
        self.arg = arg

    def start(self):
        self.board.initialise()
        while True:
            self.turn(1)
            self.check_state()
            self.turn(2)
            self.check_state()


class Board:
    """docstring for Board"""

    def __init__(self):
        pass

    def initialise(self):
        raise Exception("to be implemented in subclass")


class NoughtsAndCrossesBoard(Board):
    """docstring for NoughtsAndCrossesBoard"""

    WIDTH = 3
    HEIGHT = 3

    def __init__(self):
        super(NoughtsAndCrossesBoard, self).__init__()

    def initialise(self):
        self.brd = [
            ["" for _ in range(self.WIDTH)]
            for _ in range(self.HEIGHT)
        ]


class GameType(Enum):
    NOUGHTSANDCROSSES = 1

class NoughtsAndCrossesGame(Game):
    """docstring for NoughtsAndCrossesGame"""

    def __init__(self):
        super(NoughtsAndCrossesGame, self).__init__()
        self.board = NoughtsAndCrossesBoard()

from enum import Enum


class Game:
    """docstring for Game"""

    def __init__(self, arg):
        self.arg = arg

    def start(self):
        self.board.initialise()
        while True:
            self.turn(1)
            if self.check_state() == 0:
                print("player 1 has won!")
                # to be implemented
                return self.end()
            self.turn(2)
            if self.check_state() == 1:
                print("player 2 has won!")
                # to be implemented
                return self.end()
            self.check_state()


class Board:
    """docstring for Board"""

    def __init__(self):
        pass

    def initialise(self):
        raise Exception("to be implemented in subclass")

    def check_state(self):
        return 2


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

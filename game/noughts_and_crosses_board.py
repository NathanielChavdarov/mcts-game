from .board import Board


class NoughtsAndCrossesBoard(Board):
    """docstring for NoughtsAndCrossesBoard"""

    WIDTH = 3
    HEIGHT = 3

    def __init__(self):
        super(NoughtsAndCrossesBoard, self).__init__()

    def initialise(self):
        self.brd = [
            [" " for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)
        ]

    def display(self):
        for r in self.brd:
            print(" -" * len(r))
            for c in r:
                print("|" + c, end="")
            print("|")
        print(" -" * len(r))

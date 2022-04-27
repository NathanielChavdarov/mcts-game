from typing import Tuple

from .board import Board

class NoughtsAndCrossesBoard(Board):
    """docstring for NoughtsAndCrossesBoard"""

    WIDTH = 3
    HEIGHT = 3

    def __init__(self):
        super(NoughtsAndCrossesBoard, self).__init__()

    def display(self) -> None:
        for r in self.brd:
            print(" -" * len(r))
            for c in r:
                print("|" + c, end="")
            print("|")
        print(" -" * len(r))
        print("\n")

    def get(self, x: int, y: int) -> str:
        return self.brd[x][y]

    def initialise(self) -> None:
        self.brd = [
            [" " for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)
        ]

    def update(self, move: Tuple[int, int], player: int) -> None:
        if self.brd[move[0]][move[1]] != " ":
            raise Exception(f"Position x: {move[0]} y: {move[1]} has already been taken")
        if player not in (0, 1):
            raise Exception(f"Player number {player} is invalid")
        self.brd[move[0]][move[1]] = "XO"[player]

    def has_won(self, player: int) -> bool:
        p = "XO"[player]
        # checking rows
        if any(all(cell == p for cell in row) for row in self.brd):
            return True
        # checking columns
        if any(all(row[i] == p for row in self.brd) for i in range(3)):
            return True
        # checking right to left diagonal
        if (self.brd[0][2], self.brd[1][1], self.brd[2][0]) == (p, p, p):
            return True
        # checking left to right diagonal
        if (self.brd[0][0], self.brd[1][1], self.brd[2][2]) == (p, p, p):
            return True
        return False

    def stalemate(self) -> bool:
        return all(all(cell != " " for cell in row) for row in self.brd)

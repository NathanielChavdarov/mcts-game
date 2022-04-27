class Game:
    """docstring for Game"""

    def __init__(self):
        pass

    def play(self) -> int:
        self.board.initialise()
        while True:
            self.turn(0)
            # self.board.display()
            if self.board.has_won(0):
                # print("player 1 has won!")
                return 0
            if self.board.stalemate():
                return -1
            self.turn(1)
            # self.board.display()
            if self.board.has_won(1):
                # print("player 2 has won!")
                return 1

    def turn(self, player: int):
        move = self.players[player].choosemove(self.board)
        self.board.update(move, player)

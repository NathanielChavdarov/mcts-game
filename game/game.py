class Game:
    """docstring for Game"""

    def __init__(self):
        pass

    def start(self):
        self.board.initialise()
        while True:
            self.turn(0)
            if self.check_state() == 0:
                print("player 1 has won!")
                # to be implemented
                return self.end()
            self.turn(1)
            if self.check_state() == 1:
                print("player 2 has won!")
                # to be implemented
                return self.end()

    def turn(self, player: int):
        move = self.players[player].choosemove(self.board)

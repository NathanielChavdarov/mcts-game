from .board import Board


# class Tree():
#     """docstring for Tree"""
#     def __init__(self):
#         pass


class Node():
    """docstring for Node"""
    def __init__(self, board: Board, move, player: int):
        self.board = board
        self.move = move
        self.player = player
        self.children = []

    def add_child(self, child: Node) -> None:
        self.children.append(child)


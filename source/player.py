from source.pieces import Pieces


class Player:
    def __init__(self, pid: int, name: str, piece: Pieces):
        self._pid = pid
        self._name = name
        self._piece = piece

    def play(self, board):
        while True:
            x, y = list(map(int, input('Enter X, Y:').split(' ')))
            if board.is_valid_coordinate(x, y) and board.add(pieces=self._piece, x=x, y=y):
                board.print_board()
                return x, y
            print(f'Retry your X={x}, Y={y}. Its not valid')

    def get_name(self):
        return self._name

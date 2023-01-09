from source.pieces import Pieces


class Board:
    def __init__(self, size: int):
        self._size = size
        self._matrix = [[None] * self._size for _ in range(self._size)]

    def print_board(self):
        for row in self._matrix:
            for col in row:
                if col is not None:
                    print(col.get_symbol(), end='|')
                else:
                    print(' ', end='|')
            print()

    def add(self, pieces: Pieces, x: int, y: int) -> bool:
        if self._matrix[x][y] is None:
            self._matrix[x][y] = pieces
            return True
        return False

    def is_valid_coordinate(self, x: int, y: int) -> bool:
        return 0 <= x < self._size and 0 <= y < self._size

    def get_size(self):
        return self._size

    def validate_piece(self, x: int, y: int, target_x: int, target_y: int):
        if self._matrix[target_x][target_y] is None:
            return False
        piece: Pieces = self._matrix[x][y]
        target: Pieces = self._matrix[target_x][target_y]
        return True if piece == target else False



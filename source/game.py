from typing import List

from source.board import Board
from source.pieces import SymbolFactory
from source.player import Player


class Game:

    def __init__(self, size):
        self._board = Board(size)
        self._players = []
        self._max_turn = size*size

    def add_players(self, players: List):
        for i, player in enumerate(players):
            name, symbol = player
            self._players.append(Player(pid=i + 1, name=name, piece=SymbolFactory.symbol_factory(symbol)))

    def winner_check(self, x: int, y: int) -> bool:
        row_wise_col_match = True
        col_wise_row_match = True
        diagonal_match = True
        anti_diagonal_match = True
        size = self._board.get_size()

        # validate input row, column wise all match
        for col in range(size):
            if not self._board.validate_piece(x=x, y=y, target_x=x, target_y=col):
                row_wise_col_match = False
                break

        # validate input column row wise all match
        for row in range(size):
            if not self._board.validate_piece(x=x, y=y, target_x=row, target_y=y):
                col_wise_row_match = False
                break

        # validate input row col diagonal match
        for row, col in zip(list(range(size)), list(range(size))):
            if not self._board.validate_piece(x=x, y=y, target_x=row, target_y=col):
                diagonal_match = False
                break

        # validate anti diagonal
        for row, col in zip(list(range(size)), list(range(size))[::-1]):
            if not self._board.validate_piece(x=x, y=y, target_x=row, target_y=col):
                anti_diagonal_match = False
                break
        return row_wise_col_match or col_wise_row_match or diagonal_match or anti_diagonal_match

    def start(self):
        print('-----------Game start------------')
        self._board.print_board()
        while self._max_turn > 1:
            for player in self._players:
                print(f'{player.get_name()} Turn')
                x, y = player.play(board=self._board)
                self._max_turn -= 1
                if self.winner_check(x, y):
                    print(f'{player.get_name()} is winner')
                    print('-------Game Over--------------')
                    return
        print('Game Tie')
        print('--------Game Over----------------')

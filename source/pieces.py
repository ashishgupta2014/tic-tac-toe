from enum import Enum


class Pieces:
    def __init__(self, symbol: str):
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol


class PiecesX(Pieces):
    def __init__(self, symbol: str):
        super().__init__(symbol)


class PiecesO(Pieces):
    def __init__(self, symbol: str):
        super().__init__(symbol)


class SymbolFactory(Enum):
    X = 'X'
    O = 'O'

    @classmethod
    def symbol_factory(cls, symbol: str):
        if cls.X.value.upper() == symbol:
            return PiecesX(symbol=symbol)
        elif cls.O.value.upper() == symbol:
            return PiecesO(symbol=symbol)
        raise ValueError(f'Currently {symbol} not available for the choice')

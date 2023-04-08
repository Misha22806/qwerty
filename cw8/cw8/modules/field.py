from .head import Head
from .tail import Tail
from .fruit import Fruit


class Field:
    def __init__(self, size: int = 5, symbol: str = "□"):
        self.size = size
        self.symbol = symbol

    def render(self, head: Head, tail: Tail, fruit: Fruit):
        field = []
        for y in range(self.size):
            field.append([])
            for x in range(self.size):
                field[y].append(self.symbol)

        return field

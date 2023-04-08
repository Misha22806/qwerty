import random

from .head import Head
from .tail import Tail


class Fruit:
    def __init__(self, fieldSize: int, head: Head, tail: Tail, symbol: str = "●"):
        self.fieldSize = fieldSize
        self.head = head
        self.tail = tail

        self.symbol = symbol

        self.generate()

    def generate(self):
        self.x = random.randint(0, self.fieldSize - 1)
        self.y = random.randint(0, self.fieldSize - 1)
        if self.x == self.head.x and self.y == self.head.y:
            self.generate()
            return
        for element in self.tail.elements:
            if self.x == element.x and self.y == element.y:
                self.generate()
                return

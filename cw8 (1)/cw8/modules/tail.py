from .head import Head


class TailElement:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x


class Tail:
    def __init__(self, head: Head):
        self.head = head
        self.elements = []

    def move(self):
        if len(self.elements) > 1:
            for i in range(len(self.elements) - 1, 0, -1):
                self.elements[i] = TailElement(
                    self.elements[i - 1].y, self.elements[i - 1].x
                )
        if len(self.elements) > 0:
            self.elements[0] = TailElement(self.head.y, self.head.x)

    def add(self):
        self.elements.append(TailElement(self.head.y, self.head.x))

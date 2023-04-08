import random
import keyboard


class Head:
    def __init__(self, fieldSize: int, symbol: str = "■"):
        self.fieldSize = fieldSize
        self.symbol = symbol
        self.direction = ""

        self.x = random.randint(0, self.fieldSize - 1)
        self.y = random.randint(0, self.fieldSize - 1)
        keyboard.hook(self.keyboard)

    def keyboard(self, event):
        if event.name == "w" or event.name == "up":
            self.direction = "up"
        elif event.name == "s" or event.name == "down":
            self.direction = "down"
        elif event.name == "a" or event.name == "left":
            self.direction = "left"
        elif event.name == "d" or event.name == "right":
            self.direction = "right"

    def move(self):
        if self.direction == "up":
            self.y -= 1
            if self.y < 0:
                self.y = self.fieldSize - 1
        elif self.direction == "down":
            pass
        elif self.direction == "left":
            pass
        elif self.direction == "right":
            pass

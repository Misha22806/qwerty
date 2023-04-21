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
        if (event.name == "w" or event.name == "up") and self.direction != "down":
            self.direction = "up"
        elif (event.name == "s" or event.name == "down") and self.direction != "up":
            self.direction = "down"
        elif (event.name == "a" or event.name == "left") and self.direction != "right":
            self.direction = "left"
        elif (event.name == "d" or event.name == "right") and self.direction != "left":
            self.direction = "right"

    def move(self):
        if self.direction == "up":
            self.y -= 1
            if self.y < 0:
                self.y = self.fieldSize - 1
        elif self.direction == "down":
            self.y += 1
            if self.y > self.fieldSize - 1:
                self.y = 0
        elif self.direction == "left":
            self.x -= 1
            if self.x < 0:
                self.x = self.fieldSize - 1
        elif self.direction == "right":
            self.x += 1
            if self.x > self.fieldSize - 1:
                self.x = 0

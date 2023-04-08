import random
 
 
class Fruit:
    def __init__(self, fieldSize, head, body, symbol: str = "●"):
        self.fieldSize = fieldSize
        self.head = head
        self.body = body
 
        self.symbol = symbol
 
        self.generate()
 
    def generate(self):
        # Рандомные координаты в пределах поля
        self.x = random.randint(0, self.fieldSize - 1)
        self.y = random.randint(0, self.fieldSize - 1)
        # 0 - fieldSize
        # self.x
        # self.y
        if self.x == self.head.x and self.y == self.head.y:
            self.generate()
            return
        # body.elements
        # Если координаты совпадают с координатами головы, то тогда генерируем опять
        # Тоже самое с телом
        for element in self.body.elements:
            if self.x == element.x and self.y == element.y:
                self.generate()
                return
    
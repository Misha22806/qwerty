import os
import time
from modules.field import Field
from modules.head import Head
from modules.tail import Tail
from modules.fruit import Fruit

# Голова
# Тело(Хвост)
# Яблочки
# Поле

# Задания
# 1. Создание поля размера 2х2 - infinity x infinity +
# 2. Создать голову змейки в рандомных координатах +
# 3. Создать фрукт +
# 4. Сделать передвижение змейки
# 5. Кушаем фрукт и растем
# 6. Создаем новый фрукт
# 7. Поражение или победа

size = int(input("Field size: "))
field = Field(size)
head = Head(size)
tail = Tail(head)
fruit = Fruit(size, head, tail)

speed = 0.3

while True:
    os.system("cls")

    tail.move()
    head.move()

    for element in tail.elements:
        if head.y == element.y and head.x == element.x:
            os.system("cls")
            print("Game over")
            exit()

    if head.y == fruit.y and head.x == fruit.x:
        speed -= 0.25 / (size * size)
        tail.add()
        fruit.generate()

    # Делаете проверку на победу
    # Если длина(len) tail.elements будет равна size * size - 1
    # Пишем победа и exit()
    if len(tail.elements) == size * size - 1:
        print("Победа!")
        exit()

    renderedField = field.render(head, tail, fruit)

    for y in range(size):
        for x in range(size):
            print(renderedField[y][x], end=" ")
        print("")

    time.sleep(speed)

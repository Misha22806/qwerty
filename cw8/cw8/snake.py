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
tail = Tail()
fruit = Fruit(size, head, tail)

while True:
    os.system("cls")

    renderedField = field.render(head, tail, fruit)

    for y in range(size):
        for x in range(size):
            print(renderedField[y][x], end=" ")
        print("")

    time.sleep(1)

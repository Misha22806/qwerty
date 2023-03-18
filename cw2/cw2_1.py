import time
import random
 
 
class Student:
    def __init__(self, name: str):
        self.name = name
        self.progress = 0
        self.stress = 0
 
    def study(self):
        # random values
        # progress +
        self.progress += random.randint(3, 7)
        self.stress += random.randint(3, 7)
        # stress +
        if self.progress >= 100:
            self.progress = 100
        if self.stress >= 100:
            self.stress = 100
 
    def rest(self):
        # random values
        self.progress -= 2
        self.stress -= 2
        # progress -
        # stress -
        # < 0
        if self.progress <= 0:
            self.progress = 0
        if self.stress <= 0:
            self.stress = 0
        pass
 
    def info(self):
        # Имя | текущий прогресс по учебе n | текущий стресс n
        print(f"{self.name} | Прогресс: {self.progress} | Стресс: {self.stress}")
 
 
students = [
    Student("Fedor"),
    Student("Anton"),
    Student("Anna"),
    Student("Bob"),
    Student("Misha"),
    # 5 студентов
]
 
progress_winner = None
stress_winner = None
 
day = 1
winner = None
 
while True:
     print(f"Day: {day}")
     for student in students:
        action = random.choice([student.rest, student.study])
        action()
        student.info()
        if student.progress == 100 and student.stress == 100:
            winner = student
     if winner:
         break
     day += 1
     time.sleep(0.2)
import random


class Unit:
    def __init__(self, name: str, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def attack(self, target):
        target.hp -= random.randint(self.strength - 2, self.strength + 2)

import random
from .unit import Unit
from .player import Player


class Enemy(Unit):
    def __init__(self, name: str, hp, strength):
        super().__init__(name, hp, strength)

    def attack(self, target: Player):
        damage = target.defense() - random.randint(self.strength - 2, self.strength + 2)
        if damage < 0:
            damage = 0
        print(f"Enemy damage {damage}")
        target.hp -= damage

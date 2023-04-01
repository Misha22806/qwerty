import random
from .unit import Unit


class Player(Unit):
    def __init__(self, name: str):
        super().__init__(name, 100, 10)
        self.level = 1

        self.defense = 10

        self.weapon = None
        self.armor = None

    def attack(self, target: Unit):
        damage = self.strength
        if self.weapon:
            damage += self.weapon.strength
        target.hp -= random.randint(damage - 2, damage + 2)

    def heal(self):
        pass

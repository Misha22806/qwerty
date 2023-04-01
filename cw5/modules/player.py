import random
from .unit import Unit
from .item import Item


class Player(Unit):
    def __init__(self, name: str):
        super().__init__(name, 100, 10)
        self.level = 1

        self.__defense = 10

        self.__weapon: Item | None = None
        self.__armor: Item | None = None

    def attack(self, target: Unit):
        damage = self.strength
        if self.__weapon:
            damage += self.__weapon.value
        target.hp -= random.randint(damage - 2, damage + 2)

    def heal(self):
        self.hp += random.randint(self.level + 10, self.level + 15)

    def change_armor(self, armor: Item):
        if isinstance(armor, Item):
            self.__armor = armor

    def change_weapon(self, weapon: Item):
        if isinstance(weapon, Item):
            self.__weapon = weapon

    def defense(self):
        if isinstance(self.__armor, Item):
            return self.__defense + self.__armor.value
        else:
            return self.__defense

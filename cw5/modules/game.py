from .player import Player
from .enemy import Enemy
from .item import Item
 
import time
import random
 
enemy_names = [
    "Дикобраз",
    "Скелет",
    "Паук",
    "Богдан",
    "Иван",
    "Дмитрий",
    "Евкакий",
    "Котопес",
    "Киндигишнян",
    "Володя",
    "Олег",
    "Парикмахер",
]
 
# Имена оружия и брони
weapon_names = []
 
armor_names = []
 
 
class Game:
    def __init__(self, name: str):
        self.player = Player(name)
        self.enemy_hp = 10
        self.enemy_atk = 3
 
        self.enemy = Enemy(random.choice(enemy_names), self.enemy_hp, self.enemy_atk)
 
    def show_actions(self):
        print("Actions: ")
        # Написать действия
        print("1. ")
        print("2. ")
 
    def equip_actions(self):
        print("Equip: ")
        print("1. Yes")
        print("2. No")
 
    def start(self):
        while True:
            print(f"Player lvl: {self.player.level}")
            print(f"Player HP: {self.player.hp}")
            print(f"Enemy {self.enemy.name} HP: {self.enemy.hp}")
 
            self.show_actions()
            choice = input("-> ")
            if choice == "1":
                self.player.attack(self.enemy)
            if choice == "2":
                # player исцеляется
                pass
 
            self.enemy.attack(self.player)
 
            if self.enemy.hp <= 0:
                self.enemy_hp += 10
                self.enemy_atk += 2
                self.enemy = Enemy(
                    random.choice(enemy_names), self.enemy_hp + 10, self.enemy_atk + 2
                )
                # С шансом 25% с enemy падает 2 итема: оружия и броня
                chance = random.randint(1, 100)
                if chance <= 25:
                    # Персонаж может их одеть или выбросить
                    value = self.player.level * 3 + 5
                    weapon = Item(
                        random.choice(weapon_names),
                        random.randint(value - 3, value + 3),
                    )
                    print(f"Weapon Name: {weapon.name}")
                    print(f"Weapon Strength: {weapon.value}")
                    self.equip_actions()
                    choice = input("-> ")
                    if choice == "1":
                        self.player.change_weapon(weapon)
                    # Делаем все тоже самое для брони
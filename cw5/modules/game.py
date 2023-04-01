from .player import Player
from .enemy import Enemy
 
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
 
    def start(self):
        while True:
            print(f"Player lvl: {self.player.level}")
            print(f"Player HP: {self.player.hp}")
            print(f"Enemy {self.enemy.name} HP: {self.enemy.hp}")
 
            self.show_actions()
            choice = input("-> ")
            if choice == 1:
                self.player.attack(self.enemy)
            if choice == 2:
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
                # Персонаж может их одеть или выбросить              
from .player import Player
from .enemy import Enemy

import time

hp = 20
atk = 11


class Game:
    def __init__(self, name: str):
        self.player = Player(name)
        self.enemy = Enemy("Дикобраз", hp, atk)

    def start(self):
        while True:
            self.player.attack(self.enemy)
            self.enemy.attack(self.player)
            print(f"Player {self.player.hp}")
            print(f"Enemy {self.enemy.hp}")
            if self.enemy.hp <= 0:
                self.enemy = Enemy("Дикобраз", hp + 10, atk + 2)
            print(f"Enemy {self.enemy.hp}")
            time.sleep(1)

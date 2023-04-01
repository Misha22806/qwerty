from .colors import *
from .game import Game


class Menu:
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        print(f"{BOLD}{PINK}Welcome to the {YELLOW}Burger-punk Adventure{RESET}")
        self.game.start()

    def exit(self):
        exit(0)

from .game import Game


class Menu:
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        print("Welcome to the Burger-punk Adventure")
        self.game.start()

    def exit(self):
        exit(0)

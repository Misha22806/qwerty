from modules.menu import Menu
from modules.game import Game

name = input("Input your game name: ")
game = Game(name)
menu = Menu(game)
menu.start()

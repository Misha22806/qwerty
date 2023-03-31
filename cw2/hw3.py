class Menu:
    def start(self):
        print("Игра началась!")
        
    def exit(self):
        print("Игра закончилась!")
        import sys
        sys.exit()
menu = Menu()
menu.start() # Игра началась!
menu.exit() # приложение закрывается
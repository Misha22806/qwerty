import colorama


from .head import Head
from .tail import Tail
from .fruit import Fruit

colorama.init()


class Field:
    def __init__(self, size: int = 5, symbol: str = "□"):
        self.size = size
        self.symbol = symbol

    def render(self, head: Head, tail: Tail, fruit: Fruit):
        field = []
        for y in range(self.size):
            field.append([])
            for x in range(self.size):
                field[y].append(self.symbol)

        field[fruit.y][
            fruit.x
        ] = f"{colorama.Fore.RED}{fruit.symbol}{colorama.Fore.RESET}"

        for element in tail.elements:
            field[element.y][
                element.x
            ] = f"{colorama.Fore.GREEN}{head.symbol}{colorama.Fore.RESET}"

        field[head.y][
            head.x
        ] = f"{colorama.Fore.CYAN}{head.symbol}{colorama.Fore.RESET}"

        return field

class Cat:
    def __init__(self, name: str):
        self.name = name
    def meow(self):
        print(f"{self.name} : МяУ!")
    def walk(self):
        print(f"{self.name} : Идет")
    def jump(self):
        print(f"{self.name} : Прыгает")
    def sleep(self):
        print(f"{self.name} : Спит")
    def sit(self):
        print(f"{self.name} : Сидит")

cat_name = input("\nВведите имя кота\n")
Name = Cat(cat_name)

Name.meow()
Name.walk()
Name.jump()
Name.sleep()
Name.sit()

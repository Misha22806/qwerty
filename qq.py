class Phone:
    def __init__(self, brand, model, storage): # конструктор класса Phone с названием бренда, модели и хранилища
        self.brand = brand
        self.model = model
        self.storage = storage
        self.flashlight = Flashlight()
    

    def phone_info(self): # метод вывода информации о телефоне
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage, "GB")
        
    def clear_storage(self): # метод очистки хранилища телефона
        self.storage = 0
        print("Storage cleared.")
        
    def upgrade_storage(self, upgrade): # метод апгрейда хранилища телефона
        self.storage += upgrade
        print("Storage upgraded to", self.storage, "GB.")

    def turn_on_flashlight(self): # метод включения фонарика
        self.flashlight.turn_on()
    
    def turn_off_flashlight(self): # метод выключения фонарика
        self.flashlight.turn_off()

class Flashlight:
    def init(self):
        self.on = False

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

flashlight = Flashlight()
flashlight.turn_on()
print(flashlight.on) # Output: True
flashlight.turn_off()
print(flashlight.on) # Output: False

my_phone = Phone("Apple", "iPhone 12", 128) # создание экземпляра класса Phone с параметрами бренда, модели и размера хранилища
my_phone.phone_info() # вызов phone_info для вывода информации о созданном телефоне
my_phone.clear_storage() # вызов clear_storage для очистки хранилища
my_phone.upgrade_storage(256) # вызов метода upgrade_storage для увеличения хранилища на 64 GB
my_phone.phone_info() # вызов phone_info для вывода новой информации о телефоне
my_phone.turn_on_flashlight() # включение фонарика
print("Включение фонарика") # Output: True
my_phone.turn_off_flashlight() # выключение фонарика
print("Выключение фонарика") # Output: False




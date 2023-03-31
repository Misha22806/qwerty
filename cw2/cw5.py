class Base:
    name = "Base"
    point = 10
 
    def teleport(self):
        print(f"{self.name} casting teleport")
 
 
class Mage(Base):
    name = "Mage"
 
    def fireball(self):
        print(f"{self.name} casting fireball")
 
 
class Warrior(Base):
    name = "Warrior"
 
    def splash(self):
        print(f"{self.name} casting splash")
 
 
class Archer(Base):
    name = "Archer"
 
    def invisibility(self):
        print(f"{self.name} casting invisibility")
 
 
class BattleMage(Mage, Warrior):
    name = "Battle Mage"
 
    def enchantWeapon(self):
        print(f"{self.name} casting enchant weapon")
 
class Pathfinder(Archer, Warrior):
    name = "Pathfinder"
 
    def psi_blades(self):
        print(f"{self.name} casting psi blades")
 
class Vampire_hunter(Mage, Archer):
    name = "Vampire hunter"
 
    def multishot(self):
        print(f"{self.name} casting multishot")

class Hero(BattleMage, Vampire_hunter, Pathfinder):
    name = "Hero"
 
    def invoke(self):
        print(f"{self.name} casting invoke")


 
base = Base()
mage = Mage()
warrior = Warrior()
archer = Archer()
battleMage = BattleMage()
pathfinder = Pathfinder()
vampire_hunter = Vampire_hunter()
hero = Hero()
 
mage.fireball()
warrior.splash()
archer.invisibility()
base.teleport()
mage.teleport()
archer.teleport()
warrior.teleport()
 
battleMage.fireball()
battleMage.splash()
battleMage.teleport()
battleMage.enchantWeapon()

pathfinder.psi_blades()
pathfinder.splash()
pathfinder.teleport()
pathfinder.invisibility()

vampire_hunter.multishot()
vampire_hunter.teleport()
vampire_hunter.fireball()
vampire_hunter.invisibility()

hero.teleport()
hero.fireball()
hero.invisibility()
hero.splash()
hero.enchantWeapon()
hero.psi_blades()
hero.multishot()

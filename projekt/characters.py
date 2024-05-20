import random
from music import ultimate_sombra


# Główny class postaci używany potem do tworzenia postaci
class Character:
    def __init__(self, name, max_health, max_mana):
        self.name = name
        self.max_health = max_health
        self.max_mana = max_mana
        self.current_health = max_health
        self.current_mana = max_mana

    def attack(self):
        raise NotImplementedError("Subclasses must implement the attack method.")

    def use_special_ability(self, enemy):
        raise NotImplementedError("Subclasses must implement the use_special_ability method.")

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0

    def is_defeated(self):
        return self.current_health == 0

    def gain_mana(self, mana):
        self.current_mana += mana
        if self.current_mana > self.max_mana:
            self.current_mana = self.max_mana

class Sombra(Character):
    def __init__(self):
        self.name = "Sombra"
        self.max_health = 200
        self.max_mana = 500
        self.current_health = self.max_health
        self.current_mana = 500
        self.inventory = []

    def attack(self):
        return 35

    def use_special_ability(self, enemy):
        if self.current_mana >= 25:
            damage = 50
            self.current_mana -= 25
            enemy.take_damage(damage)
            ultimate_sombra()
            print(f"{self.name} używa umiejętności specjalnej i zadaje {damage} obrażeń {enemy.name}!")

    def display_inventory(self):
        print("Twoje aktualne przedmioty w inwentarzu:")
        for index, item in enumerate(self.inventory):
            print(f"{index + 1}. {item.name}: {item.description}")




class Reinhardt(Character):
    def __init__(self):
        self.name = "Reinhardt"
        self.max_health = 500
        self.max_mana = 500
        self.current_health = self.max_health
        self.current_mana = 500
        self.shield_health = 100
        self.inventory = []

    def attack(self):
        return 40

    def use_special_ability(self, enemy):
        if self.current_mana >= 40:
            damage = 60
            self.current_mana -= 40
            enemy.take_damage(damage)
            print(f"{self.name} używa umiejętności specjalnej i zadaje {damage} obrażeń {enemy.name}!")
    
    def activate_shield(self):
        if self.shield_health > 0:
            self.shield_active = True
            print(f"{self.name} aktywuje tarczę o zdrowiu {self.shield_health} HP.")
        else:
            print(f"{self.name} nie ma już zdrowia w tarczy.")

    def display_inventory(self):
        print("Twoje aktualne przedmioty w inwentarzu:")
        for index, item in enumerate(self.inventory):
            print(f"{index + 1}. {item.name}: {item.description}")

class Widowmaker(Character):
    def __init__(self):
        self.name = "Widowmaker"
        self.max_health = 175
        self.max_mana = 500
        self.current_health = self.max_health
        self.current_mana = 300
        self.critical_chance = 1  # Szansa na cios krytyczny na początku gry
        self.enemies_defeated = 0  # Licznik pokonanych przeciwników
        self.inventory = []

    def attack(self):
        damage = random.randint(10, 60)
        if self.enemies_defeated % 3 == 0 and self.enemies_defeated > 0:
            if random.random() < 1 / self.critical_chance:
                print(f"{self.name} wykonuje cios krytyczny i zabija przeciwnika!")
                damage = 999  # Zabija przeciwnika
            else:
                print(f"{self.name} wykonuje strzał z snajperki i zadaje {damage} obrażeń.")
        else:
            print(f"{self.name} wykonuje strzał z snajperki i zadaje {damage} obrażeń.")
        return damage
    
    def use_special_ability(self, enemy):
        if self.current_mana >= 40:
            damage = 100
            self.current_mana -= 40
            enemy.take_damage(damage)
            print(f"{self.name} używa umiejętności specjalnej i zadaje {damage} obrażeń {enemy.name}!")
    
    def display_inventory(self):
        print("Twoje aktualne przedmioty w inwentarzu:")
        for index, item in enumerate(self.inventory):
            print(f"{index + 1}. {item.name}: {item.description}")

class Ana(Character):
    def __init__(self):
        self.name = "Ana"
        self.max_health = 200
        self.max_mana = 500
        self.current_health = self.max_health
        self.current_mana = 500
        self.enemies_defeated = 0
        self.inventory = []
    
    def attack(self):
        damage = random.randint(10,30)
        return damage
    
    def use_special_ability(self, enemy):
        if self.current_mana >= 40 and self.current_health <= 50:
            damage = 110
            leczenie = 50
            self.current_mana -= 40
            self.current_health += 50
            enemy.take_damage(damage)
            print(f"{self.name} używa umiejętności specjalnej i zadaje {damage} obrażeń {enemy.name}! Dodatkowo {self.name} leczy {leczenie}hp")
    
    def display_inventory(self):
        print("Twoje aktualne przedmioty w inwentarzu:")
        for index, item in enumerate(self.inventory):
            print(f"{index + 1}. {item.name}: {item.description}")

class Zarya(Character):
    def __init__(self):
        self.name = "Zarya"
        self.max_health = 475
        self.max_mana = 500
        self.current_health = self.max_health
        self.current_mana = 500
        self.enemies_defeated = 0
        self.inventory = []

    def attack(self):
        return 45
    
    def use_special_ability(self, enemy):
        if self.current_mana >= 35:
            damage = 130
            self.current_mana -= 40
            enemy.take_damage(damage)
            print(f"{self.name} używa umiejętności specjalnej i zadaje {damage} obrażeń {enemy.name}")






#   ██████ ▓█████  ██ ▄█▀ ██▀███  ▓█████  ▄████▄   ██▓ ██ ▄█▀ ██▓
# ▒██    ▒ ▓█   ▀  ██▄█▒ ▓██ ▒ ██▒▓█   ▀ ▒██▀ ▀█  ▓██▒ ██▄█▒ ▓██▒
# ░ ▓██▄   ▒███   ▓███▄░ ▓██ ░▄█ ▒▒███   ▒▓█    ▄ ▒██▒▓███▄░ ▒██▒
#   ▒   ██▒▒▓█  ▄ ▓██ █▄ ▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██▒░██░▓██ █▄ ░██░
# ▒██████▒▒░▒████▒▒██▒ █▄░██▓ ▒██▒░▒████▒▒ ▓███▀ ░░██░▒██▒ █▄░██░
# ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒ ▒▒ ▓▒░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░░▓  ▒ ▒▒ ▓▒░▓  
# ░ ░▒  ░ ░ ░ ░  ░░ ░▒ ▒░  ░▒ ░ ▒░ ░ ░  ░  ░  ▒    ▒ ░░ ░▒ ▒░ ▒ ░
# ░  ░  ░     ░   ░ ░░ ░   ░░   ░    ░   ░         ▒ ░░ ░░ ░  ▒ ░
#       ░     ░  ░░  ░      ░        ░  ░░ ░       ░  ░  ░    ░  
#                                        ░                      


class Freddy(Character):
    def __init__(self):
        self.name = "Freddy"
        self.max_health = 450
        self.max_mana = 500
        self.current_health = self.max_health
        self.current_mana = 387
        self.inventory = []
    
    def attack(self):
        damage = random.randint(10,99)
        return damage
    
    def use_special_ability(self, enemy):
        if self.current_mana >= 300:
            damage = 999
            self.current_mana -= 300
            enemy.take_damage(damage)
            print(f"{self.name} odgryza przeciwnikowi glowe...")

class test(Character):
        def __init__(self):
            self.name = "test"
            self.max_health = 99999999999
            self.max_mana = 999999999
            self.current_health = self.max_health
            self.current_mana = 999999999
            self.inventory = []
        def attack(self):
            return 1000000
        def use_special_ability(self, enemy):
            if self.current_mana >= 1:
                damage = 99999999
                self.current_mana -= 1
                enemy.take_damage(damage)
                print(f"._.")

class dodatkowefunkcjepostaci(Character):
    def __init__(self, name, max_health, max_mana):
        super().__init__("olus", max_health = 100, max_mana = 100)

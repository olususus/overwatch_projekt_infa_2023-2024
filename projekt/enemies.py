import random


# Główny class przeciwników
class Enemy:
    def __init__(self, name, max_health):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health

    def attack(self):
        raise NotImplementedError("Subclasses must implement the attack method.")

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0

    def is_defeated(self):
        return self.current_health == 0

class Bastion(Enemy):
    def __init__(self):
        super().__init__("Bastion", max_health=200)

    def attack(self):
        return random.randint(10,40)

class Kiriko(Enemy):
    def __init__(self):
        super().__init__("Kiriko", max_health=100)

    def attack(self):
        return random.randint(1,30)

class Roadhog(Enemy):
    def __init__(self):
        super().__init__("Roadhog", max_health=250)

    def attack(self):
        return random.randint(10,50)

class Echo(Enemy):
    def __init__(self):
        super().__init__("Echo", max_health=180)

    def attack(self):
        return random.randint(5,29)

class Cassidy(Enemy):
    def __init__(self):
        super().__init__("Cassidy", max_health=170)

    def attack(self):
        return random.randint(10,30)

class Lucio(Enemy):
    def __init__(self):
        super().__init__("Lucio", max_health=200)

    def attack(self):
        return random.randint(15, 25)

class Ashe(Enemy):
    def __init__(self):
        super().__init__("Ashe", max_health=150)
        self.turns_until_grenade = 5  # Licznik tur do rzucenia granatem

    def attack(self):
        # Jeśli przyszedł czas na rzucenie granatem
        if self.turns_until_grenade == 0:
            damage = random.randint(10, 50)
            self.turns_until_grenade = 5  # Zresetuj licznik tur do granatu
            return damage
        else:
            self.turns_until_grenade -= 1
            return random.randint(1, 20)  # Zwykły atak z losowym obrażeniem

    def take_damage(self, damage):
        super().take_damage(damage)
        if random.random() < 0.2:  # 20% szansy na dodatkowe obrażenia od ognistego granatu
            fire_damage = random.randint(5, 15)
            print(f"{self.name} otrzymuje dodatkowe obrażenia od ognistego granatu: {fire_damage}")
            super().take_damage(fire_damage)

class Springtrap(Enemy):
    def __init__(self):
        super().__init__("Springtrap", max_health=200)
        self.turns_until_knife = 2
    def attack(self):
        if self.turns_until_knife == 0:
            damage = random.randint(10,60)
            self.turns_until_knife = 2
            print("-" * 50)
            print(f"Springtrap używa swojego noża do zadania {damage} {self.name}")
            return damage
        else:
            self.turns_until_knife -= 1
            return random.randint(1,30)

class Hanzo(Enemy):
    def __init__(self):
        super().__init__("Hanzo", max_health=110)
        self.turns_until_arrow = 3
    def attack(self):
        if self.turns_until_arrow == 0:
            damage = random.randint(5,55)
            self.turns_until_arrow = 3
            print("-" * 50)
            print(f"Hanzo używa swojej superstrzały do zadania {damage} {self.name}")
            return damage
        else:
            self.turns_until_arrow -= 1
            return random.randint(10,30)

class Junkrat(Enemy):
    def __init__(self, name, max_health):
        super().__init__(name, max_health)

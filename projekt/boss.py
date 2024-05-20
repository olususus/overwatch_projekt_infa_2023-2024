import random


# Główny class bosa używany do tworzenia bosów później
class Boss:
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

class Orisa(Boss):
    def __init__(self):
        super().__init__("Orisa", max_health=700)

    def attack(self):
        return random.randint(1,100)

class Mauga(Boss):
    def __init__(self):
        super().__init__("Mauga", max_health=800)
    
    def attack(self):
        return random.randint(40,150)
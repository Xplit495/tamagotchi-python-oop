from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self, name, max_health, base_hunger, base_energy, base_happiness):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.hunger = base_hunger
        self.energy = base_energy
        self.happiness = base_happiness
        self.age = 0
        self.is_sick = False
        self.stage = "bébé"

    def feed(self,):
        pass

    def play(self):
        pass

    def sleep(self):
        pass

    def heal(self):
        pass

    @abstractmethod
    def make_sound(self):
        ...

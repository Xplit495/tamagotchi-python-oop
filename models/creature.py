import random
from abc import ABC, abstractmethod
from models.food import Food

class Creature(ABC):
    def __init__(self, name, max_health, max_hunger, max_energy, max_happiness):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.hunger = max_hunger
        self.max_hunger = max_hunger
        self.max_energy = max_energy
        self.energy = max_energy
        self.max_happiness = max_happiness
        self.happiness = max_happiness
        self.is_sick = False
        self.is_alive = True
        self.alive_days = 1
        self.stage = "bébé"

    def heal(self, heal_gain):
        self.health += heal_gain
        if self.health > self.max_health:
            self.health = self.max_health

    def damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False

    def feed(self, food: Food):
        self.hunger += food.satiety
        if self.hunger > self.max_hunger:
            self.hunger = self.max_hunger
        if food.is_good_quality:
            self.heal(food.health_effect)
        else:
            self.damage(food.health_effect)

    def starve(self, hunger):
        self.hunger -= hunger
        if self.hunger < 0:
            self.hunger = 0
            self.health = 0
            self.is_alive = False

    def sleep(self, energy, lose_hunger):
        self.energy += energy
        self.hunger -= lose_hunger
        if self.energy > self.max_energy:
            self.energy = self.max_energy
        self.starve(lose_hunger)

    def play(self, happiness, lose_energy):
        self.happiness += happiness
        self.energy -= lose_energy
        if self.happiness > self.max_happiness:
            self.happiness = self.max_happiness
        if self.energy < 0:
            self.energy = 0

    def get_sick(self):
        self.is_sick = True

    def cure(self):
        self.is_sick = False

    def grow(self):
        if self.alive_days == 10:
            self.stage = "enfant"
        elif self.alive_days == 30:
            self.stage = "adulte"
        elif self.alive_days == 60:
            self.stage = "mort"
            self.is_alive = False

    def time_pass(self):
        self.starve(1)
        self.alive_days += 1
        self.grow()
        sick_probability = random.randint(1, 100)
        if 1 <= sick_probability <= 5 and not self.is_sick:
            self.get_sick()
        if self.is_sick:
            self.damage(1)

    @abstractmethod
    def make_sound(self):
        pass

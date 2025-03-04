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
        if self.alive_days == 20:
            self.stage = "enfant"
        elif self.alive_days == 50:
            self.stage = "adulte"
        elif self.alive_days == 100:
            self.stage = "mort"
            self.is_alive = False

    def time_pass(self):
        hunger_loss = random.randint(1, 3)
        self.starve(hunger_loss)

        energy_loss = random.randint(1, 2)
        self.energy = max(0, self.energy - energy_loss)

        happiness_loss = random.randint(1, 2)
        self.happiness = max(0, self.happiness - happiness_loss)

        self.alive_days += 1
        self.grow()

        sick_probability = random.randint(1, 100)
        base_chance = 5

        if self.hunger < self.max_hunger * 0.3:
            base_chance += 3

        if self.happiness < self.max_happiness * 0.3:
            base_chance += 2

        if 1 <= sick_probability <= base_chance and not self.is_sick:
            self.get_sick()

        if self.is_sick:
            self.damage(1)
            self.energy = max(0, self.energy - 1)
            self.happiness = max(0, self.happiness - 1)

    @abstractmethod
    def make_sound(self):
        pass

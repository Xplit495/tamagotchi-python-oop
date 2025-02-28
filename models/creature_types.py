from models.creature import Creature


class Puppy(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=100, max_hunger=70, max_energy=100, max_happiness=90)

    def make_sound(self):
        return "Wouf!"


class Kitten(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=80, max_hunger=60, max_energy=90, max_happiness=60)

    def make_sound(self):
        return "Miaou!"


class Dragon(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=200, max_hunger=80, max_energy=70, max_happiness=60)

    def make_sound(self):
        return "Groar!"


class Bunny(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=70, max_hunger=50, max_energy=110, max_happiness=85)

    def make_sound(self):
        return "Sniff sniff!"


class Hamster(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=60, max_hunger=55, max_energy=120, max_happiness=80)

    def make_sound(self):
        return "Squeak!"


class FoxCub(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=85, max_hunger=65, max_energy=95, max_happiness=75)

    def make_sound(self):
        return "Yip yip!"


class Penguin(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=90, max_hunger=75, max_energy=70, max_happiness=85)

    def make_sound(self):
        return "Wenk wenk!"


class Panda(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=110, max_hunger=80, max_energy=60, max_happiness=90)

    def make_sound(self):
        return "Squee!"


class BabyTurtle(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=120, max_hunger=40, max_energy=40, max_happiness=75)

    def make_sound(self):
        return "Chirp!"
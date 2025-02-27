from models.creature import Creature


class Kitten(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=80, base_hunger=60, base_energy=90, base_happiness=80)

    def make_sound(self):
        return "Miaou!"


class Puppy(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=100, base_hunger=70, base_energy=100, base_happiness=90)

    def make_sound(self):
        return "Wouf!"


class Dragon(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=150, base_hunger=80, base_energy=70, base_happiness=60)

    def make_sound(self):
        return "Groar!"


class Bunny(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=70, base_hunger=50, base_energy=110, base_happiness=85)

    def make_sound(self):
        return "Sniff sniff!"


class Hamster(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=60, base_hunger=55, base_energy=120, base_happiness=80)

    def make_sound(self):
        return "Squeak!"


class FoxCub(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=85, base_hunger=65, base_energy=95, base_happiness=75)

    def make_sound(self):
        return "Yip yip!"


class Penguin(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=90, base_hunger=75, base_energy=70, base_happiness=85)

    def make_sound(self):
        return "Wenk wenk!"


class Panda(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=110, base_hunger=80, base_energy=60, base_happiness=90)

    def make_sound(self):
        return "Squee!"


class BabyTurtle(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=120, base_hunger=40, base_energy=50, base_happiness=75)

    def make_sound(self):
        return "Chirp!"
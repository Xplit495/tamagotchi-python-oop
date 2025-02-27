from models.creature import Creature


class Puppy(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=100, hunger=70, energy=100, happiness=90)

    def make_sound(self):
        return "Wouf!"


class Kitten(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=80, hunger=60, energy=90, happiness=60)

    def make_sound(self):
        return "Miaou!"


class Dragon(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=200, hunger=80, energy=70, happiness=60)

    def make_sound(self):
        return "Groar!"


class Bunny(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=70, hunger=50, energy=110, happiness=85)

    def make_sound(self):
        return "Sniff sniff!"


class Hamster(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=60, hunger=55, energy=120, happiness=80)

    def make_sound(self):
        return "Squeak!"


class FoxCub(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=85, hunger=65, energy=95, happiness=75)

    def make_sound(self):
        return "Yip yip!"


class Penguin(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=90, hunger=75, energy=70, happiness=85)

    def make_sound(self):
        return "Wenk wenk!"


class Panda(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=110, hunger=80, energy=60, happiness=90)

    def make_sound(self):
        return "Squee!"


class BabyTurtle(Creature):
    def __init__(self, name):
        super().__init__(name, max_health=120, hunger=40, energy=40, happiness=75)

    def make_sound(self):
        return "Chirp!"
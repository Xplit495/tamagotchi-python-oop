from models.creature import Creature


class Puppy(Creature):
    """
    Classe représentant un chiot.

    Caractéristiques:
        - Santé élevée
        - Énergie élevée
        - Bonheur élevé
    """

    def __init__(self, name):
        super().__init__(name, max_health=100, max_hunger=70, max_energy=100, max_happiness=90)

    def make_sound(self):
        """Retourne le son caractéristique du chiot."""
        return "Wouf!"


class Kitten(Creature):
    """
    Classe représentant un chaton.

    Caractéristiques:
        - Santé moyenne
        - Énergie élevée
        - Bonheur moyen
    """

    def __init__(self, name):
        super().__init__(name, max_health=80, max_hunger=60, max_energy=90, max_happiness=60)

    def make_sound(self):
        """Retourne le son caractéristique du chaton."""
        return "Miaou!"


class Dragon(Creature):
    """
    Classe représentant un dragon.

    Caractéristiques:
        - Santé très élevée
        - Faim élevée
        - Énergie moyenne
        - Bonheur moyen
    """

    def __init__(self, name):
        super().__init__(name, max_health=200, max_hunger=80, max_energy=70, max_happiness=60)

    def make_sound(self):
        """Retourne le son caractéristique du dragon."""
        return "Groar!"


class Bunny(Creature):
    """
    Classe représentant un lapin.

    Caractéristiques:
        - Santé faible
        - Faim faible
        - Énergie très élevée
        - Bonheur élevé
    """

    def __init__(self, name):
        super().__init__(name, max_health=70, max_hunger=50, max_energy=110, max_happiness=85)

    def make_sound(self):
        """Retourne le son caractéristique du lapin."""
        return "Sniff sniff!"


class Hamster(Creature):
    """
    Classe représentant un hamster.

    Caractéristiques:
        - Santé très faible
        - Faim moyenne
        - Énergie extrêmement élevée
        - Bonheur élevé
    """

    def __init__(self, name):
        super().__init__(name, max_health=60, max_hunger=55, max_energy=120, max_happiness=80)

    def make_sound(self):
        """Retourne le son caractéristique du hamster."""
        return "Squeak!"


class FoxCub(Creature):
    """
    Classe représentant un renardeau.

    Caractéristiques:
        - Santé moyenne-élevée
        - Faim moyenne
        - Énergie élevée
        - Bonheur moyen-élevé
    """

    def __init__(self, name):
        super().__init__(name, max_health=85, max_hunger=65, max_energy=95, max_happiness=75)

    def make_sound(self):
        """Retourne le son caractéristique du renardeau."""
        return "Yip yip!"


class Penguin(Creature):
    """
    Classe représentant un pingouin.

    Caractéristiques:
        - Santé moyenne-élevée
        - Faim élevée
        - Énergie moyenne
        - Bonheur élevé
    """

    def __init__(self, name):
        super().__init__(name, max_health=90, max_hunger=75, max_energy=70, max_happiness=85)

    def make_sound(self):
        """Retourne le son caractéristique du pingouin."""
        return "Wenk wenk!"


class Panda(Creature):
    """
    Classe représentant un panda.

    Caractéristiques:
        - Santé très élevée
        - Faim très élevée
        - Énergie faible
        - Bonheur très élevé
    """

    def __init__(self, name):
        super().__init__(name, max_health=110, max_hunger=80, max_energy=60, max_happiness=90)

    def make_sound(self):
        """Retourne le son caractéristique du panda."""
        return "Squee!"


class BabyTurtle(Creature):
    """
    Classe représentant un bébé tortue.

    Caractéristiques:
        - Santé extrêmement élevée
        - Faim très faible
        - Énergie très faible
        - Bonheur moyen-élevé
    """

    def __init__(self, name):
        super().__init__(name, max_health=120, max_hunger=40, max_energy=40, max_happiness=75)

    def make_sound(self):
        """Retourne le son caractéristique de la bébé tortue."""
        return "Chirp!"
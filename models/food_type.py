from models.food import Food

class Apple(Food):
    name = "Pomme"
    satiety = 3
    is_good_quality = True
    health_effect = 3

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class Chicken(Food):
    name = "Poulet"
    satiety = 8
    is_good_quality = True
    health_effect = 4

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class Fish(Food):
    name = "Poisson"
    satiety = 7
    is_good_quality = True
    health_effect = 5

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class Rice(Food):
    name = "Riz"
    satiety = 6
    is_good_quality = True
    health_effect = 2

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class Egg(Food):
    name = "Œuf"
    satiety = 4
    is_good_quality = True
    health_effect = 3

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class Broccoli(Food):
    name = "Brocoli"
    satiety = 2
    is_good_quality = True
    health_effect = 5

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class Banana(Food):
    name = "Banane"
    satiety = 4
    is_good_quality = True
    health_effect = 2

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class Cake(Food):
    name = "Gâteau"
    satiety = 7
    is_good_quality = False
    health_effect = 3

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class Chocolate(Food):
    name = "Chocolat"
    satiety = 5
    is_good_quality = False
    health_effect = 2

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class Pizza(Food):
    name = "Pizza"
    satiety = 10
    is_good_quality = False
    health_effect = 4

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class FrenchFries(Food):
    name = "Frites"
    satiety = 6
    is_good_quality = False
    health_effect = 5

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class IceCream(Food):
    name = "Glace"
    satiety = 4
    is_good_quality = False
    health_effect = 3

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class Hamburger(Food):
    name = "Hamburger"
    satiety = 9
    is_good_quality = False
    health_effect = 5

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)


class ChipsSnack(Food):
    name = "Chips"
    satiety = 4
    is_good_quality = False
    health_effect = 4

    def __init__(self):
        super().__init__(self.name, self.satiety, self.is_good_quality, self.health_effect)
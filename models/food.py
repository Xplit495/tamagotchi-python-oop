from abc import ABC

class Food(ABC):
    def __init__(self, name, satiety, is_good_quality, health_effect):
        self.name = name
        self.satiety = satiety
        self.is_good_quality = is_good_quality
        self.health_effect = health_effect

    def __str__(self):
        return self.name

# Aliments de bonne qualité (healthy)
class Apple(Food):
    def __init__(self):
        super().__init__("Pomme", 3, True, 3)

class Carrot(Food):
    def __init__(self):
        super().__init__("Carotte", 2, True, 2)

class Chicken(Food):
    def __init__(self):
        super().__init__("Poulet", 8, True, 4)

class Fish(Food):
    def __init__(self):
        super().__init__("Poisson", 7, True, 5)

class Rice(Food):
    def __init__(self):
        super().__init__("Riz", 6, True, 2)

class Egg(Food):
    def __init__(self):
        super().__init__("Œuf", 4, True, 3)

class Yogurt(Food):
    def __init__(self):
        super().__init__("Yaourt", 3, True, 4)

class Broccoli(Food):
    def __init__(self):
        super().__init__("Brocoli", 2, True, 5)

class Oatmeal(Food):
    def __init__(self):
        super().__init__("Flocons d'avoine", 5, True, 3)

class Banana(Food):
    def __init__(self):
        super().__init__("Banane", 4, True, 2)


# Aliments de mauvaise qualité (unhealthy)
class Cake(Food):
    def __init__(self):
        super().__init__("Gâteau", 7, False, -3)

class Chocolate(Food):
    def __init__(self):
        super().__init__("Chocolat", 5, False, -2)

class Pizza(Food):
    def __init__(self):
        super().__init__("Pizza", 10, False, -4)

class FrenchFries(Food):
    def __init__(self):
        super().__init__("Frites", 6, False, -5)

class IceCream(Food):
    def __init__(self):
        super().__init__("Glace", 4, False, -3)

class Soda(Food):
    def __init__(self):
        super().__init__("Soda", 2, False, -4)

class Candy(Food):
    def __init__(self):
        super().__init__("Bonbons", 3, False, -5)

class Hamburger(Food):
    def __init__(self):
        super().__init__("Hamburger", 9, False, -5)

class Donut(Food):
    def __init__(self):
        super().__init__("Beignet", 5, False, -3)

class ChipsSnack(Food):
    def __init__(self):
        super().__init__("Chips", 4, False, -4)
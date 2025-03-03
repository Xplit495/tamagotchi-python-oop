from abc import ABC

class Food(ABC):
    def __init__(self, name, satiety, is_good_quality, health_effect):
        self.name = name
        self.satiety = satiety
        self.is_good_quality = is_good_quality
        self.health_effect = health_effect

    @staticmethod
    def get_info(food):
        sign = "+" if food.is_good_quality else "-"
        return f"{food.name} - Satiété: {food.satiety}, Effet sur la santé: {sign}{food.health_effect}"

from abc import ABC

class Food(ABC):
    def __init__(self, name, satiety, is_good_quality, health_effect):
        self.name = name
        self.satiety = satiety
        self.is_good_quality = is_good_quality
        self.health_effect = health_effect

    @staticmethod
    def informations(aliment):
        if aliment.is_good_quality:
            return f"{aliment.name} - Satiété: {aliment.satiety}, Effet sur la santé: +{aliment.health_effect}"

        return f"{aliment.name} - Satiété: {aliment.satiety}, Effet sur la santé: -{aliment.health_effect}"
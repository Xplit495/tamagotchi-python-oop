from abc import ABC


class Food(ABC):
    """
    Classe abstraite qui définit une nourriture que les créatures peuvent consommer.

    Cette classe sert de base pour tous les types d'aliments dans le jeu et
    définit leurs propriétés communes: nom, effet sur la satiété, qualité et
    effet sur la santé.

    Attributes:
        name (str): Nom de l'aliment
        satiety (int): Points de satiété que l'aliment apporte
        is_good_quality (bool): Indique si l'aliment est sain (True) ou malsain (False)
        health_effect (int): Points de santé affectés (positif ou négatif selon la qualité)
    """

    def __init__(self, name, satiety, is_good_quality, health_effect):
        """
        Initialise un nouvel aliment avec ses propriétés.

        Args:
            name (str): Nom de l'aliment
            satiety (int): Points de satiété apportés
            is_good_quality (bool): True si l'aliment est sain, False sinon
            health_effect (int): Points de santé affectés par la consommation
        """
        self.name = name
        self.satiety = satiety
        self.is_good_quality = is_good_quality
        self.health_effect = health_effect

    @staticmethod
    def get_info(food):
        """
        Retourne une description textuelle de l'aliment.

        Args:
            food: L'instance de Food dont on veut obtenir l'information

        Returns:
            str: Description de l'aliment incluant son nom, l'effet sur la satiété et l'effet sur la santé
        """
        sign = "+" if food.is_good_quality else "-"
        return f"{food.name} - Satiété: {food.satiety}, Effet sur la santé: {sign}{food.health_effect}"
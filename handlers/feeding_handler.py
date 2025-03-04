import time

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from models.food_type import (
    Apple, Chicken, Fish, Rice, Egg, Broccoli, Banana,
    Cake, Chocolate, Pizza, FrenchFries, IceCream, Hamburger, ChipsSnack
)
from utils.clear_terminal import clear_terminal


def handle_feeding(creature):
    """
    Gère le processus d'alimentation de la créature.

    Cette fonction affiche un menu de nourriture, permet au joueur de choisir
    un aliment, et applique les effets de cet aliment à la créature.

    Args:
        creature: L'objet créature à nourrir
    """
    clear_terminal()

    # Liste de tous les aliments disponibles classés par catégorie
    food_classes = [
        {"class": Apple, "category": "sain"},
        {"class": Chicken, "category": "sain"},
        {"class": Fish, "category": "sain"},
        {"class": Rice, "category": "sain"},
        {"class": Egg, "category": "sain"},
        {"class": Broccoli, "category": "sain"},
        {"class": Banana, "category": "sain"},
        {"class": Cake, "category": "malsain"},
        {"class": Chocolate, "category": "malsain"},
        {"class": Pizza, "category": "malsain"},
        {"class": FrenchFries, "category": "malsain"},
        {"class": IceCream, "category": "malsain"},
        {"class": Hamburger, "category": "malsain"},
        {"class": ChipsSnack, "category": "malsain"}
    ]

    # Construction du menu de sélection des aliments, commençant par les aliments sains
    food_choices = [Separator("=== Aliments sains ===")]

    for food_item in food_classes:
        food_class = food_item["class"]
        if food_item["category"] == "sain":
            food_choices.append(Choice(value=food_class, name=food_class.get_info(food_class)))

    # Ajout des aliments malsains après un séparateur
    food_choices.append(Separator(""))
    food_choices.append(Separator("=== Aliments malsains ==="))

    for food_item in food_classes:
        food_class = food_item["class"]
        if food_item["category"] == "malsain":
            food_choices.append(Choice(value=food_class, name=food_class.get_info(food_class)))

    # Demander au joueur de choisir un aliment
    selected_food_class = inquirer.select(
        message=f"Que voulez-vous donner à manger à {creature.name} ?",
        choices=food_choices
    ).execute()

    # Instancier l'aliment choisi
    food = selected_food_class()

    # Animation de l'alimentation
    clear_terminal()
    print(f"{creature.name} mange un(e) {food.name}...")

    for _ in range(3):
        print("miam", end="", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        print(" ", end="", flush=True)
    print()

    # Appliquer les effets de l'aliment à la créature
    creature.feed(food)

    # Afficher un message différent selon la qualité de l'aliment
    if food.is_good_quality:
        print(
            f"C'était délicieux et nutritif ! {creature.name} a gagné {food.satiety} points de satiété et {food.health_effect} points de santé.")
    else:
        print(
            f"Ce n'était pas très bon pour sa santé... {creature.name} a gagné {food.satiety} points de satiété mais a perdu {food.health_effect} points de santé.")

    # La créature fait un son pour exprimer sa satisfaction
    creature.make_sound()
    input("\nAppuyez sur Entrée pour continuer...")
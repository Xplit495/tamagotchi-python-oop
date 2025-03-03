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
    clear_terminal()

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

    food_choices = [Separator("=== Aliments sains ===")]

    for food_item in food_classes:
        food_class = food_item["class"]
        if food_item["category"] == "sain":
            food_choices.append(Choice(value=food_class, name=food_class.get_info(food_class)))

    food_choices.append(Separator(""))
    food_choices.append(Separator("=== Aliments malsains ==="))

    for food_item in food_classes:
        food_class = food_item["class"]
        if food_item["category"] == "malsain":
            food_choices.append(Choice(value=food_class, name=food_class.get_info(food_class)))

    selected_food_class = inquirer.select(
        message=f"Que voulez-vous donner à manger à {creature.name} ?",
        choices=food_choices
    ).execute()

    food = selected_food_class()

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

    creature.feed(food)

    if food.is_good_quality:
        print(
            f"C'était délicieux et nutritif ! {creature.name} a gagné {food.satiety} points de satiété et {food.health_effect} points de santé.")
    else:
        print(
            f"Ce n'était pas très bon pour sa santé... {creature.name} a gagné {food.satiety} points de satiété mais a perdu {food.health_effect} points de santé.")

    creature.make_sound()
    input("\nAppuyez sur Entrée pour continuer...")
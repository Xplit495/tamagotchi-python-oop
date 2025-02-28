import time

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from models.food import Food

from models.food_type import (
    Apple, Chicken, Fish, Rice, Egg, Broccoli, Banana,
    Cake, Chocolate, Pizza, FrenchFries, IceCream, Hamburger, ChipsSnack
)
from utils.clear_terminal import clear_terminal


def handle_feeding(creature):
    clear_terminal()

    food_choices = [
        Separator("=== Aliments sains ==="),
        Choice(value=Apple(), name=Food.informations(Apple())),
        Choice(value=Chicken(), name=Food.informations(Chicken())),
        Choice(value=Fish(), name=Food.informations(Fish())),
        Choice(value=Rice(), name=Food.informations(Rice())),
        Choice(value=Egg(), name=Food.informations(Egg())),
        Choice(value=Broccoli(), name=Food.informations(Broccoli())),
        Choice(value=Banana(), name=Food.informations(Banana())),

        Separator(""),
        Separator("=== Aliments malsains ==="),
        Choice(value=Cake(), name=Food.informations(Cake())),
        Choice(value=Chocolate(), name=Food.informations(Chocolate())),
        Choice(value=Pizza(), name=Food.informations(Pizza())),
        Choice(value=FrenchFries(), name=Food.informations(FrenchFries())),
        Choice(value=IceCream(), name=Food.informations(IceCream())),
        Choice(value=Hamburger(), name=Food.informations(Hamburger())),
        Choice(value=ChipsSnack(), name=Food.informations(ChipsSnack()))
    ]

    food = inquirer.select(
        message=f"Que voulez-vous donner à manger à {creature.name} ?",
        choices=food_choices
    ).execute()

    clear_terminal()
    print(f"{creature.name} mange {food.name}...")

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

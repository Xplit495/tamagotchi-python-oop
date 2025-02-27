from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from utils.clear_terminal import clear_terminal

from models.creature_types import Kitten, Puppy, Bunny, Hamster, FoxCub, Panda, Dragon, Penguin, BabyTurtle


def init_creature():
    print("Bienvenue dans le menu de création de votre petit monstre !\n")

    creature_mapping = {
        "Chaton": Kitten,
        "Chiot": Puppy,
        "Lapin": Bunny,
        "Hamster": Hamster,
        "Renardeau": FoxCub,
        "Panda": Panda,
        "Dragon": Dragon,
        "Pingouin": Penguin,
        "Bébé tortue": BabyTurtle
    }

    creature_choices = [
        Choice(value="Chaton", name="Chaton - Petit chat joueur et câlin"),
        Choice(value="Chiot", name="Chiot - Petit chien énergique et loyal"),
        Choice(value="Lapin", name="Lapin - Lapin aux longues oreilles qui adore sauter"),
        Choice(value="Hamster", name="Hamster - Petit rongeur aux joues pleines de nourriture"),
        Choice(value="Renardeau", name="Renardeau - Bébé renard curieux et espiègle"),
        Choice(value="Panda", name="Panda - Bébé panda gourmand et câlin"),
        Choice(value="Dragon", name="Dragon - Bébé dragon adorable malgré ses petites flammes"),
        Choice(value="Pingouin", name="Pingouin - Petit pingouin maladroit sur terre mais agile dans l'eau"),
        Choice(value="Bébé tortue", name="Bébé tortue - Tortue lente mais résistante"),
    ]

    while True:
        creature_type = inquirer.select(
            message="Commencez par sélectionner le type de votre créature :",
            choices=creature_choices
        ).execute()

        print(f"Vous avez choisi un(e) {creature_type} !")

        if inquirer.confirm(message="Confirmer votre choix ?").execute():
            clear_terminal()
            break
        clear_terminal()

    while True:
        name = inquirer.text(
            message=f"Quel nom souhaitez-vous donner à votre {creature_type} :",
            validate=lambda text: 0 < len(text) <= 20 and text.isalpha(),
            invalid_message="Le nom doit contenir entre 1 et 20 lettres (pas de chiffres ou caractères spéciaux)"
        ).execute()

        print(f"Votre {creature_type} s'appellera donc {name} !")

        if inquirer.confirm(message="Confirmer votre choix ?").execute():
            clear_terminal()
            break
        clear_terminal()

    creature_class = creature_mapping[creature_type]
    creature = creature_class(name)

    print("Créature créée avec succès!")
    input("\nAppuyez sur Entrée pour continuer...")
    clear_terminal()

    return creature
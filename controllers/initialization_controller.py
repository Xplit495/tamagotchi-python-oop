from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from utils.clear_terminal import clear_terminal

from models.creature_types import Kitten, Puppy, Bunny, Hamster, FoxCub, Panda, Dragon, Penguin, BabyTurtle


def init_creature():
    """
    Gère le processus de création d'une nouvelle créature.

    Cette fonction guide l'utilisateur à travers le processus de sélection
    du type de créature et de choix d'un nom, puis instancie et retourne
    la créature créée.

    Returns:
        Creature: Une instance de la créature nouvellement créée
    """
    print("Bienvenue dans le menu de création de votre petit monstre !\n")

    # Dictionnaire associant les noms des créatures à leurs classes correspondantes
    creature_mapping = {
        "Chiot": Puppy,
        "Chaton": Kitten,
        "Dragon": Dragon,
        "Lapin": Bunny,
        "Hamster": Hamster,
        "Renardeau": FoxCub,
        "Pingouin": Penguin,
        "Panda": Panda,
        "Bébé tortue": BabyTurtle
    }

    # Liste des choix de créatures avec leurs descriptions pour le menu de sélection
    creature_choices = [
        Choice(value="Chiot", name="Chiot - Petit chien énergique et loyal"),
        Choice(value="Chaton", name="Chaton - Petit chat joueur et câlin"),
        Choice(value="Dragon", name="Dragon - Bébé dragon adorable malgré ses petites flammes"),
        Choice(value="Lapin", name="Lapin - Lapin aux longues oreilles qui adore sauter"),
        Choice(value="Hamster", name="Hamster - Petit rongeur aux joues pleines de nourriture"),
        Choice(value="Renardeau", name="Renardeau - Bébé renard curieux et espiègle"),
        Choice(value="Pingouin", name="Pingouin - Petit pingouin maladroit sur terre mais agile dans l'eau"),
        Choice(value="Panda", name="Panda - Bébé panda gourmand et câlin"),
        Choice(value="Bébé tortue", name="Bébé tortue - Tortue lente mais résistante"),
    ]

    # Boucle pour la sélection du type de créature
    while True:
        creature_type = inquirer.select(
            message="Commencez par sélectionner le type de votre créature :",
            choices=creature_choices
        ).execute()

        print(f"Vous avez choisi un(e) {creature_type} !")

        # Demande de confirmation du choix
        if inquirer.confirm(message="Confirmer votre choix ?").execute():
            clear_terminal()
            break
        clear_terminal()

    # Boucle pour le choix du nom de la créature
    while True:
        name = inquirer.text(
            message=f"Quel nom souhaitez-vous donner à votre {creature_type} :",
            validate=lambda text: 0 < len(text) <= 20 and text.isalpha(),
            invalid_message="Le nom doit contenir entre 1 et 20 lettres (pas de chiffres ou caractères spéciaux)"
        ).execute()

        print(f"Votre {creature_type} s'appellera donc {name} !")

        # Demande de confirmation du nom
        if inquirer.confirm(message="Confirmer votre choix ?").execute():
            clear_terminal()
            break
        clear_terminal()

    # Création de l'instance de la créature avec le type et le nom choisis
    creature_class = creature_mapping[creature_type]
    creature = creature_class(name)

    print(f"{creature.name} à été créé avec succès!")
    input("\nAppuyez sur Entrée pour continuer...")
    clear_terminal()

    return creature
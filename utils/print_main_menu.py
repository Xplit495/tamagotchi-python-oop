from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator


def display_menu(creature):
    choices = [
        Choice(value="feed", name="Nourrir"),
        Choice(value="play", name="Jouer"),
        Choice(value="sleep", name="Dormir"),
    ]

    if creature.health < creature.max_health:
        choices.append(Choice(value="heal", name="Soigner"))

    if creature.is_sick:
        choices.append(Choice(value="cure", name="Guérir"))

    choices.extend([Separator(),
                   Choice(value="save", name="Sauvegarder la partie"),
                   Choice(value="quit", name="Quitter le jeu")
    ])

    return inquirer.select(
        message=f"Que voulez-vous faire avec {creature.name} ?",
        choices=choices
    ).execute()

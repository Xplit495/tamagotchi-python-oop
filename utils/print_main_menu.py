from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator


def display_menu(creature):
    """
    Génère un menu interactif dynamique pour les actions avec la créature.

    Cette fonction crée un menu contextuel qui s'adapte à l'état actuel de la créature,
    en proposant des options d'interaction appropriées.

    Args:
        creature (Creature): L'objet créature pour lequel générer le menu.

    Returns:
        str: La valeur de l'action choisie par l'utilisateur.

    Fonctionnalités principales :
    - Options de base : nourrir, jouer, dormir
    - Options conditionnelles basées sur l'état de la créature :
      * Option de soins si la santé est basse
      * Option de guérison si la créature est malade
    - Séparateur visuel
    - Options de sauvegarde et de quitte
    """
    # Création de la liste des choix principaux
    choices = [
        # Actions de base
        Choice(value="feed", name="Nourrir"),
        Choice(value="play", name="Jouer"),
        Choice(value="sleep", name="Dormir"),
    ]

    # Ajout conditionnel de l'option de soins
    if creature.health < creature.max_health:
        choices.append(Choice(value="heal", name="Soigner"))

    # Ajout conditionnel de l'option de guérison
    if creature.is_sick:
        choices.append(Choice(value="cure", name="Guérir"))

    # Ajout des options supplémentaires avec un séparateur
    choices.extend([Separator(),
                   Choice(value="save", name="Sauvegarder la partie"),
                   Choice(value="quit", name="Quitter le jeu")
    ])

    # Affichage et sélection du menu interactif
    return inquirer.select(
        message=f"Que voulez-vous faire avec {creature.name} ?",
        choices=choices
    ).execute()
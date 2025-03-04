import time
from utils.clear_terminal import clear_terminal
import random
import keyboard


def handle_playing(creature):
    """
    Gère l'activité de jeu de la créature.

    Vérifie si la créature a suffisamment d'énergie pour jouer,
    puis lance un mini-jeu de cache-cache pour augmenter son bonheur.

    Args:
        creature: L'objet créature qui va jouer
    """
    clear_terminal()

    # Vérifier si la créature a assez d'énergie pour jouer
    if creature.energy < 10:
        print(f"{creature.name} est trop fatigué pour jouer maintenant.")
        input("Appuyez sur Entrée pour continuer...")
        return

    # Lancer le mini-jeu
    mini_game(creature)


def mini_game(creature):
    """
    Mini-jeu de cache-cache où le joueur doit retrouver sa position aléatoire sur une grille.

    Le joueur se déplace sur une grille 9x9 à l'aide des flèches directionnelles.
    Le nombre de mouvements nécessaires influence le gain de bonheur de la créature.

    Args:
        creature: L'objet créature qui va gagner du bonheur en jouant
    """
    print(f"Vous allez jouer à un mini-jeu pour augmenter le bonheur de {creature.name} !\n")
    print(f"Vous allez incarner {creature.name} et vous allez devoir vous retrouver dans la carte.")
    print("Bien sur votre position est aléatoire (ce serait trop facile sinon).\n")

    # Initialisation de la grille 9x9 (0: espace vide, 1: position actuelle, 2: positions visitées)
    hide_and_seek_map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],  # Position de départ (centre)
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # Générer une position aléatoire à atteindre
    random_position = get_random_position()
    user_position = (4, 4)  # Position initiale au centre

    counter = 0  # Compteur de mouvements

    # Boucle principale du jeu
    while True:
        print_map(hide_and_seek_map)

        print(
            '\n\nVotre position actuelle est représenté par 📍, vous pouvez maintenant utiliser les flèches directionnelles pour vous déplacer.\n')
        time.sleep(0.5)

        # Obtenir la direction choisie par le joueur
        direction = get_user_input()

        # Sauvegarder la position actuelle avant déplacement
        user_position_saved = user_position

        # Traiter le déplacement selon la direction
        match direction:
            case 'up':
                if user_position[0] > 0:  # Vérifier si le déplacement est dans les limites
                    user_position = (user_position[0] - 1, user_position[1])
                else:
                    print("Vous ne pouvez pas aller plus haut.")
                    time.sleep(1)
            case 'down':
                if user_position[0] < 8:
                    user_position = (user_position[0] + 1, user_position[1])
                else:
                    print("Vous ne pouvez pas aller plus bas.")
                    time.sleep(1)
            case 'left':
                if user_position[1] > 0:
                    user_position = (user_position[0], user_position[1] - 1)
                else:
                    print("Vous ne pouvez pas aller plus à gauche.")
                    time.sleep(1)
            case 'right':
                if user_position[1] < 8:
                    user_position = (user_position[0], user_position[1] + 1)
                else:
                    print("Vous ne pouvez pas aller plus à droite.")
                    time.sleep(1)

        # Vérifier si le joueur a atteint la position cible
        if user_position == random_position:
            print("Bravo, vous vous êtes retrouvé !")
            creature.play(counter, counter / 2)  # Le bonheur gagné dépend du nombre de mouvements
            time.sleep(5)
            break

        counter += 1  # Incrémenter le compteur de mouvements

        # Mettre à jour la grille: marquer l'ancienne position comme visitée et la nouvelle comme position actuelle
        hide_and_seek_map[user_position_saved[0]][user_position_saved[1]] = 2
        hide_and_seek_map[user_position[0]][user_position[1]] = 1
        clear_terminal()


def get_user_input():
    """
    Capture l'entrée du joueur via les touches fléchées.

    Returns:
        str: Direction choisie ('up', 'down', 'left', 'right')
    """
    while True:
        if keyboard.is_pressed('up'):
            return 'up'
        elif keyboard.is_pressed('down'):
            return 'down'
        elif keyboard.is_pressed('left'):
            return 'left'
        elif keyboard.is_pressed('right'):
            return 'right'


def get_random_position():
    """
    Génère une position aléatoire différente de la position de départ.

    Returns:
        tuple: Coordonnées (ligne, colonne) de la position aléatoire
    """
    while True:
        random_position = (random.randint(0, 8), random.randint(0, 8))
        # S'assurer que la position aléatoire n'est pas la position de départ (4,4)
        if random_position[0] != 4 or random_position[1] != 4:
            return random_position


def print_map(hide_and_seek_map):
    """
    Affiche la grille de jeu avec des emojis pour représenter les différents éléments.

    Args:
        hide_and_seek_map (list): Grille 2D représentant l'état du jeu
    """
    for line in range(len(hide_and_seek_map)):
        print('\n', end='')
        for column in range(len(hide_and_seek_map[line])):
            if hide_and_seek_map[line][column] == 0:
                print('🪨', end=' ')  # Espace vide
            elif hide_and_seek_map[line][column] == 1:
                print('📍', end=' ')  # Position actuelle
            elif hide_and_seek_map[line][column] == 2:
                print('❌ ', end=' ')  # Position visitée
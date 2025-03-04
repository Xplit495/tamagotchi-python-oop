from utils.argument_parser import argument_parser
from utils.load_save_file import load_save_file
from utils.print_ascii_art import print_ascii_art
from controllers.game_controller import *
from controllers.initialization_controller import *

if __name__ == '__main__':
    """
    Point d'entrée principal pour le jeu de créature virtuelle Tamagoshit.

    Flux de démarrage du jeu :
    1. Nettoie le terminal
    2. Affiche un message de bienvenue
    3. Gère le chargement de partie :
       - Via un fichier de sauvegarde spécifié en argument
       - Ou en créant une nouvelle créature
    4. Lance le contrôleur de jeu principal
    5. Affiche un message de fin

    Fonctionnalités principales :
    - Support du chargement de partie existante
    - Création de nouvelle créature si aucune sauvegarde n'est fournie
    - Utilisation de contrôleurs pour la logique de jeu
    """
    # Nettoie le terminal au démarrage
    clear_terminal()
    # Initialise la créature à None
    creature = None

    # Message de bienvenue humoristique
    print("Bienvenue dans le jeu Tamagoshit ! (Le jeu de Tamagotchi mais juste en moins bien)\n")

    # Analyse des arguments de ligne de commande
    save_file = argument_parser()

    # Tentative de chargement d'une partie existante
    if save_file:
        print("Chargement de la partie...")
        # Charge la créature à partir du fichier de sauvegarde
        creature = load_save_file(save_file)

        # Lance le jeu si le chargement est réussi
        if creature:
            # Affiche l'art ASCII de la créature
            print_ascii_art(creature)
            # Lance le contrôleur de jeu
            game_controller(creature)
    else:
        # Crée une nouvelle créature si aucune sauvegarde n'est fournie
        creature = init_creature()
        # Affiche l'art ASCII de la créature
        print_ascii_art(creature)
        # Lance le contrôleur de jeu
        game_controller(creature)

    # Message de fin
    print(f"Merci d'avoir joué !")
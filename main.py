from utils.argument_parser import argument_parser
from utils.load_save_file import load_save_file
from controllers.game_controller import *
from controllers.initialization_controller import *

if __name__ == '__main__':
    clear_terminal()
    print("Bienvenue dans le jeu Tamagoshit ! (Le jeu de Tamagotchi mais juste en moins bien)\n")
    save_file = argument_parser()
    if save_file:
        print("Chargement de la partie...")
        load_save_file(save_file)
    else:
        creature = init_creature()
        game_controller(creature)

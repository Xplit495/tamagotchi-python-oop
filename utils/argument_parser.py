import argparse

def argument_parser():
    parser = argparse.ArgumentParser(description='Ce programme est un petit jeu Tamagotchi.')

    parser.add_argument('-s', '--save', help='Permet de charger le fichier de sauvegarde. Exemple : python main.py -s save.json')

    return parser.parse_args().save

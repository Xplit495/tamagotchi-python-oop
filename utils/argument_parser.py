import argparse

def argument_parser():
    """
    Analyse les arguments de ligne de commande pour le jeu de créature virtuelle.

    Cette fonction utilise argparse pour gérer les options de ligne de commande,
    permettant principalement de charger un fichier de sauvegarde existant.

    Fonctionnalités :
    - Option -s ou --save : Permet de spécifier un fichier de sauvegarde à charger
    - Fournit une description du programme
    - Retourne le chemin du fichier de sauvegarde s'il est spécifié, sinon None

    Exemple d'utilisation :
    python main.py -s save.json  # Charge une sauvegarde existante
    python main.py               # Démarre un nouveau jeu sans sauvegarde

    Returns:
        str or None: Chemin du fichier de sauvegarde si spécifié, sinon None
    """
    # Création du parser avec une description du programme
    parser = argparse.ArgumentParser(description='Ce programme est un petit jeu Tamagotchi.')

    # Ajout de l'argument pour charger un fichier de sauvegarde
    parser.add_argument('-s', '--save',
                        help='Permet de charger le fichier de sauvegarde. Exemple : python main.py -s save.json')

    # Parse les arguments et retourne le chemin de sauvegarde
    return parser.parse_args().save
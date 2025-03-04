import os

def clear_terminal():
    """
    Efface le contenu du terminal de manière multiplateforme.

    Cette fonction détecte le système d'exploitation et utilise la commande
    appropriée pour effacer l'écran du terminal :
    - Sur Windows (systèmes avec 'nt'), utilise 'cls'
    - Sur Unix/Linux/macOS, utilise 'clear'

    Cette approche permet de nettoyer l'affichage du terminal de manière
    transparente, quelque soit le système d'exploitation utilisé.
    """
    # Vérifie le nom du système d'exploitation
    if os.name == 'nt':
        # Pour Windows (NT = New Technology)
        os.system('cls')
    else:
        # Pour Unix-like systems (Linux, macOS)
        os.system('clear')
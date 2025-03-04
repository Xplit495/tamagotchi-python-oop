import pickle
import os
import time
import datetime
from InquirerPy import inquirer
from utils.clear_terminal import clear_terminal


def save_game(creature):
    """
    Gère la sauvegarde de la partie de la créature virtuelle.

    Cette fonction offre plusieurs options de sauvegarde :
    - Créer une nouvelle sauvegarde
    - Écraser la dernière sauvegarde existante
    - Gestion du répertoire de sauvegarde
    - Génération de noms de fichiers uniques

    Args:
        creature (Creature): L'objet créature à sauvegarder.

    Fonctionnalités principales :
    - Création du répertoire de sauvegarde si inexistant
    - Menu interactif de choix de sauvegarde
    - Utilisation de pickle pour sérialiser l'objet
    - Gestion des erreurs de sauvegarde
    - Feedback visuel du processus de sauvegarde
    """
    # Nettoie le terminal avant l'affichage
    clear_terminal()
    print("=== SAUVEGARDE DE LA PARTIE ===\n")

    # Création du répertoire de sauvegarde si nécessaire
    save_dir = "saves"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Définition des choix de sauvegarde
    choices = [
        {"name": "Créer une nouvelle sauvegarde", "value": "new"},
        {"name": "Écraser la dernière sauvegarde", "value": "overwrite"}
    ]

    # Recherche des sauvegardes existantes
    existing_saves = []
    if os.path.exists(save_dir):
        # Récupère les fichiers de sauvegarde et les trie par date de modification
        save_files = [os.path.join(save_dir, f) for f in os.listdir(save_dir) if f.endswith('.save')]
        save_files.sort(key=lambda x: os.path.getmtime(x))
        existing_saves = save_files

    # Choix automatique si aucune sauvegarde n'existe
    if not existing_saves:
        choice = "new"
    else:
        # Menu de sélection du type de sauvegarde
        choice = inquirer.select(
            message="Comment voulez-vous sauvegarder votre partie ?",
            choices=choices
        ).execute()

    # Génération du nom de fichier
    if choice == "new":
        # Nouvelle sauvegarde avec horodatage
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{save_dir}/{creature.name}_{timestamp}.save"
    else:
        # Écrasement de la dernière sauvegarde
        filename = existing_saves[-1] if existing_saves else f"{save_dir}/{creature.name}_new.save"

    try:
        # Sauvegarde de la créature via pickle
        with open(filename, 'wb') as save_file:
            pickle.dump(creature, save_file)

        # Affichage des informations de sauvegarde
        print(f"Sauvegarde dans le fichier : {filename}")
        print("Sauvegarde en cours...")

        # Animation de chargement simple
        for _ in range(5):
            print(".", end="", flush=True)
            time.sleep(0.3)

        print("\nSauvegarde terminée avec succès !")

    except Exception as e:
        # Gestion des erreurs de sauvegarde
        print(f"Erreur lors de la sauvegarde : {str(e)}")

    # Pause avant de retourner au menu
    input("\nAppuyez sur Entrée pour continuer...")
import pickle
import os
import time
import datetime
from InquirerPy import inquirer
from utils.clear_terminal import clear_terminal


def save_game(creature):
    clear_terminal()
    print("=== SAUVEGARDE DE LA PARTIE ===\n")

    save_dir = "saves"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    choices = [
        {"name": "Créer une nouvelle sauvegarde", "value": "new"},
        {"name": "Écraser la dernière sauvegarde", "value": "overwrite"}
    ]

    existing_saves = []
    if os.path.exists(save_dir):
        save_files = [os.path.join(save_dir, f) for f in os.listdir(save_dir) if f.endswith('.save')]
        save_files.sort(key=lambda x: os.path.getmtime(x))
        existing_saves = save_files

    if not existing_saves:
        choice = "new"
    else:
        choice = inquirer.select(
            message="Comment voulez-vous sauvegarder votre partie ?",
            choices=choices
        ).execute()

    if choice == "new":
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{save_dir}/{creature.name}_{timestamp}.save"
    else:
        filename = existing_saves[-1] if existing_saves else f"{save_dir}/{creature.name}_new.save"

    try:
        with open(filename, 'wb') as save_file:
            pickle.dump(creature, save_file)

        print(f"Sauvegarde dans le fichier : {filename}")
        print("Sauvegarde en cours...")

        for _ in range(5):
            print(".", end="", flush=True)
            time.sleep(0.3)

        print("\nSauvegarde terminée avec succès !")

    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {str(e)}")

    input("\nAppuyez sur Entrée pour continuer...")
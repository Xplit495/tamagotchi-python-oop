import pickle
import os
import datetime
from InquirerPy import inquirer
from utils.clear_terminal import clear_terminal


def load_save_file(save_file):
    try:
        if save_file and os.path.exists(save_file):
            with open(save_file, 'rb') as file:
                creature = pickle.load(file)
                print(f"Partie chargée : {creature.name} (Jour {creature.alive_days})")
                input("\nAppuyez sur Entrée pour continuer...")
                return creature

        save_dir = "saves"
        if not os.path.exists(save_dir):
            print("Aucune sauvegarde trouvée.")
            input("\nAppuyez sur Entrée pour continuer...")
            return None

        save_files = [os.path.join(save_dir, f) for f in os.listdir(save_dir) if f.endswith('.save')]

        if not save_files:
            print("Aucune sauvegarde trouvée.")
            input("\nAppuyez sur Entrée pour continuer...")
            return None

        save_files.sort(key=lambda x: os.path.getmtime(x))

        choices = []
        for save_path in save_files:
            save_name = os.path.basename(save_path)
            mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(save_path))
            mod_time_str = mod_time.strftime("%Y-%m-%d %H:%M:%S")
            choices.append({
                "name": f"{save_name} (créé le {mod_time_str})",
                "value": save_path
            })

        choices.append({"name": "Créer une nouvelle partie", "value": "new"})

        clear_terminal()
        print("=== CHARGEMENT D'UNE PARTIE ===\n")
        selected_save = inquirer.select(
            message="Sélectionnez une sauvegarde à charger :",
            choices=choices
        ).execute()

        if selected_save == "new":
            from controllers.initialization_controller import init_creature
            return init_creature()

        with open(selected_save, 'rb') as file:
            creature = pickle.load(file)
            print(f"Partie chargée : {creature.name} (Jour {creature.alive_days})")
            input("\nAppuyez sur Entrée pour continuer...")
            return creature

    except Exception as e:
        print(f"Erreur lors du chargement de la sauvegarde : {str(e)}")
        input("\nAppuyez sur Entrée pour continuer...")
        return None
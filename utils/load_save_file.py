import pickle
import os
import datetime
from InquirerPy import inquirer
from utils.clear_terminal import clear_terminal


def load_save_file(save_file):
    """
    Charge un fichier de sauvegarde pour une créature virtuelle.

    Cette fonction gère plusieurs scénarios de chargement de sauvegarde :
    1. Chargement via un fichier spécifié en argument
    2. Sélection parmi les sauvegardes existantes
    3. Création d'une nouvelle partie si aucune sauvegarde n'existe

    Args:
        save_file (str, optional): Chemin du fichier de sauvegarde à charger directement.

    Returns:
        object or None: L'objet créature chargé ou None si aucune sauvegarde n'est chargée.

    Fonctionnalités principales :
    - Vérifie l'existence du fichier de sauvegarde spécifié
    - Liste et trie les sauvegardes existantes par date de modification
    - Permet de sélectionner une sauvegarde via un menu interactif
    - Offre l'option de créer une nouvelle partie
    - Gère les erreurs potentielles lors du chargement
    """
    try:
        # Tentative de chargement direct si un fichier de sauvegarde est spécifié
        if save_file and os.path.exists(save_file):
            with open(save_file, 'rb') as file:
                creature = pickle.load(file)
                print(f"Partie chargée : {creature.name} (Jour {creature.alive_days})")
                input("\nAppuyez sur Entrée pour continuer...")
                return creature

        # Définition du répertoire de sauvegarde
        save_dir = "saves"
        if not os.path.exists(save_dir):
            print("Aucune sauvegarde trouvée.")
            input("\nAppuyez sur Entrée pour continuer...")
            return None

        # Récupération de la liste des fichiers de sauvegarde
        save_files = [os.path.join(save_dir, f) for f in os.listdir(save_dir) if f.endswith('.save')]

        # Vérification de l'existence de sauvegardes
        if not save_files:
            print("Aucune sauvegarde trouvée.")
            input("\nAppuyez sur Entrée pour continuer...")
            return None

        # Tri des sauvegardes par date de modification
        save_files.sort(key=lambda x: os.path.getmtime(x))

        # Préparation des choix pour le menu de sélection
        choices = []
        for save_path in save_files:
            save_name = os.path.basename(save_path)
            # Conversion de la date de modification
            mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(save_path))
            mod_time_str = mod_time.strftime("%Y-%m-%d %H:%M:%S")
            choices.append({
                "name": f"{save_name} (créé le {mod_time_str})",
                "value": save_path
            })

        # Ajout de l'option pour créer une nouvelle partie
        choices.append({"name": "Créer une nouvelle partie", "value": "new"})

        # Nettoyage de l'écran et affichage du menu de sélection
        clear_terminal()
        print("=== CHARGEMENT D'UNE PARTIE ===\n")
        selected_save = inquirer.select(
            message="Sélectionnez une sauvegarde à charger :",
            choices=choices
        ).execute()

        # Gestion du choix de nouvelle partie
        if selected_save == "new":
            from controllers.initialization_controller import init_creature
            return init_creature()

        # Chargement de la sauvegarde sélectionnée
        with open(selected_save, 'rb') as file:
            creature = pickle.load(file)
            print(f"Partie chargée : {creature.name} (Jour {creature.alive_days})")
            input("\nAppuyez sur Entrée pour continuer...")
            return creature

    except Exception as e:
        # Gestion des erreurs lors du chargement
        print(f"Erreur lors du chargement de la sauvegarde : {str(e)}")
        input("\nAppuyez sur Entrée pour continuer...")
        return None
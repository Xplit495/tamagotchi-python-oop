import random
import time

from InquirerPy import inquirer

from handlers.curing_handler import handle_curing
from handlers.feeding_handler import handle_feeding
from handlers.healing_handler import handle_healing
from handlers.playing_handler import handle_playing
from handlers.sleeping_handler import handle_sleeping
from utils.clear_terminal import clear_terminal
from utils.print_creature_status import display_creature_status
from utils.print_main_menu import display_menu
from utils.random_events import display_random_event
from utils.saving_game import save_game


def game_controller(creature):
    """
    Contrôleur principal du jeu qui gère la boucle de jeu et les interactions de l'utilisateur.

    Cette fonction maintient la boucle de jeu principale, affiche l'état de la créature,
    traite les choix du joueur et gère le passage du temps et les événements aléatoires.

    Args:
        creature: L'objet créature contrôlé par le joueur

    Returns:
        bool: False si le jeu se termine, pour indiquer à l'appelant que le jeu est terminé
    """
    day_count = 0  # Compteur de jours passés depuis le début de la partie

    while True:  # Boucle principale du jeu
        for i in range(2):  # Deux actions par jour
            # Vérifier si la créature est encore en vie
            if not creature.is_alive:
                clear_terminal()
                print(f"Oh non! {creature.name} n'est plus de ce monde...")
                print(f"Il a vécu {creature.alive_days} jours.")
                input("Appuyez sur Entrée pour quitter...")
                return False

            # Afficher l'état actuel de la créature
            clear_terminal()
            display_creature_status(creature)

            # Obtenir le choix d'action du joueur
            choice = display_menu(creature)

            # Traiter le choix du joueur
            if choice == "feed":
                handle_feeding(creature)
            elif choice == "play":
                handle_playing(creature)
            elif choice == "sleep":
                handle_sleeping(creature)
            elif choice == "heal":
                handle_healing(creature)
            elif choice == "cure":
                handle_curing(creature)
            elif choice == "save":
                save_game(creature)
            elif choice == "quit":
                if inquirer.confirm(
                        message="Voulez-vous vraiment quitter ? Les progrès non sauvegardés seront perdus.").execute():
                    return False

        # Fin de la journée - passage du temps
        clear_terminal()
        print("Une journée passe...")
        time.sleep(1)

        # Incrémenter le compteur de jours
        day_count += 1

        # 50% de chance qu'un événement aléatoire se produise
        if random.random() < 0.5:
            display_random_event(creature)
            time.sleep(2)

        # Appliquer les effets du passage du temps sur la créature
        creature.time_pass()

        # Vérifier s'il y a des alertes critiques à afficher
        alerts = creature.check_critical_status()

        if alerts:
            clear_terminal()
            print("\n=== ALERTES DE FIN DE JOURNÉE ===")
            for alert in alerts:
                print(alert)
            time.sleep(3)  # Pause pour que le joueur puisse lire les alertes
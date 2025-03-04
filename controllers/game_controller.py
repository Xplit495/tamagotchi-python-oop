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
    day_count = 0

    while True:
        for i in range(2):

            if not creature.is_alive:
                clear_terminal()
                print(f"Oh non! {creature.name} n'est plus de ce monde...")
                print(f"Il a vécu {creature.alive_days} jours.")
                input("Appuyez sur Entrée pour quitter...")
                return False

            clear_terminal()
            display_creature_status(creature)

            choice = display_menu(creature)

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

        clear_terminal()
        print("Une journée passe...")
        time.sleep(1)

        day_count += 1
        if random.random() < 0.5:
            display_random_event(creature)
            time.sleep(2)

        creature.time_pass()

        alerts = creature.check_critical_status()

        if alerts:
            clear_terminal()
            print("\n=== ALERTES DE FIN DE JOURNÉE ===")
            for alert in alerts:
                print(alert)
            time.sleep(3)

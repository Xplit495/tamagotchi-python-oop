from InquirerPy import inquirer

from handlers.curing_handler import handle_curing
from handlers.feeding_handler import handle_feeding
from handlers.healing_handler import handle_healing
from handlers.playing_handler import handle_playing
from handlers.sleeping_handler import handle_sleeping
from utils.clear_terminal import clear_terminal
from utils.print_creature_status import display_creature_status
from utils.print_main_menu import display_menu
from utils.saving_game import save_game


def game_controller(creature):
    game_running = True

    while game_running:
        if not creature.is_alive:
            clear_terminal()
            print(f"Oh non! {creature.name} n'est plus de ce monde...")
            print(f"Il a vécu {creature.alive_days} jours.")
            input("Appuyez sur Entrée pour quitter...")
            return

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
                game_running = False

    return game_running

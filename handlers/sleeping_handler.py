import random
import time

from utils.clear_terminal import clear_terminal


def handle_sleeping(creature):
    clear_terminal()

    energy_gain = creature.max_energy
    hunger_loss = 5
    sleep_duration = 5

    print(f"{creature.name} s'endort...")
    time.sleep(1)

    progress_width = 40
    for i in range(progress_width + 1):
        percent = i / progress_width

        bar = "█" * i + "░" * (progress_width - i)

        dream = ""

        if i % 5 == 0:
            dream = random.choice([
                f"{creature.name} rêve de nourriture",
                f"{creature.name} rêve de jeux",
                "Zzz...",
                f"{creature.name} se retourne dans son sommeil",
                f"{creature.name} ronronne doucement"
            ])

        print(f"\r{dream} [{bar}] {int(percent * 100)}%", end="", flush=True)
        time.sleep(sleep_duration / progress_width)


    creature.sleep(energy_gain, hunger_loss)

    print(f"\n{creature.name} se réveille et se sent revigoré !")
    print(f"+{energy_gain} points d'énergie")
    print(f"-{hunger_loss} points de satiété")

    input("\nAppuyez sur Entrée pour continuer...")

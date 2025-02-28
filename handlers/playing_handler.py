from utils.clear_terminal import clear_terminal


def handle_playing(creature):
    clear_terminal()

    if creature.energy < 20:
        print(f"{creature.name} est trop fatigué pour jouer maintenant.")
        input("Appuyez sur Entrée pour continuer...")
        return

    creature.play(15, 10)

    print(f"Vous jouez avec {creature.name}.")
    print(f"{creature.name} dit: {creature.make_sound()}")
    print("Il a l'air plus heureux maintenant!")

    input("Appuyez sur Entrée pour continuer...")

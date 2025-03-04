import random
import time
import os

from utils.clear_terminal import clear_terminal


def handle_sleeping(creature):
    """
    Gère le processus de sommeil de la créature.

    Affiche une animation de progression pendant que la créature dort,
    puis lui applique les effets du sommeil (gain d'énergie, perte de faim).

    Args:
        creature: L'objet créature qui va dormir
    """
    clear_terminal()

    # Configurer les effets du sommeil
    energy_gain = 20  # Points d'énergie gagnés
    hunger_loss = 5  # Points de satiété perdus
    sleep_duration = 5  # Durée de l'animation en secondes

    print(f"{creature.name} s'endort...\n")
    time.sleep(1)

    # Choisir aléatoirement un message de rêve
    dream = random.choice([
        f"{creature.name} rêve de nourriture",
        f"{creature.name} rêve de jeux",
        "Zzz...",
        f"{creature.name} se retourne dans son sommeil",
        f"{creature.name} ronronne doucement"
    ])

    # Détecter la largeur du terminal pour un affichage propre
    terminal_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80

    # Animer une barre de progression pour représenter le sommeil
    progress_width = 40  # Largeur de la barre de progression
    for i in range(progress_width + 1):
        percent = i / progress_width
        bar = "█" * i + "░" * (progress_width - i)

        output = f"{dream} [{bar}] {int(percent * 100)}%"

        # Effacer la ligne avant d'afficher la nouvelle progression
        print(f"\r{' ' * terminal_width}", end="", flush=True)
        print(f"\r{output}", end="", flush=True)

        # Attendre un court instant pour l'animation
        time.sleep(sleep_duration / progress_width)

    # Appliquer les effets du sommeil à la créature
    creature.sleep(energy_gain, hunger_loss)

    # Afficher le résultat du sommeil
    print(f"\n{creature.name} se réveille et se sent revigoré !")
    print(f"+{energy_gain} points d'énergie")
    print(f"-{hunger_loss} points de satiété")

    input("\nAppuyez sur Entrée pour continuer...")
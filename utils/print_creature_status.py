import random

from utils.clear_terminal import clear_terminal
from utils.print_ascii_art import print_ascii_art


def display_creature_status(creature):
    clear_terminal()

    print_ascii_art(creature)

    print(f"========= {creature.name} =========")
    print(f"En vie depuis : {creature.alive_days} jours | Stade: {creature.stage}")
    print("-" * 40)

    stats = [
        {"name": "Santé", "value": creature.health, "max": creature.max_health},
        {"name": "Faim", "value": creature.hunger, "max": creature.max_hunger},
        {"name": "Énergie", "value": creature.energy, "max": creature.max_energy},
        {"name": "Bonheur", "value": creature.happiness, "max": creature.max_happiness}
    ]

    for stat in stats:
        percentage = int((stat["value"] / stat["max"]) * 10)
        bar = "█" * percentage + "░" * (10 - percentage)

        status_indicator = ""
        if percentage <= 2:
            status_indicator = "⚠️"
        elif percentage <= 3:
            status_indicator = "⚠"

        print(f"{stat['name']:8} [{bar}] {stat['value']}/{stat['max']} {status_indicator}")

    alerts = creature.check_critical_status()

    if alerts:
        print("\n=== ALERTES ===")
        for alert in alerts:
            print(alert)

    if creature.is_sick:
        print("\n⚠️  ATTENTION: Votre créature est malade et perd de la santé! ⚠️")

    avg_percentage = (creature.health / creature.max_health +
                      creature.hunger / creature.max_hunger +
                      creature.energy / creature.max_energy +
                      creature.happiness / creature.max_happiness) / 4

    print("\n" + "-" * 40)
    if avg_percentage > 0.8:
        messages = [
            f"{creature.name} est en pleine forme !",
            f"{creature.name} semble très heureux aujourd'hui !",
            f"{creature.name} déborde d'énergie et de vitalité !"
        ]
        print(random.choice(messages))
    elif avg_percentage > 0.5:
        messages = [
            f"{creature.name} se porte plutôt bien.",
            f"{creature.name} semble content.",
            f"{creature.name} est dans un état correct."
        ]
        print(random.choice(messages))
    elif avg_percentage > 0.3:
        messages = [
            f"{creature.name} ne se sent pas très bien...",
            f"{creature.name} a besoin de votre attention.",
            f"{creature.name} pourrait aller mieux."
        ]
        print(random.choice(messages))
    else:
        messages = [
            f"{creature.name} est dans un état inquiétant !",
            f"{creature.name} a besoin de soins urgents !",
            f"{creature.name} ne tiendra plus longtemps dans cet état !"
        ]
        print(random.choice(messages))

    print("\n")